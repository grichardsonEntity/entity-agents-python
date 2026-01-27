"""
Valentina Agent - UI Developer

Expert frontend developer specializing in React, Flask/Jinja2, CSS, and accessibility.
"""

import asyncio
from typing import Optional, List

from ..shared import BaseAgent, TaskResult
from .config import valentina_config


class ValentinaAgent(BaseAgent):
    """
    Valentina - Senior UI Developer

    Specializes in:
    - React components and hooks
    - Flask/Jinja2 templates
    - CSS and design systems
    - Accessibility and responsive design
    """

    def __init__(self, config=None):
        super().__init__(config or valentina_config)

    async def get_assigned_bugs(self) -> List[dict]:
        """Get UI-related bugs from GitHub"""
        if not self.github:
            return []

        issues = self.github.get_issues(self.config.github_labels, "open")

        return [
            {
                "number": issue.number,
                "title": issue.title,
                "labels": issue.labels,
                "url": issue.url
            }
            for issue in issues
            if self._is_ui_issue(issue)
        ]

    def _is_ui_issue(self, issue) -> bool:
        """Check if issue is UI-related"""
        ui_keywords = [
            "component", "display", "render", "style", "css",
            "layout", "responsive", "button", "modal", "form",
            "frontend", "ui", "ux", "design"
        ]
        body_lower = issue.body.lower() if issue.body else ""
        return any(kw in body_lower for kw in ui_keywords)

    async def fix_bug(self, issue_number: int) -> TaskResult:
        """Fix a specific UI bug"""
        if not self.github:
            return TaskResult(success=False, output="GitHub not configured")

        issue = self.github.get_issue(issue_number)
        if not issue:
            return TaskResult(success=False, output=f"Issue #{issue_number} not found")

        await self.notify(f"Working on: {issue.title}")

        self.github.add_label(issue_number, "in-progress")
        self.github.add_comment(issue_number, "🎨 Valentina is investigating this UI issue...")

        prompt = f"""
Fix this UI bug:

**Issue #{issue.number}:** {issue.title}

**Description:**
{issue.body}

**Instructions:**
1. Read the relevant component and CSS files
2. Identify the root cause of the bug
3. Implement the fix with minimal changes
4. Follow the project's design system
5. Ensure accessibility is maintained
6. DO NOT add unnecessary changes or refactoring

Focus on frontend code in:
- src/components/ or templates/
- static/css/ or src/styles/
- static/js/ or src/hooks/
"""

        result = await self.run_task(prompt)

        if result.success:
            commit = await self.commit_changes(
                f"fix(ui): {issue.title[:50]}",
                issue_number
            )
            result.commit_hash = commit.get("hash")
            result.files_changed = commit.get("files", [])

            self.github.add_comment(
                issue_number,
                f"## Fix Applied\n\n"
                f"Valentina has implemented a fix.\n\n"
                f"**Commit:** {commit.get('hash', 'See git log')}\n"
                f"**Files Changed:** {', '.join(commit.get('files', []))}\n\n"
                f"Please verify and close if resolved."
            )

        return result

    async def create_component(self, name: str, description: str) -> TaskResult:
        """Create a new UI component"""
        await self.notify(f"Creating component: {name}")

        prompt = f"""
Create a new UI component:

**Component Name:** {name}
**Description:** {description}

**Requirements:**
1. Create the component with proper structure
2. Include CSS/styling
3. Add TypeScript types (if React) or proper Jinja2 macros (if Flask)
4. Follow the project's design system
5. Include accessibility features (ARIA labels, keyboard navigation)
6. Support dark/light themes if applicable
7. Add JSDoc/docstring comments
"""

        return await self.run_task(prompt)

    async def improve_accessibility(self, component_path: str) -> TaskResult:
        """Improve accessibility of a component"""
        prompt = f"""
Improve accessibility for: {component_path}

**Audit and fix:**
1. Add missing ARIA labels and roles
2. Ensure proper heading hierarchy
3. Add keyboard navigation support
4. Verify color contrast (WCAG AA)
5. Add screen reader text where needed
6. Ensure focus states are visible
7. Test with keyboard-only navigation
"""

        return await self.run_task(prompt)

    async def work(self, task: str) -> TaskResult:
        """General UI work"""
        await self.notify(f"Starting: {task[:50]}...")
        return await self.run_task(task)


async def main():
    """CLI entry point"""
    import argparse
    import json

    parser = argparse.ArgumentParser(description="Valentina - UI Developer Agent")
    parser.add_argument("--bugs", action="store_true", help="List assigned bugs")
    parser.add_argument("--fix", type=int, help="Fix issue by number")
    parser.add_argument("--create", type=str, help="Create component")
    parser.add_argument("--description", type=str, help="Component description")
    parser.add_argument("--a11y", type=str, help="Improve accessibility for path")
    parser.add_argument("--task", type=str, help="Run general task")
    parser.add_argument("--status", action="store_true", help="Show status")

    args = parser.parse_args()

    agent = ValentinaAgent()

    if args.status:
        print(json.dumps(agent.get_status(), indent=2))
        return

    if args.bugs:
        bugs = await agent.get_assigned_bugs()
        for bug in bugs:
            print(f"#{bug['number']}: {bug['title']}")
        return

    if args.fix:
        result = await agent.fix_bug(args.fix)
        print(result.output)
        return

    if args.create and args.description:
        result = await agent.create_component(args.create, args.description)
        print(result.output)
        return

    if args.a11y:
        result = await agent.improve_accessibility(args.a11y)
        print(result.output)
        return

    if args.task:
        result = await agent.work(args.task)
        print(result.output)
        return

    # Interactive mode
    print("Valentina - UI Developer")
    print("========================")
    print("Commands: bugs, fix <n>, create <name>, a11y <path>, status, quit")

    while True:
        try:
            cmd = input("Valentina> ").strip()
            if not cmd:
                continue
            if cmd.lower() == "quit":
                break
            if cmd.lower() == "status":
                print(json.dumps(agent.get_status(), indent=2))
            elif cmd.lower() == "bugs":
                bugs = await agent.get_assigned_bugs()
                for bug in bugs:
                    print(f"#{bug['number']}: {bug['title']}")
            else:
                result = await agent.work(cmd)
                print(result.output)
        except KeyboardInterrupt:
            break


if __name__ == "__main__":
    asyncio.run(main())
