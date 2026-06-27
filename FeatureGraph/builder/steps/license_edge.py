"""Step license_edge: 双向抽取 requires_license 边 → feature_requires_license.jsonl。

双向抽取（覆盖率对齐黄金集）：
1. 正向：从 features.jsonl 的 availability_raw 抽（特性 → License）
2. 反向：从 licenses.jsonl 的 feature_refs 抽（License → 特性，匹配黄金集主要来源）

支持 --sample 过滤；用旧 l1_*_feature_license.csv 黄金集对照覆盖率（约束4）。
"""
from __future__ import annotations

from pathlib import Path

from ..core.io import load_jsonl, write_jsonl
from ..core.legacy import load_legacy_licenses
from ..core.license_edge import extract_license_edges_from_feature
from .registry import step


@step("license_edge", output_file="feature_requires_license.jsonl")
def run(ctx):
    nf, version = ctx["nf"], ctx["version"]
    data_dir = Path(ctx["data_dir"])
    features = load_jsonl(data_dir / "features.jsonl")
    licenses = load_jsonl(data_dir / "licenses.jsonl")
    sample = ctx.get("sample")
    rerun = ctx.get("rerun_target")

    feat_ids = {f["feature_code"] for f in features}

    edges: list[dict] = []
    seen: set[str] = set()

    def _add(e: dict) -> None:
        if e["edge_id"] not in seen:
            seen.add(e["edge_id"])
            edges.append(e)

    # 1) 正向：特性 availability_raw → License
    for f in features:
        code = f["feature_code"]
        if sample and code not in sample:
            continue
        if rerun and rerun not in code:
            continue
        ev = [f["source_path"]] if f.get("source_path") else []
        for e in extract_license_edges_from_feature(code, f, nf=nf, version=version, evidence_ids=ev):
            _add(e)

    # 2) 反向：License.feature_refs → 特性（UNC 黄金集主要来源）
    lic_by_code = {l["license_code"]: l for l in licenses if l.get("license_code")}
    for lic in licenses:
        refs = lic.get("feature_refs") or []
        if not refs:
            continue
        lic_code = lic["license_code"]
        lic_id = lic["id"]
        ev_ids = [lic["source_path"]] if lic.get("source_path") else []
        for feat_code in refs:
            feat_code = feat_code.strip()
            if not feat_code:
                continue
            if feat_code not in feat_ids:
                continue  # 特性不在 features.jsonl（跨网元/版本）
            if sample and feat_code not in sample:
                continue
            if rerun and rerun not in feat_code:
                continue
            src = f"{nf}@{version}@Feature@{feat_code}"
            edge = {
                "source_id": src,
                "relation_type": "requires_license",
                "target_id": lic_id,
                "nf": nf,
                "version": version,
                "feature_code": feat_code,
                "license_code": lic_code,
                "control_item_id": lic.get("control_item_id", ""),
                "source_type": "license_doc_reverse",   # 反向抽取标识（正向是 feature_overview）
                "edge_id": f"{src}|requires_license|{lic_id}",
                "source_evidence_ids": ev_ids,
            }
            _add(edge)

    out = data_dir / "feature_requires_license.jsonl"
    write_jsonl(out, edges)

    # 黄金集对照（约束4：旧数据纳入流程）
    legacy_dir = ctx.get("legacy_dir")
    note = ""
    if legacy_dir and not sample:
        legacy_path = ctx["project_root"] / legacy_dir
        gold = load_legacy_licenses(legacy_path, nf)
        gold_codes = {(g["feature_code"], g["license_code"]) for g in gold}
        new_codes = {(e["feature_code"], e["license_code"]) for e in edges}
        missing = gold_codes - new_codes
        note = f" | 黄金集={len(gold_codes)} 缺失={len(missing)}"

    # 按 source_type 分布
    from collections import Counter
    src_dist = Counter(e["source_type"] for e in edges)
    print(f"[license_edge:{nf}/{version}] {len(edges)} requires_license 边 "
          f"(source={dict(src_dist)}) → {out}{note}")
    return len(edges)
