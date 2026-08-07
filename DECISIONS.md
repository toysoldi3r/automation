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
