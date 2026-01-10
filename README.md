# Entity Agents - Python Edition

A team of 11 specialized autonomous AI agents for software development, powered by Claude.

## Quick Start

```python
from entity_agents import get_agent

# Get an agent by name
valentina = get_agent("valentina")

# Run a task
result = await valentina.fix_bug(123)
print(result.output)
```

## Agents

| Agent | Role | Specialty |
|-------|------|-----------|
| **Valentina** | UI Developer | React, Flask/Jinja2, CSS, accessibility |
| **Sydney** | Senior Backend Developer | Python, FastAPI, databases, Docker |
| **Amber** | Systems Architect | System design, microservices, APIs |
| **Victoria** | AI Researcher | LLMs, embeddings, RAG, vector DBs |
| **Brett Jr** | Cybersecurity Specialist | Security audits, auth, encryption |
| **Tango** | QA Tester | pytest, Jest, testing strategies |
| **Sugar** | Documentation Specialist | Technical writing, API docs, diagrams |
| **Sophie** | Mobile Developer | React Native, PWA, iOS, Android |
| **Asheton** | Product Strategist | Requirements, roadmap, prioritization |
| **Maxwell** | Data Research Engineer | Web scraping, ETL, databases |
| **Harper** | Grant Researcher & Writer | Funding, proposals, compliance |
| **Quinn** | Network Engineer | Infrastructure, Docker, K8s, VPN |

## Installation

```bash
pip install entity-agents

# Or from source
git clone https://github.com/grichardsonEntity/entity-agents-python.git
cd entity-agents-python
pip install -e .
```

## Requirements

- Python 3.10+
- Claude CLI installed and configured (`claude` command available)

## Usage

### Direct Import

```python
from entity_agents import SydneyAgent, ValentinaAgent

# Create agent instances
sydney = SydneyAgent()
valentina = ValentinaAgent()

# Run specialized tasks
await sydney.create_endpoint("POST", "/api/users", "Create a new user")
await valentina.create_component("Button", "Accessible button component")
```

### CLI Usage

Each agent has a CLI interface:

```bash
# Sydney - Backend Developer
python -m entity_agents.sydney --endpoint POST /api/users --description "Create user"

# Valentina - UI Developer
python -m entity_agents.valentina --component Button --description "Primary button"

# Tango - QA Tester
python -m entity_agents.tango --write src/utils.py --type unit

# Quinn - Network Engineer
python -m entity_agents.quinn --deploy docker-compose.yml --env staging
```

### Agent Status

```bash
python -m entity_agents.sydney --status
```

## Configuration

Each agent can be configured with custom settings:

```python
from entity_agents.shared import BaseConfig, NotificationConfig

config = BaseConfig(
    name="Sydney",
    role="Senior Backend Developer",
    project_root="/path/to/project",
    github_repo="owner/repo",
    notifications=NotificationConfig(
        file_enabled=True,
        macos_enabled=True,
        sms_enabled=True,
        sms_phone="+1234567890"
    )
)

sydney = SydneyAgent(config)
```

## Notifications

Agents can notify via:

- **File logging** - Writes to `.entity-agents/logs/`
- **macOS notifications** - Native desktop notifications
- **SMS (iMessage)** - Via macOS Messages app

## Approval Workflow

Dangerous operations require approval:

```python
# This will request approval before deploying to production
await quinn.deploy_containers("docker-compose.yml", environment="production")

# Check pending approvals
print(quinn.pending_approvals)
```

## Project Structure

```
entity-agents-python/
├── shared/             # Base classes and utilities
│   ├── base_agent.py   # BaseAgent class
│   ├── config.py       # Configuration dataclasses
│   ├── notifier.py     # Notification system
│   ├── github.py       # GitHub API client
│   └── git.py          # Git operations
├── valentina/          # UI Developer
├── sydney/             # Backend Developer
├── amber/              # Systems Architect
├── victoria/           # AI Researcher
├── brettjr/            # Cybersecurity
├── tango/              # QA Tester
├── sugar/              # Documentation
├── sophie/             # Mobile Developer
├── asheton/            # Product Strategist
├── maxwell/            # Data Engineer
├── harper/             # Grant Writer
└── quinn/              # Network Engineer
```

## License

MIT

## Links

- [Entity Agents (Prompt Files)](https://github.com/grichardsonEntity/entity-agents)
- [Entity Agents Node](https://github.com/grichardsonEntity/entity-agents-node)
