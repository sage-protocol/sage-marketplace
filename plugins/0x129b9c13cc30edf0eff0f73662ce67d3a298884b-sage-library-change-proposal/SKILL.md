---
name: sage-library-change-proposal
description: "Turn session, curator, social, or collaborator evidence into a reviewable library-change proposal (patch, add, compose, archive) without mutating the library."
sage-inline-sidecars: false
license: MIT
metadata:
  version: 0.2.0
  author: sage-protocol
  tags: [sage-protocol, libraries, proposals, sessions, evidence, curation]
---

# Sage Library Change Proposal

Convert untrusted signals into a small proposal that another agent can inspect,
approve, reject, or repair. Proposal generation never changes a library. Use it
when evidence suggests fixing a defect, aligning a skill's value with what people
need, adding or composing a complementary skill, or archiving one. Do not use it
when an approved exact proposal is ready to apply.

Search before drafting, choose the smallest change, default to a local/private
surface, attach evidence quality, and name the one approval being requested.
One session or one social post is a lead, not a mutation.

## Task-specific instructions

Open the relevant section of [references/task-guide.md](references/task-guide.md)
before that operation, not the full guide for unrelated work. Sections cover:
Worked examples; Inputs; Workflow; Proposal schema; Decision rules; Present the
decision; Output.

## Authority and completion

The task defines scope. Continue authorized local reads and disposable checks without
asking again at each step. Stop only at a missing input or a real authority boundary.
No skill grants permission to sign, pay, publish, alter shared/governed state, or
expand credentials. Preserve relevant previews and verify authoritative state after
writes. Report what was verified and any remaining blocker; do not force packaging,
feedback, or public participation into an unrelated task.

## Distribution notices

See [source and change notices](references/DISTRIBUTION-NOTICES.md) and the
[license text](references/LICENSE.txt).
