"""
Sydney Agent - Full Stack Developer

Expert in Python, FastAPI, Node.js, databases, React, CSS, and API design.
Combines backend and frontend expertise for complete feature development.
"""

import asyncio
from typing import Optional, List

from ..shared import BaseAgent, TaskResult
from .config import sydney_config


class SydneyAgent(BaseAgent):
    """
    Sydney - Full Stack Developer

    Specializes in:
    - Python/FastAPI backend services
    - Node.js/Express APIs
    - Database design and optimization
    - Docker containerization
    - React components and hooks
    - Flask/Jinja2 templates
    - CSS and design systems
    - Accessibility and responsive design
    """

    def __init__(self, config=None):
        super().__init__(config or sydney_config)

    # ==================== BACKEND METHODS ====================

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
2. Add proper request/response validation with Pydantic
3. Include comprehensive error handling
4. Add OpenAPI documentation
5. Write a basic test for the endpoint

**Before delivering, verify:**
- [ ] Request validation is complete
- [ ] Response model matches spec
- [ ] Error cases are handled
- [ ] OpenAPI docs are accurate
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

**Before delivering, verify:**
- [ ] Health endpoint works
- [ ] Environment variables are documented
- [ ] Dockerfile builds successfully
- [ ] Service starts without errors
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

**Before delivering, verify:**
- [ ] Query execution plan improved
- [ ] No N+1 query issues
- [ ] Indexes are appropriate
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

**Before delivering, verify:**
- [ ] Up migration works
- [ ] Down migration reverses changes
- [ ] Models match schema
"""

        return await self.run_task(prompt)

    async def design_schema(self, entities: str, relationships: str = None) -> TaskResult:
        """Design database schema"""
        await self.notify(f"Designing schema for: {entities[:50]}")

        prompt = f"""
Design database schema:

**Entities:** {entities}
{f"**Relationships:** {relationships}" if relationships else ""}

**Deliverables:**

## 1. Entity-Relationship Diagram

```mermaid
erDiagram
    [entities and relationships]
```

## 2. SQLAlchemy Models

```python
# models.py
[Complete model definitions with relationships]
```

## 3. Pydantic Schemas

```python
# schemas.py
[Request/response schemas]
```

## 4. Migration

```python
# alembic migration
[Migration script]
```

**Before delivering, verify:**
- [ ] All relationships are defined
- [ ] Indexes are appropriate
- [ ] Cascades are correct
- [ ] Models have proper types
"""

        return await self.run_task(prompt)

    # ==================== FRONTEND METHODS ====================

    async def create_component(self, name: str, description: str) -> TaskResult:
        """Create a new UI component"""
        await self.notify(f"Creating component: {name}")

        prompt = f"""
Create a new UI component:

**Component Name:** {name}
**Description:** {description}

**Requirements:**
1. Create the component with proper structure
2. Include CSS/styling (CSS Modules preferred)
3. Add TypeScript types (if React) or proper Jinja2 macros (if Flask)
4. Follow the project's design system
5. Include accessibility features (ARIA labels, keyboard navigation)
6. Support dark/light themes if applicable
7. Add JSDoc/docstring comments

**Before delivering, verify:**
- [ ] Component renders correctly
- [ ] Accessibility is complete (ARIA, focus states)
- [ ] Responsive design works
- [ ] Dark/light themes work (if applicable)
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

