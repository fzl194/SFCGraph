# ConfigTask/builder/steps/split_tasks.py
"""Step 2: Agent 拆 task（per-doc, 每批 agent_batch_size 份）。

Agent 调用由执行者触发（Agent 工具 / subagent dispatch）。
本文件负责：输入构造 + 输出解析 + 进度管理 + 核查接线。
"""
import json
import re

from builder.steps.registry import step
from builder.agent.prompts import SPLIT_TASKS_PROMPT
from builder.agent.runner import run_agent_step
from builder.steps.verify_split import verify_candidate


def build_agent_input(batch):
    """构造 Agent 输入。"""
    return [
        {
            "doc_path": doc["doc_path"],
            "feature_id": doc.get("feature_id", ""),
            "num_steps": doc["num_steps"],
            "steps": [
                {"step_num": s["step_num"], "step_desc": s["step_desc"], "commands": s["commands"]}
                for s in doc["steps"]
            ],
        }
        for doc in batch
    ]


def build_prompt(batch):
    """构造 Agent prompt 字符串。"""
    input_data = build_agent_input(batch)
    return SPLIT_TASKS_PROMPT.format(
        n_docs=len(batch),
        doc_key=batch[0]["doc_path"] if batch else "",
        input_json=json.dumps(input_data, ensure_ascii=False, indent=2),
    )


def parse_agent_output(raw_text, batch):
    """解析 Agent 输出文本 → {doc_path: [candidate, ...]}。"""
    # 提取 JSON
    if isinstance(raw_text, dict):
        data = raw_text
    else:
        json_match = re.search(r'\{.*\}', raw_text, re.DOTALL)
        if not json_match:
            return {}
        data = json.loads(json_match.group())

    results = {}
    for doc in batch:
        doc_path = doc["doc_path"]
        cands_raw = data.get(doc_path, [])
        candidates = []
        for i, c in enumerate(cands_raw):
            candidates.append({
                "doc_path": doc_path,
                "feature_id": doc.get("feature_id", ""),
                "candidate_id": f"{doc.get('feature_id', 'UNKNOWN')}#{i+1:03d}",
                "step_range": c.get("step_range"),
                "candidate_desc": c.get("candidate_desc", ""),
                "commands": c.get("commands", []),
                "boundary_source": "agent",
            })
        results[doc_path] = candidates
    return results


@step("split_tasks", output_file="task_candidates.jsonl")
def run(ctx):
    """Agent-1: 拆 task。

    执行方式：
    1. 本函数读 doc_steps.jsonl，找出未处理的文档
    2. 构造 Agent prompt 并输出（执行者用 Agent 工具调）
    3. 执行者把 Agent 返回写入 task_candidates.jsonl
    4. 重跑 verify_split 核查
    """
    doc_steps_path = ctx["data_dir"] / "doc_steps.jsonl"
    all_docs = []
    with open(doc_steps_path, encoding="utf-8") as f:
        for line in f:
            all_docs.append(json.loads(line))

    progress = run_agent_step.__wrapped__ if hasattr(run_agent_step, '__wrapped__') else None

    # 简化版：输出第一批待处理的 prompt，执行者手动调 Agent
    from builder.agent.runner import load_progress
    progress = load_progress(ctx, "split_tasks")

    todo = [d for d in all_docs if progress.get(d["doc_path"]) != "ok"]
    if not todo:
        print(f"  全部已完成 ({len(progress)}/{len(all_docs)})")
        return 0

    batch_size = ctx.get("agent_batch_size", 5)
    batch = todo[:batch_size]

    prompt = build_prompt(batch)
    print(f"  待处理: {len(todo)} 份, 当前批次: {len(batch)} 份")
    print(f"  PROMPT:\n{prompt[:500]}...")
    print(f"\n  执行者请用 Agent 工具发送完整 prompt，返回结果写入 task_candidates.jsonl")
    print(f"  然后运行: python build_all.py UDG 20.15.2 verify_split")
    return len(todo)
