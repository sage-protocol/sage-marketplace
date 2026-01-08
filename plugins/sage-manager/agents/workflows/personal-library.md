<objective>
Manage personal prompt libraries: vault (private/encrypted), personal (public wallet-owned), and personal marketplace (licensed content).
</objective>

<mcp_tools>
**MCP Tools (read-only, prefer when available)**

If scroll MCP is registered, use these for listing/searching:
- `mcp__scroll__list_libraries` → List all libraries (personal + vault + DAO)
- `mcp__scroll__search_prompts` → Search prompts by keyword or semantic query
- `mcp__scroll__trending_prompts` → Discover popular prompts
- `mcp__scroll__get_prompt` → Get full prompt content by key
- `mcp__scroll__builder_recommend` → Get AI recommendations for prompts

**CLI Commands (for writes)**
All publish, push, and delete operations use sage CLI:
- `sage library personal push` / `sage library vault push`
- `sage personal publish` / `sage personal premium publish`
- `sage library personal delete` / `sage library vault delete`

**Routing:**
```
List/Search prompts → MCP_FIRST: mcp__scroll__*, else: sage library personal list
Push/Publish prompts → Always: sage CLI (requires wallet signing)
```
</mcp_tools>

<vault_vs_personal>
**Understanding the Two Library Types:**

| Aspect | Personal Library | Vault Library |
|--------|------------------|---------------|
| **Visibility** | Public, discoverable | Private, encrypted |
| **Access** | Anyone can view manifest | Only owner can access |
| **Use Case** | Share prompts publicly | Store private prompts |
| **CLI Namespace** | `sage library personal` | `sage library vault` |
| **Auth** | SIWE signature | SIWE signature |
| **On-chain** | Yes (LibraryRegistry) | Yes (LibraryRegistry) |

**When to use Personal:**
- You want to share prompts with the community
- You're building a public portfolio of work
- You want others to be able to install your prompts via `sage install`

**When to use Vault:**
- Private prompt collections for personal use
- Work-in-progress prompts not ready for public
- Sensitive or proprietary content
- Encrypted storage with only your wallet able to decrypt

**Both require SIWE authentication** - you sign a message with your wallet to prove ownership. The difference is in visibility and encryption.
</vault_vs_personal>

<command_reference>
```
# Personal libraries (wallet-owned prompt collections, SIWE auth)
sage library personal create --name "My Prompts"      # Create personal library
sage library personal list                            # List your libraries
sage library personal info <id>                       # Get library details (includes manifestCid)
sage library personal push <id> --dir ./prompts       # Upload prompts to library
sage library personal delete <id>                     # Delete library

# Vault libraries (private/encrypted, same API as personal)
sage library vault create --name "My Vault"           # Create vault library
sage library vault list                               # List your vaults
sage library vault info <id>                          # Get vault details
sage library vault push <id> --dir ./prompts          # Upload to vault
sage library vault delete <id>                        # Delete vault

# View prompts inside a library (requires manifest download)
sage library personal info <id>                       # Get manifestCid
sage ipfs download <manifestCid>                      # Download manifest JSON to see prompt list

# Personal marketplace (licensed prompts)
sage personal create                                  # Create registry (once)
sage personal publish <key> --file <path> --tags "..."
sage personal list [--creator 0x...]                  # List prompts
sage personal my-licenses                             # Your licenses

# Premium commands
sage personal premium publish <key> --file <path> --price <n>
sage personal premium price <creator> <key>           # Check price
sage personal premium buy <creator> <key> -y          # Buy license
sage personal premium access <creator> <key>          # Decrypt content
sage personal premium unlist <key> -y                 # Remove listing
```
</command_reference>

<personal_vs_dao>
| Type | Storage | Governance | Discoverability | Use Case |
|------|---------|------------|-----------------|----------|
| **Personal Governance DAO** | On-chain (LibraryRegistry) | Operator mode (no voting) | Full on-chain (subgraph indexed) | Solo creators who want instant updates + full discoverability |
| Personal Library | Off-chain (IPFS Worker) | None | Public but limited | Simple public sharing (faster setup) |
| Vault Library | Off-chain (IPFS Worker, encrypted) | None | Private only | Private/encrypted prompt storage |
| Personal Marketplace | On-chain (MarketRegistry) | None | Marketplace only | Licensed/premium prompt sales |
| Community DAO | On-chain (LibraryRegistry) | Token voting required | Full on-chain | Community-managed libraries |

**Key distinction**:
- **Personal DAO** (`--governance personal`) = ON-chain, fully discoverable via subgraph, direct Timelock updates (no voting)
- **Personal Library** (`sage library personal`) = OFF-chain via IPFS Worker API, simpler but less discoverable

