"""Unit tests for command_graph.service — get_command_parameters & get_command_graph.

These tests bypass the asset-directory scan and inject in-memory buckets
directly, so they run without the real CommandGraph/data tree. They verify:
  - strict command_id matching in get_command_parameters
  - empty list for a command with no parameters
  - graph node/edge assembly, including:
      * one command node + one node per parameter
      * has_parameter edges (command -> param)
      * depends_on edges with a short condition label (=VALUE) and a full title
      * an external parameter referenced by depends_on is surfaced as a
        parameter_external node (the relationship is never dropped)
"""
import sys
from pathlib import Path

# Make platform-next importable when running pytest from the repo root or
# from inside platform-next/. Inserting the parent of this file resolves to
# the platform-next/ directory.
PLATFORM_ROOT = Path(__file__).resolve().parent.parent
if str(PLATFORM_ROOT) not in sys.path:
    sys.path.insert(0, str(PLATFORM_ROOT))

from command_graph.service import CommandGraphService, _last_segment  # noqa: E402


def _make_service() -> CommandGraphService:
    """Build a CommandGraphService without triggering the real asset scan.

    We construct via __new__ so __init__ (which calls _load against the real
    assets_root) is skipped, then populate the in-memory fields directly.
    """
    svc = CommandGraphService.__new__(CommandGraphService)
    svc._assets_root = None
    svc._doc_root = PLATFORM_ROOT
    svc._records = []
    svc._by_id = {}
    svc._params = {}
    svc._has_param = {}
    svc._depends = {}
    return svc


def _seed_simple(svc: CommandGraphService) -> None:
    """Seed a (UDG, 20.15.2) bucket with a 2-parameter command that has one
    intra-command depends_on edge and one depends_on edge whose target is an
    external parameter (not in this command's own parameter set)."""
    nf, ver = "UDG", "20.15.2"
    cmd_id = f"{nf}@{ver}@MMLCommand@SET AUTOLOGPOLICY"

    svc._records.append({
        "command_id": cmd_id,
        "command_name": "SET AUTOLOGPOLICY",
        "command_name_zh": "设置自动日志策略",
        "nf": nf,
        "version": ver,
    })
    svc._by_id[cmd_id] = svc._records[-1]

    def pid(name: str) -> str:
        return f"{nf}@{ver}@CommandParameter@SET AUTOLOGPOLICY:{name}"

    svc._params[(nf, ver)] = [
        {
            "parameter_id": pid("BKSERVERIPTYPE"),
            "command_id": cmd_id,
            "parameter_name": "BKSERVERIPTYPE",
            "parameter_name_zh": "备份服务器IP类型",
            "data_type": "枚举",
            "required_mode": "必选",
        },
        {
            "parameter_id": pid("IPV4"),
            "command_id": cmd_id,
            "parameter_name": "IPV4",
            "parameter_name_zh": "IPv4地址",
            "data_type": "字符串",
            "required_mode": "可选",
        },
    ]
    svc._has_param[(nf, ver)] = [
        {"edge_type": "has_parameter", "from_command_ref": cmd_id,
         "to_parameter_ref": pid("BKSERVERIPTYPE")},
        {"edge_type": "has_parameter", "from_command_ref": cmd_id,
         "to_parameter_ref": pid("IPV4")},
    ]
    # one intra-command edge (BKSERVERIPTYPE -> IPV4), one edge to an external
    # parameter (BKSERVERIPTYPE -> EXTERNAL_PARAM, not in the param set above)
    svc._depends[(nf, ver)] = [
        {"edge_type": "depends_on",
         "from_parameter_ref": pid("BKSERVERIPTYPE"),
         "to_parameter_ref": pid("IPV4"),
         "condition_ref": "BKSERVERIPTYPE", "condition_logic": "等于",
         "condition_value": "IPV4"},
        {"edge_type": "depends_on",
         "from_parameter_ref": pid("BKSERVERIPTYPE"),
         "to_parameter_ref": f"{nf}@{ver}@CommandParameter@OTHERCMD:EXTERNAL_PARAM",
         "condition_ref": "BKSERVERIPTYPE", "condition_logic": "等于",
         "condition_value": "SOMETHING"},
    ]


