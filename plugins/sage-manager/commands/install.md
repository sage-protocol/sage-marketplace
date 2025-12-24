---
name: sage-install
description: Install prompts or skills from Sage Protocol
allowed-tools: Bash(sage install:*), Bash(which sage:*)
argument-hint: <source>
---

Install a prompt or skill from Sage Protocol.

Sources: DAO address, IPFS CID, `github:user/repo/path`, or bundled skill name.

```bash
# Check CLI is installed
which sage || echo "Error: Sage CLI not installed. Run: npm install -g @sage-protocol/cli"

# Install from source
sage install $ARGUMENTS --json
```
