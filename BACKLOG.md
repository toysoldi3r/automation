# Backlog

Items are ordered. Product implementation is blocked by the validation gate in
[ROADMAP.md](ROADMAP.md).

## Now — market validation

1. Recruit maintainers via public repositories containing `schedule:` workflows;
   do not collect private contact data or send bulk unsolicited messages.
2. Use a neutral interview script: ask about the last failure, discovery path,
   consequences, frequency, and current workaround before describing a solution.
3. Record anonymized interview notes, explicit permission for any quotation, and
   evidence strength in `RESEARCH.md`.
4. Verify GitHub documentation, pricing, API limits, App permissions, and native
   monitoring behavior when network access is available.
5. Test willingness to pay with two offers: $12/month for up to 20 scheduled
   workflows and $29/month for an organization tier. These are experiments, not
   validated prices.
6. Produce an alternative teardown for GitHub-native notifications,
   Healthchecks.io, Better Stack, Cronitor, Sentry Crons, and general workflow
   observability products.

## Next — only after Gate 1 passes

- Write the smallest end-to-end technical design.
- Create a threat model and minimal-permissions review.
- Prototype schedule parsing, including POSIX cron edge cases and time zones.
- Prototype GitHub run reconciliation and missed-run grace periods.
- Add deterministic tests before connecting to live repositories.

## Explicitly not planned

- A generic uptime-monitoring platform.
- AI-generated incident summaries before reliable detection exists.
- Additional CI providers before GitHub demand is demonstrated.
- Dashboards or analytics without a validated buying use case.
