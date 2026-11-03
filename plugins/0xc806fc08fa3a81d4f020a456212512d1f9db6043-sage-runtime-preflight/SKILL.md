---
name: sage-runtime-preflight
description: "Diagnose Sage CLI, daemon, hook, MCP, auth, or doctor failures (pending config migrations, deprecated delegation allowlist entries) before selecting a repair."
tags:
  - sage-protocol
  - runtime
  - setup
  - doctor
  - daemon
  - mcp
  - auth
  - config-migration
  - config_schema_migrations_pending
  - delegation-allowlist
  - doctor --fix
metadata:
  tags: [sage-protocol, runtime, setup, doctor, daemon, mcp, auth, config-migration, config_schema_migrations_pending, delegation-allowlist, doctor --fix]
sage-inline-sidecars: false
---

# sage-runtime-preflight

Start with the observed symptom and narrowest read. Run the broader diagnostic set only when the failing layer is unknown. Diagnose hooks, RPC, wallet auth, and binary drift separately. If `sage daemon status` hangs after a rebuild, treat it as a signing or keychain question for `sage-rebuild-reinstall`, not a daemon fault: inspect the resolved daemon binary and its signature, and do not restart, delete a socket, or re-sign merely because the read hangs. Do not kill processes, remove sockets, reinstall software, or reconnect credentials merely because a read failed. Continue safe diagnostics; request authority only for the needed repair.

## Task-specific instructions

Open the relevant section of [references/task-guide.md](references/task-guide.md) before that operation, not the full guide for unrelated work. Sections cover: Classify the blocker; MCP hub; hooks; read-RPC; smallest repair. Existing references linked there retain their own scope and exact command contracts.

## Wallet readiness is not spending approval

Before any signing flow, read `sage wallet status --format json` and inspect
`data.daemon.source`: `daemon` is a daemon-derived report, `legacy` is an older
daemon's compatibility projection, and `local` means live readiness is unknown.
A `signable` report is not spending approval and never authorizes secret access;
capability, network, amount, recipient, policy, and consent stay separate checks.

## Authority and completion

The task defines scope. Continue authorized local reads and disposable checks without
asking again at each step. Stop only at a missing input or a real authority boundary.
No skill grants permission to sign, pay, publish, alter shared/governed state, or
expand credentials. Preserve relevant previews and verify authoritative state after
writes. Report what was verified and any remaining blocker; do not force packaging,
feedback, or public participation into an unrelated task.
