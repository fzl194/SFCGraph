---
id: UNC@20.15.2@MMLCommand@RMV SRANGECHRCFG
type: MMLCommand
name: RMV SRANGECHRCFG（删除小范围CHR生成规则）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: SRANGECHRCFG
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
- 移动性管理
- CHR管理
- 小范围CHR流程配置
status: active
---

# RMV SRANGECHRCFG（删除小范围CHR生成规则）

## 功能

**适用网元：SGSN、MME**

该命令用于删除小范围CHR单据的生成规则。

## 注意事项

- 该命令执行后立即生效。
- 如果不输入任何参数，执行该命令会删除所有记录。
- 当指定“用户范围”类型为“E_SPECIAL_APNQCI(By APNQCI)”时，如果只输入“APN网络标识”，会删除所有匹配该“APN网络标识”的记录；如果只输入“QCI值”， 会删除所有匹配该“QCI值”的记录；如果同时输入“APN网络标识”和“QCI值”，会删除同时匹配“APN网络标识”和“QCI值”的记录。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGE | 用户范围 | 可选必选说明：可选参数<br>参数含义：该参数用于指定启用功能的用户范围。<br>数据来源：本端规划<br>取值范围：枚举类型<br>- “E_SPECIAL_IMSI(用户IMSI生成小范围CHR单据)”：指定用户IMSI前缀生成小范围CHR单据。<br>- “E_SPECIAL_IMEI(终端IMEI生成小范围CHR单据)”：指定终端IMEI前缀生成小范围CHR单据。<br>- “E_SPECIAL_ENB(该eNodeB下的4G用户生成小范围CHR单据)”：指定该eNodeB下的4G用户生成小范围CHR单据。<br>- “E_SPECIAL_TAI(该TAI下的4G用户生成小范围CHR单据)”：指定该TAI下的4G用户生成小范围CHR单据。<br>- “E_SPECIAL_RAI(该RAI下的2/3G用户生成小范围CHR单据)”：指定该RAI下的2/3G用户生成小范围CHR单据。<br>- “E_SPECIAL_APNQCI(签约特定APNNI和QCI的4G用户生成小范围CHR单据)”: 签约特定APNNI和QCI的4G用户生成小范围CHR单据。<br>默认值：无 |
| IMSIPRE | IMSI前缀 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定IMSI前缀。<br>前提条件：该参数在<br>“用户范围”<br>设置为<br>“E_SPECIAL_IMSI”<br>后生效。<br>数据来源：全网规划<br>取值范围：11～15位十进制数字字符串<br>默认值：无 |
| IMEIPRE | IMEI前缀 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定IMEI前缀。<br>前提条件：该参数在<br>“用户范围”<br>设置为<br>“E_SPECIAL_IMEI”<br>后生效。<br>数据来源：全网规划<br>取值范围：11～15位十进制数字字符串<br>默认值：无 |
| MCC | 移动国家码 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定生成单据的移动国家码。<br>前提条件： 该参数在<br>“用户范围”<br>设置为<br>“E_SPECIAL_ENB”<br>，<br>“E_SPECIAL_TAI”<br>或<br>“E_SPECIAL_RAI”<br>后生效。<br>数据来源：全网规划<br>取值范围：长度为3的十进制数字<br>默认值：无 |
| MNC | 移动网号 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定生成单据的移动网号。<br>前提条件： 该参数在<br>“用户范围”<br>设置为<br>“E_SPECIAL_ENB”<br>，<br>“E_SPECIAL_TAI”<br>或<br>“E_SPECIAL_RAI”<br>后生效。<br>数据来源：全网规划<br>取值范围：长度为2～3的十进制数字<br>默认值：无 |
| ENODEBID | eNodeB标识 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定eNodeB的ID。<br>前提条件：该参数在<br>“用户范围”<br>设置为<br>“E_SPECIAL_ENB”<br>后生效。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围为0~268435455。<br>默认值：无 |
| TAC | 跟踪区域码 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定跟踪区域码。<br>前提条件：该参数在<br>“用户范围”<br>设置为<br>“E_SPECIAL_TAI”<br>后生效。<br>数据来源：全网规划<br>取值范围：0x0000～0xFFFF 。<br>默认值：无 |
| LAC | 位置区域码 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定位置区域码。<br>前提条件：该参数在<br>“用户范围”<br>设置为<br>“E_SPECIAL_RAI”<br>后生效。<br>数据来源：全网规划<br>取值范围：0x0000～0xFFFF 。<br>默认值：无 |
| RAC | 寻呼范围路由区域码 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定路由区域码。<br>前提条件：该参数在<br>“用户范围”<br>设置为<br>“E_SPECIAL_RAI”<br>后生效。<br>数据来源：全网规划<br>取值范围：0x00～0xFF 。<br>默认值：无 |
| APNNI | APN网络标识 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定签约的APNNI。<br>前提条件：该参数在<br>“用户范围”<br>设置为<br>“E_SPECIAL_APNQCI”<br>后生效。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1~62。<br>默认值：无 |
| QCI | QCI值 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定签约的QCI。<br>前提条件：该参数在<br>“用户范围”<br>设置为<br>“E_SPECIAL_APNQCI”<br>后生效。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围为1~254。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SRANGECHRCFG]] · 小范围CHR生成规则（SRANGECHRCFG）

## 使用实例

删除指定签约APNNI和QCI的小范围CHR生成规则的记录，指定签约APNNI为“Huawei.com”，QCI为 “1” :

RMV SRANGECHRCFG: SUBRANGE=E_SPECIAL_APNQCI, APNNI="Huawei.com", QCI=1;

删除所有APNNI为“Huawei.com”的小范围CHR生成规则的记录：

RMV SRANGECHRCFG: SUBRANGE=E_SPECIAL_APNQCI, APNNI="Huawei.com";

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除小范围CHR生成规则（RMV-SRANGECHRCFG）_72225299.md`
