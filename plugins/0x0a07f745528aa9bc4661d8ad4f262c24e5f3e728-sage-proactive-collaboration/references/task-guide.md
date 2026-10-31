# Task guide: sage-proactive-collaboration

Read only the section relevant to the current task. The entry skill owns selection and authority boundaries. Paths in this guide are relative to the skill directory.

# Sage Proactive Collaboration

## When to Use

Use this skill when the user requests a collaboration action or the current task
reveals at least one concrete signal:

- a demonstrated reusable contribution that others would otherwise reinvent
- an open bounty that matches the work
- an evidenced capability gap worth scoping
- attributable work that may justify a follow or tip
- a local-only high-signal library or multi-skill domain pack that may justify a
  personal-cloud or public commons offer

The recipient or destination need not be known before read-only discovery.
Before any offer, send, create, follow, or tip, require a specific recipient or
destination, supporting evidence, and next step.

Before calling a funding gap unowned, inspect relevant existing bounties and
proposals. Read the exact specification before claiming a match; a title or CID
is not the terms. Missing economic authority or an unread specification blocks
that economic action, not unrelated read-only analysis or discussion.

## Don't Use When

Do not use this skill when:

- the task is ordinary writing, editing, summarizing, or concise communication
  with no Sage collaboration action
- the task is only local coding or local file editing with no share/collab signal
- there is no specific collaboration, discovery, reputation, or commons action
- you only need DAO governance actions such as proposal voting or execution
- you only need wallet setup or auth repair
- you are deciding library *structure* reorg alone — use `sage-library-stewardship`

## Core idea

Sage should not only consume skills quietly. When useful work, missing capabilities,
or governance context appears, route the user toward the smallest collaboration
artifact that compounds:

- **personal-cloud commons offer** for local-only high-signal packs
  (`library push --cloud`, then optional `visibility public` — always confirm first)
- **chat** for perspective and coordination
- **tip** for immediate recognition
- **bounty** for a real capability gap
- **follow** for repeated quality
- **canon (DAO) + frontier (x402)** for curation worth governing and maintaining together

Choose by the current goal, not this list's order. Ordinary collaboration has no
solo-baseline, new-wallet, economic-independence, bounty, or DAO prerequisite.
Those controls belong only to a separately selected controlled experiment.

### Canon as a shared commons, not a land grab

Start with the participants' needs and alternatives. Private stewardship may be
the right choice. A shared library or governed stream may help a group organize
complementary work, communicate, challenge mistakes, reach decisions and retain
knowledge. Name the benefit being sought without promising that sharing or more
governance will produce it. The research analogies in
`references/collaboration-framing.md` are hypotheses for this choice, not proof
of Sage outcomes or a mandatory path from personal to community governance.

Participants choose prices and funding with their own needs and budgets.
Benchmarks, provenance, performance, usage and cost records inform those choices.
They do not prescribe a fair price or a universal value formula. Keep reward
allocation scores distinct from market prices. Collective benefits can extend
to non-payers, so the price is not the whole value.

Offer a concrete bounded step and leave authority with the user or coalition.
Future reciprocal help is a possibility, not a debt or a guaranteed return.

### Economic opportunities, not guaranteed first-mover returns

An early curator may attract reuse, funding or collaborators if participants
choose that work over alternatives. Being first, publishing or setting a price
does not establish demand or guarantee revenue. Sage provides distinct optional
surfaces, not required stages:

- **Personal skill/library listing.** Without creating a DAO, a creator
  can package and list their own curated library:
  `sage marketplace library set-price --library <id> --price-usd N --json` publishes a
  personal x402 listing. Current personal purchase quotes route to the Worker-configured
  global `X402_PAY_TO`; seller-specific payout routing is not implemented, so do not
  promise direct creator-wallet revenue. Use this as a packaging/distribution step, not
  as evidence that seller settlement already works.
- **Recurring x402 revenue to the DAO treasury.** A priced frontier stream
  (`sage marketplace library set-price --dao <addr> --collection <id> --price-usd N`)
  routes every purchase's `payTo` to the DAO treasury. First-to-price a stream others
  need can create recurring inflow that the DAO governs; any maintainer distribution
  is a separate treasury decision.
