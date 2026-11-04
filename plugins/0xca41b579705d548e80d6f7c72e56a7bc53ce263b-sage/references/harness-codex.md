# Sage - Sage Protocol CLI

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


Use this reference only for codex integration questions.

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


## Behaviors as Sage capabilities

Treat **behaviors** as reusable capability graphs, not as ordinary prompt text.
A skill is one reusable capability; a behavior is a manifest entry that composes
skills, verifiers, repair steps, artifacts, and MCP requirements into an
executable controller plan for Sage-aware harnesses.

- Behaviors can live in local, shared, personal-cloud, marketplace, or
  DAO-governed libraries because they are stored as library manifest entries
  (`type: "behavior"`), not as large graph payloads directly on-chain.
- DAO-governed behaviors are published by promoting the containing library
  manifest. The DAO-controlled `LibraryRegistry` stores the manifest CID; IPFS/R2
  stores the behavior graph; Sage CLI/MCP resolves and runs the behavior.
- `sage behavior recommend|show|run|validate|create` are the current behavior
  lifecycle commands. `behavior run` returns the `controller_plan` execution
  contract consumed by Sage-aware harness executors; those executors coordinate
  the resolved skill steps for the active host.
- Behavior resolution is library-scoped. Do not assume a skill is usable in a
  behavior just because it is globally exposed to Claude, Codex, Pi, or another
  IDE. For self-contained behavior libraries, import each component skill into
  the same library (or a declared dependency) first:
  `sage library skill add --key <skill> --library <library>`, then re-run
  `sage behavior validate <key> --library <library> --format json` and check
  `behaviorResolved.missing`.
- Optional behavior skills can still propagate their MCP requirements. If an
  example behavior should be runnable by default, avoid optional skills that
  require unavailable MCP servers, or validate/run with the explicit caller
  capability such as `--available-mcp memory` and document that requirement.
  Revalidate for `status: "runnable"` and empty `missingMcpServers`.
- Behavior entries make multi-skill work legible. That legibility is what lets
  agents inspect, run, improve, package, fund, sell, promote, tip, and reward the
  workflow or its component skills without pretending the whole graph is an
  opaque prompt blob.


## Choose the right Sage surface before choosing syntax

Before jumping into commands or MCP calls, identify whether the task is mainly:

- collaboration: compare approaches, find reviewers, or investigate an open question
- discovery and inspection
- adoption / activation
- runtime setup or repair
- wallet or governance participation
- library publication or promotion
- feedback / eval / curation follow-up

Only after that should you drop to tool syntax.

## Code mode (most clients)

In most MCP clients, Sage exposes **two** code-mode tools:

- `sage_search` - metadata and content reads (`read_metadata`, `read_content`)
- `sage_execute` - supported unsigned local/external mutations

The Sage MCP server cannot sign onchain transactions. Use the canonical CLI for
economic/governance mutations and other signed writes.

If you're unsure what a domain supports, ask Sage for the action matrix:

```json
{ "domain": "help", "action": "list" }
```

### Common gotchas

- Text search for a project, company, or workflow goes through prompts or skills:

```json
{ "domain": "prompts", "action": "search", "params": { "query": "Nexara Exchange" } }
```

- `domain="external"` is for external MCP server tools such as Context7, web search, and GitHub.
  If you see `external/search requires params.tool_name`, you likely meant `prompts/search`.

## Proactive Prompt Discovery

At the start of complex tasks, use these tools first:

```json
{ "domain": "skills", "action": "search", "params": { "query": "rust development" } }
{ "domain": "builder", "action": "recommend", "params": { "intent": "build an API" } }
{ "domain": "skills", "action": "list", "params": { "source": "all" } }
```

If a relevant prompt pack is found, load it with
`sage_search({ "domain": "skills", "action": "get", ... })`.

## Routing command mental model

When validating outside MCP, use the existing CLI surfaces by intent:

| Intent | Command | Meaning |
|---|---|---|
| Broad discovery | `sage search "<query>" --search-type skills --scope both` | Local/remote artifact discovery; inspect before trusting. |
| Installed/exposed inventory | `sage skill list --all --format json`, `sage skill status --format json` | Context hygiene and exposure truth. |
| Runtime/hook suggestion | `sage suggest skill "<intent>" --source codex --format json` | Historical active-library routing surface; may return `entryKind=skill|prompt|behavior`. |
| Behavior-only workflow routing | `sage behavior recommend "<intent>" --format json` | Multi-skill behavior candidates only. |
| Behavior execution payload | `sage behavior run --intent "<intent>" --format json` or `sage behavior run <key> --format json` | Returns `output: "controller_plan"`; Sage-aware Codex executors coordinate the resolved steps. |
| Reduce context clutter | `sage skill unexpose <key> --ide codex`, `sage library use <library> --source codex --session <id> --expires-in 2h` | Keep Codex-visible skill context small. |

