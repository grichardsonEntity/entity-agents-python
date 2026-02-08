"""
Amber Agent - Systems Architect

Expert in system design, microservices, event-driven architecture,
domain-driven design, cloud-native patterns, performance engineering,
legacy migration, and architectural decisions.
"""

import asyncio
from typing import Optional, List

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
    - Event-driven architecture (CQRS, Event Sourcing, Sagas)
    - Legacy system refactoring and migration
    - Performance engineering and capacity planning
    - Domain-Driven Design (bounded contexts, aggregates)
    - Cloud-native patterns (12-factor, circuit breakers)
    - System observability (OpenTelemetry, SLI/SLO)
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

    async def design_event_architecture(
        self, domain: str, events: str, consumers: str
    ) -> TaskResult:
        """Design event-driven architecture with CQRS, event sourcing, and saga orchestration"""
        await self.notify(f"Designing event architecture for: {domain[:50]}...")

        prompt = f"""
Design an event-driven architecture for the following domain:

**Domain:** {domain}
**Key Events:** {events}
**Consumers:** {consumers}

**Provide:**

## 1. Event Catalog
For each domain event:
- Event name (past tense, e.g., OrderPlaced)
- Event schema (JSON with versioning)
- Producer service
- Consumer services
- Ordering guarantees required

## 2. Event Bus Selection
- Recommended technology (Kafka, RabbitMQ, Redis Streams, NATS) with justification
- Topic/queue design and partitioning strategy
- Retention and replay policies
- Dead letter queue configuration

## 3. CQRS Design
- Command model (write side) — aggregates, command handlers, validators
- Query model (read side) — projections, materialized views, query handlers
- Synchronization strategy between write and read models

## 4. Event Sourcing (if applicable)
- Event store design
- Snapshot strategy for aggregate rehydration
- Event versioning and upcasting approach
- Projection rebuild strategy

## 5. Saga Orchestration
- Saga flow diagram for multi-step processes
- Compensating actions for each step (rollback strategy)
- Saga state machine definition
- Timeout and retry policies

## 6. Idempotency & Deduplication
- Idempotency key strategy
- Deduplication mechanism (at-least-once to effectively-once)
- Consumer offset management

## 7. Consistency & Error Handling
- Eventual consistency boundaries
- Error handling and dead letter processing
- Monitoring and alerting for event processing lag

## 8. Trade-offs
- Why this approach over synchronous alternatives
- Complexity cost vs. scalability gain
"""

        return await self.run_task(prompt)

    async def plan_migration(
        self, legacy_system: str, target_architecture: str
    ) -> TaskResult:
        """Plan migration strategy from legacy system to target architecture"""
        await self.notify(f"Planning migration from: {legacy_system[:50]}...")

        prompt = f"""
Create a migration plan from legacy to target architecture:

**Legacy System:** {legacy_system}
**Target Architecture:** {target_architecture}

**Provide:**

## 1. Current State Assessment
- Legacy system inventory (services, databases, integrations)
- Pain points and technical debt catalog
- Dependency map and coupling analysis
- Data flow documentation

## 2. Migration Strategy
- **Strangler Fig Pattern** application plan:
  - Facade/proxy layer design
  - Feature-by-feature migration sequence
  - Routing rules (legacy vs new)
- **Branch by Abstraction** opportunities:
  - Abstraction layer interfaces
  - Switchover mechanism
- **Anti-Corruption Layer** design:
  - Translation boundaries
  - Data mapping between old and new models

## 3. Parallel Run Plan
- Shadow traffic configuration
- Dual-write strategy with reconciliation
- Comparison and verification tooling
- Divergence detection and alerting

## 4. Incremental Milestones
For each phase:
- Scope (what migrates)
- Duration estimate
- Success criteria
- Rollback procedure
- Dependencies and blockers

## 5. Data Migration
- Data mapping between legacy and target schemas
- ETL/CDC pipeline design
- Data validation and reconciliation approach
- Zero-downtime cutover strategy

## 6. Risk Assessment
- Migration risks ranked by impact and likelihood
- Rollback strategy for each milestone
- Feature flags for gradual rollout
- Communication plan for stakeholders

## 7. Timeline & Resource Estimate
- Phased timeline with dependencies
- Team allocation per phase
- Infrastructure requirements during transition
"""

        return await self.run_task(prompt)

    async def performance_baseline(
        self, system_description: str, slas: str
    ) -> TaskResult:
        """Create performance analysis framework with baselines and capacity model"""
        await self.notify(f"Building performance baseline for: {system_description[:50]}...")

        prompt = f"""
Create a performance engineering framework:

**System:** {system_description}
**SLA Requirements:** {slas}

**Provide:**

## 1. Performance Baseline
- Key performance metrics to capture (latency p50/p95/p99, throughput, error rate)
- Baseline measurement methodology
- Benchmark test suite design
- Historical trend analysis approach

## 2. Profiling Strategy
- **CPU Profiling**: Hot path identification, flame graph analysis
- **Memory Profiling**: Heap analysis, leak detection, GC tuning
- **I/O Profiling**: Disk I/O patterns, network I/O analysis
- **Database Profiling**: Query performance, connection pool sizing, index effectiveness
- Recommended tools per technology stack

## 3. Bottleneck Identification
- Amdahl's Law application to parallelizable components
- Queuing theory analysis (Little's Law) for service capacity
- Resource saturation points per component
- Critical path analysis through the system

## 4. Capacity Model
- Load model: expected traffic patterns (steady state, peak, burst)
- Resource requirements per request type
- Scaling curves: linear vs. sublinear scaling analysis
- Cost per unit of capacity

## 5. Load Testing Plan
- Test scenarios: smoke, load, stress, soak, spike
- Test data generation strategy
- Environment requirements for realistic testing
- Success criteria per test type

## 6. Optimization Recommendations
- Quick wins (caching, connection pooling, query optimization)
- Medium-term improvements (architecture changes, async processing)
- Long-term investments (re-architecture, technology migration)
- Priority matrix (impact vs effort)

## 7. SLA Mapping
- SLI definitions for each SLA target
- Error budget calculation
- Alerting thresholds and escalation procedures
- Capacity headroom requirements
"""

        return await self.run_task(prompt)

    async def design_ddd(self, domain_description: str) -> TaskResult:
        """Design Domain-Driven Design architecture with bounded contexts and aggregates"""
        await self.notify(f"Designing DDD for: {domain_description[:50]}...")

        prompt = f"""
Design a Domain-Driven Design architecture:

**Domain Description:** {domain_description}

**Provide:**

## 1. Domain Analysis
- Core domain identification (competitive advantage)
- Supporting domains
- Generic domains (buy/outsource candidates)
- Domain expert roles and ubiquitous language glossary

## 2. Bounded Contexts
For each bounded context:
- Name and responsibility
- Ubiquitous language terms specific to this context
- Team ownership
- Data ownership and storage strategy

## 3. Context Map
- Relationships between bounded contexts:
  - Partnership
  - Shared Kernel
  - Customer-Supplier
  - Conformist
  - Anti-Corruption Layer
  - Open Host Service / Published Language
- Diagram of context relationships

## 4. Aggregate Design
For each key aggregate:
- Aggregate root entity
- Value objects
- Invariants (business rules enforced)
- Consistency boundary
- Expected size and transaction scope

## 5. Domain Events
- Events that cross bounded context boundaries (integration events)
- Events within a bounded context (domain events)
- Event naming conventions (past tense, business language)
- Event schema with versioning strategy

## 6. Application Services & Use Cases
- Key use cases per bounded context
- Command/query separation
- Transaction boundaries
- Cross-context coordination (sagas, process managers)

## 7. Implementation Guidance
- Module/package structure per bounded context
- Repository pattern and persistence strategy
- Domain event publishing mechanism
- Testing strategy (unit, integration, contract tests)
"""

        return await self.run_task(prompt)

    async def cloud_native_review(self, application: str) -> TaskResult:
        """Perform cloud-native readiness review with 12-factor compliance and resilience assessment"""
        await self.notify(f"Cloud-native review for: {application[:50]}...")

        prompt = f"""
Perform a comprehensive cloud-native architecture review:

**Application:** {application}

**Provide:**

## 1. Twelve-Factor App Compliance
For each factor, assess current state and provide recommendations:
1. **Codebase** — One codebase tracked in VCS, many deploys
2. **Dependencies** — Explicitly declare and isolate dependencies
3. **Config** — Store config in the environment
4. **Backing Services** — Treat backing services as attached resources
5. **Build, Release, Run** — Strictly separate build and run stages
6. **Processes** — Execute the app as stateless processes
7. **Port Binding** — Export services via port binding
8. **Concurrency** — Scale out via the process model
9. **Disposability** — Maximize robustness with fast startup and graceful shutdown
10. **Dev/Prod Parity** — Keep development, staging, and production similar
11. **Logs** — Treat logs as event streams
12. **Admin Processes** — Run admin/management tasks as one-off processes

Compliance rating per factor: Compliant / Partially / Non-Compliant

## 2. Resilience Patterns Assessment
- **Circuit Breakers**: Implementation status, configuration, fallback strategies
- **Bulkheads**: Thread pool / connection pool isolation
- **Retry Patterns**: Exponential backoff, jitter, max retries, idempotency
- **Timeouts**: Connection, read, write timeouts per dependency
- **Rate Limiting**: Client-side and server-side rate limiting
- **Graceful Degradation**: Feature flag fallbacks, reduced functionality mode

## 3. Container & Orchestration Review
- Dockerfile best practices (multi-stage, non-root, minimal base)
- Resource limits and requests (CPU, memory)
- Health checks (liveness, readiness, startup probes)
- Pod disruption budgets and anti-affinity rules
- Horizontal Pod Autoscaler configuration

## 4. Observability Assessment
- Distributed tracing implementation
- Structured logging with correlation IDs
- Metrics exposure (Prometheus, OpenMetrics)
- Dashboard and alerting coverage
- SLI/SLO definitions

## 5. Security Posture
- Secrets management (Vault, sealed secrets, external secrets)
- Network policies and service mesh mTLS
- Image scanning and supply chain security
- RBAC and least-privilege access

## 6. Recommendations
- Priority-ordered action items
- Quick wins vs. strategic investments
- Migration path for non-compliant items
"""

        return await self.run_task(prompt)

    async def design_observability(
        self, services: str, requirements: str
    ) -> TaskResult:
        """Design comprehensive observability stack with tracing, logging, metrics, and SLO definitions"""
        await self.notify(f"Designing observability for: {services[:50]}...")

        prompt = f"""
Design a comprehensive observability architecture:

**Services:** {services}
**Requirements:** {requirements}

**Provide:**

## 1. OpenTelemetry Setup
- Instrumentation strategy: auto-instrumentation vs manual spans
- SDK configuration per language/framework
- Collector deployment topology (sidecar vs gateway vs agent)
- Sampling strategy (head-based, tail-based, adaptive)
- Resource attributes and semantic conventions

## 2. Distributed Tracing Design
- Trace context propagation (W3C TraceContext, B3)
- Span naming conventions and attribute standards
- Critical path tracing for key user journeys
- Trace-to-log and trace-to-metric correlation
- Backend selection (Jaeger, Tempo, X-Ray) with justification

## 3. Structured Logging Architecture
- Log format standard (JSON with required fields)
- Required fields: timestamp, level, service, traceId, spanId, correlationId
- Log levels policy (when to use each level)
- Log aggregation pipeline (Fluentd/Fluent Bit to Elasticsearch/Loki)
- Log retention and rotation policies
- Sensitive data redaction rules

## 4. Metrics Design
- **RED Method** (Rate, Errors, Duration) per service
- **USE Method** (Utilization, Saturation, Errors) per resource
- **Four Golden Signals** mapping
- Custom business metrics definition
- Metric naming conventions and label standards
- Cardinality management strategy
- Backend selection (Prometheus, Mimir, CloudWatch)

## 5. SLI/SLO Definitions
For each critical service:
- Service Level Indicators (SLIs) with measurement method
- Service Level Objectives (SLOs) with target percentages
- Error budget calculation and burn rate alerts
- SLA mapping (external commitments vs internal objectives)
- Rolling window configuration (30-day, 7-day)

## 6. Dashboard Design
- Executive overview dashboard (system health at a glance)
- Service-level dashboards (per-service deep dive)
- Infrastructure dashboards (node, pod, container metrics)
- Business metrics dashboards
- On-call dashboards with runbook links
- Grafana/Datadog layout recommendations

## 7. Alerting Strategy
- Alert hierarchy: page, ticket, log
- Alert routing rules and escalation paths
- Alert fatigue prevention (grouping, inhibition, silencing)
- Runbook template for each alert
- On-call rotation integration

## 8. Cost & Scaling
- Data volume estimation per signal type
- Storage and retention cost model
- Sampling trade-offs for cost optimization
- Scaling plan for observability infrastructure
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
    parser.add_argument("--event-arch", type=str, help="Design event-driven architecture for domain")
    parser.add_argument("--events", type=str, help="Key events for event architecture")
    parser.add_argument("--consumers", type=str, help="Event consumers")
    parser.add_argument("--migrate", type=str, help="Legacy system to migrate from")
    parser.add_argument("--target-arch", type=str, help="Target architecture for migration")
    parser.add_argument("--perf-baseline", type=str, help="System description for performance baseline")
    parser.add_argument("--slas", type=str, help="SLA requirements for performance baseline")
    parser.add_argument("--ddd", type=str, help="Domain description for DDD design")
    parser.add_argument("--cloud-review", type=str, help="Application for cloud-native review")
    parser.add_argument("--observability", type=str, help="Services for observability design")
    parser.add_argument("--obs-requirements", type=str, help="Observability requirements")
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

    if args.event_arch and args.events and args.consumers:
        result = await agent.design_event_architecture(
            args.event_arch, args.events, args.consumers
        )
        print(result.output)
        return

    if args.migrate and args.target_arch:
        result = await agent.plan_migration(args.migrate, args.target_arch)
        print(result.output)
        return

    if args.perf_baseline and args.slas:
        result = await agent.performance_baseline(args.perf_baseline, args.slas)
        print(result.output)
        return

    if args.ddd:
        result = await agent.design_ddd(args.ddd)
        print(result.output)
        return

    if args.cloud_review:
        result = await agent.cloud_native_review(args.cloud_review)
        print(result.output)
        return

    if args.observability and args.obs_requirements:
        result = await agent.design_observability(
            args.observability, args.obs_requirements
        )
        print(result.output)
        return

    if args.task:
        result = await agent.work(args.task)
        print(result.output)
        return

    print("Amber - Systems Architect")
    print("=========================")
    print("Use --help for options")
    print()
    print("Commands:")
    print("  --design <requirements>         Design system architecture")
    print("  --review <description>          Review architecture proposal")
    print("  --adr <title> --context --decision  Create ADR")
    print("  --api <resource> --operations   Design API contract")
    print("  --schema <requirements>         Design database schema")
    print("  --event-arch <domain> --events --consumers  Event-driven architecture")
    print("  --migrate <legacy> --target-arch <target>   Migration plan")
    print("  --perf-baseline <system> --slas <slas>      Performance baseline")
    print("  --ddd <domain>                  Domain-Driven Design")
    print("  --cloud-review <application>    Cloud-native review")
    print("  --observability <services> --obs-requirements <reqs>  Observability design")
    print("  --task <description>            General architecture task")


if __name__ == "__main__":
    asyncio.run(main())
