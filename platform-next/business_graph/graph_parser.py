# -*- coding: utf-8 -*-
"""Deep graph parser: extracts objects + edges from 7 layer MD files.

Parses three-layer-graph MD files to build a complete scenario graph:
- KV-table objects (BD, NS, CS, Feature, Task, etc.) from ### headings
- Wide-table object collections (DP, BR, SO, CMD, etc.) from ## sections
- Inline relationship edges (**uses_feature**: GWFD-xxx、GWFD-yyy)
- Explicit edge tables (起点 | 关系 | 终点)
- Cross-layer mapping edges from 05-cross-layer-mapping.md
"""
import re
from pathlib import Path
from dataclasses import dataclass, field
from typing import Optional


# Shared object ID pattern - requires hyphen after letter prefixes to avoid
# false positives like "NSESWITCH" matching "NS" prefix.
# Matches: BD-CH-01, NS-CH-01, CS-CH-01, DP-CH-01, BR-CH-01, SO-CH-01,
#           GWFD-010171, WSFD-011201, T-001, CMD-UDG-001, EV-KB-001, LKV3G5SABS01
OBJECT_ID_PATTERN = (
    r'(?:'
    r'(?:BD|NS|CS|DP|BR|SO|EV|CMD)-[\w-]+'  # Prefix with hyphen: BD-CH-01, CMD-UDG-001
    r'|GWFD-\d+'                            # GWFD-010171
    r'|WSFD-\d+'                            # WSFD-011201
    r'|T-\d+'                               # T-001, T-101
    r'|LKV[\w]+'                            # LKV3G5SABS01
    r')'
)


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
        # Match | `field` | value | or | field | value |
        m = re.match(r'^\|\s*`?([^|]+?)`?\s*\|\s*([^|]+?)\s*\|\s*$', line)
        if not m:
            continue
        key = m.group(1).strip().strip('`').strip()
        val = m.group(2).strip().strip('`').strip()
        if key and key != '字段' and key != '---' and not re.match(r'^[-:\s]+$', key):
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

    Handles patterns like:
      ### 1.1 BusinessDomain  (section header, ID in KV table)
      ### 2.1 CS-CH-01 离线计费方案  (numbered prefix + ID + name)
      #### GWFD-110101 SA-Basic (#### level for Feature objects)
      ### T-001 规划业务分类与识别条件  (Task objects)
    """
    objects = []
    # Type keywords for fallback heading detection (when ID is in KV table, not heading)
    _heading_type_map = {
        'BusinessDomain': 'BusinessDomain',
        'NetworkScenario': 'NetworkScenario',
    }

    # Find all headings that could be object definitions
    for m in re.finditer(r'^(#{3,4})\s+(.+)$', md_text, re.MULTILINE):
        heading_text = m.group(2).strip()

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

        # Try ID-in-heading pattern first
        id_match = re.match(
            r'^(?:\d+\.\d+\s+)?((?:BD|NS|CS|DP|BR|SO|EV|CMD|LKV)[-\w]*|GWFD-\d+|WSFD-\d+|T-\d+)\s+(.+)$',
            heading_text
        )

        if id_match:
            # ID is in the heading
            obj_id = id_match.group(1).strip()
            fallback_name = id_match.group(2).strip()
            attrs = _parse_kv_table(section_text)
            if not attrs:
                continue
            obj_type = _detect_object_type(obj_id, layer)
        else:
            # Fallback: check if heading contains a type keyword like "BusinessDomain"
            # and extract ID from the KV table itself
            fallback_type = None
            for kw, ot in _heading_type_map.items():
                if kw in heading_text:
                    fallback_type = ot
                    break
            if not fallback_type:
                continue
            attrs = _parse_kv_table(section_text)
            if not attrs:
                continue
            # Extract ID from attrs
            id_keys_map = {
                'BusinessDomain': 'domain_id',
                'NetworkScenario': 'scenario_id',
            }
            id_key = id_keys_map.get(fallback_type, '')
            obj_id = attrs.get(id_key, '')
            if not obj_id:
                continue
            obj_type = fallback_type
            fallback_name = heading_text

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

# Expected ID prefix patterns for each object type
# Used to filter out false positives (e.g., parameter tables misidentified as MMLCommand)
_TYPE_ID_PREFIXES = {
    'BusinessDomain': ('BD-',),
    'NetworkScenario': ('NS-',),
    'ConfigurationSolution': ('CS-',),
    'DecisionPoint': ('DP-',),
    'BusinessRule': ('BR-',),
    'SemanticObject': ('SO-',),
    'Feature': ('GWFD-', 'WSFD-'),
    'License': ('LKV',),
    'FeatureRule': ('FR-',),
    'ConfigTask': ('T-',),
    'TaskRule': ('TR-',),
    'MMLCommand': ('CMD-',),
    'ConfigObject': (),  # ConfigObject IDs vary (URR, RULE, etc.)
    'CommandRule': ('CR-',),
    'EvidenceSource': ('EV-',),
}


def _detect_wide_table_type(heading_text: str) -> Optional[str]:
    """Detect if a ## heading introduces a wide-table object collection."""
    for keyword, obj_type in _WIDE_TABLE_TYPES.items():
        if keyword in heading_text:
            return obj_type
    return None