**Before delivering, verify:**
- [ ] ARIA labels are complete
- [ ] Keyboard navigation works
- [ ] Focus states are visible
- [ ] Color contrast passes WCAG AA
"""

        return await self.run_task(prompt)

    async def fix_ui_bug(self, issue_number: int) -> TaskResult:
        """Fix a UI bug from GitHub"""
        if not self.github:
            return TaskResult(success=False, output="GitHub not configured")

        issue = self.github.get_issue(issue_number)
        if not issue:
            return TaskResult(success=False, output=f"Issue #{issue_number} not found")

        await self.notify(f"Working on UI: {issue.title}")

        self.github.add_label(issue_number, "in-progress")
        self.github.add_comment(issue_number, "🎨 Sydney is investigating this UI issue...")

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

**Before delivering, verify:**
- [ ] Bug is fixed
- [ ] No regression in related components
- [ ] Accessibility maintained
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
                f"Sydney has implemented a fix.\n\n"
                f"**Commit:** {commit.get('hash', 'See git log')}\n"
                f"**Files Changed:** {', '.join(commit.get('files', []))}\n\n"
                f"Please verify and close if resolved."
            )

        return result

    # ==================== FULL-STACK METHODS ====================

    async def create_feature(
        self,
        name: str,
        description: str,
        include_api: bool = True,
        include_ui: bool = True
    ) -> TaskResult:
        """Create a complete feature with API and UI"""
        await self.notify(f"Creating feature: {name}")

        prompt = f"""
Create a complete feature:

**Feature Name:** {name}
**Description:** {description}
**Include API:** {include_api}
**Include UI:** {include_ui}

{"## 1. API Design" if include_api else ""}
{'''
**Endpoint(s):**
- Design RESTful endpoints for this feature
- Define request/response schemas
- Include proper validation
- Add OpenAPI documentation
''' if include_api else ""}

{"## 2. Database (if needed)" if include_api else ""}
{'''
- Design any required schema changes
- Create migration if needed
- Define models
''' if include_api else ""}

{"## 3. UI Components" if include_ui else ""}
{'''
**Components:**
- Design component hierarchy
- Implement with proper styling
- Add accessibility features
- Include loading/error states
''' if include_ui else ""}

{"## 4. Integration" if include_api and include_ui else ""}
{'''
- Connect UI to API
- Handle API errors gracefully
- Add loading states
- Test complete flow
''' if include_api and include_ui else ""}

**Before delivering, verify:**
- [ ] API endpoints work correctly
- [ ] UI components render properly
- [ ] Integration is complete
- [ ] Error handling works
- [ ] Accessibility is complete
"""

        return await self.run_task(prompt)

    async def create_crud_feature(
        self,
        entity_name: str,
        fields: str,
        include_ui: bool = True
    ) -> TaskResult:
        """Create a complete CRUD feature with API and optional UI"""
        await self.notify(f"Creating CRUD for: {entity_name}")

        prompt = f"""
Create complete CRUD functionality for:

**Entity:** {entity_name}
**Fields:** {fields}
**Include UI:** {include_ui}

## 1. Database Model

```python
# SQLAlchemy model with proper types and relationships
```

## 2. Pydantic Schemas

```python
# Create, Update, Response schemas
```

## 3. API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| GET | /{entity_name}s | List all |
| GET | /{entity_name}s/{{id}} | Get one |
| POST | /{entity_name}s | Create |
| PUT | /{entity_name}s/{{id}} | Update |
| DELETE | /{entity_name}s/{{id}} | Delete |

Implement all endpoints with:
- Proper validation
- Error handling
- Pagination for list
- OpenAPI docs

{"## 4. UI Components" if include_ui else ""}
{f'''
- List view with pagination
- Detail view
- Create/Edit form
- Delete confirmation
- Loading and error states
''' if include_ui else ""}

**Before delivering, verify:**
- [ ] All CRUD operations work
- [ ] Validation is complete
- [ ] Error handling is comprehensive
- [ ] UI is accessible (if included)
"""

        return await self.run_task(prompt)

    async def fix_bug(self, issue_number: int) -> TaskResult:
        """Fix a bug (determines if backend or frontend)"""
        if not self.github:
            return TaskResult(success=False, output="GitHub not configured")

        issue = self.github.get_issue(issue_number)
        if not issue:
            return TaskResult(success=False, output=f"Issue #{issue_number} not found")

        await self.notify(f"Working on: {issue.title}")

        self.github.add_label(issue_number, "in-progress")
        self.github.add_comment(issue_number, "⚙️ Sydney is investigating this issue...")

        prompt = f"""
Fix this bug:

**Issue #{issue.number}:** {issue.title}

**Description:**
{issue.body}

