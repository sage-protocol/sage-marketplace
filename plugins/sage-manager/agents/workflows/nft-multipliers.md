<objective>
Manage VotingMultiplierNFT: create tiers, mint NFTs, check voting power, and participate in auctions.
</objective>

<contract_background>
**VotingMultiplierNFT Contract**

The voting multiplier system is backed by `VotingMultiplierNFT.sol`. Key on-chain concepts:

**Multiplier Format (basis points):**
- `100` = 1x (no bonus)
- `150` = 1.5x multiplier
- `200` = 2x multiplier
- `300` = 3x multiplier
- `500` = 5x multiplier (MAX_MULTIPLIER)

**Tier Structure:**
```solidity
struct Tier {
    string name;        // e.g., "Founding Member"
    uint256 multiplier; // 100 = 1x, 200 = 2x
    uint256 maxSupply;  // 0 = unlimited
    uint256 minted;     // Current mint count
    uint256 price;      // Wei, 0 = admin-only
    address dao;        // DAO this tier belongs to
}
```

**Key Contract Functions:**
- `createTierViaGovernance(subdao, name, multiplier, maxSupply, price)` - Permissionless for any DAO (checks GOVERNANCE_ROLE)
- `mint(to, tierId, uri)` - MINTER_ROLE required
- `publicMint(tierId, uri)` - Only if tier.price > 0
- `getMultiplier(account, dao)` - Get account's multiplier for a DAO

**Security:**
- DAOs must be registered with the factory (`daoFactory.isSubDAO()`)
- Max 20 NFTs per account (prevents DoS in multiplier calculation)
- Multipliers are checkpointed on every transfer (prevents gaming)

**Required Environment Variables:**
```bash
VOTING_MULTIPLIER_NFT_ADDRESS=0x...    # VotingMultiplierNFT contract
SAGE_AUCTION_HOUSE_ADDRESS=0x...       # SageAuctionHouse (optional)
SUBDAO_FACTORY_ADDRESS=0x...           # Factory for DAO validation
```

**Contract Roles:**
- `DEFAULT_ADMIN_ROLE` - Can create tiers, grant roles
- `MINTER_ROLE` - Can mint to any address
- `GOVERNANCE_ROLE` - On SubDAO, allows tier creation via governance
</contract_background>

<why_multipliers>
**Problem**: In token governance, voting power equals token holdings. This creates two issues:
1. **Plutocracy** - Whoever buys the most tokens controls decisions
2. **No recognition** - Long-term contributors have the same voice as newcomers

**Solution**: VotingMultiplierNFT lets DAOs recognize valuable contributors with multiplied voting power.

**Use cases**:
- **Founding Members**: Early supporters who took risk get 2-3x voting power
- **Contributors**: People who complete bounties earn multiplier NFTs
- **Auction Winners**: Daily auctions fund the treasury while distributing influence
- **Reputation Tiers**: Different levels of trust = different multipliers

**Key insight**: NFTs are **transferable**. Contributors can sell their multiplier if they leave. New members can buy in via auctions. Influence flows to those who value it most.
</why_multipliers>

<how_it_works>
**Components**:

1. **VotingMultiplierNFT** - ERC721 NFT that stores multiplier values
   - Each NFT has a multiplier (100=1x, 150=1.5x, 200=2x)
   - Each NFT belongs to a specific DAO
   - Multiple NFTs stack multiplicatively: 1.5x × 1.25x = 1.875x
   - Max 5x multiplier (500), max 20 NFTs per account

2. **MultipliedVotes** - IVotes wrapper contract
   - Governor uses this instead of raw SXXX token
   - Automatically calculates: `effectiveVotes = baseVotes × multiplier`
   - Multipliers are checkpointed at every transfer (prevents gaming)

3. **SageAuctionHouse** - Nouns-style continuous auction
   - Mints 1 NFT per auction (e.g., every 24 hours)
   - 100% of proceeds go to DAO treasury
   - Anyone can settle ended auctions (incentivized by gas efficiency)

**Example**:
```
User has 1000 SXXX delegated to self
User owns "Founder" NFT (2x multiplier) for this DAO
User owns "Contributor" NFT (1.5x multiplier) for this DAO

Base votes: 1000
Multiplier: 2x × 1.5x = 3x (15000 basis points)
Effective votes: 3000
```

**Historical accuracy**: Multipliers are checkpointed at every NFT transfer. This prevents buying NFTs after a proposal is created to influence the vote.
</how_it_works>

<command_reference>
```
# Configuration & Status
sage nft doctor                                       # Check config and permissions
sage multiplier status --subdao 0x...                 # Check if DAO uses multipliers
sage multiplier describe --subdao 0x...               # Detailed multiplier config

# View Tiers & Voting Power
sage nft list-tiers --dao 0x...                       # List tiers for DAO
sage nft my-multiplier [--dao 0x...]                  # Check your multiplier
sage multiplier calculate [address] --subdao 0x...    # Full voting power breakdown

# Tier Creation (via governance)
sage nft tier create --name <n> --multiplier <m> --subdao 0x... \
  [--max-supply <n>] [--price <eth>] -y               # Propose new tier

# Minting
sage nft mint --tier <id> --to <addr> --uri <uri> -y  # MINTER role required
sage nft public-mint --tier <id> --uri <uri> -y       # If tier has price > 0

# Permissions
sage nft grant-role --role MINTER --to <addr> -y      # ADMIN role required

# Auctions (primary namespace)
sage auction status                                   # Current auction status
sage auction bid <amount>                             # Place bid (ETH)
sage auction settle                                   # Settle ended auction
sage auction info                                     # Auction house config
sage auction bids [-l <limit>]                        # Recent bids from subgraph
sage auction history [-l <limit>]                     # Past auction winners

# Alternative auction commands (via multiplier namespace)
sage multiplier auction status
sage multiplier auction bid <amount>
sage multiplier auction settle
```

