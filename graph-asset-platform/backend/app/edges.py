import re
from .models import Edge
from typing import Optional

# 重新导出，便于 `from app.edges import parse_edges, Edge`
__all__ = ["parse_edges", "Edge"]

# - {relation}: [[ {to_id} ]]
_LINE_RE = re.compile(r"^\s*-\s*(?P<rel>[^:]+?):\s*\[\[(?P<to>[^\]]+)\]\]\s*$", re.M)

def parse_edges(edge_section: str, from_id: str, from_version: Optional[str]) -> list:
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
