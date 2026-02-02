"""
Entity Agents - Python Edition

A team of 12 specialized autonomous AI agents for software development.

Team:
- Shelly: Chief of Staff - Executive Assistant & Project Orchestrator
- Sydney: Full Stack Developer (merged Sydney + original Valentina)
- Valentina: Technical Writer & Content Strategist (merged Sugar + Harper)
- Vera: Cloud & AI Platform Specialist (GCP, Vertex AI, HIPAA)
- Amber: Systems Architect
- Victoria: AI Researcher
- BrettJr: Cybersecurity Specialist
- Tango: QA Tester
- Sophie: Mobile Developer
- Asheton: Product Strategist
- Maxwell: Data Research Engineer
- Quinn: Network Engineer
"""

from .shared import BaseAgent, BaseConfig, TaskResult, ApprovalRequest

# Agent imports
from .shelly import ShellyAgent, shelly_config
from .sydney import SydneyAgent, sydney_config
from .valentina import ValentinaAgent, valentina_config
from .amber import AmberAgent, amber_config
from .victoria import VictoriaAgent, victoria_config
from .brettjr import BrettJrAgent, brettjr_config
from .tango import TangoAgent, tango_config
from .sophie import SophieAgent, sophie_config
from .asheton import AshetonAgent, asheton_config
from .maxwell import MaxwellAgent, maxwell_config
from .quinn import QuinnAgent, quinn_config
from .vera import VeraAgent, vera_config

__version__ = "2.2.0"

__all__ = [
    # Base classes
    "BaseAgent",
    "BaseConfig",
    "TaskResult",
    "ApprovalRequest",
    # Agents
    "ShellyAgent",
    "SydneyAgent",
    "ValentinaAgent",
    "AmberAgent",
    "VictoriaAgent",
    "BrettJrAgent",
    "TangoAgent",
    "SophieAgent",
    "AshetonAgent",
    "MaxwellAgent",
    "QuinnAgent",
    "VeraAgent",
    # Configs
    "shelly_config",
    "sydney_config",
    "valentina_config",
    "amber_config",
    "victoria_config",
    "brettjr_config",
    "tango_config",
    "sophie_config",
    "asheton_config",
    "maxwell_config",
    "quinn_config",
    "vera_config",
]

# Agent registry for dynamic access
AGENTS = {
    "shelly": ShellyAgent,
    "sydney": SydneyAgent,
    "valentina": ValentinaAgent,
    "amber": AmberAgent,
    "victoria": VictoriaAgent,
    "brettjr": BrettJrAgent,
    "tango": TangoAgent,
    "sophie": SophieAgent,
    "asheton": AshetonAgent,
    "maxwell": MaxwellAgent,
    "quinn": QuinnAgent,
    "vera": VeraAgent,
}


def get_agent(name: str) -> BaseAgent:
    """Get an agent instance by name"""
    name_lower = name.lower().replace(" ", "").replace("-", "")
    if name_lower not in AGENTS:
        raise ValueError(f"Unknown agent: {name}. Available: {list(AGENTS.keys())}")
    return AGENTS[name_lower]()
