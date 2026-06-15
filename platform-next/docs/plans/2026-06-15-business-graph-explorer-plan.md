# 业务图谱探索器 Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** 将业务图谱前端从"MD 章节平铺"重构为"级联卡片树 + 对象详情面板"，基于关系边层层递进展示 BD→NS→CS→Feature→Task→Command 完整链路。

**Architecture:** 后端新增 `graph_parser.py` 从 7 个 MD 文件中提取对象库 + 边集合，通过 `/graph` API 返回完整图。前端新增 CascadeTree（级联卡片）+ ObjectDetail（详情面板）组件，客户端构建树并渲染。

**Tech Stack:** FastAPI + Python（后端），Vue3 + TypeScript + Element Plus（前端）

**Design Doc:** `docs/plans/2026-06-15-business-graph-explorer-design.md`

---

## Phase 1: 后端图解析器

### Task 1: 创建 graph_parser.py 骨架 + KV 表对象提取

**Files:**
- Create: `platform-next/business_graph/graph_parser.py`

**Step 1: 创建 graph_parser.py，实现 KV 表对象提取**

KV 表对象包括 BD、NS、CS、Feature、Task。它们的共同模式：`### x.x ID Name` 或 `#### ID Name` 标题后紧跟 `| 字段 | 值 |` 表。

```python
# -*- coding: utf-8 -*-
"""Deep graph parser: extracts objects + edges from 7 layer MD files."""
import re
from pathlib import Path
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class GraphObject:
    object_id: str
    object_type: str  # BusinessDomain, NetworkScenario, ConfigurationSolution, Feature, ConfigTask, ...
    name: str
    summary: str
    layer: str  # business, feature, task, command, mapping, evidence
    attributes: dict = field(default_factory=dict)


@dataclass
class GraphEdge:
    from_id: str
    relation: str  # contains, instantiated_as, uses_feature, decomposes_to, invokes, ...
    to_id: str
    meta: dict = field(default_factory=dict)


@dataclass
class ScenarioGraph:
    objects: dict[str, GraphObject] = field(default_factory=dict)
    edges: list[GraphEdge] = field(default_factory=list)
    root_id: str = ""

    def to_dict(self) -> dict:
        return {
            "objects": {
                oid: {
                    "object_id": obj.object_id,
                    "object_type": obj.object_type,
                    "name": obj.name,
                    "summary": obj.summary,
                    "layer": obj.layer,
                    "attributes": obj.attributes,
                }
                for oid, obj in self.objects.items()
            },
            "edges": [
                {"from": e.from_id, "relation": e.relation, "to": e.to_id, "meta": e.meta}
                for e in self.edges
            ],
            "root_id": self.root_id,
        }


# --- KV-table object extraction ---

# Pattern: ### x.x ID Name or #### ID Name (Feature/Task level headings)
_KV_HEADING_RE = re.compile(
    r'^#{3,4}\s+(?:\d+\.\d+\s+)?([A-Z]{2,5}[-_]?\w*|GWFD-\d+|WSFD-\d+|T-\d+)\s+(.+?)$',
    re.MULTILINE
)

# KV table row: | `field_name` | value |
_KV_ROW_RE = re.compile(r'^\|\s*`?([^|]+?)`?\s*\|\s*([^|]+?)\s*\|\s*$')


def _extract_id_from_heading(heading_text: str) -> tuple[str, str]:
    """Extract object ID and name from heading text like 'CS-CH-01 离线计费方案'."""
    parts = heading_text.strip().split(None, 1)
    obj_id = parts[0].strip()
    obj_name = parts[1].strip() if len(parts) > 1 else obj_id
    return obj_id, obj_name


def _parse_kv_table(text: str) -> dict:
    """Parse a | 字段 | 值 | table into a dict."""
    attrs = {}
    for line in text.split('\n'):
        m = _KV_ROW_RE.match(line)
        if not m:
            continue
        key = m.group(1).strip().strip('`').strip()
        val = m.group(2).strip().strip('`').strip()
        if key and key != '字段' and key != '---':
            attrs[key] = val
    return attrs


def _detect_object_type(obj_id: str, layer: str) -> str:
    """Detect object type from ID pattern and layer."""
    if obj_id.startswith('BD-'):
        return 'BusinessDomain'
    if obj_id.startswith('NS-'):
        return 'NetworkScenario'
    if obj_id.startswith('CS-'):
        return 'ConfigurationSolution'
    if obj_id.startswith('DP-'):
        return 'DecisionPoint'
    if obj_id.startswith('BR-'):
        return 'BusinessRule'
    if obj_id.startswith('SO-'):
        return 'SemanticObject'
    if obj_id.startswith('GWFD-') or obj_id.startswith('WSFD-'):
        return 'Feature'
    if re.match(r'^T-\d+', obj_id):
        return 'ConfigTask'
    if obj_id.startswith('CMD-'):
        return 'MMLCommand'
    if obj_id.startswith('EV-'):
        return 'EvidenceSource'
    if obj_id.startswith('LKV'):
        return 'License'
    return 'Unknown'


def _extract_name_field(attrs: dict, fallback: str) -> str:
    """Get the best name from common attribute keys."""
    for key in ('domain_name', 'scenario_name', 'solution_name', 'feature_name',
                'task_name', 'command_name', 'semantic_object_name',
                'rule_name', 'decision_name', 'license_name'):
        if key in attrs:
            return attrs[key]
    return fallback


def _extract_summary_field(attrs: dict) -> str:
    """Get the best summary from common attribute keys."""
    for key in ('domain_summary', 'scenario_summary', 'solution_summary', 'feature_summary',
                'task_summary', 'command_summary', 'semantic_summary', 'rule_logic',
                'decision_question'):
        if key in attrs:
            return attrs[key]
    return ""


def parse_kv_objects(md_text: str, layer: str) -> list[GraphObject]:
    """Extract KV-table objects from a layer MD file.

    Scans for ### or #### headings that look like object IDs,
    then parses the immediately following KV table.
    """
    objects = []
    # Find all headings that could be object definitions
    for m in re.finditer(r'^(#{3,4})\s+(.+)$', md_text, re.MULTILINE):
        heading_text = m.group(2).strip()

        # Skip section headers that aren't objects (e.g., "1.1 基础感知")
        # Must start with an ID-like pattern
        id_match = re.match(
            r'^((?:BD|NS|CS|DP|BR|SO|EV|CMD|LKV)[-\w]*|GWFD-\d+|WSFD-\d+|T-\d+)\s+(.+)$',
            heading_text
        )
        if not id_match:
            continue

        obj_id = id_match.group(1).strip()
        fallback_name = id_match.group(2).strip()

        # Get text until next heading of same or higher level
        heading_level = len(m.group(1))
        start = m.end()
        next_heading = re.search(
            rf'^#{{1,{heading_level}}}\s+',
            md_text[start:],
            re.MULTILINE
        )
        end = start + next_heading.start() if next_heading else len(md_text)
        section_text = md_text[start:end]

        attrs = _parse_kv_table(section_text)
        if not attrs:
            continue

        obj_type = _detect_object_type(obj_id, layer)
        name = _extract_name_field(attrs, fallback_name)
        summary = _extract_summary_field(attrs)

        objects.append(GraphObject(
            object_id=obj_id,
            object_type=obj_type,
            name=name,
            summary=summary,
            layer=layer,
            attributes=attrs,
        ))

    return objects
