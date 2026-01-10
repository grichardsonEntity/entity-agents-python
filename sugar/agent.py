"""
Sugar Agent - Documentation Specialist

Expert in technical writing, API docs, and architecture diagrams.
"""

import asyncio
from typing import Optional, List

from ..shared import BaseAgent, TaskResult
from .config import sugar_config


class SugarAgent(BaseAgent):
    """
    Sugar - Documentation Specialist

    Specializes in:
    - Technical writing
    - API documentation
    - Architecture diagrams
    - User guides
    """

    def __init__(self, config=None):
        super().__init__(config or sugar_config)

    async def document_feature(self, feature: str, code_path: str = None) -> TaskResult:
        """Document a feature"""
        await self.notify(f"Documenting feature: {feature}")

        prompt = f"""
Document feature: {feature}
{f"Code location: {code_path}" if code_path else ""}

**First:**
1. Read and understand the feature code
2. Identify key components and flows
3. Note any configuration options

**Create documentation:**

## Feature: {feature}

### Overview
What this feature does and why it exists

### How It Works
Technical explanation with flow diagram

### Configuration
Required settings and options

### Usage Examples
```python
# Example code
```

### API Reference (if applicable)
Endpoint documentation

### Troubleshooting
Common issues and solutions

**Save to:** docs/features/{feature.lower().replace(' ', '-')}.md
"""

        return await self.run_task(prompt)

    async def document_api(self, endpoint: str, code_path: str = None) -> TaskResult:
        """Document an API endpoint"""
        await self.notify(f"Documenting API: {endpoint}")

        prompt = f"""
Document API endpoint: {endpoint}
{f"Code location: {code_path}" if code_path else ""}

**Generate OpenAPI-style documentation:**

## {endpoint}

### Description
What this endpoint does

### Authentication
Required authentication method

### Request

**Headers:**
| Header | Required | Description |
|--------|----------|-------------|
| Authorization | Yes | Bearer token |

**Parameters:**
| Name | Type | Required | Description |
|------|------|----------|-------------|
| ... | ... | ... | ... |

**Request Body:**
```json
{{
  "field": "value"
}}
```

### Response

**Success (200):**
```json
{{
  "data": {{}}
}}
```

**Errors:**
| Status | Description |
|--------|-------------|
| 400 | Bad Request |
| 401 | Unauthorized |
| 404 | Not Found |

### Example

```bash
curl -X POST {endpoint} \\
  -H "Authorization: Bearer $TOKEN" \\
  -H "Content-Type: application/json" \\
  -d '{{"field": "value"}}'
```
"""

        return await self.run_task(prompt)

    async def create_diagram(self, subject: str, diagram_type: str = "flow") -> TaskResult:
        """Create a Mermaid diagram"""
        await self.notify(f"Creating {diagram_type} diagram for: {subject}")

        prompt = f"""
Create {diagram_type} diagram for: {subject}

**Diagram types:**
- flow: Process or data flow
- sequence: Interaction sequence
- class: Class relationships
- er: Entity relationships
- state: State machine

**Generate Mermaid diagram:**

```mermaid
{f"graph TD" if diagram_type == "flow" else ""}
{f"sequenceDiagram" if diagram_type == "sequence" else ""}
{f"classDiagram" if diagram_type == "class" else ""}
{f"erDiagram" if diagram_type == "er" else ""}
{f"stateDiagram-v2" if diagram_type == "state" else ""}
    ... diagram content ...
```

**Include:**
- Clear labels
- Proper relationships
- Legend if complex
- Brief description below diagram
"""

        return await self.run_task(prompt)

    async def update_readme(self, project_path: str = ".") -> TaskResult:
        """Update project README"""
        await self.notify(f"Updating README for: {project_path}")

        prompt = f"""
Update README for project at: {project_path}

**Review current state:**
1. Read existing README.md
2. Scan project structure
3. Check package.json/pyproject.toml for details

**Ensure README has:**

# Project Name

Brief description

## Features
- Feature 1
- Feature 2

## Quick Start

```bash
# Installation
pip install ...

# Run
python ...
```

## Configuration
Environment variables and options

## Usage
Common use cases with examples

## API Reference
Link to API docs or brief overview

## Development
Setup for contributors

## License
License information
"""

        return await self.run_task(prompt)

    async def create_architecture_doc(self, system: str) -> TaskResult:
        """Create architecture documentation"""
        prompt = f"""
Create architecture documentation for: {system}

## Architecture: {system}

### Overview
System purpose and scope

### High-Level Architecture

```mermaid
graph TD
    subgraph Frontend
        A[Web App]
    end
    subgraph Backend
        B[API Gateway]
        C[Service A]
        D[Service B]
    end
    subgraph Data
        E[Database]
        F[Cache]
    end
    A --> B
    B --> C
    B --> D
    C --> E
    D --> F
```

### Components

| Component | Technology | Purpose |
|-----------|------------|---------|
| ... | ... | ... |

### Data Flow
How data moves through the system

### Security
Authentication, authorization, encryption

### Deployment
How the system is deployed

### Scaling
How components scale

### Monitoring
Logging, metrics, alerts
"""

        return await self.run_task(prompt)

    async def work(self, task: str) -> TaskResult:
        """General documentation work"""
        await self.notify(f"Starting: {task[:50]}...")
        return await self.run_task(task)


async def main():
    """CLI entry point"""
    import argparse
    import json

    parser = argparse.ArgumentParser(description="Sugar - Documentation Agent")
    parser.add_argument("--feature", type=str, help="Document feature")
    parser.add_argument("--api", type=str, help="Document API endpoint")
    parser.add_argument("--diagram", type=str, help="Create diagram for subject")
    parser.add_argument("--type", type=str, default="flow", help="Diagram type")
    parser.add_argument("--readme", type=str, nargs="?", const=".", help="Update README")
    parser.add_argument("--architecture", type=str, help="Create architecture doc")
    parser.add_argument("--task", type=str, help="Run general task")
    parser.add_argument("--status", action="store_true", help="Show status")

    args = parser.parse_args()

    agent = SugarAgent()

    if args.status:
        print(json.dumps(agent.get_status(), indent=2))
        return

    if args.feature:
        result = await agent.document_feature(args.feature)
        print(result.output)
        return

    if args.api:
        result = await agent.document_api(args.api)
        print(result.output)
        return

    if args.diagram:
        result = await agent.create_diagram(args.diagram, args.type)
        print(result.output)
        return

    if args.readme is not None:
        result = await agent.update_readme(args.readme)
        print(result.output)
        return

    if args.architecture:
        result = await agent.create_architecture_doc(args.architecture)
        print(result.output)
        return

    if args.task:
        result = await agent.work(args.task)
        print(result.output)
        return

    print("Sugar - Documentation Specialist")
    print("=================================")
    print("Use --help for options")


if __name__ == "__main__":
    asyncio.run(main())
