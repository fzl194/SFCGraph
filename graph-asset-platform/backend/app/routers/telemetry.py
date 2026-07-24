"""telemetry router：SKILL 取用频次聚合查询（受鉴权中间件保护，需 can_frontend）。"""
from fastapi import APIRouter, Query

from ..telemetry.aggregator import aggregate_stats

router = APIRouter()


@router.get("/telemetry/stats")
def telemetry_stats(days: int = Query(default=30, ge=1, le=365)):
    """返回最近 days 天的 SKILL 取用频次聚合：{total, by_type, top_ids, timeline, by_user}。"""
    return aggregate_stats(days)