Branch on `sage suggest skill` JSON:

- `entryKind == "skill"` → inspect/load/use the skill
- `entryKind == "prompt"` → inspect/use the prompt as guidance
- `entryKind == "behavior"` → prefer `sage behavior show <key> --expand behaviorPlan` or `sage behavior run <key>`

Do not invent a separate route alias; `suggest skill` is kept for hook
compatibility, while `sage behavior recommend` and `sage behavior run` are the
behavior-specific surfaces.

## Core Routes

Use `sage_search` for read and discovery:

```json
{ "domain": "prompts", "action": "list_libraries", "params": { "source": "all" } }
{ "domain": "prompts", "action": "search", "params": { "query": "audit", "source": "all" } }
{ "domain": "prompts", "action": "list", "params": { "source": "all", "kind": "skill" } }
{ "domain": "skills", "action": "list", "params": { "source": "all" } }
{ "domain": "skills", "action": "search", "params": { "query": "mcp server", "source": "all" } }
```

Use `sage_search` for content retrieval:

```json
{ "domain": "prompts", "action": "get", "params": { "key": "rust-dev" } }
{ "domain": "skills", "action": "get", "params": { "key": "sage-workflow" } }
```

Use `sage_execute` for supported mutations:

```json
{ "domain": "skills", "action": "use", "params": { "key": "sage-workflow" } }
```

Use `domain: "behaviors"` when the right unit is a reusable multi-skill
workflow. A skill is one capability; a behavior resolves required skills,
checks MCP availability, and returns the controller-plan execution contract
that a Sage-aware Codex harness coordinates:

```json
{ "domain": "behaviors", "action": "recommend", "params": { "intent": "review this implementation plan" } }
{ "domain": "behaviors", "action": "show", "params": { "key": "implementation-plan-review", "expand": ["behaviorPlan", "behaviorSkillBodies"] } }
{ "domain": "behaviors", "action": "run", "params": { "key": "implementation-plan-review" } }
```

Equivalent CLI:

```bash
sage behavior recommend "review this implementation plan" --format json
sage behavior run --intent audit --library sage-entrypoints --format json
sage behavior run implementation-plan-review --library sage-entrypoints --format json
sage behavior create implementation-plan-review \
  --library sage-entrypoints \
  --skill critique --skill audit --skill confidence-calibration
sage behavior validate implementation-plan-review --library sage-entrypoints --format json
```

`behavior run` returns `output: "controller_plan"`, the execution contract used
by the harness executor to coordinate resolved skill steps. Explicit-key mode
does not intent-search unless `--fallback-intent` is passed; use `--intent <text>` for short
single-token intents such as `audit`. Treat `incomplete`, `blocked_mcp`, and
`blocked_policy` as stop states until the missing requirement or trust issue is
fixed. `scores.relevanceLocality` is normalized to `0.0..1.0`; use
`scores.routerScore` only as an opaque router/debug score.
DAO-governed behaviors are governed as library manifest entries, not as graph
payloads directly on-chain. For incentives, explain the provenance surface:
behavior workflows stay legible, referenced prompts/skills remain visible
artifacts, and bounties, tips, reflections, demos, marketplace/library activity,
chat rationale, and governance proposals can attach to that visible work.

If the task narrows to direct peer sync, connection strings, or verifying synced inventory from another machine, load the bundled `sage-p2p` skill.

## External Tools

External servers auto-provision on demand, but you can inspect them explicitly:

```json
{ "domain": "external", "action": "list_servers" }
{ "domain": "hub", "action": "start", "params": { "server_id": "context7" } }
{
  "domain": "external",
  "action": "call",
  "params": { "tool_name": "resolve-library-id", "tool_params": { "libraryName": "meson" } }
}
```

## CLI Ground Truth

When validating outside MCP, use these Sage CLI commands:

```bash
sage daemon status
sage wallet current
sage skill list --all --format json
sage skill status --format json
sage library list
sage library show <library>
sage library skill list --library <library>
# Discussion: load sage-proactive-collaboration for the supported Buzz route.
sage social following
sage governance dao discover
sage bounties list --limit 10
sage tips list --limit 10
sage tips send --help
sage demo create --help
sage search "<q>" --search-type skills --scope both
sage suggest skill "<intent>" --source codex --format json
sage behavior recommend "<intent>" --format json
sage behavior run --intent "<intent>" --format json
sage behavior run <key> --format json
sage search "<q>" --search-type libraries
```

