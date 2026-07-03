#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
校验bandwidth-doc-list.md中特性文件数与CSV映射是否一致，
并校验业务专题、概念文档的md路径是否真实存在。
"""
import os
import sys
import csv
import re

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

ROOT = r'D:\mywork\KnowledgeBase\SFCGraph'

# 从doc-list.md解析的特性元数据（id, name, product, declared_count）
features_declared = [
    ('GWFD-110101', 'UDG', 7),
    ('GWFD-020351', 'UDG', 9),
    ('GWFD-020353', 'UDG', 2),
    ('GWFD-020354', 'UDG', 6),
    ('GWFD-020357', 'UDG', 5),
    ('GWFD-020358', 'UDG', 13),
    ('GWFD-020359', 'UDG', 5),
    ('GWFD-020305', 'UDG', 4),
    ('GWFD-110301', 'UDG', 3),
    ('GWFD-110302', 'UDG', 5),
    ('GWFD-110311', 'UDG', 24),
    ('GWFD-110312', 'UDG', 3),
    ('GWFD-110313', 'UDG', 4),
    ('GWFD-110331', 'UDG', 4),
    ('GWFD-110332', 'UDG', 4),
    ('GWFD-111600', 'UDG', 1),
    ('WSFD-109101', 'UNC', 25),
    ('WSFD-109102', 'UNC', 6),
    ('WSFD-109104', 'UNC', 6),
    ('WSFD-109107', 'UNC', 6),
    ('WSFD-109108', 'UNC', 3),
    ('WSFD-211005', 'UNC', 4),
    ('WSFD-211009', 'UNC', 6),
    ('WSFD-211101', 'UNC', 5),
]


def load_csv_feature_files(product):
    """加载CSV，返回{feature_id: [file_path, ...]}"""
    csv_path = os.path.join(ROOT, 'FeatureGraph', 'data', 'legacy',
                            f'{product}_feature_files.csv')
    result = {}
    with open(csv_path, encoding='utf-8') as f:
        reader = csv.DictReader(f)
        # 自动识别列名
        fid_col = None
        path_col = None
        for col in reader.fieldnames:
            cl = col.lower().strip()
            if 'feature' in cl and 'id' in cl:
                fid_col = col
            elif 'file' in cl and 'path' in cl:
                path_col = col
            elif cl == 'feature_id':
                fid_col = col
            elif cl == 'file_path':
                path_col = col
        if not fid_col or not path_col:
            # 尝试第一列和第二列
            fid_col = reader.fieldnames[0]
            path_col = reader.fieldnames[1] if len(reader.fieldnames) > 1 else None
        for row in reader:
            fid = row[fid_col].strip()
            path = row[path_col].strip()
            if fid and path:
                result.setdefault(fid, []).append(path)
    return result


print('=' * 60)
print('特性文件数校验')
print('=' * 60)
print(f'{"特性ID":<15} {"产品":<6} {"声明":<6} {"CSV":<6} {"匹配":<6}')
print('-' * 60)

udg_csv = load_csv_feature_files('UDG')
unc_csv = load_csv_feature_files('UNC')

mismatch = 0
missing_in_csv = 0
for fid, prod, declared in features_declared:
    csv_data = udg_csv if prod == 'UDG' else unc_csv
    csv_count = len(csv_data.get(fid, []))
    match = '✓' if csv_count == declared else '✗'
    if csv_count != declared:
        mismatch += 1
    if fid not in csv_data:
        missing_in_csv += 1
    print(f'{fid:<15} {prod:<6} {declared:<6} {csv_count:<6} {match}')

print('-' * 60)
print(f'总特性: {len(features_declared)}, 不匹配: {mismatch}, CSV缺失: {missing_in_csv}')

# 校验doc-list.md中的md路径是否存在
print()
print('=' * 60)
print('md文件存在性校验（业务专题+概念文档）')
print('=' * 60)
doc_list_path = os.path.join(ROOT, 'business-graph', '带宽控制场景', 'bandwidth-doc-list.md')
with open(doc_list_path, encoding='utf-8') as f:
    content = f.read()

# 提取所有以 output/ 开头、以 .md 结尾的行（允许中间含空格）
paths = re.findall(r'^(output/.*\.md)\s*$', content, re.MULTILINE)
print(f'共解析到 {len(paths)} 个md路径')

missing_files = []
for p in paths:
    abs_p = os.path.join(ROOT, p.replace('/', os.sep))
    if not os.path.exists(abs_p):
        missing_files.append(p)

if missing_files:
    print(f'✗ 不存在的路径: {len(missing_files)}')
    for m in missing_files[:20]:
        print(f'  {m}')
else:
    print('✓ 所有路径均存在')

# 统计特性部分声明的文件数总和
total_declared = sum(f[2] for f in features_declared)
print()
print('=' * 60)
print('汇总')
print('=' * 60)
print(f'特性文件总数（声明）: {total_declared}')
print(f'业务专题+概念文档md（实际路径）: {len(paths)}')
print(f'全部文档总计: {total_declared + len(paths)}')
