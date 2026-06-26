# ConfigTask/tests/test_commands.py
from builder.core.commands import parse_step_commands, commands_for_range
from builder.steps.commands import run

_STEPS = """1. 配置使用量上报规则组属性。
    a. 配置URR。
      **ADD URR**
    b. 配置URR组。
      **ADD URRGROUP**
2. 配置PCC策略组。
  **ADD PCCPOLICYGRP**
3. 配置过滤条件。
  **ADD FILTER**
"""


def test_parse_step_commands_captures_substeps():
    sc = parse_step_commands(_STEPS)
    assert sc[1] == ["ADD URR", "ADD URRGROUP"]   # 子步骤 a/b 都在 step1
    assert sc[2] == ["ADD PCCPOLICYGRP"]
    assert sc[3] == ["ADD FILTER"]


def test_commands_for_range_constructs_refs():
    refs = commands_for_range(_STEPS, (1, 2), "UDG", "20.15.2")
    assert refs == [
        "UDG@20.15.2@MMLCommand@ADD URR",
        "UDG@20.15.2@MMLCommand@ADD URRGROUP",
        "UDG@20.15.2@MMLCommand@ADD PCCPOLICYGRP",
    ]


def test_commands_step_fills_task():
    ctx = {
        "nf": "UDG", "version": "20.15.2",
        "features": [{"feature_id": "GWFD-020301", "sections": {"操作步骤": _STEPS},
                      "tasks": [{"step_range": (1, 2), "phase_name": "配置业务费率"}]}],
    }
    n = run(ctx)
    assert n == 3
    cmds = ctx["features"][0]["tasks"][0]["commands"]
    assert [c["command_ref"] for c in cmds] == [
        "UDG@20.15.2@MMLCommand@ADD URR",
        "UDG@20.15.2@MMLCommand@ADD URRGROUP",
        "UDG@20.15.2@MMLCommand@ADD PCCPOLICYGRP",
    ]
