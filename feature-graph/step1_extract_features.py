"""
step1_extract_features.py

Step 1: 从xlsx提取特性清单（UDG和UNC分开处理）

输出:
  - data/UDG_features.csv
  - data/UNC_features.csv
"""

import csv
import re
from collections import Counter
from pathlib import Path

import openpyxl

BASE_DIR = Path(__file__).resolve().parent

FID_RE = re.compile(r"^(GWFD|WSFD|IPFD|NPFD)-(\d{3,6})$")

# 每个xlsx的NF列定义: col_index → "NF名称(代际)"
UDG_NF_COLUMNS = {
    2: "GGSN(2G&3G)",
    3: "S/PGW-U(4G)",
    4: "S/PGW-U(5G NSA)",
    5: "UPF(5G)",
    6: "NB-IoT",
}

UNC_NF_COLUMNS = {
    2: "SGSN(2.5&3G)",
    3: "GGSN-C(2.5&3G)",
    4: "MME(4G)",
    5: "S/PGW-C(4G)",
    6: "NB-IoT(4G)",
    7: "5G MME(5G NSA)",
    8: "5G S/PGW-C(5G NSA)",
    9: "AMF(5G SA)",
    10: "SMF(5G SA)",
    11: "NRF(5G SA)",
}


def build_csv_fields(nf_columns):
    fixed = ["id", "feature_id", "feature_name", "product_type", "product_version",
             "is_directory", "section", "parent_feature_id"]
    return fixed + list(nf_columns.values())


def extract_from_sheet(ws, nf_columns, product_type, product_version):
    features = []
    current_section = ""
    current_parent_fid = ""

    for row in ws.iter_rows(min_row=1, values_only=True):
        col0 = str(row[0]).strip() if row[0] else ""
        col1 = str(row[1]).strip() if row[1] else ""
        col2 = str(row[2]).strip() if row[2] else ""

        if not FID_RE.match(col0):
            if col0 and not col1 and col0 not in ("E", "N", "M", "-"):
                current_section = col0
                current_parent_fid = ""
            continue

        fid = col0
        fname = col1
        is_dir = (col2 == "目录")

        if is_dir:
            current_parent_fid = fid

        nf_values = {}
        for col_idx, col_name in nf_columns.items():
            val = ""
            if col_idx < len(row) and row[col_idx] is not None:
                val = str(row[col_idx]).strip()
            nf_values[col_name] = val

        record = {
            "id": f"{product_type}:{fid}",
            "feature_id": fid,
            "feature_name": fname,
            "product_type": product_type,
            "product_version": product_version,
            "is_directory": "true" if is_dir else "false",
            "section": current_section,
            "parent_feature_id": current_parent_fid if not is_dir else "",
        }
        record.update(nf_values)
        features.append(record)

    return features


def dedup(features):
    seen = set()
    result = []
    for f in features:
        if f["feature_id"] not in seen:
            seen.add(f["feature_id"])
            result.append(f)
    return result


def extract_vendor(xlsx_path, sheet_indices, nf_columns, product_type, product_version):
    wb = openpyxl.load_workbook(xlsx_path, read_only=True)
    all_features = []
    for idx in sheet_indices:
        ws = wb.worksheets[idx]
        all_features.extend(extract_from_sheet(ws, nf_columns, product_type, product_version))
    wb.close()
    return dedup(all_features)


def write_csv(features, output_path, fields):
    with open(output_path, "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(features)


def print_summary(label, features):
    dirs = sum(1 for f in features if f["is_directory"] == "true")
    leaves = sum(1 for f in features if f["is_directory"] == "false")
    by_prefix = Counter(f["feature_id"][:4] for f in features)
    print(f"\n{'='*60}")
    print(f"{label}: {len(features)} total ({leaves} leaf, {dirs} directory)")
    print(f"  by prefix: {dict(sorted(by_prefix.items()))}")
    print(f"  First 5 rows:")
    for f in features[:5]:
        marker = "[DIR]" if f["is_directory"] == "true" else "     "
        parent = f" <- {f['parent_feature_id']}" if f["parent_feature_id"] else ""
        print(f"    {marker} {f['feature_id']} | {f['feature_name'][:30]}{parent}")


def main():
    data_dir = BASE_DIR / "data"
    data_dir.mkdir(exist_ok=True)

    # UDG
    udg_path = BASE_DIR / "UDG 20.15.2 特性清单 01.xlsx"
    udg_fields = build_csv_fields(UDG_NF_COLUMNS)
    print(f"[Step 1] Extracting UDG from {udg_path.name} ...")
    udg = extract_vendor(udg_path, sheet_indices=[1, 2],
                         nf_columns=UDG_NF_COLUMNS,
                         product_type="UDG", product_version="20.15.2")
    write_csv(udg, data_dir / "UDG_features.csv", udg_fields)
    print_summary("UDG", udg)

    # UNC
    unc_path = BASE_DIR / "UNC 20.15.2 特性清单 01.xlsx"
    unc_fields = build_csv_fields(UNC_NF_COLUMNS)
    print(f"\n[Step 1] Extracting UNC from {unc_path.name} ...")
    unc = extract_vendor(unc_path, sheet_indices=[2, 3],
                         nf_columns=UNC_NF_COLUMNS,
                         product_type="UNC", product_version="20.15.2")
    write_csv(unc, data_dir / "UNC_features.csv", unc_fields)
    print_summary("UNC", unc)

    print(f"\n[OK] Step 1 done. Files: data/UDG_features.csv, data/UNC_features.csv")


if __name__ == "__main__":
    main()
