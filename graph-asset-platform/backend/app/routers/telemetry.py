"""telemetry router：取用频次聚合查询（受鉴权中间件保护）。"""
from fastapi import APIRouter, Query

from ..telemetry.aggregator import aggregate

router = APIRouter()


@router.get("/telemetry/stats")
def telemetry_stats(days: int = Query(default=30, ge=1, le=365)):
    """返回最近 days 天的取用频次聚合：{total, by_type, top_ids, timeline}。"""
    return aggregate(days)