```

**Step 2: 验证 KV 对象提取**

```bash
cd D:/mywork/KnowledgeBase/SFCGraph/platform-next
python -c "
from business_graph.graph_parser import parse_kv_objects
from pathlib import Path

# Test with business layer
md = Path('../business-graph/计费场景/three-layer-graph/01-business-graph.md').read_text(encoding='utf-8')
objs = parse_kv_objects(md, 'business')
for o in objs:
    print(f'{o.object_type:25s} {o.object_id:15s} {o.name}')
print(f'Total: {len(objs)}')
"
```

Expected: 应看到 BD-CH-01、NS-CH-01、CS-CH-01~07 共 9 个对象。

**Step 3: Commit**

```bash
git add platform-next/business_graph/graph_parser.py
git commit -m "feat: add graph_parser.py with KV-table object extraction"
```

---

### Task 2: 宽表对象提取（DP/BR/SO/License/Command）

**Files:**
- Modify: `platform-next/business_graph/graph_parser.py`

**Step 1: 添加宽表解析函数**

宽表模式：`## N. TypeName（N个）` 标题后跟一个多列表格，每行是一个对象。

```python
# Add to graph_parser.py

# --- Wide-table object extraction ---

# Map section keywords to object types
_WIDE_TABLE_TYPES = {
    'BusinessDomain': 'BusinessDomain',
    'NetworkScenario': 'NetworkScenario',
    'ConfigurationSolution': 'ConfigurationSolution',
    'DecisionPoint': 'DecisionPoint',
    'BusinessRule': 'BusinessRule',
    'SemanticObject': 'SemanticObject',
    'Feature': 'Feature',
    'SubFeature': 'SubFeature',
    'License': 'License',
    'FeatureRule': 'FeatureRule',
    'ConfigTask': 'ConfigTask',
    'TaskRule': 'TaskRule',
    'MMLCommand': 'MMLCommand',
    'CommandParameter': 'CommandParameter',
    'ConfigObject': 'ConfigObject',
    'CommandRule': 'CommandRule',
    'EvidenceSource': 'EvidenceSource',
}


def _detect_wide_table_type(heading_text: str) -> Optional[str]:
    """Detect if a ## heading introduces a wide-table object collection."""
    for keyword, obj_type in _WIDE_TABLE_TYPES.items():
        if keyword in heading_text:
            return obj_type
    return None


def _parse_wide_table(text: str, obj_type: str, layer: str) -> list[GraphObject]:
    """Parse a wide table where each row is an object, columns are attributes."""
    objects = []
    lines = text.split('\n')

    # Find the first table header
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if line.startswith('|') and not line.startswith('|:'):
            # Check if next line is separator
            if i + 1 < len(lines) and re.match(r'^\|[\s:|-]+\|$', lines[i + 1].strip()):
                break
        i += 1

    if i >= len(lines):
        return objects

    # Parse headers
    headers = [h.strip().strip('`').strip() for h in lines[i].strip().strip('|').split('|')]
    i += 2  # skip header + separator

    # Parse rows
    while i < len(lines):
        line = lines[i].strip()
        if not line.startswith('|'):
            break
        cells = [c.strip().strip('`').strip() for c in line.strip('|').split('|')]
        # Pad to header length
        while len(cells) < len(headers):
            cells.append('')

        attrs = {headers[j]: cells[j] for j in range(len(headers)) if headers[j]}

        # Determine object ID from first column or common ID fields
        obj_id = ''
        for key in ('domain_id', 'scenario_id', 'solution_id', 'decision_id',
                     'rule_id', 'semantic_object_id', 'feature_id', 'subfeature_id',
                     'license_id', 'task_id', 'command_id', 'parameter_id',
                     'object_id', 'evidence_id'):
            if key in attrs and attrs[key]:
                obj_id = attrs[key]
                break

        if not obj_id:
            obj_id = cells[0] if cells else ''

        if not obj_id:
            i += 1
            continue

        name = _extract_name_field(attrs, obj_id)
        summary = _extract_summary_field(attrs)

        objects.append(GraphObject(
            object_id=obj_id,
            object_type=obj_type,
            name=name,
            summary=summary,
            layer=layer,
            attributes=attrs,
        ))
        i += 1

    return objects


def parse_wide_table_objects(md_text: str, layer: str) -> list[GraphObject]:
    """Extract wide-table object collections from a layer MD file."""
    objects = []
    for m in re.finditer(r'^##\s+(.+)$', md_text, re.MULTILINE):
        heading_text = m.group(1).strip()
        obj_type = _detect_wide_table_type(heading_text)
        if not obj_type:
            continue

        # Get section text until next ## heading
        start = m.end()
        next_h2 = re.search(r'^##\s+', md_text[start:], re.MULTILINE)
        end = start + next_h2.start() if next_h2 else len(md_text)
        section_text = md_text[start:end]

        objects.extend(_parse_wide_table(section_text, obj_type, layer))

    return objects
```

**Step 2: 验证宽表对象提取**

```bash
cd D:/mywork/KnowledgeBase/SFCGraph/platform-next
python -c "
from business_graph.graph_parser import parse_wide_table_objects
from pathlib import Path

md = Path('../business-graph/计费场景/three-layer-graph/01-business-graph.md').read_text(encoding='utf-8')
objs = parse_wide_table_objects(md, 'business')
types = {}
for o in objs:
    types.setdefault(o.object_type, []).append(o)
for t, os in types.items():
    print(f'{t}: {len(os)}')
    for o in os[:3]:
        print(f'  {o.object_id} {o.name}')
print(f'Total wide-table objects: {len(objs)}')
"
```

Expected: DP(8)、BR(16)、SO(12)。

**Step 3: Commit**

```bash
git add platform-next/business_graph/graph_parser.py
git commit -m "feat: add wide-table object extraction to graph_parser"
```

---

### Task 3: 边提取（内联标记 + 跨层映射边表）

**Files:**
- Modify: `platform-next/business_graph/graph_parser.py`

**Step 1: 添加内联标记边提取**

CS 对象的 KV 表后面有内联关系标记，如 `**uses_feature**: GWFD-010171、GWFD-020301`。

```python
# Add to graph_parser.py

# --- Edge extraction ---

# Inline relationship markers: **relation_type**: value1、value2、value3
_INLINE_RELATION_RE = re.compile(
    r'\*\*(\w+)\*\*[：:]\s*(.+?)(?=\n\n|\n\*\*|\n####|\n###|\n##|\Z)',
    re.DOTALL
)

