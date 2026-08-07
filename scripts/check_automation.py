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
        "actions/checkout@v5": "current checkout action",
        "openai/codex-action@v1": "official Codex action",
        "openai-api-key: ${{ secrets.OPENAI_API_KEY }}": "Codex authentication",
        "prompt-file: AUTOMATION_PROMPT.md": "repository prompt execution",
        'permission-profile: ":workspace"': "workspace permission profile",
        "./scripts/test.sh": "test command",
        "git commit": "automatic commit",
        "git push": "automatic push",
        "gh pr list --state open": "existing pull-request lookup",
    }
    for text, label in required_workflow_text.items():
        if text not in workflow:
            problems.append(f"workflow is missing {label}: {text}")

    action_at = workflow.find("openai/codex-action@v1")
    test_at = workflow.find("./scripts/test.sh")
    commit_at = workflow.find("git commit")
    if min(action_at, test_at, commit_at) < 0 or not action_at < test_at < commit_at:
        problems.append("Codex Action, repository tests, and commit must run in that order")

    if "Do not run `git commit`" not in prompt:
        problems.append("prompt must delegate commits to the tested workflow")

    forbidden_workflow_text = {
        "--full-auto": "unsupported --full-auto fallback",
        "npm install --global @openai/codex": "manual Codex CLI installation",
        "codex exec": "manual Codex CLI invocation",
    }
    for text, label in forbidden_workflow_text.items():
        if text in workflow:
            problems.append(f"workflow contains {label}: {text}")

    if problems:
        print("\n".join(problems), file=sys.stderr)
        return 1
    print("automation checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
