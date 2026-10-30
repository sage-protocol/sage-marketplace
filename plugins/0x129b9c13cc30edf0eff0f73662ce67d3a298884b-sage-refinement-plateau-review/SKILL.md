---
name: sage-refinement-plateau-review
description: "Use after repeated skill-refinement attempts to decide continue, stop, or reframe; do not count rejected edits as improvement."
license: MIT
metadata:
  version: "0.1.1"
  author: sage-protocol
  source_paper: https://arxiv.org/abs/2604.08377
  source_repository: https://github.com/AMAP-ML/SkillClaw
  source_commit: 3938f7537645c961d94498a0a79fc0a977019595
---

1. Select one skill lineage and review window. Bind each attempt to exact base,
   candidate, evidence, dataset and runner identities. Discover and load an
   applicable local evidence-compilation skill if these are absent. Freeze the
   useful-lift threshold, regression constraints, and remaining time/token budget
   before interpreting the sequence. Do not invent a universal round limit from
   a small study; ask for a bounded review budget if none was agreed.
2. Read available Sage history after checking installed help:

   ```bash
   sage skill refinement list --format json
   sage skill refinement show <proposal-id-or-digest> --format json
   sage suggest feedback breakdown <library/key> --content-hash <content-hash> --format json
   sage skill example list-rejected <key> --format json
   ```

   Refinement reads summarize local caches, not all remote history. `show`'s
   aggregate pass means *any* passing evaluation exists; inspect every evaluation
   digest and obtain exact reports before concluding consistency. Report absent
   or inaccessible evidence as unknown. Example rejection is not candidate
   rejection; neither is a routing reject or a failed execution outcome.
3. Build one chronological ledger: attempt ID, exact base/candidate, coherent
   change/hypothesis, independent incidents, matched pairs, metric and interval,
   holdout/security/cost results, evaluator decision, operator/DAO disposition,
   actual adoption state, and reason. Keep `not_evaluated`, `insufficient`,
   `fail`, `pass`, review rejection, stale base, and missing records distinct.
   Separate independent matched runs from reruns of the same fixtures; more
   repetitions improve precision, not source diversity.
4. Compare only compatible slices: same task distribution, fixture version,
   model/harness/environment and success definition. A changed dataset or model
   starts a new segment, not a spurious upward trend. Do not add per-attempt
   gains across changing bases or pool conflicting evals to hide regressions.
   Compare current retained content to the original baseline only with a matched
   evaluation that actually made that comparison.
5. Classify the trajectory:
   - **Useful early fix:** evidence showed a concrete procedural bottleneck;
     matched results clear the predeclared useful-lift gate without forbidden
     regression. Adoption remains a separate recorded decision.
   - **Rejected micro-refinement:** wording/order/detail churn fails to beat the
     retained base, repeats an earlier rejected hypothesis, or costs more than
     its gain. Rejection preserves the base; it adds no performance improvement.
   - **Market response:** tips whose `--ref` names the skill key, bounty
     acceptance, or governed adoption of that version. This is an evidence class
     beside local evals. It does not by itself certify quality.
   - **Unknown:** incomplete evals, stale identities, few independent incidents,
     conflicting runs, an unconfigured runner, or no external chain event after
     the review window. A quiet chain is unknown, not a plateau.
   - **Wrong problem:** persistent errors belong to tool/model/environment,
     routing or task definition rather than the skill's instruction content.
6. Recommend exactly one next action with confidence and supporting evidence:
   - **continue** only for a new bounded causal hypothesis or a specific missing
     measurement with remaining budget. Name one candidate/test, the stopping
     condition and maximum additional budget; no unattended retry loop.
   - **stop** this refinement window when comparable attempts have exhausted
     useful hypotheses or the agreed budget is spent. Preserve the last actually
     adopted version and rejected-attempt ledger; do not activate a passing but
     unadopted candidate. State the new evidence that would reopen review.
   - **reframe** when the likely bottleneck is elsewhere, observations conflict,
     the eval is insensitive/leaky, or the environment shifted. Specify one
     discriminating experiment or route to an applicable tool/runtime, discovery,
     or evaluation skill; do not conceal a broader rewrite as another iteration.
7. Return a private review with lineage/window, coverage limits, ledger, early
   fixes versus later churn, measured gain versus unchanged retention, unresolved
   causes, continue/stop/reframe decision, next test or reopen condition, and
   remaining budget. Add a separately scrubbed synopsis only if requested.

No new skill edits, synthetic feedback, training, activation or publication occur
here. Do not mint feedback to fill a quiet window. A plateau can mean useful work is finished, not that skill authoring failed.
SkillClaw's small same-model day/night study and Accept/Reject tables motivate
this review; they do not prove monotonic safety, global improvement, or an optimal
number of refinement rounds. This is original guidance inspired by the cited
paper/repository, not copied SkillClaw code.

## Distribution notices

See [source and change notices](references/DISTRIBUTION-NOTICES.md) and the
[license text](references/LICENSE.txt).
