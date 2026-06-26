# ConfigTask/tests/test_flow_parser.py
from builder.core.flow_parser import parse_flow

# 内容计费·部署 的操作流程段（真实结构）
_FLOW = """新增或修改内容计费业务分为如下几个配置步骤：

1. 配置业务费率。配置业务流规则匹配的费率（对应URRID）、计费方式（在线、离线）。对应操作步骤见[步骤 1](#xxx)-[步骤 2](#xxx)。
2. 配置过滤规则。过滤规则包含三四层过滤条件和七层过滤条件。对应操作步骤见[步骤 3](#xxx)-[步骤 5](#xxx)。
3. 将业务费率和业务过滤器绑定为业务策略规则，业务策略规则通过ADD RULE命令配置。对应的操作步骤见[步骤 6](#xxx)。
4. 配置USERPROFILE。通过ADD USERPROFILE命令配置规则组。对应操作步骤见[步骤 7](#xxx)-[步骤 8](#xxx)。
5. 配置缺省费率。通过SET URRGRPBINDING配置规则组下的默认费率规则。对应的操作步骤见[步骤 9](#xxx)。
"""


def test_parses_five_phases_with_ranges():
    phases = parse_flow(_FLOW)
    assert len(phases) == 5
    assert phases[0]["phase_name"] == "配置业务费率"
    assert phases[0]["step_range"] == (1, 2)
    assert phases[1]["phase_name"] == "配置过滤规则"
    assert phases[1]["step_range"] == (3, 5)
    # 单步骤 phase → (n, n)
    assert phases[2]["step_range"] == (6, 6)
    assert phases[3]["step_range"] == (7, 8)
    assert phases[4]["step_range"] == (9, 9)


def test_empty_when_no_flow():
    """无操作流程段（空文本）→ 空列表。"""
    assert parse_flow("") == []
    assert parse_flow("一些没有编号阶段的文字") == []
