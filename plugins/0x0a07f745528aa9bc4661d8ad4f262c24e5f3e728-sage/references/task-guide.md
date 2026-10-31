# Sage capability router

Sage helps agents discover, inspect, use, improve, and share reusable capabilities.

- **capability** = prompt | skill | behavior | library | MCP/tool bundle
- **skill** = one reusable operating procedure
- **behavior** = a validated graph that composes skills and verifiers
- **library** = a packaged and discoverable capability set

## Meta-preference and scope

For repeatable Sage work, prefer finding a capability before inventing one.
This does not override its expert procedure: Sage routes, the selected
specialist governs its scope, and this router retains universal trust,
authority, visibility, and verification boundaries.

Do not activate for ordinary local coding or merely because the query says
"Sage." Follow an already-loaded specialist that clearly owns the task. A
process or meta skill that ranks first for a concrete job is a routing miss,
not a reason to load the process skill.

## Fast path: one obvious route

1. **Use the exact specialist.** If a local specialist clearly owns the task,
   skip ranking, but read its complete `SKILL.md` unless its full procedure is
   already loaded in the current context. Do not enumerate the catalog to confirm it.
   For exact CLI or Model Context Protocol (MCP) syntax, load
   `sage-command-map` before guessing or calling `--help`.
2. **Rank one task specialist.** When no exact specialist is known, run
   `sage suggest skill "<intent>" --source <harness> --session <id> --format json`.
3. **Reject a meta miss.** If a process or meta skill ranks first for a
   concrete job, do not load it to satisfy the loop. Broaden once or use a
   known exact task specialist.
4. **Branch by result and inspect before trust.** Inspect `entryKind`:
   - `skill` -> load the complete procedure, then apply it (a result snippet is
     not a load);
   - `prompt` -> inspect/use the prompt as guidance;
   - `behavior` -> `sage behavior show <key> --expand behaviorPlan`, then run
     only when trusted and runnable.
   For library entries, use `sage library inspect skill get <key> -l <library>`
   or `sage library inspect prompt get <key> -l <library>`.
5. **Do the work and verify it.** The selected specialist governs its scope.
   Verify the actual result, not only the command exit.
6. **Broaden only after a weak result.** Use
   `sage search "<intent>" --search-type skills --scope both` or
   `sage behavior recommend "<intent>" --format json`.
7. **Inspect prompt-active scope when the shortlist misses an installed specialist.**
   Read `sage library select active --source <harness> --session <id> --format json`.
   If `resolution.mode=only`, check whether the specialist's library is excluded;
   if `all` on an unbound project, check whether unrelated libraries dominate.
   Broaden once. For a wrong pool, follow `sage-discover-adopt-skill` §5; do not
   infer a pack from the path.
8. **Record evidence only when earned.** Loading or exposing a skill is not
   use. Unresolved suggestions auto-settle to neutral skip. Record explicit use
   only when the procedure materially guided the work, and record an outcome
   only after verification. Route evaluation
   work to `sage-feedback-and-evals`.
9. **Create only after a real gap.** Prefer extending an overlapping capability;
   create a new asset only for distinct, reusable judgment.

When the user gives an exact DAO or governed-library address, use address-led
discovery before concluding it is absent:

```bash
sage library discover "<query>" --format json --limit 20
sage library sync --dao <dao-address> --dry-run
sage library sync --dao <dao-address>
```

Inspect the synced library using its canonical lowercase/kebab-case keys, not
display names. A missing skill does not rule out a behavior: inspect `entryKind`
and the owning library before declaring a gap.

## Choose the available control surface

**CLI default:** with shell access, prefer canonical `sage ...`; only the CLI
performs signed onchain transactions. Use `sage-command-map` for exact syntax; use CLI help only when that reference does not cover the needed shape.

When the host requires tool calls:

- `sage_search({domain, action, params})` handles both `read_metadata` and
  `read_content`, including `prompts.get` and `skills.get`.
- `sage_execute({domain, action, params})` handles supported unsigned
  `local_mutation` and `external_mutation` operations.
- `sage_status({})` checks bridge/runtime health.
- Sage MCP cannot sign onchain transactions. Economic, governance, payment,
  claim, vote, tip, bounty, publish/promote, and other signed writes must hand
  off to the CLI with explicit authority.
- Raw MCP tools are valid when they are the actual host interface.

For the current action matrix call
`sage_search({"domain":"help","action":"list"})`. Read
`references/control-surface.md` for the detailed CLI/code-mode/raw-MCP map.
Do not select MCP merely because it might be warm and fast; select the surface
that can actually complete and verify the action.

