#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
解析bandwidth-doc-list.md中Section 2+3的所有md路径，
按相关性智能分组为~10个文件/batch。
策略：按(产品,专题)分组 → 路径排序（同目录自然聚类）→ 按10个一组切分 → 合并小尾巴
"""
import os
import re
import sys
from collections import defaultdict

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

ROOT = r'D:\mywork\KnowledgeBase\SFCGraph'
DOC_LIST = os.path.join(ROOT, 'business-graph', '带宽控制场景', 'bandwidth-doc-list.md')

with open(DOC_LIST, encoding='utf-8') as f:
    content = f.read()

paths = re.findall(r'^(output/.*\.md)\s*$', content, re.MULTILINE)
print(f'Total md paths: {len(paths)}')


def get_topic_key(path):
    """提取(产品, 专题)作为大分组key"""
    product = 'UDG' if 'UDG_Product_Documentation' in path else 'UNC'
    parts = path.split('/')

    if '业务专题' in parts:
        idx = parts.index('业务专题')
        if idx + 1 < len(parts):
            return (product, parts[idx + 1])
    elif '5G基础知识' in parts:
        return (product, '5G基础知识')
    return (product, '其他')


# 第一步：按(产品,专题)分组
topic_groups = defaultdict(list)
for p in paths:
    key = get_topic_key(p)
    topic_groups[key].append(p)

print(f'\n=== 按(产品,专题)分组: {len(topic_groups)} 个专题 ===')
for key in sorted(topic_groups.keys()):
    print(f'  {key[0]}|{key[1]}: {len(topic_groups[key])} files')

# 第二步：每个专题内，路径排序后按10个一组切分
# 路径排序的妙处：同目录的文件自然聚类
raw_batches = []
for key in sorted(topic_groups.keys()):
    files = sorted(topic_groups[key])  # 路径排序
    product, topic = key

    # 按10个一组切分
    for i in range(0, len(files), 10):
        chunk = files[i:i+10]
        part_num = i // 10 + 1
        total_parts = (len(files) + 9) // 10
        if total_parts == 1:
            batch_name = f'{product}|{topic}'
        else:
            batch_name = f'{product}|{topic}|part{part_num}'
        raw_batches.append((batch_name, chunk))

print(f'\n=== 切分后: {len(raw_batches)} 个batch ===')

# 第三步：合并小尾巴batch（<6个文件的）
# 合并策略：同(产品,专题)的相邻小batch合并；不同专题但同产品的小batch合并
final_batches = []
i = 0
while i < len(raw_batches):
    name, files = raw_batches[i]

    if len(files) >= 8:
        # 大batch，直接保留
        final_batches.append((name, files))
        i += 1
    else:
        # 小batch，尝试合并后续相邻的小batch
        merged = list(files)
        merged_names = [name]
        j = i + 1
        while j < len(raw_batches) and len(merged) < 10:
            next_name, next_files = raw_batches[j]
            # 只合并同产品的
            if next_name.split('|')[0] == name.split('|')[0]:
                if len(merged) + len(next_files) <= 16:
                    merged.extend(next_files)
                    merged_names.append(next_name)
                    j += 1
                else:
                    break
            else:
                break

        # 生成合并后的名称
        if len(merged_names) == 1:
            final_batches.append((merged_names[0], merged))
        else:
            # 取共同前缀
            product = merged_names[0].split('|')[0]
            # 找共同的专题
            topics = set()
            for n in merged_names:
                parts = n.split('|')
                topics.add(parts[1])
            if len(topics) == 1:
                topic_name = list(topics)[0]
                final_batches.append((f'{product}|{topic_name}|合并', merged))
            else:
                final_batches.append((f'{product}|{"+".join(sorted(topics))}|合并', merged))
        i = j

# 打印结果
print(f'\n=== 最终batch数: {len(final_batches)} ===')
total_files = 0
for i, (name, files) in enumerate(final_batches, 1):
    total_files += len(files)
    marker = '⚠️' if len(files) < 5 or len(files) > 14 else '✓'
    print(f'  Batch-{i:02d}: {name} ({len(files)} files) {marker}')
print(f'总文件数: {total_files}')

sizes = [len(f) for _, f in final_batches]
print(f'\nBatch大小: min={min(sizes)}, max={max(sizes)}, avg={sum(sizes)/len(sizes):.1f}')
print(f'5-14文件的batch: {sum(1 for s in sizes if 5 <= s <= 14)}/{len(sizes)}')

# 生成topic-batch-plan.md
out = []
out.append('# 带宽控制场景 - 业务专题+概念文档 Batch计划')
out.append('')
out.append(f'> 数据来源：bandwidth-doc-list.md Section 2(业务专题) + Section 3(5G基础知识概念)')
out.append(f'> 分组策略：按(产品,专题)分组 → 路径排序（同目录聚类）→ 按~10个文件/batch切分')
out.append(f'> 共 {len(final_batches)} 个batch，{total_files} 个md文件')
out.append('')

out.append('## 总览')
out.append('')
out.append('| Batch | 分组主题 | 产品 | 文件数 |')
out.append('|-------|---------|------|--------|')
for i, (name, files) in enumerate(final_batches, 1):
    parts = name.split('|')
    product = parts[0]
    topic_display = ' / '.join(parts[1:])
    out.append(f'| Batch-{i:02d} | {topic_display} | {product} | {len(files)} |')
out.append(f'| | **合计** | | **{total_files}** |')
out.append('')
out.append('---')
out.append('')

for i, (name, files) in enumerate(final_batches, 1):
    parts = name.split('|')
    product = parts[0]
    topic_display = ' / '.join(parts[1:])
    out.append(f'## Batch-{i:02d}: {topic_display} ({product}, {len(files)} files)')
    out.append('')
    out.append('```')
    for f in sorted(files):
        out.append(f)
    out.append('```')
    out.append('')
    out.append('---')
    out.append('')

output_path = os.path.join(ROOT, 'business-graph', '带宽控制场景', 'topic-batch-plan.md')
with open(output_path, 'w', encoding='utf-8') as f:
    f.write('\n'.join(out))

print(f'\nGenerated: {output_path}')
