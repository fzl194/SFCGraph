---
id: UNC@20.15.2@MMLCommand@RMV QOSTRANS
type: MMLCommand
name: RMV QOSTRANS（删除签约QoS转换配置）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: QOSTRANS
command_category: 配置类
applicable_nf:
- SGSN
effect_mode: 立即生效
is_dangerous: false
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

# RMV QOSTRANS（删除签约QoS转换配置）

## 功能

**适用网元：SGSN**

该命令用于删除一条指定的QoS转换配置信息。

## 注意事项

- 该命令执行后立即生效。
- 该命令执行后，SGSN将不再对指定用户范围的用户签约数据进行转换。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGE | 用户范围 | 可选必选说明：必选参数<br>参数含义：待删除的QoS转换所包含的用户范围。<br>取值范围：<br>- “ALL_USER(所有用户)”：全局约束，对所有用户有效。<br>- “SPECIAL_USER(指定用户)”：对指定的“IMSIPRE(IMSI前缀)”用户有效。<br>默认值：无 |
| IMSIPRE | IMSI前缀 | 可选必选说明：条件必选参数<br>参数含义：该参数用于系统根据对用户的IMSI进行匹配，从而区分不同的用户群。<br>前提条件：该参数在<br>“SUBRANGE(用户范围)”<br>参数配置为<br>“SPECIAL_USER(指定用户)”<br>后生效。<br>取值范围：5～15位十进制数字<br>默认值：无 |
| MBRULKO | 原始QoS上行最大速率 | 可选必选说明：可选参数<br>参数含义：该参数用于指定HLR签约数据中的QoS上行最大速率。<br>数据来源：整网规划<br>取值范围：0～255<br>默认值：无<br>配置原则：<br>- 1～63表示速率为1kbit/s～63kbit/s，以1kbit/s递增。<br>- 64～127表示速率为64kbit/s～568kbit/s，以8kbit/s递增。<br>- 128～254表示速率为576kbit/s～8640kbit/s，以64kbit/s递增。<br>- 255表示速率为0kbit/s。<br>- 原始QoS速率不能全为0。 |
| GBRULKO | 原始QoS上行保证速率 | 可选必选说明：可选参数<br>参数含义：该参数用于指定HLR签约数据中的QoS上行保证速率。<br>数据来源：整网规划<br>取值范围：0～255<br>默认值：无<br>配置原则：<br>- 1～63表示速率为1kbit/s～63kbit/s，以1kbit/s递增。<br>- 64～127表示速率为64kbit/s～568kbit/s，以8kbit/s递增。<br>- 128～254表示速率为576kbit/s～8640kbit/s，以64kbit/s递增。<br>- 255表示速率为0kbit/s。 |
| MBRDLKO | 原始QoS下行最大速率 | 可选必选说明：可选参数<br>参数含义：该参数用于指定HLR签约数据中的QoS下行最大速率。<br>数据来源：整网规划<br>取值范围：0～255<br>默认值：无<br>配置原则：<br>- 1～63表示速率为1kbit/s～63kbit/s，以1kbit/s递增。<br>- 64～127表示速率为64kbit/s～568kbit/s，以8kbit/s递增。<br>- 128～254表示速率为576kbit/s～8640kbit/s，以64kbit/s递增。<br>- 255表示速率为0kbit/s。<br>- 原始下行QoS速率与扩展下行QoS速率必须有一个为0。 |
| GBRDLKO | 原始QoS下行保证速率 | 可选必选说明：可选参数<br>参数含义：该参数用于指定HLR签约数据中的QoS下行保证速率。<br>数据来源：整网规划<br>取值范围：0～255<br>默认值：无<br>配置原则：<br>- 1～63表示速率为1kbit/s～63kbit/s，以1kbit/s递增。<br>- 64～127表示速率为64kbit/s～568kbit/s，以8kbit/s递增。<br>- 128～254表示速率为576kbit/s～8640kbit/s，以64kbit/s递增。<br>- 255表示速率为0kbit/s。<br>- 原始下行QoS速率与扩展下行QoS速率不能同时不为0。 |
| MBRDLKEXO | 原始QoS扩展下行最大速率 | 可选必选说明：可选参数<br>参数含义：该参数用于指定HLR签约数据中的QoS扩展下行最大速率。<br>数据来源：整网规划<br>取值范围：0～255<br>默认值：无<br>配置原则：<br>- 1～63表示速率为1kbit/s～63kbit/s，以1kbit/s递增。<br>- 64～127表示速率为64kbit/s～568kbit/s，以8kbit/s递增。<br>- 128～254表示速率为576kbit/s～8640kbit/s，以64kbit/s递增。<br>- 255表示速率为0kbit/s。 |
| MGRDLKEXO | 原始QoS扩展下行保证速率 | 可选必选说明：可选参数<br>参数含义：该参数用于指定HLR签约数据中的QoS扩展下行保证速率。<br>数据来源：整网规划<br>取值范围：0～255<br>默认值：无<br>配置原则：<br>- 1～63表示速率为1kbit/s～63kbit/s，以1kbit/s递增。<br>- 64～127表示速率为64kbit/s～568kbit/s，以8kbit/s递增。<br>- 128～254表示速率为576kbit/s～8640kbit/s，以64kbit/s递增。<br>- 255表示速率为0kbit/s。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/QOSTRANS]] · 签约QoS转换配置（QOSTRANS）

## 使用实例

1. 删除用户范围为所有用户的QoS转换配置信息：
  RMV QOSTRANS: SUBRANGE=ALL_USER;
2. 删除用户范围为指定用户，IMSI前缀为123456的QoS转换配置信息：
  RMV QOSTRANS: SUBRANGE=SPECIAL_USER, IMSIPRE="123456";

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除签约QoS转换配置(RMV-QOSTRANS)_26146232.md`