**Instructions:**
1. Analyze if this is a backend, frontend, or full-stack issue
2. Read the relevant files
3. Identify the root cause
4. Implement the fix
5. Add/update tests
6. DO NOT break existing functionality

**Before delivering, verify:**
- [ ] Root cause identified
- [ ] Fix is minimal and focused
- [ ] Tests pass
- [ ] No regressions
"""

        result = await self.run_task(prompt)

        if result.success:
            # Determine commit prefix based on files changed
            prefix = "fix"
            commit = await self.commit_changes(
                f"{prefix}: {issue.title[:50]}",
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

    # ==================== GRAPHQL METHODS ====================

    async def create_graphql_schema(
        self,
        entities: str,
        relationships: str = None
    ) -> TaskResult:
        """Create a GraphQL schema with types, queries, mutations, subscriptions, and DataLoader"""
        await self.notify(f"Creating GraphQL schema for: {entities[:50]}")

        prompt = f"""
Create a complete GraphQL schema:

**Entities:** {entities}
{f"**Relationships:** {relationships}" if relationships else ""}

## Deliverables

### 1. Schema Types
- Define GraphQL types for each entity
- Add input types for create/update mutations
- Include connection types for cursor-based pagination (Relay spec)
- Define enums, interfaces, and unions where appropriate

### 2. Queries
- Single entity lookup by ID
- Paginated list queries with cursor-based pagination
- Filter and sort arguments
- Use DataLoader for batched/cached field resolution

### 3. Mutations
- Create, update, delete for each entity
- Input validation with clear error messages
- Return the mutated entity

### 4. Subscriptions
- Real-time updates for entity changes (created, updated, deleted)
- PubSub pattern with proper topic naming
- Filter subscriptions by relevant criteria

### 5. DataLoader Setup
```python
from strawberry.dataloader import DataLoader

async def load_users(keys: list[int]) -> list[User]:
    users = await db.users.filter(id__in=keys)
    user_map = {{u.id: u for u in users}}
    return [user_map.get(k) for k in keys]

user_loader = DataLoader(load_fn=load_users)
```

### 6. Federation (if multi-service)
- Entity references with @key directive
- Extend types across subgraphs
- Gateway composition strategy

**Before delivering, verify:**
- [ ] All types are properly defined
- [ ] Pagination follows cursor-based spec
- [ ] DataLoader eliminates N+1 queries
- [ ] Subscriptions have proper PubSub setup
- [ ] Input validation is comprehensive
- [ ] Schema compiles without errors
"""

        return await self.run_task(prompt)

    # ==================== CACHING METHODS ====================

    async def setup_caching(
        self,
        service: str,
        cache_strategy: str = "cache-aside"
    ) -> TaskResult:
        """Set up Redis caching layer with TTL, invalidation, and configurable strategy"""
        await self.notify(f"Setting up {cache_strategy} caching for: {service}")

        prompt = f"""
Set up a caching layer for service: {service}

**Cache Strategy:** {cache_strategy}

## Deliverables

### 1. Redis Cache Service
```python
class CacheService:
    # Implement {cache_strategy} pattern
    # - cache-aside: Read from cache first, fetch from DB on miss, populate cache
    # - write-through: Write to cache and DB simultaneously
    # - write-behind: Write to cache immediately, async write to DB
```

### 2. TTL Strategy
- Define per-entity TTL values based on data volatility
- Implement sliding expiration for frequently accessed data
- Add stale-while-revalidate for improved latency

### 3. Cache Invalidation
- Tag-based invalidation (invalidate all caches related to an entity)
- Event-driven invalidation on writes/updates/deletes
- Pattern-based key cleanup
- Versioned cache keys for safe deployments

### 4. HTTP Caching Headers
- Set Cache-Control, ETag, Last-Modified on API responses
- Implement conditional requests (If-None-Match, If-Modified-Since)
- Configure CDN-friendly headers (Surrogate-Control, Surrogate-Key)

