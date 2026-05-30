# -*- coding: utf-8 -*-
"""Update mandatory dirs for UNC and regenerate MD."""
import json, sys

sys.stdout.reconfigure(encoding='utf-8')

path = 'D:/mywork/KnowledgeBase/SFCGraph/business-graph/feature_scan_raw.json'
with open(path, 'r', encoding='utf-8') as f:
    features = json.load(f)

# Mark UNC mandatory directories
UNC_MANDATORY = {'智能PCC解决方案', '计费管理功能'}

updated = 0
for f in features:
    if f['source'] == 'UNC' and f['dir'] in UNC_MANDATORY and f['status'] == '未读':
        f['status'] = '纳入'
        f['reason'] = '用户要求'
        updated += 1

with open(path, 'w', encoding='utf-8') as f:
    json.dump(features, f, ensure_ascii=False, indent=2)

print(f'Updated {updated} UNC features to 纳入')

# Stats
udg_in = sum(1 for f in features if f['source']=='UDG' and f['status']=='纳入')
udg_un = sum(1 for f in features if f['source']=='UDG' and f['status']=='未读')
unc_in = sum(1 for f in features if f['source']=='UNC' and f['status']=='纳入')
unc_un = sum(1 for f in features if f['source']=='UNC' and f['status']=='未读')
print(f'UDG: 纳入{udg_in} 未读{udg_un}')
print(f'UNC: 纳入{unc_in} 未读{unc_un}')
print(f'总计: 纳入{udg_in+unc_in} 未读{udg_un+unc_un}')
