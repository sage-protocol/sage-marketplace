---
name: sage-install
description: Install prompts or skills via the Sage CLI (skills auto-activate in Claude Code)
allowed-tools: Bash(which:*), Bash(npm:*), Bash(sage:*), Bash(mkdir:*), Bash(ls:*)
argument-hint: <source>
---

Install prompts or skills using the Sage CLI.

**Sources:**
- `bafkrei...` - CID (IPFS content address)
- `0x...` - DAO address (installs DAO's library)
- `github:org/repo` - GitHub repository
- `github:org/repo/path` - GitHub repo subpath
- `./local/path` - Local directory (skill folder with SKILL.md, or prompt files)
- `skill-name` - Bundled skill from CLI

**Skill Auto-Discovery:**
Skills containing `SKILL.md` are installed to `.claude/skills/<name>/` and a slash-command is created in `.claude/commands/<name>.md`.
Prompts are installed to `prompts/` (workspace). If no workspace exists, `sage install` initializes one automatically.

```bash
set -euo pipefail

SOURCE="${ARGUMENTS:-}"
if [ -z "$SOURCE" ]; then
  echo "Usage: /sage-install <cid | 0xDAO | github:org/repo[/path] | ./path | skill-name>"
  echo ""
  echo "Examples:"
  echo "  /sage-install bafkreiab...          # Install from IPFS CID"
  echo "  /sage-install 0x61835...            # Install from DAO library"
  echo "  /sage-install github:sage/prompts   # Install from GitHub"
  echo "  /sage-install github:sage/prompts/skills/my-skill  # Install from GitHub subpath"
  echo "  /sage-install ./skills/my-skill     # Install from local folder"
  echo "  /sage-install my-custom-skill       # Install bundled skill"
  exit 1
fi

# Ensure CLI is installed
if ! which sage >/dev/null 2>&1; then
  echo "Installing Sage CLI..."
  npm install -g @sage-protocol/cli
fi

echo "Fetching: $SOURCE"
sage install "$SOURCE" --to "." -y --json 2>/dev/null || sage install "$SOURCE" --to "." -y

echo ""
echo "Installed. Locations:"
echo "  - Skills:  .claude/skills/ + .claude/commands/"
echo "  - Prompts: prompts/"
echo ""
echo "Next:"
echo "  - List installed deps: /sage-list"
```
