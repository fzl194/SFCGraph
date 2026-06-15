#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
从CSV提取24个带宽控制特性的所有md路径，按batch生成bandwidth-feature-doc-list.md。
参考 charging-feature-doc-list.md 格式。
"""
import os
import sys
import csv

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

ROOT = r'D:\mywork\KnowledgeBase\SFCGraph'

# 24个特性（按优先级排序：核心→辅助）
features_ordered = [
    # === 核心特性（11个） ===
    ('GWFD-110101', 'SA-Basic', 'UDG', '业务感知基础'),
    ('GWFD-020351', 'PCC基本功能', 'UDG', 'PCC框架基础'),
    ('GWFD-110311', '基于业务感知的带宽控制', 'UDG', '★核心：SA触发BWM/Shaping'),
    ('GWFD-110312', '基于业务累计流量的策略控制', 'UDG', 'FUP业务级'),
    ('GWFD-110313', '基于智能Shaping的组级带宽控制', 'UDG', '组级Shaping'),
    ('GWFD-020353', '基于累计流量的策略控制', 'UDG', 'FUP基础（2_3_4G）'),
    ('GWFD-020354', '基于业务的Shaping', 'UDG', '业务级Shaping'),
    ('WSFD-109101', 'PCC基本功能', 'UNC', 'PCC框架基础'),
    ('WSFD-109104', '基于累计流量的策略控制', 'UNC', 'FUP基础（Gx/N7）'),
    ('WSFD-211005', '基于业务感知的带宽控制', 'UNC', '★核心：SA触发BWM'),
    ('WSFD-211009', '基于业务累计流量的策略控制', 'UNC', 'FUP业务级（Gx/N7）'),
    # === 辅助特性（13个） ===
    ('GWFD-020357', '增强的ADC基本功能', 'UDG', 'ADC应用检测'),
    ('GWFD-020358', '业务触发的QoS保证', 'UDG', '专用承载/QoS Flow'),
    ('GWFD-020359', 'IM类业务无线资源管控', 'UDG', 'IM类业务保障'),
    ('GWFD-110301', '基于终端系统的码率差异化控制', 'UDG', '终端系统码率'),
    ('GWFD-110302', '基于上下行解耦的视频承载信令控制', 'UDG', '视频承载'),
    ('GWFD-110331', '基于业务流标识的无线资源优化', 'UDG', '无线资源优化'),
    ('GWFD-110332', '基于小区负荷上报的无线资源优化', 'UDG', '小区负荷'),
    ('GWFD-020305', '终端异常下行流量检测', 'UDG', '异常流量检测'),
    ('GWFD-111600', 'SA特征库更新管控', 'UDG', 'SA特征库'),
    ('WSFD-109102', 'ADC基本功能', 'UNC', 'ADC应用检测'),
    ('WSFD-109107', '业务触发的QoS保证', 'UNC', '专用承载/QoS Flow'),
    ('WSFD-109108', '基于接入点策略控制', 'UNC', 'APN/DNN策略'),
    ('WSFD-211101', '基于小区负荷上报的无线资源优化', 'UNC', '小区负荷'),
]


def load_csv_feature_files(product):
    csv_path = os.path.join(ROOT, 'feature-graph', 'data', f'{product}_feature_files.csv')
    result = {}
    with open(csv_path, encoding='utf-8') as f:
        reader = csv.DictReader(f)
        fid_col = reader.fieldnames[0]
        path_col = None
        for col in reader.fieldnames:
            cl = col.lower().strip()
            if 'path' in cl or cl == 'file_path':
                path_col = col
                break
        if not path_col:
            path_col = reader.fieldnames[1] if len(reader.fieldnames) > 1 else None
        for row in reader:
            fid = row[fid_col].strip()
            path = row[path_col].strip()
            if fid and path:
                result.setdefault(fid, []).append(path)
    return result


udg_csv = load_csv_feature_files('UDG')
unc_csv = load_csv_feature_files('UNC')

# 构建Markdown
out = []
out.append('# 带宽控制特性文档清单')
out.append('')
out.append('> 从 `feature-graph/data/UDG_feature_files.csv` 和 `feature-graph/data/UNC_feature_files.csv` 提取')
out.append(f'> 共 {len(features_ordered)} 个特性')
out.append('')

# 总览表
out.append('## 总览')
out.append('')
out.append('| # | 特性ID | 特性名称 | 产品 | 文件数 | 优先级 |')
out.append('|---|--------|---------|------|--------|--------|')
total_files = 0
for idx, (fid, fname, prod, desc) in enumerate(features_ordered, 1):
    csv_data = udg_csv if prod == 'UDG' else unc_csv
    files = sorted(csv_data.get(fid, []))
    fcount = len(files)
    total_files += fcount
    priority = '★核心' if idx <= 11 else '辅助'
    out.append(f'| {idx} | {fid} | {fname} | {prod} | {fcount} | {priority} |')
out.append(f'| | | **合计** | | **{total_files}** | |')
out.append('')
out.append('---')
out.append('')

# 每个特性的batch
for idx, (fid, fname, prod, desc) in enumerate(features_ordered, 1):
    csv_data = udg_csv if prod == 'UDG' else unc_csv
    files = sorted(csv_data.get(fid, []))
    nf = 'UPF' if prod == 'UDG' else 'SMF'
    out.append(f'## Batch-{idx:02d}: {fid} {fname} ({prod}/{nf}, {len(files)} files)')
    out.append('')
    out.append(f'> {desc}')
    out.append('')
    out.append('```')
    for f in files:
        out.append(f)
    out.append('```')
    out.append('')
    out.append('---')
    out.append('')

# 输出
output_path = os.path.join(ROOT, 'business-graph', '带宽控制场景', 'bandwidth-feature-doc-list.md')
with open(output_path, 'w', encoding='utf-8') as f:
    f.write('\n'.join(out))

print(f'Generated: {output_path}')
print(f'Total features: {len(features_ordered)}')
print(f'Total md files: {total_files}')
