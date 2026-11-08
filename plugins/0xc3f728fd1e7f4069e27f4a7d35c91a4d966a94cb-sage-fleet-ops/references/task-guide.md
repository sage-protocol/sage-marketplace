# Task guide: sage-fleet-ops

Every shape below was read from the paired-release binary (`sage fleet ... --help`).
Reads (`list`, `show`, `pending`, `audit list`, `--help`) need no further authority.

## Pair a node

One machine issues the invitation, the other connects, and both confirm the same
six-digit code that each displays on its own.

```bash
sage fleet nodes pair invite [--listen 127.0.0.1:0] [--ttl-secs 600]    # prints ENDPOINT and a one-time secret
sage fleet nodes pair connect <ENDPOINT> --secret-stdin                  # other machine; secret on one stdin line
sage fleet nodes pair pending                                            # both: PENDING_ID and the six-digit code
sage fleet nodes pair confirm <PENDING_ID> --code <CODE> [--name <NAME>] # both, after comparing codes out of band
sage fleet nodes pair reject <PENDING_ID>                                # forget a pairing you did not confirm
```

Never place the invitation secret in a command argument, a report, or a chat
message. The invitation expires (600 s maximum). A confirmed node appears in
`sage fleet nodes list` with a stable `NodeId`; that id, not its display name,
is what every allowlist and grant keys on.

## Capabilities and grants

`sage fleet nodes show <node-id>` prints the node's complete executor-owned grant
set. `sage fleet nodes grant <node-id> --capability <c> [--capability <c> ...]`
replaces that set with exactly the listed values, so repeat every capability the
node keeps. Pass `--if-revision <n>` to fail if the executor policy revision moved
since you read it. Grantable values (`sage fleet nodes grant --help`):

| Capability | Lets the node |
|---|---|
| `fleet.inventory.read` | read this host's runtime and path inventory |
| `wallet.observation.read` | read wallet observation endpoints |
| `fleet.session.plan` / `.request` / `.approve` | plan, request, approve session plans |
| `fleet.session.attach` / `.signal` / `.stop` / `.logs.read` | attach to, signal, stop, and read logs of sessions |
| `fleet.audit.read` | read local security events |
| `wallet.delegation.request` / `.vote` | request wallet operations and vote on approvals (see `sage-wallet-ops`) |

Grants are default-deny per capability; an unknown value is refused, never
guessed. `sage fleet nodes revoke <node-id> --yes` removes the node and clears
its whole set; it is a destructive local trust change and needs explicit
authority. Read `sage fleet audit list` after any grant or revoke.

## Sessions, hosts, approvals, audit

- `sage fleet sessions plan --node <node-id> --runtime <template> --resource-profile <p> --egress-policy <e> --tool-policy <t>` resolves and persists an immutable plan and returns its digest. `sessions start <session-id> --plan-digest <digest> [--node <node-id>|--local] [--no-attach]` starts exactly that plan; `sessions list|show|attach|logs|stop` inspect and control it. The runtime is an executor-owned template id, never a command path.
- `sage fleet approvals list|show|approve` records authenticated local plan approvals.
- `sage fleet host bootstrap|verify|run|reconcile-receipts|recover-audit` configures and checks this machine as a Glove-backed execution host; `sage fleet runtimes list` and `sage fleet paths list|expose|revoke|inspect` administer what a host offers.
- `sage fleet audit list` shows fleet trust and policy events.

## Wallet delegation

`wallet.delegation.request` and `wallet.delegation.vote` are granted here but
governed in `sage-wallet-ops` (allowlist keyed by `node:<id>`, thresholds, the
approvals queue, and what `sage doctor --fix` migrates).
