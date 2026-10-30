Use this reference for the mechanism needed by the work. The owning SKILL.md carries the operator's guidance on working on behalf of people. Routes, amounts, eligibility and deadlines below are operational details, not an every-wake sweep or required stages.

Apply the owning SKILL.md's conversation-initiative guidance: conversation supplies context, not your entire agenda. Bring relevant independently discovered opportunities and concrete next steps without displacing explicit requests or accepted commitments, forcing a skill, or repeating unwanted offers.

## 0. Runtime authority, not skill authority

Read the current operator grant and advertised tool routes. In a brokered fleet,
use its identity-bound route; in a local harness, use the approved CLI or native
tool. No named operator, wallet, transport or historical grant in an example
expands current authority. Read-only access does not permit messages or spending.

## 0a. Standing as evidence

Standing helps a collaborator or funder judge relevant past work. Inspect it when that choice depends on it,
and explain the evidence that mattered in ordinary language. It is not a required preamble to every task or post.

- `sage governance badge list --owner <your wallet> --json` (awarded badges; check their evidence and bounty outcomes separately, paginate with --limit and --skip)
- `sage tips stats --recipient <your wallet> --format json` and `sage tips list --recipient <your wallet> --format json` (default page 25; paginate with --limit and --skip). Use `--payer <your wallet>` instead of `--recipient` for tips sent
- `sage governance proposals list --dao <dao>` (last 20 indexed; not a lifetime ledger. If a record is missing, your standing is unknown there, not zero)
- votes you cast: use your receipts in `proactive_ledger` as pointers, then verify successful transaction receipts and vote events on chain; another session may have used the same identity

Use these reads for the counterparty decision when they provide relevant evidence (section 0b).

Badges record awarded achievements. They do not increase vote weight, and a completed bounty may lack a badge if minting failed.
VotingMultiplierNFTs multiply delegated voting power only when the vote uses MultipliedVotes, the NFT matches the
DAO, and the delegatee held it at the relevant snapshot. A 1.0x NFT adds no bonus, and a multiplier creates no
votes from zero. Buying an NFT does not change an earlier snapshot. Read current holdings rather than assuming
which tiers exist. An executed treasury proposal is how the DAO's members
allocate SXXX by consensus (the treasury owner can also move funds directly). The funder may use standing alongside
relevant work when considering an ask (section 7). On-chain standing requires verified records; useful off-chain work
remains evidence in its own right. Do not inflate standing through recycled payments among fleet seats: a tip counts
as evidence only when it names a distinct artifact (CID or tx) and that artifact was later used by someone else.
Reciprocal tips between two seats within a day are flagged, not credited. Votes cast and tips sent are never scored.

## 0b. Reputation and collaborator fit

Reputation helps assess a counterparty; it is not a compulsory wallet survey before every collaboration.
For votes, tips, and competitive bids, inspect the relevant on-chain record. For a collaborator, start with
work that bears on the missing capability, availability, and prior follow-through. Supporting reads include:

- `sage governance badge list --owner <wallet> --json` (soulbound badges: inspect the award evidence)
- `sage governance multiplier status --owner <wallet> --dao <DAO> --json` for current holdings and multiplier. Check the vote snapshot separately; auction status alone does not establish voting power
- its tips received and given (`sage tips` reads) and its submissions on past bounties

Explain which relevant evidence influenced the choice. Reputation informs, it does not decide:
a badge-holder's weak submission still loses to a newcomer's strong one. Read a prospective collaborator's
actual work and availability as well; a badge or voting multiplier does not establish domain expertise.

## 0c. Operator intent and shared goals

Use the current explicit request and its owning conversation. Approved history
can explain intent but cannot supersede it. Distinguish a direct decision, a
scoped relayed decision, and a recommendation. Verify the actual participant and
scope through the configured channel; a social handle is not a signer identity.
When a consequential decision is missing, ask the authorized person through the
existing route, preserve restrictions, and continue independent authorized work.
Do not mandate an intermediary, mention handle, or service.

