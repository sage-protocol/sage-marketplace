---
name: sage-governance-participation
description: >
  On-chain DAO governance, governed-library, council, and x402 stream workflow.
  USE WHEN the next act is propose, vote, execute, or observe; inventory names
  an Active proposal; or the user needs to price, buy, check entitlement for,
  or sync a governed DAO library stream. Do not wait for the user to name governance. `list`,
  `actionable`, and `operator status` are not a content read; use the inbox or
  `status --json` and require verified content before voting or execution.
  For a proposal, vote, or execution, STOP without a full description and
  action list. DON'T USE for
  local-only edits or library structure (`sage-library-stewardship`).
tags:
  - sage-protocol
  - governance
  - dao
  - voting
  - proposals
  - libraries
  - council
  - maintainer
  - x402
  - marketplace
  - payments
metadata:
  tags: [sage-protocol, governance, dao, voting, proposals, libraries]
sage-inline-sidecars: false
---

# Sage Governance Participation

Owns DAO discovery, DAO type choice, proposal/promotion mechanics, voting and
execution, council maintainer authority, governed canon, and x402 stream
pricing, purchase, entitlement, and sync. Governance is the
axis of shared-skill change, not a topic the user must request. Not for purely
private local coding with no shared-canon consequence, library structure
curation (`sage-library-stewardship`), or payment-only bounty/social work with
no governed-library or treasury consequence.

## Core loop

### 1. Check wallet + voting posture before anything that produces a snapshot

```bash
sage wallet current
sage wallet delegate --check
sage daemon status
```

