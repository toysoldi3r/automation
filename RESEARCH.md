# Market research

Last updated: 2026-08-07

Automation infrastructure added on this date does not change the evidence level
or validate the leading hypothesis. It makes future hourly research and product
iterations reproducible on a single review branch.

## Evidence standard and current limitation

This first run established a candidate comparison, not demand validation. An
attempt to search public GitHub issues through the GitHub API failed because this
environment's outbound tunnel returned HTTP 403; the configured web-search tool
also returned HTTP 401. No search results, customers, interviews, or demand
metrics are claimed. Links below are a verification queue based on known product
documentation and must be checked before being treated as current evidence.

Evidence strength used here:

1. first-hand incident and paid/pilot commitment;
2. repeated public reports with identifiable contexts;
3. product documentation showing a limitation or manual workflow;
4. inference or hypothesis (never presented as observed demand).

## Candidate comparison

Scores are preliminary hypotheses on a 1–5 scale (5 is favorable). “Evidence” is
scored low because live sources and users have not yet been validated.

| Candidate | Severity | Weak alternatives | Evidence | WTP | Feasibility | Distribution | Low maintenance | Revenue | Total / 40 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Scheduled GitHub Actions reliability monitor | 4 | 3 | 2 | 3 | 4 | 3 | 3 | 3 | 25 |
| GitHub Actions cost anomaly attribution | 4 | 2 | 2 | 4 | 3 | 3 | 2 | 4 | 24 |
| Webhook payload contract-drift monitor | 4 | 2 | 2 | 3 | 3 | 2 | 2 | 3 | 21 |
| Dependabot noise prioritizer | 3 | 2 | 3 | 2 | 4 | 2 | 3 | 2 | 21 |

The totals compare what to validate first; they do not establish a market.

## Leading hypothesis: scheduled Actions reliability

### Problem and target customer

Scheduled workflows may perform backups, synchronization, reporting, cleanup, or
release automation. A run that starts late or never starts can remain invisible
because there is no failed run to notify on. The proposed customer is a small
software team or platform owner with several business-relevant scheduled Actions
and no dedicated workflow-observability platform.

The differentiator to test is **zero instrumentation**: install a narrowly scoped
GitHub App, discover schedules, and alert when expected runs do not appear. Most
dead-man-switch monitors instead ask every job to send a success ping. Whether
avoiding that setup is valuable enough to buy remains an open question.

### Alternatives and competition to verify

- GitHub scheduled workflow documentation and caveats:
  <https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows#schedule>
- GitHub Actions monitoring/alerts:
  <https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows/notifications-for-workflow-runs>
- Healthchecks.io cron monitoring: <https://healthchecks.io/>
- Better Stack cron monitoring: <https://betterstack.com/cron-job-monitoring>
- Cronitor: <https://cronitor.io/cron-job-monitoring>
- Sentry Crons: <https://docs.sentry.io/product/crons/>

General cron monitors are mature, creating meaningful competition. The opportunity
exists only if automatic discovery, GitHub-native ownership, and missing-run
detection remove enough recurring setup or risk to motivate switching/payment.

### Monetization hypothesis

Test $12/month for 20 scheduled workflows and $29/month for an organization tier,
with a short free trial. Pricing is an interview instrument, not evidence of
willingness to pay. A plausible buyer is an engineering lead paying to reduce the
risk and investigation time of silent automation failures.

### Principal risks

- GitHub may already provide adequate notifications or add native missing-run
  detection.
- GitHub API permissions/rate limits may make reliable, low-trust detection hard.
- General cron monitors may be cheap and “add one ping” may not be painful.
- Schedule semantics, queued runs, disabled workflows, default-branch changes,
  and repository inactivity can create false alarms and high support cost.
- Reaching teams at the moment they experience the problem may be difficult.

## Other candidates

### GitHub Actions cost anomaly attribution

Recurring risk and a clearer budget owner suggest willingness to pay, but GitHub
already exposes usage/billing information and CI-optimization vendors compete in
this space. Required verification queue:

- <https://docs.github.com/en/billing/managing-billing-for-your-products/managing-billing-for-github-actions>
- <https://docs.github.com/en/enterprise-cloud@latest/billing/reference/actions-minute-multipliers>

Rejected for this validation cycle because API/data availability, native reports,
and vendor competition could leave little defensible gap.

### Webhook contract-drift monitor

Provider payload changes or undocumented assumptions can cause incidents, but
Hookdeck, Svix, webhook gateways, contract tests, and observability vendors make
the category fragmented rather than obviously underserved. A proxy also handles
sensitive payloads, increasing trust and maintenance costs. Deprioritized pending
first-hand evidence of a narrower provider-specific pain.

### Dependabot noise prioritizer

Public developer discussion frequently centers on dependency-update volume, but
GitHub configuration, grouping, auto-merge tooling, Renovate, and security tools
already address much of it. Distribution is difficult and willingness to pay for
another prioritization layer appears weaker than for operational risk. Rejected
unless interviews identify a narrow compliance or audit workflow.

## Questions that can invalidate the leader

1. When did a scheduled GitHub workflow last run late or go missing, and what was
   the consequence?
2. How was it detected, and how long did diagnosis/remediation take?
3. Why is workflow failure notification or an external success ping inadequate?
4. How many important schedules exist, and who owns their reliability budget?
5. What App permissions and data retention would be unacceptable?
6. Would the team install a pilot now? If successful, would it pay $12 or $29 per
   month? If not, what existing alternative wins and why?
