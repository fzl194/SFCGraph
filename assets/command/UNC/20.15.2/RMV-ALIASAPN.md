---
id: UNC@20.15.2@MMLCommand@RMV ALIASAPN
type: MMLCommand
name: RMV ALIASAPN（删除别名APN配置）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: ALIASAPN
command_category: 配置类
applicable_nf:
- SGSN
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 业务安全管理
- 会话管理
- 别名APN管理
status: active
---

# RMV ALIASAPN（删除别名APN配置）

## 功能

**适用网元：SGSN、MME**

该命令用于删除APN（Access Point Name）转换配置。在需要调整APN别名映射规则时使用。

## 注意事项

- 该命令在运营商调整网络时使用，对于已有连接的APN不即时生效。
- 该命令执行后立即生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGE | 用户范围 | 可选必选说明：必选参数<br>参数含义：该参数用于指定签约用户的范围。<br>取值范围：<br>- “ALL_USER(所有用户)”<br>- “IMSI_PREFIX(指定IMSI前缀)”<br>- “IMSI_RANGE(指定IMSI范围)”<br>默认值：无 |
| IMSIPRE | IMSI前缀 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定IMSI前缀。<br>前提条件：该参数在<br>“用户范围”<br>参数设置为<br>“IMSI_PREFIX(指定IMSI前缀)”<br>时，才需要配置。<br>取值范围：1～15位数字<br>默认值：无<br>说明：根据IMSI、“原始APNNI”映射唯一的“转换APNNI”。 |
| IMSI | IMSI | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定IMSI，对该IMSI所在号段进行删除。<br>前提条件：该参数在<br>“用户范围”<br>参数设置为<br>“IMSI_RANGE(指定IMSI范围)”<br>时，才需要配置。<br>取值范围：1～15位数字<br>默认值：无<br>说明：根据IMSI、“原始APNNI”映射唯一的“转换APNNI”。 |
| OLDAPN | 原始APNNI | 可选必选说明：必选参数<br>参数含义：该参数用于指定签约数据进行匹配后的APN NI。<br>取值范围：1～62<br>默认值：无<br>说明：- “原始APNNI”由一个或多个LABEL构成，各LABEL间用“.”间隔。每个LABEL的构成字符只能是字母A～Z或a～z、数字0～9和中划线“-”，字母不区分大小写。例如“HUAWEI.COM”。<br>- APN网络标识地址不能以“rac”、“lac”、“sgsn”或“rnc”开头，不能以“.gprs”结尾。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/ALIASAPN]] · 别名APN配置（ALIASAPN）

## 使用实例

删除 “用户范围” 为 “ALL_USER(所有用户)” 、 “原始APNNI” 为 “WCDMA” 的APN别名配置记录。

RMV ALIASAPN: SUBRANGE=ALL_USER, OLDAPN="WCDMA";

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除别名APN配置(RMV-ALIASAPN)_26145686.md`
