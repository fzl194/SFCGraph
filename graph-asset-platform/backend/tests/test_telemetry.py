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