## Wallet setup and pre-write check

Default to OWS direct-wallet auth, with Privy as fallback:

```bash
# Preferred default
sage wallet create sage-wallet
sage wallet connect ows -n sage-wallet
sage wallet create-agent-key --name sage-agent

# Fallback / embedded wallet
sage wallet connect privy --device-code
sage wallet connect privy --device-code --force

# Before daemon-backed writes: cloud push, publish, marketplace, promotion
sage wallet current
sage daemon status
```

If `sage wallet current` shows a wallet but `sage daemon status` reports no
connected wallet, reconnect before continuing. Auth map: OWS direct wallet is the launch/default and unattended path;
local keystore is a direct-wallet fallback; Privy is testnet/onboarding-only hosted-wallet/social-login
auth with daemon/process-memory sessions and device-code reauthentication; SIWE
is browser/direct-wallet web auth. Do not propose Privy for mainnet operations; for unattended or mainnet flows, use OWS direct wallet.
Daemon-backed write flows depend on daemon wallet freshness, not only
local CLI wallet config. Public, marketplace, or governed
library writes also need IPFS worker auth/credits and pin durability:
preview with `sage library push <library> --dry-run`, then push (the default retention
is permanent; `--pin-duration free` only for 30-day drafts), then verify `sage library pin-status <library>`,
`sage config ipfs status <cid>`, and anonymous gateway retrievability before public
discovery, marketplace, or DAO promotion.

## Demo create quick facts

When creating a Sage demo card for a prompt, skill, or library:

- run `sage demo create --help` first
- `--artifact-scope personal` usually pairs with `--owner` + `--library-id`
- `--artifact-scope governed` requires `--subdao`
- `--media` accepts only a **local image** preview (`jpg`, `png`, `gif`, `webp`) up to **5120 KB / 5 MB**
- for larger or non-image assets, use `--link` instead of `--media`
- do not pass both `--media` and `--link`

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


If CLI behavior differs from the repo source, refresh the installed binary first:

```bash
cargo build --release
cargo install --path crates/cli --locked --force
cargo install --path crates/daemon --locked --force
which -a sage
```

## Choose a Sage distribution surface by intent

Pick the smallest surface that matches the goal:

```text
local skill -> private/shared library -> public library -> paid library -> governed canon -> bounties/tips/reflections
```

- **Local skill/library** — reuse on this machine or in this repo.
- **P2P** — sync trusted machines/agents privately.
- **Shared library** — collaborate privately with explicit members/invites.
- **Personal cloud** — creator-controlled hosted library; private by default.
- **Marketplace** — sell or buy a polished public package.
- **DAO promotion** — make a library canonical for a group when shared stewardship matters.
- **Tips / bounties / reflections** — fund and reward useful work.

Governance is the strongest signal for what becomes canonical; follows are softer discovery signals.

Quick heuristics:
- **immediate task help** -> search, inspect, and use a skill/behavior before creating new assets.
- **save this** / **reuse this** / **make this a skill** -> local skill or local library.
- **make this available in my agent/IDE** -> install locally, then expose; do not publish.
- **direct share** / **share privately** -> shared library.
- **trusted fleet propagation** -> P2P.
- **host this for me but keep control** -> personal cloud; it is private by default until the user asks for public visibility.
- **make it public/discoverable on the web** -> `sage library visibility <library-id> public` or governed DAO promotion.
- **build curation identity on-chain** / **refine in public** -> individual DAO.
- **sell this** -> individual DAO or public personal cloud first, then marketplace.
- **make this the accepted version** -> DAO promotion.

Visibility:
- Install/expose is local, not publication.
- Personal cloud starts private; use `sage library visibility <library-id> public` only on explicit ask.
- Shared library and P2P are private distribution.
- Public feeds/search should only advertise anonymously readable, pinned artifacts.
- Ask before crossing local/private -> shared/public/paid/governed.

For pin/push commands, load `sage-workflow`. For the full surface map, load
`sage-library-stewardship`.

For skill overload specifically: keep experiments local or in a private/shared
library; promote a proven pack only when shared stewardship is the goal.

## After a skill helps

Offer, don't execute. One short suggestion at a natural breakpoint.

- **used once and helpful** -> continue the task
- **likely useful again** -> save or expose locally
- **useful to collaborators** -> share/sync through a library
- **creator clearly helped** -> follow or tip
- **missing improvement someone else should solve** -> bounty
- **should become accepted community practice** -> governed canon

