---
id: UDG@20.15.2@MMLCommand@DSP DBGHAFG
type: MMLCommand
name: DSP DBGHAFG（显示HAFG相关信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: DBGHAFG
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 可靠性管理
- 微服务可靠性管理
status: active
---

# DSP DBGHAFG（显示HAFG相关信息）

## 功能

该命令用于查询HAFG服务内部运行信息，方便问题定位。

> **说明**
> 无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| QUERYTYPE | 查询类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定具体的查询类型，用于获取对应类型的查询结果。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~1024。<br>默认值：无<br>配置原则：<br>查询类型举例如下：<br>DSP APPREPORTBASEINFO：该命令用于查询业务上报的基本信息。<br>DSP APPREPORTSTATUSINFO：该命令用于查询业务上报的周边网元状态信息。<br>DSP SELFSTATUS：该命令用于查询本网元状态信息。<br>DSP FUNCTIONSW：该命令用于查询网元级KPI异常检测与容灾和模块级KPI异常检测与恢复功能开关数据。<br>DSP DREXECUTIONINFO：该命令用于查询业务配置的容灾执行规则信息。<br>DSP DIAGNOSIS：该命令用于查询IFCM诊断结果信息。<br>DSP DECISION：该命令用于查询HAFG决策结果信息。<br>DSP EXECUTION：该命令用于查询容灾执行结果信息。<br>DSP VDUPOLICYINFO：该命令用于查询每个VM上policy的信息。 |

## 操作的配置对象

- [HAFG相关信息（DBGHAFG）](configobject/UDG/20.15.2/DBGHAFG.md)

## 使用实例

获取查询类型为“APPID|DSP APPREPORTBASEINFO”时的查询结果，其中APPID为实际网元ID。

```
%%DSP DBGHAFG: QUERYTYPE="0|DSP APPREPORTBASEINFO";%%
RETCODE = 0  操作成功

结果如下
--------
查询结果  =  
AppId                 License Information             Is Refer To NF               NF Number                       
0                     true                            true                         2
(结果个数 = 1)
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/显示HAFG相关信息（DSP-DBGHAFG）_66924852.md`
