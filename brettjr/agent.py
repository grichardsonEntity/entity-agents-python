"""
Brett Jr Agent - Cybersecurity Specialist

Expert in security audits, authentication, and encryption.
"""

import asyncio
from typing import Optional, List

from ..shared import BaseAgent, TaskResult
from .config import brettjr_config


class BrettJrAgent(BaseAgent):
    """
    Brett Jr - Cybersecurity Specialist

    Specializes in:
    - Security audits
    - Authentication/authorization
    - Encryption and key management
    - Container and network security
    """

    def __init__(self, config=None):
        super().__init__(config or brettjr_config)

    async def security_audit(self, target: str) -> TaskResult:
        """Run comprehensive security audit"""
        await self.notify(f"Security audit: {target}")

        prompt = f"""
Perform security audit on: {target}

**Check for OWASP Top 10:**
1. Injection (SQL, Command, XSS)
2. Broken Authentication
3. Sensitive Data Exposure
4. XML External Entities (XXE)
5. Broken Access Control
6. Security Misconfiguration
7. Cross-Site Scripting (XSS)
8. Insecure Deserialization
9. Using Components with Known Vulnerabilities
10. Insufficient Logging & Monitoring

**Additional Checks:**
- Hardcoded secrets or credentials
- Insecure direct object references
- Missing input validation
- Error handling that leaks information
- Insecure dependencies

**Output Format:**
For each finding, provide:
- Severity (Critical/High/Medium/Low)
- File and line number
- Description
- Remediation
- Secure code example
"""

        return await self.run_task(prompt)

    async def review_authentication(self, auth_code_path: str) -> TaskResult:
        """Review authentication implementation"""
        await self.notify(f"Reviewing auth: {auth_code_path}")

        prompt = f"""
Review authentication implementation at: {auth_code_path}

**Verify:**
1. Password Storage
   - Using bcrypt/argon2/PBKDF2?
   - Adequate work factor?

2. Token Security
   - JWT properly validated?
   - Algorithm specified (not 'none')?
   - Expiration enforced?
   - Refresh token rotation?

3. Session Management
   - Secure session storage?
   - Session fixation prevention?
   - Proper logout/invalidation?

4. Rate Limiting
   - Login attempt limiting?
   - Account lockout policy?

5. MFA
   - MFA available/enforced for sensitive ops?
   - Secure MFA implementation?

**Provide:**
- Current security score (1-10)
- Critical issues
- Recommended improvements
- Secure code examples
"""

        return await self.run_task(prompt)

    async def audit_container_security(self, dockerfile_path: str) -> TaskResult:
        """Audit Docker container security"""
        prompt = f"""
Audit container security for: {dockerfile_path}

**Check:**
1. Base Image
   - Using minimal image (alpine, distroless)?
   - Pinned version (not :latest)?
   - From trusted source?

2. User Context
   - Running as non-root?
   - USER instruction present?

3. Secrets Handling
   - No secrets in image?
   - Using build args correctly?
   - Multi-stage build for secrets?

4. Resource Limits
   - Memory limits defined?
   - CPU limits defined?

5. Network
   - Minimal exposed ports?
   - No privileged mode?

6. Dependencies
   - No unnecessary packages?
   - Vulnerability scan results?

**Provide:**
- Security rating (A-F)
- Required fixes
- Recommended improvements
- Hardened Dockerfile example
"""

        return await self.run_task(prompt)

    async def check_secrets(self, directory: str = ".") -> TaskResult:
        """Scan for exposed secrets"""
        await self.notify(f"Scanning for secrets in: {directory}")

        prompt = f"""
Scan for exposed secrets in: {directory}

**Search for:**
1. API keys and tokens
2. Passwords and credentials
3. Private keys (SSH, SSL)
4. Database connection strings
5. AWS/GCP/Azure credentials
6. JWT secrets
7. Webhook URLs with tokens

**Check files:**
- .env files
- Config files (json, yaml, toml)
- Source code
- Docker files
- CI/CD configs
- Git history (if accessible)

**Patterns to find:**
- password=, passwd=, pwd=
- api_key=, apikey=, key=
- secret=, token=
- -----BEGIN PRIVATE KEY-----
- AKIA (AWS access key prefix)

**Output:**
For each finding:
- File and line
- Type of secret
- Severity
- Remediation (use env var, vault, etc.)
"""

        return await self.run_task(prompt)

    async def create_security_policy(self, scope: str) -> TaskResult:
        """Create security policy document"""
        prompt = f"""
Create security policy for: {scope}

**Include:**

## 1. Authentication Policy
- Password requirements
- MFA requirements
- Session management

## 2. Authorization Policy
- Role definitions
- Permission matrix
- Least privilege principle

## 3. Data Protection
- Encryption requirements
- PII handling
- Data retention

## 4. Secure Development
- Code review requirements
- Security testing
- Dependency management

## 5. Incident Response
- Reporting procedures
- Response steps
- Communication plan

## 6. Compliance
- Relevant standards (SOC2, GDPR, etc.)
- Audit requirements
"""

        return await self.run_task(prompt)

    async def work(self, task: str) -> TaskResult:
        """General security work"""
        await self.notify(f"Starting: {task[:50]}...")
        return await self.run_task(task)


async def main():
    """CLI entry point"""
    import argparse
    import json

    parser = argparse.ArgumentParser(description="Brett Jr - Cybersecurity Agent")
    parser.add_argument("--audit", type=str, help="Run security audit")
    parser.add_argument("--auth", type=str, help="Review authentication")
    parser.add_argument("--container", type=str, help="Audit container security")
    parser.add_argument("--secrets", type=str, nargs="?", const=".", help="Scan for secrets")
    parser.add_argument("--policy", type=str, help="Create security policy")
    parser.add_argument("--task", type=str, help="Run general task")
    parser.add_argument("--status", action="store_true", help="Show status")

    args = parser.parse_args()

    agent = BrettJrAgent()

    if args.status:
        print(json.dumps(agent.get_status(), indent=2))
        return

    if args.audit:
        result = await agent.security_audit(args.audit)
        print(result.output)
        return

    if args.auth:
        result = await agent.review_authentication(args.auth)
        print(result.output)
        return

    if args.container:
        result = await agent.audit_container_security(args.container)
        print(result.output)
        return

    if args.secrets is not None:
        result = await agent.check_secrets(args.secrets)
        print(result.output)
        return

    if args.policy:
        result = await agent.create_security_policy(args.policy)
        print(result.output)
        return

    if args.task:
        result = await agent.work(args.task)
        print(result.output)
        return

    print("Brett Jr - Cybersecurity Specialist")
    print("====================================")
    print("Use --help for options")


if __name__ == "__main__":
    asyncio.run(main())
