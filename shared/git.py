"""
Git Client - Git operations for agents
"""

import subprocess
from dataclasses import dataclass
from pathlib import Path
from typing import List, Optional


@dataclass
class CommitResult:
    """Result of a git commit"""
    success: bool
    hash: Optional[str]
    files: List[str]
    message: str


class GitClient:
    """Git operations client"""

    def __init__(self, repo_path: str = "."):
        self.repo_path = Path(repo_path).expanduser().resolve()

    def _run_git(self, args: List[str]) -> subprocess.CompletedProcess:
        """Run git command"""
        return subprocess.run(
            ["git"] + args,
            cwd=self.repo_path,
            capture_output=True,
            text=True
        )

    def status(self) -> str:
        """Get git status"""
        result = self._run_git(["status", "--short"])
        return result.stdout

    def diff(self, staged: bool = False) -> str:
        """Get git diff"""
        args = ["diff"]
        if staged:
            args.append("--staged")
        result = self._run_git(args)
        return result.stdout

    def add(self, paths: List[str] = None):
        """Stage files"""
        if paths is None:
            paths = ["."]
        self._run_git(["add"] + paths)

    def commit(self, message: str, issue_number: Optional[int] = None) -> CommitResult:
        """Create a commit"""
        # Get staged files
        staged = self._run_git(["diff", "--staged", "--name-only"])
        files = staged.stdout.strip().split("\n") if staged.stdout.strip() else []

        # Build commit message
        full_message = message
        if issue_number:
            full_message += f"\n\nCloses #{issue_number}"
        full_message += "\n\nCo-Authored-By: Claude <noreply@anthropic.com>"

        # Commit
        result = self._run_git(["commit", "-m", full_message])

        if result.returncode != 0:
            return CommitResult(
                success=False,
                hash=None,
                files=files,
                message=result.stderr
            )

        # Get commit hash
        hash_result = self._run_git(["rev-parse", "HEAD"])
        commit_hash = hash_result.stdout.strip()[:8]

        return CommitResult(
            success=True,
            hash=commit_hash,
            files=files,
            message=message
        )

    def push(self, remote: str = "origin", branch: Optional[str] = None) -> bool:
        """Push to remote"""
        args = ["push", remote]
        if branch:
            args.append(branch)
        result = self._run_git(args)
        return result.returncode == 0

    def pull(self, remote: str = "origin", branch: Optional[str] = None) -> bool:
        """Pull from remote"""
        args = ["pull", remote]
        if branch:
            args.append(branch)
        result = self._run_git(args)
        return result.returncode == 0

    def checkout(self, branch: str, create: bool = False) -> bool:
        """Checkout branch"""
        args = ["checkout"]
        if create:
            args.append("-b")
        args.append(branch)
        result = self._run_git(args)
        return result.returncode == 0

    def current_branch(self) -> str:
        """Get current branch name"""
        result = self._run_git(["branch", "--show-current"])
        return result.stdout.strip()

    def log(self, count: int = 5) -> str:
        """Get recent commit log"""
        result = self._run_git(["log", f"-{count}", "--oneline"])
        return result.stdout
