"""
step3_audit_report.py

Step 3: 生成审核报告，列出所有特殊情况：
  - md文件未归类到任何特性
  - md文件归属的特性不在xlsx清单中
  - 特性清单中无md文档的特性
  - 统计汇总

输出: data/audit_report.md
"""

import csv
import os
import re
from collections import defaultdict
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = BASE_DIR.parent

FEATURE_DIR_PATTERN = re.compile(r"^(GWFD|WSFD|IPFD|NPFD)-(\d{3,6})\s")

UDG_DOC_ROOT = PROJECT_ROOT / "output" / "UDG_Product_Documentation_CH_20.15.2" / "特性部署" / "特性指南" / "UDG特性指南"
UNC_DOC_ROOT = PROJECT_ROOT / "output" / "UNC 20.15.2 产品文档(裸机容器) 05" / "网络部署" / "特性部署" / "UNC特性指南"


def load_features(path):
    rows = []
    with open(path, encoding="utf-8-sig") as f:
        for row in csv.DictReader(f):
            rows.append(row)
    return rows


def load_mapped(path):
    mapped = defaultdict(list)
    with open(path, encoding="utf-8-sig") as f:
        for row in csv.DictReader(f):
            mapped[row["feature_id"]].append(row["file_path"])
    return mapped


def scan_all_md(doc_root, fid_set):
    """扫描全部md文件，返回三类: (unmatched, extra_fid, normal_count)"""
    if not doc_root.exists():
        return [], [], 0

    unmatched = []       # 路径和文件名中均无特性ID
    extra_fid = []       # 有特性ID但不在xlsx清单中
    normal = 0

    for root, dirs, filenames in os.walk(doc_root):
        dirs[:] = [d for d in dirs if not d.endswith(".assets")]

        path_parts = Path(root).parts
        path_fids = []
        for part in path_parts:
            m = FEATURE_DIR_PATTERN.match(part)
            if m:
                path_fids.append(f"{m.group(1)}-{m.group(2)}")

        for fn in sorted(filenames):
            if not fn.endswith(".md"):
                continue

            try:
                rel = str((Path(root) / fn).relative_to(PROJECT_ROOT)).replace("\\", "/")
            except ValueError:
                rel = str(Path(root) / fn).replace("\\", "/")

            assigned = ""
            if path_fids:
                assigned = path_fids[-1]
            else:
                m2 = re.match(r"^(GWFD|WSFD|IPFD|NPFD)-(\d{3,6})", fn)
                if m2:
                    assigned = f"{m2.group(1)}-{m2.group(2)}"

            if not assigned:
                unmatched.append(rel)
            elif assigned not in fid_set:
                extra_fid.append((assigned, rel))
            else:
                normal += 1

    return unmatched, extra_fid, normal


