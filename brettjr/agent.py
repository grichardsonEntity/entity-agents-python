"""
Brett Jr Agent - Cybersecurity Specialist

Expert in security audits, authentication, encryption, compliance,
threat modeling, supply chain security, and zero trust architecture.
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
    - Compliance frameworks (SOC 2, PCI-DSS, NIST, ISO 27001, FedRAMP, HIPAA)
    - Threat modeling (STRIDE, DREAD, attack trees)
    - Supply chain security and SBOM
    - SAST/DAST integration
    - Incident response planning
    - Zero trust architecture
    - API security
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

    async def compliance_audit(self, framework: str, scope: str) -> TaskResult:
        """Conduct compliance audit against a specific framework with control mapping and gap analysis"""
        await self.notify(f"Compliance audit ({framework}): {scope}")

        prompt = f"""
Conduct a comprehensive compliance audit for: {scope}
Framework: {framework}

**Phase 1: Control Mapping**
Map the system's existing security controls to the {framework} framework requirements.
For each control family/domain, identify:
- Control ID and description
- Current implementation status (Implemented / Partially Implemented / Not Implemented / Not Applicable)
- Evidence available (logs, configs, policies, procedures)

**Phase 2: Gap Analysis**
For each gap identified:
- Control requirement that is not met
- Current state vs. required state
- Risk level (Critical / High / Medium / Low)
- Business impact of non-compliance

**Phase 3: Remediation Plan**
For each gap, provide:
- Specific remediation steps
- Estimated effort (hours/days)
- Priority ranking
- Owner recommendation
- Timeline for completion

**Framework-Specific Guidance:**
- SOC 2 Type II: Map to Trust Service Criteria (CC1-CC9, availability, processing integrity, confidentiality, privacy)
- PCI-DSS: Map to 12 requirements with sub-requirements, identify CDE scope
- NIST 800-53: Map to control families (AC, AU, CA, CM, CP, IA, IR, MA, MP, PE, PL, PM, PS, RA, SA, SC, SI, SR)
- ISO 27001: Map to Annex A controls, assess ISMS maturity
- FedRAMP: Determine impact level (Low/Moderate/High), map to baseline controls
- HIPAA: Assess administrative, physical, technical safeguards, identify ePHI flows

**Output Format:**
1. Executive Summary with compliance score percentage
2. Control mapping matrix
3. Gap analysis with risk ratings
4. Prioritized remediation roadmap
5. Evidence collection checklist
"""

        return await self.run_task(prompt)

    async def threat_model(self, system_description: str, assets: str) -> TaskResult:
        """Build STRIDE threat model with risk scoring and mitigations"""
        await self.notify(f"Threat modeling: {system_description[:50]}...")

        prompt = f"""
Build a comprehensive threat model for the following system.

**System Description:** {system_description}

**Critical Assets:** {assets}

**Phase 1: System Decomposition**
- Identify trust boundaries
- Map data flows (DFD Level 0 and Level 1)
- Enumerate entry points and exit points
- Identify external dependencies and third-party integrations

**Phase 2: STRIDE Analysis**
For each component and data flow, analyze threats using STRIDE:

| Threat Category | Component | Threat Description | Attack Vector |
|----------------|-----------|-------------------|---------------|
| **S**poofing | ... | ... | ... |
| **T**ampering | ... | ... | ... |
| **R**epudiation | ... | ... | ... |
| **I**nformation Disclosure | ... | ... | ... |
| **D**enial of Service | ... | ... | ... |
| **E**levation of Privilege | ... | ... | ... |

**Phase 3: DREAD Risk Scoring**
For each identified threat, score using DREAD (1-10 each):
- **D**amage Potential: How much damage if exploited?
- **R**eproducibility: How easy to reproduce?
- **E**xploitability: How easy to exploit?
- **A**ffected Users: How many users impacted?
- **D**iscoverability: How easy to discover?

Calculate overall risk score: (D + R + E + A + D) / 5

**Phase 4: Attack Trees**
For the top 3 highest-risk threats, create attack trees:
- Root goal (attacker objective)
- AND/OR decomposition of sub-goals
- Leaf nodes with cost/effort/probability
- Highlight most likely attack paths

**Phase 5: Mitigations**
For each threat, recommend:
- Preventive controls
- Detective controls
- Corrective controls
- MITRE ATT&CK technique mapping where applicable

**Output:**
1. Threat matrix with all identified threats
2. Risk-scored and prioritized threat list
3. Attack trees for top threats
4. Mitigation recommendations with implementation priority
5. Residual risk assessment after mitigations
"""

        return await self.run_task(prompt)

    async def dependency_audit(self, project_path: str) -> TaskResult:
        """Audit supply chain: vulnerable dependencies, license issues, SBOM generation"""
        await self.notify(f"Dependency audit: {project_path}")

        prompt = f"""
