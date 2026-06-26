# ConfigTask/builder/steps/assemble.py
"""规则步9 assemble：把 features/tasks 拼成 ConfigTask 骨架 dict 列表。

填身份/来源字段；语义字段（task_logical_name/task_goal/task_summary）留空、
binding_type 未填——都交给后续 Agent。raw_steps_text 存原文切片（raw_steps_text_raw），
Agent 步压缩为指令式。
"""
from builder.steps.registry import step
from builder.core.commands import steps_text_for_range
from builder.constants import ID_TMPL, STATUS_ACTIVE, CATEGORY_CONFIG, SECTION_STEPS


@step("assemble")
def run(ctx):
    nf, version = ctx["nf"], ctx["version"]
    seq = 0
    skeleton = []
    for feat in ctx["features"]:
        steps_text = feat["sections"].get(SECTION_STEPS, "")
        for task in feat["tasks"]:
            seq += 1
            skeleton.append({
                "task_id": ID_TMPL.format(nf=nf, version=version, seq=seq),
                "task_logical_name": "",            # Agent 填（phase 名归一化）
                "nf": nf,
                "version": version,
                "raw_steps_text_raw": steps_text_for_range(steps_text, task["step_range"]),
                "task_goal": "",                    # Agent 填
                "task_summary": "",                 # Agent 填
                "commands": task["commands"],       # command_ref + parameters(含 reference_hint)，binding_type 待 Agent
                "task_category": CATEGORY_CONFIG,
                "status": STATUS_ACTIVE,
                "source_evidence_ids": [feat["doc_path"]],
                # hint（给 Agent 用，最终 emit 前清掉）
                "_phase_hint": task.get("phase_name"),
                "_boundary_source": task.get("boundary_source"),
                "_feature_id": feat["feature_id"],
            })
    ctx["skeleton"] = skeleton
    return len(skeleton)