### 5. Cache Decorator
```python
def cached(ttl: int = 300, tags: list[str] = None):
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            key = generate_cache_key(func, args, kwargs)
            return await cache_service.cache_aside(key, lambda: func(*args, **kwargs), ttl=ttl)
        return wrapper
    return decorator
```

### 6. Monitoring
- Cache hit/miss ratio metrics
- Latency tracking for cache vs DB reads
- Memory usage monitoring
- Alert on high miss rates

**Before delivering, verify:**
- [ ] Cache strategy correctly implemented
- [ ] TTL values are appropriate for data type
- [ ] Invalidation covers all write paths
- [ ] No stale data scenarios unhandled
- [ ] HTTP caching headers are correct
- [ ] Monitoring is in place
"""

        return await self.run_task(prompt)

    # ==================== WEBSOCKET METHODS ====================

    async def create_websocket_endpoint(
        self,
        path: str,
        description: str
    ) -> TaskResult:
        """Create a WebSocket endpoint with connection management, heartbeats, and reconnection"""
        await self.notify(f"Creating WebSocket endpoint: {path}")

        prompt = f"""
Create a WebSocket endpoint:

**Path:** {path}
**Description:** {description}

## Deliverables

### 1. Connection Manager
```python
class ConnectionManager:
    def __init__(self):
        self.active_connections: dict[str, WebSocket] = {{}}
        self.rooms: dict[str, set[str]] = {{}}

    async def connect(self, websocket: WebSocket, client_id: str):
        await websocket.accept()
        self.active_connections[client_id] = websocket

    async def disconnect(self, client_id: str):
        self.active_connections.pop(client_id, None)
        # Clean up room memberships

    async def broadcast(self, message: dict, room: str = None):
        # Send to all or room members

    async def send_personal(self, client_id: str, message: dict):
        # Send to specific client
```

### 2. WebSocket Endpoint
- Accept connections with authentication
- Parse message types (JSON protocol)
- Route messages to appropriate handlers
- Handle disconnections gracefully

### 3. Heartbeat / Keep-Alive
- Server-initiated ping every 30 seconds
- Client pong response handling
- Disconnect stale connections after 3 missed pongs
- Configurable heartbeat interval

### 4. Message Protocol
```python
class WSMessage(BaseModel):
    type: str  # "subscribe", "unsubscribe", "message", "ping", "pong"
    channel: Optional[str] = None
    payload: Optional[dict] = None
    id: Optional[str] = None  # For request-response correlation
```

### 5. Reconnection Support
- Send connection state on reconnect
- Message queue for offline clients (brief window)
- Last-event-id support for resuming streams
- Exponential backoff guidance for clients

### 6. Scaling Considerations
- Redis Pub/Sub for multi-instance message distribution
- Sticky sessions configuration notes
- Connection count limits and backpressure

**Before delivering, verify:**
- [ ] Connection lifecycle is complete (connect, message, disconnect)
- [ ] Heartbeat keeps connections alive
- [ ] Authentication is enforced
- [ ] Message protocol is well-defined
- [ ] Reconnection is supported
- [ ] Error handling covers all edge cases
"""

        return await self.run_task(prompt)

    # ==================== BACKGROUND JOBS METHODS ====================

    async def setup_background_jobs(
        self,
        job_descriptions: str
    ) -> TaskResult:
        """Set up task queue with retries, DLQ, scheduling, and monitoring"""
        await self.notify(f"Setting up background jobs: {job_descriptions[:50]}")

        prompt = f"""
Set up background job processing:

**Jobs Required:** {job_descriptions}

## Deliverables

### 1. Task Queue Configuration
```python
# Celery configuration (Python)
app = Celery('tasks')
app.config_from_object({{
    'broker_url': 'redis://localhost:6379/0',
    'result_backend': 'redis://localhost:6379/1',
    'task_serializer': 'json',
    'result_serializer': 'json',
    'accept_content': ['json'],
    'task_track_started': True,
    'task_acks_late': True,
    'worker_prefetch_multiplier': 1,
}})
```

### 2. Job Definitions
- Define each job/task with clear input/output types
- Set appropriate timeouts per job type
- Configure concurrency limits where needed

