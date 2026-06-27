# ConfigTask/tests/test_finalize_fields.py
"""finalize_fields 后处理单测：只补齐字段，基本信息不丢失。

外网（当下）能补：command_ref 全键、source_evidence_ids、中间态 _ 前缀。
内网（命令图谱参数表/依赖全集齐后）单独程序补：parameter_ref 全键、source_ref。
"""
from builder.steps.finalize_fields import finalize_record

MML = {"ADD URR", "ADD RULE", "ADD FILTER"}


def _base(cluster_id="c1"):
    return {"cluster_id": cluster_id, "commands": []}


def test_command_ref_wrapped_to_full_key():
    task = _base()
    task["commands"] = [{"command_ref": "ADD URR", "parameters": []}]
    finalize_record(task, {"c1": {"members": []}}, MML, "UDG", "20.15.2")
    assert task["commands"][0]["command_ref"] == "UDG@20.15.2@MMLCommand@ADD URR"


def test_command_ref_unknown_kept_bare_no_fabrication():
    """未知命令保留裸名，不臆造全键（基本信息不丢失）。"""
    task = _base()
    task["commands"] = [{"command_ref": "ADD NOPE", "parameters": []}]
    finalize_record(task, {"c1": {"members": []}}, MML, "UDG", "20.15.2")
    assert task["commands"][0]["command_ref"] == "ADD NOPE"


def test_command_ref_idempotent_if_already_full_key():
    task = _base()
    full = "UDG@20.15.2@MMLCommand@ADD URR"
    task["commands"] = [{"command_ref": full, "parameters": []}]
    finalize_record(task, {"c1": {"members": []}}, MML, "UDG", "20.15.2")
    assert task["commands"][0]["command_ref"] == full  # 不二次包装


def test_source_evidence_ids_aggregated_dedup():
    task = _base()
    cl = {"members": [{"doc_path": "a.md"}, {"doc_path": "b.md"}, {"doc_path": "a.md"}]}
    finalize_record(task, {"c1": cl}, MML, "UDG", "20.15.2")
    assert sorted(task["source_evidence_ids"]) == ["a.md", "b.md"]


def test_source_evidence_ids_empty_when_cluster_missing():
    task = _base("orphan")
    finalize_record(task, {}, MML, "UDG", "20.15.2")
    assert task["source_evidence_ids"] == []


def test_intermediate_fields_prefixed():
    task = _base()
    task["decision_points"] = ["x"]
    task["split_notes"] = "y"
    finalize_record(task, {"c1": {"members": []}}, MML, "UDG", "20.15.2")
    assert task["_decision_points"] == ["x"]
    assert task["_split_notes"] == "y"
    assert "decision_points" not in task
    assert "split_notes" not in task


def test_intermediate_prefix_idempotent():
    task = _base()
    task["_decision_points"] = ["x"]
    finalize_record(task, {"c1": {"members": []}}, MML, "UDG", "20.15.2")
    assert task["_decision_points"] == ["x"]


def test_parameter_ref_left_bare_for_intranet_program():
    """parameter_ref / source_ref 不动，留给内网程序（命令图谱参数表在内网）。"""
    task = _base()
    task["commands"] = [{"command_ref": "ADD URR", "parameters": [
        {"parameter_ref": "URRNAME", "binding_type": "variable"}]}]
    finalize_record(task, {"c1": {"members": []}}, MML, "UDG", "20.15.2")
    p = task["commands"][0]["parameters"][0]
    assert p["parameter_ref"] == "URRNAME"   # 仍裸名
    assert "source_ref" not in p             # 未补


def test_no_basic_info_loss_other_fields_preserved():
    """既有字段一律保留，后处理只补不删。"""
    task = _base()
    task.update({
        "task_id": "UDG@20.15.2@ConfigTask@00001",
        "task_logical_name": "配置计费三件套",
        "business_domains": ["计费"],
        "source_cluster_members": 19,
        "extraction_method": "inline_enriched",
    })
    finalize_record(task, {"c1": {"members": []}}, MML, "UDG", "20.15.2")
    assert task["task_id"] == "UDG@20.15.2@ConfigTask@00001"
    assert task["task_logical_name"] == "配置计费三件套"
    assert task["business_domains"] == ["计费"]
    assert task["source_cluster_members"] == 19
    assert task["extraction_method"] == "inline_enriched"