**Multiplier values**: 100=1x, 150=1.5x, 200=2x, 300=3x, 500=5x (max)
</command_reference>

<process>
**Step 1: Check if your DAO uses multipliers**
```bash
sage multiplier status --subdao 0x...
```

If disabled, multipliers need to be enabled during DAO creation or via governance.

**Step 2: Check your current voting power**
```bash
# Quick check - your multiplier for this DAO
sage nft my-multiplier --dao 0x...

# Detailed breakdown - base votes, multiplier, effective votes
sage multiplier calculate --subdao 0x...
```

If you have 1x (no multiplier), you need to acquire an NFT for this DAO.

**Step 3: Acquire an NFT**

Option A - **Win an auction** (most common):
```bash
# Check current auction
sage auction status

# Place bid (must exceed reserve price or 5% above current bid)
sage auction bid 0.1

# After auction ends, anyone can settle (winner gets NFT)
sage auction settle
```

Option B - **Public mint** (if tier has price set):
```bash
# View available tiers
sage nft list-tiers --dao 0x...

# Mint from tier with price > 0
sage nft public-mint --tier 1 --uri "ipfs://..." -y
```

Option C - **Earn from MINTER/admin**:
```bash
# Complete bounties, earn reputation, or be granted by DAO admin
# MINTERs can mint to any address:
sage nft mint --tier 0 --to 0xRecipient --uri "ipfs://..." -y
```

**Step 4: Verify your voting power increased**
```bash
sage multiplier calculate --subdao 0x...
```
</process>

<creating_tiers>
**Tiers are created via governance proposals.** Anyone can propose; community votes.

```bash
sage nft tier create \
  --subdao 0x... \
  --name "Founder" \
  --multiplier 200 \
  --max-supply 50 \
  --price 0 \
  -y
```

This creates a governance proposal. After it passes and executes, the tier exists.

**Tier design guidance**:

| Tier Type | Multiplier | Max Supply | Price | Distribution |
|-----------|------------|------------|-------|--------------|
| **Founder** | 200-300 (2-3x) | 10-50 | 0 | Admin/auction only |
| **Contributor** | 150-200 (1.5-2x) | 100-500 | 0 | Minted for bounty completion |
| **Supporter** | 125-150 (1.25-1.5x) | 1000+ | 0.05 ETH | Public mint |
| **Auction** | 150-200 | Unlimited | 0 | Via SageAuctionHouse |

**Price = 0 means**:
- Admin/MINTER only (tier won't appear in public mint)
- Or distributed via auction (if auction house uses this tier)
</creating_tiers>

<auction_workflow>
**Auctions fund the treasury while distributing influence.**

SageAuctionHouse runs Nouns-style continuous auctions:
- Mints 1 NFT per auction period (e.g., every 24 hours)
- 100% of proceeds go to DAO treasury
- Extends auction if bid placed near end (time buffer)
- Anyone can settle ended auctions and start the next one

**Workflow**:
```bash
# 1. Check auction status
sage auction status

# Output shows:
# - Current NFT ID being auctioned
# - Current bid and bidder
# - Time remaining
# - Reserve price and min increment

# 2. Place a bid
sage auction bid 0.15

# Bid must be:
# - At least reserve price (if first bid)
# - At least 5% higher than current bid

# 3. Wait for auction to end
# If outbid, your ETH is automatically refunded

# 4. Settle and start next auction
sage auction settle

# Winner receives NFT, treasury receives ETH
# New auction starts automatically
```

**Viewing history**:
```bash
# Recent bids (requires subgraph)
sage auction bids -l 20

# Past auction winners
sage auction history -l 10
```
</auction_workflow>

<environment>
Required environment variables:
```bash
VOTING_MULTIPLIER_NFT_ADDRESS=0x...    # VotingMultiplierNFT contract
SAGE_AUCTION_HOUSE_ADDRESS=0x...       # SageAuctionHouse (for auctions)
SUBGRAPH_URL=https://...               # For auction history/bids queries
```

Set via `.env` or `sage config`.
</environment>

<when_to_use_multipliers>
**Use multipliers when**:
- You want to recognize founding members who took early risk
- Contributors earn lasting influence (not just tokens)
- You need ongoing treasury funding via auctions
- Reputation matters more than just capital

**Don't use multipliers when**:
- Pure token democracy is the goal
- Simplicity is paramount (adds complexity)
- DAO is very small (< 10 members)
- Short-lived governance needs

**Decision framework**:
```
┌─────────────────────────────────────────────┐
│ Does contribution history matter?           │
│   NO  → Skip multipliers, use plain tokens  │
│   YES ↓                                     │
├─────────────────────────────────────────────┤
│ Want ongoing treasury funding?              │
│   NO  → Create tiers, admin-mint only       │
│   YES → Deploy SageAuctionHouse             │
├─────────────────────────────────────────────┤
│ Want public mint option?                    │
│   NO  → Price = 0, MINTER distributes       │
│   YES → Set price > 0 on public tiers       │
└─────────────────────────────────────────────┘
```
</when_to_use_multipliers>

<success_criteria>
- [ ] Multiplier status checked for target DAO
- [ ] NFT contract configured (`sage nft doctor` passes)
- [ ] Tier(s) created via governance proposal
- [ ] NFT acquired (auction, public mint, or admin grant)
- [ ] Voting power multiplied (verified with `multiplier calculate`)
</success_criteria>
