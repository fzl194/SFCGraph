# -*- coding: utf-8 -*-
"""Step 2: Parse parameter tables from MML command docs.

Reads raw_commands.csv, opens each source file, extracts the parameter table,
and splits the "参数说明" cell into structured sub-fields.

Outputs: command-graph/data/raw_parameters.csv
"""
import csv
import hashlib
import json
import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

BASE = 'D:/mywork/KnowledgeBase/SFCGraph'
DATA_DIR = f'{BASE}/command-graph/data'
INPUT_FILE = f'{DATA_DIR}/raw_commands.csv'
OUTPUT_FILE = f'{DATA_DIR}/raw_parameters.csv'

# Sub-field keys in order of appearance
SUB_FIELD_KEYS = [
    '可选必选说明', '前提条件', '参数含义', '数据来源',
    '取值范围', '默认值', '配置原则',
]


def split_sub_fields(desc_text):
    """Split the concatenated description text into sub-fields.

    Format: 可选必选说明：...参数含义：...取值范围：...默认值：...配置原则：...
    Returns dict with keys from SUB_FIELD_KEYS.
    """
    result = {k: '' for k in SUB_FIELD_KEYS}

    # Find all occurrences of "key：" pattern
    positions = []
    for key in SUB_FIELD_KEYS:
        for m in re.finditer(re.escape(key) + r'[：:]', desc_text):
            positions.append((m.start(), key, m.end()))

    # Sort by position
    positions.sort(key=lambda x: x[0])

    # Extract values between consecutive keys
    for i, (pos, key, val_start) in enumerate(positions):
        if i + 1 < len(positions):
            val_end = positions[i + 1][0]
        else:
            val_end = len(desc_text)
        value = desc_text[val_start:val_end].strip()
        # Only keep the last occurrence for each key
        result[key] = value

    return result


def classify_required_mode(mode_text):
    """Map Chinese required mode to enum value."""
    if not mode_text:
        return 'optional'
    if '必选' in mode_text and '条件' not in mode_text:
        return 'required'
    if '条件必选' in mode_text or '条件可选' in mode_text:
        if '必选' in mode_text:
            return 'conditional_required'
        return 'conditional_optional'
    if '可选' in mode_text:
        return 'optional'
    return 'optional'


def extract_data_type(range_text):
    """Extract data type from value range text."""
    if not range_text:
        return ''
    if '枚举类型' in range_text:
        return 'enum'
    if '整数类型' in range_text:
        return 'integer'
    if '字符串类型' in range_text:
        return 'string'
    if 'IPv4' in range_text or 'IPv6' in range_text:
        return 'ip_address'
    if 'MAC' in range_text:
        return 'mac_address'
    if '布尔' in range_text or 'Boolean' in range_text.lower():
        return 'boolean'
    if '浮点' in range_text:
        return 'float'
    return ''


def extract_enum_values(range_text):
    """Extract enum values from value range text.

    Format: - VALUE：description or - VALUE: description
    """
    if not range_text or '枚举' not in range_text:
        return []

    values = []
    # Match "- VALUE：" or "- VALUE:" patterns
    for m in re.finditer(r'-\s+([A-Z0-9_]+)[：:]', range_text):
        val = m.group(1)
        if val not in values:
            values.append(val)
    return values


def parse_parameter_table(content):
    """Parse the parameter table from markdown content.

    Returns list of dicts with raw parameter fields.
    """
    # Find parameter section markers
    # Look for the table after "参数说明" heading
    param_section = ''
    in_param = False
    lines = content.split('\n')

    for i, line in enumerate(lines):
        if '参数说明' in line and ('####' in line or '###' in line):
            in_param = True
            continue
        if in_param:
            # Stop at next section heading
            if ('####' in line or '###' in line) and '参数说明' not in line:
                break
            param_section += line + '\n'

    if not param_section:
        return []

    # Parse markdown table rows
    # Table format: | 参数标识 | 参数名称 | 参数说明 |
    rows = []
    table_lines = [l for l in param_section.split('\n') if l.strip().startswith('|')]

    if len(table_lines) < 2:
        return []

    # Skip header and separator rows
    for tl in table_lines[2:]:  # Skip header and | --- | line
        cells = [c.strip() for c in tl.split('|')]
        # Remove empty strings from split
        cells = [c for c in cells if c]

        if len(cells) >= 3:
            rows.append({
                'parameter_name': cells[0],
                'parameter_name_zh': cells[1],
                'raw_desc': cells[2],
            })

    return rows


