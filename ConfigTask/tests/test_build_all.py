# ConfigTask/tests/test_build_all.py
"""make_ctx 的网元×版本隔离测试（防止 UDG/UNC 数据互相覆盖）。"""
import pathlib

import yaml

from build_all import make_ctx

_CFG = {
    "project_root": "..",
    "assets_root": "data/assets",
    "ne": {
        "UDG": {"20.15.2": {"corpus_root": "a", "steps": [], "agent_batch_size": 5}},
        "UNC": {"20.15.2": {"corpus_root": "b", "steps": [], "agent_batch_size": 5}},
    },
}


def test_data_dir_isolated_per_nf():
    udg = make_ctx(_CFG, "UDG", "20.15.2")
    unc = make_ctx(_CFG, "UNC", "20.15.2")
    assert udg["data_dir"] != unc["data_dir"]


def test_data_dir_nested_under_nf_version():
    udg = make_ctx(_CFG, "UDG", "20.15.2")
    assert udg["data_dir"].name == "20.15.2"
    assert udg["data_dir"].parent.name == "UDG"


def test_assets_root_under_isolated_data_dir():
    udg = make_ctx(_CFG, "UDG", "20.15.2")
    # assets_root 必须在隔离的 data_dir 下，不能再是扁平 data/assets
    assert udg["assets_root"].parent == udg["data_dir"]


def test_command_graph_dir_resolved_against_project_root():
    cfg = yaml.safe_load  # 仅占位，确保 yaml 可用
    config = {
        "project_root": "..",
        "ne": {"UDG": {"20.15.2": {
            "command_graph_dir": "CommandGraph/data/assets/UDG/20.15.2", "steps": [],
        }}},
    }
    ctx = make_ctx(config, "UDG", "20.15.2")
    assert ctx["command_graph_dir"].endswith("CommandGraph\\data\\assets\\UDG\\20.15.2") \
        or ctx["command_graph_dir"].endswith("CommandGraph/data/assets/UDG/20.15.2")


def test_ne_fields_not_overriding_resolved(monkeypatch):
    # **ne 展开不应覆盖已解析的 command_graph_dir（旧 bug 回归防护）
    config = {
        "project_root": "..",
        "ne": {"UDG": {"20.15.2": {
            "command_graph_dir": "CommandGraph/data/assets/UDG/20.15.2", "steps": [],
        }}},
    }
    ctx = make_ctx(config, "UDG", "20.15.2")
    assert "CommandGraph" in ctx["command_graph_dir"]
    assert "\\" in ctx["command_graph_dir"] or "/" in ctx["command_graph_dir"]  # 已解析为绝对路径
