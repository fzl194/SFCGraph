"""assets router：bundle 导入（异步）/ 导出 / 导入记录 / 统计。

- ``POST /import``         : multipart zip → 立即 202 + job_id；后台 ``_process_import``
                             解压→归类→合并→重建→更新 job→追加 ``_imports.log``。
- ``GET  /import/jobs``    : 活 job 列表（内存，processing/done/failed）。
- ``GET  /import/jobs/{id}``: 单 job 状态（轮询用）。
- ``GET  /imports``        : 历史导入日志（一行一条 JSON，完成时落盘）。
- ``GET  /export``         : 流式 zip（可选 ``nf/version/domain/scenario`` 过滤）。
- ``GET  /stats``          : 按 UI 层聚合的对象/边统计。

注：``/imports``=历史持久化（与旧 ImportHistoryItem 字段一致，兼容），
``/import/jobs``=实时活状态（内存）。两个端点共存。
"""
import io
import json
from collections import Counter, defaultdict

from fastapi import APIRouter, BackgroundTasks, File, HTTPException, UploadFile
from fastapi.responses import StreamingResponse

from ..bundle import export_bundle, import_bundle
from .. import config as _config
from ..jobs import create_job, get_job, list_jobs, update_job
from ..service import get_service, import_lock
from ..ui_layers import ui_layer_of

router = APIRouter()


def _log_path():
    # 运行时从 config 取（测试 monkeypatch config.DATA_DIR 后生效）
    return _config.DATA_DIR / "_imports.log"


def _append_import_log(record: dict) -> None:
    """追加一条导入记录到 ``_imports.log``（一行 JSON）。

    抽出来便于 ``_process_import`` 完成后写完整记录，保持 ``GET /imports`` 历史
    兼容（字段与旧 ImportHistoryItem 一致）。
    """
    log_path = _log_path()
    log_path.parent.mkdir(parents=True, exist_ok=True)
    with log_path.open("a", encoding="utf-8") as f:
        f.write(json.dumps(record, ensure_ascii=False) + "\n")


def _counts(svc) -> dict:
    c: Counter = Counter()
    for obj in svc.index.nodes.values():
        c[obj.type] += 1
    return dict(c)


def _edge_count(svc) -> int:
    return sum(len(v) for v in svc.index.out.values())


def _process_import(job_id: str, zip_bytes: bytes) -> None:
    """后台导入：解压→归类→合并→重建→更新 job + 写历史日志。

    用模块级 ``import_lock`` 串行化（导入+rebuild 必须原子化，否则读 API 可能
    看到半导入状态）。任意失败不卡死 job——记 failed + error。
    """
    svc = get_service()
    try:
        with import_lock:
            res = import_bundle(zip_bytes, svc.store, svc.registry)
            svc.rebuild()  # 读 API 必须看到最新数据
        update_job(
            job_id, status="done",
            added=res.added, updated=res.updated,
            skipped=res.skipped, warnings=res.warnings,
        )
        # 兼容 GET /imports：完成后写一条完整历史记录
        _append_import_log({
            "added": res.added, "updated": res.updated,
            "skipped": res.skipped, "warnings_n": len(res.warnings),
        })
    except Exception as ex:  # noqa: BLE001 任意失败不卡死 job
        update_job(job_id, status="failed", error=str(ex))


@router.post("/import", status_code=202)
async def do_import(file: UploadFile = File(...),
                    bg: BackgroundTasks = BackgroundTasks()):
    """异步导入：立即 202 + job_id，后台处理。

    FastAPI TestClient（httpx）默认会等 BackgroundTasks 完成再返回响应，
    故测试里 202 响应到达时 job 通常已 done；生产是真正异步。
    """
    data = await file.read()
    job = create_job()
    bg.add_task(_process_import, job.job_id, data)
    return {"job_id": job.job_id, "status": "processing"}


@router.get("/import/jobs")
def jobs_list():
    """活 job 列表（内存，按 started_at 倒序，最多 100）。"""
    return [j.summary() for j in list_jobs()]


@router.get("/import/jobs/{job_id}")
def job_detail(job_id: str):
    j = get_job(job_id)
    if j is None:
        raise HTTPException(status_code=404, detail="job 不存在")
    return j.summary()


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


def _dd_to_plain(d):
    """把 defaultdict 嵌套结构递归转成普通 dict（JSON 可序列化）。"""
    if isinstance(d, dict):
        return {k: _dd_to_plain(v) for k, v in d.items()}
    return d


@router.get("/stats")
def stats():
    """统计：按 UI 层聚合 node 数（每个 md 实例；多版本计多次，与旧口径一致）。"""
    svc = get_service()
    idx = svc.index

    per_layer: defaultdict = defaultdict(int)
    per_layer_per_nf: defaultdict = defaultdict(lambda: defaultdict(int))
    per_layer_per_nf_per_version: defaultdict = defaultdict(
        lambda: defaultdict(lambda: defaultdict(int)))
    per_domain: defaultdict = defaultdict(int)
    per_domain_scenario: defaultdict = defaultdict(lambda: defaultdict(int))

    for obj in idx.nodes.values():
        ul = ui_layer_of(obj.layer)
        per_layer[ul] += 1
        if obj.nf:
            per_layer_per_nf[ul][obj.nf] += 1
            if obj.version:
                per_layer_per_nf_per_version[ul][obj.nf][obj.version] += 1
        if obj.domain:
            per_domain[obj.domain] += 1
            if obj.scenario:
                per_domain_scenario[obj.domain][obj.scenario] += 1

    return {
        "object_counts_by_type": _counts(svc),
        "edge_count": _edge_count(svc),
        "nfs": sorted(idx.nfs()),
        "versions_per_nf": idx.versions_per_nf(),
        "per_layer": dict(per_layer),
        "per_layer_per_nf": _dd_to_plain(dict(per_layer_per_nf)),
        "per_layer_per_nf_per_version": _dd_to_plain(
            {k: dict(v) for k, v in per_layer_per_nf_per_version.items()}),
        "per_domain": dict(per_domain),
        "per_domain_scenario": _dd_to_plain(dict(per_domain_scenario)),
    }
