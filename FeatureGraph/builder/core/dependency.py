"""依赖/互斥/弱语义解析（移植 step4 extract_feature_dependencies）。

输入 Feature 节点的 feature_interaction_raw（"与其他特性的交互"节原文），
返回扁平 dep 列表；classify_edges 再按 schema 拆 depends_on/conflicts_with/candidates
并补四段式 source_id/target_id、conflict_pair_id、source_evidence_ids。
"""
from __future__ import annotations

import re

FEATURE_ID_SEARCH_RE = re.compile(r"((?:GWFD|WSFD|IPFD|NPFD|SFFD)-\d{3,6})")
URL_FID_RE = re.compile(r"\([^)]*?((?:GWFD|WSFD|IPFD|NPFD|SFFD)-\d{3,6})[^)]*\)")


def _lookup_by_name(raw_name: str, feature_lookup: dict) -> str:
    """无特性ID时用功能名模糊匹配（移植 step4 lookup_feature_by_name）。"""
    name = raw_name.strip()
    m = re.match(r"\[([^\]]+)\]", name)
    if m:
        name = m.group(1).strip()
    if name in ("NA", "-", "无", "—", "N/A", "不涉及", "无。"):
        return ""
    matches = [fid for fid, fname in feature_lookup.items() if fname and (name in fname or fname in name)]
    return matches[0] if len(matches) == 1 else ""


def extract_dependencies(feature_code: str, raw_fields: dict, feature_lookup: dict | None = None) -> list[dict]:
    """解析 feature_interaction_raw → 扁平 dep 列表（含 raw_type/desc/control_item）。

    支持 4/3/2 列格式；URL 笔误纠正（优先 URL 中的特性ID）；自引用过滤。
    """
    feature_lookup = feature_lookup or {}
    text = raw_fields.get("feature_interaction_raw", "")
    if not text or "不涉及" in text:
        return []

    deps: list[dict] = []
    for line in text.split("\n"):
        parts = [p.strip() for p in line.strip().split("|")]
        parts = [p for p in parts if p and p != "---"]
        if len(parts) < 2:
            continue
        h0 = parts[0].strip("*").strip()
        h1 = parts[1].strip("*").strip() if len(parts) > 1 else ""
        if h0 in ("交互类型", "交互") or h1 in ("相关特性", "和其他特性的交互关系"):
            continue

        if len(parts) >= 4:  # | 交互类型 | 相关特性 | 控制项名称 | 交互说明 |
            dep_type_raw, related = parts[0], parts[1]
            control = parts[2] if len(parts) > 2 else ""
            desc = parts[3] if len(parts) > 3 else ""
        elif len(parts) == 3:  # | 交互类型 | 相关特性 | 交互关系 |
            dep_type_raw, related, desc, control = parts[0], parts[1], parts[2], ""
        elif len(parts) == 2:  # | 相关特性 | 交互关系 |
            dep_type_raw, related, desc, control = "交互", parts[0], parts[1], ""
        else:
            continue

        control = re.sub(r"<[^>]+>", "", re.sub(r"<br\s*/?>", "; ", control)).strip()
        url_m = URL_FID_RE.search(related)
        target = url_m.group(1) if url_m else (FEATURE_ID_SEARCH_RE.search(related).group(1) if FEATURE_ID_SEARCH_RE.search(related) else "")
        if not target:
            target = _lookup_by_name(related, feature_lookup)
        desc = re.sub(r"<[^>]+>", " ", re.sub(r"<br\s*/?>", " ", desc)).strip()
        dep_type = _normalize_type(dep_type_raw)
        if target == feature_code:  # 自引用过滤
            continue
        if len(dep_type) > 10 and dep_type == dep_type_raw:  # 未映射长句
            continue
        if not target:
            continue
        deps.append({"source_feature_code": feature_code, "target_feature_code": target,
                     "raw_type": dep_type, "description": desc, "control_item": control,
                     "source_type": "overview_explicit"})
    return deps


def _normalize_type(dep_type_raw: str) -> str:
    if dep_type_raw in ("依赖", "必须先开启"):
        return "depends_on"
    if dep_type_raw in ("互斥", "冲突"):
        return "conflicts_with"
    if dep_type_raw in ("影响", "与其他特性的影响", "与其他特性间的影响", "其他可能的影响"):
        return "affects"
    if dep_type_raw in ("被影响", "其他"):
        return "other"
    if "协同" in dep_type_raw:
        return "cooperates_with"
    if dep_type_raw == "支持":
        return "supports"
    if "交互" in dep_type_raw or "关系" in dep_type_raw:
        return "interacts_with"
    return dep_type_raw


def classify_edges(deps: list[dict], nf: str, version: str, evidence_lookup: dict | None = None) -> dict[str, list[dict]]:
    """拆 depends_on / conflicts_with / candidates，补四段式 id + conflict_pair_id + source_evidence_ids。"""
    evidence_lookup = evidence_lookup or {}

    def src(d): return f"{nf}@{version}@Feature@{d['source_feature_code']}"
    def tgt(d): return f"{nf}@{version}@Feature@{d['target_feature_code']}"

    result: dict[str, list[dict]] = {"depends_on": [], "conflicts_with": [], "candidates": []}
    for d in deps:
        base = {
            "source_id": src(d), "relation_type": d["raw_type"], "target_id": tgt(d),
            "nf": nf, "version": version,
            "source_feature_code": d["source_feature_code"], "target_feature_code": d["target_feature_code"],
            "description": d["description"], "control_item": d["control_item"], "source_type": d["source_type"],
            "edge_id": f"{src(d)}|{d['raw_type']}|{tgt(d)}",
            "source_evidence_ids": evidence_lookup.get(d["source_feature_code"], []),
        }
        if d["raw_type"] == "depends_on":
            result["depends_on"].append(base)
        elif d["raw_type"] == "conflicts_with":
            pair = sorted([d["source_feature_code"], d["target_feature_code"]])
            base["conflict_pair_id"] = f"conflict:{pair[0]}-{pair[1]}"
            result["conflicts_with"].append(base)
        else:  # cooperates_with/affects/interacts_with/supports/other → candidates 待审
            base["raw_type"] = d["raw_type"]
            result["candidates"].append(base)
    return result
