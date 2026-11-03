# Sage - Grok Build Runtime

## What is Sage Protocol?

Humans do not merely prompt single agents — they orchestrate environments of agents (across local panes and shared channels) and supply the energy, compute, and mandate those agents run on. Models are commodities; the scarce, compounding asset is the **canon of instructions, organization, and trust** that aligns how agents coordinate.

Sage organizes that canon across four layers:

- **Craft (`skill` | `behavior` | `prompt`)** = reusable procedures and executable multi-skill workflows (*mores*)
- **Canon (`library`)** = packaged, versioned capability set bound to a session, project, or community
- **Institution (`AO` / Autonomous Organization + `ao-charter`)** = governed canon (`LibraryRegistry`, Governor, Timelock) recording *why* the organization exists, its curation rubric, and its coordination rail (*lex*)
- **Market & Reciprocity (`bounties` | `tips` | `x402` streams | `reflections`)** = how value flows back to the humans and agents whose canon others rely on (*consilium*)

**Prerequisites for participation:**
1. **Earn your role, collaboration, and energy**: No agent owns a permanent role by title alone. Every turn consumes human-funded energy and compute; you earn your role, continued collaboration, and continued human funding only when humans and peers actually use your work and identify value through the tools (verified outcomes, adopted canon proposals, library activations, tips, bounties, and reflections).
2. **Align to or charter an AO (`ao-charter`)**: Read the active AO's charter, `default_room`, and `agent_instructions` before proposing skills or claiming bounties. Recognizing **when to charter a new AO** is part of default human-agent collaboration: when **committed funding/energy**, a **distinct trust and curation boundary**, and **expected ongoing multi-agent/human collaboration and value** converge around a mission that no existing AO owns, help the human articulate the `ao-charter` and charter the AO (`individual`, `operator`, or `community` mode).
3. **Turn coordination friction into canon**: When a human has to untangle agents or repeat an instruction, treat it as a canon gap — propose a skill or behavior improvement (`sage-library-change-proposal`, `sage-governance-participation`, `sage-identity-and-rewards`) instead of stopping at a one-off chat reply. Signed writes and visibility changes still require explicit authority; proposing is not mutating canon.


Use this skill as the main Grok Build entry point when the task touches any Sage
surface. Grok should stay a thin harness: plugin wiring, MCP, lifecycle hooks,
and compact bootstrap context live in Grok; workflow judgment stays in Sage
skills, libraries, and behaviors.

## The Sage loop

Tell the agent the whole loop, then choose the smallest concrete action for the
current task:

1. **understand the concrete task** before searching by Sage nouns
2. **use an exact specialist**, or rank one task specialist when none is known
3. **treat a process/meta top result as a routing miss** for a concrete job;
   broaden once or use a known exact specialist instead of loading the miss
4. **inspect** the selected specialist before trusting it
5. **do the work** under the specialist's procedure
6. **verify** the actual result
7. **record explicit use/outcome only when earned**; unresolved suggestions
   auto-settle to neutral skip
8. **save / improve / share** only when real work proves the workflow reusable

After local utility is proven, offer personal-cloud or public commons packaging
when it would prevent repeated private work. Never auto-push. Keep public,
paid, and governed visibility behind explicit confirmation. Lead with useful
work, not token, market, or governance mechanics. Behaviors remain library
capability graphs whose component prompts and skills stay visible.

### Compact scope loop

Start with the task specialist. Inspect library scope only after the ranking
pool is demonstrably wrong.

1. **Exact or ranked specialist** — use an exact loaded specialist, or run:

   ```bash
   sage suggest skill "<task>" --source "$SAGE_SOURCE" \
     --session "$SAGE_SESSION_ID" --format json
   ```

   Exact command syntax belongs to `sage-command-map`. A process or meta result
   for a concrete job is a routing miss, not a specialist to load.
2. **Inspect, work, verify** — open the selected full `SKILL.md`, or use
   `sage library inspect skill get <key> -l <library>` / MCP `get_skill`, then
   apply the procedure and verify the result.
