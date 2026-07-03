"""测试 build_index.py 的 build_compounds() —— compound 登记表派生(spec §8.3)。

对应 spec docs/superpowers/specs/2026-07-02-compound-feature-extraction-design.md §8.3。
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))

from build_index import build_compounds  # noqa: E402


def _atom(tid, cmd):
    return {"task_id": f"UDG@20.15.2@Task@{tid}", "task_layer": "atom",
            "ref": f"UDG@20.15.2@MMLCommand@{cmd}"}


def _compound(tid, atom_ids, name=None, intent=None):
    rels = [{"from_task_ref": f"UDG@20.15.2@Task@{a}",
             "to_task_ref": f"UDG@20.15.2@Task@{b}"} for a, b in zip(atom_ids, atom_ids[1:])]
    return {"task_id": f"UDG@20.15.2@Task@{tid}", "task_layer": "compound",
            "task_logical_name": name or f"compound-{tid}", "task_intent": intent or f"intent-{tid}",
            "task_relations": rels}


def _feature(tid, compound_refs):
    return {"task_id": f"UDG@20.15.2@Task@{tid}", "task_layer": "feature",
            "task_relations": [{"from_task_ref": f"UDG@20.15.2@Task@{c}",
                                "to_task_ref": f"UDG@20.15.2@Task@{c}",
                                "relation_type": "contains"} for c in compound_refs]}


# ---------- build_compounds ----------

def test_compounds_keys_and_command_set():
    """compound 条目含 {compound_id, logical_name, phase, intent, command_set, features_using},command_set 从 atom.ref 解析。"""
    tasks = [_atom("0-00001", "ADD URR"), _atom("0-00002", "ADD URRGROUP"),
             _compound("1-00001", ["0-00001", "0-00002"], name="计费三件套", intent="费率→策略组")]
    c = build_compounds(tasks)
    assert "1-00001" in c
    entry = c["1-00001"]
    for k in ("compound_id", "logical_name", "phase", "intent", "command_set", "features_using"):
        assert k in entry, f"缺字段 {k}"
    assert set(entry["command_set"]) == {"ADD URR", "ADD URRGROUP"}
    assert entry["phase"] == "计费三件套"  # phase = logical_name
    assert entry["intent"] == "费率→策略组"


def test_compounds_skips_non_compound():
    """只收 task_layer=compound,atom/feature/generalized 不进 compounds。"""
    tasks = [_atom("0-00001", "ADD URR"),
             _compound("1-00001", ["0-00001"]),
             _feature("2-00001", ["1-00001"])]
    c = build_compounds(tasks)
    assert set(c.keys()) == {"1-00001"}


def test_features_using_reverse():
    """features_using = 引用该 compound 的 feature/generalized task(从其 task_relations 反查)。"""
    tasks = [_atom("0-00001", "ADD URR"),
             _compound("1-00001", ["0-00001"]),
             _feature("2-00001", ["1-00001"]),
             _feature("2-00002", ["1-00001"])]
    c = build_compounds(tasks)
    assert set(c["1-00001"]["features_using"]) == {"2-00001", "2-00002"}


def test_command_set_empty_for_compound_without_atom_refs():
    """compound 的 task_relations 不指向 atom 时,command_set 为空(不报错)。"""
    tasks = [_compound("1-00001", [])]
    c = build_compounds(tasks)
    assert c["1-00001"]["command_set"] == []
