---
id: UNC@20.15.2@MMLCommand@LST HOMESMFINSTID
type: MMLCommand
name: LST HOMESMFINSTID（查询指定归属地SMF实例标识）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: HOMESMFINSTID
command_category: 查询类
applicable_nf:
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 移动性管理
- NF发现和选择管理
- 归属地SMF选择策略管理
status: active
---

# LST HOMESMFINSTID（查询指定归属地SMF实例标识）

## 功能

**适用NF：SMF**

该命令用于在对接归属地SMF时，查询指定用户接入的SMF实例标识。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGE | 用户范围 | 可选必选说明：可选参数<br>参数含义：该参数用于指定用户范围。<br>数据来源：本端规划<br>取值范围：<br>- IMSI_PRE（IMSI前缀）<br>- MSISDN_PRE（MSISDN前缀）<br>默认值：无<br>配置原则：<br>IMSI_PRE和MSISDN_PRE记录的优先级受SET PROXYSMFFUNC命令中的QUERYTYPE参数控制。 |
| PREFIX | 前缀 | 可选必选说明：可选参数<br>参数含义：该参数用于指定用户号码前缀。当参数SUBRANGE为"IMSI_PRE"时，本参数表示IMSI号码前缀，当参数SUBRANGE为"MSISDN_PRE"时，本参数表示MSISDN号码前缀。使用时按照最长匹配进行查询。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~15。<br>默认值：无<br>配置原则：<br>取值范围为1~15位数字。 |

## 操作的配置对象

- [指定归属地SMF实例标识（HOMESMFINSTID）](configobject/UNC/20.15.2/HOMESMFINSTID.md)

## 使用实例

假设运营商需要查询一个SUBRANGE为“IMSI_PRE”、PREFIX为“3080107000”的HOMESMFINSTID配置。

```
LST HOMESMFINSTID:SUBRANGE=IMSI_PRE,PREFIX="3080107000";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询指定归属地SMF实例标识（LST-HOMESMFINSTID）_70382313.md`
