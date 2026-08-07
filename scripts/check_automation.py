#!/usr/bin/env python3
"""Check safety-critical invariants of the hourly automation workflow."""

from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parent.parent
WORKFLOW = ROOT / ".github/workflows/hourly-autonomous-engineering.yml"
PROMPT = ROOT / "AUTOMATION_PROMPT.md"


def main() -> int:
    problems: list[str] = []
    workflow = WORKFLOW.read_text(encoding="utf-8") if WORKFLOW.exists() else ""
    prompt = PROMPT.read_text(encoding="utf-8") if PROMPT.exists() else ""

    required_workflow_text = {
        'cron: "7 * * * *"': "hourly cron schedule",
        "automation/hourly-product": "persistent automation branch",
        "< AUTOMATION_PROMPT.md": "repository prompt execution",
        "./scripts/test.sh": "test command",
        "git commit": "automatic commit",
        "git push": "automatic push",
        "gh pr list --state open": "existing pull-request lookup",
    }
    for text, label in required_workflow_text.items():
        if text not in workflow:
            problems.append(f"workflow is missing {label}: {text}")

    test_at = workflow.find("./scripts/test.sh")
    commit_at = workflow.find("git commit")
    if test_at < 0 or commit_at < 0 or test_at > commit_at:
        problems.append("repository tests must run before the automatic commit")

    if "Do not run `git commit`" not in prompt:
        problems.append("prompt must delegate commits to the tested workflow")

    if problems:
        print("\n".join(problems), file=sys.stderr)
        return 1
    print("automation checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
