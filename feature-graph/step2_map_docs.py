"""
step2_map_docs.py

Step 2: 基于Step 1输出的特性清单，扫描产品文档目录，
        将每个md文件归属到路径上最深层的特性。

前置: data/UDG_features.csv, data/UNC_features.csv (Step 1 输出)

输出:
  - data/UDG_feature_files.csv  (feature_id, product_type, file_path)
  - data/UNC_feature_files.csv  (feature_id, product_type, file_path)
"""

import csv
import os
import re
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = BASE_DIR.parent

FEATURE_DIR_PATTERN = re.compile(r"^(GWFD|WSFD|IPFD|NPFD)-(\d{3,6})\s")

UDG_DOC_ROOT = PROJECT_ROOT / "output" / "UDG_Product_Documentation_CH_20.15.2" / "特性部署" / "特性指南" / "UDG特性指南"
UNC_DOC_ROOT = PROJECT_ROOT / "output" / "UNC 20.15.2 产品文档(裸机容器) 05" / "网络部署" / "特性部署" / "UNC特性指南"


def load_feature_ids(csv_path):
    """从Step 1的CSV中读取所有feature_id"""
    fids = set()
    with open(csv_path, encoding="utf-8-sig") as f:
        for row in csv.DictReader(f):
            fids.add(row["feature_id"])
    return fids


def scan_feature_docs(doc_root, product_type, valid_feature_ids):
    """
    扫描产品文档目录，将md文件归属到路径上最深层的特性。

    规则:
      - 路径上可能有多个特性目录（父/子），取最后一个（最深层）
      - 也能匹配文件名中的特性编号
      - 只归入特性清单中存在的特性ID
      - 不匹配任何特性的md文件单独统计但不输出
    """
    if not doc_root.exists():
        print(f"  [WARN] doc root not found: {doc_root}")
        return [], int, int

    results = []
    total_md = 0
    unmatched = 0

    for root, dirs, filenames in os.walk(doc_root):
        dirs[:] = [d for d in dirs if not d.endswith(".assets")]

        path_parts = Path(root).parts
        path_feature_ids = []
        for part in path_parts:
            m = FEATURE_DIR_PATTERN.match(part)
            if m:
                path_feature_ids.append(f"{m.group(1)}-{m.group(2)}")

        for fn in sorted(filenames):
            if not fn.endswith(".md"):
                continue

            total_md += 1

            # 确定归属特性ID：优先路径中的，再尝试文件名
            assigned_fid = ""

            if path_feature_ids:
                # 取路径上最后一个（最深层）特性
                assigned_fid = path_feature_ids[-1]
            else:
                m = re.match(r"^(GWFD|WSFD|IPFD|NPFD)-(\d{3,6})", fn)
                if m:
                    assigned_fid = f"{m.group(1)}-{m.group(2)}"

            if not assigned_fid or assigned_fid not in valid_feature_ids:
                unmatched += 1
                continue

            try:
                rel_path = str((Path(root) / fn).relative_to(PROJECT_ROOT)).replace("\\", "/")
            except ValueError:
                rel_path = str(Path(root) / fn).replace("\\", "/")

            results.append({
                "feature_id": assigned_fid,
                "product_type": product_type,
                "file_path": rel_path,
            })

    return results, total_md, unmatched


def write_file_mapping(file_rows, output_path):
    fields = ["feature_id", "product_type", "file_path"]
    with open(output_path, "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(file_rows)


def main():
    data_dir = BASE_DIR / "data"

    # 加载Step 1的特性清单
    print("[Step 2] Loading feature lists from Step 1 ...")
    udg_fids = load_feature_ids(data_dir / "UDG_features.csv")
    unc_fids = load_feature_ids(data_dir / "UNC_features.csv")
    print(f"  UDG: {len(udg_fids)} features")
    print(f"  UNC: {len(unc_fids)} features")

    # 扫描文档
    print(f"\n[Step 2] Scanning UDG docs: {UDG_DOC_ROOT}")
    udg_files, udg_total, udg_unmatched = scan_feature_docs(UDG_DOC_ROOT, "UDG", udg_fids)
    print(f"  Total md: {udg_total}, matched: {len(udg_files)}, unmatched: {udg_unmatched}")

    print(f"\n[Step 2] Scanning UNC docs: {UNC_DOC_ROOT}")
    unc_files, unc_total, unc_unmatched = scan_feature_docs(UNC_DOC_ROOT, "UNC", unc_fids)
    print(f"  Total md: {unc_total}, matched: {len(unc_files)}, unmatched: {unc_unmatched}")

    write_file_mapping(udg_files, data_dir / "UDG_feature_files.csv")
    write_file_mapping(unc_files, data_dir / "UNC_feature_files.csv")

    # 覆盖率统计
    print(f"\n{'='*60}")
    print("Coverage Summary")
    print(f"{'='*60}")

    for label, features_csv, file_rows in [
        ("UDG", data_dir / "UDG_features.csv", udg_files),
        ("UNC", data_dir / "UNC_features.csv", unc_files),
    ]:
        leaves = []
        with open(features_csv, encoding="utf-8-sig") as f:
            for row in csv.DictReader(f):
                if row["is_directory"] == "false":
                    leaves.append(row)
        leaf_ids = set(r["feature_id"] for r in leaves)
        files_with_docs = set(fr["feature_id"] for fr in file_rows)
        covered = leaf_ids & files_with_docs
        no_docs = leaf_ids - files_with_docs

        pct = len(covered) / len(leaf_ids) * 100 if leaf_ids else 0
        print(f"\n  {label}: {len(leaves)} leaf features")
        print(f"    With docs:    {len(covered)} ({pct:.1f}%)")
        print(f"    Without docs: {len(no_docs)}")
        if no_docs and len(no_docs) <= 20:
            name_map = {r["feature_id"]: r["feature_name"] for r in leaves}
            for fid in sorted(no_docs):
                print(f"      {fid} | {name_map[fid]}")
        elif no_docs:
            name_map = {r["feature_id"]: r["feature_name"] for r in leaves}
            for fid in sorted(no_docs)[:10]:
                print(f"      {fid} | {name_map[fid]}")
            print(f"      ... and {len(no_docs) - 10} more")

    print(f"\n[OK] Step 2 done. Files: data/UDG_feature_files.csv, data/UNC_feature_files.csv")


if __name__ == "__main__":
    main()
