"""测试 serve.build_assets() 返回的 by_layer / relation_targets 字段结构。

对应 spec docs/superpowers/specs/2026-07-02-review-ui-by-layer-design.md §4。
"""
import sys
from collections import Counter

sys.path.insert(0, "ConfigTask/review-ui")

from serve import build_assets  # noqa: E402


# ---------- by_layer ----------

def test_by_layer_has_4_keys():
    """by_layer 必须有 atom/compound/feature/generalized 4 个键,solution 不出现。"""
    a = build_assets()
    assert "by_layer" in a
    assert set(a["by_layer"].keys()) == {"atom", "compound", "feature", "generalized"}


def test_by_layer_each_value_is_sorted_sids():
    """by_layer 每个值是 _short id 列表,按 id 升序。"""
    a = build_assets()
    for layer, sids in a["by_layer"].items():
        assert isinstance(sids, list)
        assert sids == sorted(sids), f"{layer} 未按 id 升序: {sids[:5]}..."
        for sid in sids:
            # 形如 "0-00001" / "1-00012" / "2-00083" / "4-00001"
            assert sid.split("-")[0].isdigit(), f"{layer} 含非法 sid: {sid}"


def test_by_layer_counts_match():
    """by_layer 计数应等于对应 task_layer 的 task 数。"""
    a = build_assets()
    layer_counts = Counter(t["task_layer"] for t in a["tasks"])
    for layer in ("atom", "compound", "feature", "generalized"):
        assert len(a["by_layer"][layer]) == layer_counts.get(layer, 0), (
            f"{layer}: by_layer={len(a['by_layer'][layer])} tasks={layer_counts.get(layer, 0)}"
        )


# ---------- relation_targets ----------

def test_relation_targets_present():
    """relation_targets 是 dict,sid → [引用到的其他 task _short 列表]"""
    a = build_assets()
    assert "relation_targets" in a
    assert isinstance(a["relation_targets"], dict)


def test_relation_targets_excludes_self():
    """任何 task 的 relation_targets 列表都不包含自身 sid"""
    a = build_assets()
    for sid, targets in a["relation_targets"].items():
        assert sid not in targets, f"{sid} 出现在自己的 relation_targets 中"


def test_relation_targets_sorted_and_unique():
    """每个 task 的 relation_targets 列表去重 + 按 id 升序"""
    a = build_assets()
    for sid, targets in a["relation_targets"].items():
        assert targets == sorted(targets), f"{sid} 未按 id 升序: {targets}"
        assert len(targets) == len(set(targets)), f"{sid} 含重复"


def test_relation_targets_atoms_have_no_dangling():
    """relation_targets 引用的 sid 必须真实存在于 tasks"""
    a = build_assets()
    tb = {t["_short"]: t for t in a["tasks"]}
    for sid, targets in a["relation_targets"].items():
        for t in targets:
            assert t in tb, f"{sid}.relation_targets 含不存在的 {t}"


def test_relation_targets_known_feature_has_compound_or_atom_children():
    """sanity: feature 2-00001 应至少引用 1 个 compound 或 atom(其编排下层)"""
    a = build_assets()
    targets = a["relation_targets"].get("2-00001", [])
    assert len(targets) >= 1
    assert any(t.startswith("1-") or t.startswith("0-") for t in targets), (
        f"2-00001 应编排至少 1 个 compound/atom, 实得 {targets}"
    )