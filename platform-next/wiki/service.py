"""wiki 查询服务：载入/构建索引到内存，提供 categories/group/list/neighborhood/md/search。

启动时若 index_path 不存在或 stale（mtime < assets 最新 mtime），自动重建。
"""
from __future__ import annotations
import threading
from pathlib import Path

from wiki.build_wiki_index import build_index, deserialize_index, serialize_index
from wiki.models import Index
from wiki.parser import object_type_of

# 分组字段（每类一个主字段）
_GROUP_FIELD = {
    "MMLCommand": "category_path",
    "ConfigObject": "object_kind",
    "Feature": "parent_feature_code",
    "License": "applicable_nf",
    "Task": "task_layer",
}

# 导航/索引文件 —— 不进图谱（它们列了同类全部对象，制造噪声边，不是知识关系）
_NAV_BASENAMES = {"index.md", "CLAUDE.md", "README.md", "log.md", "PROGRESS.md"}


def _is_nav(path: str) -> bool:
    """是否导航/索引文件（按 basename 判定）。"""
    return path.rsplit("/", 1)[-1] in _NAV_BASENAMES


class WikiService:
    def __init__(self, assets_root: Path, index_path: Path) -> None:
        self.assets_root = Path(assets_root).resolve()
        self.index_path = Path(index_path)
        self._index: Index | None = None
        self._lock = threading.Lock()

    @property
    def index(self) -> Index:
        # load-once-and-cache + 锁：避免首请求并发时多线程同时反序列化/构建索引
        if self._index is None:
            with self._lock:
                if self._index is None:
                    self._index = self._load_or_build()
        return self._index

    def warm_up(self) -> None:
        """启动时一次性载入索引（在 lifespan 调用），避免首请求并发竞态。"""
        _ = self.index

    def _load_or_build(self) -> Index:
        # 有索引文件直接载入（~1-2s）；缺失才全量构建。
        # assets 变更后用 CLI 手动重建：
        #   python -m wiki.build_wiki_index ../assets wiki/data/wiki_index.json
        if self.index_path.exists():
            return deserialize_index(self.index_path.read_text(encoding="utf-8"))
        idx = build_index(self.assets_root)
        self.index_path.parent.mkdir(parents=True, exist_ok=True)
        self.index_path.write_text(serialize_index(idx), encoding="utf-8")
        return idx

    # ---- 查询 ----

    def categories(self) -> list[dict]:
        agg: dict[str, dict[str, dict[str, int]]] = {}
        for n in self.index.nodes.values():
            if not n.nf or not n.version:
                continue
            agg.setdefault(n.type, {}).setdefault(n.nf, {}).setdefault(n.version, 0)
            agg[n.type][n.nf][n.version] += 1
        return [
            {"type": t, "nfs": [{"nf": nf, "versions": [{"version": v, "count": c} for v, c in vers.items()]}
                                for nf, vers in nfs.items()]}
            for t, nfs in agg.items()
        ]

    def group(self, ntype: str, nf: str, version: str) -> list[dict]:
        field = _GROUP_FIELD.get(ntype, "")
        buckets: dict[str, int] = {}
        for n in self.index.nodes.values():
            if n.type != ntype or n.nf != nf or n.version != version:
                continue
            val = dict(n.group).get(field, "(未分组)")
            buckets[val] = buckets.get(val, 0) + 1
        return [{"key": k, "count": v} for k, v in sorted(buckets.items(), key=lambda x: -x[1])]

    def list_objs(self, ntype: str, nf: str, version: str,
                  group_field: str | None = None, group_value: str | None = None,
                  q: str | None = None, page: int = 1, size: int = 100) -> dict:
        items = []
        for n in self.index.nodes.values():
            if n.type != ntype or n.nf != nf or n.version != version:
                continue
            if group_field and group_value:
                if dict(n.group).get(group_field) != group_value:
                    continue
            if q and q.lower() not in (n.name + n.title + n.id).lower():
                continue
            items.append({"path": n.path, "name": n.name, "id": n.id, "title": n.title})
        items.sort(key=lambda x: x["name"])
        total = len(items)
        start = (page - 1) * size
        return {"items": items[start:start + size], "total": total, "page": page, "size": size}

    def _node_dict(self, path: str | None, obj_id: str | None, resolved: bool) -> dict:
        if path and path in self.index.nodes:
            n = self.index.nodes[path]
            return {"path": n.path, "id": n.id, "type": n.type, "name": n.name,
                    "nf": n.nf, "version": n.version, "title": n.title, "resolved": True}
        return {"path": None, "id": obj_id or "", "type": object_type_of(obj_id or ""),
                "name": (obj_id or "").split("@")[-1], "resolved": resolved}

    def neighborhood(self, path: str) -> dict:
        idx = self.index
        center = idx.nodes.get(path)
        if not center:
            return {"center": None, "nodes": [], "edges": []}
        nodes: dict[str, dict] = {path: self._node_dict(path, center.id, True)}
        edges: list[dict] = []
        # 出向（resolved 命中用节点 id，否则用 None 路径占位）。跳过导航目标。
        for e in idx.out_edges.get(path, ()):
            if e.resolved and e.dst in idx.nodes and _is_nav(e.dst):
                continue
            if e.resolved and e.dst in idx.nodes:
                nodes.setdefault(e.dst, self._node_dict(e.dst, idx.nodes[e.dst].id, True))
            else:
                nodes.setdefault(e.dst, self._node_dict(None, e.dst, e.resolved))
            edges.append({"from": e.src, "to": e.dst, "relation_type": e.relation_type, "resolved": e.resolved})
        # 反链。跳过导航源（index.md/CLAUDE.md 等）。
        for src in idx.reverse.get(path, ()):
            if _is_nav(src):
                continue
            sn = idx.nodes.get(src)
            nodes.setdefault(src, self._node_dict(src, sn.id if sn else "", True))
            # 反链边：从 src 指向 center，关系类型取 src 自己出向边中对 center 的那条
            src_out = {(ee.dst, ee.relation_type) for ee in idx.out_edges.get(src, ())}
            rel = next((r for (d, r) in src_out if d == path), "related")
            # reverse 仅含真实文件源（Chunk1 reverse 只收 resolved 边），故 resolved=True
            edges.append({"from": src, "to": path, "relation_type": rel, "resolved": True})
        return {
            "center": self._node_dict(path, center.id, True),
            "nodes": list(nodes.values()),
            "edges": edges,
        }

    def md(self, path: str) -> dict | None:
        full = (self.assets_root / path).resolve()
        try:
            full.relative_to(self.assets_root)  # 路径穿越防护
        except ValueError:
            return None
        if not full.is_file() or full.suffix != ".md":
            return None
        n = self.index.nodes.get(path.replace("\\", "/"))
        return {"path": path, "content": full.read_text(encoding="utf-8"),
                "meta": {"type": n.type if n else None, "name": n.name if n else None,
                         "title": n.title if n else None}}

    def search(self, q: str, limit: int = 30) -> list[dict]:
        ql = q.lower()
        out = []
        for n in self.index.nodes.values():
            if ql in (n.name + " " + n.title + " " + n.id).lower():
                out.append({"path": n.path, "type": n.type, "name": n.name, "title": n.title})
                if len(out) >= limit:
                    break
        return out

    def locate(self, path: str) -> dict | None:
        """对象在左树里的位置（type/nf/version/分组桶），供前端逐层展开高亮。
        非"可分类"对象（evidence/schema/skill/无 nf·version）返回 None。"""
        n = self.index.nodes.get(path.replace("\\", "/"))
        if not n or not n.type or not n.nf or not n.version:
            return None
        gf = _GROUP_FIELD.get(n.type)
        gv = dict(n.group).get(gf) if gf else None
        return {"path": n.path, "type": n.type, "nf": n.nf, "version": n.version,
                "group_field": gf, "group_value": gv}


# 单例（router 用）
_SERVICE: WikiService | None = None


def get_service() -> WikiService:
    global _SERVICE
    if _SERVICE is None:
        from shared.config import get_config
        cfg = get_config().get("wiki", {})
        root = Path(cfg.get("assets_root", "../assets"))
        if not root.is_absolute():
            root = Path(__file__).resolve().parent.parent / root
        idx = Path(__file__).resolve().parent / "data" / "wiki_index.json"
        _SERVICE = WikiService(root, idx)
    return _SERVICE
