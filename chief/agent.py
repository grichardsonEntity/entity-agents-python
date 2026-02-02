"""
Chief of Staff Agent - Executive Assistant & Project Orchestrator

Monitors all projects and agent teams, provides status updates,
coordinates work, and helps human supervisors manage everything.
"""

import asyncio
import subprocess
import json
from datetime import datetime, timedelta
from pathlib import Path
from typing import Optional, List, Dict, Any

from ..shared import BaseAgent, TaskResult
from .config import chief_config, MONITORED_PROJECTS, PYTHON_AGENTS, NODE_AGENTS


class ChiefOfStaffAgent(BaseAgent):
    """
    Chief of Staff - Executive Assistant & Project Orchestrator

    Monitors:
    - All Entity projects
    - Python agent team
    - Node agent team

    Provides:
    - Status updates
    - Daily briefings
    - Priority recommendations
    - Handoff coordination
    """

    def __init__(self, config=None):
        super().__init__(config or chief_config)
        self.projects = MONITORED_PROJECTS
        self.python_agents = PYTHON_AGENTS
        self.node_agents = NODE_AGENTS

    # ==================== STATUS METHODS ====================

    async def get_project_status(self, project_path: Path) -> Dict[str, Any]:
        """Get status for a single project"""
        status = {
            "name": project_path.name,
            "path": str(project_path),
            "exists": project_path.exists(),
            "git_status": None,
            "recent_commits": [],
            "branches": [],
            "has_status_file": False,
            "status_file_content": None,
        }

        if not project_path.exists():
            return status

        try:
            # Git status
            result = subprocess.run(
                ["git", "status", "--porcelain"],
                cwd=str(project_path),
                capture_output=True,
                text=True,
                timeout=10
            )
            status["git_status"] = "clean" if not result.stdout.strip() else "dirty"
            status["uncommitted_changes"] = len(result.stdout.strip().split('\n')) if result.stdout.strip() else 0

            # Recent commits (last 24 hours)
            result = subprocess.run(
                ["git", "log", "--oneline", "-10", "--since=24 hours ago"],
                cwd=str(project_path),
                capture_output=True,
                text=True,
                timeout=10
            )
            status["recent_commits"] = [
                line.strip() for line in result.stdout.strip().split('\n') if line.strip()
            ]

            # Current branch
            result = subprocess.run(
                ["git", "branch", "--show-current"],
                cwd=str(project_path),
                capture_output=True,
                text=True,
                timeout=10
            )
            status["current_branch"] = result.stdout.strip()

            # Check for .status.md file
            status_file = project_path / ".status.md"
            if status_file.exists():
                status["has_status_file"] = True
                status["status_file_content"] = status_file.read_text()[:500]

        except Exception as e:
            status["error"] = str(e)

        return status

    async def get_all_project_statuses(self) -> List[Dict[str, Any]]:
        """Get status for all monitored projects"""
        statuses = []
        for project in self.projects:
            status = await self.get_project_status(project)
            statuses.append(status)
        return statuses

    async def get_python_agent_status(self, agent_name: str) -> Dict[str, Any]:
        """Get status of a Python agent"""
        try:
            result = subprocess.run(
                ["python", "-m", f"entity_agents.{agent_name}", "--status"],
                capture_output=True,
                text=True,
                timeout=30
            )
            if result.returncode == 0:
                return json.loads(result.stdout)
            return {"name": agent_name, "status": "error", "error": result.stderr}
        except Exception as e:
            return {"name": agent_name, "status": "error", "error": str(e)}

    async def get_node_agent_status(self, agent_name: str) -> Dict[str, Any]:
        """Get status of a Node agent"""
        node_agents_path = Path.home() / "Projects" / "entity-agents-node"
        try:
            result = subprocess.run(
                ["npm", "run", f"{agent_name}:status"],
                cwd=str(node_agents_path),
                capture_output=True,
                text=True,
                timeout=30
            )
            if result.returncode == 0:
                return json.loads(result.stdout)
            return {"name": agent_name, "status": "unavailable"}
        except Exception as e:
            return {"name": agent_name, "status": "error", "error": str(e)}

    async def get_all_agent_statuses(self) -> Dict[str, List[Dict]]:
        """Get status of all agents in both teams"""
        python_statuses = []
        node_statuses = []

        for agent in self.python_agents:
            status = await self.get_python_agent_status(agent)
            python_statuses.append(status)

        for agent in self.node_agents:
            status = await self.get_node_agent_status(agent)
            node_statuses.append(status)

        return {
            "python_team": python_statuses,
            "node_team": node_statuses
        }

    # ==================== REPORTING METHODS ====================

    async def quick_status(self) -> TaskResult:
        """Generate quick status overview"""
        await self.notify("Generating quick status...")

        project_statuses = await self.get_all_project_statuses()

        lines = ["📊 **Entity Status Overview**", ""]

        for proj in project_statuses:
            if not proj["exists"]:
                indicator = "⚪"
                status_text = "Not found"
            elif proj.get("error"):
                indicator = "🔴"
                status_text = "Error"
            elif proj["recent_commits"]:
                indicator = "🟢"
                status_text = f"{len(proj['recent_commits'])} commits (24h)"
            elif proj["git_status"] == "dirty":
                indicator = "🟡"
                status_text = f"{proj['uncommitted_changes']} uncommitted changes"
            else:
                indicator = "⚪"
                status_text = "No recent activity"

            lines.append(f"{indicator} **{proj['name']}**: {status_text}")

        output = "\n".join(lines)
        return TaskResult(success=True, output=output)

    async def daily_briefing(self) -> TaskResult:
        """Generate comprehensive daily briefing"""
        await self.notify("Generating daily briefing...")

        project_statuses = await self.get_all_project_statuses()
        today = datetime.now().strftime("%Y-%m-%d")

        lines = [
            f"## Entity Daily Briefing - {today}",
            "",
            "### Executive Summary",
            ""
        ]

        # Count activity
        active_projects = sum(1 for p in project_statuses if p.get("recent_commits"))
        total_commits = sum(len(p.get("recent_commits", [])) for p in project_statuses)
        dirty_projects = sum(1 for p in project_statuses if p.get("git_status") == "dirty")

        lines.append(f"{active_projects} projects with activity, {total_commits} commits in last 24h, {dirty_projects} with uncommitted changes.")
        lines.append("")

        # Project status table
        lines.extend([
            "### Project Status",
            "",
            "| Project | Status | Recent Commits | Branch |",
            "|---------|--------|----------------|--------|"
        ])

        for proj in project_statuses:
            if not proj["exists"]:
                lines.append(f"| {proj['name']} | ⚪ Not found | - | - |")
                continue

            if proj.get("recent_commits"):
                status = "🟢 Active"
                commits = str(len(proj["recent_commits"]))
            elif proj.get("git_status") == "dirty":
                status = "🟡 Uncommitted"
                commits = "0"
            else:
                status = "⚪ Quiet"
                commits = "0"

            branch = proj.get("current_branch", "unknown")
            lines.append(f"| {proj['name']} | {status} | {commits} | {branch} |")

        lines.append("")

        # Recent activity
        lines.extend(["### Recent Activity (Last 24h)", ""])

        for proj in project_statuses:
            if proj.get("recent_commits"):
                lines.append(f"**{proj['name']}:**")
                for commit in proj["recent_commits"][:3]:
                    lines.append(f"  - {commit}")
                lines.append("")

        # Recommendations
        lines.extend([
            "### Recommended Focus",
            ""
        ])

        priorities = []
        for proj in project_statuses:
            if proj.get("git_status") == "dirty":
                priorities.append(f"Commit/push changes in **{proj['name']}**")

        if priorities:
            for i, p in enumerate(priorities[:3], 1):
                lines.append(f"{i}. {p}")
        else:
            lines.append("All projects in good state. Continue current work.")

        output = "\n".join(lines)
        return TaskResult(success=True, output=output)

    async def blocker_report(self) -> TaskResult:
        """Generate report of blockers and issues"""
        await self.notify("Checking for blockers...")

        # This would integrate with GitHub issues in a full implementation
        prompt = """Check for blockers across all Entity projects:

1. Check each project for:
   - Failed CI/CD (if applicable)
   - Stale branches
   - Merge conflicts
   - Uncommitted changes that might indicate stuck work

2. Check GitHub for:
   - Issues labeled 'blocked' or 'help wanted'
   - PRs waiting for review
   - Failed checks

Report any blockers found, or confirm if there are none."""

        return await self.run_task(prompt)

    # ==================== COORDINATION METHODS ====================

    async def handoff(self, from_agent: str, to_agent: str, project: str, context: str = "") -> TaskResult:
        """Coordinate handoff between agents"""
        await self.notify(f"Coordinating handoff: {from_agent} → {to_agent}")

        prompt = f"""Coordinate a handoff between agents:

**From:** {from_agent}
**To:** {to_agent}
**Project:** {project}
**Context:** {context}

Tasks:
1. Check recent commits by {from_agent} in {project}
2. Identify what was completed
3. Identify what {to_agent} needs to do next
4. List any open issues or concerns
5. Generate a handoff summary

Format the output as a clear handoff document."""

        return await self.run_task(prompt)

    async def recommend_priorities(self) -> TaskResult:
        """Recommend what to focus on"""
        await self.notify("Analyzing priorities...")

        project_statuses = await self.get_all_project_statuses()

        prompt = f"""Based on the current project statuses, recommend priorities:

Project Status Summary:
{json.dumps(project_statuses, indent=2, default=str)}

Consider:
1. Blockers that are preventing other work
2. Uncommitted changes that should be pushed
3. Projects with no recent activity that might need attention
4. Dependencies between projects

Provide a prioritized list of 3-5 recommended actions."""

        return await self.run_task(prompt)

    async def wrap_up(self) -> TaskResult:
        """End of day wrap up"""
        await self.notify("Generating wrap-up summary...")

        project_statuses = await self.get_all_project_statuses()

        lines = [
            "## End of Day Summary",
            "",
            "### Completed Today",
            ""
        ]

        for proj in project_statuses:
            if proj.get("recent_commits"):
                lines.append(f"**{proj['name']}:** {len(proj['recent_commits'])} commits")
                for commit in proj["recent_commits"][:2]:
                    lines.append(f"  - {commit}")
                lines.append("")

        lines.extend([
            "### Pending",
            ""
        ])

        for proj in project_statuses:
            if proj.get("git_status") == "dirty":
                lines.append(f"- **{proj['name']}:** {proj['uncommitted_changes']} uncommitted changes")

        lines.extend([
            "",
            "### Tomorrow's Priorities",
            "",
            "1. Review and commit any pending changes",
            "2. Continue work on active projects",
            "3. Check for any new blockers",
        ])

        output = "\n".join(lines)
        return TaskResult(success=True, output=output)

    # ==================== CLI INTERFACE ====================

    async def work(self, task: str) -> TaskResult:
        """General work - interpret command and route appropriately"""
        task_lower = task.lower().strip()

        if "status" in task_lower and "quick" in task_lower:
            return await self.quick_status()
        elif "status" in task_lower:
            return await self.quick_status()
        elif "briefing" in task_lower or "brief" in task_lower:
            return await self.daily_briefing()
        elif "blocker" in task_lower:
            return await self.blocker_report()
        elif "priorit" in task_lower or "focus" in task_lower:
            return await self.recommend_priorities()
        elif "wrap" in task_lower or "end of day" in task_lower:
            return await self.wrap_up()
        elif "handoff" in task_lower:
            # Parse handoff request
            return await self.run_task(f"Parse and execute this handoff request: {task}")
        else:
            # General request - use Claude to figure it out
            return await self.run_task(task)