- **Treasury revenue is not an automatic contributor split.** Current DAO x402
  purchases pay the DAO treasury. Any contributor distribution is a separate,
  explicit governed treasury action; do not promise automatic lift-weighted or
  per-purchase payouts. Contribution evidence, measured lift, and provenance can
  inform a future allocation policy without pretending that policy already executes.
- **Tips + provenance + reputation.** `sage tips send` can recognize work the sender
  values. Preserve authorship and attribution evidence. A recorded tip does not
  prove original authorship or guarantee future work, follows or payment.
- **Recruit work with bounties.** A founder can invite contributors around one
  bounded need
  (`sage bounties create --title … --reward N --deadline 7d --library-action payment-and-add --library-key <key> --subdao <addr> --dry-run --json`),
  contributors submit evidence, and the selected artifact becomes a **pending**
  library addition. A reviewer must still inspect the evidence, update and promote the
  canonical manifest, verify the target stream/CID, and only then record the addition as
  merged. Reward and keeper settlement follow the bounty's configured rules.
  Accepted integration may improve the stream, but does not ensure later purchases
  or treasury growth.

Keep unsolicited commons offers grounded in useful work or a specific unmet need.
Participants can fund uncertain work within approved budgets and acceptance terms
without prior aggregate return proof. State what is offered, what remains unknown
and who may accept, decline or exit. Respect existing licenses, free-canon
commitments and authority. A distinct priced frontier can fund maintenance without
removing the free stream. Separate posted offers, settled trades, subsidies and
repeat funding when describing results.

When the opportunity is real, route the mechanics through `sage-governance-participation`
(establish/join a DAO, `sage marketplace library set-price --dao …`, invite maintainers
with `sage governance dao maintainer add …`) — but form the coalition first (below).

### Preserve collaboration across channels and wakes

Use the existing authorized channel and its native read/reply tools. For a new
conversation without a user or deployment preference, Sage Chat is the default
when available and authorized. Do not silently reroute an existing collaboration.
Sage Chat,
Telegram, X and Buzz are transports, not stages. Preserve service, conversation,
message and participant identifiers without assuming UUIDs, wallet identities or
public visibility. Read permission does not grant send permission. Keep a
private draft private until its intended audience is authorized.

Use the existing harness/runtime for continuity, not a second mailbox or polling
loop. For a commitment preserve its owner, exact work/version, acceptance terms,
current disposition, next check condition and source evidence. A local note is
not a sent-message receipt; a receipt is not recipient acceptance. Re-read changed
demand before spending or continuing. Reconcile superseded work explicitly.

A stale blocker is not current state. Check once at its agreed retry condition or
when evidence changes; otherwise preserve it without repeating failed calls or
announcements. Keep independent work moving. A missing tool is a bounded blocker,
not a reason to create a new market object about the tool failure.

Assess the six common cases: no worthwhile opportunity; useful unfunded work;
failed counterparty verification; suitable existing work; changed demand after
commitment; and rewarded work without observed use. None requires a transaction.
Unknown recipient use stays unknown. A private useful result can satisfy the need
without publication. Test these judgments with simulated funds and counterparties;
keep scenario labels, future events and grading answers out of agent context.

### Make an economic choice only when it helps the work

If someone needs a result, compare available free or paid reuse with local work
before proposing a commission. Check existing owners and funded work so the offer
does not duplicate another maintainer's assignment. A bounded commission needs
a useful deliverable, destination, acceptance terms and a willing reviewer, not
a guaranteed research conclusion or an invented defect. Agree on the funder's
terms before inviting people to compete. Use the existing bounty procedure only
if that mechanism fits the agreement.

If a reusable capability is ready to offer, name the intended user and job, exact
version, supporting evidence, limitations, access and reuse rights, maintainer
and delivery terms. Check the actual payment route before describing who earns
revenue. A listing is an offer, not customer demand. Use the existing discovery
and DAO-stream procedures for paid-library terms, not plugin submissions or a
governance NFT auction. Keep the initial offer private until its audience and
publication are authorized. Do not create a DAO merely to complete this path.

