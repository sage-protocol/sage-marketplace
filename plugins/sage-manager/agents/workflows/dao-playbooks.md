<objective>
Create and configure DAOs using governance playbooks - predefined configuration presets that set up voting, permissions, and execution modes.
</objective>

<command_reference>
```
# RECOMMENDED: Create single-wallet-owned DAO (no token voting)
sage dao create-operator --name "My DAO" --description "..." \
  --executor <your-wallet-address> \
  [--admin <admin-address>]           # defaults to executor \

# Create DAO with playbook (Plan/Apply). Run with --dry-run to generate a plan JSON.
sage dao create-playbook --help

# Create DAO with playbook (for community/token voting)
sage dao create-playbook --playbook <id> --name "My DAO" --description "..." \
  [--owners 0x...,0x...] [--threshold <n>] \
  [--min-stake <amount>] \
  [--voting-period "3 days"] [--quorum-votes 100] \
  [--proposal-threshold <amount>] \
  [--manifest <path-or-cid>] [--manifest-version <version>] \
  [--wizard] [--dry-run] [--yes]

# Create DAO directly (without playbook). Requires --min-stake.
sage dao create --name "My DAO" --min-stake 100 \
  [--type personal|team|community] \
  [--manifest ./prompts/manifest.json] [--manifest-version "1"]

# Fork an existing DAO's library (displays cost breakdown)
sage dao fork <source-address> \
  [--name "Forked DAO"] [--description "..."] \
  [--fee] [--yes]

# Apply a previously generated plan
sage dao create-playbook --apply plan.json

# Plan/Apply with manifest
sage project plan --manifest ./prompts/manifest.json
sage project apply plan.json

# Apply governance template to existing SubDAO
sage governance apply-template --subdao 0x... --template <name> \
  [--operator 0x...] [--cooldown <sec>]
```
</command_reference>

<playbook_types>
**Playbook to Profile Mapping (3-Axis Model):**

| Playbook ID | governanceKind | proposalAccess | executionAccess | Use Case |
|-------------|----------------|----------------|-----------------|----------|
| `personal` | OPERATOR | COUNCIL_ONLY | COUNCIL_ONLY | Solo creator, EOA control |
| `council-closed` | OPERATOR | COUNCIL_ONLY | COUNCIL_ONLY | Team Safe, no token voting |
| `council-drafts` | TOKEN | COMMUNITY_THRESHOLD | COUNCIL_ONLY | Community proposes, council executes |
| `community` | TOKEN | COMMUNITY_THRESHOLD | ANYONE | Full token democracy (voting-period: 3 days, quorum-votes: 100) |
| `community-long` | TOKEN | COMMUNITY_THRESHOLD | ANYONE | Broader participation (voting-period: 7 days, quorum-votes: 50) |

**Legacy playbooks (deprecated):**
| `council` | (legacy) | - | - | Use `council-closed` instead |

**Profile axis meanings:**
- `governanceKind`: OPERATOR (council decides) vs TOKEN (token voting)
- `proposalAccess`: COUNCIL_ONLY (only council can propose) vs COMMUNITY_THRESHOLD (anyone with enough tokens)
- `executionAccess`: COUNCIL_ONLY (council Safe executes) vs ANYONE (anyone can execute passed proposals)
</playbook_types>

<playbook_parameters>
Each playbook sets these governance parameters:

Defaults below are sourced from `packages/cli/src/config/playbooks.json`:

| Playbook ID | Executor | Proposal Threshold | Voting Period | Quorum Votes | Min Stake |
|------------|----------|--------------------|--------------|-------------|--------------|
| `personal` | EOA | `0` | `0` | `1` | `0` |
| `council-closed` | Safe | `0` | `0` | `1` | `0` |
| `council-drafts` | Safe | `10000` | `3 days` | `100` | `100` |
| `community` | Timelock | `10000` | `3 days` | `100` | `100` |
| `community-long` | Timelock | `10000` | `7 days` | `50` | `100` |

**Key differences:**
- **Personal vs Council-Closed**: Same profile, different executor (EOA vs Safe multisig)
- **Council-Drafts vs Community**: Community proposes/votes in both, but council-drafts requires council to execute
- **Community vs Community-Long**: Same profile, different voting period and quorum-votes
</playbook_parameters>

<process>
**Step 1: Choose your governance model**

**Agent step (ask + preview before creating):**

