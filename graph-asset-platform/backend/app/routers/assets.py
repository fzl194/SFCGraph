"""assets router：bundle 导入 / 导出 / 导入记录 / 统计。

- ``POST /import``  : multipart zip → import_bundle → rebuild → 追加 ``_imports.log``
                      → 返回 ``{added, updated, skipped, warnings, counts}``。
- ``GET  /imports`` : 上传记录列表。
- ``GET  /export``  : 流式 zip（可选 ``nf/version/domain/scenario`` 过滤）。
- ``GET  /stats``   : ``{object_counts_by_type, edge_count, nfs, versions_per_nf}``。

``counts`` 与 ``/stats`` 一致，便于前端导入后直接刷新概览。
"""
import io
import json
from collections import Counter

from fastapi import APIRouter, File, UploadFile
from fastapi.responses import StreamingResponse

from ..bundle import export_bundle, import_bundle
from .. import config as _config
from ..service import get_service

router = APIRouter()


def _log_path():
    # 运行时从 config 取（测试 monkeypatch config.DATA_DIR 后生效）
    return _config.DATA_DIR / "_imports.log"


def _counts(svc) -> dict:
    c: Counter = Counter()
    for obj in svc.index.nodes.values():
        c[obj.type] += 1
    return dict(c)


def _edge_count(svc) -> int:
    return sum(len(v) for v in svc.index.out.values())


@router.post("/import")
async def do_import(file: UploadFile = File(...)):
    data = await file.read()
    svc = get_service()
    res = import_bundle(data, svc.store, svc.registry)
    svc.rebuild()  # 读 API 必须看到最新数据
    # 追加导入记录（一行一条 JSON，便于 tail / 后续聚合）
    log_path = _log_path()
    log_path.parent.mkdir(parents=True, exist_ok=True)
    with log_path.open("a", encoding="utf-8") as f:
        f.write(json.dumps(
            {"added": res.added, "updated": res.updated,
             "skipped": res.skipped, "warnings_n": len(res.warnings)},
            ensure_ascii=False,
        ) + "\n")
    return {
        "added": res.added,
        "updated": res.updated,
        "skipped": res.skipped,
        "warnings": res.warnings,
        "counts": _counts(svc),
    }


@router.get("/imports")
def imports_log():
    log_path = _log_path()
    if not log_path.exists():
        return []
    rows = []
    for line in log_path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            rows.append(json.loads(line))
        except json.JSONDecodeError:
            continue
    return rows


@router.get("/export")
def do_export(nf: str | None = None,
              version: str | None = None,
              domain: str | None = None,
              scenario: str | None = None):
    svc = get_service()
    z = export_bundle(svc.store, nf=nf, version=version,
                      domain=domain, scenario=scenario)
    return StreamingResponse(
        io.BytesIO(z),
        media_type="application/zip",
        headers={"Content-Disposition": "attachment; filename=assets.zip"},
    )


@router.get("/stats")
def stats():
    svc = get_service()
    return {
        "object_counts_by_type": _counts(svc),
        "edge_count": _edge_count(svc),
        "nfs": sorted(svc.index.nfs()),
        "versions_per_nf": svc.index.versions_per_nf(),
    }


# 业务层类型（scope=cross, layer=Business）—— 概览图以这些为根节点。
_BUSINESS_TYPES = ("BusinessDomain", "NetworkScenario", "ConfigurationSolution")


@router.get("/overview")
def overview():
    """业务层概览图（GraphView 默认渲染，无需指定对象）。

    优先返回业务树：nodes = 所有 scope=cross 的对象（BD/NS/CS），
    edges = 这些对象的出向边（构成 NS→CS / BD→NS 等业务结构）。
    业务层为空时退化为层摘要：nodes = 各 layer（带 object_counts），无 edges。
    payload 与 subgraph 同形：``{nodes:[{id,type,label}], edges:[{from,relation,to}]}``。
    """
    svc = get_service()
    idx = svc.index

    business_nodes = []
    seen_ids = set()
    for (id_, _ver), obj in idx.nodes.items():
        if obj.scope != "cross":
            continue
        if id_ in seen_ids:
            continue
        seen_ids.add(id_)
        label = _node_label(obj.frontmatter, id_)
        business_nodes.append({"id": id_, "type": obj.type, "label": label})

    if business_nodes:
        edges = []
        for (id_, _ver), obj in idx.nodes.items():
            if obj.scope != "cross":
                continue
            for e in idx.out_edges(id_, obj.version):
                edges.append({
                    "from": e.from_id,
                    "relation": e.relation or "",
                    "to": e.to,
                })
        return {"nodes": business_nodes, "edges": _dedup_edges(edges)}

    # 退化：业务层为空 → 返回层摘要
    layer_counts: Counter = Counter()
    for obj in idx.nodes.values():
        if obj.layer:
            layer_counts[obj.layer] += 1
    layer_nodes = [
        {"id": layer, "type": "Layer", "label": layer,
         "object_count": count}
        for layer, count in sorted(layer_counts.items())
    ]
    return {"nodes": layer_nodes, "edges": []}


def _node_label(fm: dict, fallback_id: str) -> str:
    """优先用 name_zh/name frontmatter 字段；否则用 id 末段。"""
    for key in ("name_zh", "name", "title"):
        v = fm.get(key)
        if isinstance(v, str) and v.strip():
            return v.strip()
    parts = fallback_id.split("@")
    return parts[-1] if parts else fallback_id


def _dedup_edges(edges: list) -> list:
    """同 from+relation+to 去重（多版本/重复索引）。"""
    seen = set()
    out = []
    for e in edges:
        k = (e["from"], e["relation"], e["to"])
        if k in seen:
            continue
        seen.add(k)
        out.append(e)
    return out


@router.get("/browse")
def browse(path: str = "", q: str | None = None, limit: int = 200, offset: int = 0):
    """按目录懒加载资产树（治前端性能：展开某层只读该层子项，不再一次拉全量）。

    - ``path``：assets 内相对目录（""=根，如 "Command/UDG/20.15.2"）。
    - 返回该目录直接子目录 + 分页后的文件；文件 ``id`` 由文件名派生（去 ``.md``）。
    - 隐藏 ``_`` 前缀内部项（``_index/``、``_imports.log``）。
    - ``q``：文件名子串过滤；``limit/offset``：文件分页（大版本目录可有数千文件）。
    """
    svc = get_service()
    dirs, files = svc.store.list_dir(path)
    dirs = [d for d in dirs if not d.startswith("_")]
    files = [f for f in files if not f.startswith("_")]
    if q:
        ql = q.lower()
        files = [f for f in files if ql in f.lower()]
    total = len(files)
    page = files[offset:offset + limit]
    file_objs = [
        {"name": f, "id": f.removesuffix(".md") if f.endswith(".md") else f}
        for f in page
    ]
    return {
        "path": path,
        "dirs": dirs,
        "files": file_objs,
        "total_files": total,
        "offset": offset,
        "limit": limit,
    }
