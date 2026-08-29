# Experience compilation contract

Use Sage records as the evidence authority, Markdown as the reviewed synthesis,
and YAMS as the local retrieval index. IPFS may distribute the reviewed skill
package. YAMS retrieval does not make a note authoritative.

## Sources

- WikiSkill paper: https://arxiv.org/abs/2608.27454
- YAMS repository: https://github.com/trvon/yams
- Sage examples, rejected examples, outcomes, refinement proposals, and
  evaluations for the exact target skill version
- Sanitized, aggregate local evidence when the operator has approved those
  inputs

## Evidence brief

A refinement brief contains:

```yaml
target:
  library: <library>
  skill: <skill-key>
  base_version: <version-or-manifest-cid>
  content_hash: <exact-content-hash>
evidence:
  refs: []
  digests: []
  freshness: <window>
  source_diversity: <count-and-kinds>
  exact_version_rows: <count>
pattern:
  recurring: <bounded-observation>
  scope:
    harnesses: []
    model_families: []
    task_families: []
    modules: []
  contradictions: []
  prior_interventions:
    accepted: []
    rejected: []
hypothesis:
  claim: <one-causal-claim>
  smallest_change: <one-bounded-delta>
  disconfirming_case: <case-that-should-fail-the-claim>
verification:
  fixtures: []
  baseline: <result>
  candidate: <result>
  independent_reproduction: <result-or-pending>
privacy:
  public_safe: false
  local_only_inputs: []
  excluded_content: []
```

A field may be unknown. Mark it unknown instead of inferring it. Counts without
version attribution stay historical.

## Aggregate compiler contract

`scripts/compile_evidence.py` accepts only roots named explicitly by the
operator. It may inspect:

- modification time, extension, and byte size for session files;
- sanitized nightly harvest, opportunity, and candidate JSON documents;
- the `skill_execution` and `rejected_examples` tables in a Sage metrics
  database opened in read-only mode.

The compiler emits aggregate counts, grouped execution evidence, input digests,
a privacy declaration, and limitations. It must not emit raw session content,
raw session paths, prompts, tool output, credentials, or reasoning blocks.

## DAO review criteria

A governed candidate is reviewable when:

1. its base version and candidate hash are exact;
2. current-version evidence is separate from historical evidence;
3. the candidate addresses a gap the base does not already handle;
4. fixtures cover the observed failure and a nearby disconfirming case;
5. a second harness reproduces the result;
6. every public artifact passes a privacy and provenance review;
7. rollback is defined;
8. accepted and rejected decisions return to Sage evidence records.

Voters should judge whether the candidate improves the decision made before a
skill mutation. More notes, more retrieval hits, or more proposal volume are not
success by themselves.
