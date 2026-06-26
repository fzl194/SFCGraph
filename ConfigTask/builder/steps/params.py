# ConfigTask/builder/steps/params.py
"""规则步6 params：按命令从数据规划表抽参数，构造 parameter_ref + reference_hint。

为每个 task.commands[i] 填 parameters = [{parameter_ref, reference_hint}]。
binding_type 留给 Agent 步（语义分类）。
"""
from builder.steps.registry import step
from builder.core.params import parse_param_table
from builder.constants import SECTION_DATA, PARAM_REF_TMPL


@step("params")
def run(ctx):
    nf, version = ctx["nf"], ctx["version"]
    total = 0
    for feat in ctx["features"]:
        table = parse_param_table(feat["sections"].get(SECTION_DATA, ""))
        for task in feat["tasks"]:
            for cmd_entry in task["commands"]:
                cmd_name = cmd_entry["command_ref"].split("@MMLCommand@", 1)[1]
                params = table.get(cmd_name, [])
                cmd_entry["parameters"] = [
                    {
                        "parameter_ref": PARAM_REF_TMPL.format(
                            nf=nf, version=version, cmd=cmd_name, param=p["parameter_name"]),
                        "reference_hint": p["reference_hint"],
                    }
                    for p in params
                ]
                total += len(cmd_entry["parameters"])
    return total
