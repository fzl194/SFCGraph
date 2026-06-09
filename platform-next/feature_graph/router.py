"""Feature graph API routes."""
from fastapi import APIRouter, Query
from fastapi.responses import FileResponse
from pydantic import BaseModel
from .service import get_service
from .review_service import get_review_store

router = APIRouter(prefix="/api/v1/feature-graph", tags=["feature-graph"])


@router.get("/columns")
def get_columns():
    svc = get_service()
    return {"columns": svc.get_column_config()}


@router.get("/stats")
def get_stats():
    svc = get_service()
    return svc.get_stats()


@router.get("/features")
def list_features(
    product_type: str | None = Query(None),
    feature_type: str | None = Query(None),
    section: str | None = Query(None),
    search: str | None = Query(None),
    page: int = Query(1, ge=1),
    size: int = Query(50, ge=1, le=200),
):
    svc = get_service()
    return svc.list_features(
        product_type=product_type,
        feature_type=feature_type,
        section=section,
        search=search,
        page=page,
        size=size,
    )


@router.get("/features/{feature_id}")
def get_feature(feature_id: str, product_type: str | None = Query(None)):
    svc = get_service()
    feature = svc.get_feature(feature_id, product_type=product_type)
    if not feature:
        return {"error": "Feature not found", "feature_id": feature_id}
    return feature


@router.get("/features/{feature_id}/docs")
def get_feature_docs(feature_id: str):
    svc = get_service()
    return {"docs": svc.get_feature_docs(feature_id)}


@router.get("/features/{feature_id}/dependencies")
def get_feature_deps(feature_id: str):
    svc = get_service()
    return {"dependencies": svc.get_feature_deps(feature_id)}


@router.get("/features/{feature_id}/licenses")
def get_feature_licenses(feature_id: str):
    svc = get_service()
    return {"licenses": svc.get_feature_licenses(feature_id)}


@router.get("/dependencies")
def get_all_dependencies(dependency_type: str | None = Query(None)):
    svc = get_service()
    return {"dependencies": svc.get_all_dependencies(dependency_type)}


@router.get("/licenses")
def get_all_licenses():
    svc = get_service()
    return {"licenses": svc.get_all_licenses()}


@router.get("/doc-content")
def get_doc_content(path: str = Query(..., description="Relative path to md file")):
    svc = get_service()
    content = svc.get_doc_content(path)
    return {"content": content, "path": path}


@router.get("/file")
def serve_file(path: str = Query(..., description="Relative path to file")):
    """Serve a static file (image, etc.) from doc_root."""
    svc = get_service()
    full_path = svc.resolve_doc_path(path)
    if not full_path:
        return {"error": "Access denied or file not found"}
    # Determine content type from extension
    suffix = full_path.suffix.lower()
    content_types = {
        ".png": "image/png",
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".gif": "image/gif",
        ".svg": "image/svg+xml",
        ".webp": "image/webp",
        ".pdf": "application/pdf",
    }
    media_type = content_types.get(suffix, "application/octet-stream")
    return FileResponse(str(full_path), media_type=media_type)


# --- Review endpoints ---

class ReviewRequest(BaseModel):
    item_type: str   # "dependency" | "license"
    item_id: str
    comment: str = ""

class BulkReviewRequest(BaseModel):
    item_type: str
    item_ids: list[str]


@router.post("/review/accept")
def review_accept(req: ReviewRequest):
    store = get_review_store()
    item = store.accept(req.item_type, req.item_id, req.comment)
    return {"status": item.status.value, "item_id": item.item_id}


@router.post("/review/reject")
def review_reject(req: ReviewRequest):
    store = get_review_store()
    item = store.reject(req.item_type, req.item_id, req.comment)
    return {"status": item.status.value, "item_id": item.item_id}


@router.post("/review/reset")
def review_reset(req: ReviewRequest):
    store = get_review_store()
    item = store.reset(req.item_type, req.item_id)
    return {"status": item.status.value, "item_id": item.item_id}


@router.get("/review/bulk")
def review_bulk(
    item_type: str = Query(...),
    item_ids: str = Query(..., description="Comma-separated item IDs"),
):
    store = get_review_store()
    ids = [i.strip() for i in item_ids.split(",") if i.strip()]
    return {"statuses": store.bulk_get(item_type, ids)}


@router.get("/review/all")
def review_all(item_type: str | None = Query(None)):
    store = get_review_store()
    return {"reviews": store.get_all(item_type)}
