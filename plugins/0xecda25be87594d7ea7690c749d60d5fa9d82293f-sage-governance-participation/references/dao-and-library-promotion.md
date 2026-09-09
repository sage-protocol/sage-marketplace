# DAO creation, promotion, and the proposal surface

## Creating the right DAO type

```bash
sage governance dao create --name "My Individual DAO" --description "..." --governance individual
sage governance dao create --name "Council DAO" --description "..." --governance council --operator 0x...
sage governance dao create --name "Community DAO" --description "..." --governance community --manifest-cid <cid>
```

- **community** creation can be seeded with `--manifest-cid`
- **individual/council** flows usually create first, then promote libraries after
  creation
- `--council <address>` on `dao create` schedules the first council seat in the
  same run (see `council-and-x402.md`)
- delegation must precede the first proposal or competitive bounty — see
  `voting-power-and-snapshots.md`

## Promote vs. proposal-create

Use `sage library promote` when the real job is governed library publication or
update:

```bash
sage library show <lib>
sage library promote <local-library> --dao <dao-address> --collection default --dry-run
sage library promote <local-library> --dao <dao-address> --collection default
```

For community-governed library updates, the explicit proposal surface may be the
right path:

```bash
sage governance proposals create --proposal-type library --dao <dao-address> --cid <cid> --library default "Update library"
```

## Behaviors are governed through the manifest

Behaviors follow the same path as prompts and skills: they live inside the
library manifest. A DAO governs the canonical behavior by governing the manifest
CID in `LibraryRegistry`; the behavior graph itself is not stored on-chain.

For behavior incentives, explain the governance/provenance surface honestly: the
DAO governs the canonical library version, referenced prompts and skills remain
visible artifacts, and bounties, tips, reflections, demos, chat rationale, and
governance discussion can target either the behavior workflow or the component
capabilities it composes.

## Timelock delay is normal, not breakage

Promotion executes on a timelock delay (24h on current deploys). `library
publish promote --auto` schedules the operation; keep the daemon running so it
auto-executes. Anything that depends on the promoted library — notably
`set-price` — fails before execution with `DAO library '<id>' was not found`.
That means wait, not that something broke. Confirm the library landed first:

```bash
sage governance dao discover <dao-address>
```

## Badges, multiplier levels, and the governance NFT auction

```bash
sage governance badge list --owner 0x... --json
sage governance badge show <badge-id> --json
sage governance multiplier status --owner 0x... --dao <dao-address> --json
sage governance multiplier tier <tier-id> --json
sage governance auction status --json
sage governance auction bid --amount 0.25 --yes --json
```

Direct badge and global multiplier writes are authority-gated:

```bash
sage governance badge mint --to 0x... --badge-id <id> --evidence-uri ipfs://... --dry-run --json
sage governance badge revoke --from 0x... --badge-id <id> --dry-run --json
sage governance badge set-minter --address 0x... --allowed true --dry-run --json
sage governance multiplier create-tier --dao <dao-address> --name "Steward" --multiplier 150 --max-supply 100 --price-wei 0 --dry-run --json
sage governance multiplier mint --to 0x... --tier-id <id> --token-uri ipfs://... --dry-run --json
```

For ordinary DAO-scoped tier creation and NFT awards, use proposal types
`multiplier-tier` and `multiplier-mint`. Those encode
`createTierViaGovernance` and `mintViaGovernance` for the DAO timelock. Bounty
badge recovery and configuration use the same authority-safe pattern:

```bash
sage governance proposals create --proposal-type bounty-retry-badge --dao <dao-address> --bounty-id <id> "Retry failed bounty badge" --dry-run
sage governance proposals create --proposal-type bounty-set-badge --dao <dao-address> --badge 0x... "Update bounty badge contract" --dry-run
```

The auction commands operate VotingMultiplierNFT inventory for ETH. They do not
sell library access or grant DAO membership.
