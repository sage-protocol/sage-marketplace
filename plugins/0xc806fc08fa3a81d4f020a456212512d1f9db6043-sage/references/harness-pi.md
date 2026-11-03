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


Use this reference only for pi integration questions.

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

## Code mode tools

Sage exposes **two** tools — `sage_search` (read/discovery) and `sage_execute` (write/mutation) — plus direct `hub_*` tools for server lifecycle.

Use `sage_search` for discovery:

```json
{"domain":"prompts","action":"search","params":{"query":"rust development"}}
{"domain":"skills","action":"list"}
{"domain":"builder","action":"recommend","params":{"intent":"build an API"}}
{"domain":"governance","action":"list_subdaos"}
{"domain":"help","action":"list"}
```

Use `sage_execute` for actions:

```json
{"domain":"prompts","action":"get","params":{"key":"rust-dev"}}
{"domain":"prompts","action":"create","params":{"key":"my-prompt","name":"My Prompt","content":"..."}}
{"domain":"skills","action":"get","params":{"key":"sage-workflow"}}
{"domain":"skills","action":"use","params":{"key":"mcp-builder"}}
```

Use `domain:"behaviors"` when the user needs a reusable multi-skill workflow
instead of one skill. Pi does not have Sage hook routing, so call behavior
commands or code-mode actions manually:

```json
{"domain":"behaviors","action":"recommend","params":{"intent":"review this implementation plan"}}
{"domain":"behaviors","action":"show","params":{"key":"implementation-plan-review","expand":["behaviorPlan","behaviorSkillBodies"]}}
{"domain":"behaviors","action":"run","params":{"key":"implementation-plan-review"}}
```

Equivalent CLI:

```bash
sage behavior recommend "review this implementation plan" --format json
sage behavior run --intent audit --library sage-entrypoints --format json
sage behavior run implementation-plan-review --library sage-entrypoints --format json
sage behavior validate implementation-plan-review --library sage-entrypoints --format json
```

`behavior run` returns `output: "controller_plan"`, the execution contract used
by Sage-aware harness executors to coordinate resolved skill steps. Respect
`runnable`, `incomplete`, `blocked_mcp`, `blocked_policy`, and `not_found`; do
not auto-run remote or untrusted behaviors without inspection. Use `--intent
<text>` for short single-token intents because Pi has no pre-prompt behavior
hook. DAO-governed
behaviors are governed through the containing library manifest CID. For
incentives, explain the provenance surface: behavior workflows stay legible,
referenced prompts/skills remain visible artifacts, and bounties, tips,
reflections, demos, marketplace/library activity, chat rationale, and governance
proposals can attach to that visible work.

External tools (web search, GitHub, memory, docs) auto-provision on demand:

```json
{"domain":"external","action":"list_servers"}
{"domain":"external","action":"call","params":{"tool_name":"brave_web_search","tool_params":{"query":"..."}}}
{"domain":"external","action":"call","params":{"tool_name":"resolve-library-id","tool_params":{"libraryName":"meson"}}}
```

Direct hub tools: `hub_list_servers`, `hub_start_server`, `hub_stop_server`, `hub_status`, `hub_session_list`, `hub_add_server` (registers only — start next). Prefer aliases for external tools (`sage mcp call <alias>`); do not use `server_id:tool_name`.

If the task narrows to direct peer sync, connection strings, or verifying what another machine actually received, switch to the bundled `sage-p2p` skill.

## Routing command mental model

Pi has no Sage hook system, so use the manual command equivalents directly:

| Intent | Command | Meaning |
|---|---|---|
| Explore what exists | `sage search "<query>" --search-type skills --scope both` | Broad local/remote discovery; inspect before trusting. |
| Inspect installed/exposed skills | `sage skill list --all --format json`, `sage skill status --format json` | Inventory and context hygiene. |
| Runtime recommendation | `sage suggest skill "<intent>" --source pi --format json` | Active-library suggestions; may return skills, prompts, or behaviors. Inspect `entryKind`. |
| Workflow recommendation | `sage behavior recommend "<intent>" --format json` | Behavior-only workflow candidates. |
| Behavior execution payload | `sage behavior run --intent "<intent>" --format json` or `sage behavior run <key> --format json` | Returns `output: "controller_plan"`; Sage-aware Pi executors coordinate the resolved steps. |

