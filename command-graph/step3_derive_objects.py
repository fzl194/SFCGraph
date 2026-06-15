# -*- coding: utf-8 -*-
"""Step 3: Derive ConfigObjects from commands and parameters.

Groups commands by object_keyword, derives object properties from ADD commands,
and infers command→object relationship types from verbs.

Outputs:
  - command-graph/data/config_objects.csv
  - command-graph/data/cmd_object_relations.csv
"""
import csv
import json
import os
import sys
from collections import defaultdict

sys.stdout.reconfigure(encoding='utf-8')

BASE = 'D:/mywork/KnowledgeBase/SFCGraph'
DATA_DIR = f'{BASE}/command-graph/data'
COMMANDS_FILE = f'{DATA_DIR}/raw_commands.csv'
PARAMS_FILE = f'{DATA_DIR}/raw_parameters.csv'
OBJECTS_FILE = f'{DATA_DIR}/config_objects.csv'
RELATIONS_FILE = f'{DATA_DIR}/cmd_object_relations.csv'

# Verb → relation type mapping
VERB_RELATION_MAP = {
    'ADD': 'creates',
    'MOD': 'modifies',
    'SET': 'sets',
    'DEL': 'deletes',
    'RMV': 'deletes',
    'LST': 'operates_on',
    'DSP': 'operates_on',
    # Less common verbs default to 'operates_on'
}


def get_relation_type(verb):
    """Map verb to ConfigObject relation type."""
    return VERB_RELATION_MAP.get(verb, 'operates_on')


def infer_object_kind(object_name, commands_for_object):
    """Infer object_kind from the command set and object name heuristics."""
    name_upper = object_name.upper()

    # Heuristic patterns
    if name_upper.endswith('GROUP') or name_upper.endswith('GRP'):
        return 'group'
    if 'BINDING' in name_upper or 'BIND' in name_upper:
        return 'binding'
    if name_upper.startswith('SET ') or 'GLOBAL' in name_upper or 'GLB' in name_upper:
        return 'global_setting'
    if name_upper.endswith('PROP') or name_upper.endswith('PROFILE'):
        return 'profile'
    if name_upper == 'REFRESHSRV' or 'REFRESH' in name_upper:
        return 'action'
    if 'FILTER' in name_upper and 'GRP' not in name_upper:
        return 'filter'
    # Default
    return 'entity'


