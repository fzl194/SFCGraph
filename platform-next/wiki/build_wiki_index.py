"""扫 assets/ 全量 md，组装 Index（nodes + edges + 反邻接）。

两遍：
  pass1: 逐文件解析 front-matter + 正文链接 → nodes、id_to_path、body edges、占位边
  pass2: front-matter 派生边（task.ref→command、feature.parent_feature_code→parent），经 id_to_path 解析后去重加入
"""
from __future__ import annotations
import json
import sys
import posixpath
from collections import defaultdict
from pathlib import Path

import yaml

from wiki.models import Edge, Index, Node
from wiki.parser import extract_links, object_type_of, parse_front_matter, split_front_matter

# type -> 取分组字段的函数（返回 ((field, value), ...) tuple）
_GROUP_FIELDS = {
    "MMLCommand": lambda m: _pairs(m, "category_path", "verb", "object_keyword"),
    "ConfigObject": lambda m: _pairs(m, "object_kind", "object_name"),
    "Feature": lambda m: _pairs(m, "feature_category", "parent_feature_code", "catalog_section"),
    "License": lambda m: _pairs(m, "applicable_nf"),
    "Task": lambda m: _pairs(m, "task_layer", "ref"),
}


def _pairs(m: dict, *keys: str) -> tuple[tuple[str, str], ...]:
    out: list[tuple[str, str]] = []
    for k in keys:
        if k not in m:
            continue
        v = m[k]
        if isinstance(v, list):
            v = "/".join(str(x) for x in v)
        if v in (None, ""):
            continue
        out.append((k, str(v)))
    return tuple(out)


def _first_h1(body: str) -> str:
    for line in body.splitlines():
        s = line.strip()
        if s.startswith("# "):
            return s[2:].strip()
    return ""


def build_index(assets_root: Path) -> Index:
    assets_root = assets_root.resolve()
    nodes: dict[str, Node] = {}
    id_to_path: dict[str, str] = {}
    out_edges: dict[str, list[Edge]] = defaultdict(list)
    reverse: dict[str, list[str]] = defaultdict(list)

    for md_path in sorted(assets_root.rglob("*.md")):
        rel = md_path.relative_to(assets_root).as_posix()
        text = md_path.read_text(encoding="utf-8")
        fm_text, body = split_front_matter(text)
        meta = parse_front_matter(fm_text)
        ntype = str(meta.get("type", _infer_type_from_path(rel)))
        group_fn = _GROUP_FIELDS.get(ntype)
        group = group_fn(meta) if group_fn else ()
        title = _first_h1(body) or str(meta.get("name", ""))
        node = Node(
            path=rel,
            id=str(meta.get("id", "")),
            type=ntype,
            name=str(meta.get("name", title)),
            nf=meta.get("nf"),
            version=meta.get("version"),
            status=str(meta.get("status", "")),
            title=title,
            group=group,
        )
        nodes[rel] = node
        if node.id:
            id_to_path[node.id] = rel

        # 正文 + 占位边
        seen: set[tuple[str, str]] = set()
        for lk in extract_links(body):
            key = (lk.dst, lk.relation_type)
            if key in seen:
                continue
            seen.add(key)
            out_edges[rel].append(Edge(src=rel, dst=lk.dst, relation_type=lk.relation_type, resolved=lk.resolved))
            if lk.resolved:
                reverse[lk.dst].append(rel)

    # pass2: front-matter 派生边（经 id_to_path 解析）
    for rel, node in nodes.items():
        meta_path_pairs: list[tuple[str, str]] = []  # (ref_value, relation_type)
        if node.type == "Task":
            # 重新读 meta 取 ref（轻量：node 未存 raw ref，这里从 group 重建亦可；改用重新解析）
            fm_text, _ = split_front_matter((assets_root / rel).read_text(encoding="utf-8"))
            ref = parse_front_matter(fm_text).get("ref")
            if ref:
                meta_path_pairs.append((ref, "ref_command"))
        if node.type == "Feature":
            fm_text, _ = split_front_matter((assets_root / rel).read_text(encoding="utf-8"))
            parent = parse_front_matter(fm_text).get("parent_feature_code")
            if parent:
                # parent_feature_code 不是完整 id，拼成 Feature id 查 id_to_path
                pid = f"{node.nf}@{node.version}@Feature@{parent}"
                meta_path_pairs.append((pid, "parent"))
        for ref_value, rel_type in meta_path_pairs:
            tgt_path = id_to_path.get(ref_value)
            key = (tgt_path or ref_value, rel_type)
            existing = {(e.dst, e.relation_type) for e in out_edges[rel]}
            if key in existing:
                continue
            if tgt_path:
                out_edges[rel].append(Edge(src=rel, dst=tgt_path, relation_type=rel_type, resolved=True))
                reverse[tgt_path].append(rel)

    return Index(
        nodes=nodes,
        id_to_path=id_to_path,
        out_edges={k: tuple(v) for k, v in out_edges.items()},
        reverse={k: tuple(v) for k, v in reverse.items()},
    )


def _infer_type_from_path(rel: str) -> str:
    top = rel.split("/", 1)[0]
    return {
        "command": "MMLCommand",
        "configobject": "ConfigObject",
        "feature": "Feature",
        "license": "License",
        "task": "Task",
    }.get(top, top.capitalize())


def _node_to_dict(n: Node) -> dict:
    return {
        "path": n.path, "id": n.id, "type": n.type, "name": n.name,
        "nf": n.nf, "version": n.version, "status": n.status,
        "title": n.title, "group": [list(p) for p in n.group],
    }


def _edge_to_dict(e: Edge) -> dict:
    return {"from": e.src, "to": e.dst, "relation_type": e.relation_type, "resolved": e.resolved}


def serialize_index(idx: Index) -> str:
    payload = {
        "nodes": {p: _node_to_dict(n) for p, n in idx.nodes.items()},
        "edges": [_edge_to_dict(e) for edges in idx.out_edges.values() for e in edges],
        "reverse": dict(idx.reverse),
        "id_to_path": dict(idx.id_to_path),
    }
    return json.dumps(payload, ensure_ascii=False, indent=2)


def deserialize_index(text: str) -> Index:
    d = json.loads(text)
    nodes = {p: Node(
        path=n["path"], id=n["id"], type=n["type"], name=n["name"],
        nf=n["nf"], version=n["version"], status=n["status"],
        title=n["title"], group=tuple(tuple(p) for p in n["group"]),
    ) for p, n in d["nodes"].items()}
    out_edges: dict[str, list[Edge]] = defaultdict(list)
    for e in d["edges"]:
        out_edges[e["from"]].append(Edge(src=e["from"], dst=e["to"], relation_type=e["relation_type"], resolved=e["resolved"]))
    return Index(
        nodes=nodes,
        id_to_path=d["id_to_path"],
        out_edges={k: tuple(v) for k, v in out_edges.items()},
        reverse={k: tuple(v) for k, v in d["reverse"].items()},
    )


def main(argv: list[str] | None = None) -> int:
    """CLI: python -m wiki.build_wiki_index <assets_root> <out_json>"""
    argv = argv or sys.argv[1:]
    if len(argv) < 2:
        print("usage: build_wiki_index <assets_root> <out_json>", file=sys.stderr)
        return 2
    assets_root = Path(argv[0])
    out = Path(argv[1])
    idx = build_index(assets_root)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(serialize_index(idx), encoding="utf-8")
    print(f"indexed {len(idx.nodes)} nodes -> {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
