# Sage workflow and behavior routing

Sage capabilities are prompts, skills, behaviors, libraries, and MCP/tool bundles. A prompt is one artifact type; a skill is one reusable operating procedure; a behavior is an executable multi-skill workflow; a library is a packaged and discoverable capability set.

## Search -> inspect -> activate/use

1. Search or suggest candidates.
2. Inspect before trusting remote or unfamiliar results.
3. Activate/use intentionally.
4. Verify the outcome.
5. Record feedback when a suggestion or behavior actually helped.

For Pi/manual routing, prefer:

```bash
sage suggest skill "<intent>" --source pi --format json
sage behavior recommend "<intent>" --format json
sage search "<intent>" --search-type skills --scope both
```

Try 2-3 query phrasings when search quality matters: task verb/object, domain phrase, and failure mode.

## Library publish and pinning rules

For public, marketplace, or governed library flows, verify storage durability as part of the workflow, not as an afterthought:

```bash
sage doctor --include-details
sage wallet current
sage daemon status
sage config ipfs balance
sage library push <library> --dry-run --pin-duration 12months
sage library push <library> --cloud --pin-duration 12months --message "<what changed>"
sage library pin-status <library>
sage config ipfs status <manifest-or-item-cid>
```

Use `--pin-duration 12months` or `permanent` for artifacts intended to remain discoverable. If anonymous gateways cannot fetch the canonical CID (`no providers found`, 404, 504, owner-only, timeout), do not promote/sell/publicize that CID; re-push or re-pin from a local source of truth first.

## Behavior rules

- `sage behavior run` returns `output: "controller_plan"`, the execution contract consumed by Sage-aware harness executors to coordinate resolved skill steps.
- Behavior resolution is library-scoped. A skill being globally exposed to an IDE does not make it available inside a behavior.
- For self-contained behavior libraries, import component skills with `sage library skill add --key <skill> --library <library>` and re-run `sage behavior validate`.
- Optional behavior skills can still propagate MCP requirements. Validate with `--available-mcp <server>` only when the caller can provide that server.
- Do not auto-run remote or untrusted behaviors. Inspect/sync/install through normal Sage trust paths first.

## Feedback semantics

Route detailed feedback/RLM work to `sage-feedback-and-evals`, but preserve the tri-state distinction:

```bash
sage suggest feedback use --used <key>
sage suggest feedback skip
sage suggest feedback reject
```

Use `reject` when suggestions were actively bad, not merely unused. RLM `rlm_*` daemon settings hot-reload through the settings update path; do not tell users a daemon restart is required unless the behavior was re-verified.