### 3. Retry Strategy
- Exponential backoff: retry_delay * 2^attempt
- Max retries per job type (default: 3)
- Configurable retry exceptions (transient vs permanent)
- Dead letter queue for permanently failed jobs

### 4. Dead Letter Queue (DLQ)
```python
@app.task
def handle_dead_letter(original_task, args, kwargs, exc_info):
    # Log failure details
    # Send alert notification
    # Store for manual review/replay
```

### 5. Scheduling
- Periodic tasks via celery-beat or BullMQ repeatable jobs
- Cron expressions for complex schedules
- One-off delayed jobs with ETA

### 6. Monitoring & Observability
- Job status dashboard (Flower / Bull Board)
- Metrics: queue depth, processing time, failure rate
- Alerts on: DLQ growth, queue backlog, worker crashes
- Structured logging for job execution

### 7. Worker Configuration
- Worker pools and concurrency settings
- Priority queues for different job types
- Graceful shutdown handling

**Before delivering, verify:**
- [ ] All jobs are defined with proper types
- [ ] Retry logic handles transient failures
- [ ] DLQ captures permanent failures
- [ ] Scheduling is configured correctly
- [ ] Monitoring dashboard is set up
- [ ] Workers handle graceful shutdown
"""

        return await self.run_task(prompt)

    # ==================== API VERSIONING METHODS ====================

    async def create_api_version(
        self,
        current_version: str,
        changes: str
    ) -> TaskResult:
        """Create API versioning strategy with migration plan and deprecation notices"""
        await self.notify(f"Creating API version plan: {current_version} -> next")

        prompt = f"""
Create an API versioning strategy:

**Current Version:** {current_version}
**Planned Changes:** {changes}

## Deliverables

### 1. Version Strategy
- Determine versioning approach (URL path /api/v2/, header, or content negotiation)
- Define version routing middleware
- Set up version-specific route registration

### 2. New Version Implementation
```python
# URL versioning example
from fastapi import APIRouter

v1_router = APIRouter(prefix="/api/v1")
v2_router = APIRouter(prefix="/api/v2")

# Shared business logic
# Version-specific request/response adapters
```

### 3. Migration Plan
| Endpoint | v{current_version} (Current) | Next Version (Changes) | Breaking? |
|----------|------|------|----------|
| [List affected endpoints with changes] |

### 4. Deprecation Strategy
- Add Sunset header to deprecated endpoints
- Add Deprecation header with date
- Include Link header pointing to new version docs
- Log usage of deprecated endpoints for tracking

```python
@app.middleware("http")
async def deprecation_headers(request, call_next):
    response = await call_next(request)
    if request.url.path.startswith("/api/v1"):
        response.headers["Deprecation"] = "true"
        response.headers["Sunset"] = "2025-06-01T00:00:00Z"
        response.headers["Link"] = '</api/v2/docs>; rel="successor-version"'
    return response
```

### 5. Client Communication
- Changelog document for the new version
- Migration guide with before/after examples
- SDK/client library update notes
- Timeline: deprecation announcement -> warning period -> sunset

### 6. Coexistence Plan
- Both versions run simultaneously during transition
- Shared service/business logic layer
- Version-specific adapters for request/response transformation
- Database compatibility across versions