async def main():
    """CLI entry point"""
    import argparse

    parser = argparse.ArgumentParser(description="Chief of Staff - Project Orchestrator")

    parser.add_argument("--status", action="store_true", help="Quick status overview")
    parser.add_argument("--briefing", action="store_true", help="Full daily briefing")
    parser.add_argument("--blockers", action="store_true", help="Check for blockers")
    parser.add_argument("--priorities", action="store_true", help="Recommend priorities")
    parser.add_argument("--wrap-up", action="store_true", help="End of day summary")
    parser.add_argument("--handoff", nargs=3, metavar=("FROM", "TO", "PROJECT"), help="Coordinate handoff")
    parser.add_argument("--task", type=str, help="General task/question")
    parser.add_argument("--json", action="store_true", help="Output as JSON")

    args = parser.parse_args()

    agent = ChiefOfStaffAgent()

    result = None

    if args.status:
        result = await agent.quick_status()
    elif args.briefing:
        result = await agent.daily_briefing()
    elif args.blockers:
        result = await agent.blocker_report()
    elif args.priorities:
        result = await agent.recommend_priorities()
    elif args.wrap_up:
        result = await agent.wrap_up()
    elif args.handoff:
        result = await agent.handoff(args.handoff[0], args.handoff[1], args.handoff[2])
    elif args.task:
        result = await agent.work(args.task)
    else:
        # Default to quick status
        result = await agent.quick_status()

    if result:
        if args.json:
            print(json.dumps({
                "success": result.success,
                "output": result.output
            }, indent=2))
        else:
            print(result.output)


if __name__ == "__main__":
    asyncio.run(main())
