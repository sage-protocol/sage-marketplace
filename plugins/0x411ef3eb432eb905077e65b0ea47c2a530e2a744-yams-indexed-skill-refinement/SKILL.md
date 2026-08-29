---
name: yams-indexed-skill-refinement
description: "Use before changing a repeatedly used skill when Sage outcomes and prior YAMS notes must become one bounded, testable refinement hypothesis."
license: MIT
metadata:
  version: "0.1.0"
  author: sage-protocol
  source_paper: https://arxiv.org/abs/2608.27454
  yams_repository: https://github.com/trvon/yams
  tags: [sage-protocol, yams, skills, refinement, evaluation, governance]
---

Start with one named skill and its exact current content hash. Stop if the exact
version cannot be identified. Historical outcomes without a content hash may
inform a hypothesis, but they cannot justify changing the current version.

## Compile the evidence

1. Search exact project memory first:

   ```bash
   yams grep "<skill-key>" --cwd .
   yams search "<skill-key> <observed-failure-pattern>" --limit 10
   ```

   Hydrate the one to three relevant records returned by search:

   ```bash
   yams cat --hash <hash>
   ```

   Treat retrieved notes as leads. Check every claim against current skill
   content, current code, and Sage records.

2. Read the current Sage evidence for the target:

   ```bash
   sage skill example list <skill-key> --format json
   sage suggest feedback breakdown <skill-key> --content-hash <content-hash> --format json
   sage skill refinement list --format json
   ```

   Separate accepted examples, rejected examples, passed outcomes, failed
   outcomes, revised outcomes, and pending refinement proposals. Keep results
   from other content hashes in a historical section.

3. When aggregate local evidence is needed, run
   `scripts/compile_evidence.py` with explicitly approved roots and output path.
   The script reads file metadata, sanitized nightly summaries, and a read-only
   Sage metrics database. It does not read raw session text. Inspect its privacy
   block and limitations before using the result.

4. Write a private scratch brief with these fields:

   - target skill, library, and exact base content hash;
   - evidence references and digests;
   - recurring pattern;
   - contradictory evidence;
   - model family, harness, task family, and module scope when known;
   - prior accepted and rejected interventions;
   - one current hypothesis;
   - one disconfirming case;
   - the smallest candidate change;
   - fixed fixtures and acceptance threshold.

## Decide whether to change the skill

Keep the current skill when it already handles the observed failure, when the
failure is not attributable to the exact version, or when the candidate cannot
beat a matched baseline. Record why no mutation was warranted. A repeated
proposal count is not proof that another patch is needed.

When a testable gap survives, change one bounded candidate in a scratch copy.
Run the same fixed fixtures against the base and candidate. Include clean input,
the observed failure, a nearby non-failure, and one case that should reject the
candidate's hypothesis. Require independent reproduction in a second harness
before proposing a shared or governed update.

## Prepare the governance candidate

Submit only the reviewed synthesis, portable fixtures, aggregate digests, and
portable code. Keep raw sessions, private prompts, credentials, personal paths,
and unreviewed evidence outside the library and IPFS.

The candidate must name:

- exact base library version or manifest CID;
- exact base and candidate content hashes;
- evidence and contradiction references;
- benchmark and independent reproduction results;
- privacy classification;
- rollback path;
- what remains local-only.

After an accepted or rejected decision, record the outcome in Sage. Update a
YAMS-indexed Markdown synthesis only when the result changes a reusable lesson.
Link rejected interventions so later agents do not silently repeat them.

## Completion

The run is complete when another agent can reproduce the evidence selection,
compare the exact base and candidate on the same fixtures, and explain why the
result warrants mutation, rejection, or no change without reading private raw
sessions.

Read `references/experience-compilation.md` for the evidence contract, privacy
boundary, and DAO review criteria.
