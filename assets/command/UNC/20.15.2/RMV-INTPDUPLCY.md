---
id: UNC@20.15.2@MMLCommand@RMV INTPDUPLCY
type: MMLCommand
name: RMV INTPDUPLCY（删除异网漫游PDU会话重建策略）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: INTPDUPLCY
command_category: 配置类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 移动性管理
- AMF漫游功能控制
- 异网漫游PDU会话重建策略管理
status: active
---

# RMV INTPDUPLCY（删除异网漫游PDU会话重建策略）

## 功能

**适用NF：AMF**

该命令用于删除异网漫游用户的PDU会话重建策略。

## 注意事项

下一次移动性流程生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGE | 用户范围 | 可选必选说明：必选参数<br>参数含义：该参数用于指定PDU会话重建策略生效的用户范围。<br>数据来源：全网规划<br>取值范围：<br>- “INTERNAT_ROAM_USER（所有异网漫游用户）”：所有异网漫游用户。<br>- “IMSI_PREFIX（IMSI前缀）”：指定IMSI前缀的异网漫游用户。<br>- “SPECIFIC_IMSI（指定IMSI）”：指定IMSI的异网漫游用户。<br>默认值：无<br>配置原则：无 |
| IMSIPRE | IMSI前缀 | 可选必选说明：该参数在"SUBRANGE"配置为"IMSI_PREFIX"时为条件必选参数。<br>参数含义：该参数用于指定PDU会话重建策略的用户IMSI前缀。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是5~14。<br>默认值：无<br>配置原则：无 |
| IMSI | IMSI | 可选必选说明：该参数在"SUBRANGE"配置为"SPECIFIC_IMSI"时为条件必选参数。<br>参数含义：该参数用于指定PDU会话重建策略的用户IMSI（完整IMSI）。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度是15。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@INTPDUPLCY]] · 异网漫游PDU会话重建策略（INTPDUPLCY）

## 使用实例

删除生效范围为所有异网漫游用户的PDU会话重建策略，执行如下命令：

```
RMV INTPDUPLCY:SUBRANGE=INTERNAT_ROAM_USER;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-INTPDUPLCY.md`
