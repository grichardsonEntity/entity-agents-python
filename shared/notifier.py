"""
Notifier - Send notifications from agents

Supports: file logging, macOS notifications, SMS (iMessage), email
"""

import subprocess
from datetime import datetime
from pathlib import Path
from typing import Optional

from .config import NotificationConfig


class Notifier:
    """Send notifications through various channels"""

    def __init__(self, agent_name: str, config: NotificationConfig):
        self.agent_name = agent_name
        self.config = config
        self._setup_log_file()

    def _setup_log_file(self):
        """Create log directory if needed"""
        if self.config.file_enabled:
            log_path = Path(self.config.file_path).expanduser()
            log_path.parent.mkdir(parents=True, exist_ok=True)

    def notify(self, message: str, level: str = "info"):
        """Send notification through all enabled channels"""
        timestamp = datetime.now().isoformat()
        formatted = f"[{timestamp}] [{level.upper()}] {self.agent_name}: {message}"

        # File logging
        if self.config.file_enabled:
            self._log_to_file(formatted)

        # macOS notification
        if self.config.macos_enabled:
            self._macos_notify(message, level)

        # SMS via iMessage
        if self.config.sms_enabled and self.config.sms_phone:
            self._sms_notify(message)

        # Always print to console
        print(formatted)

    def _log_to_file(self, message: str):
        """Write to log file"""
        try:
            log_path = Path(self.config.file_path).expanduser()
            with open(log_path, "a") as f:
                f.write(message + "\n")
        except Exception as e:
            print(f"Failed to write to log: {e}")

    def _macos_notify(self, message: str, level: str = "info"):
        """Send macOS notification"""
        try:
            title = f"{self.agent_name}"
            if level == "error":
                title += " - Error"
            elif level == "approval":
                title += " - Approval Needed"

            subprocess.run([
                "osascript", "-e",
                f'display notification "{message}" with title "{title}"'
            ], check=True, capture_output=True)
        except Exception:
            pass

    def _sms_notify(self, message: str):
        """Send SMS via macOS iMessage"""
        try:
            phone = self.config.sms_phone
            sms_msg = f"{self.agent_name}: {message}"
            subprocess.run([
                "osascript", "-e",
                f'''tell application "Messages"
                    set targetService to 1st account whose service type = iMessage
                    set targetBuddy to participant "{phone}" of targetService
                    send "{sms_msg}" to targetBuddy
                end tell'''
            ], check=True, capture_output=True)
        except Exception as e:
            print(f"SMS notification failed: {e}")

    def info(self, message: str):
        """Send info notification"""
        self.notify(message, "info")

    def error(self, message: str):
        """Send error notification"""
        self.notify(message, "error")

    def approval(self, message: str):
        """Send approval request notification"""
        self.notify(message, "approval")

    def success(self, message: str):
        """Send success notification"""
        self.notify(message, "success")
