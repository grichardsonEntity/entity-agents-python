"""
Harper Agent - Grant Researcher & Writer

Expert in funding research, proposal development, and compliance.
"""

import asyncio
from typing import Optional, List

from ..shared import BaseAgent, TaskResult
from .config import harper_config


class HarperAgent(BaseAgent):
    """
    Harper - Grant Researcher & Writer

    Specializes in:
    - Funding research
    - Proposal development
    - Compliance
    - Grant management
    """

    def __init__(self, config=None):
        super().__init__(config or harper_config)

    async def research_funding(
        self,
        project_type: str,
        budget_range: str = None,
        geographic_focus: str = None
    ) -> TaskResult:
        """Research funding opportunities"""
        await self.notify(f"Researching funding for: {project_type}")

        prompt = f"""
Research funding opportunities for:
- Project type: {project_type}
{f"- Budget range: {budget_range}" if budget_range else ""}
{f"- Geographic focus: {geographic_focus}" if geographic_focus else ""}

**Search:**
1. Federal sources (Grants.gov, NSF, NIH, DOE)
2. Foundation sources (FDO, GrantWatch, Candid)
3. Corporate giving programs
4. State/local opportunities

**For each opportunity, document:**

## Opportunity: [Name]

| Field | Value |
|-------|-------|
| Funder | [Name] |
| Type | Federal/Foundation/Corporate |
| Award Range | $X - $Y |
| Deadline | [Date] |
| Eligibility | [Requirements] |
| Match Required | Yes/No (X%) |

### Alignment Analysis
- Mission match: High/Medium/Low
- Capacity match: High/Medium/Low
- Competitiveness: High/Medium/Low

### Recommendation
Pursue / Monitor / Pass

### Next Steps
1. [Action item]

**Provide top 5-10 opportunities ranked by fit.**
"""

        return await self.run_task(prompt)

    async def write_needs_statement(
        self,
        problem: str,
        target_population: str,
        data_sources: List[str] = None
    ) -> TaskResult:
        """Write a compelling needs statement"""
        await self.notify(f"Writing needs statement for: {problem[:50]}")

        prompt = f"""
Write needs statement for grant proposal:

**Problem:** {problem}
**Target Population:** {target_population}
{f"**Data sources:** {', '.join(data_sources)}" if data_sources else ""}

**Create needs statement following this structure:**

## Statement of Need

### The Problem
[Clear, compelling opening statement about the problem]

### Evidence
[3-5 data points from credible sources demonstrating the problem's scope]

- Statistic 1 (Source, Year)
- Statistic 2 (Source, Year)
- Statistic 3 (Source, Year)

### Impact
[Who is affected and how - make it personal and relatable]

### Current Gap
[What existing solutions are missing or inadequate]

### Urgency
[Why this must be addressed now - trends, deadlines, windows of opportunity]

### Our Unique Position
[Why we are positioned to address this need]

**Word count target:** 300-500 words
**Tone:** Urgent but hopeful, data-driven but human
"""

        return await self.run_task(prompt)

    async def create_budget(
        self,
        project_description: str,
        total_budget: float,
        duration_months: int = 12
    ) -> TaskResult:
        """Create grant budget with justification"""
        await self.notify(f"Creating budget: ${total_budget:,.0f}")

        prompt = f"""
Create grant budget and justification:

**Project:** {project_description}
**Total Budget:** ${total_budget:,.0f}
**Duration:** {duration_months} months

## Budget

### Personnel
| Position | FTE | Annual Salary | Effort | Cost |
|----------|-----|--------------|--------|------|
| Project Director | 1.0 | $X | X% | $X |
| ... | ... | ... | ... | ... |

**Subtotal Personnel:** $X

### Fringe Benefits (X% of salaries)
$X

### Travel
| Purpose | Cost |
|---------|------|
| ... | ... |

**Subtotal Travel:** $X

### Equipment (>$5,000/item)
| Item | Cost |
|------|------|
| ... | ... |

**Subtotal Equipment:** $X

### Supplies
| Category | Cost |
|----------|------|
| ... | ... |

**Subtotal Supplies:** $X

### Contractual
| Vendor/Purpose | Cost |
|----------------|------|
| ... | ... |

**Subtotal Contractual:** $X

### Other Direct Costs
| Item | Cost |
|------|------|
| ... | ... |

**Subtotal Other:** $X

### Indirect Costs (X% MTDC)
$X

## TOTAL: ${total_budget:,.0f}

## Budget Justification

### Personnel
[Detailed justification for each position]

### Fringe Benefits
[Rate and basis]

### Travel
[Purpose and breakdown of each trip]

### Equipment
[Why needed, alternatives considered]

### Supplies
[Categories and usage]

### Contractual
[Scope, selection process]

### Other
[Detailed breakdown]

### Indirect
[Rate agreement reference]
"""

        return await self.run_task(prompt)

    async def evaluate_opportunity(
        self,
        opportunity_name: str,
        rfp_url: str = None
    ) -> TaskResult:
        """Evaluate a specific funding opportunity"""
        prompt = f"""
Evaluate funding opportunity: {opportunity_name}
{f"RFP/FOA: {rfp_url}" if rfp_url else ""}

## Go/No-Go Analysis

### Basic Eligibility
| Requirement | Status | Notes |
|-------------|--------|-------|
| Organization type | ✓/✗ | ... |
| Geographic | ✓/✗ | ... |
| Prior relationship | ✓/✗ | ... |

### Strategic Fit
| Factor | Score (1-5) | Notes |
|--------|-------------|-------|
| Mission alignment | X | ... |
| Capacity to execute | X | ... |
| Competitive position | X | ... |
| Strategic value | X | ... |

**Total Score:** X/20

### Resource Requirements
- Proposal development: X hours
- Match/cost share: $X
- Personnel commitment: X FTE
- New capabilities needed: [List]

### Risks
| Risk | Impact | Likelihood | Mitigation |
|------|--------|------------|------------|
| ... | ... | ... | ... |

### Decision

**Recommendation:** Pursue / Pass / Request More Info

**Rationale:**
[Explanation]

**If pursuing, next steps:**
1. [Action with deadline]
2. [Action with deadline]
"""

        return await self.run_task(prompt)

    async def write_objectives(self, project_goals: str) -> TaskResult:
        """Write SMART objectives"""
        prompt = f"""
Write SMART objectives for:

{project_goals}

## Goals and Objectives

### Goal 1: [Broad goal statement]

**Objective 1.1:**
By [DATE], [TARGET NUMBER] [TARGET POPULATION] will [MEASURABLE OUTCOME]
as measured by [ASSESSMENT METHOD], resulting in [QUANTIFIABLE CHANGE].

**Objective 1.2:**
...

### Goal 2: [Broad goal statement]

**Objective 2.1:**
...

## Logic Model

| Inputs | Activities | Outputs | Short-term Outcomes | Long-term Outcomes |
|--------|------------|---------|---------------------|-------------------|
| ... | ... | ... | ... | ... |

## Evaluation Plan

| Objective | Indicator | Data Source | Frequency | Target |
|-----------|-----------|-------------|-----------|--------|
| 1.1 | ... | ... | ... | ... |
"""

        return await self.run_task(prompt)

    async def work(self, task: str) -> TaskResult:
        """General grant work"""
        await self.notify(f"Starting: {task[:50]}...")
        return await self.run_task(task)


