"""
Base Agent - Foundation for all Entity agents

Provides common functionality:
- Task execution via Claude CLI
- Notifications
- GitHub integration
- Git operations
- Approval workflow
"""

import asyncio
import json
import subprocess
import uuid
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Optional, List, Dict, Any

# Marker that agents use to signal they're blocked and need input.
# Added to system prompts so Claude knows to use it.
BLOCKED_MARKER = "AGENT_BLOCKED:"

BLOCKED_INSTRUCTION = (
    "\n\nIMPORTANT: If you cannot complete this task because you need "
    "information, credentials, a decision, or clarification from the team, "
    "do NOT guess or fail silently. Instead, end your response with the "
    f"exact marker '{BLOCKED_MARKER}' followed by your specific question. "
    f"Example: '{BLOCKED_MARKER} Which database should I use — Qdrant on "
    "port 6333 or PostgreSQL on 5432?'"
)

from .config import BaseConfig
from .notifier import Notifier
from .github import GitHubClient
from .git import GitClient


@dataclass
class TaskResult:
    """Result from an agent task"""
    success: bool
    output: str
    files_changed: List[str] = None
    commit_hash: Optional[str] = None
    needs_approval: bool = False
    approval_prompt: str = ""
    session_id: Optional[str] = None
    blocked: bool = False
    blocker_question: str = ""

    def __post_init__(self):
        if self.files_changed is None:
            self.files_changed = []


@dataclass
class ApprovalRequest:
    """Request for human approval"""
    task_id: str
    description: str
    details: str
    options: List[str]
    created_at: datetime


