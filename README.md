# Automation product discovery

This repository is in **market-discovery**, not product-build, mode. The current
working hypothesis is a zero-instrumentation reliability monitor for scheduled
GitHub Actions. It is deliberately provisional: the next milestone is validating
the problem with maintainers before implementation.

Project state is recorded in:

- [ROADMAP.md](ROADMAP.md) — stage gates and milestones
- [BACKLOG.md](BACKLOG.md) — ordered work, including validation interviews
- [RESEARCH.md](RESEARCH.md) — evidence, alternatives, and candidate comparison
- [DECISIONS.md](DECISIONS.md) — decisions and their reversal criteria

## Documentation check

Run the repository's current test suite with:

```sh
python3 scripts/check_docs.py
```
