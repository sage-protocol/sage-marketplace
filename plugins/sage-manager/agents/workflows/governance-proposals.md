<objective>
Manage the full governance proposal lifecycle: create proposals, vote, queue after success, and execute after timelock.
</objective>

<command_reference>
```
# Profile detection (run first)
sage governance diag [--subdao 0x...]                 # Full governance profile analysis
sage governance preflight [--subdao 0x...]            # Profile-aware readiness check
sage governance threshold-status [--subdao 0x...]     # Threshold check with delegation status

# Proposal commands
sage governance propose-custom --description "..." --target 0x... --calldata 0x... -y
sage governance wizard                                # Interactive proposal builder
sage governance list [--subdao 0x...]                 # List proposals
sage governance info <id>                             # Proposal details
sage governance status <id>                           # On-chain status + manifest
sage governance vote <id> <support> -y                # Vote (0=against, 1=for, 2=abstain)
sage governance vote-with-reason <id> <support> --reason "..." -y
sage governance queue <id> -y                         # Queue succeeded proposal
sage governance execute <id> -y                       # Execute after timelock
sage governance watch <id>                            # Auto queue + execute
sage governance last                                  # Get last proposal ID
sage governance inspect <id>                          # Decode proposal actions
sage governance quorum                                # Show quorum config
sage governance threshold                             # Show proposal threshold
sage governance self-delegate                         # Delegate to self
sage governance delegation [address]                  # Check delegation status

# Alternative vote commands via proposals namespace
sage proposals inbox --subdao 0x...
sage proposals preview <id> --subdao 0x...
sage proposals vote <id> <for|against|abstain> --subdao 0x... -y
sage proposals execute <id> --subdao 0x... -y
```

**Notes:**
- Use `sage proposals ...` for day-to-day proposal navigation (inbox/preview/vote/execute).
- Use `sage governance ...` for diagnostics and advanced operations (preflight/diag/inspect/templates).
</command_reference>

<authority>
**Agent Responsibilities (MCP vs CLI)**

**MCP Server (read-only)**
- Navigate DAO structure and governance profiles
- Query proposal states, voting power, and thresholds
- Generate CLI commands for the user to execute
- Iterate on prompts locally before publishing

**CLI (execution surface)**
- Submit transactions: propose, vote, queue, execute
- Run readiness checks (`preflight`, `threshold-status`)
- Delegate voting power and manage vote/propose prerequisites
- Execute fix-flow commands when readiness checks fail

The MCP server provides discovery and command generation; the CLI handles all state-changing operations.
</authority>

<preflight>
**Always run preflight before creating proposals:**

```bash
sage governance preflight --subdao 0x...
```

**And before voting:**

```bash
sage governance preflight --subdao 0x... --action vote
```

This runs the same diagnostics as the CLI’s `GovernanceManager.preflightProposeDiagnostics()`:

- Resolves Governor/SubDAO context
- Prints proposal config: `proposalThreshold`, `votingDelay`, `votingPeriod`, `proposalCooldown`
- Checks proposal cooldown (blocks proposals until cooldown expires)
- Computes voting power at the previous clock tick and compares to `proposalThreshold` (delegation required; NFT multipliers apply when enabled)

For voting, preflight additionally checks (when supported by the Governor):
- Delegation status (no delegation → 0 votes)
- `minVotesToVote` (default: **1 SXXX** effective votes) to prevent 0-weight vote spam and reduce per-voter farming via wallet-splitting

If threshold is not met in token governance mode, preflight prints concrete next steps (from the CLI source):

```bash
💡 To gain voting power:
   1. Ensure you hold SXXX tokens (`sage sxxx balance`)
   2. Self-delegate voting power: `sage sxxx delegate-self`
   3. Wait one block for delegation to take effect

🔍 Run 'sage dao doctor --subdao 0x...' for detailed voting power diagnostics
```

Treat any `❌` or `⚠️` from `sage governance preflight` as blockers and fix them
before attempting to propose.

**Threshold-Status Quick Check:**
```bash
sage governance threshold-status --subdao 0x...
```
Output: threshold, your votes at clock()-1, shortfall, delegation status.
</preflight>

<delegation_warning>
**MultipliedVotes Delegation Warning**

If the Governor's voting token is a **MultipliedVotes wrapper** (NFT multipliers), delegate on the **base token**, not the wrapper.

⚠️ Calling `delegate()` on a MultipliedVotes wrapper **will revert**.

```bash
# Delegate on the base token (usually SXXX), not the wrapper
sage sxxx delegate-self
```
</delegation_warning>

<cancelability>
**Proposal Cancelability**

Proposals can be canceled if your voting power drops below threshold while **Pending/Active**.

