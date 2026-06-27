"""Step verify: FeatureGraph 数据完整性审计 → audit_report.md。

检查 Feature↔Feature 边的 target 必须是已存在 Feature；requires_license 的
target 必须在 licenses.jsonl；输出 feature_category/config_relevance 分布。
"""
from __future__ import annotations

from pathlib import Path

from ..core.io import load_jsonl
from .registry import step


def _target_code(target_id: str) -> str:
    """从四段式 target_id 提取 feature_code：UDG@20.15.2@Feature@GWFD-XXX → GWFD-XXX。"""
    return target_id.rsplit("@", 1)[-1]


@step("verify")
def run(ctx):
    nf, version = ctx["nf"], ctx["version"]
    d = Path(ctx["data_dir"])
    features = load_jsonl(d / "features.jsonl")
    licenses = load_jsonl(d / "licenses.jsonl")
    relations = load_jsonl(d / "feature_relations.jsonl")
    req_lic = load_jsonl(d / "feature_requires_license.jsonl")

    depends = [e for e in relations if e["relation_type"] == "depends_on"]
    conflicts = [e for e in relations if e["relation_type"] == "conflicts_with"]
    candidates = [e for e in relations if e["relation_type"] not in ("depends_on", "conflicts_with")]

    feat_ids = {f["feature_code"] for f in features}
    lic_ids = {l["id"] for l in licenses}

    dangling_dep = [e for e in depends if _target_code(e["target_id"]) not in feat_ids]
    dangling_conf = [e for e in conflicts if _target_code(e["target_id"]) not in feat_ids]
    dangling_lic = [e for e in req_lic if e["target_id"] not in lic_ids]

    cat_counts: dict[str, int] = {}
    cr_counts: dict[str, int] = {}
    for f in features:
        c = f.get("feature_category", "")
        cat_counts[c] = cat_counts.get(c, 0) + 1
        r = f.get("config_relevance", "")
        cr_counts[r] = cr_counts.get(r, 0) + 1

    lines = [
        f"# FeatureGraph 审计报告 {nf}@{version}",
        "",
        "## 概要",
        f"- Feature 节点: {len(features)}",
        f"- License 节点: {len(licenses)}",
        f"- Feature<->Feature 边: {len(relations)} (depends_on={len(depends)}, conflicts_with={len(conflicts)}, 候选={len(candidates)})",
        f"- 悬空 target: depends_on={len(dangling_dep)}, conflicts_with={len(dangling_conf)}",
        f"- requires_license 边: {len(req_lic)} (未对齐 License 节点: {len(dangling_lic)})",
        "",
        "## feature_category 分布",
    ]
    for c, n in sorted(cat_counts.items(), key=lambda x: -x[1]):
        lines.append(f"- {c or '(空)'}: {n}")
    lines.append("")
    lines.append("## config_relevance 分布")
    for r, n in sorted(cr_counts.items(), key=lambda x: -x[1]):
        lines.append(f"- {r or '(空)'}: {n}")
    lines.append("")

    if dangling_dep:
        lines.append("## depends_on 悬空 target (前20)")
        for e in dangling_dep[:20]:
            lines.append(f"- {_target_code(e['source_id'])} -> {_target_code(e['target_id'])}")
        lines.append("")
    if dangling_conf:
        lines.append("## conflicts_with 悬空 target (前20)")
        for e in dangling_conf[:20]:
            lines.append(f"- {_target_code(e['source_id'])} -> {_target_code(e['target_id'])}")
        lines.append("")
    if dangling_lic:
        lines.append("## requires_license 未对齐 License 节点 (前20)")
        for e in dangling_lic[:20]:
            lines.append(f"- {e['feature_code']} -> {e['license_code']}")
        lines.append("")

    out = d / "audit_report.md"
    out.write_text("\n".join(lines), encoding="utf-8")
    issues = len(dangling_dep) + len(dangling_conf) + len(dangling_lic)
    print(f"[verify:{nf}/{version}] 悬空/未对齐问题: {issues} -> {out}")
    return issues
