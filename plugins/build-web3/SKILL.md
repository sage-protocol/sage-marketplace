---
name: build-web3
description: Build Web3 dApps and smart contracts from scratch through shipping. Full lifecycle for EVM/Base development with Solidity, Foundry, Next.js, and viem/wagmi. Covers contracts, frontend, testing, security analysis, and deployment.
---

<essential_principles>

## How Web3 Development Works

These principles apply to ALL workflows in this skill.

### 1. Contracts Are Immutable - Test First

Once deployed, smart contracts cannot be changed (unless using proxy patterns). This means:
- Write comprehensive tests BEFORE deployment
- Use fuzz testing and invariant testing in Foundry
- Security vulnerabilities can drain millions - treat every contract as critical
- Always verify contracts on block explorers after deployment

### 2. Gas Costs Money

Every computation costs ETH. Optimize aggressively:
- Pack storage variables (use uint96 instead of uint256 when possible)
- Use `calldata` instead of `memory` for read-only function parameters
- Batch operations when possible
- Avoid loops with unbounded iterations

### 3. Frontend Needs Wallet Context

Web3 frontends differ from traditional apps:
- All state-changing operations require wallet signatures
- Users can reject transactions at any time
- Network switching and wallet disconnection must be handled gracefully
- Always show transaction status and confirmations

### 4. Events Are Your API

Smart contracts emit events - these are your primary data source:
- Index events with The Graph for efficient queries
- Emit all data needed for frontend/indexing (avoid eth_calls)
- Events are cheaper than storage reads

</essential_principles>

<intake>
**What would you like to do?**

1. Build a smart contract
2. Build a dApp frontend
3. Debug an issue
4. Write/run tests
5. Analyze security
6. Ship (deploy)
7. Something else

**Wait for response before proceeding.**
</intake>

<routing>
| Response | Workflow |
|----------|----------|
| 1, "contract", "solidity", "smart contract" | `workflows/build-contract.md` |
| 2, "dapp", "frontend", "next", "ui", "web" | `workflows/build-dapp.md` |
| 3, "debug", "fix", "bug", "error", "broken" | `workflows/debug.md` |
| 4, "test", "tests", "fuzz", "coverage" | `workflows/test.md` |
| 5, "security", "audit", "analyze", "vulnerability" | `workflows/analyze.md` |
| 6, "deploy", "ship", "verify", "mainnet", "testnet" | `workflows/ship.md` |
| 7, other | Clarify, then select workflow |

**After reading the workflow, follow it exactly.**
</routing>

<verification_loop>
## After Every Change

**For contracts:**
```bash
# 1. Compile
forge build

# 2. Run tests
forge test -vvv

# 3. Check gas
forge test --gas-report
```

**For frontend:**
```bash
# 1. Type check
npx tsc --noEmit

# 2. Build
npm run build

# 3. Run locally
npm run dev
```

Report results to user before proceeding.
</verification_loop>

<reference_index>
## Domain Knowledge

All in `references/`:

**Architecture:** architecture.md - Diamond pattern, project structure, tech stack
**Patterns:** solidity-patterns.md - Best practices, Foundry, testing, optimization
**Avoid:** anti-patterns.md - Common mistakes, security vulnerabilities
</reference_index>

<workflows_index>
## Workflows

All in `workflows/`:

| File | Purpose |
|------|---------|
| build-contract.md | Create/modify Solidity smart contracts |
| build-dapp.md | Create/modify Next.js frontend with wallet integration |
| debug.md | Debug contracts and frontend issues |
| test.md | Write and run tests (unit, fuzz, invariant) |
| analyze.md | Security analysis and vulnerability detection |
| ship.md | Deploy contracts and frontend to testnet/mainnet |
</workflows_index>
