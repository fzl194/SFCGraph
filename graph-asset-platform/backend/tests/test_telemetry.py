"""telemetry 测试：recorder（新签名）+ aggregator（stats skill对象级 + activity按user）。"""
import json
from datetime import datetime, timedelta, timezone


def _use_tmp_telemetry(tmp_path, monkeypatch):
    f = tmp_path / "access.jsonl"
    import app.config as cfg
    monkeypatch.setattr(cfg, "TELEMETRY_FILE", f)
    return f


def _now():
    return datetime.now(timezone.utc).isoformat()


def _seed(f, rows):
    with open(f, "w", encoding="utf-8") as out:
        for r in rows:
            out.write(json.dumps(r, ensure_ascii=False) + "\n")


# ---------- recorder ----------

def test_record_appends_with_new_fields(tmp_path, monkeypatch):
    f = _use_tmp_telemetry(tmp_path, monkeypatch)
    from app.telemetry.recorder import record
    record("/md", "F@1", "Feature", user="sa", caller="skill", level="object")
    rec = json.loads(f.read_text(encoding="utf-8").strip())
    assert rec["user"] == "sa" and rec["caller"] == "skill" and rec["level"] == "object"
    assert rec["endpoint"] == "/md" and rec["id"] == "F@1" and rec["type"] == "Feature"


def test_record_makes_parent_dir(tmp_path, monkeypatch):
    f = tmp_path / "nested" / "deep" / "access.jsonl"
    import app.config as cfg
    monkeypatch.setattr(cfg, "TELEMETRY_FILE", f)
    from app.telemetry.recorder import record
    record("/domains", "BD@x", "BusinessDomain", user="sa", caller="skill", level="object")
    assert f.exists()


def test_record_swallows_failure(tmp_path, monkeypatch):
    import app.config as cfg
    monkeypatch.setattr(cfg, "TELEMETRY_FILE", tmp_path)  # 目录 → open 抛
    from app.telemetry.recorder import record
    record("/md", "x", "y", user="u", caller="c", level="object")  # 不抛


# ---------- aggregator ----------

def test_aggregate_stats_skill_objects_only(tmp_path, monkeypatch):
    f = _use_tmp_telemetry(tmp_path, monkeypatch)
    _seed(f, [
        {"ts": _now(), "user": "sk1", "caller": "skill", "endpoint": "/md", "id": "F@1", "type": "Feature", "level": "object"},
        {"ts": _now(), "user": "sk1", "caller": "skill", "endpoint": "/md", "id": "F@1", "type": "Feature", "level": "object"},
        {"ts": _now(), "user": "sk2", "caller": "skill", "endpoint": "/domains", "id": "BD@x", "type": "BusinessDomain", "level": "object"},
        {"ts": _now(), "user": "fe", "caller": "web", "endpoint": "/md", "id": "F@1", "type": "Feature", "level": "object"},  # web 不计
        {"ts": _now(), "user": "fe", "caller": "web", "endpoint": "/api/v1/objects/F@1/md", "id": "", "type": "", "level": "request"},  # request 不计
    ])
    from app.telemetry.aggregator import aggregate_stats
    r = aggregate_stats(days=30)
    assert r["total"] == 3
    assert r["by_type"]["Feature"] == 2
    assert r["by_user"] == {"sk1": 2, "sk2": 1}
    assert r["top_ids"][0]["id"] == "F@1"


def test_aggregate_stats_days_filter(tmp_path, monkeypatch):
    old = (datetime.now(timezone.utc) - timedelta(days=40)).isoformat()
    new = (datetime.now(timezone.utc) - timedelta(days=1)).isoformat()
    f = _use_tmp_telemetry(tmp_path, monkeypatch)
    _seed(f, [
        {"ts": old, "user": "sk", "caller": "skill", "endpoint": "/md", "id": "OLD", "type": "Feature", "level": "object"},
        {"ts": new, "user": "sk", "caller": "skill", "endpoint": "/md", "id": "NEW", "type": "Feature", "level": "object"},
    ])
    from app.telemetry.aggregator import aggregate_stats
    r = aggregate_stats(days=10)
    assert r["total"] == 1
    assert r["top_ids"][0]["id"] == "NEW"


def test_aggregate_activity_by_user(tmp_path, monkeypatch):
    f = _use_tmp_telemetry(tmp_path, monkeypatch)
    _seed(f, [
        {"ts": _now(), "user": "fe", "caller": "web", "endpoint": "/api/v1/objects/F@1/md", "level": "request"},
        {"ts": _now(), "user": "fe", "caller": "web", "endpoint": "/api/v1/stats", "level": "request"},
        {"ts": _now(), "user": "fe", "caller": "web", "endpoint": "/md", "id": "F@1", "type": "Feature", "level": "object"},  # 对象级，应被排除
        {"ts": _now(), "user": "other", "caller": "web", "endpoint": "/api/v1/objects/F@2/md", "level": "request"},
    ])
    from app.telemetry.aggregator import aggregate_activity
    r = aggregate_activity("fe", days=30)
    assert len(r) == 2  # fe 的两条 request（object 级被排除）
    assert all(item["endpoint"] for item in r)


def test_aggregate_stats_by_operator(tmp_path, monkeypatch):
    """by_operator：SKILL 调用按工号追溯那批人。"""
    f = _use_tmp_telemetry(tmp_path, monkeypatch)
    _seed(f, [
        {"ts": _now(), "user": "Agent平台A", "operator": "EMP001", "caller": "skill", "endpoint": "/md", "id": "F@1", "type": "Feature", "level": "object"},
        {"ts": _now(), "user": "Agent平台A", "operator": "EMP001", "caller": "skill", "endpoint": "/md", "id": "F@2", "type": "Feature", "level": "object"},
        {"ts": _now(), "user": "Agent平台A", "operator": "EMP002", "caller": "skill", "endpoint": "/domains", "id": "BD@x", "type": "BusinessDomain", "level": "object"},
        {"ts": _now(), "user": "fe", "operator": "", "caller": "web", "endpoint": "/md", "id": "F@1", "type": "Feature", "level": "object"},  # web 不计
    ])
    from app.telemetry.aggregator import aggregate_stats
    r = aggregate_stats(days=30)
    assert r["by_operator"] == {"EMP001": 2, "EMP002": 1}
    assert r["by_user"] == {"Agent平台A": 3}
