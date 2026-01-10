"""
Entity Agents - Shared Utilities

Common functionality for all agents.
"""

from .base_agent import BaseAgent, TaskResult, ApprovalRequest
from .config import BaseConfig, NotificationConfig, MCPServerConfig, PermissionMode
from .notifier import Notifier
from .github import GitHubClient
from .git import GitClient

__all__ = [
    "BaseAgent",
    "TaskResult",
    "ApprovalRequest",
    "BaseConfig",
    "NotificationConfig",
    "MCPServerConfig",
    "PermissionMode",
    "Notifier",
    "GitHubClient",
    "GitClient",
]