# ---- get_command_parameters ----
def test_get_command_parameters_strict_match():
    svc = _make_service()
    _seed_simple(svc)
    params = svc.get_command_parameters("UDG", "SET AUTOLOGPOLICY", "20.15.2")
    assert len(params) == 2
    names = {p["parameter_name"] for p in params}
    assert names == {"BKSERVERIPTYPE", "IPV4"}


def test_get_command_parameters_empty_for_unknown_command():
    svc = _make_service()
    _seed_simple(svc)
    # ADD URR exists in the real data with zero parameters; here it is simply
    # absent from the bucket, which must yield an empty list (not an error).
    assert svc.get_command_parameters("UDG", "ADD URR", "20.15.2") == []


def test_get_command_parameters_version_isolation():
    svc = _make_service()
    _seed_simple(svc)
    # A different version has no bucket at all -> empty.
    assert svc.get_command_parameters("UDG", "SET AUTOLOGPOLICY", "9.9.9") == []


# ---- get_command_graph ----
def test_graph_node_and_edge_counts():
    svc = _make_service()
    _seed_simple(svc)
    g = svc.get_command_graph("UDG", "SET AUTOLOGPOLICY", "20.15.2")
    # 1 command + 2 params + 1 external = 4 nodes
    assert len(g["nodes"]) == 4
    groups = {n["group"] for n in g["nodes"]}
    assert groups == {"command", "parameter", "parameter_external"}
    # 2 has_parameter + 2 depends_on = 4 edges
    assert len(g["edges"]) == 4
    edge_types = [e["type"] for e in g["edges"]]
    assert edge_types.count("has_parameter") == 2
    assert edge_types.count("depends_on") == 2


def test_graph_depends_on_label_and_title():
    svc = _make_service()
    _seed_simple(svc)
    g = svc.get_command_graph("UDG", "SET AUTOLOGPOLICY", "20.15.2")
    dep_edges = [e for e in g["edges"] if e["type"] == "depends_on"]
    # short label uses the condition value; title carries the full condition
    ipv4_edge = next(e for e in dep_edges if e["to"].endswith(":IPV4"))
    assert ipv4_edge["label"] == "=IPV4"
    assert ipv4_edge["title"] == "BKSERVERIPTYPE 等于 IPV4"


def test_graph_external_parameter_surfaced_as_node():
    svc = _make_service()
    _seed_simple(svc)
    g = svc.get_command_graph("UDG", "SET AUTOLOGPOLICY", "20.15.2")
    ext_nodes = [n for n in g["nodes"] if n["group"] == "parameter_external"]
    assert len(ext_nodes) == 1
    ext = ext_nodes[0]
    # label is the last colon segment of the parameter ref
    assert ext["label"] == "EXTERNAL_PARAM"
    assert ext["id"].endswith(":EXTERNAL_PARAM")


def test_graph_empty_command_still_emits_command_node():
    svc = _make_service()
    _seed_simple(svc)
    g = svc.get_command_graph("UDG", "ADD URR", "20.15.2")
    # command has no params — spec: still draw the command node
    assert len(g["nodes"]) == 1
    assert g["nodes"][0]["group"] == "command"
    assert g["nodes"][0]["label"] == "ADD URR"
    assert g["edges"] == []


# ---- helper ----
def test_last_segment_handles_command_with_spaces():
    ref = "UDG@20.15.2@CommandParameter@SET AUTOLOGPOLICY:BKSERVERIPTYPE"
    assert _last_segment(ref) == "BKSERVERIPTYPE"
    assert _last_segment("") == ""
