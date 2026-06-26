"""统一图 service 测试：_load_graph（聚合 adjacency）+ get_subgraph（BFS）。

对照 spec §3.2（内存图）/ §3.3（get_subgraph）。
"""
import sys
from pathlib import Path

PLATFORM_ROOT = Path(__file__).resolve().parent.parent
if str(PLATFORM_ROOT) not in sys.path:
    sys.path.insert(0, str(PLATFORM_ROOT))

from command_graph.service import CommandGraphService  # noqa: E402


def _make_service() -> CommandGraphService:
    svc = CommandGraphService.__new__(CommandGraphService)
    svc._assets_root = None
    svc._doc_root = PLATFORM_ROOT
    svc._records = []
    svc._by_id = {}
    svc._params = {}
    svc._has_param = {}
    svc._depends = {}
    svc._obj_objects = {}
    svc._obj_edges = {}
    svc._param_refs = {}
    svc._obj_refers_to = {}
    svc._adjacency = {}
    return svc


def _seed_graph(svc: CommandGraphService) -> None:
    """seed：ADD URR 命令 + 2 参数 + URR/URRGROUP 对象 + 5 类边。"""
    nf, ver = "UDG", "20.15.2"
    cmd = f"{nf}@{ver}@MMLCommand@ADD URR"
    p1 = f"{nf}@{ver}@CommandParameter@ADD URR:URRNAME"
    p2 = f"{nf}@{ver}@CommandParameter@ADD URR:URRID"
    p_ref = f"{nf}@{ver}@CommandParameter@ADD URRGROUP:UPURRNAME1"  # 跨命令 ref 源（悬空，无点记录）
    obj = f"{nf}@{ver}@ConfigObject@URR"
    obj_grp = f"{nf}@{ver}@ConfigObject@URRGROUP"

    svc._records = [{"command_id": cmd, "command_name": "ADD URR", "nf": nf, "version": ver}]
    svc._by_id = {cmd: svc._records[0]}
    svc._params[(nf, ver)] = [
        {"parameter_id": p1, "parameter_name": "URRNAME", "command_id": cmd},
        {"parameter_id": p2, "parameter_name": "URRID", "command_id": cmd},
    ]
    svc._obj_objects = {
        obj: {"object_id": obj, "object_name": "URR", "object_kind": "entity"},
        obj_grp: {"object_id": obj_grp, "object_name": "URRGROUP", "object_kind": "group"},
    }
    svc._has_param[(nf, ver)] = [
        {"from_command_ref": cmd, "to_parameter_ref": p1},
        {"from_command_ref": cmd, "to_parameter_ref": p2},
    ]
    svc._depends[(nf, ver)] = [
        {"from_parameter_ref": p1, "to_parameter_ref": p2,
         "condition_ref": "URRNAME", "condition_logic": "等于", "condition_value": "X"},
    ]
    # 跨命令引用：UPURRNAME1 references URRNAME
    svc._param_refs[(nf, ver)] = [
        {"from_parameter_ref": p_ref, "to_parameter_ref": p1,
         "source_condition": "!null", "binding_strength": "强绑定", "cascade_delete": False},
    ]
    svc._obj_edges[(nf, ver)] = [
        {"from_command_ref": cmd, "to_object_ref": obj, "edge_type": "creates"},
    ]
    svc._obj_refers_to[(nf, ver)] = [
        {"from_object_ref": obj_grp, "to_object_ref": obj, "via_parameter": ["UPURRNAME1"]},
    ]
    svc._load_graph()


def test_load_graph_nodes_and_edges():
    svc = _make_service()
    _seed_graph(svc)
    adj = svc._adjacency
    # 点：ADD URR + URRNAME/URRID + URR/URRGROUP + UPURRNAME1(悬空 ref 端点)
    assert "UDG@20.15.2@MMLCommand@ADD URR" in adj
    assert "UDG@20.15.2@CommandParameter@ADD URR:URRNAME" in adj
    assert "UDG@20.15.2@CommandParameter@ADD URRGROUP:UPURRNAME1" in adj  # 悬空端点补入
    assert "UDG@20.15.2@ConfigObject@URR" in adj
    # 边类型齐全
    edge_types = {et for e in adj.values() for (_, et, _) in e["out"]}
    assert {"has_parameter", "conditional_required", "references", "creates", "refers_to"} <= edge_types
    # 悬空端点 type=None
    assert adj["UDG@20.15.2@CommandParameter@ADD URRGROUP:UPURRNAME1"]["node"]["type"] is None


def test_get_subgraph_command_2hop_with_references():
    svc = _make_service()
    _seed_graph(svc)
    center = "UDG@20.15.2@MMLCommand@ADD URR"
    g = svc.get_subgraph(center, hops=2,
                         edge_types=["has_parameter", "creates", "references", "conditional_required"])
    ids = {n["id"] for n in g["nodes"]}
    assert center in ids
    assert "UDG@20.15.2@CommandParameter@ADD URR:URRNAME" in ids      # 1跳参数
    assert "UDG@20.15.2@ConfigObject@URR" in ids                       # 1跳对象
    assert "UDG@20.15.2@CommandParameter@ADD URRGROUP:UPURRNAME1" in ids  # 2跳跨命令 ref
    ets = {e["type"] for e in g["edges"]}
    assert {"has_parameter", "creates", "references"} <= ets


def test_get_subgraph_edge_type_filter_excludes():
    svc = _make_service()
    _seed_graph(svc)
    center = "UDG@20.15.2@MMLCommand@ADD URR"
    g = svc.get_subgraph(center, hops=2, edge_types=["has_parameter"])
    assert {e["type"] for e in g["edges"]} == {"has_parameter"}
    # creates 被过滤 → URR 对象不出现
    assert "UDG@20.15.2@ConfigObject@URR" not in {n["id"] for n in g["nodes"]}


def test_get_subgraph_unknown_center_empty():
    svc = _make_service()
    _seed_graph(svc)
    assert svc.get_subgraph("NOT_EXIST", hops=2) == {"nodes": [], "edges": []}


def test_get_subgraph_multi_conditional_required_not_merged():
    """同对节点多条不同条件 conditional_required 边各自保留（spec §3.3 身份去重）。"""
    svc = _make_service()
    nf, ver = "UDG", "20.15.2"
    p1 = f"{nf}@{ver}@CommandParameter@ADD DEMO:SWITCH"
    p2 = f"{nf}@{ver}@CommandParameter@ADD DEMO:IPV4"
    svc._params[(nf, ver)] = [
        {"parameter_id": p1, "parameter_name": "SWITCH"},
        {"parameter_id": p2, "parameter_name": "IPV4"},
    ]
    svc._depends[(nf, ver)] = [
        {"from_parameter_ref": p1, "to_parameter_ref": p2, "condition_ref": "SWITCH", "condition_logic": "等于", "condition_value": "A"},
        {"from_parameter_ref": p1, "to_parameter_ref": p2, "condition_ref": "SWITCH", "condition_logic": "等于", "condition_value": "B"},
    ]
    svc._load_graph()
    g = svc.get_subgraph(p1, hops=1, edge_types=["conditional_required"])
    cr_edges = [e for e in g["edges"] if e["type"] == "conditional_required"]
    assert len(cr_edges) == 2  # 两条不同条件边都保留
    vals = {e["properties"]["condition_value"] for e in cr_edges}
    assert vals == {"A", "B"}
