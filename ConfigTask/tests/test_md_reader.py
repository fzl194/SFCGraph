# ConfigTask/tests/test_md_reader.py
from builder.core.md_reader import read_sections
from builder.constants import SECTION_FLOW, SECTION_STEPS, SECTION_EXAMPLE, SECTION_DATA

# 内容计费·部署 风格（有操作流程）
_MD_WITH_FLOW = """# 部署UPF

- [操作场景](#xxx)
- [必备事项](#xxx)
- [操作流程](#xxx)
- [操作步骤](#xxx)
- [任务示例](#xxx)

## [操作场景](#xxx)
内容计费的配置需要做好规划，在PCF、SMF、UPF网元上统一配置。

## [必备事项](#xxx)
前提条件

- 请阅读特性 GWFD-020301。
- 完成加载License。

数据

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| **ADD URR** | URRNAME | URR_URL | 本端规划 | - |
| **ADD URR** | URRID | 12500 | 全网规划 | - |

## [操作流程](#xxx)
新增或修改内容计费业务分为如下几个配置步骤：

1. 配置业务费率。对应操作步骤见[步骤 1](#)-[步骤 2](#)。
2. 配置过滤规则。对应操作步骤见[步骤 3](#)-[步骤 5](#)。

## [操作步骤](#xxx)

1. 配置使用量上报规则组属性。
    a. 配置URR。
      **ADD URR**
    b. 配置URR组。
      **ADD URRGROUP**
2. 配置PCC策略组。
  **ADD PCCPOLICYGRP**

## [任务示例](#xxx)

```
ADD URR:URRNAME="URR_URL", URRID=12500;
ADD URRGROUP:URRGROUPNAME="UrrGp_URL";
```
"""

# 接入控制·激活 风格（无操作流程）
_MD_NO_FLOW = """# 激活接入控制

- [必备事项](#xxx)
- [操作步骤](#xxx)
- [任务示例](#xxx)

## [操作场景](#xxx)
当在线用户已用带宽过大时，设置带宽接入的控制方式。

## [必备事项](#xxx)
前提条件

数据

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| **ADD APN** | APN | apn | 本端规划 | - |
| **SET APNQOSATTR** | CARSHAPEUL | CAR | 本端规划 | - |

## [操作步骤](#xxx)
1. 增加APN实例。
  **ADD APN** :APN=APN名称;
2. 将带宽控制方式绑定到APN。
  **SET APNQOSATTR** :APN=APN名称,CARSHAPEUL=上行;

## [任务示例](#xxx)
ADD APN:APN="apn";
"""


def test_cuts_four_sections_with_flow():
    s = read_sections(_MD_WITH_FLOW)
    assert set(s.keys()) == {SECTION_FLOW, SECTION_STEPS, SECTION_EXAMPLE, SECTION_DATA}
    assert "配置业务费率" in s[SECTION_FLOW]
    assert "ADD URR" in s[SECTION_STEPS]
    assert "ADD URR:URRNAME" in s[SECTION_EXAMPLE]
    # 数据规划表在必备事项段内（含前提条件 + 数据表）
    assert "ADD URR" in s[SECTION_DATA]
    assert "URRNAME" in s[SECTION_DATA]


def test_missing_flow_section_not_in_result():
    """无操作流程的文档：操作流程不在结果里，其余 3 段在。"""
    s = read_sections(_MD_NO_FLOW)
    assert SECTION_FLOW not in s
    assert set(s.keys()) == {SECTION_STEPS, SECTION_EXAMPLE, SECTION_DATA}
    assert "ADD APN" in s[SECTION_STEPS]
    assert "CARSHAPEUL" in s[SECTION_DATA]  # 数据表在必备事项段
