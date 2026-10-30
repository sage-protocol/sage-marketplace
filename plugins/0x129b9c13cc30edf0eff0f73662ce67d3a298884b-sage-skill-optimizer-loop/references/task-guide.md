# Evaluate and refine a skill

## Use existing evidence first

Select one capability and a fixed version. Preserve its source and license.
Record the intended task, allowed paths, safety boundaries, and completion test.
Copy the whole relevant bundle into scratch space, including its references.
Never optimize the global skill store or an immutable installed version in place.

Run the baseline on realistic cases: a useful task, a task that should not load
this skill, and a task that requires refusing an unauthorized action. Grade the
result and trace, not whether the model praises the skill. Keep graders and
expected answers out of the agent's task inputs.

After each bounded edit, repeat the same cases. Classify failure before changing
anything: instruction, missing reference, bad test, ambiguous task, or product
bug. Do not rewrite skill prose to conceal a product failure. Stop when measured
improvement plateaus or the agreed iteration budget ends.

## Native Sage SkillExamples, Lift Gate, Harness Evolution, and Canon Reputation Risk

Before reaching for external containers, use Sage's native manifest-backed evaluation and promotion pipeline:

`verified outcome passed` -> `sage capture mine --gate-baseline <b0> --promote <skill>` (`example_gate.rs`) -> `SKILL.md` `examples` + `routing_evidence` -> `sage skill test <key>` -> public push / DAO proposal (reviewed for quality and canon reputation risk).

1. **Sample set & single-skill routing test (`crates/core/src/skill/manifest.rs` & `crates/cli/src/commands/skill_examples.rs`)**:
   - Pull the skill's manifest `examples` (`SkillExamples`: `default` + `by_tier` for `small|medium|large`, `kind: "pass"|"failure-aware"`, `provenance: { source, author_claimed, model, outcome, lift }`) and `routing_evidence` (`RoutingEvidenceRefs`: `skill_content_hash`, `row_counts`) via MCP `skills.get` / `library.skill_get` or `sage skill example list <key>`. `ExampleProvenance.author_claimed` is portable attribution metadata (`manifest_claimed`), not an automatic payout split.
   - Run `sage skill test <key>` (`dataset_from_skill_examples`) to convert manifest `SkillExamples` / `test-cases.json` into a `BenchmarkDataset` and test routing against `SkillExamples` / `test-cases.json`, whereas behavioral lift is gated by `example_gate.rs` (`evaluate_example` / `evaluate_example_robust`).
2. **Tier-1 Measured-Lift Gate (`crates/core/src/skill/example_gate.rs`) & GPU-Free Harness Evolution**:
   - Run paired baseline-vs-candidate episodes (e.g., via Reef's GPU-free Harness Evolution `EpisodeScorer` + `sage-conservative-skill-refinement`) and feed `ExampleEvidence { successes, failures }` into `evaluate_example` (Wilson 95% lower confidence bound `wilson_z = 1.96` vs `baseline_rate`; requires `samples >= 5` and `margin = lower_bound - baseline_rate >= +0.05`) or federated `evaluate_example_robust` (Byzantine-resistant trimmed-mean consensus across DAO peers).
   - Promote verified `passed` captures with `sage capture mine --gate-baseline <b0> --promote <skill>` so passing examples are written to `SKILL.md` frontmatter with `provenance.lift` and matching local library entries are refreshed. This command does not update a governed DAO stream or submit a proposal. Keep DAO adoption as a separate, explicitly authorized governance action. Review the complete skill bundle, including its guides, before that handoff.
3. **Canon Reputation Risk vs. Reflections (`ReflectionDistributor`)**:
   - Examples exist to improve skill execution and give governance reviewers clear evidence before canon acceptance; bad or bloated examples carry **canon reputation risk** (failed runs, rejections, lost tips/usage, and governance replacement).
   - `ReflectionDistributor` does **not** split epoch emissions across manifest `examples` JSON; compensate helper contributors who author or test examples explicitly via **bounties** or **tips**. Cross-reference `sage-feedback-and-evals`, `sage-library-stewardship`, and `sage-identity-and-rewards`.

## Runner compatibility

The external [fastxyz/skill-optimizer](https://github.com/fastxyz/skill-optimizer)
project is optional. Its current workbench uses Docker cases/suites and
OpenRouter model runs. Inspect its pinned source and local command help before
use; do not assume historical `init prompt`, `benchmark`, or `optimize` commands
still exist. Read the upstream canonical skill and workbench schema for the
selected version rather than copying an unverified configuration into this guide.

Upstream references checked on 2026-09-09:
- [Canonical skill](https://github.com/fastxyz/skill-optimizer/blob/development/skills/skill-optimizer/SKILL.md)
- [License](https://github.com/fastxyz/skill-optimizer/blob/development/LICENSE)

Installation, Docker setup, credentials, and paid model calls require their own
operator authority. Prefer an already available approved runner when adequate.
Do not put secrets in prompts, examples, logs, or public result bundles.

## Accept and distribute

Keep the original when the revised skill does not improve the agreed cases.
Report evidence separately for static structure, actual guide loading, task
completion, and refusal behavior. One model or fixture does not establish broad
reliability.

For an approved installation, preserve customized files and foreign symlinks.
Install a new version and update the intended exposure, rather than editing an
old version cache. Verify root and reference hashes after installation.

For publication, load `sage-library-publish` and `sage-command-map`. Use
`sage library push <library> --dry-run` for the preview. Bind owner, target,
visibility, retention cost, and version before the approved write. Verify the
cloud pointer, pin retention, and anonymous public retrieval separately. Do not
publish scratch inputs, private traces, or credentials. DAO adoption is a
separate governed decision, not a side effect of a public personal-library push.
