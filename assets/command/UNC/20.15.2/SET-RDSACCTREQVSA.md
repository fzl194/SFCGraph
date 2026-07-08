---
id: UNC@20.15.2@MMLCommand@SET RDSACCTREQVSA
type: MMLCommand
name: SET RDSACCTREQVSA（设置RADIUS计费服务器组的私有扩展属性）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: RDSACCTREQVSA
command_category: 配置类
applicable_nf:
- PGW-C
- SMF
effect_mode: 立即生效
is_dangerous: false
max_records: 1000
category_path:
- 业务服务管理
- 会话管理
- RADIUS管理
- RADIUS计费管理
- 扩展信元控制
status: active
---

# SET RDSACCTREQVSA（设置RADIUS计费服务器组的私有扩展属性）

## 功能

**适用NF：PGW-C、SMF**

该命令用来新增指定RADIUS服务器组的RADIUS计费3gpp和3gpp2私有扩展属性的配置，用来控制RADIUS计费消息中携带哪些3gpp和3gpp2私有扩展属性的字段。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1000。
- 当前版本不支持此命令的TWANID、THREEGPP2、THREEGPP2BSID参数。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | THREEGPP | IMSI | CHARGINGID | PDPTYPE | CGADDRESS | NEGOTIAEDQOS | SGSNSGWADDRESS | GGSNADDRESS | IMSIMCCMNC | GGSNMCCMNC | NSAPI | SELECTIONMODE | CHARGINGCHAR | SGSNSGWMCCMNC | IMEISV | INTERIMUPDATE | STOP | RATTYPE | ULI | MSTIMEZONE | STOPINDICATOR | NEGOTIAEDDSCP | PACKETFILTER | SGSNIPV6ADDRESS | GGSNIPV6ADDRESS | TWANID | THREEGPP2 | THREEGPP2BSID | CGIPV6ADDR |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 初始值 | DISABLE | ENABLE | ENABLE | ENABLE | ENABLE | ENABLE | ENABLE | ENABLE | ENABLE | ENABLE | ENABLE | ENABLE | ENABLE | ENABLE | ENABLE | DISABLE | DISABLE | ENABLE | ENABLE | ENABLE | ENABLE | ENABLE | ENABLE | ENABLE | ENABLE | DISABLE | DISABLE | DISABLE | DISABLE |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RDSSVRGRPNAME | RADIUS Server Group名称 | 可选必选说明：必选参数<br>参数含义：RADIUS服务器组名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：配置RADIUS服务器组名前，需要先使用ADD RDSSVRGRP命令配置RADIUS服务器组信息。 |
| THREEGPP | 支持3gpp私有扩展属性 | 可选必选说明：必选参数<br>参数含义：指定是否支持3gpp私有扩展属性。<br>数据来源：全网规划<br>取值范围：枚举类型。<br>- DISABLE：不支持。<br>- ENABLE：支持。<br>默认值：无<br>配置原则：无 |
| IMSI | 携带3GPP-IMSI属性 | 可选必选说明：条件可选参数<br>前提条件：该参数在“THREEGPP”配置为“ENABLE”时为可选参数。<br>参数含义：指定是否携带3GPP-IMSI属性。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不携带该字段。<br>- ENABLE：携带该字段。<br>默认值：无<br>配置原则：无 |
| CHARGINGID | 携带3GPP-Charging-ID属性 | 可选必选说明：条件可选参数<br>前提条件：该参数在“THREEGPP”配置为“ENABLE”时为可选参数。<br>参数含义：指定是否携带3GPP-Charging-ID属性。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不携带该字段。<br>- ENABLE：携带该字段。<br>默认值：无<br>配置原则：无 |
| PDPTYPE | 携带3GPP-PDP-Type属性 | 可选必选说明：条件可选参数<br>前提条件：该参数在“THREEGPP”配置为“ENABLE”时为可选参数。<br>参数含义：指定是否携带3GPP-PDP-Type属性。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不携带该字段。<br>- ENABLE：携带该字段。<br>默认值：无<br>配置原则：无 |
| CGADDRESS | 携带3GPP-CG-Address属性 | 可选必选说明：条件可选参数<br>前提条件：该参数在“THREEGPP”配置为“ENABLE”时为可选参数。<br>参数含义：指定是否携带3GPP-CG-Address属性。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不携带该字段。<br>- ENABLE：携带该字段。<br>默认值：无<br>配置原则：无 |
| CGIPV6ADDR | 携带3GPP-CG-IPv6-Address属性 | 可选必选说明：条件可选参数<br>前提条件：该参数在“THREEGPP”配置为“ENABLE”时为可选参数。<br>参数含义：指定是否携带3GPP-CG-IPv6-Address属性。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不携带该字段。<br>- ENABLE：携带该字段。<br>默认值：无<br>配置原则：如果ThreeGpp配置为DISABLE，CGIPv6Addr为DISABLE。 |
| NEGOTIAEDQOS | 携带3GPP-GPRS-Negotiated-QoS-Profile扩展属性 | 可选必选说明：条件可选参数<br>前提条件：该参数在“THREEGPP”配置为“ENABLE”时为可选参数。<br>参数含义：指定是否携带3GPP-GPRS-Negotiated-QoS-Profile扩展属性。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不携带该字段。<br>- ENABLE：携带该字段。<br>默认值：无<br>配置原则：如果ThreeGpp配置为DISABLE，NegotiaedQos为DISABLE。 |
| SGSNSGWADDRESS | 携带3GPP-SGSN（SGW）-Address | 可选必选说明：条件可选参数<br>前提条件：该参数在“THREEGPP”配置为“ENABLE”时为可选参数。<br>参数含义：指定是否携带3GPP-SGSN（SGW）-Address。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不携带该字段。<br>- ENABLE：携带该字段。<br>默认值：无<br>配置原则：如果ThreeGpp配置为DISABLE，SgsnSgwAddress为DISABLE。 |
| GGSNADDRESS | 携带3GPP-GGSN-Address信元 | 可选必选说明：条件可选参数<br>前提条件：该参数在“THREEGPP”配置为“ENABLE”时为可选参数。<br>参数含义：指定是否携带3GPP-GGSN-Address信元。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不携带该字段。<br>- ENABLE：携带该字段。<br>默认值：无<br>配置原则：如果ThreeGpp配置为DISABLE，GgsnAddress为DISABLE。 |
| IMSIMCCMNC | 携带IMSI-MCC-MNC信元 | 可选必选说明：条件可选参数<br>前提条件：该参数在“THREEGPP”配置为“ENABLE”时为可选参数。<br>参数含义：指定是否携带IMSI-MCC-MNC信元。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不携带该字段。<br>- ENABLE：携带该字段。<br>默认值：无<br>配置原则：如果ThreeGpp配置为DISABLE，ImsiMccMnc为DISABLE。 |
| GGSNMCCMNC | 携带GGSN-MCC-MNC信元 | 可选必选说明：条件可选参数<br>前提条件：该参数在“THREEGPP”配置为“ENABLE”时为可选参数。<br>参数含义：指定是否携带GGSN-MCC-MNC信元。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不携带该字段。<br>- ENABLE：携带该字段。<br>默认值：无<br>配置原则：如果ThreeGpp配置为DISABLE，GgsnMccMnc为DISABLE。 |
| NSAPI | 携带3GPP-NSAPI属性 | 可选必选说明：条件可选参数<br>前提条件：该参数在“THREEGPP”配置为“ENABLE”时为可选参数。<br>参数含义：指定是否携带3GPP-NSAPI属性。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不携带该字段。<br>- ENABLE：携带该字段。<br>默认值：无<br>配置原则：如果ThreeGpp配置为DISABLE，Nsapi为DISABLE。 |
| SELECTIONMODE | 携带3GPP-Selection-Mode属性 | 可选必选说明：条件可选参数<br>前提条件：该参数在“THREEGPP”配置为“ENABLE”时为可选参数。<br>参数含义：指定是否携带3GPP-Selection-Mode属性。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不携带该字段。<br>- ENABLE：携带该字段。<br>默认值：无<br>配置原则：如果ThreeGpp配置为DISABLE，SelectionMode为DISABLE。 |
| CHARGINGCHAR | 携带3GPP-Charging-Characteristics属性 | 可选必选说明：条件可选参数<br>前提条件：该参数在“THREEGPP”配置为“ENABLE”时为可选参数。<br>参数含义：指定是否携带3GPP-Charging-Characteristics属性。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不携带该字段。<br>- ENABLE：携带该字段。<br>默认值：无<br>配置原则：如果ThreeGpp配置为DISABLE，ChargingChar为DISABLE。 |
| SGSNSGWMCCMNC | 携带SGSN（SGW）-MCC-MNC扩展属性 | 可选必选说明：条件可选参数<br>前提条件：该参数在“THREEGPP”配置为“ENABLE”时为可选参数。<br>参数含义：指定是否携带SGSN(SGW)-MCC-MNC扩展属性。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不携带该字段。<br>- ENABLE：携带该字段。<br>默认值：无<br>配置原则：如果ThreeGpp配置为DISABLE，SgsnSgwMccMnc为DISABLE。 |
| IMEISV | 携带IMEISV扩展属性 | 可选必选说明：条件可选参数<br>前提条件：该参数在“THREEGPP”配置为“ENABLE”时为可选参数。<br>参数含义：指定是否携带IMEISV扩展属性。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不携带该字段。<br>- ENABLE：携带该字段。<br>默认值：无<br>配置原则：如果ThreeGpp配置为DISABLE，Imeisv为DISABLE。 |
| INTERIMUPDATE | Accouting Interim消息是否携带IMEISV扩展属性 | 可选必选说明：条件可选参数<br>前提条件：该参数在“IMEISV”配置为“ENABLE”时为可选参数。<br>参数含义：指定是否Accouting Interim消息是否携带IMEISV扩展属性。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不携带该字段。<br>- ENABLE：携带该字段。<br>默认值：无<br>配置原则：无 |
| STOP | Accouting Stop消息是否携带IMEISV扩展属性 | 可选必选说明：条件可选参数<br>前提条件：该参数在“IMEISV”配置为“ENABLE”时为可选参数。<br>参数含义：指定是否Accouting Stop消息是否携带IMEISV扩展属性。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不携带该字段。<br>- ENABLE：携带该字段。<br>默认值：无<br>配置原则：无 |
| RATTYPE | 携带3GPP-RAT-Type扩展属性 | 可选必选说明：条件可选参数<br>前提条件：该参数在“THREEGPP”配置为“ENABLE”时为可选参数。<br>参数含义：指定是否携带3GPP-RAT-Type扩展属性。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不携带该字段。<br>- ENABLE：携带该字段。<br>默认值：无<br>配置原则：如果ThreeGpp配置为DISABLE，RatType为DISABLE。 |
| ULI | 携带User-Location-Info扩展属性 | 可选必选说明：条件可选参数<br>前提条件：该参数在“THREEGPP”配置为“ENABLE”时为可选参数。<br>参数含义：指定是否携带User-Location-Info扩展属性。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不携带该字段。<br>- ENABLE：携带该字段。<br>默认值：无<br>配置原则：如果ThreeGpp配置为DISABLE，Uli为DISABLE。 |
| MSTIMEZONE | 携带3GPP-MS-TimeZone属性 | 可选必选说明：条件可选参数<br>前提条件：该参数在“THREEGPP”配置为“ENABLE”时为可选参数。<br>参数含义：指定是否携带3GPP-MS-TimeZone属性。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不携带该字段。<br>- ENABLE：携带该字段。<br>默认值：无<br>配置原则：如果ThreeGpp配置为DISABLE，MsTimeZone为DISABLE。 |
| STOPINDICATOR | 携带stop-indicator扩展属性 | 可选必选说明：条件可选参数<br>前提条件：该参数在“THREEGPP”配置为“ENABLE”时为可选参数。<br>参数含义：指定是否携带stop-indicator扩展属性。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不携带该字段。<br>- ENABLE：携带该字段。<br>默认值：无<br>配置原则：如果ThreeGpp配置为DISABLE，StopIndicator为DISABLE。 |
| NEGOTIAEDDSCP | 携带3GPP-Negotiated-DSCP属性 | 可选必选说明：条件可选参数<br>前提条件：该参数在“THREEGPP”配置为“ENABLE”时为可选参数。<br>参数含义：指定是否携带3GPP-Negotiated-DSCP属性。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不携带该字段。<br>- ENABLE：携带该字段。<br>默认值：无<br>配置原则：如果ThreeGpp配置为DISABLE，NegotiaedDscp为DISABLE。 |
| PACKETFILTER | 携带packet-filter扩展属性 | 可选必选说明：条件可选参数<br>前提条件：该参数在“THREEGPP”配置为“ENABLE”时为可选参数。<br>参数含义：指定是否携带packet-filter扩展属性。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不携带该字段。<br>- ENABLE：携带该字段。<br>默认值：无<br>配置原则：如果ThreeGpp配置为DISABLE，PacketFilter为DISABLE。 |
| SGSNIPV6ADDRESS | 携带3GPP-SGSN-IPv6-Address属性 | 可选必选说明：条件可选参数<br>前提条件：该参数在“THREEGPP”配置为“ENABLE”时为可选参数。<br>参数含义：指定是否携带3GPP-SGSN-IPv6-Address属性。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不携带该字段。<br>- ENABLE：携带该字段。<br>默认值：无<br>配置原则：如果ThreeGpp配置为DISABLE，SgsnIPv6Address为DISABLE。 |
| GGSNIPV6ADDRESS | 携带3GPP-GGSN-IPv6-Address属性 | 可选必选说明：条件可选参数<br>前提条件：该参数在“THREEGPP”配置为“ENABLE”时为可选参数。<br>参数含义：指定是否携带3GPP-GGSN-IPv6-Address属性。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不携带该字段。<br>- ENABLE：携带该字段。<br>默认值：无<br>配置原则：如果ThreeGpp配置为DISABLE，GgsnIPv6Address为DISABLE。 |
| TWANID | 携带twan-id扩展属性 | 可选必选说明：条件可选参数<br>前提条件：该参数在“THREEGPP”配置为“ENABLE”时为可选参数。<br>参数含义：指定是否携带twan-id扩展属性。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不携带该字段。<br>- ENABLE：携带该字段。<br>默认值：无<br>配置原则：无 |
| THREEGPP2 | 支持3gpp2私有扩展属性 | 可选必选说明：必选参数<br>参数含义：指定是否支持3gpp2私有扩展属性。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不支持。<br>- ENABLE：支持。<br>默认值：无<br>配置原则：无 |
| THREEGPP2BSID | 携带3gpp2-bsid私有属性 | 可选必选说明：条件可选参数<br>前提条件：该参数在“THREEGPP2”配置为“ENABLE”时为可选参数。<br>参数含义：指定是否携带3gpp2–bsid私有属性。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不携带该字段。<br>- ENABLE：携带该字段。<br>默认值：无<br>配置原则：如果THREEGPP2配置为DISABLE，THREEGPP2BSID为DISABLE。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/RDSACCTREQVSA]] · RADIUS计费服务器组的私有扩展属性（RDSACCTREQVSA）

## 使用实例

新增名为“radiusgroup”的Radius服务器组为支持RADIUS计费3gpp私有扩展属性，不携带3GPP-IMSI属性，携带3GPP-Charging-ID属性，根据Radius计费消息中携带的这些私有扩展属性字段进行相关的业务控制：

```
SET RDSACCTREQVSA: RDSSVRGRPNAME="radiusgroup", THREEGPP=ENABLE, IMSI=DISABLE, CHARGINGID=ENABLE, THREEGPP2=DISABLE;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-RDSACCTREQVSA.md`
