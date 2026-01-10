"""
Entity Agents - Python Edition

A team of 11 specialized autonomous AI agents for software development.
"""

from .shared import BaseAgent, BaseConfig, TaskResult, ApprovalRequest

# Agent imports
from .valentina import ValentinaAgent, valentina_config
from .sydney import SydneyAgent, sydney_config
from .amber import AmberAgent, amber_config
from .victoria import VictoriaAgent, victoria_config
from .brettjr import BrettJrAgent, brettjr_config
from .tango import TangoAgent, tango_config
from .sugar import SugarAgent, sugar_config
from .sophie import SophieAgent, sophie_config
from .asheton import AshetonAgent, asheton_config
from .maxwell import MaxwellAgent, maxwell_config
from .harper import HarperAgent, harper_config
from .quinn import QuinnAgent, quinn_config

__version__ = "1.0.0"

__all__ = [
    # Base classes
    "BaseAgent",
    "BaseConfig",
    "TaskResult",
    "ApprovalRequest",
    # Agents
    "ValentinaAgent",
    "SydneyAgent",
    "AmberAgent",
    "VictoriaAgent",
    "BrettJrAgent",
    "TangoAgent",
    "SugarAgent",
    "SophieAgent",
    "AshetonAgent",
    "MaxwellAgent",
    "HarperAgent",
    "QuinnAgent",
    # Configs
    "valentina_config",
    "sydney_config",
    "amber_config",
    "victoria_config",
    "brettjr_config",
    "tango_config",
    "sugar_config",
    "sophie_config",
    "asheton_config",
    "maxwell_config",
    "harper_config",
    "quinn_config",
]

# Agent registry for dynamic access
AGENTS = {
    "valentina": ValentinaAgent,
    "sydney": SydneyAgent,
    "amber": AmberAgent,
    "victoria": VictoriaAgent,
    "brettjr": BrettJrAgent,
    "tango": TangoAgent,
    "sugar": SugarAgent,
    "sophie": SophieAgent,
    "asheton": AshetonAgent,
    "maxwell": MaxwellAgent,
    "harper": HarperAgent,
    "quinn": QuinnAgent,
}


def get_agent(name: str) -> BaseAgent:
    """Get an agent instance by name"""
    name_lower = name.lower().replace(" ", "").replace("-", "")
    if name_lower not in AGENTS:
        raise ValueError(f"Unknown agent: {name}. Available: {list(AGENTS.keys())}")
    return AGENTS[name_lower]()