Conduct a comprehensive supply chain security audit for project at: {project_path}

**Phase 1: Dependency Inventory**
- Enumerate all direct and transitive dependencies
- Identify dependency managers (pip, npm, cargo, go mod, etc.)
- Check lock file presence and integrity
- Map the full dependency tree

**Phase 2: Vulnerability Scanning**
For each dependency:
- Check against NVD (National Vulnerability Database)
- Check against GitHub Advisory Database
- Check against OSV (Open Source Vulnerabilities)
- Report CVE IDs, severity (CVSS score), and affected versions
- Identify if patches/updates are available
- Flag end-of-life or unmaintained packages

**Phase 3: License Compliance**
- Identify license for each dependency
- Flag copyleft licenses (GPL, AGPL, LGPL)
- Identify license incompatibilities
- Check for packages with no license or unknown license
- Generate license obligation summary

**Phase 4: SBOM Generation**
Generate Software Bill of Materials including:
- Package name, version, supplier
- Download location, checksums
- Relationship type (direct/transitive)
- Output in CycloneDX or SPDX format recommendations

**Phase 5: Supply Chain Risk Assessment**
- Identify typosquatting risks
- Check package maintainer reputation and activity
- Assess dependency freshness (time since last update)
- Flag single-maintainer critical dependencies
- Check for dependency confusion risks

**Output:**
1. Dependency inventory with risk ratings
2. Vulnerability report with remediation actions
3. License compliance matrix
4. SBOM structure recommendation
5. Supply chain risk summary with prioritized actions
"""

        return await self.run_task(prompt)

    async def setup_sast(self, project_path: str, language: str) -> TaskResult:
        """Configure static analysis tools with CI integration"""
        await self.notify(f"Setting up SAST for {language} project: {project_path}")

        prompt = f"""
Configure comprehensive static analysis (SAST) for the project at: {project_path}
Primary Language: {language}

**Phase 1: Tool Selection and Configuration**

Based on language ({language}), configure appropriate tools:

For Python:
- Bandit configuration (.bandit, pyproject.toml)
- Semgrep rules (custom + community rulesets)
- Safety for dependency checking
- mypy for type safety (security-relevant)

For JavaScript/TypeScript:
- ESLint with security plugins (eslint-plugin-security, eslint-plugin-no-secrets)
- Semgrep rules for JS/TS
- npm audit configuration
- CodeQL queries for JavaScript

For Go:
- gosec configuration
- Semgrep rules for Go
- govulncheck setup

For Java:
- SpotBugs with FindSecBugs plugin
- Semgrep rules for Java
- OWASP Dependency-Check

General (all languages):
- Semgrep custom rules for project-specific patterns
- CodeQL workflow configuration
- Secret detection (gitleaks, trufflehog)

**Phase 2: Rule Configuration**
- Define severity thresholds (what blocks CI)
- Configure false positive suppressions
- Create custom rules for project-specific security patterns
- Set up baseline for existing findings

**Phase 3: CI/CD Integration**
Provide configurations for:
- GitHub Actions workflow
- Pre-commit hooks (.pre-commit-config.yaml)
- Pull request annotations
- SARIF output for GitHub Security tab

**Phase 4: Triage Workflow**
- Define process for reviewing findings
- Create suppression/ignore file templates
- Set up finding tracking and metrics
- Define SLA for fixing findings by severity

**Output:**
1. Tool configuration files (ready to use)
2. CI/CD pipeline configuration
3. Pre-commit hook setup
4. Custom rule examples
5. Triage process documentation
6. Metric tracking recommendations
"""

        return await self.run_task(prompt)

    async def incident_response_plan(self, system: str, threat_scenarios: str) -> TaskResult:
        """Create IR playbook with detection, containment, eradication, and recovery steps"""
        await self.notify(f"Creating IR plan for: {system}")

        prompt = f"""
Create a comprehensive Incident Response Plan for the following system and threat scenarios.

**System:** {system}

**Threat Scenarios:** {threat_scenarios}

**Phase 1: Preparation**
- IR team roles and responsibilities (Incident Commander, Technical Lead, Communications, Legal)
- Communication channels and escalation paths
- Tool inventory (SIEM, EDR, forensics tools)
- Runbook maintenance and training schedule
- Tabletop exercise schedule

**Phase 2: Detection and Analysis**
For each threat scenario, define:
- Detection indicators (IOCs - Indicators of Compromise)
- Alert sources (SIEM rules, IDS/IPS, application logs, cloud alerts)
- Severity classification criteria:
  - **P1 (Critical):** Active data breach, ransomware, complete service compromise
  - **P2 (High):** Confirmed intrusion, privilege escalation, data exfiltration attempt
  - **P3 (Medium):** Suspicious activity, policy violation, vulnerability exploitation attempt
  - **P4 (Low):** Reconnaissance, failed attacks, minor policy violations
