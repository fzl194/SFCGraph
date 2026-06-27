"""core/io.py 测试。"""
import json

from builder.core.io import load_jsonl, write_jsonl


def test_write_then_load_roundtrip(tmp_path):
    items = [{"id": "a", "v": 1}, {"id": "b", "v": 2}]
    out = tmp_path / "x.jsonl"
    write_jsonl(out, items)
    assert [json.loads(l) for l in out.read_text(encoding="utf-8").splitlines()] == items
    assert load_jsonl(out) == items


def test_load_missing_returns_empty(tmp_path):
    assert load_jsonl(tmp_path / "nope.jsonl") == []


def test_write_creates_parent_dirs(tmp_path):
    out = tmp_path / "a" / "b" / "c.jsonl"
    write_jsonl(out, [{"id": "x"}])
    assert out.exists()
