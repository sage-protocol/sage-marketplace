# Reuse the coordination components

Use this check before adding coordination tools, handoff records, action claims,
schedulers, or reports. Sage and the selected runtime already provide components;
discover their current contracts instead of assuming a new layer is needed.

## Map the need to its owner

| Need | Reuse first | Boundary |
| --- | --- | --- |
| Find a capable participant or procedure | Sage skill, prompt, behavior, and library discovery | Inspect the selected capability before use. |
| Compose several procedures | Sage behaviors and their declared skills | A behavior controller plan is not completed execution. |
| Discuss, request review, or show a result | The existing authorized Buzz thread and supported mentions | A mention requests attention; it does not grant authority. |
| Send a private session handoff or ask | Sage native inbox through the installed CLI or `sage_inbox_*` adapter | Check session identity, visibility, and receipts; receipt or acceptance is not completion. |
| Resume work and schedule a due step | The selected harness/runtime's supported continuation and scheduling | Discover actual support. Do not build a second scheduler in Sage or Commons by default. |
| Bind decisions, incentives, or paid work | Existing Sage proposal, bounty, feedback, and reward surfaces when needed | Discussion does not require a bounty or DAO. Signed and public effects retain their approval gates. |
| Verify progress | Existing request, turn, tool, artifact, and relay receipts | Observation is not authority, quality, or useful completion. |

## Before inventing a component

1. Recover the requested outcome, current owner, authority, and existing thread
   or inbox context. A local draft or report does not become authoritative state.
2. Search Sage from the target workspace. Inspect the owning skills and current
   tool schemas. Test the relevant read-only route when its availability is in doubt.
3. Map each required operation and durable record to an existing owner. Compose
   those components in a skill or behavior; do not duplicate their state or gates.
4. Classify a failure as missing, not loaded, advertised but not attempted,
   rejected, broken, or genuinely unsupported. Repair loading, usage, or the
   owning component before proposing a replacement. A denied effect is not a gap.
5. If a required primitive is genuinely absent, document the reproducer, checked
   alternatives, smallest extension to the owning component, and regression cases.
   Obtain explicit approval before adding parallel coordination state, a timer,
   action reservations, or a dispatcher. Record its owner and removal condition.

Existing compatibility machinery is not approval to extend it. Preserve pending
work when migrating it; do not delete ledgers or stop timers without approval.
A patch may be reviewed in Buzz or through an authorized Git workflow. Use Sage
inbox for private session handoffs when appropriate, not as a mandatory detour
for every public review.

## Keep evidence judgments separate

- **Delivery:** the intended response was accepted and independently read back
  in its request's thread. A completed response need not schedule another wake.
- **Continuation:** remaining work was retrieved and acted on at the next
  relevant turn, or a real blocker was preserved. Report not required when no
  continuation is due; unknown when evidence is missing.
- **Usefulness:** the result meets the requested acceptance criteria, supported
  by the relevant artifact, test, decision, or independent use.

Join evidence using explicit request, turn, session, tool-call, and receipt IDs
where the producers actually emit them. A broker process scope may span multiple
turns; it is not automatically a turn ID. Time windows can locate candidates,
but channel + agent + time alone does not prove causality. Link a fired wake
through its emitted-event receipt and the matching turn; then verify that the
turn resumed this work. Unknown links stay unknown.

Before calling a report verified, inspect the producers' real schemas. Test with
sanitized real-shaped records, including null `reply_to`, purpose-keyed wakes,
unrelated same-channel activity, concurrent turns, and delivery with no further
work. Do not add workflow steps merely to make a reporting verdict pass.

## Regression cases

| Situation | Required decision |
| --- | --- |
| A private ask can use Sage inbox | Reuse the native route; do not create a mailbox database. |
| A tool exists but was not attempted | Fix routing or usage; do not invent another tool. |
| A one-hour deadline exceeds a heartbeat's cadence | Inspect supported scheduling; propose only a demonstrated missing primitive, with separate approval. |
| A response is complete with no next action | Assess delivery and usefulness; continuation is not required. |
| An unrelated wake fires later in the same channel | Do not count it as this request's continuation. |
| Fixtures pass but producers omit the assumed IDs | Mark the join unsupported and test real-shaped records before rollout. |

## Transport adapters, not collaboration stages

Keep intent, owner, commitment, authority and evidence independent of the channel.
Sage Chat is the default for a new authorized collaboration without an existing
conversation or user/deployment channel preference. Sage Chat, Telegram, X and
Buzz are alternative configured transports; a default does not migrate work. Preserve
service-scoped conversation, message and actor references; never convert a handle
to a wallet or assume a thread ID is globally unique. A local harness can use the
same collaboration procedure without joining a fleet.

Discover actual read, reply, identity and receipt capabilities at the adapter
boundary. Existing transport-specific UUIDs or mention fields stay in that
adapter; do not impose them on generic skill guidance. No connector installation,
public post or cross-channel context transfer follows merely from discovery.
Scheduling belongs to the selected runtime, including when the transport itself
has no wake feature. Unsupported delivery remains explicit, not an invented receipt.
