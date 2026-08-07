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
./scripts/test.sh
```

## Hourly autonomous run

`.github/workflows/hourly-autonomous-engineering.yml` runs at minute 7 of every
hour (GitHub schedules can start late during periods of high load). It checks out
the persistent `automation/hourly-product` branch when present, executes the
instructions in `AUTOMATION_PROMPT.md`, tests the resulting tree, and only then
commits and pushes. The workflow creates a pull request on the first successful
change; subsequent runs push to the same branch and therefore update that pull
request.

### Required repository setup

After merging this setup into the default branch:

1. Add an Actions repository secret named `OPENAI_API_KEY` containing an OpenAI
   API key with an appropriate project budget and usage limits.
2. Under **Settings → Actions → General → Workflow permissions**, select
   **Read and write permissions** and enable **Allow GitHub Actions to create and
   approve pull requests**. Organization policy must permit these settings.
3. Keep GitHub Actions enabled. Scheduled workflows run from the default branch,
   so this workflow file must remain there.
4. Optionally protect the default branch and require review/checks. The automation
   pushes only `automation/hourly-product`; it does not merge its own pull request.
5. Run **Hourly autonomous engineering → Run workflow** once to verify the secret,
   repository policy, Codex access, branch push, and pull-request creation. After
   that setup check, no recurring manual action is required.

The workflow grants its `GITHUB_TOKEN` only `contents: write` and
`pull-requests: write`, serializes runs to avoid branch races, and has a 50-minute
timeout so one run cannot overlap the next. The Codex CLI is installed from the
official `@openai/codex` npm package on each fresh GitHub-hosted runner. Codex is
given workspace-write sandboxing with outbound network access so it can perform
the market research required by the prompt; review changes before merging and use
an API project whose budget and permissions are limited to this automation.

The workflow configures Codex's approval and sandbox policies as top-level `-c`
settings before the `exec` subcommand. Do not change this back to
`codex exec --full-auto`: the hosted runner's Codex CLI rejects `--full-auto` as
an `exec` argument. The install step prints the installed version and smoke-tests
`codex exec --help`, while a separate preflight emits a clear error when
`OPENAI_API_KEY` is missing.
