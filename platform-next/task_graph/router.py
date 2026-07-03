"""ConfigTask (动态任务层) API routes."""
from fastapi import APIRouter, Query

from .service import get_service

router = APIRouter(prefix="/api/v1/task-graph", tags=["task-graph"])


@router.get("/stats")
def get_stats():
    return get_service().get_stats()


@router.get("/tasks")
def list_tasks(
    nf: str | None = Query(None),
    version: str | None = Query(None),
    layer: str | None = Query(None, description="atom|compound|feature|solution|generalized"),
    search: str | None = Query(None),
    page: int = Query(1, ge=1),
    size: int = Query(50, ge=1, le=200),
):
    return get_service().list_tasks(nf=nf, version=version, layer=layer,
                                    search=search, page=page, size=size)


@router.get("/task")
def get_task(
    nf: str = Query(...),
    version: str = Query(...),
    task_id: str = Query(..., description="短 id 如 2-00001 或完整 id"),
):
    t = get_service().get_task(nf, version, task_id)
    if not t:
        return {"error": "Task not found", "nf": nf, "version": version, "task_id": task_id}
    return t


@router.get("/task-tree")
def get_task_tree(
    task_id: str = Query(..., description="短 id 或完整 id"),
):
    return get_service().get_task_tree(task_id)
