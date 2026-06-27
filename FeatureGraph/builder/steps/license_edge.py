"""Step license_edge: 读 features.jsonl 的 availability_raw → feature_requires_license.jsonl。

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
    features = load_jsonl(Path(ctx["data_dir"]) / "features.jsonl")
    sample = ctx.get("sample")
    rerun = ctx.get("rerun_target")

    edges: list[dict] = []
    seen: set[str] = set()
    for f in features:
        code = f["feature_code"]
        if sample and code not in sample:
            continue
        if rerun and rerun not in code:
            continue
        ev = [f["source_path"]] if f.get("source_path") else []
        for e in extract_license_edges_from_feature(code, f, nf=nf, version=version, evidence_ids=ev):
            if e["edge_id"] not in seen:
                seen.add(e["edge_id"])
                edges.append(e)

    out = Path(ctx["data_dir"]) / "feature_requires_license.jsonl"
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

    print(f"[license_edge:{nf}/{version}] {len(edges)} requires_license 边 → {out}{note}")
    return len(edges)
