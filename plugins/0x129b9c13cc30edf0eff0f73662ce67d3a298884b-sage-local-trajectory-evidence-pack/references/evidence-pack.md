Read installed help for the chosen command family; stop or mark unavailable
rather than replacing absent evidence with a guessed CLI or database join.
Run `sage doctor --include-details` before recommending runtime changes. Do not
repair runtime, enable capture, or change retention from this procedure.

## Local evidence reads

```bash
sage capture status --format json
sage capture list --limit 20 --format json
sage suggest feedback status --format json
sage suggest feedback show --correlation-id <suggestion-id> --format json
sage suggest feedback breakdown <library/key> --content-hash <base-sha256> --format json
sage skill example list <key> --library <library> --format json
sage skill example list-rejected <key> --format json
sage skill refinement list --format json
sage skill refinement show <proposal-id-or-digest> --format json
```

- Capture list has bounded prompt previews, not full transcripts. Even previews
  can be private. Check daemon status, truncation, limit, and source coverage;
  offline with an empty list means unknown, not zero. Obtain richer action/tool
  evidence only from explicitly approved local harness records.
- `show` audits the correlated suggestion and corrections; `breakdown` aggregates
  execution outcomes. Source/session/capture/skill-hash bindings must actually
  exist. Do not infer exact identity from key spelling or a current install.
- Full load is not applied use, and use is not a verified pass. Keep downgraded
  unverified claims separate. For future earned feedback, delegate to the loaded
  feedback skill; never backfill old outcomes using today's capture ID. Echo an
  explicitly supplied `sage:evidence-context.v1` capture ID verbatim; inspect
  returned automatic linkage rather than guessing one.
- Refinement `show` returns a CLI summary plus diff, not the full
  `SkillRefinementProposalV1` or evaluation envelope. A missing cached proposal
  is not proof no remote proposal exists. Its aggregate `pass` can coexist with
  failing evaluations; inspect all evaluation identities before concluding gain.

## Optional local routing snapshot

Only with approved local output and a fixed window:

```bash
sage capture mine --routing-evidence-output <private-output-dir> --window-start-ms <start-ms> --window-end-ms <end-ms> --format json
```

Inspect digest, exclusions, source/session caps, and session/time split. This
snapshot is routing evidence, not a complete G(s) trajectory pack or negative
skill-body example dataset. Default example mining selects positive examples;
never interpret absent failures as success. Do not use `--promote`, attach the
snapshot, train, activate, sync, or upload it in this workflow.

## Private pack contract

Use Markdown or JSON as a local sidecar, not a new Sage transport/schema claim.
Keep unknown fields explicitly unknown. Include:

| Section | Required content |
|---|---|
| Target | Qualified key, library, base manifest/revision, content SHA-256, selection origin; governance verification result when applicable |
| Coverage | Fixed window, approved input kinds, truncation/errors, excluded rows and reasons, retention, local pack digest |
| Local evidence index | Stable local IDs and input digests; private lookup map stored separately; no raw text in the pack |
| Groups | G(s), G(empty), unknown; overlapping memberships and deduplication rule |
| Version partitions | Exact-base, other-hash, no-hash counts; per-event attribution when versions changed mid-session |
| Observations | Sanitized sequence summary, referenced/loaded/applied states, explicit outcome, implicated instruction/step, supported links and missing steps |
| Diversity | Unique incident/session counts; task, model, harness, environment slices; maximum contributor share and unknown dimensions |
| Synthesis | Recurring failure, successful counterexamples, conflicting evidence, prior accepted/rejected attempts, alternative causes |
| Handoff | One testable hypothesis or abstention, readiness, suggested disconfirming fixture, evidence still needed |
| Privacy | Local-only inputs; approved processing boundary; public-safe review not performed or its explicit result |

Freeze the input set before counting. A repeated single-user incident is not
independent corroboration. Single-operator data can support a narrowly scoped
local hypothesis, but not population-wide claims; with only one incident or no
disconfirming evidence, request another case instead of a rewrite.

For public review, derive a new synthesis with portable fixtures, bounded
aggregate counts and approved provenance only. Remove transcripts, private
prompts, secrets, home paths, identities, private source locators, and raw tool
output. Even hashes/counts can identify rare private activity: omit unsafe
small slices and keep the private lookup map out. A privacy scan plus independent
content review is required; a `public_safe` label alone proves nothing.
