# -*- coding: utf-8 -*-
"""Copy included feature MD files to SKILL/feature/{网元}/{特性ID}/ structure."""
import csv, json, os, shutil, sys

sys.stdout.reconfigure(encoding='utf-8')

BASE = 'D:/mywork/KnowledgeBase/SFCGraph'
OUTPUT = f'{BASE}/output'
DEST = f'{BASE}/business-graph/SKILL/feature'

# 1. Load included features
with open(f'{BASE}/business-graph/scripts/feature_scan_raw.json', 'r', encoding='utf-8') as f:
    features = json.load(f)
included_ids = {f['id'] for f in features if f['status'] == '纳入'}
# Map feature_id -> {id, name, nf, source}
feat_map = {f['id']: f for f in features if f['status'] == '纳入'}

print(f'Included features: {len(included_ids)}')

# 2. Load file mappings from CSV
file_map = {}  # feature_id -> [relative_paths]
for csv_file in ['UDG_feature_files.csv', 'UNC_feature_files.csv']:
    csv_path = f'{BASE}/FeatureGraph/data/legacy/{csv_file}'
    if not os.path.exists(csv_path):
        continue
    with open(csv_path, 'r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        for row in reader:
            fid = row['feature_id'].strip()
            fpath = row['file_path'].strip()
            if fid not in file_map:
                file_map[fid] = []
            file_map[fid].append(fpath)

# 3. Map source to NF tag for directory naming
def get_nf_dir(feat):
    """Return NF directory name like UDG/UPF or UNC/SMF."""
    source = feat['source']
    nf = feat['nf'].split('/')[-1] if '/' in feat['nf'] else feat['nf']
    return f'{source}/{nf}'

# 4. Copy files
copied_features = 0
copied_files = 0
missing = []

for fid in sorted(included_ids):
    feat = feat_map[fid]
    nf_dir = get_nf_dir(feat)
    dest_dir = f'{DEST}/{nf_dir}/{fid}'

    if fid not in file_map:
        missing.append(fid)
        continue

    os.makedirs(dest_dir, exist_ok=True)

    for rel_path in file_map[fid]:
        src = f'{BASE}/{rel_path}'
        if not os.path.exists(src):
            # Try with output prefix
            src = f'{OUTPUT}/{rel_path.replace("output/", "", 1)}' if rel_path.startswith('output/') else src
        if os.path.exists(src):
            fname = os.path.basename(src)
            dest_file = f'{dest_dir}/{fname}'
            shutil.copy2(src, dest_file)
            copied_files += 1
        else:
            if fid not in missing:
                missing.append(fid)

    if os.listdir(dest_dir):
        copied_features += 1
    else:
        os.rmdir(dest_dir)
        if fid not in missing:
            missing.append(fid)

print(f'Copied: {copied_features} features, {copied_files} files')
if missing:
    print(f'\nMissing ({len(missing)}):')
    for m in missing:
        feat = feat_map.get(m, {})
        print(f'  {m} {feat.get("name", "?")} ({feat.get("nf", "?")})')

# 5. Summary by NF
print('\n--- Summary ---')
nf_count = {}
for fid in sorted(included_ids):
    feat = feat_map[fid]
    nf_dir = get_nf_dir(feat)
    nf_count[nf_dir] = nf_count.get(nf_dir, 0) + 1
for nf, c in sorted(nf_count.items()):
    print(f'{nf}: {c} features')
