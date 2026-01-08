<objective>
Manage the full prompt lifecycle: ideation, creation, iteration, versioning, and publishing to on-chain registries. Includes install flows from DAO/CID/GitHub/bundled skills.
</objective>

<quickstart>
**FASTEST PATH: Create a DAO with prompts in one command**

```bash
# Scan directory, upload to IPFS, create DAO, register manifest, auto-save alias
sage library quickstart --name "My Library" --from-dir ./prompts/

# With governance type
sage library quickstart --name "My Library" --from-dir ./prompts/ --governance personal  # Vault operator (default)
sage library quickstart --name "My Library" --from-dir ./prompts/ --governance team      # Council multisig
sage library quickstart --name "My Library" --from-dir ./prompts/ --governance community # Token voting

# Preview without executing
sage library quickstart --name "My Library" --from-dir ./prompts/ --dry-run
```

After quickstart:
- Alias auto-saved (e.g., `my-library`)
- Context auto-set to new DAO
- Run `sage prompts publish --yes --library-id default --exec` to publish updates (personal DAOs auto-execute)
- Run `sage prompts publish --yes --library-id default` for community DAOs (creates proposal)
</quickstart>

<install_sources>
**Install prompts or skills**

```bash
# From DAO
sage install 0xYourDaoAddress --library-id default

# V5 multi-library: install from a non-default stream
sage install 0xYourDaoAddress --library-id writing

# Create a new stream (one-time)
DATA=$(cast calldata "createLibrary(address,string)" 0xYourDaoAddress writing)

# Community/team: create a proposal (custom call)
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
- SIWE vault prompts are private; use `sage library vault`.
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

```bash
# One-shot publish (creates proposal for community DAOs)
sage prompts publish --yes --library-id default

# Personal DAO: auto-execute without manual voting
sage prompts publish --yes --library-id default --exec

# Create proposal only (no submit)
sage prompts propose --yes

# Alternative: publish to a specific DAO (without setting context)
sage prompts init --import-from ./prompts/
sage prompts publish --yes --subdao 0xDAO --library-id default --pin
```

**Personal DAOs (`--governance personal`)**: Use `--exec` flag for instant publishing. The system automatically votes, queues, and executes - no manual governance steps required.

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

# 5. Publish back to DAO
# For personal DAOs: instant publish with --exec
sage prompts publish --yes --exec

# For community DAOs: creates proposal, then vote
sage prompts publish --yes
sage proposals inbox
sage governance vote-with-reason <id> 1 "Improved edge case handling"
```

**Governance Types:**
- `--governance personal`: Use `--exec` for instant auto-vote/execute (no manual steps)
- `--governance team`: Council multisig approval required
- `--governance community`: Token holder voting required

---

### ERROR RECOVERY

| Error | Cause | Fix Command |
|-------|-------|-------------|
| `NonceMismatch` | Concurrent update | `sage prompts sync --pull` then retry |
| `No manifest registered` | DAO has no library | `sage prompts init && sage prompts publish --yes` |
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

# Publishing
sage prompts publish --yes --library-id default       # One-shot publish (default stream)
sage prompts publish --yes --library-id default --exec  # Personal DAO: auto-vote/execute
sage prompts propose --yes                            # Create proposal only
sage prompts sync                                     # Sync with on-chain

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
sage prompts publish --dry-run                        # Preview the manifest built from workspace changes

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

**CRITICAL: How `sage prompts publish` works:**

The `publish` command does NOT use `manifest.json`. It works by:
1. Reading the workspace snapshot (`.sage/workspace.json`)
2. Identifying changed prompts since last publish
3. Building a new manifest on-the-fly
4. Uploading prompts + manifest to IPFS
5. Updating on-chain pointer (direct or proposal)
</workspace_setup>
