"""扫 assets/ md，组装 Index（nodes + edges + 反邻接）。

- build_index: 全量构建（首次 / 索引缺失）。
- update_incremental: 增量更新——只重读 mtime 新于上次的文件 + 删除已消失文件，
  reverse 整体重建（O(边)，无 IO）。重启时秒级拾取新增/改动对象。
"""
from __future__ import annotations
import json
import sys
from collections import defaultdict
from pathlib import Path

from wiki.models import Edge, Index, Node
from wiki.parser import extract_links, object_type_of, parse_front_matter, split_front_matter

# type -> 取分组字段的函数（返回 ((field, value), ...) tuple）
_GROUP_FIELDS = {
    "MMLCommand": lambda m: _pairs(m, "category_path", "verb", "object_keyword"),
    "ConfigObject": lambda m: _pairs(m, "object_kind", "object_name"),
    "Feature": lambda m: _pairs(m, "feature_category", "parent_feature_code", "catalog_section"),
    "License": lambda m: _pairs(m, "applicable_nf"),
    "Task": lambda m: _pairs(m, "task_layer", "ref"),
    "BusinessDomain": lambda m: _pairs(m, "domain"),
    "NetworkScenario": lambda m: _pairs(m, "domain", "scenario"),
    "ConfigurationSolution": lambda m: _pairs(m, "domain", "scenario"),
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


def _infer_type_from_path(rel: str) -> str:
    """front-matter 无 type 时的路径兜底推断。business/ 下是业务层（含 SOP/index/审视），不应硬推 BD——
    走 generic 命名，由 Lint/前端后续处理。"""
    top = rel.split("/", 1)[0]
    return {
        "command": "MMLCommand",
        "configobject": "ConfigObject",
        "feature": "Feature",
        "license": "License",
        "task": "Task",
    }.get(top, top.capitalize())


def _parse_file(md_path: Path, assets_root: Path) -> tuple[Node, list[Edge], dict]:
    """解析单个 md → (node, 正文+占位边, front-matter dict)。
    front-matter 派生边不在此处（需跨文件 id_to_path 解析），见 _fm_edges。"""
    rel = md_path.relative_to(assets_root).as_posix()
    text = md_path.read_text(encoding="utf-8")
    fm_text, body = split_front_matter(text)
    meta = parse_front_matter(fm_text)
    obj_id = str(meta.get("id", ""))
    # 业务层目录（business/）下 front-matter 必须有 id+type 才算 typed 对象；
    # 缺其一视为 SOP/index/CLAUDE 等元文件，不入 nodes（不进 categories/图谱）。
    # 其他目录保持原行为：按已有 front-matter 或路径兜底推断，避免误伤其他场景下
    # 缺少 front-matter 的纯内容文件。
    if rel.startswith("business/") and (not obj_id or not meta.get("type")):
        return None, [], meta
    id_parts = obj_id.split("@") if obj_id else []
    ntype = str(meta.get("type") or object_type_of(obj_id) or _infer_type_from_path(rel))
    group_fn = _GROUP_FIELDS.get(ntype)
    group = group_fn(meta) if group_fn else ()
    title = _first_h1(body) or str(meta.get("name", ""))
    # nf/version 优先取 front-matter；缺失时从 4 段式对象 ID 回填（2 段式业务层 ID 保持 None）
    nf = meta.get("nf") or (id_parts[0] if len(id_parts) >= 4 else None)
    version = meta.get("version") or (id_parts[1] if len(id_parts) >= 4 else None)
    node = Node(
        path=rel, id=obj_id, type=ntype, name=str(meta.get("name", title)),
        nf=nf, version=version, status=str(meta.get("status", "")),
        title=title, group=group,
    )
    body_edges: list[Edge] = []
    seen: set[tuple[str, str]] = set()
    for lk in extract_links(body):
        key = (lk.dst, lk.relation_type)
        if key in seen:
            continue
        seen.add(key)
        body_edges.append(Edge(src=rel, dst=lk.dst, relation_type=lk.relation_type, resolved=lk.resolved))
    return node, body_edges, meta


def _fm_edges(node: Node, meta: dict, id_to_path: dict[str, str]) -> list[Edge]:
    """front-matter 派生边（Task.ref→command、Feature.parent_feature_code→parent），
    经 id_to_path 解析；仅返回命中（resolved）的。"""
    out: list[Edge] = []
    if node.type == "Task":
        ref = meta.get("ref")
        if ref:
            tgt = id_to_path.get(ref)
            if tgt:
                out.append(Edge(src=node.path, dst=tgt, relation_type="ref_command", resolved=True))
    if node.type == "Feature":
        parent = meta.get("parent_feature_code")
        if parent:
            pid = f"{node.nf}@{node.version}@Feature@{parent}"
            tgt = id_to_path.get(pid)
            if tgt:
                out.append(Edge(src=node.path, dst=tgt, relation_type="parent", resolved=True))
    return out


def _rebuild_reverse(out_edges: dict[str, list[Edge]]) -> dict[str, list[str]]:
    reverse: dict[str, list[str]] = defaultdict(list)
    for src, edges in out_edges.items():
        for e in edges:
            if e.resolved:
                reverse[e.dst].append(src)
    return reverse


def build_index(assets_root: Path) -> Index:
    assets_root = assets_root.resolve()
    nodes: dict[str, Node] = {}
    id_to_path: dict[str, str] = {}
    out_edges: dict[str, list[Edge]] = defaultdict(list)
    parsed: dict[str, tuple[Node, list[Edge], dict]] = {}

    # pass1：逐文件解析节点 + 正文边；元文件（无 id/type）跳过
    for md_path in sorted(assets_root.rglob("*.md")):
        node, body_edges, meta = _parse_file(md_path, assets_root)
        if node is None:                         # 元文件，不入 nodes/edges
            continue
        rel = node.path
        parsed[rel] = (node, body_edges, meta)
        nodes[rel] = node
        if node.id:
            id_to_path[node.id] = rel
        for e in body_edges:
            out_edges[rel].append(e)

    # pass2：front-matter 派生边（经 id_to_path 解析，与正文边去重）
    for rel, (node, _body_edges, meta) in parsed.items():
        existing = {(e.dst, e.relation_type) for e in out_edges[rel]}
        for fe in _fm_edges(node, meta, id_to_path):
            if (fe.dst, fe.relation_type) in existing:
                continue
            existing.add((fe.dst, fe.relation_type))
            out_edges[rel].append(fe)

    reverse = _rebuild_reverse(out_edges)
    return Index(
        nodes=nodes,
        id_to_path=id_to_path,
        out_edges={k: tuple(v) for k, v in out_edges.items()},
        reverse={k: tuple(v) for k, v in reverse.items()},
    )


def update_incremental(idx: Index, assets_root: Path, cutoff_mtime: float) -> tuple[Index, int]:
    """增量更新：只重读 mtime 新于 cutoff_mtime 的文件 + 删除已消失文件。
    reverse 整体重建（O(边)，无 IO）。返回 (新 index, 变更文件数)；无变更返回 (原 idx, 0)。"""
    assets_root = assets_root.resolve()
    changed: list[Path] = []
    on_disk: set[str] = set()
    for f in assets_root.rglob("*.md"):
        rel = f.relative_to(assets_root).as_posix()
        on_disk.add(rel)
        if f.stat().st_mtime > cutoff_mtime + 1:   # +1s grace
            changed.append(f)
    deleted = set(idx.nodes) - on_disk
    if not changed and not deleted:
        return idx, 0

    new_nodes = dict(idx.nodes)
    new_id2p = dict(idx.id_to_path)
    new_out: dict[str, list[Edge]] = {k: list(v) for k, v in idx.out_edges.items()}

    def _drop(rel: str) -> None:
        old = new_nodes.get(rel)
        if old and old.id and new_id2p.get(old.id) == rel:
            new_id2p.pop(old.id, None)
        new_nodes.pop(rel, None)
        new_out.pop(rel, None)

    # 先解析改动文件、更新 nodes + id_to_path（fm 边解析依赖 id2p）
    parsed: dict[str, tuple[Node, list[Edge], dict]] = {}
    for f in changed:
        node, body_edges, meta = _parse_file(f, assets_root)
        rel = f.relative_to(assets_root).as_posix()
        if node is None:                       # 元文件（business/ 下无 id/type），不入索引
            _drop(rel)
            continue
        parsed[rel] = (node, body_edges, meta)
        _drop(rel)                       # 清旧（id 可能变）
        new_nodes[rel] = node
        if node.id:
            new_id2p[node.id] = rel
    for rel in deleted:
        _drop(rel)

    # 重算改动文件的全量边（正文 + fm 派生，fm 用最新 id2p）
    for rel, (node, body_edges, meta) in parsed.items():
        edges = list(body_edges)
        existing = {(e.dst, e.relation_type) for e in edges}
        for fe in _fm_edges(node, meta, new_id2p):
            if (fe.dst, fe.relation_type) in existing:
                continue
            existing.add((fe.dst, fe.relation_type))
            edges.append(fe)
        new_out[rel] = edges

    reverse = _rebuild_reverse(new_out)
    new_idx = Index(
        nodes=new_nodes,
        id_to_path=new_id2p,
        out_edges={k: tuple(v) for k, v in new_out.items()},
        reverse={k: tuple(v) for k, v in reverse.items()},
    )
    return new_idx, len(changed) + len(deleted)


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
