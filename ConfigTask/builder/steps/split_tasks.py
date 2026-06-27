# ConfigTask/builder/steps/split_tasks.py
"""Step 2 (Agent-1): 拆 task —— prep / pause / ingest 模型。

不调 LLM。纯文件交接：
- prep：pending docs（不在 task_candidates.jsonl 的）分批 → 全部 prompt 写到
        data/agent_prompts/split_tasks/{key}.txt（key = 批内 doc 集合哈希，稳定）
- check：data/agent_outputs/split_tasks/{key}.json 齐了 → ingest；未齐 → 返回 "PAUSE"
- ingest：解析输出 → 追加 task_candidates.jsonl（done 从输出派生：doc_path 在 candidates 里）

build_all 遇 PAUSE 停；调 Agent 写输出后重跑 build_all 即续。
"""
import json
import hashlib

from builder.steps.registry import step
from builder.agent.prompts import SPLIT_TASKS_PROMPT


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
    """解析 Agent 输出 → {doc_path: [candidate, ...]}。

    输出可为 dict 或含 JSON 的文本。每 doc 的 candidate 补 doc_path/feature_id/candidate_id。
    """
    import re
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


def _batch_key(batch):
    """批内 doc 集合的稳定哈希（sorted doc_path）→ batch_<hash8>。"""
    h = hashlib.md5("|".join(sorted(d["doc_path"] for d in batch)).encode()).hexdigest()[:8]
    return f"batch_{h}"


@step("split_tasks", output_file="task_candidates.jsonl", agent=True)
def run(ctx):
    """prep → check → ingest。返回 int=完成数 / "PAUSE"=待回填。"""
    data_dir = ctx["data_dir"]
    prompts_dir = data_dir / "agent_prompts" / "split_tasks"
    outputs_dir = data_dir / "agent_outputs" / "split_tasks"
    prompts_dir.mkdir(parents=True, exist_ok=True)
    outputs_dir.mkdir(parents=True, exist_ok=True)

    # 读 doc_steps
    all_docs = []
    with open(data_dir / "doc_steps.jsonl", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                all_docs.append(json.loads(line))

    # done = doc_path 已在 task_candidates.jsonl（输出派生）
    cand_path = data_dir / "task_candidates.jsonl"
    done_docs = set()
    if cand_path.exists():
        with open(cand_path, encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:
                    done_docs.add(json.loads(line)["doc_path"])

    # rerun：强制把匹配 doc 当 pending（重抽）
    rerun = ctx.get("rerun_target")
    pending_docs = [d for d in all_docs
                    if (d["doc_path"] not in done_docs) or (rerun and rerun in d["doc_path"])]

    if not pending_docs:
        print(f"  全部已完成 ({len(done_docs)}/{len(all_docs)} 文档)")
        return len(done_docs)

    # 分批
    batch_size = ctx.get("agent_batch_size", 5)
    batches = [pending_docs[i:i + batch_size]
               for i in range(0, len(pending_docs), batch_size)]

    # prep：每批写 prompt（幂等）
    for batch in batches:
        key = _batch_key(batch)
        (prompts_dir / f"{key}.txt").write_text(build_prompt(batch), encoding="utf-8")

    # check + ingest：输出齐了的批回填
    ingested = 0
    still_pending = []
    with open(cand_path, "a", encoding="utf-8") as f:
        for batch in batches:
            key = _batch_key(batch)
            out_file = outputs_dir / f"{key}.json"
            if not out_file.exists():
                still_pending.append(key)
                continue
            results = parse_agent_output(out_file.read_text(encoding="utf-8"), batch)
            for doc_path, cands in results.items():
                for c in cands:
                    f.write(json.dumps(c, ensure_ascii=False) + "\n")
                    ingested += 1

    if still_pending:
        print(f"  prep: {len(batches)} 批 prompt 已就绪 → {prompts_dir}")
        print(f"  已回填 {ingested} candidate；仍待处理 {len(still_pending)} 批:")
        for k in still_pending[:12]:
            print(f"    - {prompts_dir}/{k}.txt  →  写输出到 {outputs_dir}/{k}.json")
        if len(still_pending) > 12:
            print(f"    ... 等 {len(still_pending) - 12} 批")
        return "PAUSE"

    print(f"  全部回填: {ingested} candidate（{len(batches)} 批）")
    return ingested
