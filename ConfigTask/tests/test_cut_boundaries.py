# ConfigTask/tests/test_cut_boundaries.py
from builder.steps.cut_boundaries import run
from builder.core.csv_loader import FeatureDoc

# 内容计费·部署 风格：5 phase + 11 步（步骤10-11 未被 phase 收编）
_MD_WITH_FLOW = """# 部署UPF

## [必备事项](#xxx)
前提条件
数据
| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| **ADD URR** | URRNAME | URR_URL | 本端规划 | - |

## [操作流程](#xxx)
1. 配置业务费率。对应操作步骤见[步骤 1](#xxx)-[步骤 2](#xxx)。
2. 配置过滤规则。对应操作步骤见[步骤 3](#xxx)-[步骤 5](#xxx)。
3. 业务策略规则。对应操作步骤见[步骤 6](#xxx)。
4. 配置USERPROFILE。对应操作步骤见[步骤 7](#xxx)-[步骤 8](#xxx)。
5. 配置缺省费率。对应操作步骤见[步骤 9](#xxx)。

## [操作步骤](#xxx)
1. 配置URR。
  **ADD URR**
2. 配置URR组。
  **ADD URRGROUP**
3. 配置过滤条件。
  **ADD FILTER**
4. 配置流过滤器。
  **ADD FLOWFILTER**
5. 绑定。
  **ADD FLTBINDFLOWF**
6. 添加规则。
  **ADD RULE**
7. 添加User Profile。
  **ADD USERPROFILE**
8. 绑定规则。
  **ADD RULEBINDING**
9. 配置缺省费率。
  **SET URRGRPBINDING**
10. 配置防欺诈。
  **ADD SPECURRGRPLIST**
11. 刷新生效。
  **SET REFRESHSRV**

## [任务示例](#xxx)
ADD URR:URRNAME="URR_URL";
"""

# 接入控制·激活 风格：无操作流程
_MD_NO_FLOW = """# 激活接入控制

## [必备事项](#xxx)
数据
| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| **ADD APN** | APN | apn | 本端规划 | - |

## [操作步骤](#xxx)
1. 增加APN实例。
  **ADD APN**
2. 绑定带宽控制方式。
  **SET APNQOSATTR**

## [任务示例](#xxx)
ADD APN:APN="apn";
"""


def test_cut_with_flow_5_tasks(tmp_path):
    md = tmp_path / "部署UPF.md"
    md.write_text(_MD_WITH_FLOW, encoding="utf-8")
    ctx = {"feature_docs": [FeatureDoc("GWFD-020301", "UDG", str(md))]}
    n = run(ctx)
    assert n == 5
    tasks = ctx["features"][0]["tasks"]
    assert tasks[0]["step_range"] == (1, 2)
    assert tasks[4]["step_range"] == (9, 11)   # phase⑤ 吸收 10、11
    assert tasks[4]["boundary_source"] == "flow"
    assert ctx["features"][0]["sections"]      # sections 已存


def test_cut_no_flow_one_agent_pending(tmp_path):
    md = tmp_path / "激活接入控制.md"
    md.write_text(_MD_NO_FLOW, encoding="utf-8")
    ctx = {"feature_docs": [FeatureDoc("GWFD-010151", "UDG", str(md))]}
    n = run(ctx)
    assert n == 1
    t = ctx["features"][0]["tasks"][0]
    assert t["boundary_source"] == "agent_pending"
    assert t["step_range"] == (1, 2)           # 整段（2 步）作 1 candidate
