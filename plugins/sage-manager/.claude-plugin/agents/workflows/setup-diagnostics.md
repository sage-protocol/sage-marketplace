<objective>
Set up CLI environment, configure wallets, manage governance context, and diagnose issues.
</objective>

<builtin_defaults>
**NPM Fresh Install (No .env Required)**

The CLI ships with built-in defaults for Base Sepolia. These work out of the box:

| Setting | Default Value |
|---------|---------------|
| `RPC_URL` | https://sepolia.base.org |
| `CHAIN_ID` | 84532 |
| `PRIVY_APP_ID` | cmfvc54l600dpl40cjqza7ccm |
| `SAGE_PRIVY_RELAY_URL` | https://app.sageprotocol.io |
| `SAGE_SUBGRAPH_URL` | Goldsky v1.0.5 |

```bash
# Verify built-in defaults work
sage doctor
sage dao info 0x61835539c76Ea4FfD5AcEFb7d2D62E876fdDf751
```

Only override if you need a different RPC or network.
</builtin_defaults>

<command_reference>
```
# CLI install
npm install -g @sage-protocol/cli
sage --version

# Wallet
sage wallet init                                      # Interactive setup
sage wallet doctor                                    # Diagnose issues
sage wallet connect --type <privy|cast|web3auth>
sage wallet list                                      # List accounts
sage wallet use <addressOrIndex>                      # Switch account
sage wallet current                                   # Show active wallet
sage wallet balance                                   # ETH balance
sage wallet import                                    # Import mnemonic/key
sage wallet sign <message>

# Privy-specific (relay is default; no localhost)
sage wallet connect-privy | create-privy | disconnect-privy | logout-privy
sage wallet connect-privy --local                     # Only if localhost OAuth is allowed
sage wallet privy-status

# DAO Context (recommended)
sage dao use <address>                                # Set working DAO (preferred)
sage dao save <address> --alias <name>                # Save DAO with alias
sage dao list                                         # List saved DAOs

# Context (alternative)
sage context init                                     # Initialize .sage/
sage context show                                     # Current context
sage context use <subdaoAddress>                      # Set governance context
sage context gov-set --subdao 0x... --governor 0x...
sage context gov-clear                               # Clear context
sage context audit                                    # Audit context + RPC
sage context profiles                                 # List saved profiles
sage context save <name> | restore <name>

# Config
sage config show                                      # Show configuration
sage config env                                       # Environment variables
sage config set-rpc <url> --chain-id <id>
sage config ai                                        # Configure AI provider
sage config ipfs                                      # Configure IPFS
```
</command_reference>

<initial_setup>
**Step 1: Initialize wallet**
```bash
# Interactive wallet setup
sage wallet init

# Recommended: Privy via web app relay (default)
sage wallet connect-privy

# Optional local OAuth (only if explicitly allowed)
sage wallet connect-privy --local
```

**Step 2: Verify wallet**
```bash
sage wallet doctor
```

Checks: wallet connection, RPC health, chainId, ETH balance.

**Step 3: Set governance context**
```bash
# Use a DAO as working context (recommended)
sage dao use 0xSubDAOAddress

# Or use context command
sage context use 0xSubDAOAddress

# Or set explicitly
sage context gov-set --subdao 0x... --governor 0x...
```

**Step 4: Verify context**
```bash
sage context show
```

Shows: Governor, SubDAO, Timelock, Registry addresses.

**Note:** `sage dao use` is preferred as it also derives Governor and Timelock addresses automatically.
</initial_setup>

<wallet_management>
**List available wallets:**
```bash
sage wallet list
```

**Switch active wallet:**
```bash
sage wallet use 0xAddress
# Or by index
sage wallet use 0
```

**Import new wallet:**
```bash
sage wallet import
```
Supports mnemonic or private key, stored encrypted.

**Check current wallet:**
```bash
sage wallet current
```

**Check balance:**
```bash
sage wallet balance
```

**Sign a message:**
```bash
sage wallet sign "message to sign"
```
</wallet_management>

<context_management>
**Save context profile:**
```bash
sage context save production
```

Saves current RPC/addresses for later.

**Restore profile:**
```bash
sage context restore production
```

**List profiles:**
```bash
sage context profiles
```

**Audit context:**
```bash
sage context audit
```

Checks governance context and RPC health.

**Clear context:**
```bash
sage context gov-clear
```

**View recent SubDAOs:**
```bash
sage context gov-history
```
</context_management>

<configuration>
**Set RPC URL:**
```bash
sage config set-rpc https://rpc.example.com --chain-id 84532
```

**Prefer SAGE_RPC_URL over RPC_URL:**
```bash
export SAGE_RPC_URL=https://base-sepolia.publicnode.com
```

**Configure AI provider:**
```bash
sage config ai
```

**Configure IPFS:**
```bash
sage config ipfs
```

**Show current config:**
```bash
sage config show
```

**Show environment variables:**
```bash
sage config env
```

**Export for shell:**
```bash
sage config env export
```
</configuration>

<diagnostics>
**Full system diagnostic:**
```bash
sage doctor
```

Checks: RPC health, chainId, workspace, Claude Code integration, contract addresses.

**Dual-CLI diagnostics (if scroll installed):**
```bash
# Check scroll status
scroll --version
scroll daemon status

# MCP hub status
scroll hub status

# If scroll MCP is registered, use MCP tools:
# - mcp__scroll__get_project_context → project state, wallet, libraries
# - mcp__scroll__hub_status → running MCP servers
```

**Component-specific diagnostics:**
```bash
sage nft doctor                       # NFT/multiplier config
sage bounty doctor                    # Bounty system config
sage auction status                   # Current auction state
sage contributor level                # Contributor staking level
```

**Context audit:**
```bash
sage context audit
```

Checks governance context and RPC health.

**Common issues:**

| Issue | Command | Solution |
|-------|---------|----------|
| No wallet | `wallet current` | `wallet connect --type privy` |
| Wrong network | `doctor` | `config set-rpc` |
| No context | `context show` | `context use 0x...` |
| No voting power | `sxxx delegation` | `sxxx delegate-self` |
| Low ETH | `wallet balance` | Fund wallet |
</diagnostics>