# Main-chain relation types (for tree building)
MAIN_CHAIN_RELATIONS = {
    'contains', 'instantiated_as', 'uses_feature', 'uses_task',
    'decomposes_to', 'invokes', 'operates_on', 'has_parameter',
}


def parse_inline_edges(md_text: str, owner_layer: str = "") -> list[GraphEdge]:
    """Extract edges from inline **relation**: value markers.

    These appear in CS object definitions, Feature definitions, etc.
    The owner context is determined from the surrounding heading.
    """
    edges = []

    # Split by ### headings to get owner context
    sections = re.split(r'^(#{3,4}\s+.+)$', md_text, flags=re.MULTILINE)

    current_owner = ""
    for i, section in enumerate(sections):
        if re.match(r'^#{3,4}\s+', section):
            # Extract owner ID from heading
            m = re.match(r'^#{3,4}\s+(?:\d+\.\d+\s+)?((?:BD|NS|CS|DP|BR|SO|GWFD|WSFD|T-)[-\w]*)', section)
            if m:
                current_owner = m.group(1)
            continue

        if not current_owner:
            continue

        # Find inline relationship markers in this section
        for m in _INLINE_RELATION_RE.finditer(section):
            relation = m.group(1).strip()
            value_text = m.group(2).strip()

            # Split by 、 or , and clean each target
            targets = re.split(r'[、,;；]', value_text)
            for target in targets:
                target = target.strip().strip('`').strip()
                # Clean up role annotations like "GWFD-010171 离线UDG"
                # Keep the ID part
                target_match = re.match(
                    r'^((?:BD|NS|CS|DP|BR|SO|GWFD|WSFD|T-|CMD-|EV-|LKV)[-\w]*)',
                    target
                )
                if target_match:
                    clean_target = target_match.group(1)
                    # Extract role from remaining text
                    role_text = target[len(clean_target):].strip()
                    role_text = re.sub(r'^[（(【\[].*?[）)】\]]', '', role_text).strip()
                    meta = {}
                    if role_text:
                        meta['context'] = role_text[:100]
                    edges.append(GraphEdge(
                        from_id=current_owner,
                        relation=relation,
                        to_id=clean_target,
                        meta=meta,
                    ))

    return edges


def parse_edge_table(md_text: str) -> list[GraphEdge]:
    """Extract edges from explicit edge tables (起点 | 关系 | 终点).

    Used in 01-business-graph.md §8 and 05-cross-layer-mapping.md §1-§4.
    """
    edges = []
    lines = md_text.split('\n')

    i = 0
    while i < len(lines):
        line = lines[i].strip()

        # Look for tables with edge-like headers
        if line.startswith('|') and i + 1 < len(lines):
            headers_raw = line.strip('|').split('|')
            headers = [h.strip().strip('`').strip() for h in headers_raw]

            # Check if this looks like an edge table
            # Headers might be: 起点|关系|终点, CS|uses_feature|Feature, from|relation|to, etc.
            from_col = _find_edge_column(headers, ['起点', 'from', 'CS', 'ConfigTask', 'Feature', 'DP'])
            rel_col = _find_edge_column(headers, ['关系', 'relation', 'uses_feature', 'uses_task',
                                                    'decomposes_to', 'invokes', 'targets',
                                                    'selects', 'sets_value_pattern', 'constrained_by',
                                                    'has_decision', 'uses_semantic_object'])
            to_col = _find_edge_column(headers, ['终点', 'to', 'Feature', 'ConfigTask', 'MMLCommand',
                                                  '目标', 'SemanticObject', 'ConfigObject'])

            if from_col is not None and to_col is not None and from_col != to_col:
                # Skip separator row
                if i + 1 < len(lines) and re.match(r'^\|[\s:|-]+\|$', lines[i + 1].strip()):
                    i += 2
                    relation_fallback = headers[rel_col] if rel_col is not None and rel_col < len(headers) else ''

                    while i < len(lines):
                        row_line = lines[i].strip()
                        if not row_line.startswith('|'):
                            break
                        cells = row_line.strip('|').split('|')
                        cells = [c.strip().strip('`').strip() for c in cells]

                        if from_col >= len(cells) or to_col >= len(cells):
                            i += 1
                            continue

                        from_val = cells[from_col]

                        # Relation: from rel_col or from cell
                        if rel_col is not None and rel_col < len(cells):
                            rel_val = cells[rel_col] or relation_fallback
                        else:
                            rel_val = relation_fallback

                        to_val = cells[to_col]

                        # Extract IDs from cell text (may contain descriptions)
                        from_match = re.search(
                            r'((?:BD|NS|CS|DP|BR|SO|GWFD|WSFD|T-|CMD-|EV-|LKV)[-\w]*)',
                            from_val
                        )
                        # to_val may contain multiple targets separated by 、or ,
                        to_targets = re.findall(
                            r'((?:BD|NS|CS|DP|BR|SO|GWFD|WSFD|T-|CMD-|EV-|LKV)[-\w]*)',
                            to_val
                        )

                        if from_match and to_targets:
                            from_id = from_match.group(1)
                            for to_id in to_targets:
                                edges.append(GraphEdge(
                                    from_id=from_id,
                                    relation=rel_val,
                                    to_id=to_id,
                                ))
                        i += 1
                    continue
        i += 1

    return edges


def _find_edge_column(headers: list[str], keywords: list[str]) -> Optional[int]:
    """Find column index matching any keyword."""
    for idx, h in enumerate(headers):
        for kw in keywords:
            if kw.lower() in h.lower():
                return idx
    return None


def dedup_edges(edges: list[GraphEdge]) -> list[GraphEdge]:
    """Remove duplicate edges (same from+relation+to)."""
    seen = set()
    result = []
    for e in edges:
        key = (e.from_id, e.relation, e.to_id)
        if key not in seen:
            seen.add(key)
            result.append(e)
    return result
```

**Step 2: 验证边提取**

```bash
cd D:/mywork/KnowledgeBase/SFCGraph/platform-next
python -c "
from business_graph.graph_parser import parse_inline_edges, parse_edge_table, dedup_edges
from pathlib import Path

# Inline edges from business layer
md1 = Path('../business-graph/计费场景/three-layer-graph/01-business-graph.md').read_text(encoding='utf-8')
inline_edges = parse_inline_edges(md1)

# Table edges from cross-layer mapping
md5 = Path('../business-graph/计费场景/three-layer-graph/05-cross-layer-mapping.md').read_text(encoding='utf-8')
table_edges = parse_edge_table(md5)

all_edges = dedup_edges(inline_edges + table_edges)

# Count by relation type
from collections import Counter
rels = Counter(e.relation for e in all_edges)
for r, c in rels.most_common():
    print(f'{r:30s} {c}')
