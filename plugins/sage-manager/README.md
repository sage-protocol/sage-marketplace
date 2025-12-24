# Sage Manager Plugin

Manage Sage Protocol prompts and skills directly from Claude Code.

## Installation

```bash
claude plugin install sage-manager@every-marketplace
```

Requires Sage CLI:
```bash
npm install -g @sage-protocol/cli
```

## Commands

### `/sage-install <source>`

Install prompts or skills from various sources:

- **DAO**: `0x5be53fB4...` - On-chain DAO library
- **IPFS**: `QmT5NvUto...` or `bafkrei...` - Content CID
- **GitHub**: `github:user/repo/path` - Repository
- **Bundled**: `build-web3` - CLI bundled skills

### `/sage-list`

List all installed dependencies with metadata.

### `/sage-update [key] [--all]`

Update dependencies to latest versions. Use `--all` for all, or specify a key.

## License

MIT
