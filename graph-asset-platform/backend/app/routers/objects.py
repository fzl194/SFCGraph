"""objects router：对象列表 / 单对象 / 邻居 / 原始 md / 子图。

版本解析（spec §6.4）：
- 不带 ``version`` → 该 id **最新现存版本**（语义化最大；id 仅在旧版本时落到旧版本，不 404）。
- ``version=X`` 但 X 不在该 id 的 ``versions[]`` → 404 + ``available_versions``（spec §8.2）。
- id 完全不存在 → 404。

``id`` 含 ``@`` 与空格；FastAPI 路径参数可接收（客户端负责 URL-encode）。
"""
from typing import Optional

from fastapi import APIRouter, HTTPException, Query
from fastapi.responses import PlainTextResponse

from ..models import Edge, Object
from ..service import get_service

router = APIRouter()


# ---------- 序列化辅助 ----------

def _dump(o: Object) -> dict:
    return {
        "id": o.id,
        "type": o.type,
        "layer": o.layer,
        "scope": o.scope,
        "nf": o.nf,
        "version": o.version,
        "domain": o.domain,
        "scenario": o.scenario,
        "frontmatter": o.frontmatter,
        "body_md": o.body_md,
        "source_path": o.source_path,
    }


def _dump_edge(e: Edge) -> dict:
    return {
        "from": e.from_id,
        "from_version": e.from_version,
        "relation": e.relation,
        "to": e.to,
    }


def _resolve(id_: str, version: Optional[str]) -> Object:
    """解析对象；不存在 / 指定版本缺失 → HTTPException(404)。

    指定版本缺失时附带 ``available_versions``（spec §8.2）。
    """
    idx = get_service().index
    available = idx.versions_of(id_)
    if not available:
        raise HTTPException(status_code=404, detail=f"对象不存在: {id_}")
    obj = idx.resolve_node(id_, version)
    if obj is None:
        # id 存在但指定版本不在 versions[] → 404 + 列出可用版本
        raise HTTPException(
            status_code=404,
            detail={
                "message": f"版本不存在: {id_}@{version}",
                "available_versions": available,
            },
        )
    return obj


# ---------- /objects ----------

@router.get("/objects")
def list_objects(type: Optional[str] = None,
                 q: Optional[str] = None,
                 nf: Optional[str] = None,
                 domain: Optional[str] = None,
                 page: int = 1,
                 size: int = 50):
    """按 id 聚合列表（多版本合并为一行，versions[] 聚合）。"""
    idx = get_service().index
    # 先按 id 取一个代表节点（最新版本），再聚合 versions
    latest_per_id: dict = {}
    for (id_, _ver), obj in idx.nodes.items():
        cur = latest_per_id.get(id_)
        if cur is None or (obj.version or "") > (cur.version or ""):
            latest_per_id[id_] = obj
    rows = []
    ql = q.lower() if q else None
    for id_, obj in latest_per_id.items():
        if type and obj.type != type:
            continue
        if nf and obj.nf != nf:
            continue
        if domain and obj.domain != domain:
            continue
        if ql and ql not in id_.lower() and ql not in str(obj.frontmatter.get("name", "")).lower():
            continue
        rows.append({
            "id": id_,
            "type": obj.type,
            "layer": obj.layer,
            "nf": obj.nf,
            "domain": obj.domain,
            "name": obj.frontmatter.get("name"),
            "versions": idx.versions_of(id_),
        })
    # 稳定排序：按 type 再按 id
    rows.sort(key=lambda r: (r["type"] or "", r["id"]))
    start = (page - 1) * size
    return rows[start:start + size]


# ---------- /objects/{id} ----------

@router.get("/objects/{id_}")
def get_object(id_: str, version: Optional[str] = Query(default=None)):
    obj = _resolve(id_, version)
    idx = get_service().index
    return {
        **_dump(obj),
        "versions": idx.versions_of(obj.id),
        "out_edges": [_dump_edge(e) for e in idx.out_edges(obj.id, obj.version)],
    }


@router.get("/objects/{id_}/neighbors")
def neighbors(id_: str,
              hops: int = 1,
              version: Optional[str] = Query(default=None)):
    # hops 目前固定单跳（v1）；保留参数以兼容前端
    _ = hops
    obj = _resolve(id_, version)
    idx = get_service().index
    out = [_dump_edge(e) for e in idx.out_edges(obj.id, obj.version)]
    back = [_dump_edge(e) for e in idx.in_edges(obj.id)]
    return {"center": _dump(obj), "out": out, "in": back}


@router.get("/objects/{id_}/md", response_class=PlainTextResponse)
def get_md(id_: str, version: Optional[str] = Query(default=None)):
    obj = _resolve(id_, version)
    return PlainTextResponse(
        obj.raw_md,
        media_type="text/markdown; charset=utf-8",
    )


# ---------- /subgraph ----------

@router.get("/subgraph")
def subgraph(center: str,
             hops: int = 1,
             type: Optional[str] = None,
             version: Optional[str] = Query(default=None)):
    idx = get_service().index
    start = _resolve(center, version)
    visited: set = set()
    nodes: list = []
    edges: list = []
    # BFS：hops=0 仅中心；hops=1 中心 + 直接邻居（1 条边可达）；以此类推。
    # 每轮把 frontier 节点纳入结果 + 收集其出边目标作为下一轮 frontier；
    # 因此需要 hops+1 轮（第 0 轮纳入中心，第 1..hops 轮纳入对应跳数的邻居）。
    frontier = [(start.id, start.version)]
    for _depth in range(max(0, hops) + 1):
        nxt = []
        for cid, cver in frontier:
            if (cid, cver) in visited:
                continue
            visited.add((cid, cver))
            n = idx.node(cid, cver)
            if n is None:
                continue
            nodes.append(_dump(n))
            for e in idx.out_edges(cid, cver):
                edges.append(_dump_edge(e))
                tv = idx.latest_version_of_id(e.to)
                if tv is not None and (e.to, tv) not in visited:
                    nxt.append((e.to, tv))
        if not nxt:
            break
        frontier = nxt
    return {"nodes": nodes, "edges": edges}
