# -*- coding: utf-8 -*-
"""Full exhaustive scan of ALL UDG and UNC feature directories."""
import os, re, sys, json

sys.stdout.reconfigure(encoding='utf-8')

UDG_BASE = 'D:/mywork/KnowledgeBase/SFCGraph/output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南'
UNC_BASE = 'D:/mywork/KnowledgeBase/SFCGraph/output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南'

# Mandatory include directories (user specified)
UDG_MANDATORY = {'业务感知功能', '计费功能', '智能策略控制功能'}

def scan_dir_full(base, dir_name):
    """Return all features as list of dicts."""
    full = os.path.join(base, dir_name)
    if not os.path.isdir(full):
        return []

    features = []

    # Subdirectory features
    for entry in sorted(os.listdir(full)):
        p = os.path.join(full, entry)
        if os.path.isdir(p) and not entry.endswith('.assets'):
            m = re.match(r'((?:GWFD|WSFD|IPFD|NPFD)-\d+)\s+(.+)', entry)
            if m:
                features.append({
                    'id': m.group(1),
                    'name': m.group(2),
                    'dir': dir_name,
                    'type': 'subdir'
                })
            else:
                features.append({
                    'id': '?',
                    'name': entry,
                    'dir': dir_name,
                    'type': 'subdir'
                })

    # Standalone md features
    for entry in sorted(os.listdir(full)):
        if entry.endswith('.md') and not entry.endswith('.assets'):
            m = re.match(r'((?:GWFD|WSFD|IPFD|NPFD)-\d+)\s+(.+?)_\d+\.md', entry)
            if m:
                fid, fname = m.group(1), m.group(2)
                if not any(f['id'] == fid and f['name'] == fname for f in features):
                    features.append({
                        'id': fid,
                        'name': fname,
                        'dir': dir_name,
                        'type': 'md'
                    })
            else:
                # non-standard name, skip overview/参考信息 etc
                name = re.sub(r'_\d{6,}\.md$', '', entry)
                if '概述' not in name and '参考信息' not in name and '描述' not in name:
                    features.append({
                        'id': '?',
                        'name': name,
                        'dir': dir_name,
                        'type': 'md'
                    })

    return features

def determine_nf(feature_id):
    """Determine network element from feature ID prefix."""
    if feature_id.startswith('GWFD'):
        return 'UDG/UPF'
    elif feature_id.startswith('WSFD'):
        return 'UNC/SMF'
    elif feature_id.startswith('IPFD'):
        return 'UDG/UPF'
    elif feature_id.startswith('NPFD'):
        return 'UNC'
    return '?'

def scan_all(base, label, mandatory_dirs=None):
    """Scan all directories, return all features."""
    if mandatory_dirs is None:
        mandatory_dirs = set()

    all_features = []
    for entry in sorted(os.listdir(base)):
        p = os.path.join(base, entry)
        if not os.path.isdir(p):
            continue
        feats = scan_dir_full(base, entry)
        for f in feats:
            f['nf'] = determine_nf(f['id'])
            f['source'] = label
            if entry in mandatory_dirs:
                f['status'] = '纳入'
                f['reason'] = '用户要求'
            else:
                f['status'] = '未读'
                f['reason'] = ''
        all_features.extend(feats)
    return all_features

# Scan UDG
udg_features = scan_all(UDG_BASE, 'UDG', UDG_MANDATORY)

# Scan UNC - no mandatory dirs specified yet
unc_features = scan_all(UNC_BASE, 'UNC')

# Save as JSON for later processing
all_features = udg_features + unc_features
with open('D:/mywork/KnowledgeBase/SFCGraph/business-graph/feature_scan_raw.json', 'w', encoding='utf-8') as f:
    json.dump(all_features, f, ensure_ascii=False, indent=2)

# Print summary
print(f'UDG: {len(udg_features)} features')
print(f'UNC: {len(unc_features)} features')
print(f'Total: {len(all_features)} features')
print(f'UDG mandatory (纳入): {sum(1 for f in udg_features if f["status"] == "纳入")}')
print(f'UDG unread: {sum(1 for f in udg_features if f["status"] == "未读")}')
print(f'UNC unread: {sum(1 for f in unc_features if f["status"] == "未读")}')

# Print by directory for UDG
print('\n=== UDG 按目录统计 ===')
dirs = {}
for f in udg_features:
    d = f['dir']
    if d not in dirs:
        dirs[d] = {'纳入': 0, '未读': 0}
    dirs[d][f['status']] += 1
for d, counts in sorted(dirs.items()):
    flag = '★' if counts['纳入'] > 0 else ' '
    print(f'{flag} {d}: 纳入{counts["纳入"]} 未读{counts["未读"]}')

# Print by directory for UNC (top relevant dirs only)
print('\n=== UNC 按目录统计（仅可能的业务感知相关）===')
unc_dirs = {}
for f in unc_features:
    d = f['dir']
    if d not in unc_dirs:
        unc_dirs[d] = 0
    unc_dirs[d] += 1
# Print all
for d, count in sorted(unc_dirs.items(), key=lambda x: -x[1]):
    print(f'  {d}: {count}')