def main():
    print('=' * 60)
    print('Step 3: Deriving ConfigObjects from commands')
    print('=' * 60)

    # Load commands
    with open(COMMANDS_FILE, 'r', encoding='utf-8-sig') as f:
        commands = list(csv.DictReader(f))
    print(f'Loaded {len(commands)} commands')

    # Load parameters
    with open(PARAMS_FILE, 'r', encoding='utf-8-sig') as f:
        params = list(csv.DictReader(f))
    print(f'Loaded {len(params)} parameters')

    # Index params by command_id
    params_by_cmd = defaultdict(list)
    for p in params:
        params_by_cmd[p['command_id']].append(p)

    # Group commands by object_keyword (case-insensitive)
    # Also track which products have each object
    obj_cmds = defaultdict(list)  # object_keyword -> [command rows]
    for cmd in commands:
        obj_cmds[cmd['object_keyword']].append(cmd)

    # Derive config objects
    objects = []
    relations = []

    for obj_name, cmds in sorted(obj_cmds.items()):
        # Collect products
        products = set(c['product'] for c in cmds)

        # Find the ADD command (primary source for attributes)
        add_cmds = [c for c in cmds if c['verb'] == 'ADD']
        if not add_cmds:
            # Fall back to MOD or first command
            add_cmds = [c for c in cmds if c['verb'] == 'MOD']
        if not add_cmds:
            add_cmds = [cmds[0]]

        primary_cmd = add_cmds[0]

        # Get parameters from primary command
        obj_params = params_by_cmd.get(primary_cmd['command_id'], [])

        # Identifier parameters = required params
        identifier_params = [
            p['parameter_name'] for p in obj_params
            if p['required_mode'] == 'required'
        ]

        # Build attributes list from all params
        attributes = []
        for p in obj_params:
            attributes.append({
                'parameter_name': p['parameter_name'],
                'data_type': p['data_type'],
                'required_mode': p['required_mode'],
                'default_value': p['default_value'],
                'condition': p['condition_expression'],
            })

        # Infer object_kind
        object_kind = infer_object_kind(obj_name, cmds)

        # Get description from primary command summary
        description = primary_cmd.get('command_summary', '')

        # Applicable NF: merge from all commands
        all_nf = set()
        for c in cmds:
            try:
                nf_list = json.loads(c.get('applicable_nf', '[]'))
                all_nf.update(nf_list)
            except (json.JSONDecodeError, TypeError):
                pass

        # Collect category paths
        all_categories = set()
        for c in cmds:
            try:
                cats = json.loads(c.get('category_path', '[]'))
                if cats:
                    all_categories.add(tuple(cats))
            except (json.JSONDecodeError, TypeError):
                pass

        # Use the most specific (longest) category path
        category = list(max(all_categories, key=len)) if all_categories else []

        object_id = obj_name  # Use object_keyword as ID (unique across products)

        objects.append({
            'object_id': object_id,
            'object_name': obj_name,
            'object_kind': object_kind,
            'identifier_parameters_json': json.dumps(
                identifier_params, ensure_ascii=False
            ),
            'attributes_count': len(attributes),
            'attributes_json': json.dumps(attributes, ensure_ascii=False),
            'applicable_nf_json': json.dumps(sorted(all_nf), ensure_ascii=False),
            'applicable_products_json': json.dumps(sorted(products), ensure_ascii=False),
            'category_path_json': json.dumps(category, ensure_ascii=False),
            'description': description[:500],
            'commands_count': len(cmds),
        })

        # Generate command→object relations
        for cmd in cmds:
            rel_type = get_relation_type(cmd['verb'])
            relations.append({
                'command_id': cmd['command_id'],
                'object_name': obj_name,
                'relation_type': rel_type,
            })

    # Write config objects
    obj_fields = [
        'object_id', 'object_name', 'object_kind', 'identifier_parameters_json',
        'attributes_count', 'attributes_json', 'applicable_nf_json',
        'applicable_products_json', 'category_path_json', 'description',
        'commands_count',
    ]
    with open(OBJECTS_FILE, 'w', encoding='utf-8-sig', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=obj_fields)
        writer.writeheader()
        writer.writerows(objects)

    # Write command→object relations
    rel_fields = ['command_id', 'object_name', 'relation_type']
    with open(RELATIONS_FILE, 'w', encoding='utf-8-sig', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=rel_fields)
        writer.writeheader()
        writer.writerows(relations)

    # Stats
    kinds = {}
    for o in objects:
        k = o['object_kind']
        kinds[k] = kinds.get(k, 0) + 1

    rel_types = {}
    for r in relations:
        t = r['relation_type']
        rel_types[t] = rel_types.get(t, 0) + 1

    products_count = defaultdict(int)
    for o in objects:
        prods = json.loads(o['applicable_products_json'])
        if len(prods) > 1:
            products_count['both'] += 1
        else:
            products_count[prods[0]] += 1

    print(f'\n{"=" * 60}')
    print(f'Results')
    print(f'{"=" * 60}')
    print(f'Config objects: {len(objects)}')
    print(f'Command→Object relations: {len(relations)}')
    print(f'\nObject kind distribution:')
    for k in sorted(kinds, key=kinds.get, reverse=True):
        print(f'  {k}: {kinds[k]}')
    print(f'\nRelation type distribution:')
    for t in sorted(rel_types, key=rel_types.get, reverse=True):
        print(f'  {t}: {rel_types[t]}')
    print(f'\nProduct distribution:')
    for p in sorted(products_count):
        print(f'  {p}: {products_count[p]}')

    # Verify key objects
    print(f'\nKey config objects (charging scenario):')
    for name in ['URR', 'URRGROUP', 'PCCPOLICYGRP', 'RULE', 'FLOWFILTER', 'USERPROFILE']:
        obj = [o for o in objects if o['object_name'] == name]
        if obj:
            o = obj[0]
            ids = json.loads(o['identifier_parameters_json'])
            prods = json.loads(o['applicable_products_json'])
            print(f'  {name}: kind={o["object_kind"]}, ids={ids}, attrs={o["attributes_count"]}, products={prods}')

    print(f'\nOutput: {OBJECTS_FILE}')
    print(f'Output: {RELATIONS_FILE}')


if __name__ == '__main__':
    main()
