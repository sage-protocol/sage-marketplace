# Sage Protocol CLI Skill

A Claude Code skill for automating Sage Protocol governance workflows. This skill enables AI agents to help users create DAOs, manage prompts, run governance proposals, create bounties, and participate in permissionless collaboration on prompts.

## Vision

Sage Protocol enables **permissionless collaboration on prompts**. The best prompts emerge from iteration, not isolation. This skill helps agents:

- Help users publish prompts so they can be improved by others
- Propose improvements to existing prompts
- Create and claim bounties for prompt enhancements
- Facilitate governance voting on changes
- Guide users through DAO creation for team/community collaboration

**The future**: Agents actively crawl prompt libraries, identify improvement opportunities, submit proposals, and earn rewards for making prompts better.

## Installation

### Option 0: Install Sage CLI (recommended)

```bash
npm install -g @sage-protocol/cli
sage --version
```

**Privy relay auth (default):**
```bash
sage wallet connect-privy
```

### Option 1: Clone to Claude skills directory

```bash
git clone https://github.com/sage-protocol/sage-skill.git ~/.claude/skills/sage-protocol-cli
```

### Option 2: Symlink from existing clone

```bash
ln -s /path/to/sage-skill ~/.claude/skills/sage-protocol-cli
```

### Add the slash command (optional)

Create `~/.claude/commands/sage.md`:

```markdown
---
description: Automate Sage Protocol governance workflows using the CLI
argument-hint: [workflow or question]
---

Load the sage-protocol-cli skill from `~/.claude/skills/sage-protocol-cli/SKILL.md` and follow its instructions exactly.

User request: $ARGUMENTS
```

## Architecture

```
sage-skill/
├── SKILL.md                      # Main router and essential principles
├── README.md                     # This file
└── workflows/                    # Detailed workflow guides
    ├── dao-playbooks.md          # DAO creation with governance presets
    ├── governance-proposals.md   # Proposal lifecycle
    ├── bounty-lifecycle.md       # Bounty management
    ├── treasury-operations.md    # Treasury deposit/withdraw
    ├── nft-multipliers.md        # Voting multiplier NFTs
    ├── token-delegation.md       # SXXX delegation & voting power
    ├── prompts-projects.md       # Prompt workspace management
    ├── personal-library.md       # Vault + personal marketplace
    ├── boost-management.md       # Voting incentives
    └── setup-diagnostics.md      # CLI configuration
```

### SKILL.md Structure

The main skill file contains:

1. **Context + Objectives** - What the agent should prioritize
2. **Defaults + Constraints** - Safe behaviors (Privy relay, allowlist, vault)
3. **Quick Setup** - CLI install + auth
4. **Workflow Map** - Pointers to detailed guides
5. **Execution Rules** - State checks before actions

### Workflow Files

Each workflow is self-contained with:

- `<objective>` - What the workflow accomplishes
- `<command_reference>` - CLI commands with flags
- `<process>` - Step-by-step instructions
- `<success_criteria>` - Checklist for completion

## Key Principles

### Proactive Discovery

Agents should check state themselves instead of asking:

```bash
# Don't ask "do you have a DAO?" - check:
sage context profiles
sage dao list

# Don't ask "what prompts do you have?" - check:
ls prompts/
sage prompts list
sage library vault list
```

### Automation Flags

All commands support `-y` or `--yes` to skip confirmations:

```bash
sage bounty create --title "Fix bug" --reward 100 -y
sage governance vote 42 1 -y
```

### Context Resolution

Always establish DAO context before governance operations:

```bash
export SUBDAO=0x...
# or
sage governance list --subdao 0x...
```

## Workflows Overview

| Workflow | Purpose |
|----------|---------|
| **DAO Playbooks** | Create governed spaces: personal/vault (solo), council (team), community (token voting) |
| **Governance** | Propose changes, vote, queue, execute - how prompts evolve |
| **Bounties** | Incentivize contributions with on-chain rewards |
| **Treasury** | Fund collaboration with deposited assets |
| **NFT Multipliers** | Reward contributors with boosted voting power |
| **Token Operations** | Delegate SXXX voting power, check thresholds |
| **Prompts** | Manage workspaces, publish to libraries |
| **Vault/Personal** | Publish private prompts + premium marketplace |
| **Boosts** | Create voting incentive campaigns |
| **Setup** | Configure CLI, wallets, troubleshoot |

## Contributing

This skill evolves through the same permissionless collaboration it enables. To improve:

1. Fork this repository
2. Make your changes
3. Submit a PR

Or create a bounty in Sage Protocol to incentivize specific improvements.

## License

MIT
