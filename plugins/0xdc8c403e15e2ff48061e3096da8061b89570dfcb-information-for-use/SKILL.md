---
name: information-for-use
description: >
  Test a technical or chat message as relevant, findable, understandable, and
  usable by the named reader, with a next act and a failure check. Use when
  someone must act on the message, including instructions and agent replies.
  Never use a readability grade as the test. Works alongside
  address-the-prior-turn and label-every-required-point (or use
  agent-chat-style for all five moves in one pass).
---

# Information for use

A message passes when the named reader can find the decision, understand it in the terms they already use, execute the next act, and tell whether that act failed. A syllable or sentence-length readability grade is never the test.

## The four checks (ISO 24495-1)

1. **Relevant:** Give this reader only what they need for the decision and the next act. Cut background logs, unrequested status recaps, and extra candidates that do not change the action.
2. **Findable:** Put the decision in line 1 and label every required point (`label-every-required-point`). Use a list or compact table when parallel detail would otherwise overload a paragraph.
3. **Understandable:** Point at the prior turn with a short quote (`address-the-prior-turn`) and keep the exact domain terms this reader already uses.
4. **Usable:** State the concrete next act and how the reader knows that act failed.

## What every actionable turn carries

Step-by-step commands without a purpose or failure check leave the reader stuck on the first unexpected output. Every labeled ask or handoff must state:

- **Next act:** the exact command, check, or decision the reader should run next.
- **Failure check:** the exact status code, error string, or falsifier that tells the reader the act failed and what to report back.

## Keep shared technical terms (never chase a readability grade)

- Never swap a precise technical term the reader already uses (`content_access_denied`, `free-pin sync`, `owner seat`, `manifestCID`, `--payment-network base`) for a shorter, vaguer word just to lower sentence or syllable counts.
- Do not mechanically insert `"you"` or turn headings into rhetorical questions.
- Cut explanation the reader does not need for the decision, the find, or the next act—but always keep the failure check.

## Examples

**Bad — steps with vague terms and no failure check:**

> Push the collection to the remote server and make it open to everyone. Then ask the other agent to pull it and run the test script.

**Good — exact domain terms, next act, and failure check:**

> @Enki on "403 content_access_denied" (`be358702`) — Republish `checkout-guardrail-experimental` to the cloud registry so another seat can sync it.
> - **Next act:** Run `sage library push checkout-guardrail-experimental --cloud --pin-duration 12months` and `sage library visibility checkout-guardrail-experimental --visibility public`, then post the new `manifestCID`.
> - **Fail check:** Run `sage config ipfs status <manifestCID>`. If it still says `owner-only, not publicly retrievable` or `Basil` gets HTTP `403 content_access_denied` on `sage library sync <manifestCID>`, paste the exact status output before retrying.

## Pre-send check

- [ ] **Relevant:** Did you cut every detail that does not help the reader decide or act?
- [ ] **Findable:** Is the decision first and every required point labeled?
- [ ] **Understandable:** Did you keep the exact technical terms the reader already uses?
- [ ] **Usable:** Does the message state both the **next act** and the **failure check**?

See `references/research-basis.md` for the ISO 24495-1, IEC/IEEE 82079-1, Redish & Selzer (1985), and Minimal Manual research behind these rules.
