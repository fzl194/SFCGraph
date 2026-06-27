"""Step dependency: 读 features.jsonl 的 feature_interaction_raw → 解析边表。

输出：feature_depends_on.jsonl / feature_conflicts_with.jsonl / feature_relation_candidates.jsonl
支持 --sample 过滤。
"""
from __future__ import annotations

from pathlib import Path

from ..core.dependency import classify_edges, extract_dependencies
from ..core.io import load_jsonl, write_jsonl
from .registry import step


@step("dependency", output_file="feature_depends_on.jsonl")
def run(ctx):
    nf, version = ctx["nf"], ctx["version"]
    features = load_jsonl(Path(ctx["data_dir"]) / "features.jsonl")
    feature_lookup = {f["feature_code"]: f.get("name", "") for f in features}
    evidence_lookup = {f["feature_code"]: [f["source_path"]] for f in features if f.get("source_path")}
    sample = ctx.get("sample")
    rerun = ctx.get("rerun_target")

    all_depends: list[dict] = []
    all_conflicts: list[dict] = []
    all_candidates: list[dict] = []
    for f in features:
        code = f["feature_code"]
        if sample and code not in sample:
            continue
        if rerun and rerun not in code:
            continue
        deps = extract_dependencies(code, f, feature_lookup)
        edges = classify_edges(deps, nf, version, evidence_lookup)
        all_depends += edges["depends_on"]
        all_conflicts += edges["conflicts_with"]
        all_candidates += edges["candidates"]

    all_depends = _dedup(all_depends)
    all_conflicts = _dedup(all_conflicts)

    data_dir = Path(ctx["data_dir"])
    write_jsonl(data_dir / "feature_depends_on.jsonl", all_depends)
    write_jsonl(data_dir / "feature_conflicts_with.jsonl", all_conflicts)
    write_jsonl(data_dir / "feature_relation_candidates.jsonl", all_candidates)
    print(f"[dependency:{nf}/{version}] depends_on={len(all_depends)} "
          f"conflicts={len(all_conflicts)} candidates={len(all_candidates)}")
    return len(all_depends) + len(all_conflicts)


def _dedup(edges: list[dict]) -> list[dict]:
    seen, out = set(), []
    for e in edges:
        if e["edge_id"] not in seen:
            seen.add(e["edge_id"])
            out.append(e)
    return out
