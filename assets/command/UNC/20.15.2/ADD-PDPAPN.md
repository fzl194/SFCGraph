---
id: UNC@20.15.2@MMLCommand@ADD PDPAPN
type: MMLCommand
name: ADD PDPAPN（增加本地APN NI配置）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: PDPAPN
command_category: 配置类
applicable_nf:
- SGSN
- MME
effect_mode: 立即生效
is_dangerous: false
max_records: 1024
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 业务安全管理
- 会话管理
- 本地APNNI管理
status: active
---

# ADD PDPAPN（增加本地APN NI配置）

## 功能

**适用网元：SGSN、MME**

该命令用于增加指定用户PDP类型与APN NI地址的映射关系，即为指定用户PDP类型配置缺省的APNNI地址。

UNC 中一次激活场景和MME中PDN连接建立场景，用户匹配到野卡或者匹配到多组签约数据时，需要根据IMSI和PDP/PDN类型查询本地的APN NI。

## 注意事项

- 该命令执行后立即生效。
- 本表最大记录数为1024。
- 当“用户范围”设置为“IMSI_PREFIX（指定IMSI前缀）”或“IMSI_RANGE（指定IMSI范围）”时，如果IMSI和PDP/PDN类型的组合同时匹配到多条记录，使用“PDP/PDN类型”非“所有类型”的记录。例如用户123030000000001使用IPV4协议，在[表1](#ZH-CN_MMLREF_0000001172345275__tab1)所示场景下，匹配到记录1；在[表2](#ZH-CN_MMLREF_0000001172345275__tab2)所示场景下，匹配到记录1。
  *表1 示例1*

  | 记录 | 用户范围 | IMSI前缀 | PDP/PDN类型 | PDP/PDN类型 |
  | --- | --- | --- | --- | --- |
  | 记录1 | “IMSI_PREFIX（指定IMSI前缀）” | 12303 | IPV4协议 | IPV4协议 |
  | 记录2 | “IMSI_PREFIX（指定IMSI前缀）” | 123030000000001 | 所有类型 | 所有类型 |
  *表2 示例2*

  | 记录 | 用户范围 | 起始IMSI | 终止IMSI | PDP/PDN类型 | PDP/PDN类型 |
  | --- | --- | --- | --- | --- | --- |
  | 记录1 | “IMSI_RANGE（指定IMSI范围）” | 12301 | 12309 | IPV4协议 | IPV4协议 |
  | 记录2 | “IMSI_RANGE（指定IMSI范围）” | 123030000000001 | 123030000000001 | 所有类型 | 所有类型 |

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGE | 用户范围 | 可选必选说明：必选参数<br>参数含义：该参数用于指定签约用户的范围。<br>数据来源：整网规划<br>取值范围：<br>- “ALL_USER(所有用户)”<br>- “IMSI_PREFIX(指定IMSI前缀)”<br>- “IMSI_RANGE(指定IMSI范围)”<br>默认值：无<br>说明：- “用户范围”+（“IMSI前缀”或“起始IMSI”“终止IMSI”组成的IMSI范围）+“PDP/PDN类型”不能重复。根据IMSI、“PDP/PDN类型”映射唯一的“APN NI”。<br>- 当存在“用户范围”为“IMSI_PREFIX（指定IMSI前缀）”的记录时，不允许再添加“用户范围”为“IMSI_RANGE（指定IMSI范围）”的记录。同理，当存在“用户范围”为“IMSI_RANGE（指定IMSI范围）”的记录时，不允许再添加“用户范围”为“IMSI_PREFIX（指定IMSI前缀）”的记录。 |
| IMSIPRE | IMSI前缀 | 可选必选说明：条件必选参数<br>参数含义：系统根据该参数值对用户的IMSI进行匹配，从而区分不同的用户群。<br>前提条件：该参数在<br>“用户范围”<br>参数设置为<br>“IMSI_PREFIX(指定IMSI前缀)”<br>时，才需要配置。<br>数据来源：整网规划<br>取值范围：1～15位数字<br>默认值：无<br>说明：根据IMSI、<br>“PDP/PDN类型”<br>映射唯一的<br>“APN NI”<br>。 |
| BEGIMSI | 起始IMSI | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定起始IMSI。<br>前提条件：该参数在<br>“用户范围”<br>参数设置为<br>“IMSI_RANGE(指定IMSI范围)”<br>时，才需要配置。<br>数据来源：整网规划<br>取值范围：1～15位数字<br>默认值：无<br>配置原则：输入的起始IMSI必须小于或者等于终止IMSI。判断起始IMSI和终止IMSI大小的原则是：<br>- 对于输入IMSI的长度小于系统规定IMSI长度时，将该IMSI补足0到规定长度后进行大小比较，且起始IMSI必须小于终止IMSI。<br>- 只有输入IMSI长度等于系统规定长度时，起始IMSI才能等于终止IMSI。<br>- 对于系统规定IMSI长度为15的情况，如[表1](#ZH-CN_MMLREF_0000001172345275__tab1)所示。 |
| ENDIMSI | 终止IMSI | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定终止IMSI。<br>前提条件：该参数在<br>“用户范围”<br>参数设置为<br>“IMSI_RANGE(指定IMSI范围)”<br>时，才需要配置。<br>数据来源：整网规划<br>取值范围：1～15位数字<br>默认值：无<br>配置原则：当终止IMSI与起始IMSI长度全为15位时，终止IMSI要大于等于起始IMSI，否则终止IMSI要大于起始IMSI。 |
| PDPTYPE | PDP/PDN类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定PDP类型。<br>数据来源：整网规划<br>取值范围：<br>- “PT_IPV4(IPV4协议)”：表示用户激活的PDP类型为IPV4协议。<br>- “PT_IPV6(IPV6协议)”：表示用户激活的PDP类型为IPV6协议。<br>- “PT_PPP(点对点通信协议)”：表示用户激活的PDP类型为点对点通信协议。<br>- “PT_IPV4_IPV6(IPV4和IPV6协议)”：表示用户激活的PDP类型为IPV4和IPV6协议。<br>- “PT_ALL(所有类型)”：表示用户激活的PDP类型为所有类型，不包含Non-IP类型。<br>默认值：无<br>配置原则：输入的PDP类型不允许与已有的记录重复。 |
| APNNI | APN网络标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定APN网络标识地址。<br>数据来源：整网规划<br>取值范围：1～62位字符串<br>默认值：无<br>配置原则：<br>- APN网络标识地址由一个或多个LABEL构成，各LABEL间用“.”间隔。每个LABEL的构成字符只能是字母A～Z或a～z、数字0～9和中划线“-”，字母不区分大小写。例如“HUAWEI.COM”。<br>- APN网络标识地址不能以“rac”、“lac”、“sgsn”或“rnc”开头，不能以“.gprs”结尾，不能取值为“*”。<br>说明：输入的APN NI参数应为类似于XXX.XXX的形式，如“123.net”。如果配置的APN NI不正确，可能因DNS解析失败而导致激活流程失败。 |

## 操作的配置对象

- [本地APN NI配置（PDPAPN）](configobject/UNC/20.15.2/PDPAPN.md)

## 使用实例

增加一个 “用户范围” 为 “所有用户” ， “PDP/PDN类型” 为 “PT_IPV4” ， “APN网络标识” 为 “CNNET” 的记录：

ADD PDPAPN: SUBRANGE=ALL_USER, PDPTYPE=PT_IPV4, APNNI="CNNET";

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加本地APN-NI配置(ADD-PDPAPN)_72345275.md`
