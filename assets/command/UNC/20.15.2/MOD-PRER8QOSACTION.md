---
id: UNC@20.15.2@MMLCommand@MOD PRER8QOSACTION
type: MMLCommand
name: MOD PRER8QOSACTION（修改Pre-R8 QoS控制动作配置）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: PRER8QOSACTION
command_category: 配置类
applicable_nf:
- GGSN
effect_mode: 对新用户生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- QoS
- PreR8 QoS配置
- PreR8 QoS控制动作
status: active
---

# MOD PRER8QOSACTION（修改Pre-R8 QoS控制动作配置）

## 功能

**适用NF：GGSN**

该命令用于修改QoS上下行保证带宽门限、最高带宽门限以及带宽超过门限值时对QoS用户的处理动作。

## 注意事项

- 该命令执行后只对新激活用户生效。

- 带宽取值为4294967295时，表示无效值。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| QOSPROFILENAME | QoS Profile名 | 可选必选说明：必选参数<br>参数含义：该参数用于指定QoS Profile的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。不区分大小写。<br>默认值：无<br>配置原则：<br>QOSPROFILENAME字段值必须先在QOSPROFILE或QOSGLOBAL对象中添加成功。 |
| TRAFFICCLASS | 业务类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定业务类型。<br>数据来源：本端规划<br>取值范围：<br>- “CONVERSATIONAL（会话类）”：表示用户签约信息中业务类型的级别为会话层面，优先级高。<br>- “STREAMING（流媒体类）”：表示用户签约信息中业务类型的级别为流媒体层面。<br>- “INTERACTIVE（交互类）”：表示用户签约信息中业务类型的级别为交互层面。<br>- “BACKGROUND（后台类）”：表示用户签约信息中业务类型的级别为后台层面。<br>默认值：无<br>配置原则：无 |
| GBRDL | 下行GBR(千比特/秒) | 可选必选说明：该参数在"TRAFFICCLASS"配置为"CONVERSATIONAL"、"STREAMING"时为条件可选参数。<br>参数含义：该参数用于设置用户下行保证比特速率。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~600000，4294967295，单位是千比特每秒。<br>默认值：无<br>配置原则：<br>GBRDL的值必须小于等于MBRDL。<br>GBRDL与MBRDL的值一个下发另一个不下发，则另一个会被赋相同的值。 |
| GBRDLACTION | 超过下行GBR的处理 | 可选必选说明：该参数在"TRAFFICCLASS"配置为"CONVERSATIONAL"、"STREAMING"时为条件可选参数。<br>参数含义：该参数用于指定超出用户下行保证比特速率时的动作。<br>数据来源：本端规划<br>取值范围：<br>- “DEGRADE（降级）”：表示如果请求的级别超过配置最高级别，则请求的级别自动降为配置的最高级别。<br>- “REJECT（拒绝）”：表示如果请求的级别超过配置的最高级别，则协商结束，激活失败。<br>默认值：无<br>配置原则：无 |
| GBRUL | 上行GBR(千比特/秒) | 可选必选说明：该参数在"TRAFFICCLASS"配置为"CONVERSATIONAL"、"STREAMING"时为条件可选参数。<br>参数含义：该参数用于设置用户上行保证比特速率。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~600000，4294967295，单位是千比特每秒。<br>默认值：无<br>配置原则：<br>GBRUL的值必须小于等于MBRUL。<br>GBRUL与MBRUL的值一个下发另一个不下发，则另一个会被赋相同的值。 |
| GBRULACTION | 超过上行GBR的处理 | 可选必选说明：该参数在"TRAFFICCLASS"配置为"CONVERSATIONAL"、"STREAMING"时为条件可选参数。<br>参数含义：该参数用于指定超出用户上行保证比特速率时的动作。<br>数据来源：本端规划<br>取值范围：<br>- “DEGRADE（降级）”：表示如果请求的级别超过配置最高级别，则请求的级别自动降为配置的最高级别。<br>- “REJECT（拒绝）”：表示如果请求的级别超过配置的最高级别，则协商结束，激活失败。<br>默认值：无<br>配置原则：无 |
| MBRDL | 下行MBR(千比特/秒) | 可选必选说明：可选参数<br>参数含义：该参数用于设置用户下行最大比特速率。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~600000，4294967295，单位是千比特每秒。<br>默认值：无<br>配置原则：<br>GBRDL的值必须小于等于MBRDL。<br>GBRDL与MBRDL的值一个下发另一个不下发，则另一个会被赋相同的值。 |
| MBRDLACTION | 超过下行MBR的处理 | 可选必选说明：可选参数<br>参数含义：该参数用于指定超出用户下行最大比特速率时的动作。<br>数据来源：本端规划<br>取值范围：<br>- “DEGRADE（降级）”：表示如果请求的级别超过配置最高级别，则请求的级别自动降为配置的最高级别。<br>- “REJECT（拒绝）”：表示如果请求的级别超过配置的最高级别，则协商结束，激活失败。<br>默认值：无<br>配置原则：无 |
| MBRUL | 上行MBR(千比特/秒) | 可选必选说明：可选参数<br>参数含义：该参数用于设置用户上行最大比特速率。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~600000，4294967295，单位是千比特每秒。<br>默认值：无<br>配置原则：<br>GBRUL的值必须小于等于MBRUL。<br>GBRUL与MBRUL的值一个下发另一个不下发，则另一个会被赋相同的值。 |
| MBRULACTION | 超过上行MBR的处理 | 可选必选说明：可选参数<br>参数含义：该参数用于指定超出用户上行最大比特速率时的动作。<br>数据来源：本端规划<br>取值范围：<br>- “DEGRADE（降级）”：表示如果请求的级别超过配置最高级别，则请求的级别自动降为配置的最高级别。<br>- “REJECT（拒绝）”：表示如果请求的级别超过配置的最高级别，则协商结束，激活失败。<br>默认值：无<br>配置原则：无 |
| THP | THP值 | 可选必选说明：该参数在"TRAFFICCLASS"配置为"INTERACTIVE"时为条件可选参数。<br>参数含义：该参数用于配置用户通信处理优先级的门限。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~3。<br>默认值：无<br>配置原则：无 |
| THPACTION | 超过THP的处理 | 可选必选说明：该参数在"TRAFFICCLASS"配置为"INTERACTIVE"时为条件可选参数。<br>参数含义：该参数用于指定当QoS信息中TRAFFICCLASS为INTERACTIVE类的用户的通信处理优先级高于THP配置的值时，UNC对该类用户的处理动作。<br>数据来源：本端规划<br>取值范围：<br>- “DEGRADE（降级）”：表示如果请求的级别超过配置最高级别，则请求的级别自动降为配置的最高级别。<br>- “REJECT（拒绝）”：表示如果请求的级别超过配置的最高级别，则协商结束，激活失败。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/PRER8QOSACTION]] · Pre-R8 QoS控制动作配置（PRER8QOSACTION）

## 使用实例

修改“QOSPROFILENAME”为“test”的上下行保证带宽门限、最高带宽门限以及带宽超过门限值时对QoS用户的处理动作：

```
MOD PRER8QOSACTION:QOSPROFILENAME="test",TRAFFICCLASS=CONVERSATIONAL,GBRDL=121,GBRDLACTION=DEGRADE,GBRUL=44,GBRULACTION=DEGRADE,MBRDL=144,MBRDLACTION=REJECT,MBRUL=55,MBRULACTION=DEGRADE;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/MOD-PRER8QOSACTION.md`
