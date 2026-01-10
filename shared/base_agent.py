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
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Optional, List, Dict, Any

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

    async def run_task(self, prompt: str, timeout: int = 600) -> TaskResult:
        """Execute a task using Claude CLI"""
        await self.notify(f"Starting task: {prompt[:50]}...")

        try:
            result = subprocess.run(
                [
                    "claude",
                    "--print",
                    "--system-prompt", self.config.system_prompt,
                    prompt
                ],
                capture_output=True,
                text=True,
                timeout=timeout,
                cwd=str(self.config.get_project_root())
            )

            output = result.stdout if result.returncode == 0 else result.stderr
            success = result.returncode == 0

            task_result = TaskResult(
                success=success,
                output=output,
                files_changed=[],
                needs_approval=False
            )

            self.task_history.append(task_result)

            if success:
                await self.notify("Task completed successfully")
            else:
                await self.notify(f"Task failed: {output[:100]}", level="error")

            return task_result

        except subprocess.TimeoutExpired:
            await self.notify(f"Task timed out after {timeout}s", level="error")
            return TaskResult(success=False, output="Task timed out", files_changed=[])
        except Exception as e:
            await self.notify(f"Task error: {str(e)}", level="error")
            return TaskResult(success=False, output=str(e), files_changed=[])

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

    async def work(self, task: str) -> TaskResult:
        """General work method - override in subclasses for specialized behavior"""
        return await self.run_task(task)