def main():
    data_dir = BASE_DIR / "data"

    # 加载数据
    udg_features = load_features(data_dir / "UDG_features.csv")
    unc_features = load_features(data_dir / "UNC_features.csv")
    udg_mapped = load_mapped(data_dir / "UDG_feature_files.csv")
    unc_mapped = load_mapped(data_dir / "UNC_feature_files.csv")

    udg_fid_set = set(r["feature_id"] for r in udg_features)
    unc_fid_set = set(r["feature_id"] for r in unc_features)
    name_map = {r["feature_id"]: r["feature_name"] for r in udg_features + unc_features}

    # 扫描全部md
    udg_unmatched, udg_extra, udg_normal = scan_all_md(UDG_DOC_ROOT, udg_fid_set)
    unc_unmatched, unc_extra, unc_normal = scan_all_md(UNC_DOC_ROOT, unc_fid_set)

    # 生成报告
    lines = []

    def p(s=""):
        lines.append(s)

    p("# 特性文档映射审核报告")
    p()

    # ── Section 1: 未归类md ──
    p("## 1. md文件未归类到任何特性（路径和文件名中均无特性ID）")
    p()
    p(f"共 {len(udg_unmatched) + len(unc_unmatched)} 个文件")
    p()
    p(f"### UDG ({len(udg_unmatched)} 个)")
    p()
    for f in udg_unmatched:
        p(f"- `{f}`")
    p()
    p(f"### UNC ({len(unc_unmatched)} 个)")
    p()
    for f in unc_unmatched:
        p(f"- `{f}`")

    # ── Section 2: 特性不在清单 ──
    p()
    p("## 2. md文件归属的特性不在xlsx特性清单中")
    p()
    p(f"共 {len(udg_extra) + len(unc_extra)} 个文件")
    p()
    p(f"### UDG ({len(udg_extra)} 个)")
    p()
    for fid, fpath in udg_extra:
        p(f"- `{fid}` | `{fpath}`")
    p()
    p(f"### UNC ({len(unc_extra)} 个)")
    p()
    for fid, fpath in unc_extra:
        p(f"- `{fid}` | `{fpath}`")

    # ── Section 3: 特性无文档 ──
    p()
    p("## 3. 特性清单中有特性但无md文档")
    p()

    for label, features, mapped in [("UDG", udg_features, udg_mapped), ("UNC", unc_features, unc_mapped)]:
        no_docs = [f for f in features if f["feature_id"] not in mapped]
        p(f"### {label}: {len(no_docs)} 个特性无文档 (共 {len(features)} 个)")
        p()
        p("| feature_id | 特性名称 | 类型 | 所属分组 | 父特性 |")
        p("|------------|----------|------|----------|--------|")
        for f in no_docs:
            tp = "目录" if f["is_directory"] == "true" else "叶子"
            parent = f.get("parent_feature_id", "")
            parent_name = name_map.get(parent, "")
            parent_str = f"{parent} {parent_name}" if parent else ""
            p(f"| {f['feature_id']} | {f['feature_name']} | {tp} | {f['section']} | {parent_str} |")
        p()

    # ── Section 4: 汇总 ──
    p("## 4. 统计汇总")
    p()

    udg_total_md = udg_normal + len(udg_unmatched) + len(udg_extra)
    unc_total_md = unc_normal + len(unc_unmatched) + len(unc_extra)
    udg_no_doc = sum(1 for f in udg_features if f["feature_id"] not in udg_mapped)
    unc_no_doc = sum(1 for f in unc_features if f["feature_id"] not in unc_mapped)
    udg_has_doc = len(udg_features) - udg_no_doc
    unc_has_doc = len(unc_features) - unc_no_doc

    p("| 指标 | UDG | UNC | 合计 |")
    p("|------|-----|-----|------|")
    p(f"| 特性总数 | {len(udg_features)} | {len(unc_features)} | {len(udg_features) + len(unc_features)} |")
    p(f"| 有文档特性 | {udg_has_doc} | {unc_has_doc} | {udg_has_doc + unc_has_doc} |")
    p(f"| 无文档特性 | {udg_no_doc} | {unc_no_doc} | {udg_no_doc + unc_no_doc} |")
    p(f"| 已归类md | {udg_normal} | {unc_normal} | {udg_normal + unc_normal} |")
    p(f"| 未归类md(无特性ID) | {len(udg_unmatched)} | {len(unc_unmatched)} | {len(udg_unmatched) + len(unc_unmatched)} |")
    p(f"| 归属非清单特性md | {len(udg_extra)} | {len(unc_extra)} | {len(udg_extra) + len(unc_extra)} |")
    p(f"| md文件总计 | {udg_total_md} | {unc_total_md} | {udg_total_md + unc_total_md} |")

    # 写出
    report = "\n".join(lines)
    out_path = data_dir / "audit_report.md"
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(report)

    # 控制台打印摘要
    print(report)
    print(f"\n[OK] Report saved to {out_path}")


if __name__ == "__main__":
    main()