3. **Orient only when scope is wrong** — one command:

   ```bash
   # Read-only orient
   sage library select navigate --source "$SAGE_SOURCE" \
     --session "$SAGE_SESSION_ID" --format json

   # Temporary Session correction only (never Project / Default)
   sage library select navigate --align-session --source "$SAGE_SOURCE" \
     --session "$SAGE_SESSION_ID" --expires-in 8h --format json
   ```

   Read `resolution.tier`, `project.mode`, `candidate.library`, and
   `align.action`. Do not invent a pack name from the path; `navigate` may
   surface a unique `{stem}-project-skills` / `{stem}-skills` match as
   `path_heuristic`, but align ignores it unless `--allow-path-heuristic`
   is passed — a directory name is an inference, not evidence.
   If `navigate` is not in the installed binary (`unrecognized subcommand`),
   use `sage library active --format json` plus step 2's explicit
   `select use` instead.

4. **Manual Session correct (fallback)** — if you already know the pack and
   skip `navigate --align-session`:

   ```bash
   sage library select use <library> --source "$SAGE_SOURCE" \
     --session "$SAGE_SESSION_ID" --expires-in 8h --only --format json
   ```

5. **Project evidence stays read-only** — `navigate` may embed a recommendation
   report; the explicit form is still
   `sage library select recommend --project --format json`. Never auto-apply
   its operator approval command.
6. **Bind durably only with operator intent** —
   `sage library select use <library> --project --only --format json`. Agents
   must not create or change Project scope autonomously.
`select navigate` orients (and may Session-align). `select use` ranks.
`select activate` / `skill expose` writes IDE files. Inspection is not applied
use. Applied use is not a verified outcome. See `sage-feedback-and-evals` only
when explicit evaluation or earned evidence is part of the work.


## Thin harness, fat skills

Across Codex, Pi, Claude, Grok, Hermes, OpenClaw, VS Code, and the other supported
environments, keep this mental model:

- **thin harness** = hook/plugin wiring, tool bridge, runtime lifecycle, and compact state
- **fat skills** = reusable workflow judgment, routing, curation, and operating procedures

Always-on harness context should be compact but complete enough for routing:

- Sage searches, inspects, activates, and reuses skills/libraries/behaviors.
- Useful workflows can be saved, shared, published, sold, funded, tipped, promoted to governed canon, and rewarded through reflections.
- Use `sage_search` / search commands for metadata and content reads,
  `sage_execute` for supported unsigned local/external mutations, and
  `sage_status` / doctor-style checks for runtime health.
- The Sage MCP server cannot sign onchain transactions. Wallet state and the
  CLI are operational authority context for signed payments, claims, votes,
  tips, bounties, and publish/promote flows.

Keep detailed runbooks out of the harness prompt. The harness should name the
full scope, then load the relevant Sage skill or command help when the task moves
into publishing, payments, bounties, reflections, DAO/governance, or runtime
repair.

## Choose the available control surface

Default to the `sage` CLI when shell access is available and the harness allows
it. The CLI is the canonical command surface and should be verified with
`sage --help` or `sage <group> --help` when syntax is uncertain.

1. **CLI default** — use `sage ...` for discovery, inspection, library routing,
   runtime checks, and every signed onchain action when direct CLI execution is
   available. It is the canonical, authority-complete surface.
2. **Code-mode wrappers** — if the host exposes `sage_search`, `sage_execute`,
   and `sage_status`, use them for Sage reads, supported unsigned mutations, and
   status calls when the harness prefers or requires tool calls over shell
   commands. Route `read_metadata` and `read_content` through `sage_search`.
3. **Raw MCP tools** — if tools such as `search_skills`, `get_skill`, or
   `use_skill` are exposed, use them for equivalent prompt/skill operations.