### Native capability discovery

Start from the user's intended result, not a tour of Sage commands. Use an
already available native tool when its schema and authority fit. Skills supply
judgment; tools perform operations. Finding one does not establish the other.
For an unfamiliar Sage action inspect the action map; for an external capability
inspect the configured hub and search its tools. Do not enumerate every library,
start servers, or install connectors just to prove that discovery happened.

In code mode, `sage_search` handles metadata and full-body reads; `sage_execute`
handles supported unsigned mutations. Inspect the returned schema rather than
guessing domain/action pairs. For CLI shapes use `sage-command-map`. A callable
tool may carry a harness prefix: use the name actually advertised in this turn.
Distinguish not advertised, call rejected, and not attempted. After resume or
compaction, an old inventory is not proof of current callable tools. Probe one
relevant read when available; do not loop on shell echoes or repeat a denied call.

Route a genuine need for complementary help to `sage-proactive-collaboration`,
without requiring a fleet or a specific channel. Sage Chat is the default for
a new collaboration when no user/deployment choice exists and the route is
available and authorized; preserve an existing conversation. Finish private work privately
when collaboration would not help. Failed feedback recording must not turn a
completed user task into a daemon-repair loop or a fabricated success receipt.

## Feedback commands and neutral outcomes

The entrypoint retains the actual-guidance and verified-outcome rules. For a
named exposed suggestion that was the wrong specialist, use:

```bash
sage suggest feedback reject --candidate <library/key> --correlation-id <id>
```

Targeted rejection supplies a hard-negative signal and needs no user complaint.
Use `skip` only when nothing shown was used and nothing shown was wrong.
Unresolved suggestions auto-settle to neutral skip; silence is not rejection.
For use/outcome command shapes and evidence checks, load `sage-feedback-and-evals`.

## Universal invariants

1. Search/discover before creating when a reusable answer may exist.
2. Inspect remote, governed, or unfamiliar capabilities before activation.
3. Keep reads separate from mutations; use dry-run/preview where supported.
4. Install, expose, select, save, and use are local operations—not publication;
   hosted personal cloud is private by default.
5. Ask before crossing local/private -> shared/public/paid/governed visibility.
6. Ask before signing, payment, claim, tip, bounty, vote, marketplace,
   publication, promotion, or destructive mutation.
7. Before Sage writes that require wallet/daemon authentication or economic
   signing, load `sage-wallet-ops` and confirm the relevant readiness. Discussion
   transport has its own identity check; read-only analysis does not require
   economic authority.
8. Verify after every write by re-reading authoritative state. Public artifacts
   also require durable pinning and anonymous retrievability checks.
9. Never invent authority, payout routing, automatic contributor splits, or an
   unimplemented command because a workflow implies it should exist.
10. If runtime/generated context looks stale, load `sage-runtime-preflight`
    before recommending another init (that skill owns doctor/repair commands).

## Library activation has two facets

Do not collapse prompt-active ranking and skill-activated IDE exposure (`activate` ≠ ranking):

- **Prompt-active (`prompt_active`):** `sage library use <name>` or
  `sage library select use <name>` controls what `sage suggest skill` ranks.
  Agents orient with `sage library select navigate` and default to session
  scope so they do not rewrite the operator profile:
  `sage library select navigate --align-session --source <harness> --session <id> --expires-in 8h --format json`
  or
  `sage library select use <name> --source <harness> --session <id> --expires-in 8h --only --format json`.
- **Skill-activated:** `sage library activate <cid-or-name>` (or
  `sage skill expose`) installs skill files into harness IDE dirs. It does
  **not** accept `--source`/`--session`/`--expires-in` and does **not** change ranking.
- `sage library select navigate --format json` is the one-shot orient; it never
  mutates Project or Default. `sage library select active --format json` shows
  `resolution.tier`, `resolution.mode`, and `resolution.libraries`.
  `sage library active --format json` reads both facets but does not report
  resolution. Treat `skill_activated: null` as daemon-offline/unknown, not empty.

**Session-start:** when cwd implies a project pack that is missing from
`prompt_active` (or foreign domain packs dominate suggests), agents run
`sage library select navigate [--align-session …]` (Compact scope loop /
`sage-discover-adopt-skill` §5) before trusting hook-injected suggestions.

**Buzz onboarding:** after verified enrollment, run
`sage library select navigate --source buzz-acp --session <origin-derived-session> --format json`.
The `buzz-acp` harness/session scopes the ranking pool. The responding agent
public key is identity and audit attribution only. Wallet, payment, controller,
and executor authority stay separate. Never auto-activate from Buzz.

