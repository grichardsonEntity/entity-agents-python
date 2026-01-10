"""
Sydney Agent - Senior Backend Developer

Expert in Python, FastAPI, Node.js, databases, and API design.
"""

import asyncio
from typing import Optional, List

from ..shared import BaseAgent, TaskResult
from .config import sydney_config


class SydneyAgent(BaseAgent):
    """
    Sydney - Senior Backend Developer

    Specializes in:
    - Python/FastAPI backend services
    - Node.js/Express APIs
    - Database design and optimization
    - Docker containerization
    """

    def __init__(self, config=None):
        super().__init__(config or sydney_config)

    async def create_endpoint(
        self,
        method: str,
        path: str,
        description: str,
        request_body: str = None,
        response: str = None
    ) -> TaskResult:
        """Create a new API endpoint"""
        await self.notify(f"Creating endpoint: {method} {path}")

        prompt = f"""
Create a new API endpoint:

**Method:** {method}
**Path:** {path}
**Description:** {description}

{f"**Request Body:**\n{request_body}" if request_body else ""}
{f"**Response:**\n{response}" if response else ""}

**Requirements:**
1. Follow existing patterns in the codebase
2. Add proper request/response validation
3. Include error handling
4. Add OpenAPI documentation
5. Write a basic test for the endpoint
"""

        return await self.run_task(prompt)

    async def create_service(self, name: str, description: str) -> TaskResult:
        """Create a new microservice"""
        await self.notify(f"Creating service: {name}")

        prompt = f"""
Create a new microservice:

**Service Name:** {name}
**Description:** {description}

**Structure:**
```
services/{name}/
├── Dockerfile
├── requirements.txt
├── app.py              # Entry point with FastAPI
├── config.py           # Environment configuration
├── models.py           # Pydantic models
└── utils.py            # Helper functions
```

**Requirements:**
1. Include /health endpoint
2. Use environment variables for config
3. Add proper error handling
4. Include Dockerfile
5. Add to docker-compose.yml if applicable
"""

        return await self.run_task(prompt)

    async def optimize_query(self, query_location: str) -> TaskResult:
        """Optimize a database query"""
        prompt = f"""
Optimize the database query at: {query_location}

**Analyze and improve:**
1. Add appropriate indexes
2. Optimize JOIN operations
3. Use query caching if beneficial
4. Consider pagination for large results
5. Add query profiling comments
"""

        return await self.run_task(prompt)

    async def add_database_migration(self, description: str) -> TaskResult:
        """Create a database migration"""
        prompt = f"""
Create a database migration:

**Description:** {description}

**Requirements:**
1. Create proper up/down migration
2. Handle data migrations if needed
3. Add rollback safety
4. Update models to match
"""

        return await self.run_task(prompt)

    async def fix_bug(self, issue_number: int) -> TaskResult:
        """Fix a backend bug"""
        if not self.github:
            return TaskResult(success=False, output="GitHub not configured")

        issue = self.github.get_issue(issue_number)
        if not issue:
            return TaskResult(success=False, output=f"Issue #{issue_number} not found")

        await self.notify(f"Working on: {issue.title}")

        self.github.add_label(issue_number, "in-progress")
        self.github.add_comment(issue_number, "⚙️ Sydney is investigating this backend issue...")

        prompt = f"""
Fix this backend bug:

**Issue #{issue.number}:** {issue.title}

**Description:**
{issue.body}

**Instructions:**
1. Read the relevant service files
2. Identify the root cause
3. Implement the fix
4. Add/update tests
5. DO NOT break existing functionality

Focus on backend code in:
- services/
- routes/
- models/
"""

        result = await self.run_task(prompt)

        if result.success:
            commit = await self.commit_changes(
                f"fix(api): {issue.title[:50]}",
                issue_number
            )
            result.commit_hash = commit.get("hash")

            self.github.add_comment(
                issue_number,
                f"## Fix Applied\n\n"
                f"Sydney has implemented a fix.\n\n"
                f"**Commit:** {commit.get('hash', 'See git log')}"
            )

        return result

    async def work(self, task: str) -> TaskResult:
        """General backend work"""
        await self.notify(f"Starting: {task[:50]}...")
        return await self.run_task(task)


async def main():
    """CLI entry point"""
    import argparse
    import json

    parser = argparse.ArgumentParser(description="Sydney - Backend Developer Agent")
    parser.add_argument("--endpoint", nargs=2, metavar=("METHOD", "PATH"), help="Create endpoint")
    parser.add_argument("--description", type=str, help="Description for endpoint/service")
    parser.add_argument("--service", type=str, help="Create microservice")
    parser.add_argument("--optimize", type=str, help="Optimize query at location")
    parser.add_argument("--migration", type=str, help="Create migration")
    parser.add_argument("--fix", type=int, help="Fix issue by number")
    parser.add_argument("--task", type=str, help="Run general task")
    parser.add_argument("--status", action="store_true", help="Show status")

    args = parser.parse_args()

    agent = SydneyAgent()

    if args.status:
        print(json.dumps(agent.get_status(), indent=2))
        return

    if args.endpoint and args.description:
        result = await agent.create_endpoint(args.endpoint[0], args.endpoint[1], args.description)
        print(result.output)
        return

    if args.service and args.description:
        result = await agent.create_service(args.service, args.description)
        print(result.output)
        return

    if args.optimize:
        result = await agent.optimize_query(args.optimize)
        print(result.output)
        return

    if args.migration:
        result = await agent.add_database_migration(args.migration)
        print(result.output)
        return

    if args.fix:
        result = await agent.fix_bug(args.fix)
        print(result.output)
        return

    if args.task:
        result = await agent.work(args.task)
        print(result.output)
        return

    print("Sydney - Backend Developer")
    print("==========================")
    print("Use --help for options")


if __name__ == "__main__":
    asyncio.run(main())
