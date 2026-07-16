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