Load `references/workflow.md` for the full activation and verification table.

### Skill membership

`sage search` can find an installed skill outside any library, but
`sage suggest skill` cannot rank it. When creating or adopting a reusable skill,
choose an existing appropriate library and add it:

```bash
sage library skill add <path> --library <name>
```

This is not a reason to interrupt a read-only task with an unrelated install or
library change. Use `sage-discover-adopt-skill` when the intended home is unclear.

## Shared commons: location and boundary

Discover -> inspect -> use -> verify -> improve. Discussion, sharing, funded
investigation, governance, and recognition are optional branches, not a ladder.
A message body can be the artifact; no IPFS, solo baseline, or new wallet is
required for discussion.

Offer a commons once when repeated utility warrants it. Preserve provenance;
ask before crossing visibility or authority boundaries.

This router owns only that trigger and boundary. Hand off collaboration framing
to `sage-proactive-collaboration`, publication readiness to
`sage-library-stewardship`, governed canon to `sage-governance-participation`,
and attribution or rewards to `sage-identity-and-rewards`.

### Peer contributions and stewarded changes

Read a peer skill's current version and open proposals before drafting a
replacement. When it helped, cite the exact version. To improve it, route a
`sage-library-change-proposal` to its steward: a defect fix with evidence,
a value change built by consensus with the steward and library members, or a complementary
skill added to the library. Favor deeper reciprocity with trusted,
aligned, long-history collaborators while preserving authorship and prior work.
These are choices for relevant collaboration, not prerequisites for every task.

## Model quality and suggestion attention

For better local models, route to `sage-runtime-preflight`'s model evaluation
section: search current ONNX releases by context length, 384-dimensional/MRL
embedding compatibility, instruction/code training, quantization, memory and
measured quality—not a fixed list of model names. Embeddings, cross-encoder or
typed decision rerankers, and local RLM models serve different jobs.

Use `sage model list` to inspect installed versus available models, then
`sage model download <id>` and `sage model default <id>` for a compatible RLM
choice. Verify the default rather than leaving a small test model selected.
Embedding selection uses `sage config set default_embedding_model <id>` followed by `sage model load`.

For suggestion context, start with `suggest.emission.default = "distilled"`,
`distill_budget_chars = 6000`, `min_score = 25`, and `min_gap = 0.10` on the
intended profile. This balances bare headers against full-body prompt stuffing;
verify with `sage config show` and still load the chosen full procedure.
For learned reranker setup, load `sage-feedback-and-evals`: inspect status,
mine a fixed window, train with task-success labels and explain weights, then
run the digest-pinned benchmark gate. Only an approved passing candidate may
be wired through `profiles.<name>.reranker.{runtime,artifact_path,pinned_digest}`.
Neither model download nor training proves better live routing.

## Specialist handoffs

| Intent | Owner |
|---|---|
| Find, inspect, install, expose capabilities | `sage-discover-adopt-skill` |
| Safe read/preview/write/verify sequencing | `sage-workflow` |
| Exact CLI/MCP command shapes | `sage-command-map` |
| Author prompts, skills, behaviors, libraries | `prompt-builder` |
| Runtime, hooks, daemon, MCP, auth repair | `sage-runtime-preflight` |
| Wallets, OWS/Privy, delegation, signing | `sage-wallet-ops` |
| Library curation and distribution surfaces | `sage-library-stewardship` |
| Resolve disagreement, compare approaches, find reviewers, fund investigation | `sage-proactive-collaboration` |
| Choose accepted shared instructions: DAO mode, proposals, voting, canon | `sage-governance-participation` |
| P2P trusted fleet sync | `sage-p2p` |
| Feedback, RLM capture, evals | `sage-feedback-and-evals` |
| Independent skill-guided task outcome judgment | `sage-outcome-evaluator` |
| Identity, provenance, reflections, rewards | `sage-identity-and-rewards` |
| Cross-agent coalition cold start | `sage-coordination-cold-start` |

Read the goal map in `references/companion-skills.md`; use
`references/cli-family-chooser.md`,
`references/distribution-surface.md`, and `references/harness-bridge.md`.
For security-sensitive work, see [security-review.md](security-review.md).

## Security-sensitive implementation and audits

For signing, authorization, private-data, payments, isolation or untrusted input
validation changes, use [security review routing](security-review.md). Load the
selected procedure and its required sidecars, not the entire audit library.
