"""
Vera Agent - Cloud & AI Platform Specialist

Expert in Google Cloud Platform, Vertex AI, HIPAA compliance, and multi-tenant SaaS.
"""

import asyncio
from typing import Optional, List, Dict

from ..shared import BaseAgent, TaskResult
from .config import vera_config


class VeraAgent(BaseAgent):
    """
    Vera - Cloud & AI Platform Specialist

    Specializes in:
    - Google Cloud Platform architecture
    - Vertex AI agent development
    - HIPAA compliance
    - Multi-tenant SaaS patterns
    - Infrastructure as Code (Terraform)
    """

    def __init__(self, config=None):
        super().__init__(config or vera_config)

    # ============================================
    # GCP PROJECT MANAGEMENT
    # ============================================

    async def setup_gcp_project(
        self,
        project_name: str,
        environment: str = "dev",
        hipaa_compliant: bool = False
    ) -> TaskResult:
        """Set up a new GCP project with best practices"""
        await self.notify(f"Setting up GCP project: {project_name}")

        prompt = f"""
Set up a new GCP project:

**Project:** {project_name}
**Environment:** {environment}
**HIPAA Compliant:** {hipaa_compliant}

**Create Terraform configuration for:**

## 1. Project Structure
```hcl
# terraform/projects/{project_name}/main.tf
```

## 2. Required APIs
Enable these services:
- aiplatform.googleapis.com (Vertex AI)
- run.googleapis.com (Cloud Run)
- cloudfunctions.googleapis.com
- storage.googleapis.com
- bigquery.googleapis.com
- logging.googleapis.com
- monitoring.googleapis.com
{"- dlp.googleapis.com (Data Loss Prevention)" if hipaa_compliant else ""}

## 3. IAM Configuration
- Application service account (least privilege)
- Developer access group
- CI/CD service account

## 4. Networking
- VPC with private subnets
- Cloud NAT for outbound
- Private Service Access for managed services
{"- VPC Service Controls perimeter" if hipaa_compliant else ""}

## 5. Logging & Monitoring
- Audit logs enabled
- Log sink to BigQuery for analysis
- Alert policies for errors and costs

{'''## 6. HIPAA Configuration
- Enable Access Transparency
- Configure CMEK encryption
- Set up DLP inspection policies
- Document BAA requirements''' if hipaa_compliant else ""}

## 7. Budget & Alerts
- Monthly budget with 50%, 90% alerts
- Cost allocation labels

**Output:**
- Terraform files in terraform/projects/{project_name}/
- README with setup instructions
- variables.tf with required inputs

**Request approval before applying.**
"""

        result = await self.run_task(prompt)

        if result.success:
            await self.request_approval(
                description=f"GCP project setup ready: {project_name}",
                details="Review Terraform configuration before applying.",
                options=["Approve", "Reject", "Request Changes"]
            )
            result.needs_approval = True

        return result

    async def estimate_costs(
        self,
        project_description: str,
        users: int,
        data_volume_gb: float = 10.0
    ) -> TaskResult:
        """Estimate monthly GCP costs for a project"""
        await self.notify(f"Estimating costs for: {project_description[:50]}")

        prompt = f"""
Estimate monthly GCP costs:

**Project:** {project_description}
**Expected Users:** {users}
**Data Volume:** {data_volume_gb} GB

**Provide cost breakdown:**

## 1. Compute
| Service | Configuration | Monthly Cost |
|---------|---------------|--------------|
| Cloud Run | X instances, Y vCPU, Z GB RAM | $X |
| Cloud Functions | X invocations | $X |
| GKE (if applicable) | X nodes | $X |

## 2. Vertex AI
| Usage | Volume | Cost |
|-------|--------|------|
| Gemini Flash input tokens | X M tokens | $X |
| Gemini Flash output tokens | X M tokens | $X |
| Gemini Pro (if needed) | X M tokens | $X |
| Agent Engine | X sessions | $X |

## 3. Storage
| Service | Volume | Monthly Cost |
|---------|--------|--------------|
| Cloud Storage | X GB | $X |
| BigQuery Storage | X GB | $X |
| BigQuery Queries | X TB scanned | $X |

## 4. Networking
| Service | Usage | Monthly Cost |
|---------|-------|--------------|
| Egress | X GB | $X |
| Cloud NAT | X GB processed | $X |
| Load Balancer | X hours | $X |

## 5. Operations
| Service | Usage | Monthly Cost |
|---------|-------|--------------|
| Cloud Logging | X GB | $X |
| Cloud Monitoring | X metrics | $X |

## Total Estimate

| Category | Monthly Cost |
|----------|--------------|
| Compute | $X |
| AI/ML | $X |
| Storage | $X |
| Networking | $X |
| Operations | $X |
| **TOTAL** | **$X** |

## Cost Optimization Recommendations
1. [Recommendation 1]
2. [Recommendation 2]
3. [Recommendation 3]

## Assumptions
- [List key assumptions]
"""

        return await self.run_task(prompt)

    # ============================================
    # VERTEX AI METHODS
    # ============================================

    async def deploy_vertex_agent(
        self,
        agent_name: str,
        description: str,
        model: str = "gemini-1.5-flash",
        environment: str = "staging"
    ) -> TaskResult:
        """Deploy a Vertex AI agent"""
        await self.notify(f"Deploying agent: {agent_name} to {environment}")

        if environment in ["production", "prod"]:
            await self.request_approval(
                description=f"Production agent deployment: {agent_name}",
                details="This will deploy an agent to production.",
                options=["Deploy", "Cancel", "Deploy to Staging First"]
            )

        prompt = f"""
Deploy Vertex AI agent:

**Agent Name:** {agent_name}
**Description:** {description}
**Model:** {model}
**Environment:** {environment}

**Implementation Steps:**

## 1. Agent Definition
Create agent configuration:
```python
# agents/{agent_name}/agent.py
from vertexai.preview import reasoning_engines

agent_config = {{
    "name": "{agent_name}",
    "description": "{description}",
    "model": "{model}",
    "tools": [],  # Add tool definitions
    "instructions": \"\"\"{description}\"\"\"
}}
```

## 2. Tool Definitions
```python
# Define tools the agent can use
tools = [
    # Add relevant tools
]
```

## 3. Grounding Configuration
```python
# Configure data sources for grounding
grounding_config = {{
    "sources": [
        # GCS, BigQuery, or Search sources
    ]
}}
```

## 4. Deployment Script
```python
# deploy.py
from google.cloud import aiplatform
from vertexai.preview import reasoning_engines

aiplatform.init(
    project="{environment}_PROJECT_ID",
    location="us-central1"
)

agent = reasoning_engines.ReasoningEngine.create(
    reasoning_engine=agent_config,
    display_name="{agent_name}",
)
print(f"Agent deployed: {{agent.resource_name}}")
```

## 5. Testing
```python
# Test the deployed agent
session = agent.create_session()
response = session.query("Test query")
print(response.text)
```

## 6. Monitoring Setup
- Create dashboard for agent metrics
- Set up alerts for errors and latency
- Configure logging for debugging

**Deliverables:**
- [ ] Agent code in agents/{agent_name}/
- [ ] Deployment script
- [ ] Test script
- [ ] Monitoring dashboard config
"""

        return await self.run_task(prompt)

    async def configure_mcp_server(
        self,
        server_type: str,
        configuration: str
    ) -> TaskResult:
        """Configure an MCP server for Vertex AI agents"""
        await self.notify(f"Configuring MCP server: {server_type}")

        prompt = f"""
Configure MCP server for Vertex AI integration:

**Server Type:** {server_type}
**Configuration:** {configuration}

**Implementation:**

## 1. MCP Server Setup

### For existing servers (Monday.com, HubSpot, etc.)
```python
from mcp import Client, StdioServerParameters

async def connect_{server_type.lower().replace('.', '_')}_mcp():
    \"\"\"Connect to {server_type} MCP server\"\"\"
    server_params = StdioServerParameters(
        command="npx",
        args=["@package/{server_type}-mcp@latest"],
        env={{
            "API_TOKEN": os.environ["{server_type.upper()}_API_TOKEN"]
        }}
    )

    client = Client()
    await client.connect(server_params)
    return client
```

### For custom MCP servers
```python
# mcp_servers/{server_type}/server.py
from mcp.server import Server
from mcp.types import Tool, TextContent

server = Server("{server_type}")

@server.list_tools()
async def list_tools() -> list[Tool]:
    return [
        Tool(
            name="tool_name",
            description="Tool description",
            inputSchema={{
                "type": "object",
                "properties": {{
                    "param": {{"type": "string"}}
                }}
            }}
        )
    ]

@server.call_tool()
async def call_tool(name: str, arguments: dict) -> list[TextContent]:
    # Implement tool logic
    return [TextContent(type="text", text="Result")]
```

## 2. Authentication Setup
- Secure credential storage (Secret Manager)
- Service account for MCP server
- Token rotation policy

## 3. Integration with Vertex AI Agent
```python
# In agent configuration
tools = [
    mcp_tool("{server_type}", "tool_name"),
]
```

## 4. Testing
```python
# Test MCP connection
async def test_mcp():
    client = await connect_{server_type.lower()}_mcp()
    tools = await client.list_tools()
    print(f"Available tools: {{tools}}")

    # Test tool invocation
    result = await client.call_tool("tool_name", {{"param": "value"}})
    print(f"Result: {{result}}")
```

## 5. Security Considerations
- [ ] Credentials in Secret Manager
- [ ] Least privilege access
- [ ] Audit logging enabled
- [ ] Rate limiting configured

**Deliverables:**
- [ ] MCP server code or configuration
- [ ] Authentication setup
- [ ] Integration code
- [ ] Test script
"""

        return await self.run_task(prompt)

    # ============================================
    # HIPAA COMPLIANCE
    # ============================================

    async def hipaa_compliance_audit(self, project_id: str) -> TaskResult:
        """Audit GCP project for HIPAA compliance"""
        await self.notify(f"HIPAA compliance audit: {project_id}")

        prompt = f"""
Perform HIPAA compliance audit for GCP project: {project_id}

**Audit Checklist:**

## 1. Business Associate Agreement
- [ ] BAA executed with Google Cloud
- [ ] Covered services documented

## 2. Access Controls
```bash
# Check IAM policies
gcloud projects get-iam-policy {project_id} --format=json

# List service accounts
gcloud iam service-accounts list --project={project_id}
```

**Verify:**
- [ ] No overly permissive roles (Owner, Editor on service accounts)
- [ ] Service accounts use Workload Identity where possible
- [ ] Human access uses groups, not individual bindings

## 3. Audit Logging
```bash
# Check audit log configuration
gcloud logging sinks list --project={project_id}

# Verify data access logs enabled
gcloud projects get-iam-policy {project_id} --format=json | jq '.auditConfigs'
```

**Verify:**
- [ ] Admin Activity logs enabled (default)
- [ ] Data Access logs enabled for PHI services
- [ ] Log sink to secure destination
- [ ] Log retention >= 6 years

## 4. Encryption
```bash
# Check CMEK configuration
gcloud kms keyrings list --location=us-central1 --project={project_id}
```

**Verify:**
- [ ] Encryption at rest (default or CMEK)
- [ ] Encryption in transit (TLS 1.2+)
- [ ] CMEK for sensitive data (recommended)
- [ ] Key rotation enabled

## 5. Network Security
```bash
# Check VPC configuration
gcloud compute networks list --project={project_id}
gcloud compute firewall-rules list --project={project_id}
```

**Verify:**
- [ ] VPC Service Controls enabled
- [ ] Private Google Access configured
- [ ] No public IPs on sensitive resources
- [ ] Firewall rules follow least privilege

## 6. Data Loss Prevention
```bash
# Check DLP configuration
gcloud dlp job-triggers list --project={project_id}
```

**Verify:**
- [ ] DLP inspection for PHI
- [ ] De-identification policies configured
- [ ] Alerts for PHI detection

## 7. HIPAA-Eligible Services Only
**Verify only these services store PHI:**
- Cloud Storage
- BigQuery
- Cloud SQL
- Firestore
- Cloud Spanner
- Vertex AI (with BAA)
- Cloud Healthcare API

## Audit Report

| Category | Status | Findings | Remediation |
|----------|--------|----------|-------------|
| BAA | PASS/FAIL | | |
| Access Controls | PASS/FAIL | | |
| Audit Logging | PASS/FAIL | | |
| Encryption | PASS/FAIL | | |
| Network Security | PASS/FAIL | | |
| DLP | PASS/FAIL | | |
| Service Selection | PASS/FAIL | | |

## Critical Findings
[List any critical compliance gaps]

## Remediation Plan
1. [Priority action items]
"""

        return await self.run_task(prompt)

    # ============================================
    # MULTI-TENANT MANAGEMENT
    # ============================================

    async def onboard_tenant(
        self,
        tenant_id: str,
        tenant_name: str,
        tier: str = "standard"
    ) -> TaskResult:
        """Onboard a new tenant to the multi-tenant platform"""
        await self.notify(f"Onboarding tenant: {tenant_name}")

        prompt = f"""
Onboard new tenant to multi-tenant platform:

**Tenant ID:** {tenant_id}
**Tenant Name:** {tenant_name}
**Tier:** {tier}

**Onboarding Steps:**

## 1. Create Tenant Project (if project-per-tenant)
```hcl
# Run Terraform with tenant variables
terraform apply -var="tenant_id={tenant_id}" -var="tenant_name={tenant_name}" -var="tier={tier}"
```

## 2. Configure IAM
```bash
# Create tenant admin group
gcloud identity groups create {tenant_id}-admins@domain.com

# Bind to tenant project
gcloud projects add-iam-policy-binding project-{tenant_id} \\
  --member="group:{tenant_id}-admins@domain.com" \\
  --role="roles/viewer"
```

## 3. Provision Storage
```bash
# Create tenant bucket
gsutil mb -p project-{tenant_id} -l us-central1 gs://{tenant_id}-data/

# Set lifecycle policy
gsutil lifecycle set lifecycle.json gs://{tenant_id}-data/
```

## 4. Configure Agent Access
```python
# Grant tenant access to shared agents
agent_config = {{
    "tenant_id": "{tenant_id}",
    "allowed_agents": ["agent1", "agent2"],
    "rate_limits": {{
        "requests_per_minute": 60 if "{tier}" == "standard" else 120
    }}
}}
```

## 5. Set Up Billing
```bash
# Link to billing account or set budget
gcloud billing budgets create \\
  --billing-account=BILLING_ACCOUNT_ID \\
  --display-name="{tenant_name} Budget" \\
  --budget-amount=1000USD \\
  --threshold-rule=percent=50 \\
  --threshold-rule=percent=90
```

## 6. Compliance Validation
- [ ] HIPAA configurations applied
- [ ] Data isolation verified
- [ ] Audit logging enabled
- [ ] Encryption configured

## 7. Generate Documentation
Create tenant-specific documentation:
- API credentials
- Access instructions
- Support contacts
- SLA details

**Verification Checklist:**
- [ ] Project created and accessible
- [ ] IAM correctly configured
- [ ] Storage provisioned
- [ ] Agent access working
- [ ] Billing configured
- [ ] Compliance validated
- [ ] Documentation delivered

**Tenant Summary:**
| Field | Value |
|-------|-------|
| Tenant ID | {tenant_id} |
| Project | project-{tenant_id} |
| Storage | gs://{tenant_id}-data/ |
| Tier | {tier} |
| Status | Active |
"""

        return await self.run_task(prompt)

    async def offboard_tenant(self, tenant_id: str, retain_data_days: int = 30) -> TaskResult:
        """Offboard a tenant from the platform"""
        await self.notify(f"Offboarding tenant: {tenant_id}")

        await self.request_approval(
            description=f"Tenant offboarding: {tenant_id}",
            details=f"This will disable tenant access. Data retained for {retain_data_days} days.",
            options=["Proceed", "Cancel", "Extend Retention"]
        )

        prompt = f"""
Offboard tenant from platform:

**Tenant ID:** {tenant_id}
**Data Retention:** {retain_data_days} days

**CAUTION: This is a destructive operation. Verify approval before proceeding.**

**Offboarding Steps:**

## 1. Disable Access (Immediate)
```bash
# Remove IAM bindings
gcloud projects remove-iam-policy-binding project-{tenant_id} \\
  --member="group:{tenant_id}-admins@domain.com" \\
  --role="roles/viewer"

# Revoke service account keys
gcloud iam service-accounts keys list --iam-account=app@project-{tenant_id}.iam.gserviceaccount.com
```

## 2. Archive Data
```bash
# Move to archive bucket with retention
gsutil -m cp -r gs://{tenant_id}-data/ gs://archive-bucket/{tenant_id}/

# Set deletion date
gsutil lifecycle set archive-lifecycle.json gs://archive-bucket/{tenant_id}/
```

## 3. Disable Services
```bash
# Disable billing (prevents new charges)
gcloud billing projects unlink project-{tenant_id}

# Shut down Cloud Run services
gcloud run services list --project=project-{tenant_id} --format="value(name)" | \\
  xargs -I {{}} gcloud run services delete {{}} --project=project-{tenant_id} --quiet
```

## 4. Schedule Deletion
```bash
# Schedule project deletion after retention period
gcloud projects delete project-{tenant_id}
# Note: 30-day recovery window applies
```

## 5. Update Records
- Remove from active tenant list
- Update billing records
- Archive support tickets
- Document offboarding date

## 6. Compliance
- [ ] Data export provided to tenant (if requested)
- [ ] Audit log of offboarding actions
- [ ] Confirmation of access revocation

**Timeline:**
| Date | Action |
|------|--------|
| Today | Access disabled, data archived |
| +{retain_data_days} days | Data eligible for deletion |
| +{retain_data_days + 30} days | Project permanently deleted |
"""

        return await self.run_task(prompt)

    # ============================================
    # INFRASTRUCTURE AS CODE
    # ============================================

    async def review_terraform(self, terraform_path: str) -> TaskResult:
        """Review Terraform configuration for best practices"""
        await self.notify(f"Reviewing Terraform: {terraform_path}")

        prompt = f"""
Review Terraform configuration at: {terraform_path}

**Review Checklist:**

## 1. Security Review
- [ ] No hardcoded credentials or secrets
- [ ] Service accounts use least privilege
- [ ] Encryption configured (at rest and transit)
- [ ] Network security (firewall rules, VPC)
- [ ] IAM bindings follow principle of least privilege

## 2. Best Practices
- [ ] Resources have descriptive names
- [ ] Labels applied consistently
- [ ] Variables used for environment-specific values
- [ ] Outputs defined for important values
- [ ] Modules used for reusable components

## 3. Cost Optimization
- [ ] Right-sized instances
- [ ] Autoscaling configured where appropriate
- [ ] Lifecycle policies on storage
- [ ] Committed use discounts considered

## 4. Maintainability
- [ ] Code is DRY (Don't Repeat Yourself)
- [ ] Comments explain non-obvious logic
- [ ] Consistent formatting
- [ ] Version constraints on providers

## 5. HIPAA Compliance (if applicable)
- [ ] Only HIPAA-eligible services for PHI
- [ ] Audit logging enabled
- [ ] Encryption with CMEK
- [ ] VPC Service Controls

## Findings

| Severity | File | Line | Issue | Recommendation |
|----------|------|------|-------|----------------|
| Critical | | | | |
| High | | | | |
| Medium | | | | |
| Low | | | | |

## Summary
- Total issues: X
- Critical: X
- High: X
- Medium: X
- Low: X

## Recommended Actions
1. [Priority fixes]
"""

        return await self.run_task(prompt)

    # ============================================
    # GENERAL
    # ============================================

    async def work(self, task: str) -> TaskResult:
        """General cloud platform work"""
        await self.notify(f"Starting: {task[:50]}...")
        return await self.run_task(task)