print(f'Total edges: {len(all_edges)}')
"
```

Expected: 看到 uses_feature(~20)、uses_task(7)、decomposes_to(~14)、invokes(~30)、contains、instantiated_as 等关系类型。

**Step 3: Commit**

```bash
git add platform-next/business_graph/graph_parser.py
git commit -m "feat: add edge extraction (inline markers + cross-layer tables) to graph_parser"
```

---

### Task 4: 整合 parse_scenario_graph + API endpoint

**Files:**
- Modify: `platform-next/business_graph/graph_parser.py`
- Modify: `platform-next/business_graph/router.py`
- Modify: `platform-next/business_graph/service.py`

**Step 1: 在 graph_parser.py 添加 parse_scenario_graph 函数**

```python
# Add to graph_parser.py

from .service import LAYER_FILES


def parse_scenario_graph(tlg_dir: Path) -> ScenarioGraph:
    """Parse all 7 layer files into a complete graph.

    Args:
        tlg_dir: Path to three-layer-graph/ directory
    """
    graph = ScenarioGraph()

    # Layer file mapping: (layer_id, file_name, parse_mode)
    # KV layers: extract KV-table objects + inline edges
    # Wide layers: extract wide-table objects + table edges
    layer_configs = [
        ('business', '01-business-graph.md'),
        ('feature', '02-feature-graph.md'),
        ('task', '03-task-layer.md'),
        ('command', '04-command-graph.md'),
    ]

    all_edges = []

    for layer_id, file_name in layer_configs:
        path = tlg_dir / file_name
        if not path.exists():
            continue

        md = path.read_text(encoding='utf-8')

        # Extract objects (both KV and wide-table patterns)
        kv_objs = parse_kv_objects(md, layer_id)
        wide_objs = parse_wide_table_objects(md, layer_id)

        for obj in kv_objs + wide_objs:
            if obj.object_id not in graph.objects:
                graph.objects[obj.object_id] = obj

        # Extract edges
        inline_edges = parse_inline_edges(md)
        table_edges = parse_edge_table(md)
        all_edges.extend(inline_edges)
        all_edges.extend(table_edges)

    # Cross-layer mapping file (primary edge source)
    mapping_path = tlg_dir / '05-cross-layer-mapping.md'
    if mapping_path.exists():
        md = mapping_path.read_text(encoding='utf-8')
        all_edges.extend(parse_edge_table(md))

    graph.edges = dedup_edges(all_edges)

    # Find root (BusinessDomain)
    for oid, obj in graph.objects.items():
        if obj.object_type == 'BusinessDomain':
            graph.root_id = oid
            break

    return graph
```

**Step 2: 在 service.py 添加 get_graph 方法**

```python
# Add to BusinessGraphService class in service.py

def get_graph(self, scenario_id: str):
    """Build complete graph for a scenario."""
    from .graph_parser import parse_scenario_graph
    scen = self.get_scenario(scenario_id)
    if not scen:
        return None
    tlg_dir = self._doc_root / scen.dir_path / "three-layer-graph"
    return parse_scenario_graph(tlg_dir)
```

**Step 3: 在 router.py 添加 graph endpoint**

```python
# Add to router.py

@router.get("/scenarios/{scenario_id}/graph")
def get_scenario_graph(scenario_id: str):
    """Get complete graph (objects + edges) for a scenario."""
    svc = get_service()
    graph = svc.get_graph(scenario_id)
    if not graph:
        return {"error": "Scenario not found", "scenario_id": scenario_id}
    return graph.to_dict()
```

**Step 4: 启动后端验证**

```bash
cd D:/mywork/KnowledgeBase/SFCGraph/platform-next
python -c "import uvicorn; uvicorn.run('main:app', host='0.0.0.0', port=8000)" &
sleep 3

# Test graph API
python -c "
import urllib.request, json
# 计费场景
url = 'http://localhost:8000/api/v1/business-graph/scenarios/%E8%AE%A1%E8%B4%B9%E5%9C%BA%E6%99%AF/graph'
with urllib.request.urlopen(url) as resp:
    d = json.loads(resp.read().decode('utf-8'))
print(f'Objects: {len(d[\"objects\"])}')
print(f'Edges: {len(d[\"edges\"])}')
print(f'Root: {d[\"root_id\"]}')

# Count by type
from collections import Counter
types = Counter(obj['object_type'] for obj in d['objects'].values())
for t, c in types.most_common():
    print(f'  {t}: {c}')
"
```

Expected: Objects ~150+, Edges ~100+, Root = BD-CH-01.

**Step 5: Commit**

```bash
git add platform-next/business_graph/graph_parser.py platform-next/business_graph/service.py platform-next/business_graph/router.py
git commit -m "feat: add /graph API endpoint with full scenario graph parsing"
```

---

## Phase 2: 前端级联卡片树

### Task 5: 创建 CascadeNode.vue + CascadeTree.vue

**Files:**
- Create: `platform-next/frontend/src/business_graph/CascadeNode.vue`
- Create: `platform-next/frontend/src/business_graph/CascadeTree.vue`

**Step 1: 创建 CascadeNode.vue（递归卡片节点）**

```vue
<template>
  <div class="cascade-node" :class="{ selected: isSelected }">
    <!-- Connection line from parent -->
    <div v-if="relationLabel" class="cascade-edge">
      <div class="cascade-edge-line"></div>
      <span class="cascade-edge-label">{{ relationLabel }}</span>
    </div>

    <!-- Card body -->
    <div class="cascade-card" @click="handleSelect" :class="{ selected: isSelected }">
      <div class="cascade-card-header">
        <span class="cascade-type-badge" :style="{ background: typeColor }">
          {{ typeLabel }}
        </span>
        <span class="cascade-card-id">{{ node.object_id }}</span>
        <span class="cascade-card-name">{{ node.name }}</span>
        <span v-if="sharedCount > 1" class="cascade-shared-badge">⟲共享</span>
        <button
          v-if="hasChildren"
          class="cascade-expand-btn"
          @click.stop="toggleExpand"
        >{{ expanded ? '▾' : '▸' }}</button>
      </div>
      <p v-if="node.summary" class="cascade-card-summary">{{ node.summary }}</p>
      <div class="cascade-card-meta">
        <span v-for="(count, rel) in childCounts" :key="rel" class="cascade-meta-pill">
          {{ count }} {{ relLabel(rel) }}
        </span>
      </div>
    </div>

    <!-- Children -->
    <div v-if="expanded && hasChildren" class="cascade-children">
      <div class="cascade-children-row">
        <CascadeNode
          v-for="child in children"
          :key="child.object_id"
          :node="child"
          :relation-label="childRelation"
          :graph="graph"
          :selected-id="selectedId"
          :shared-counts="sharedCounts"
          :max-depth="maxDepth - 1"
          :current-depth="currentDepth + 1"
          @select="$emit('select', $event)"
          @navigate="$emit('navigate', $event)"
        />
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed, ref } from 'vue'

interface GraphObject {
  object_id: string
  object_type: string
  name: string
  summary: string
  layer: string
  attributes: Record<string, string>
}

interface GraphEdge {
  from: string
  relation: string
  to: string
  meta?: Record<string, string>
}