**Before delivering, verify:**
- [ ] Version routing works correctly
- [ ] Deprecation headers are set on old version
- [ ] Migration guide covers all breaking changes
- [ ] Both versions can coexist
- [ ] Client communication is clear
- [ ] Sunset timeline is defined
"""

        return await self.run_task(prompt)

    # ==================== GENERAL ====================

    async def work(self, task: str) -> TaskResult:
        """General full-stack work"""
        await self.notify(f"Starting: {task[:50]}...")
        return await self.run_task(task)


async def main():
    """CLI entry point"""
    import argparse
    import json

    parser = argparse.ArgumentParser(description="Sydney - Full Stack Developer Agent")

    # Backend arguments
    parser.add_argument("--endpoint", nargs=2, metavar=("METHOD", "PATH"), help="Create endpoint")
    parser.add_argument("--description", type=str, help="Description for endpoint/service/component")
    parser.add_argument("--service", type=str, help="Create microservice")
    parser.add_argument("--optimize", type=str, help="Optimize query at location")
    parser.add_argument("--migration", type=str, help="Create migration")
    parser.add_argument("--schema", type=str, help="Design schema for entities")

    # Frontend arguments
    parser.add_argument("--component", type=str, help="Create UI component")
    parser.add_argument("--a11y", type=str, help="Improve accessibility for path")
    parser.add_argument("--fix-ui", type=int, help="Fix UI issue by number")

    # Full-stack arguments
    parser.add_argument("--feature", type=str, help="Create complete feature")
    parser.add_argument("--crud", type=str, help="Create CRUD for entity")
    parser.add_argument("--fields", type=str, help="Fields for CRUD entity")
    parser.add_argument("--no-ui", action="store_true", help="Skip UI for feature/crud")

    # GraphQL arguments
    parser.add_argument("--graphql", type=str, help="Create GraphQL schema for entities")
    parser.add_argument("--relationships", type=str, help="Relationships for GraphQL schema")

    # Caching arguments
    parser.add_argument("--cache", type=str, help="Set up caching for service")
    parser.add_argument("--cache-strategy", type=str, default="cache-aside",
                        choices=["cache-aside", "write-through", "write-behind"],
                        help="Caching strategy (default: cache-aside)")

    # WebSocket arguments
    parser.add_argument("--websocket", type=str, help="Create WebSocket endpoint at path")
    parser.add_argument("--ws-description", type=str, help="Description for WebSocket endpoint")

    # Background jobs arguments
    parser.add_argument("--jobs", type=str, help="Set up background jobs (describe jobs)")

    # API versioning arguments
    parser.add_argument("--api-version", type=str, help="Current API version to create new version from")
    parser.add_argument("--version-changes", type=str, help="Planned changes for new API version")

    # General
    parser.add_argument("--fix", type=int, help="Fix issue by number")
    parser.add_argument("--task", type=str, help="Run general task")
    parser.add_argument("--status", action="store_true", help="Show status")

    args = parser.parse_args()

    agent = SydneyAgent()

    if args.status:
        print(json.dumps(agent.get_status(), indent=2))
        return

    # Backend operations
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

    if args.schema:
        result = await agent.design_schema(args.schema)
        print(result.output)
        return

    # Frontend operations
    if args.component and args.description:
        result = await agent.create_component(args.component, args.description)
        print(result.output)
        return

    if args.a11y:
        result = await agent.improve_accessibility(args.a11y)
        print(result.output)
        return

    if args.fix_ui:
        result = await agent.fix_ui_bug(args.fix_ui)
        print(result.output)
        return

    # Full-stack operations
    if args.feature and args.description:
        result = await agent.create_feature(
            args.feature,
            args.description,
            include_ui=not args.no_ui
        )
        print(result.output)
        return

    if args.crud and args.fields:
        result = await agent.create_crud_feature(
            args.crud,
            args.fields,
            include_ui=not args.no_ui
        )
        print(result.output)
        return

    # GraphQL operations
    if args.graphql:
        result = await agent.create_graphql_schema(args.graphql, args.relationships)
        print(result.output)
        return

    # Caching operations
    if args.cache:
        result = await agent.setup_caching(args.cache, args.cache_strategy)
        print(result.output)
        return

    # WebSocket operations
    if args.websocket and args.ws_description:
        result = await agent.create_websocket_endpoint(args.websocket, args.ws_description)
        print(result.output)
        return

    # Background jobs operations
    if args.jobs:
        result = await agent.setup_background_jobs(args.jobs)
        print(result.output)
        return

    # API versioning operations
    if args.api_version and args.version_changes:
        result = await agent.create_api_version(args.api_version, args.version_changes)
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

    print("Sydney - Full Stack Developer")
    print("==============================")
    print("Use --help for options")


if __name__ == "__main__":
    asyncio.run(main())
