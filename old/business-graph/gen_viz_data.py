import csv, json, os
from collections import Counter

data_dir = os.path.join(os.path.dirname(__file__), 'data')

def read_csv(path):
    rows = []
    with open(path, encoding='utf-8-sig') as f:
        for r in csv.DictReader(f):
            rows.append(r)
    return rows

nodes = {}
edges = []

def add_node(nid, label, group, title=''):
    nodes[nid] = {'label': label, 'group': group, 'title': title}

def add_edge(src, tgt, rel, group):
    if src in nodes and tgt in nodes:
        edges.append({'from': src, 'to': tgt, 'relation': rel, 'group': group})

# 01-business-entities
for r in read_csv(f'{data_dir}/01-business-entities/business_domains.csv'):
    add_node(r['domain_id'], r['domain_name'], 'BusinessDomain', r.get('domain_summary',''))

for r in read_csv(f'{data_dir}/01-business-entities/network_scenarios.csv'):
    add_node(r['scenario_id'], r['scenario_name'], 'NetworkScenario', r.get('scenario_summary',''))

for r in read_csv(f'{data_dir}/01-business-entities/reference_patterns.csv'):
    add_node(r['pattern_id'], r['pattern_name'], 'ReferencePattern', r.get('pattern_summary',''))

for r in read_csv(f'{data_dir}/01-business-entities/delivery_solutions.csv'):
    add_node(r['solution_id'], r['solution_name'], 'DeliverySolution', r.get('summary',''))

for r in read_csv(f'{data_dir}/01-business-entities/engineering_tasks.csv'):
    add_node(r['task_id'], r['task_name'], 'EngineeringTask', r.get('task_summary',''))

# 03-semantic-entities
for r in read_csv(f'{data_dir}/03-semantic-entities/domain_semantic_objects.csv'):
    add_node(r['semantic_object_id'], r['semantic_object_name'], 'DomainSemanticObject', r.get('definition_boundary',''))

# 05-feature-entities
for r in read_csv(f'{data_dir}/05-feature-entities/capabilities.csv'):
    add_node(r['capability_id'], r['capability_name'], 'Capability', r.get('capability_summary',''))

for r in read_csv(f'{data_dir}/05-feature-entities/features.csv'):
    add_node(r['feature_code'], r['feature_name'], 'Feature', r.get('feature_summary',''))

# 07-command-entities
for r in read_csv(f'{data_dir}/07-command-entities/config_objects.csv'):
    add_node(r['config_object_id'], r['config_object_name'], 'ConfigObject', r.get('summary',''))

# 09-runtime-validation-risk
for r in read_csv(f'{data_dir}/09-runtime-validation-risk/runtime_flows.csv'):
    add_node(r['runtime_flow_id'], r['runtime_flow_name'], 'RuntimeFlow', r.get('summary',''))

for r in read_csv(f'{data_dir}/09-runtime-validation-risk/validation_plans.csv'):
    add_node(r['validation_plan_id'], r['validation_plan_name'], 'ValidationPlan', r.get('summary',''))

for r in read_csv(f'{data_dir}/09-runtime-validation-risk/diagnosis_rules.csv'):
    add_node(r['diagnosis_rule_id'], r['diagnosis_rule_name'], 'DiagnosisRule', r.get('summary',''))

for r in read_csv(f'{data_dir}/09-runtime-validation-risk/risk_constraints.csv'):
    add_node(r['risk_constraint_id'], r['risk_constraint_name'], 'RiskConstraint', r.get('summary',''))

# 10-evidence
for r in read_csv(f'{data_dir}/10-evidence/evidence.csv'):
    add_node(r['evidence_id'], r['title'][:45], 'Evidence', r.get('evidence_summary',''))

# Edges
# 02-business-relations
for r in read_csv(f'{data_dir}/02-business-relations/business_domain_scenario_mapping.csv'):
    add_edge(r['domain_id'], r['scenario_id'], r['relation_type'], 'contains')

for r in read_csv(f'{data_dir}/02-business-relations/scenario_pattern_mapping.csv'):
    add_edge(r['scenario_id'], r['pattern_id'], r['relation_type'], 'has_pattern')