interface GraphData {
  objects: Record<string, GraphObject>
  edges: GraphEdge[]
  root_id: string
}

const props = withDefaults(defineProps<{
  node: GraphObject
  relationLabel?: string
  graph: GraphData
  selectedId?: string
  sharedCounts?: Record<string, number>
  maxDepth?: number
  currentDepth?: number
}>(), {
  maxDepth: 3,
  currentDepth: 1,
})

const emit = defineEmits<{
  (e: 'select', id: string): void
  (e: 'navigate', id: string): void
}>()

const expanded = ref(props.currentDepth <= 2) // Auto-expand first 2 levels

// Tree-driving relations (top-to-bottom hierarchy)
const TREE_RELATIONS: Record<string, string> = {
  'BusinessDomain': 'contains',
  'NetworkScenario': 'instantiated_as',
  'ConfigurationSolution': 'uses_feature',
  'Feature': 'decomposes_to',
  'ConfigTask': 'invokes',
}

const childRelation = computed(() => TREE_RELATIONS[props.node.object_type] || '')

const children = computed<GraphObject[]>(() => {
  if (!childRelation.value || props.currentDepth >= props.maxDepth) return []
  const childIds = props.graph.edges
    .filter(e => e.from === props.node.object_id && e.relation === childRelation.value)
    .map(e => e.to)
  return childIds
    .map(id => props.graph.objects[id])
    .filter(Boolean)
})

const hasChildren = computed(() => {
  if (props.currentDepth >= props.maxDepth) return false
  // Check if there are any children in the graph (without computing all)
  return props.graph.edges.some(
    e => e.from === props.node.object_id && e.relation === childRelation.value
  )
})

const childCounts = computed<Record<string, number>>(() => {
  const counts: Record<string, number> = {}
  for (const e of props.graph.edges) {
    if (e.from === props.node.object_id) {
      counts[e.relation] = (counts[e.relation] || 0) + 1
    }
  }
  return counts
})

const isSelected = computed(() => props.selectedId === props.node.object_id)
const sharedCount = computed(() => props.sharedCounts?.[props.node.object_id] || 1)

const TYPE_LABELS: Record<string, string> = {
  BusinessDomain: '业务域',
  NetworkScenario: '场景',
  ConfigurationSolution: '方案',
  Feature: '特性',
  ConfigTask: '任务',
  MMLCommand: '命令',
  DecisionPoint: '决策',
  BusinessRule: '规则',
  SemanticObject: '语义',
}

const TYPE_COLORS: Record<string, string> = {
  BusinessDomain: '#6366f1',
  NetworkScenario: '#8b5cf6',
  ConfigurationSolution: '#3b82f6',
  Feature: '#06b6d4',
  ConfigTask: '#10b981',
  MMLCommand: '#f59e0b',
}

const typeLabel = computed(() => TYPE_LABELS[props.node.object_type] || props.node.object_type)
const typeColor = computed(() => TYPE_COLORS[props.node.object_type] || '#64748b')

function relLabel(rel: string): string {
  const labels: Record<string, string> = {
    uses_feature: '特性',
    uses_task: '任务',
    decomposes_to: '任务',
    invokes: '命令',
    constrained_by: '规则',
    has_decision: '决策',
    uses_semantic_object: '语义',
    requires_license: 'License',
  }
  return labels[rel] || rel
}

function handleSelect() {
  emit('select', props.node.object_id)
  if (hasChildren.value && !expanded.value) {
    expanded.value = true
  }
}

function toggleExpand() {
  expanded.value = !expanded.value
}
</script>
```

**Step 2: 创建 CascadeTree.vue（树容器）**

```vue
<template>
  <div class="cascade-tree">
    <CascadeNode
      v-if="rootNode"
      :node="rootNode"
      :graph="graph"
      :selected-id="selectedId"
      :shared-counts="sharedCounts"
      :max-depth="maxDepth"
      :current-depth="1"
      @select="$emit('select', $event)"
      @navigate="$emit('navigate', $event)"
    />
  </div>
</template>

<script setup lang="ts">
import { computed } from 'vue'
import CascadeNode from './CascadeNode.vue'

interface GraphObject {
  object_id: string
  object_type: string
  name: string
  summary: string
  layer: string
  attributes: Record<string, string>
}

interface GraphEdge {
  from: string
  relation: string
  to: string
}

interface GraphData {
  objects: Record<string, GraphObject>
  edges: GraphEdge[]
  root_id: string
}

const props = withDefaults(defineProps<{
  graph: GraphData
  selectedId?: string
  maxDepth?: number
}>(), {
  maxDepth: 4,
})

defineEmits<{
  (e: 'select', id: string): void
  (e: 'navigate', id: string): void
}>()

const rootNode = computed(() => {
  if (!props.graph.root_id) return null
  return props.graph.objects[props.graph.root_id] || null
})

