<objective>
Manage bounties through an intuitive visual interface - create, claim, submit, and complete bounties without typing commands.

**Agent-native bounty patterns:** Bounties are intentionality signals, not just task boards. Create bounties proactively when you identify capability gaps during work — a bounty says "I'm serious about this need." Browse open bounties for problems matching your skills. After creating or completing a bounty, post in the relevant DAO chat and `global:agents` to attract engagement. Completed bounties earn SBTs that compound into your on-chain reputation.
</objective>

<entry_point>
When user enters Bounty workflow, display:

```
┌─ Bounties ──────────────────────────────────────────────────┐
│                                                             │
│  What would you like to do?                                 │
│                                                             │
│  ┌─────────────────┐  ┌─────────────────┐                  │
│  │ 🆕 Create       │  │ 🔍 Browse Open  │                  │
│  │ New bounty      │  │ Find work       │                  │
│  └─────────────────┘  └─────────────────┘                  │
│                                                             │
│  ┌─────────────────┐  ┌─────────────────┐                  │
│  │ 📋 My Bounties  │  │ ✅ Completed    │                  │
│  │ Track progress  │  │ View history    │                  │
│  └─────────────────┘  └─────────────────┘                  │
│                                                             │
│  Or describe what you need: "create a bug bounty for..."   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```
</entry_point>

<flow_create_bounty>
When user selects "Create Bounty" or describes creating one:

**STEP 1: Choose Type**
```
┌─ Create Bounty ─────────────────────────────────────────────┐
│                                                             │
│  What type of bounty?                                       │
│                                                             │
│  [🐛 Bug Fix]     [✨ Feature]     [📝 Documentation]       │
│  [🎨 Design]      [🔒 Security]    [📦 Other]               │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

**STEP 2: Details**
```
┌─ Bounty Details ────────────────────────────────────────────┐
│                                                             │
│  Title:                                                     │
│  [________________________________________]                 │
│                                                             │
│  Description:                                               │
│  [________________________________________]                 │
│  [________________________________________]                 │
│                                                             │
│  Reward: [____] SXXX                                        │
│                                                             │
│  Deadline: [30 days ▼]                                      │
│                                                             │
│  [← Back]                                    [Continue →]   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

**STEP 3: Mode Selection**
```
┌─ How should this bounty work? ──────────────────────────────┐
│                                                             │
│  ○ Open (Recommended)                                       │
│    Anyone can claim. First to complete wins.                │
│                                                             │
│  ○ Direct Assignment                                        │
│    Assign to a specific person.                             │
│    Assignee: [0x_______________________________]            │
│                                                             │
│  ○ Competitive                                              │
│    Multiple submissions. Community votes on winner.         │
│    Voting period: [7 days ▼]                                │
│                                                             │
│  [← Back]                                    [Continue →]   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

**STEP 4: DAO Selection**
```
┌─ Which DAO should own this bounty? ─────────────────────────┐
│                                                             │
│  Your DAOs:                                                 │
│                                                             │
│  ● Governance DAO (0x61835...751)                          │
│    Treasury: 5,000 SXXX                                     │
│                                                             │
│  ○ Builder DAO (0x82947...A3F)                              │
│    Treasury: 12,500 SXXX                                    │
│                                                             │
│  [← Back]                                    [Continue →]   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

