---
id: UNC@20.15.2@MMLCommand@ADD IMSIAPNCONVERT
type: MMLCommand
name: ADD IMSIAPNCONVERT（增加APNNI转换配置）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: IMSIAPNCONVERT
command_category: 配置类
applicable_nf:
- SGSN
- MME
effect_mode: 立即生效
is_dangerous: false
max_records: 100
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 业务安全管理
- 会话管理
- APNNI转换管理
status: active
---

# ADD IMSIAPNCONVERT（增加APNNI转换配置）

## 功能

**适用网元：SGSN、MME**

该命令用于增加别名APN（Access Point Name）转换配置。如果用户激活请求消息中携带的APN和本配置命令“OLDAPN（请求APNNI）”匹配，则用户激活请求消息中携带的APN将被替换为“NEWAPN（转换APNNI）”后再进行签约数据匹配。

## 注意事项

- 该命令执行后立即生效。
- 本表最大记录数为100。
- 此配置涉及请求信息纠正功能特性（特性编号：WSFD-106004，License项：LKV2RINCOR02），执行命令请使用[**DSP LICENSE**](../../../../../../平台服务管理/操作维护/License管理/显示License(DSP LICENSE)_00360098.md)命令确认对应特性license是否得到授权，执行[**LST LICENSESWITCH**](../../../../../../平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md)命令确认特性开关状态为“ENABLE(打开)”。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGE | 用户范围 | 可选必选说明：必选参数<br>参数含义：该参数用于指定签约用户的范围。<br>数据来源：整网规划<br>取值范围：<br>- “ALL_USER(所有用户)”<br>- “IMSI_PREFIX(指定IMSI前缀)”<br>- “IMSI_RANGE(指定IMSI范围)”<br>默认值：无<br>说明：- “用户范围”+(“IMSI前缀”或“起始IMSI”“终止IMSI”组成的IMSI范围)+“请求APNNI”不能重复。根据IMSI、“请求APNNI”映射唯一的“转换APNNI”。<br>- 当存在“用户范围”为“IMSI_PREFIX(指定IMSI前缀)”的记录时，不允许再添加“用户范围”为“IMSI_RANGE(指定IMSI范围)”的记录。同理，当存在“用户范围”为“IMSI_RANGE(指定IMSI范围)”的记录时，不允许再添加“用户范围”为“IMSI_PREFIX(指定IMSI前缀)”的记录。 |
| IMSIPRE | IMSI前缀 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定IMSI前缀。<br>前提条件：该参数在<br>“用户范围”<br>参数设置为<br>“IMSI_PREFIX(指定IMSI前缀)”<br>时，才需要配置。<br>数据来源：整网规划<br>取值范围：1~15位数字<br>默认值：无<br>说明：根据<br>“IMSI前缀”<br>、<br>“请求APNNI”<br>映射唯一的<br>“转换APNNI”<br>。 |
| BEGIMSI | 起始IMSI | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定起始IMSI。<br>前提条件：该参数在<br>“用户范围”<br>参数设置为<br>“IMSI_RANGE(指定IMSI范围)”<br>时，才需要配置。<br>数据来源：整网规划<br>取值范围：1~15位数字<br>默认值：无<br>配置原则：输入的起始IMSI必须小于或者等于终止IMSI。判断起始IMSI和终止IMSI大小的原则是：<br>- 对于输入IMSI的长度小于系统规定的IMSI长度时，将该IMSI补足0到规定长度后进行大小比较，且起始IMSI必须小于终止IMSI。<br>- 只有输入IMSI长度等于系统规定长度时，起始IMSI才能等于终止IMSI。<br>- 对于系统规定IMSI长度为15的情况，如[表1](#ZH-CN_MMLREF_0000001172225339__tab1)所示。 |
| ENDIMSI | 终止IMSI | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定终止IMSI。<br>前提条件：该参数在<br>“用户范围”<br>参数设置为<br>“IMSI_RANGE(指定IMSI范围)”<br>时，才需要配置。<br>数据来源：整网规划<br>取值范围：1~15位数字<br>默认值：无 |
| OLDAPN | 请求APNNI | 可选必选说明：必选参数<br>参数含义：该参数用于指定匹配的激活请求消息中携带的APN NI。<br>数据来源：整网规划<br>取值范围：1~62位字符串<br>默认值：无<br>说明：- “请求APNNI”由一个或多个LABEL构成，各LABEL间用“.”间隔。每个LABEL的构成字符只能是字母A~Z或a~z、数字0~9和中划线“-”。例如“HUAWEI.COM”。<br>- APN网络标识地址不能以“rac”、“lac”、“sgsn”或“rnc”开头，不能以“.gprs”结尾，不能取值为“*”。<br>- 当“请求APN”相同时，输入的起始IMSI和终止IMSI定义的IMSI号段范围不允许与其它记录定义的IMSI号段范围相互交叉、包含或重合。 |
| APNCONVERT | APN转换 | 可选必选说明：可选参数<br>参数含义：该参数用于设置APN转换规则。<br>数据来源：整网规划<br>取值范围：<br>- “WILDCARD_SUBSCRIPTION_USER(对签约了野卡APN的用户启用)”：表示对签约了野卡APN的用户启用。<br>- “NO_WILDCARD_SUBSCRIPTION_USER(对未签约野卡APN的用户启用)”：表示对未签约野卡APN的用户启用。<br>- “ALL_USER(对号段内的用户都启用)”：表示对号段内的用户都启用。<br>默认值：<br>“WILDCARD_SUBSCRIPTION_USER(对签约了野卡APN的用户启用)” |
| NEWAPN | 转换APNNI | 可选必选说明：必选参数<br>参数含义：该参数用于指定进行转换后的APNNI。<br>数据来源：整网规划<br>取值范围：1~62位字符串<br>默认值：无<br>说明：- “转换APNNI”由一个或多个LABEL构成，各LABEL间用“.”间隔。每个LABEL的构成字符只能是字母A~Z或a~z、数字0~9和中划线“-”。例如“HUAWEI.COM”。<br>- APN网络标识地址不能以“rac”、“lac”、“sgsn”或“rnc”开头，不能以“.gprs”结尾，不能取值为“*”。 |
| DESC | 描述 | 可选必选说明：可选参数<br>参数含义：该参数用于增加配置命令的描述信息。<br>数据来源：整网规划<br>取值范围：0~32位字符串<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@IMSIAPNCONVERT]] · APNNI转换配置（IMSIAPNCONVERT）

