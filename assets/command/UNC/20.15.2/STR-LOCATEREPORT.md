---
id: UNC@20.15.2@MMLCommand@STR LOCATEREPORT
type: MMLCommand
name: STR LOCATEREPORT（开始位置上报）
nf: UNC
version: 20.15.2
verb: STR
object_keyword: LOCATEREPORT
command_category: 动作类
applicable_nf:
- SMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- 位置上报管理
- 会话位置上报管理
status: active
---

# STR LOCATEREPORT（开始位置上报）

## 功能

**适用NF：SMF**

该命令用于设置开始用户位置上报参数。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IMSI | 用户标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定用户标识。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~100。<br>默认值：无<br>配置原则：无 |
| PDUSESSIONID | PDU会话ID | 可选必选说明：必选参数<br>参数含义：该参数用于指定PDU会话ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~15。<br>默认值：无<br>配置原则：无 |
| REPORTTYPE | 报告类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定报告类型。<br>数据来源：本端规划<br>取值范围：<br>- “OneTime（一次）”：单次上报位置<br>- “Continuous（多次）”：持续上报位置<br>默认值：无<br>配置原则：无 |
| REPORTSTATUS | 上报状态 | 可选必选说明：必选参数<br>参数含义：该参数用于启动或停止位置上报。<br>数据来源：本端规划<br>取值范围：<br>- “Start（开始）”：开始位置上报<br>- “Stop（停止）”：停止位置上报<br>默认值：无<br>配置原则：<br>在STR LOCATEREPORT命令中应选择配置“Start”，在STOP LOCATEREPORT命令中应选择配置“Stop”。 |
| LOCATEFILTER | 过滤条件 | 可选必选说明：必选参数<br>参数含义：该参数用于指定过滤条件，指示在TA还是CELL内才上报位置。<br>数据来源：本端规划<br>取值范围：<br>- “Tai（Tai）”：Tai<br>- “CellId（CellId）”：CellId<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/LOCATEREPORT]] · 位置上报（LOCATEREPORT）

## 使用实例

启动上报用户位置时使用该命令：

```
STR LOCATEREPORT:IMSI="12",PDUSESSIONID=2,ReportType=OneTime,REPORTSTATUS=Start,LOCATEFILTER=Tai;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/开始位置上报（STR-LOCATEREPORT）_09653133.md`
