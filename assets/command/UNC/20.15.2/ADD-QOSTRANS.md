---
id: UNC@20.15.2@MMLCommand@ADD QOSTRANS
type: MMLCommand
name: ADD QOSTRANS（增加签约QoS转换配置）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: QOSTRANS
command_category: 配置类
applicable_nf:
- SGSN
effect_mode: 立即生效
is_dangerous: false
max_records: 128
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- QoS管理
- Pre-R8 QoS
- QoS协商控制
- 签约QoS转换
status: active
---

# ADD QOSTRANS（增加签约QoS转换配置）

## 功能

**适用网元：SGSN**

该命令用于增加QoS转换功能记录。当SGSN、GGSN、RNC、MS等网元支持Rel7格式的QoS，但是HLR只支持Rel5或者更早版本的QoS时，通过QoS转换特性可以在不升级HLR的情况下使用HSPA+功能。当MS附着到SGSN时，HLR给SGSN发送签约数据，SGSN根据转换规则，把签约请求中携带的Rel5或Rel99版本的QoS转换为Rel7版本的QoS，保存在用户的签约数据中，MS就会使用Rel7版本的QoS发起业务请求。

## 注意事项

- 此命令执行后立即生效。
- 此命令最大记录数为128。
- 对于修改签约的R99版本的QoS时，原始速率只需要配置“MBRULKO(原始QoS上行最大速率)”、“GBRULKO(原始QoS上行保证速率)”、“MBRDLKO(原始QoS下行最大速率)”和“GBRDLKO(原始QoS下行保证速率)”四个参数；对于修改签约的R5版本的QoS时，原始速率只需要配置“MBRULKO(原始QoS上行最大速率)”、“GBRULKO(原始QoS上行保证速率)”、“MBRDLKEXO(原始QoS扩展下行最大速率)”和“MGRDLKEXO(原始QoS扩展下行保证速率)”四个参数，输入多余的原始上下行速率参数执行命令会失败。
- 此配置涉及基于IMSI号段的QoS控制特性（特性编号：WSFD-105104，License部件编码：LKV2IMSIQOS02），执行命令请使用[**DSP LICENSE**](../../../../../../../平台服务管理/操作维护/License管理/显示License(DSP LICENSE)_00360098.md)命令确认对应特性license是否得到授权，执行[**LST LICENSESWITCH**](../../../../../../../平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md)命令确认特性开关状态为“ENABLE(打开)”。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGE | 用户范围 | 可选必选说明：必选参数<br>参数含义：该参数用于指定QoS转换所包含的用户范围。<br>数据来源：整网规划<br>取值范围：<br>- “ALL_USER(所有用户)”：全局约束，对所有用户有效。<br>- “SPECIAL_USER(指定用户)”：对指定的“IMSIPRE(IMSI前缀)”用户有效。<br>默认值：无 |
| IMSIPRE | IMSI前缀 | 可选必选说明：条件必选参数<br>参数含义：该参数用于系统根据对用户的IMSI进行匹配，从而区分不同的用户群。<br>前提条件：该参数在<br>“SUBRANGE(用户范围)”<br>参数配置为<br>“SPECIAL_USER(指定用户)”<br>后生效。<br>数据来源：整网规划<br>取值范围：5～15位十进制数字<br>默认值：无 |
| MBRULKO | 原始QoS上行最大速率 | 可选必选说明：可选参数<br>参数含义：该参数用于指定HLR签约数据中的QoS上行最大速率。<br>数据来源：整网规划<br>取值范围：0～255<br>默认值：0<br>配置原则：<br>- 1～63表示速率为1kbit/s～63kbit/s，以1kbit/s递增。<br>- 64～127表示速率为64kbit/s～568kbit/s，以8kbit/s递增。<br>- 128～254表示速率为576kbit/s～8640kbit/s，以64kbit/s递增。<br>- 255表示速率为0kbit/s。<br>- 原始QoS速率不能全为0。 |
| GBRULKO | 原始QoS上行保证速率 | 可选必选说明：可选参数<br>参数含义：该参数用于指定HLR签约数据中的QoS上行保证速率。<br>数据来源：整网规划<br>取值范围：0～255<br>默认值：0<br>配置原则：<br>- 1～63表示速率为1kbit/s～63kbit/s，以1kbit/s递增。<br>- 64～127表示速率为64kbit/s～568kbit/s，以8kbit/s递增。<br>- 128～254表示速率为576kbit/s～8640kbit/s，以64kbit/s递增。<br>- 255表示速率为0kbit/s。 |
| MBRDLKO | 原始QoS下行最大速率 | 可选必选说明：可选参数<br>参数含义：该参数用于指定HLR签约数据中的QoS下行最大速率。<br>数据来源：整网规划<br>取值范围：0～255<br>默认值：0<br>配置原则：<br>- 1～63表示速率为1kbit/s～63kbit/s，以1kbit/s递增。<br>- 64～127表示速率为64kbit/s～568kbit/s，以8kbit/s递增。<br>- 128～254表示速率为576kbit/s～8640kbit/s，以64kbit/s递增。<br>- 255表示速率为0kbit/s。<br>- 原始下行QoS速率与扩展下行QoS速率必须有一个为0。 |
| GBRDLKO | 原始QoS下行保证速率 | 可选必选说明：可选参数<br>参数含义：该参数用于指定HLR签约数据中的QoS下行保证速率。<br>数据来源：整网规划<br>取值范围：0～255<br>默认值：0<br>配置原则：<br>- 1～63表示速率为1kbit/s～63kbit/s，以1kbit/s递增。<br>- 64～127表示速率为64kbit/s～568kbit/s，以8kbit/s递增。<br>- 128～254表示速率为576kbit/s～8640kbit/s，以64kbit/s递增。<br>- 255表示速率为0kbit/s。<br>- 原始下行QoS速率与扩展下行QoS速率不能同时不为0。 |
| MBRDLKEXO | 原始QoS扩展下行最大速率 | 可选必选说明：可选参数<br>参数含义：该参数用于指定HLR签约数据中的QoS扩展下行最大速率。<br>数据来源：整网规划<br>取值范围：0～255<br>默认值：0<br>配置原则：<br>- 1～63表示速率为1kbit/s～63kbit/s，以1kbit/s递增。<br>- 64～127表示速率为64kbit/s～568kbit/s，以8kbit/s递增。<br>- 128～254表示速率为576kbit/s～8640kbit/s，以64kbit/s递增。<br>- 255表示速率为0kbit/s。 |
| MGRDLKEXO | 原始QoS扩展下行保证速率 | 可选必选说明：可选参数<br>参数含义：该参数用于指定HLR签约数据中的QoS扩展下行保证速率。<br>数据来源：整网规划<br>取值范围：0～255<br>默认值：0<br>配置原则：<br>- 1～63表示速率为1kbit/s～63kbit/s，以1kbit/s递增。<br>- 64～127表示速率为64kbit/s～568kbit/s，以8kbit/s递增。<br>- 128～254表示速率为576kbit/s～8640kbit/s，以64kbit/s递增。<br>- 255表示速率为0kbit/s。 |
| MBRULKEXT | 目标QoS扩展上行最大速率 | 可选必选说明：可选参数<br>参数含义：该参数用于指定SGSN转换后的QoS扩展上行最大速率。<br>数据来源：整网规划<br>取值范围：0～250<br>默认值：0<br>配置原则：<br>- 0～74表示速率为8600kbit/s～16000kbit/s，以100kbit/s递增。例如74表示扩展最大速率为16 Mbit/s。<br>- 75～186表示速率为17000kbit/s～128000kbit/s，以1000kbit/s递增。例如79表示扩展大速率为21 Mbit/s。<br>- 187～250表示速率为130000kbit/s～256000kbit/s，以2000kbit/s递增。<br>- 目标扩展QoS速率不能全为0。 |
| GBRUPLKEXT | 目标QoS扩展上行保证速率 | 可选必选说明：可选参数<br>参数含义：该参数用于指定SGSN转换后的QoS扩展上行保证速率。<br>数据来源：整网规划<br>取值范围：0～250<br>默认值：0<br>配置原则：<br>- 0～74表示速率为8600kbit/s～16000kbit/s，以100kbit/s递增。例如74表示扩展最大速率为16 Mbit/s。<br>- 75～186表示速率为17000kbit/s～128000kbit/s，以1000kbit/s递增。例如79表示扩展大速率为21 Mbit/s。<br>- 187～250表示速率为130000kbit/s～256000kbit/s，以2000kbit/s递增。 |
| MBRDLKEXT | 目标QoS扩展下行最大速率 | 可选必选说明：可选参数<br>参数含义：该参数用于指定SGSN转换后的QoS扩展下行最大速率。<br>数据来源：整网规划<br>取值范围：0～250<br>默认值：0<br>配置原则：<br>- 0～74表示速率为8600kbit/s～16000kbit/s，以100kbit/s递增。例如74表示扩展最大速率为16 Mbit/s。<br>- 75～186表示速率为17000kbit/s～128000kbit/s，以1000kbit/s递增。例如79表示扩展大速率为21 Mbit/s。<br>- 187～250表示速率为130000kbit/s～256000kbit/s，以2000kbit/s递增。 |
| GBRDLKEXT | 目标QoS扩展下行保证速率 | 可选必选说明：可选参数<br>参数含义：该参数用于指定SGSN转换后的QoS扩展下行保证速率。<br>数据来源：整网规划<br>取值范围：0～250<br>默认值：0<br>配置原则：<br>- 0～74表示速率为8600kbit/s～16000kbit/s，以100kbit/s递增。例如74表示扩展最大速率为16 Mbit/s。<br>- 75～186表示速率为17000kbit/s～128000kbit/s，以1000kbit/s递增。例如79表示扩展大速率为21 Mbit/s。<br>- 187～250表示速率为130000kbit/s～256000kbit/s，以2000kbit/s递增。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/QOSTRANS]] · 签约QoS转换配置（QOSTRANS）

## 使用实例

1. 增加所有用户QoS转换记录：
  ADD QOSTRANS: SUBRANGE=ALL_USER, MBRULKO=120, GBRULKO=200, MBRDLKO=120, GBRDLKO=200, MBRDLKEXO=0, MGRDLKEXO=0, MBRULKEXT=200, GBRUPLKEXT=250, MBRDLKEXT=200, GBRDLKEXT=250;
2. 增加指定用户QoS转换记录：
  ADD QOSTRANS: SUBRANGE=SPECIAL_USER, IMSIPRE="123456", MBRULKO=120, GBRULKO=200, MBRDLKO=120, GBRDLKO=200, MBRDLKEXO=0, MGRDLKEXO=0, MBRULKEXT=200, GBRUPLKEXT=250, MBRDLKEXT=200, GBRDLKEXT=250;

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加签约QoS转换配置(ADD-QOSTRANS)_72345831.md`
