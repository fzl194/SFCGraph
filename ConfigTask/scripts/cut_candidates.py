"""Phase 2 Step 2：单文档内切 Task 候选。

双模式：
- 有操作流程（91 份）→ 规则切（flow_parser + cut_tasks，已验证）
- 无操作流程（564 份）→ 标记 boundary_source=agent_pending，留给 Agent 切

产出：ConfigTask/data/task_candidates.jsonl
每条 = 一个 task candidate（一份文档可产出多个 candidate）
"""
import json
import re
import sys
import pathlib

PROJECT_ROOT = pathlib.Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(PROJECT_ROOT / "ConfigTask"))

from builder.core.flow_parser import parse_flow
from builder.core.cut_tasks import count_steps, cut_tasks_by_phases
from builder.constants import SECTION_FLOW, SECTION_STEPS

DATA_DIR = PROJECT_ROOT / "ConfigTask" / "data"


def cut_with_flow(steps: list) -> list:
    """规则模式：有操作流程的文档，用 flow_parser + cut_tasks 切。

    steps = doc_steps.jsonl 里的 steps 列表。
    返回 task candidate 列表。
    """
    # 从 doc_steps.jsonl 里无法直接拿到操作流程原文（只有 steps），
    # 但 has_operation_flow=True 说明文档有操作流程段。
    # 我们需要读原文拿操作流程段——但 doc_steps.jsonl 没存操作流程段文本。
    # 所以规则模式需要回到原文。
    # → 这个函数应该在 extract_steps.py 阶段就处理，而不是后处理。
    # 暂时返回 None，标记需要回原文处理。
    return None


def cut_without_flow(steps: list, doc_path: str, feature_id: str) -> list:
    """无操作流程 → 简单策略：整份文档作为 1 个 candidate，标 agent_pending。

    Agent 在后续步骤里根据 step_desc 语义分段。
    """
    all_commands = []
    for s in steps:
        all_commands.extend(s["commands"])
    return [{
        "candidate_id": f"{feature_id}#cand-001",
        "step_range": [steps[0]["step_num"], steps[-1]["step_num"]] if steps else None,
        "candidate_desc": "",  # 待 Agent 填
        "commands": all_commands,
        "boundary_source": "agent_pending",
        "step_count": len(steps),
    }]


def main():
    doc_steps_path = DATA_DIR / "doc_steps.jsonl"
    output_path = DATA_DIR / "task_candidates.jsonl"

    # 读原文缓存（避免重复读文件）
    from builder.core.md_reader import read_sections

    candidates = []
    stats = {"rule_cut": 0, "agent_pending": 0, "total_candidates": 0}

    with open(doc_steps_path, encoding="utf-8") as f:
        for line in f:
            doc = json.loads(line)
            doc_path = PROJECT_ROOT / doc["doc_path"]
            feature_id = doc.get("feature_id", "")
            steps = doc["steps"]

            if doc["has_operation_flow"] and doc_path.exists():
                # 规则模式：读原文操作流程段 → flow_parser → cut_tasks
                md_text = doc_path.read_text(encoding="utf-8", errors="ignore")
                sections = read_sections(md_text)
                flow_text = sections.get(SECTION_FLOW, "")
                steps_text = sections.get(SECTION_STEPS, "")

                if flow_text:
                    phases = parse_flow(flow_text)
                    total_steps = count_steps(steps_text)
                    tasks = cut_tasks_by_phases(phases, total_steps)

                    if tasks:
                        # 把 step_range 映射到 commands
                        for i, task in enumerate(tasks):
                            sr = task["step_range"]
                            cmds = []
                            if sr:
                                for s in steps:
                                    if sr[0] <= s["step_num"] <= sr[1]:
                                        cmds.extend(s["commands"])
                            candidates.append({
                                "doc_path": doc["doc_path"],
                                "feature_id": feature_id,
                                "candidate_id": f"{feature_id}#cand-{i+1:03d}",
                                "step_range": list(sr) if sr else None,
                                "candidate_desc": task.get("phase_name", ""),
                                "commands": cmds,
                                "boundary_source": "flow",
                                "step_count": (sr[1] - sr[0] + 1) if sr else 0,
                            })
                        stats["rule_cut"] += 1
                        stats["total_candidates"] += len(tasks)
                        continue

            # 无操作流程 / 规则模式失败 → agent_pending
            cands = cut_without_flow(steps, doc["doc_path"], feature_id)
            for c in cands:
                c["doc_path"] = doc["doc_path"]
            candidates.extend(cands)
            stats["agent_pending"] += 1
            stats["total_candidates"] += len(cands)

    # 写产出
    with open(output_path, "w", encoding="utf-8") as f:
        for c in candidates:
            f.write(json.dumps(c, ensure_ascii=False) + "\n")

    print(f"产出 candidate 数: {stats['total_candidates']}")
    print(f"规则切文档: {stats['rule_cut']}（每份切出多个 candidate）")
    print(f"Agent 待切文档: {stats['agent_pending']}（每份暂为 1 个 candidate）")
    print(f"产出文件: {output_path}")


if __name__ == "__main__":
    main()