Branch on `entryKind`: `skill` means inspect/load/use the skill, `prompt`
means use it as prompt guidance, and `behavior` means inspect/run through
`sage behavior show <key>` or `sage behavior run <key>`. Do not invent a
separate route alias.

## Quick Commands

```bash
sage doctor                          # Runtime health first
sage wallet current                  # Direct wallet/session status
sage daemon status                   # Daemon wallet/runtime status
sage library list                    # Library authoring surfaces
sage governance dao discover         # DAO discovery and governance-mode context
# Discussion: load sage-proactive-collaboration for the supported Buzz route.
sage social following                # Current follow graph
sage bounties list --limit 10        # Funded-work surfaces
sage tips list --limit 10            # Tip history / recognition surface
sage tips send --help                # Tip send flags; dry-run before signing
sage reflection list                 # Reward / reflection surface
sage agent info                      # ERC-8004 identity status
sage demo list                       # Capability demos
sage demo create --help              # Demo-create flags, media constraints, examples
sage capture status                  # Local RLM capture state
sage metrics rlm                     # Local RLM analytics state
sage suggest skill "task" --format json # Active-library suggestions; inspect entryKind
sage behavior recommend "task"       # Get reusable multi-skill behavior suggestions
sage behavior run --intent audit     # Single-token intent; returns controller_plan execution contract
sage behavior run <key>              # Return behavior execution payload for the harness executor
sage skill add <source>              # Install prompt pack (legacy alias: sage prompt add)
sage mcp hub list                    # Registered servers (not necessarily running)
sage mcp hub status                  # Running set (daemon required)
sage mcp hub start <id>              # Policy-gated start; persists callable aliases
sage mcp call <alias> --args '{...}' # Prefer aliases after start
```

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


Notes:
- `marketplace` is a real top-level CLI family in the current binary; `auction` is still intentionally out of scope here.
- Marketplace coverage now spans worker-native whole-library snapshot flows (`marketplace library list`, `show`, `set-price`, `unlist`, `buy`, `entitlement`, `download`, `save`), personal cloud publish (`library push --cloud`, `library visibility`), governed promotion (`library promote`), demos, and non-CLI web/worker surfaces. Do not suggest legacy `marketplace prompt ...` commands.
- Do not assume one generic promotion path: community DAOs can be seeded with `--manifest-cid` at creation, while individual/council-style flows publish first and promote after creation.
- Governance-type chooser: `individual` for owner-controlled updates, `council` for named shared stewardship, `community` for token-holder voting. These are alternatives, not a progression; voting establishes an authorized decision, not factual correctness. Always inspect with `sage governance dao info` + `sage governance proposals list` before assuming `proposals vote` is the active path.
- Proposal title convention: the on-chain description is a single string; the web app renders `first_line = title` and `rest = body`. `library promote` prepends `Add library: <name>` / `Update library: <name>` as the title line. Override with `--description "Custom title\n\nCustom body"` when you need a different title. Use `sage governance proposals status <id> --dao 0x...` to verify lifecycle + inspect stored description.
- Proposal execute is lifecycle-aware: `Queued + Ready` submits, `Queued + Waiting` reports ETA and exits, `Queued + Unset` (indexer lag) attempts optimistically, `Defeated|Canceled|Expired` refuses with a reason.
- Current launch risk is not CLI absence but worker/auth reliability, end-to-end listing availability, and confusion between voteable governor flows versus council/timelock flows.

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


## Wallet Model

- `sage wallet current` reports the direct wallet session and, when present, the selected on-chain delegation for the active chain.
- Preferred default: create/connect an OWS direct wallet with `sage wallet create sage-wallet`, `sage wallet connect ows -n sage-wallet`, then `sage wallet create-agent-key --name sage-agent` for automation.
- Local keystore is a direct-wallet fallback when OWS is unavailable.
- Fallback hosted-wallet/social-login wallet: `sage wallet connect privy --device-code` or `sage wallet connect privy --device-code --force`; Privy bearer sessions are daemon/process-memory only and require device-code reauthentication after daemon restart.
- SIWE/browser sessions are separate direct-wallet web auth.
- Do not propose Privy for mainnet operations. Privy is testnet/onboarding only; for unattended or mainnet flows, use OWS direct wallet.
- Before daemon-backed writes (`library push --cloud`, publish, marketplace, promotion), check both `sage wallet current` and `sage daemon status`; reconnect if they disagree.
- Before public, marketplace, or governed library writes, verify IPFS worker auth/credits and pin durability: `sage config ipfs balance`, `sage library push <library> --dry-run`, then push; the default retention is permanent (`--pin-duration free` only for 30-day drafts). After pushing, confirm `sage library pin-status <library>`, `sage config ipfs status <cid>`, and anonymous gateway retrievability before public discovery, marketplace, or DAO promotion.