- Initial triage checklist
- Evidence collection procedures

**Phase 3: Containment**
- Short-term containment (immediate actions to stop bleeding)
  - Network isolation procedures
  - Account suspension/password reset
  - Service shutdown criteria
- Long-term containment (while preparing remediation)
  - Temporary security controls
  - Enhanced monitoring
  - Communication with affected parties
- Containment verification steps

**Phase 4: Eradication**
- Root cause identification procedures
- Malware removal steps
- Vulnerability patching process
- Configuration hardening
- Credential rotation scope and procedure
- Third-party notification requirements

**Phase 5: Recovery**
- System restoration procedures
- Data integrity verification
- Phased service restoration plan
- Enhanced monitoring during recovery
- User communication and access restoration
- Business continuity activation criteria

**Phase 6: Post-Incident**
- Post-incident review template (within 72 hours)
- Root cause analysis (5 Whys, fishbone diagram)
- Lessons learned documentation
- Control improvement recommendations
- Metrics to track:
  - Mean Time to Detect (MTTD)
  - Mean Time to Respond (MTTR)
  - Mean Time to Contain (MTTC)
  - Mean Time to Recover

**Phase 7: Breach Notification**
- Regulatory requirements by jurisdiction
  - GDPR: 72-hour notification to DPA
  - US State laws: Varies by state
  - HIPAA: 60-day notification
  - PCI-DSS: Immediate notification to acquirer
- Notification templates (regulators, customers, public)
- Legal review checklist
- PR/communications plan

**Output:**
1. Complete IR playbook for each threat scenario
2. Escalation matrix
3. Communication templates
4. Evidence collection checklist
5. Post-incident review template
6. Breach notification decision tree
"""

        return await self.run_task(prompt)

    async def zero_trust_assessment(self, architecture_description: str) -> TaskResult:
        """Assess zero trust maturity and provide recommendations"""
        await self.notify(f"Zero trust assessment: {architecture_description[:50]}...")

        prompt = f"""
Conduct a Zero Trust Architecture maturity assessment for the following system.

**Architecture Description:** {architecture_description}

**Assessment Pillars:**

### 1. Identity
- Authentication mechanisms (SSO, MFA, passwordless)
- Identity providers and federation
- Service-to-service identity (mTLS, SPIFFE/SPIRE)
- Conditional access policies
- Identity governance and lifecycle
**Maturity Rating:** (Traditional / Advanced / Optimal)

### 2. Devices
- Device inventory and management (MDM/UEM)
- Device health attestation
- Endpoint detection and response (EDR)
- BYOD policies and controls
**Maturity Rating:** (Traditional / Advanced / Optimal)

### 3. Networks
- Micro-segmentation implementation
- Software-defined perimeter
- Encrypted communications (mTLS everywhere)
- DNS security
- East-west traffic inspection
**Maturity Rating:** (Traditional / Advanced / Optimal)

### 4. Applications and Workloads
- Application access policies
- Application-level authentication
- Container/serverless security
- CI/CD pipeline security
- Runtime application self-protection (RASP)
**Maturity Rating:** (Traditional / Advanced / Optimal)

### 5. Data
- Data classification and labeling
- Data loss prevention (DLP)
- Encryption at rest and in transit
- Access logging and monitoring
- Data rights management
**Maturity Rating:** (Traditional / Advanced / Optimal)

### 6. Visibility and Analytics
- Security Information and Event Management (SIEM)
- User and Entity Behavior Analytics (UEBA)
- Network Detection and Response (NDR)
- Centralized logging and correlation
- Threat intelligence integration
**Maturity Rating:** (Traditional / Advanced / Optimal)

### 7. Automation and Orchestration
- Security Orchestration, Automation and Response (SOAR)
- Automated policy enforcement
- Infrastructure as Code security
- Automated incident response
**Maturity Rating:** (Traditional / Advanced / Optimal)

**Output:**
1. Current maturity scorecard (per pillar)
2. Overall Zero Trust maturity level
3. Gap analysis for each pillar
4. Prioritized roadmap (quick wins, medium-term, long-term)
5. Architecture recommendations with diagrams (text-based)
6. Implementation cost/effort estimates
7. Key metrics and KPIs to track progress
"""

        return await self.run_task(prompt)

    async def api_security_review(self, api_spec: str) -> TaskResult:
        """Review API security: OAuth flows, input validation, rate limiting, gateway config"""
        await self.notify(f"API security review: {api_spec[:50]}...")

        prompt = f"""
Conduct a comprehensive API security review for the following API specification/system.

