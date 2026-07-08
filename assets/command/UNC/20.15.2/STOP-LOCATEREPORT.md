---
id: UNC@20.15.2@MMLCommand@STOP LOCATEREPORT
type: MMLCommand
name: STOP LOCATEREPORT（停止位置上报）
nf: UNC
version: 20.15.2
verb: STOP
object_keyword: LOCATEREPORT
command_category: 调测类
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

# STOP LOCATEREPORT（停止位置上报）

## 功能

**适用NF：SMF**

该命令用于设置停止用户位置上报参数。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IMSI | 用户标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定用户标识。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~100。<br>默认值：无<br>配置原则：无 |
| PDUSESSIONID | PDU会话ID | 可选必选说明：必选参数<br>参数含义：该参数用于指定PDU会话ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~15。<br>默认值：无<br>配置原则：无 |
| REPORTSTATUS | 上报状态 | 可选必选说明：必选参数<br>参数含义：该参数用于启动或停止位置上报。<br>数据来源：本端规划<br>取值范围：<br>- “Start（开始）”：开始位置上报<br>- “Stop（停止）”：停止位置上报<br>默认值：无<br>配置原则：<br>在STR LOCATEREPORT命令中应选择配置“Start”，在STOP LOCATEREPORT命令中应选择配置“Stop”。 |

## 操作的配置对象

- [位置上报（LOCATEREPORT）](configobject/UNC/20.15.2/LOCATEREPORT.md)

## 使用实例

停止上报用户位置时使用该命令：

```
STOP LOCATEREPORT:IMSI="12",PDUSESSIONID=2,REPORTSTATUS=Stop;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/停止位置上报（STOP-LOCATEREPORT）_09652274.md`
