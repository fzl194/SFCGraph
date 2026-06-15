# -*- coding: utf-8 -*-
"""Step 4: Extract parameter dependencies and command ordering constraints.

Intra-command deps: from condition_expression field.
Cross-command deps: parameter values referencing other commands' identifier params.
Command ordering: from notes mentioning execution order.

Outputs:
  - command-graph/data/param_dependencies.csv
  - command-graph/data/cmd_ordering.csv
"""
import csv
import json
import os
import re
import sys
from collections import defaultdict

sys.stdout.reconfigure(encoding='utf-8')

BASE = 'D:/mywork/KnowledgeBase/SFCGraph'
DATA_DIR = f'{BASE}/command-graph/data'
PARAMS_FILE = f'{DATA_DIR}/raw_parameters.csv'
COMMANDS_FILE = f'{DATA_DIR}/raw_commands.csv'
OBJECTS_FILE = f'{DATA_DIR}/config_objects.csv'
DEPS_FILE = f'{DATA_DIR}/param_dependencies.csv'
ORDERING_FILE = f'{DATA_DIR}/cmd_ordering.csv'

# Pattern to extract condition: 该参数在"PARAMNAME"配置为"VALUE"时
CONDITION_PATTERN = re.compile(
    r'[该此]参数在[\""\u201c]([A-Z0-9_]+)[\""\u201d]'
    r'配置为[\""\u201c]([^\""\u201d]+)[\""\u201d]'
)

# Alternative pattern: 当PARAMNAME=VALUE时
CONDITION_PATTERN2 = re.compile(
    r'当\s*([A-Z0-9_]+)\s*[=为]\s*([A-Z0-9_]+)\s*时'
)

# Pattern to find command references in notes
CMD_REF_PATTERN = re.compile(
    r'(ADD|MOD|SET|DEL|RMV)\s+([A-Z][A-Z0-9_]+)'
)


def extract_intra_command_deps(params):
    """Extract dependencies within the same command from condition_expression."""
    deps = []

    for p in params:
        cond = p.get('condition_expression', '')
        if not cond:
            continue

        command_id = p['command_id']
        param_name = p['parameter_name']

        # Try pattern 1: 该参数在"PARAM"配置为"VALUE"时
        matches = CONDITION_PATTERN.findall(cond)
        if matches:
            for source_param, cond_value in matches:
                deps.append({
                    'source_command_id': command_id,
                    'source_param': source_param,
                    'target_command_id': command_id,
                    'target_param': param_name,
                    'condition_value': cond_value,
                    'condition_expression': cond[:200],
                    'dep_type': 'intra_command',
                })
            continue

        # Try pattern 2: 当PARAM=VALUE时
        matches = CONDITION_PATTERN2.findall(cond)
        if matches:
            for source_param, cond_value in matches:
                deps.append({
                    'source_command_id': command_id,
                    'source_param': source_param,
                    'target_command_id': command_id,
                    'target_param': param_name,
                    'condition_value': cond_value,
                    'condition_expression': cond[:200],
                    'dep_type': 'intra_command',
                })
            continue

        # Generic: just record the condition without parsed source
        deps.append({
            'source_command_id': command_id,
            'source_param': '',
            'target_command_id': command_id,
            'target_param': param_name,
            'condition_value': '',
            'condition_expression': cond[:200],
            'dep_type': 'intra_command_unparsed',
        })

    return deps


def extract_cross_command_deps(params, commands):
    """Extract cross-command dependencies from reference_target heuristics.

    When a parameter's name or description references another object's identifier,
    create a cross-command dependency.
    """
    deps = []

    # Build a map: object_keyword -> set of identifier param names
    with open(OBJECTS_FILE, 'r', encoding='utf-8-sig') as f:
        objects = list(csv.DictReader(f))

    obj_ids = {}
    for o in objects:
        try:
            ids = json.loads(o['identifier_parameters_json'])
            obj_ids[o['object_name']] = ids
        except (json.JSONDecodeError, TypeError):
            obj_ids[o['object_name']] = []

    # Build command_id -> (verb, object_keyword, product) map
    cmd_info = {}
    for c in commands:
        cmd_info[c['command_id']] = {
            'verb': c['verb'],
            'object_keyword': c['object_keyword'],
            'product': c['product'],
        }

    # Index params by command_id
    params_by_cmd = defaultdict(list)
    for p in params:
        params_by_cmd[p['command_id']].append(p)

    # For each parameter, check if it references another object's identifier
    for p in params:
        pname = p['parameter_name']
        cmd_id = p['command_id']
        product = cmd_info.get(cmd_id, {}).get('product', '')

        # Check against known object identifiers
        for obj_name, id_params in obj_ids.items():
            for id_param in id_params:
                # If parameter name matches an identifier of a different object
                # (e.g., UPURRNAME1 is not an identifier of URR but references it)
                # Heuristic: if description mentions the object name
                desc = p.get('description', '')
                config_principle = p.get('config_principle', '')
                combined = desc + config_principle

                if obj_name in combined and id_param != pname:
                    # Check if this is actually a reference
                    # The param name might contain the object keyword
                    obj_kw_upper = obj_name.upper()
                    if obj_kw_upper in pname.upper() or obj_kw_upper in combined[:100]:
                        source_cmd_id = cmd_id
                        # Find ADD command for referenced object in same product
                        target_cmd_id = f'{product}:ADD {obj_name}'

                        if target_cmd_id != cmd_id and target_cmd_id in cmd_info:
                            deps.append({
                                'source_command_id': target_cmd_id,
                                'source_param': id_param,
                                'target_command_id': cmd_id,
                                'target_param': pname,
                                'condition_value': '',
                                'condition_expression': f'{pname} references {obj_name}',
                                'dep_type': 'cross_command',
                            })

    return deps


