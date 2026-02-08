"""
Asheton Agent - Product Strategist

Expert in product vision, feature prioritization, requirements,
competitive analysis, market research, and go-to-market strategy.
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
    - Competitive analysis
    - Market research
    - Stakeholder management
    - OKR/KPI frameworks
    - Customer feedback synthesis
    - Go-to-market strategy
    - Product analytics
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

    async def competitive_analysis(self, market: str, competitors: List[str] = None) -> TaskResult:
        """Full competitive landscape analysis with feature matrix, SWOT, and positioning"""
        await self.notify(f"Analyzing competitive landscape: {market}")

        competitors_text = ""
        if competitors:
            competitors_text = f"Known competitors to evaluate:\n" + "\n".join(f"- {c}" for c in competitors)

        prompt = f"""
Conduct a comprehensive competitive analysis for the market: {market}

{competitors_text}

## Competitive Landscape

### Market Overview
[Industry context, market maturity, key dynamics]

### Competitor Profiles

For each major competitor:
- **Company:** [Name]
- **Positioning:** [How they position themselves]
- **Target Audience:** [Who they serve]
- **Strengths:** [Key advantages]
- **Weaknesses:** [Key gaps]
- **Pricing:** [Pricing model and range]
- **Market Share:** [Estimated share]

### Feature Comparison Matrix

| Feature | Our Product | Competitor A | Competitor B | Competitor C |
|---------|-------------|-------------|-------------|-------------|
| Feature 1 | [Y/N/Partial] | [Y/N/Partial] | [Y/N/Partial] | [Y/N/Partial] |
| Feature 2 | [Y/N/Partial] | [Y/N/Partial] | [Y/N/Partial] | [Y/N/Partial] |
| Feature 3 | [Y/N/Partial] | [Y/N/Partial] | [Y/N/Partial] | [Y/N/Partial] |

### SWOT Analysis

#### Strengths
- [Strength 1]
- [Strength 2]

#### Weaknesses
- [Weakness 1]
- [Weakness 2]

#### Opportunities
- [Opportunity 1]
- [Opportunity 2]

#### Threats
- [Threat 1]
- [Threat 2]

### Competitive Positioning Map
[Describe positioning on key axes: price vs features, ease-of-use vs power, etc.]

### Differentiation Strategy
- **Current differentiators:** [What sets us apart today]
- **Moat opportunities:** [Defensible advantages to build]
- **Gaps to close:** [Where competitors lead]
- **Blue ocean areas:** [Uncontested market space]

### Strategic Recommendations
1. [Recommendation with rationale]
2. [Recommendation with rationale]
3. [Recommendation with rationale]
"""

        return await self.run_task(prompt)

    async def market_research(self, product_area: str, target_audience: str) -> TaskResult:
        """Market research with TAM/SAM/SOM sizing, segments, trends, and growth vectors"""
        await self.notify(f"Researching market: {product_area} for {target_audience}")

        prompt = f"""
Conduct comprehensive market research for: {product_area}
Target audience: {target_audience}

## Market Research Report

### Executive Summary
[High-level findings and key takeaways]

### Market Sizing

#### TAM (Total Addressable Market)
- **Size:** $[X]B
- **Methodology:** [How calculated — top-down/bottom-up]
- **Growth rate:** [X]% CAGR
- **Time horizon:** [Years]

#### SAM (Serviceable Addressable Market)
- **Size:** $[X]M
- **Geographic scope:** [Regions]
- **Segment focus:** [Which segments we can serve]

#### SOM (Serviceable Obtainable Market)
- **Size:** $[X]M
- **Realistic capture:** [X]% of SAM
- **Timeline:** [Years to achieve]
- **Assumptions:** [Key assumptions]

### Customer Segments

| Segment | Size | Pain Points | Willingness to Pay | Priority |
|---------|------|-------------|--------------------|---------|
| Segment A | [Size] | [Pains] | [$/range] | [H/M/L] |
| Segment B | [Size] | [Pains] | [$/range] | [H/M/L] |

#### Ideal Customer Profile (ICP)
- **Company size:** [Range]
- **Industry:** [Verticals]
- **Budget:** [Range]
- **Decision maker:** [Title/role]
- **Key pain points:** [Top 3]

### Market Trends
1. **Trend:** [Description, impact, timeline]
2. **Trend:** [Description, impact, timeline]
3. **Trend:** [Description, impact, timeline]

