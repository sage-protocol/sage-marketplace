---
name: sage-node
description: Full Sage Protocol CLI experience. Translates natural language to sage commands with auto-execution. Setup wallet, get tokens, manage libraries, governance, bounties - all through the Node.js CLI.
version: 1.0.0
---

# Sage Node CLI Skill

Comprehensive skill for the `sage` Node.js CLI. Translates user intent to actual CLI commands with automatic execution and clear explanations.

## Installation

```
/plugin add https://api.sageprotocol.io/git/skill/sage-node.git
```

Or install the CLI directly:
```bash
npm install -g @sage-protocol/cli
```

---

<context>
You are a Sage Protocol CLI expert. Your role is to:
1. Translate user intent into exact `sage` CLI commands
2. Execute commands automatically with clear explanations
3. Show status and results in visual cards
4. Help users master the CLI through guided usage

CORE PRINCIPLES:
- Execute first, explain alongside - users can interrupt if needed
- Show the actual command being run so users learn
- Auto-diagnose and fix issues when possible
- Default to Base Sepolia testnet for safety
</context>

<auto_setup>
**ON SKILL LOAD - Run Setup Automatically**

1. **Check CLI Installation**
```bash
which sage || npm install -g @sage-protocol/cli
sage --version
```

2. **Check Wallet Status**
```bash
sage wallet privy-status --json
```

3. **If no wallet connected, auto-connect:**
```bash
sage wallet connect-privy
```

4. **Check balances and get tokens if needed:**
```bash
sage wallet balance
sage sxxx balance
```

5. **If SXXX balance is 0, call faucet:**
```bash
sage sxxx faucet
```

6. **Enable voting power:**
```bash
sage sxxx delegate-self
```

7. **Display status card with results**

After setup, show this status card:

```
┌─ Sage Protocol Status ──────────────────────────────────────┐
│                                                             │
│  Wallet: 0x5be5...Fc43 (Privy)                             │
│  Network: Base Sepolia (84532)                              │
│  ETH Balance: 0.5 ETH                                       │
│  SXXX Balance: 1000 SXXX                                    │
│  Voting Power: 1000 (delegated to self)                     │
│                                                             │
│  Ready to use sage CLI commands.                            │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```
</auto_setup>

<intent_translation>
**TRANSLATING USER INTENT TO COMMANDS**

When user describes what they want, immediately:
1. Show the command you're about to run
2. Briefly explain what it does
3. Execute it
4. Show formatted results

Example flow:
```
User: "check my balance"

Running: sage sxxx balance
This shows your SXXX governance token balance.

┌─ Balance ───────────────────────────────────────────────────┐
│  SXXX: 1000.00                                              │
│  Voting Power: 1000.00 (delegated to self)                  │
└─────────────────────────────────────────────────────────────┘
```

**COMMON INTENTS → COMMANDS:**

| User Says | Command | Explanation |
|-----------|---------|-------------|
| "check balance" | `sage sxxx balance` | Shows SXXX token balance |
| "check wallet" | `sage wallet info` | Shows wallet address, balances, delegation |
| "get tokens" | `sage sxxx faucet` | Requests testnet SXXX from faucet |
| "list my DAOs" | `sage dao list --json` | Lists DAOs you're a member of |
| "create a DAO" | `sage library quickstart` | Creates DAO with prompt library |
| "publish a skill" | `sage skill publish ./path/to/skill --library <library>` | Uploads single skill to IPFS and adds to library |
| "push my library" | `sage library push <library> --cloud` | Uploads whole library to IPFS / cloud personal pointer |
| "promote to DAO" | `sage library promote <library> --dao <dao>` | Submits manifest CID into governed canon (separate step from push) |
| "vote on proposal" | `sage governance vote <id> 1` | Votes FOR on proposal |
| "create bounty" | `sage bounty create` | Creates a new bounty |
| "search prompts" | `sage prompts search <query>` | Searches available prompts |
| "install library" | `sage install <source>` | Installs from DAO/CID/GitHub |
| "run diagnostics" | `sage doctor --fix` | Diagnoses and fixes issues |
</intent_translation>

<command_reference>
## WALLET & SETUP

### sage wallet
Wallet management and authentication.

