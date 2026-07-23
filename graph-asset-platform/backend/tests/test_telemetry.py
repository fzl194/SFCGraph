"""telemetry 测试：recorder 追加 / aggregator 聚合 / 接口。"""
import json
from pathlib import Path


def _use_tmp_telemetry(tmp_path, monkeypatch):
    """把 config.TELEMETRY_FILE 指到临时目录，隔离测试。"""
    f = tmp_path / "access.jsonl"
    import app.config as cfg
    monkeypatch.setattr(cfg, "TELEMETRY_FILE", f)
    return f


def test_record_appends_jsonl_line(tmp_path, monkeypatch):
    f = _use_tmp_telemetry(tmp_path, monkeypatch)
    from app.telemetry.recorder import record
    record("/md", "UDG@Feature@F-1", "Feature")
    record("/md", "UDG@Feature@F-1", "Feature")
    lines = f.read_text(encoding="utf-8").strip().split("\n")
    assert len(lines) == 2
    rec = json.loads(lines[0])
    assert rec["endpoint"] == "/md"
    assert rec["id"] == "UDG@Feature@F-1"
    assert rec["type"] == "Feature"
    assert "ts" in rec


def test_record_makes_parent_dir(tmp_path, monkeypatch):
    f = tmp_path / "nested" / "deep" / "access.jsonl"
    import app.config as cfg
    monkeypatch.setattr(cfg, "TELEMETRY_FILE", f)
    from app.telemetry.recorder import record
    record("/domains", "BusinessDomain@demo", "BusinessDomain")
    assert f.exists()


def test_record_swallows_failure(tmp_path, monkeypatch):
    """打点失败绝不抛（观测用，不阻断业务）。"""
    import app.config as cfg
    # TELEMETRY_FILE 指到已存在目录 → open(dir, 'a') 跨平台必抛（Windows/Linux 均可复现）
    monkeypatch.setattr(cfg, "TELEMETRY_FILE", tmp_path)
    from app.telemetry.recorder import record
    record("/md", "x", "y")  # 不抛即通过


def _seed(f, rows):
    """直接写若干行 jsonl 作为打点种子。"""
    with open(f, "w", encoding="utf-8") as out:
        for r in rows:
            out.write(json.dumps(r, ensure_ascii=False) + "\n")


def test_aggregate_three_dimensions(tmp_path, monkeypatch):
    """三维聚合：total/by_type/top_ids/timeline。动态种子（now），不依赖固定日期。"""
    from datetime import datetime, timezone
    now_ts = datetime.now(timezone.utc).isoformat()
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    f = _use_tmp_telemetry(tmp_path, monkeypatch)
    _seed(f, [
        {"ts": now_ts, "endpoint": "/md", "id": "F@1", "type": "Feature"},
        {"ts": now_ts, "endpoint": "/md", "id": "F@1", "type": "Feature"},
        {"ts": now_ts, "endpoint": "/md", "id": "C@2", "type": "MMLCommand"},
        {"ts": now_ts, "endpoint": "/domains", "id": "BD@x", "type": "BusinessDomain"},
    ])
    from app.telemetry.aggregator import aggregate
    r = aggregate(days=30)
    assert r["total"] == 4
    assert r["by_type"]["Feature"] == 2
    assert r["by_type"]["MMLCommand"] == 1
    assert r["top_ids"][0] == {"id": "F@1", "type": "Feature", "count": 2}
    assert r["timeline"] == [{"date": today, "count": 4}]


def test_aggregate_days_filter(tmp_path, monkeypatch):
    """老记录（now-40d）被 days=10 过滤；新记录（now-1d）保留。动态种子，无日期漂移 flaky。"""
    from datetime import datetime, timedelta, timezone
    now = datetime.now(timezone.utc)
    old_ts = (now - timedelta(days=40)).isoformat()
    new_ts = (now - timedelta(days=1)).isoformat()
    f = _use_tmp_telemetry(tmp_path, monkeypatch)
    _seed(f, [
        {"ts": old_ts, "endpoint": "/md", "id": "OLD", "type": "Feature"},
        {"ts": new_ts, "endpoint": "/md", "id": "NEW", "type": "Feature"},
    ])
    from app.telemetry.aggregator import aggregate
    r = aggregate(days=10)
    assert r["total"] == 1  # 只剩 NEW
    assert r["top_ids"][0]["id"] == "NEW"