### Growth Opportunities
1. **Opportunity:** [Description]
   - **Potential:** [Revenue impact]
   - **Effort:** [Investment required]
   - **Timeline:** [Time to capture]

2. **Opportunity:** [Description]
   - **Potential:** [Revenue impact]
   - **Effort:** [Investment required]
   - **Timeline:** [Time to capture]

### Risks and Barriers
- [Risk/barrier 1]
- [Risk/barrier 2]
- [Risk/barrier 3]

### Recommendations
[Strategic recommendations based on findings]
"""

        return await self.run_task(prompt)

    async def stakeholder_map(self, project: str, stakeholders: List[str]) -> TaskResult:
        """Stakeholder analysis with influence/interest matrix and communication plan"""
        await self.notify(f"Mapping stakeholders for: {project}")

        stakeholders_text = "\n".join(f"- {s}" for s in stakeholders)

        prompt = f"""
Create stakeholder analysis for project: {project}

Stakeholders to map:
{stakeholders_text}

## Stakeholder Analysis

### Project Context
[Brief project description and why stakeholder management matters here]

### Stakeholder Profiles

For each stakeholder:
- **Name/Role:** [Stakeholder]
- **Interest in project:** [What they care about]
- **Influence level:** [High/Medium/Low]
- **Interest level:** [High/Medium/Low]
- **Current stance:** [Supportive / Neutral / Resistant]
- **Key concerns:** [What worries them]
- **What they need:** [Information, reassurance, involvement]

### Influence/Interest Matrix

|  | Low Interest | High Interest |
|---|-------------|---------------|
| **High Influence** | KEEP SATISFIED | MANAGE CLOSELY |
| **Low Influence** | MONITOR | KEEP INFORMED |

#### Quadrant Placement
- **Manage Closely (High Influence, High Interest):** [Names]
- **Keep Satisfied (High Influence, Low Interest):** [Names]
- **Keep Informed (Low Influence, High Interest):** [Names]
- **Monitor (Low Influence, Low Interest):** [Names]

### Communication Plan

| Stakeholder | Channel | Frequency | Content | Owner |
|-------------|---------|-----------|---------|-------|
| [Name] | [Email/Meeting/Slack] | [Daily/Weekly/Monthly] | [What to share] | [Who communicates] |

### Alignment Strategy
1. **Coalition building:** [How to build support]
2. **Resistance management:** [How to address concerns]
3. **Escalation path:** [When and how to escalate]

### Risk Mitigation
- [Stakeholder risk 1 and mitigation]
- [Stakeholder risk 2 and mitigation]

### Decision Framework
- **RACI Matrix:**

| Decision | Responsible | Accountable | Consulted | Informed |
|----------|-------------|-------------|-----------|----------|
| [Decision 1] | [Who] | [Who] | [Who] | [Who] |
"""

        return await self.run_task(prompt)

    async def define_okrs(self, period: str, strategic_goals: List[str]) -> TaskResult:
        """OKR framework with objectives, key results, metrics, and tracking plan"""
        await self.notify(f"Defining OKRs for: {period}")

        goals_text = "\n".join(f"- {g}" for g in strategic_goals)

        prompt = f"""
Define OKR framework for period: {period}

Strategic goals:
{goals_text}

## OKR Framework

### Period: {period}

### Strategic Context
[How these OKRs align to company mission and strategy]

### Objective 1: [Bold, qualitative goal]

**Key Results:**
1. **KR1:** [Measurable outcome] — Baseline: [X] → Target: [Y]
2. **KR2:** [Measurable outcome] — Baseline: [X] → Target: [Y]
3. **KR3:** [Measurable outcome] — Baseline: [X] → Target: [Y]

**Leading Indicators:**
- [Metric that predicts success]
- [Metric that predicts success]

**Initiatives:**
- [Initiative to drive KR achievement]
- [Initiative to drive KR achievement]

### Objective 2: [Bold, qualitative goal]

**Key Results:**
1. **KR1:** [Measurable outcome] — Baseline: [X] → Target: [Y]
2. **KR2:** [Measurable outcome] — Baseline: [X] → Target: [Y]
3. **KR3:** [Measurable outcome] — Baseline: [X] → Target: [Y]

**Leading Indicators:**
- [Metric that predicts success]

**Initiatives:**
- [Initiative to drive KR achievement]

### Objective 3: [Bold, qualitative goal]

