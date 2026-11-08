---
name: sage-fleet-ops
description: "Pair Sage fleet nodes, grant or revoke a node's complete capability set, and run fleet session, host, approval, and audit commands over the authenticated plane."
tags:
  - sage-protocol
  - fleet
  - fleet-nodes
  - node-pairing
  - pair a new fleet node
  - capabilities
  - grant
  - revoke
  - node-id
  - sessions
  - hosts
  - audit
metadata:
  tags: [sage-protocol, fleet, fleet-nodes, node-pairing, pair a new fleet node, capabilities, grant, revoke, node-id, sessions, hosts, audit]
examples:
  default:
    - input: pair a new fleet node
      output: 'pair invite on one machine; pair connect <ENDPOINT> --secret-stdin on the other; compare the six-digit code out of band; pair confirm <PENDING_ID> --code <CODE> on each.'
      kind: pass
      provenance:
        source: curated
    - input: which capabilities can I grant a fleet node
      output: 'The twelve values in sage fleet nodes grant --help; read sage fleet nodes show <node-id> first, because grant replaces the complete set.'
      kind: pass
      provenance:
        source: curated
sage-inline-sidecars: false
---

# sage-fleet-ops

Use when pairing a new fleet node, asking which capabilities a node can hold,
revoking a node, or planning, starting, or stopping a fleet session. Pairing
proves identity and grants nothing; a grant replaces the node's complete
capability set. Not for wallet approvals and votes (`sage-wallet-ops`), Buzz
agent fleets, or peer library sync (`sage-p2p`). Use the paired-release CLI:
where an npm `@sage-protocol/cli` wrapper is also installed, `which -a sage`
can list that older build first, and it lacks these verbs.

## Task-specific instructions

Open the relevant section of [references/task-guide.md](references/task-guide.md)
before that operation, not the full guide for unrelated work. Sections cover:
Pair a node; Capabilities and grants; Sessions, hosts, approvals, audit.
Existing references linked there retain their own scope and exact command contracts.

## Authority and completion

The task defines scope. Continue authorized local reads and disposable checks without
asking again at each step. Stop only at a missing input or a real authority boundary.
No skill grants permission to sign, pay, publish, alter shared/governed state, or
expand credentials. Pairing, grants, revokes, path exposure, and session start change
what another machine may do here: each needs the operator's explicit approval of the
exact change. Preserve relevant previews and verify authoritative state after writes
(re-read the node or session). Report what was verified and any remaining blocker.
