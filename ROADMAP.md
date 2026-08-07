# Roadmap

## Current stage: problem validation

Do not build the service until the validation gate below is met. The product
hypothesis is a GitHub App that discovers scheduled GitHub Actions, detects late
or missing runs without requiring workflow edits, and alerts the owning team.

Hourly autonomous iterations now run through a persistent review branch. They may
advance research and repository tooling, but must not bypass the validation gate.

### Gate 1 — validate the problem (next)

- Interview at least 10 maintainers or platform engineers who operate scheduled
  Actions workflows.
- Obtain at least 5 first-hand examples of a missed or materially delayed job.
- Confirm how incidents are detected today and quantify response effort.
- Ask for a concrete commitment (pilot installation or paid design partnership),
  rather than treating positive opinions as purchase intent.
- Recheck GitHub's current native capabilities and at least five alternatives.

**Pass condition:** at least three qualified teams report the problem monthly or
more often, lack an acceptable existing solution, and agree to install a pilot;
at least one agrees to pay the proposed entry price if the pilot meets agreed
reliability criteria. Otherwise pivot or stop.

### Gate 2 — concierge pilot

- Define permissions, retention, deletion, and false-alarm budgets.
- Manually onboard 3–5 design partners.
- Build only schedule discovery, expected-run calculation, run ingestion, and one
  alert channel.
- Measure detection accuracy and operator response; do not infer value from app
  installs alone.

### Gate 3 — paid minimum viable product

- Add self-service GitHub App installation and billing.
- Publish a transparent reliability model and security documentation.
- Add organization-level status and alert routing only when pilot evidence shows
  they affect purchase or retention.

### Later, evidence-dependent

- Historical duration/regression alerts.
- Incident timelines and audit exports.
- Support for non-GitHub schedulers.