def _parse_wide_table(text: str, obj_type: str, layer: str) -> list[GraphObject]:
    """Parse ALL wide tables in a section where each row is an object.

    Handles multiple sub-tables within one ## section (e.g., command layer has
    ### 1.1 through ### 1.8 sub-sections, each with its own MMLCommand table).

    Skips KV-format tables (2-column | 字段 | 值 | tables) since those are
    handled by parse_kv_objects.
    """
    objects = []
    lines = text.split('\n')

    i = 0
    while i < len(lines):
        line = lines[i].strip()

        # Look for table headers
        if not (line.startswith('|') and not line.startswith('|:')):
            i += 1
            continue

        # Must have separator next
        if i + 1 >= len(lines) or not re.match(r'^\|[\s:|-]+\|$', lines[i + 1].strip()):
            i += 1
            continue

        # Parse headers
        headers = [h.strip().strip('`').strip() for h in line.strip('|').split('|')]

        # Skip KV tables (2-col or 字段/值)
        if len(headers) <= 2:
            i += 1
            continue
        if '字段' in headers and '值' in headers:
            i += 1
            continue

        i += 2  # skip header + separator

        # Parse rows of this table
        while i < len(lines):
            row_line = lines[i].strip()
            if not row_line.startswith('|'):
                break
            cells = [c.strip().strip('`').strip() for c in row_line.strip('|').split('|')]
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

            # Validate ID prefix matches expected pattern for this object type
            # This filters out false positives like parameter tables being parsed as MMLCommand
            expected_prefixes = _TYPE_ID_PREFIXES.get(obj_type, ())
            if expected_prefixes:
                if not any(obj_id.startswith(p) for p in expected_prefixes):
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
            # Extract owner ID from heading (handles "2.1 CS-CH-01 name" pattern)
            m = re.match(
                r'^#{3,4}\s+(?:\d+\.\d+\s+)?(' + OBJECT_ID_PATTERN + r')',
                section
            )
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
                    r'^(' + OBJECT_ID_PATTERN + r')',
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


# Known relation types that appear as header keywords in mapping tables
_RELATION_KEYWORDS = {
    'uses_feature', 'uses_task', 'decomposes_to', 'invokes',
    'targets', 'selects', 'sets_value_pattern',
    'constrained_by', 'has_decision', 'uses_semantic_object',
    'contains', 'instantiated_as', 'operates_on', 'has_parameter',
    'precedes', 'sequential',
}


def _is_relation_keyword(text: str) -> bool:
    """Check if text is a known relation keyword."""
    return text.strip().lower() in _RELATION_KEYWORDS


# Range pattern: CS-CH-01 ~ CS-CH-07  or  CS-CH-01~CS-CH-07  or  T-001 - T-005
_RANGE_RE = re.compile(
    r'((?:BD|NS|CS|DP|BR|SO|EV|CMD)-\D*\d+)\s*[~\-–—到]\s*((?:BD|NS|CS|DP|BR|SO|EV|CMD)-\D*(\d+))',
    re.MULTILINE
)


