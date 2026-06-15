# -*- coding: utf-8 -*-
"""Business graph data service.

Scans `business-graph/*/three-layer-graph/` to discover domains and scenarios.
Parses MD files lightly: splits by headings, extracts markdown tables.

Design constraints:
- NEVER modify source files under business-graph/ (design-time assets).
- Light parsing only — re-parse on demand when MD updates.
- Configuration-driven: new scenarios discovered automatically by directory scan.
"""
import re
from pathlib import Path
from dataclasses import dataclass, field
from functools import lru_cache


# Layer file order (matches three-layer-graph convention)
LAYER_FILES = [
    ("overview", "00-overview.md", "总览"),
    ("business", "01-business-graph.md", "第1层 · 业务图谱"),
    ("feature", "02-feature-graph.md", "第2层 · 特性图谱"),
    ("task", "03-task-layer.md", "第3层 · 任务原子层"),
    ("command", "04-command-graph.md", "第4层 · 命令图谱"),
    ("mapping", "05-cross-layer-mapping.md", "第5层 · 跨层映射"),
    ("evidence", "06-evidence-index.md", "第6层 · 证据层"),
]


@dataclass
class Table:
    headers: list[str]
    rows: list[dict]
    title: str = ""


@dataclass
class Section:
    level: int  # 2 for ##, 3 for ###
    title: str
    raw: str  # full raw text of this section (excluding heading)
    tables: list[Table] = field(default_factory=list)
    paragraphs: list[str] = field(default_factory=list)


@dataclass
class LayerDoc:
    layer_id: str
    layer_name: str
    file_name: str
    title: str  # first H1
    sections: list[Section]
    raw: str  # full MD content


@dataclass
class Scenario:
    scenario_id: str  # directory name, e.g. "计费场景"
    scenario_name: str  # parsed from NS table
    domain_id: str  # parsed from BD table, e.g. "BD-CH-01"
    domain_name: str  # e.g. "业务感知"
    dir_path: str
    summary: str = ""
    object_counts: dict = field(default_factory=dict)


@dataclass
class Domain:
    domain_id: str
    domain_name: str
    summary: str = ""
    scenarios: list[Scenario] = field(default_factory=list)


# ---------- MD parsing helpers ----------

_HEADING_RE = re.compile(r'^(#{1,6})\s+(.+?)\s*$', re.MULTILINE)
_TABLE_ROW_RE = re.compile(r'^\|(.+)\|\s*$')
_TABLE_SEP_RE = re.compile(r'^\|[\s:|-]+\|\s*$')


def _parse_table(lines: list[str], start: int) -> tuple[Table | None, int]:
    """Try to parse a markdown table starting near `lines[start]`.

    Returns (table, next_index) or (None, start+1).
    """
    n = len(lines)
    i = start
    # Skip blank lines
    while i < n and not lines[i].strip():
        i += 1
    if i >= n:
        return None, start + 1

    # First table row (header)
    if not _TABLE_ROW_RE.match(lines[i]):
        return None, start + 1
    header_line = i
    # Separator row
    if i + 1 >= n or not _TABLE_SEP_RE.match(lines[i + 1]):
        return None, start + 1

    headers_raw = lines[i].strip().strip('|').split('|')
    headers = [h.strip().strip('`').strip() for h in headers_raw]

    i += 2  # skip header + separator
    rows = []
    while i < n and _TABLE_ROW_RE.match(lines[i]):
        cells_raw = lines[i].strip().strip('|').split('|')
        # pad/truncate to header length
        while len(cells_raw) < len(headers):
            cells_raw.append('')
        row = {headers[j]: cells_raw[j].strip().strip('`').strip() for j in range(len(headers))}
        rows.append(row)
        i += 1

    return Table(headers=headers, rows=rows), i


def _extract_tables(text: str) -> list[Table]:
    """Extract all markdown tables from a text block."""
    lines = text.split('\n')
    tables = []
    i = 0
    while i < len(lines):
        if _TABLE_ROW_RE.match(lines[i]):
            tbl, next_i = _parse_table(lines, i)
            if tbl and tbl.rows:
                tables.append(tbl)
                i = next_i
                continue
        i += 1
    return tables


def _split_sections(md_text: str) -> list[Section]:
    """Split MD by ## and ### headings. Return list of sections."""
    matches = list(_HEADING_RE.finditer(md_text))
    if not matches:
        return [Section(level=0, title='', raw=md_text, tables=_extract_tables(md_text))]

    sections = []
    for idx, m in enumerate(matches):
        level = len(m.group(1))
        if level < 2:  # skip H1
            continue
        title = m.group(2).strip()
        start = m.end()
        end = matches[idx + 1].start() if idx + 1 < len(matches) else len(md_text)
        raw = md_text[start:end].strip()

        # Find preceding table title (line ending with table label)
        # Look back for a line like "*表1 xxx*" or "**xxx**"
        tables = _extract_tables(raw)
        # Extract paragraphs (non-table, non-heading text)
        paras = []
        for blk in re.split(r'\n\s*\n', raw):
            blk_clean = blk.strip()
            if not blk_clean:
                continue
            if _TABLE_ROW_RE.match(blk_clean.split('\n')[0]):
                continue
            # strip markdown bold/italic markers for readability
            paras.append(blk_clean)

        sections.append(Section(level=level, title=title, raw=raw, tables=tables, paragraphs=paras))
    return sections