Before running `sage dao create-playbook`, ask/confirm:
- Which playbook ID should be used? (personal / council-closed / council-drafts / community / community-long)
- Who should control execution? (EOA vs Safe vs Timelock is implied by playbook; confirm owners/threshold for Safe playbooks)
- Do you want to override governance params? (`--proposal-threshold`, `--quorum-votes`, `--voting-period`, `--min-stake`)
- Should the DAO start with an initial library manifest? (`--manifest`, `--manifest-version`)
- Do you want a plan preview first? (`--dry-run` to save a plan JSON, then `--apply`)

Then present the exact command you will run and only execute after the user approves (use `--yes` only after explicit approval).

**PATH A (recommended for prompt libraries): `library quickstart`**

If the user already has prompts in `./prompts/`, this is the fastest path:
```bash
sage library quickstart --name "My Library" --from-dir ./prompts/ --dry-run
sage library quickstart --name "My Library" --from-dir ./prompts/
```

After creation, save and set context:
```bash
sage dao save 0xNEW_SUBDAO --alias my-library
sage dao use my-library
```

**PATH B: Single-wallet-owned DAO (no token voting)**

Use `create-operator` for DAOs owned by a single wallet. No token voting - you are the executor.

```bash
sage dao create-operator \
  --name "My Library" \
  --description "Personal prompt collection" \
  --executor $(sage wallet address)
```

This is the fastest path for solo creators who want full control without token voting overhead.

**For solo creators (OPERATOR mode with playbook):**
```bash
sage dao create-playbook --playbook personal \
  --name "My Library" \
  --description "Personal prompt collection" \
  --yes
```

**For teams without token voting (OPERATOR mode):**
```bash
# Team with Safe multisig
sage dao create-playbook --playbook council-closed \
  --name "Team Library" \
  --description "Collaborative prompts" \
  --owners "0xAlice,0xBob,0xCharlie" \
  --threshold 2 \
  --yes

# Or single executor without Safe
sage dao create-operator \
  --name "Team Library" \
  --description "Collaborative prompts" \
  --executor 0xYourWallet
```

For community proposals with council execution (TOKEN + COUNCIL_ONLY):
```bash
sage dao create-playbook --playbook council-drafts \
  --name "Hybrid DAO" \
  --description "Community proposes, council executes" \
  --owners "0xAlice,0xBob,0xCharlie" \
  --threshold 2 \
  --yes
```

For full token democracy (TOKEN + ANYONE):
```bash
sage dao create-playbook --playbook community \
  --name "Community DAO" \
  --description "Token-governed library" \
  --voting-period "3 days" \
  --quorum-votes 100 \
  --yes
```

**Step 2: (Optional) Generate plan first (dry-run)**
```bash
sage dao create-playbook --playbook community \
  --name "Test DAO" \
  --dry-run
```

This outputs a plan JSON file without executing. Review it, then:
```bash
sage dao create-playbook --apply plan-20241206.json
```

**Step 3: (Optional) Use wizard for interactive setup**
```bash
sage dao create-playbook --wizard
```

Prompts for all parameters interactively.

**Step 4: Save and set context after creation**

When DAO creation completes, it outputs the new SubDAO address. You MUST save and set context:

```bash
# After: ✅ SubDAO deployed: 0xF2B5FAD21d461A5133209EB1cbe146606218E5A1

# Save the DAO with an alias (CORRECT syntax)
sage dao save 0xF2B5FAD21d461A5133209EB1cbe146606218E5A1 --alias my-dao

# Set as working DAO context
sage dao use my-dao

# Verify context is set
sage context show
```

**IMPORTANT: Command syntax notes:**
- `dao save` requires: `<address> --alias <name>` (NOT `--name`)
- `dao use` accepts aliases: `sage dao use my-dao` ✅

**Step 5: (For Community DAOs ONLY) Delegate voting power before publishing**

Community DAOs use token voting. Before you can publish prompts (which creates a governance proposal), you MUST:

```bash
# 1. Delegate SXXX voting power to yourself (required for ERC20Votes)
sage sxxx delegate-self
# Expected: ✔ Delegated voting power to self

# 2. Run preflight to verify you can propose
sage governance preflight --subdao 0x...
# Expected: ✅ Proposer readiness: OK

# 3. Now you can publish (creates governance proposal)
sage prompts init
sage prompts publish --yes
```

**If preflight fails with "insufficient proposer votes":**
```bash
# Check your SXXX balance
sage sxxx balance

# Get more testnet SXXX if needed
sage sxxx faucet

# Then delegate and retry
sage sxxx delegate-self
sage prompts publish --yes
```

This step is NOT needed for personal/operator DAOs (OPERATOR mode) - those use direct execution.
</process>

<allowance_and_prereqs>
**Before creating or forking DAOs, ensure SXXX allowance and context are correct.**

