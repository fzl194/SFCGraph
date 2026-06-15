# -*- coding: utf-8 -*-
"""Step 1b: Extract command_function, notes, permission, examples from MD files.

For UDG: extract from MD and compare with existing kgdata values.
For UNC: extract from MD (no kgdata to compare).

Output:
  - data/md_extracted_fields.csv  (both UDG + UNC)
  - data/udg_comparison.csv       (UDG only: kgdata vs MD comparison)
  - data/extraction_comparison_report.md
"""
import csv
import json
import os
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

BASE = 'D:/mywork/KnowledgeBase/SFCGraph'
DATA_DIR = f'{BASE}/command-graph/data'
DOC_ROOT = f'{BASE}/output'

# Section patterns: match ## or #### heading with section name
# Handles: ## [命令功能](anchor) or #### [命令功能](anchor) or ## 命令功能 or #### 命令功能
SECTION_NAMES = ['命令功能', '注意事项', '操作用户权限', '使用实例']
# All known section names (including ones we don't extract, used as boundaries)
ALL_SECTION_NAMES = ['命令功能', '注意事项', '操作用户权限', '参数说明', '使用实例',
                     '输出结果说明', '参考信息', '依赖关系', '命令间约束']

# Pattern to match a section heading (## or ####) followed by optional [name](anchor) or plain text
HEADING_PATTERN = re.compile(
    r'^(#{2,4})\s+\[?(' + '|'.join(re.escape(s) for s in SECTION_NAMES) + r')\]?'
    r'(?:\([^)]*\))?\s*$',
    re.MULTILINE
)

# Boundary pattern: any known section name at any heading level (2-4)
BOUNDARY_PATTERN = re.compile(
    r'^(#{2,4})\s+\[?(' + '|'.join(re.escape(s) for s in ALL_SECTION_NAMES) + r')\]?'
    r'(?:\([^)]*\))?\s*$',
    re.MULTILINE
)


def extract_sections(md_text: str) -> dict[str, str]:
    """Extract named sections from MD text.

    Returns dict: {section_name: content_text}
    """
    # Find all target section headings
    target_matches = list(HEADING_PATTERN.finditer(md_text))
    if not target_matches:
        return {}

    # Find ALL boundary headings (including sections we don't extract)
    boundary_matches = list(BOUNDARY_PATTERN.finditer(md_text))

    result = {}
    for m in target_matches:
        section_name = m.group(2)
        start = m.end()

        # Find the next boundary heading after this one
        end = len(md_text)
        for bm in boundary_matches:
            if bm.start() > m.end():
                end = bm.start()
                break

        content = md_text[start:end].strip()

        # Clean: remove anchor links, normalize whitespace
        content = re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', content)
        # Remove markdown bold markers but keep text
        content = re.sub(r'\*\*([^*]+)\*\*', r'\1', content)
        # Strip leading/trailing blank lines
        content = content.strip()

        result[section_name] = content

    return result


def normalize_for_comparison(text: str) -> str:
    """Normalize text for comparison: collapse whitespace, strip punctuation differences."""
    if not text:
        return ''
    # Collapse all whitespace to single space
    text = re.sub(r'\s+', ' ', text).strip()
    # Remove markdown artifacts
    text = text.replace('**', '').replace('`', '')
    # Normalize quotes
    text = text.replace('"', '"').replace('"', '"').replace(''', "'").replace(''', "'")
    return text


def load_existing_csv(path: str) -> dict[str, dict]:
    """Load existing CSV into dict keyed by product:command_name."""
    result = {}
    with open(path, 'r', encoding='utf-8-sig') as f:
        for row in csv.DictReader(f):
            key = f"{row['product']}:{row['command_name']}"
            result[key] = row
    return result


