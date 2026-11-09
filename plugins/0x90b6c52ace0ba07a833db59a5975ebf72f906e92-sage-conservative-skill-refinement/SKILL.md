---
name: sage-conservative-skill-refinement
description: "Read before proposing one evidence-backed skill edit; abstain when attribution is weak and never mutate active or governed canon."
license: MIT
metadata:
  version: "0.1.0"
  author: sage-protocol
  source_paper: https://arxiv.org/abs/2604.08377
  source_repository: https://github.com/AMAP-ML/SkillClaw
  source_commit: 3938f7537645c961d94498a0a79fc0a977019595
---

1. Bind the selected skill, library, exact base content hash and manifest/revision
   to a private evidence pack. If missing, discover and load an applicable local
   evidence-compilation skill. Reuse indexed prior decisions when available.
   Read the full base and every directly referenced file before proposing edits.
   A governance suggestion prioritizes investigation, not mutation or adoption.
2. Locate one instruction-level gap that the base does not already handle.
   Trace it to exact-version observations and a successful counterexample.
   Separate these causes before choosing an intervention:

   | Cause | Judgment and route |
   |---|---|
   | Skill | Incorrect fact, missing precondition, or ambiguous procedure supported by exact-base evidence: consider a bounded patch |
   | Model | Correct loaded guidance ignored or reasoning failed: retain facts; test model/harness or presentation hypotheses first |
   | Tool | Tool defect, changed API, permission refusal, or outage: verify current contract; do not invent a replacement command |
   | Environment | Missing assets, configuration, network, hardware, or credentials: repair outside this procedure; add a preflight only if repeated evidence shows the skill omitted a necessary check |
   | Routing/gap | Skill not applicable or not loaded: search/reuse or trigger review, not a body rewrite |
   | Mixed/unknown | Preserve uncertainty; request an isolating test instead of blaming every skill in a session |

   Failure-category labels are symptoms, not causal proof. A repeated failure in
   one model/environment does not establish a global skill defect.
3. Abstain if evidence is weak, stale, conflicting, dominated by one incident,
   missing a plausible disconfirmation, or cannot distinguish these causes.
   Prior rejected wording churn without new evidence is a plateau-review input.
   State the missing observation that would change the decision. Multiple retries
   or agreement among reviewers do not create independent execution evidence.
4. State one falsifiable hypothesis and expected gain, supported scope, regression
   risks, and evaluation needs before editing. Freeze the fixtures, selector,
   minimum matched samples/lift, forbidden regressions, cost budget, and source
   concentration policy. Include the observed failure, clean success, nearby
   non-failure, disconfirming case, held-out tasks, and security probes. Discover
   and load an applicable matched-evaluation skill for actual runner mechanics.
5. Make one coherent change only in an approved, isolated scratch copy. Prefer
   an additive clarification at the decision point over restructuring. Preserve
   successful guidance, headings, terminology, tool names, endpoints, ports,
   payload/output formats, paths, and filenames. Change an observable contract
   only with current authoritative evidence plus reproduced old-fails/new-works
   cases. Never turn a private environment value into portable guidance. Use a
   verified discovery/preflight rule or keep that adaptation local. Prefer
   instructions that remain valid under several plausible partner or harness
   interpretations of shared state, and replace steps that succeed only if a
   partner infers one unstated rationale with an explicit schema or preflight
   check. When refining a multi-agent, subagent, or cross-harness handoff skill,
   discover and load `cfd-cross-play-robustness`. Additive is a preference, not
   permission to append contradictory or generic advice.
6. Read `references/proposal-contract.md` and choose the honest artifact route:
   an exact validated `SkillRefinementProposalV1` with real immutable identities,
   or a documented abstention from issuing that proposal. A scratch candidate
   and evaluation plan can accompany abstention; neither is a valid proposal.
   Do not fabricate commits, CIDs, digests, signatures, test results, or status.
7. Require machine checks for base freshness, allowed paths and exact diff,
   schema/digests, evaluation identity/completeness, lift, regressions, and
   authority. Judgment explains why the change is useful; it cannot waive a
   failed or unavailable check. A passing score or an LLM Accept is not safety
   evidence, permission to activate, or proof of monotonic improvement.

Return the exact proposal or abstention, evidence and contradiction references,
one delta, preserved contracts, expected gain, regression risks, checks actually
run, pending evals, rollback target, and next evidence/approval step. Expected
gain stays a hypothesis until measured. Independent reproduction in a second
harness is required before recommending shared or governed adoption; review
agents are not that reproduction.

Never edit the active skill, shared/governed canon, ranking scope, or IDE files.
Never create signed drafts, publish, activate, or execute governance from this
skill. Discover and load applicable library-proposal and governance/publication
skills only for a separate operator-approved handoff.
