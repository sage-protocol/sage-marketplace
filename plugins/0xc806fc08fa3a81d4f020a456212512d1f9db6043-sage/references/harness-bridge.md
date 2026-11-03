# Harness bridge routing

This is explanatory bridge guidance, not a separate top-level skill. Use it when the question is how Sage should be loaded or repaired in a specific agent harness.

## First-contact surface by harness

- **Claude Code**: init-installed `sage` skill plus Sage MCP server and hook-managed suggestions. Plugin-bundled Claude skills may add setup-specific guidance; avoid two router-shaped active skills in the same harness.
- **Codex**: init-installed rendered Codex `sage` skill and onboarding. Codex may not load sibling references automatically, so the router names files explicitly.
- **Pi**: init-installed rendered Pi `sage` skill and code-mode wrappers (`sage_search`, `sage_execute`, `sage_status`). Pi has no Sage hook system; use manual `sage suggest skill` / `sage behavior recommend` equivalents.
- **OpenClaw**: init-installed skill plus SOUL/context posture and optional plugin hooks.
- **Hermes**: init-installed skill plus registered external skills dir and SOUL/context posture.
- **Cursor, Crush, OpenCode, Droid**: receive the same multi-file install bundle when `sage init` detects them; harness-specific behavior guidance is deferred until there is a real divergence.

## Repair routing

Use existing commands and skills; do not invent a bridge status command.

1. If Sage commands/tools are missing or stale, run `sage doctor --include-details` and load `sage-runtime-preflight` when available.
2. If generated onboarding or skills are stale, rerun `sage init`; this is the canonical post-upgrade repair trigger for bundled skill files and references. Re-running `sage init` is now safer for OpenCode because existing OpenCode config is preserved rather than overwritten.
3. If daemon-backed writes are failing, compare `sage wallet current` with `sage daemon status`.
4. If MCP/tool availability is unclear, check `sage mcp hub status`, `sage_status({})`, or raw MCP `hub_status` depending on the host.
5. If the issue is adopt-vs-create-vs-search behavior, hand off to `sage-discover-adopt-skill` rather than duplicating that runbook here.

Common stale symptoms: old `sage skill get` examples, missing `entryKind` branching, missing `references/*` files next to `SKILL.md`, stale wallet guidance that lacks OWS first, or public/private guidance that treats install/expose as publish.
