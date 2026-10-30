# Sage library change proposal: task guide

Open the section for the current step. The entrypoint keeps the authority rules.

## Worked examples

- **Use:** Repeated sanitized Hermes and Codex cards show agents cannot find a
  Sage P2P capability. Search prior art, attach aggregate card IDs and confidence,
  draft the smallest library diff plus tests, and leave status at `proposed`.
- **Do not mutate:** A popular social post says a skill is essential. Treat
  popularity as discovery only; inspect the artifact, seek execution evidence,
  and draft rather than execute a governed change.

## Inputs

Allowed evidence includes:

- sanitized cross-harness session cards
- Sage suggestion/use/outcome summaries
- curator reports and proposal inbox entries
- repository issues, tests, and concrete artifacts
- chat requests and social search results
- bounty submissions and independent attestations

Raw transcripts, secrets, private prompts, and personal data are not proposal
payloads. Preserve references or aggregate counts instead of copying content.

## Workflow

1. **Classify the signal** as repeated use, failure, missing capability,
   discoverability miss, stale content, unsafe content, duplicate capability, or
   collaboration opportunity.
2. **Search before drafting** with Sage local/remote skill, behavior, and library
   discovery. Inspect close candidates. A retrieval miss is not proof of absence.
3. **Choose the smallest change:** reuse, expose, retag, patch, add an example,
   compose a behavior, fork, archive, or create a new asset.
4. **Choose the intended surface:** local/private, trusted P2P, shared, public,
   paid, or governed. Default to local/private when intent is not explicit.
5. **Draft the exact delta and verification plan.** Keep content and metadata
   changes visible. Include behavior dependency resolution when applicable.
6. **Attach evidence quality:** freshness, source diversity, confidence, privacy
   classification, contradictory evidence, and whether any execution outcome was
   actually observed.
7. **Request the correct approval.** Agent-lead approval may authorize only the
   policy scope it names; it cannot imply wallet, public, paid, or governance
   authority.

## Proposal schema

```json
{
  "schema_version": 1,
  "proposal_id": "library-change-<stable-id>",
  "status": "proposed",
  "target": {
    "library": "<library>",
    "base_version": "<version-or-cid>",
    "key": "<skill-or-behavior-key>"
  },
  "change": {
    "kind": "reuse|expose|patch|add|compose|archive",
    "summary": "<smallest useful delta>",
    "draft_path": "<local path or null>",
    "expected_diff": "<human-readable diff summary>"
  },
  "evidence": {
    "sanitized_refs": [],
    "aggregate_counts": {},
    "execution_outcomes": [],
    "social_or_chat_leads": [],
    "contradictions": [],
    "freshness": "<window>",
    "confidence": 0.0
  },
  "prior_art": [],
  "verification": {
    "commands": [],
    "acceptance": [],
    "rollback": "<path>"
  },
  "authority": {
    "requested_scope": "local_private",
    "required_approvers": [],
    "forbidden_without_operator": ["public", "paid", "governed", "wallet"]
  },
  "council": {
    "verdicts": [],
    "unresolved_objections": []
  }
}
```

## Decision rules

- One session or one social post normally produces a lead, not a mutation.
- Repeated cross-session evidence can justify a proposal, not automatic approval.
- If an existing skill is close, prefer patch/fork/behavior composition over a
  duplicate key.
- Behavior changes should name component skills and validation commands.
- Public collaboration summaries must be independently scrubbed even when the
  source cards were already sanitized.
- A proposal becomes stale when the target base version/CID changes; rebase and
  re-review it rather than applying it optimistically.

## Present the decision

When proposal communication is authorized, give the proposal one short decision
post in its owning thread. State the proposed change, why it matters, the target
and exact base version, the proposed revision, the strongest verified evidence,
the unresolved objection or evidence gap, and the one decision needed from its
owner. State the tested runtime version when command behavior is evidence. Link
the reviewable artifact; keep the full typed payload and diagnostics in replies
or an authorized linked artifact, not the opening post.

Name the approval being requested: research, an exact change, publication, or
adoption. One does not imply the others. Silence is not approval. Preserve dissent
and acknowledge a hold, narrowing, rejection, or revision before continuing.

Keep material revisions in the same thread and identify the revision they
replace. Scope, evidence, risk, cost, or a changed decision can justify a new
decision post. Wording-only edits and unchanged blockers do not. Do not open a
competing thread or repeat the ask because no one answered.

For Buzz, load `buzz-contextual-conversation` for the decision-post and notifier
procedure. Where the operator has authorized Rook notifications, mention Rook
once on a review-ready post or material revision and link the owning thread.
Missing review material is not review-ready. Notification is not approval or
proof of delivery, and this procedure grants no posting or publication authority.

## Output

Return the completed proposal, unresolved questions, and the exact next approval
or evidence step. Do not run the mutation.