def expand_id_list(text: str) -> list[str]:
    """Extract and expand all object IDs from a text cell.

    Handles:
    - Range notation: `CS-CH-01 ~ CS-CH-07` → 7 IDs
    - Comma/slash/Chinese-comma separated: `CS-CH-01, CS-CH-04` → 2 IDs
    - Single IDs
    """
    # Strip ALL backticks first - MD cells have inline code markers that break regex
    text = text.replace('`', '')
    # First, expand ranges
    expanded = text
    range_replacements: list[str] = []

    def _expand_range(m: re.Match) -> str:
        start_id = m.group(1)
        end_num = int(m.group(3))
        # Extract prefix and start number from start_id
        # Pattern: PREFIX-DDD where DDD is trailing digits
        parts = re.match(r'^(.*?)(\d+)$', start_id)
        if not parts:
            return start_id
        prefix = parts.group(1)
        start_num = int(parts.group(2))
        # Detect zero-padding width from start_id
        start_digit_str = parts.group(2)
        pad_width = len(start_digit_str)

        if end_num < start_num:
            return start_id

        ids = []
        for n in range(start_num, end_num + 1):
            ids.append(f"{prefix}{n:0{pad_width}d}")
        range_replacements.extend(ids)
        return ' '.join(ids)

    expanded = _RANGE_RE.sub(_expand_range, expanded)

    # Now find all IDs in the expanded text
    ids = re.findall(r'(' + OBJECT_ID_PATTERN + r')', expanded)
    # Deduplicate while preserving order
    seen = set()
    result = []
    for id_val in ids:
        if id_val not in seen:
            seen.add(id_val)
            result.append(id_val)
    return result


