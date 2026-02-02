"""
Shelly Agent
Chief of Staff - Executive Assistant & Project Orchestrator
"""

from .agent import ShellyAgent
from .config import shelly_config, MONITORED_PROJECTS, PYTHON_AGENTS, NODE_AGENTS

__all__ = [
    "ShellyAgent",
    "shelly_config",
    "MONITORED_PROJECTS",
    "PYTHON_AGENTS",
    "NODE_AGENTS",
]