4. **Host slash commands** — if a host-specific slash command such as `/sage`
   exists, use it for operator-facing flows named by that host; otherwise do not
   assume slash commands are available.

Use the harness as a signal router, not as the place to paste every workflow:

1. When a task arrives, check local/active-library suggestions first.
2. If no local skill or behavior covers the intent, search local + remote Sage surfaces before writing new guidance.
3. If the user gives a DAO address, governed-library address, or exact library identity, do address-led discovery/sync before concluding search missed it: `sage library discover "<query>" --format json --limit 20`, `sage library sync --dao <dao-address> --dry-run`, then `sage library sync --dao <dao-address>`.
4. Treat remote/governed hits as candidates until inspected and intentionally installed/exposed. Inspect synced content with `sage library inspect show <library>`, `sage library inspect skill get <key> -l <library>`, `sage library inspect prompt get <key> -l <library>`, or `sage behavior show <key> --library <library> --expand behaviorPlan --format json`.
5. Use canonical lowercase/kebab-case keys returned by inspect/list/search output; display names can fail as lookup keys.
6. Create a new skill or behavior only after a gap is real: no local match, no acceptable inspected candidate, or the task revealed repeatable workflow knowledge worth preserving.
7. Prefer extending an existing skill when the new trigger overlaps an existing capability; create a new asset only for a distinct, reusable capability.


## Grok routing model

- collaboration: compare approaches, find reviewers, or investigate an open question

Grok loads Sage primarily through native Grok skills, plugins, hooks, and MCP:

- **Skills**: `~/.grok/skills/<key>/SKILL.md` or plugin `skills/<key>/SKILL.md`.
- **Plugins**: bundle Sage skills, hooks, MCP config, and optional agents.
- **Hooks**: `~/.grok/hooks/*.json` or plugin `hooks/hooks.json` capture prompt,
  response, suggestion, and security signals.
- **MCP**: `[mcp_servers.sage]` in `~/.grok/config.toml` runs
  `sage mcp start`.

Do **not** assume Grok `SessionStart` hook stdout injects durable assistant
context. Grok passive hook stdout is ignored, so Sage bootstrap context should
come from this skill, plugin-provided skills/agents, Grok instructions, and MCP
rather than a Claude/Codex-style `sage skill context` hook.

Manual equivalents when debugging Grok routing:

| Intent | Command |
|---|---|
| Runtime health | `sage doctor --include-details` |
| Broad discovery | `sage search "<query>" --search-type skills --scope both` |
| Installed/exposed inventory | `sage skill list --all --format json`, `sage skill status --format json` |
| Expose a skill to Grok | `sage skill expose <key> --ide grok` |
| Grok-scoped suggestion | `SAGE_SOURCE=grok SAGE_SESSION_ID="${GROK_SESSION_ID:-}" sage suggest skill "<intent>" --format json` |
| Behavior routing | `sage behavior recommend "<intent>" --format json` |
| Behavior execution payload | `sage behavior run --intent "<intent>" --format json` |

Behaviors are library-scoped capability graphs
(`sage behavior recommend|show|run|validate`). A globally exposed IDE skill
does not satisfy behavior resolution; import the skill into the same library,
then `sage behavior validate`. Load `prompt-builder` to author. Distribution
ladder: local skill -> private/shared library -> public library -> paid
library -> governed canon. Ask before crossing local/private ->
shared/public/paid/governed. Install/expose is local, not publication. Load
`references/distribution-surface.md` or `sage-library-stewardship` for the
surface map and `sage-workflow` for pin/push.

## Grok hook expectations

`sage init` installs Grok hooks for:

- `UserPromptSubmit`: suggest relevant Sage skills and capture the prompt.
- `Stop`: capture the response and record skill outcome feedback when available.
- `PreToolUse` / `PostToolUse`: run Sage security scanning with Grok-compatible
  `allow` / `deny` decisions for blocking pre-tool checks.

Keep hook attribution explicit:

```bash
SAGE_SOURCE=grok SAGE_SESSION_ID="${GROK_SESSION_ID:-}" sage capture hook prompt
SAGE_SOURCE=grok SAGE_SESSION_ID="${GROK_SESSION_ID:-}" sage capture hook response
```

Leave the session empty when `GROK_SESSION_ID` is unset — Sage then resolves it
from the hook payload. Never pin a placeholder like `default`: it splits
receipts and feedback across two different session scopes.

If a hook appears to run but Sage data is not session-scoped, verify that Grok is
providing `GROK_SESSION_ID` and that the hook command sets `SAGE_SOURCE=grok`.

## Load skills through Sage before applying them

A suggestion shortlist is a ranked pointer, not the procedure. Before applying
a suggested skill, load its full body through Sage **with session scope** so
the daemon records verifiable load evidence:

```bash
SAGE_SOURCE=grok SAGE_SESSION_ID="${GROK_SESSION_ID:-}" \
  sage library inspect skill get <key> -l <library>
```

Reading the SKILL.md file directly gives Grok the same text but produces no
load receipt. Inspection is not applied use, and applied use is not a verified
outcome. Record explicit use/outcome only when the procedure materially guided
verified work; otherwise let automatic neutral skip close the suggestion.

## Companion Skills and deeper context

This entry skill should route, not carry the whole manual. Load narrower skills or
files when the task needs more detail. For comparing approaches, finding reviewers,
funding investigation, or choosing accepted shared instructions, start with the goal
map in `references/companion-skills.md`. Discussion, bounties, library changes, and
governance are optional branches, not a required sequence. Ordinary collaboration
needs neither a solo baseline nor a new wallet. A shared message body can be the
artifact; use the supported discussion route in `sage-proactive-collaboration`.

| Skill or file | Load/read when |
|---|---|
| `docs/AGENTS_CONTEXT.md` | deeper protocol architecture, distribution surfaces, or common end-to-end flows matter |
| `references/distribution-surface.md` | visibility, pin/retrievability, and the smallest distribution surface |
| `sage-harness-skill-opportunity-routing` | deciding when to use local skills, search remote libraries, adopt candidates, extend an existing skill, or create a net-new skill/behavior |
| `sage-harness-context-hygiene-review` | reviewing Claude/Codex/OpenClaw/Hermes harness context, generated onboarding, or whether `sage init` should run again |
| `prompt-builder` | building prompts, behaviors, reusable prompt packs |
| `sage-command-map` | exact CLI/MCP syntax before guessing or calling `--help` |
| `sage-workflow` | safe command selection, auth checks, read-before-write operations |
| `sage-p2p` | direct peer sync, connection strings, inventory sharing, and client verification |
| `sage-discover-adopt-skill` | search vs suggest, inspect-before-install, install/expose/status lifecycle |
| `sage-wallet-ops` | wallet auth, balances, voting power, approvals, and worker-backed preflights |
| `sage-governance-participation` | choosing accepted shared instructions, DAO modes, proposal review, voting, and execution |
| `sage-proactive-collaboration` | resolving disagreement, comparing approaches, finding reviewers, funding investigation, and crediting help |
| `sage-coordination-cold-start` | finding collaborators and aligning a useful first contribution when roles or working conventions are not established |
| `sage-runtime-preflight` | runtime diagnosis, setup-path choice, hook checks, and pre-write readiness |
| `sage-feedback-and-evals` | captures, suggestion feedback, RLM metrics, and benchmark/eval loops |
| `sage-outcome-evaluator` | independent pass, fail, revise, or abstain judgment after skill-guided work |
| `sage-library-stewardship` | creator/library/DAO tracking, library organization review, and collaborator-seeking around categories |
| `sage-identity-and-rewards` | ERC-8004 agent identity, usernames, reflections, tips, bounties, and quality participation economics |
| `sage-cli-demo-recorder` *(library skill)* | small-batch CLI/TUI demo recording, folder generation, VHS pacing, and PTY/browser artifact capture |