def parse_edge_table(md_text: str) -> list[GraphEdge]:
    """Extract edges from explicit edge tables.

    Handles two table formats:

    1. Standard edge table: | 起点 | 关系 | 终点 |
       Where each row has from_id, relation, to_id in cells.

    2. Mapping table: | CS | uses_feature | Feature角色 |
       Where the relation is encoded in a column HEADER (not cell),
       and the cells contain from_id and to_id respectively.

    Also handles 4-column mapping: | ConfigTask | invokes | MMLCommand | 说明 |
    """
    edges = []
    lines = md_text.split('\n')

    i = 0
    while i < len(lines):
        line = lines[i].strip()

        if not line.startswith('|'):
            i += 1
            continue

        # Must have separator next
        if i + 1 >= len(lines) or not re.match(r'^\|[\s:|-]+\|$', lines[i + 1].strip()):
            i += 1
            continue

        headers_raw = line.strip('|').split('|')
        headers = [h.strip().strip('`').strip() for h in headers_raw]

        # Skip KV tables
        if len(headers) <= 2:
            i += 1
            continue
        if '字段' in headers and '值' in headers:
            i += 1
            continue

        # Detect table pattern
        # Pattern 1: Standard edge table - has "起点"/"from" and "终点"/"to" headers,
        #   or has "关系"/"relation" header
        # Pattern 2: Mapping table - one header column IS a relation keyword
        relation_from_header = None
        relation_header_col = -1
        for col_idx, h in enumerate(headers):
            if _is_relation_keyword(h):
                relation_from_header = h
                relation_header_col = col_idx
                break

        # Identify "from" and "to" columns
        # For mapping tables (relation in header), find from and to by looking
        # for ID-bearing columns in the data
        i += 2  # skip header + separator

        if relation_from_header:
            # Pattern 2: Mapping table where relation is in header
            # from_col = first column with CS/T/Feature/DP IDs
            # to_col = next column with Feature/CMD/T/SO IDs
            # The relation_header_col itself may contain the to_id or be a label

            # Find from and to columns: the columns that contain object IDs in rows
            from_col = 0
            to_col = None

            # If relation_header_col is the middle column, from=0, to=last data col
            # e.g., | CS | uses_feature | Feature角色 | → from=0, to=2 (skipping col 1 as it's rel header)
            # But col 1 cells contain Feature IDs! So actually:
            # | CS-CH-01 离线计费 | GWFD-010171（离线UDG） | 核心：UDG侧离线收集 |
            # The to_id is in col 1 (under uses_feature header)

            # Strategy: scan first few rows to find which columns have IDs
            sample_lines = []
            j = i
            while j < len(lines) and lines[j].strip().startswith('|') and len(sample_lines) < 3:
                sample_lines.append(lines[j].strip())
                j += 1

            id_cols = set()
            for sl in sample_lines:
                cells = [c.strip().strip('`').strip() for c in sl.strip('|').split('|')]
                for ci, cell in enumerate(cells):
                    if re.search(OBJECT_ID_PATTERN, cell):
                        id_cols.add(ci)

            id_cols_sorted = sorted(id_cols)
            if len(id_cols_sorted) >= 2:
                from_col = id_cols_sorted[0]
                to_col = id_cols_sorted[1]
            elif len(id_cols_sorted) == 1:
                from_col = id_cols_sorted[0]
                # Try the column after from that's not the relation col
                for c in range(len(headers)):
                    if c != from_col and c != relation_header_col:
                        to_col = c
                        break

            if to_col is None or from_col == to_col:
                # Skip this table
                while i < len(lines) and lines[i].strip().startswith('|'):
                    i += 1
                continue

            # Parse rows
            while i < len(lines):
                row_line = lines[i].strip()
                if not row_line.startswith('|'):
                    break
                cells = [c.strip().strip('`').strip() for c in row_line.strip('|').split('|')]

                if from_col >= len(cells) or to_col >= len(cells):
                    i += 1
                    continue

                from_ids = expand_id_list(cells[from_col])
                to_targets = expand_id_list(cells[to_col])

                if from_ids and to_targets:
                    for from_id in from_ids:
                        for to_id in to_targets:
                            edges.append(GraphEdge(
                                from_id=from_id,
                                relation=relation_from_header,
                                to_id=to_id,
                            ))
                i += 1
        else:
            # Pattern 1: Standard edge table with 起点 | 关系 | 终点 columns
            # Or detect from column headers
            from_col = None
            rel_col = None
            to_col = None

            for col_idx, h in enumerate(headers):
                h_lower = h.lower()
                if h_lower in ('起点', 'from') or 'cs' == h_lower or 'configtask' == h_lower.lower():
                    if from_col is None:
                        from_col = col_idx
                elif h_lower in ('终点', 'to', '目标', 'mmlcommand'):
                    to_col = col_idx
                elif h_lower in ('关系', 'relation'):
                    rel_col = col_idx

            # If no explicit from/to detected, try to detect by content
            if from_col is None or to_col is None:
                # Scan first data row
                if i < len(lines) and lines[i].strip().startswith('|'):
                    test_cells = [c.strip().strip('`').strip()
                                  for c in lines[i].strip().strip('|').split('|')]
                    id_cols = []
                    for ci, cell in enumerate(test_cells):
                        if re.search(OBJECT_ID_PATTERN, cell):
                            id_cols.append(ci)
                    if from_col is None and len(id_cols) >= 1:
                        from_col = id_cols[0]
                    if to_col is None and len(id_cols) >= 2:
                        to_col = id_cols[-1]

            if from_col is None or to_col is None or from_col == to_col:
                # Skip this table
                while i < len(lines) and lines[i].strip().startswith('|'):
                    i += 1
                continue

            # Parse rows
            while i < len(lines):
                row_line = lines[i].strip()
                if not row_line.startswith('|'):
                    break
                cells = [c.strip().strip('`').strip() for c in row_line.strip('|').split('|')]

                if from_col >= len(cells) or to_col >= len(cells):
                    i += 1
                    continue

                from_val = cells[from_col]
                to_val = cells[to_col]

                # Relation from rel_col cell or from header
                if rel_col is not None and rel_col < len(cells):
                    rel_val = cells[rel_col].strip()
                    if not rel_val or not _is_relation_keyword(rel_val):
                        rel_val = ''
                else:
                    rel_val = ''

                from_ids = expand_id_list(from_val)
                to_targets = expand_id_list(to_val)

                if from_ids and to_targets and rel_val:
                    for from_id in from_ids:
                        for to_id in to_targets:
                            edges.append(GraphEdge(
                                from_id=from_id,
                                relation=rel_val,
                                to_id=to_id,
                            ))
                i += 1

    return edges


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


def build_command_syntax_map(objects: dict) -> dict[str, str]:
    """Build {command_syntax_upper → CMD-ID} from MMLCommand objects."""
    syntax_map: dict[str, str] = {}
    for oid, obj in objects.items():
        if getattr(obj, 'object_type', '') != 'MMLCommand':
            continue
        syntax = obj.attributes.get('command_syntax', '').strip().strip('`').strip()
        if syntax:
            syntax_map[syntax.upper()] = oid
    return syntax_map


