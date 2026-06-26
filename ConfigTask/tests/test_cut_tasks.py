# ConfigTask/tests/test_cut_tasks.py
from builder.core.cut_tasks import count_steps, cut_tasks_by_phases

# 内容计费 5 phase（step_range 来自 flow_parser）
_PHASES = [
    {"phase_name": "配置业务费率", "step_range": (1, 2)},
    {"phase_name": "配置过滤规则", "step_range": (3, 5)},
    {"phase_name": "业务策略规则", "step_range": (6, 6)},
    {"phase_name": "配置USERPROFILE", "step_range": (7, 8)},
    {"phase_name": "配置缺省费率", "step_range": (9, 9)},
]


def test_count_steps():
    steps = "1. 配置URR。\n  ADD URR\n2. 配置URR组。\n a. 子步骤\n3. 配置PCC策略组。"
    assert count_steps(steps) == 3


def test_cut_5_tasks_unassigned_attach_to_last():
    """内容计费：5 phase，11 步；步骤10-11 未被 phase 覆盖 → 归入 phase⑤。"""
    tasks = cut_tasks_by_phases(_PHASES, total_steps=11)
    assert len(tasks) == 5
    # 前 4 个 step_range 不变
    assert tasks[0]["step_range"] == (1, 2)
    assert tasks[3]["step_range"] == (7, 8)
    # phase⑤ 原 (9,9)，吸收 10、11 → (9,11)
    assert tasks[4]["phase_name"] == "配置缺省费率"
    assert tasks[4]["step_range"] == (9, 11)
    assert all(t["boundary_source"] == "flow" for t in tasks)


def test_cut_no_unassigned_when_total_covers_all():
    """总步数正好被 phase 覆盖时，无附加。"""
    phases = [{"phase_name": "A", "step_range": (1, 2)}, {"phase_name": "B", "step_range": (3, 4)}]
    tasks = cut_tasks_by_phases(phases, total_steps=4)
    assert tasks[0]["step_range"] == (1, 2)
    assert tasks[1]["step_range"] == (3, 4)