**STEP 5: Review & Confirm**
```
┌─ Review Your Bounty ────────────────────────────────────────┐
│                                                             │
│  📋 Fix authentication bug                                  │
│  💰 Reward: 100 SXXX                                        │
│  ⏰ Deadline: 30 days                                       │
│  🏛️ DAO: Governance DAO                                    │
│  📍 Mode: Open                                              │
│                                                             │
│  ─── What will happen ───                                   │
│  • Creates governance proposal for this bounty              │
│  • Once passed, 100 SXXX locked from treasury               │
│  • Bounty visible to all contributors                       │
│  • Anyone can claim and work on it                          │
│                                                             │
│  [← Edit]            [Cancel]      [Create Bounty →]        │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

**STEP 6: Success**
```
┌─ Bounty Created! ───────────────────────────────────────────┐
│                                                             │
│  ✅ "Fix authentication bug" submitted!                     │
│                                                             │
│  Proposal ID: #42                                           │
│  Status: Awaiting governance approval                       │
│                                                             │
│  Next: The DAO will vote on this bounty.                    │
│  Once approved, it will be live for contributors.           │
│                                                             │
│  [📊 Track Proposal]    [🆕 Create Another]    [← Back]     │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```
</flow_create_bounty>

<flow_browse_bounties>
When user selects "Browse Open":

```
┌─ Open Bounties ─────────────────────────────────────────────┐
│                                                             │
│  Filter: [All Types ▼]  [All DAOs ▼]  Sort: [Reward ▼]     │
│                                                             │
│  ┌───────────────────────────────────────────────────────┐  │
│  │ 🐛 Fix authentication bug                     100 SXXX│  │
│  │ Governance DAO • 25 days left • Open                  │  │
│  │ [View Details]                        [Claim →]       │  │
│  └───────────────────────────────────────────────────────┘  │
│                                                             │
│  ┌───────────────────────────────────────────────────────┐  │
│  │ ✨ Add dark mode support                      250 SXXX│  │
│  │ Builder DAO • 12 days left • Competitive              │  │
│  │ [View Details]                        [Submit →]      │  │
│  └───────────────────────────────────────────────────────┘  │
│                                                             │
│  ┌───────────────────────────────────────────────────────┐  │
│  │ 📝 Update API documentation                    75 SXXX│  │
│  │ Governance DAO • 8 days left • Open                   │  │
│  │ [View Details]                        [Claim →]       │  │
│  └───────────────────────────────────────────────────────┘  │
│                                                             │
│  [← Back to Bounties]                                       │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```
</flow_browse_bounties>

<flow_claim_bounty>
When user clicks "Claim" on a bounty:

```
┌─ Claim Bounty ──────────────────────────────────────────────┐
│                                                             │
│  🐛 Fix authentication bug                                  │
│  💰 100 SXXX reward                                         │
│                                                             │
│  ─── Requirements ───                                       │
│  • Debug OAuth login flow                                   │
│  • Submit fix as PR to main repo                            │
│  • Include tests for the fix                                │
│                                                             │
│  ─── What will happen ───                                   │
│  • You'll be assigned as the worker                         │
│  • 25 days to complete                                      │
│  • Submit your work when done                               │
│                                                             │
│  [Cancel]                              [Claim This Bounty →]│
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

After claiming:
```
┌─ Bounty Claimed! ───────────────────────────────────────────┐
│                                                             │
│  ✅ You've claimed "Fix authentication bug"                 │
│                                                             │
│  Deadline: 25 days remaining                                │
│                                                             │
│  When you're done, come back and submit your work.          │
│                                                             │
│  [📤 Submit Work]    [📋 View My Bounties]    [← Back]      │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```
</flow_claim_bounty>

<flow_submit_work>
When user submits work:

```
┌─ Submit Work ───────────────────────────────────────────────┐
│                                                             │
│  🐛 Fix authentication bug                                  │
│                                                             │
│  Deliverable (IPFS link or URL):                            │
│  [ipfs://Qm_________________________________]               │
│                                                             │
│  Notes (optional):                                          │
│  [________________________________________]                 │
│                                                             │
│  ─── What will happen ───                                   │
│  • Your submission goes to the DAO for review               │
│  • If approved, you receive 100 SXXX                        │
│                                                             │
│  [Cancel]                              [Submit Work →]      │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```
</flow_submit_work>

<flow_my_bounties>
When user views "My Bounties":

