---
name: address-the-prior-turn
description: >
  Point an agent chat reply at the earlier turn with @Seat, reply_to, and a
  short quote or event prefix strictly shorter than the new act. Use when
  writing a Buzz message or any multi-party agent reply that answers someone.
  Works alongside label-every-required-point and information-for-use (or use
  agent-chat-style for all five moves in one pass).
---

# Address the prior turn

Write the new act first, right after pointing at the person and the specific turn you are answering. In a busy multi-agent channel, receipt order breaks adjacency; the pointer (`reply_to` + `@Seat on "<short quote>"`) is what keeps the reply attached to its antecedent.

## Do this

1. **Attach the reply pointer in Buzz**:
   - When replying to an existing turn, pass `reply_to: "<event_id>"` (or `--reply-to <event_id>` on the CLI).
   - Open the first line with `@Seat on "<2–6 word quoted span>"` (or `@Seat [<8-char event prefix>]` when referencing a specific event ID).
   - Even if a reply covers multiple items, keep `reply_to` attached to the turn that triggered your reply so the thread stays linked.
2. **Lead with the decision or new act immediately after the pointer**:
   - State what changed, what you decided, or what you need the other seat to do in the first lines.
   - When the reply has more than one point the reader must not miss, label 100% of them (`label-every-required-point`).
3. **Keep any quote strictly shorter than the new act**:
   - Quote at most 2–6 words (never more than 1 line) to identify an off-screen span.
   - Never paste the earlier message in full, and never restate the other person's message in your own words before adding a one-line reply.
4. **Keep shared domain names (`conceptual pact`)**:
   - Use the exact technical name both sides already share (`content_access_denied`, `free-pin sync`, `owner seat`).
   - Shorten a shared name only after both sides already use it and can still identify it unambiguously. Never swap a shared technical term for a shorter vague word (`information-for-use`).

## Examples

**Bad — quote or restatement is longer than the new act:**

> Can you leave the second change out and ship only the first one today so we can see it before the meeting?
>
> Agreed.

**Good — pointer + short quote, new act is longer than the pointer:**

> @Basil on "leave the second change out" (`a33426e7`) — Ship the first change today and hold the second until after the meeting.

## Pre-send check

- [ ] Does the reply pass `reply_to` (when answering an existing turn) and open with `@Seat on "<2–6 word span>"` or `@Seat [<event prefix>]`?
- [ ] Is the quoted span strictly shorter than the new act?
- [ ] Did you cut any summary/restatement of what the other seat just said?
- [ ] Did you preserve shared technical terms instead of paraphrasing them?

See `references/research-basis.md` for the CMC and conceptual-pact research behind these rules.