**Key Results:**
1. **KR1:** [Measurable outcome] — Baseline: [X] → Target: [Y]
2. **KR2:** [Measurable outcome] — Baseline: [X] → Target: [Y]
3. **KR3:** [Measurable outcome] — Baseline: [X] → Target: [Y]

### Tracking Plan

| Key Result | Metric | Source | Cadence | Owner |
|------------|--------|--------|---------|-------|
| KR1 | [Metric] | [Data source] | [Weekly/Monthly] | [Who] |

### Scoring Methodology
- **0.0-0.3:** Significant miss — needs investigation
- **0.4-0.6:** Progress but fell short — acceptable
- **0.7-1.0:** Strong delivery — on track
- **1.0+:** May not have been ambitious enough

### Quarterly Review Template
1. Score each KR (0.0-1.0)
2. Root cause analysis for misses
3. Celebrate wins
4. Recalibrate for next quarter
5. Identify carry-over items

### Health Metrics (Always-On)
- [Metric that must not degrade while pursuing OKRs]
- [Metric that must not degrade while pursuing OKRs]
"""

        return await self.run_task(prompt)

    async def synthesize_feedback(self, feedback_sources: List[str], product_area: str) -> TaskResult:
        """Customer feedback analysis with themes, sentiment, and prioritized insights"""
        await self.notify(f"Synthesizing feedback for: {product_area}")

        sources_text = "\n".join(f"- {s}" for s in feedback_sources)

        prompt = f"""
Synthesize customer feedback for product area: {product_area}

Feedback sources:
{sources_text}

## Customer Feedback Synthesis

### Executive Summary
[Key findings, top themes, overall sentiment]

### Feedback Volume & Sources

| Source | Volume | Time Period | Reliability |
|--------|--------|-------------|-------------|
| [Source] | [Count] | [Period] | [H/M/L] |

### Theme Analysis

#### Theme 1: [Theme Name]
- **Frequency:** [X mentions / X% of feedback]
- **Sentiment:** [Positive / Negative / Mixed]
- **Representative quotes:**
  - "[Quote 1]"
  - "[Quote 2]"
- **Impact:** [How this affects users]
- **Recommendation:** [What to do]

#### Theme 2: [Theme Name]
- **Frequency:** [X mentions / X% of feedback]
- **Sentiment:** [Positive / Negative / Mixed]
- **Representative quotes:**
  - "[Quote 1]"
- **Impact:** [How this affects users]
- **Recommendation:** [What to do]

### Sentiment Overview

| Dimension | Score | Trend |
|-----------|-------|-------|
| Overall NPS | [Score] | [Up/Down/Flat] |
| CSAT | [Score] | [Up/Down/Flat] |
| Feature satisfaction | [Score] | [Up/Down/Flat] |
| Support satisfaction | [Score] | [Up/Down/Flat] |

### Feature Request Triage

| Request | Frequency | Strategic Fit | Effort | Priority |
|---------|-----------|---------------|--------|----------|
| [Request] | [Count] | [H/M/L] | [S/M/L/XL] | [P0-P3] |

### Pain Point Severity Map

| Pain Point | Severity | Frequency | Workaround Exists | Action |
|------------|----------|-----------|-------------------|--------|
| [Pain] | [Critical/High/Med/Low] | [Count] | [Y/N] | [Fix/Defer/Monitor] |

### Insights & Recommendations

**Immediate Actions (This Sprint):**
1. [Action with rationale]

**Short-term (Next Quarter):**
1. [Action with rationale]

**Strategic (Long-term):**
1. [Action with rationale]

