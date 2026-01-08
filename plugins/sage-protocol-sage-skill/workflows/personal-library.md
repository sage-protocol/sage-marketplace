<objective>
Manage personal prompt libraries: vault (private/encrypted), personal (public wallet-owned), and personal marketplace (licensed content).
</objective>

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
| Type | Ownership | Governance | Use Case |
|------|-----------|------------|----------|
| Vault (on-chain personal) | Your EOA | Operator | Private or personal prompt libraries (on-chain) |
| Personal Marketplace | Your EOA | None | Licensed/premium prompt sales |
| DAO/SubDAO | DAO treasury | Proposals required | Community-managed libraries |
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

**Path C: Personal Marketplace (licensed/premium content)**

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
- [ ] Vault library created and pushed
- [ ] Personal registry created
- [ ] Free prompts published to IPFS + on-chain
- [ ] Premium content encrypted and priced
- [ ] Licenses purchasable
- [ ] Purchased content accessible
</success_criteria>
