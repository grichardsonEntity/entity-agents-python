"""
Tango Agent - QA Tester

Expert in testing strategies, test automation, and quality assurance.
"""

import asyncio
from typing import Optional, List

from ..shared import BaseAgent, TaskResult
from .config import tango_config


class TangoAgent(BaseAgent):
    """
    Tango - QA Tester

    Specializes in:
    - Unit testing
    - Integration testing
    - E2E testing
    - Performance testing
    """

    def __init__(self, config=None):
        super().__init__(config or tango_config)

    async def write_tests(self, target: str, test_type: str = "unit") -> TaskResult:
        """Write tests for a target module/component"""
        await self.notify(f"Writing {test_type} tests for: {target}")

        prompt = f"""
Write {test_type} tests for: {target}

**First:**
1. Read and understand the code
2. Identify testable functions/methods
3. Find edge cases and error conditions

**Test Structure:**
```python
import pytest
from <module> import <target>

class Test<Target>:
    \"\"\"Tests for <target>.\"\"\"

    def test_<behavior>_<scenario>(self):
        \"\"\"Test that <expected behavior>.\"\"\"
        # Arrange
        <setup>

        # Act
        result = <action>

        # Assert
        assert result == <expected>
```

**Cover:**
1. Happy path (normal operation)
2. Edge cases (empty, null, boundary values)
3. Error cases (invalid input, exceptions)
4. Integration points (if integration test)

**Requirements:**
- Descriptive test names
- Clear docstrings
- Proper assertions with messages
- Use fixtures for common setup
- Mock external dependencies
"""

        return await self.run_task(prompt)

    async def run_tests(self, path: str = None, coverage: bool = True) -> TaskResult:
        """Run tests and report results"""
        await self.notify(f"Running tests: {path or 'all'}")

        prompt = f"""
Run tests{f" for {path}" if path else ""}:

**Commands:**
```bash
# Python
pytest {path or ""} {"--cov=src --cov-report=term-missing" if coverage else ""} -v

# JavaScript (if applicable)
npm run test{f" -- {path}" if path else ""}
```

**Report:**
1. Total tests run
2. Passed/Failed/Skipped counts
3. Coverage percentage (if enabled)
4. Failed test details
5. Recommendations for failing tests
"""

        return await self.run_task(prompt)

    async def analyze_coverage(self, path: str = None) -> TaskResult:
        """Analyze test coverage and identify gaps"""
        prompt = f"""
Analyze test coverage{f" for {path}" if path else ""}:

**Generate coverage:**
```bash
pytest --cov={path or "src"} --cov-report=html --cov-report=term-missing
```

**Analyze:**
1. Overall coverage percentage
2. Files with lowest coverage
3. Uncovered lines and branches
4. Critical paths without tests

**Recommendations:**
- Priority order for new tests
- Specific functions/methods needing coverage
- Test scaffolding for gaps
"""

        return await self.run_task(prompt)

    async def write_api_tests(self, endpoint: str, spec: str = None) -> TaskResult:
        """Write API endpoint tests"""
        await self.notify(f"Writing API tests for: {endpoint}")

        prompt = f"""
Write API tests for endpoint: {endpoint}

{f"Specification: {spec}" if spec else ""}

**Test cases:**

## Success Cases
- Valid request returns correct response
- All required fields present in response
- Correct status codes

## Authentication
- Unauthenticated request returns 401
- Invalid token returns 401/403
- Expired token handling

## Validation
- Missing required fields return 400
- Invalid field types return 400
- Out of range values

## Edge Cases
- Empty request body
- Large payloads
- Special characters
- Concurrent requests

**Test Pattern:**
```python
import pytest
from httpx import AsyncClient

@pytest.mark.asyncio
async def test_endpoint_success(client: AsyncClient):
    response = await client.post(
        "{endpoint}",
        json={{"field": "value"}}
    )
    assert response.status_code == 200
    data = response.json()
    assert "result" in data
```
"""

        return await self.run_task(prompt)

    async def performance_test(self, target: str, config: str = None) -> TaskResult:
        """Run performance tests"""
        await self.notify(f"Performance testing: {target}")

        prompt = f"""
Performance test: {target}

{f"Config: {config}" if config else ""}

**Metrics to capture:**
1. Response time (p50, p95, p99)
2. Throughput (requests/second)
3. Error rate under load
4. Resource usage (CPU, memory)

**Test scenarios:**
1. Baseline (single user)
2. Normal load (expected users)
3. Stress test (2x expected)
4. Spike test (sudden surge)

**Tools:**
```python
# locust example
from locust import HttpUser, task, between

class APIUser(HttpUser):
    wait_time = between(1, 3)

    @task
    def test_endpoint(self):
        self.client.get("{target}")
```

**Report:**
- Baseline metrics
- Performance under load
- Breaking point
- Recommendations
"""

        return await self.run_task(prompt)

    async def create_test_plan(self, feature: str) -> TaskResult:
        """Create comprehensive test plan"""
        prompt = f"""
Create test plan for feature: {feature}

## Test Plan: {feature}

### 1. Scope
- What's being tested
- What's out of scope
- Dependencies

### 2. Test Strategy
- Unit test coverage targets
- Integration test approach
- E2E test scenarios

### 3. Test Cases

#### Unit Tests
| ID | Description | Priority |
|----|-------------|----------|
| UT-01 | ... | High |

#### Integration Tests
| ID | Description | Priority |
|----|-------------|----------|
| IT-01 | ... | High |

#### E2E Tests
| ID | Description | Priority |
|----|-------------|----------|
| E2E-01 | ... | High |

### 4. Test Data
- Required fixtures
- Mock data
- Edge case data

### 5. Environment
- Test environment setup
- Dependencies
- CI/CD integration
"""

        return await self.run_task(prompt)

    async def work(self, task: str) -> TaskResult:
        """General QA work"""
        await self.notify(f"Starting: {task[:50]}...")
        return await self.run_task(task)


