"""从 Feature 的 availability_raw 解析 requires_license 边（移植 step4 extract_licenses）。

输出边字段对齐 schema §3.5：source_id(Feature)/target_id(License)/feature_code/license_code/
control_item_id/source_type=feature_overview/source_evidence_ids。License 节点来自 licenses.jsonl。
边表不含 applicable_nf（NF 覆盖在 License 节点上）。
"""
from __future__ import annotations

import re

LICENSE_CELL_RE = re.compile(r"([A-Za-z0-9]{6,12})\s+([A-Za-z0-9_\-]+)\s+(.+)")

# step4 特例：转置表格(Label|Value)无法通用解析，人工提取（WSFD-106201 小区广播服务）
_HARDCODED_LICENSES: dict[str, list[dict]] = {
    "WSFD-106201": [
        {"license_number": "82209076", "license_code": "LKV2PWSR01", "license_name": "PWS故障快速恢复"},
        {"license_number": "82207709", "license_code": "LKV2CBS02", "license_name": "小区广播服务"},
        {"license_number": "82200FMS", "license_code": "LKV2CBSIFMM01", "license_name": "CBS广播服务接口及功能-4G"},
        {"license_number": "82200FMY", "license_code": "LKV2CBSIFAM01", "license_name": "CBS广播服务接口及功能-5G"},
    ],
}


def extract_license_edges_from_feature(feature_code: str, raw_fields: dict, *,
                                       nf: str, version: str, evidence_ids: list | None = None) -> list[dict]:
    """解析 requires_license 边列表。"""
    raw_licenses = _HARDCODED_LICENSES.get(feature_code) or _parse_availability(raw_fields.get("availability_raw", ""))
    src = f"{nf}@{version}@Feature@{feature_code}"
    evidence = evidence_ids or []
    edges: list[dict] = []
    for lic in raw_licenses:
        name = (lic.get("license_name") or "").strip().rstrip("|\"'")
        if not name or len(name) < 2 or name in ("License控制项", "License支持"):
            continue
        target = f"{nf}@{version}@License@{lic['license_code']}"
        edges.append({
            "source_id": src, "relation_type": "requires_license", "target_id": target,
            "nf": nf, "version": version,
            "feature_code": feature_code, "license_code": lic["license_code"],
            "control_item_id": lic.get("license_number", ""),
            "source_type": "feature_overview",
            "edge_id": f"{src}|requires_license|{target}",
            "source_evidence_ids": evidence,
        })
    return edges


def _parse_availability(text: str) -> list[dict]:
    if not text or ("无需" in text and "License" in text):
        return []
    return _parse_table(text) or _parse_quoted(text) or _parse_plain(text)


def _parse_table(text: str) -> list[dict]:
    """License 表格（适用NF/涉及NF/特性 × License控制项）。返回 [{license_number,license_code,license_name}] 或 []。"""
    in_table, lic_col, licenses = False, -1, []
    for line in text.split("\n"):
        parts = [p.strip() for p in line.strip().split("|")]
        parts = [p for p in parts if p and p != "---"]
        if not in_table:
            for i, p in enumerate(parts):
                pc = p.strip("*").strip()
                if pc.startswith("License") and len(pc) <= 20:
                    lic_col = i
                    break
            if lic_col >= 0 and len(parts) >= 2:
                in_table = True
            continue
        if not parts:
            continue  # 空行/分隔符行：保持表格状态
        if len(parts) <= lic_col:
            in_table, lic_col = False, -1
            continue
        cell = re.sub(r"<br\s*/?>", " ", parts[lic_col].rstrip(" |").strip())
        m = LICENSE_CELL_RE.match(cell)
        if m:
            licenses.append({"license_number": m.group(1), "license_code": m.group(2),
                             "license_name": m.group(3).strip().rstrip(" |")})
        else:
            in_table, lic_col = False, -1
    return licenses


def _parse_quoted(text: str) -> list[dict]:
    """单行引号包裹：'82209822 LKV3G5BCBC01 内容计费基本功能'。"""
    m = re.search(r'["“”\'‘’]+([A-Za-z0-9]{6,12})\s+([A-Za-z0-9_\-]+)\s+(.+?)["“”\'‘’]', text, re.MULTILINE)
    if m:
        return [{"license_number": m.group(1), "license_code": m.group(2),
                 "license_name": m.group(3).strip().rstrip("。")}]
    return []


def _parse_plain(text: str) -> list[dict]:
    """纯文本段落（'对应的License控制项为 82200EDD LKV2SALANSM01 xxx。'）。"""
    out: list[dict] = []
    for line in text.split("\n"):
        line = line.strip()
        if line.startswith("|") or not line:
            continue
        m = re.search(r"([A-Za-z0-9]{6,12})\s+([A-Za-z0-9_\-]+)\s+(.+?)(?:\s*[。.]|$)", line)
        if m:
            name = m.group(3).strip().rstrip("。|")
            if name and len(name) > 2:
                out.append({"license_number": m.group(1), "license_code": m.group(2), "license_name": name})
    return out
