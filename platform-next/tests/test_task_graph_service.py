"""ConfigTaskService 字段派生 + relations/parents 逻辑测试。"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from shared.config import load_config
from task_graph.service import get_service, _short, _parse_ref

def setup_module(module):
    load_config()


def test_short_and_parse_ref():
    assert _short("UDG@20.15.2@Task@0-00001") == "0-00001"
    assert _short("") == ""
    assert _parse_ref("UDG@20.15.2@MMLCommand@ADD URR") == {"type": "MMLCommand", "value": "ADD URR"}
    assert _parse_ref("UDG@20.15.2@Feature@GWFD-020301") == {"type": "Feature", "value": "GWFD-020301"}
    assert _parse_ref("") == {}


def test_stats_counts():
    svc = get_service()
    st = svc.get_stats()
    assert st["total_tasks"] == 201
    assert st["total_rules"] == 205
    assert st["total_dps"] == 55
    assert any(v["nf"] == "UDG" and v["version"] == "20.15.2" and v["task_count"] == 201 for v in st["ne_versions"])


def test_list_tasks_layer_filter_and_slim():
    svc = get_service()
    r = svc.list_tasks(nf="UDG", version="20.15.2", layer="feature")
    assert r["total"] == 10
    assert all(it["task_layer"] == "feature" for it in r["items"])
    it = r["items"][0]
    assert it["ref_type"] == "Feature"
    assert "n_dps" in it and "n_rules" in it and "n_relations" in it


def test_get_task_returns_own_relations_and_children():
    svc = get_service()
    t = svc.get_task("UDG", "20.15.2", "2-00002")
    assert t is not None
    assert len(t["task_relations"]) == 6
    r0 = t["task_relations"][0]
    for k in ("from_short", "to_short", "relation_type"):
        assert k in r0
    children = {r["from_short"] for r in t["task_relations"]} | {r["to_short"] for r in t["task_relations"]}
    children.discard("2-00002")
    assert "1-00001" in children and "0-00016" in children


def test_get_task_parents():
    svc = get_service()
    t = svc.get_task("UDG", "20.15.2", "0-00016")
    assert t is not None
    assert t["task_relations"] == []
    parent_shorts = [p["short"] for p in t["parents"]]
    assert "2-00002" in parent_shorts


def test_get_task_dp_with_impacts():
    svc = get_service()
    t = svc.get_task("UDG", "20.15.2", "2-00002")
    dps = t["decision_points"]
    assert any(d["decision_id"].endswith("0-00154") for d in dps)
    dp = next(d for d in dps if d["decision_id"].endswith("0-00154"))
    impacts = [imp for opt in dp["options"] for imp in opt.get("impacts", [])]
    assert any(imp.get("target_type") == "task" for imp in impacts)


def test_get_task_ref_cross_link():
    svc = get_service()
    feat = svc.get_task("UDG", "20.15.2", "2-00001")
    assert feat["ref_parsed"] == {"type": "Feature", "value": "GWFD-020301"}
    atom = svc.get_task("UDG", "20.15.2", "0-00001")
    assert atom["ref_parsed"]["type"] == "MMLCommand"
    assert atom["ref_parsed"]["value"] == "ADD URR"


def test_task_tree():
    svc = get_service()
    tr = svc.get_task_tree("0-00016")
    assert tr["center"] == "0-00016"
    assert any(n["id"] == "2-00002" for n in tr["nodes"])


def test_get_task_endpoint_relations_for_leaf():
    """atom 0-00016 是叶子(无 own task_relations),但作为端点被 2-00002 引用 → endpoint_relations 非空且含 1-00004/2-00002 侧"""
    svc = get_service()
    t = svc.get_task("UDG", "20.15.2", "0-00016")
    assert t is not None
    assert t["task_relations"] == []                      # 叶子无 own 边
    assert len(t["endpoint_relations"]) >= 1              # 但作为端点有边
    others = {e["other"] for e in t["endpoint_relations"]}
    # 2-00002 编排 0-00016:它把 1-00004→0-00016 写在自己的 task_relations 里,
    # 所以 0-00016 作为端点的 other 是 1-00004;orchestrator 2-00002 在 parents 里
    assert "1-00004" in others or "2-00002" in others     # 引用方在
    # 每条补全 name/layer
    e0 = t["endpoint_relations"][0]
    for k in ("other", "other_logical_name", "other_layer", "direction", "relation_type"):
        assert k in e0
