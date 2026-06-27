"""从特性清单 xlsx 抽取 Feature seed（移植 step1_extract_features）。

返回 dict 列表，字段对齐 schema §2.1：
feature_code/name/is_directory/catalog_section/parent_feature_code/nf_support_map/product_version。
"""
from __future__ import annotations

import re
from pathlib import Path

import openpyxl

FID_RE = re.compile(r"^(GWFD|WSFD|IPFD|NPFD)-(\d{3,6})$")

UDG_NF_COLUMNS = {
    2: "GGSN(2G&3G)", 3: "S/PGW-U(4G)", 4: "S/PGW-U(5G NSA)", 5: "UPF(5G)", 6: "NB-IoT",
}
UNC_NF_COLUMNS = {
    2: "SGSN(2.5&3G)", 3: "GGSN-C(2.5&3G)", 4: "MME(4G)", 5: "S/PGW-C(4G)",
    6: "NB-IoT(4G)", 7: "5G MME(5G NSA)", 8: "5G S/PGW-C(5G NSA)",
    9: "AMF(5G SA)", 10: "SMF(5G SA)", 11: "NRF(5G SA)",
}

NF_COLUMNS = {"UDG": UDG_NF_COLUMNS, "UNC": UNC_NF_COLUMNS}


def extract_seed(xlsx_path: str | Path, sheets: list[int], nf_columns: dict[int, str]) -> list[dict]:
    """读指定 sheet，返回 Feature seed dict 列表（按 feature_code 去重）。"""
    wb = openpyxl.load_workbook(xlsx_path, read_only=True)
    out: list[dict] = []
    for idx in sheets:
        ws = wb.worksheets[idx]
        out.extend(_extract_sheet(ws, nf_columns))
    wb.close()
    seen, result = set(), []
    for f in out:
        if f["feature_code"] not in seen:
            seen.add(f["feature_code"])
            result.append(f)
    return result


def _extract_sheet(ws, nf_columns: dict[int, str]) -> list[dict]:
    features: list[dict] = []
    current_section, current_parent_fid = "", ""
    for row in ws.iter_rows(min_row=1, values_only=True):
        col0 = str(row[0]).strip() if row[0] else ""
        col1 = str(row[1]).strip() if row[1] else ""
        col2 = str(row[2]).strip() if len(row) > 2 and row[2] else ""

        if not FID_RE.match(col0):
            # 非特性行：可能是 section 标题行（仅首列有值）
            if col0 and not col1 and col0 not in ("E", "N", "M", "-", "_"):
                current_section, current_parent_fid = col0, ""
            continue

        fid, is_dir = col0, (col2 == "目录")
        if is_dir:
            current_parent_fid = fid

        nf_map: dict[str, str] = {}
        for col_idx, col_name in nf_columns.items():
            val = ""
            if col_idx < len(row) and row[col_idx] is not None:
                val = str(row[col_idx]).strip()
            if val and val != "_":
                nf_map[col_name] = val

        features.append({
            "feature_code": fid,
            "name": col1,
            "is_directory": is_dir,
            "catalog_section": current_section,
            "parent_feature_code": current_parent_fid if not is_dir else "",
            "nf_support_map": "; ".join(f"{k}={v}" for k, v in nf_map.items()),
            "product_version": "20.15.2",
        })
    return features