async def main():
    """CLI entry point"""
    import argparse
    import json

    parser = argparse.ArgumentParser(description="Harper - Grant Research Agent")
    parser.add_argument("--research", type=str, help="Research funding for project type")
    parser.add_argument("--budget", type=str, help="Budget range for research")
    parser.add_argument("--needs", type=str, help="Write needs statement for problem")
    parser.add_argument("--population", type=str, help="Target population for needs")
    parser.add_argument("--create-budget", type=str, help="Create budget for project")
    parser.add_argument("--amount", type=float, help="Budget amount")
    parser.add_argument("--evaluate", type=str, help="Evaluate opportunity")
    parser.add_argument("--objectives", type=str, help="Write objectives for goals")
    parser.add_argument("--task", type=str, help="Run general task")
    parser.add_argument("--status", action="store_true", help="Show status")

    args = parser.parse_args()

    agent = HarperAgent()

    if args.status:
        print(json.dumps(agent.get_status(), indent=2))
        return

    if args.research:
        result = await agent.research_funding(args.research, args.budget)
        print(result.output)
        return

    if args.needs and args.population:
        result = await agent.write_needs_statement(args.needs, args.population)
        print(result.output)
        return

    if args.create_budget and args.amount:
        result = await agent.create_budget(args.create_budget, args.amount)
        print(result.output)
        return

    if args.evaluate:
        result = await agent.evaluate_opportunity(args.evaluate)
        print(result.output)
        return

    if args.objectives:
        result = await agent.write_objectives(args.objectives)
        print(result.output)
        return

    if args.task:
        result = await agent.work(args.task)
        print(result.output)
        return

    print("Harper - Grant Researcher & Writer")
    print("===================================")
    print("Use --help for options")


if __name__ == "__main__":
    asyncio.run(main())
