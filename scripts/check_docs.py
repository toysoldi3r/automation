#!/usr/bin/env python3
"""Fail when required product-discovery documents or local Markdown links drift."""

from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parent.parent
REQUIRED = ("ROADMAP.md", "BACKLOG.md", "RESEARCH.md", "DECISIONS.md")
LINK = re.compile(r"\[[^]]+\]\(([^)]+)\)")


def errors() -> list[str]:
    problems: list[str] = []
    for name in REQUIRED:
        path = ROOT / name
        if not path.is_file():
            problems.append(f"missing required document: {name}")

    for path in ROOT.glob("*.md"):
        for target in LINK.findall(path.read_text(encoding="utf-8")):
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            local_target = target.split("#", 1)[0]
            if local_target and not (path.parent / local_target).exists():
                problems.append(f"{path.name}: broken local link: {target}")
    return problems


def main() -> int:
    problems = errors()
    if problems:
        print("\n".join(problems), file=sys.stderr)
        return 1
    print("documentation checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