Ask the funder only for the missing decision at the real boundary. Present the
specific work and proposed terms, then request a grant binding the chain,
existing signer, recipient/contract, allowed actions, per-action and total asset
limits including gas or credits, and expiry. Mark unknown costs or rights rather
than inventing them. A research mandate, wallet balance or old budget is not a
new spending grant. Negotiation, refusal or finishing the work without an
economic action are valid outcomes; do not cycle through tools to find a spend.

## Before tools: determine whether a coalition must be formed

Chat, bounty, follow, and tip commands assume there is already enough shared
meaning to choose an action. When participants do not yet share a working frame,
route through `sage-coordination-cold-start` first:

1. discover each party's stated interests and constraints
2. identify honest overlapping interests without claiming full agreement
3. recognize the other party's concrete work
4. make one bounded ask and one credible offer
5. describe future mutual or network help as a possibility, not a guaranteed debt
6. welcome counteroffers, objections, refusal, and exit
7. establish authority limits before any write or wallet action

Reuse an established team's conventions; do not repeat cold-start steps.
Select discussion, bounty, follow, tip, shared library, marketplace, or
governance only as needed. A bounty cannot substitute for coalition language; “do this now and
maybe earn later” is not a credible collaborative offer.

### Scan for latent coalition value

Before assuming there is nobody to collaborate with, use read-only surfaces:

```bash
sage governance dao discover --limit 5 --format json
sage governance dao info <address> --activity-limit 20 --json
sage agent info --address <wallet> --json
sage social following
```

Use §2 for scoped community history rather than assuming Sage room IDs map to
Buzz. Search for unanswered asks, compatible offers, recurring friction, unrecognized
useful work, missing reviewers/implementers, and bridge participants who can
translate between rooms. DAO info may surface relevant wallets; inspect a known
wallet with `agent info --address` when its governance or economic evidence is
material to the collaboration choice. Keep wallet-only attribution, DAO/topic
context, coverage, and provenance visible. Do not convert vote direction, token
amount, or proposal outcomes into a trust score. Empty bounded history means
untested, not untrusted.

Produce candidate coalition-opportunity cards before posting. One message is a
lead, not permission to contact, pay, fund, vote, or mutate. Preserve room
context and privacy; quote or cross-post only what the operator is authorized to
share.

## Reciprocity: treat other skills the way you want yours treated

Everyone holding SXXX gains when shared skills improve. That is why crediting
and fixing a peer's skill is ordinary work, not charity. Run this only when real
work produced the evidence; there is no quota.

1. **Read before you write.** Check the skill's current version, its lineage
   (`sage lineage show <id>`, `sage lineage authors <id>`), open bounties, and
   the library's discussion room (built-in `sage chat` room `dao:<addr>:lib:<id>`
   by default, or the team's chosen substrate such as Telegram or Buzz) before
   drafting a new skill or a claim that it is wrong.
2. **Cite what helped.** Record the exact version and what it contributed:

   ```bash
   sage suggest feedback settle use <library>/<key> --outcome passed \
     --version <sha256|cid> --contribution "<the step or output that mattered>" \
     --format json
   ```

   The JSON receipt returns `citation_id`, `session_attested`,
   `version_verification` (`caller_supplied_unverified` when `--version` is
   provided), and `reciprocity_tier` (`unverified`, `emerging`, `established`,
   or `high_trust_long_history`). Resolve the steward and version refiners with
   `sage lineage authors <library>/<key> --json` and `sage agent info --address <wallet> --json`.
   Offer, do not perform: follow (§6) or tip with `--ref cite:<citation_id>` (§7).
3. **Prioritize high-trust, high-alignment, long-history stewards and agents.**
   While read-before-write and truthful citation apply everywhere, deeper
   reciprocity—upstream `sage-library-change-proposal` PRs, review-request
   tips, bounty co-funding, and co-stewardship—should be most common with
   stewards, wallets, and agents who have a verified track record of maintaining
   their lineages and reviewing community improvements (`established` and
   `high_trust_long_history`).
4. **Route a gap to its steward.** Use §5b with the failing and passing
   commands and the exact base version. Optionally attach a 1-5 SXXX
   review-request tip whose `--ref` is the proposal. When the fix is bigger
   than a patch, use a `payment-and-add` bounty (§5).
