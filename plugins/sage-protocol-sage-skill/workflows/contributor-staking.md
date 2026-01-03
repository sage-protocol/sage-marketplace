<objective>
Manage contributor staking: stake SXXX tokens to build contribution level, track tasks, and monitor reputation.
</objective>

<contributor_vs_governance>
**Important Distinction:**

| System | Purpose | Token Use | Contract |
|--------|---------|-----------|----------|
| **Contributor Staking** | Task eligibility, contribution levels | Stake SXXX (locked) | SimpleContributorSystem |
| **Governance Voting** | DAO voting power | Delegate SXXX (not locked) | Governor + SXXX token |

Contributor staking is **separate** from governance voting power:
- Staking locks tokens in the contributor system
- Delegation keeps tokens in your wallet but assigns voting power
- You can do both, but they serve different purposes

**When to stake:**
- You want to complete bounties/tasks requiring a minimum level
- You want to build on-chain reputation through completed work
- You want to access contributor-gated features

**When to delegate:**
- You want to vote on governance proposals
- You want voting power (or want to give it to a representative)
</contributor_vs_governance>

<command_reference>
```
# Diagnostics
sage contributor level                               # Check your contribution level
sage contributor level <address>                     # Check another address

# Staking
sage contributor stake <amount>                      # Stake SXXX tokens
sage contributor unstake <amount>                    # Unstake SXXX tokens

# Status & Tasks
sage contributor status [address]                    # Full profile (stake + badges + reputation)
sage contributor tasks [address]                     # View completed tasks
sage contributor list                                # List active contributors (requires indexing)

# Related commands
sage sxxx balance                                    # Check SXXX token balance
sage reputation check <address>                      # Full trust signal lookup
sage sbt doctor                                      # Diagnose badge/SBT configuration
```
</command_reference>

<contribution_levels>
Contribution levels are calculated from:

| Factor | Weight | Description |
|--------|--------|-------------|
| SXXX Staked | High | More tokens = higher level |
| Time Staked | Medium | Longer stake duration increases level |
| Completed Tasks | High | Each completed task adds to level |
| Recent Activity | Low | Active contributors get slight boost |

Levels unlock:
- **Level 1+**: Access to basic bounties
- **Level 3+**: Access to priority bounties
- **Level 5+**: Eligible for direct assignment bounties
- **Level 10+**: Trusted contributor status
</contribution_levels>

<process>
**Step 1: Check your current level**
```bash
sage contributor level
```

Shows: SXXX staked, time staked, completed tasks, activity status, contribution level.

**Step 2: Stake tokens to increase level**
```bash
# First check your SXXX balance
sage sxxx balance

# Stake tokens (approves and stakes in one transaction)
sage contributor stake 100
```

The CLI automatically approves the SXXX spending before staking.

**Step 3: Complete bounties to build reputation**
```bash
# Find available bounties
sage bounty list --subdao 0x...

# Claim and complete bounties
sage bounty claim --bounty-id <id> -y
sage bounty submit --bounty-id <id> --deliverable "ipfs://..." -y
```

Completed bounties increase your contribution level permanently.

**Step 4: View your full contributor status**
```bash
sage contributor status
```

Shows: staking info, badges, reputation signals, and recent activity.

**Step 5: Unstake when needed**
```bash
sage contributor unstake 50
```

Note: Unstaking reduces your contribution level proportionally.
</process>

<viewing_reputation>
The contributor system tracks:

1. **On-chain staking** (SimpleContributorSystem contract)
   - SXXX staked amount
   - Time staked
   - Completed tasks count
   - Active status

2. **Trust signals** (via subgraph)
   - Soulbound badges (SoulboundBadge contract)
   - Total contributions across DAOs
   - Badge evidence and timestamps

```bash
# Full status with both sources
sage contributor status

# Just on-chain contributor data
sage contributor level

# Just reputation/badges
sage reputation check <address>
```
</viewing_reputation>

<environment>
Required environment variables:
```bash
SIMPLE_CONTRIBUTOR_SYSTEM_ADDRESS=0x...    # SimpleContributorSystem contract
SXXX_TOKEN_ADDRESS=0x...                   # SXXX token for staking
SUBGRAPH_URL=https://...                   # For reputation lookup
```

Built-in defaults work for Base Sepolia. Override via `.env` or `sage config`.
</environment>

<success_criteria>
- [ ] Contribution level checked (`sage contributor level`)
- [ ] SXXX tokens staked (`sage contributor stake`)
- [ ] Tasks completed to build reputation
- [ ] Full status verified (`sage contributor status`)
</success_criteria>
