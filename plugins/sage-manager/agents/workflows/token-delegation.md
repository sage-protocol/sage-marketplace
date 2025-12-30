<objective>
Manage SXXX tokens: check balances, delegate voting power, approve spending, and request testnet tokens.
</objective>

<command_reference>
```
# Token operations
sage sxxx info                                        # Token metadata
sage sxxx stats                                       # Comprehensive stats
sage sxxx balance [address]                           # Check balance
sage sxxx delegation [address]                        # Check delegation status
sage sxxx votes [address]                             # Alias for delegation
sage sxxx delegate-self                               # Delegate to yourself (you vote)
sage sxxx delegate <address> --confirm                # Delegate to representative (they vote for you)
sage sxxx approve <spender> <amount>                  # Approve spending
sage sxxx approve-gov <amount>                        # Approve for Governor
sage sxxx allowance <owner> <spender>                 # Check allowance
sage sxxx ensure-allowance <spender> <amount> -y      # Check + approve if needed
sage sxxx ensure-allowance-gov <amount> -y            # Same for Governor
sage sxxx transfer <to> <amount>                      # Transfer tokens
sage sxxx faucet                                      # Testnet tokens (Base Sepolia)

# Governance helpers
sage governance self-delegate                         # Delegate SXXX voting power to self
sage governance preflight --subdao 0x...              # Full proposer readiness diagnostics
```

**Notes:**
- Prefer `--subdao` (or `--gov`) for governance context; some commands use `--dao` instead (check `--help`).
- Use `-y` to skip confirmations
- Most commands accept saved aliases for `--subdao` / `--library` (after `sage dao save ... --alias name`).
</command_reference>

<voting_power_model>
SXXX uses ERC20Votes (checkpointed voting):

1. **Hold tokens** - Own SXXX tokens
2. **Delegate** - Assign voting power (to self or others)
3. **Vote** - Use delegated voting power on proposals

Without delegation, tokens have no voting power even if held.
</voting_power_model>

<process>
**Step 1: Check token info**
```bash
# Basic metadata
sage sxxx info

# Comprehensive stats
sage sxxx stats
```

**Step 2: Check your balance**
```bash
sage sxxx balance
```

**Step 3: Delegate voting power to yourself**
```bash
sage sxxx delegate-self
```

This is required to vote. Without self-delegation, your tokens have no voting power. Community (token-governed) DAOs also require a minimum effective voting power to vote (`minVotesToVote`, default **1 SXXX**).

**Step 4: Check delegation status**
```bash
# Your delegation
sage sxxx delegation

# Another address
sage sxxx delegation 0x...
```

**Step 5: Approve tokens for spending**
```bash
# Approve for any spender
sage sxxx approve 0xSpender 1000

# Some flows may provide helpers for common spenders
sage sxxx approve-gov 1000
```

**Step 6: Ensure allowance (guided flow)**
```bash
# Check and approve if needed
sage sxxx ensure-allowance 0xSpender 500

# Some flows may provide helpers for common spenders
sage sxxx ensure-allowance-gov 500
```

**Step 7: Transfer tokens**
```bash
sage sxxx transfer 0xRecipient 100
```

**Step 8: Get testnet tokens (Base Sepolia only)**
```bash
sage sxxx faucet
```
</process>

<delegation_patterns>
**Self-delegation (most common):**
```bash
sage sxxx delegate-self              # You control your voting power
sage governance self-delegate        # Convenience wrapper (same effect)
```
You vote with your own tokens.

**Delegate to a representative:**
```bash
# Check who you currently delegate to
sage sxxx delegation

# Delegate to someone you trust to vote on your behalf
sage sxxx delegate 0xAlice --confirm
# OR with -y to skip confirmation
sage sxxx delegate 0xAlice -y
```
They will vote using your tokens' voting power.

**Undelegate (take back voting power):**
```bash
# To stop delegating to someone else and vote yourself again:
sage sxxx delegate-self
```
This is how you "undelegate" - by delegating back to yourself.

**Check voting power before proposal:**
```bash
# Ensure you have voting power on SXXX
sage sxxx delegation
# If it shows "Not delegated", run:
sage sxxx delegate-self

# If the DAO uses an NFT multiplier wrapper, delegate on the base token (SXXX), not the wrapper.
sage sxxx delegate-self
```
</delegation_patterns>

<allowance_management>
Before operations requiring token spend:

```bash
# Check existing allowance
sage sxxx allowance 0xYourAddress 0xSpender

# If insufficient, approve
sage sxxx approve 0xSpender 1000

# Or use guided flow
sage sxxx ensure-allowance 0xSpender 1000 -y
```

Common spenders needing approval:
- Bounty system (for reward funding)
- Premium purchase contracts (USDC approvals)
- Paid pinning (USDC approvals)

Note: Governance proposing/voting does not require ERC20 allowances.
</allowance_management>

<governance_participation>
**Governance participation (threshold model):**

Token-governed DAOs use ERC20Votes on SXXX (no staking - just hold + delegate):
- **Hold SXXX**
- **Delegate voting power** (usually to yourself)
- Meet DAO gates:
  - **Voting**: `minVotesToVote` (default 1 SXXX)
  - **Proposing**: `proposalThreshold`

```bash
# Detect governance profile + thresholds
sage governance diag --subdao 0x...

# Delegate voting power (required for ERC20Votes)
sage sxxx delegate-self

# Readiness checks
sage governance preflight --subdao 0x... --action vote
sage governance preflight --subdao 0x... --action propose
```

Council-only / operator DAOs do not use token voting; follow the council/timelock execution workflow instead.
</governance_participation>

<success_criteria>
- [ ] Governance profile checked (`sage governance diag`)
- [ ] Token balance checked
- [ ] Voting power delegated (to self or representative)
- [ ] Allowances set for required contracts
- [ ] Faucet used for testnet tokens (if applicable)
- [ ] Vote/propose gates satisfied (`minVotesToVote`, `proposalThreshold`)
- [ ] `sage governance preflight` passes for the target SubDAO
</success_criteria>
