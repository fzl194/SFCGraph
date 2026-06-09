"""Business graph API routes — placeholder."""
from fastapi import APIRouter

router = APIRouter(prefix="/api/v1/business-graph", tags=["business-graph"])


@router.get("/status")
def get_status():
    return {"status": "placeholder", "message": "Business graph module not yet implemented"}