- Maintain voting power until proposal reaches Succeeded
- CLI warns if you're within 20% of threshold
</cancelability>

<governance_modes>
**Governance Profiles (3-Axis Model)**

v2+ DAOs use an orthogonal 3-axis governance profile. Run `sage governance diag` to detect:

```bash
sage governance diag --subdao 0x...
```

Output shows:
- `governanceKind`: OPERATOR (council decides) or TOKEN (token voting)
- `proposalAccess`: COUNCIL_ONLY or COMMUNITY_THRESHOLD
- `executionAccess`: COUNCIL_ONLY or ANYONE
- `playbook`: derived name (council-closed, council-drafts, community, legacy)
- `isCouncil`: convenience flag for council-controlled DAOs

**OPERATOR mode (personal / council-closed)**
- `governanceKind: OPERATOR`, `proposalAccess: COUNCIL_ONLY`
- No token voting (threshold=0, quorum=0)
- Council Safe or EOA has EXECUTOR_ROLE on Timelock
- `preflight` shows:
  - Council role check
  - Timelock permissions
  - No voting power requirements
- Actions:
  - Direct Timelock scheduling: `sage timelock schedule ...`
  - Council approval flows

**TOKEN + COUNCIL_ONLY (council-drafts)**
- `governanceKind: TOKEN`, `proposalAccess: COMMUNITY_THRESHOLD`, `executionAccess: COUNCIL_ONLY`
- Community proposes via token threshold
- Community votes on proposals
- Council Safe executes successful proposals
- `preflight` shows:
  - Token requirements (hold + delegate; `proposalThreshold` + `minVotesToVote`)
  - "Council executes" reminder
- Prerequisites:
  - `sage sxxx delegate-self`
- After vote succeeds: Council Safe calls `execute()` on Timelock

**TOKEN + ANYONE (community)**
- `governanceKind: TOKEN`, `executionAccess: ANYONE`
- Full token democracy
- Anyone can execute passed proposals
- `preflight` shows:
  - `proposalThreshold` (votes required)
  - Your current votes at snapshot
  - Shortfall and exact steps to fix
  - Voting gate (`minVotesToVote`) when enabled
- Prerequisites:
  - `sage sxxx delegate-self`

**Legacy DAOs (v1)**
- `playbook: legacy` or `governanceKind: null`
- Profile not initialized; uses heuristic detection
- Upgrade path: migrate to v2 factory

**Always run diagnostics first:**
```bash
sage dao use 0x...                         # Set context
sage governance diag --subdao 0x...        # Understand profile
sage governance preflight --subdao 0x...   # Check readiness
```

Only proceed to proposing once preflight is clean.
</governance_modes>

<process>
**Step 1: Ensure context**
```bash
# Set working DAO for session (recommended)
sage dao use 0x...

# Or verify current context
sage context show

# Alternative: export environment variable
export SUBDAO=0x...
```

**Step 2: Create proposal**

Option A - Custom proposal (full control):
```bash
sage governance propose-custom \
  --description "Proposal description" \
  --target 0xContractAddress \
  --value 0 \
  --calldata 0x... \
  -y
```

Option B - Use wizard for common actions:
```bash
sage governance wizard
```

Option C - Parameter changes:
```bash
sage governance set --voting-delay 1d --voting-period 3d -y
```

**Step 3: Track proposal**
```bash
# Get proposal ID from output or cache
sage governance last

# Check status
sage governance status <id>
```

**Step 4: Vote**
```bash
# Wait for Active state
sage governance status <id>

# Vote (1=For, 0=Against, 2=Abstain)
sage governance vote <id> 1 -y

# Or with reason
sage governance vote-with-reason <id> 1 "Supporting this improvement" -y
```

**Step 5: Queue (after Succeeded)**
```bash
sage governance queue <id> -y
```

**Step 6: Execute (after timelock ETA)**
```bash
sage governance execute <id> -y
```

**Automated flow (recommended for agents):**
```bash
# Watch handles queue + execute automatically
sage governance watch <id>
```
</process>

<economic_parameters>
**Use governance proposals (not ad‑hoc `set` calls) to change shared economic parameters.**

The following knobs are all intended to be driven by proposals or timelock‑scheduled batches, not by one‑off admin transactions:

- **Library fork fees** – `LibraryRegistry.setLibraryForkFee(dao, fee)`
- **Bounty stake / premium splits** – `GovernanceConfig.setCreatorStakeBps` and `setPremiumRevSplit`
- **Boost / rebate programs** – `sage boost ...` flows tied to specific proposals
- **Prompt / library upgrades** – `LibraryRegistry.updateLibrary` via `sage prompts publish` / `sage prompts propose`

Example: set a library fork fee for a DAO via a normal CLI proposal:

