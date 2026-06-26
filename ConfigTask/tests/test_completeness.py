# ConfigTask/tests/test_completeness.py
"""完整性核查：原文档的所有命令都出现在且仅出现在一个 candidate 中。"""
from builder.verify.completeness import verify_completeness


def test_all_commands_covered():
    doc = {"steps": [{"commands": ["ADD URR", "ADD RULE"]}]}
    candidates = [{"commands": ["ADD URR"]}, {"commands": ["ADD RULE"]}]
    assert verify_completeness(doc, candidates) == []


def test_missing_command():
    doc = {"steps": [{"commands": ["ADD URR", "ADD RULE", "ADD FILTER"]}]}
    candidates = [{"commands": ["ADD URR"]}, {"commands": ["ADD RULE"]}]
    errors = verify_completeness(doc, candidates)
    assert len(errors) == 1
    assert "ADD FILTER" in errors[0]


def test_duplicate_command():
    doc = {"steps": [{"commands": ["ADD URR", "ADD RULE"]}]}
    candidates = [{"commands": ["ADD URR", "ADD RULE"]}, {"commands": ["ADD URR"]}]
    errors = verify_completeness(doc, candidates)
    assert any("重复" in e for e in errors)


def test_empty_doc():
    doc = {"steps": [{"commands": []}]}
    assert verify_completeness(doc, []) == []