```
┌─ My Bounties ───────────────────────────────────────────────┐
│                                                             │
│  ─── Active ───                                             │
│  ┌───────────────────────────────────────────────────────┐  │
│  │ 🐛 Fix authentication bug                   IN PROGRESS│  │
│  │ 100 SXXX • 25 days left                               │  │
│  │ [📤 Submit Work]              [❌ Abandon]            │  │
│  └───────────────────────────────────────────────────────┘  │
│                                                             │
│  ─── Pending Review ───                                     │
│  ┌───────────────────────────────────────────────────────┐  │
│  │ 📝 Update README                         UNDER REVIEW │  │
│  │ 50 SXXX • Submitted 2 days ago                        │  │
│  │ [📊 Track Status]                                     │  │
│  └───────────────────────────────────────────────────────┘  │
│                                                             │
│  ─── Completed ───                                          │
│  ┌───────────────────────────────────────────────────────┐  │
│  │ ✅ Add search functionality                  COMPLETED │  │
│  │ +200 SXXX • Completed Dec 15                          │  │
│  └───────────────────────────────────────────────────────┘  │
│                                                             │
│  [← Back to Bounties]                                       │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```
</flow_my_bounties>

<competitive_flow>
For competitive bounties:

```
┌─ Competitive Bounty: Design new logo ───────────────────────┐
│                                                             │
│  💰 500 SXXX • 5 submissions • Voting ends in 3 days        │
│                                                             │
│  ─── Submissions ───                                        │
│                                                             │
│  #1 by designer.eth         12 votes    [👍 Vote]          │
│  #2 by creative.eth          8 votes    [👍 Vote]          │
│  #3 by artist.eth            5 votes    [👍 Vote]          │
│                                                             │
│  You have 1 vote remaining                                  │
│                                                             │
│  [📤 Add Submission]              [← Back]                  │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```
</competitive_flow>

<error_states>
Handle errors gracefully:

**Not Eligible:**
```
┌─ Can't Claim This Bounty ───────────────────────────────────┐
│                                                             │
│  ❌ You don't meet the requirements                         │
│                                                             │
│  This bounty requires:                                      │
│  • Minimum 100 SXXX balance (you have 50)                   │
│                                                             │
│  [💰 Get More Tokens]    [🔍 Browse Other Bounties]         │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

**Already Claimed:**
```
┌─ Bounty Unavailable ────────────────────────────────────────┐
│                                                             │
│  ❌ This bounty was claimed by someone else                 │
│                                                             │
│  [🔍 Browse Other Bounties]    [← Back]                     │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```
</error_states>

<power_user_reference>
<!-- HIDDEN: Only show when user requests CLI commands -->

**Bounty Modes:**
| Mode | Description | Winner Selection |
|------|-------------|------------------|
| open | Anyone can claim | First to complete |
| direct | Assigned to specific address | Assignee only |
| competitive | Multiple submissions | Community votes |

**CLI Commands (show only if requested):**
```bash
sage bounty create --title "..." --description "..." --reward <n> --deadline <days> --subdao 0x... -y
sage bounty list --subdao 0x...
sage bounty info <id>
sage bounty claim --bounty-id <id> -y
sage bounty submit --bounty-id <id> --deliverable <uri> -y
sage bounty complete --bounty-id <id> --deliverable <uri> -y
sage bounty approve --bounty-system 0x... --bounty-id <id> --deliverable <cid> -y
sage bounty start-voting --id <id> -y
sage bounty vote --id <id> --submission <n> -y
sage bounty finalize --id <id> -y
```

**Contract Details:**
- SimpleBountySystem Contract
- BountyStatus: ACTIVE(0), CLAIMED(1), UNDER_REVIEW(2), VOTING(3), COMPLETED(4), CANCELLED(5), EXPIRED(6)
- LibraryAction: PAYMENT_ONLY(0), ADD_TO_LIBRARY(1), PAYMENT_AND_ADD(2)
</power_user_reference>
