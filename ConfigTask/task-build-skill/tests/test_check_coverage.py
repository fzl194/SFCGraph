"""测试 check_feature_coverage.check_coverage() —— per-DP-分支覆盖硬闸(spec §4)。

对应 spec docs/superpowers/specs/2026-07-02-compound-feature-extraction-design.md §4。
关键点:① key off target_type∈{task,command}(不看 effect_type 名)② 环检测 ③ per-variant 集合相等 ④ 结构基线 + DP impact 增删。
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))

from check_feature_coverage import check_coverage, short  # noqa: E402


def _atom(tid, cmd):
    return {"task_id": f"UDG@20.15.2@Task@{tid}", "task_layer": "atom",
            "ref": f"UDG@20.15.2@MMLCommand@{cmd}"}


def _compound(tid, atom_ids):
    return {"task_id": f"UDG@20.15.2@Task@{tid}", "task_layer": "compound",
            "task_relations": [{"from_task_ref": f"UDG@20.15.2@Task@{a}",
                                "to_task_ref": f"UDG@20.15.2@Task@{b}"} for a, b in zip(atom_ids, atom_ids[1:])]}


def _feature(tid, child_ids):
    return {"task_id": f"UDG@20.15.2@Task@{tid}", "task_layer": "feature",
            "task_relations": [{"from_task_ref": f"UDG@20.15.2@Task@{tid}",
                                "to_task_ref": f"UDG@20.15.2@Task@{c}",
                                "relation_type": "contains"} for c in child_ids]}


def _dp(did, owner, opts):
    """opts: {option_id: [impacts...]} each impact {target_type, target_ref, effect_type}"""
    options = []
    for oid, impacts in opts.items():
        options.append({"option_id": oid, "impacts": impacts})
    return {"decision_id": f"UDG@20.15.2@DecisionPoint@{did}",
            "owner_task_ref": f"UDG@20.15.2@Task@{owner}", "options": options}


def _variants(fid, variants):
    return {"feature_id": fid, "variants": variants}


BASE_TASKS = [
    _atom("0-00001", "ADD URR"),
    _atom("0-00002", "ADD URRGROUP"),
    _atom("0-00003", "ADD FILTER"),
    _compound("1-00001", ["0-00001", "0-00002"]),  # 计费三件套(子集)
    _feature("2-00001", ["1-00001", "0-00003"]),   # feature 含 compound + 直挂 atom
]


# ---------- per-variant 集合相等 ----------

def test_pass_single_variant():
    """单变体:结构命令集 == md_required → ok。"""
    v = _variants("GWFD-020301", [{"name": "基础", "dp_options": {},
                                   "md_required_commands": ["ADD URR", "ADD URRGROUP", "ADD FILTER"]}])
    r = check_coverage("2-00001", BASE_TASKS, [], v)
    assert r["ok"] is True
    assert r["variants_checked"] == 1
    assert set(r["struct_commands"]) == {"ADD URR", "ADD URRGROUP", "ADD FILTER"}


def test_fail_missing_command():
    """active 缺 md 要求的命令 → 报 缺。"""
    v = _variants("GWFD-020301", [{"name": "基础", "dp_options": {},
                                   "md_required_commands": ["ADD URR", "ADD URRGROUP", "ADD FILTER", "ADD X"]}])
    r = check_coverage("2-00001", BASE_TASKS, [], v)
    assert r["ok"] is False
    assert len(r["failures"]) == 1
    assert "ADD X" in r["failures"][0]["missing"]


def test_fail_extra_command():
    """active 多 md 没有的命令 → 报 多。"""
    v = _variants("GWFD-020301", [{"name": "仅URR", "dp_options": {},
                                   "md_required_commands": ["ADD URR"]}])
    r = check_coverage("2-00001", BASE_TASKS, [], v)
    assert r["ok"] is False
    assert "ADD URRGROUP" in r["failures"][0]["extra"]
    assert "ADD FILTER" in r["failures"][0]["extra"]


# ---------- DP impact 增删(key off target_type)----------

def test_dp_exclude_carves_variant():
    """DP impact target_type=command + excludes → 该变体去掉该命令;md_required 匹配 → ok。"""
    dps = [_dp("0-00050", "2-00001", {
        "opt-no-filter": [{"target_type": "command", "target_ref": "ADD FILTER", "effect_type": "excludes"}]})]
    v = _variants("GWFD-020301", [
        {"name": "带过滤", "dp_options": {}, "md_required_commands": ["ADD URR", "ADD URRGROUP", "ADD FILTER"]},
        {"name": "无过滤", "dp_options": {"0-00050": "opt-no-filter"},
         "md_required_commands": ["ADD URR", "ADD URRGROUP"]},
    ])
    r = check_coverage("2-00001", BASE_TASKS, dps, v)
    assert r["ok"] is True, r
    assert r["variants_checked"] == 2


def test_dp_adds_conditional_command():
    """DP impact target_type=task + adds → 该变体加该 atom 的命令(条件出现)。"""
    # 加一个条件 atom 0-00004 ADD URRFAILACTION,不在 feature 结构里,只在 DP adds 时出现
    tasks = BASE_TASKS + [_atom("0-00004", "ADD URRFAILACTION")]
    dps = [_dp("0-00051", "2-00001", {
        "opt-online": [{"target_type": "task", "target_ref": "UDG@20.15.2@Task@0-00004", "effect_type": "adds"}]})]
    v = _variants("GWFD-020301", [
        {"name": "基础", "dp_options": {},
         "md_required_commands": ["ADD URR", "ADD URRGROUP", "ADD FILTER"]},
        {"name": "在线", "dp_options": {"0-00051": "opt-online"},
         "md_required_commands": ["ADD URR", "ADD URRGROUP", "ADD FILTER", "ADD URRFAILACTION"]},
    ])
    r = check_coverage("2-00001", tasks, dps, v)
    assert r["ok"] is True, r


# ---------- 环检测 ----------

def test_ring_detected():
    """compound 互相 contains 形成环 → 报 环错,不无限递归。"""
    tasks = [
        _atom("0-00001", "ADD URR"),
        {"task_id": "UDG@20.15.2@Task@1-00001", "task_layer": "compound",
         "task_relations": [{"from_task_ref": "UDG@20.15.2@Task@1-00001",
                             "to_task_ref": "UDG@20.15.2@Task@1-00002"}]},
        {"task_id": "UDG@20.15.2@Task@1-00002", "task_layer": "compound",
         "task_relations": [{"from_task_ref": "UDG@20.15.2@Task@1-00002",
                             "to_task_ref": "UDG@20.15.2@Task@1-00001"}]},  # 回到 1-00001 = 环
        _feature("2-00001", ["1-00001"]),
    ]
    v = _variants("GWFD-020301", [{"name": "x", "dp_options": {}, "md_required_commands": ["ADD URR"]}])
    r = check_coverage("2-00001", tasks, [], v)
    assert r["ok"] is False
    assert any(e["kind"] == "ring" for e in r["errors"]), r["errors"]
