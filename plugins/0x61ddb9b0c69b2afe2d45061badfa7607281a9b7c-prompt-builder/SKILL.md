---
name: prompt-builder
version: "1.0.0"
description: >
  Builds Sage prompts, skills, and behaviors through search-first reuse and
  structured composition. USE WHEN creating a new prompt pack, refining an
  existing one, or wiring multiple skills into a reusable behavior. DON'T USE
  WHEN the task is simple Sage discovery (`sage-discover-adopt-skill`),
  operational execution (`sage-workflow`), or a one-off answer that should not
  become a reusable asset.
tags:
  - prompts
  - behaviors
  - methodology
  - sage-protocol
  - library
  - workflow
metadata:
  tags: [prompts, behaviors, methodology, sage-protocol, library, workflow]
author: sage-protocol
references:
  - references/layer-architecture.md
  - references/behavior-schema.md
---

# Prompt Builder

## Overview

Use this skill when a task should become a reusable Sage asset instead of a one-off instruction blob.
The goal is simple: search first, reuse what already exists, create only the missing pieces, and package the result so it can be installed, activated, or governed later.

## When to Use

Use this skill when you need to:

- build a new prompt, skill, or behavior for Sage
- improve or refactor an existing prompt pack
- combine multiple skills into a behavior workflow
- turn repeated session guidance into something reusable and shareable
- decide whether something should be inline text, a skill, or a behavior-backed library entry

## When NOT to Use

Do not use this skill when:

- the user only needs ordinary Sage discovery and the correct skill is `sage`
- the user needs a safe operational procedure and the correct skill is `sage-workflow`
- the task is a one-off answer that does not need to become a reusable asset
- the correct next step is inspecting or activating an existing skill rather than authoring a new one

## Workflow

### 1. Classify the request

First decide whether you are building a reusable Sage asset at all:

- **no asset / direct session answer** — the request is genuinely one-off and should just be answered
- **inline prompt** — a single reusable directive that is still self-contained
- **skill** — installed guidance for a recurring task pattern
- **behavior** — an executable multi-skill workflow that composes existing skills

Classification cues:

- if the user only needs a one-off answer for this session, default to **no asset / direct session answer**
- if the user explicitly says “just for this session,” “one-off,” or otherwise rejects packaging, do **not** escalate to an inline prompt, skill, or behavior unless they separately ask to save it for reuse
- repeated onboarding or cross-session guidance usually defaults to a **skill**
- a request to chain existing skills in order should default to a **behavior**, not a monolithic inline prompt
- only choose an **inline prompt** when the content is self-contained and still likely to see light reuse

State the classification explicitly and explain why that packaging fits better than the other options, especially when choosing **no asset** over packaging.

If the correct classification is **no asset / direct session answer**, stop the packaging workflow there and answer the user directly. Do not search for, draft, or create reusable Sage assets just to satisfy process.

If unclear, ask the smallest clarifying question that distinguishes these.

### 2. Search before writing

If and only if you are actually building or revising a reusable asset, exhaust Sage-native search first.

```json
{ "domain": "skills", "action": "search", "params": { "query": "<intent>" } }
{ "domain": "prompts", "action": "search", "params": { "query": "<intent>" } }
{ "domain": "builder", "action": "recommend", "params": { "intent": "<intent>" } }
```

CLI routing equivalents:

```bash
sage search "<intent>" --search-type skills --scope both
sage skill discover "<intent>"        # installable GitHub-backed skills (daemon-backed)
sage skill list --all --format json
sage suggest skill "<intent>" --format json
sage behavior recommend "<intent>" --format json
```

## Discover more

Before authoring a new skill, search Sage for something reusable instead of reinventing it:

- `sage search "<intent>" --search-type skills --scope both` — installed + Sage Protocol skills
- `sage skill discover "<intent>"` — installable GitHub-backed skills, each with a `sage skill add github:<repo>` install hint
- `sage search "<intent>" --search-type libraries` — curated libraries to adopt
- `sage library select activate <library>` — activate a library so its skills are usable

Use `sage search` for broad discovery. Use `sage suggest skill` only when you
want active-library runtime suggestions, and inspect `entryKind` because the
historical command name can return `skill`, `prompt`, or `behavior` entries.
Use `sage behavior recommend` when you specifically want behavior-only workflow
candidates. Do not invent a separate route alias.

If something relevant exists, inspect it before creating anything new.

```json
{ "domain": "skills", "action": "get", "params": { "key": "<key>" } }
{ "domain": "prompts", "action": "get", "params": { "key": "<key>" } }
```

Do not jump straight into drafting new text. First say what you plan to search, what you found, and whether the best next move is reuse, extension, or net-new creation.

### 3. Reuse before inventing

For every capability the asset needs:

- if it already exists in a skill or prompt, reference it
- if it almost exists, refine or extend it
- only create new content for the real gap

For behaviors, prefer wiring existing skills rather than duplicating their bodies.

### 4. Decide the packaging level

Use this rule:

