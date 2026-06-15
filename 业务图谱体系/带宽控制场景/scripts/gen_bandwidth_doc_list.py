#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
生成带宽控制场景文档清单。
- 特性：仅列出特性ID（24个，共171文件），用户后续单独阅读
- 业务专题：列出所有md文件等权重（6个专题，281文件）
- 5G基础知识概念文档：列出所有md文件（8个目录，36文件）
- 排除：MML命令文档、其他无关业务专题
"""
import os
import sys

# 设置标准输出为utf-8（Windows下避免GBK编码问题）
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

ROOT = r'D:\mywork\KnowledgeBase\SFCGraph'
UDG_ROOT = os.path.join(ROOT, 'output', 'UDG_Product_Documentation_CH_20.15.2')
UNC_ROOT = os.path.join(ROOT, 'output', 'UNC 20.15.2 产品文档(裸机容器) 05')


def collect_md(base_abs_path):
    """递归收集目录下所有md文件，返回相对路径列表（按路径排序）。"""
    result = []
    if not os.path.exists(base_abs_path):
        return result
    for root, dirs, files in os.walk(base_abs_path):
        for f in files:
            if f.endswith('.md'):
                abs_path = os.path.join(root, f)
                rel_path = os.path.relpath(abs_path, ROOT).replace(os.sep, '/')
                result.append(rel_path)
    return sorted(result)


# ============================================================
# Part 1: 特性清单（24个，仅ID和概要，不展开文件）
# ============================================================
features = [
    # UDG 16个
    ('GWFD-110101', 'SA-Basic', 'UDG', 7, '业务感知基础（与计费场景共享，需重读）'),
    ('GWFD-020351', 'PCC基本功能', 'UDG', 9, 'PCC框架基础（与计费场景共享，需重读）'),
    ('GWFD-110311', '基于业务感知的带宽控制', 'UDG', 24, '★核心：SA触发BWM/Shaping'),
    ('GWFD-110312', '基于业务累计流量的策略控制', 'UDG', 3, 'FUP业务级'),
    ('GWFD-110313', '基于智能Shaping的组级带宽控制', 'UDG', 4, '组级Shaping'),
    ('GWFD-020353', '基于累计流量的策略控制', 'UDG', 2, 'FUP基础（2_3_4G）'),
    ('GWFD-020354', '基于业务的Shaping', 'UDG', 6, '业务级Shaping'),
    ('GWFD-020357', '增强的ADC基本功能', 'UDG', 5, 'ADC应用检测'),
    ('GWFD-020358', '业务触发的QoS保证', 'UDG', 13, '专用承载/QoS Flow'),
    ('GWFD-020359', 'IM类业务无线资源管控', 'UDG', 5, 'IM类业务保障'),
    ('GWFD-110301', '基于终端系统的码率差异化控制', 'UDG', 3, '终端系统码率'),
    ('GWFD-110302', '基于上下行解耦的视频承载信令控制', 'UDG', 5, '视频承载'),
    ('GWFD-110331', '基于业务流标识的无线资源优化', 'UDG', 4, '无线资源优化'),
    ('GWFD-110332', '基于小区负荷上报的无线资源优化', 'UDG', 4, '小区负荷'),
    ('GWFD-020305', '终端异常下行流量检测', 'UDG', 4, '异常流量检测'),
    ('GWFD-111600', 'SA特征库更新管控', 'UDG', 1, 'SA特征库'),
    # UNC 8个
    ('WSFD-109101', 'PCC基本功能', 'UNC', 25, 'PCC框架（与计费场景共享，需重读）'),
    ('WSFD-109102', 'ADC基本功能', 'UNC', 6, 'ADC应用检测'),
    ('WSFD-109104', '基于累计流量的策略控制', 'UNC', 6, 'FUP基础（Gx/N7）'),
    ('WSFD-109107', '业务触发的QoS保证', 'UNC', 6, '专用承载/QoS Flow'),
    ('WSFD-109108', '基于接入点策略控制', 'UNC', 3, 'APN/DNN策略'),
    ('WSFD-211005', '基于业务感知的带宽控制', 'UNC', 4, '★核心：SA触发BWM'),
    ('WSFD-211009', '基于业务累计流量的策略控制', 'UNC', 6, 'FUP业务级（Gx/N7）'),
    ('WSFD-211101', '基于小区负荷上报的无线资源优化', 'UNC', 5, '小区负荷'),
]

# ============================================================
# Part 2: 业务专题（6个，列出所有md文件）
# ============================================================
topics = [
    ('UDG', 'UDG业务感知专题', os.path.join(UDG_ROOT, '特性部署', '业务专题', 'UDG业务感知专题'),
     'SA基础+ SA action含BWM/Shaping/重定向/阻塞/Remark'),
    ('UDG', '5G Core FUP解决方案', os.path.join(UDG_ROOT, '特性部署', '业务专题', '5G Core FUP解决方案'),
     'FUP累计流量带宽控制方案'),
    ('UDG', '5G Core 重点业务保障解决方案', os.path.join(UDG_ROOT, '特性部署', '业务专题', '5G Core 重点业务保障解决方案'),
     'GBR保障/重点业务带宽保障'),
    ('UDG', '5G Core 体验感知解决方案', os.path.join(UDG_ROOT, '特性部署', '业务专题', '5G Core 体验感知解决方案'),
     'QoE体验感知支撑带宽决策'),
    ('UNC', '5G Core FUP解决方案', os.path.join(UNC_ROOT, '网络部署', '业务专题', '5G Core FUP解决方案'),
     'FUP累计流量带宽控制方案（控制面视角）'),
    ('UNC', '5G PCC之SM策略解决方案', os.path.join(UNC_ROOT, '网络部署', '业务专题', '5G PCC之SM策略解决方案'),
     'SM策略E2E实现（含QoS、带宽、FUP）'),
]

# ============================================================
# Part 3: 5G基础知识概念文档（8个目录）
# ============================================================
concepts = [
    ('UDG', 'QoS概念', os.path.join(UDG_ROOT, '5G基础知识', '一望5G', 'QoS')),
    ('UDG', '业务感知（SA）解读', os.path.join(UDG_ROOT, '5G基础知识', '一望5G',
                                                '5G Core业务解决方案解读：业务感知（SA）')),
    ('UDG', 'PCC策略之E2E QoS管理机制', os.path.join(UDG_ROOT, '5G基础知识', '一望5G',
                                                     '5G Core业务解决方案解读：5G PCC策略之E2E QoS管理机制')),
    ('UDG', 'PCC策略之静态规则解读', os.path.join(UDG_ROOT, '5G基础知识', '一望5G',
                                                  '5G Core业务解决方案解读 -5G PCC策略之静态规则解读')),
    ('UNC', 'QoS概念', os.path.join(UNC_ROOT, '5G基础知识', '一望5G', 'QoS')),
    ('UNC', '业务感知（SA）解读', os.path.join(UNC_ROOT, '5G基础知识', '一望5G',
                                                '5G Core业务解决方案解读：业务感知（SA）')),
    ('UNC', 'PCC策略之E2E QoS管理机制', os.path.join(UNC_ROOT, '5G基础知识', '一望5G',
                                                     '5G Core业务解决方案解读：5G PCC策略之E2E QoS管理机制')),
    ('UNC', 'PCC策略之静态规则解读', os.path.join(UNC_ROOT, '5G基础知识', '一望5G',
                                                  '5G Core业务解决方案解读：5G PCC策略之静态规则解读')),
]


# ============================================================
# 构建Markdown
# ============================================================
out = []
out.append('# 带宽控制场景文档清单')
out.append('')
out.append('> 业务感知第二子场景：带宽控制（Bandwidth Control）')
out.append('> 数据来源：UDG + UNC 整个产品文档')
out.append('> 特性：仅定位特性ID（用户后续单独阅读），不展开特性文件清单')
out.append('> 业务专题、概念文档：列出所有md文件，等权重')
out.append('> 排除：MML命令文档、与带宽控制无关的业务专题')
out.append('')

# 总览
out.append('## 总览')
out.append('')
out.append('| 类别 | UDG | UNC | 合计 |')
out.append('|------|-----|-----|------|')
udg_feat = sum(f[3] for f in features if f[2] == 'UDG')
unc_feat = sum(f[3] for f in features if f[2] == 'UNC')
out.append(f'| 特性（24个，仅ID） | {sum(1 for f in features if f[2]=="UDG")}个 / {udg_feat}文件 | {sum(1 for f in features if f[2]=="UNC")}个 / {unc_feat}文件 | {len(features)}个 / {udg_feat+unc_feat}文件 |')

topic_files = []
for product, name, path, desc in topics:
    md_files = collect_md(path)
    topic_files.extend(md_files)
udg_topic = sum(len(collect_md(p[2])) for p in topics if p[0] == 'UDG')
unc_topic = sum(len(collect_md(p[2])) for p in topics if p[0] == 'UNC')
udg_topic_count = sum(1 for p in topics if p[0] == 'UDG')
unc_topic_count = sum(1 for p in topics if p[0] == 'UNC')
out.append(f'| 业务专题（6个，展开文件） | {udg_topic_count}个 / {udg_topic}文件 | {unc_topic_count}个 / {unc_topic}文件 | {len(topics)}个 / {udg_topic+unc_topic}文件 |')

concept_files = []
for product, name, path in concepts:
    md_files = collect_md(path)
    concept_files.extend(md_files)
udg_concept = sum(len(collect_md(p[2])) for p in concepts if p[0] == 'UDG')
unc_concept = sum(len(collect_md(p[2])) for p in concepts if p[0] == 'UNC')
udg_concept_count = sum(1 for p in concepts if p[0] == 'UDG')
unc_concept_count = sum(1 for p in concepts if p[0] == 'UNC')
out.append(f'| 5G基础知识概念（8个目录） | {udg_concept_count}个 / {udg_concept}文件 | {unc_concept_count}个 / {unc_concept}文件 | {len(concepts)}个 / {udg_concept+unc_concept}文件 |')

total_files = (udg_feat + unc_feat) + (udg_topic + unc_topic) + (udg_concept + unc_concept)
out.append(f'| **合计** | - | - | **{total_files} md文件** |')
out.append('')
out.append('---')
out.append('')

# ============================================================
# Section 1: 特性清单（仅ID）
# ============================================================
out.append('## Section 1: 特性清单（仅ID，不展开文件）')
out.append('')
out.append('> 用户后续会单独指定特性阅读。本节仅做ID登记和优先级标注。')
out.append('')

# 优先级分组
out.append('### 1.1 核心特性（必读）')
out.append('')
out.append('| 特性ID | 特性名称 | 产品 | 文件数 | 说明 |')
out.append('|--------|---------|------|--------|------|')
core_ids = {'GWFD-110311', 'WSFD-211005', 'GWFD-020351', 'WSFD-109101', 'GWFD-110101',
            'GWFD-020354', 'GWFD-110313', 'GWFD-020353', 'GWFD-110312', 'WSFD-109104', 'WSFD-211009'}
for fid, fname, prod, fcount, desc in features:
    if fid in core_ids:
        out.append(f'| {fid} | {fname} | {prod} | {fcount} | {desc} |')
out.append('')

out.append('### 1.2 辅助特性（按需阅读）')
out.append('')
out.append('| 特性ID | 特性名称 | 产品 | 文件数 | 说明 |')
out.append('|--------|---------|------|--------|------|')
for fid, fname, prod, fcount, desc in features:
    if fid not in core_ids:
        out.append(f'| {fid} | {fname} | {prod} | {fcount} | {desc} |')
out.append('')
out.append('---')
out.append('')

# ============================================================
# Section 2: 业务专题（展开md文件）
# ============================================================
out.append('## Section 2: 业务专题（展开md文件，等权重）')
out.append('')
batch = 1
for product, name, path, desc in topics:
    md_files = collect_md(path)
    out.append(f'### Batch-{batch:02d}: {name} ({product}, {len(md_files)} files)')
    out.append('')
    out.append(f'> {desc}')
    out.append('')
    out.append('```')
    for md in md_files:
        out.append(md)
    out.append('```')
    out.append('')
    out.append('---')
    out.append('')
    batch += 1

# ============================================================
# Section 3: 5G基础知识概念文档
# ============================================================
out.append('## Section 3: 5G基础知识概念文档（等权重）')
out.append('')
for product, name, path in concepts:
    md_files = collect_md(path)
    out.append(f'### {product} - {name} ({len(md_files)} files)')
    out.append('')
    out.append('```')
    for md in md_files:
        out.append(md)
    out.append('```')
    out.append('')
    out.append('---')
    out.append('')

# ============================================================
# Section 4: 排除说明
# ============================================================
out.append('## Section 4: 排除说明')
out.append('')
out.append('### 4.1 命令文档（不单独读取）')
out.append('')
out.append('- `output/UDG_Product_Documentation_CH_20.15.2/OM参考/命令/UDG MML命令/`')
out.append('- `output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/`')
out.append('- 说明：用户指定命令不单独读取；如需命令细节，从特性文档中提取。')
out.append('')
out.append('### 4.2 与带宽控制无关的业务专题')
out.append('')
out.append('UDG排除的业务专题：')
out.append('- 5G Core 计费解决方案（已纳入计费场景）')
out.append('- 5G Core IPv6组网解决方案（组网相关，非带宽）')
out.append('- 5G Core 国际漫游解决方案（漫游相关，非带宽）')
out.append('- 5G Core 流控解决方案（如有，信令流控非用户面带宽）')
out.append('- 5G Core 媒体中继解决方案（媒体中继，非带宽）')
out.append('- 5G Core 容灾解决方案（容灾相关）')
out.append('- 5G Core 用户IP地址管理解决方案（地址管理）')
out.append('- 5G Core 智家随行解决方案（智家专用）')
out.append('- UDG NAT/UDG SFIP/UDG vTCP_OPT/UDG报表/UDG防欺诈/UDG头增强 功能专题（与带宽无关）')
out.append('')
out.append('UNC排除的业务专题：')
out.append('- 5G Core 4_5G互操作解决方案（互操作）')
out.append('- 5G Core IPv6组网解决方案（组网）')
out.append('- 5G Core NRF解决方案（NRF）')
out.append('- 5G Core ULCL分流解决方案（ULCL，属于第三子场景：访问限制/分流）')
out.append('- 5G Core 计费解决方案（已纳入计费场景）')
out.append('- 5G Core 流控解决方案（信令流控，非用户面带宽）')
out.append('- 5G Core 容灾解决方案（容灾）')
out.append('- 5G Core 用户IP地址管理解决方案（地址管理）')
out.append('- 5GC国际漫游解决方案（漫游）')
out.append('- UNC UPF选择/UNC接入控制/UNC网元选择 专题（接入控制属于第三子场景）')
out.append('')
out.append('### 4.3 边界判断')
out.append('')
out.append('**纳入带宽控制场景**：')
out.append('- 用户面带宽限制/整形（Shaping、Policing、BWM）')
out.append('- 累计流量触发带宽重定向（FUP）')
out.append('- GBR保障（保证比特速率，带宽下限）')
out.append('- 业务触发QoS（专用承载，间接影响带宽）')
out.append('- ADC（应用检测控制，触发带宽策略）')
out.append('- PCC/SA基础框架（带宽控制依赖的底座）')
out.append('')
out.append('**未纳入（属于其他子场景）**：')
out.append('- 访问限制（URL过滤、重定向、阻塞）→ 第三子场景')
out.append('- 接入控制（APN接入、UPF选择）→ 第三子场景')
out.append('- 纯信令流控（NRF/AMF/SMF流控）→ 不属于业务感知')
out.append('')

# ============================================================
# 输出
# ============================================================
output_path = os.path.join(ROOT, 'business-graph', '带宽控制场景', 'bandwidth-doc-list.md')
os.makedirs(os.path.dirname(output_path), exist_ok=True)
with open(output_path, 'w', encoding='utf-8') as f:
    f.write('\n'.join(out))

print(f'Generated: {output_path}')
print(f'Total features: {len(features)} ({udg_feat+unc_feat} files)')
print(f'Total topic files: {len(topic_files)}')
print(f'Total concept files: {len(concept_files)}')
print(f'Grand total: {total_files} md files')
