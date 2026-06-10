"""批量审计脚本：对比原始md与抽取CSV的依赖关系和License"""
import csv, re, os
from pathlib import Path
from collections import defaultdict

BASE = Path(__file__).resolve().parent.parent

def load_csv(path):
    with open(path, encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))

# 加载数据
dep_udg = load_csv(BASE / "feature-graph/data/l1_udg_feature_dependency.csv")
dep_unc = load_csv(BASE / "feature-graph/data/l1_unc_feature_dependency.csv")
lic_udg = load_csv(BASE / "feature-graph/data/l1_udg_feature_license.csv")
lic_unc = load_csv(BASE / "feature-graph/data/l1_unc_feature_license.csv")
files_udg = load_csv(BASE / "feature-graph/data/UDG_feature_files.csv")
files_unc = load_csv(BASE / "feature-graph/data/UNC_feature_files.csv")

# 构建索引
dep_by_src = defaultdict(list)
for r in dep_udg + dep_unc:
    dep_by_src[r["source_feature_id"]].append(r)

lic_by_fid = defaultdict(list)
for r in lic_udg + lic_unc:
    lic_by_fid[r["feature_id"]].append(r)

# 文件映射 - 找概述文件
overview_files = {}
for rows in [files_udg, files_unc]:
    fid_files = defaultdict(list)
    for r in rows:
        fid_files[r["feature_id"]].append(r["file_path"])
    for fid, fps in fid_files.items():
        overview = None
        for fp in fps:
            if "概述" in os.path.basename(fp):
                overview = fp
                break
        if not overview:
            for fp in fps:
                bn = os.path.basename(fp)
                if bn.startswith(fid):
                    overview = fp
                    break
        if not overview and len(fps) == 1:
            overview = fps[0]
        if overview:
            overview_files[fid] = overview

SECTION_RE = re.compile(r"####\s*\[([^\]]+)\]")
FEATURE_ID_SEARCH_RE = re.compile(r"((?:GWFD|WSFD|IPFD|NPFD|SFFD)-\d{3,6})")

def read_sections(filepath):
    fp = Path(filepath)
    if not fp.exists():
        return None
    try:
        with open(fp, encoding="utf-8") as f:
            content = f.read()
    except Exception:
        return None
    sections = {}
    cur = None
    lines = []
    for line in content.split("\n"):
        m = SECTION_RE.match(line)
        if m:
            if cur:
                sections[cur] = "\n".join(lines).strip()
            cur = m.group(1)
            lines = []
        elif cur:
            lines.append(line)
    if cur:
        sections[cur] = "\n".join(lines).strip()
    return sections

def parse_dep_table(text):
    """解析交互表格，返回原始行"""
    if not text or "不涉及" in text:
        return []
    rows = []
    for line in text.split("\n"):
        parts = [p.strip() for p in line.strip().split("|")]
        parts = [p for p in parts if p and p != "---"]
        if len(parts) < 4:
            continue
        header0 = parts[0].strip("*").strip()
        header1 = parts[1].strip("*").strip() if len(parts) > 1 else ""
        if header0 in ("交互类型", "交互") or header1 in ("相关特性",):
            continue
        fid_match = FEATURE_ID_SEARCH_RE.search(parts[1])
        target_fid = fid_match.group(1) if fid_match else ""
        rows.append({
            "dep_type_raw": parts[0],
            "related_raw": parts[1],
            "control_item": parts[2] if len(parts) > 2 else "",
            "description": parts[3] if len(parts) > 3 else "",
            "target_fid": target_fid,
        })
    return rows

# ========== PART 1: 依赖关系审计 ==========
print("=" * 70)
print("PART 1: 依赖关系审计")
print("=" * 70)

all_dep_fids = sorted(set(r["source_feature_id"] for r in dep_udg + dep_unc))
# 按前缀分层抽样
gwfd = [f for f in all_dep_fids if f.startswith("GWFD")]
ipfd_npfd = [f for f in all_dep_fids if f.startswith("IPFD") or f.startswith("NPFD")]
wsfd = [f for f in all_dep_fids if f.startswith("WSFD")]

audit_dep_fids = gwfd + ipfd_npfd + wsfd[:30]

dep_pass = dep_partial = dep_fail = 0
dep_details = []
dropped_rows = []

