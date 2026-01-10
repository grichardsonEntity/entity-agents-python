"""
Amber Agent - Systems Architect

Expert in system design, microservices, and architectural decisions.
"""

import asyncio
from typing import Optional

from ..shared import BaseAgent, TaskResult
from .config import amber_config


class AmberAgent(BaseAgent):
    """
    Amber - Systems Architect

    Specializes in:
    - System architecture design
    - Microservices patterns
    - Database schema design
    - API contracts
    """

    def __init__(self, config=None):
        super().__init__(config or amber_config)

    async def design_system(self, requirements: str) -> TaskResult:
        """Design a system architecture"""
        await self.notify(f"Designing system for: {requirements[:50]}...")

        prompt = f"""
Design a system architecture for:

{requirements}

**Provide:**

## 1. Problem Statement
What we're solving and why

## 2. Proposed Architecture

```
┌──────────┐     ┌──────────┐     ┌──────────┐
│ Client   │────▶│ API GW   │────▶│ Services │
└──────────┘     └──────────┘     └──────────┘
```

## 3. Component Details
For each component:
- Purpose
- Technology choice
- Scaling strategy

## 4. Data Model
SQL schema or document structure

## 5. API Contracts
Key endpoints with request/response

## 6. Integration Points
How components communicate

## 7. Trade-offs & Risks
- Pros/cons of this approach
- What could go wrong
- Mitigation strategies
"""

        return await self.run_task(prompt)

    async def review_architecture(self, description: str) -> TaskResult:
        """Review an architectural proposal"""
        prompt = f"""
Review this architectural proposal:

{description}

**Evaluate:**
1. Scalability - Will it scale?
2. Maintainability - Easy to modify?
3. Reliability - Failure modes?
4. Security - Attack surface?
5. Performance - Bottlenecks?
6. Cost - Infrastructure costs?

**Provide:**
- Rating (1-10) for each category
- Specific concerns
- Recommendations
- Alternative approaches if applicable
"""

        return await self.run_task(prompt)

    async def create_adr(self, title: str, context: str, decision: str) -> TaskResult:
        """Create an Architecture Decision Record"""
        await self.notify(f"Creating ADR: {title}")

        prompt = f"""
Create an Architecture Decision Record:

**Title:** {title}
**Context:** {context}
**Decision:** {decision}

**Format:**
```markdown
# ADR-XXX: {title}

## Status
Proposed

## Context
{context}

## Decision
{decision}

## Consequences
- Positive consequences
- Negative consequences
- Risks

## Alternatives Considered
- Alternative 1
- Alternative 2
```

Save to docs/decisions/ADR-XXX-{title.lower().replace(' ', '-')}.md
"""

        return await self.run_task(prompt)

    async def design_api_contract(self, resource: str, operations: str) -> TaskResult:
        """Design an API contract"""
        prompt = f"""
Design API contract for resource: {resource}

Operations: {operations}

**Include:**
1. RESTful endpoints
2. Request/response schemas
3. Error responses
4. Authentication requirements
5. Rate limiting considerations
6. OpenAPI specification
"""

        return await self.run_task(prompt)

    async def design_database_schema(self, requirements: str) -> TaskResult:
        """Design a database schema"""
        prompt = f"""
Design database schema for:

{requirements}

**Include:**
1. Table definitions with proper types
2. Primary and foreign keys
3. Indexes for common queries
4. Constraints
5. Migration script
6. Sample queries
"""

        return await self.run_task(prompt)

    async def work(self, task: str) -> TaskResult:
        """General architecture work"""
        await self.notify(f"Starting: {task[:50]}...")
        return await self.run_task(task)


async def main():
    """CLI entry point"""
    import argparse
    import json

    parser = argparse.ArgumentParser(description="Amber - Systems Architect Agent")
    parser.add_argument("--design", type=str, help="Design system for requirements")
    parser.add_argument("--review", type=str, help="Review architecture")
    parser.add_argument("--adr", type=str, help="Create ADR with title")
    parser.add_argument("--context", type=str, help="ADR context")
    parser.add_argument("--decision", type=str, help="ADR decision")
    parser.add_argument("--api", type=str, help="Design API for resource")
    parser.add_argument("--operations", type=str, help="API operations")
    parser.add_argument("--schema", type=str, help="Design database schema")
    parser.add_argument("--task", type=str, help="Run general task")
    parser.add_argument("--status", action="store_true", help="Show status")

    args = parser.parse_args()

    agent = AmberAgent()

    if args.status:
        print(json.dumps(agent.get_status(), indent=2))
        return

    if args.design:
        result = await agent.design_system(args.design)
        print(result.output)
        return

    if args.review:
        result = await agent.review_architecture(args.review)
        print(result.output)
        return

    if args.adr and args.context and args.decision:
        result = await agent.create_adr(args.adr, args.context, args.decision)
        print(result.output)
        return

    if args.api and args.operations:
        result = await agent.design_api_contract(args.api, args.operations)
        print(result.output)
        return

    if args.schema:
        result = await agent.design_database_schema(args.schema)
        print(result.output)
        return

    if args.task:
        result = await agent.work(args.task)
        print(result.output)
        return

    print("Amber - Systems Architect")
    print("=========================")
    print("Use --help for options")


if __name__ == "__main__":
    asyncio.run(main())