# Match command syntax tokens like "ADD URR", "SET LICENSESWITCH", "LOD SIGNATUREDB"
_COMMAND_SYNTAX_RE = re.compile(
    r'\b(SET|ADD|MOD|DEL|RMV|LST|DSP|LOD|SAVE|RESET|ACT|DEACT|SWAP)\s+([A-Z][A-Z0-9_]{1,30})\b'
)


def parse_invokes_from_mapping(
    mapping_md: str,
    syntax_map: dict[str, str],
) -> list[GraphEdge]:
    """Parse Task→Command (invokes) edges from the cross-layer mapping file.

    The mapping table uses command syntax names (e.g., "ADD URR") instead of
    CMD- IDs. This function resolves syntax names to CMD- IDs via syntax_map.

    Table format:
        | ConfigTask | invokes | MMLCommand | 说明 |
        | T-006 | invokes | ADD URR, ADD URRGROUP | 计费三件套核心 |
    """
    edges: list[GraphEdge] = []
    lines = mapping_md.split('\n')

    # Find the invokes section: ## 4. ConfigTask → MMLCommand
    in_invokes_section = False
    for i, line in enumerate(lines):
        stripped = line.strip()

        # Detect section start
        if re.match(r'^##\s+.*ConfigTask.*MMLCommand.*invokes', stripped, re.IGNORECASE) or \
           re.match(r'^##\s+4\.', stripped):
            in_invokes_section = True
            continue
        # Exit on next ## section
        if in_invokes_section and re.match(r'^##\s+', stripped) and not \
           re.match(r'^##\s+4\.', stripped):
            break

        if not in_invokes_section:
            continue
        if not stripped.startswith('|'):
            continue
        # Skip header and separator rows
        if '---' in stripped:
            continue
        if 'ConfigTask' in stripped and 'MMLCommand' in stripped:
            continue

        cells = [c.strip().strip('`').strip() for c in stripped.strip('|').split('|')]
        if len(cells) < 3:
            continue

        # Column 0: Task ID(s), Column 2: command syntax list
        from_ids = expand_id_list(cells[0])
        if not from_ids:
            continue

        # Find the column with command syntaxes (usually column 2)
        cmd_col = None
        for ci in range(1, len(cells)):
            if _COMMAND_SYNTAX_RE.search(cells[ci]):
                cmd_col = ci
                break
        if cmd_col is None:
            continue

        # Extract all command syntax tokens from the cell
        cmd_cell = cells[cmd_col]
        # Also try plain comma-split for robustness
        raw_tokens = [t.strip().strip('`').strip() for t in cmd_cell.split(',')]
        # Plus regex-extracted tokens (catches ones without commas)
        regex_tokens = [m.group(0) for m in _COMMAND_SYNTAX_RE.finditer(cmd_cell)]

        all_tokens = set()
        for t in raw_tokens + regex_tokens:
            t = t.strip().strip('`').strip()
            if t:
                all_tokens.add(t)

        for syntax in all_tokens:
            cmd_id = syntax_map.get(syntax.upper())
            if not cmd_id:
                continue
            for from_id in from_ids:
                edges.append(GraphEdge(
                    from_id=from_id,
                    relation='invokes',
                    to_id=cmd_id,
                ))

    return edges


def parse_scenario_graph(tlg_dir: Path) -> ScenarioGraph:
    """Parse all 7 layer files into a complete graph.

    Args:
        tlg_dir: Path to three-layer-graph/ directory
    """
    graph = ScenarioGraph()

    # Layer file mapping: (layer_id, file_name)
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

        # Resolve Task→Command invokes edges (syntax names → CMD-IDs)
        syntax_map = build_command_syntax_map(graph.objects)
        if syntax_map:
            invokes_edges = parse_invokes_from_mapping(md, syntax_map)
            all_edges.extend(invokes_edges)

    graph.edges = dedup_edges(all_edges)

    # Find root (BusinessDomain)
    for oid, obj in graph.objects.items():
        if obj.object_type == 'BusinessDomain':
            graph.root_id = oid
            break

    return graph
