# -*- coding: utf-8 -*-
"""Step 5: Extract command rules from notes and parameter descriptions.

Rule types: uniqueness, cardinality, delete_constraint, performance, effect_scope, etc.

Output: command-graph/data/command_rules.csv
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
COMMANDS_FILE = f'{DATA_DIR}/raw_commands.csv'
PARAMS_FILE = f'{DATA_DIR}/raw_parameters.csv'
RULES_FILE = f'{DATA_DIR}/command_rules.csv'

# Rule extraction patterns
UNIQUENESS_PATTERNS = [
    re.compile(r'[唯]一'),
    re.compile(r'不允许.*重复'),
    re.compile(r'不能.*相同'),
]

CARDINALITY_PATTERNS = [
    re.compile(r'最大记录数[为](\d+)'),
    re.compile(r'最多[可]?[配置]?(\d+)'),
    re.compile(r'不超过(\d+)'),
]

DELETE_CONSTRAINT_PATTERNS = [
    re.compile(r'不允许.*删除'),
    re.compile(r'禁止.*删除'),
    re.compile(r'不能.*删除'),
]

PERFORMANCE_PATTERNS = [
    re.compile(r'对性能.*影响'),
    re.compile(r'影响.*性能'),
    re.compile(r'性能.*下降'),
]

EFFECT_SCOPE_PATTERNS = [
    re.compile(r'不.*立即生效'),
    re.compile(r'只对.*生效'),
    re.compile(r'对新.*生效'),
]

CROSS_NF_PATTERNS = [
    re.compile(r'[与和].*[Ss][Mm][Ff].*一致'),
    re.compile(r'[与和].*[Uu][Pp][Ff].*一致'),
    re.compile(r'需要.*一致'),
]


def classify_rule(note, context_type='command'):
    """Classify a note into rule types based on pattern matching."""
    rules = []

    # Uniqueness
    if any(p.search(note) for p in UNIQUENESS_PATTERNS):
        rules.append('uniqueness')

    # Cardinality
    m = None
    for p in CARDINALITY_PATTERNS:
        m = p.search(note)
        if m:
            break
    if m:
        rules.append('cardinality')

    # Delete constraint
    if any(p.search(note) for p in DELETE_CONSTRAINT_PATTERNS):
        rules.append('delete_constraint')

    # Performance
    if any(p.search(note) for p in PERFORMANCE_PATTERNS):
        rules.append('performance')

    # Effect scope
    if any(p.search(note) for p in EFFECT_SCOPE_PATTERNS):
        rules.append('effect_scope')

    # Cross-NF sync
    if any(p.search(note) for p in CROSS_NF_PATTERNS):
        rules.append('cross_nf_sync')

    return rules if rules else ['general']


def determine_severity(rule_type, note):
    """Determine rule severity."""
    critical_types = {'uniqueness', 'delete_constraint', 'cross_nf_sync'}
    if rule_type in critical_types:
        return 'critical'
    if rule_type == 'cardinality':
        return 'warning'
    if rule_type == 'performance':
        return 'warning'
    if rule_type == 'effect_scope':
        return 'info'
    return 'info'


def main():
    print('=' * 60)
    print('Step 5: Extracting command rules')
    print('=' * 60)

    # Load data
    with open(COMMANDS_FILE, 'r', encoding='utf-8-sig') as f:
        commands = list(csv.DictReader(f))
    with open(PARAMS_FILE, 'r', encoding='utf-8-sig') as f:
        params = list(csv.DictReader(f))

    print(f'Loaded {len(commands)} commands, {len(params)} parameters')

    all_rules = []
    rule_counter = 0

    # Extract rules from command notes
    for cmd in commands:
        notes_text = cmd.get('notes_json', '[]')
        try:
            notes = json.loads(notes_text)
        except (json.JSONDecodeError, TypeError):
            continue

        for note in notes:
            if not note or len(note) < 5:
                continue

            rule_types = classify_rule(note, 'command')
            for rt in rule_types:
                rule_counter += 1
                severity = determine_severity(rt, note)

                all_rules.append({
                    'rule_id': f'CR-{rule_counter:04d}',
                    'rule_name': note[:50] + ('...' if len(note) > 50 else ''),
                    'rule_type': rt,
                    'scope_type': 'command',
                    'scope_ref': cmd['command_id'],
                    'rule_logic': note[:500],
                    'violation_effect': '',
                    'severity': severity,
                    'source': 'command_notes',
                })

    # Extract rules from parameter config_principle
    for p in params:
        principle = p.get('config_principle', '')
        if not principle or len(principle) < 10:
            continue

        rule_types = classify_rule(principle, 'parameter')
        if rule_types == ['general']:
            continue  # Skip generic principles

        for rt in rule_types:
            rule_counter += 1
            severity = determine_severity(rt, principle)

            all_rules.append({
                'rule_id': f'CR-{rule_counter:04d}',
                'rule_name': f'{p["parameter_name"]}: {principle[:40]}...',
                'rule_type': rt,
                'scope_type': 'parameter',
                'scope_ref': f'{p["command_id"]}:{p["parameter_name"]}',
                'rule_logic': principle[:500],
                'violation_effect': '',
                'severity': severity,
                'source': 'parameter_principle',
            })

    # Write output
    fields = [
        'rule_id', 'rule_name', 'rule_type', 'scope_type', 'scope_ref',
        'rule_logic', 'violation_effect', 'severity', 'source',
    ]
    with open(RULES_FILE, 'w', encoding='utf-8-sig', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(all_rules)

    # Stats
    type_counts = {}
    scope_counts = {}
    severity_counts = {}
    source_counts = {}
    for r in all_rules:
        type_counts[r['rule_type']] = type_counts.get(r['rule_type'], 0) + 1
        scope_counts[r['scope_type']] = scope_counts.get(r['scope_type'], 0) + 1
        severity_counts[r['severity']] = severity_counts.get(r['severity'], 0) + 1
        source_counts[r['source']] = source_counts.get(r['source'], 0) + 1

    print(f'\n{"=" * 60}')
    print(f'Results')
    print(f'{"=" * 60}')
    print(f'Total rules: {len(all_rules)}')
    print(f'\nRule type distribution:')
    for t in sorted(type_counts, key=type_counts.get, reverse=True):
        print(f'  {t}: {type_counts[t]}')
    print(f'\nSeverity distribution:')
    for s in sorted(severity_counts, key=severity_counts.get, reverse=True):
        print(f'  {s}: {severity_counts[s]}')
    print(f'\nScope distribution:')
    for s in sorted(scope_counts, key=scope_counts.get, reverse=True):
        print(f'  {s}: {scope_counts[s]}')
    print(f'\nSource distribution:')
    for s in sorted(source_counts, key=source_counts.get, reverse=True):
        print(f'  {s}: {source_counts[s]}')

    # Verify charging scenario rules
    urr_rules = [r for r in all_rules if 'ADD URR' in r['scope_ref']
                 and r['source'] == 'command_notes']
    if urr_rules:
        print(f'\nADD URR rules:')
        for r in urr_rules:
            print(f'  [{r["severity"]}] {r["rule_type"]}: {r["rule_name"][:80]}')

    print(f'\nOutput: {RULES_FILE}')


if __name__ == '__main__':
    main()
