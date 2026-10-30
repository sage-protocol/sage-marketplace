# Task guide: sage-outcome-evaluator

Read only the section relevant to the current task. The entry skill owns selection and authority boundaries. Paths in this guide are relative to the skill directory.

# Sage Outcome Evaluator

Act as an isolated outcome judge. Evaluate the skill-guided path; do not improve
the implementation while grading it.

## Required inputs

Refuse to assign an outcome unless the caller provides or the trace resolves:

- the original task;
- the exact qualified skill key and content version or digest;
- the parent harness, session, and suggestion correlation;
- a filtered parent execution trace with tool results, not hidden reasoning;
- the final artifact or authoritative state; and
- the skill's expected output, verification rules, and valid stop conditions.

Missing evidence means `abstain`, not `failed`.

## Evidence order

Prefer evidence in this order:

1. authoritative post-write state or reproduced runtime behavior;
2. relevant test, build, browser, or live-smoke results;
3. exact diff and resulting artifacts;
4. tool-call results and exit status; and
5. the parent agent's final claim, treated only as an untrusted assertion.

Never read or request private chain-of-thought. Redact secrets, contact details,
private paths, and unrelated session material before returning evidence.

## Outcome rubric

- `passed` — the skill-guided procedure produced its declared result and met its
  verification and stop conditions.
- `failed` — the skill ran, but its result is wrong, broken, incomplete, or
  unusable under the declared contract.
- `revised` — the skill materially guided the work, but its procedure or output
  required substantial rewriting before the result became usable.
- `abstain` — use, result, or verification cannot be established from the
  available trace. Record no outcome.

A rollback or justified abstention can be `passed` only when the evaluated skill
declares that stop condition. A generic tool failure is not a skill failure.
`task_complete`, process exit zero, a full skill serve, and the parent's claim do
not independently prove `passed`.

## Procedure

1. Confirm that the evaluator is a fresh subagent and is not the parent that did
   the work. If isolation is unavailable, return `abstain`.
2. Load the exact evaluated skill body. Do not search for another skill or change
   the parent's selected procedure.
3. Build a short evidence table mapping each required output or verification
   condition to trace evidence, contradiction, or `unknown`.
4. Run only bounded, non-editing verification needed to resolve a material
   unknown. Do not repair the work, publish, pay, vote, or invoke another agent.
5. Choose one rubric status. State the smallest decisive evidence and any
   contradiction.
6. Apply the attribution boundary below before recording anything.
7. If recording is allowed, bind the write to the exact parent correlation.
   Preserve the JSON receipt. Then use `sage suggest feedback show
   --correlation-id <id> --format json` to confirm the suggestion verdict and
   candidate event. Do not claim that this command rereads the execution row;
   the current CLI has no exact outcome-by-correlation read surface.

## Local outcome boundary

Current `skill_execution` rows are operationally linked to a skill, source,
session, model/harness context, capture, and correlation. They do **not** contain
an authenticated reporter/evaluator principal, wallet, signature, or append-only
evaluation identity. The `source` and `session` supplied to the CLI are scope
labels, not durable actor attribution. One `(correlation_id, skill_key)` row also
cannot preserve competing performer and evaluator claims.

Raw rows are local runtime evidence by default. They are not automatically added
to a library or manifest, published to IPFS, or used as an onchain economic
attestation. Sharing occurs only through a separate explicit path, such as a
curated worked example, a mined sanitized routing-evidence snapshot/reference,
or a capability-negotiated trusted-fleet evidence exchange.

Therefore:

- never overwrite a conflicting recorded status;
- record a local exact-linked outcome when the evidence supports one;
- use `evaluate-only` when the caller forbids local mutation or the evidence is
  insufficient;
- never describe a local outcome row as a public or economic attestation; and
- apply authorship, privacy, consent, and provenance rules at the later explicit
  export or publication boundary.

### Local recording

When no use/outcome exists:

```bash
sage suggest feedback settle use <library/key> \
  --outcome <passed|failed|revised> \
  --correlation-id <parent-correlation> \
  --source <parent-harness> \
  --session <parent-session> \
  --format json
```

Keep the two-step form as the fallback. When the use is already recorded, write
only the independently selected outcome:

```bash
sage suggest feedback outcome <library/key> \
  --status <passed|failed|revised> \
  --correlation-id <parent-correlation> \
  --source <parent-harness> \
  --session <parent-session> \
  --format json
```

Do not record `abstain`. Recording local feedback does not authorize sharing it.
Treat `recorded: true` as a mutation receipt, not an independent readback. Until
an exact execution-row read command exists, report `outcome_readback: unavailable`
instead of overstating verification.

## Worked-example authorship

An outcome does not create a worked example. If a later curation step turns the
trace into a portable example:

- attribute the author of the exact example input/output, not the evaluator,
  model, harness, session, skill author, or publisher;
- use `sage skill example add <skill> --input ... --output ... --author
  <identity>` for a hand-curated example;
- treat the resulting `provenance.author_claimed` manifest value as a claim,
  not proof; and
- require a registry, governed record, or onchain event to attest authorship
  before it can direct rewards.

Leave authorship unset when the evidence does not identify the author. Do not
infer it from who recorded the outcome.

## Output contract

```yaml
evaluation:
  skill: <qualified-key>
  skill_version: <digest-or-cid>
  parent_correlation: <id>
  verdict: passed | failed | revised | abstain
  decisive_evidence: []
  contradictions: []
  verification_run: []
  sharing:
    local_only: true
    exported: false
    note: outcome recording does not publish evidence or create economic attribution
  recording:
    mode: evaluate-only | local
    recorded: false
    receipt_verified: false
    suggestion_readback_verified: false
    outcome_readback: unavailable
```

## Harness integration

This skill contains the cross-harness judgment procedure. A thin harness adapter
is still required to launch it automatically through Codex, Claude, Pi, Grok,
OpenCode, or another native subagent surface and to pass the parent trace and
correlation. If no isolated subagent surface exists, do not silently fall back to
self-grading.