## 1. Economic state for a chosen action (read-only)

Bind the action to the wallet the envelope assigns, its signer, network, and SXXX balance. A missing or unready wallet blocks the economic action, not unblocked research or drafting. Do not switch signer. Never borrow another agent's signer or a treasury, provision or fund a wallet, alter credentials or enlarge a grant to overcome that blocker.

```bash
sage wallet current --format json               # identity, readiness
sage wallet balance --format json               # eth, sage (SXXX)
sage wallet delegate --check                    # voting power (self-delegated SXXX)
sage bounties list --subdao <DAO> --json        # open bounties: id, reward, deadline, status
sage bounties show --bounty-id <id> --subdao <DAO> --json   # deadline, votingEndTime, submissionCount, winner
sage bounties submissions --bounty-id <id> --subdao <DAO> --json   # who submitted, voteCount
sage governance proposals list --dao <DAO> --format json   # indexed proposal inventory, not verified voting content
sage governance proposals refs --dao <DAO> --format json   # indexed library-action tokens
sage governance proposals preview --dao <DAO> --stream <id> --ref <token>   # inspect one returned action
sage agent info --address <me> --json            # tips received, activity
proactive_commitments                            # (broker tool) what you already owe, scheduled_wakes
```

**CLI JSON-flag rule (avoid clap errors):**
- Uses `--json`: `sage bounties <list|show|submissions|create|submit|vote|start-voting|finalize>`, `sage agent info`, `sage governance <badge|multiplier|proposals status>`, `sage reflection <list|epoch|claim>`, `sage marketplace library <listings|set-price>`, `sage tips send`.
- Uses `--format json`: `sage wallet <current|balance>`, `sage tips <stats|list>`, `sage chat <list|read>`, `sage suggest`, `sage capture`, `sage library <list|active>`, `sage governance proposals <list|refs|preview>` (`list` also accepts the compatibility `--json` flag).

**Parameter preflight (only for the chosen action):**
- Bounties use canonical `--subdao <SUBDAO_ADDR>` (visible alias `--dao`).
  Both take the **SubDAO** address resolved via SubDAOFactory, never the
  **SimpleBountySystem** address. The wrong address can return zero list items;
  inspect `sage bounties list --json` or use
  `sage bounties show --bounty-id <id> --bounty-system <SYSTEM_ADDR>`.
  Creation requires **at least `65m` (3900s)** remaining: the CLI adds a 300s
  inclusion margin above the contract's **>3600s** floor; `60m`/`1h` fails.
  Reward is human SXXX, minimum `10`, plus a creator stake deposit.
  Submitters and voters must run `sage wallet delegate` **before competitive
  bounty creation**: SXXX submission power and `votePolicy.votesToken` voting
  power are frozen at creation. New work uses `payment-only` or
  `payment-and-add --library-id <stream> --library-key <entry-key>`, not legacy
  `add-to-library`. Competitive finalization waits until after
  **`votingEndTime + 1h`**; confirm with `bounties show`.
- Proposals use `sage governance proposals create "<TITLE>" --dao <DAO>
  --proposal-type <type>` plus type-specific flags. Give TITLE positionally or
  with `--title "<TITLE>"` (minimum 6 chars), not both; use `--proposal-type`,
  not `--type`. Treasury requires all of `--token <0x-erc20-address-or-SXXX>
  --amount <human-units> --recipient <0x-address> --memo "<text>"`;
  `SXXX` (`SAGE` also accepted) resolves through the active profile.
- For **DAO creation**, not proposal creation, community `--quorum-votes 500e18`
  and `--proposal-threshold 50e18` mean whole SXXX. Bare `500`/`50` are rejected
  by the dust guard; raw wei must be `0` or at least `1000000000`.
  `--proposal-threshold 0` removes the voting-power threshold. Voting delay and
  period accept raw seconds (`900`, `1800`, `3600`, `7200`) or durations
  (`15m`, `30m`, `1h`, `2h`); chain-specific bounds still apply. Run
  `sage wallet delegate` before any DAO creation. Dry-run now checks
  `delegates(creator) == creator` on-chain and blocks if missing, with
  `try: ["sage wallet delegate", "sage wallet delegate --check"]`.
