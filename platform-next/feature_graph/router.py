"""Feature graph API routes（对齐 command_graph/router.py 端点风格）。"""
from fastapi import APIRouter, Query
from fastapi.responses import FileResponse

from .service import get_service

router = APIRouter(prefix="/api/v1/feature-graph", tags=["feature-graph"])


@router.get("/stats")
def get_stats():
    return get_service().get_stats()


@router.get("/features")
def list_features(
    nf: str = Query(...), version: str = Query(...),
    search: str | None = Query(None), category: str | None = Query(None),
    page: int = Query(1, ge=1), size: int = Query(50, ge=1, le=200),
):
    return get_service().list_features(nf, version, search, category, page, size)


@router.get("/licenses")
def list_licenses(
    nf: str = Query(...), version: str = Query(...),
    search: str | None = Query(None),
    page: int = Query(1, ge=1), size: int = Query(50, ge=1, le=200),
):
    return get_service().list_licenses(nf, version, search, page, size)


@router.get("/feature")
def get_feature(nf: str = Query(...), version: str = Query(...), code: str = Query(...)):
    rec = get_service().get_feature(nf, version, code)
    return rec or {"error": "Feature not found", "code": code}


@router.get("/feature-docs")
def get_feature_docs(nf: str = Query(...), version: str = Query(...), code: str = Query(...)):
    return {"docs": get_service().get_feature_docs(nf, version, code)}


@router.get("/feature-relations")
def get_feature_relations(nf: str = Query(...), version: str = Query(...), code: str = Query(...)):
    return {"relations": get_service().get_feature_relations(nf, version, code)}


@router.get("/feature-licenses")
def get_feature_licenses(nf: str = Query(...), version: str = Query(...), code: str = Query(...)):
    return {"licenses": get_service().get_feature_licenses(nf, version, code)}


@router.get("/feature-graph")
def get_feature_graph(
    nf: str = Query(...), version: str = Query(...), code: str = Query(...),
    hops: int = Query(1, ge=1, le=3), edge_types: str | None = Query(None),
):
    types = [t.strip() for t in edge_types.split(",") if t.strip()] if edge_types else None
    return get_service().get_feature_graph(nf, version, code, hops, types)


@router.get("/license")
def get_license(nf: str = Query(...), version: str = Query(...), code: str = Query(...)):
    rec = get_service().get_license(nf, version, code)
    return rec or {"error": "License not found", "code": code}


@router.get("/license-features")
def get_license_features(nf: str = Query(...), version: str = Query(...), code: str = Query(...)):
    return {"feature_codes": get_service().get_license_features(nf, version, code)}


@router.get("/doc-content")
def get_doc_content(path: str = Query(...)):
    return {"content": get_service().get_doc_content(path), "path": path}


@router.get("/file")
def serve_file(path: str = Query(...)):
    full = get_service().resolve_doc_path(path)
    if not full:
        return {"error": "Access denied or file not found"}
    content_types = {".png": "image/png", ".jpg": "image/jpeg", ".jpeg": "image/jpeg",
                     ".gif": "image/gif", ".svg": "image/svg+xml", ".webp": "image/webp"}
    media_type = content_types.get(full.suffix.lower(), "application/octet-stream")
    return FileResponse(str(full), media_type=media_type)
