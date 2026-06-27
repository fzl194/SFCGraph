"""Step verify: FeatureGraph 数据完整性审计 → audit_report.md。

检查：depends_on/conflicts_with 的 target 必须是已存在 Feature；
requires_license 的 target 必须在 licenses.jsonl；弱依赖隔离在 candidates；
输出 feature_category/config_relevance 分布。
"""
from __future__ import annotations

from pathlib import Path

from ..core.io import load_jsonl
from .registry import step


@step("verify")
def run(ctx):
    nf, version = ctx["nf"], ctx["version"]
    d = Path(ctx["data_dir"])
    features = load_jsonl(d / "features.jsonl")
    licenses = load_jsonl(d / "licenses.jsonl")
    depends = load_jsonl(d / "feature_depends_on.jsonl")
    conflicts = load_jsonl(d / "feature_conflicts_with.jsonl")
    req_lic = load_jsonl(d / "feature_requires_license.jsonl")
    candidates = load_jsonl(d / "feature_relation_candidates.jsonl")

    feat_ids = {f["feature_code"] for f in features}
    lic_ids = {l["id"] for l in licenses}

    dangling_dep = [e for e in depends if e["target_feature_code"] not in feat_ids]
    dangling_conf = [e for e in conflicts if e["target_feature_code"] not in feat_ids]
    dangling_lic = [e for e in req_lic if e["target_id"] not in lic_ids]

    cat_counts: dict[str, int] = {}
    cr_counts: dict[str, int] = {}
    for f in features:
        cat_counts[f.get("feature_category", "")] = cat_counts.get(f.get("feature_category", ""), 0) + 1
        cr_counts[f.get("config_relevance", "")] = cr_counts.get(f.get("config_relevance", ""), 0) + 1

    lines = [
        f"# FeatureGraph 审计报告 {nf}@{version}",
        "",
        "## 概要",
        f"- Feature 节点: {len(features)}",
        f"- License 节点: {len(licenses)}",
        f"- depends_on 边: {len(depends)}（悬空 target: {len(dangling_dep)}）",
        f"- conflicts_with 边: {len(conflicts)}（悬空 target: {len(dangling_conf)}）",
        f"- requires_license 边: {len(req_lic)}（未对齐 License 节点: {len(dangling_lic)}）",
        f"- 候选弱关系: {len(candidates)}（已隔离，不进核心边表）",
        "",
        "## feature_category 分布",
    ]
    for c, n in sorted(cat_counts.items(), key=lambda x: -x[1]):
        lines.append(f"- {c or '(空)'}: {n}")
    lines.append("")
    lines.append("## config_relevance 分布")
    for c, n in sorted(cr_counts.items(), key=lambda x: -x[1]):
        lines.append(f"- {c or '(空)'}: {n}")
    lines.append("")

    if dangling_dep:
        lines.append("## depends_on 悬空 target（前20）")
        for e in dangling_dep[:20]:
            lines.append(f"- {e['source_feature_code']} → {e['target_feature_code']}")
        lines.append("")
    if dangling_lic:
        lines.append("## requires_license 未对齐 License 节点（前20）")
        for e in dangling_lic[:20]:
            lines.append(f"- {e['feature_code']} → {e['license_code']}")
        lines.append("")

    out = d / "audit_report.md"
    out.write_text("\n".join(lines), encoding="utf-8")
    issues = len(dangling_dep) + len(dangling_conf) + len(dangling_lic)
    print(f"[verify:{nf}/{version}] 悬空/未对齐问题: {issues} → {out}")
    return issues