for fid in audit_dep_fids:
    product = "UDG" if fid.startswith("GWFD") or fid.startswith("IPFD") or fid.startswith("NPFD") else "UNC"
    csv_rows = dep_by_src[fid]

    if fid not in overview_files:
        dep_details.append((fid, len(csv_rows), 0, "NO_OVERVIEW_FILE", "SKIP"))
        continue

    sections = read_sections(overview_files[fid])
    if sections is None:
        dep_details.append((fid, len(csv_rows), 0, "FILE_READ_ERROR", "SKIP"))
        continue

    dep_text = ""
    for key in sections:
        if "交互" in key and "特性" in key:
            dep_text = sections[key]
            break

    orig_rows = parse_dep_table(dep_text)
    orig_with_fid = [r for r in orig_rows if r["target_fid"]]
    orig_without_fid = [r for r in orig_rows if not r["target_fid"]]

    csv_targets = set(r["target_feature_id"] for r in csv_rows)
    orig_targets = set(r["target_fid"] for r in orig_with_fid)

    missing_in_csv = orig_targets - csv_targets
    extra_in_csv = csv_targets - orig_targets

    issues = []
    if missing_in_csv:
        issues.append(f"Missing:{missing_in_csv}")
    if extra_in_csv:
        issues.append(f"Extra:{extra_in_csv}")
    for r in orig_without_fid:
        dropped_rows.append((fid, r["related_raw"], r["dep_type_raw"]))
        issues.append(f"NoFID:{r['related_raw'][:30]}")

    # 检查类型映射错误
    type_map = {
        "依赖": "depends_on", "必须先开启": "depends_on",
        "互斥": "conflicts_with", "冲突": "conflicts_with",
        "影响": "affects", "支持": "supports",
    }
    for csv_r in csv_rows:
        for orig_r in orig_with_fid:
            if csv_r["target_feature_id"] == orig_r["target_fid"]:
                raw = orig_r["dep_type_raw"]
                for k, v in type_map.items():
                    if k in raw and csv_r["dependency_type"] != v:
                        issues.append(f"TypeMap:{csv_r['target_feature_id']} raw={raw} csv={csv_r['dependency_type']}")

    verdict = "PASS"
    if missing_in_csv or extra_in_csv:
        verdict = "FAIL" if len(missing_in_csv) > 1 else "PARTIAL"
    elif orig_without_fid:
        verdict = "PARTIAL"

    if verdict == "PASS": dep_pass += 1
    elif verdict == "PARTIAL": dep_partial += 1
    else: dep_fail += 1

    dep_details.append((fid, len(csv_rows), len(orig_with_fid), " | ".join(issues) if issues else "OK", verdict))

print(f"\nAudited: {len(dep_details)} features")
print(f"PASS: {dep_pass} | PARTIAL: {dep_partial} | FAIL: {dep_fail}")
print()

print("--- NON-PASS Details ---")
for fid, csv_n, orig_n, issues, verdict in dep_details:
    if verdict != "PASS":
        print(f"  [{verdict}] {fid}: CSV={csv_n} Orig={orig_n} | {issues}")

print(f"\n--- Dropped rows (no feature ID in original): {len(dropped_rows)} ---")
for fid, raw, dtype in dropped_rows[:40]:
    print(f"  {fid}: type={dtype} raw='{raw[:60]}'")
if len(dropped_rows) > 40:
    print(f"  ... and {len(dropped_rows) - 40} more")


# ========== PART 2: License 审计 ==========
print("\n" + "=" * 70)
print("PART 2: License 审计")
print("=" * 70)

# 找所有 has_overview=yes 的特性
feat_udg = load_csv(BASE / "feature-graph/data/l1_udg_feature_attributes.csv")
feat_unc = load_csv(BASE / "feature-graph/data/l1_unc_feature_attributes.csv")

all_features = feat_udg + feat_unc
overview_yes = [r["feature_id"] for r in all_features if r.get("has_overview") == "yes"]

# 分成有license和无license两组
with_lic = [fid for fid in overview_yes if lic_by_fid[fid]]
without_lic = [fid for fid in overview_yes if not lic_by_fid[fid]]

print(f"\nhas_overview=yes: {len(overview_yes)}")
print(f"With license in CSV: {len(with_lic)}")
print(f"Without license in CSV: {len(without_lic)}")

# 审计有License的 (抽样30个)
lic_pass = lic_fail = 0
lic_issues = []
lic_audit = list(with_lic[:30])

