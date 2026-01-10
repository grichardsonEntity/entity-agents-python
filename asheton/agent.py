"""
Asheton Agent - Product Strategist

Expert in product vision, feature prioritization, and requirements.
"""

import asyncio
from typing import Optional, List

from ..shared import BaseAgent, TaskResult
from .config import asheton_config


class AshetonAgent(BaseAgent):
    """
    Asheton - Product Strategist

    Specializes in:
    - Product vision
    - Feature prioritization
    - User stories
    - Roadmap planning
    """

    def __init__(self, config=None):
        super().__init__(config or asheton_config)

    async def evaluate_feature(self, feature: str) -> TaskResult:
        """Evaluate a feature request"""
        await self.notify(f"Evaluating feature: {feature}")

        prompt = f"""
Evaluate feature request: {feature}

**Analysis:**

## User Story
As a [user type], I want [{feature}] so that [benefit]

## Impact Assessment
- User value: [High/Medium/Low]
- Business value: [High/Medium/Low]
- Strategic alignment: [High/Medium/Low]

## Effort Assessment
- Development complexity: [S/M/L/XL]
- Dependencies: [List any]
- Risks: [Technical/Resource risks]

## Acceptance Criteria
- [ ] Criterion 1
- [ ] Criterion 2
- [ ] Criterion 3

## Priority Recommendation
**Priority:** P[0-3]

**Justification:**
[Why this priority level]

## Go/No-Go Decision
**Recommendation:** [Proceed / Defer / Decline]

**Rationale:**
[Explanation]
"""

        return await self.run_task(prompt)

    async def prioritize_backlog(self, items: List[str]) -> TaskResult:
        """Prioritize a list of backlog items"""
        await self.notify(f"Prioritizing {len(items)} items")

        items_formatted = "\n".join(f"- {item}" for item in items)

        prompt = f"""
Prioritize these backlog items:
{items_formatted}

**Create prioritized backlog:**

## Priority Matrix

| Item | Impact | Effort | Score | Priority |
|------|--------|--------|-------|----------|
| ... | H/M/L | S/M/L/XL | 1-10 | P0-P3 |

## Recommended Order

### P0 - Do Now
1. [Item] - [Justification]

### P1 - Next Sprint
1. [Item] - [Justification]

### P2 - Backlog
1. [Item] - [Justification]

### P3 - Future / Defer
1. [Item] - [Justification]

## Dependencies
- [Item A] requires [Item B]

## Recommendations
- Items to combine
- Items to split
- Items to remove
"""

        return await self.run_task(prompt)

    async def create_roadmap(self, timeframe: str, goals: str) -> TaskResult:
        """Create a product roadmap"""
        await self.notify(f"Creating roadmap: {timeframe}")

        prompt = f"""
Create product roadmap for: {timeframe}

**Goals:**
{goals}

## Product Roadmap

### Vision
[Overall product direction]

### Phase 1: Foundation
**Goal:** [What we're achieving]
**Features:**
- [ ] Feature 1
- [ ] Feature 2

**Success Metrics:**
- Metric 1: [Target]

### Phase 2: Enhancement
**Goal:** [What we're achieving]
**Features:**
- [ ] Feature 1
- [ ] Feature 2

**Success Metrics:**
- Metric 1: [Target]

### Phase 3: Scale
**Goal:** [What we're achieving]
**Features:**
- [ ] Feature 1
- [ ] Feature 2

**Success Metrics:**
- Metric 1: [Target]

## Dependencies
- External: [APIs, services]
- Internal: [Teams, resources]

## Risks
| Risk | Impact | Mitigation |
|------|--------|------------|
| ... | ... | ... |

## Success Metrics
- Overall KPIs
- Phase-specific metrics
"""

        return await self.run_task(prompt)

    async def write_user_stories(self, feature: str, personas: List[str] = None) -> TaskResult:
        """Write user stories for a feature"""
        prompt = f"""
Write user stories for feature: {feature}

{f"Personas: {', '.join(personas)}" if personas else ""}

## User Stories

### Epic: {feature}

**Story 1:**
As a [user type],
I want [goal],
So that [benefit].

**Acceptance Criteria:**
- [ ] Given [context], when [action], then [outcome]
- [ ] Given [context], when [action], then [outcome]

**Story 2:**
...

## Story Map

```
Epic: {feature}
├── Story 1
│   ├── Task 1.1
│   └── Task 1.2
├── Story 2
│   ├── Task 2.1
│   └── Task 2.2
```

## MVP Definition
Which stories are essential for MVP:
- Story X (essential)
- Story Y (essential)
- Story Z (nice to have)
"""

        return await self.run_task(prompt)

    async def strategic_decision(self, question: str, options: List[str] = None) -> TaskResult:
        """Analyze a strategic decision"""
        await self.notify(f"Analyzing: {question}")

        options_text = ""
        if options:
            options_text = "Options to consider:\n" + "\n".join(f"- {o}" for o in options)

        prompt = f"""
Strategic decision: {question}

{options_text}

## Decision Analysis

### Context
[Current situation and constraints]

### Options

| Option | Description | Pros | Cons |
|--------|-------------|------|------|
| A | ... | ... | ... |
| B | ... | ... | ... |

### Evaluation Criteria
1. [Criterion] - Weight: [1-5]
2. [Criterion] - Weight: [1-5]

### Scoring Matrix

| Option | Criterion 1 | Criterion 2 | Total |
|--------|-------------|-------------|-------|
| A | X | Y | Z |
| B | X | Y | Z |

### Recommendation
**Choose:** [Option]

**Rationale:**
[Why this option]

### Implementation
[Next steps if approved]

### Risks
[What could go wrong and mitigation]
"""

        return await self.run_task(prompt)

    async def work(self, task: str) -> TaskResult:
        """General product work"""
        await self.notify(f"Starting: {task[:50]}...")
        return await self.run_task(task)


async def main():
    """CLI entry point"""
    import argparse
    import json

    parser = argparse.ArgumentParser(description="Asheton - Product Strategist Agent")
    parser.add_argument("--evaluate", type=str, help="Evaluate feature")
    parser.add_argument("--prioritize", type=str, nargs="+", help="Prioritize items")
    parser.add_argument("--roadmap", type=str, help="Create roadmap for timeframe")
    parser.add_argument("--goals", type=str, help="Roadmap goals")
    parser.add_argument("--stories", type=str, help="Write user stories for feature")
    parser.add_argument("--decide", type=str, help="Strategic decision question")
    parser.add_argument("--task", type=str, help="Run general task")
    parser.add_argument("--status", action="store_true", help="Show status")

    args = parser.parse_args()

    agent = AshetonAgent()

    if args.status:
        print(json.dumps(agent.get_status(), indent=2))
        return

    if args.evaluate:
        result = await agent.evaluate_feature(args.evaluate)
        print(result.output)
        return

    if args.prioritize:
        result = await agent.prioritize_backlog(args.prioritize)
        print(result.output)
        return

    if args.roadmap and args.goals:
        result = await agent.create_roadmap(args.roadmap, args.goals)
        print(result.output)
        return

    if args.stories:
        result = await agent.write_user_stories(args.stories)
        print(result.output)
        return

    if args.decide:
        result = await agent.strategic_decision(args.decide)
        print(result.output)
        return

    if args.task:
        result = await agent.work(args.task)
        print(result.output)
        return

    print("Asheton - Product Strategist")
    print("============================")
    print("Use --help for options")


if __name__ == "__main__":
    asyncio.run(main())
