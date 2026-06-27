# ConfigTask/tests/test_split_tasks.py
"""split_tasks 的 prep/pause/ingest 模型集成测试。"""
import json

from builder.steps.split_tasks import run, _batch_key, build_prompt, parse_agent_output


def _write_jsonl(path, records):
    if records:
        path.write_text("\n".join(json.dumps(r, ensure_ascii=False) for r in records) + "\n",
                        encoding="utf-8")
    else:
        path.write_text("", encoding="utf-8")


def _ctx(data_dir, batch_size=5):
    return {"data_dir": data_dir, "agent_batch_size": batch_size}


def _doc(path, fid="GWFD-X", steps=2):
    return {
        "doc_path": path, "feature_id": fid, "num_steps": steps,
        "steps": [{"step_num": i + 1, "step_desc": f"步骤{i+1}", "commands": ["ADD URR"]}
                  for i in range(steps)],
    }


def test_prep_writes_prompt_and_pauses(tmp_path):
    _write_jsonl(tmp_path / "doc_steps.jsonl", [_doc("a.md"), _doc("b.md")])
    _write_jsonl(tmp_path / "task_candidates.jsonl", [_doc("a.md")])  # a 已 done
    ctx = _ctx(tmp_path)
    result = run(ctx)
    assert result == "PAUSE"
    # b pending → 1 批 prompt 已写
    prompts = list((tmp_path / "agent_prompts" / "split_tasks").glob("*.txt"))
    assert len(prompts) == 1


def test_ingest_when_output_present(tmp_path):
    _write_jsonl(tmp_path / "doc_steps.jsonl", [_doc("b.md")])
    _write_jsonl(tmp_path / "task_candidates.jsonl", [])  # 空，b pending
    ctx = _ctx(tmp_path)
    # 第一次：prep + PAUSE
    assert run(ctx) == "PAUSE"
    key = _batch_key([_doc("b.md")])
    # 模拟 Agent 输出
    out = tmp_path / "agent_outputs" / "split_tasks" / f"{key}.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps({"b.md": [
        {"step_range": [1, 2], "candidate_desc": "配置URR", "commands": ["ADD URR"]}
    ]}, ensure_ascii=False), encoding="utf-8")
    # 第二次：ingest → 非 PAUSE
    result = run(ctx)
    assert result == 1
    # candidate 已追加
    cands = [json.loads(l) for l in (tmp_path / "task_candidates.jsonl").read_text(encoding="utf-8").splitlines()]
    assert any(c["doc_path"] == "b.md" for c in cands)


def test_all_done_skips(tmp_path):
    _write_jsonl(tmp_path / "doc_steps.jsonl", [_doc("a.md")])
    _write_jsonl(tmp_path / "task_candidates.jsonl", [_doc("a.md")])  # a 已 done
    ctx = _ctx(tmp_path)
    result = run(ctx)
    assert result == 1  # 全 done，非 PAUSE
    # 不应写 prompt
    assert not (tmp_path / "agent_prompts").exists() or \
           not list((tmp_path / "agent_prompts" / "split_tasks").glob("*.txt"))


def test_batch_key_stable():
    b = [_doc("a.md"), _doc("b.md")]
    assert _batch_key(b) == _batch_key([_doc("b.md"), _doc("a.md")])  # 顺序无关


def test_parse_agent_output_builds_candidates():
    batch = [_doc("a.md", fid="GWFD-001")]
    raw = json.dumps({"a.md": [{"step_range": [1, 1], "candidate_desc": "x", "commands": ["ADD URR"]}]})
    res = parse_agent_output(raw, batch)
    assert "a.md" in res
    c = res["a.md"][0]
    assert c["feature_id"] == "GWFD-001"
    assert c["candidate_id"] == "GWFD-001#001"
    assert c["doc_path"] == "a.md"