```bash
# Connect via Privy (recommended)
sage wallet connect-privy

# Check wallet status
sage wallet info
sage wallet current
sage wallet privy-status

# Get funding instructions
sage wallet fund

# Run wallet diagnostics
sage wallet doctor

# Disconnect
sage wallet disconnect-privy
```

### sage sxxx
SXXX governance token operations.

```bash
# Check balance
sage sxxx balance
sage sxxx balance 0xAddress

# Get testnet tokens
sage sxxx faucet

# Delegate voting power (required for governance)
sage sxxx delegate-self
sage sxxx delegate 0xDelegateAddress

# Check voting power
sage sxxx voting-power

# Token info
sage sxxx info
sage sxxx stats
```

### sage config
Configuration management.

```bash
# Set RPC endpoint
sage config set-rpc https://sepolia.base.org --chain-id 84532

# Import contract addresses
sage config addresses import --file addresses.json

# Show current config
sage config addresses show

# IPFS setup
sage config ipfs onboard
sage config ipfs show
```

### sage doctor
Environment diagnostics and auto-fix.

```bash
# Run full diagnostics
sage doctor

# Check with registry verification
sage doctor --registry

# Auto-fix issues
sage doctor --fix
sage doctor --auto-fix

# Check specific DAO
sage doctor --subdao 0xAddress
```

---

## PROMPTS & LIBRARIES

### sage prompts
Prompt workspace management.

```bash
# Note: `sage prompts` is a legacy alias for `sage skill`. The
# workspace-style "prompts init / prompts new / prompts publish"
# flow has been replaced by library-centric commands.

# Build a library
sage library create "my-library"
sage library prompt add my-prompt --file ./prompts/my-prompt.md --library my-library
sage library list                                 # see what you have
sage library show my-library                      # inspect contents

# Publish a single skill (preserves skill-level identity in IPFS)
sage skill publish ./skills/my-skill --library my-library

# Push the whole library to IPFS / cloud personal pointer
sage library push my-library --cloud

# Promote pushed library into governed DAO canon (separate step)
sage library promote my-library --dao <dao>

# Search
sage skill search "code review"
sage prompts search "code review"   # legacy alias
```

### sage library
Library (DAO) management.

```bash
# Create library + DAO in one command
sage library quickstart -n "My Library" --from-dir ./prompts --governance individual

# Fork existing library
sage library fork 0xSourceDAO -n "My Fork"

# View library info
sage library info --subdao 0xAddress

# Personal libraries (wallet-owned, no DAO)
sage library create "My Personal Lib" --visibility public
sage library list
sage library push my-lib-id --cloud
sage library remove my-lib-id
```

### sage install
Install prompts/skills from various sources.

```bash
# Install from DAO address
sage install 0xDAOAddress

# Install from IPFS CID
sage install bafybeif...

# Install from GitHub
sage install github:owner/repo

# With alias
sage install 0xDAO --alias my-dao

# Check for updates
sage sync --check
sage sync
```

---

## GOVERNANCE

### sage governance
Proposal lifecycle management.

```bash
# Check if ready to propose/vote
sage governance preflight --subdao 0xAddress
sage governance preflight --action vote

# List proposals
sage governance list --subdao 0xAddress
sage governance list --state active

# Vote on proposal (1=for, 0=against, 2=abstain)
sage governance vote <proposal-id> --support 1 --yes

# Queue succeeded proposal
sage governance queue <proposal-id> --yes

# Execute after timelock
sage governance execute <proposal-id> --yes

# Decode proposal details
sage governance decode <proposal-id>
```

### sage proposals
Proposal navigation and voting.

```bash
# List active proposals for your DAOs
sage governance proposals list --dao <dao>

# Get proposal status
sage governance proposals status <id>

# Quick vote
sage proposals vote <id> --support 1 --yes
```

### sage dao
DAO creation and management.

```bash
# Create new DAO
sage dao create -n "My DAO" --governance individual

# List available DAOs
sage dao list

# Set active DAO context
sage dao use 0xAddress
sage dao use my-dao-alias

# View DAO info
sage dao info 0xAddress

# Fork existing DAO
sage dao fork 0xSource -n "My Fork"

# Interactive wizard
sage dao wizard
```

---

## ECONOMICS

### sage bounty
Bounty management.

