# ConfigTask/builder/steps/cut_boundaries.py
"""规则步3 cut_boundaries：读 md → md_reader → flow_parser → 切 task 边界。

- 有操作流程：phase → task（未覆盖步骤按连续性归前一个 task）
- 无操作流程（接入控制/eDRX）：产 1 个 agent_pending candidate，待 Agent 分组（决策 B）

产出 ctx['features'] = [{feature_id, doc_path, sections, tasks}]
"""
from builder.steps.registry import step
from builder.core.md_reader import read_sections
from builder.core.flow_parser import parse_flow
from builder.core.cut_tasks import count_steps, cut_tasks_by_phases
from builder.constants import SECTION_FLOW, SECTION_STEPS


@step("cut_boundaries")
def run(ctx):
    features = []
    for doc in ctx["feature_docs"]:
        md = open(doc.doc_path, encoding="utf-8").read()
        sections = read_sections(md)
        phases = parse_flow(sections.get(SECTION_FLOW, ""))
        total = count_steps(sections.get(SECTION_STEPS, ""))
        if phases:
            tasks = cut_tasks_by_phases(phases, total)
        else:
            # 决策 B：无操作流程 → 1 candidate，整段命令序列待 Agent 分组
            tasks = [{
                "phase_name": None,
                "step_range": (1, total) if total else None,
                "boundary_source": "agent_pending",
            }]
        features.append({
            "feature_id": doc.feature_id,
            "doc_path": doc.doc_path,
            "sections": sections,
            "tasks": tasks,
        })
    ctx["features"] = features
    return sum(len(f["tasks"]) for f in features)
