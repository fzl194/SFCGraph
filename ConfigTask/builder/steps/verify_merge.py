# ConfigTask/builder/steps/verify_merge.py
"""Step 核查：对 Agent-2（merge_fields）产出的 ConfigTask 做字段/枚举校验。

HARD（拒绝，需重抽）：
- task_logical_name / task_goal / task_summary 非空
- commands 非空；每 command_ref 非空
- 每参数 binding_type ∈ {fixed, variable, reference}
- variable → variable_source ∈ {local_planned, global_planned, peer_planned, decision_driven}
- fixed → 有 fixed_value
WARN（提醒）：缺 _decision_points / _split_notes（中间态种子）
"""
import json

from builder.steps.registry import step

_BINDING = {"fixed", "variable", "reference"}
_VSOURCE = {"local_planned", "global_planned", "peer_planned", "decision_driven"}


def verify_task(task):
    """返回错误列表，每条前缀 HARD: 或 WARN:。空表 = 通过。"""
    errors = []
    for f in ("task_logical_name", "task_goal", "task_summary"):
        if not task.get(f):
            errors.append(f"HARD:{f} 为空")

    cmds = task.get("commands", [])
    if not cmds:
        errors.append("HARD:commands 为空")
    for c in cmds:
        if not c.get("command_ref"):
            errors.append("HARD:command_ref 为空")
        for p in c.get("parameters", []):
            ref = p.get("parameter_ref", "?")
            bt = p.get("binding_type")
            if bt not in _BINDING:
                errors.append(f"HARD:{ref} binding_type 非法/缺失: {bt}")
                continue
            if bt == "variable":
                if p.get("variable_source") not in _VSOURCE:
                    errors.append(f"HARD:{ref} variable 但 variable_source 非法/缺失: {p.get('variable_source')}")
            elif bt == "fixed":
                if not p.get("fixed_value"):
                    errors.append(f"HARD:{ref} fixed 但无 fixed_value")

    if "_decision_points" not in task and "decision_points" not in task:
        errors.append("WARN:缺 decision_points（下一阶段规则抽取的种子）")
    if "_split_notes" not in task and "split_notes" not in task:
        errors.append("WARN:缺 split_notes")
    return errors


@step("verify_merge")
def run(ctx):
    data_dir = ctx["data_dir"]
    path = data_dir / "config_tasks.jsonl"
    if not path.exists():
        print("  跳过: config_tasks.jsonl 不存在")
        return 0

    tasks = [json.loads(line) for line in open(path, encoding="utf-8") if line.strip()]
    hard = warn = 0
    hard_tasks = []
    for t in tasks:
        errs = verify_task(t)
        h = [e for e in errs if e.startswith("HARD:")]
        w = [e for e in errs if e.startswith("WARN:")]
        hard += len(h)
        warn += len(w)
        if h:
            hard_tasks.append((t.get("task_id", "?"), h))

    print(f"  校验 {len(tasks)} task: HARD {hard}, WARN {warn}")
    for tid, h in hard_tasks[:15]:
        print(f"    HARD {tid}: {h}")
    if hard:
        print(f"  [HARD] {len(hard_tasks)} task 有 HARD 错误，需重抽（删对应 data/agent_outputs/merge_fields/<cid>.json 后重跑）")
    elif not warn:
        print(f"  [OK] 全部通过")
    return len(tasks)