```bash
# 1. Get LibraryRegistry address from your profile
cat .sage/config.json | jq '.profiles.default.addresses.LIBRARY_REGISTRY_ADDRESS'

# 2. Encode calldata for setLibraryForkFee(dao, fee)
FEE_WEI=$(node -e "console.log(require('ethers').ethers.parseEther('100').toString())")
DATA=$(sage calldata library-set-fork-fee \
  --dao 0xParentDAO \
  --fee-wei $FEE_WEI)

# 3. Propose via Governor (timelock will execute on LibraryRegistry)
sage governance propose-custom \
  --description "Set library fork fee to 100 SXXX" \
  --target 0xLibraryRegistry \
  --value 0 \
  --calldata "$DATA" \
  --subdao 0xParentDAO \
  -y
```

Patterns for other levers (all using **regular CLI proposal commands**):

- **Bounty economics (creator stake + premium split)**  
  - Initial setup or batch changes:
    ```bash
    sage dao-config propose-initial \
      --subdao 0xDAO \
      --config 0xGovernanceConfig \
      --bounty-stake-bps 200 \
      --rev-split "80/10/10"
    ```
    This builds a single `propose(...)` call on the Governor that updates `setCreatorStakeBps` and `setPremiumRevSplit` together.
  - For advanced cases, you can also target `GovernanceConfig` directly with:
    ```bash
    sage governance propose-custom --description "Update bounty stake" \
      --target 0xGovernanceConfig \
      --calldata 0xEncoded_setCreatorStakeBps \
      --subdao 0xDAO -y
    ```

- **Boost configuration (USDC incentives)**  
  - Day‑to‑day boosts are created and funded with:
    ```bash
    sage boost create --proposal-id <id> --governor 0x... --per-voter 1000000 --max-voters 100 -y
    sage boost fund   --proposal-id <id> --amount 100000000 -y
    ```
    These operate on the BoostManager contracts but are still tied to a specific `proposalId` on the Governor.
  - Policy‑level changes (e.g., Merkle policy adapters) should be done with proposals that call the relevant policy contracts, using `sage calldata ...` + `sage governance propose-custom`.

- **Prompt / library upgrades**  
  - Use the normal publishing flows; they already wrap governance:
    ```bash
    sage prompts publish --yes          # Build manifest, update LibraryRegistry via proposal
    sage prompts propose --yes          # Only build proposal, do not auto‑execute
    ```
    Under the hood these call `LibraryRegistry.updateLibrary(dao, manifestCID, version)` through the Governor/Timelock.

Governance mode guidance:

- **Personal / operator DAOs** – You *can* use operator‑style helpers (`dao-config apply-initial`, direct timelock scheduling) when a single EOA or Safe controls the DAO, but it’s often still worth using proposals for auditability.
- **Council DAOs** – Prefer `sage dao-config propose-initial` or `sage governance propose-custom`, let the council vote/execute, and avoid direct `set-*` calls from a single signer.
- **Community DAOs** – Always route economic changes through the full proposal lifecycle:
  `sage governance preflight` → `propose-*` → `vote` → `queue` → `execute`.

Always think in terms of **“propose → vote → queue → execute”** for shared economic settings, regardless of governance mode; operator‑style helpers are exceptions for tightly‑controlled DAOs, not the default.
</economic_parameters>

<proposal_states>
| State | Meaning | Next Action |
|-------|---------|-------------|
| Pending | Voting not started | Wait for voting delay |
| Active | Voting open | Vote |
| Succeeded | Passed, ready to queue | Queue |
| Queued | In timelock | Wait for ETA, then execute |
| Executed | Complete | Done |
| Defeated | Failed vote | None (create new proposal) |
| Canceled | Withdrawn | None |
| Expired | Missed execution window | None |
</proposal_states>

<common_commands>
```bash
# List all proposals
sage governance list --subdao 0x...

# Detailed info (state, quorum, votes, timing)
sage governance info <id>                # Human-readable summary
sage governance info <id> --json         # Machine-friendly details (stateRaw, quorum, votes, snapshot/deadline)

# Inspect actions and calldata
sage governance inspect <id>

# Check your SXXX voting power
sage sxxx delegation

# Check quorum requirements
sage governance quorum

# Delegate to yourself (required for voting power)
sage governance self-delegate
```
</common_commands>

<defensive_workflow>
**Gather all information BEFORE taking governance actions (to avoid CLI errors).**

For any proposal you’re about to vote on, queue, or execute:

