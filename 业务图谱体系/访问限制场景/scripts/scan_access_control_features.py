#!/usr/bin/env python3
"""
扫描访问限制场景相关特性的所有md文件
从feature-graph/data的CSV文件中筛选
"""

import csv
import os

# 访问限制场景相关特性ID列表
ACCESS_CONTROL_FEATURES = [
    # UDG 特性
    'GWFD-020357',  # 增强的ADC基本功能
    'GWFD-110261',  # HTTP头增强
    'GWFD-110262',  # RTSP头增强
    'GWFD-110263',  # HTTPS头增强
    'GWFD-110281',  # 用户Portal
    'GWFD-110282',  # Web Proxy
    'GWFD-110284',  # HTTP智能重定向
    'GWFD-110471',  # URL过滤基本功能
    'GWFD-110401',  # HTTP头防欺诈
    # UNC 特性
    'WSFD-109102',  # ADC基本功能
    'WSFD-211001',  # 基于初始接入位置的策略控制
]

UDG_ROOT = 'D:/mywork/KnowledgeBase/SFCGraph/output/UDG_Product_Documentation_CH_20.15.2'
UNC_ROOT = 'D:/mywork/KnowledgeBase/SFCGraph/output/UNC 20.15.2 产品文档(裸机容器) 05'

def scan_features():
    """从CSV扫描并列出所有特性文件"""

    results = {}

    # 扫描UDG
    udg_csv = 'D:/mywork/KnowledgeBase/SFCGraph/feature-graph/data/UDG_feature_files.csv'
    with open(udg_csv, 'r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        for row in reader:
            fid = row['feature_id']
            if fid in ACCESS_CONTROL_FEATURES:
                if fid not in results:
                    results[fid] = {'product': 'UDG', 'files': []}
                full_path = os.path.join(UDG_ROOT, row['file_path'])
                results[fid]['files'].append(full_path)

    # 扫描UNC
    unc_csv = 'D:/mywork/KnowledgeBase/SFCGraph/feature-graph/data/UNC_feature_files.csv'
    with open(unc_csv, 'r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        for row in reader:
            fid = row['feature_id']
            if fid in ACCESS_CONTROL_FEATURES:
                if fid not in results:
                    results[fid] = {'product': 'UNC', 'files': []}
                full_path = os.path.join(UNC_ROOT, row['file_path'])
                results[fid]['files'].append(full_path)

    return results

def scan_all_md_in_feature_dir(feature_id, product):
    """扫描特性目录下所有的md文件"""
    if product == 'UDG':
        # 扫描UDG特性指南目录
        base_dir = os.path.join(UDG_ROOT, '特性部署/特性指南/UDG特性指南')
    else:
        base_dir = os.path.join(UNC_ROOT, '网络部署/特性部署/UNC特性指南')

    all_md_files = []

    # 头增强系列
    if feature_id in ['GWFD-110261', 'GWFD-110262', 'GWFD-110263', 'GWFD-110281', 'GWFD-110282', 'GWFD-110284']:
        search_dir = os.path.join(base_dir, '智能策略控制功能')
    elif feature_id == 'GWFD-110471':
        search_dir = os.path.join(base_dir, '业务感知功能')
    elif feature_id == 'GWFD-110401':
        search_dir = os.path.join(base_dir, '计费防欺诈功能')
    elif feature_id == 'GWFD-020357':
        search_dir = os.path.join(base_dir, '智能策略控制功能/GWFD-020357 增强的ADC基本功能')
    elif feature_id == 'WSFD-109102':
        search_dir = os.path.join(base_dir, '智能PCC解决方案/WSFD-109102 ADC基本功能')
    elif feature_id == 'WSFD-211001':
        search_dir = os.path.join(base_dir, '智能PCC解决方案')
    else:
        search_dir = base_dir

    if os.path.exists(search_dir):
        for root, dirs, files in os.walk(search_dir):
            for f in files:
                if f.endswith('.md'):
                    all_md_files.append(os.path.join(root, f))

    return all_md_files

def main():
    results = scan_features()

    print("=" * 80)
    print("访问限制场景特性文件扫描结果")
    print("=" * 80)

    for fid in sorted(results.keys()):
        info = results[fid]
        print(f"\n## {fid} ({info['product']})")
        print(f"共 {len(info['files'])} 个文件（来自CSV）")

        # 额外扫描该特性目录下所有md文件
        extra_files = scan_all_md_in_feature_dir(fid, info['product'])
        if extra_files:
            # 去重
            existing = set(info['files'])
            new_files = [f for f in extra_files if f not in existing]
            if new_files:
                print(f"额外发现 {len(new_files)} 个md文件:")
                for f in sorted(new_files):
                    print(f"  + {f}")

        print("文件列表:")
        for f in sorted(info['files']):
            print(f"  - {f}")

if __name__ == '__main__':
    main()