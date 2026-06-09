"""Command graph API routes — placeholder."""
from fastapi import APIRouter

router = APIRouter(prefix="/api/v1/command-graph", tags=["command-graph"])


@router.get("/status")
def get_status():
    return {"status": "placeholder", "message": "Command graph module not yet implemented"}