DAO creation and fork flows often require the factory contract to spend SXXX on your behalf. To avoid allowance errors mid-way through `dao create` or `dao fork`:

```bash
# 1. Set and verify DAO/factory context
sage dao use 0x...                                    # or skip for fresh create
sage context show                                     # confirm network + addresses

# 2. Find factory address from your profile
cat .sage/config.json | jq '.profiles.default.addresses.SUBDAO_FACTORY_ADDRESS'

# 3. Ensure SXXX allowance to the factory
sage sxxx ensure-allowance <factory> 2000 -y          # or a higher amount for multiple operations

# 4. (Optional) Check your SXXX balance
sage sxxx balance
```

Then run your DAO creation command:

```bash
sage dao create-playbook --playbook council --name "Web3 Dev Council" --yes
# or
sage dao create --name "My DAO" --manifest ./prompts/manifest.json --manifest-version "1.0.0"
```

Following this pattern prevents common failures like:
- “insufficient allowance” when the factory tries to burn/charge SXXX
- confusing mid-command prompts to approve SXXX under time pressure
</allowance_and_prereqs>

<governance_templates>
Apply governance templates to existing SubDAOs:

**Community Drafts, Board Executes:**
```bash
sage governance apply-template \
  --subdao 0x... \
  --template community-drafts-board-exec \
  --operator 0xSafeAddress
```
- Community members can create proposals
- Board (Safe multisig) executes approved proposals
- Good for: DAOs wanting community input with controlled execution

**Token Democracy:**
```bash
sage governance apply-template \
  --subdao 0x... \
  --template token-democracy \
  --anyone-exec
```
- Full token-based governance
- Anyone can execute passed proposals (with `--anyone-exec`)
- Good for: Fully decentralized governance
</governance_templates>

<dao_with_initial_manifest>
**Create DAO with prompts already included.**

Instead of creating an empty DAO and publishing prompts later, you can create a DAO with an initial manifest - prompts are published as part of DAO creation.

From a manifest file (using the v3 manifest schema where the JSON contains `"version": "3.0.0"` at the top level, and `--manifest-version` is the library’s own release label, defaulting to `"1"`):
```bash
sage dao create --name "My DAO" \
  --manifest ./prompts/manifest.json \
  --manifest-version "1"
```

From an existing IPFS CID:
```bash
sage dao create --name "My DAO" \
  --manifest QmExistingCID \
  --manifest-version "1"
```

With a playbook:
```bash
sage dao create-playbook --playbook personal \
  --name "My Library" \
  --manifest ./prompts/manifest.json \
  --manifest-version "1" \
  --yes
```

The CLI will:
1. Detect if `--manifest` is a CID (starts with `Qm...` or `bafy...`) or a file path
2. If file path: read, parse JSON (expecting manifest v3 with `"version": "3.0.0"`), then upload to IPFS
3. Pass the manifest CID to the DAO creation transaction
4. DAO is created with prompts already in its library
</dao_with_initial_manifest>

<dao_forking>
**Fork an existing DAO's library to create a new DAO.**

Forking creates a new DAO based on an existing one - inheriting its prompt library while establishing independent governance. This is useful for remixing or evolving prompts in a new direction.

```bash
sage dao fork <source-address>
```

**Cost breakdown:**
Before executing, the CLI displays a cost breakdown:

```
┌─────────────────────────────────────────────┐
│             Fork Cost Breakdown             │
├─────────────────────────────────────────────┤
│  SXXX Burn:           1000.0 SXXX           │
│  Library Fork Fee:    100.0 SXXX            │
│                       → Parent treasury     │
├─────────────────────────────────────────────┤
│  Total SXXX:          1100.0 SXXX           │
├─────────────────────────────────────────────┤
│  Your SXXX Balance:   5000.0 SXXX ✓         │
└─────────────────────────────────────────────┘
```

**Cost components:**
| Component | Description | Destination |
|-----------|-------------|-------------|
| SXXX Burn | Base cost for DAO creation (default: 1000 SXXX) | Burned (supply reduction) |
| Library Fork Fee | Per-library fee set by parent DAO | Parent DAO treasury |

**Library fork fees** are set by each DAO in the LibraryRegistry. They incentivize quality libraries - popular libraries that get forked frequently generate treasury revenue.

**Options:**
```bash
sage dao fork <source-address> \
  [--name "Forked DAO"] \
  [--description "My remix"] \
  [--fee]                        # Use stable token fee instead of SXXX
  [-y | --yes]                   # Skip confirmation
```

