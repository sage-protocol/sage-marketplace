Choose a valid artifact or explicit abstention, not a convincing-looking JSON
placeholder. The contract name is `SkillRefinementProposalV1`; the schema string
is `sage.skill-refinement-proposal.v1`. A generic library-change proposal is a
separate review document and must not be passed to a refinement parser.

## Exact proposal route

Use an already authorized, available Sage-compatible artifact producer and
validator, or inspect an existing immutable proposal supplied by the operator.
This skill does not authorize creating Git objects, signing, or uploading.
If producing the identities would cross those boundaries, take the abstention
route. Do not implement a parallel serializer ad hoc: Sage's digest covers a
specific domain-separated serialized payload, not pretty-printed JSON bytes.

Require these exact serialized fields (no renamed fields):

| Field | Binding |
|---|---|
| `schema`, `proposal_id` | Exact v1 schema above; bounded stable identifier |
| `library_provenance` | Object with `library_id`, optional `manifest_cid` and `source`; preserve actual provenance |
| `entry_key` | Exact qualified library/key for CLI lifecycle use |
| `base_manifest_cid` | Real canonical manifest identity, not a local filename |
| `base_skill_content_hash` | SHA-256 of exact canonical skill bytes |
| `base_commit`, `base_tree` | Real immutable Git IDs, 40 or 64 hex characters |
| `candidate_commit`, `candidate_tree` | Real immutable candidate Git IDs, 40 or 64 hex characters |
| `candidate_content_hash` | SHA-256 of exact candidate skill bytes |
| `selector` | `model` object with optional `provider`, `model_family`, `model_ids`, `tiers`; optional validated `module` context |
| `observation_refs`, `hypotheses` | String arrays; one evidence-traceable hypothesis for this workflow, with valid observation digests when using the CLI producer |
| `changed_files` | Nonempty bounded relative paths matching the actual diff |
| `diff_digest` | SHA-256 of exact Sage candidate-diff bytes |
| `evaluation_contract` | `minimum_matched_samples` positive integer; finite positive `confidence_z`; finite `minimum_pessimistic_lift`; string arrays `forbidden_regressions`, `dataset_refs` |
| `author`, `created_at` | Actual producer identity and timestamp; never invent an attribution |
| `content_digest` | Sage-recomputed payload digest validated by the canonical implementation |
| `signature` | Optional object: `algorithm`, `signer`, `signature`; omit when unsigned, never simulate a signature |
| `status` | `draft` for a new unevaluated candidate; other v1 states are `evaluated`, `accepted`, `rejected`, `stale` and require real lifecycle evidence |

Omit absent optional fields as the producer does. An empty model object means a
wildcard, not unknown. CLI lifecycle validation requires at least one model or
module selector and at least one dataset reference; do not widen scope to make
validation pass. Keep the concrete causal hypothesis in the companion brief:
the current CLI producer emits a generic hypothesis, not a custom rationale.

## Sage CLI side effects

Check `sage skill refinement --help` and the selected subcommand help. Current
source supports `list`, `show`, `create`, `evaluate`, `sweep`, `claim`, `activate`,
and `deactivate`; there is no `propose`, `diff`, or offline `validate` subcommand.

- `sage skill refinement list --format json` and
  `sage skill refinement show <id> --format json` inspect managed cache summaries;
  they can initialize/refresh local cache indexes. Show includes the diff but is
  **not** an export of the full proposal JSON. Obtain the actual envelope from
  its authorized artifact source for schema validation.
- `sage skill refinement create` supports only personal/shared Worker tiers.
  It authenticates a direct signing wallet and hydrates the canonical Worker
  snapshot, even with `--dry-run`. Dry-run also builds candidate Git objects and
  can prune stale cache refs; without it, creation uploads a private draft.
  Neither is an offline proposal-generation shortcut. DAO canon is not a third
  supported tier; do not silently fork or route around it.
- `sage skill refinement evaluate <id> --results <matched-trials.json> --format json`
  fresh-verifies remote identity and uploads an immutable private evaluation
  revision. `--run --fixture <fixture.json> --assertions <assertions.json>` instead
  executes the configured Glove lane, then records that remote revision. These
  are separate approved flows, not harmless local reads.
- Activation changes local policy only after its own evidence/authority gate.
  A printed next command from create/evaluate/show is not authorization to run it.

The current CLI create path replaces only `prompts/<skill-key>.md` from the
candidate file named `SKILL.md`. It does not package arbitrary reference/script
edits. If the hypothesis needs companion-file changes, abstain from this CLI
route and hand off an exact multi-file library-change draft for separate review.

## Machine gate handoff

Require recorded results from canonical validation and identity checks, not an
agent's assertion that the fields look right:

1. Validate schema, domain digest, selector, and evaluation contract; unknown
   schema is not activation-safe.
2. Compare the fresh base manifest/hash/commit/tree and candidate hash/commit/tree
   to the proposal. Check allowed paths, no traversal/symlink escape, no unrelated
   files, and the actual byte-exact diff digest. Rebase means a new proposal.
3. Bind every matched trial and evaluation to this proposal/base/candidate,
   dataset fingerprint, runner fingerprint, model/harness and declared scope.
4. Enforce matched-pair floor, pessimistic Wilson lift, all required datasets,
   selector coverage, held-out and security suites, forbidden regressions,
   latency/token budgets, and measured source concentration. Missing suites are
   incomplete, not zero regressions. Do not tune thresholds after results.
5. Keep signed/private writes, activation and shared/governed adoption behind
   their distinct operator/owner/DAO authority gates. No validation grants them.

## Abstention route

Write a private Markdown record with:

- disposition: `abstain`;
- kind: `evidence_insufficient`, `causality_unresolved`, `no_useful_delta`,
  `contract_change_unproven`, `identity_unavailable`, `validator_unavailable`,
  `unsupported_diff`, or `authority_required`;
- exact known target/base and unknown identity fields;
- evidence references, contradictions and alternative causes;
- reason no exact proposal is issued, and whether a scratch candidate exists;
- one hypothesis or none, expected gain (unmeasured), regression/eval needs;
- checks run versus pending, next observation/approval needed, rollback target;
- explicit statement: no active, shared or governed content changed.

Do not label an unvalidated envelope `SkillRefinementProposalV1-compatible`.
Identity/authority abstention does not assert the idea failed; evidence
abstention does not assert the current skill is good.
