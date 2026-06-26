# ConfigTask/builder/core/cut_tasks.py
"""task 边界切割核心逻辑（纯函数，可单测）。

- 有操作流程：phase → task；未被 phase 覆盖的步骤按连续性归入前一 task。
- 无操作流程：调用方负责产 1 个 agent_pending candidate（决策 B）。
"""
import re

# 操作步骤项：行首 "数字. "
_STEP_ITEM_RE = re.compile(r'^\d+\.\s', re.MULTILINE)


def count_steps(steps_text: str) -> int:
    """数操作步骤段的步骤数（行首 N. 出现次数）。"""
    return len(_STEP_ITEM_RE.findall(steps_text))


def cut_tasks_by_phases(phases: list, total_steps: int) -> list:
    """phase → task 边界；未覆盖步骤按连续性归入 step_range 最大的前一个 task。

    Args:
        phases: flow_parser 输出 [{phase_name, step_range}]
        total_steps: 操作步骤总步数
    Returns:
        [{phase_name, step_range, boundary_source:"flow"}]
    """
    tasks = [
        {"phase_name": p["phase_name"], "step_range": p["step_range"], "boundary_source": "flow"}
        for p in phases
    ]
    if not total_steps:
        return tasks
    # 收集已覆盖步骤
    covered = set()
    for t in tasks:
        if t["step_range"]:
            covered.update(range(t["step_range"][0], t["step_range"][1] + 1))
    # 未覆盖步骤归入"step_range.end < s 中最大的那个 task"（连续性兜底）
    for s in range(1, total_steps + 1):
        if s in covered:
            continue
        target = None
        for t in tasks:
            if t["step_range"] and t["step_range"][1] < s:
                target = t  # 取最后一个满足的
        if target:
            target["step_range"] = (target["step_range"][0], s)
            covered.add(s)
    return tasks
