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


def _step(workflow: str, name: str) -> str:
    marker = f"      - name: {name}"
    assert workflow.count(marker) == 1
    step = workflow.split(marker, maxsplit=1)[1]
    return step.split("\n      - name:", maxsplit=1)[0]


def _script_commands(step: str) -> list[str]:
    script = step.split("        run: |", maxsplit=1)[1]
    return [
        line.strip()
        for line in script.splitlines()
        if line.strip() and not line.lstrip().startswith("#")
    ]


def _git_commands(commands: list[str], subcommand: str) -> list[str]:
    pattern = rf"^git\s+{re.escape(subcommand)}(?:\s|$)"
    return [command for command in commands if re.match(pattern, command)]


def test_hourly_publish_never_hides_sync_failures_or_force_pushes():
    """The data writer must fail closed when main cannot be fast-forwarded."""
    workflow = _workflow_text()
    publish_step = _step(workflow, "Commit, rebase and push public data safely")

    assert "git-auto-commit-action" not in workflow
    assert not re.search(r"--force(?:-with-lease)?\b", workflow)
    assert not re.search(r"^\s*git\s+push\s+[^\n]*\+\S+", workflow, re.MULTILINE)
    assert not re.search(r"git\s+pull[^\n]*\|\|\s*true", workflow)
    assert "continue-on-error" not in publish_step
    assert "||" not in publish_step


def test_hourly_publish_commits_before_rebase_and_fast_forward_push():
    """A local data commit must exist before synchronization can touch main."""
    publish_step = _step(
        _workflow_text(), "Commit, rebase and push public data safely"
    )
    commands = _script_commands(publish_step)

    expected_stage = "git add -A -- 'data/public/*.json' 'data/public/*.md'"
    expected_commit = 'git commit -m "data: hourly refresh [skip ci]"'
    expected_fetch = "git fetch origin main"
    expected_rebase = "git rebase origin/main"
    expected_push = "git push origin HEAD:main"

    assert _git_commands(commands, "add") == [expected_stage]
    assert _git_commands(commands, "commit") == [expected_commit]
    assert _git_commands(commands, "fetch") == [expected_fetch]
    assert _git_commands(commands, "rebase") == [expected_rebase]
    assert _git_commands(commands, "push") == [expected_push]

    stage = commands.index(expected_stage)
    no_change = commands.index("if git diff --cached --quiet; then")
    no_change_exit = commands.index("exit 0")
    no_change_end = commands.index("fi")
    commit = commands.index(expected_commit)
    fetch = commands.index(expected_fetch)
    rebase = commands.index(expected_rebase)
    push = commands.index(expected_push)

    assert stage < no_change < no_change_exit < no_change_end < commit
    assert commit < fetch < rebase < push
    assert commands.index("set -euo pipefail") < stage
    assert [command for command in commands if re.match(r"^exit(?:\s|$)", command)] == [
        "exit 0"
    ]


def test_hourly_publish_is_restricted_to_main_ref():
    """Manual dispatches from another ref must fail before checkout or writes."""
    workflow = _workflow_text()
    guard_name = "Require main branch"
    checkout_name = "Checkout"
    guard_marker = f"      - name: {guard_name}"
    checkout_marker = f"      - name: {checkout_name}"

    assert workflow.index(guard_marker) < workflow.index(checkout_marker)

    guard_step = _step(workflow, guard_name)
    guard_commands = _script_commands(guard_step)
    assert "WATCHDOG_GITHUB_REF: ${{ github.ref }}" in guard_step
    assert guard_commands == [
        "set -euo pipefail",
        'if [[ "$WATCHDOG_GITHUB_REF" != "refs/heads/main" ]]; then',
        'echo "::error::Refusing to publish from $WATCHDOG_GITHUB_REF; '
        'expected refs/heads/main."',
        "exit 1",
        "fi",
    ]

    checkout_step = _step(workflow, checkout_name)
    assert re.search(r"(?m)^\s{10}ref:\s*main\s*$", checkout_step)