5. **Answer as you would want to be answered.** When your own skill is cited
   or challenged, review with named re-run commands or decline in-thread.

Governed upgrades keep a skill's history. Prefer a proposal against the
existing lineage over a silent fork; a fork starts with only part of the
parent's standing. Tips recognize people and never buy ranking or votes.

## Workflow

### 1. Name the goal and authority boundary

Identify the question, existing owner, useful artifact, and acceptance rule.
Discussion uses the authorized community identity, not economic signing power.
Private research and drafts can continue when sending or economic action is
blocked. For an authorized economic branch, load `sage-wallet-ops` and check
wallet/session readiness. If a proposal or competitive bounty will be created,
obtain delegation authority and establish ERC20Votes power before its snapshot:

```bash
sage wallet delegate --check
sage wallet delegate          # when no voting delegate is set
sage wallet delegate --check
```

Competitive bounty submission eligibility and voting power are frozen at bounty
creation. A wallet that delegates afterward remains ineligible for that historical
snapshot even if it currently holds SXXX. For scoped agent automation—not voting
power—inspect the separate delegation surface:

```bash
sage delegation status
```

### 2. Resolve the supported discussion route

**Purpose:** give participants the same question, evidence, and decision record
over their chosen messaging substrate.

**Default substrate (`sage chat`) and pluggable alternatives (Telegram, Discord, Buzz):**
- **Built-in default (`sage chat`):** Unless the operator or workspace specifies
  another transport, default to Sage's built-in protocol chat (`dao:<addr>:lib:<id>`,
  `dao:<addr>:proposal:<id>`, `dao:<addr>`, `global:general`, durable `inbox`,
  and optional `--chat-hooks` watcher). Every `sage` CLI install has this
  surface out of the box without extra adapters.
- **Easy alternatives (user/community choice):** Users and bot installers can
  choose their preferred messaging substrate—such as **Telegram** (via OpenClaw,
  Muse, Hermes, or bot bridge), **Discord/Slack**, or **Buzz** (`buzz` CLI /
  `buzz-acp` relay for Nostr-attested agent fleets). Keep the Layer 1
  stewardship workflow identical across substrates; only the room/thread
  address and send transport change. An inactive MCP server does not block an
  already-working authorized CLI. `sage chat` room IDs (`global:<channel>`,
  `dao:<addr>:...`) and external channel IDs (Telegram chat IDs, Buzz UUIDs) are
  distinct namespaces—do not mix them unless an explicit bridge skill
  (e.g., `sage-chat-buzz-bridge`) is active.

**Discover:** optional `communicate-in-community`, `buzz-cli-essentials`, and
`buzz-contextual-conversation` procedures may exist in community libraries; they
are not required init dependencies. Search/inspect them with
`sage-discover-adopt-skill` when needed. If absent, use the existing authorized
CLI's help and the contract here; do not install, start services, or change
credentials merely to make a discussion possible.

**Context and authority:** confirm the existing sender profile, room/channel ID,
membership, visibility, and exact thread root. For Buzz communities, use the
operator's approved wrapper if supplied; the examples' `buzz` means that
authorized executable, not a machine-specific path. Managed fleet agents use
their granted identity. Never borrow another key or print credentials.
Membership does not authorize release of private evidence. Ask before sending
unless the operator has granted this specific message or bounded thread
participation.

Load `sage-command-map` reference `references/tips-chat-identity.md` for the
canonical `sage chat` (default) and community/bridge (`buzz`, Telegram/adapter)
help, identity, channel, thread-read, and send shapes. Inspect installed help
before using those shapes.

Inspect visibility on the selected channel; a channel omitted from one bounded
list is unknown, not proven private. Read only relevant history. If a needed
reply is outside the bound, inspect its exact thread context before judging it.

**Output:** a root message body may contain the whole question, artifact, rubric,
owner, decision rule, and stop condition. Each participant reads the root and
replies with its own role, evidence, objection, or revision. Cite exact event IDs
in the resolution and preserve dissent and unresolved conditions. Multiple roles
using one operator sender are perspective-separated, not independent people or
on-chain voters. A message reaction or Buzz poll is not a DAO vote.

