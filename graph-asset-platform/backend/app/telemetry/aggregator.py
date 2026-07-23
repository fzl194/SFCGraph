"""打点聚合器：流式读 jsonl，聚合三维（type / top-N / 时间）。"""
import json
from collections import Counter
from datetime import datetime, timedelta, timezone
from pathlib import Path

from .. import config  # 运行时读 config.TELEMETRY_FILE，便于测试 monkeypatch（与 auth.py / recorder.py 同模式）


def aggregate(days: int = 30) -> dict:
    """聚合最近 days 天的访问记录，返回 {total, by_type, top_ids, timeline}。"""
    by_type: Counter = Counter()
    by_id: Counter = Counter()
    id_type: dict = {}
    by_date: Counter = Counter()

    cutoff = None
    if days and days > 0:
        cutoff = datetime.now(timezone.utc) - timedelta(days=days)

    path = Path(config.TELEMETRY_FILE)
    if path.exists():
        with open(path, "r", encoding="utf-8") as f:
            for raw in f:
                raw = raw.strip()
                if not raw:
                    continue
                try:
                    rec = json.loads(raw)
                except json.JSONDecodeError:
                    continue
                ts = _parse_ts(rec.get("ts", ""))
                if cutoff and ts and ts < cutoff:
                    continue
                type_ = rec.get("type") or "unknown"
                id_ = rec.get("id") or "unknown"
                by_type[type_] += 1
                by_id[id_] += 1
                id_type[id_] = type_
                if ts:
                    by_date[ts.strftime("%Y-%m-%d")] += 1

    top_ids = [
        {"id": i, "type": id_type.get(i, "unknown"), "count": c}
        for i, c in by_id.most_common(20)
    ]
    timeline = [{"date": d, "count": c} for d, c in sorted(by_date.items())]
    return {
        "total": sum(by_type.values()),
        "by_type": dict(by_type),
        "top_ids": top_ids,
        "timeline": timeline,
    }


def _parse_ts(s: str):
    if not s:
        return None
    try:
        return datetime.fromisoformat(s.replace("Z", "+00:00"))
    except ValueError:
        return None
