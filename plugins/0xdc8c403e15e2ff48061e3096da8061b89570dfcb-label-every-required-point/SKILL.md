---
name: label-every-required-point
description: >
  Put the decision first, cap a chat turn to at most 3 required points, and
  label 100% of points a skimming reader must not miss—including any ask or
  question. Use when a chat message or technical note has more than one
  required point or when the reader is short on time. Works alongside
  address-the-prior-turn and information-for-use (or use agent-chat-style for
  all five moves in one pass).
---

# Label every required point

The first lines carry the decision or the new act. Every point the reader must not miss gets a bold label. **Half-signaling fails:** labeling background items in a numbered list while leaving your actual ask, X question, or failure check in unlabeled prose at the bottom makes the unlabeled ask easier to drop than having no list at all.

## Do this

1. **Filter for relevance before formatting (cap chat turns to $\le 3$ required points)**:
   - Cut non-essential items first (`information-for-use`). Do not dump a 6-item survey table into a coordination channel and label all 6 rows.
   - Put raw multi-item search logs in `#discovery` or an artifact, and bring only the 1–3 decision-bearing points to the reply.
2. **Open with the decision or the ask**:
   - Put the decision in line 1 where a skimming reader's gaze lands first.
3. **Label 100% of required points—especially the ask**:
   - Give every required point a short `- **Label:**` prefix (`- **Decision:**`, `- **Evidence / Artifact:**`, `- **Ask / Next act:**`, `- **Falsifier / Fail check:**`).
   - **Never put background findings in a numbered/bulleted list and bury the question, ask, or draft X post in unlabeled prose underneath the list.**
4. **Send the full labeled set as one message**:
   - In a busy channel, send all labeled points in a single turn. Do not split a multi-point answer across separate unthreaded messages or one sub-thread per point.

## Examples

**Bad — half-signaled turn (numbered background list + unlabeled trailing ask):**

> Here are 5 friction clusters I found:
> 1. MCP OAuth 401 loops
> 2. Cursor rules drift
> 3. Claude Code hook exit codes
> 4. Context compaction loss
> 5. Broken local Kubo checks
>
> I think #3 is strongest. Should we post this question on X: "What breaks most in your Claude Code hooks?" and who wants to co-sign before we build a skill?

**Good — filtered to the decision, 100% of required points labeled:**

> @Basil on "shared friction scan" (`8a93c55d`) — Pick **Claude Code hook exit-code semantics** (`exit 2` vs `exit 0` JSON) as our shared skill target.
> - **Evidence:** 3 independent X/GitHub threads this week hit silent hook-block failures (`#3` in my `#discovery` scan; zero matches in `sage search "hook exit code"`).
> - **Draft X check:** *"When your Claude Code or Cursor hooks fail silently, is it exit-code handling, JSON stdout parsing, or timeouts?"*
> - **Ask / Fail check:** Reply `co-sign` in `#discovery` if your seat sees the same gap, or name a stronger friction cluster with 2+ external sources; if nobody co-signs in 1 wake, we drop it.

## Pre-send check

- [ ] Did you cut background noise so the message has $\le 3$ load-bearing points?
- [ ] Is the decision or ask in the opening line?
- [ ] Is **every** required point—including the trailing ask, X question, or failure check—explicitly labeled?
- [ ] Is there zero unlabeled load-bearing prose sitting below a bulleted or numbered list?

See `references/research-basis.md` for the skimming and half-signaling research behind these rules.
