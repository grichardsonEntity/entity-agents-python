"""
Base Configuration for Entity Agents

Shared configuration patterns for all agents.
"""

import os
from dataclasses import dataclass, field
from typing import Optional, List, Dict
from enum import Enum
from pathlib import Path


class PermissionMode(Enum):
    """Agent permission levels"""
    MANUAL = "manual"
    ACCEPT_EDITS = "acceptEdits"
    ACCEPT_ALL = "acceptAll"


@dataclass
class MCPServerConfig:
    """Configuration for an MCP server connection"""
    name: str
    enabled: bool = False
    command: Optional[str] = None
    args: List[str] = field(default_factory=list)
    env: Dict[str, str] = field(default_factory=dict)


@dataclass
class NotificationConfig:
    """Notification settings for agents"""
    file_enabled: bool = True
    file_path: str = "~/entity-agents/logs/notifications.log"
    macos_enabled: bool = True
    sms_enabled: bool = False
    sms_phone: str = ""
    email_enabled: bool = False
    email_address: str = ""
    github_enabled: bool = True


@dataclass
class BaseConfig:
    """Base configuration for all agents"""

    # Identity
    name: str = "Agent"
    role: str = "General Agent"

    # Model settings
    model: str = "claude-sonnet-4-20250514"
    planning_model: str = "claude-opus-4-20250514"

    # Permissions
    permission_mode: PermissionMode = PermissionMode.ACCEPT_EDITS

    # Project settings (set per-project via CLAUDE.md)
    project_root: str = "."
    output_dir: str = "./output"

    # Allowed operations
    allowed_tools: List[str] = field(default_factory=lambda: [
        "Read", "Write", "Edit", "Glob", "Grep", "Bash",
    ])

    # Allowed bash patterns
    allowed_bash_patterns: List[str] = field(default_factory=lambda: [
        "git *",
        "gh *",
        "python *",
        "pip *",
        "npm *",
        "docker *",
    ])

    # Blocked dangerous commands
    blocked_bash_patterns: List[str] = field(default_factory=lambda: [
        "rm -rf /",
        "rm -rf ~",
        "> /dev/*",
        "mkfs *",
    ])

    # File access
    allowed_paths: List[str] = field(default_factory=lambda: ["*"])
    blocked_paths: List[str] = field(default_factory=lambda: [
        "~/.ssh/id_*",
        "~/.aws/credentials",
        "*/.env*",
        "*/secrets/*",
    ])

    # Notifications
    notifications: NotificationConfig = field(default_factory=NotificationConfig)

    # MCP Servers
    mcp_servers: Dict[str, MCPServerConfig] = field(default_factory=dict)

    # GitHub integration
    github_repo: str = ""
    github_labels: List[str] = field(default_factory=list)

    # System prompt (set per-agent)
    system_prompt: str = "You are a helpful AI agent."

    def get_project_root(self) -> Path:
        """Get expanded project root path"""
        return Path(self.project_root).expanduser().resolve()

    def get_output_dir(self) -> Path:
        """Get expanded output directory path"""
        return Path(self.output_dir).expanduser().resolve()
