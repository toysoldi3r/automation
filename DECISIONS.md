# Decision log

## 2026-08-07 — validate scheduled GitHub Actions reliability first

**Status:** provisional; no product implementation authorized yet.

**Context:** The repository contained no product direction or research. Four
automation-adjacent candidates were compared. Live discovery was attempted, but
the web-search service returned HTTP 401 and direct GitHub API access was blocked
by an outbound HTTP 403. It would be misleading to call any direction validated.

**Decision:** Start interviews and current-alternative verification for a
zero-instrumentation monitor that detects missing or late scheduled GitHub Actions
runs. Its hypothesized advantage is a narrow, recurring operational risk and less
setup than ping-based cron monitors. Delay software construction until the explicit
validation gate in `ROADMAP.md` passes.

**Why not build now:** Code would test technical feasibility but not the weakest
assumptions: incident frequency, dissatisfaction with existing monitors, App trust,
distribution, and willingness to pay.

**Reversal criteria:** Stop or pivot if interviews show the problem is rare,
failure notifications are adequate, teams will not grant the minimum GitHub App
permissions, three qualified pilot teams cannot be found, or no buyer commits to
the proposed price after a successful pilot. Re-rank candidates if verified
evidence materially changes the preliminary scores.

## 2026-08-07 — use a tested persistent branch for hourly automation

**Status:** accepted.

**Decision:** A scheduled GitHub Actions job executes the versioned
`AUTOMATION_PROMPT.md`, runs the repository-owned test entry point, and commits
only after it passes. All runs reuse `automation/hourly-product`; the job looks for
an open pull request before creating one, so routine runs update the same review
surface.

**Rationale:** Keeping the prompt and tests in version control makes behavior
reviewable. Separating agent edits from workflow-owned commit/push operations
enforces the test-before-commit ordering. Concurrency and a timeout prevent hourly
runs from racing on the shared branch.

**Trade-offs:** Installing the current official Codex npm package at run time is
less reproducible than pinning a version, but avoids silently freezing the agent
on an obsolete release. Changes remain review-gated and never self-merge. Revisit
this choice if upstream release drift causes failures; pin a verified version and
schedule dependency updates instead.
