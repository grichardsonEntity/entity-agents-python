"""
Tango Agent - QA Tester

Expert in testing strategies, test automation, quality assurance,
security testing, accessibility auditing, and visual regression.
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
    - Security testing (OWASP)
    - Accessibility auditing (WCAG 2.1 AA)
    - Visual regression testing
    - Contract testing
    - CI/CD pipeline integration
    - Test data management
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

    async def security_test(self, target: str, test_type: str = "owasp") -> TaskResult:
        """Run security tests - OWASP, injection, auth bypass, secrets scanning"""
        await self.notify(f"Security testing ({test_type}): {target}")

        prompt = f"""
Run security tests on: {target}
Test type: {test_type}

## OWASP Top 10 Test Suite

### A01: Broken Access Control
- Test horizontal privilege escalation (access other users' data)
- Test vertical privilege escalation (access admin functions)
- Test IDOR (Insecure Direct Object References)
- Verify CORS configuration
- Test directory traversal

### A02: Cryptographic Failures
- Check for sensitive data in plaintext
- Verify TLS configuration
- Check password hashing algorithms
- Validate token generation entropy

### A03: Injection
- **SQL Injection**: parameterized query bypass attempts
- **XSS**: reflected, stored, DOM-based payloads
- **Command Injection**: shell metacharacter testing
- **LDAP Injection**: filter manipulation
- **NoSQL Injection**: MongoDB operator injection

```python
@pytest.mark.security
class TestInjection:
    SQL_PAYLOADS = [
        "' OR '1'='1", "'; DROP TABLE users;--",
        "1 UNION SELECT * FROM information_schema.tables",
        "admin'--", "1; EXEC xp_cmdshell('dir')"
    ]

    XSS_PAYLOADS = [
        '<script>alert(1)</script>',
        '<img src=x onerror=alert(1)>',
        'javascript:alert(1)',
        '{{{{constructor.constructor("alert(1)")()}}}}',
    ]

    def test_sql_injection(self, client, endpoint):
        for payload in self.SQL_PAYLOADS:
            response = client.get(f"{{endpoint}}?q={{payload}}")
            assert response.status_code != 500
            assert "error" not in response.text.lower() or "sql" not in response.text.lower()

    def test_xss(self, client, endpoint):
        for payload in self.XSS_PAYLOADS:
            response = client.post(endpoint, json={{"input": payload}})
            assert payload not in response.text
```

### A04: Insecure Design
- Test rate limiting on sensitive endpoints
- Verify account lockout mechanisms
- Test CAPTCHA effectiveness

### A05: Security Misconfiguration
- Check default credentials
- Verify security headers (CSP, HSTS, X-Frame-Options)
- Test error handling (no stack traces exposed)
- Check debug mode is disabled

### A07: Authentication Bypass
- Token manipulation (JWT algorithm confusion, signature stripping)
- Session fixation attacks
- Credential stuffing protection
- Password reset flow vulnerabilities

### Secrets Scanning
```bash
# Scan for hardcoded secrets
detect-secrets scan {target} --all-files
bandit -r {target} -ll
semgrep --config=p/secrets {target}
trivy fs {target} --security-checks secret
```

**Report:**
- Vulnerabilities found (severity: Critical/High/Medium/Low)
- OWASP category mapping
- Proof of concept for each finding
- Remediation recommendations
- Coordinate with BrettJr for pipeline integration
"""

        return await self.run_task(prompt)

    async def accessibility_audit(self, target: str, standard: str = "wcag-aa") -> TaskResult:
        """Run accessibility audit - WCAG compliance, keyboard nav, screen reader, color contrast"""
        await self.notify(f"Accessibility audit ({standard}): {target}")

        prompt = f"""
Run accessibility audit on: {target}
Standard: {standard}

## WCAG 2.1 AA Compliance Audit

### Automated Testing
```python
import pytest
from playwright.async_api import async_playwright

@pytest.mark.accessibility
async def test_wcag_compliance(page):
    await page.goto("{target}")

    # Inject and run axe-core
    await page.add_script_tag(url="https://cdnjs.cloudflare.com/ajax/libs/axe-core/4.7.0/axe.min.js")
    results = await page.evaluate("axe.run()")

    violations = results["violations"]
    critical = [v for v in violations if v["impact"] in ("critical", "serious")]
    assert len(critical) == 0, f"Critical a11y violations: {{critical}}"
```

```bash
# CLI audit tools
npx pa11y {target} --standard WCAG2AA --reporter json
npx lighthouse {target} --only-categories=accessibility --output=json
```

### Manual Checks

#### 1. Keyboard Navigation
- [ ] All interactive elements reachable via Tab key
- [ ] Logical tab order (left-to-right, top-to-bottom)
- [ ] Visible focus indicators on all focusable elements
- [ ] No keyboard traps (can Tab away from all elements)
- [ ] Skip links present for main content
- [ ] Custom keyboard shortcuts documented
- [ ] Escape key closes modals/popups
- [ ] Arrow keys work in custom widgets (menus, sliders, tabs)

#### 2. Screen Reader Compatibility
- [ ] All images have meaningful alt text (or alt="" for decorative)
- [ ] Form inputs have associated labels
- [ ] ARIA landmarks used (main, nav, banner, contentinfo)
- [ ] ARIA live regions for dynamic content updates
- [ ] Heading hierarchy is logical (h1 -> h2 -> h3, no skipping)
- [ ] Tables have proper headers (th, scope, caption)
- [ ] Custom widgets have correct ARIA roles and states
- [ ] Error messages announced to screen readers

#### 3. Color Contrast
- [ ] Normal text: minimum 4.5:1 contrast ratio
- [ ] Large text (18px+ or 14px+ bold): minimum 3:1 contrast ratio
- [ ] UI components and graphics: minimum 3:1 contrast ratio
- [ ] Focus indicators: minimum 3:1 contrast ratio
- [ ] Information not conveyed by color alone
- [ ] Links distinguishable from body text without color

#### 4. Responsive Accessibility
- [ ] Content reflows at 400% zoom without horizontal scrolling
- [ ] Touch targets minimum 44x44 CSS pixels
- [ ] Text resizable up to 200% without loss of functionality
- [ ] Orientation not locked (works portrait and landscape)

#### 5. Motion and Animation
- [ ] Respects prefers-reduced-motion media query
- [ ] No auto-playing content that lasts >5 seconds
- [ ] No content that flashes more than 3 times per second

**Report:**
- Total violations by impact (critical, serious, moderate, minor)
- WCAG success criteria mapping
- Screenshots of violations
- Remediation steps with code examples
- Coordinate with Sophie for mobile accessibility
"""

        return await self.run_task(prompt)

    async def visual_regression_test(self, target: str, baseline_path: str = None) -> TaskResult:
        """Run visual regression tests - screenshot comparison, layout validation, responsive breakpoints"""
        await self.notify(f"Visual regression testing: {target}")

        prompt = f"""
Run visual regression tests on: {target}
{f"Baseline path: {baseline_path}" if baseline_path else "Generate new baselines if none exist."}

## Visual Regression Test Suite

### Screenshot Capture
```python
import pytest
from playwright.async_api import async_playwright
from pathlib import Path
from PIL import Image, ImageChops

BREAKPOINTS = {{
    "mobile": 375,
    "tablet": 768,
    "desktop": 1280,
    "wide": 1920,
}}

BASELINE_DIR = Path("{baseline_path or 'tests/visual/baselines'}")
CURRENT_DIR = Path("tests/visual/current")
DIFF_DIR = Path("tests/visual/diffs")

@pytest.fixture
async def browser():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        yield browser
        await browser.close()

@pytest.mark.visual
class TestVisualRegression:

    @pytest.mark.parametrize("name,width", BREAKPOINTS.items())
    async def test_responsive_screenshot(self, browser, name, width):
        page = await browser.new_page(viewport={{"width": width, "height": 900}})
        await page.goto("{target}")
        await page.wait_for_load_state("networkidle")

        screenshot_path = CURRENT_DIR / f"{{name}}.png"
        await page.screenshot(path=str(screenshot_path), full_page=True)

        baseline = BASELINE_DIR / f"{{name}}.png"
        if baseline.exists():
            diff = self._compare_images(baseline, screenshot_path)
            assert diff < 0.01, f"Visual diff {{diff:.2%}} exceeds 1% threshold at {{name}}"

    def _compare_images(self, baseline_path, current_path):
        baseline = Image.open(baseline_path)
        current = Image.open(current_path)
        if baseline.size != current.size:
            return 1.0  # Size mismatch = 100% diff
        diff = ImageChops.difference(baseline, current)
        pixels = list(diff.getdata())
        total = len(pixels) * 255 * 3
        diff_sum = sum(sum(p) for p in pixels)
        return diff_sum / total
```

### Layout Validation
- Verify critical element positions have not shifted
- Check element dimensions against expected ranges
- Validate z-index stacking order
- Detect overflow and clipping issues

### Responsive Breakpoints
| Breakpoint | Width | Key Checks |
|------------|-------|------------|
| Mobile | 375px | Hamburger menu visible, single column, touch targets |
| Tablet | 768px | Sidebar collapses, grid adjusts, navigation adapts |
| Desktop | 1280px | Full layout, sidebar visible, multi-column |
| Wide | 1920px | Content max-width respected, no stretching |

### Cross-Browser Testing
- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)

