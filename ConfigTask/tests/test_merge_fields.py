# ConfigTask/tests/test_merge_fields.py
"""merge_fields 的 prep/pause/ingest 模型集成测试。"""
import json

from builder.steps.merge_fields import run, build_agent_input, build_prompt, parse_output


def _write_jsonl(path, records):
    if records:
        path.write_text("\n".join(json.dumps(r, ensure_ascii=False) for r in records) + "\n",
                        encoding="utf-8")
    else:
        path.write_text("", encoding="utf-8")


def _cluster(cid, n=1):
    return {
        "cluster_id": cid, "core_commands": ["ADD URR"], "member_count": n,
        "business_domains": ["计费"],
        "members": [{
            "candidate_id": f"{cid}#m1", "feature_id": "GWFD-001",
            "candidate_desc": "x", "commands": ["ADD URR"],
            "step_text": "配置URR", "command_examples": ["ADD URR:URRID=1;"],
            "param_rows": [{"command": "ADD URR", "param_code": "URRID", "obtain_method": "全网规划"}],
        }],
    }


def _ctx(data_dir):
    return {"data_dir": data_dir, "nf": "UDG", "version": "20.15.2"}


def test_prep_pauses_when_output_missing(tmp_path):
    _write_jsonl(tmp_path / "task_clusters_enriched.jsonl", [_cluster("cluster-002"), _cluster("cluster-003")])
    _write_jsonl(tmp_path / "config_tasks.jsonl", [])  # 全 pending
    result = run(_ctx(tmp_path))
    assert result == "PAUSE"
    prompts = list((tmp_path / "agent_prompts" / "merge_fields").glob("*.txt"))
    assert len(prompts) == 2


def test_ingest_when_output_present(tmp_path):
    _write_jsonl(tmp_path / "task_clusters_enriched.jsonl", [_cluster("cluster-003")])
    _write_jsonl(tmp_path / "config_tasks.jsonl", [])
    assert run(_ctx(tmp_path)) == "PAUSE"
    out = tmp_path / "agent_outputs" / "merge_fields" / "cluster-003.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps({
        "task_logical_name": "配置URR", "task_goal": "g", "task_summary": "s",
        "commands": [{"command_ref": "ADD URR", "parameters": [
            {"parameter_ref": "URRID", "binding_type": "variable", "variable_source": "global_planned"}]}],
        "decision_points": [], "split_notes": ""
    }, ensure_ascii=False), encoding="utf-8")
    result = run(_ctx(tmp_path))
    assert result == 1
    recs = [json.loads(l) for l in (tmp_path / "config_tasks.jsonl").read_text(encoding="utf-8").splitlines() if l.strip()]
    assert recs[0]["cluster_id"] == "cluster-003"
    assert recs[0]["task_id"] == "UDG@20.15.2@ConfigTask@00001"


def test_done_cluster_not_pending(tmp_path):
    _write_jsonl(tmp_path / "task_clusters_enriched.jsonl", [_cluster("cluster-003")])
    _write_jsonl(tmp_path / "config_tasks.jsonl", [{"cluster_id": "cluster-003"}])  # 已 done
    result = run(_ctx(tmp_path))
    assert result == 1  # 非 PAUSE


def test_parse_output_extracts_json():
    raw = '一些文字 {"task_logical_name":"x","task_goal":"g","task_summary":"s","commands":[]} 尾巴'
    t = parse_output(raw, "cluster-001", "UDG", "20.15.2", 5)
    assert t["cluster_id"] == "cluster-001"
    assert t["task_id"] == "UDG@20.15.2@ConfigTask@00006"
    assert t["task_logical_name"] == "x"


def test_parse_output_no_json_returns_none():
    assert parse_output("无JSON", "c1", "UDG", "20.15.2", 0) is None
