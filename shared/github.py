"""
GitHub Client - Interact with GitHub API

Uses gh CLI for authentication and API calls.
"""

import json
import subprocess
from dataclasses import dataclass
from typing import List, Optional


@dataclass
class GitHubIssue:
    """Represents a GitHub issue"""
    number: int
    title: str
    body: str
    state: str
    labels: List[str]
    assignees: List[str]
    url: str


@dataclass
class GitHubPR:
    """Represents a GitHub pull request"""
    number: int
    title: str
    body: str
    state: str
    head: str
    base: str
    url: str


class GitHubClient:
    """GitHub API client using gh CLI"""

    def __init__(self, repo: str):
        self.repo = repo

    def _run_gh(self, args: List[str]) -> str:
        """Run gh CLI command"""
        cmd = ["gh"] + args + ["--repo", self.repo]
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode != 0:
            raise Exception(f"gh command failed: {result.stderr}")
        return result.stdout

    def get_issues(
        self,
        labels: Optional[List[str]] = None,
        state: str = "open",
        limit: int = 30
    ) -> List[GitHubIssue]:
        """Get issues from repository"""
        args = ["issue", "list", "--state", state, "--limit", str(limit), "--json",
                "number,title,body,state,labels,assignees,url"]

        if labels:
            args.extend(["--label", ",".join(labels)])

        output = self._run_gh(args)
        data = json.loads(output)

        return [
            GitHubIssue(
                number=item["number"],
                title=item["title"],
                body=item.get("body", ""),
                state=item["state"],
                labels=[l["name"] for l in item.get("labels", [])],
                assignees=[a["login"] for a in item.get("assignees", [])],
                url=item["url"],
            )
            for item in data
        ]

    def get_issue(self, number: int) -> Optional[GitHubIssue]:
        """Get a specific issue"""
        try:
            args = ["issue", "view", str(number), "--json",
                    "number,title,body,state,labels,assignees,url"]
            output = self._run_gh(args)
            item = json.loads(output)

            return GitHubIssue(
                number=item["number"],
                title=item["title"],
                body=item.get("body", ""),
                state=item["state"],
                labels=[l["name"] for l in item.get("labels", [])],
                assignees=[a["login"] for a in item.get("assignees", [])],
                url=item["url"],
            )
        except Exception:
            return None

    def create_issue(
        self,
        title: str,
        body: str,
        labels: Optional[List[str]] = None
    ) -> GitHubIssue:
        """Create a new issue"""
        args = ["issue", "create", "--title", title, "--body", body]

        if labels:
            for label in labels:
                args.extend(["--label", label])

        args.extend(["--json", "number,title,body,state,labels,assignees,url"])

        output = self._run_gh(args)
        item = json.loads(output)

        return GitHubIssue(
            number=item["number"],
            title=item["title"],
            body=item.get("body", ""),
            state=item["state"],
            labels=[l["name"] for l in item.get("labels", [])],
            assignees=[a["login"] for a in item.get("assignees", [])],
            url=item["url"],
        )

    def add_label(self, issue_number: int, label: str):
        """Add label to issue"""
        self._run_gh(["issue", "edit", str(issue_number), "--add-label", label])

    def remove_label(self, issue_number: int, label: str):
        """Remove label from issue"""
        self._run_gh(["issue", "edit", str(issue_number), "--remove-label", label])

    def add_comment(self, issue_number: int, body: str):
        """Add comment to issue"""
        self._run_gh(["issue", "comment", str(issue_number), "--body", body])

    def close_issue(self, issue_number: int):
        """Close an issue"""
        self._run_gh(["issue", "close", str(issue_number)])

    def get_prs(self, state: str = "open", limit: int = 30) -> List[GitHubPR]:
        """Get pull requests"""
        args = ["pr", "list", "--state", state, "--limit", str(limit), "--json",
                "number,title,body,state,headRefName,baseRefName,url"]

        output = self._run_gh(args)
        data = json.loads(output)

        return [
            GitHubPR(
                number=item["number"],
                title=item["title"],
                body=item.get("body", ""),
                state=item["state"],
                head=item["headRefName"],
                base=item["baseRefName"],
                url=item["url"],
            )
            for item in data
        ]

    def create_pr(
        self,
        title: str,
        body: str,
        head: str,
        base: str = "main"
    ) -> GitHubPR:
        """Create a pull request"""
        args = ["pr", "create", "--title", title, "--body", body,
                "--head", head, "--base", base,
                "--json", "number,title,body,state,headRefName,baseRefName,url"]

        output = self._run_gh(args)
        item = json.loads(output)

        return GitHubPR(
            number=item["number"],
            title=item["title"],
            body=item.get("body", ""),
            state=item["state"],
            head=item["headRefName"],
            base=item["baseRefName"],
            url=item["url"],
        )