### Workflow
1. Capture current screenshots at all breakpoints
2. Compare against baselines (if they exist)
3. Generate diff images highlighting changes
4. Report pixel-diff percentage per viewport
5. Update baselines when changes are intentional

**Report:**
- Pass/fail per breakpoint and browser
- Diff percentage and highlighted diff images
- Layout drift warnings
- Recommendations for responsive fixes
"""

        return await self.run_task(prompt)

    async def contract_test(self, api_spec: str, implementation: str) -> TaskResult:
        """Run contract tests - API contract verification, schema validation"""
        await self.notify(f"Contract testing: {api_spec} vs {implementation}")

        prompt = f"""
Run contract tests:
- API Spec: {api_spec}
- Implementation: {implementation}

## API Contract Verification

### OpenAPI Spec Validation
```python
import pytest
from openapi_spec_validator import validate_spec
import yaml
import json

def test_spec_is_valid():
    with open("{api_spec}") as f:
        spec = yaml.safe_load(f)
    validate_spec(spec)  # Raises if invalid

def test_endpoints_match_spec():
    \"\"\"Verify all spec endpoints are implemented.\"\"\"
    spec = load_spec("{api_spec}")
    routes = get_app_routes("{implementation}")

    for path, methods in spec["paths"].items():
        for method in methods:
            if method in ("get", "post", "put", "patch", "delete"):
                assert (path, method) in routes, f"Missing: {{method.upper()}} {{path}}"
```

