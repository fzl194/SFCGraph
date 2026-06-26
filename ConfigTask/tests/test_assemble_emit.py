# ConfigTask/tests/test_assemble_emit.py
import json
from builder.steps.assemble import run as assemble
from builder.steps.emit_skeleton import run as emit


def _ctx(tmp_path):
    return {
        "nf": "UDG", "version": "20.15.2", "assets_root": tmp_path,
        "features": [{
            "feature_id": "GWFD-020301",
            "doc_path": "/p/部署UPF.md",
            "sections": {"操作步骤": "1. 配置URR。\n  **ADD URR**\n2. 配置URR组。\n  **ADD URRGROUP**\n"},
            "tasks": [{
                "phase_name": "配置业务费率", "step_range": (1, 2), "boundary_source": "flow",
                "commands": [{"command_ref": "UDG@20.15.2@MMLCommand@ADD URR",
                              "parameters": [{"parameter_ref": "UDG@20.15.2@CommandParameter@ADD URR:URRNAME",
                                              "reference_hint": False}]}],
            }],
        }],
    }


def test_assemble_builds_skeleton_with_empty_semantics(tmp_path):
    ctx = _ctx(tmp_path)
    n = assemble(ctx)
    assert n == 1
    t = ctx["skeleton"][0]
    assert t["task_id"] == "UDG@20.15.2@ConfigTask@00001"
    assert t["task_logical_name"] == ""           # Agent 填
    assert t["task_goal"] == "" and t["task_summary"] == ""
    assert "ADD URR" in t["raw_steps_text_raw"]   # 原文切片
    assert "ADD URRGROUP" in t["raw_steps_text_raw"]
    assert t["task_category"] == "配置"
    assert t["status"] == "active"
    assert t["source_evidence_ids"] == ["/p/部署UPF.md"]
    assert t["_boundary_source"] == "flow"
    assert t["_phase_hint"] == "配置业务费率"
    # commands 带过来
    assert t["commands"][0]["parameters"][0]["parameter_ref"].endswith(":URRNAME")
    # binding_type 未填
    assert "binding_type" not in t["commands"][0]["parameters"][0]


def test_emit_writes_jsonl(tmp_path):
    ctx = _ctx(tmp_path)
    assemble(ctx)
    n = emit(ctx)
    assert n == 1
    out = tmp_path / "UDG" / "20.15.2" / "config_tasks.skeleton.jsonl"
    assert out.exists()
    lines = out.read_text(encoding="utf-8").strip().splitlines()
    assert len(lines) == 1
    obj = json.loads(lines[0])
    assert obj["task_id"] == "UDG@20.15.2@ConfigTask@00001"
