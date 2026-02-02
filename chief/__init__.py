"""
Chief of Staff Agent
Executive Assistant & Project Orchestrator
"""

from .agent import ChiefOfStaffAgent
from .config import chief_config, MONITORED_PROJECTS, PYTHON_AGENTS, NODE_AGENTS

__all__ = [
    "ChiefOfStaffAgent",
    "chief_config",
    "MONITORED_PROJECTS",
    "PYTHON_AGENTS",
    "NODE_AGENTS",
]
