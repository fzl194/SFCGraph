---
id: UNC@20.15.2@MMLCommand@MOD QOSCHARS
type: MMLCommand
name: MOD QOSCHARS（修改QoS特征）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: QOSCHARS
command_category: 配置类
applicable_nf:
- PGW-C
- SMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 计费和策略的业务管理
- 业务策略
- 业务质量特征
status: active
---

# MOD QOSCHARS（修改QoS特征）

## 功能

**适用NF：PGW-C、SMF**

该命令用来修改QoS特征，其中包括资源类型、5QI优先级、包时延预算、包错误率、平均窗口、最大数据突发。

业务触发专载流程，如果PCF下发了这些参数，以PCF下发的为准，否则读取该配置中的Qos参数。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| FQI | 5QI或QCI | 可选必选说明：必选参数<br>参数含义：该参数用于配置5QI或QCI，不同的5QI或QCI的业务流需使用不同的承载。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1~255。<br>默认值：无<br>配置原则：无 |
| RESOURCETYPE | QoS资源类型 | 可选必选说明：可选参数<br>参数含义：该参数用于表示QoS流是“NON_GBR”、 “Critical_GBR”还是“NON_CRITICAL_GBR”。<br>数据来源：全网规划<br>取值范围：<br>- NON_GBR（非GBR QoS流）<br>- NON_CRITICAL_GBR（非时延关键GBR QoS流）<br>- CRITICAL_GBR（延迟关键GBR QoS流）<br>默认值：无<br>配置原则：无 |
| PRIORITYLEVEL | 5QI优先级 | 可选必选说明：可选参数<br>参数含义：该参数用于表示5QI或QCI优先级。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1~127。<br>默认值：无<br>配置原则：<br>取值越小，优先级越高。 |
| PACKETDELBUDGET | 包时延预算(毫秒) | 可选必选说明：可选参数<br>参数含义：该参数用于指示数据包延迟预算。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1~1000，单位是毫秒。<br>默认值：无<br>配置原则：<br>请参考3GPP 23.501协议中表“Standardized 5QI to QoS characteristics mapping”进行配置。 |
| PACKETERRRATE | 包错误率 | 可选必选说明：可选参数<br>参数含义：该参数用于表示数据包错误率。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~32。<br>默认值：无<br>配置原则：<br>请参考3GPP 23.501协议中表“Standardized 5QI to QoS characteristics mapping”进行配置。 |
| AVERWINDOW | 平均窗口(毫秒) | 可选必选说明：该参数在"RESOURCETYPE"配置为"NON_CRITICAL_GBR"、"CRITICAL_GBR"时为条件必选参数。<br>参数含义：该参数用于指示平均窗口。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1~4095，单位是毫秒。<br>默认值：无<br>配置原则：<br>请参考3GPP 23.501协议中表“Standardized 5QI to QoS characteristics mapping”进行配置。 |
| MAXDATABURSTVOL | 最大数据突发量(字节) | 可选必选说明：该参数在"RESOURCETYPE"配置为"CRITICAL_GBR"时为条件必选参数。<br>参数含义：该参数用于指示最大数据突发量。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1~4095，单位是字节。<br>默认值：无<br>配置原则：<br>请参考3GPP 23.501协议中表“Standardized 5QI to QoS characteristics mapping”进行配置。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/QOSCHARS]] · QoS特征（QOSCHARS）

## 使用实例

修改一个5QI为“12”的QOS特征，资源类型为GBR，5QI优先级为10，包时延预算为1，包错误率为“4E-6”，平均窗口为1。

```
MOD QOSCHARS: FQI=12, RESOURCETYPE=NON_CRITICAL_GBR, PRIORITYLEVEL=10, PACKETDELBUDGET=1, PACKETERRRATE="4E-6", AVERWINDOW=1;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改QoS特征（MOD-QOSCHARS）_71516445.md`
