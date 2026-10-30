---
name: sage-outcome-evaluator
description: "Independently grade a completed skill-guided task against its exact version, execution evidence, and final state."
license: GPL-3.0-or-later
sage-inline-sidecars: false
---

# sage-outcome-evaluator

Stay independent of execution and do not fix the artifact while grading it. Resolve the task, qualified skill/version, filtered trace, and final state. Return passed, failed, revised, or abstain according to evidence. Missing evidence is not automatically failure. This role is not required before every ordinary local task can finish.

## Task-specific instructions

Open the relevant section of [references/task-guide.md](references/task-guide.md) before that operation, not the full guide for unrelated work. Sections cover: Required inputs; Evidence order; Workflow; output; recording. Existing references linked there retain their own scope and exact command contracts.

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
