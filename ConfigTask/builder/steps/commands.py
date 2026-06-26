# ConfigTask/builder/steps/commands.py
"""规则步4+5 commands：按 task 的 step_range 从操作步骤抽命令，构造 command_ref。

为每个 task 填 task['commands'] = [{command_ref}]（parameters 留给 params 步）。
agent_pending task（step_range 覆盖整段）也抽，后续 Agent 分组时再重组。
"""
from builder.steps.registry import step
from builder.core.commands import commands_for_range
from builder.constants import SECTION_STEPS


@step("commands")
def run(ctx):
    nf, version = ctx["nf"], ctx["version"]
    total = 0
    for feat in ctx["features"]:
        steps_text = feat["sections"].get(SECTION_STEPS, "")
        for task in feat["tasks"]:
            refs = commands_for_range(steps_text, task["step_range"], nf, version)
            task["commands"] = [{"command_ref": r} for r in refs]
            total += len(refs)
    return total
