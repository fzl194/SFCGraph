---
id: UNC@20.15.2@MMLCommand@RMV GWSELPLCY
type: MMLCommand
name: RMV GWSELPLCY（删除GGSN/P-GW选择策略）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: GWSELPLCY
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
- GTP-C接口管理
- GnGp-GGSN_S5_S8接口管理
- GGSN_P-GW选择
status: active
---

# RMV GWSELPLCY（删除GGSN/P-GW选择策略）

## 功能

![](删除GGSN_P-GW选择策略（RMV GWSELPLCY）_72225623.assets/notice_3.0-zh-cn_2.png)

- 当“用户范围”为“IMSI_RANGE（指定IMSI范围）”，且输入的IMSI为所对应记录的“BEGIMSI（起始IMSI）”时，将对该号段配置记录进行删除。
- 当“用户范围”为“IMSI_PREFIX（指定IMSI前缀）”时，即将删除匹配指定IMSI前缀的配置策略，请确认IMSI前缀的填写准确无误。

**适用网元：SGSN、MME**

该命令用于删除GGSN/P-GW选择策略。

## 注意事项

- 该命令执行后对已经激活PDP用户不立即生效，其他用户立即生效。
- 当“用户范围”为“IMSI_RANGE（指定IMSI范围）”，且输入的IMSI为所对应记录的“BEGIMSI（起始IMSI）”时，将对该号段配置记录进行删除。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGE | 用户范围 | 可选必选说明：必选参数<br>参数含义：该参数用于指定待删除GGSN/P-GW选择策略的用户范围。<br>取值范围：<br>- “ALL_USER（所有用户）”<br>- “IMSI_PREFIX（指定IMSI前缀）”<br>- “IMSI_RANGE（指定IMSI范围）”<br>- “FOREIGN_USER（外网用户）”<br>- “HOME_USER（本网用户）”<br>- “MSISDN_PREFIX(指定MSISDN前缀)”<br>- “SPECIFIC_IMSI(特定IMSI)”<br>- “SPECIFIC_MSISDN(特定MSISDN)”<br>默认值：无 |
| IMSIPRE | IMSI前缀 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定IMSI前缀。<br>前提条件：只有<br>“用户范围”<br>为<br>“IMSI_PREFIX（指定IMSI前缀）”<br>时，该参数才有效。<br>取值范围：1～15位十进制数字字符串<br>默认值：无 |
| BEGIMSI | 起始IMSI | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定号段的起始IMSI，对该IMSI所在号段进行删除。<br>前提条件：只有<br>“用户范围”<br>为<br>“IMSI_RANGE（指定IMSI范围）”<br>时，该参数才有效。<br>取值范围：1～15位十进制数字字符串<br>默认值：无 |
| NOID | 运营商标识 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定运营商标识。<br>前提条件：该参数在<br>“SUBRANGE（用户范围）”<br>配置为<br>“FOREIGN_USER（外网用户）”<br>或<br>“HOME_USER（本网用户）”<br>后生效。<br>对于外网用户，该参数用于指定与互联PLMN签订漫游协议的本局运营商标识，对于本网用户，该参数是本网用户对应的运营商标识。<br>数据来源：整网规划<br>取值范围：0～64，128～254<br>默认值：无 |
| USERSUBTYPE | 用户子类 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定本网用户的范围，本网用户范围可以是本网所有用户、本网本地用户或本网异地用户。<br>签约数据中心接口为Gr时，才能获取HLR Number，并通过HLR Number来细分本网用户为本地用户或异地用户；当签约数据中心接口为S6d时，由于无法获取HLR Number，不能对本网用户细分为本地用户或异地用户。<br>前提条件：该参数在<br>“用户范围”<br>参数配置为<br>“HOME_USER（本网用户）”<br>时生效。<br>数据来源：整网规划<br>取值范围：<br>- “HOME_ALL_USER(本网所有用户)”<br>- “HOME_LOCAL_USER(本网本地用户)”<br>- “HOME_UNLOCAL_USER(本网异地用户)”<br>默认值：无 |
| MSISDNPRE | MSISDN前缀 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定MSISDN前缀。<br>前提条件: 只有“SUBRANGE（用户范围）”为“MSISDN_PREFIX(指定MSISDN前缀)”时，该参数才有效。<br>数据来源：整网规划<br>取值范围：1～15位十进制数字字符串<br>默认值：无 |
| IMSI | IMSI | 可选必选说明：条件必选参数<br>参数说明：该参数用于指定国际移动用户标识。<br>前提条件：此参数在“用户范围”设置为“SPECIFIC_IMSI(特定IMSI)”后生效。<br>取值范围：15位十进制数字字符串<br>默认值：无 |
| MSISDN | MSISDN | 可选必选说明：条件必选参数<br>参数说明：该参数用于指定移动台国际ISDN号码。<br>前提条件：此参数在“用户范围”设置为“SPECIFIC_MSISDN (特定MSISDN)”后生效。<br>取值范围：13位十进制数字字符串<br>默认值：无 |
| APNNI | APNNI | 可选必选说明：必选参数<br>参数含义：该参数用于指定APNNI。<br>取值范围：1～62位字符串<br>默认值：无<br>说明：- APN网络标识地址由一个或多个LABEL构成，各LABEL间用“.”间隔。<br>- 每个LABEL的构成字符只能是字母A～Z或a～z、数字0～9和中划线“-”，字母不区分大小写。<br>- APN网络标识地址不能以“rac”、“lac”、“sgsn”或“rnc”开头，不能以“.gprs”结尾。<br>- 符号“*”表示通配符，即不限制APNNI。 如果APNNI为“*”，表示该记录适用于所有的APNNI，否则该记录适用于指定的APNNI记录。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/GWSELPLCY]] · GGSN/P-GW选择策略（GWSELPLCY）

## 使用实例

删除 “用户范围” 为 “所有用户” ， “APNNI” 为 “HUAWEI1.com” 的配置：

RMV GWSELPLCY: SUBRANGE=ALL_USER, APNNI="HUAWEI1.com";

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除GGSN_P-GW选择策略（RMV-GWSELPLCY）_72225623.md`