## Environment Variables

- `BRAVE_API_KEY` - For brave-search server (web/news/local/video search)
- `GITHUB_TOKEN` - For github server tools

## Pi Runtime Notes

`sage init` (with Pi auto-detected) installs the extended core bundle under `~/.pi/agent/skills/`: `sage`, `prompt-builder`, `sage-workflow`, `sage-command-map`, `sage-p2p`, `sage-discover-adopt-skill`, `sage-wallet-ops`, `sage-governance-participation`, `sage-proactive-collaboration`, `sage-coordination-cold-start`, `sage-runtime-preflight`, `sage-feedback-and-evals`, `sage-outcome-evaluator`, `sage-library-stewardship`, and `sage-identity-and-rewards`. Pi has no hook system, so there is no equivalent to Codex `~/.codex/hooks.json` or Claude `~/.claude/settings.json` hook-based routing — Pi's native skill loader discovers these files directly and the agent loads them through normal skill invocation.

Because there are no pre-prompt hooks, Pi does not receive automatic ranking
injection. A process/meta result for a concrete job is a routing miss: broaden
once or use a known exact task specialist. Feedback is not a required turn
close; unresolved suggestions auto-settle to neutral skip.

**Procedure load (Pi-critical):** Pi has **no** Sage UserPromptSubmit skill injection. Skills execute as **instructions for the model** (not a Sage runtime). Prefer **native load**: `/skill:<name>` or `read` `~/.pi/agent/skills/<name>/SKILL.md` (or project `.agents/skills/`). Optional rank: `sage suggest skill` (distilled shortlist only). Then **freestyle with tools** under skill constraints. Library-only body: `sage library inspect skill get <key> -l <lib>` or MCP `get_skill`/`use_skill`. Never `sage skill context <key>` for load. Record explicit use only after material guidance and an outcome only after verification.

**Agent-managed session scope (automatic, every Pi run):** Pi has no pre-prompt hooks, so the agent must own ranking scope.

```bash
export SAGE_SOURCE=pi
export SAGE_SESSION_ID=<stable-run-id>   # reuse for suggest + feedback this run
# One-shot orient (+ optional Session align). Never mutates Project/Default.
sage library select navigate --source pi --session "$SAGE_SESSION_ID" --format json
sage library select navigate --align-session --source pi --session "$SAGE_SESSION_ID" \
  --expires-in 8h --format json
# Fallback when the pack is already known:
sage library select use <project-pack> --source pi --session "$SAGE_SESSION_ID" \
  --expires-in 8h --only --format json
# Then rank:
sage suggest skill "<intent>" --source pi --session "$SAGE_SESSION_ID" --format json
```

Rules: `activate` ≠ ranking (`select activate` is IDE exposure only). Prefer `navigate --align-session` or session-scoped `select use` over permanent profile mutation. Do not invent packs from path alone — trust `navigate` candidate/evidence. Feedback/evals is an explicit evaluation path, not a mandatory closeout.

**Pi exposure safety:** Pi scans project/global `.pi` and `.agents` skill roots as one collision namespace. Library activation protects current-project skills by default. `--allow-pi-skill-collision` accepts risk for one activation but does not clear an existing suppression. Keep a durable per-key decision with `sage skill unexpose <key> --namespace pi --persist`; clear it only with `sage skill expose <key> --namespace pi --clear-suppression --force`. Suppression removes only Sage-owned Pi-visible exposure, not non-Pi native exposure, and startup/update reconciliation honors it. Run `sage doctor --scope skills --include-details` in each relevant project: doctor distinguishes actual, prospective, and protected collisions, and says when no project scan ran. Sage cannot predict skills later added to unknown projects. Old daemons ignore suppressions, so remove affected Sage-owned Pi exposure before rollback.

In headless runs (`pi -p`), use an exact known specialist first. Rank before
acting only when no exact specialist is known; inspect scope after a routing miss.

Routing feedback (only after material guidance or explicit rejection):