for fid in lic_audit:
    if fid not in overview_files:
        continue
    sections = read_sections(overview_files[fid])
    if sections is None:
        continue

    # 找"可获得性" section
    avail_text = ""
    for key in sections:
        if "可获得性" in key or "可获得" in key:
            avail_text = sections[key]
            break

    if not avail_text:
        lic_issues.append((fid, "NO_SECTION", lic_by_fid[fid]))
        lic_fail += 1
        continue

    # 检查是否说无需License
    if "无需" in avail_text and "License" in avail_text:
        lic_issues.append((fid, "SHOULD_BE_EMPTY", lic_by_fid[fid]))
        lic_fail += 1
        continue

    # 统计原文中应该有多少条license
    lic_pattern = re.compile(r"[A-Za-z0-9]{6,12}\s+[A-Za-z0-9_\-]+\s+.{4,}")
    lic_matches = lic_pattern.findall(avail_text)
    expected_count = len(lic_matches)
    actual_count = len(lic_by_fid[fid])

    # 检查字段正确性
    field_issues = []
    for lr in lic_by_fid[fid]:
        if not lr["license_number"] or len(lr["license_number"]) < 6:
            field_issues.append(f"bad_number:{lr['license_number']}")
        if not lr["license_name"] or len(lr["license_name"]) < 3:
            field_issues.append(f"bad_name:{lr['license_name']}")

    if field_issues:
        lic_issues.append((fid, f"FIELD_ERR:{field_issues}", lic_by_fid[fid]))
        lic_fail += 1
    elif abs(expected_count - actual_count) <= 1:
        lic_pass += 1
    else:
        lic_issues.append((fid, f"COUNT_MISMATCH:expected~{expected_count}_got_{actual_count}", lic_by_fid[fid]))
        lic_fail += 1

print(f"\nLicense audit (with license): {len(lic_audit)} sampled")
print(f"PASS: {lic_pass} | FAIL: {lic_fail}")

# 审计无License的 (抽样30个看是否真的无需License)
missed_license = []
no_license_needed = []
lic_audit_empty = list(without_lic[:30])

for fid in lic_audit_empty:
    if fid not in overview_files:
        continue
    sections = read_sections(overview_files[fid])
    if sections is None:
        continue

    avail_text = ""
    for key in sections:
        if "可获得性" in key or "可获得" in key:
            avail_text = sections[key]
            break

    if not avail_text:
        continue

    if "无需" in avail_text and "License" in avail_text:
        no_license_needed.append(fid)
    else:
        # 检查是否有license内容被漏掉
        lic_matches = re.findall(r"[A-Za-z0-9]{6,12}\s+[A-Za-z0-9_\-]+\s+.{4,}", avail_text)
        if lic_matches:
            missed_license.append((fid, lic_matches))
        else:
            # 可能是其他格式的"无需"
            if "License" in avail_text or "license" in avail_text.lower():
                no_license_needed.append(fid)

print(f"\nLicense audit (without license): {len(lic_audit_empty)} sampled")
print(f"No license needed (correct): {len(no_license_needed)}")
print(f"MISSED (should have license): {len(missed_license)}")

for fid, matches in missed_license:
    print(f"  MISSED: {fid}")
    for m in matches[:3]:
        print(f"    -> {m[:80]}")


# ========== PART 3: 统计汇总 ==========
print("\n" + "=" * 70)
print("PART 3: 汇总统计")
print("=" * 70)

total_deps = len(dep_udg) + len(dep_unc)
total_lics = len(lic_udg) + len(lic_unc)

print(f"\nDependencies: {total_deps} total")
print(f"  UDG: {len(dep_udg)} | UNC: {len(dep_unc)}")
print(f"  Audited: {len(dep_details)}")
print(f"  Dep PASS: {dep_pass} ({dep_pass*100//max(len(dep_details),1)}%)")
print(f"  Dep PARTIAL: {dep_partial}")
print(f"  Dep FAIL: {dep_fail}")
print(f"  Dropped (no FID): {len(dropped_rows)}")

print(f"\nLicenses: {total_lics} total")
print(f"  UDG: {len(lic_udg)} | UNC: {len(lic_unc)}")
print(f"  With license sampled: {len(lic_audit)}, PASS: {lic_pass}, FAIL: {lic_fail}")
print(f"  Without license sampled: {len(lic_audit_empty)}")
print(f"  Correctly no license: {len(no_license_needed)}")
print(f"  Missed (extraction bug): {len(missed_license)}")
