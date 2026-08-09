"""Regression checks for workflows that write directly to ``main``."""

from __future__ import annotations

import re
from pathlib import Path


WORKFLOW = (
    Path(__file__).resolve().parents[1]
    / ".github"
    / "workflows"
    / "scrape_hourly.yml"
)


def _workflow_text() -> str:
    return WORKFLOW.read_text(encoding="utf-8")


def _publish_step(workflow: str) -> str:
    marker = "      - name: Commit, rebase and push public data safely"
    step = workflow.split(marker, maxsplit=1)[1]
    return step.split("\n      - name:", maxsplit=1)[0]


def test_hourly_publish_never_hides_sync_failures_or_force_pushes():
    """The data writer must fail closed when main cannot be fast-forwarded."""
    workflow = _workflow_text()
    publish_step = _publish_step(workflow)

    assert "git-auto-commit-action" not in workflow
    assert not re.search(r"--force(?:-with-lease)?\b", workflow)
    assert not re.search(r"git\s+pull[^\n]*\|\|\s*true", workflow)
    assert "continue-on-error" not in publish_step
    assert "||" not in publish_step


def test_hourly_publish_commits_before_rebase_and_fast_forward_push():
    """A local data commit must exist before synchronization can touch main."""
    publish_step = _publish_step(_workflow_text())
    commands = [line.strip() for line in publish_step.splitlines()]

    stage = commands.index("git add -A -- 'data/public/*.json' 'data/public/*.md'")
    commit = commands.index('git commit -m "data: hourly refresh [skip ci]"')
    fetch = commands.index("git fetch origin main")
    rebase = commands.index("git rebase origin/main")
    push = commands.index("git push origin HEAD:main")

    assert stage < commit < fetch < rebase < push
    assert commands.index("set -euo pipefail") < stage
