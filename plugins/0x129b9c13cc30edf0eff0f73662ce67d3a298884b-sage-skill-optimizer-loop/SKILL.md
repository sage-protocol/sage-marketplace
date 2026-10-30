---
name: sage-skill-optimizer-loop
description: "Evaluate and refine a Sage skill in private scratch space; retain only improvements supported by behavior tests."
tags: [sage-protocol, skills, evaluation]
license: GPL-3.0-or-later
sage-inline-sidecars: false
---

# Sage skill refinement

Inspect the candidate and its license. Test a baseline before editing. Work in
private scratch space with explicit allowed paths and a bounded iteration count.
Keep only improvements supported by the same behavior tests, without weakening
safety or making unrelated tasks load more guidance.

Open [references/task-guide.md](references/task-guide.md) before choosing a
runner or starting a refinement. It covers deterministic evidence, upstream
compatibility, negative controls, and publication checks.

Do not execute untrusted skills directly. A benchmark quote, wallet balance,
or proposed improvement is not spending or installation authority. Ask before
paid runs, credential changes, customized-file replacement, publication, or
governance. Continue authorized local inspection without inventing extra gates.

Report baseline and revised results, failures, accepted changes, and remaining
limits. A returned plan or shorter file is not proof of improved behavior.

## Distribution notices

See [source and change notices](references/DISTRIBUTION-NOTICES.md) and the
[license text](references/LICENSE.txt).
