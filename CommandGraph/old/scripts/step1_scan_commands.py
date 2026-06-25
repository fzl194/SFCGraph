# -*- coding: utf-8 -*-
"""Step 1: Scan all MML commands.

UDG: from kgdata CSV (华为 Hedex 结构化数据)
UNC: from MD filenames (无 kgdata)

Outputs: command-graph/data/raw_commands.csv
"""
import csv
import json
import os
import re
import sys
from pathlib import Path
from collections import defaultdict
from urllib.parse import unquote

sys.stdout.reconfigure(encoding='utf-8')

BASE = 'D:/mywork/KnowledgeBase/SFCGraph'
KGDATA_DIR = f'{BASE}/command-graph/data/kgdata'
OUTPUT_DIR = f'{BASE}/command-graph/data'
OUTPUT_UDG = f'{OUTPUT_DIR}/udg_commands.csv'
OUTPUT_UNC = f'{OUTPUT_DIR}/unc_commands.csv'

# UDG MD files root (for file_path binding)
UDG_MD_ROOT = f'{BASE}/output/UDG_Product_Documentation_CH_20.15.2/OM参考/命令/UDG MML命令'
UNC_MD_ROOT = f'{BASE}/output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令'

VERSION = '20.15.2'

# MD filename regex
FILENAME_PATTERN = re.compile(r'^(.+?)[（(]\s*([A-Z]+)\s+([A-Z0-9_]+)\s*[）)]')
FILENAME_PATTERN_SINGLE = re.compile(r'^(.+?)[（(]\s*([A-Z]{2,})\s*[）)]')


def build_md_path_index(md_root):
    """Build topic_id -> MD file_path mapping from MD filenames.

    MD filename contains a numeric ID: 增加URR（ADD URR）_82837629.md
    kgdata topic_id: CONCEPT_0182837629 → last digits 82837629
    """
    index = {}
    output_base = f'{BASE}/output/'
    for root, dirs, files in os.walk(md_root):
        for f in files:
            if not f.endswith('.md'):
                continue
            # Extract numeric ID from filename: _12345678.md
            m = re.search(r'_(\d+)\.md$', f)
            if m:
                num_id = m.group(1)
                full_path = os.path.join(root, f).replace('\\', '/')
                rel_path = full_path
                if rel_path.startswith(output_base):
                    rel_path = rel_path[len(output_base):]
                index[num_id] = rel_path
    return index