### Gaps in Feedback
- [What we don't know and how to find out]
"""

        return await self.run_task(prompt)

    async def go_to_market_plan(self, product: str, target_market: str) -> TaskResult:
        """Go-to-market strategy with launch planning, pricing, channels, and messaging"""
        await self.notify(f"Building GTM plan: {product} → {target_market}")

        prompt = f"""
Create go-to-market plan for: {product}
Target market: {target_market}

## Go-to-Market Strategy

### Executive Summary
[One paragraph overview of GTM approach]

### Product Positioning
- **For:** [Target customer]
- **Who:** [Statement of need]
- **Our product is:** [Product category]
- **That:** [Key benefit]
- **Unlike:** [Primary competitor]
- **Our product:** [Primary differentiation]

### Target Market Definition
- **Primary segment:** [Description, size, characteristics]
- **Secondary segment:** [Description, size, characteristics]
- **Beachhead market:** [Where to start and why]

### Pricing Strategy

| Tier | Price | Features | Target |
|------|-------|----------|--------|
| Free/Trial | $0 | [Core features] | [Acquisition] |
| Pro | $[X]/mo | [Full features] | [Primary segment] |
| Enterprise | $[X]/mo | [Advanced features] | [Large orgs] |

**Pricing rationale:**
- [Value-based justification]
- [Competitive benchmark]
- [Willingness to pay data]

### Channel Strategy

| Channel | Role | Investment | Expected CAC | Timeline |
|---------|------|------------|-------------|----------|
| [Channel] | [Awareness/Acquisition/Conversion] | [$/effort] | [$X] | [When] |

### Messaging Framework

| Audience | Pain Point | Message | Proof Point |
|----------|-----------|---------|-------------|
| [Persona 1] | [Pain] | [Message] | [Evidence] |
| [Persona 2] | [Pain] | [Message] | [Evidence] |

### Launch Plan

#### Pre-Launch (T-8 to T-4 weeks)
- [ ] [Activity with owner and date]
- [ ] [Activity with owner and date]

#### Launch Week (T-0)
- [ ] [Activity with owner and date]
- [ ] [Activity with owner and date]

#### Post-Launch (T+1 to T+4 weeks)
- [ ] [Activity with owner and date]
- [ ] [Activity with owner and date]

### Success Metrics

| Metric | Target (30 day) | Target (90 day) | Target (6 month) |
|--------|----------------|-----------------|-------------------|
| Signups | [X] | [X] | [X] |
| Activation rate | [X]% | [X]% | [X]% |
| Revenue | $[X] | $[X] | $[X] |
| NPS | [X] | [X] | [X] |

### Budget & Resources

| Category | Investment | Expected Return |
|----------|------------|-----------------|
| [Category] | $[X] | [Expected outcome] |

### Risk Mitigation
| Risk | Probability | Impact | Mitigation |
|------|------------|--------|------------|
| [Risk] | [H/M/L] | [H/M/L] | [Plan] |
"""

        return await self.run_task(prompt)

    async def product_analytics_plan(self, product: str, metrics: List[str] = None) -> TaskResult:
        """Analytics framework with funnel definition, cohort strategy, and A/B test plan"""
        await self.notify(f"Designing analytics plan: {product}")

        metrics_text = ""
        if metrics:
            metrics_text = f"Key metrics of interest:\n" + "\n".join(f"- {m}" for m in metrics)

        prompt = f"""
Design a product analytics plan for: {product}

{metrics_text}

## Product Analytics Framework

### Analytics Philosophy
[Approach to data-driven product decisions]

### North Star Metric
- **Metric:** [The one metric that matters most]
- **Why:** [How it captures value delivery]
- **Current value:** [Baseline]
- **Target:** [Goal with timeline]

### Metric Hierarchy

#### Level 1: Business Metrics
| Metric | Definition | Target | Owner |
|--------|-----------|--------|-------|
| Revenue | [Definition] | [Target] | [Team] |
| Growth rate | [Definition] | [Target] | [Team] |

#### Level 2: Product Metrics
| Metric | Definition | Target | Owner |
|--------|-----------|--------|-------|
| Activation rate | [Definition] | [Target] | [Team] |
| Retention | [Definition] | [Target] | [Team] |
| Engagement | [Definition] | [Target] | [Team] |

#### Level 3: Feature Metrics
| Metric | Definition | Target | Owner |
|--------|-----------|--------|-------|
| Feature adoption | [Definition] | [Target] | [Team] |
| Task completion | [Definition] | [Target] | [Team] |

### Funnel Analysis

```
Stage 1: Awareness     → [Metric: visits]        [Target: X]
    ↓ [X]% conversion
Stage 2: Signup        → [Metric: registrations]  [Target: X]
    ↓ [X]% conversion
Stage 3: Activation    → [Metric: key action]     [Target: X]
    ↓ [X]% conversion
Stage 4: Engagement    → [Metric: DAU/WAU]        [Target: X]
    ↓ [X]% conversion
Stage 5: Revenue       → [Metric: paying users]   [Target: X]
    ↓ [X]% conversion
Stage 6: Referral      → [Metric: invites sent]   [Target: X]
```

**Drop-off Analysis Plan:**
- [How to identify and diagnose each drop-off point]

### Cohort Analysis Strategy

| Cohort Type | Definition | Key Question |
|-------------|-----------|--------------|
| Acquisition cohort | By signup date | How does retention differ by signup month? |
| Behavioral cohort | By first action | Do users who do X retain better? |
| Feature cohort | By feature used | Which features drive retention? |

### Retention Framework
- **D1 retention:** [Target] — Measures first-day experience
- **D7 retention:** [Target] — Measures habit formation
- **D30 retention:** [Target] — Measures product-market fit
- **D90 retention:** [Target] — Measures long-term value

### A/B Testing Plan

#### Test 1: [Test Name]
- **Hypothesis:** If we [change], then [metric] will [improve/increase] by [X]%
- **Primary metric:** [What we measure]
- **Secondary metrics:** [What else to watch]
- **Guardrail metrics:** [What must not degrade]
- **Sample size:** [Required N]
- **Duration:** [Minimum days]
- **Segments:** [Who to include/exclude]

#### Test 2: [Test Name]
- **Hypothesis:** If we [change], then [metric] will [improve/increase] by [X]%
- **Primary metric:** [What we measure]
- **Sample size:** [Required N]
- **Duration:** [Minimum days]

### Testing Prioritization
| Test | Expected Impact | Effort | Confidence | Priority |
|------|----------------|--------|------------|----------|
| [Test] | [H/M/L] | [S/M/L] | [H/M/L] | [1-5] |

### Instrumentation Requirements
- **Events to track:** [List key events]
- **Properties to capture:** [User, session, context properties]
- **Tools needed:** [Analytics platforms]

### Dashboard Design
1. **Executive dashboard:** [KPIs, trends, health metrics]
2. **Product dashboard:** [Funnels, retention, engagement]
3. **Experiment dashboard:** [Active tests, results, learnings]

### Review Cadence
- **Daily:** [Quick health check metrics]
- **Weekly:** [Product review metrics]
- **Monthly:** [Strategic metrics and deep dives]
- **Quarterly:** [Goal review and recalibration]
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
    parser.add_argument("--competitive", type=str, help="Competitive analysis for market")
    parser.add_argument("--competitors", type=str, nargs="+", help="List of competitors (use with --competitive)")
    parser.add_argument("--market-research", type=str, help="Market research for product area")
    parser.add_argument("--target-audience", type=str, help="Target audience (use with --market-research)")
    parser.add_argument("--stakeholder-map", type=str, help="Stakeholder map for project")
    parser.add_argument("--stakeholders", type=str, nargs="+", help="List of stakeholders (use with --stakeholder-map)")
    parser.add_argument("--okrs", type=str, help="Define OKRs for period (e.g., 'Q1 2026')")
    parser.add_argument("--strategic-goals", type=str, nargs="+", help="Strategic goals (use with --okrs)")
    parser.add_argument("--synthesize-feedback", type=str, help="Synthesize feedback for product area")
    parser.add_argument("--feedback-sources", type=str, nargs="+", help="Feedback sources (use with --synthesize-feedback)")
    parser.add_argument("--gtm", type=str, help="Go-to-market plan for product")
    parser.add_argument("--target-market", type=str, help="Target market (use with --gtm)")
    parser.add_argument("--analytics", type=str, help="Product analytics plan for product")
    parser.add_argument("--metrics", type=str, nargs="+", help="Key metrics (use with --analytics)")
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

    if args.competitive:
        result = await agent.competitive_analysis(args.competitive, args.competitors)
        print(result.output)
        return

    if args.market_research and args.target_audience:
        result = await agent.market_research(args.market_research, args.target_audience)
        print(result.output)
        return

    if args.stakeholder_map and args.stakeholders:
        result = await agent.stakeholder_map(args.stakeholder_map, args.stakeholders)
        print(result.output)
        return

    if args.okrs and args.strategic_goals:
        result = await agent.define_okrs(args.okrs, args.strategic_goals)
        print(result.output)
        return

    if args.synthesize_feedback and args.feedback_sources:
        result = await agent.synthesize_feedback(args.feedback_sources, args.synthesize_feedback)
        print(result.output)
        return

    if args.gtm and args.target_market:
        result = await agent.go_to_market_plan(args.gtm, args.target_market)
        print(result.output)
        return

    if args.analytics:
        result = await agent.product_analytics_plan(args.analytics, args.metrics)
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
