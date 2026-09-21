# Automation product discovery

> [!IMPORTANT]
> Workflow fixes do not take effect until this branch is merged into the default
> branch. If a failed run still shows commit `6c52558` or
> `actions/checkout@v4`, it is running the old workflow—not the fix in this
> repository state. Merge first, then start a new run; do not re-run the old job.

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

## Hourly autonomous runner

The workflow in
[`.github/workflows/hourly-autonomous-engineering.yml`](.github/workflows/hourly-autonomous-engineering.yml)
runs at minute 17 of every hour and can also be started manually. It continues a
single `automation/hourly-product` branch, asks the official Codex action for one
focused improvement, runs `./scripts/test.sh`, and only then commits and pushes.
It creates a pull request when necessary and retries PR creation on later runs,
even when the agent made no new change in that later run.

The agent does not receive the repository's `GITHUB_TOKEN`: checkout credentials
are not persisted, and the token is scoped to the branch preparation, publish,
and pull-request steps. Changes therefore remain reviewable rather than being
written directly to the default branch.

### Enable the hourly runner

1. **Merge the pull request containing this workflow into the default branch.**
   Scheduled runs only load workflow definitions from the default branch. A
   re-run also uses the workflow from the original run's commit, so re-running
   an older failure does not test a workflow fix made by a later commit.
2. In **Settings → Secrets and variables → Actions**, add a repository secret
   named `OPENAI_API_KEY`.
3. In **Settings → Actions → General → Workflow permissions**, select **Read and
   write permissions** and enable **Allow GitHub Actions to create and approve
   pull requests**. Organization policy can override these repository settings.
4. Ensure Actions are enabled for the repository and keep this workflow file on
   the default branch. GitHub only schedules workflows from the default branch.
5. Open **Actions → Hourly autonomous engineering → Run workflow**, select the
   updated default branch, and start a new run. Confirm its title contains the
   commit SHA that includes this workflow before relying on the result.

When a new-version run fails, open its **Summary**. The final diagnostic step
lists the outcome of secret validation, branch preparation, Codex, tests,
publishing, and PR creation, so an exit code is tied to the responsible stage.

Scheduled runs are best-effort and may be delayed. The non-round minute reduces
contention, but this workflow is an engineering loop—not a precision scheduler
or production availability mechanism.

### Diagnose a failed run

- **Missing `OPENAI_API_KEY`:** add the secret under the exact name above. The
  preflight step fails with a direct error before invoking Codex.
- **Push returns HTTP 403:** grant Actions read/write workflow permissions and
  check whether an organization policy restricts the repository token.
- **`gh pr create` is forbidden:** enable the pull-request setting in step 2.
  The next hourly run retries creation even if it produces no additional commit.
- **Branch merge conflict:** resolve the conflict on
  `automation/hourly-product` or delete that branch after preserving wanted
  changes; the next run recreates it from the default branch.
- **No scheduled runs:** confirm the workflow exists on the default branch and
  has not been disabled. Use `workflow_dispatch` to distinguish configuration
  failures from scheduler delays.
- **A run still shows `actions/checkout@v4`:** that run is executing the old
  workflow. The current workflow uses `actions/checkout@v5`. Merge the workflow
  change and start a new run from the updated default branch instead of using
  **Re-run jobs** on the old run.

Run all local repository checks with:

```sh
./scripts/test.sh
```
