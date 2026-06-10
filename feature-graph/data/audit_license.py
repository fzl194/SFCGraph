import csv, sys, re
sys.stdout.reconfigure(encoding='utf-8')

feature_files = {}
with open('UNC_feature_files.csv', 'r', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)
    for row in reader:
        fid = row['feature_id']
        path = row['file_path']
        if fid not in feature_files:
            feature_files[fid] = []
        feature_files[fid].append(path)

license_map = {}
with open('l1_unc_feature_license.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        fid = row['feature_id']
        if fid not in license_map:
            license_map[fid] = []
        license_map[fid].append(row)

def find_overview_file(fid):
    files = feature_files.get(fid, [])
    overview_candidates = [f for f in files if '概述' in f]
    if overview_candidates:
        return overview_candidates
    root_files = [f for f in files if not any(kw in f for kw in ['配置', '调测', '激活', '参考', '实现', '关键', 'N19', '主用', '相关', '创建', '流程', '告警'])]
    if root_files:
        return root_files[:1]
    return files[:1] if files else []

def extract_license_section(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except:
        return None, 'error'

    m = re.search(r'(?:^|\n)(#{1,6}\s*\[?可获得性\]?[^\n]*)\n(.*?)(?=\n#{1,4}[^#]|\Z)', content, re.DOTALL)
    if m:
        return m.group(0), 'found'

    for kw in ['无需License', '无需 License']:
        idx = content.find(kw)
        if idx != -1:
            return content[max(0,idx-200):idx+200], 'no_license_needed'
    return None, 'not_found'

def parse_licenses(section):
    if not section:
        return 'empty', 0, []

    if '无需License' in section or '无需 License' in section:
        return 'no_license_needed', 0, []

    # Check for table format (License控制项 table)
    table_lines = []
    in_table = False
    for line in section.split('\n'):
        stripped = line.strip()
        if 'License控制项' in stripped and stripped.startswith('|'):
            in_table = True
            continue
        if in_table:
            if stripped.startswith('|') and '---' in stripped:
                continue
            if stripped.startswith('|') and stripped.count('|') >= 3:
                table_lines.append(stripped)
            elif not stripped.startswith('|') and stripped and not stripped.startswith('>') and not stripped.startswith('**') and not stripped.startswith('-') and not stripped.startswith('本'):
                break

    if table_lines:
        licenses = []
        for tl in table_lines:
            parts = [p.strip() for p in tl.split('|')]
            # Determine format: 2-col table (适用NF, License控制项) or 3-col (特性, 适用NF, License控制项)
            if len(parts) >= 4:
                if '适用NF' in ''.join(parts):
                    # 2-col: | NF | License控制项 |
                    nf_part = parts[1] if len(parts) > 1 else ''
                    lic_part = parts[2] if len(parts) > 2 else ''
                else:
                    # 3-col: | 特性 | 适用NF | License控制项 |
                    nf_part = parts[2] if len(parts) > 2 else ''
                    lic_part = parts[3] if len(parts) > 3 else (parts[2] if len(parts) > 2 else '')

                # Handle the case where it's actually 2-col (| 适用NF | License |)
                # but parsed as 3 because of trailing |
                if lic_part == '' and len(parts) == 4:
                    lic_part = parts[2]
                    nf_part = parts[1]

            else:
                nf_part = ''
                lic_part = ''

            # Parse: number code name
            m = re.match(r'(\d+)\s+(\S+)\s+(.*)', lic_part.strip().replace('<br>', ''))
            if m:
                licenses.append((m.group(1), m.group(2), m.group(3).strip(), nf_part.replace('<br>', '')))
            else:
                licenses.append(('', '', lic_part.strip(), nf_part))
        return 'license_table', len(licenses), licenses

    # Check for quoted text format
    # Format 1: 控制项为 "NUMBER CODE NAME"
    quoted_m = re.search(r'License控制项为\s*["\u201c]?(\d+)\s+(\S+)\s+(.*?)["\u201d]?(?:。|$)', section, re.MULTILINE)
    if quoted_m:
        return 'license_quoted', 1, [(quoted_m.group(1), quoted_m.group(2), quoted_m.group(3).strip(), '')]

    # Format 2: 控制项为 CODE NUMBER NAME
    quoted_m2 = re.search(r'License控制项为\s+(\S+)\s+(\d+)\s+(.*?)(?:。|$)', section, re.MULTILINE)
    if quoted_m2:
        return 'license_quoted', 1, [(quoted_m2.group(2), quoted_m2.group(1), quoted_m2.group(3).strip(), '')]

    # Format 3: 控制项为 NUMBER CODE NAME (without quotes)
    plain_m = re.search(r'License控制项为\s+(\d+)\s+(\S+)\s+(.*?)(?:。|\n)', section)
    if plain_m:
        return 'license_plain', 1, [(plain_m.group(1), plain_m.group(2), plain_m.group(3).strip(), '')]

    return 'unknown', 0, []

# ===== AUDIT =====
cat_c = ['WSFD-106101', 'WSFD-104401', 'WSFD-225003', 'WSFD-227102']
cat_a = [
    'WSFD-010000', 'WSFD-011501', 'WSFD-102701', 'WSFD-104412',
    'WSFD-111000', 'WSFD-227101', 'WSFD-107001', 'WSFD-109001',
    'WSFD-205011', 'WSFD-102702', 'WSFD-104002', 'WSFD-223002',
]
cat_b = [
    'WSFD-010005', 'WSFD-010102', 'WSFD-010105', 'WSFD-010201',
    'WSFD-010301', 'WSFD-010400', 'WSFD-010501', 'WSFD-010701',
    'WSFD-010801', 'WSFD-011101', 'WSFD-011201', 'WSFD-011301',
    'WSFD-011502', 'WSFD-103001', 'WSFD-103002',
]

results = []

for fid in cat_c + cat_a + cat_b:
    cat = 'C' if fid in cat_c else ('A' if fid in cat_a else 'B')
    csv_licenses = license_map.get(fid, [])
    csv_count = len(csv_licenses)
    overview_files = find_overview_file(fid)

    if not overview_files:
        results.append((fid, cat, 'no_file', 0, csv_count, [], 'ERROR', 'No overview file found'))
        continue

    all_licenses = []
    section_format = 'unknown'
    notes = ''

    for of in overview_files:
        section, status = extract_license_section(of)
        if status == 'found':
            fmt, count, lics = parse_licenses(section)
            if lics:
                all_licenses.extend(lics)
                section_format = fmt
        elif status == 'no_license_needed':
            section_format = 'no_license_needed'

    expected_count = len(all_licenses)

    if section_format == 'no_license_needed' and csv_count == 0:
        verdict = 'PASS_NO_LICENSE'
    elif expected_count == csv_count and expected_count > 0:
        verdict = 'PASS'
    elif expected_count == 0 and csv_count == 0:
        verdict = 'PASS_NO_LICENSE'
    elif csv_count > 0 and expected_count > 0 and csv_count < expected_count:
        verdict = 'PARTIAL'
    elif csv_count == 0 and expected_count > 0:
        verdict = 'MISSING'
    elif csv_count > expected_count and expected_count > 0:
        verdict = 'EXTRA_IN_CSV'
    else:
        verdict = 'UNCLEAR'

    results.append((fid, cat, section_format, expected_count, csv_count, all_licenses, verdict, notes))

# Print summary table
print(f'Feature ID | Cat | Format | Expected | CSV | Verdict')
print(f'---|---|---|---|---|---')
for fid, cat, fmt, exp, csvc, lics, verdict, notes in results:
    print(f'{fid} | {cat} | {fmt} | {exp} | {csvc} | {verdict}')

print()
print('=== DETAILED FINDINGS ===')
for fid, cat, fmt, exp, csvc, lics, verdict, notes in results:
    if verdict not in ('PASS', 'PASS_NO_LICENSE'):
        print(f'\n### {fid} [Cat {cat}] - {verdict}')
        print(f'Format: {fmt}, Expected: {exp}, CSV: {csvc}')
        if lics:
            for num, code, name, nf in lics:
                print(f'  Expected: {num} {code} {name} | NF: {nf}')
        csv_data = license_map.get(fid, [])
        if csv_data:
            for row in csv_data:
                print(f'  CSV has: {row["license_number"]} {row["license_code"]} {row["license_name"]} | NF: {row["applicable_nf"]}')
