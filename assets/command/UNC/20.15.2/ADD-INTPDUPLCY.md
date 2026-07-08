---
id: UNC@20.15.2@MMLCommand@ADD INTPDUPLCY
type: MMLCommand
name: ADD INTPDUPLCY（增加异网漫游PDU会话重建策略）
nf: UNC
version: 20.15.2
verb: ADD
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

# ADD INTPDUPLCY（增加异网漫游PDU会话重建策略）

## 功能

**适用NF：AMF**

该命令用于增加异网漫游用户的PDU会话重建策略。异网漫游用户在拜访网络内跨POOL移动时，可能造成HR模式会话的V-SMF和H-SMF跨省且跨运营商交互。增加该配置后，AMF可以对指定范围内的用户在指定条件下重建会话，为UE重新选择在同一省份内的V-SMF和H-SMF。

## 注意事项

- 下一次移动性流程生效。

- 最多可输入1024条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGE | 用户范围 | 可选必选说明：必选参数<br>参数含义：该参数用于指定PDU会话重建策略生效的用户范围。<br>数据来源：全网规划<br>取值范围：<br>- “INTERNAT_ROAM_USER（所有异网漫游用户）”：所有异网漫游用户。<br>- “IMSI_PREFIX（IMSI前缀）”：指定IMSI前缀的异网漫游用户。<br>- “SPECIFIC_IMSI（指定IMSI）”：指定IMSI的异网漫游用户。<br>默认值：无<br>配置原则：无 |
| IMSIPRE | IMSI前缀 | 可选必选说明：该参数在"SUBRANGE"配置为"IMSI_PREFIX"时为条件必选参数。<br>参数含义：该参数用于指定PDU会话重建策略的用户IMSI前缀。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是5~14。<br>默认值：无<br>配置原则：无 |
| IMSI | IMSI | 可选必选说明：该参数在"SUBRANGE"配置为"SPECIFIC_IMSI"时为条件必选参数。<br>参数含义：该参数用于指定PDU会话重建策略的用户IMSI（完整IMSI）。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度是15。<br>默认值：无<br>配置原则：无 |
| IMSPDUPLCY | 语音会话重建策略 | 可选必选说明：可选参数<br>参数含义：该参数用于指定异网漫游用户发生Inter类注册和切换流程时，语音会话的重建策略。<br>优先使用ADD NGVOICEDEPLOY中配置的VOICEDNN来识别语音会话，如果ADD NGVOICEDEPLOY未配置，则系统默认以“IMS”作为语音DNN来识别语音会话。<br>数据来源：全网规划<br>取值范围：<br>- “NO_REACT（不重建）”：Inter注册和Inter切换流程中不重建PDU会话。<br>- “REACT_ENTER_CMIDLE（进入空闲态后重建）”：等用户进入空闲态后重建会话。<br>- “IMMEDIATE_REACT（立即重建）”：Inter注册和Inter切换流程中立即重建会话。<br>默认值：无<br>配置原则：无 |
| NONIMSPDUPLCY | 非语音会话重建策略 | 可选必选说明：可选参数<br>参数含义：该参数用于指定异网漫游用户发生Inter类注册和切换流程时，非语音会话的重建策略。<br>数据来源：全网规划<br>取值范围：<br>- “NO_REACT（不重建）”：Inter注册和Inter切换流程中不重建PDU会话。<br>- “REACT_ENTER_CMIDLE（进入空闲态后重建）”：等用户进入空闲态后重建会话。<br>- “IMMEDIATE_REACT（立即重建）”：Inter注册和Inter切换流程中立即重建会话。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [异网漫游PDU会话重建策略（INTPDUPLCY）](configobject/UNC/20.15.2/INTPDUPLCY.md)

## 使用实例

增加一条异网漫游PDU会话重建策略，对所有异网漫游用户生效，数据会话和语音会话都等进入空闲态后再重建，执行如下命令：

```
ADD INTPDUPLCY:SUBRANGE=INTERNAT_ROAM_USER,IMSPDUPLCY=REACT_ENTER_CMIDLE,NONIMSPDUPLCY=REACT_ENTER_CMIDLE;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加异网漫游PDU会话重建策略（ADD-INTPDUPLCY）_15306282.md`
