# Public shared-commons onramp and bounty→canon integration

Lead with a useful capability, not governance mechanics. Governance is an earned
stewardship layer around demonstrated utility; bounties, x402 revenue, tips,
provenance, and reflections stay distinct and auditable forms of participation.

1. **Prove utility locally.** Search, inspect, use, and validate a skill,
   behavior, or coherent library before asking anyone to govern or pay for it.
2. **Prefer an existing commons.** Inspect comparable DAOs, their library
   streams, current bounties, and maintainers before creating another DAO:

   ```bash
   sage governance dao discover
   sage governance dao info <dao-address> --activity-limit 20 --json
   sage library discover --dao <dao-address> --format json
   sage bounties list --subdao <dao-address> --limit 50 --json
   sage governance dao council list --dao <dao-address> --json
   ```

   Treat recent wallets as leads for contextual inspection, not ranked trust.
   Use `sage agent info --address <wallet> --json` when one wallet's public
   governance/economic evidence is relevant. Preserve wallet-only attribution,
   coverage, and provenance.
3. **Join at the smallest useful scope, but establish voting power early.**
   `sage dao join <dao-address> --activate-library` syncs the primary library.
   Add `--self-delegate` before any proposal or competitive-bounty snapshot when
   the wallet may vote or submit. A later delegation cannot change a frozen
   snapshot.
4. **Fund a bounded gap, not generic participation.** Use `payment-only` when the
   deliverable should only be paid. Use `payment-and-add` only when the
   acceptance contract names the target stream, entry key, evidence, and
   integration review.
5. **Keep payment and canon acceptance separate.** Winner selection and payout do
   not update a manifest. A reviewer must inspect the winning artifact, update
   and validate the library, promote the exact manifest through the DAO's
   governance mode, and verify the public CID before marking a pending addition
   merged.
6. **Attribute only actual integration.** The indexed `fromBounty` contribution
   is created only when an exact pending `(DAO, stream, key, entry CID)` appears
   in a public manifest update. Winner selection alone does not qualify.
   Bounty-backed integration is not additionally scored as an
   accepted-contribution reflection reward; bounty completion remains the
   reward-bearing class.
7. **Keep the commons legible.** A free canon stream supports discovery and
   public benefit. A distinct x402 frontier may fund the treasury. Current DAO
   purchases pay the treasury; contributor distributions are separate governed
   treasury decisions, not automatic per-purchase splits.

## Bounty winner → governed canon, in order

pending addition → exact manifest integration/promotion → CID verification →
settlement.
