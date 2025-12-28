<objective>
Manage treasury assets: deposit tokens, schedule withdrawals, check balances and reserves.
</objective>

<command_reference>
```
# Read-only overview (uses configured treasury address, or resolve via --subdao)
sage treasury info [--subdao 0xSubDAO] [--json]                  # Display reserves, POL, pending
sage treasury balance [--subdao 0xSubDAO] [--json]               # Alias for info

# Deposits (requires signer)
sage treasury deposit <token> <amount> [--subdao 0xSubDAO] [--wrap] [--decimals <n>] [--json] -y

# Withdrawals (legacy queue flows; availability depends on deployed treasury implementation)
sage treasury withdraw schedule <token> <amount> <recipient> [--subdao 0xSubDAO] [--decimals <n>] -y
sage treasury withdraw confirm <id> [--subdao 0xSubDAO]
sage treasury withdraw cancel <id> [--subdao 0xSubDAO]

# Manual price overrides (legacy; availability depends on deployed treasury implementation)
sage treasury price override <token> <price> [--subdao 0xSubDAO] [--ttl <seconds>]
sage treasury price clear <token> [--subdao 0xSubDAO]
```
Token argument: ETH, WETH, USDC, SAGE, or 0xTokenAddress
</command_reference>

<process>
**Step 1: Check treasury status**
```bash
# Set DAO context once per session
sage dao use 0x...

# Then inspect treasury
sage treasury info
```

Shows: reserves, protocol-owned liquidity (POL), pending withdrawals.

**Step 2: Deposit assets**

Deposit ETH:
```bash
sage treasury deposit ETH 0.5
```

Deposit ERC20:
```bash
sage treasury deposit 0xTokenAddress 100
```

Deposit with wrap (ETH → WETH):
```bash
sage treasury deposit ETH 1.0 --wrap
```

**Step 3: Schedule withdrawals**

Withdrawals go through timelock for security:
```bash
sage treasury withdraw schedule 0xToken 50.0 0xRecipient
```

**Step 4: Manage price oracles**

Override price (for tokens without Chainlink):
```bash
sage treasury price override 0xToken 1.05 --ttl 3600
```

Tip: `sage treasury info` includes current manual overrides.
</process>

<common_patterns>
```bash
# Full treasury status
sage treasury info

# Treasury resolution by DAO (when you don't want to set context)
sage treasury info --subdao 0x...
```
</common_patterns>

<success_criteria>
- [ ] Treasury balance checked before operations
- [ ] Deposits confirmed on-chain
- [ ] Withdrawals scheduled through proper timelock
- [ ] Price overrides set with appropriate TTL
</success_criteria>