async def main():
    """CLI entry point"""
    import argparse
    import json

    parser = argparse.ArgumentParser(description="Vera - Cloud & AI Platform Specialist")
    parser.add_argument("--setup-project", type=str, help="Set up GCP project")
    parser.add_argument("--environment", type=str, default="dev", help="Environment")
    parser.add_argument("--hipaa", action="store_true", help="HIPAA compliant")
    parser.add_argument("--estimate-costs", type=str, help="Project description for cost estimate")
    parser.add_argument("--users", type=int, default=10, help="Expected users")
    parser.add_argument("--deploy-agent", type=str, help="Deploy Vertex AI agent")
    parser.add_argument("--agent-desc", type=str, help="Agent description")
    parser.add_argument("--model", type=str, default="gemini-1.5-flash", help="Model")
    parser.add_argument("--configure-mcp", type=str, help="Configure MCP server type")
    parser.add_argument("--mcp-config", type=str, help="MCP configuration")
    parser.add_argument("--hipaa-audit", type=str, help="HIPAA audit project ID")
    parser.add_argument("--onboard-tenant", type=str, help="Onboard tenant ID")
    parser.add_argument("--tenant-name", type=str, help="Tenant name")
    parser.add_argument("--tier", type=str, default="standard", help="Tenant tier")
    parser.add_argument("--offboard-tenant", type=str, help="Offboard tenant ID")
    parser.add_argument("--review-terraform", type=str, help="Review Terraform path")
    parser.add_argument("--task", type=str, help="Run general task")
    parser.add_argument("--status", action="store_true", help="Show status")

    args = parser.parse_args()

    agent = VeraAgent()

    if args.status:
        print(json.dumps(agent.get_status(), indent=2))
        return

    if args.setup_project:
        result = await agent.setup_gcp_project(
            args.setup_project, args.environment, args.hipaa
        )
        print(result.output)
        return

    if args.estimate_costs:
        result = await agent.estimate_costs(args.estimate_costs, args.users)
        print(result.output)
        return

    if args.deploy_agent and args.agent_desc:
        result = await agent.deploy_vertex_agent(
            args.deploy_agent, args.agent_desc, args.model, args.environment
        )
        print(result.output)
        return

    if args.configure_mcp and args.mcp_config:
        result = await agent.configure_mcp_server(args.configure_mcp, args.mcp_config)
        print(result.output)
        return

    if args.hipaa_audit:
        result = await agent.hipaa_compliance_audit(args.hipaa_audit)
        print(result.output)
        return

    if args.onboard_tenant and args.tenant_name:
        result = await agent.onboard_tenant(args.onboard_tenant, args.tenant_name, args.tier)
        print(result.output)
        return

    if args.offboard_tenant:
        result = await agent.offboard_tenant(args.offboard_tenant)
        print(result.output)
        return

    if args.review_terraform:
        result = await agent.review_terraform(args.review_terraform)
        print(result.output)
        return

    if args.task:
        result = await agent.work(args.task)
        print(result.output)
        return

    print("Vera - Cloud & AI Platform Specialist")
    print("=====================================")
    print("Use --help for options")


if __name__ == "__main__":
    asyncio.run(main())
