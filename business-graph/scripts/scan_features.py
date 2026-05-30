# -*- coding: utf-8 -*-
"""Scan UDG feature directories and output feature lists."""
import os, re, sys

sys.stdout.reconfigure(encoding='utf-8')

BASE = 'D:/mywork/KnowledgeBase/SFCGraph/output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南'

def scan_dir(rel_path):
    """Scan a feature directory, return list of (feature_id, feature_name, dir_name)."""
    full = os.path.join(BASE, rel_path)
    if not os.path.isdir(full):
        print(f"[WARN] Not found: {full}")
        return []
    features = []
    for entry in sorted(os.listdir(full)):
        p = os.path.join(full, entry)
        if os.path.isdir(p) and not entry.endswith('.assets'):
            m = re.match(r'(GWFD-\d+)\s+(.+)', entry)
            if m:
                features.append((m.group(1), m.group(2), entry))
            else:
                features.append(('?', entry, entry))
    return features

def print_table(title, features):
    print(f'\n## {title}（{len(features)}个）\n')
    print('| # | 特性ID | 特性名称 |')
    print('|---|--------|---------|')
    for i, (fid, fname, _) in enumerate(features, 1):
        print(f'| {i} | {fid} | {fname} |')

# 1. 业务感知功能
f1 = scan_dir('业务感知功能')
print_table('业务感知功能', f1)

# 2. 计费功能
f2 = scan_dir('计费功能')
print_table('计费功能', f2)

# 3. 智能策略控制功能
f3 = scan_dir('智能策略控制功能')
print_table('智能策略控制功能', f3)

# 4. List all other top-level dirs for exploration
print('\n--- UDG特性指南 所有目录 ---\n')
all_dirs = []
for entry in sorted(os.listdir(BASE)):
    p = os.path.join(BASE, entry)
    if os.path.isdir(p) and entry not in ('业务感知功能', '计费功能', '智能策略控制功能'):
        all_dirs.append(entry)
print(f'其他目录（{len(all_dirs)}个）:')
for d in all_dirs:
    print(f'  - {d}')