## 使用实例

1. 增加一条 “用户范围” 为 “指定IMSI前缀” ， “IMSI前缀” 为 “123007551111111” ， “请求APNNI” 为 “WCDMA” 的用户， “APN转换” 为 “对签约了野卡APN的用户启用” ， “转换APNNI” 为 “HUAWEI1.COM” 的APNNI转换记录：
  ADD IMSIAPNCONVERT: SUBRANGE=IMSI_PREFIX, IMSIPRE="123007551111111", OLDAPN="WCDMA", NEWAPN="HUAWEI1.COM";
2. 增加一条 “用户范围” 为 “指定IMSI范围” ， “起始IMSI” 为 “123007552222222” ， “终止IMSI” 为 “123007553333333” ， “请求APNNI” 为 “WCDMA” ， “APN转换” 为 “对签约了野卡APN的用户启用” ， “转换APNNI” 为 “HUAWEI1.COM” 的APNNI转换记录。
  ADD IMSIAPNCONVERT: SUBRANGE=IMSI_RANGE, BEGIMSI="123007552222222", ENDIMSI="123007553333333", OLDAPN="WCDMA", NEWAPN="HUAWEI1.COM";
  假设IMSI为123007552222223的手机用户签约了“WCDMA”和“HUAWEI1.COM”两个APN，当用户携带APN“WCDMA”进行激活时，如果配置了上述命令，则用户请求的APN被替换为“HUAWEI1.COM”，后续激活流程中实际使用的APN为“HUAWEI1.COM”； 如果未配置上述命令，则用户请求的APN为“WCDMA”，后续激活流程中实际使用的APN为“WCDMA”；

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-IMSIAPNCONVERT.md`
