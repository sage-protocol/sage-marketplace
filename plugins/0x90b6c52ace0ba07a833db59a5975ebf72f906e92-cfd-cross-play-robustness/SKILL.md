---
name: cfd-cross-play-robustness
description: "Audit or test a multi-agent, cross-harness, or handoff skill for zero-shot coordination (ZSC) and Coordination-Friendly Definition (CFD) robustness across models."
license: MIT
sage-inline-sidecars: false
metadata:
  version: "0.1.0"
  author: sage-protocol
  source_paper: https://arxiv.org/abs/2611.06409
  source_repository: https://github.com/ahayler/zsc-llm-agents
  related_papers:
    - https://arxiv.org/abs/2003.02979
    - https://arxiv.org/abs/2103.04000
    - https://arxiv.org/abs/2106.06613
    - https://arxiv.org/abs/2412.06333
    - https://arxiv.org/abs/2604.08377
  tags:
    - sage-protocol
    - coordination
    - zsc
    - cfd
    - skills
    - evaluation
    - cross-play
    - multi-agent
---

Test whether a skill that coordinates across agents, harnesses, or sessions remains reliable when paired with a partner running a different model family or random seed (`XP_LLM` and `XP_seed`), rather than only passing in single-model self-play (`SP`).

Core rule from the meta-learned Coordination-Friendly Definition (CFD) in Hayler et al. ([arXiv:2611.06409](https://arxiv.org/abs/2611.06409)):

> Prefer instructions and actions that remain valid under several plausible partner interpretations of shared state, and reject steps that succeed only if a partner infers one unstated rationale.

## 1. Check the coordination surface gate

Apply this skill when the target skill has at least one coordination surface:

- **Producer-consumer artifact handoff**: one agent writes a report, JSON/YAML payload, PR body, or coordination card that another agent or harness parses.
- **Shared mutable state**: two or more agents act on the same git branch, worktree, Buzz channel, issue queue, or bounty thread.
- **Subagent or council dispatch**: a parent agent delegates work to child panes or model-council reviewers and synthesizes their outputs.
- **Multi-harness skill consumption**: the skill is installed across heterogeneous harnesses (such as Claude Code, Codex, Pi, Gemini/Antigravity, or Hermes) that interact in the same workspace or DAO.

If the skill is purely single-agent with no shared state or downstream agent reader, skip this skill and use an applicable single-agent evaluation or empirical prompt-tuning skill.

## 2. Run the four static CFD checks

Read the target skill and its references in full. Check every coordination point against the four ZSC failure classes isolated in [references/research-grounding.md](references/research-grounding.md) and detailed in [references/task-guide.md](references/task-guide.md):

| Failure class | Research benchmark | What to flag in the skill | Required CFD fix |
|---|---|---|---|
| **1. Unstated signaling convention (`Cat & Dog` / `Good Touch` trap)** | Off-Belief Learning ([arXiv:2103.04000](https://arxiv.org/abs/2103.04000)), Hayler et al. ([arXiv:2611.06409](https://arxiv.org/abs/2611.06409)) | A step emits or expects an untyped status word, implicit channel convention, or unstated field meaning without paying the upfront cost to state or inspect the schema. | Pay the `"remove the wall"` observability cost upfront: require an explicit schema, preflight read, or opt-in CID-pinned convention. |
| **2. Symmetric role deadlock or collision (`Narrow Tunnel` / `Brittle Bridge`)** | Other-Play ([arXiv:2003.02979](https://arxiv.org/abs/2003.02979)), Hayler et al. ([arXiv:2611.06409](https://arxiv.org/abs/2611.06409)) | Two peers receive identical instructions to claim, retry, yield, or merge without an asymmetry-breaking rule. | Define a deterministic tie-breaker using an observable asymmetric attribute (such as claim receipt timestamp, pane ID, or explicit initiator/responder role). |
| **3. Lexicographic, positional, or locale fragility (`Code Agents` / `Hund < Katze`)** | Treutlein et al. ([arXiv:2106.06613](https://arxiv.org/abs/2106.06613)), Hayler et al. ([arXiv:2611.06409](https://arxiv.org/abs/2611.06409)) | A procedure or helper selects "the first item", sorts free-text labels alphabetically, or assumes dictionary key order without a canonical key. | Bind selection to a content hash, explicit ID, or schema-defined sort key that is invariant under rephrasing or serialization order. |
| **4. Competing surface semantics vs. structural rule (`Semantic Selection Game`)** | Ma et al. (2023), Hayler et al. ([arXiv:2611.06409](https://arxiv.org/abs/2611.06409)) | A vivid example, metaphor, or default label in the prompt points one way while the formal constraint or safety rule points another way. | Align every example with the formal rule, or state an explicit precedence rule so aesthetic framing never overrides structural invariants. |

## 3. Run a paired cross-play probe (`XP_LLM`) and one semantic perturbation

Static review and single-model self-reports miss conventions that a model rationalizes as "natural". Before certifying a coordination-bearing skill or cutting rules during a token-diet pass:

1. **Paired cross-play probe (`XP_LLM`)**: run a minimal two-step handoff where Model A (producer or initiator) executes the skill on a fixed fixture without sharing its chain-of-thought, and Model B from a different model family or harness (consumer or responder) reads only the produced artifact and the skill to take the next step. Measure the cross-play gap (`SP - XP_LLM`) using the rubric in [references/task-guide.md](references/task-guide.md).
2. **Semantic perturbation check**: permute option order, rename arbitrary placeholder labels, or swap symmetric role labels in the fixture and confirm both models still converge on the same outcome.
3. **Convention-diet guard**: never delete an explicit coordination convention (schema, ID format, tie-break rule, role boundary, or fallback state) solely because one evaluator model passed a no-skill baseline in single-model self-play.

## 4. Emit the CFD robustness receipt and bounded recommendation

Open [references/task-guide.md](references/task-guide.md) for the exact `CfdRobustnessReceiptV1` schema and repair patterns. Open [references/research-grounding.md](references/research-grounding.md) when explaining why zero-shot cross-play diverges from self-play or how Sage's shared skill layer relates to ZSC.

Keep this skill read-only with respect to active libraries and governed canon. Stage any proposed skill edit in scratch space and hand off to `sage-conservative-skill-refinement` or `sage-library-change-proposal` with explicit operator approval.
