"""打点聚合：stats（扫 objects.jsonl，SKILL 取用，按小时）+ activity（扫 requests.jsonl，用户轨迹）。"""
import json
from collections import Counter
from datetime import datetime, timedelta, timezone
from pathlib import Path

from .. import config

_STATS_ENDPOINTS = {"/md", "/domains"}


def _iter_records(path: Path):
    if not path.exists():
        return
    with open(path, "r", encoding="utf-8") as f:
        for raw in f:
            raw = raw.strip()
            if not raw:
                continue
            try:
                yield json.loads(raw)
            except json.JSONDecodeError:
                continue


def _parse_ts(s):
    if not s:
        return None
    try:
        return datetime.fromisoformat(s.replace("Z", "+00:00"))
    except ValueError:
        return None


def aggregate_stats(days: int = 30) -> dict:
    """扫 objects.jsonl：只 caller=skill + endpoint∈{/md,/domains}。timeline 按小时（当天内波动可见）。"""
    cutoff = datetime.now(timezone.utc) - timedelta(days=days) if days > 0 else None
    by_type, by_id, id_type, by_hour, by_user, by_operator = (
        Counter(), Counter(), {}, Counter(), Counter(), Counter()
    )
    for rec in _iter_records(Path(config.TELEMETRY_OBJECTS_FILE)):
        if rec.get("level") != "object" or rec.get("caller") != "skill":
            continue
        if rec.get("endpoint") not in _STATS_ENDPOINTS:
            continue
        ts = _parse_ts(rec.get("ts", ""))
        if cutoff and ts and ts < cutoff:
            continue
        t, i, u = rec.get("type") or "?", rec.get("id") or "?", rec.get("user") or "?"
        by_type[t] += 1
        by_id[i] += 1
        id_type[i] = t
        by_user[u] += 1
        op = rec.get("operator") or ""
        if op:
            by_operator[op] += 1
        if ts:
            by_hour[ts.strftime("%m-%d %H:00")] += 1  # 按小时（当天内多次取用可见波动）
    timeline = [{"date": d, "count": c} for d, c in sorted(by_hour.items())]
    return {
        "total": sum(by_type.values()),
        "by_type": dict(by_type),
        "top_ids": [{"id": i, "type": id_type.get(i, "?"), "count": c} for i, c in by_id.most_common(20)],
        "timeline": timeline,
        "by_user": dict(by_user),
        "by_operator": dict(by_operator),
    }


def aggregate_activity(username: str, days: int = 30) -> list:
    """扫 requests.jsonl：某 user 的 request 级轨迹，按时间倒序。"""
    cutoff = datetime.now(timezone.utc) - timedelta(days=days) if days > 0 else None
    rows = []
    for rec in _iter_records(Path(config.TELEMETRY_REQUESTS_FILE)):
        if rec.get("user") != username:
            continue
        if rec.get("level") != "request":
            continue
        ts = _parse_ts(rec.get("ts", ""))
        if cutoff and ts and ts < cutoff:
            continue
        rows.append({
            "ts": rec.get("ts", ""),
            "endpoint": rec.get("endpoint", ""),
            "caller": rec.get("caller", ""),
            "operator": rec.get("operator", ""),
        })
    rows.sort(key=lambda r: r["ts"], reverse=True)
    return rows
