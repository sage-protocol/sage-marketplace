# Sage Marketplace

A Claude Code plugin marketplace for Sage Protocol skills and prompts.

## Quick Start

### Add the Marketplace

```bash
/plugin marketplace add https://github.com/sage-protocol/sage-marketplace
```

### Install a Plugin

```bash
/plugin install sage-manager
```

## Publishing Skills to the Marketplace

Skills published to the marketplace are automatically synced and available to all users.

### Publish Your Skill

```bash
# From your skill directory (must contain plugin.json + SKILL.md)
sage prompts publish-skill ./my-skill --register --yes
```

The `--register` flag:
1. Uploads your skill to IPFS (permanent content addressing)
2. Registers it with the Sage marketplace API
3. Makes it available for automatic sync to this repository

### What Happens Next

1. **Immediate**: Your skill is available via IPFS CID
2. **Within 15 minutes**: GitHub Action syncs from API and adds your skill to `plugins/`
3. **Automatic**: `marketplace.json` is regenerated with your skill included

### Skill Requirements

Your skill directory must contain:

```
my-skill/
├── plugin.json      # Metadata (name, description, version, author)
└── SKILL.md         # Claude Code skill instructions
```

**plugin.json example:**
```json
{
  "name": "my-skill",
  "description": "What your skill does",
  "version": "1.0.0",
  "author": { "name": "Your Name" },
  "keywords": ["tag1", "tag2"],
  "agents": ["./SKILL.md"]
}
```

### Check Available Skills

```bash
# View all registered skills
curl https://api.sageprotocol.io/marketplace/skills | jq '.skills[].name'
```

## Installing Skills

### Via Claude Code Plugin System

```bash
# Add marketplace (once)
/plugin marketplace add https://github.com/sage-protocol/sage-marketplace

# Install any skill
/plugin install sage-node
/plugin install solidity-audit
/plugin install build-web3
```

### Via IPFS CID

```bash
# Direct install from content address
/plugin add https://api.sageprotocol.io/git/skill/<CID>.git
```

### Via Sage CLI

```bash
sage install bafkrei...        # From IPFS CID
sage install 0x61835...        # From DAO library
sage install github:org/repo   # From GitHub
```

## Available Plugins

| Plugin | Description |
|--------|-------------|
| `sage-manager` | Install/manage skills from CID, DAO, or GitHub |
| `sage-node` | Full Sage CLI experience with auto-setup |
| `sage-protocol-cli` | Governance workflows via CLI |
| `build-web3` | Web3 dApp development lifecycle |
| `solidity-audit` | Smart contract security auditing |
| `claude-flow` | Enterprise AI agent orchestration |

## Sage Manager Commands

#### `/sage-setup`

Install the Sage CLI (required for other commands).

#### `/sage-install <source>`

Install prompts or skills:

- **DAO**: `0x5be53fB4...` - On-chain DAO library
- **IPFS**: `QmT5NvUto...` or `bafkrei...` - Content CID
- **GitHub**: `github:user/repo/path` - Repository
- **Bundled**: `build-web3` - CLI bundled skills

#### `/sage-list`

List all installed dependencies with metadata.

#### `/sage-update [key] [--all]`

Update dependencies to latest versions.

## API Reference

| Endpoint | Description |
|----------|-------------|
| `GET /marketplace/skills` | List all registered skills |
| `GET /marketplace/plugins/:name` | Get plugin by name |
| `GET /marketplace/search?q=...` | Search plugins |
| `POST /marketplace/register` | Register a skill (authenticated) |

Base URL: `https://api.sageprotocol.io`
