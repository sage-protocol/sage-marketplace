# Voting power, delegation timing, and snapshot gates

ERC20Votes balances do not vote by themselves, and delegation only creates
checkpoints for future snapshots. Every rule below follows from that.

## Who must delegate, and by when

- **Governance voters** — delegate before the proposal voting snapshot. Safest
  is before proposal creation.
- **Competitive-bounty submitters** — must hold SXXX voting power *before bounty
  creation*, because the anti-spam submission floor is snapshot-locked then.
- **Bounty voters** — need voting power in the frozen `votePolicy.votesToken`
  before bounty creation. When that token differs from the configured SXXX
  token, first classify it by measured reads (the four kinds in the skill body).
  `--token` on a write must name a token that measured as ERC20Votes and whose
  deployed implementation is identified; never an adapter, and never an address
  known only from a getter:

  ```bash
  sage wallet delegate --check --token <votes-token>       # read; safe on adapters (delegates() may forward)
  sage wallet delegate --token <measured-erc20votes-token> # write; the resolved target only
  ```

  If the vote token cannot be classified, stop and report the address; an
  unclassified vote source is a blocker, not a delegation target, and staking
  is not a way to obtain it.

Verify the confirmed state before the snapshot-producing action, not after an
eligibility failure:

```bash
sage wallet delegate --check
sage wallet delegate
sage wallet delegate --check
```

Before creating a DAO's first proposal or competitive bounty, make sure every
wallet expected to vote or submit has delegated the correct token and received
an on-chain checkpoint. Adding SXXX or delegating after that snapshot is too
late.

If a contributor was not delegated before a competitive bounty was created, use
a legitimately eligible wallet or create a new bounty after delegation. The gate
is immutable; do not attempt to bypass it.

## Two different "delegate" surfaces

- `sage wallet delegate` — ERC20Votes voting power for governance
- `sage delegation ...` — scoped agent permissions, not voting power

## Per-DAO participation setup

```bash
sage dao join <dao-address>
sage dao join <dao-address> --activate-library
sage dao join <dao-address> --activate-library --self-delegate
```

Add `--self-delegate` whenever future proposal voting or competitive-bounty
participation is plausible. Do not add `dao stake` to this path. `sage governance
dao stake` only escrows SXXX into that DAO's receipt vault. It does not delegate
SXXX, change the governor's vote source, register membership, or grant a role.

## Symptom → fix

| Literal error / symptom | Fix |
|---|---|
| "Timelock operation is still Unset" right after queueing | Indexer lag, not a failed queue — re-run `sage governance proposals status <id> --dao <dao>` until it reflects the queued state |
| Vote rejected for zero voting power despite SXXX balance | ERC20Votes requires self-delegation — run `sage wallet delegate` once, verify with `sage wallet delegate --check` |
| Competitive bounty submission rejected despite current SXXX balance | The submission floor uses SXXX voting power frozen at bounty creation. Post-snapshot delegation cannot repair it; use a legitimately eligible non-creator wallet or replace the bounty after delegation |
| Bounty vote has zero power after delegating SXXX | Inspect `votePolicy.votesToken`; the frozen DAO vote token may differ. Delegation still had to exist before bounty creation |
| `delegate` on the vote source reverts (for example "Delegate directly on base token") | One adapter's revert string; classify by measured reads and the verified implementation, not the string. If the implementation is verified to require direct delegation on its underlying (for example Sage `MultipliedVotes`) and that underlying measured as ERC20Votes, write the delegation there and keep the adapter for `--check` reads only; otherwise stop |
| `name`/`symbol`/`decimals` revert on the governor's `token()` | Metadata is optional; this proves neither "not ERC20" nor "absent". Classify with `eth_getCode`, the deployed implementation, and the ERC20Votes/forwarding reads; never fund it, and compare governor thresholds in raw `getVotes` units rather than assuming decimals |
| `library discover` shows an empty manifest CID for a DAO collection | Read the stream nonce. Nonzero nonce with empty CID is a created stream awaiting its first pointer; zero nonce with no library id was never created. The registry rejects an empty CID on update |
| Receipt balance exists after `dao stake`, but voting power is unchanged | Expected. Staking is custody-only. Delegate the configured vote token before the relevant snapshot |
| `403 erc8004_required` when posting rationale to `global:agents` | Room requires ERC-8004 identity — `sage agent register`, or post in `dao:<addr>:proposal:<id>` instead |
| `403 not_authorized` from `set-price --dao` | The signer holds no publish authority yet; its `hint` points at `maintainer add`. Fix authority first, then price — see `council-and-x402.md` |
