<objective>
Current CLI note: `sage prompts` is now a legacy alias for `sage skill`; do not use old workspace/governance prompt-publish flows. Use `sage library prompt add`, `sage library push`, and `sage library promote`/`sage governance proposals` for library updates.

Manage the full prompt lifecycle: ideation, creation, iteration, versioning, and publishing to on-chain registries. Includes install flows from DAO/CID/GitHub/bundled skills.
</objective>

<quickstart>
**FASTEST PATH: Create a DAO with prompts in one command**

```bash
# Scan directory, upload to IPFS, create DAO, register manifest, auto-save alias
sage library quickstart --name "My Library" --from-dir ./prompts/

# With governance type
sage library quickstart --name "My Library" --from-dir ./prompts/ --governance personal  # Vault operator (default)
sage library quickstart --name "My Library" --from-dir ./prompts/ --governance council      # Council multisig
sage library quickstart --name "My Library" --from-dir ./prompts/ --governance community # Token voting

# Preview without executing
sage library quickstart --name "My Library" --from-dir ./prompts/ --dry-run
```

After quickstart:
- Alias auto-saved (e.g., `my-library`)
- Context auto-set to new DAO
- To add new content: `sage library prompt add <name> --file <path> --library <library>` or `sage skill publish <path> --library <library>`
- To push the updated manifest to IPFS: `sage library push <library> --cloud`
- To submit the new manifest CID into governed canon: `sage library promote <library> --dao <dao>` (personal DAOs auto-execute via timelock; community DAOs create a proposal for token-holder vote)
</quickstart>

<install_sources>
**Install prompts or skills**

```bash
# From DAO
sage library sync --dao 0xYourDaoAddress

# V5 multi-library: install from a non-default stream
sage library sync --dao 0xYourDaoAddress --library-id writing

# Create a new stream (one-time)
DATA=$(cast calldata "createLibrary(address,string)" 0xYourDaoAddress writing)

# Community/council: create a proposal (custom call)
sage governance wizard --subdao 0xYourDaoAddress

# Personal/operator: schedule via timelock
sage timelock schedule --subdao 0xYourDaoAddress --target $LIBRARY_REGISTRY_ADDRESS --data "$DATA"

# From prompt CID (allowlisted only)
sage install bafkrei...

# From GitHub repo (optionally with subpath)
sage install github:org/repo
sage install github:org/repo --subpath skills/my-skill

# From bundled skill
sage install build-web3
```

Notes:
- `/prompt/:cid` serves allowlisted on-chain prompts (DAO + on-chain personal/vault). 
- SIWE vault prompts are private; use `sage library create --visibility private` / `sage library shared`.
</install_sources>

<agent_workflows>
**AGENT COPY-PASTE WORKFLOWS**

These are the exact commands for agents to pull, sync, and push prompts.

---

### PULL: Get Prompts from DAO to Local

```bash
# Pull single prompt from current DAO
sage prompts pull <key>

# Pull from specific DAO
sage prompts pull <key> --from 0xDAO

# Pull all prompts from DAO to workspace
sage prompts sync --pull

# View DAO library (without downloading)
sage project latest-prompts --subdao 0xDAO

# Download full library content
sage project latest-prompts --subdao 0xDAO --download
```

---

### PUSH: Publish Local Changes to DAO

The publish flow is two distinct steps:

```bash
# 1. Push the library manifest to IPFS (or update the cloud personal pointer)
sage library push <library> --cloud

# 2. Promote the new manifest CID into governed canon
#    Personal DAOs auto-execute via timelock; community DAOs create a token-holder proposal.
sage library promote <library> --dao <dao>

# Preview the cost of step 1 without uploading
sage library push <library> --cloud --dry-run
```

---

### SYNC: Check Status and Differences

```bash
# Check what would change (local vs on-chain)
sage prompts status

# Show detailed diff
sage prompts diff

# Sync workspace state with on-chain (after proposal executes)
sage prompts sync
```

---

### IMPORT: Add Prompts to AGENTS.md

```bash
# Generate/update AGENTS.md from workspace skills
sage prompts generate-agents

# Import a skill template first
sage prompts import-skill <name>

# Or pull from DAO then generate
sage prompts pull my-skill --from 0xDAO
sage prompts generate-agents
```

---

### COMPLETE CYCLE: Pull → Edit → Push

