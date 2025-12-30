<objective>
Manage voting boosts: create incentives for governance participation, fund boost pools, and claim rebates.
</objective>

<command_reference>
```
sage boost create --proposal-id <id> --governor 0x... --per-voter <usdc> --max-voters <n> \
  [--kind direct|merkle|custom] [--policy 0x...] [--min-votes <n>] \
  [--payout-mode fixed|variable] [--support any|for] \
  [--start-at <unix>] [--expires-at <unix>] [--permit] -y

# per-voter uses 6 decimals (USDC): 1_000_000 = 1 USDC
# Total pool = per-voter × max-voters (USDC auto-approved to manager)
```
</command_reference>

<boost_types>
| Type | Description | Claiming |
|------|-------------|----------|
| **Direct** | Fixed amount per voter | Automatic |
| **Merkle** | Based on eligibility proof | Requires proof |
| **Custom** | Custom payout logic | Policy-dependent |
</boost_types>

<process>
**Step 1: Create a boost**
```bash
sage boost create \
  --proposal-id 1 \
  --governor 0x... \
  --per-voter 1000000 \
  --max-voters 100 \
  -y
```

Parameters:
- `--per-voter`: Amount per voter (in token decimals, e.g., 1000000 = 1 USDC)
- `--max-voters`: Maximum voters to incentivize
- Total pool = per-voter × max-voters

**Step 2: Fund the boost**
```bash
sage boost fund \
  --proposal-id 1 \
  --amount 10000000 \
  -y
```

**Step 3: Check boost status**
```bash
sage boost status --proposal-id 1 --governor 0x...
```

Shows: total pool, claimed amount, remaining, eligible voters.

**Step 4: Set Merkle root (for Merkle boosts)**
```bash
sage boost set-root \
  --proposal-id 1 \
  --root 0x... \
  -y
```

**Step 5: Claim boost rebate**
```bash
sage boost claim \
  --proposal-id 1 \
  --proof '["0x...","0x..."]' \
  -y
```

**Step 6: Finalize boost (admin)**
```bash
# Return unclaimed funds to creator
sage boost finalize --proposal-id 1 -y
```
</process>

<common_patterns>
```bash
# Create and fund in sequence
sage boost create --proposal-id 1 --per-voter 500000 --max-voters 50 -y && \
sage boost fund --proposal-id 1 --amount 25000000 -y

# Check if you can claim
sage boost status --proposal-id 1

# View all boosts for a governor
sage boost list --governor 0x...
```
</common_patterns>

<success_criteria>
- [ ] Boost created with appropriate incentive amount
- [ ] Pool funded with sufficient tokens
- [ ] Merkle root set (if Merkle type)
- [ ] Voters able to claim after voting
- [ ] Unclaimed funds returned via finalize
</success_criteria>