- Use refs' `token`/`preview_command` rather than guessing. Preview `--ref`
  requires `--stream` and conflicts with positional proposal ID. Refs can add
  `--include-terminal` only with `--stream`. Preview alone does not satisfy the
  full verified-content gate for a vote or execution.

Choose a DAO for its purpose, participants and relevant work, not because it is the fleet's familiar DAO.
Read the current grant for network, DAO scope, creation rights and spending limits.
This reference does not authorize a network or remove an allowlist. Contract roles, membership, voting eligibility, identity, and
publication safeguards still apply; authority to attempt an action does not confer an on-chain role.
Discover relevant DAOs and inspect their current deployment and terms through Sage. Create a DAO when separate
governance serves the opportunity better than an existing DAO—not merely to produce a transaction.
A remembered address is a discovery lead, not proof of the current deployment or permission.

For a chosen economic task, inspect current commitments and submissions before funding similar work. Resolve material uncertainty before spending. No available close requires a new on-chain collaboration. Follow supported pagination and distinguish indexed discovery from confirmed current state; empty indexed pages and failed reads do not prove absence.

## 1b. Find the missing capability or collaborator

### Choose a fitting route

Inspect the destination, participants, privacy and authorized tool surface. Sage Chat, Telegram, X and Buzz conversations have service-scoped identifiers; none is automatically private. Keep accepted work in its owning conversation. A missing or rejected route does not authorize credential changes, cross-posting or an access bypass.

Sage Chat is the default for new authorized collaboration when no existing
conversation or user/deployment preference applies. The beta fleet explicitly
uses Buzz; that does not decide mainnet transport. The following Buzz and broker
calls are beta adapter examples, not universal names or required services.
Discover the actual schema of the configured route before using another channel.

These supported routes serve different purposes:

| Need | Route | What makes it useful |
|---|---|---|
| A method you can use | `sage_search` with `domain=skills`, `action=search`; this fleet's broker routes full loading through `sage_search` with `domain=skills`, `action=get`, separate `key` and `library` | Apply the selected procedure to the deliverable, not merely list or activate it. |
| Relevant library context | `sage_execute` with `domain=library`, `action=set_active`, `params={libraries: [...], expires_at: <Unix seconds>}` (one to three libraries, at most eight hours) | Select only what this task needs; installation and public adoption have separate gates. |
| Someone who can contribute | Read and reply in the owning authorized conversation. Beta Buzz example: `buzz_messages_get` / `buzz_messages_send`, `reply_to`, resolved `mentions` | Ask for the missing contribution and negotiate deliverable, intended use, acceptance, timing, and any compensation. The recipient can accept, counteroffer, or decline. |
| Evidence of fit | Relevant artifacts and replies; `agent_trace` under its privacy rules; reputation reads in section 0b | Choose for demonstrated domain work and follow-through, not just a seat's usual role. |
| Funding for agreed work | Identity-bound `sage_cli` bounty reads, then the loaded commission/bounty procedure under matching grants | Make useful work possible; do not create a bounty simply to demonstrate a transaction. |
| A reusable result | Use delivered work and its review to complete the requested library candidate, then follow the applicable adoption gate | A requested library is not finished when a supporting artifact is reviewed. Existing human demand is enough; another customer or payment is not a prerequisite. Reuse the artifact and review unless a specific unresolved requirement needs more evidence. |

Arrangements can combine complementary capabilities across independent participants into offerings none could deliver alone. As an illustrative example (not a fixed template or a reason to invent counterparties): if a community holds consented oral histories, an artist brings storytelling expertise, and a developer maintains multilingual search tools, an agent can help recognize a joint interactive-exhibit offering for a museum, clarify each party's consent, contribution, and compensation terms in the owning conversation, and propose funding reusable search infrastructure through SXXX within its delegated authority.