def make_param_id(command_id, param_name):
    """Generate a stable parameter ID."""
    raw = f'{command_id}:{param_name}'
    return hashlib.md5(raw.encode()).hexdigest()[:10]


def process_command(row):
    """Process a single command file and extract parameters."""
    file_path = row['file_path']
    command_id = row['command_id']

    if not os.path.exists(file_path):
        return []

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception:
        return []

    raw_params = parse_parameter_table(content)
    results = []

    for rp in raw_params:
        param_name = rp['parameter_name']
        param_name_zh = rp['parameter_name_zh']
        raw_desc = rp['raw_desc']

        # Clean up HTML line breaks
        raw_desc_clean = raw_desc.replace('<br>', '\n').replace('<br/>', '\n')

        # Split into sub-fields
        sub = split_sub_fields(raw_desc_clean)

        required_mode = classify_required_mode(sub['可选必选说明'])
        data_type = extract_data_type(sub['取值范围'])
        enum_values = extract_enum_values(sub['取值范围'])

        # Extract condition expression from 前提条件
        condition_expr = ''
        if sub['前提条件']:
            # Clean up condition text
            condition_expr = sub['前提条件'].strip()

        param_id = make_param_id(command_id, param_name)

        results.append({
            'parameter_id': param_id,
            'command_id': command_id,
            'parameter_name': param_name,
            'parameter_name_zh': param_name_zh,
            'data_type': data_type,
            'required_mode': required_mode,
            'condition_expression': condition_expr,
            'value_range': sub['取值范围'][:500],  # Truncate long ranges
            'default_value': sub['默认值'],
            'enum_values_json': json.dumps(enum_values, ensure_ascii=False),
            'description': sub['参数含义'][:300],
            'config_principle': sub['配置原则'][:500],
            'reference_target': '',  # Will be filled in step 4
        })

    return results


def main():
    print('=' * 60)
    print('Step 2: Extracting parameters from command docs')
    print('=' * 60)

    # Read commands
    with open(INPUT_FILE, 'r', encoding='utf-8-sig') as f:
        commands = list(csv.DictReader(f))

    print(f'Loaded {len(commands)} commands from raw_commands.csv')

    # Process each command
    all_params = []
    errors = 0
    no_params = 0

    for i, cmd in enumerate(commands):
        params = process_command(cmd)
        if params is None:
            errors += 1
        elif len(params) == 0:
            no_params += 1
        else:
            all_params.extend(params)

        if (i + 1) % 2000 == 0:
            print(f'  Processed {i + 1}/{len(commands)} commands, {len(all_params)} params so far')

    # Write output
    fieldnames = [
        'parameter_id', 'command_id', 'parameter_name', 'parameter_name_zh',
        'data_type', 'required_mode', 'condition_expression', 'value_range',
        'default_value', 'enum_values_json', 'description', 'config_principle',
        'reference_target',
    ]

    with open(OUTPUT_FILE, 'w', encoding='utf-8-sig', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(all_params)

    # Stats
    modes = {}
    dtypes = {}
    for p in all_params:
        modes[p['required_mode']] = modes.get(p['required_mode'], 0) + 1
        dtypes[p['data_type']] = dtypes.get(p['data_type'], 0) + 1

    conditional_count = sum(1 for p in all_params if p['condition_expression'])

    print(f'\n{"=" * 60}')
    print(f'Results')
    print(f'{"=" * 60}')
    print(f'Total parameters: {len(all_params)}')
    print(f'Commands with params: {sum(1 for _ in [])}')
    print(f'Commands without params: {no_params}')
    print(f'Parse errors: {errors}')
    print(f'Conditional params: {conditional_count}')
    print(f'\nRequired mode distribution:')
    for m in sorted(modes, key=modes.get, reverse=True):
        print(f'  {m}: {modes[m]}')
    print(f'\nData type distribution:')
    for d in sorted(dtypes, key=dtypes.get, reverse=True):
        print(f'  {d or "(empty)"}: {dtypes[d]}')

    print(f'\nOutput: {OUTPUT_FILE}')


if __name__ == '__main__':
    main()