**When to fork:**
- You want to evolve prompts in a new direction
- You're creating a variant for a different use case
- You want to start with an existing library rather than from scratch
- Parent DAO charges reasonable fork fees you're willing to pay

**Example workflow:**
```bash
# 1. Check the source DAO's library and fork fee
# (e.g. via governance info / status, or DAO docs)

# 2. Fork the DAO (displays cost breakdown)
sage dao fork 0xSourceDAO --name "My Fork"

# 3. Set context to your new DAO
sage dao use 0xNewDAO

# 4. Evolve the library independently
sage prompts publish -y
```
</dao_forking>

<plan_apply_pattern>
The Plan/Apply pattern separates planning from execution:

```bash
# 1. Generate plan (review governance config before committing)
sage dao create-playbook --playbook council --name "Test" --dry-run
# Creates: plan-<timestamp>.json

# 2. Review the plan
cat plan-<timestamp>.json

# 3. Apply when ready
sage dao create-playbook --apply plan-<timestamp>.json
```

With manifest:
```bash
# 1. Generate plan with manifest
sage project plan --manifest ./prompts/manifest.json

# 2. Review and apply
sage project apply plan.json
```

Benefits:
- Review governance settings before on-chain commitment
- Share plans for team approval
- Reproduce DAO configurations
- Playbook CID is stamped to IPFS for provenance
- Include initial prompts in the plan
</plan_apply_pattern>

<governance_patterns>
**How to change economics and config based on governance profile**

**OPERATOR mode (personal / council-closed)**
- `governanceKind: OPERATOR`, `proposalAccess: COUNCIL_ONLY`
- One EOA or Safe multisig controls the DAO.
- When fine for quick changes:
  - `sage dao-config apply-initial --subdao 0x... --voting-period-blocks ... --quorum-votes ...`
  - Direct `sage dao-config set-*` commands with `--execute` (Timelock schedules + executes).
- When to still use proposals:
  - You want an on-chain audit trail for upgrades or economic changes.
  - Use `sage dao-config propose-initial` or `sage governance propose-custom`.
- Execution: Council Safe or EOA directly executes on Timelock.

**TOKEN + COUNCIL_ONLY (council-drafts)**
- `governanceKind: TOKEN`, `proposalAccess: COMMUNITY_THRESHOLD`, `executionAccess: COUNCIL_ONLY`
- Community proposes and votes; council executes.
- Always use proposals for economic changes:
  ```bash
  sage dao-config propose-initial \
    --subdao 0xDAO \
    --config 0xGovernanceConfig \
    --bounty-stake-bps 200 \
    --rev-split "80/10/10"
  ```
- After vote succeeds, council Safe calls `execute()` on Timelock.
- Council has final say on what gets executed.

**TOKEN + ANYONE (community / community-long)**
- `governanceKind: TOKEN`, `executionAccess: ANYONE`
- Token holders vote, anyone executes passed proposals.
- Always use proposals:
  - For library fork fees:
    - `sage calldata library-set-fork-fee ...` → `sage governance propose-custom ...`
  - For bounty/premium economics:
    - `sage dao-config propose-initial ...` or `sage governance propose-custom ...`
  - For prompt/library changes:
    - `sage prompts publish --yes` or `sage prompts propose --yes`
- Never rely on direct `set-*` / operator-style helpers; they bypass token holder approval.

**Profile detection:**
```bash
sage governance diag --subdao 0x...   # Shows profile and convenience flags
```
</governance_patterns>

<customization>
Override playbook defaults:

```bash
sage dao create-playbook --playbook community \
  --name "Custom DAO" \
  --voting-period "5 days" \
  --quorum-votes 100 \
  --proposal-threshold "5000" \
  --yes
```

| Override | Description |
|----------|-------------|
| `--voting-period` | Duration (e.g., "3 days", "72 hours", "4320 blocks") |
| `--quorum-votes` | Quorum in SXXX tokens (e.g., 100 for 100 SXXX) |
| `--proposal-threshold` | SXXX required to propose |
| `--manifest` | Initial manifest file path or IPFS CID |
| `--manifest-version` | Version string for the initial manifest |
</customization>

<success_criteria>
- [ ] Playbook selected based on governance needs
- [ ] DAO created with correct parameters
- [ ] (Council) Safe owners and threshold configured
- [ ] (Community) Voting period and quorum set appropriately
- [ ] Playbook CID stamped to IPFS for provenance
- [ ] (If manifest) Initial prompts published to DAO library
- [ ] (If fork) Cost breakdown reviewed, fork fee paid to parent treasury
</success_criteria>
