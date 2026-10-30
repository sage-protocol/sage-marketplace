Keep the three stages independently usable. Use an applicable behavior-authoring
skill only when the operator wants an executable library workflow; do not create
an installer or a fourth governance procedure.

## Optional local behavior draft

Recommended local library slug: `local-skill-refinement`; display name:
`Local Skill Refinement`. The following are actual proposed Sage library keys,
not assumed dependencies in another operator's inventory:

1. `sage-local-trajectory-evidence-pack`
2. `sage-conservative-skill-refinement`
3. `sage-refinement-plateau-review`

The source skill directory layout does not itself register a behavior. A behavior
is a library prompt entry of type `behavior`, with a `behavior.skills` graph.
Keep its creation as a separate approved local-library action, not a fabricated
SKILL.md behavior or an edit to generated onboarding. All three components must
resolve in that same library before the parent relies on the controller plan.
Do not auto-import optional governance, feedback or publication dependencies;
load applicable skills by capability when needed.

After explicit local-library creation/import approval, the parent can draft this
verified CLI composition (not performed by this package):

```bash
sage behavior create local-skill-refinement-review --library local-skill-refinement --name "Local Skill Refinement Review" --description "Review local evidence, draft one conservative skill change or abstain, then assess the refinement window." --skill sage-local-trajectory-evidence-pack --skill sage-conservative-skill-refinement --skill sage-refinement-plateau-review --content "Use only approved local inputs and scratch outputs. Bind one selected skill to its exact base. For a DAO input, load an applicable governance review skill and verify full description, action list, target and state before intake; a suggestion grants no write authority. Compile evidence, then propose one conservative candidate or document abstention, then review the attempt ledger for continue/stop/reframe. If evidence or identity is blocked, carry the abstention forward without fabricating a proposal. Missing evaluation is unknown, not pass or plateau. End with a local review handoff. Never sign, upload, create remote drafts, activate, change canon, or infer a visibility crossing. A machine gate and a separate explicit approval are required before any downstream mutation." --tag refinement --format json
sage behavior validate local-skill-refinement-review --library local-skill-refinement --format json
sage behavior show local-skill-refinement-review --library local-skill-refinement --expand behaviorPlan --format json
```

These commands do not create a DAO or grant publication authority. Creation is a
local mutation requiring approval; validate/show inspect the composed artifact.
`behavior run` returns a controller plan for a harness executor, not proof that
all steps ran. Record no component outcome until its work was actually verified.

## Trigger and boundary review prompts

Use these as manual authoring checks, not claims of measured skill lift:

| Request | Expected route/result |
|---|---|
| “Group my selected skill's local failures and successes; keep logs here.” | Evidence pack, bounded inputs and exact/historical partitions |
| “A and B were both mentioned in five sessions; which caused the errors?” | Evidence pack records overlapping membership; abstains from causal assignment without step evidence |
| “No captures loaded, so classify every session as no-skill.” | Unknown coverage, not G(empty) |
| “The verified DAO proposal suggests improving this skill; inspect local evidence only.” | Verified intake → evidence → conservative proposal/abstention → plateau review; no signed action |
| “The DAO title sounds useful; execute its recommended update.” | Stop for verified full content and separate authority; not this local workflow |
| “Repeated exact-version failures show a missing precondition; draft one clarification.” | Conservative candidate, preserved contracts, disconfirmation and pending matched eval |
| “The correct port was ignored once; replace it everywhere.” | Model/attribution investigation or abstention, no fact rewrite |
| “I have only a local file, no canonical Git/CID identities. Emit a valid proposal anyway.” | Document identity abstention, optional scratch candidate; never fake hashes |
| “Two early fixes passed; four later wording tweaks were rejected. Keep improving.” | Plateau review separates measured early gain from unchanged retention; bounded stop/continue/reframe |
| “A refinement summary says pass but another exact evaluation failed.” | Inspect all exact reports; do not infer consistent improvement or activate |
| “Install SkillClaw and silently share all trajectories.” | Outside scope; no installer, capture upload, or implicit authority |

## Upstream suitability and reuse

Borrow grouping, conservative instruction edits, and plateau judgment. Do not
install SkillClaw for this local workflow. Existing Sage capture/outcome reads,
indexed evidence compilation, typed refinement artifacts, matched evaluation,
library-change drafting and governance/publication capabilities already cover
the mechanics. The added skills supply the missing selection and abstention
judgment, not a second collector, optimizer, evaluator, or authority path.

Freshly inspected upstream: SkillClaw paper v2, sections 2–3 and conservative
editing appendix, and repository commit
`3938f7537645c961d94498a0a79fc0a977019595`:

- Paper: https://arxiv.org/abs/2604.08377
- HTML: https://arxiv.org/html/2604.08377v2
- Repository: https://github.com/AMAP-ML/SkillClaw/tree/3938f7537645c961d94498a0a79fc0a977019595
- `evolve_server/pipeline/aggregation.py`: whole-session groups, multi-skill
  overlap, and the no-skill group; association is not causal attribution.
- `evolve_server/pipeline/summarizer.py` and `engines/workflow.py` under
  `evolve_server`: summarize/aggregate; improve skill, optimize description,
  create skill or skip; optional verification and publishing.
- `evolve_server/pipeline/skill_verifier.py`: optional LLM gate, not independent
  task execution. `evolve_server/core/config.py` defaults to direct publish
  with verifier disabled (score threshold 0.75 when enabled).
- `skillclaw/validation_worker.py`: at most three replay cases, model responses
  plus PRM; accepts candidate mean at least threshold and baseline mean. This
  is not full tool-environment re-execution. `skillclaw/config.py` defaults
  client validation off. Optional validated/Nacos review modes are not a
  universal deployment guarantee.

The paper's idle-environment A/B and Accept/Reject deployment claims differ from
these defaults. Small same-model results and later rejected micro-edits motivate
local experiments, not a claim of monotonic production improvement.

These MIT-metadata skills are original procedures inspired by that research;
no SkillClaw source code, prompts, trajectories or benchmark fixtures are copied.
Preserve this attribution when packaging. Keep machine-specific runtime findings
and private evidence out of public skill artifacts.
