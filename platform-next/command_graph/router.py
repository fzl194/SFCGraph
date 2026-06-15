"""Command graph API routes."""
from fastapi import APIRouter, Query
from fastapi.responses import FileResponse
from .service import get_service

router = APIRouter(prefix="/api/v1/command-graph", tags=["command-graph"])


@router.get("/stats")
def get_stats():
    svc = get_service()
    return svc.get_stats()


@router.get("/commands")
def list_commands(
    product: str | None = Query(None),
    search: str | None = Query(None),
    page: int = Query(1, ge=1),
    size: int = Query(50, ge=1, le=200),
):
    svc = get_service()
    return svc.list_commands(product=product, search=search, page=page, size=size)


@router.get("/command")
def get_command(
    product: str = Query(...),
    command_name: str = Query(...),
):
    svc = get_service()
    cmd = svc.get_command(product, command_name)
    if not cmd:
        return {"error": "Command not found", "product": product, "command_name": command_name}
    return cmd


@router.get("/command-md")
def get_command_md(
    product: str = Query(...),
    command_name: str = Query(...),
):
    svc = get_service()
    content = svc.get_command_md(product, command_name)
    return {"content": content, "product": product, "command_name": command_name}


@router.get("/doc-content")
def get_doc_content(path: str = Query(..., description="Relative path to md file")):
    svc = get_service()
    content = svc.get_doc_content(path)
    return {"content": content, "path": path}


@router.get("/file")
def serve_file(path: str = Query(..., description="Relative path to file")):
    """Serve a static file (image, etc.) from doc_root/output."""
    svc = get_service()
    full_path = svc.resolve_doc_path(path)
    if not full_path:
        return {"error": "Access denied or file not found"}
    suffix = full_path.suffix.lower()
    content_types = {
        ".png": "image/png",
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".gif": "image/gif",
        ".svg": "image/svg+xml",
        ".webp": "image/webp",
    }
    media_type = content_types.get(suffix, "application/octet-stream")
    return FileResponse(str(full_path), media_type=media_type)