def extract_command_ordering(commands):
    """Extract command ordering constraints from notes."""
    orderings = []

    for cmd in commands:
        notes_text = cmd.get('notes_json', '[]')
        try:
            notes = json.loads(notes_text)
        except (json.JSONDecodeError, TypeError):
            continue

        for note in notes:
            # Look for "必须" + command reference
            if '必须' in note or '需要先' in note or '之后' in note:
                refs = CMD_REF_PATTERN.findall(note)
                for verb, keyword in refs:
                    ref_cmd = f'{cmd["product"]}:{verb} {keyword}'
                    if '必须最后' in note or '最后执行' in note:
                        orderings.append({
                            'command_id': cmd['command_id'],
                            'relates_to_command_id': ref_cmd,
                            'relation': 'must_be_last',
                            'note': note[:200],
                        })
                    elif '必须' in note or '需要先' in note:
                        orderings.append({
                            'command_id': cmd['command_id'],
                            'relates_to_command_id': ref_cmd,
                            'relation': 'must_precede',
                            'note': note[:200],
                        })

    return orderings


def main():
    print('=' * 60)
    print('Step 4: Extracting dependencies and ordering')
    print('=' * 60)

    # Load data
    with open(PARAMS_FILE, 'r', encoding='utf-8-sig') as f:
        params = list(csv.DictReader(f))
    print(f'Loaded {len(params)} parameters')

    with open(COMMANDS_FILE, 'r', encoding='utf-8-sig') as f:
        commands = list(csv.DictReader(f))
    print(f'Loaded {len(commands)} commands')

    # Extract intra-command deps
    print('\nExtracting intra-command dependencies...')
    intra_deps = extract_intra_command_deps(params)
    print(f'  Found: {len(intra_deps)}')

    # Extract cross-command deps
    print('Extracting cross-command dependencies...')
    cross_deps = extract_cross_command_deps(params, commands)
    print(f'  Found: {len(cross_deps)}')

    # Combine all deps
    all_deps = intra_deps + cross_deps

    # Write dependencies
    dep_fields = [
        'source_command_id', 'source_param', 'target_command_id',
        'target_param', 'condition_value', 'condition_expression', 'dep_type',
    ]
    with open(DEPS_FILE, 'w', encoding='utf-8-sig', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=dep_fields)
        writer.writeheader()
        writer.writerows(all_deps)

    # Extract command ordering
    print('Extracting command ordering constraints...')
    orderings = extract_command_ordering(commands)
    print(f'  Found: {len(orderings)}')

    ord_fields = ['command_id', 'relates_to_command_id', 'relation', 'note']
    with open(ORDERING_FILE, 'w', encoding='utf-8-sig', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=ord_fields)
        writer.writeheader()
        writer.writerows(orderings)

    # Stats
    dep_types = {}
    for d in all_deps:
        t = d['dep_type']
        dep_types[t] = dep_types.get(t, 0) + 1

    print(f'\n{"=" * 60}')
    print(f'Results')
    print(f'{"=" * 60}')
    print(f'Total dependencies: {len(all_deps)}')
    for t in sorted(dep_types, key=dep_types.get, reverse=True):
        print(f'  {t}: {dep_types[t]}')
    print(f'\nCommand ordering constraints: {len(orderings)}')

    # Verify key deps for ADD URR
    urr_deps = [d for d in all_deps if d['source_command_id'] == 'UDG:ADD URR'
                and d['dep_type'] == 'intra_command']
    if urr_deps:
        print(f'\nADD URR (UDG) intra-command deps:')
        for d in urr_deps:
            print(f'  {d["source_param"]} --[{d["condition_value"]}]--> {d["target_param"]}')

    print(f'\nOutput: {DEPS_FILE}')
    print(f'Output: {ORDERING_FILE}')


if __name__ == '__main__':
    main()