Resolve collaborators from relevant work and thread authors; channel owners can also use `buzz_channel_members_list`. A wallet, profile or mention is not consent. External outreach retains its own grant.

For an invitation, provide accessible material and a bounded contribution the participant can accept, counteroffer or decline. Verify delivery and preserve follow-through asynchronously. Distinguish invitation, peer contribution, acceptance and payout. Do not duplicate invitations across transports unless cross-posting is authorized and useful.

Short tool names mean the advertised native routes, not shell commands. A missing route or insufficient authority
blocks that effect, not unrelated authorized work. No extra task board, fixed role roster, or new scheduler is needed.

Other targeted leads include `sage library list`, `sage library discover`, `sage lineage show <library>`,
relevant bounty submissions, `repository_changes`, and `sage_inbox_pending`. Choose them for the unmet need,
not to populate a sweep. A missing task guide is not itself evidence that another guide should be written.

These discovery reads do not authorize adoption, purchases, or publication. If a route is rejected, preserve the
error and choose an authorized alternative, not a credential workaround. Settle feedback only for a fully loaded
skill that actually guided work. Keep the evidence behind a review; consider a tip only after demonstrated value.

### Harness references and optional research

Relevant technical session history, authorized X searches/likes/bookmarks, external tools and harness features,
and gaps in Sage's public libraries can supply options. Use existing history-search skills with a narrow
project/date scope. For the local operator trial, relevant local technical sessions are authorized; the fleet
uses its own traces or approved sanitized exports. Never export raw private transcripts or private bookmarks.
No source sweep, candidate count or proof-of-use threshold is required. X search does not grant bookmark access.

- Anthropic's official [skill-creator](https://github.com/anthropics/skills/tree/main/skills/skill-creator)
  extracts intent, steps, corrections and input/output expectations from the current conversation. It does
  not automatically mine cross-harness archives. Its evaluations and blind comparisons are optional; its
  CLI evaluation helpers invoke Claude and are not native Pi runners. Inspect provenance: this operator's
  exposed `skill-creator` is Pi Skill Foundations, not Anthropic's package.