def strip_html(html_text):
    """Strip HTML tags and normalize whitespace."""
    if not html_text:
        return ''
    text = unquote(html_text).replace('+', ' ')
    text = re.sub(r'<[^>]+>', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text


def load_udg_commands():
    """Load UDG commands from kgdata CSV."""
    # Build MD path index
    md_index = build_md_path_index(UDG_MD_ROOT)
    print(f'  MD path index: {len(md_index)} files')

    # Load kgdata
    commands = {}  # Name -> {attr: value}
    for i in [1, 2]:
        path = f'{KGDATA_DIR}/UDG_MML命令_{i}.csv'
        with open(path, 'r', encoding='utf-8') as f:
            for row in csv.DictReader(f):
                name = row['Name']
                attr = row['Attribute Name']
                val = row['Attribute Value']
                if name not in commands:
                    commands[name] = {}
                commands[name][attr] = val

    # Pre-build suffix lookup: for each md_id length, group md_ids
    # Then for each topic_id, try matching by checking if any md_id is a suffix
    md_by_len = defaultdict(list)
    for md_id, md_path in md_index.items():
        md_by_len[len(md_id)].append((md_id, md_path))

    results = []
    for name, attrs in commands.items():
        # Extract fields from kgdata
        cmd_code = unquote(attrs.get('命令码', '')).replace('+', ' ')
        cmd_name_zh = unquote(attrs.get('命令名称', ''))
        topic_id = attrs.get('_topic_id', '')

        if not cmd_code:
            continue

        # Bind MD file path via topic_id numeric suffix matching
        file_path = ''
        category_path = []
        if topic_id:
            topic_digits = re.sub(r'[^0-9]', '', topic_id)
            topic_len = len(topic_digits)
            # Try md_ids of various lengths as suffix of topic_digits
            for md_id_len, md_entries in md_by_len.items():
                if md_id_len > topic_len:
                    continue
                suffix = topic_digits[topic_len - md_id_len:]
                for md_id, md_path in md_entries:
                    if md_id == suffix:
                        file_path = md_path
                        md_prefix = 'UDG_Product_Documentation_CH_20.15.2/OM参考/命令/UDG MML命令/'
                        if file_path.startswith(md_prefix):
                            rest = file_path[len(md_prefix):]
                            category_path = [p for p in Path(rest).parent.parts if p]
                        break
                if file_path:
                    break

        # kgdata provides these fields directly
        command_function = strip_html(attrs.get('命令功能', ''))
        notes = strip_html(attrs.get('注意事项', ''))
        examples = strip_html(attrs.get('使用实例', ''))
        permission = strip_html(attrs.get('操作用户权限', ''))

        results.append({
            'product': 'UDG',
            'version': VERSION,
            'command_name': cmd_code,
            'command_name_zh': cmd_name_zh,
            'category_path': json.dumps(category_path, ensure_ascii=False),
            'file_path': file_path,
            'topic_id': topic_id,
            'command_function': command_function,
            'notes': notes,
            'permission': permission,
            'examples': examples,
        })

    return results


def load_unc_commands():
    """Load UNC commands from MD filenames."""
    output_base = f'{BASE}/output/'
    results = []

    for root, dirs, files in os.walk(UNC_MD_ROOT):
        for f in files:
            if not f.endswith('.md') or '命令申明' in f or '声明' in f:
                continue

            stem = os.path.splitext(f)[0]
            m = FILENAME_PATTERN.match(stem)
            single_word = False
            if not m:
                m = FILENAME_PATTERN_SINGLE.match(stem)
                if m:
                    single_word = True
                else:
                    continue

            cmd_name_zh = m.group(1).strip()
            if single_word:
                cmd_code = m.group(2).upper()
            else:
                verb = m.group(2).upper()
                keyword = m.group(3).upper()
                cmd_code = f'{verb} {keyword}'

            # Relative file path
            full_path = os.path.join(root, f).replace('\\', '/')
            rel_path = full_path
            if rel_path.startswith(output_base):
                rel_path = rel_path[len(output_base):]

            # Category path from directory structure
            rel_to_root = os.path.relpath(full_path, UNC_MD_ROOT)
            category_path = [p for p in Path(rel_to_root).parent.parts if p]

            results.append({
                'product': 'UNC',
                'version': VERSION,
                'command_name': cmd_code,
                'command_name_zh': cmd_name_zh,
                'category_path': json.dumps(category_path, ensure_ascii=False),
                'file_path': rel_path,
                'topic_id': '',
                'command_function': '',
                'notes': '',
                'permission': '',
                'examples': '',
            })

    return results


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    print('=' * 60)
    print('Step 1: Loading MML commands')
    print('=' * 60)

    print('\nLoading UDG from kgdata...')
    udg = load_udg_commands()
    print(f'  UDG: {len(udg)} commands')

    print('Loading UNC from MD filenames...')
    unc = load_unc_commands()
    print(f'  UNC: {len(unc)} commands')

    # Write separate CSVs
    fieldnames = [
        'product', 'version', 'command_name', 'command_name_zh',
        'category_path', 'file_path', 'topic_id',
        'command_function', 'notes', 'permission', 'examples',
    ]

    with open(OUTPUT_UDG, 'w', encoding='utf-8-sig', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(udg)

    with open(OUTPUT_UNC, 'w', encoding='utf-8-sig', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(unc)

    # Stats
    udg_with_func = sum(1 for r in udg if r['command_function'])
    udg_with_md = sum(1 for r in udg if r['file_path'])

    print(f'\n{"=" * 60}')
    print(f'Results')
    print(f'{"=" * 60}')
    print(f'UDG: {len(udg)} (with function: {udg_with_func}, with MD: {udg_with_md})')
    print(f'UNC: {len(unc)}')
    print(f'\nOutput: {OUTPUT_UDG}')
    print(f'Output: {OUTPUT_UNC}')


if __name__ == '__main__':
    main()