**Recommendation**: For solo creators who want full discoverability, use **Personal Governance DAO** (Path C below).
</personal_vs_dao>

<process>
**Path A: Personal Library (public, discoverable)**

Use personal libraries when you want to share prompts publicly.

```bash
# 1. Create a personal library
sage library personal create --name "My Public Prompts"

# 2. Push prompts from local directory
sage library personal push my-public-prompts --dir ./prompts

# 3. List your libraries
sage library personal list

# 4. Get library info (includes manifestCid for others to install)
sage library personal info my-public-prompts
```

Others can install your library:
```bash
sage install <your-wallet-address>  # or use library CID
```

---

**Path B: Vault Library (private, encrypted)**

Use vault libraries for private prompt collections only you can access.

```bash
# 1. Create a vault library
sage library vault create --name "My Private Vault"

# 2. Push prompts (encrypted storage)
sage library vault push my-private-vault --dir ./prompts

# 3. List your vaults
sage library vault list

# 4. Get vault info
sage library vault info my-private-vault
```

Vault content is encrypted and only accessible with your wallet signature.

---

**Path C: Personal Governance DAO (RECOMMENDED for full discoverability)**

Create a DAO in operator mode. Get full on-chain discoverability with instant updates - no voting required.

```bash
# 1. Create DAO + upload prompts in one command
sage library quickstart \
  --name "My Skills Library" \
  --from-dir ./prompts \
  --governance personal

# This creates:
# - SubDAO contract (your library address)
# - Timelock (for scheduling updates)
# - Alias saved (e.g., my-skills-library)

# 2. Publish updates (auto-detects operator mode, schedules directly via Timelock)
sage prompts publish --subdao my-skills-library --files ./prompts/new-skill.md --yes

# 3. With --exec flag, also auto-executes after timelock delay (usually 0 for personal)
sage prompts publish --subdao my-skills-library --files ./prompts/new-skill.md --yes --exec

# 4. Sync to scroll for local access
scroll library sync
```

**Why use Personal Governance DAO?**
- Full on-chain discoverability (indexed by subgraph, searchable via scroll)
- **No voting required** - operator mode uses direct Timelock scheduling
- Professional library structure (versioned manifests, CIDs)
- Can upgrade to community governance later if desired

---

**Path D: Personal Marketplace (licensed/premium content)**

Use the marketplace for selling prompts or distributing licensed content.

**Step 1: Create personal registry (one-time)**
```bash
sage personal create
```

**Step 2: Publish free prompts**
```bash
sage personal publish <key> \
  --file ./prompts/my-prompt.md \
  --tags "analysis,research"
```

**Step 3: List your prompts**
```bash
# Your prompts
sage personal list

# Another creator's prompts
sage personal list --creator 0x...
```
</process>

<premium_content>
**Publish premium (paid) content:**
```bash
sage personal premium publish <key> \
  --file ./prompts/premium-guide.md \
  --price 10
```

Content is encrypted. Buyers receive a license to decrypt.

**Check pricing:**
```bash
sage personal premium price <creator> <key>
```

Shows: base price, protocol fee, creator receives.

**Buy a license:**
```bash
sage personal premium buy <creator> <key> -y
```

**Access purchased content:**
```bash
sage personal premium access <creator> <key>
```

Decrypts and displays content you've licensed.

**View your licenses:**
```bash
sage personal my-licenses
```

**Unlist premium content:**
```bash
sage personal premium unlist <key> -y
```
</premium_content>

<creator_workflow>
Full creator workflow:
```bash
# 1. Create registry (once)
sage personal create

# 2. Create and test prompt locally
sage prompts new --kind prompt --name "trading-strategy"
# ... edit prompt ...

# 3. Publish as premium
sage personal premium publish trading-strategy \
  --file ./prompts/trading-strategy.md \
  --price 25

# 4. Check it's listed
sage personal list

# 5. Monitor sales via events/subgraph
```
</creator_workflow>

<success_criteria>
**For Personal Governance DAO (recommended):**
- [ ] DAO created with `sage library quickstart --governance personal`
- [ ] Prompts uploaded to IPFS
- [ ] Operator mode detected (output shows "Operator mode: scheduled" or "executed")
- [ ] Library synced to scroll (`scroll library sync`)
- [ ] Prompts discoverable via `scroll search_prompts`

**For Vault/Personal Library:**
- [ ] Vault library created and pushed
- [ ] Personal registry created
- [ ] Free prompts published to IPFS

**For Premium Marketplace:**
- [ ] Premium content encrypted and priced
- [ ] Licenses purchasable
- [ ] Purchased content accessible
</success_criteria>
