# ConfigTask/tests/test_contiguity.py
"""连续性核查：step_range 覆盖 [1, N] 无重叠无缺口。"""
from builder.verify.contiguity import verify_contiguity


def test_full_coverage():
    assert verify_contiguity([{"step_range": [1, 2]}, {"step_range": [3, 5]}], 5) == []


def test_gap():
    errors = verify_contiguity([{"step_range": [1, 2]}, {"step_range": [4, 5]}], 5)
    assert any("3" in e for e in errors)


def test_overlap():
    errors = verify_contiguity([{"step_range": [1, 2]}, {"step_range": [2, 5]}], 5)
    assert any("重叠" in e for e in errors)


def test_single_candidate():
    assert verify_contiguity([{"step_range": [1, 11]}], 11) == []