```bash
# 1. Verify context
sage dao use 0x...                            # Set working DAO
sage context show                             # Confirm Governor/SubDAO/Timelock

# 2. Inspect proposal health
sage governance info <id>                     # Shows state, quorum, total votes
sage governance status <id>                   # On-chain status + manifest

# 3. Ensure your voting power is active
sage sxxx delegation                          # Check SXXX delegation
sage governance self-delegate                 # If not self-delegated

# 4. Run proposer diagnostics before proposing / queueing
sage governance preflight --subdao 0x...      # Checks delegation/votes, thresholds, cooldown, minVotesToVote

# 5. If allowance errors occur (SXXX approvals)
cat .sage/config.json | jq '.profiles.default.addresses.SUBDAO_FACTORY_ADDRESS'
sage sxxx ensure-allowance <factory> 2000 -y  # Or a higher amount if needed
```

Use this pattern to avoid common failures like:
- “insufficient allowance” when creating or forking DAOs
- “proposal not active / wrong state” when trying to queue/execute
- “insufficient voting power” when trying to propose
</defensive_workflow>

<success_criteria>
- [ ] Context resolved (subdao set)
- [ ] Preflight passed
- [ ] Proposal created and ID captured
- [ ] Votes cast during Active period
- [ ] Queued after Succeeded
- [ ] Executed after timelock ETA
</success_criteria>

<agent_complete_example>
**Complete Agent Workflow: Create and Execute a Proposal**

This shows the full flow from context setup to proposal execution. Replace placeholders with actual values.

```bash
# PHASE 1: Setup
# ===============
# Set the working DAO context
sage dao use 0xSUBDAO_ADDRESS

# Verify context is set
sage context show
# Expected: Shows SubDAO, Governor, Timelock

# Check wallet balance
sage sxxx balance
# Expected: ✔ SXXX Balance for 0x...: NNNN SXXX

# PHASE 2: Preflight
# ==================
# Run diagnostics before proposing
sage governance preflight --subdao 0xSUBDAO

# If "insufficient voting power" error:
sage sxxx delegate-self
# Ensure you hold enough SXXX to meet the DAO's proposalThreshold, then wait 1 block and re-run preflight

# PHASE 3: Create Proposal
# ========================
# Option A: Publish prompts (auto-creates proposal)
sage prompts publish --yes
# Expected: Proposal created with ID: 553902...

# Option B: Custom proposal
sage governance propose-custom \
  --description "Add new feature X" \
  --target 0xTARGET_CONTRACT \
  --calldata 0xCALLDATA \
  --subdao 0xSUBDAO \
  -y
# Expected: Proposal ID: NNNN...

# Save the proposal ID!
PROPOSAL_ID="553902..."

# PHASE 4: Vote
# =============
# Check proposal state (should be 1 = Active)
sage governance status $PROPOSAL_ID --subdao 0xSUBDAO
# Expected: State: Active

# Cast vote (use vote-with-reason for large IDs)
sage governance vote-with-reason $PROPOSAL_ID 1 "Approving this proposal" --subdao 0xSUBDAO
# Expected: ✔ Vote cast successfully

# Verify vote was recorded
sage governance info $PROPOSAL_ID --subdao 0xSUBDAO
# Expected: Shows votes For: NNNN

# PHASE 5: Wait for voting period
# ==============================
# Check when voting ends
sage governance info $PROPOSAL_ID --subdao 0xSUBDAO
# Look for "Voting ends" timestamp

# PHASE 6: Queue (after vote succeeds)
# ====================================
# Check state is 4 (Succeeded)
sage governance status $PROPOSAL_ID --subdao 0xSUBDAO
# Expected: State: Succeeded

# Queue the proposal
sage governance queue $PROPOSAL_ID --subdao 0xSUBDAO
# Expected: ✔ Proposal queued

# PHASE 7: Execute (after timelock delay)
# ======================================
# Check state is 5 (Queued) and ETA has passed
sage governance status $PROPOSAL_ID --subdao 0xSUBDAO
# Expected: State: Queued, ETA: <timestamp>

# Execute the proposal
sage governance execute $PROPOSAL_ID --subdao 0xSUBDAO
# Expected: ✔ Proposal executed

# Alternative: Auto-wait and execute
sage governance watch $PROPOSAL_ID --subdao 0xSUBDAO
# This waits for state changes and auto-queues/executes
```

**Error Recovery:**

| Error | Solution |
|-------|----------|
| `insufficient voting power` | Ensure you hold enough SXXX, delegate to self (`sxxx delegate-self`), wait 1 block |
| `proposal already exists` | Check `governance last` for existing ID |
| `proposal not active` | Check `governance status` - may have ended |
| `timelock: operation is not ready` | Wait for ETA to pass |
| `NaN` with large proposal ID | Use `vote-with-reason` instead of `vote` |
| `query exceeds max block range` | CLI should auto-fallback to subgraph |
</agent_complete_example>