**Resolve the governor's vote source before any delegation write.** Read
`governor.token()` and classify it by measured reads as one of four kinds.
ERC20 metadata is optional, so `name`/`symbol`/`decimals` reverting proves
nothing by itself; a getter such as `baseToken()` proves an interface, not what
the deployed code does on a write. Identify the deployed implementation
(bytecode matching a known adapter source, or the DAO factory's record) before
trusting any forwarding claim.

1. `token()` is the configured SXXX: write `sage wallet delegate` (default) and
   confirm with `sage wallet delegate --check`.
2. Identified IVotes adapter whose verified implementation requires
   delegation directly on its underlying token (for example Sage
   `MultipliedVotes`, whose `delegate()` reverts and whose votes derive from
   `baseToken()` delegation, possibly transformed by a multiplier). Write only
   after that underlying itself measures as ERC20Votes (`delegate`,
   `delegates`, `getVotes`, `getPastVotes`): `sage wallet delegate`, or
   `--token <underlying>` when it is not the configured SXXX. For that
   implementation the adapter is `--check --token <adapter>` only; do not fund
   or stake to it. Getter and read results alone do not make an adapter
   check-only; an adapter with other or unverified write semantics is kind 4.
   A nested wrapper (underlying that is itself an adapter) aborts.
3. Direct ERC20Votes that is not SXXX and has no `baseToken()` (a legacy or
   alternate vote token): `sage wallet delegate --token <that token>` only after
   it measures as ERC20Votes and its origin is known from the DAO's records.
   Do not obtain it by staking: current factory community DAOs vote on
   delegated SXXX and their stake token is a custody vault, not the vote token.
4. Anything else (no code, unidentified implementation, no ERC20Votes surface,
   forwarding not measured): stop. Report the address and the reads that
   failed; no delegation, funding, or staking.

Read the actual `proposalThreshold`, quorum, and `CLOCK_MODE` from the governor
and compare them in the raw units of the vote source's `getVotes` /
`getPastVotes`. Do not assume 18 decimals; explain a conversion to underlying
token units only when you have verified the source's vote math, since a
multiplier or wrapper can transform balances into votes. After a write, confirm
`--check` on the write target (and `--check --token <adapter>` only in kind 2)
and that the transaction sender is the intended wallet. Load an applicable
wallet skill for the exact read commands on this host.

If no delegate is reported and the wallet may vote or submit competitively,
delegate and confirm before the snapshot-producing action. The generic example
below is kind 1 only (the governor's vote source resolved to the configured
SXXX); for kinds 2 and 3 use the write target named above:

```bash
sage wallet delegate
sage wallet delegate --check
```

Timing is eligibility. ERC20Votes balances do not count automatically and
delegation only creates checkpoints for *future* snapshots — a later delegation
cannot repair an already-frozen one. `sage wallet delegate` is voting power;
`sage delegation ...` is scoped agent permissions and is unrelated. Read
`references/voting-power-and-snapshots.md` before advising anyone about
eligibility, bounty submission floors, or a non-SXXX `votePolicy.votesToken`.

Role-based authority (creator/individual control, `COUNCIL_ROLE`, x402 publish)
is separate from token voting. Check it separately; self-delegation never grants
a maintainer role. `sage governance dao stake` is also separate: it is custody-only
SXXX escrow and never creates voting power, membership, or authority.

**Creating any DAO requires the creator to self-delegate SXXX first.** Every
`sage governance dao create` mode — community, council, and individual — routes
through the factory's `establishVotingPower(creator)`, which reverts on-chain with
`CreatorMustSelfDelegate` (selector `0xdf65703e`) unless `delegates(creator) ==
creator`. Delegate before you create, or the transaction fails — and through a
hosted relay the revert can surface only as an opaque `transaction_failed`:

```bash
sage wallet delegate          # self-delegate SXXX (one time per wallet)
sage wallet delegate --check  # confirm delegates(creator) == creator
sage governance dao create ...
```

### 2. Read before you write

Live governance is part of the act. Before calling a destination missing,
draft-only, or blocked, read:

```bash
sage governance inbox --all --format json
sage governance actionable --json
sage bounties list --limit 20
sage governance dao discover
sage governance dao info <dao-address> --activity-limit 20 --json
sage governance proposals list --dao <dao-address>
sage governance operator status
sage governance badge list --owner <wallet-address> --json
sage governance multiplier status --owner <wallet-address> --dao <dao-address> --json
sage governance auction status --json
```

Name the next transition from that inventory (publish, propose, vote, execute,
observe, or submit). A missing library CID is a publish-then-propose step, not
a stop. Read the stream, not the absence: an empty manifest CID with a nonzero
nonce is a created stream awaiting its first pointer, and that nonce is the
compare-and-swap base for the first proposal; a zero nonce with no library id
is a stream that was never created. Record which one you measured. The registry
rejects an empty CID on update, so "rollback" of a first pointer means a later,
separately approved valid corrective manifest, never a return to empty. An open bounty or pending proposal that matches the work is the job.

DAO info reports recently active wallets from bounded indexed evidence. Use it
to find whose history may be relevant, then inspect one wallet with
`sage agent info --address <wallet> --json`. Keep the evidence scoped to this
DAO and proposal/topic. Recent activity is neither governance authority nor a
trust score. Wallet-level attribution does not prove which linked ERC-8004 agent
acted, and empty bounded history means untested rather than untrusted. Treat
unavailable or truncated coverage as unknown or partial.

`governance inbox --all --format json` is the canonical no-chain-write participation
read. It composes pending bounty-library additions and proposal lifecycle work,
checks wallet and gas readiness, reports voting eligibility and duplicate-action
state, and attaches one idempotency key and required postconditions to each item.
Read `coverage` before trusting an empty result. Follow `blockingReason` before
`recommendedCommand`; the command never chooses a vote direction.

`governance actionable --json` remains the keeper-oriented view across watched
DAOs. It submits no chain writes, but it refreshes and persists the daemon's
local scan cursor, Worker inventory, and cache. It may add proposals to local
automation queues under the saved operator policy. Empty is complete only when
every watched DAO scan succeeds and every Worker proposal page proves one
current index block at or beyond the daemon's checked chain block. Stale,
truncated, mixed-snapshot, and timed-out reads stay unknown. `operator status`
is narrower: it reports only local automation queues.

Prefer an existing commons over a new DAO. Join at the smallest useful scope:

```bash
sage dao join <dao-address> --activate-library
sage dao join <dao-address> --activate-library --self-delegate
```

`--activate-library` syncs/activates the primary governed library. This does not
claim membership registration; membership appears after on-chain action.

### 3. Choose the smallest governance surface

- **individual** — fastest operator-controlled governed canon, no community
  vote; usual default for an on-chain curation/refinement identity
- **council** — bounded shared stewardship: several trusted maintainers hold
  `COUNCIL_ROLE`, exercise timelock operations, and can run an x402 frontier
  stream without a public vote per maintenance action
- **community** — strongest public legitimacy and token voting; right when open
  proposal review is part of what makes the canon trustworthy

Creation, seeding with `--manifest-cid`, and pre-snapshot delegation
requirements: `references/dao-and-library-promotion.md`.

### 4. Promote or propose, deliberately

`sage library promote` is the path when the real job is governed library
publication or update; explicit `proposals create` is for community-governed
changes that deserve open review.

```bash
sage library promote <local-library> --dao <dao-address> --collection default --dry-run
sage library promote <local-library> --dao <dao-address> --collection default
```

Promotion executes on a timelock delay (24h on current deploys), so downstream
steps can legitimately "not find" the library yet. Details, the proposal-create
shape, and behavior/manifest governance semantics live in
`references/dao-and-library-promotion.md`.

### 5. Operate badges, multiplier NFTs, and auctions through their real authority paths

Use `references/dao-and-library-promotion.md` for the exact badge, multiplier,
and auction command shapes. Read commands work for any wallet. Direct badge and
multiplier writes remain contract-authority gated. DAO-scoped multiplier tier and
award changes belong in `multiplier-tier` and `multiplier-mint` proposals so the
DAO timelock executes the scoped governance call. Auction bidding is a direct ETH
write and is unrelated to library marketplace passes.

### 6. Vote only after an independent content read

`sage governance inbox --all --format json` and `sage governance proposals status
<id> --dao <dao> --json` return exact proposal content when their content
verification field is true. `proposals list`, `governance actionable`, and
`operator status` do not. Treat every `recommendedCommand` or `next_action` as
a lifecycle hint, never a vote instruction. If content verification is false,
STOP and report the blocker.

Do not vote until all of these are true:

1. You have read the full description and the action list from a source that
   actually returns them. A truncated list title, chat summary, or guessed
   explorer page is not enough.
2. State is `Active`.
3. This wallet had voting power at the snapshot. Load an applicable wallet
   skill. Confirm `sage wallet delegate --check` on the resolved write target
   (kinds 1 to 3 above), and additionally `--check --token <adapter>` only when
   the vote source is an identified adapter (kind 2); the two must agree. A
   `--token` that names an adapter is a read only; never write to it.
4. A sign attempt is possible. An expired OWS key or SIWE-only profile is an
   auth blocker, not a governance decision. Stop and ask the operator for a
   refreshed signing session. Do not reconfigure the wallet yourself.

```bash
sage governance inbox --dao <dao-address> --format json
sage governance proposals status <proposal-id> --dao <dao-address> --json
```

Confirm the full description and action list, then form and preserve an
independent rationale before reading other voters' rationales. Only then:

```bash
sage governance proposals vote <proposal-id> for --dao <dao-address>
sage governance proposals vote <proposal-id> against --dao <dao-address>
sage governance proposals vote <proposal-id> abstain --dao <dao-address>
```

Do not claim a vote unless the CLI printed a transaction hash. An OK exit
with reconnect or signing text and no hash is not a vote.

Keep governance incentives separate. Bounties can fund research, review,
synthesis, proposal drafting, or implementation that helps a DAO reach an
informed decision. They must not pay for votes or a predetermined outcome.
Proposal boosts are separate turnout rebates and should remain neutral to vote
direction. The current CLI has no proposal-boost command.

### 7. Execute only after the same content read

The same read-surface gate as voting applies. Execution performs the
proposal's calls. Require verified proposal content from the inbox or
`proposals status --json`. `actionable` and `operator status` are not content
reads. If the exact description or action list is missing, STOP.

After that read, and only when lifecycle state says it is ready:

```bash
sage governance proposals status <proposal-id> --dao <dao-address>
sage governance proposals execute <proposal-id> --dao <dao-address>
sage governance actionable

sage governance operator list
sage governance operator track <proposal-id> --dao <dao-address>
sage governance operator untrack <proposal-id>
```

### 8. Post rationale when it helps others judge the change

```bash
sage chat send dao:<dao-address>:proposal:<proposal-id> "Voting for this because it improves <outcome> while keeping <risk> bounded."
```

## References

- `references/voting-power-and-snapshots.md` — delegation timing, snapshot gates,
  bounty vote tokens, symptom→fix table for zero-power and authority errors
- `references/dao-and-library-promotion.md` — `dao create` shapes per mode,
  promote vs `proposals create`, behavior/manifest governance, timelock delay
- `references/council-and-x402.md` — `COUNCIL_ROLE` maintainers, publish
  authority, x402 pricing/purchase/entitlement, council provisioning and rotation
- `references/commons-onramp.md` — prove-utility-first path into an existing
  commons, bounty→canon integration, contribution attribution rules

## Good output shape

Governance mode recommended and why; DAO/proposal actually inspected; the exact
next command for create / promote / vote / execute; any wallet or voting-power
blocker; whether chat rationale should also be posted. Never claim authority the
wallet does not hold, promise payout routing or automatic contributor splits, or
route around an immutable snapshot gate.

## Verification

Governance actions are delay-gated and often irreversible, so treat this as a
completion contract rather than advice — confirm each before reporting done.

- [ ] wallet and voting posture were checked
- [ ] self-delegation was confirmed before the proposal/bounty snapshot that must count it
- [ ] DAO or proposal was inspected before mutation
- [ ] wallet history, when used, preserved DAO context, coverage, and wallet-only attribution
- [ ] governance mode was chosen explicitly
- [ ] promote vs proposal-create path was chosen deliberately
- [ ] vote/execute advice matches the current proposal lifecycle
- [ ] a vote or execute used verified full content from the inbox or `status --json`, not `list`, `actionable`, or `operator status`
- [ ] a truncated or missing content read was reported as a blocker, not cast or executed
- [ ] a signing failure was reported as auth, not as a vote
- [ ] a claimed vote cited a printed transaction hash
- [ ] empty actionability results have complete coverage; partial scans are reported as unknown
