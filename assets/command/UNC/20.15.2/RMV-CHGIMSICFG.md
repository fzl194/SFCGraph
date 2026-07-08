---
id: UNC@20.15.2@MMLCommand@RMV CHGIMSICFG
type: MMLCommand
name: RMV CHGIMSICFG（删除IMSI计费配置）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: CHGIMSICFG
command_category: 配置类
applicable_nf:
- SGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 计费管理
- IMSI计费配置
status: active
---

# RMV CHGIMSICFG（删除IMSI计费配置）

## 功能

**适用网元：SGSN**

该命令用来删除 “IMSI前缀” 计费配置表中某条 “IMSI前缀” 的配置。

## 注意事项

- 该命令执行后立即生效，影响新激活用户的话单生成策略，但该配置只对之后激活的用户有效。
- 当没有指定“计费属性”、“拜访类型”字段时，如果输入的必选参数“用户范围”、“IMSI前缀”、“APNNI”能够同时匹配到多条记录，则此操作会将所有的匹配记录删除。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGE | 用户范围 | 可选必选说明：必选参数<br>参数含义：该参数用于指定所包含的用户范围。<br>取值范围：<br>- “ALL_USER（所有用户）”<br>- “IMSI_PREFIX（指定IMSI前缀）”<br>默认值：无 |
| IMSIPRE | IMSI前缀 | 可选必选说明：条件必选参数<br>参数含义：该参数用于系统根据指定用户的IMSI进行匹配，从而区分不同的用户群。<br>取值范围：5～15位十进制字符串<br>默认值：无 |
| VISITTYPE | 拜访类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定用户的拜访类型 。<br>取值范围：<br>- “ROAMING（使用归属地GGSN的漫游用户）”<br>- “VISITING（使用拜访地GGSN的漫游用户）”<br>默认值：无<br>说明：- 此参数仅对漫游用户生效；当ALL值已设置时，相同的APN NI和IMSI Prefix时不能添加其它的拜访类型。<br>- 此参数不允许设置为空。 |
| APNNI | APNNI | 可选必选说明：必选参数<br>参数含义：该参数用于指定APN网络标识。<br>取值范围：最大长度为62个字符<br>默认值：无<br>说明：- 用户范围取“ALL_USER（所有用户）”值时，此参数不允许配置为“*”。<br>- 除了用户范围取“ALL_USER（所有用户）”的其他情况下，此参数只允许输入一个“*”或符合下述原则的字符串。<br>- APN网络标识地址由一个或多个LABEL构成，各LABEL间用“.”间隔。<br>- 每个LABEL的构成字符只能是字母A～Z或a～z、数字0～9和中划线“-”，字母不区分大小写。<br>- APN网络标识地址不能以“rac”、“lac”、“sgsn”或“rnc”开头，不能以“.gprs”结尾。 |
| CC | 计费属性 | 可选必选说明：可选参数<br>参数含义：该参数用于指定计费属性。<br>取值范围：<br>- HOT_BILLING(实时计费)<br>- FLAT_RATE(包月制)<br>- PREPAID_SERVICE（预付费）<br>- NORMAL_BILLING（普通计费）<br>默认值：无<br>说明：- 针对同一APN NI和IMSI PRE不允许计费属性选择交叉，例如：同一APN NI（HUAWEI.COM）和IMSI PRE（12301）不允许配置同时配置CC为Hot Billing and Flat Rate和Hot Billing and Prepaid Service两条记录。<br>- 此参数不允许设置为空。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@CHGIMSICFG]] · IMSI计费配置（CHGIMSICFG）

## 使用实例

删除 “IMSI前缀” 为 “123036” ， “APNNI” 为 “*” 的计费配置：

RMV CHGIMSICFG: SUBRANGE=IMSI_PREFIX, IMSIPRE="123036", APNNI="*";

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-CHGIMSICFG.md`