### Schema Validation
```python
from jsonschema import validate

@pytest.mark.contract
class TestResponseSchemas:

    def test_response_matches_schema(self, client, endpoint, spec):
        response = client.get(endpoint)
        schema = spec["paths"][endpoint]["get"]["responses"]["200"]["content"]["application/json"]["schema"]
        validate(instance=response.json(), schema=schema)

    def test_request_validation(self, client, endpoint, spec):
        \"\"\"Send invalid request bodies and verify proper 400 responses.\"\"\"
        request_schema = spec["paths"][endpoint]["post"]["requestBody"]["content"]["application/json"]["schema"]
        invalid_payloads = generate_invalid_payloads(request_schema)
        for payload in invalid_payloads:
            response = client.post(endpoint, json=payload)
            assert response.status_code == 400
```

### Consumer-Driven Contracts (Pact)
```python
from pact import Consumer, Provider

@pytest.fixture
def pact():
    pact = Consumer("frontend").has_pact_with(
        Provider("api"),
        pact_dir="./pacts"
    )
    pact.start_service()
    yield pact
    pact.stop_service()
    pact.verify()

def test_get_user(pact):
    expected = {{"id": 1, "name": "Test User"}}
    pact.given("a user exists").upon_receiving(
        "a request for a user"
    ).with_request(
        "GET", "/api/users/1"
    ).will_respond_with(200, body=expected)

    with pact:
        result = get_user(pact.uri, 1)
        assert result == expected
```