**API Specification:** {api_spec}

**Phase 1: Authentication and Authorization Review**
- OAuth 2.0 flow analysis:
  - Authorization Code + PKCE (recommended for SPAs and mobile)
  - Client Credentials (service-to-service)
  - Verify no Implicit or Resource Owner Password grants
- OpenID Connect implementation:
  - ID token validation
  - UserInfo endpoint security
  - Proper scope definitions
- Token security:
  - Token lifetime and rotation
  - Token storage (secure, no localStorage for sensitive tokens)
  - Token revocation mechanism
  - JWT algorithm verification (RS256 preferred, reject 'none')
- API key management:
  - Key rotation policy
  - Scope/permission restrictions
  - Key exposure monitoring

**Phase 2: Input Validation and Data Protection**
- Request validation:
  - Schema validation (OpenAPI/JSON Schema enforcement)
  - Content-Type enforcement
  - Payload size limits
  - Parameter type checking
- Injection prevention:
  - SQL injection (parameterized queries)
  - NoSQL injection
  - Command injection
  - LDAP injection
  - GraphQL injection (if applicable)
- Data exposure:
  - Response field filtering (no over-fetching)
  - Sensitive data masking in logs
  - Error message information leakage
  - Stack trace exposure prevention

**Phase 3: Rate Limiting and Abuse Prevention**
- Rate limiting strategy:
  - Per-user/per-IP limits
  - Per-endpoint limits (sensitive endpoints more restrictive)
  - Token bucket vs. sliding window algorithm
  - Distributed rate limiting (Redis-backed)
- Abuse prevention:
  - Bot detection
  - Request fingerprinting
  - Anomaly detection
  - Geographic restrictions (if applicable)
- DDoS protection:
  - Layer 7 DDoS mitigation
  - Request queuing
  - Circuit breaker patterns

**Phase 4: API Gateway and Infrastructure**
- Gateway configuration:
  - TLS 1.2+ enforcement
  - Certificate management
  - CORS policy review
  - Security headers (HSTS, CSP, X-Content-Type-Options)
- Network security:
  - mTLS for internal services
  - VPN/private network for admin APIs
  - IP whitelisting for partner APIs
- Monitoring and logging:
  - API access logging
  - Anomaly detection
  - Real-time alerting
  - Audit trail completeness

**Phase 5: API-Specific Vulnerabilities**
- BOLA (Broken Object Level Authorization)
- BFLA (Broken Function Level Authorization)
- Mass assignment
- Excessive data exposure
- Server-Side Request Forgery (SSRF)
- Improper inventory management (shadow APIs)

**Output:**
1. Security scorecard by category
2. Critical and high findings with remediation
3. OAuth/OIDC flow recommendations
4. Rate limiting configuration templates
5. API gateway hardening checklist
6. Monitoring and alerting recommendations
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
    parser.add_argument("--compliance", type=str, nargs=2, metavar=("FRAMEWORK", "SCOPE"),
                        help="Compliance audit (e.g., --compliance 'SOC2' 'payment-service')")
    parser.add_argument("--threat-model", type=str, nargs=2, metavar=("SYSTEM", "ASSETS"),
                        help="Threat model (e.g., --threat-model 'API gateway' 'user-data,tokens')")
    parser.add_argument("--dep-audit", type=str, help="Dependency/supply chain audit")
    parser.add_argument("--sast", type=str, nargs=2, metavar=("PROJECT", "LANGUAGE"),
                        help="Setup SAST (e.g., --sast './myproject' 'python')")
    parser.add_argument("--ir-plan", type=str, nargs=2, metavar=("SYSTEM", "THREATS"),
                        help="Incident response plan (e.g., --ir-plan 'prod-api' 'data-breach,ransomware')")
    parser.add_argument("--zero-trust", type=str, help="Zero trust assessment")
    parser.add_argument("--api-security", type=str, help="API security review")
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

    if args.compliance:
        result = await agent.compliance_audit(args.compliance[0], args.compliance[1])
        print(result.output)
        return

    if args.threat_model:
        result = await agent.threat_model(args.threat_model[0], args.threat_model[1])
        print(result.output)
        return

    if args.dep_audit:
        result = await agent.dependency_audit(args.dep_audit)
        print(result.output)
        return

    if args.sast:
        result = await agent.setup_sast(args.sast[0], args.sast[1])
        print(result.output)
        return

    if args.ir_plan:
        result = await agent.incident_response_plan(args.ir_plan[0], args.ir_plan[1])
        print(result.output)
        return

    if args.zero_trust:
        result = await agent.zero_trust_assessment(args.zero_trust)
        print(result.output)
        return

    if args.api_security:
        result = await agent.api_security_review(args.api_security)
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
