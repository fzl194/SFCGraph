---
id: UNC@20.15.2@MMLCommand@ADD ALIASAPN
type: MMLCommand
name: ADD ALIASAPN（增加别名APN配置）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: ALIASAPN
command_category: 配置类
applicable_nf:
- SGSN
- MME
effect_mode: ''
is_dangerous: false
max_records: 1024
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 业务安全管理
- 会话管理
- 别名APN管理
status: active
---

# ADD ALIASAPN（增加别名APN配置）

## 功能

**适用网元：SGSN、MME**

该命令用于增加别名APN(Access Point Name)转换配置。APN别名配置用于将原始APN映射为别名APN。APN别名映射功能是将签约数据匹配后的APN NI映射成配置的别名APN NI，使用新的APN NI发起DNS解析。这样可以屏蔽用户APN的差异以及降低用户关于APN的配置要求，用户可以随意配置或者不配置，但系统可以把这些映射成实际使用的通用APN。

## 注意事项

- 该命令只在运营商调整网络时使用，对于已有连接的APN不起作用，只对新建立连接的APN起作用。
- 此命令最大记录数为1024。
- 此配置涉及别名APN特性（特性编号：WSFD-106203，license部件编码：LKV2ALIASAPN02），执行命令请使用[**DSP LICENSE**](../../../../../../平台服务管理/操作维护/License管理/显示License(DSP LICENSE)_00360098.md)命令确认对应特性license是否得到授权，执行[**LST LICENSESWITCH**](../../../../../../平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md)命令确认特性开关状态为“打开”。
- 当“用户范围”设置为“IMSI_PREFIX（指定IMSI前缀）”或“IMSI_RANGE（指定IMSI范围）”时，如果IMSI和原始APNNI的组合同时匹配到多条记录，使用“原始APNNI”非*的记录。例如用户123030000000001使用HUAWEI1.COM，在[表1](#ZH-CN_MMLREF_0000001172345281__tab1)所示场景下，匹配到记录1；在[表2](#ZH-CN_MMLREF_0000001172345281__tab2)所示场景下，匹配到记录1。

*表1 示例1*

| 记录 | 用户范围 | IMSI前缀 | 原始APNNI |
| --- | --- | --- | --- |
| 记录1 | “IMSI_PREFIX（指定IMSI前缀）” | 12303 | HUAWEI1.COM |
| 记录2 | “IMSI_PREFIX（指定IMSI前缀）” | 123030000000001 | * |

*表2 示例2*

| 记录 | 用户范围 | 起始IMSI | 终止IMSI | 原始APNNI |
| --- | --- | --- | --- | --- |
| 记录1 | “IMSI_RANGE（指定IMSI范围）” | 12301 | 12309 | HUAWEI1.COM |
| 记录2 | “IMSI_RANGE（指定IMSI范围）” | 123030000000001 | 123030000000001 | * |

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGE | 用户范围 | 可选必选说明：必选参数<br>参数含义：该参数用于指定签约用户的范围。<br>数据来源：整网规划<br>取值范围：<br>- “ALL_USER(所有用户)”<br>- “IMSI_PREFIX(指定IMSI前缀)”<br>- “IMSI_RANGE(指定IMSI范围)”<br>默认值：无<br>说明：- “用户范围”+（“IMSI前缀”或“起始IMSI” “终止IMSI”组成的IMSI范围）+“原始APNNI”不能重复。根据IMSI、“原始APNNI”映射唯一的“转换APNNI”。<br>- 当存在“用户范围”为“IMSI_PREFIX(指定IMSI前缀)”的记录时，不允许再添加“用户范围”为“IMSI_RANGE(指定IMSI范围)”的记录。同理，当存在“用户范围”为“IMSI_RANGE(指定IMSI范围)”的记录时，不允许再添加“用户范围”为“IMSI_PREFIX(指定IMSI前缀)”的记录。 |
| IMSIPRE | IMSI前缀 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定IMSI前缀。<br>前提条件：该参数在<br>“用户范围”<br>参数设置为<br>“IMSI_PREFIX(指定IMSI前缀)”<br>时，才需要配置。<br>数据来源：整网规划<br>取值范围：1～15位数字<br>默认值：无<br>说明：- 根据“IMSI前缀”、“原始APNNI”映射唯一的“转换APNNI”。 |
| BEGIMSI | 起始IMSI | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定起始IMSI。<br>前提条件：该参数在<br>“用户范围”<br>参数设置为<br>“IMSI_RANGE(指定IMSI范围)”<br>时，才需要配置。<br>数据来源：整网规划<br>取值范围：1～15位数字<br>默认值：无<br>配置原则：输入的起始IMSI必须小于或者等于终止IMSI。判断起始IMSI和终止IMSI大小的原则是：<br>- 对于输入IMSI的长度小于系统规定IMSI长度时，将该IMSI补足0到规定长度后进行大小比较，且起始IMSI必须小于终止IMSI。<br>- 只有输入IMSI长度等于系统规定长度时，起始IMSI才能等于终止IMSI。<br>- 对于系统规定IMSI长度为15的情况，如[表3](#ZH-CN_MMLREF_0000001172345281__tab3)所示。<br>说明：根据“起始IMSI”和“终止IMSI”组成的范围、“原始APNNI”映射唯一的“转换APNNI”。 |
| ENDIMSI | 终止IMSI | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定终止IMSI。<br>前提条件：该参数在<br>“用户范围”<br>参数设置为<br>“IMSI_RANGE(指定IMSI范围)”<br>时，才需要配置。<br>数据来源：整网规划<br>取值范围：1～15位数字<br>默认值：无<br>配置原则：输入的起始IMSI必须小于或者等于终止IMSI。判断起始IMSI和终止IMSI大小的原则是：<br>- 对于输入IMSI的长度小于系统规定IMSI长度时，将该IMSI补足0到规定长度后进行大小比较，且起始IMSI必须小于终止IMSI。<br>- 只有输入IMSI长度等于系统规定长度时，起始IMSI才能等于终止IMSI。<br>- 对于系统规定IMSI长度为15的情况，如[表3](#ZH-CN_MMLREF_0000001172345281__tab3)所示。<br>说明：根据“起始IMSI”和“终止IMSI”组成的范围、“原始APNNI”映射唯一的“转换APNNI”。 |
| OLDAPN | 原始APNNI | 可选必选说明：必选参数<br>参数含义：该参数用于指定签约数据进行匹配后的APN NI。<br>数据来源：整网规划<br>取值范围：1～62<br>默认值：无<br>说明：- “原始APNNI”由一个或多个LABEL构成，各LABEL间用“.”间隔。每个LABEL的构成字符只能是字母A～Z或a～z、数字0～9和中划线“-”，字母不区分大小写。例如“HUAWEI.COM”。<br>- APN网络标识地址不能以“rac”、“lac”、“sgsn”或“rnc”开头，不能以“.gprs”结尾。 |
| NEWAPN | 转换APNNI | 可选必选说明：必选参数<br>参数含义：该参数用于指定进行转换后的APNNI。<br>数据来源：整网规划<br>取值范围：1～62<br>默认值：无<br>说明：- “转换APNNI”由一个或多个LABEL构成，各LABEL间用“.”间隔。每个LABEL的构成字符只能是字母A～Z或a～z、数字0～9和中划线“-”，字母不区分大小写。例如“HUAWEI.COM”。<br>- APN网络标识地址不能以“rac”、“lac”、“sgsn”或“rnc”开头，不能以“.gprs”结尾，不能取值为“*”。 |
| DESC | 描述 | 可选必选说明：可选参数<br>参数含义：该参数用于增加配置命令的描述信息。<br>数据来源：整网规划<br>取值范围：0~32位字符串<br>默认值：无 |

## 操作的配置对象

- [别名APN配置（ALIASAPN）](configobject/UNC/20.15.2/ALIASAPN.md)

## 使用实例

增加一条 “用户范围” 为 “ALL_USER(所有用户)” 、 “原始APNNI” 为 “WCDMA” 、 “转换APNNI” 为 “HUAWEI1.COM” 的APN别名配置记录。

ADD ALIASAPN: SUBRANGE=ALL_USER, OLDAPN="WCDMA", NEWAPN="HUAWEI1.COM";

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加别名APN配置(ADD-ALIASAPN)_72345281.md`