```bash
sage_mark_guided_use({ skills: ["<current-suggested-key>"] })   # preferred inside the Pi adapter
SAGE_SOURCE=pi sage suggest feedback settle use <library/key> --outcome passed|failed|revised --format json  # primary manual/headless write
SAGE_SOURCE=pi sage suggest feedback use --used <library/key>   # two-step fallback with a real correlation
SAGE_SOURCE=pi sage suggest feedback reject
```

The Pi tool is the mechanical `Use` declaration: the candidate must be in the
current suggestion and its full procedure must have been loaded in this Pi
session. Reads alone do not count. Calls are additive when another current
candidate is applied later in the same turn.

Automatic skip is the normal neutral close when no specialist guided the work.
`reject` is a negative signal only when the user explicitly says a shown
suggestion was wrong.

Execution feedback (did the skill actually work when used):

```bash
# Primary when routing use is still pending:
SAGE_SOURCE=pi sage suggest feedback settle use <skill-key> --outcome passed|failed|revised --format json
# Two-step fallback after the adapter or manual use write:
sage suggest feedback outcome <skill-key> --status passed --source pi
sage suggest feedback outcome <skill-key> --status failed --source pi
sage suggest feedback outcome <skill-key> --status revised --source pi --query-preview "short context"
```

An unknown `<skill-key>` is refused (exit non-zero, nothing written, near-miss suggested) so a typo cannot invent ranking data — report the exact key, or add `--allow-unknown-key` for a remote/P2P skill.

The signals remain distinct even though the primary command writes them atomically:
a skill can be `use`d and still `failed` at execution. Keep the two-step form for
cases where the use write already exists.

## Installed vs exposed skills: what and why

When the task is "install this skill into my IDE" or "make this available to Copilot/Codex/Pi", keep these steps separate on purpose:

```bash
sage search "audit" --search-type skills --scope both
sage skill add sage:<cid> --library <local-library>
# or create a new owning local library intentionally:
sage skill add <source> --new-library "Agent Skills"
# plugin imports can select one entry or all entries:
sage skill add ./plugin-pack --entry skills/review-helper --library <local-library>
sage skill add ./plugin-pack --all-entries --library <local-library>
sage skill expose <key> --ide <target>
sage skill status <key>
```

Why this order matters:

- `sage search ...` is discovery only. Remote results are candidates until reviewed.
- `sage skill add ...` installs a managed local copy and syncs it into a chosen local library. If multiple local libraries exist, choose ownership with `--library <name>` or intentionally create one with `--new-library "Name"`. Current CLI flows also try to auto-expose the new install to available global IDE targets.
- Source auto-detection accepts Sage CIDs / IPFS URLs, GitHub repo specs or URLs, npm package names (`npx:` / `npm:` / bare / scoped packages), and local skill or plugin paths. Use `--entry <id-or-key>` or `--all-entries` for supported multi-skill plugin paths; imported skills retain source/add-history metadata.
- `sage skill expose ...` explicitly targets the exact harness path you want, or repairs a missing link. Do not assume auto-exposure covered the specific IDE target you need.
- `sage skill status <key>` and `sage skill list --all` verify the real installed/exposed state instead of guessing.
- `sage skill remove <key>` is the cleanup step when the skill was only installed for testing.

For VS Code / Copilot specifically:

```bash
sage skill expose <key> --ide vscode
sage skill expose <key> --ide vscode-global
```

If `skill expose` says no IDEs are available, run `sage init` or the IDE-specific setup flow first so the target skill directories already exist.

## Cross-IDE parity

The same `sage init` detects Claude Code, Codex, Pi, and the other supported IDEs in one pass. Claude Code installs globally under `~/.claude/skills/` and keeps the current project's `.claude/skills/` compatibility copy; it uses `~/.claude/settings.json` hooks plus the `sage` MCP server. Codex installs globally under `~/.codex/skills/` and uses `~/.codex/hooks.json` with the experimental `codex_hooks` feature flag. Pi installs globally under `~/.pi/agent/skills/` and uses SKILL.md discovery only. All three surfaces share the same 16-key extended core bundle: `sage`, `prompt-builder`, `sage-workflow`, `sage-command-map`, `sage-p2p`, `sage-discover-adopt-skill`, `sage-wallet-ops`, `sage-fleet-ops`, `sage-governance-participation`, `sage-proactive-collaboration`, `sage-coordination-cold-start`, `sage-runtime-preflight`, `sage-feedback-and-evals`, `sage-outcome-evaluator`, `sage-library-stewardship`, and `sage-identity-and-rewards`.