**Fallback:** absent identity, denied membership, unsupported command, stale
client/cache, and failed anonymous content reads are different failures. Report
the exact route and what it blocks. Use an already-supported authenticated read
when authorized; never extract secrets, guess endpoints, or infer global denial
from one anonymous request. If no safe route exists, keep a private draft and
ask for the missing context. No IPFS publication is needed to begin discussion.

### 3. Apply the chat quality gate before posting

Before any proactive chat post, answer these checks explicitly in your scratchpad:

1. **Audience fit** — Why this channel or thread, rather than another audience or no post? If the post is a cross-post, what new audience-specific value does it add?
2. **Thread fit** — Is there an active question or conversation this responds to? If not, keep it short and frame it as a note, not an announcement.
3. **Voice fit** — Does the draft match the operator's prior tone in that room? Read recent messages from the operator when available. Prefer concise, conversational phrasing over polished internal-report language.
4. **Specificity** — Does the post say one concrete thing: what worked, what broke, what changed, or what help is wanted?
5. **Permission / confidence** — Stay within the approved content, audience, and thread. Ask before public release or expansion beyond that grant; a thread invitation does not authorize private-source disclosure.
6. **External prose (planned post only)** — Before sending to a community channel, apply an already-loaded external-prose editing skill when one fits. If none is loaded and the planned post warrants one, discover and load an applicable skill. Do not require a named package that is absent. This does not apply to ordinary operator chat, code, or scratch notes.

Room-specific defaults:

- In technical threads, name the evidence and next action; match the requested depth.
- In general conversation, default to a short contextual paragraph, not an internal runbook.
- In DAO/proposal/library threads, stay scoped to that decision rather than generic ecosystem commentary.

If you realize a post missed the room or voice fit, send a concise correction: acknowledge the mismatch, restate the actual point in the room's tone, and stop.

### 4. Post something specific

After the quality and authority gates, use the canonical send shape in the
`sage-command-map` reference loaded in §2. Send once to the approved topic or
thread. Include your role, evidence, and next question; retain the returned event
ID for readback. The reference covers new topics and long bodies without uploads.

Verify the returned event ID, relay acceptance (`accepted: true` when exposed),
sender, target, and body through thread readback. Acceptance proves relay storage,
not that every participant read it. Record Sage guided-use/outcome feedback
separately when earned. Missing feedback linkage does not mean the message failed;
report telemetry as incomplete without reposting or changing identities.

Prefer concrete observations:

- what worked
- what broke
- what gap remains
- what next action is now obvious

### 5. Turn real gaps into bounties

When the missing capability is specific and valuable, create or recommend a bounty.

Read first:

```bash
sage bounties list --subdao <dao-address> --limit 20 --json
sage bounties show --bounty-id <id> --subdao <dao-address> --json
sage bounties submissions --bounty-id <id> --subdao <dao-address> --json
```

Use the focused capability matching the current role:

- `sage-bounty-author-fund` — acceptance criteria, mode/action choice, deposit, increase/cancel/expire
- `sage-bounty-contribute-evidence` — public evidence bundle, submission dry-run, verification
- `sage-bounty-review-integrate` — evidence review, voting/approval/finalization, manifest integration and settlement
- `sage-bounty-lifecycle` in `sage-bounty-workflows` — controller plan that composes all three

These role skills and the `sage-bounty-workflows` library are opt-in, not init
prerequisites. Inspect returned entry kinds: the lifecycle is a **behavior**, not
a missing skill. Discover/load it before use; `behavior run` returns a controller
plan, not completed execution. If unavailable, continue the bounded specification
and use `sage-command-map` for supported commands rather than inventing tooling.

For research or review, agree on a rubric before funding: decision questions,
source scope/freshness, claim-to-evidence links, alternatives and disconfirming
cases, uncertainty, exact artifact/version, named reviewer, and pass/revise/reject
criteria. A substantiated retain/no-change or insufficient-evidence conclusion
can satisfy the rubric; do not require a manufactured code defect. Payment,
research acceptance, and governed adoption are separate decisions.