class BaseAgent:
    """
    Base class for all Entity agents.

    Provides common functionality for:
    - Running tasks via Claude CLI
    - Sending notifications
    - GitHub integration
    - Git operations
    - Approval workflows
    """

    def __init__(self, config: BaseConfig):
        self.config = config
        self.notifier = Notifier(config.name, config.notifications)
        self.git = GitClient(config.project_root)

        if config.github_repo:
            self.github = GitHubClient(config.github_repo)
        else:
            self.github = None

        self.pending_approvals: List[ApprovalRequest] = []
        self.task_history: List[TaskResult] = []
        self._setup_directories()

    def _setup_directories(self):
        """Create necessary directories"""
        output_dir = self.config.get_output_dir()
        output_dir.mkdir(parents=True, exist_ok=True)

        logs_dir = output_dir / "logs"
        logs_dir.mkdir(parents=True, exist_ok=True)

    async def notify(self, message: str, level: str = "info"):
        """Send notification"""
        self.notifier.notify(message, level)

    async def request_approval(
        self,
        description: str,
        details: str,
        options: List[str] = None
    ) -> ApprovalRequest:
        """Request human approval for an action"""
        if options is None:
            options = ["Approve", "Reject", "Modify"]

        request = ApprovalRequest(
            task_id=f"approval_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
            description=description,
            details=details,
            options=options,
            created_at=datetime.now()
        )

        self.pending_approvals.append(request)

        # Save to file
        approvals_file = self.config.get_output_dir() / "pending_approvals.json"
        approvals_data = [
            {
                "task_id": a.task_id,
                "description": a.description,
                "details": a.details,
                "options": a.options,
                "created_at": a.created_at.isoformat()
            }
            for a in self.pending_approvals
        ]
        with open(approvals_file, "w") as f:
            json.dump(approvals_data, f, indent=2)

        await self.notify(f"Approval needed: {description}", level="approval")

        return request

    def _get_permission_flags(self) -> list[str]:
        """Get CLI permission flags based on agent role.

        Supervisor (Shelly) gets broad access + web research.
        Workers get project-scoped access only.
        Falls back to acceptEdits if permission module unavailable.
        """
        try:
            from mcp_entity_server.permissions import (
                get_supervisor_profile, get_worker_profile, build_cli_flags
            )
            is_supervisor = self.config.name.lower() == "shelly"
            project = str(self.config.get_project_root().name) if self.config.project_root != "." else None

            if is_supervisor:
                profile = get_supervisor_profile(project)
            else:
                profile = get_worker_profile(project)
            return build_cli_flags(profile)
        except ImportError:
            # Fallback: just use acceptEdits if the MCP server isn't installed
            return ["--permission-mode", "acceptEdits"]

    async def run_task(self, prompt: str, timeout: int = 600) -> TaskResult:
        """Execute a task using Claude CLI with session tracking.

        Generates a unique session ID so the task can be resumed later
        if the agent gets blocked and needs more input.
        """
        session_id = str(uuid.uuid4())
        await self.notify(f"Starting task (session {session_id[:8]}): {prompt[:50]}...")

        # Append the blocked-detection instruction to the system prompt
        system_prompt = self.config.system_prompt + BLOCKED_INSTRUCTION

        # Build command with permission flags
        permission_flags = self._get_permission_flags()

        try:
            cmd = [
                "claude",
                "--print",
                "--session-id", session_id,
                "--output-format", "json",
                "--system-prompt", system_prompt,
                *permission_flags,
                prompt,
            ]
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=timeout,
                cwd=str(self.config.get_project_root()),
            )

            # Parse JSON output from Claude CLI
            output_text = ""
            if result.stdout:
                try:
                    json_out = json.loads(result.stdout)
                    output_text = json_out.get("result", result.stdout)
                except json.JSONDecodeError:
                    output_text = result.stdout

            if result.returncode != 0:
                output_text = result.stderr or output_text

            success = result.returncode == 0

            # Check if the agent signaled it's blocked
            blocked = False
            blocker_question = ""
            if success and BLOCKED_MARKER in output_text:
                blocked = True
                # Extract everything after the marker as the question
                marker_pos = output_text.rfind(BLOCKED_MARKER)
                blocker_question = output_text[marker_pos + len(BLOCKED_MARKER):].strip()
                await self.notify(
                    f"Blocked: {blocker_question[:100]}", level="approval"
                )

            task_result = TaskResult(
                success=success and not blocked,
                output=output_text,
                files_changed=[],
                needs_approval=False,
                session_id=session_id,
                blocked=blocked,
                blocker_question=blocker_question,
            )

            self.task_history.append(task_result)

            if blocked:
                await self.notify(f"Waiting for input (session {session_id[:8]})")
            elif success:
                await self.notify("Task completed successfully")
            else:
                await self.notify(f"Task failed: {output_text[:100]}", level="error")

            return task_result

        except subprocess.TimeoutExpired:
            await self.notify(f"Task timed out after {timeout}s", level="error")
            return TaskResult(
                success=False, output="Task timed out",
                files_changed=[], session_id=session_id,
            )
        except Exception as e:
            await self.notify(f"Task error: {str(e)}", level="error")
            return TaskResult(
                success=False, output=str(e),
                files_changed=[], session_id=session_id,
            )

    async def commit_changes(
        self,
        message: str,
        issue_number: Optional[int] = None
    ) -> Dict[str, Any]:
        """Stage and commit changes"""
        self.git.add()
        result = self.git.commit(message, issue_number)

        return {
            "success": result.success,
            "hash": result.hash,
            "files": result.files,
            "message": result.message
        }

    def get_status(self) -> Dict[str, Any]:
        """Get current agent status"""
        return {
            "name": self.config.name,
            "role": self.config.role,
            "pending_approvals": len(self.pending_approvals),
            "tasks_completed": len(self.task_history),
            "tasks_succeeded": sum(1 for t in self.task_history if t.success),
            "project_root": str(self.config.get_project_root()),
            "github_repo": self.config.github_repo,
        }

    async def resume_task(
        self, session_id: str, answer: str, timeout: int = 600
    ) -> TaskResult:
        """Resume a blocked task by providing the answer to the agent's question.

        Uses claude --resume to continue the exact session where the agent
        stopped working. The agent retains full memory of what it was doing.
        """
        await self.notify(f"Resuming session {session_id[:8]} with answer...")

        permission_flags = self._get_permission_flags()

        try:
            cmd = [
                "claude",
                "--print",
                "--resume", session_id,
                "--output-format", "json",
                *permission_flags,
                answer,
            ]
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=timeout,
                cwd=str(self.config.get_project_root()),
            )

            # Parse JSON output
            output_text = ""
            if result.stdout:
                try:
                    json_out = json.loads(result.stdout)
                    output_text = json_out.get("result", result.stdout)
                except json.JSONDecodeError:
                    output_text = result.stdout

            if result.returncode != 0:
                output_text = result.stderr or output_text

            success = result.returncode == 0

            # Check if the agent is blocked again (needs another answer)
            blocked = False
            blocker_question = ""
            if success and BLOCKED_MARKER in output_text:
                blocked = True
                marker_pos = output_text.rfind(BLOCKED_MARKER)
                blocker_question = output_text[marker_pos + len(BLOCKED_MARKER):].strip()
                await self.notify(
                    f"Still blocked: {blocker_question[:100]}", level="approval"
                )

            task_result = TaskResult(
                success=success and not blocked,
                output=output_text,
                files_changed=[],
                session_id=session_id,
                blocked=blocked,
                blocker_question=blocker_question,
            )

            self.task_history.append(task_result)

            if blocked:
                await self.notify(f"Needs more input (session {session_id[:8]})")
            elif success:
                await self.notify("Resumed task completed successfully")
            else:
                await self.notify(f"Resumed task failed: {output_text[:100]}", level="error")

            return task_result

        except subprocess.TimeoutExpired:
            await self.notify(f"Resumed task timed out after {timeout}s", level="error")
            return TaskResult(
                success=False, output="Task timed out",
                files_changed=[], session_id=session_id,
            )
        except Exception as e:
            await self.notify(f"Resume error: {str(e)}", level="error")
            return TaskResult(
                success=False, output=str(e),
                files_changed=[], session_id=session_id,
            )

    async def work(self, task: str) -> TaskResult:
        """General work method - override in subclasses for specialized behavior"""
        return await self.run_task(task)
