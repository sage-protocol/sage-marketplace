# Behavior Schema — Reference

## Overview

A "behavior" is a library entry of type `behavior` that references skills to
compose multi-step workflows. The Sage behavior engine auto-generates execution
plans from the declared skill dependencies.

## JSON Schema

### Minimal Behavior

```json
{
  "key": "my-behavior",
  "name": "My Behavior",
  "type": "behavior",
  "content": "High-level directive.",
  "behavior": {
    "skills": ["skill-a", "skill-b"]
  }
}
```

### Full Behavior

```json
{
  "key": "security-review",
  "name": "Security Review",
  "type": "behavior",
  "description": "Multi-skill security review workflow.",
  "content": "<role>\nYou are a senior security engineer.\n</role>\n\n<task>\nPerform a thorough security review.\n</task>\n\n<critical>\nNever skip static analysis.\nAlways report severity levels.\n</critical>",
  "tags": ["security", "workflow", "behavior"],
  "category": "security",
  "model": "claude-sonnet-4-20250514",
  "behavior": {
    "version": "1",
    "skills": [
      "tob-static-analysis",
      {
        "key": "tob-differential-review",
        "required": true,
        "alias": "review"
      },
      {
        "key": "tob-variant-analysis",
        "required": false,
        "alias": "variants"
      }
    ]
  },
  "mcp_servers": ["semgrep"],
  "extra": {}
}
```

## Skill Reference Formats

### String Shorthand

```json
"skills": ["skill-key"]
```

Equivalent to `{ "key": "skill-key", "required": true }`.

### Object Form

```json
"skills": [
  {
    "key": "skill-key",
    "required": true,
    "alias": "short-name"
  }
]
```

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `key` | string | required | Skill key to resolve |
| `required` | bool | `true` | Whether behavior fails if skill is missing |
| `alias` | string | none | Short name used in plan rendering |

## Resolution Algorithm

When a behavior is requested with expansion, skills are resolved in order:

1. **Active library prompts** with `type: "skill"` matching the key
2. **Installed skills** (on-disk SKILL.md files) matching the key
3. **All local library prompts** matching the key
4. **Missing** — skill could not be found

Resolution produces a `BehaviorResolved` with:
- `skills: Vec<ResolvedSkill>` — metadata for each referenced skill
- `missing: Vec<String>` — required skills that couldn't be found
- `mcp_servers_union: Vec<String>` — all MCP servers needed

## Expansion Modes

Controlled via the `expand` parameter on `get_prompt`:

| Mode | What It Returns |
|------|----------------|
| `behavior` | Parsed + normalized skill refs (`BehaviorSpec`) |
| `behaviorResolved` | Resolved skill metadata (`BehaviorResolved`) |
| `behaviorPlan` | Auto-generated execution plan + rendered Markdown |
| `behaviorSkillBodies` | Full skill content for each resolved skill |

### Usage via MCP

```json
{
  "tool": "get_prompt",
  "arguments": {
    "key": "security-review",
    "expand": ["behaviorPlan", "behaviorSkillBodies"]
  }
}
```

## Execution Plan Structure

Auto-generated from `BehaviorPlan::from_resolved()`:

```json
{
  "version": "1",
  "inputs": [
    { "name": "task", "description": "The task to perform", "required": true },
    { "name": "context", "description": "Additional context", "required": false }
  ],
  "steps": [
    {
      "id": "step-1",
      "title": "Static Analysis",
      "skill_key": "tob-static-analysis",
      "instruction": "Apply the Static Analysis skill: ...",
      "uses": [],
      "produces": ["output-1"]
    },
    {
      "id": "step-2",
      "title": "Differential Review",
      "skill_key": "tob-differential-review",
      "instruction": "Apply the Differential Review skill: ...",
      "uses": ["step-1"],
      "produces": ["output-2"]
    }
  ]
}
```

## Creating Behaviors Programmatically

### Via CLI

```bash
sage behavior create rust-review \
  --library my_library \
  --skill rust-style \
  --skill rust-error-handling \
  --optional-skill confidence-calibration \
  --description "Review Rust code with style and error-handling guidance"

sage behavior validate rust-review --library my_library --format json
sage behavior show rust-review --library my_library \
  --expand behaviorPlan --expand behaviorSkillBodies --format json
sage behavior run --intent audit --library my_library --format json
sage behavior run rust-review --library my_library --format json
```

`behavior run` returns `output: "controller_plan"`, the execution contract used
by Sage-aware harness executors to coordinate the resolved skill steps. A bare
single token is an explicit behavior key; use `--intent <text>` for short
single-token intents or `--fallback-intent` when explicit-key lookup should fall
back to intent search.
In recommendation JSON, `scores.relevanceLocality` is normalized to `0.0..1.0`
and `scores.routerScore` is an opaque router/debug score.

### Via MCP / code-mode action

```json
{
  "domain": "behaviors",
  "action": "show",
  "params": {
    "key": "rust-review",
    "library": "my_library",
    "expand": ["behaviorPlan", "behaviorSkillBodies"]
  }
}
```

### Via Library JSON

Edit the library manifest directly to add the `behavior` field:

```json
{
  "prompts": [
    {
      "key": "rust-review",
      "name": "Rust Code Review",
      "type": "behavior",
      "content": "...",
      "tags": ["rust", "behavior"],
      "behavior": {
        "skills": ["rust-style", "rust-error-handling"]
      }
    }
  ]
}
```

## Best Practices

1. **Keep behaviors focused** — 3-7 skills per behavior is ideal
2. **Order skills logically** — the plan chains them sequentially
3. **Mark optional skills** — use `required: false` for nice-to-have steps
4. **Include MCP servers** — declare servers the behavior needs beyond what skills declare
5. **Write good content** — the behavior's `content` field is the "overview" that frames the plan
6. **Use aliases** — for long skill keys that appear in rendered plans
7. **Test resolution** — use `sage behavior validate <key> --library <library> --format json`
8. **Version behaviors** — use the manifest `version` field when behavior evolves