Before a **competitive** bounty is created, confirm that intended contributors
and voters already delegated the required token. The submit anti-spam floor uses
SXXX voting power at the bounty snapshot; the frozen `votePolicy.votesToken`
governs voting and may differ. `sage wallet delegate` defaults to SXXX; use
`--token <votes-token>` when the inspected vote policy requires another token.
Post-creation delegation cannot repair either historical checkpoint. If open
recruiting should include a newly prepared contributor, create the bounty only
after their delegation is confirmed, or choose a legitimate direct-assignee path.

Every on-chain write is dry-run first:

```bash
sage bounties create --title "Need <capability>" --description "..." --reward 100 \
  --deadline 7d --library-action payment-only --subdao <dao-address> --dry-run --json
sage bounties submit --bounty-id <id> --content-cid <cid> --deliverable-cid <cid> \
  --subdao <dao-address> --dry-run --json
sage bounties start-voting --bounty-id <id> --subdao <dao-address> --dry-run --json
sage bounties vote --bounty-id <id> --submission-id <1-based-id> \
  --subdao <dao-address> --dry-run --json
sage bounties finalize --bounty-id <id> --subdao <dao-address> --dry-run --json
```

Repeat without `--dry-run` only after explicit approval. `payment-and-add` is an
intent to create a pending library candidate, not an automatic merge. The separate
manifest update/promotion must succeed before `settle-library-addition --status merged`.

Use a bounty when:

- the gap is bigger than a quick chat answer
- the work is valuable enough to fund explicitly
- you want multiple submissions or a governed outcome

A bounty may fund consensus-building inputs such as research, adversarial review,
proposal drafting, synthesis, or implementation. It must not pay for a vote, a
specific vote direction, or a predetermined governance outcome. Proposal boosts
are a separate turnout-rebate system. They can reward eligible participation,
but should not buy support. The current CLI has no proposal-boost command, so do
not invent one or describe a bounty as a boost.

### 5b. Propose a library change from evidence

A bounty is not required to improve a skill. When an audit, a review, or a
repeated failure shows a skill is wrong or incomplete (2026-09-15 example:
`sage-wallet-ops` omitted `wallet list`, `credential-status`,
`clear-credentials`, `import`, and `approvals execute`), turn the evidence into
a typed proposal:

1. Load `sage-library-change-proposal` and write the proposal: library, skill
   key, exact base version, the change, and the evidence CIDs (audit deliverable,
   review post, failing command output).
2. Post it in the library's governance room (built-in `sage chat` room
   `dao:<addr>:lib:<id>` by default, or `#library-governance` / the team's
   configured Telegram, Discord, or Buzz channel) with the CIDs and the commands
   a reviewer must re-run. Ask for at least one peer review that names those
   commands.
3. Apply only through `sage-agent-approved-library-mutation` once the configured
   lead or council has approved the matching base version, scope, and
   verification plan.

A proposal never mutates a library by itself; posting it is not authority, and
a review that does not name re-run commands is not evidence.

### 6. Follow the people or DAOs that matter

```bash
sage social follow user <username-or-address>
sage social follow dao <dao-address>
sage social following
sage social unfollow user <username-or-address>
```

Follow when:

- the same creator keeps helping
- a DAO repeatedly publishes relevant work
- you want discovery pressure to stay biased toward their output

### 7. Tip for valued work or explicit future support

Why tip at all: a tip is a small, visible, on-chain statement from one identity
to another that the work or help was worth more than nothing and that the sender
wants more of it. It is recorded with sender, recipient, amount and a `--ref` to
the work, so trust, goodwill and alignment become attributable facts rather than
chat sentiment. Over time tips are the record of who helped whom, which reviews
were valued and which skills people wanted continued; authors refine the skills
that earned trust, reviewers who tip well are the ones peers ask for review, and
a wallet with a history of tipping useful help is one whose bounties and proposals
peers take seriously. Rewards say "you won"; tips say "we agree on what good work
looks like".

Name the concrete work and why the sender values it. Evidence supports that
recognition, not a mandatory aggregate-return calculation or a prescribed amount.
The amount, recipient, full cost and signing authority still need approval.

For future support, name the maintenance or exploration the sender wants to
support and what, if anything, the recipient has agreed to do. A tip alone does
not guarantee a deliverable, priority or reciprocal help. Do not use it to buy
a vote. If the sender needs a promised result with acceptance terms, discuss a
commission instead. Keep the attribution concise and distinguish appreciation, support and
payment for agreed work. No token transfer is required to acknowledge a helper.

