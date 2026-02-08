"""
Quinn Agent - Network Engineer & Deployment Specialist

Expert in networking, containers, infrastructure, deployments,
load balancing, DNS, disaster recovery, monitoring, service mesh, and edge computing.
"""

import asyncio
from typing import Optional, List

from ..shared import BaseAgent, TaskResult
from .config import quinn_config


class QuinnAgent(BaseAgent):
    """
    Quinn - Network Engineer & Deployment Specialist

    Specializes in:
    - Network architecture
    - Container deployment
    - Infrastructure management
    - VPN and security
    - Load balancing (HAProxy, Nginx, Traefik)
    - DNS management and failover
    - Disaster recovery planning
    - Monitoring and alerting (Prometheus, Grafana)
    - Service mesh (Istio, Linkerd)
    - CDN and edge computing
    """

    def __init__(self, config=None):
        super().__init__(config or quinn_config)

    async def design_network(self, requirements: str) -> TaskResult:
        """Design a network architecture"""
        await self.notify(f"Designing network for: {requirements[:50]}")

        prompt = f"""
Design network architecture for:

{requirements}

**Include:**

## 1. Network Topology

```
[ASCII or Mermaid diagram showing network architecture]
```

## 2. IP Addressing Scheme
| Network | CIDR | Purpose | Gateway |
|---------|------|---------|---------|
| ... | ... | ... | ... |

## 3. VLAN Design
| VLAN ID | Name | Purpose | Subnet |
|---------|------|---------|--------|
| ... | ... | ... | ... |

## 4. Firewall Rules
| Direction | Source | Destination | Port | Action |
|-----------|--------|-------------|------|--------|
| ... | ... | ... | ... | ... |

## 5. VPN Configuration
- Type: WireGuard/Tailscale
- Peers
- Routing

## 6. High Availability
- Redundancy approach
- Failover mechanism

## 7. Security Considerations
- Attack surface
- Segmentation
- Monitoring

**Request approval before implementation.**
"""

        result = await self.run_task(prompt)

        if result.success:
            await self.request_approval(
                description="Network design ready for review",
                details="Please review architecture before implementation.",
                options=["Approve", "Reject", "Request Changes"]
            )
            result.needs_approval = True

        return result

    async def deploy_containers(
        self,
        compose_file: str,
        environment: str = "staging"
    ) -> TaskResult:
        """Deploy containers using Docker Compose"""
        await self.notify(f"Deploying to {environment}: {compose_file}")

        if environment in ["production", "prod"]:
            await self.request_approval(
                description=f"Production deployment: {compose_file}",
                details="This will deploy to production. Please confirm.",
                options=["Deploy", "Cancel", "Deploy to Staging First"]
            )

        prompt = f"""
Deploy containers from: {compose_file}
Environment: {environment}

**Steps:**
1. Validate compose file syntax
2. Check for security issues
3. Pull latest images
4. Deploy with appropriate settings
5. Verify containers healthy
6. Report status

**Commands:**
```bash
# Validate
docker compose -f {compose_file} config

# Deploy
docker compose -f {compose_file} up -d

# Check health
docker compose -f {compose_file} ps
docker compose -f {compose_file} logs --tail=50
```

**Report:**
- Containers started
- Health status
- Any issues
"""

        return await self.run_task(prompt)

    async def configure_vpn(
        self,
        vpn_type: str,
        config_details: str
    ) -> TaskResult:
        """Configure VPN (WireGuard or Tailscale)"""
        await self.notify(f"Configuring {vpn_type} VPN")

        prompt = f"""
Configure {vpn_type} VPN:

{config_details}

**Include:**

## 1. Key Generation (if WireGuard)
```bash
wg genkey | tee privatekey | wg pubkey > publickey
```

## 2. Server Configuration
```ini
[Interface]
Address = 10.0.0.1/24
ListenPort = 51820
PrivateKey = <server_private_key>

[Peer]
PublicKey = <client_public_key>
AllowedIPs = 10.0.0.2/32
```

## 3. Client Configuration
```ini
[Interface]
Address = 10.0.0.2/24
PrivateKey = <client_private_key>

[Peer]
PublicKey = <server_public_key>
Endpoint = server:51820
AllowedIPs = 0.0.0.0/0
```

## 4. Firewall Rules
```bash
# Allow WireGuard
iptables -A INPUT -p udp --dport 51820 -j ACCEPT
# NAT for VPN clients
iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE
```

## 5. Testing
```bash
ping 10.0.0.1  # Test connectivity
wg show        # Check tunnel status
```

**DO NOT apply without approval.**
"""

        result = await self.run_task(prompt)

        if result.success:
            await self.request_approval(
                description=f"VPN configuration ready: {vpn_type}",
                details="Review before applying.",
                options=["Apply", "Reject", "Test First"]
            )
            result.needs_approval = True

        return result

    async def troubleshoot_network(self, issue: str) -> TaskResult:
        """Troubleshoot network issues"""
        await self.notify(f"Troubleshooting: {issue[:50]}")

        prompt = f"""
Troubleshoot network issue:

{issue}

**Diagnostic steps:**

## 1. Identify Symptoms
- What's failing?
- When did it start?
- What changed?

## 2. Connectivity Tests
```bash
ping <target>
traceroute <target>
mtr <target>
```

## 3. DNS Resolution
```bash
dig <domain>
nslookup <domain>
```

## 4. Port Connectivity
```bash
nc -zv <host> <port>
telnet <host> <port>
```

## 5. Service Status
```bash
systemctl status <service>
docker ps
kubectl get pods
```

## 6. Log Analysis
```bash
tail -f /var/log/syslog
journalctl -u <service>
docker logs <container>
```

## 7. Root Cause Analysis
[Identified cause]

## 8. Resolution Steps
1. [Step 1]
2. [Step 2]

## 9. Prevention
[How to prevent recurrence]
"""

        return await self.run_task(prompt)

    async def kubernetes_deployment(
        self,
        manifests_path: str,
        namespace: str = "default"
    ) -> TaskResult:
        """Deploy to Kubernetes"""
        await self.notify(f"K8s deployment: {manifests_path}")

        if namespace in ["production", "prod"]:
            await self.request_approval(
                description=f"K8s production deployment: {manifests_path}",
                details=f"Deploying to namespace: {namespace}",
                options=["Deploy", "Cancel"]
            )

        prompt = f"""
Deploy Kubernetes manifests from: {manifests_path}
Namespace: {namespace}

**Steps:**

## 1. Validate
```bash
kubectl apply --dry-run=client -f {manifests_path}
kubeval {manifests_path}
```

## 2. Check Resources
```bash
# Resource requests/limits
kubectl apply -f {manifests_path} --dry-run=server
```

## 3. Deploy
```bash
kubectl apply -f {manifests_path} -n {namespace}
```

## 4. Verify Rollout
```bash
kubectl rollout status deployment/<name> -n {namespace}
kubectl get pods -n {namespace}
```

## 5. Check Services
```bash
kubectl get svc -n {namespace}
kubectl get ingress -n {namespace}
```

## 6. Health Check
```bash
kubectl logs -l app=<name> -n {namespace} --tail=50
```

**Report:**
- Deployment status
- Pod health
- Service endpoints
- Any issues
"""

        return await self.run_task(prompt)

    async def security_audit(self, target: str) -> TaskResult:
        """Run infrastructure security audit"""
        prompt = f"""
Security audit on: {target}

**Check:**

## 1. Open Ports
```bash
nmap -sS -sV {target}
```

## 2. Firewall Rules
- External exposure
- Internal segmentation

## 3. SSL/TLS
- Certificate validity
- Protocol versions
- Cipher suites

## 4. Authentication
- SSH configuration
- API authentication
- Service accounts

## 5. Container Security
- Non-root users
- Resource limits
- Image vulnerabilities

## 6. Network Segmentation
- VLAN isolation
- Service mesh

**Findings:**

| Severity | Finding | Impact | Remediation |
|----------|---------|--------|-------------|
| Critical | ... | ... | ... |
| High | ... | ... | ... |
| Medium | ... | ... | ... |
"""

        return await self.run_task(prompt)

    async def setup_load_balancer(
        self,
        service: str,
        backend_servers: List[str],
        algorithm: str = "round-robin"
    ) -> TaskResult:
        """Configure load balancer with HAProxy/Nginx/Traefik"""
        await self.notify(f"Setting up load balancer for: {service}")

        backends_str = "\n".join(f"  - {s}" for s in backend_servers)

        prompt = f"""
Set up load balancer for service: {service}
Algorithm: {algorithm}
Backend servers:
{backends_str}

**Include:**

## 1. Load Balancer Selection
- Evaluate HAProxy vs Nginx vs Traefik for this use case
- L4 (TCP) vs L7 (HTTP) routing decision
- Justify selection based on requirements

## 2. HAProxy Configuration
```haproxy
global
    log /dev/log local0
    maxconn 4096
    stats socket /var/run/haproxy.sock mode 660

defaults
    mode http
    log global
    option httplog
    option dontlognull
    timeout connect 5s
    timeout client 30s
    timeout server 30s
    retries 3

frontend {service}_frontend
    bind *:80
    bind *:443 ssl crt /etc/ssl/certs/{service}.pem
    http-request redirect scheme https unless {{ ssl_fc }}
    default_backend {service}_backend

backend {service}_backend
    balance {algorithm.replace('-', '')}
    option httpchk GET /health
    http-check expect status 200
    default-server inter 3s fall 3 rise 2
{chr(10).join(f'    server srv{i+1} {s} check' for i, s in enumerate(backend_servers))}
```

## 3. Nginx Alternative
```nginx
upstream {service}_backend {{
    {algorithm.replace('-', '_')};
{chr(10).join(f'    server {s};' for s in backend_servers)}
}}

server {{
    listen 443 ssl;
    server_name {service}.example.com;

    ssl_certificate /etc/ssl/certs/{service}.pem;
    ssl_certificate_key /etc/ssl/private/{service}.key;

    location / {{
        proxy_pass http://{service}_backend;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }}

    location /health {{
        access_log off;
        return 200 "healthy";
    }}
}}
```

## 4. Health Check Configuration
- Active health checks: HTTP GET /health every 3s
- Passive health checks: Track 5xx responses
- Fall threshold: 3 consecutive failures
- Rise threshold: 2 consecutive successes
- Grace period: 30s on startup

## 5. SSL Termination
- Certificate management (Let's Encrypt / internal CA)
- TLS 1.2+ enforcement
- Cipher suite selection (ECDHE preferred)
- HSTS headers
- OCSP stapling

## 6. Sticky Sessions (if needed)
- Cookie-based affinity
- Session persistence timeout
- Drain connections gracefully

## 7. Monitoring Integration
- Export metrics to Prometheus
- HAProxy stats page / Nginx stub_status
- Alert on backend health changes
- Track response times per backend

## 8. Testing
```bash
# Verify configuration
haproxy -c -f /etc/haproxy/haproxy.cfg
nginx -t

# Test load distribution
for i in $(seq 1 10); do curl -s http://{service}.example.com/health; done

# Check backend health
curl http://localhost:9101/metrics  # HAProxy exporter
```

**Request approval before applying to production.**
"""

        result = await self.run_task(prompt)

        if result.success:
            await self.request_approval(
                description=f"Load balancer config ready for {service}",
                details=f"Algorithm: {algorithm}, Backends: {len(backend_servers)}",
                options=["Apply", "Reject", "Test First"]
            )
            result.needs_approval = True

        return result

    async def configure_dns(
        self,
        domain: str,
        records: List[dict],
        provider: str = "cloudflare"
    ) -> TaskResult:
        """Manage DNS records with failover and TTL optimization"""
        await self.notify(f"Configuring DNS for: {domain}")

        records_str = "\n".join(
            f"  - {r.get('type', 'A')} {r.get('name', '@')} -> {r.get('value', '')} (TTL: {r.get('ttl', 300)})"
            for r in records
        )

        prompt = f"""
Configure DNS for domain: {domain}
Provider: {provider}
Records:
{records_str}

**Include:**

## 1. DNS Record Configuration
| Type | Name | Value | TTL | Priority | Proxy |
|------|------|-------|-----|----------|-------|
{chr(10).join(f"| {r.get('type', 'A')} | {r.get('name', '@')} | {r.get('value', '')} | {r.get('ttl', 300)} | {r.get('priority', '-')} | {r.get('proxy', 'No')} |" for r in records)}

## 2. Record Type Guidance
- **A/AAAA** - Direct IP mapping, use for root domain or when CNAME not possible
- **CNAME** - Alias to another domain, cannot be used at zone apex
- **MX** - Mail exchange with priority values, ensure SPF/DKIM/DMARC alignment
- **TXT** - SPF records, DKIM keys, domain verification, DMARC policies
- **SRV** - Service discovery records (_service._proto.name)
- **CAA** - Certificate Authority Authorization, restrict who can issue certs

## 3. TTL Strategy
- **Pre-migration**: Lower TTL to 60s at least 48h before changes
- **Active failover records**: TTL 60-120s for fast failover
- **Stable records**: TTL 3600-86400s for reduced query load
- **MX records**: TTL 3600s (balance between stability and flexibility)
- **Post-migration**: Raise TTL back after verification

## 4. Failover Configuration
```
Primary:   A    {domain}  ->  <primary_ip>    (health-checked)
Secondary: A    {domain}  ->  <secondary_ip>  (failover)
```
- Health check endpoint: HTTPS GET /health
- Check interval: 30s
- Failover trigger: 3 consecutive failures
- Failback: Automatic after 60s of healthy responses

## 5. Split-Horizon DNS (if applicable)
- **Internal zone**: Private IPs for internal services
- **External zone**: Public IPs for external access
- Conditional forwarding rules
- VPN client resolution

## 6. {provider.title()} API Management
```bash
# List existing records
curl -X GET "https://api.cloudflare.com/client/v4/zones/ZONE_ID/dns_records" \\
  -H "Authorization: Bearer $CF_API_TOKEN"

# Create/update records
curl -X POST "https://api.cloudflare.com/client/v4/zones/ZONE_ID/dns_records" \\
  -H "Authorization: Bearer $CF_API_TOKEN" \\
  -H "Content-Type: application/json" \\
  --data '{{"type":"A","name":"{domain}","content":"<ip>","ttl":300}}'
```

## 7. Verification
```bash
# Check propagation
dig +short {domain} A
dig +short {domain} MX
dig +trace {domain}

# Verify from multiple locations
dig @8.8.8.8 {domain}
dig @1.1.1.1 {domain}

# Check DNSSEC
dig {domain} +dnssec
```

## 8. Security
- DNSSEC enabled and validated
- CAA records restricting certificate issuance
- SPF, DKIM, DMARC for email authentication
- API tokens scoped to minimal permissions

**Verify propagation before confirming completion.**
"""

        result = await self.run_task(prompt)

        if result.success:
            await self.request_approval(
                description=f"DNS configuration ready for {domain}",
                details=f"Provider: {provider}, Records: {len(records)}",
                options=["Apply", "Reject", "Review Records"]
            )
            result.needs_approval = True

        return result

    async def disaster_recovery_plan(
        self,
        services: List[str],
        rto: str,
        rpo: str
    ) -> TaskResult:
        """Create disaster recovery plan with backup strategy and failover procedures"""
        await self.notify(f"Creating DR plan for {len(services)} services (RTO: {rto}, RPO: {rpo})")

        services_str = "\n".join(f"  - {s}" for s in services)

        prompt = f"""
Create Disaster Recovery Plan:

Services:
{services_str}

Recovery Time Objective (RTO): {rto}
Recovery Point Objective (RPO): {rpo}

**Include:**

## 1. Service Classification
| Service | Tier | RTO | RPO | Dependencies | Failover Type |
|---------|------|-----|-----|-------------|---------------|
{chr(10).join(f"| {s} | TBD | {rto} | {rpo} | TBD | TBD |" for s in services)}

Tiers:
- **Tier 1 (Critical)**: Must recover within minutes, zero/near-zero data loss
- **Tier 2 (Important)**: Recover within hours, minimal data loss acceptable
- **Tier 3 (Standard)**: Recover within days, some data loss acceptable

## 2. Backup Strategy (3-2-1 Rule)
- **3 copies** of all critical data
- **2 different media types** (disk + object storage, or disk + tape)
- **1 offsite copy** (different region/provider)

### Backup Schedule
| Data Type | Method | Frequency | Retention | Storage | Encryption |
|-----------|--------|-----------|-----------|---------|------------|
| Databases | pg_dump / mysqldump | Every 6h | 30 days | S3 + Glacier | AES-256 |
| Application state | Volume snapshots | Daily | 14 days | Cross-region | AES-256 |
| Configuration | Git + encrypted vault | On change | Indefinite | Multi-repo | GPG |
| Secrets | Vault backup | Daily | 90 days | Offline + S3 | AES-256 |

### Backup Verification
- Automated restore testing weekly
- Checksum validation on all backups
- Alert on backup failures immediately

## 3. Failover Procedures

### Automated Failover
```
Trigger: Health check fails for 3 consecutive checks (90s)
  1. DNS failover activates (TTL: 60s)
  2. Load balancer removes unhealthy backends
  3. Standby services promoted to active
  4. Notification sent to on-call team
  5. Automated verification of failover health
```

### Manual Failover Runbook
```
Step 1: Confirm outage (check monitoring, not just alerts)
Step 2: Activate incident channel (#incident-YYYY-MM-DD)
Step 3: Execute failover:
  - DNS: Update records to DR site
  - LB: Switch traffic to DR backends
  - DB: Promote replica to primary
Step 4: Verify all services healthy
Step 5: Notify stakeholders
Step 6: Begin root cause analysis
```

### Failback Procedure
```
Step 1: Confirm primary site fully restored
Step 2: Sync data from DR site back to primary
Step 3: Verify data integrity (checksums, row counts)
Step 4: Gradual traffic shift (10% -> 25% -> 50% -> 100%)
Step 5: Monitor for 24h before decommissioning DR active state
```

## 4. DR Testing Schedule
| Test Type | Frequency | Scope | Duration |
|-----------|-----------|-------|----------|
| Tabletop exercise | Monthly | All teams | 2 hours |
| Component failover | Quarterly | Per service | 4 hours |
| Full DR drill | Semi-annually | All services | 8 hours |
| Chaos engineering | Continuous | Random | Automated |

### DR Test Checklist
- [ ] All backups verified restorable
- [ ] Failover completes within RTO
- [ ] Data loss within RPO
- [ ] Communication plan executed
- [ ] All runbooks accurate and current
- [ ] Lessons learned documented

## 5. Communication Plan
| Event | Notify | Channel | Template |
|-------|--------|---------|----------|
| Outage detected | On-call engineer | PagerDuty | incident-alert |
| DR activated | Engineering team | Slack #incidents | dr-activation |
| Customer impact | Support + Comms | Email + Status page | customer-impact |
| Recovery complete | All stakeholders | All channels | recovery-complete |

## 6. Runbook Template
For each service, create:
- Pre-conditions checklist
- Step-by-step recovery procedure
- Verification steps
- Rollback procedure
- Escalation contacts
- Estimated time per step

**Review and approve DR plan before scheduling first drill.**
"""

        result = await self.run_task(prompt)

        if result.success:
            await self.request_approval(
                description=f"DR plan ready for review ({len(services)} services)",
                details=f"RTO: {rto}, RPO: {rpo}. Review before scheduling DR drill.",
                options=["Approve", "Reject", "Request Changes"]
            )
            result.needs_approval = True

        return result

    async def setup_monitoring(
        self,
        infrastructure: List[str],
        services: List[str]
    ) -> TaskResult:
        """Set up Prometheus + Grafana monitoring stack with alerting"""
        await self.notify(f"Setting up monitoring for {len(services)} services on {len(infrastructure)} hosts")

        infra_str = "\n".join(f"  - {i}" for i in infrastructure)
        services_str = "\n".join(f"  - {s}" for s in services)

        prompt = f"""
Set up monitoring stack:

Infrastructure:
{infra_str}

Services:
{services_str}

**Include:**

## 1. Prometheus Configuration
```yaml
# prometheus.yml
global:
  scrape_interval: 15s
  evaluation_interval: 15s
  external_labels:
    cluster: production
    environment: prod

rule_files:
  - "alerts/*.yml"
  - "recording_rules/*.yml"

scrape_configs:
  - job_name: 'prometheus'
    static_configs:
      - targets: ['localhost:9090']

  - job_name: 'node-exporter'
    static_configs:
      - targets:
{chr(10).join(f"          - '{i}:9100'" for i in infrastructure)}

  - job_name: 'application'
    metrics_path: /metrics
    static_configs:
      - targets:
{chr(10).join(f"          - '{s}'" for s in services)}

  - job_name: 'blackbox'
    metrics_path: /probe
    params:
      module: [http_2xx]
    static_configs:
      - targets:
{chr(10).join(f"          - 'https://{s}'" for s in services)}
    relabel_configs:
      - source_labels: [__address__]
        target_label: __param_target
      - target_label: __address__
        replacement: blackbox-exporter:9115

alerting:
  alertmanagers:
    - static_configs:
        - targets: ['alertmanager:9093']
```

## 2. Alerting Rules
```yaml
# alerts/infrastructure.yml
groups:
  - name: infrastructure
    rules:
      - alert: HighCPUUsage
        expr: 100 - (avg by(instance) (rate(node_cpu_seconds_total{{mode="idle"}}[5m])) * 100) > 80
        for: 5m
        labels:
          severity: warning
        annotations:
          summary: "High CPU usage on {{{{ $labels.instance }}}}"
          description: "CPU usage is above 80% for 5 minutes."

      - alert: HighMemoryUsage
        expr: (1 - node_memory_MemAvailable_bytes / node_memory_MemTotal_bytes) * 100 > 85
        for: 5m
        labels:
          severity: warning
        annotations:
          summary: "High memory usage on {{{{ $labels.instance }}}}"

      - alert: DiskSpaceLow
        expr: (1 - node_filesystem_avail_bytes / node_filesystem_size_bytes) * 100 > 90
        for: 5m
        labels:
          severity: critical
        annotations:
          summary: "Disk space critically low on {{{{ $labels.instance }}}}"

      - alert: ServiceDown
        expr: up == 0
        for: 1m
        labels:
          severity: critical
        annotations:
          summary: "Service {{{{ $labels.job }}}} is down on {{{{ $labels.instance }}}}"

      - alert: HighErrorRate
        expr: rate(http_requests_total{{status=~"5.."}}[5m]) / rate(http_requests_total[5m]) > 0.05
        for: 5m
        labels:
          severity: critical
        annotations:
          summary: "High error rate (>5%) on {{{{ $labels.instance }}}}"

      - alert: HighLatency
        expr: histogram_quantile(0.95, rate(http_request_duration_seconds_bucket[5m])) > 1
        for: 5m
        labels:
          severity: warning
        annotations:
          summary: "High p95 latency on {{{{ $labels.instance }}}}"
```

## 3. Alertmanager Configuration
```yaml
# alertmanager.yml
global:
  resolve_timeout: 5m

route:
  group_by: ['alertname', 'cluster']
  group_wait: 10s
  group_interval: 10s
  repeat_interval: 1h
  receiver: 'default'
  routes:
    - match:
        severity: critical
      receiver: 'pagerduty-critical'
      continue: true
    - match:
        severity: warning
      receiver: 'slack-warnings'

receivers:
  - name: 'default'
    slack_configs:
      - channel: '#monitoring'
        send_resolved: true

  - name: 'pagerduty-critical'
    pagerduty_configs:
      - service_key: '<pagerduty_key>'
        severity: 'critical'

  - name: 'slack-warnings'
    slack_configs:
      - channel: '#monitoring-warnings'
        send_resolved: true

inhibit_rules:
  - source_match:
      severity: 'critical'
    target_match:
      severity: 'warning'
    equal: ['alertname', 'instance']
```

## 4. Grafana Dashboards

### Infrastructure Dashboard (RED Method)
- **Rate**: Requests per second per service
- **Errors**: Error rate percentage per service
- **Duration**: p50/p95/p99 latency per service

### System Dashboard (USE Method)
- **Utilization**: CPU, memory, disk, network bandwidth
- **Saturation**: Load average, memory pressure, disk I/O wait
- **Errors**: System errors, OOM kills, disk errors

### SLA Dashboard
- Uptime percentage (target: 99.9%)
- Error budget remaining
- SLO burn rate
- Incident count and MTTR

### Per-Service Dashboard
- Request rate and error rate
- Latency histograms
- Active connections
- Resource consumption (CPU, memory)

## 5. SLA Monitoring
```yaml
# recording_rules/sla.yml
groups:
  - name: sla
    rules:
      - record: sla:availability:ratio
        expr: 1 - (sum(rate(http_requests_total{{status=~"5.."}}[30d])) / sum(rate(http_requests_total[30d])))

      - record: sla:error_budget:remaining
        expr: 1 - ((1 - sla:availability:ratio) / (1 - 0.999))
```

## 6. Docker Compose Deployment
```yaml
# docker-compose.monitoring.yml
services:
  prometheus:
    image: prom/prometheus:latest
    volumes:
      - ./prometheus:/etc/prometheus
      - prometheus_data:/prometheus
    ports:
      - "9090:9090"
    restart: unless-stopped

  grafana:
    image: grafana/grafana:latest
    volumes:
      - grafana_data:/var/lib/grafana
      - ./grafana/dashboards:/etc/grafana/provisioning/dashboards
    ports:
      - "3000:3000"
    environment:
      - GF_SECURITY_ADMIN_PASSWORD=${{GRAFANA_PASSWORD}}
    restart: unless-stopped

  alertmanager:
    image: prom/alertmanager:latest
    volumes:
      - ./alertmanager:/etc/alertmanager
    ports:
      - "9093:9093"
    restart: unless-stopped

  node-exporter:
    image: prom/node-exporter:latest
    ports:
      - "9100:9100"
    restart: unless-stopped

  blackbox-exporter:
    image: prom/blackbox-exporter:latest
    ports:
      - "9115:9115"
    restart: unless-stopped

volumes:
  prometheus_data:
  grafana_data:
```

## 7. Verification
```bash
# Check Prometheus targets
curl http://localhost:9090/api/v1/targets

# Check Alertmanager
curl http://localhost:9093/api/v2/status

# Verify Grafana
curl http://localhost:3000/api/health

# Test alert firing
curl -X POST http://localhost:9093/api/v2/alerts -d '[{{"labels":{{"alertname":"test"}}}}]'
```

**Deploy monitoring stack and verify all targets are up.**
"""

        return await self.run_task(prompt)

    async def configure_service_mesh(
        self,
        services: List[str],
        mesh_type: str = "istio"
    ) -> TaskResult:
        """Configure service mesh with mTLS and traffic management"""
        await self.notify(f"Configuring {mesh_type} service mesh for {len(services)} services")

        services_str = "\n".join(f"  - {s}" for s in services)

        prompt = f"""
Configure {mesh_type} service mesh:

Services:
{services_str}

**Include:**

## 1. Mesh Installation
{"### Istio" if mesh_type == "istio" else "### Linkerd"}
```bash
{"# Install Istio with demo profile" if mesh_type == "istio" else "# Install Linkerd"}
{"istioctl install --set profile=production" if mesh_type == "istio" else "linkerd install | kubectl apply -f -"}

# Enable sidecar injection for namespace
{"kubectl label namespace default istio-injection=enabled" if mesh_type == "istio" else "kubectl annotate namespace default linkerd.io/inject=enabled"}

# Verify installation
{"istioctl verify-install" if mesh_type == "istio" else "linkerd check"}
```

## 2. Mutual TLS (mTLS)
{"```yaml" if mesh_type == "istio" else "```yaml"}
{'''# PeerAuthentication - enforce mTLS
apiVersion: security.istio.io/v1beta1
kind: PeerAuthentication
metadata:
  name: default
  namespace: default
spec:
  mtls:
    mode: STRICT''' if mesh_type == "istio" else '''# Linkerd auto-enables mTLS
# Verify mTLS status
# linkerd viz edges deployment
# linkerd viz tap deployment/<name> --namespace default'''}
```

## 3. Traffic Management
```yaml
{'''# VirtualService - traffic routing
apiVersion: networking.istio.io/v1beta1
kind: VirtualService
metadata:
  name: service-routing
spec:
  hosts:
    - "*.default.svc.cluster.local"
  http:
    - route:
        - destination:
            host: service-v1
          weight: 90
        - destination:
            host: service-v2
          weight: 10
      retries:
        attempts: 3
        perTryTimeout: 2s
      timeout: 10s''' if mesh_type == "istio" else '''# TrafficSplit for canary
apiVersion: split.smi-spec.io/v1alpha1
kind: TrafficSplit
metadata:
  name: service-split
spec:
  service: service-root
  backends:
    - service: service-v1
      weight: 900m
    - service: service-v2
      weight: 100m'''}
```

## 4. Circuit Breaker
```yaml
{'''# DestinationRule with circuit breaker
apiVersion: networking.istio.io/v1beta1
kind: DestinationRule
metadata:
  name: circuit-breaker
spec:
  host: "*.default.svc.cluster.local"
  trafficPolicy:
    connectionPool:
      tcp:
        maxConnections: 100
      http:
        h2UpgradePolicy: DEFAULT
        http1MaxPendingRequests: 100
        http2MaxRequests: 1000
    outlierDetection:
      consecutive5xxErrors: 5
      interval: 10s
      baseEjectionTime: 30s
      maxEjectionPercent: 50''' if mesh_type == "istio" else '''# Linkerd uses retry budgets and timeouts
# Configure via ServiceProfile
apiVersion: linkerd.io/v1alpha2
kind: ServiceProfile
metadata:
  name: service.default.svc.cluster.local
spec:
  routes:
    - name: GET /api
      condition:
        method: GET
        pathRegex: /api/.*
      isRetryable: true
      timeout: 5s'''}
```

## 5. Fault Injection (Testing)
```yaml
{'''# Inject faults for chaos testing
apiVersion: networking.istio.io/v1beta1
kind: VirtualService
metadata:
  name: fault-injection
spec:
  hosts:
    - service-a
  http:
    - fault:
        delay:
          percentage:
            value: 10
          fixedDelay: 5s
        abort:
          percentage:
            value: 5
          httpStatus: 503
      route:
        - destination:
            host: service-a''' if mesh_type == "istio" else '''# Linkerd fault injection via HTTPRoute
# Use with chaos engineering tools like Chaos Mesh or Litmus'''}
```

## 6. Observability
```bash
# Distributed tracing
{"kubectl apply -f https://raw.githubusercontent.com/istio/istio/release-1.20/samples/addons/jaeger.yaml" if mesh_type == "istio" else "linkerd viz install | kubectl apply -f -"}

# Service graph
{"kubectl apply -f https://raw.githubusercontent.com/istio/istio/release-1.20/samples/addons/kiali.yaml" if mesh_type == "istio" else "linkerd viz dashboard &"}

# Metrics
{"kubectl apply -f https://raw.githubusercontent.com/istio/istio/release-1.20/samples/addons/prometheus.yaml" if mesh_type == "istio" else "linkerd viz stat deployment --namespace default"}
```

## 7. Per-Service Configuration
{chr(10).join(f"### {s}" + chr(10) + f"- Sidecar injection: enabled" + chr(10) + f"- mTLS: STRICT" + chr(10) + f"- Retry policy: 3 attempts, 2s timeout" + chr(10) + f"- Circuit breaker: 5 consecutive 5xx errors" for s in services)}

## 8. Verification
```bash
# Check sidecar injection
kubectl get pods -n default -o jsonpath='{{.items[*].spec.containers[*].name}}'

# Verify mTLS
{"istioctl authn tls-check" if mesh_type == "istio" else "linkerd viz edges deployment"}

# Check traffic flow
{"istioctl proxy-status" if mesh_type == "istio" else "linkerd viz top deployment"}
```

**Request approval before enabling in production namespace.**
"""

        result = await self.run_task(prompt)

        if result.success:
            await self.request_approval(
                description=f"{mesh_type.title()} service mesh config ready",
                details=f"Services: {len(services)}, mTLS: STRICT",
                options=["Apply", "Reject", "Test in Staging"]
            )
            result.needs_approval = True

        return result

    async def setup_cdn(
        self,
        domain: str,
        origin: str,
        cache_rules: List[dict]
    ) -> TaskResult:
        """Configure CDN and edge computing with cache policies"""
        await self.notify(f"Setting up CDN for: {domain}")

        rules_str = "\n".join(
            f"  - Path: {r.get('path', '/*')}, TTL: {r.get('ttl', '86400')}, "
            f"Cache: {r.get('cache', 'standard')}"
            for r in cache_rules
        )

        prompt = f"""
Configure CDN for domain: {domain}
Origin: {origin}
Cache rules:
{rules_str}

**Include:**

## 1. CDN Provider Selection
- Evaluate Cloudflare vs CloudFront vs Fastly
- Consider: geographic distribution, edge features, pricing, DDoS protection

## 2. Origin Configuration
```
Origin server: {origin}
Origin protocol: HTTPS
Origin port: 443
Origin timeout: 30s
Origin retries: 3
Origin shield: enabled (closest PoP to origin)
```

## 3. Cache Rules
| Path Pattern | TTL | Cache Level | Edge TTL | Browser TTL | Bypass Conditions |
|-------------|-----|-------------|----------|-------------|-------------------|
{chr(10).join(f"| {r.get('path', '/*')} | {r.get('ttl', '86400')} | {r.get('cache', 'standard')} | {r.get('edge_ttl', r.get('ttl', '86400'))} | {r.get('browser_ttl', '3600')} | {r.get('bypass', 'none')} |" for r in cache_rules)}

### Cache-Control Headers
```
# Static assets (images, CSS, JS)
Cache-Control: public, max-age=31536000, immutable

# API responses (if cacheable)
Cache-Control: public, max-age=60, stale-while-revalidate=300

# Dynamic content (no cache)
Cache-Control: private, no-cache, no-store

# HTML pages
Cache-Control: public, max-age=300, stale-while-revalidate=600
```

## 4. Edge Configuration (Cloudflare Workers example)
```javascript
// Edge routing / A/B testing
addEventListener('fetch', event => {{
  event.respondWith(handleRequest(event.request));
}});

async function handleRequest(request) {{
  const url = new URL(request.url);

  // Custom cache key
  const cacheKey = new Request(url.toString(), request);
  const cache = caches.default;

  // Check cache first
  let response = await cache.match(cacheKey);
  if (response) return response;

  // Fetch from origin
  response = await fetch(request);

  // Clone and cache
  const responseClone = response.clone();
  response = new Response(responseClone.body, responseClone);
  response.headers.set('X-Cache', 'MISS');
  response.headers.set('Cache-Control', 'public, max-age=3600');

  event.waitUntil(cache.put(cacheKey, response.clone()));
  return response;
}}
```

## 5. Purge Strategy
```bash
# Purge by URL
curl -X POST "https://api.cloudflare.com/client/v4/zones/ZONE_ID/purge_cache" \\
  -H "Authorization: Bearer $CF_API_TOKEN" \\
  -d '{{"files":["https://{domain}/path/to/resource"]}}'

# Purge by cache tag
curl -X POST "https://api.cloudflare.com/client/v4/zones/ZONE_ID/purge_cache" \\
  -H "Authorization: Bearer $CF_API_TOKEN" \\
  -d '{{"tags":["product-page","static-assets"]}}'

# Purge everything (use sparingly)
curl -X POST "https://api.cloudflare.com/client/v4/zones/ZONE_ID/purge_cache" \\
  -H "Authorization: Bearer $CF_API_TOKEN" \\
  -d '{{"purge_everything":true}}'
```

## 6. Security at the Edge
- **DDoS Protection**: Rate limiting, challenge pages, IP reputation
- **WAF Rules**: OWASP core ruleset, custom rules, bot management
- **SSL/TLS**: Full (strict) mode, minimum TLS 1.2, HSTS enabled
- **Origin Protection**: Authenticated origin pulls, IP allowlisting

## 7. Performance Optimization
- **Minification**: HTML, CSS, JavaScript
- **Image Optimization**: WebP/AVIF conversion, lazy loading, responsive images
- **Brotli Compression**: Enable for text-based assets
- **HTTP/3**: Enable QUIC for improved performance
- **Early Hints**: 103 status code for preloading critical resources
- **Prefetch**: Speculative prefetching of likely next pages

## 8. Monitoring & Analytics
- Cache hit ratio (target: >90%)
- Origin response times
- Edge response times
- Bandwidth saved
- Error rates by PoP
- Geographic distribution of traffic

## 9. Verification
```bash
# Check CDN headers
curl -I https://{domain}/ | grep -E "(cf-|x-cache|cache-control|age)"

# Verify SSL
openssl s_client -connect {domain}:443 -servername {domain}

# Test cache hit
curl -sI https://{domain}/static/style.css | grep "cf-cache-status"
# First request: MISS, second request: HIT

# Performance test
curl -w "@curl-format.txt" -o /dev/null -s https://{domain}/
```

**Review cache rules and security settings before activating.**
"""

        result = await self.run_task(prompt)

        if result.success:
            await self.request_approval(
                description=f"CDN configuration ready for {domain}",
                details=f"Origin: {origin}, Cache rules: {len(cache_rules)}",
                options=["Activate", "Reject", "Test First"]
            )
            result.needs_approval = True

        return result

    async def work(self, task: str) -> TaskResult:
        """General infrastructure work"""
        await self.notify(f"Starting: {task[:50]}...")
        return await self.run_task(task)