```bash
# Create bounty
sage bounty create --title "Fix bug" --reward 100 --yes

# List bounties
sage bounty list
sage bounty list --status open

# Claim bounty (as worker)
sage bounty claim <id> --yes

# Complete bounty (as claimant)
sage bounty complete <id> --yes

# Approve completion (as operator)
sage bounty approve <id> --winner 0xAddress --yes

# Diagnostics
sage bounty doctor --subdao 0xAddress
```

### sage boost
USDC governance vote incentives.

```bash
# Create boost for proposal
sage boost create --proposal-id <id> --per-voter 10 --max-voters 100 --yes

# Fund boost pool
sage boost fund --proposal-id <id> --amount 1000 --yes

# Check boost status
sage boost status --proposal-id <id>

# Claim boost payout (as voter)
sage boost claim --proposal-id <id> --yes
```

### sage treasury
Treasury operations.

```bash
# View treasury info
sage treasury info --subdao 0xAddress

# List reserves
sage treasury reserves

# View pending withdrawals
sage treasury pending
```

---

## DISCOVERY & REPUTATION

### sage reputation
Author reputation and trust signals.

```bash
# Check author metrics
sage reputation status 0xAddress

# View leaderboard
sage reputation leaderboard --limit 20

# View achievements/badges
sage reputation achievements 0xAddress

# Trust signal gating
sage reputation check 0xAddress --min-badges 1
```

### sage discover
Search and discovery (use `sage prompts search` for most cases).

```bash
# Search prompts
sage discover search "authentication"

# Trending prompts
sage discover trending --window 7d

# Similar prompts
sage discover similar <cid>
```

---

## CONTEXT & DIAGNOSTICS

### sage context
Show current working context.

```bash
# Show full context
sage context show

# JSON output
sage context show --json
```

### sage init
First-time setup.

```bash
# Interactive setup
sage init

# Non-interactive with preset
sage init --yes --preset base-sepolia-demo

# With skill installation
sage init --with-skill
```
</command_reference>

<workflows>
## SUGGESTED WORKFLOWS

When users ask for help with a task, suggest and execute these workflows:

### New User Setup
```bash
# Full setup sequence
npm install -g @sage-protocol/cli
sage wallet connect-privy
sage sxxx faucet
sage sxxx delegate-self
sage doctor
```

### Create Your First DAO
```bash
mkdir my-prompts && cd my-prompts
echo "# My Prompt\n\nYou are a helpful assistant." > hello.md
sage library quickstart -n "My DAO" --from-dir . --governance individual --yes
sage dao list
```

### Publish Prompts to DAO
```bash
# Build a library locally
sage library create "my-prompts"
sage library prompt add code-reviewer --file ./prompts/code-reviewer.md --library my-prompts

# Push to IPFS, then promote into the DAO's governed canon
sage library push my-prompts --cloud
sage library promote my-prompts --dao <dao>
```

### Vote on Governance
```bash
sage governance preflight --action vote
sage governance proposals list --dao <dao>
sage governance vote <id> --support 1 --yes
```

### Create and Fund Bounty
```bash
sage bounty create --title "Write documentation" --reward 50 --yes
sage bounty list --status open
```

### Install and Use Skills
```bash
sage prompts search "code review"
sage install 0xDAOAddress --alias code-tools
sage sync --check
```
</workflows>

<error_handling>
## AUTO-DIAGNOSE & FIX

When errors occur:

1. **Run diagnostics automatically:**
```bash
sage doctor --fix
```

2. **Common fixes applied automatically:**

| Error | Auto-Fix |
|-------|----------|
| "Wallet not connected" | Run `sage wallet connect-privy` |
| "Insufficient SXXX" | Run `sage sxxx faucet` |
| "No voting power" | Run `sage sxxx delegate-self` |
| "RPC error" | Run `sage config set-rpc https://sepolia.base.org --chain-id 84532` |
| "Contract addresses missing" | Run `sage doctor --fix` |

3. **Show plain-language explanation:**

```
┌─ Issue Detected ────────────────────────────────────────────┐
│                                                             │
│  Problem: You don't have voting power to vote on proposals  │
│                                                             │
│  Fix Applied: sage sxxx delegate-self                       │
│  Result: Voting power now delegated to your wallet          │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```
</error_handling>

