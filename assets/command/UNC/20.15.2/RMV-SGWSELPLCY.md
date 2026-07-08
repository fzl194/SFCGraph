---
id: UNC@20.15.2@MMLCommand@RMV SGWSELPLCY
type: MMLCommand
name: RMV SGWSELPLCY（删除S-GW选择策略）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: SGWSELPLCY
command_category: 配置类
applicable_nf:
- SGSN
- MME
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- GTP-C接口管理
- S11接口管理
- S-GW选择策略
status: active
---

# RMV SGWSELPLCY（删除S-GW选择策略）

## 功能

![](删除S-GW选择策略(RMV SGWSELPLCY)_72225653.assets/notice_3.0-zh-cn_2.png)

- 参数（IMSI前缀）：即将删除匹配指定IMSI前缀的配置策略，请确认IMSI前缀的填写准确无误。
- 参数（MSISDN）：即将删除匹配指定MSISDN前缀的配置策略，请确认MSISDN前缀的填写准确无误。

**适用网元：SGSN、MME**

该命令用于删除S-GW选择策略。

## 注意事项

- 该命令执行后对新的LTE Attach/LTE TAU/LTE Handover/（GnGp SGSN->MME）/（GnGp SGSN->S4 SGSN）/S4 SGSN PDP Context Activation/（S4 SGSN->S4 SGSN）/（S4 SGSN->MME）/（MME->S4 SGSN）流程生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGE | 用户范围 | 可选必选说明：必选参数<br>参数含义：该参数用于指定用户范围。<br>数据来源：整网规划<br>取值范围：<br>- “IMSI_PREFIX(指定IMSI前缀)”<br>- “MSISDN_PREFIX(指定MSISDN前缀)”<br>- “SPECIFIC_IMSI(特定IMSI)”<br>- “SPECIFIC_MSISDN(特定MSISDN)”<br>默认值：无 |
| IMSIPRE | IMSI前缀 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定IMSI前缀。<br>前提条件：只有<br>“SUBRANGE（用户范围）”<br>为<br>“IMSI_PREFIX（指定IMSI前缀）”<br>时，该参数才有效。<br>数据来源：整网规划<br>取值范围：1～15位十进制数字字符串<br>默认值：无 |
| MSISDNPRE | MSISDN前缀 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定MSISDN前缀。<br>前提条件：只有<br>“SUBRANGE（用户范围）”<br>为<br>“MSISDN_PREFIX(指定MSISDN前缀)”<br>时，该参数才有效。<br>数据来源：整网规划<br>取值范围：1～15位十进制数字字符串<br>默认值：无 |
| IMSI | IMSI | 可选必选说明：条件必选参数<br>参数说明：该参数用于指定国际移动用户标识。<br>前提条件：此参数在“用户范围”设置为“SPECIFIC_IMSI(特定IMSI)”后生效。<br>取值范围：15位十进制数字字符串<br>默认值：无 |
| MSISDN | MSISDN | 可选必选说明：条件必选参数<br>参数说明：该参数用于指定移动台国际ISDN号码。<br>前提条件：此参数在“用户范围”设置为“SPECIFIC_MSISDN (特定MSISDN)”后生效。<br>取值范围：13位十进制数字字符串<br>默认值：无 |
| SLCTM | 选择方法 | 可选必选说明：可选参数<br>参数含义：该参数用于指定选择方法。<br>数据来源：整网规划<br>取值范围：<br>- “S-GW_QNAME(指定S-GW的查询域名)”<br>- “S-GW_IP (指定S-GW的IP地址)”<br>默认值：无 |

## 操作的配置对象

- [S-GW选择策略（SGWSELPLCY）](configobject/UNC/20.15.2/SGWSELPLCY.md)

## 使用实例

1. 删除S-GW选择策略，通过 “用户范围” 为 “MSISDN_PREFIX(指定MSISDN前缀)” 方式删除
  RMV SGWSELPLCY: SUBRANGE=MSISDN_PREFIX, MSISDNPRE="83023";
2. 删除S-GW选择策略，通过 “用户范围” 为 “IMSI_PREFIX(指定IMSI前缀)” 方式删除
  RMV SGWSELPLCY: SUBRANGE=IMSI_PREFIX, IMSIPRE="12303";

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除S-GW选择策略(RMV-SGWSELPLCY)_72225653.md`