// Calculate shared counts (how many parents reference each object)
const sharedCounts = computed<Record<string, number>>(() => {
  const counts: Record<string, number> = {}
  for (const e of props.graph.edges) {
    counts[e.to] = (counts[e.to] || 0) + 1
  }
  return counts
})
</script>
```

**Step 3: 验证编译**

```bash
cd D:/mywork/KnowledgeBase/SFCGraph/platform-next/frontend
npx vue-tsc --noEmit 2>&1 | head -20
```

Expected: 无编译错误。

**Step 4: Commit**

```bash
git add platform-next/frontend/src/business_graph/CascadeNode.vue platform-next/frontend/src/business_graph/CascadeTree.vue
git commit -m "feat: add CascadeNode + CascadeTree components for graph tree view"
```

---

## Phase 3: 右侧详情面板

### Task 6: 创建 ObjectDetail.vue + AttrTable.vue + RelGroup.vue

**Files:**
- Create: `platform-next/frontend/src/business_graph/ObjectDetail.vue`

**Step 1: 创建 ObjectDetail.vue**

```vue
<template>
  <div class="object-detail" v-if="obj">
    <!-- Section 1: Header -->
    <div class="detail-header">
      <div class="detail-type-row">
        <span class="detail-type-badge" :style="{ background: typeColor }">
          {{ typeLabel }}
        </span>
        <span class="detail-id">{{ obj.object_id }}</span>
      </div>
      <h2 class="detail-name">{{ obj.name }}</h2>
      <p v-if="obj.summary" class="detail-summary">{{ obj.summary }}</p>
    </div>

    <!-- Section 2: Schema Attributes -->
    <div class="detail-section" v-if="Object.keys(obj.attributes).length">
      <h3 class="detail-section-title">Schema 属性</h3>
      <div class="attr-table">
        <div v-for="(val, key) in obj.attributes" :key="key" class="attr-row">
          <div class="attr-key">{{ key }}</div>
          <div class="attr-val">{{ cleanValue(val) }}</div>
        </div>
      </div>
    </div>

    <!-- Section 3: Relationships -->
    <div class="detail-section" v-if="downstreamGroups.length || upstreamGroups.length || crossGroups.length">
      <h3 class="detail-section-title">关联关系</h3>

      <!-- Downstream (main chain) -->
      <div v-for="g in downstreamGroups" :key="g.relation" class="rel-group">
        <div class="rel-group-header" @click="g.collapsed = !g.collapsed">
          <span class="rel-arrow">{{ g.collapsed ? '▸' : '▾' }}</span>
          <span class="rel-label">下游 · {{ relLabel(g.relation) }}</span>
          <span class="rel-count">{{ g.edges.length }}</span>
        </div>
        <div v-if="!g.collapsed" class="rel-items">
          <div
            v-for="edge in g.edges"
            :key="edge.to"
            class="rel-item"
            @click="$emit('navigate', edge.to)"
          >
            <span class="rel-item-id">{{ edge.to }}</span>
            <span class="rel-item-name">{{ graph.objects[edge.to]?.name || '' }}</span>
            <span v-if="edge.meta?.context" class="rel-item-meta">{{ edge.meta.context }}</span>
          </div>
        </div>
      </div>

      <!-- Upstream (who references me) -->
      <div v-for="g in upstreamGroups" :key="'up_' + g.relation" class="rel-group">
        <div class="rel-group-header" @click="g.collapsed = !g.collapsed">
          <span class="rel-arrow">{{ g.collapsed ? '▸' : '▾' }}</span>
          <span class="rel-label">上游 · {{ relLabel(g.relation) }}</span>
          <span class="rel-count">{{ g.edges.length }}</span>
        </div>
        <div v-if="!g.collapsed" class="rel-items">
          <div
            v-for="edge in g.edges"
            :key="edge.from"
            class="rel-item"
            @click="$emit('navigate', edge.from)"
          >
            <span class="rel-item-id">{{ edge.from }}</span>
            <span class="rel-item-name">{{ graph.objects[edge.from]?.name || '' }}</span>
          </div>
        </div>
      </div>

      <!-- Cross-cutting (rules, decisions, semantic) -->
      <div v-for="g in crossGroups" :key="g.relation" class="rel-group">
        <div class="rel-group-header" @click="g.collapsed = !g.collapsed">
          <span class="rel-arrow">{{ g.collapsed ? '▸' : '▾' }}</span>
          <span class="rel-label">{{ relLabel(g.relation) }}</span>
          <span class="rel-count">{{ g.edges.length }}</span>
        </div>
        <div v-if="!g.collapsed" class="rel-items">
          <div
            v-for="edge in g.edges"
            :key="edge.to"
            class="rel-item"
            @click="$emit('navigate', edge.to)"
          >
            <span class="rel-item-id">{{ edge.to }}</span>
            <span class="rel-item-name">{{ graph.objects[edge.to]?.name || '' }}</span>
          </div>
        </div>
      </div>
    </div>
  </div>
  <div v-else class="object-detail-empty">
    选择左侧对象查看详情
  </div>
</template>

<script setup lang="ts">
import { computed, reactive } from 'vue'

interface GraphObject {
  object_id: string
  object_type: string
  name: string
  summary: string
  attributes: Record<string, string>
}

interface GraphEdge {
  from: string
  relation: string
  to: string
  meta?: Record<string, string>
}

interface GraphData {
  objects: Record<string, GraphObject>
  edges: GraphEdge[]
  root_id: string
}

const props = defineProps<{
  obj: GraphObject | null
  graph: GraphData
}>()

defineEmits<{
  (e: 'navigate', id: string): void
}>()

// Main-chain downstream relations
const DOWNSTREAM_RELS = ['contains', 'instantiated_as', 'uses_feature', 'uses_task', 'decomposes_to', 'invokes', 'operates_on']
// Cross-cutting relations
const CROSS_RELS = ['constrained_by', 'has_decision', 'uses_semantic_object', 'requires_license', 'selects', 'sets_value_pattern']

interface RelGroupData {
  relation: string
  edges: GraphEdge[]
  collapsed: boolean
}

const downstreamGroups = computed<RelGroupData[]>(() => {
  if (!props.obj) return []
  return props.graph.edges
    .filter(e => e.from === props.obj!.object_id && DOWNSTREAM_RELS.includes(e.relation))
    .reduce((groups: RelGroupData[], edge) => {
      let g = groups.find(g => g.relation === edge.relation)
      if (!g) {
        g = reactive({ relation: edge.relation, edges: [], collapsed: false })
        groups.push(g)
      }
      g.edges.push(edge)
      return groups
    }, [])
})

const upstreamGroups = computed<RelGroupData[]>(() => {
  if (!props.obj) return []
  return props.graph.edges
    .filter(e => e.to === props.obj!.object_id && DOWNSTREAM_RELS.includes(e.relation))
    .reduce((groups: RelGroupData[], edge) => {
      let g = groups.find(g => g.relation === edge.relation)
      if (!g) {
        g = reactive({ relation: edge.relation, edges: [], collapsed: false })
        groups.push(g)
      }
      g.edges.push(edge)
      return groups
    }, [])
})

const crossGroups = computed<RelGroupData[]>(() => {
  if (!props.obj) return []
  return props.graph.edges
    .filter(e => e.from === props.obj!.object_id && CROSS_RELS.includes(e.relation))
    .reduce((groups: RelGroupData[], edge) => {
      let g = groups.find(g => g.relation === edge.relation)
      if (!g) {
        g = reactive({ relation: edge.relation, edges: [], collapsed: false })
        groups.push(g)
      }
      g.edges.push(edge)
      return groups
    }, [])
})

const TYPE_LABELS: Record<string, string> = {
  BusinessDomain: '业务域',
  NetworkScenario: '场景',
  ConfigurationSolution: '方案',
  Feature: '特性',
  ConfigTask: '任务',
  DecisionPoint: '决策点',
  BusinessRule: '业务规则',
  SemanticObject: '语义对象',
  MMLCommand: 'MML命令',
  ConfigObject: '配置对象',
  License: 'License',
}

const TYPE_COLORS: Record<string, string> = {
  BusinessDomain: '#6366f1',
  NetworkScenario: '#8b5cf6',
  ConfigurationSolution: '#3b82f6',
  Feature: '#06b6d4',
  ConfigTask: '#10b981',
  MMLCommand: '#f59e0b',
  DecisionPoint: '#ec4899',
  BusinessRule: '#ef4444',
  SemanticObject: '#14b8a6',
}

const typeLabel = computed(() => props.obj ? (TYPE_LABELS[props.obj.object_type] || props.obj.object_type) : '')
const typeColor = computed(() => props.obj ? (TYPE_COLORS[props.obj.object_type] || '#64748b') : '#64748b')

function relLabel(rel: string): string {
  const labels: Record<string, string> = {
    contains: '包含场景',
    instantiated_as: '实例化方案',
    uses_feature: '使用特性',
    uses_task: '使用任务',
    decomposes_to: '分解为任务',
    invokes: '调用命令',
    operates_on: '操作对象',
    constrained_by: '约束规则',
    has_decision: '决策点',
    uses_semantic_object: '语义对象',
    requires_license: '需要License',
    selects: '选择',
    sets_value_pattern: '设置参数模式',
  }
  return labels[rel] || rel
}

