# -*- coding: utf-8 -*-
"""Generate final MVP feature list MD - only included features."""
import json, sys

sys.stdout.reconfigure(encoding='utf-8')

with open('D:/mywork/KnowledgeBase/SFCGraph/business-graph/scripts/feature_scan_raw.json', 'r', encoding='utf-8') as f:
    features = json.load(f)

included = [f for f in features if f['status'] == '纳入']
udg_in = [f for f in included if f['source'] == 'UDG']
unc_in = [f for f in included if f['source'] == 'UNC']

def escape_md(s):
    return str(s).replace('|', '\\|')

def print_section(title, feats):
    print(f'\n### {title}（{len(feats)}个）\n')
    print('| # | 特性ID | 特性名称 | 网元 | 层级目录 | 原因 |')
    print('|---|--------|---------|------|---------|------|')
    for i, f in enumerate(feats, 1):
        print(f'| {i} | {escape_md(f["id"])} | {escape_md(f["name"])} | {f["nf"]} | {escape_md(f["dir"])} | {escape_md(f["reason"])} |')

print('# MVP业务感知特性清单\n')
print(f'> 从651个特性中筛选出{len(included)}个与业务感知场景相关的特性\n')
print(f'| 网元 | 纳入数量 |')
print(f'|------|---------|')
print(f'| UDG (用户面) | {len(udg_in)} |')
print(f'| UNC (控制面) | {len(unc_in)} |')
print(f'| **总计** | **{len(included)}** |')

# ---- UDG纳入 ----
print('\n---\n\n## UDG 用户面纳入特性\n')
udg_dirs = []
seen = set()
for f in udg_in:
    if f['dir'] not in seen:
        udg_dirs.append(f['dir'])
        seen.add(f['dir'])

for dirname in udg_dirs:
    feats = [f for f in udg_in if f['dir'] == dirname]
    if feats:
        print_section(f'UDG - {dirname}', feats)

# ---- UNC纳入 ----
print('\n---\n\n## UNC 控制面纳入特性\n')
unc_dirs = []
seen = set()
for f in unc_in:
    if f['dir'] not in seen:
        unc_dirs.append(f['dir'])
        seen.add(f['dir'])

for dirname in unc_dirs:
    feats = [f for f in unc_in if f['dir'] == dirname]
    if feats:
        print_section(f'UNC - {dirname}', feats)
