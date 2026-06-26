# ConfigTask/builder/steps/verify_split.py
"""Step 2 核查：对 Agent-1 产出做完整性/连续性/对象族检查。"""
import json

from builder.steps.registry import step
from builder.verify.completeness import verify_completeness
from builder.verify.contiguity import verify_contiguity
from builder.verify.object_family import verify_family_coherence


def verify_candidate(doc, candidates):
    """对单份文档的 candidates 做全维度核查。

    Returns:
        list[str]: 错误列表（HARD: = 硬约束，WARN: = 软约束）
    """
    errors = []

    # 硬约束：完整性
    comp_errors = verify_completeness(doc, candidates)
    errors.extend(f"HARD: {e}" for e in comp_errors)

    # 硬约束：连续性
    total_steps = doc.get("num_steps", 0)
    cont_errors = verify_contiguity(candidates, total_steps)
    errors.extend(f"HARD: {e}" for e in cont_errors)

    # 硬约束：非空
    for i, c in enumerate(candidates):
        if not c.get("commands"):
            errors.append(f"HARD: candidate[{i}] 无命令")

    # 软约束：对象族
    for i, c in enumerate(candidates):
        fam_warnings = verify_family_coherence(c.get("commands", []))
        errors.extend(f"WARN: candidate[{i}] {w}" for w in fam_warnings)

    return errors


@step("verify_split")
def run(ctx):
    """核查 task_candidates.jsonl。"""
    doc_steps_path = ctx["data_dir"] / "doc_steps.jsonl"
    candidates_path = ctx["data_dir"] / "task_candidates.jsonl"

    if not candidates_path.exists():
        print("  跳过：task_candidates.jsonl 不存在")
        return 0

    docs = {}
    with open(doc_steps_path, encoding="utf-8") as f:
        for line in f:
            d = json.loads(line)
            docs[d["doc_path"]] = d

    doc_candidates = {}
    with open(candidates_path, encoding="utf-8") as f:
        for line in f:
            c = json.loads(line)
            doc_candidates.setdefault(c["doc_path"], []).append(c)

    total_errors = 0
    for doc_path, doc in docs.items():
        candidates = doc_candidates.get(doc_path, [])
        errors = verify_candidate(doc, candidates)
        hard = [e for e in errors if e.startswith("HARD:")]
        if hard:
            print(f"  FAIL {doc_path}: {hard}")
            total_errors += len(hard)

    if total_errors == 0:
        print(f"  核查通过: {len(docs)} 份文档")
    else:
        print(f"  核查失败: {total_errors} 个硬约束错误")

    return total_errors