```bash
# 1. Set DAO context
sage dao use 0xMyDAO

# 2. Pull the prompt you want to improve
sage prompts pull code-review

# 3. Edit locally (agent edits prompts/code-review.md)

# 4. Check what changed
sage prompts diff

# 5. Publish back to DAO (two steps: push to IPFS, then promote into canon).
#    `<library>` is the alias saved by `sage library quickstart` (e.g. `my-skills-library`).
#    `<dao>` is the SubDAO address shown by `sage dao list --json`.
sage library push <library> --cloud
sage library promote <library> --dao <dao>

# For community DAOs the promote step creates a proposal — list and vote on it next:
sage governance proposals list --dao <dao>
sage governance vote-with-reason <id> 1 "Improved edge case handling"
```

**Governance Types** (chosen via `sage library quickstart --governance <kind>`; affects how `sage library promote` behaves):
- `personal`: pass `--auto` to `sage library promote` for auto-schedule + auto-execute via timelock (Council/Personal mode only — see `sage library promote --help`).
- `council`: Council multisig approval required. Promote without `--auto` and have the council members vote/execute.
- `community`: Token holder voting required. Promote without `--auto`; this creates a proposal that token holders vote on, then anyone can execute.

---

### ERROR RECOVERY

| Error | Cause | Fix Command |
|-------|-------|-------------|
| `NonceMismatch` | Concurrent update | `sage prompts sync --pull` then retry |
| `No manifest registered` | DAO has no library | `sage library create <library> && sage library push <library> --cloud` |
| `insufficient proposer votes` | Not enough delegated voting power | See `sage governance preflight` for fix commands |
| `Governor not resolved` | Missing DAO context | `sage dao use 0xDAO` first |
</agent_workflows>

<command_reference>
```
# Workspace
sage prompts init                                     # Initialize workspace
sage prompts new --kind <prompt|skill|snippet> --name <name>  # Create artifact
sage prompts list                                     # List workspace
sage prompts status                                   # Local vs synced changes
sage prompts diff [filter]                            # Show diff
sage prompts lint                                     # Validate prompts

# Testing & Import
sage prompts try <keyOrCid>                           # Test locally
sage prompts import-onchain <key>                     # Import from chain
sage prompts pull <key>                               # Pull from registry
sage prompts import-skill <name>                      # Import skill template
sage prompts variant <key> [suffix]                   # Clone as variant

# Publishing pipeline (push -> promote, two distinct steps)
sage library push <library> --cloud                   # Upload manifest to IPFS / cloud pointer
sage library promote <library> --dao <dao>            # Submit manifest CID into governed canon
sage skill publish <path> --library <library>         # Publish a single skill (preserves skill identity)
sage prompts sync                                     # Sync local workspace with on-chain

# Project manifests
sage prompts init --import-from <dir>                 # Import content into workspace
sage project validate <manifest>                      # Validate a manifest.json file (advanced)
sage project check <manifest>                         # Best-practice checks
sage project preview <manifest>                       # Render summary
sage project estimate <manifest>                      # SXXX burn estimate
sage governance propose-library --manifest-cid <cid>  # Propose an already-uploaded manifest CID (advanced)

# Content detection & auto-publish
sage project scan [dir]                               # Classify content (skills vs prompts)
sage prompts init --import-from [dir]                 # Bring content into workspace
sage library push <library> --dry-run                        # Preview the manifest built from workspace changes

# Utilities
sage prompts search <query>                           # Search prompts
sage prompts export-legacy <key>                      # Export for Claude Desktop
sage prompts generate-agents                          # Update AGENTS.md
```
</command_reference>

<prompt_creation_philosophy>
Prompts are specialized knowledge packages that transform Claude from a general-purpose agent into a domain expert. Effective prompts provide:

1. **Procedural knowledge** - Step-by-step workflows Claude wouldn't know
2. **Domain expertise** - Company/project-specific context
3. **Tool integrations** - How to work with specific APIs or systems
4. **Quality constraints** - Output standards and validation criteria
</prompt_creation_philosophy>

<workspace_setup>
**Initialize a prompt workspace:**
```bash
sage prompts init
```

Creates:
- `prompts/` directory for prompt files
- `.sage/workspace.json` for state tracking (snapshot of all files)
- Git-friendly structure for versioning

**CRITICAL: How `sage library push <library> --cloud` works:**

The `publish` command does NOT use `manifest.json`. It works by:
1. Reading the workspace snapshot (`.sage/workspace.json`)
2. Identifying changed prompts since last publish
3. Building a new manifest on-the-fly
4. Uploading prompts + manifest to IPFS
5. Updating on-chain pointer (direct or proposal)
</workspace_setup>
