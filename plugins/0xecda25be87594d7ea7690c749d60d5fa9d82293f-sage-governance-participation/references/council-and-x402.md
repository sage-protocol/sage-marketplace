# Council maintainers and x402 stream publishing

A public DAO does **not** require a pass. Pricing is an optional commerce layer
for one named stream — usually a separately maintained `frontier` — when
recurring access can fund the treasury without removing the free governed canon.
Price only after utility and upkeep needs are real; a DAO existing is not a
reason to make paid access the default.

Who may publish a DAO x402 stream (`set-price --dao`): a wallet with
`COUNCIL_ROLE` on the SubDAO, a Timelock governance role, or the DAO creator.
`COUNCIL_ROLE` is the maintainer role and works across all governance modes.

```bash
# 1. Publish the governed source first; this alone is public, not paid
sage library promote <local-library> --dao <dao-address> --collection frontier --dry-run
sage library promote <local-library> --dao <dao-address> --collection frontier

# 2. Confirm the active wallet can publish before pricing anything
sage governance dao authority --dao <dao-address> --json

# 3. Make an optional 30-day x402 stream pass available
sage marketplace library set-price --dao <dao-address> --collection frontier --price-usd 5 --json
sage marketplace library show dao:<dao-address>:frontier --json

# 4. Buyer explicitly purchases and verifies the entitlement
sage marketplace library buy dao:<dao-address>:frontier --x402
sage marketplace library entitlement dao:<dao-address>:frontier --json
sage marketplace library download dao:<dao-address>:frontier --output ./frontier.library.json

# 5. See current maintainers, then invite one (governed COUNCIL_ROLE change)
sage governance dao council list --dao <dao-address> --json
sage governance dao maintainer add <wallet> --dao <dao-address>
sage governance dao maintainer remove <wallet> --dao <dao-address>   # revoke when trust ends

# Stop new sales without changing the governed library itself
sage marketplace library unlist --dao <dao-address> --collection frontier

# Which DAOs does the active wallet already maintain?
sage governance dao council mine
```

## States that must stay distinct

- **public source** — promoted DAO stream; no pass implied
- **priced stream / pass available** — one stream has an active x402 listing
- **pass required** — a request to that priced endpoint returned HTTP 402 for a
  wallet without an active entitlement
- **pass active** — `entitlement --json` reports an `expiresAt` later than now;
  the fixed 30-day pass follows the moving stream head but grants no governance
- **encrypted** — separate Worker-KMS envelope/key-release configuration.
  Default pricing of a public snapshot is neither confidentiality nor DRM.

Keep a canon (free) stream and a frontier (priced) stream distinct: canon
establishes legitimacy and discovery; frontier may fund ongoing DAO upkeep.

## Authority, treasury, and provisioning

- DAO listing `payTo` resolves to the DAO treasury. It does not route to the
  council member who published the listing, and contributor allocation is a
  separate governed treasury decision.
- `maintainer add|remove` are governed changes, not instant writes. In a Council
  DAO a signer with Timelock proposer rights schedules the change directly;
  after the delay, resume with the printed `governance operator execute-timelock`
  command. Council-role signers without proposer rights, and Community DAOs, use
  the Governor propose → vote → queue → execute lifecycle.
- If `set-price --dao` returns 403 `not_authorized`, the signer holds no publish
  authority yet — the `hint` points at `maintainer add`. Fix authority, then price.
- **Council provisioning on Council-mode DAOs**: operator (timelock) authority
  and council authority are deliberately separate. A fresh operator DAO has an
  EMPTY council, and that is the expected state, not a deadlock — the operator's
  timelock roles (and DAO creatorship, honored by the Worker) already cover
  library/x402 publishing. Seat council members through the canonical path:
  `maintainer add` from a Timelock-proposer signer schedules
  `grantRole(COUNCIL_ROLE, ...)` on the timelock and executes after the min
  delay, or pass `--council <address>` on `dao create` to schedule the first seat
  in the same run.
- **Rotation caveat**: revoking a wallet's timelock roles does *not* revoke its
  council seat — pair with `maintainer remove`.
- `dao council mine` is the cheap way to notice you can already publish somewhere
  before proposing new authority.
