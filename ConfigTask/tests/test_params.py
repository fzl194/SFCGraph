# ConfigTask/tests/test_params.py
from builder.core.params import parse_param_table
from builder.steps.params import run

_DATA = """前提条件
- 请阅读特性。

数据

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| **ADD URR** | 使用量上报规则名称（URRNAME） | URR_URL | 本端规划 | - |
| **ADD URR** | URR标识（URRID） | 12500 | 全网规划 | - |
| **ADD URRGROUP** | 使用量上报规则组名称（URRGROUPNAME） | UrrGp_URL | 本端规划 | - |
| **ADD URRGROUP** | 上行发起URR名称1（UPURRNAME1） | URR_URL | 已配置数据中获取 | - |
| **ADD URR** | 使用量上报规则名称（URRNAME） | URR_IMS | 本端规划 | - |
"""


def test_parse_param_table_extracts_and_marks_reference():
    t = parse_param_table(_DATA)
    assert [p["parameter_name"] for p in t["ADD URR"]] == ["URRNAME", "URRID"]  # 跨表去重 URRNAME
    urrnames = [p for p in t["ADD URR"] if p["parameter_name"] == "URRNAME"]
    assert urrnames[0]["reference_hint"] is False
    up = [p for p in t["ADD URRGROUP"] if p["parameter_name"] == "UPURRNAME1"][0]
    assert up["reference_hint"] is True


def test_params_step_fills_command_parameters():
    ctx = {
        "nf": "UDG", "version": "20.15.2",
        "features": [{
            "feature_id": "GWFD-020301",
            "sections": {"数据规划表": _DATA},
            "tasks": [{
                "phase_name": "配置业务费率", "step_range": (1, 1),
                "commands": [{"command_ref": "UDG@20.15.2@MMLCommand@ADD URR"}],
            }],
        }],
    }
    run(ctx)
    params = ctx["features"][0]["tasks"][0]["commands"][0]["parameters"]
    refs = [p["parameter_ref"] for p in params]
    assert "UDG@20.15.2@CommandParameter@ADD URR:URRNAME" in refs
    assert "UDG@20.15.2@CommandParameter@ADD URR:URRID" in refs
