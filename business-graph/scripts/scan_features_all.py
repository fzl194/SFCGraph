# -*- coding: utf-8 -*-
"""Scan remaining UDG directories for business-awareness related features."""
import os, re, sys

sys.stdout.reconfigure(encoding='utf-8')

BASE = 'D:/mywork/KnowledgeBase/SFCGraph/output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南'

# Directories already covered
COVERED = {'业务感知功能', '计费功能', '智能策略控制功能'}

# Keywords that suggest business-awareness relevance
SA_KEYWORDS = [
    '计费', '策略', 'QoS', '带宽', '分流', '流量', 'DPI', '规则',
    '配额', '欠费', '重定向', 'Portal', '阻塞', '过滤', '识别',
    'PCC', 'ADC', 'URR', 'Filter', 'Rule', 'Shaping', '限速',
    '业务', '报表', '防欺诈', '体验', '保障', 'DNN', '园区',
]

def scan_dir(dir_name):
    """Scan a feature directory, return list of (feature_id, feature_name)."""
    full = os.path.join(BASE, dir_name)
    if not os.path.isdir(full):
        return []
    features = []
    for entry in sorted(os.listdir(full)):
        p = os.path.join(full, entry)
        if os.path.isdir(p) and not entry.endswith('.assets'):
            m = re.match(r'(GWFD-\d+)\s+(.+)', entry)
            if m:
                features.append((m.group(1), m.group(2)))
            else:
                features.append(('?', entry))
    return features

def has_sa_relevance(dir_name, features):
    """Check if directory or its features have SA relevance."""
    # Check directory name
    for kw in SA_KEYWORDS:
        if kw in dir_name:
            return True, f'目录名含"{kw}"'
    # Check feature names
    for fid, fname in features:
        for kw in SA_KEYWORDS:
            if kw in fname:
                return True, f'特性"{fname}"含"{kw}"'
    return False, ''

# Scan all remaining directories
print('--- UDG其余目录扫描 ---\n')

maybe_relevant = []
irrelevant = []

for entry in sorted(os.listdir(BASE)):
    p = os.path.join(BASE, entry)
    if not os.path.isdir(p) or entry in COVERED:
        continue
    features = scan_dir(entry)
    relevant, reason = has_sa_relevance(entry, features)

    if relevant:
        maybe_relevant.append((entry, features, reason))
    else:
        irrelevant.append((entry, len(features)))

# Print potentially relevant
print(f'=== 可能与业务感知相关的目录（{len(maybe_relevant)}个） ===\n')
for dir_name, features, reason in maybe_relevant:
    print(f'## {dir_name} ({len(features)}个特性) — {reason}')
    print('| # | 特性ID | 特性名称 |')
    print('|---|--------|---------|')
    for i, (fid, fname) in enumerate(features, 1):
        print(f'| {i} | {fid} | {fname} |')
    print()

# Print irrelevant
print(f'=== 与业务感知无关的目录（{len(irrelevant)}个） ===\n')
for dir_name, count in irrelevant:
    print(f'  - {dir_name} ({count}个特性)')
