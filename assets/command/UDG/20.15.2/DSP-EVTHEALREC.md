---
id: UDG@20.15.2@MMLCommand@DSP EVTHEALREC
type: MMLCommand
name: DSP EVTHEALREC（显示事件治理自愈结果）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: EVTHEALREC
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 可靠性管理
- 微服务可靠性管理
status: active
---

# DSP EVTHEALREC（显示事件治理自愈结果）

## 功能

该命令用于在事件诊断成功情况下，查询事件治理的自愈结果。

> **说明**
> 本命令只能查询事件诊断和自愈成功的事件结果，事件诊断和自愈失败的结果请使用 [**DSP EVTGOVSTAT**](显示事件诊断失败状态（DSP EVTGOVSTAT）_94913407.md) 查询。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SERVICE | 服务名称 | 可选必选说明：可选参数<br>参数含义：该参数表示策略模型绑定的服务名称，若不输入此参数，则查询整系统所有服务名称的事件诊断和自愈成功的结果。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~255。<br>默认值：无<br>配置原则：无 |
| EVENTID | 事件ID | 可选必选说明：可选参数<br>参数含义：该参数显示事件的ID，若不输入此参数，则查询整系统某服务的所有事件ID的事件诊断和自愈成功的结果。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~4294967295。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@EVTHEALREC]] · 事件治理自愈结果（EVTHEALREC）

## 使用实例

该命令用于在事件诊断成功情况下，查询事件治理的自愈结果。

```
%%DSP EVTHEALREC:;%%
RETCODE = 0  操作成功

结果如下
------------------------
服务名称				事件ID			事件策略						自愈时间					对象类型					对象ID											上报次数				事件数量
SDRS				1				关联诊断						2021-08-04 09:41:10		自愈进程					gtp-pod-6d746cb46-2jc8f192-168-1-236__103__0	6					6
SDRS				1				关联诊断						2021-08-04 09:29:10		自愈进程					gtp-pod-6d746cb46-2jc8f192-168-1-236__103__0	6					6
SDRS				1				关联诊断						2021-08-04 09:17:10		自愈进程					gtp-pod-6d746cb46-2jc8f192-168-1-236__103__0	6					6

(结果个数 = 3)
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-EVTHEALREC.md`
