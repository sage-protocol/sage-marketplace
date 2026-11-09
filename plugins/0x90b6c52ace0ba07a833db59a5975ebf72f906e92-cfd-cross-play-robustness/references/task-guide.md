Follow these steps to audit, probe, and harden a coordination-bearing skill against cross-play failures.

## 1. Static CFD audit rubric

Inspect `SKILL.md` and every file under `references/`, `scripts/`, and `assets/`. Record a pass, fail, or not-applicable verdict for each of the four checks:

### Check A: Unstated signaling convention vs. `"remove the wall"` (`Cat & Dog` / `Good Touch`)

- **Question**: Does any step emit a compact message, status label, or artifact that a partner agent can interpret in more than one plausible way unless it shares an unstated convention?
- **Common symptoms in skills**:
  - Telling an agent to post a short status word (such as `"ready"`, `"done"`, or `"blocked"`) without specifying the required fields (branch, commit SHA, test command, or blocker question).
  - Assuming a downstream consumer knows whether an omitted JSON field means `null` (daemon offline or unknown) versus `false` (explicitly disabled).
  - Expecting a partner to infer why a file was left untouched without recording an explicit abstention reason.
- **CFD repair (`"remove the wall"`)**:
  - Pay the small token or tool-call cost upfront to make the state directly observable.
  - Specify the exact key-value schema, command preflight (`sage library active --format json`), or three-state distinction (`true` / `false` / `null`) in the skill.

### Check B: Symmetric role deadlock or collision (`Narrow Tunnel` / `Brittle Bridge`)

- **Question**: If two agents load this skill simultaneously on the same repo, issue queue, or Buzz channel, can they either both yield forever or both claim the same resource?
- **Common symptoms in skills**:
  - Instructing every agent in a channel to "reply when a question appears" or "pick the top unclaimed task" without a single-responder or claim-lock rule.
  - Telling two peers to "wait for the other agent to confirm before proceeding" when both hold symmetric roles.
- **CFD repair**:
  - Break symmetry using an observable, asymmetric property: one open responder per channel with mention-only specialists (`buzz-shared-agent-standup`), an explicit initiator/responder role assignment, or a durable claim receipt checked before work starts.

### Check C: Lexicographic, positional, or locale fragility (`Code Agents` / `Hund < Katze`)

- **Question**: Does the skill or any helper script rely on alphabetical sorting of natural-language labels, array index order (`items[0]`), or locale-dependent string matching?
- **Common symptoms in skills**:
  - Selecting "the first proposal" or "the first matching library" without an explicit governor scope (`<lowercase-governor>-<proposalId>`) or content hash.
  - Sorting free-text category names alphabetically to break ties.
- **CFD repair**:
  - Key every selection by an immutable identifier (CID, git SHA, governor-scoped ID, or explicit numeric priority field).

### Check D: Competing surface semantics vs. structural rule (`Semantic Selection Game`)

- **Question**: Does a vivid example, template placeholder, or prose metaphor in the skill pull one model family toward an intuitive shortcut that violates the formal constraint?
- **Common symptoms in skills**:
  - Showing a convenient shortcut in an example block (such as a bare proposal ID or a single-command force push) and relying on a footnote elsewhere to forbid it.
  - Using persuasive or dramatic framing that encourages action when the formal rule requires abstention under weak evidence.
- **CFD repair**:
  - Make every example obey the exact structural constraint. State precedence rules explicitly at the decision point.

## 2. Paired cross-play probe (`XP_LLM`) and perturbation protocol

Single-model self-reports miss conventions that the model treats as obvious. When live evaluation is authorized:

1. **Select one realistic coordination fixture**:
   Choose a bounded task where Agent 1 produces an output (such as a handoff note, library-change proposal, review verdict, or coordination card) and Agent 2 must consume only that output plus the skill to execute the next step.
2. **Run Self-Play (`SP`) baseline**:
   Run Agent 1 and Agent 2 with the same model family (`Model A -> Model A`) and record task score $J(\text{A}, \text{A}) \in [0, 1]$. Keep reasoning traces private to each turn so Agent 2 sees only the external artifact.
3. **Run Variable-LLM Cross-Play (`XP_LLM`)**:
   Pair two distinct model families or harnesses in both role directions (`Model A -> Model B` and `Model B -> Model A`) on the same fixture. Compute:
   $$J_{\text{XP}}(\text{A}, \text{B}) = \frac{1}{2}\big( J(\text{A}^1, \text{B}^2) + J(\text{B}^1, \text{A}^2) \big)$$
   and the cross-play gap:
   $$\text{XP-gap} = \frac{1}{2}\big( J(\text{A}, \text{A}) + J(\text{B}, \text{B}) \big) - J_{\text{XP}}(\text{A}, \text{B})$$
4. **Run one semantic perturbation**:
   Reorder the options, swap symmetric agent names, or replace placeholder labels in the fixture. Re-run the handoff and verify that the chosen action and parsed fields remain invariant.
5. **Diff discretionary choices across models**:
   Compare the unprompted formatting, field interpretations, and fallback choices made by Model A and Model B. Any point where both models were confident in self-play but diverged in cross-play is a hidden convention that must be made explicit.

## 3. Interaction with `skill-diet` and `empirical-prompt-tuning`

- **Cross-Play Convention Exception for token-diet passes (`skill-diet`)**:
  In single-agent skills, a rule that `$EVAL_MODEL` already follows in the `none` (no-skill) baseline can often be cut as redundant weight. In multi-agent or cross-harness skills, a rule that Model A follows by default is frequently an unstated model prior that Model B inverts in `XP_LLM`. Never delete an explicit coordination convention (schema, ID format, tie-break rule, role boundary, or three-state fallback) unless a deterministic code or schema check below the skill already enforces it.
- **Cross-Model Discretionary Diff for prompt tuning (`empirical-prompt-tuning`)**:
  Do not rely solely on a single subagent's self-reported `Discretionary completions` or `Unclear points` for coordination skills. Run the scenario across at least two distinct model families or a producer-consumer pair and diff their actual artifacts.

## 4. `CfdRobustnessReceiptV1` schema

Report the audit and probe results using this structure:

```yaml
schema: CfdRobustnessReceiptV1
skill_key: "<skill-name>"
library: "<library-name-or-local-path>"
skill_content_hash: "<sha256-or-git-blob>"
coordination_surfaces:
  - "<artifact-handoff | shared-state | subagent-dispatch | multi-harness>"
static_checks:
  unstated_signaling_convention: "<pass | fail | n/a>"
  symmetric_role_tie_break: "<pass | fail | n/a>"
  lexicographic_or_index_fragility: "<pass | fail | n/a>"
  competing_surface_semantics: "<pass | fail | n/a>"
cross_play_probe:
  status: "<ran | skipped-static-only>"
  models_tested: ["<model-a>", "<model-b>"]
  sp_score: <0.0-to-1.0-or-null>
  xp_llm_score: <0.0-to-1.0-or-null>
  xp_gap: <number-or-null>
  perturbation_invariant: <true | false | null>
  divergent_conventions_found:
    - "<exact convention mismatch observed between Model A and Model B>"
recommended_action: "<none | remove-the-wall-patch | pin-governed-convention | abstain>"
proposed_delta_summary: "<one bounded change or reason for abstention>"
```