- **no asset / direct session answer** when the task is truly session-bound, one-off, or not worth storing as a reusable Sage asset
- **inline prompt** when the task is self-contained and likely to see light future reuse, but does not justify a full skill
- **skill** when the guidance should be reusable across sessions or harnesses
- **behavior** when the workflow depends on multiple skills executed in sequence

If the user says they keep repeating the same guidance across sessions, bias toward a **skill** first, not a fresh inline prompt.
If the user says they only need an answer right now, bias toward **no asset / direct session answer** first, not speculative packaging “just in case.”
If the user says they need a reusable workflow that chains existing skills, bias toward a **behavior** that references those skills instead of duplicating them in one large prompt.

Always explain the packaging decision in terms of reuse, discoverability, and whether the asset is compositional or self-contained.

### 5. Keep behavior dependencies resolvable

When creating a behavior:

- keep the skill list focused
- mark optional skills explicitly
- make sure every required skill is resolvable from the same library, a declared
  dependency, or the active-library scope used by the caller
- if a missing skill is essential, materialize it rather than leaving a dangling placeholder
- if a referenced skill cannot be found yet, say so explicitly and make the next step either search for an alternative or create the missing skill before finalizing the behavior
- do not assume globally exposed IDE skills satisfy behavior resolution; for a
  self-contained behavior library, import component skills explicitly with
  `sage library skill add --key <skill> --library <library>` before validation
- remember that optional skills can still add MCP requirements; if an example
  behavior should run with no extra MCP servers, avoid optional skills that
  require unavailable servers or validate/run with `--available-mcp <server>`
  and document that requirement
- remember that behaviors are library manifest entries. They can later be
  promoted as part of a DAO-governed library, but the behavior graph is
  manifest/IPFS content, not direct on-chain graph state.
- preserve provenance by referencing existing skills instead of copying their
  bodies; this keeps component prompts/skills visible as artifacts that can be
  discovered, improved, funded with bounties, tipped, demoed, or promoted.

Use the first-class behavior lifecycle commands instead of hand-editing ordinary
prompt entries when possible:

```bash
sage behavior recommend "review this implementation plan" --format json
sage behavior create implementation-plan-review \
  --library sage-entrypoints \
  --skill critique --skill audit --skill confidence-calibration \
  --description "Review implementation plans with critique, audit, and confidence calibration"
sage behavior validate implementation-plan-review --library sage-entrypoints --format json
sage behavior run --intent audit --library sage-entrypoints --format json
sage behavior run implementation-plan-review --library sage-entrypoints --format json
```

If validation reports missing required skills, fix the library contents before
changing the behavior text:

```bash
sage library skill add --key critique --library sage-entrypoints
sage library skill add --key audit --library sage-entrypoints
sage behavior validate implementation-plan-review --library sage-entrypoints --format json
```

Remember: `behavior run` returns `output: "controller_plan"`, the execution
contract used by Sage-aware harness executors to coordinate the resolved skill
steps. Use `--intent <text>` for short single-token intents; a bare single token
is an explicit behavior key unless `--fallback-intent` is passed.

### 6. Validate the result

Before finishing, check:

- if this stayed a direct session answer, was over-packaging avoided on purpose?
- if this became an asset, can someone discover it from intent?
- does it reuse existing assets instead of duplicating them?
- is it packaged at the right level?
- if it is a behavior, do the dependencies make sense in execution order?
- if this is a skill being authored or revised, is there a plan to record execution outcomes (`sage suggest feedback outcome <key> --status passed|failed|revised`; unknown keys are refused with a non-zero exit, so record under the skill's exact key) so future improvements are evidence-based, not subjective?
- did you give the user the right next step for the chosen level, whether that is a direct answer, a search to run, or an asset to inspect next?

## Common Rationalizations

| Rationalization | Reality |
|---|---|
| “It’s faster to just write a fresh prompt.” | Fresh text is often duplicated effort; Sage gets better when reusable pieces are discovered and reused. |
| “I can inline the whole workflow.” | If the task depends on multiple reusable steps, a behavior should reference skills rather than duplicate them. |
| “I don’t need to inspect existing results.” | Search results tell you that something exists, not whether it is the right fit. |
| “I’ll leave the missing skill unresolved for now.” | A behavior with unresolved required skills is not actually ready to use. |
| “This is too small to package.” | Repeated session guidance is exactly what should become a reusable Sage asset. |
| “We should package this anyway just in case.” | One-off answers should usually stay as direct session responses; unnecessary packaging creates clutter and false reuse signals. |

## Red Flags

- writing new content before searching Sage-native sources
- duplicating a skill or prompt that already exists
- creating a behavior whose required skills do not resolve
- packing too much into one monolithic prompt when the better structure is behavior + skills
- producing a result that cannot be discovered or reused later

## Verification

Before finishing, confirm:

- [ ] the request was classified as no asset, inline prompt, skill, or behavior
- [ ] no-asset responses did not trigger reusable-asset process steps unnecessarily
- [ ] Sage-native search happened before writing new content
- [ ] existing assets were reused where possible
- [ ] any new content fills a real gap rather than duplicating an existing asset
- [ ] packaging level is correct for the task
- [ ] behavior dependencies are resolvable and logically ordered when applicable