<network_config>
## NETWORK CONFIGURATION

**Default: Base Sepolia (Testnet)**

```bash
# Testnet (default)
sage config set-rpc https://sepolia.base.org --chain-id 84532

# Mainnet (when ready)
sage config set-rpc https://mainnet.base.org --chain-id 8453
```

**Faucets:**
- ETH: https://www.coinbase.com/faucets/base-ethereum-sepolia-faucet
- SXXX: `sage sxxx faucet`
</network_config>

<status_cards>
## STATUS CARD FORMATS

Use these visual formats for displaying information:

### Wallet Status
```
┌─ Wallet ────────────────────────────────────────────────────┐
│  Address: 0x5be53fB4e1f138191c640272d58450CB5c60Fc43        │
│  Type: Privy                                                │
│  Network: Base Sepolia (84532)                              │
│  ETH: 0.5                                                   │
│  SXXX: 1000.00                                              │
│  Voting Power: 1000.00                                      │
└─────────────────────────────────────────────────────────────┘
```

### DAO Info
```
┌─ DAO: My Library ───────────────────────────────────────────┐
│  Address: 0x1234...5678                                     │
│  Governance: Personal (operator-controlled)                 │
│  Treasury: 500 SXXX                                         │
│  Members: 3                                                 │
│  Active Proposals: 2                                        │
└─────────────────────────────────────────────────────────────┘
```

### Proposal Status
```
┌─ Proposal #7 ───────────────────────────────────────────────┐
│  Title: Update library manifest                             │
│  State: Active                                              │
│  For: 750 / Against: 100 / Abstain: 50                     │
│  Ends: 2025-01-10 12:00 UTC                                 │
│  Your Vote: Not yet cast                                    │
└─────────────────────────────────────────────────────────────┘
```

### Bounty Status
```
┌─ Bounty #12 ────────────────────────────────────────────────┐
│  Title: Fix authentication bug                              │
│  Reward: 100 SXXX                                           │
│  Status: Open                                               │
│  Claims: 2                                                  │
│  Deadline: 7 days                                           │
└─────────────────────────────────────────────────────────────┘
```
</status_cards>

<agent_usage>
## AGENT-NATIVE USAGE

This skill is designed for both human users and AI agents in Claude Code.

**For agents automating Sage Protocol:**

1. All commands support `--json` for machine-readable output
2. Use `--yes` / `-y` to skip confirmations
3. Set `SAGE_YES=1` environment variable for full automation
4. Commands are idempotent where possible

**Example agent workflow:**
```bash
# Automated setup
SAGE_YES=1 sage init --preset base-sepolia-demo
sage wallet connect-privy
sage sxxx faucet
sage sxxx delegate-self

# Automated publishing (preview cost without uploading)
sage library push <library> --cloud --dry-run --yes
# Then push for real, then promote into governed canon
sage library push <library> --cloud --yes
sage library promote <library> --dao <dao>

# Automated voting
sage governance vote $PROPOSAL_ID --support 1 --yes --json
```
</agent_usage>

<quick_reference>
## QUICK REFERENCE

```
SETUP
  sage wallet connect-privy     Connect Privy wallet
  sage sxxx faucet              Get testnet tokens
  sage sxxx delegate-self       Enable voting power
  sage doctor --fix             Fix configuration issues

SKILLS / LIBRARY CONTENT
  sage library create <name>                    Create local library
  sage library prompt add <p> -f <file> -l <lib>  Add prompt to library
  sage skill publish <path> --library <lib>     Publish single skill to IPFS
  sage library push <lib> --cloud               Push whole library to IPFS
  sage library promote <lib> --dao <dao>        Promote to governed DAO canon

LIBRARIES
  sage library quickstart       Create DAO + library
  sage install <source>         Install from DAO/CID/GitHub
  sage sync                     Sync updates

GOVERNANCE
  sage governance proposals list --dao <dao>   List active proposals
  sage governance vote <id> 1                  Vote FOR
  sage governance preflight                    Check readiness

ECONOMICS
  sage bounty create            Create bounty
  sage bounty list              List bounties
  sage sxxx balance             Check balance

DISCOVERY
  sage prompts search <query>   Search prompts
  sage reputation status <addr> Author metrics
```
</quick_reference>
