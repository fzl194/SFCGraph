---
id: UNC@20.15.2@MMLCommand@MOD ALIASAPN
type: MMLCommand
name: MOD ALIASAPN（修改别名APN配置）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: ALIASAPN
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
- 业务安全管理
- 会话管理
- 别名APN管理
status: active
---

# MOD ALIASAPN（修改别名APN配置）

## 功能

**适用网元：SGSN、MME**

该命令用于修改一条APN别名配置。APN别名配置用于将原始APN映射为别名APN。APN别名映射功能是将签约数据匹配后的APN NI映射成配置的别名APN NI，使用新的APN NI发起DNS解析。这样可以屏蔽用户APN的差异以及降低用户关于APN的配置要求，用户可以随意配置或者不配置，但系统可以把这些映射成实际使用的通用APN。 当运营商调整APN别名映射规则时，需要执行此命令。

当运营商调整APN别名映射规则时，需要执行此命令。

## 注意事项

- 该命令只在运营商调整网络时使用，只对后续的APN起作用，对于已有连接的APN不起作用。
- 此配置涉及别名APN特性（特性编号：WSFD-106203，license部件编码：LKV2ALIASAPN02），执行命令请使用[**DSP LICENSE**](../../../../../../平台服务管理/操作维护/License管理/显示License(DSP LICENSE)_00360098.md)命令确认对应特性license是否得到授权，执行[**LST LICENSESWITCH**](../../../../../../平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md)命令确认特性开关状态为“打开”。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGE | 用户范围 | 可选必选说明：必选参数<br>参数含义：该参数用于指定签约用户的范围。<br>数据来源：整网规划<br>取值范围：<br>- “ALL_USER(所有用户)”<br>- “IMSI_PREFIX(指定IMSI前缀)”<br>- “IMSI_RANGE(指定IMSI范围)”<br>默认值：无 |
| IMSIPRE | IMSI前缀 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定IMSI前缀。<br>前提条件：该参数在<br>“用户范围”<br>参数设置为<br>“IMSI_PREFIX(指定IMSI前缀)”<br>时，才需要配置。<br>数据来源：整网规划<br>取值范围：1～15位数字<br>默认值：无<br>说明：根据IMSI、“原始APNNI”映射唯一的“转换APNNI”。 |
| IMSI | IMSI | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定IMSI，对该IMSI所在号段进行修改。<br>前提条件：该参数在<br>“用户范围”<br>参数设置为<br>“IMSI_RANGE(指定IMSI范围)”<br>时，才需要配置。<br>数据来源：整网规划<br>取值范围：1～15位数字<br>默认值：无<br>说明：根据IMSI、“原始APNNI”映射唯一的“转换APNNI”。 |
| OLDAPN | 原始APNNI | 可选必选说明：必选参数<br>参数含义：该参数用于指定签约数据进行匹配后的APN NI。<br>数据来源：整网规划<br>取值范围：1～62<br>默认值：无<br>说明：- “原始APNNI”由一个或多个LABEL构成，各LABEL间用“.”间隔。每个LABEL的构成字符只能是字母A～Z或a～z、数字0～9和中划线“-”，字母不区分大小写。例如“HUAWEI.COM”。<br>- APN网络标识地址不能以“rac”、“lac”、“sgsn”或“rnc”开头，不能以“.gprs”结尾。 |
| NEWAPN | 转换APNNI | 可选必选说明：可选参数<br>参数含义：该参数用于指定进行转换后的APNNI。<br>数据来源：整网规划<br>取值范围：1～62<br>默认值：无<br>说明：- “转换APNNI”由一个或多个LABEL构成，各LABEL间用“.”间隔。每个LABEL的构成字符只能是字母A～Z或a～z、数字0～9和中划线“-”，字母不区分大小写。例如“HUAWEI.COM”。<br>- APN网络标识地址不能以“rac”、“lac”、“sgsn”或“rnc”开头，不能以“.gprs”结尾，不能取值为“*”。 |
| DESC | 描述 | 可选必选说明：可选参数<br>参数含义：该参数用于增加配置命令的描述信息。<br>数据来源：整网规划<br>取值范围：0~32位字符串<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/ALIASAPN]] · 别名APN配置（ALIASAPN）

## 使用实例

修改一条 “用户范围” 为 “ALL_USER(所有用户)” 、 “原始APNNI” 为 “WCDMA” 、 “转换APNNI” 为 “HUAWEI1.COM” 的APN别名配置记录。

MOD ALIASAPN: SUBRANGE=ALL_USER, OLDAPN="WCDMA", NEWAPN="HUAWEI1.com";

## 证据

- 原始手册：`evidence/UNC/20.15.2/MOD-ALIASAPN.md`
