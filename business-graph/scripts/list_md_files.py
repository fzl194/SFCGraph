# -*- coding: utf-8 -*-
"""Helper: list md file paths for unread features in specified directories."""
import json, os, re, sys

sys.stdout.reconfigure(encoding='utf-8')

UDG_BASE = 'D:/mywork/KnowledgeBase/SFCGraph/output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南'
UNC_BASE = 'D:/mywork/KnowledgeBase/SFCGraph/output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南'

with open('D:/mywork/KnowledgeBase/SFCGraph/business-graph/feature_scan_raw.json', 'r', encoding='utf-8') as f:
    features = json.load(f)

# Filter by dirs and unread status
target_dirs = sys.argv[1].split(',') if len(sys.argv) > 1 else []
source = sys.argv[2] if len(sys.argv) > 2 else 'UDG'

base = UDG_BASE if source == 'UDG' else UNC_BASE

feats = [f for f in features if f['source'] == source and f['dir'] in target_dirs and f['status'] == '未读']

print(f'Found {len(feats)} unread features in {target_dirs}\n')

for f in feats:
    dir_path = os.path.join(base, f['dir'])

    if f['type'] == 'subdir':
        # Look for 特性概述 md in the subdir
        subdir_name = None
        for entry in os.listdir(dir_path):
            if f['id'] in entry and os.path.isdir(os.path.join(dir_path, entry)):
                subdir_name = entry
                break
        if subdir_name:
            subdir_path = os.path.join(dir_path, subdir_name)
            # Find overview md
            for md in sorted(os.listdir(subdir_path)):
                if md.endswith('.md') and ('概述' in md or '特性概述' in md or '功能概述' in md):
                    print(f'{f["id"]}|{f["name"]}|{os.path.join(subdir_path, md)}')
                    break
            else:
                # No overview found, list first md
                mds = [m for m in sorted(os.listdir(subdir_path)) if m.endswith('.md')]
                if mds:
                    print(f'{f["id"]}|{f["name"]}|{os.path.join(subdir_path, mds[0])}')
                else:
                    print(f'{f["id"]}|{f["name"]}|NO_MD_FOUND')
        else:
            print(f'{f["id"]}|{f["name"]}|SUBDIR_NOT_FOUND')
    else:
        # Single md file
        md_name = None
        for entry in os.listdir(dir_path):
            if entry.endswith('.md') and f['id'] in entry:
                md_name = entry
                break
        if md_name:
            print(f'{f["id"]}|{f["name"]}|{os.path.join(dir_path, md_name)}')
        else:
            print(f'{f["id"]}|{f["name"]}|MD_NOT_FOUND')