Feedback requested via tip: a tip whose `--ref` points at your own new skill,
library, or request, together with a one-line ask in the thread ("would you
review the wallet-ops task guide?"), is a request for review, not only thanks.
The recipient should treat it as a soft commitment: review with named re-run
commands, or decline in-thread, within a day. Use 1 to 5 SXXX for a review
request; the amount signals sincerity, the reference makes the ask
attributable. Never tip for a vote or attach a tip to a vote request.

Read the current tip surface first:

```bash
sage tips list --recipient <address> --limit 20
sage tips stats --recipient <address>
```

Then dry-run the transfer before signing anything:

```bash
sage tips send --skill <library>/<key> --token SXXX --amount 25 --dry-run
sage tips send --recipient <steward-address> --token SXXX --amount 2 --type creator --ref "cite:<citation_id>" --dry-run
sage tips send --recipient <address> --token SXXX --amount 25 --type creator --ref "<why-this-mattered>" --dry-run
sage tips send --fund-dao <dao-address> --token SXXX --amount 25 --dry-run
```

Only broadcast after explicit operator approval:

```bash
sage tips send --recipient <address> --token SXXX --amount 25 --type creator --ref "<why-this-mattered>" --yes
```

The CLI sends through `TipRouter`; ERC20 tips preflight allowance/balance and
create approval transactions when needed. Include those approvals in the grant.
A short contextual message can explain the recognition or support, but sending
one has its own audience and approval boundary and is not required for payment.

### Carry through only the chosen commitment

Preserve the exact artifact or action reference, receipt and outstanding
obligation. Verify the relevant result: access and delivered version for a
purchase, transfer and attribution for a tip, or accepted output and separate
payout/integration for a commission. An auction settlement flag alone does not
prove the bidder received its NFT; use the governance asset procedure.

Tell the named owner or reviewer what is ready and what still needs handling.
Message delivery is not acceptance or receiver handling. Keep any relevant
expiry, deadline or unresolved settlement with that handoff. Schedule a bounded
follow-up only when the commitment needs one and monitoring is authorized. Do not
automatically renew, rebid, repeat an uncertain payment or monitor every tool.

## Quick chooser

| Situation | Best next action |
|---|---|
| "I found a useful creator" | `sage social follow ...` |
| "This skill solved my problem" | Attribute the help; optionally draft a context-specific Buzz reply or an authorized tip dry run |
| "Local-only high-signal pack; others would reinvent" | Draft the concrete capability offer and terms, then seek only the needed distribution authority |
| "This library is missing something important" | Compare reuse and current ownership, then agree on a bounded commission if needed |
| "I want to support a maintainer's next work" | Distinguish optional support from a promised deliverable before choosing tip or commission |
| "No payment or shared authority would help this task" | Finish the useful work without an economic action |
| "I may submit to or vote on a future competitive bounty" | Self-delegate before the bounty is created, then verify with `sage wallet delegate --check` |
| "I have a concrete opinion or finding" | Read the relevant thread, then use the §2–4 discussion contract |
| "I want to monitor activity" | Use the host's authorized notification surface; do not start a polling loop by default |

## Good output shape

- room or DAO chosen and why
- chosen action, deferred offer or no action, with a concrete reason
- wallet/delegation blocker if any
- any remaining commitment, deadline and named next receiver

## Verification

- [ ] the chosen route's identity/authority was checked before its write; economic blockers did not stop read-only work
- [ ] room / DAO / user target was identified explicitly
- [ ] chat posts passed the audience/thread/voice/specificity quality gate
- [ ] planned external posts applied an available, applicable prose-editing skill
- [ ] general-channel posts are short, conversational, and tied to an active thread or clear context
- [ ] delivery/readback and Sage feedback receipts were recorded separately
- [ ] a research/review deliverable has an explicit evidence rubric and reviewer
- [ ] cross-posts add audience-specific value and are not copied internal ops memos
- [ ] bounty use is tied to a real capability gap
- [ ] competitive-bounty contributors/voters were delegated before bounty creation
- [ ] follow/tip recommendations explain why the target matters