for r in read_csv(f'{data_dir}/02-business-relations/scenario_solution_mapping.csv'):
    add_edge(r['scenario_id'], r['solution_id'], r['relation_type'], 'instantiated_as')

for r in read_csv(f'{data_dir}/02-business-relations/delivery_solution_task_mapping.csv'):
    add_edge(r['solution_id'], r['task_id'], r['relation_type'], 'decomposes_to')

# 04-semantic-bridges
for r in read_csv(f'{data_dir}/04-semantic-bridges/scenario_semantic_mapping.csv'):
    add_edge(r['scenario_id'], r['semantic_object_id'], r['relation_type'], 'uses_semantic_object')

for r in read_csv(f'{data_dir}/04-semantic-bridges/delivery_solution_semantic_mapping.csv'):
    add_edge(r['solution_id'], r['semantic_object_id'], r['relation_type'], 'instantiates_semantic_object')

for r in read_csv(f'{data_dir}/04-semantic-bridges/semantic_capability_mapping.csv'):
    add_edge(r['semantic_object_id'], r['capability_id'], r['relation_type'], 'semantic_requires_capability')

for r in read_csv(f'{data_dir}/04-semantic-bridges/semantic_config_mapping.csv'):
    add_edge(r['semantic_object_id'], r['config_object_id'], r['relation_type'], 'semantic_realized_by_config')

for r in read_csv(f'{data_dir}/04-semantic-bridges/semantic_evidence_mapping.csv'):
    eid = r.get('evidence_id', '')
    if eid:
        add_edge(r['semantic_object_id'], eid, r.get('relation_type', 'semantic_verified_by'), 'semantic_verified_by')

# 06-feature-relations
for r in read_csv(f'{data_dir}/06-feature-relations/feature_capability_mapping.csv'):
    add_edge(r['capability_id'], r['feature_code'], r['relation_type'], 'implemented_by_feature')

# 08-cross-layer-relations
for r in read_csv(f'{data_dir}/08-cross-layer-relations/delivery_solution_capability_mapping.csv'):
    add_edge(r['solution_id'], r['capability_id'], r['relation_type'], 'requires_capability')

for r in read_csv(f'{data_dir}/08-cross-layer-relations/engineering_task_config_mapping.csv'):
    add_edge(r['task_id'], r['config_object_id'], r['relation_type'], 'realized_by_config')

# 09-runtime-validation-risk
for r in read_csv(f'{data_dir}/09-runtime-validation-risk/delivery_solution_runtime_mapping.csv'):
    add_edge(r['solution_id'], r['runtime_flow_id'], r['relation_type'], 'has_runtime_flow')

for r in read_csv(f'{data_dir}/09-runtime-validation-risk/delivery_solution_validation_mapping.csv'):
    add_edge(r['solution_id'], r['validation_plan_id'], r['relation_type'], 'validated_by')

for r in read_csv(f'{data_dir}/09-runtime-validation-risk/delivery_solution_diagnosis_mapping.csv'):
    add_edge(r['solution_id'], r['diagnosis_rule_id'], r['relation_type'], 'diagnosed_by')

for r in read_csv(f'{data_dir}/09-runtime-validation-risk/delivery_solution_risk_mapping.csv'):
    add_edge(r['solution_id'], r['risk_constraint_id'], r['relation_type'], 'constrained_by')

# 10-evidence support
for r in read_csv(f'{data_dir}/10-evidence/evidence_support_mapping.csv'):
    tgt = r['target_id']
    if tgt in nodes:
        add_edge(r['evidence_id'], tgt, r['relation_type'], 'supported_by')

# Stats
nc = Counter(v['group'] for v in nodes.values())
ec = Counter(e['group'] for e in edges)
print(f'Nodes: {len(nodes)}, Edges: {len(edges)}')
print(f'Node groups: {dict(nc)}')
print(f'Edge groups: {dict(ec)}')

out = {'nodes': [{'id': k, **v} for k, v in nodes.items()], 'edges': edges}
with open(os.path.join(os.path.dirname(__file__), 'viz_data.json'), 'w', encoding='utf-8') as f:
    json.dump(out, f, ensure_ascii=False)
print('Written viz_data.json')