### Breaking Change Detection
- Compare current spec against previous version
- Detect removed endpoints or methods
- Detect removed or renamed fields
- Detect type changes in request/response schemas
- Detect changed required field constraints

**Report:**
- Endpoints: implemented vs spec
- Schema validation results
- Breaking changes detected
- Missing or extra fields
- Type mismatches
- Coordinate with Sydney for backend API alignment
"""

        return await self.run_task(prompt)

    async def setup_ci_pipeline(self, project_path: str, test_types: List[str] = None) -> TaskResult:
        """Generate GitHub Actions workflow for test pipeline"""
        types = test_types or ["unit", "integration", "e2e"]
        await self.notify(f"Setting up CI pipeline for: {project_path} ({', '.join(types)})")

        prompt = f"""
Set up CI/CD test pipeline for: {project_path}
Test types to include: {', '.join(types)}

## GitHub Actions Test Pipeline

Generate a `.github/workflows/test.yml` with the following stages:

### Pipeline Stages
```yaml
name: Test Pipeline

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

concurrency:
  group: tests-${{{{ github.ref }}}}
  cancel-in-progress: true

jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.12'
          cache: 'pip'
      - run: pip install ruff
      - run: ruff check .

  unit-tests:
    needs: lint
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: ['3.11', '3.12']
        shard: [1, 2, 3, 4]
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: ${{{{ matrix.python-version }}}}
          cache: 'pip'
      - run: pip install -r requirements-test.txt
      - name: Run unit tests (shard ${{{{ matrix.shard }}}}/4)
        run: |
          pytest tests/unit/ \\
            --splits 4 --group ${{{{ matrix.shard }}}} \\
            --cov=src --cov-report=xml \\
            --junitxml=results-${{{{ matrix.shard }}}}.xml
      - uses: actions/upload-artifact@v4
        with:
          name: coverage-${{{{ matrix.shard }}}}
          path: coverage.xml

  integration-tests:
    needs: unit-tests
    runs-on: ubuntu-latest
    services:
      postgres:
        image: postgres:16
        env:
          POSTGRES_PASSWORD: test
        ports: ['5432:5432']
      redis:
        image: redis:7
        ports: ['6379:6379']
    steps:
      - uses: actions/checkout@v4
      - run: pytest tests/integration/ -m integration --timeout=60

  e2e-tests:
    needs: integration-tests
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: npx playwright install --with-deps
      - run: pytest tests/e2e/ --timeout=120 --retries=2

  security-tests:
    needs: lint
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: pip install bandit semgrep
      - run: bandit -r src/ -ll -f json -o bandit-report.json
      - run: semgrep --config=p/python --config=p/secrets src/

  accessibility-tests:
    needs: e2e-tests
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: npx pa11y-ci --config .pa11yci.json

  coverage-report:
    needs: [unit-tests, integration-tests]
    runs-on: ubuntu-latest
    steps:
      - uses: actions/download-artifact@v4
      - name: Merge and report coverage
        run: |
          pip install coverage
          coverage combine coverage-*/coverage.xml
          coverage report --fail-under=75
```

### Caching Strategy
- Cache pip/npm dependencies between runs
- Cache Playwright browsers
- Cache Docker layers for service containers
- Use build artifacts for cross-job data

### Test Parallelization
- Split unit tests across 4 shards using pytest-split
- Run independent jobs concurrently (lint + security in parallel)
- Use matrix strategy for multi-version testing

### Failure Handling
- Retry flaky E2E tests (max 2 retries)
- Upload test artifacts on failure
- Post failure summary to PR comments

**Output:**
- Complete workflow YAML file
- .pa11yci.json configuration
- pytest-split configuration
- README section for CI setup
"""

        return await self.run_task(prompt)

    async def generate_test_data(self, schema: str, count: int = 100) -> TaskResult:
        """Generate test data with factories and realistic fake data"""
        await self.notify(f"Generating {count} test data records for: {schema}")

        prompt = f"""
Generate test data for schema: {schema}
Count: {count}

## Test Data Generation