def _parse_layer_file(path: Path, layer_id: str, layer_name: str, file_name: str) -> LayerDoc | None:
    if not path.exists():
        return None
    raw = path.read_text(encoding='utf-8')
    # H1 title
    h1_match = re.match(r'^#\s+(.+)$', raw, re.MULTILINE)
    title = h1_match.group(1).strip() if h1_match else path.stem
    sections = _split_sections(raw)
    return LayerDoc(
        layer_id=layer_id,
        layer_name=layer_name,
        file_name=file_name,
        title=title,
        sections=sections,
        raw=raw,
    )


def _extract_first_value(table: Table, key_pattern: str) -> str:
    """Find a row whose first cell matches key_pattern, return second cell."""
    pat = re.compile(key_pattern)
    for row in table.rows:
        if not row:
            continue
        first_val = next(iter(row.values()), '')
        if pat.search(first_val):
            vals = list(row.values())
            return vals[1] if len(vals) > 1 else ''
    return ''


# ---------- Service ----------

class BusinessGraphService:
    def __init__(self):
        self._doc_root = Path(__file__).resolve().parent.parent.parent
        self._bg_root = self._doc_root / "business-graph"

    def _scenario_dirs(self) -> list[Path]:
        """Find all scenario directories containing three-layer-graph/."""
        if not self._bg_root.exists():
            return []
        result = []
        for entry in sorted(self._bg_root.iterdir()):
            if not entry.is_dir():
                continue
            tlg = entry / "three-layer-graph"
            if tlg.exists() and (tlg / "01-business-graph.md").exists():
                result.append(entry)
        return result

    def _parse_scenario(self, dir_path: Path) -> Scenario:
        """Parse a scenario directory into a Scenario object."""
        scenario_id = dir_path.name
        biz_path = dir_path / "three-layer-graph" / "01-business-graph.md"
        raw = biz_path.read_text(encoding='utf-8')

        domain_id = ""
        domain_name = ""
        scenario_name = scenario_id
        summary = ""

        tables = _extract_tables(raw)
        for tbl in tables:
            if not domain_id:
                v = _extract_first_value(tbl, r'domain_id')
                if v:
                    domain_id = v
                    domain_name = _extract_first_value(tbl, r'domain_name') or domain_name
                    summary = _extract_first_value(tbl, r'domain_summary') or summary
            if scenario_name == scenario_id:
                v = _extract_first_value(tbl, r'scenario_id')
                if v:
                    scenario_name = _extract_first_value(tbl, r'scenario_name') or scenario_id

        # Object counts: scan overview file if present
        obj_counts = {}
        overview_path = dir_path / "three-layer-graph" / "00-overview.md"
        if overview_path.exists():
            ov_raw = overview_path.read_text(encoding='utf-8')
            for tbl in _extract_tables(ov_raw):
                for row in tbl.rows:
                    cells = list(row.values())
                    if len(cells) >= 3:
                        k = cells[0].strip().strip('`').strip()
                        v = (cells[2] if len(cells) > 2 else cells[1]).strip().strip('`').strip()
                        if k:
                            obj_counts[k] = v

        return Scenario(
            scenario_id=scenario_id,
            scenario_name=scenario_name,
            domain_id=domain_id or f"BD-{scenario_id}",
            domain_name=domain_name or scenario_id,
            dir_path=str(dir_path.relative_to(self._doc_root)).replace('\\', '/'),
            summary=summary,
            object_counts=obj_counts,
        )

    def list_domains(self) -> list[Domain]:
        """List all business domains with their scenarios.

        Aggregates by domain_name (业务感知 etc.), since different scenarios
        may use different domain_id prefixes (BD-CH-01, BD-BW-01) but share
        the same domain.
        """
        domains: dict[str, Domain] = {}
        for dir_path in self._scenario_dirs():
            scen = self._parse_scenario(dir_path)
            if scen.domain_name not in domains:
                domains[scen.domain_name] = Domain(
                    domain_id=scen.domain_name,  # use name as key for aggregation
                    domain_name=scen.domain_name,
                    summary=scen.summary,
                )
            domains[scen.domain_name].scenarios.append(scen)
        return list(domains.values())

    def get_domain(self, domain_name: str) -> Domain | None:
        for d in self.list_domains():
            if d.domain_name == domain_name:
                return d
        return None

    def get_scenario(self, scenario_id: str) -> Scenario | None:
        for dir_path in self._scenario_dirs():
            if dir_path.name == scenario_id:
                return self._parse_scenario(dir_path)
        return None

    def list_layers(self, scenario_id: str) -> list[LayerDoc]:
        """Parse all layer files for a scenario."""
        scen = self.get_scenario(scenario_id)
        if not scen:
            return []
        tlg_dir = self._doc_root / scen.dir_path / "three-layer-graph"
        result = []
        for layer_id, file_name, layer_name in LAYER_FILES:
            path = tlg_dir / file_name
            layer = _parse_layer_file(path, layer_id, layer_name, file_name)
            if layer:
                result.append(layer)
        return result

    def get_layer(self, scenario_id: str, layer_id: str) -> LayerDoc | None:
        for layer in self.list_layers(scenario_id):
            if layer.layer_id == layer_id:
                return layer
        return None

    def get_raw_md(self, scenario_id: str, layer_id: str) -> str:
        """Return raw MD content for a layer."""
        layer = self.get_layer(scenario_id, layer_id)
        return layer.raw if layer else ""

    def get_graph(self, scenario_id: str):
        """Build complete graph (objects + edges) for a scenario."""
        from .graph_parser import parse_scenario_graph
        scen = self.get_scenario(scenario_id)
        if not scen:
            return None
        tlg_dir = self._doc_root / scen.dir_path / "three-layer-graph"
        return parse_scenario_graph(tlg_dir)


# Singleton
_service: BusinessGraphService | None = None


def get_service() -> BusinessGraphService:
    global _service
    if _service is None:
        _service = BusinessGraphService()
    return _service
