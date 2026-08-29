#!/usr/bin/env python3
"""Compile private aggregate evidence for one Sage skill refinement.

The caller must name every local input explicitly. The output contains counts,
digests, grouped outcomes, privacy declarations, and limitations. It never
copies raw session text or raw source paths into the artifact.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import sqlite3
import time
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

SESSION_SUFFIXES = {".json", ".jsonl"}
ISSUE_TERMS = (
    "wrapper",
    "contamination",
    "metadata",
    "duplicate",
    "boilerplate",
    "sparse",
    "untrusted",
    "project path",
    "source path",
    "session index",
)


def sha256_bytes(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def canonical_json(value: Any) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":")).encode("utf-8")


def parse_named_root(value: str) -> tuple[str, Path]:
    name, separator, raw_path = value.partition("=")
    if not separator or not name.strip() or not raw_path.strip():
        raise argparse.ArgumentTypeError("expected NAME=PATH")
    return name.strip(), Path(raw_path).expanduser()


def inventory_sessions(roots: list[tuple[str, Path]], cutoff: float) -> dict[str, Any]:
    inventory: dict[str, Any] = {}
    for source, root in roots:
        files = 0
        size_bytes = 0
        errors = 0
        if root.exists():
            for path in root.rglob("*"):
                if not path.is_file() or path.suffix not in SESSION_SUFFIXES:
                    continue
                try:
                    stat = path.stat()
                except OSError:
                    errors += 1
                    continue
                if stat.st_mtime < cutoff:
                    continue
                files += 1
                size_bytes += stat.st_size
        inventory[source] = {
            "root_present": root.exists(),
            "files": files,
            "size_bytes": size_bytes,
            "stat_errors": errors,
        }
    return inventory


def load_json(path: Path) -> Any | None:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError):
        return None


def timestamped_json_files(root: Path, prefix: str, cutoff: float) -> list[Path]:
    output: list[Path] = []
    if not root.exists():
        return output
    for path in root.glob(f"{prefix}*.json"):
        if path.name.endswith(("latest.json", "ranked.json")):
            continue
        try:
            if path.stat().st_mtime >= cutoff:
                output.append(path)
        except OSError:
            continue
    return sorted(output)


def aggregate_nightly(root: Path | None, cutoff: float, skill_key: str) -> dict[str, Any]:
    if root is None:
        return {"configured": False}

    harvest_files = timestamped_json_files(root, "harvest-", cutoff)
    opportunity_files = timestamped_json_files(root, "opportunities-", cutoff)
    candidate_files = timestamped_json_files(root, "improvement-candidates-", cutoff)

    scanned: Counter[str] = Counter()
    kept: Counter[str] = Counter()
    dropped: Counter[str] = Counter()
    drop_reasons: Counter[str] = Counter()
    issue_document_counts: Counter[str] = Counter()
    candidate_targets: Counter[str] = Counter()
    target_candidate_documents = 0
    readable_hashes: list[str] = []

    for path in harvest_files:
        value = load_json(path)
        if not isinstance(value, dict):
            continue
        readable_hashes.append(sha256_bytes(path.read_bytes()))
        for key, counter in (
            ("counts_scanned", scanned),
            ("counts_kept", kept),
            ("counts_dropped", dropped),
        ):
            rows = value.get(key)
            if isinstance(rows, dict):
                for source, count in rows.items():
                    if isinstance(count, int):
                        counter[str(source)] += count
        reasons = value.get("drop_reasons")
        if isinstance(reasons, dict):
            for reason, count in reasons.items():
                if isinstance(count, int):
                    drop_reasons[str(reason)] += count

    for path in opportunity_files:
        value = load_json(path)
        if value is None:
            continue
        readable_hashes.append(sha256_bytes(path.read_bytes()))
        searchable = json.dumps(value, ensure_ascii=False).lower()
        for term in ISSUE_TERMS:
            if term in searchable:
                issue_document_counts[term] += 1

    for path in candidate_files:
        value = load_json(path)
        if not isinstance(value, dict):
            continue
        readable_hashes.append(sha256_bytes(path.read_bytes()))
        candidates = value.get("candidates")
        if not isinstance(candidates, list):
            continue
        document_targets: set[str] = set()
        for candidate in candidates:
            if not isinstance(candidate, dict):
                continue
            target = candidate.get("target_skill") or candidate.get("target")
            if isinstance(target, str) and target:
                candidate_targets[target] += 1
                document_targets.add(target)
        if skill_key in document_targets:
            target_candidate_documents += 1

    return {
        "configured": True,
        "root_present": root.exists(),
        "harvest_documents": len(harvest_files),
        "opportunity_documents": len(opportunity_files),
        "candidate_documents": len(candidate_files),
        "source_counts": {
            "scanned": dict(scanned),
            "kept": dict(kept),
            "dropped": dict(dropped),
        },
        "drop_reasons": dict(drop_reasons.most_common()),
        "issue_document_counts": dict(issue_document_counts.most_common()),
        "candidate_target_counts": dict(candidate_targets.most_common(20)),
        "target_candidate_documents": target_candidate_documents,
        "input_set_digest": sha256_bytes("\n".join(sorted(readable_hashes)).encode("utf-8")),
        "readable_input_documents": len(readable_hashes),
    }


def table_columns(connection: sqlite3.Connection, table: str) -> set[str]:
    rows = connection.execute(f"PRAGMA table_info({table})").fetchall()
    return {str(row[1]) for row in rows}


def aggregate_sage(metrics_db: Path | None, cutoff_ms: int, skill_key: str) -> dict[str, Any]:
    if metrics_db is None:
        return {"configured": False}
    if not metrics_db.exists():
        return {"configured": True, "database_present": False}

    connection = sqlite3.connect(f"file:{metrics_db}?mode=ro", uri=True)
    connection.row_factory = sqlite3.Row
    limitations: list[str] = []
    try:
        execution_columns = table_columns(connection, "skill_execution")
        required = {"timestamp", "skill_key", "status", "source"}
        if not required.issubset(execution_columns):
            return {
                "configured": True,
                "database_present": True,
                "compatible_schema": False,
                "schema_digest": sha256_bytes(canonical_json(sorted(execution_columns))),
                "limitations": ["skill_execution is missing required aggregate columns"],
            }

        optional = {
            "failure_type": "''",
            "session_id": "NULL",
            "skill_content_hash": "NULL",
            "model_family": "NULL",
            "module_id": "NULL",
        }
        expressions = {
            column: column if column in execution_columns else fallback
            for column, fallback in optional.items()
        }
        for column in optional:
            if column not in execution_columns:
                limitations.append(f"skill_execution.{column} is unavailable")

        query = f"""
            SELECT status,
                   source,
                   COALESCE({expressions['failure_type']}, '') AS failure_type,
                   COUNT(*) AS executions,
                   COUNT(DISTINCT {expressions['session_id']}) AS sessions,
                   SUM(CASE WHEN {expressions['skill_content_hash']} IS NOT NULL THEN 1 ELSE 0 END) AS exact_content_rows,
                   SUM(CASE WHEN {expressions['model_family']} IS NOT NULL THEN 1 ELSE 0 END) AS normalized_model_rows,
                   SUM(CASE WHEN {expressions['module_id']} IS NOT NULL THEN 1 ELSE 0 END) AS module_rows
              FROM skill_execution
             WHERE timestamp >= ? AND skill_key = ?
             GROUP BY status, source, failure_type
             ORDER BY executions DESC
        """
        groups = [dict(row) for row in connection.execute(query, (cutoff_ms, skill_key))]

        rejected_columns = table_columns(connection, "rejected_examples")
        if "skill_key" in rejected_columns:
            rejected = int(
                connection.execute(
                    "SELECT COUNT(*) FROM rejected_examples WHERE skill_key = ?",
                    (skill_key,),
                ).fetchone()[0]
            )
        else:
            rejected = 0
            limitations.append("rejected_examples.skill_key is unavailable")

        schema_contract = {
            "skill_execution": sorted(execution_columns),
            "rejected_examples": sorted(rejected_columns),
        }
    finally:
        connection.close()

    totals: Counter[str] = Counter()
    sources: set[str] = set()
    for row in groups:
        count = int(row["executions"] or 0)
        totals["executions"] += count
        totals[str(row["status"])] += count
        totals["exact_content_rows"] += int(row["exact_content_rows"] or 0)
        totals["normalized_model_rows"] += int(row["normalized_model_rows"] or 0)
        totals["module_rows"] += int(row["module_rows"] or 0)
        sources.add(str(row["source"]))

    query_contract = {
        "cutoff_ms": cutoff_ms,
        "skill_key": skill_key,
        "groups": groups,
        "rejected_examples": rejected,
    }
    return {
        "configured": True,
        "database_present": True,
        "compatible_schema": True,
        "schema_digest": sha256_bytes(canonical_json(schema_contract)),
        "skill_key": skill_key,
        "totals": dict(totals),
        "distinct_sources": len(sources),
        "groups": groups,
        "rejected_examples": rejected,
        "query_digest": sha256_bytes(canonical_json(query_contract)),
        "limitations": limitations,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--days", type=int, default=60)
    parser.add_argument("--skill", required=True)
    parser.add_argument(
        "--session-root",
        action="append",
        default=[],
        type=parse_named_root,
        metavar="NAME=PATH",
        help="Approved session root. Repeat for each source.",
    )
    parser.add_argument("--nightly-state", type=Path)
    parser.add_argument("--metrics-db", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    if args.days <= 0:
        parser.error("--days must be positive")
    names = [name for name, _ in args.session_root]
    if len(names) != len(set(names)):
        parser.error("--session-root names must be unique")

    now = time.time()
    cutoff = now - args.days * 86_400
    cutoff_ms = int(cutoff * 1000)
    artifact: dict[str, Any] = {
        "schema": "sage.experience-compilation-evidence.v1",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "window": {
            "days": args.days,
            "cutoff": datetime.fromtimestamp(cutoff, timezone.utc).isoformat(),
        },
        "target_skill": args.skill,
        "privacy": {
            "raw_session_text_included": False,
            "raw_source_paths_included": False,
            "source_content_published": False,
            "artifact_visibility": "local_private",
        },
        "session_inventory": inventory_sessions(args.session_root, cutoff),
        "nightly_derived_evidence": aggregate_nightly(args.nightly_state, cutoff, args.skill),
        "sage_execution_evidence": aggregate_sage(args.metrics_db, cutoff_ms, args.skill),
        "limitations": [
            "Session inventory counts files and bytes without interpreting conversation text.",
            "Derived nightly artifacts may contain classifier errors.",
            "Outcomes without exact content hashes cannot identify the skill revision that ran.",
            "A failed outcome does not explain its cause by itself.",
        ],
    }
    artifact["artifact_digest"] = sha256_bytes(canonical_json(artifact))

    output = args.output.expanduser()
    output.parent.mkdir(parents=True, exist_ok=True, mode=0o700)
    output.write_text(json.dumps(artifact, indent=2) + "\n", encoding="utf-8")
    os.chmod(output, 0o600)
    print(json.dumps({"output": str(output), "artifact_digest": artifact["artifact_digest"]}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