### Factory Pattern (factory_boy)
```python
import factory
from faker import Faker
from datetime import datetime, timedelta

fake = Faker()

class UserFactory(factory.Factory):
    class Meta:
        model = dict

    id = factory.Sequence(lambda n: n + 1)
    email = factory.LazyFunction(lambda: fake.unique.email())
    name = factory.LazyFunction(fake.name)
    created_at = factory.LazyFunction(datetime.utcnow)
    is_active = True

    class Params:
        inactive = factory.Trait(
            is_active=False,
            deactivated_at=factory.LazyFunction(datetime.utcnow)
        )
        admin = factory.Trait(
            role="admin",
            permissions=["read", "write", "delete", "admin"]
        )

# Generate test data
users = UserFactory.build_batch({count})
inactive_users = UserFactory.build_batch(10, inactive=True)
admin_users = UserFactory.build_batch(3, admin=True)
```

### Fixture Strategies
```python
import pytest

@pytest.fixture(scope="session")
def seed_database(db_session):
    \"\"\"Seed database with baseline test data.\"\"\"
    users = UserFactory.create_batch(50)
    orders = [OrderFactory.create(user=u) for u in users[:20]]
    db_session.commit()
    yield {{"users": users, "orders": orders}}
    # Cleanup
    db_session.rollback()

@pytest.fixture(autouse=True)
def clean_between_tests(db_session):
    \"\"\"Transaction rollback between tests.\"\"\"
    db_session.begin_nested()
    yield
    db_session.rollback()
```

### Realistic Data Patterns
Based on the schema: {schema}

Generate:
1. **Valid records** - {count} records matching all constraints
2. **Edge case records** - Boundary values, max lengths, unicode, special chars
3. **Invalid records** - For negative testing (missing required fields, wrong types)
4. **Relationships** - Properly linked related records

### Cleanup Strategies
- **Transaction rollback** - Wrap each test in a transaction, rollback after
- **Truncation** - TRUNCATE tables between test suites
- **Isolated databases** - Per-test or per-suite database instances
- **Factory cleanup** - Track and delete factory-created records

### Sensitive Data Handling
- Use Faker for realistic but synthetic PII
- Never use real customer data in tests
- Anonymize production data snapshots
- Mask credit cards, SSNs, passwords

**Output:**
- Factory definitions for all schema entities
- Fixture files with proper scoping
- Seed script for database population
- Cleanup hooks for test isolation
- Edge case data sets for boundary testing
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
    parser.add_argument("--security", type=str, help="Run security tests on target")
    parser.add_argument("--security-type", type=str, default="owasp", help="Security test type (owasp, injection, auth, secrets)")
    parser.add_argument("--a11y", type=str, help="Run accessibility audit on target")
    parser.add_argument("--a11y-standard", type=str, default="wcag-aa", help="Accessibility standard (wcag-aa, wcag-aaa)")
    parser.add_argument("--visual", type=str, help="Run visual regression tests")
    parser.add_argument("--baseline", type=str, help="Baseline path for visual regression")
    parser.add_argument("--contract", type=str, nargs=2, metavar=("SPEC", "IMPL"), help="Run contract tests (spec implementation)")
    parser.add_argument("--ci", type=str, help="Set up CI pipeline for project path")
    parser.add_argument("--ci-types", type=str, nargs="+", default=["unit", "integration", "e2e"], help="Test types for CI pipeline")
    parser.add_argument("--generate-data", type=str, help="Generate test data for schema")
    parser.add_argument("--count", type=int, default=100, help="Number of test data records to generate")
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

    if args.security:
        result = await agent.security_test(args.security, args.security_type)
        print(result.output)
        return

    if args.a11y:
        result = await agent.accessibility_audit(args.a11y, args.a11y_standard)
        print(result.output)
        return

    if args.visual:
        result = await agent.visual_regression_test(args.visual, args.baseline)
        print(result.output)
        return

    if args.contract:
        result = await agent.contract_test(args.contract[0], args.contract[1])
        print(result.output)
        return

    if args.ci:
        result = await agent.setup_ci_pipeline(args.ci, args.ci_types)
        print(result.output)
        return

    if args.generate_data:
        result = await agent.generate_test_data(args.generate_data, args.count)
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