def extract_all():
    """Main extraction logic."""
    print('=' * 60)
    print('Step 1b: Extract fields from MD files')
    print('=' * 60)

    # Load existing data
    udg_existing = load_existing_csv(f'{DATA_DIR}/udg_commands.csv')
    unc_existing = load_existing_csv(f'{DATA_DIR}/unc_commands.csv')
    all_existing = {**udg_existing, **unc_existing}

    print(f'  Loaded UDG: {len(udg_existing)} commands')
    print(f'  Loaded UNC: {len(unc_existing)} commands')

    # Extract from MD
    results = {}  # key -> {field: md_value}
    no_file = 0
    parse_ok = 0
    parse_fail = 0

    for key, cmd in all_existing.items():
        file_path = cmd.get('file_path', '')
        if not file_path:
            no_file += 1
            continue

        full_path = os.path.join(DOC_ROOT, file_path)
        if not os.path.exists(full_path):
            no_file += 1
            continue

        try:
            md_text = open(full_path, 'r', encoding='utf-8').read()
            sections = extract_sections(md_text)

            results[key] = {
                'md_command_function': sections.get('命令功能', ''),
                'md_notes': sections.get('注意事项', ''),
                'md_permission': sections.get('操作用户权限', ''),
                'md_examples': sections.get('使用实例', ''),
            }

            if sections:
                parse_ok += 1
            else:
                parse_fail += 1
        except Exception as e:
            parse_fail += 1
            results[key] = {
                'md_command_function': '',
                'md_notes': '',
                'md_permission': '',
                'md_examples': f'ERROR: {e}',
            }

    print(f'\n  MD extraction: {parse_ok} ok, {parse_fail} fail, {no_file} no file')

    # --- UDG Comparison ---
    print('\n' + '=' * 60)
    print('UDG Comparison: kgdata vs MD extraction')
    print('=' * 60)

    comparison_rows = []
    field_stats = {}

    for field, kgdata_key in [
        ('command_function', 'md_command_function'),
        ('notes', 'md_notes'),
        ('permission', 'md_permission'),
        ('examples', 'md_examples'),
    ]:
        stats = {'total': 0, 'kgdata_empty': 0, 'md_empty': 0, 'both_empty': 0,
                 'exact_match': 0, 'similar': 0, 'different': 0}

        for key, cmd in udg_existing.items():
            kgdata_val = normalize_for_comparison(cmd.get(field, ''))
            md_val = normalize_for_comparison(results.get(key, {}).get(kgdata_key, ''))

            stats['total'] += 1
            kg_empty = not kgdata_val
            md_empty = not md_val

            if kg_empty:
                stats['kgdata_empty'] += 1
            if md_empty:
                stats['md_empty'] += 1
            if kg_empty and md_empty:
                stats['both_empty'] += 1
                continue

            # Compare
            if kgdata_val == md_val:
                stats['exact_match'] += 1
                sim = 'exact'
            elif kgdata_val in md_val or md_val in kgdata_val:
                stats['similar'] += 1
                sim = 'contains'
            else:
                # Check character-level similarity
                from difflib import SequenceMatcher
                ratio = SequenceMatcher(None, kgdata_val, md_val).ratio()
                if ratio > 0.8:
                    stats['similar'] += 1
                    sim = f'similar({ratio:.2f})'
                else:
                    stats['different'] += 1
                    sim = f'diff({ratio:.2f})'

            comparison_rows.append({
                'key': key,
                'field': field,
                'similarity': sim,
                'kgdata_len': len(kgdata_val),
                'md_len': len(md_val),
                'kgdata_preview': kgdata_val[:200],
                'md_preview': md_val[:200],
            })

        field_stats[field] = stats
        print(f'\n  {field}:')
        print(f'    total={stats["total"]}, kgdata_empty={stats["kgdata_empty"]}, md_empty={stats["md_empty"]}')
        print(f'    exact_match={stats["exact_match"]}, similar={stats["similar"]}, different={stats["different"]}')

    # --- Write comparison CSV ---
    comp_path = f'{DATA_DIR}/udg_comparison.csv'
    with open(comp_path, 'w', encoding='utf-8-sig', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['key', 'field', 'similarity', 'kgdata_len', 'md_len', 'kgdata_preview', 'md_preview'])
        writer.writeheader()
        writer.writerows(comparison_rows)
    print(f'\n  Comparison CSV: {comp_path}')

    # --- Write report ---
    report_path = f'{DATA_DIR}/extraction_comparison_report.md'
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write('# Step 1b: MD 提取 vs kgdata 对比报告\n\n')

        f.write('## 总览\n\n')
        f.write(f'- UDG 命令数: {len(udg_existing)}\n')
        f.write(f'- UNC 命令数: {len(unc_existing)}\n')
        f.write(f'- MD 解析成功: {parse_ok}\n')
        f.write(f'- MD 解析失败: {parse_fail}\n')
        f.write(f'- 无文件: {no_file}\n\n')

        f.write('## UDG 字段对比（kgdata vs MD）\n\n')
        for field, stats in field_stats.items():
            total_non_empty = stats['total'] - stats['both_empty']
            match_rate = (stats['exact_match'] + stats['similar']) / total_non_empty * 100 if total_non_empty > 0 else 0
            f.write(f'### {field}\n\n')
            f.write(f'| 指标 | 值 |\n|---|---|\n')
            f.write(f'| 总数 | {stats["total"]} |\n')
            f.write(f'| kgdata为空 | {stats["kgdata_empty"]} |\n')
            f.write(f'| MD为空 | {stats["md_empty"]} |\n')
            f.write(f'| 两者都为空 | {stats["both_empty"]} |\n')
            f.write(f'| 完全匹配 | {stats["exact_match"]} |\n')
            f.write(f'| 相似(>80%) | {stats["similar"]} |\n')
            f.write(f'| 差异较大(<80%) | {stats["different"]} |\n')
            f.write(f'| **匹配率** | **{match_rate:.1f}%** |\n\n')

            # Show some diff examples
            diffs = [r for r in comparison_rows if r['field'] == field and 'diff' in r['similarity']]
            if diffs:
                f.write(f'差异样例 ({len(diffs)} 条):\n\n')
                for d in diffs[:5]:
                    f.write(f'- **{d["key"]}** ({d["similarity"]})\n')
                    f.write(f'  - kgdata({d["kgdata_len"]}): {d["kgdata_preview"][:100]}\n')
                    f.write(f'  - md({d["md_len"]}): {d["md_preview"][:100]}\n\n')

        f.write('## UNC 提取统计\n\n')
        unc_extracted = {k: v for k, v in results.items() if k.startswith('UNC:')}
        unc_has_func = sum(1 for v in unc_extracted.values() if v['md_command_function'])
        unc_has_notes = sum(1 for v in unc_extracted.values() if v['md_notes'])
        unc_has_perm = sum(1 for v in unc_extracted.values() if v['md_permission'])
        unc_has_examples = sum(1 for v in unc_extracted.values() if v['md_examples'])
        f.write(f'| 字段 | 有值数 | 总数 | 覆盖率 |\n|---|---|---|---|\n')
        f.write(f'| command_function | {unc_has_func} | {len(unc_existing)} | {unc_has_func/len(unc_existing)*100:.1f}% |\n')
        f.write(f'| notes | {unc_has_notes} | {len(unc_existing)} | {unc_has_notes/len(unc_existing)*100:.1f}% |\n')
        f.write(f'| permission | {unc_has_perm} | {len(unc_existing)} | {unc_has_perm/len(unc_existing)*100:.1f}% |\n')
        f.write(f'| examples | {unc_has_examples} | {len(unc_existing)} | {unc_has_examples/len(unc_existing)*100:.1f}% |\n\n')

    print(f'  Report: {report_path}')

    # --- Write md_extracted_fields.csv ---
    ext_path = f'{DATA_DIR}/md_extracted_fields.csv'
    with open(ext_path, 'w', encoding='utf-8-sig', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['key', 'product', 'command_name',
                                                'md_command_function', 'md_notes',
                                                'md_permission', 'md_examples'])
        writer.writeheader()
        for key, cmd in {**udg_existing, **unc_existing}.items():
            product = cmd['product']
            command_name = cmd['command_name']
            md_fields = results.get(key, {})
            writer.writerow({
                'key': key,
                'product': product,
                'command_name': command_name,
                'md_command_function': md_fields.get('md_command_function', ''),
                'md_notes': md_fields.get('md_notes', ''),
                'md_permission': md_fields.get('md_permission', ''),
                'md_examples': md_fields.get('md_examples', ''),
            })
    print(f'  Extracted fields: {ext_path}')


if __name__ == '__main__':
    extract_all()
