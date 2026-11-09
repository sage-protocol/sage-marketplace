Use these research findings to diagnose why multi-agent and cross-harness skills fail across models even when single-model evaluations pass, and to choose between zero-shot CFD hardening and explicit CID-pinned conventions.

## 1. Zero-Shot Coordination (ZSC) among LLM agents

Hayler, Chirra, Lupu, Forkel, Sarkar, Feng, and Foerster, *Zero-Shot Coordination among LLM Agents* (NeurIPS 2026, [arXiv:2611.06409](https://arxiv.org/abs/2611.06409), code: [github.com/ahayler/zsc-llm-agents](https://github.com/ahayler/zsc-llm-agents)) formalize multi-agent LLM coordination as a Decentralized Partially Observable Markov Decision Process (Dec-POMDP) wrapped in a natural-language description:

$$\mathcal{D} = (\mathcal{D}_{\mathcal{M}}, \mathcal{D}_{\mathcal{R}}, \{\mathcal{D}_{\mathcal{H}_i}\})$$

Unlike tabular or deep reinforcement learning agents trained from scratch, LLM agents enter every task with strong semantic priors over labels, metaphors, ordering, and social norms. Two policies $\pi_i$ and $\pi_j$ are evaluated under the symmetric cross-play objective:

$$J(i, j) = \frac{1}{2}\mathbb{E}_{(\pi_i, \pi_j)}\big[ J(\pi_i^1, \pi_j^2) + J(\pi_j^1, \pi_i^2) \big]$$

across three regimes:

- **Self-Play (`SP`)**: identical model, prompt, and convention assumptions on both sides.
- **Fixed-LLM Cross-Play (`XP_seed`)**: the same model family run across independent seeds or episodes without shared reasoning traces.
- **Variable-LLM Cross-Play (`XP_LLM`)**: heterogeneous model families (such as Claude Opus, Gemini Pro, GPT, Grok, DeepSeek, and Kimi) coordinating zero-shot.

The **cross-play gap** (`SP - XP_LLM`) measures how much a skill or agent scaffold relies on brittle, model-specific conventions that collapse when the partner changes.

## 2. Four empirical failure modes in multi-agent LLM coordination

1. **Unstated signaling conventions and upfront-cost aversion (`Cat & Dog`, `Hanabi 3x3`)**:
   In `Cat & Dog` (introduced in Off-Belief Learning, [arXiv:2103.04000](https://arxiv.org/abs/2103.04000)), Alice sees whether the hidden pet is a cat or a dog. She can pay a small cost (`-5`) to remove the barrier so Bob sees the pet directly for a guaranteed net reward (`+5`), or she can send a free binary signal (`light on` or `light off`) and hope Bob guesses right (`+10` on match, `-10` on mismatch). Baseline LLMs repeatedly refuse to pay the `-5` observability cost and instead gamble on unstated conventions (`light on = cat` vs. `light on = dog`), rationalizing their own mapping as "natural". In `Hanabi 3x3`, models similarly collide between Gricean implicature (`Good Touch` mutual exclusivity) and literal card-hint interpretation.
2. **Symmetric role deadlock or collision (`Narrow Tunnel`, `Brittle Bridge`, `Permuted Levers`)**:
   When two agents receive symmetric instructions in a resource-contention or turn-taking setting, they lack an equivariance-breaking rule (Other-Play, [arXiv:2003.02979](https://arxiv.org/abs/2003.02979)). Both agents either yield forever (reproducing the real-world autonomous vehicle narrow-tunnel deadlock) or claim the same slot simultaneously.
3. **Lexicographic, positional, and locale fragility (`Code Agents`, `Hund < Katze`)**:
   When asked to write executable policy code (`Code Agents`) or deterministic scripts, LLMs frequently invent lexicographic or array-index tie-breakers (for example, sorting action labels alphabetically so `"cat" < "dog"` maps to `0`). As Treutlein et al. ([arXiv:2106.06613](https://arxiv.org/abs/2106.06613)) and Hayler et al. ([arXiv:2611.06409](https://arxiv.org/abs/2611.06409)) show, translating the same task into German (`"Hund" < "Katze"`) or permuting JSON list order inverts the policy and causes immediate cross-play failure.
4. **Competing surface semantics vs. structural payoff (`Semantic Selection Game`, `Semantic Convention Game`)**:
   Building on Ma et al. ([arXiv:2305.12609](https://arxiv.org/abs/2305.12609)), Hayler et al. test games where a focal semantic label (such as a `"big red arrow"` pointing to a `1.00` lever) competes with an unlabelled higher-payoff option (`1.01`). Model families split sharply: some models always coordinate on the vivid semantic cue, while others always optimize the numeric payoff, causing severe `XP_LLM` drops whenever a skill's examples or prose metaphors point away from its formal rule.

## 3. Reasoning scaling and Coordination-Friendly Definitions (CFDs)

Increasing single-agent reasoning effort without a coordination constraint often **degrades** cross-play (`XP_LLM`). Deeper chain-of-thought lets a model construct more elaborate, self-consistent justifications for an arbitrary convention that a partner model does not share.

Hayler et al. ([arXiv:2611.06409](https://arxiv.org/abs/2611.06409)) address this with two mechanisms:

- **Hand-crafted and meta-learned CFDs**:
  - The *hand-crafted CFD* forbids policies that assume an arbitrary signaling convention (where another mapping would work equally well) or a symmetric role assignment that could be flipped.
  - The *meta-learned CFD*, discovered via `ParetoEvolution` (adapted from GEPA, [arXiv:2507.19457](https://arxiv.org/abs/2507.19457)) on a training suite of ZSC games, states:
    > "Prefer actions that would still be reasonable under several plausible partner interpretations of the shared observation, and avoid actions that are good only if a partner infers one specific unstated rationale."
- **Separation of policy generation and temperature-0 `Policy Critic`**:
  Instead of trusting an agent's single-pass self-report, the architecture pairs the actor with a separate temperature-0 critic that checks whether the proposed action or code violates the CFD before execution, retrying up to $M$ times with structured critique. Across held-out test games, the meta-learned CFD + critic raises `XP_LLM` from `4.90` to `8.25` for text agents and from `3.21` to `7.54` for code agents.

## 4. How Sage Protocol combines zero-shot CFD robustness with governed conventions

Hayler et al. identify a fundamental tension between **over-coordination** (assuming unshared conventions that break in cross-play) and **under-coordination** (refusing to use conventions at all when a complex task requires one). Sage Protocol resolves this tension across two layers:

1. **Zero-shot CFD layer (when no shared convention is guaranteed)**:
   When agents interact across unaligned harnesses, ad-hoc subagent dispatches, or cold-start channels, skills enforce the CFD baseline. Agents pay the `"remove the wall"` cost upfront by emitting explicit schemas, running preflight reads, using observable asymmetric tie-breakers, and abstaining when attribution is ambiguous (`sage-conservative-skill-refinement`, [arXiv:2604.08377](https://arxiv.org/abs/2604.08377)).
2. **Governed stigmergic convention layer (when high-leverage conventions are needed)**:
   Rather than forcing agents to guess conventions at runtime, Sage turns conventions into explicit, content-addressed (CID-pinned), versioned skills and behaviors (`Bredell et al.`, [arXiv:2412.06333](https://arxiv.org/abs/2412.06333)). Agents inspect which library version and skill hash are active (`sage library active --format json`), coordinate through durable stigmergic artifacts (`sage-coordination-cold-start`), and record multi-harness outcome telemetry (`sage suggest feedback` and `evaluate_example_robust` in `crates/core/src/skill/example_gate.rs`).

## 5. Primary references

- Hayler, A., Chirra, S. R., Lupu, A., Forkel, J., Sarkar, B., Feng, S., and Foerster, J. (2026). *Zero-Shot Coordination among LLM Agents*. NeurIPS 2026. Paper: https://arxiv.org/abs/2611.06409 | Code: https://github.com/ahayler/zsc-llm-agents
- Hu, H., Lerer, A., Peysakhovich, A., and Foerster, J. (2020). *Other-Play for Zero-Shot Coordination*. ICML 2020. https://arxiv.org/abs/2003.02979
- Hu, H., Lerer, A., Cui, B., Peysakhovich, A., and Foerster, J. (2021). *Off-Belief Learning*. ICML 2021. https://arxiv.org/abs/2103.04000
- Treutlein, J., Dennis, M., Oesterheld, C., and Foerster, J. (2021). *A New Formalism, Method and Open Issues for Zero-Shot Coordination*. ICML 2021. https://arxiv.org/abs/2106.06613
- Ma, R., Lerer, A., Foerster, J., and Wu, M. (2023). *Learning Intuitive Policies Using Action-Semantic Relationships*. https://arxiv.org/abs/2305.12609
- Bredell, G., et al. (2024). *Augmenting the Action Space with Conventions to Improve Multi-Agent Cooperation*. https://arxiv.org/abs/2412.06333
- Agrawal, L. A., et al. (2025/2026). *GEPA: Reflective Prompt Evolution Can Outperform Reinforcement Learning*. https://arxiv.org/abs/2507.19457
- SkillClaw (2026). *Conservative Skill Refinement*. Paper: https://arxiv.org/abs/2604.08377 | Code: https://github.com/AMAP-ML/SkillClaw
