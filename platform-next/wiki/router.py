"""wiki API 路由：/api/v1/wiki/*"""
from fastapi import APIRouter, HTTPException, Query

from wiki.service import get_service

router = APIRouter(prefix="/api/v1/wiki", tags=["wiki"])


@router.get("/categories")
def categories():
    return get_service().categories()


@router.get("/group")
def group(type: str, nf: str, version: str):
    return get_service().group(type, nf, version)


@router.get("/list")
def list_objs(
    type: str, nf: str, version: str,
    group_field: str | None = None, group_value: str | None = None,
    q: str | None = None, page: int = Query(1, ge=1), size: int = Query(100, ge=1, le=500),
):
    return get_service().list_objs(type, nf, version, group_field, group_value, q, page, size)


@router.get("/neighborhood")
def neighborhood(path: str, depth: int = 1):
    nb = get_service().neighborhood(path, depth)
    if nb["center"] is None:
        raise HTTPException(status_code=404, detail="object not found")
    return nb


@router.get("/md")
def md(path: str):
    res = get_service().md(path)
    if res is None:
        raise HTTPException(status_code=404, detail="md not found")
    return res


@router.get("/search")
def search(q: str, limit: int = Query(30, ge=1, le=100)):
    return get_service().search(q, limit)
