"""把 Agent 批次结果追加到 task_candidates.jsonl。
Agent 输出 = {doc_path: [{step_range, candidate_desc, commands}, ...]}
从 doc_steps.jsonl 读 feature_id，构造完整 candidate 记录。
"""
import json
import sys
import pathlib

CONFIGTASK_DIR = pathlib.Path(__file__).resolve().parent.parent
DATA_DIR = CONFIGTASK_DIR / "data"

# 读 doc_steps 建立 doc_path → feature_id 映射 + doc_path → steps 映射
doc_info = {}
with open(DATA_DIR / "doc_steps.jsonl", encoding="utf-8") as f:
    for line in f:
        d = json.loads(line)
        doc_info[d["doc_path"]] = d


def process_agent_output(agent_json_str, output_file):
    """解析 Agent JSON 输出 → 追加 candidate 到 output_file。"""
    # 提取 JSON
    json_match = __import__("re").search(r'\{.*\}', agent_json_str, __import__("re").DOTALL)
    if not json_match:
        print("ERROR: 未找到 JSON")
        return 0
    data = json.loads(json_match.group())

    count = 0
    with open(output_file, "a", encoding="utf-8") as f:
        for doc_path, candidates in data.items():
            doc = doc_info.get(doc_path)
            if not doc:
                print(f"  WARN: doc_path 不在 doc_steps: {doc_path[:60]}")
                continue
            fid = doc.get("feature_id", "")
            for i, c in enumerate(candidates):
                sr = c.get("step_range")
                # 从原 steps 精确取 commands（保证不遗漏）
                cmds = []
                if sr and len(sr) == 2:
                    for s in doc["steps"]:
                        if sr[0] <= s["step_num"] <= sr[1]:
                            cmds.extend(s["commands"])
                else:
                    cmds = c.get("commands", [])

                record = {
                    "doc_path": doc_path,
                    "feature_id": fid,
                    "candidate_id": f"{fid}#{i+1:03d}" if fid else f"BATCH#{count+1:03d}",
                    "step_range": sr,
                    "candidate_desc": c.get("candidate_desc", ""),
                    "commands": cmds,
                    "boundary_source": "agent",
                }
                f.write(json.dumps(record, ensure_ascii=False) + "\n")
                count += 1
    return count


# Agent 批次1输出文件
batch1_file = sys.argv[1] if len(sys.argv) > 1 else None
batch2_file = sys.argv[2] if len(sys.argv) > 2 else None

output_file = DATA_DIR / "task_candidates.jsonl"
total = 0

if batch1_file:
    with open(batch1_file, encoding="utf-8") as f:
        n = process_agent_output(f.read(), output_file)
    print(f"批次1: +{n} candidates")
    total += n

if batch2_file:
    with open(batch2_file, encoding="utf-8") as f:
        n = process_agent_output(f.read(), output_file)
    print(f"批次2: +{n} candidates")
    total += n

print(f"总计追加: {total} candidates")