function cleanValue(val: string): string {
  if (!val) return ''
  return val.replace(/`/g, '').replace(/\*\*/g, '').trim()
}
</script>
```

**Step 2: Commit**

```bash
git add platform-next/frontend/src/business_graph/ObjectDetail.vue
git commit -m "feat: add ObjectDetail component with schema attributes and relationship groups"
```

---

## Phase 4: 整合改造 BusinessScenario.vue

### Task 7: 改造 BusinessScenario.vue 为 Explorer 布局

**Files:**
- Modify: `platform-next/frontend/src/business_graph/BusinessScenario.vue`
- Modify: `platform-next/frontend/src/api.ts`

**Step 1: 在 api.ts 添加 graph endpoint**

```typescript
// Add to businessGraphApi in api.ts
  graph: (id: string) => `${BASE}/business-graph/scenarios/${encodeURIComponent(id)}/graph`,
```

**Step 2: 重写 BusinessScenario.vue**

```vue
<template>
  <div v-if="scenario" class="page-container">
    <div class="explorer-layout">
      <!-- Header -->
      <div class="explorer-header">
        <button class="back-btn" @click="$router.push('/business-graph')">← 返回</button>
        <div class="explorer-titles">
          <div class="explorer-breadcrumb">
            {{ scenario.domain_name }} / {{ scenario.scenario_name }}
          </div>
        </div>
      </div>

      <!-- Main: Tree + Detail -->
      <div class="explorer-body" v-if="graphData">
        <!-- Left: Cascade Tree -->
        <div class="explorer-left">
          <CascadeTree
            :graph="graphData"
            :selected-id="selectedId"
            :max-depth="4"
            @select="handleSelect"
            @navigate="handleNavigate"
          />
        </div>

        <!-- Right: Object Detail -->
        <div class="explorer-right">
          <ObjectDetail
            :obj="selectedObject"
            :graph="graphData"
            @navigate="handleNavigate"
          />
        </div>
      </div>
      <div v-else class="explorer-loading">加载图数据中...</div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, computed, watch } from 'vue'
import { useRoute } from 'vue-router'
import { businessGraphApi, fetchJson } from '../api'
import CascadeTree from './CascadeTree.vue'
import ObjectDetail from './ObjectDetail.vue'

const route = useRoute()
const scenarioId = computed(() => route.params.scenarioId as string)

const loading = ref(true)
const scenario = ref<any>(null)
const graphData = ref<any>(null)
const selectedId = ref('')

const selectedObject = computed(() => {
  if (!selectedId.value || !graphData.value) return null
  return graphData.value.objects[selectedId.value] || null
})

async function loadGraph() {
  loading.value = true
  try {
    const scenData = await fetchJson(businessGraphApi.scenario(scenarioId.value))
    scenario.value = scenData.error ? null : scenData

    const graph = await fetchJson(businessGraphApi.graph(scenarioId.value))
    graphData.value = graph.error ? null : graph

    // Auto-select root
    if (graphData.value?.root_id) {
      selectedId.value = graphData.value.root_id
    }
  } finally {
    loading.value = false
  }
}

function handleSelect(id: string) {
  selectedId.value = id
}

function handleNavigate(id: string) {
  selectedId.value = id
  // Could also auto-expand tree to this node in future
}

watch([scenarioId], () => {
  loadGraph()
})

onMounted(loadGraph)
</script>

<style scoped>
.explorer-layout {
  display: flex;
  flex-direction: column;
  height: 100vh;
  padding-top: var(--space-4);
}
.explorer-header {
  display: flex;
  align-items: center;
  gap: var(--space-4);
  padding: 0 var(--space-6) var(--space-4);
  border-bottom: 1px solid var(--border);
}
.explorer-breadcrumb {
  font-size: var(--text-sm);
  color: var(--text-secondary);
}
.explorer-body {
  display: flex;
  flex: 1;
  overflow: hidden;
}
.explorer-left {
  flex: 1;
  overflow-y: auto;
  padding: var(--space-5);
}
.explorer-right {
  width: 420px;
  flex-shrink: 0;
  overflow-y: auto;
  border-left: 1px solid var(--border);
  padding: var(--space-5);
}
.explorer-loading {
  text-align: center;
  padding: var(--space-12);
  color: var(--text-tertiary);
}
</style>
```

**Step 3: 为 CascadeNode 添加基础样式**

在 CascadeNode.vue 的 `<style scoped>` 中添加：

```css
.cascade-node {
  margin-bottom: var(--space-2);
}
.cascade-edge {
  display: flex;
  align-items: center;
  gap: var(--space-2);
  padding-left: var(--space-2);
  margin-bottom: var(--space-1);
}
.cascade-edge-line {
  width: 2px;
  height: 16px;
  background: var(--border);
}
.cascade-edge-label {
  font-size: var(--text-2xs);
  color: var(--text-tertiary);
}
.cascade-card {
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: var(--radius-lg, 12px);
  padding: var(--space-3) var(--space-4);
  cursor: pointer;
  transition: all 0.15s;
}
.cascade-card:hover {
  border-color: var(--accent-glow);
  box-shadow: var(--shadow-card);
}
.cascade-card.selected {
  border-left: 3px solid var(--accent);
}
.cascade-card-header {
  display: flex;
  align-items: center;
  gap: var(--space-2);
  flex-wrap: wrap;
}
.cascade-type-badge {
  color: white;
  font-size: 10px;
  padding: 1px 8px;
  border-radius: 999px;
  font-weight: 500;
}
.cascade-card-id {
  font-family: var(--font-mono);
  font-size: var(--text-2xs);
  color: var(--text-tertiary);
}
.cascade-card-name {
  font-size: var(--text-sm);
  font-weight: 600;
  color: var(--text-primary);
}
.cascade-shared-badge {
  font-size: 10px;
  color: var(--accent);
  background: var(--accent-soft);
  padding: 1px 6px;
  border-radius: 999px;
}
.cascade-expand-btn {
  background: none;
  border: none;
  cursor: pointer;
  color: var(--text-tertiary);
  font-size: var(--text-xs);
  padding: 0 4px;
}
.cascade-card-summary {
  font-size: var(--text-2xs);
  color: var(--text-secondary);
  line-height: 1.5;
  margin: var(--space-1) 0 0;
  display: -webkit-box;
  -webkit-line-clamp: 1;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
.cascade-card-meta {
  display: flex;
  gap: var(--space-2);
  flex-wrap: wrap;
  margin-top: var(--space-1);
}
.cascade-meta-pill {
  font-size: 9px;
  color: var(--text-tertiary);
  background: var(--bg-page);
  padding: 1px 6px;
  border-radius: 999px;
}
.cascade-children {
  padding-left: var(--space-5);
  margin-top: var(--space-2);
}
.cascade-children-row {
  display: flex;
  flex-wrap: wrap;
  gap: var(--space-2);
}
.cascade-children-row .cascade-node {
  flex: 1;
  min-width: 200px;
  max-width: 320px;
}
</style>
```

**Step 4: 为 ObjectDetail 添加基础样式**

在 ObjectDetail.vue 的 `<style scoped>` 中添加：

```css
.object-detail {
  font-size: var(--text-xs);
}
.detail-header {
  margin-bottom: var(--space-4);
  padding-bottom: var(--space-3);
  border-bottom: 1px solid var(--border);
}
.detail-type-row {
  display: flex;
  align-items: center;
  gap: var(--space-2);
  margin-bottom: var(--space-1);
}
.detail-type-badge {
  color: white;
  font-size: 10px;
  padding: 1px 8px;
  border-radius: 999px;
}
.detail-id {
  font-family: var(--font-mono);
  font-size: var(--text-2xs);
  color: var(--text-tertiary);
}
.detail-name {
  font-size: var(--text-lg);
  font-weight: 700;
  margin: 0 0 var(--space-1);
}
.detail-summary {
  font-size: var(--text-xs);
  color: var(--text-secondary);
  line-height: 1.6;
  margin: 0;
}
.detail-section {
  margin-bottom: var(--space-4);
}
.detail-section-title {
  font-size: var(--text-xs);
  font-weight: 600;
  color: var(--text-tertiary);
  text-transform: uppercase;
  letter-spacing: 0.5px;
  margin: 0 0 var(--space-2);
}
.attr-table {
  display: grid;
  grid-template-columns: minmax(120px, 180px) 1fr;
  gap: 1px;
  background: var(--border-light);
  border: 1px solid var(--border-light);
  border-radius: var(--radius, 8px);
  overflow: hidden;
}
.attr-row {
  display: contents;
}
.attr-key {
  background: var(--bg-page);
  padding: 4px 10px;
  font-family: var(--font-mono);
  font-size: var(--text-2xs);
  font-weight: 500;
  color: var(--text-secondary);
}
.attr-val {
  background: var(--bg-card);
  padding: 4px 10px;
  font-size: var(--text-2xs);
  color: var(--text-primary);
  line-height: 1.5;
}
.rel-group {
  margin-bottom: var(--space-2);
}
.rel-group-header {
  display: flex;
  align-items: center;
  gap: var(--space-2);
  cursor: pointer;
  padding: var(--space-1) 0;
  user-select: none;
}
.rel-group-header:hover {
  color: var(--accent);
}
.rel-arrow {
  font-size: 10px;
  color: var(--text-tertiary);
}
.rel-label {
  font-size: var(--text-xs);
  font-weight: 500;
}
.rel-count {
  font-size: 10px;
  color: var(--accent);
  background: var(--accent-soft);
  padding: 1px 6px;
  border-radius: 999px;
}
.rel-items {
  padding-left: var(--space-5);
}
.rel-item {
  display: flex;
  align-items: baseline;
  gap: var(--space-2);
  padding: 3px 6px;
  border-radius: var(--radius, 4px);
  cursor: pointer;
  font-size: var(--text-2xs);
  transition: background 0.1s;
}
.rel-item:hover {
  background: var(--accent-soft);
}
.rel-item-id {
  font-family: var(--font-mono);
  color: var(--accent);
  flex-shrink: 0;
}
.rel-item-name {
  color: var(--text-secondary);
  flex: 1;
}
.rel-item-meta {
  color: var(--text-tertiary);
  font-style: italic;
}
.object-detail-empty {
  text-align: center;
  padding: var(--space-12);
  color: var(--text-tertiary);
}
</style>
```

**Step 5: 启动后端+前端验证**

```bash
# Start backend (if not running)
cd D:/mywork/KnowledgeBase/SFCGraph/platform-next
python -c "import uvicorn; uvicorn.run('main:app', host='0.0.0.0', port=8000)" &

# Frontend should auto-reload via Vite HMR
# Open http://localhost:3000/business-graph/计费场景
```

验证：
- 左栏显示 BD 卡片，自动展开 NS → CS
- 点击 CS 卡片右栏显示属性 + 关系
- 关系项可点击跳转

**Step 6: Commit**

```bash
git add platform-next/frontend/src/business_graph/BusinessScenario.vue platform-next/frontend/src/api.ts
git commit -m "feat: rewrite BusinessScenario as Explorer layout with cascade tree + detail panel"
```

---

## Phase 5: 修复返回按钮 + 视觉优化

### Task 8: 修复返回按钮样式 + 最终验证

**Step 1: 确保 back-btn 样式正确**

在 BusinessScenario.vue 的 `<style scoped>` 中添加：

```css
.back-btn {
  background: var(--bg-card);
  border: 1px solid var(--border);
  color: var(--text-secondary);
  padding: var(--space-2) var(--space-4);
  border-radius: var(--radius, 8px);
  font-size: var(--text-xs);
  cursor: pointer;
  transition: all 0.15s;
}
.back-btn:hover {
  border-color: var(--accent);
  color: var(--accent);
}
```

**Step 2: 验证两个场景都能正常加载**

```bash
# 计费场景
curl -s http://localhost:8000/api/v1/business-graph/scenarios/%E8%AE%A1%E8%B4%B9%E5%9C%BA%E6%99%AF/graph | python -c "import sys,json; d=json.load(sys.stdin); print(f'Objects: {len(d[\"objects\"])}, Edges: {len(d[\"edges\"])}')"

# 带宽控制场景
curl -s http://localhost:8000/api/v1/business-graph/scenarios/%E5%B8%A6%E5%AE%BD%E6%8E%A7%E5%88%B6%E5%9C%BA%E6%99%AF/graph | python -c "import sys,json; d=json.load(sys.stdin); print(f'Objects: {len(d[\"objects\"])}, Edges: {len(d[\"edges\"])}')"
```

**Step 3: Commit**

```bash
git add platform-next/frontend/src/business_graph/
git commit -m "feat: business graph explorer with cascade tree and detail panel"
```

---

## 关键文件清单

**新建:**
- `platform-next/business_graph/graph_parser.py` — 图解析器
- `platform-next/frontend/src/business_graph/CascadeTree.vue` — 级联树容器
- `platform-next/frontend/src/business_graph/CascadeNode.vue` — 递归卡片节点
- `platform-next/frontend/src/business_graph/ObjectDetail.vue` — 右侧详情面板

**修改:**
- `platform-next/business_graph/service.py` — 添加 get_graph 方法
- `platform-next/business_graph/router.py` — 添加 /graph endpoint
- `platform-next/frontend/src/business_graph/BusinessScenario.vue` — 重写为 Explorer 布局
- `platform-next/frontend/src/api.ts` — 添加 graph URL

**不修改:**
- `business-graph/` 目录下任何文件（设计态资产）
- `BusinessGraphIndex.vue`（域级卡片入口保持不变）
