---
id: UNC@20.15.2@MMLCommand@ADD IMSIDT
type: MMLCommand
name: ADD IMSIDT（增加IMSI Direct Tunnel配置）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: IMSIDT
command_category: 配置类
applicable_nf:
- SGSN
effect_mode: 立即生效
is_dangerous: false
max_records: 1024
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 网络管理
- Direct Tunnel管理
status: active
---

# ADD IMSIDT（增加IMSI Direct Tunnel配置）

## 功能

**适用网元：SGSN**

此命令用于增加IMSI DT属性信息表中的某个IMSI的DT属性记录，用来设置指定IMSI号段的用户或所有用户是否支持DT。

## 注意事项

- 此命令执行后立即生效。
- 此命令最大记录数为1024条。
- 未配置IMSI记录默认为支持DT。
- 用户要使用DT功能还需满足RNC、GGSN和APNNI支持DT功能。
- 该命令部分参数与相关特性license共同完成该特性的开启，请在设置参数前使用[**DSP LICENSE**](../../../../../平台服务管理/操作维护/License管理/显示License(DSP LICENSE)_00360098.md)命令确认对应特性license是否得到授权，执行[**LST LICENSESWITCH**](../../../../../平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md)命令确认特性开关状态为“ENABLE(打开)”，具体相关特性请参考参数的说明。
- 输入的起始IMSI必须小于或者等于终止IMSI。判断起始IMSI和终止IMSI大小的原则是：对于输入IMSI的长度小于系统规定IMSI长度时，将该IMSI补足0到规定长度后进行大小比较，且起始IMSI必须小于终止IMSI。只有输入IMSI长度等于系统规定长度时，起始IMSI才能等于终止IMSI。对于系统规定IMSI长度为15的情况，如[表1](#ZH-CN_MMLREF_0000001172345647__tab1)所示：
  *表1 IMSI限定范围*

  | 起始IMSI | 终止IMSI | 实际限定IMSI范围 |
  | --- | --- | --- |
  | 123002666 | 123002 | 增加记录失败，起始IMSI大于终止IMSI |
  | 123002 | 123002666 | 123002000000000 ~ 123002666000000，即区间[123002000000000，123002666000000] |
  | 123002 | 123002 | 增加记录失败，起始IMSI不能等于终止IMSI |
  | 123002000000000 | 123002000000000 | 仅限定IMSI号码123002000000000 |
  | 123003000000000 | 123004000000000 | 123003000000000 ~ 123004000000000，即区间[123003000000000， 123004000000000] |
- 输入的起始IMSI和终止IMSI定义的IMSI号段范围不允许与其它记录定义的IMSI号段范围相互交叉、包含或重合。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGE | 用户范围 | 可选必选说明：必选参数<br>参数含义：该参数用于指定签约用户的范围。<br>数据来源：整网规划<br>取值范围：<br>- “ALL_USER（所有用户）”<br>- “IMSI_PREFIX（指定IMSI前缀）”<br>- “IMSI_RANGE（指定IMSI范围）”<br>默认值：无<br>配置原则：<br>- 使用时首先按照用户的IMSI在“IMSI_PREFIX（指定IMSI前缀）”或“IMSI_RANGE（指定IMSI范围）”进行查询，如果查询成功则使用该记录对应的配置；如果查询失败，则查询“所有用户”对应的配置记录，如果查询成功则使用“所有用户”的配置，如果查询还失败，则默认支持DT。<br>- 当存在“用户范围”为“IMSI_PREFIX（指定IMSI前缀）”的记录时，不允许再添加“用户范围”为“IMSI_RANGE（指定IMSI范围）”的记录。同理，当存在“用户范围”为“IMSI_RANGE（指定IMSI范围）”的记录时，不允许再添加“用户范围”为“IMSI_PREFIX（指定IMSI前缀）”的记录。 |
| IMSIPRE | IMSI前缀 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定IMSI前缀。<br>前提条件：当<br>“用户范围”<br>为<br>“IMSI_PREFIX（指定IMSI前缀）”<br>时，该参数才有效。<br>数据来源：整网规划<br>取值范围：1～15位十进制字符串<br>默认值：无 |
| BEGIMSI | 起始IMSI | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定起始IMSI。<br>前提条件：当<br>“用户范围”<br>为<br>“IMSI_RANGE（指定IMSI范围）”<br>时，该参数才有效。<br>数据来源：整网规划<br>取值范围：1～15位十进制字符串<br>默认值：无<br>配置原则：起始IMSI要小于终止IMSI，或者在起始IMSI和终止IMSI等于系统长度时等于终止IMSI。 |
| ENDIMSI | 终止IMSI | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定终止IMSI。<br>前提条件：只有<br>“用户范围”<br>为<br>“IMSI_RANGE（指定IMSI范围）”<br>时，该参数才有效。<br>数据来源：整网规划<br>取值范围：1～15位十进制字符串<br>默认值：无<br>配置原则：起始IMSI要小于终止IMSI，或者在起始IMSI和终止IMSI等于系统长度时等于终止IMSI。 |
| DT | 启用Direct Tunnel | 可选必选说明：可选参数<br>参数含义：该参数用于指定是否启用基于IMSI的DT功能。<br>数据来源：整网规划<br>取值范围：<br>- “NO(否)”<br>- “YES(是)”<br>默认值：<br>“YES(是)”<br>配置原则：<br>- 取值为“NO(否)”时，表示不启用基于IMSI的DT功能。<br>- 取值为“YES(是)”时，表示启用基于IMSI的DT功能。<br>说明：- 当参数设置为“YES(是)”时，“支持Direct Tunnel功能”特性的相关license授权并开启后，此参数配置才生效（特性编号：WSFD-104506，License项：LKV2DIRTUN02）。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@IMSIDT]] · IMSI Direct Tunnel配置（IMSIDT）

## 使用实例

- 场景一
  对指定IMSI前缀用户开启DT属性配置信息：
  ADD IMSIDT: SUBRANGE=ALL_USER, DT=NO;
  ADD IMSIDT: SUBRANGE=IMSI_PREFIX, IMSIPRE="123456", DT=YES;

- 场景二
  对指定IMSI范围用户开启DT属性配置信息：
  ADD IMSIDT: SUBRANGE=ALL_USER, DT=NO;
  ADD IMSIDT: SUBRANGE=IMSI_RANGE, BEGIMSI="123456789000000", ENDIMSI="123456789888888", DT=YES;

- 场景三
  关闭指定IMSI用户DT属性配置信息：
  ADD IMSIDT: SUBRANGE=IMSI_PREFIX, IMSIPRE="123456789000000", DT=NO;

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-IMSIDT.md`