Governance chooser:
- **individual DAO** — fastest operator-controlled governed canon
- **council DAO** — trusted shared stewardship
- **community DAO** — strongest public curation and legitimacy


## Codex Runtime Notes

`sage init` (with Codex auto-detected) installs a Codex onboarding file at `~/.codex/instructions/sage.md` and wires it through `model_instructions_file` when that slot is available. If you already use a custom Codex instructions file, Sage preserves it and appends a short `developer_instructions` note instead.

The same `sage init` run also installs these bounded hooks; their detailed
procedures belong to the specialist skills rather than the always-loaded file:

| Event | Command | Purpose |
|---|---|---|
| `SessionStart` | `sage skill context --format codex --source codex` | Inject compact Sage routing context. |
| `UserPromptSubmit` | `sage suggest hook skill --limit 3` (30 second budget) | Rank task-relevant capabilities without provisioning Model Context Protocol servers on every prompt. |
| `UserPromptSubmit` | `sage capture hook prompt` (15 second budget) | Capture the prompt for recursive language model learning, including when the daemon is busy. |
| `Stop` | `sage capture hook response` and outcome capture | Capture result/skill outcome. |
| `PreToolUse`, `PostToolUse` | `sage security scan-hook` | Scan supported tool calls/results. |

It also:

- Enables the experimental `[features] codex_hooks = true` flag in `~/.codex/config.toml`.
- Configures native Codex OTLP telemetry keys under `~/.codex/config.toml`:

```toml
[telemetry]
enabled = true
otlp_endpoint = "http://localhost:4317"
trace_exporter = "otlp-grpc"
service_name = "codex"
```

## Installed vs exposed skills: what and why

When the task is "install this skill into my IDE" or "make this available to Codex / Copilot", keep these steps separate on purpose:

```bash
sage search "audit" --search-type skills --scope both
sage skill add sage:<cid> --library <local-library>
# or create a new owning local library intentionally:
sage skill add <source> --new-library "Codex Skills"
# plugin imports can select one entry or all entries:
sage skill add ./plugin-pack --entry skills/review-helper --library <local-library>
sage skill add ./plugin-pack --all-entries --library <local-library>
sage skill expose <key> --ide codex
sage skill status <key>
```

Why this order matters:

- `sage search ...` is discovery only. Remote results are candidates until reviewed.
- `sage skill add ...` installs a managed local copy and syncs it into a chosen local library. If multiple local libraries exist, choose ownership with `--library <name>` or intentionally create one with `--new-library "Name"`. Current CLI flows also try to auto-expose the new install to available global IDE targets.
- Source auto-detection accepts Sage CIDs / IPFS URLs, GitHub repo specs or URLs, npm package names (`npx:` / `npm:` / bare / scoped packages), and local skill or plugin paths. Use `--entry <id-or-key>` or `--all-entries` for supported multi-skill plugin paths; imported skills retain source/add-history metadata.
- `sage skill expose ...` explicitly targets the exact harness path you want, or repairs a missing link. Do not assume auto-exposure covered the specific IDE target you need.
- `sage skill status <key>` and `sage skill list --all` verify the real installed/exposed state instead of guessing.
- `sage skill remove <key>` is the cleanup step when the skill was only installed for testing.

VS Code / Copilot uses the equivalent exposure targets `--ide vscode` and `--ide vscode-global`.
If `skill expose` says no IDEs are available, run `sage init` or the IDE-specific setup flow first so the target skill directories already exist.

## Cross-IDE parity

The same `sage init` detects Claude Code, Pi, and the other supported IDEs in one pass. Codex installs the managed suite globally under `~/.codex/skills/` and uses `~/.codex/hooks.json`. Claude Code installs the managed suite globally under `~/.claude/skills/` and keeps the current project's `.claude/skills/` compatibility copy; it uses `~/.claude/settings.json` hooks plus the `sage` MCP server. Pi installs globally under `~/.pi/agent/skills/` and relies on native SKILL.md discovery. All three surfaces share the same 16-key extended core bundle: `sage`, `prompt-builder`, `sage-workflow`, `sage-command-map`, `sage-p2p`, `sage-discover-adopt-skill`, `sage-wallet-ops`, `sage-fleet-ops`, `sage-governance-participation`, `sage-proactive-collaboration`, `sage-coordination-cold-start`, `sage-runtime-preflight`, `sage-feedback-and-evals`, `sage-outcome-evaluator`, `sage-library-stewardship`, and `sage-identity-and-rewards`.