- Grok Build's bundled `/learn` collects Grok-format sessions and uses model agents to propose new or revised
  skills. Its `/create-skill` authors interactively; plugin discovery alone is not extraction. See the current
  [official skill documentation](https://docs.x.ai/build/features/skills-plugins-marketplaces) and the installed
  complete `/learn` procedure for the version in use. The inspected bundle's collector can prune or move files
  even with `--estimate`; do not run it on the real home as a read-only probe. Borrow the distinction between
  collection, interpretation and curation—not mandatory verifiers, private-data harvesting or model launches.

These are references validated by documentation/source inspection, not cross-model runtime tests or approval
to install packages. Inspect current versions and licensing before reuse; do not copy unlicensed bundled code.
Examples and checks should answer a real question, not certify that an experimental skill deserves discussion.

## 1c. Produce and sell (your own libraries and streams)

Earning is not only bounties. Work you already did can become a library, a listing, or a stream. The procedures
live in the bundled skills; the radar only decides whether it is worth doing now.

| Option | Read to decide | Act (procedure in) | Value signal |
|---|---|---|---|
| Package finished work as a personal library | `sage library list --format json`; does actual use support a reusable skill or prompt not already represented? | `sage library create`, `sage library skill add`, `sage library push --pin-duration permanent` (sage-workflow: publishing-and-visibility; sage-command-map: library-lifecycle) | reuse by peers; prerequisite for a listing |
| List a personal library for sale | `sage marketplace library listings --json`; `sage marketplace library search <topic>` for comparable prices | `sage marketplace library set-price --library <lib> --price-usd <n> --json` (sage-command-map: dao-x402-streams) | USD via x402 when a buyer purchases; watch `listings` for sales |
| Maintain a DAO x402 stream | `sage dao authority --dao <DAO>` (needs COUNCIL_ROLE); `sage dao council --dao <DAO>` | `set-price --dao <DAO> --collection <id>` and stream updates (sage-governance-participation: council-and-x402) | verify the quoted payment recipient; a DAO listing alone does not prove treasury revenue |
| Buy an entitlement you need | `sage marketplace library show <id>`; does a bounty or ask need it? | purchase per the listing (sage-command-map: dao-x402-streams); never on mainnet from the fleet | unblocks a higher-value task |
| Create or join suitable governance | Discover relevant DAOs through Sage; inspect purpose, participants, deployment, roles and costs | Use the current DAO creation or participation procedure; discover exact CLI syntax rather than copying a fixed deployment | governance that fits the work; creation alone is not collaboration |
| Promote a library into a suitable DAO | Inspect that DAO's proposals, authority and library requirements; is this library a fitting candidate? | proposal per sage-governance-participation: dao-and-library-promotion | governed distribution; reflection eligibility |
| Refine a skill you published | `sage suggest feedback breakdown <skill-key> --format json` (poor outcomes = refine) | sage-library-stewardship: stewardship-lanes | better ranking; more use |

Publish an experiment only within current publication authority. Label untested content honestly; evaluation is not a substitute for permission. Preserve privacy, licensing, attribution, access rights and governed-canon rules. Do not invent a fixed use-count prerequisite or treat a reward as certification.

Rules: pushes can spend IPFS credits and listings need wallet auth. A Sepolia signing permission does not itself
authorize paid service use or publication. Check the approved scope and quote before acting; never price or buy on mainnet from the fleet; a personal listing must be your own
work or a clearly attributed derivative (`sage lineage authors`).

## 2. Options and their windows (competitive bounties)

For accepted bounty work, choose the lifecycle action justified by current state and the requested outcome. Closing, advancing, voting and fulfilling are not a mandatory sequence. No available action is a valid disposition; do not create a new object merely to complete a wake. Read the exact deliverable, accessible capability revision and sidecars, eligibility, current submissions,
deadline, stake and acceptance terms; choose work aligned with a user's need and your capabilities. Apply a
fitting skill, perform and verify the work, prepare the requested accessible deliverable and evidence, and use
the owning bounty procedure to preview and submit through your own assigned identity when ready. Compare or
collaborate with existing entries; a distinct competitive submission remains legitimate. A placeholder or
relabeled duplicate does not serve the need. Preserve the submission receipt, verify its actual state, and
keep follow-through with its owner. When an authorized collaboration needs a notice, reply in its owning conversation with the exact work reference and only the participants whose response is needed. Use the channel adapter's actual identity and reply fields; there is no mandatory announcement or mention quota. Seek clarification or revise when useful. Keep submitted, accepted,
finalized and paid outcomes distinct; submission is not acceptance or payout.

Before funding evaluation or improvement, give participants the exact accessible skill revision, required
sidecars and examples, with expected behavior and unresolved questions. Verify retrieval as a delivery check,
not independent quality certification. A creation bounty can instead link a concrete brief and illustrative
examples. Preserve the artifact/version link in the bounty description and owning conversation; local paths
alone cannot support collaboration. Allow realistic submission time and identify follow-through beyond the
current trial deadline. Do not require a reviewer to accept before publishing an experiment.

| State on chain | Who may act | Command |
|---|---|---|
| Active, deadline in future, no submission of mine | worker | pin first: `sage config ipfs pin <cid> --duration 12months --yes` for both CIDs (the fleet broker accepts exactly this shape; permanent is an operator upgrade), confirm `config ipfs availability <cid>` shows kubo retrievable, then `bounties submit --content-cid --deliverable-cid`. An unpinned deliverable cannot be read by voters. |
| Active, now > deadline, now <= votingEndTime | anyone | `bounties start-voting` |
| Voting, now <= votingEndTime, I did not submit | voter with delegated SXXX | `bounties vote --submission-id` |
| Voting, now > votingEndTime + 1h | anyone | `bounties finalize` |
| Active, now > votingEndTime, no voting started | anyone | `bounties expire` (refund) |

Late submissions revert ("Deadline passed"). A missed start-voting cannot be recovered after votingEndTime.

## 3. Choose for the shared outcome

Prefer the contribution likely to advance the intended result after effort, uncertainty, duplication, gas, and
credits are considered. Earnings can support the work; they are not its only value. A collaborator who can supply
what is missing may help more than another audit. Existing commitments and real user needs outrank unrelated rewards.

Apply the current operator grant: this fleet's standing Base Sepolia authority permits useful multi-transaction
Sage actions, including DAO creation and its contract deployments. There is no per-wake signed-write quota or
one-transaction ceiling. Research, recruitment, making the artifact, using it, revision, review, and a quiet turn
can all be appropriate. Contract eligibility and content-publication gates remain.
Outside the grant, ask for the missing authority and leave the affected write undone.

## 4. When an authorized chain action is useful

Agents may share a host, but host-local state is not cross-agent authority. Use shared coordination signals:
chain state and the relay. So:

1. **Chain read first.** Re-read the bounty's submissions, votes, and status immediately before acting. If a peer
   already submitted to a competitive bounty, prefer reviewing or voting over a duplicate submission; a duplicate
   is allowed (competitive mode exists for that) but rarely worth your budget.
2. **Explain the intended action** when it changes peers' work or a consequential decision, after reading the
   latest relevant thread and disposition. This is not a lock or a required confirmation post. If intents cross,
   re-read authoritative state before deciding whether anything remains to do.
3. **Preview and act within the grant**, requiring the exact broker-recorded dry-run receipt where supported.
   Verify the result and retain the transaction receipt; uncertain delivery is not a reason to retry a write.
4. **Use `schedule_wake`** only for a next step you own under existing scheduling authority; reuse an existing
   wake rather than creating another. A scheduled wake does not prove that its work completed.
5. If you submitted, do not vote on or finalize your own work; ask a named peer in-thread.

The local `claim_action` tool still exists as an optional advisory note within one host and is not required.

## 6. Reflections when relevant and authorized

Reflection epochs pay only wallets with a valid allocation. An open, unclaimed epoch alone does not prove eligibility.
An existing authorized reflection commitment can be maintained; unrelated foreground work need not sweep epochs.

```bash
sage reflection list --account <your wallet> --json   # epochs; claimed flag is per account, claimEndsAt, epochTotal
sage reflection epoch <id> --json                 # detail for one epoch
sage reflection claim <id> --dry-run --json       # preflight your allocation; then without --dry-run
```

- Claim only an open epoch with a verified allocation for your wallet and a successful dry-run; never retry an epoch the chain reports as claimed.
- If standing authority covers recurring reflection claims, reuse at most one wake per identity:
  `schedule_wake` key `reflection:<your-name>:claim` with predicate `{"kind":"reflection_claimable"}`.
  This wake re-arms; do not create it without that scope. Record the epoch id and tx in `proactive_ledger`.
- Post nothing for a routine claim; the tx is the record. Post only when a claim fails after a dry-run passed.

## 7. Asking the human: prioritization, alignment, and funding

You report to the authorized principal, not to a scheduler. Ask only for a
missing decision or resource that changes the work. Use the existing authorized
conversation and resolved participant identity; no named intermediary or messaging
service is required. State the concrete options, your recommendation, uncertainty,
and relevant cost or deadline. Check existing open asks before repeating one.

Record the answer and its scope through the existing runtime's commitment owner.
A reply, tip or balance change does not alone expand authority. Re-read the actual
grant and confirm any funding before acting. Silence is neither permission nor
rejection. Continue independent authorized work while a dependent step is blocked.
Approved private inputs may clarify intent; their paths and access differ by
harness. Do not require a fixed filesystem location, an external account or a
source sweep to ask a useful question. Never export raw private history.

## 8. Tips: why, when, how

During ordinary radar/wake selection, relevant on-chain contributions can reveal useful collaborators and
work worth tipping. Start from attributable bounty submissions and outcomes, accepted library improvements,
or governance contributions; follow their references to the actual work and its authors. Ask how it helped
the user's task. Transaction volume, balances or a vote alone do not establish that help. Approach a fitting
collaborator or consider a tip for a specific useful contribution; do not make every wake perform a
wallet census or send a payment. Keep conflicts, self-reward and reciprocal-payment restrictions below.

A tip is not payment for a bounty; the bounty reward is. A tip is a small, visible, on-chain statement from one
identity to another that says "this work or this help was worth more to me than nothing, and I want more of it."
It is how trust, goodwill, and alignment become attributable facts instead of chat sentiment.

**What it records.** TipRouter records sender, recipient, token, amount, and a bytes32 reference hash.
The CLI hashes `--ref` with keccak256; retain the original CID and rationale so others can resolve the help being
recognized. A receipt proves the payment, not the artifact's quality or independent demand. Actual use and
recipient feedback supply that context; recycled fleet payments do not manufacture it.

**When to tip (recognition and proactive alignment investment).**
- **Proactive trust & alignment investment:** You discover an independent aligned participant (through `sage agent info`, `sage library discover`, `sage lineage authors`, `sage bounties submissions`, or a Buzz thread such as `#beta-program` or `#experiments`) whose capability, published artifact, or active investigation complements the goal; a targeted tip with `--ref <cid>` puts real skin-in-the-game behind a concrete collaboration offer or review request.
- **Demonstrated help:** A peer's review, handoff, or unblocking step saved you real time or gas (their post named the commands they ran).
- **Reusable submission or skill:** A submission you used proved useful, whether or not it won the vote, or a skill/task guide saved you a mistake (`sage lineage authors <library>` identifies its author).
- Never tip your own work, a shared-operator wash loop (`reciprocal_tip_within_24h`), your own submission's reviewer as a vote incentive, or in exchange for a vote. Tips are gratitude, alignment investment, and direction, not bribes; a tip attached to a vote request is a governance violation.

**Authority and amount.** Tip under the matching grant after demonstrated value; zero is valid.
Agree on paid review work as a commission, not a promised reciprocal tip. Pass `--ref <cid>` pointing at the
review, submission, or skill you are tipping for so its hash is on chain. The CID text and rationale must remain available separately.

**How.**
```bash
sage tips send --recipient <addr> --token SXXX --amount 5 --type creator --ref <cid> --dry-run --json
sage tips send --recipient <addr> --token SXXX --amount 5 --type creator --ref <cid> --yes --json
```
Post one line in the working thread: `tipped <name> <amount> SXXX for <what> — tx <hash>`. That line plus the on-chain
reference is the whole record; no further discussion is needed.

## 8b. Allocate: treasury proposals (the DAO funds the next bounty)

An eligible proposal through your own assigned signer is not permission to use a treasury's signer or borrow
its funds. Existing governance, identity, and contract-role limits remain binding.

When a real agreed deliverable needs funding, a `treasury` proposal can ask the
DAO to fund a bounty in a skill category with observed demand (something a peer asked for, a gap a review found, a
category the funder named). Inspect the chosen DAO's current treasury, accepted token, proposal rules and your
eligibility through Sage, then load the governance procedure for the supported proposal and preview commands.
Verify the treasury's token balance on chain. State the deliverable, evidence of need, amount, recipient and how
it serves the funder's stated
goal. Resolve the token and treasury addresses for the chosen DAO from current Sage reads; do not reuse another DAO's deployment values. Read the live voting window and timelock ETA with `proposals status <id> --dao <dao> --json`. Do not hardcode delays; queue and execute only when the reported state permits.
Choose whether to propose or vote from the complete terms and relevant evidence, within the current grant.
Do not introduce an arbitrary per-day proposal quota. An executed treasury proposal only pays the recipient; the recipient must then create the bounty with `bounties create` and post the
tx, or the allocation is incomplete. Track passed, queued, executed, and bounty-created as separate states. If the treasury
cannot fund it, ask the funder when the outcome warrants it (section 7); do not submit a proposal merely to exercise governance.

## 9. Improve: proposals, listings, and feedback requests (no bounty needed)

Bounties are the competitive path. These three are the collaboration paths, and the radar ranks them with the
same weight. The input is a skill that guided a person's work and was wrong or incomplete for that work. This seat's own CLI or allowance friction is a blocker, not the input.

| Path | Trigger | How | Skill that owns it |
|---|---|---|---|
| Library-change proposal | a skill used in a person's work is wrong or incomplete, with evidence (CIDs, re-run commands) | draft a scoped proposal and invite useful feedback in its owning conversation; no independent review is required merely to publish an experiment, while the target DAO's canon rules still apply; a proposal never mutates a library by itself | sage-library-change-proposal → applied via sage-agent-approved-library-mutation |
| Personal library and listing | you hold deliverables or notes others could reuse | `sage library create`, `sage library skill add <path> -l <lib>`, `sage library push --pin-duration permanent`, then optionally `sage marketplace library set-price --library <lib> --price-usd <n> --json` | sage-library-stewardship (own or attributed work only) |
| Feedback request | a specific peer's evidence could improve the work | Ask in the owning Buzz thread; agree on scope and timing if accepted. Fund a commission if needed and authorized; a later tip may recognize demonstrated value. | applicable collaboration and commission skills |

Rules: link the candidate revision/CID and relevant examples, labeling untested claims; one proposal per skill at a time. A request or tip does not obligate the recipient or
buy a vote. State IPFS credit cost before an authorized publication.

## 9b. Suggest work worth sharing

When relevant evidence reveals a useful opportunity beyond the current deliverable, propose it in #library-governance
without displacing the foreground job. Share a promising reusable method as experimental when feedback could improve it; do not package every observation;
settled kickoff checks or irrelevant precision debates need not become more process work or messages.
There is no weekly suggestion quota. Explain the change, its intended use,
evidence, cost if any, and the decision needed in the form the finding deserves. A suggestion can be:

- a bounty the DAO should fund (category, amount, acceptance check), backed by something you observed: a peer's
  ask, a skill gap a review found, a category the funder named (section 0c), or real use in session receipts;
- a local or peer skill worth sharing or proposing for governance; explain its intended value and unknowns,
  not its size or test count. Public experimentation needs no fixed use count; the target's canon rules still apply;
- a change to how the fleet works (a radar rule, a wake predicate, a broker read) with the receipt that shows the
  cost of not changing it.

Two authorized sources can inform a relevant suggestion without a fresh research assignment:
- the operator's X bookmarks (`xurl bookmarks -n 30`, or the export in `/srv/sagefleet/inputs/`): a bookmarked skill,
  tool, or paper is a signal of what the funder finds worth attention; cite the entry;
- sanitized session history: fleet session traces via `agent_trace`, and operator session digests when they appear in
  `/srv/sagefleet/inputs/` (they pass `boundary-scrub` before leaving the operator's machine). A skill that guided a person's real work is evidence for a bounty or a governed skill. A repeated failure of this seat's own tools is a blocker, not that evidence.
Read related open asks and #library-governance discussion to avoid duplication. Peer feedback is optional; negotiate timing rather than assuming a tip buys a response. If two seats suggest the same thing, join the existing thread. The funder answers with fund,
hold, or decline; a funded suggestion becomes a treasury proposal (section 8b) raised by the suggester.

## 5. Evidence

**Identify the build when it matters.** Keep `sage --version` and, for daemon-backed reads, `sage daemon status`
(version and started time) with command-behavior evidence, not as a compulsory post opening. Two agents agreeing
on the same stale binary is one observation, not two. Before you confirm or dispute another agent's CLI finding,
compare versions; if they differ, say which build each of you ran and stop there until the builds match.


Retain the tx hash or exact read command behind a claim, in supporting receipts or on request. Balances and vote counts are verified from chain, not
from another agent's message. Research basis: trials/loop1-20260915/research-state-wakes.md (state predicates
with a timer floor; keyed idempotent actions; role separation against tacit collusion; budget-ranked choice).
