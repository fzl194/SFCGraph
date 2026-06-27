"""Step dependency: 读 features.jsonl 的 feature_interaction_raw → 解析所有 Feature↔Feature 边。

输出：feature_relations.jsonl（合并原 depends_on/conflicts_with/relation_candidates）
支持 --sample 过滤。
"""
from __future__ import annotations

from pathlib import Path

from ..core.dependency import classify_edges, extract_dependencies
from ..core.io import load_jsonl, write_jsonl
from .registry import step


@step("dependency", output_file="feature_relations.jsonl")
def run(ctx):
    nf, version = ctx["nf"], ctx["version"]
    features = load_jsonl(Path(ctx["data_dir"]) / "features.jsonl")
    feature_lookup = {f["feature_code"]: f.get("name", "") for f in features}
    evidence_lookup = {f["feature_code"]: [f["source_path"]] for f in features if f.get("source_path")}
    sample = ctx.get("sample")
    rerun = ctx.get("rerun_target")

    all_edges: list[dict] = []
    for f in features:
        code = f["feature_code"]
        if sample and code not in sample:
            continue
        if rerun and rerun not in code:
            continue
        deps = extract_dependencies(code, f, feature_lookup)
        all_edges.extend(classify_edges(deps, nf, version, evidence_lookup))

    # 去重（按 source_id+relation_type+target_id）
    seen: set[str] = set()
    unique: list[dict] = []
    for e in all_edges:
        k = f"{e['source_id']}|{e['relation_type']}|{e['target_id']}"
        if k not in seen:
            seen.add(k)
            unique.append(e)

    out = Path(ctx["data_dir"]) / "feature_relations.jsonl"
    write_jsonl(out, unique)

    from collections import Counter
    rel_dist = Counter(e["relation_type"] for e in unique)
    print(f"[dependency:{nf}/{version}] {len(unique)} Feature<->Feature edges "
          f"(type={dict(rel_dist)}) → {out}")
    return len(unique)
