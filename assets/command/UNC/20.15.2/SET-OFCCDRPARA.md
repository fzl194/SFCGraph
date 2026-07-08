---
id: UNC@20.15.2@MMLCommand@SET OFCCDRPARA
type: MMLCommand
name: SET OFCCDRPARA（配置离线计费话单参数）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: OFCCDRPARA
command_category: 配置类
applicable_nf:
- SGW-C
- PGW-C
- SMF
effect_mode: 立即生效
is_dangerous: true
max_records: 1
category_path:
- 业务服务管理
- 会话管理
- 计费管理
- 离线计费
- 离线计费基础参数
- 离线公共参数
status: active
---

# SET OFCCDRPARA（配置离线计费话单参数）

## 功能

**适用NF：SGW-C、PGW-C、SMF**

![](配置离线计费话单参数（SET OFCCDRPARA）_09896905.assets/notice_3.0-zh-cn_2.png)

本命令属于高危命令，配置SPCDRCONTROL=PGW_SGW_CDR后需检查流量容器占用率，防止资源耗尽引发用户激活成功率下降

该命令用于配置离线计费话单参数。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | SPCDRCONTROL | PGWCDRLOTVSW | PGWCDRLOSDRATSW | PGWCDRLOSDAMBR | SRVNODEADDR | PSFCIFORMAT | CCFHCDRSW | R6EGCDRCCFHSW | LASTACTIVITYSW | SGWLOTVQOSEXT | PGWLOTVQOSEXT | PGWLOSDQOSEXT | SGWLOTVCPEPS | SGWLOTVSPRATE | PGWLOSDSPRATE | PGWLOSDAPNRATE | PGWIPV6IFID | SGWIPV6IFID | CDRAFTERTCSW | CDRAFTERTCCAUSE | STGENCRYPT |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 初始值 | PGW_CDR | DISABLE | DISABLE | DISABLE | GTPC_ADDRESS | HEX | DISABLE | DISABLE | DISABLE | DISABLE | DISABLE | DISABLE | DISABLE | DISABLE | DISABLE | DISABLE | INTERFACE_ID_EMPTY | INTERFACE_ID_EMPTY | ENABLE | MANAGEMENT_INTERVENTION | DISABLE |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GSNNODEIDPREFIX | gsn-node-id字段前缀 | 可选必选说明：可选参数<br>参数含义：该字段用于配置话单中的gsn-node-id字段的前缀。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～17。<br>默认值：无<br>配置原则：<br>- 话单中的gsn-node-id字段根据此参数和GNIDelimiter生成，当GNIDelimiter未配置时，话单中的gsn-node-id字段为此参数值；当GNIDelimiter配置时，话单中的gsn-node-id字段为此参数、GNIDelimiter、1的组合。<br>- 在线计费CCR消息中node-id信元值也为此参数值。 |
| GNIDELIMITER | gsn-node-id字段分隔符 | 可选必选说明：可选参数<br>参数含义：该字段用于配置话单中的gsn-node-id字段的分隔符。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1。<br>默认值：无<br>配置原则：话单中的gsn-node-id字段根据此参数和GSNNODEIDPREFIX生成，当此参数未配置时，话单中的gsn-node-id字段为GSNNODEIDPREFIX值；当此参数配置时，话单中的gsn-node-id字段为GSNNODEIDPREFIX、此参数、1的组合。 |
| SPCDRCONTROL | SP合一网关话单控制 | 可选必选说明：可选参数<br>参数含义：该字段用于配置控制SP合一用户只产生PGW-CDR还是同时产生SGW-CDR和PGW-CDR话单。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- PGW_CDR：PGW-CDR。<br>- PGW_SGW_CDR：PGW-CDR和SGW-CDR。<br>默认值：无<br>配置原则：无 |
| PGWCDRLOTVSW | PGW-CDR携带List of Traffic Volume | 可选必选说明：可选参数<br>参数含义：该字段用于控制PGW-CDR中是否携带listOfTrafficVolume。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：无 |
| PGWCDRLOSDRATSW | PGW-CDR话单的List of Service Data携带RAT-Type | 可选必选说明：可选参数<br>参数含义：该字段用于控制PGW-CDR话单业务容器中是否携带RAT-Type信元。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：无 |
| PGWCDRLOSDAMBR | PGW-CDR话单List of Service Data容器携带APN-AMBR开关 | 可选必选说明：可选参数<br>参数含义：该字段用于控制PGW-CDR话单List of Service Data容器携带APN-AMBR开关。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：无 |
| SRVNODEADDR | GCDR话单的sgsnAddress值 | 可选必选说明：可选参数<br>参数含义：该字段用于控制sgsnAddress字段是携带SGSN的数据面地址还是控制面地址。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- GTPU_ADDRESS：GTPU地址。<br>- GTPC_ADDRESS：GTPC地址。<br>默认值：无<br>配置原则：无 |
| PSFCIFORMAT | OCS故障导致用户离线后产生的话单pSFreeFormatData格式 | 可选必选说明：可选参数<br>参数含义：该字段用于控制OCS故障导致用户离线后产生的话单pSFurnishChargingInformatio中pSFreeFormatData字段的格式。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- HEX：十六进制。<br>- ASCII：ASCII。<br>默认值：无<br>配置原则：无 |
| CCFHCDRSW | CCFH强制产生话单开关 | 可选必选说明：可选参数<br>参数含义：该字段用于控制CCFH（Credit Control Failure Handling）是否强制产生话单。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：无 |
| CCFHCDRCC | CCFH强制产生话单填充的Charging Characteristics值 | 可选必选说明：条件可选参数<br>前提条件：该参数在“CCFHCDRSW”配置为“ENABLE”时为可选参数。<br>参数含义：该字段用于配置CCFH强制产生话单填充的Charging Characteristics的值。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～6。该参数为十六进制数据类型，仅支持输入0x/X、a-f/A-F 、0-9，允许不输入0x前缀，字母不区分大小写，取值范围0x0000~0xFFFF。<br>默认值：无<br>配置原则：无 |
| R6EGCDRCCFHSW | R6 eGCRD支持CCFH强制生成话单 | 可选必选说明：可选参数<br>参数含义：该字段用于控制CCFH发生时是否支持强制产生R6 eGCDR话单。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：无 |
| LASTACTIVITYSW | Last Activity功能开关 | 可选必选说明：可选参数<br>参数含义：该字段用于控制是否支持Last Activity功能。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：软参BYTE88设置为3后才生效。 |
| SGWLOTVQOSEXT | SGW-CDR流量容器携带扩展Qos参数开关 | 可选必选说明：可选参数<br>参数含义：该字段用于控制SGW-CDR流量容器EPC Qos中携带扩展Qos参数。<br>数据来源：对端协商<br>取值范围：枚举类型。<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：无 |
| PGWLOTVQOSEXT | PGW-CDR流量容器携带扩展Qos参数开关 | 可选必选说明：可选参数<br>参数含义：该字段用于控制PGW-CDR流量容器EPC Qos中携带扩展Qos参数。<br>数据来源：对端协商<br>取值范围：枚举类型。<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：无 |
| PGWLOSDQOSEXT | PGW-CDR业务容器携带扩展Qos参数开关 | 可选必选说明：可选参数<br>参数含义：该字段用于控制PGW-CDR业务容器EPC Qos中携带扩展Qos参数。<br>数据来源：对端协商<br>取值范围：枚举类型。<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：无 |
| SGWLOTVCPEPS | SGW-CDR话单的LoTV携带CP CIoT EPS Optimisation Indicator | 可选必选说明：可选参数<br>参数含义：该字段用于控制SGW-CDR话单List of Traffic Volumes是否携带CP CIoT EPS Optimisation Indicator。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：无 |
| SGWLOTVSPRATE | SGW-CDR话单的LoTV携带Serving PLMN Rate Control | 可选必选说明：可选参数<br>参数含义：该参数用于控制SGW-CDR话单的List of Traffic Volumes是否携带Serving PLMN Rate Control。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：无 |
| PGWLOSDSPRATE | PGW-CDR话单LoSD携带Serving PLMN Rate Control | 可选必选说明：可选参数<br>参数含义：该参数用于控制PGW-CDR话单的List of Service Data是否携带Serving PLMN Rate Control。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：无 |
| PGWLOSDAPNRATE | PGW-CDR话单的LoSD携带APN Rate Control | 可选必选说明：可选参数<br>参数含义：该参数用于控制PGW-CDR话单的List of Service Data是否携带APN Rate Control。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：无 |
| PGWIPV6IFID | G-CDR/PGW-CDR中用户IPv6地址Interface Identifier填写方式 | 可选必选说明：可选参数<br>参数含义：该参数用于控制G-CDR/PGW-CDR中用户IPv6地址Interface Identifier填写方式。<br>数据来源：全网规划<br>取值范围：枚举类型。<br>- INTERFACE_ID_EMPTY：IPv6地址Interface Identifier填写全0。<br>- INTERFACE_ID_REAL：IPv6地址Interface Identifier填写真实值。<br>默认值：无<br>配置原则：无 |
| SGWIPV6IFID | SGW-CDR中用户IPv6地址Interface Identifier填写方式 | 可选必选说明：可选参数<br>参数含义：该参数用于控制SGW-CDR中用户IPv6地址Interface Identifier填写方式。<br>数据来源：全网规划<br>取值范围：枚举类型。<br>- INTERFACE_ID_EMPTY：IPv6地址Interface Identifier填写全0。<br>- INTERFACE_ID_REAL：IPv6地址Interface Identifier填写真实值。<br>默认值：无<br>配置原则：无 |
| CDRAFTERTCSW | 费率切换后强制产生话单开关 | 可选必选说明：可选参数<br>参数含义：该字段用于控制当费率切换后的使用量不满足产生话单的条件时，是否对费率切换后的使用量强制产生一张话单。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ENABLE：对费率切换后的使用量强制产生一张话单。<br>- DISABLE：对费率切换后的使用量不强制产生话单。<br>默认值：无<br>配置原则：离线计费模板参数CDRTRIGMAXCHNG配置为ENABLE，参数CONDITIONCHANGE参数配置为1时，SMF处理费率切换时会对费率切换前的使用量产生一张话单后，如果费率切换后的用量不强制产生一张话单，会导致费率切换后大量用户时间阈值同时触发，产生大量话单，导致SMF CPU使用率大幅波动，同时对CG产生冲击。为避免此现象发生，建议配置为ENABLE。 |
| CDRAFTERTCCAUSE | 费率切换后强制产生话单的关闭原因 | 可选必选说明：条件可选参数<br>前提条件：该参数在“CDRAFTERTCSW”配置为“ENABLE”时为可选参数。<br>参数含义：该字段用于控制费率切换后的使用量强制产生的话单关闭原因值。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- MANAGEMENT_INTERVENTION：话单关闭原因值填充为managementIntervention。<br>- MAX_CHANGE_COND：话单关闭原因值填充为maxChangeCond。<br>默认值：无<br>配置原则：无 |
| STGENCRYPT | 话单缓存加密开关 | 可选必选说明：可选参数<br>参数含义：该字段用于控制是否对4G缓存话单进行加密。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不对4G缓存话单进行加密。<br>- ENABLE：对4G缓存话单进行加密。<br>默认值：无<br>配置原则：计费消息的加密存储会增加额外的性能开销，开启加密功能前请联系华为技术服务评估当前系统是否满足开启条件。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/OFCCDRPARA]] · 离线计费话单参数（OFCCDRPARA）

## 使用实例

配置离线计费话单参数，设置SP合一用户只产生PGW-CDR话单，PGW-CDR中携带listOfTrafficVolume，话单serving node address的携带GTPC地址：

```
SET OFCCDRPARA:SPCDRCONTROL=PGW_CDR,PGWCDRLOTVSW=ENABLE,SRVNODEADDR=GTPC_ADDRESS;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-OFCCDRPARA.md`