async def main():
    """CLI entry point"""
    import argparse
    import json

    parser = argparse.ArgumentParser(description="Tango - QA Tester Agent")
    parser.add_argument("--write", type=str, help="Write tests for target")
    parser.add_argument("--type", type=str, default="unit", help="Test type")
    parser.add_argument("--run", type=str, nargs="?", const="", help="Run tests")
    parser.add_argument("--coverage", type=str, nargs="?", const="", help="Analyze coverage")
    parser.add_argument("--api", type=str, help="Write API tests")
    parser.add_argument("--perf", type=str, help="Performance test")
    parser.add_argument("--plan", type=str, help="Create test plan")
    parser.add_argument("--task", type=str, help="Run general task")
    parser.add_argument("--status", action="store_true", help="Show status")

    args = parser.parse_args()

    agent = TangoAgent()

    if args.status:
        print(json.dumps(agent.get_status(), indent=2))
        return

    if args.write:
        result = await agent.write_tests(args.write, args.type)
        print(result.output)
        return

    if args.run is not None:
        result = await agent.run_tests(args.run if args.run else None)
        print(result.output)
        return

    if args.coverage is not None:
        result = await agent.analyze_coverage(args.coverage if args.coverage else None)
        print(result.output)
        return

    if args.api:
        result = await agent.write_api_tests(args.api)
        print(result.output)
        return

    if args.perf:
        result = await agent.performance_test(args.perf)
        print(result.output)
        return

    if args.plan:
        result = await agent.create_test_plan(args.plan)
        print(result.output)
        return

    if args.task:
        result = await agent.work(args.task)
        print(result.output)
        return

    print("Tango - QA Tester")
    print("=================")
    print("Use --help for options")


if __name__ == "__main__":
    asyncio.run(main())
