---
name: sage
description: "Route an unclear Sage goal to its owning capability. Skip when a specific skill already owns the task."
tags: [sage-protocol, capabilities, libraries, governance, mcp]
sage-inline-sidecars: false
---

# Sage capability router

Skills provide procedures; behaviors compose them; libraries organize them.
Sage routes work to the relevant capability. A harness executes the work;
a conversation alone does not authorize a governed change.

## Select one useful path

First understand the concrete task, then choose one path:

1. Use an exact known specialist directly. Read its complete `SKILL.md` unless
   its full procedure is already loaded in the current context.
2. Otherwise rank once:
   `sage suggest skill "<task>" --source <harness> --format json`.
3. Inspect `entryKind` and the selected content before use. Load a skill's full
   procedure; inspect prompts and behaviors through their own routes.
   A shortlist is a pointer, not a procedure load.
4. An irrelevant process/meta result is a routing miss. Broaden once with
   `sage search "<intent>" --search-type skills --scope both`, or use a known specialist.
5. Follow the selected specialist and verify the actual result.

Do not load the whole catalog, repeat discovery after a clear selection, or
activate a library merely to use an available skill. For a missing specialist
or wrong ranking pool, use `sage-discover-adopt-skill`. Exact CLI shapes belong
to `sage-command-map`; scope diagnostics are in the task guide.

| Need | Specialist |
|---|---|
| Find, install, expose | sage-discover-adopt-skill |
| Create or revise an asset | prompt-builder |
| Sequence a write safely | sage-workflow |
| Diagnose runtime/hook/MCP failure | sage-runtime-preflight |
| Wallet/auth/approvals | sage-wallet-ops |
| Security-sensitive implementation or audit | [Security review routing](references/security-review.md) |
| Proposals, voting, governed canon | sage-governance-participation |
| Collaboration, credit, or a stewarded improvement | sage-proactive-collaboration |
| Choose an economic opportunity, complementary arrangement, or SXXX trade-off | sage-economic-radar |
| Ground situated position, counterparties, and decision rights for an agreement | sage-participation-positions |
| Establish a new collaboration | sage-coordination-cold-start |
| Library organization/distribution | sage-library-stewardship |
| Use/outcome evidence or evaluation | sage-feedback-and-evals |
| Independent outcome grading | sage-outcome-evaluator |
| Identity, reflections, rewards | sage-identity-and-rewards |
| Private trusted peer sync | sage-p2p |

A funding investigation, a shared decision, or a collaboration can be the entry
point. These are alternatives, not a required sequence. Prompt-active ranking and
IDE skill exposure are separate; see the task guide before changing either.
When creating or adopting a skill, put it in an appropriate Sage library so
suggestions can rank it. Do not turn a read-only task into a packaging task.

## Use the available surface

Prefer canonical Sage CLI with shell access, or an already available native tool
whose schema and authority fit. `sage_search` handles reads; `sage_execute`
handles supported unsigned mutations. MCP cannot sign. Never bypass a security denial.
After resume or compaction, distinguish not advertised, call rejected, and
not attempted; an old inventory does not prove that a tool is callable now.

## Authority and completion

Continue authorized work through useful output and verification. Ask at actual
missing authority boundaries, not before harmless inspection. Payments,
signatures, publication, credential expansion, and governed changes
need explicit authority. Personal cloud is private by default;
ask before crossing visibility boundaries. Public artifacts need
pinning and anonymous readback. Re-read authoritative state after every write.

Loading is not use. Record use only when a suggested procedure materially guided
work, and outcomes only after verification. Reject named wrong suggestions;
never infer rejection from silence or reject an entire shortlist by default.
Failed feedback recording must not block a completed task or fabricate a receipt.
Optional packaging, feedback, economics, or a public post is not a completion gate.

## Read more only for the task at hand

These paths are relative to the directory containing this `SKILL.md`, not the
project's working directory. Open the matching file; do not load the whole list.
A native file load supplies that directory. If Sage supplied only the text,
`sage skill status sage` can locate installed copies. Use a copy only if it
matches the skill you loaded. If no matching bundle is accessible, report the
reference as unavailable. Do not guess a path or install a copy just to follow it.

| When you need to… | Read… |
|---|---|
| Audit signing, authorization, private data or other trust-boundary changes | [Security review routing](references/security-review.md) |
| Fix a wrong suggestion pool, add a skill to a library, record feedback, or improve a peer's skill | [Task guide](references/task-guide.md) |
| Choose between Sage CLI and MCP, or understand a tool's allowed effects | [Control surfaces](references/control-surface.md) |
| Set up Sage in Codex | [Codex setup](references/harness-codex.md) |
| Set up Sage in Pi | [Pi setup](references/harness-pi.md) |
| Set up Sage in Grok | [Grok setup](references/harness-grok.md) |
| Connect another supported harness | [Other harnesses](references/harness-bridge.md) |
| Decide whether collaboration, funding, or another specialist would help the goal | [Companion skills](references/companion-skills.md) |
