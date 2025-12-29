# Sage Manager Plugin

Command-free Sage Protocol experience for Claude Code. Manage DAOs, governance, bounties, staking, and prompt libraries through intuitive visual interfaces.

## Installation

```bash
# Add the Sage marketplace
/plugin marketplace add https://github.com/sage-protocol/sage-marketplace

# Install the plugin
/plugin install sage-manager
```

The CLIs will be installed automatically when you run `/sage-setup`.

## Backend Support

This plugin supports two CLI backends:

| CLI | Language | Strengths |
|-----|----------|-----------|
| **sage** | Node.js | Full on-chain features (bounties, NFTs, treasury, governance) |
| **scroll** | Rust | MCP hub, daemon, faster library sync |

### MCP Integration

If scroll is installed and registered as an MCP server, the plugin uses MCP tools for read operations (instant, no shell spawn):

```bash
# Register scroll as MCP server
claude mcp add scroll -- scroll mcp start
```

Write operations (voting, staking, publishing) always use the sage CLI as they require wallet signing.

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

- `/sage-setup` - Install/configure both CLIs (sage + scroll)
- `/sage-backend` - Show CLI status and configure preferences
- `/sage-install <source>` - Install from DAO, IPFS, or GitHub
- `/sage-list` - List installed dependencies
- `/sage-update [key]` - Update dependencies

### Backend Preferences

```bash
/sage-backend                    # Show current CLI status
/sage-backend prefer scroll      # Prefer scroll for speed/MCP
/sage-backend prefer sage        # Prefer sage for full features
/sage-backend prefer auto        # Auto-select based on operation
```

## License

MIT
