# Sage Manager Plugin

Command-free Sage Protocol experience for Claude Code. Manage DAOs, governance, bounties, staking, and prompt libraries through intuitive visual interfaces.

## Installation

```bash
# Add the Sage marketplace
/plugin marketplace add https://github.com/sage-protocol/sage-marketplace

# Install the plugin
/plugin install sage-manager
```

The CLI will be installed automatically when you start using the skill.

## Features

### Visual Dashboard
After installing this plugin, Claude will automatically show you a visual dashboard for Sage Protocol tasks. Just say what you want to do:

- "create a bounty"
- "vote on proposals"
- "stake my tokens"
- "manage my DAO"

No CLI commands required - Claude handles everything with visual menus and confirmations.

### Included Workflows
- **Libraries** - Browse, install, publish prompts
- **DAO** - Create, join, manage DAOs
- **Governance** - Vote, create proposals
- **Bounties** - Create, claim, manage bounties
- **Staking** - Stake, delegate, redelegate tokens
- **Treasury** - Manage DAO funds
- **NFTs** - Voting multipliers

### Commands (Power Users)

For those who prefer explicit commands:

- `/sage-install <source>` - Install from DAO, IPFS, or GitHub
- `/sage-list` - List installed dependencies
- `/sage-update [key]` - Update dependencies
- `/sage-setup` - Install/update Sage CLI

## License

MIT
