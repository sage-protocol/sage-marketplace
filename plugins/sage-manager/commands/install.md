---
name: sage-install
description: Install prompts or skills via the Sage CLI
allowed-tools: Bash(which sage:*), Bash(sage install:*)
argument-hint: <source>
---

Install prompts or skills using the Sage CLI.

Sources:
- DAO address
- Prompt CID (allowlisted)
- GitHub repo
- Bundled skill

```bash
set -euo pipefail

SOURCE="${ARGUMENTS:-}"
if [ -z "$SOURCE" ]; then
  echo "Usage: /sage-install <cid | 0xDAO | github:org/repo | bundled-skill>"
  exit 1
fi

if ! which sage >/dev/null 2>&1; then
  echo "Error: Sage CLI not installed. Run: /sage-setup"
  exit 1
fi

sage install "$SOURCE" --json

```
