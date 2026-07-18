import re
from .models import Edge
from typing import Optional

# 重新导出，便于 `from app.edges import parse_edges, Edge`
__all__ = ["parse_edges", "extract_implicit_edges", "Edge"]

# - {relation}: [[ {to_id} ]]
_LINE_RE = re.compile(r"^\s*-\s*(?P<rel>[^:]+?):\s*\[\[(?P<to>[^\]]+)\]\]\s*$", re.M)

# 正文内联 wikilink [[ X ]]
_WIKI_RE = re.compile(r"\[\[([^\]\n]+?)\]\]")


def parse_edges(edge_section: str, from_id: str, from_version: Optional[str]) -> list:
    """从 ``## 边`` 章节解析显式边 ``- 关系: [[目标]]``。"""
    if not edge_section:
        return []
    seen = set()
    out = []
    for m in _LINE_RE.finditer(edge_section):
        rel = m.group("rel").strip()
        to = m.group("to").strip()
        key = (from_id, rel, to)
        if key in seen:
            continue
        seen.add(key)
        out.append(Edge(from_id=from_id, from_version=from_version, relation=rel, to=to))
    return out


def extract_implicit_edges(
    fm: dict, body: str, from_id: str, from_version: Optional[str],
    include_body_links: bool = False,
) -> list:
    """从 frontmatter ``ref`` 字段 + 正文内联 ``[[X]]`` 提取隐式边。

    用于没有 ``## 边`` 章节的对象（如任务类 AtomTask/CompoundTask/FeatureTask）：
    它们通过 ``ref:`` 指向命令、正文中用 ``[[...]]`` 引用其他对象。

    - ``ref`` frontmatter 字段 → relation="引用命令"（权威，1 条）。
    - 正文内联 ``[[X]]`` → relation="参见"（仅 include_body_links=True 时）。
    - **按目标去重**：同一目标只留一条边（ref 优先于参见）。
    """
    out: list = []
    seen_targets: set = set()

    def _add(relation: str, to: str) -> None:
        target = to.strip()
        if not target or target == from_id or target in seen_targets:
            return
        seen_targets.add(target)
        out.append(Edge(from_id=from_id, from_version=from_version, relation=relation, to=target))

    # 1. ref frontmatter（任务.ref → 命令）
    ref = fm.get("ref")
    if isinstance(ref, str) and ref.strip():
        _add("引用命令", ref)

    # 2. 正文内联 [[...]] wikilink（无 ## 边 时作为兜底）
    if include_body_links:
        for m in _WIKI_RE.finditer(body or ""):
            _add("参见", m.group(1))

    return out