async def main():
    """CLI entry point"""
    import argparse
    import json

    parser = argparse.ArgumentParser(description="Quinn - Network Engineer Agent")
    parser.add_argument("--design", type=str, help="Design network for requirements")
    parser.add_argument("--deploy", type=str, help="Deploy compose file")
    parser.add_argument("--env", type=str, default="staging", help="Environment")
    parser.add_argument("--vpn", type=str, help="VPN type (wireguard/tailscale)")
    parser.add_argument("--vpn-config", type=str, help="VPN configuration")
    parser.add_argument("--troubleshoot", type=str, help="Troubleshoot issue")
    parser.add_argument("--k8s", type=str, help="K8s manifests path")
    parser.add_argument("--namespace", type=str, default="default", help="K8s namespace")
    parser.add_argument("--audit", type=str, help="Security audit target")
    parser.add_argument("--load-balancer", type=str, help="Service name for load balancer setup")
    parser.add_argument("--backends", type=str, nargs="+", help="Backend server addresses")
    parser.add_argument("--algorithm", type=str, default="round-robin",
                        choices=["round-robin", "least-connections", "weighted", "ip-hash", "random"],
                        help="Load balancing algorithm")
    parser.add_argument("--dns", type=str, help="Domain for DNS configuration")
    parser.add_argument("--dns-records", type=str, help="JSON array of DNS records")
    parser.add_argument("--dns-provider", type=str, default="cloudflare", help="DNS provider")
    parser.add_argument("--dr-plan", type=str, nargs="+", help="Services for disaster recovery plan")
    parser.add_argument("--rto", type=str, default="4h", help="Recovery Time Objective")
    parser.add_argument("--rpo", type=str, default="1h", help="Recovery Point Objective")
    parser.add_argument("--monitoring", action="store_true", help="Set up monitoring stack")
    parser.add_argument("--infra-hosts", type=str, nargs="+", help="Infrastructure hosts to monitor")
    parser.add_argument("--monitor-services", type=str, nargs="+", help="Services to monitor")
    parser.add_argument("--service-mesh", type=str, nargs="+", help="Services for service mesh")
    parser.add_argument("--mesh-type", type=str, default="istio",
                        choices=["istio", "linkerd"], help="Service mesh type")
    parser.add_argument("--cdn", type=str, help="Domain for CDN setup")
    parser.add_argument("--origin", type=str, help="Origin server for CDN")
    parser.add_argument("--cache-rules", type=str, help="JSON array of cache rules")
    parser.add_argument("--task", type=str, help="Run general task")
    parser.add_argument("--status", action="store_true", help="Show status")

    args = parser.parse_args()

    agent = QuinnAgent()

    if args.status:
        print(json.dumps(agent.get_status(), indent=2))
        return

    if args.design:
        result = await agent.design_network(args.design)
        print(result.output)
        return

    if args.deploy:
        result = await agent.deploy_containers(args.deploy, args.env)
        print(result.output)
        return

    if args.vpn and args.vpn_config:
        result = await agent.configure_vpn(args.vpn, args.vpn_config)
        print(result.output)
        return

    if args.troubleshoot:
        result = await agent.troubleshoot_network(args.troubleshoot)
        print(result.output)
        return

    if args.k8s:
        result = await agent.kubernetes_deployment(args.k8s, args.namespace)
        print(result.output)
        return

    if args.audit:
        result = await agent.security_audit(args.audit)
        print(result.output)
        return

    if args.load_balancer and args.backends:
        result = await agent.setup_load_balancer(
            args.load_balancer, args.backends, args.algorithm
        )
        print(result.output)
        return

    if args.dns and args.dns_records:
        records = json.loads(args.dns_records)
        result = await agent.configure_dns(args.dns, records, args.dns_provider)
        print(result.output)
        return

    if args.dr_plan:
        result = await agent.disaster_recovery_plan(args.dr_plan, args.rto, args.rpo)
        print(result.output)
        return

    if args.monitoring and args.infra_hosts and args.monitor_services:
        result = await agent.setup_monitoring(args.infra_hosts, args.monitor_services)
        print(result.output)
        return

    if args.service_mesh:
        result = await agent.configure_service_mesh(args.service_mesh, args.mesh_type)
        print(result.output)
        return

    if args.cdn and args.origin:
        cache_rules = json.loads(args.cache_rules) if args.cache_rules else [{"path": "/*", "ttl": "86400"}]
        result = await agent.setup_cdn(args.cdn, args.origin, cache_rules)
        print(result.output)
        return

    if args.task:
        result = await agent.work(args.task)
        print(result.output)
        return

    print("Quinn - Network Engineer & Deployment Specialist")
    print("=================================================")
    print("Use --help for options")
    print()
    print("Capabilities:")
    print("  --design          Design network architecture")
    print("  --deploy          Deploy containers (Docker Compose)")
    print("  --vpn             Configure VPN (WireGuard/Tailscale)")
    print("  --troubleshoot    Troubleshoot network issues")
    print("  --k8s             Kubernetes deployment")
    print("  --audit           Security audit")
    print("  --load-balancer   Set up load balancer (HAProxy/Nginx/Traefik)")
    print("  --dns             Configure DNS records and failover")
    print("  --dr-plan         Create disaster recovery plan")
    print("  --monitoring      Set up Prometheus + Grafana monitoring")
    print("  --service-mesh    Configure service mesh (Istio/Linkerd)")
    print("  --cdn             Set up CDN and edge computing")
    print("  --task            Run general infrastructure task")


if __name__ == "__main__":
    asyncio.run(main())
