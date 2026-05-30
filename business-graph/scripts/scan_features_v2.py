# -*- coding: utf-8 -*-
"""Scan ALL UDG/UNC feature directories including standalone md files."""
import os, re, sys

sys.stdout.reconfigure(encoding='utf-8')

UDG_BASE = 'D:/mywork/KnowledgeBase/SFCGraph/output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南'
UNC_BASE = 'D:/mywork/KnowledgeBase/SFCGraph/output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南'

def scan_feature_dir(base, dir_name):
    """Scan a feature group directory, return (subdir_features, md_features)."""
    full = os.path.join(base, dir_name)
    if not os.path.isdir(full):
        return [], []

    # Subdirectories = features with their own folder
    subdir_features = []
    for entry in sorted(os.listdir(full)):
        p = os.path.join(full, entry)
        if os.path.isdir(p) and not entry.endswith('.assets'):
            m = re.match(r'((?:GWFD|WSFD|IPFD|NPFD)-\d+)\s+(.+)', entry)
            if m:
                subdir_features.append((m.group(1), m.group(2), entry))
            else:
                subdir_features.append(('?', entry, entry))

    # Standalone md files = features without subdirectories
    md_features = []
    for entry in sorted(os.listdir(full)):
        if entry.endswith('.md'):
            # Try to extract feature ID from filename
            m = re.match(r'((?:GWFD|WSFD|IPFD|NPFD)-\d+)\s+(.+?)_\d+\.md', entry)
            if m:
                fid, fname = m.group(1), m.group(2)
                # Avoid duplicates with subdir features
                if not any(f[0] == fid for f in subdir_features):
                    md_features.append((fid, fname, entry))
            else:
                # md file without standard feature ID pattern
                name = entry.replace('.md', '')
                # Strip trailing _ID pattern
                name = re.sub(r'_\d{6,}$', '', name)
                md_features.append(('?', name, entry))

    return subdir_features, md_features


def scan_all_dirs(base, label):
    """Scan all top-level directories under a feature guide base."""
    print(f'\n{"="*60}')
    print(f'{label} 全量扫描')
    print(f'{"="*60}')

    total_sub = 0
    total_md = 0
    results = {}

    for entry in sorted(os.listdir(base)):
        p = os.path.join(base, entry)
        if not os.path.isdir(p):
            continue
        subdir_feats, md_feats = scan_feature_dir(base, entry)
        results[entry] = (subdir_feats, md_feats)
        total_sub += len(subdir_feats)
        total_md += len(md_feats)

    # Print all directories with their feature counts
    for dir_name, (subdir_feats, md_feats) in results.items():
        total = len(subdir_feats) + len(md_feats)
        if total == 0:
            continue
        print(f'\n## {dir_name} ({total}个特性: {len(subdir_feats)}子目录 + {len(md_feats)}单文件)\n')
        if subdir_feats:
            for fid, fname, _ in subdir_feats:
                print(f'  [{fid}] {fname}')
        if md_feats:
            for fid, fname, raw in md_feats:
                print(f'  [{fid}] {fname}  (单文件: {raw})')

    print(f'\n--- {label} 汇总: {total_sub}子目录特性 + {total_md}单文件特性 = {total_sub + total_md} ---')
    return results


udg_results = scan_all_dirs(UDG_BASE, 'UDG特性指南')
unc_results = scan_all_dirs(UNC_BASE, 'UNC特性指南')
