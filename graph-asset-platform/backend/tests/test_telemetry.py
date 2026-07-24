"""telemetry 测试：recorder（按 level 写不同文件）+ aggregator（stats 扫 objects 按小时 / activity 扫 requests）。"""
import json
from datetime import datetime, timedelta, timezone


def _use_tmp_telemetry(tmp_path, monkeypatch):
    """两文件指到 tmp，返回 {'object': path, 'request': path}。"""
    import app.config as cfg
    paths = {"object": tmp_path / "objects.jsonl", "request": tmp_path / "requests.jsonl"}
    monkeypatch.setattr(cfg, "TELEMETRY_OBJECTS_FILE", paths["object"])
    monkeypatch.setattr(cfg, "TELEMETRY_REQUESTS_FILE", paths["request"])
    return paths


def _now():
    return datetime.now(timezone.utc).isoformat()


def _seed(f, rows):
    with open(f, "w", encoding="utf-8") as out:
        for r in rows:
            out.write(json.dumps(r, ensure_ascii=False) + "\n")


# ---------- recorder：按 level 分文件 ----------

def test_record_object_writes_to_objects_file(tmp_path, monkeypatch):
    paths = _use_tmp_telemetry(tmp_path, monkeypatch)
    from app.telemetry.recorder import record
    record("/md", "F@1", "Feature", user="sa", caller="skill", level="object")
    rec = json.loads(paths["object"].read_text(encoding="utf-8").strip())
    assert rec["level"] == "object"
    assert not paths["request"].exists()  # object 不写 requests


def test_record_request_writes_to_requests_file(tmp_path, monkeypatch):
    paths = _use_tmp_telemetry(tmp_path, monkeypatch)
    from app.telemetry.recorder import record
    record("/api/v1/objects/F@1/md", user="fe", caller="web", level="request")
    rec = json.loads(paths["request"].read_text(encoding="utf-8").strip())
    assert rec["level"] == "request"
    assert not paths["object"].exists()


def test_record_swallows_failure(tmp_path, monkeypatch):
    import app.config as cfg
    monkeypatch.setattr(cfg, "TELEMETRY_OBJECTS_FILE", tmp_path)  # 目录 → open 抛
    from app.telemetry.recorder import record
    record("/md", "x", "y", user="u", caller="c", level="object")  # 不抛即通过


# ---------- aggregator ----------

def test_aggregate_stats_skill_objects_only(tmp_path, monkeypatch):
    paths = _use_tmp_telemetry(tmp_path, monkeypatch)
    _seed(paths["object"], [
        {"ts": _now(), "user": "sk1", "operator": "EMP001", "caller": "skill", "endpoint": "/md", "id": "F@1", "type": "Feature", "level": "object"},
        {"ts": _now(), "user": "sk1", "operator": "EMP001", "caller": "skill", "endpoint": "/md", "id": "F@1", "type": "Feature", "level": "object"},
        {"ts": _now(), "user": "sk2", "operator": "EMP002", "caller": "skill", "endpoint": "/domains", "id": "BD@x", "type": "BusinessDomain", "level": "object"},
        {"ts": _now(), "user": "fe", "operator": "", "caller": "web", "endpoint": "/md", "id": "F@1", "type": "Feature", "level": "object"},  # web 不计
    ])
    # requests 文件有数据但不影响 stats（stats 只扫 objects）
    _seed(paths["request"], [{"ts": _now(), "user": "fe", "caller": "web", "endpoint": "/api/v1/stats", "level": "request"}])
    from app.telemetry.aggregator import aggregate_stats
    r = aggregate_stats(days=30)
    assert r["total"] == 3
    assert r["by_type"]["Feature"] == 2
    assert r["by_user"] == {"sk1": 2, "sk2": 1}
    assert r["by_operator"] == {"EMP001": 2, "EMP002": 1}
    assert r["top_ids"][0]["id"] == "F@1"
    assert all(":00" in item["date"] for item in r["timeline"])  # 按小时


def test_aggregate_stats_days_filter(tmp_path, monkeypatch):
    paths = _use_tmp_telemetry(tmp_path, monkeypatch)
    old = (datetime.now(timezone.utc) - timedelta(days=40)).isoformat()
    new = (datetime.now(timezone.utc) - timedelta(days=1)).isoformat()
    _seed(paths["object"], [
        {"ts": old, "user": "sk", "operator": "", "caller": "skill", "endpoint": "/md", "id": "OLD", "type": "Feature", "level": "object"},
        {"ts": new, "user": "sk", "operator": "", "caller": "skill", "endpoint": "/md", "id": "NEW", "type": "Feature", "level": "object"},
    ])
    from app.telemetry.aggregator import aggregate_stats
    r = aggregate_stats(days=10)
    assert r["total"] == 1
    assert r["top_ids"][0]["id"] == "NEW"


def test_aggregate_activity_scans_requests_only(tmp_path, monkeypatch):
    """activity 扫 requests.jsonl；objects.jsonl 的 fe 行不进 activity。"""
    paths = _use_tmp_telemetry(tmp_path, monkeypatch)
    _seed(paths["request"], [
        {"ts": _now(), "user": "fe", "caller": "web", "endpoint": "/api/v1/objects/F@1/md", "level": "request"},
        {"ts": _now(), "user": "fe", "caller": "web", "endpoint": "/api/v1/stats", "level": "request"},
        {"ts": _now(), "user": "other", "caller": "web", "endpoint": "/api/v1/objects/F@2/md", "level": "request"},
    ])
    _seed(paths["object"], [{"ts": _now(), "user": "fe", "caller": "web", "endpoint": "/md", "id": "F@1", "type": "Feature", "level": "object"}])
    from app.telemetry.aggregator import aggregate_activity
    r = aggregate_activity("fe", days=30)
    assert len(r) == 2  # fe 的两条 request（objects 文件的 object 级不扫）
    assert all(item["endpoint"] for item in r)
