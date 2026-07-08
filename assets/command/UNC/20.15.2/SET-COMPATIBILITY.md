---
id: UNC@20.15.2@MMLCommand@SET COMPATIBILITY
type: MMLCommand
name: SET COMPATIBILITY（设置QoS兼容性配置）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: COMPATIBILITY
command_category: 配置类
applicable_nf:
- SGSN
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- QoS管理
- QoS兼容性管理
- QoS兼容性配置
status: active
---

# SET COMPATIBILITY（设置QoS兼容性配置）

## 功能

![](设置QoS兼容性配置(SET COMPATIBILITY)_72345835.assets/notice_3.0-zh-cn_2.png)

该命令影响用户会话Qos的协商结果。

**适用网元：SGSN、MME**

此命令用于设置QoS兼容性配置信息。兼容性配置是为了满足不同的运营商对协议的不同要求而作的配置。

## 注意事项

- 此命令执行后立即生效。
- 此命令与[**SET R8QOSMAP**](../EPS QoS参数到Pre-R8 QoS参数映射/设置EPS QoS参数到Pre-R8 QoS参数映射规则（SET R8QOSMAP）_26146234.md)结合使用，配置出QoS的相关映射参数。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| QOSMAP | QoS映射规则 | 可选必选说明：可选参数<br>参数含义：该参数用于指定R99与R97/98之间的QoS映射规则。<br>数据来源：本端规划<br>取值范围：<br>- “STANDARD(标准协议QoS映射规则)”：表示遵守标准协议（协议3GPP TS 23.107）QoS映射规则。<br>- “SELF_DEFINE(自定义QoS映射规则)”：表示遵守自定义QoS映射规则，详见[表1](#ZH-CN_MMLREF_0000001172345835__tab1)和[表2](#ZH-CN_MMLREF_0000001172345835__tab2)。<br>系统初始设置值：STANDARD(标准协议QoS映射规则) |
| RLBCLSMAP | Reliable Class映射规则 | 可选必选说明：可选参数<br>参数含义：该参数用于指定R99与R97/98 QoS参数Reliable Class映射规则以及R97/98 QoS协商规则。<br>数据来源：本端规划<br>取值范围：<br>- “ALLOW（允许使用确认模式LLC）”：- 当R99 QoS参数SDU Error Ratio小于等于10-5时，转换出的R97/98 QoS参数Reliable Class等于2，即UE在GERAN网络使用Acknowledged mode LLC。<br>- R97/98协商时，如果协商出来的Reliable Class小于3，那么使用该协商值。<br>- “PROHIBIT（禁止使用确认模式LLC）”：- 当R99 QoS参数SDU Error Ratio小于等于10-5时，转换出的R97/98 QoS参数Reliable Class等于3，即UE在GERAN网络不使用Acknowledged mode LLC，以防止GUL互操作中的兼容性问题。<br>- R97/98协商时，如果协商出来的Reliable Class小于3，那么就强制将Reliable Class置为3。<br>系统初始设置值：PROHIBIT（禁止使用确认模式LLC） |
| QOSCRCT | QoS纠正 | 可选必选说明：可选参数<br>参数含义：该参数用于决定是否纠正来自对端实体的消息中QoS参数的非法值。<br>数据来源：本端规划<br>取值范围：<br>- “NO(否)”：表示此时不进行纠正，如果来自对端实体的消息中带的QoS参数出现协议规定的reserved值，认为信元出错。<br>- “YES(是)”：表示此时进行纠正，如果来自对端实体的消息中带的QoS参数出现协议规定的reserved值，将其纠正为合法值，继续进行流程处理。<br>系统初始设置值：YES(是) |
| TCADJST | 流量等级调整 | 可选必选说明：可选参数<br>参数含义：该参数用于控制用户在激活请求中请求的Traffic Class为Subscribed时流量等级调整的策略。<br>数据来源：本端规划<br>取值范围：<br>- “NO(不定制调整)”：表示按照Interactive级别进行处理。<br>- “ALL(定制调整)”：表示对所有用户按照实际签约的Traffic Class进行处理。<br>- “APN(只对请求特定APNNI用户调整)”：表示只对请求特定APNNI用户按照实际签约的Traffic Class进行处理。<br>系统初始设置值：NO(不定制调整) |
| APNNI | APNNI | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定APN网络标识地址。<br>前提条件：该参数在<br>“TCADJST(流量等级调整)”<br>参数配置为<br>“APN(只对请求特定APNNI用户调整)”<br>后生效。<br>数据来源：整网规划<br>取值范围：长度不超过62的字符串<br>系统初始设置值：无<br>配置原则：<br>- APN网络标识地址由一个或多个LABEL构成，各LABEL间用“.”间隔。每个LABEL的构成字符只能是字母A~Z或a~z、数字0~9和中划线“-”，字母不区分大小写。例如“HUAWEI.COM”。<br>- APN网络标识地址不能以“rac”、“lac”、“sgsn”或“rnc”开头，不能以“.gprs”结尾，不能取值为“*”。 |
| UPLKADJST | 上行流量调整 | 可选必选说明：可选参数<br>参数含义：该参数用于指定是否进行上行流量调整。<br>数据来源：本端规划<br>取值范围：<br>- NO(否)<br>- YES(是)<br>系统初始设置值：NO(否)<br>配置原则：<br>- 该参数对于会话类和流类业务生效。 |
| MBRUPLK | 上行最大速率 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定上行最大速率。<br>前提条件：该参数在<br>“UPLKADJST(上行流量调整)”<br>参数配置为<br>“YES(是)”<br>后生效。<br>数据来源：本端规划<br>取值范围：1~255<br>系统初始设置值：1<br>配置原则：<br>- 1~63表示速率为1kbit/s~63kbit/s，以1kbit/s递增。<br>- 64~127表示速率为64kbit/s~568kbit/s，以8kbit/s递增。<br>- 128~254表示速率为576kbit/s~8640kbit/s，以64kbit/s递增。<br>- 255表示速率为0kbit/s。 |
| MBRUPLKEX | 扩展上行最大速率 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定扩展上行最大速率。<br>前提条件：该参数在<br>“UPLKADJST(上行流量调整)”<br>参数配置为<br>“YES(是)”<br>后生效。<br>数据来源：本端规划<br>取值范围：0~250<br>系统初始设置值：0<br>配置原则：<br>- 0表示不适用扩展的。<br>- 1~74表示速率为8600kbit/s~16000kbit/s，以100kbit/s递增。<br>- 75~186表示速率为17Mbit/s~128Mbit/s，以1Mbit/s递增。<br>- 187~250表示速率为130Mbit/s~156Mbit/s，以2Mbit/s递增。<br>说明：当本参数的取值为<br>“0”<br>时，系统对上行最大速率的限制取决于<br>“MBRDNLK(上行最大速率)”<br>参数的取值； 当本参数的取值不为<br>“0”<br>时，系统对上行最大速率的限制取决于本参数的取值，<br>“MBRDNLK(上行最大速率)”<br>参数的取值被忽略。 |
| DNLKADJST | 下行流量调整 | 可选必选说明：可选参数<br>参数含义：该参数用于指定是否进行下行流量调整。<br>数据来源：本端规划<br>取值范围：<br>- “NO(否)”<br>- “YES(是)”<br>系统初始设置值：NO(否)<br>配置原则：<br>- 该参数对于会话类和流类业务生效。 |
| MBRDNLK | 下行最大速率 | 可选必选说明：条件可选参数<br>参数含义：该参数用于限制下行最大速率。<br>前提条件：该参数在<br>“DNLKADJST(下行流量调整)”<br>参数配置为<br>“YES(是)”<br>后生效。<br>数据来源：本端规划<br>取值范围：1~255<br>系统初始设置值：1<br>配置原则：<br>- 1~63表示速率为1kbit/s~63kbit/s，以1kbit/s递增。<br>- 64~127表示速率为64kbit/s~568kbit/s，以8kbit/s递增。<br>- 128~254表示速率为576kbit/s~8640kbit/s，以64kbit/s递增。<br>- 255表示速率为0kbit/s。 |
| MBRDNLKEX | 扩展下行最大速率 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定扩展下行最大速率。<br>前提条件：该参数在<br>“DNLKADJST(下行流量调整)”<br>参数配置为<br>“YES(是)”<br>后生效。<br>数据来源：本端规划<br>取值范围：0~250<br>系统初始设置值：0<br>配置原则：<br>- 0表示不适用扩展。<br>- 1~74表示速率为8600kbit/s~16000kbit/s，以100kbit/s递增。<br>- 75~186表示速率为17Mbit/s~128Mbit/s，以1Mbit/s递增。<br>- 187~250表示速率为130Mbit/s~256Mbit/s，以2Mbit/s递增。<br>说明：当本参数的取值为<br>“0”<br>时，系统对下行最大速率的限制取决于<br>“MBRDNLK(下行最大速率)”<br>参数的取值； 当本参数的取值不为<br>“0”<br>时，系统对下行最大速率的限制取决于本参数的取值，<br>“MBRDNLK(下行最大速率)”<br>的取值被忽略。 |
| MTADJST | 平均吞吐量调整 | 可选必选说明：可选参数<br>参数含义：该参数用于指示在GERAN网络中，是否对MS请求的平均吞吐量进行调整。<br>数据来源：本端规划<br>取值范围：<br>- “NO(否)”：表示不进行调整。<br>- “YES(是)”：表示进行调整，即用户PDP上下文使用的R98 QoS参数中的“平均吞吐量(Mean throughput)”等于“31”，“延迟等级(Delay Class)”等于“4”。<br>系统初始设置值：NO(否) |
| DOADJUST | 发送次序调整 | 可选必选说明：可选参数<br>参数含义：该参数用于指定系统是否根据PDP的类型对Delivery order进行调整。<br>数据来源：本端规划<br>取值范围：<br>- “NO(否)”：表示不对Delivery order进行调整。<br>- “YES(是)”：如果“PDP类型”为“IPv4”或“IPv6”，并且QoS为R99以上格式，则将QoS中的“Delivery order”调整为“NO”。<br>系统初始设置值：YES(是) |
| GNQOSVER | GTPV1通道允许发送QoS98信元 | 可选必选说明：可选参数<br>参数含义：该参数用于指定GTP V1通道是否允许发送R98 QoS信元。<br>数据来源：本端规划<br>取值范围：<br>- “NO(否)”：表示对端的GGSN或SGSN不支持GTP V1通道的消息携带R98 QoS信元，携带信元最低为R99 QoS信元，以保证流程可以正常进行。<br>- “YES(是)”：表示GTP V1通道允许发送R98 QoS信元。<br>系统初始设置值：NO(否) |
| SAPI | SAPI协商模式 | 可选必选说明：可选参数<br>参数含义：该参数用于指定SAPI协商模式。<br>数据来源：本端规划<br>取值范围：<br>- “TRAFFIC_CLASS(流量等级)”：表示按照R99 QoS中的TRAFFIC CLASS进行协商。<br>- “RELIAB_CLASS(可靠性)”：表示按照R98 QoS中的RELIABILITY CLASS进行协商。<br>系统初始设置值：TRAFFIC_CLASS(流量等级) |
| SRVHANDOVER2G | Gb模式Service Handover | 可选必选说明：可选参数<br>参数含义：该参数用于指定2G业务创建PFC消息中，是否携带Service Handover信元。<br>数据来源：本端规划<br>取值范围：<br>- “NOT_SUPPORT(不支持)”<br>- “FIRST_PDP_ONLY(只对用户的首PDP支持)”<br>- “MULT_PDP(多PDP支持)”<br>系统初始设置值：NOT_SUPPORT(不支持)<br>说明：Service Handover信元作用请参见<br>[**ADD SRVHANDOVER**](../../../业务安全管理/会话管理/业务切换策略/增加业务切换策略(ADD SRVHANDOVER)_26305476.md)<br>。 |
| SRVHANDOVER3G | Iu模式Service Handover | 可选必选说明：可选参数<br>参数含义：该参数用于指定3G业务RAB指派消息中，是否携带Service Handover信元。<br>数据来源：本端规划<br>取值范围：<br>- “NOT_SUPPORT(不支持)”<br>- “FIRST_PDP_ONLY(只对用户的首PDP支持)”<br>- “MULT_PDP(多PDP支持)”<br>系统初始设置值：NOT_SUPPORT(不支持)<br>说明：Service Handover信元作用请参见<br>[**ADD SRVHANDOVER**](../../../业务安全管理/会话管理/业务切换策略/增加业务切换策略(ADD SRVHANDOVER)_26305476.md)<br>。 |
| HARP | H值 | 可选必选说明：可选参数<br>参数含义：该参数用于设置EPS ARP和Pre-R8 ARP转换参数H值。<br>数据来源：本端规划<br>取值范围：1~13<br>系统初始设置值：5<br>说明：转换规则详见<br>[表3](#ZH-CN_MMLREF_0000001172345835__tab3)<br>和<br>[表4](#ZH-CN_MMLREF_0000001172345835__tab4)<br>。 |
| MARP | M值 | 可选必选说明：可选参数<br>参数含义：该参数用于设置EPS ARP和Pre-R8 ARP转换参数M值。<br>数据来源：本端规划<br>取值范围：2~14<br>系统初始设置值：10<br>配置原则：<br>- M值必须满足：M值≥H值+1。<br>说明：转换规则详见<br>[表3](#ZH-CN_MMLREF_0000001172345835__tab3)<br>和<br>[表4](#ZH-CN_MMLREF_0000001172345835__tab4)<br>。 |
| CORREXTBR | 纠正扩展比特率 | 可选必选说明：可选参数<br>参数含义：该参数用于控制QoS协商，当用户激活请求携带的比特率和扩展比特率同时为0时，是否用签约中的R5 QoS和R7 QoS填写扩展比特率。<br>数据来源：本端规划<br>取值范围：<br>- “YES(是)”：使用签约的R5 QoS和R7 QoS填写扩展比特率充。<br>- “NO(否)”：使用“UPLKADJST（上行流量调整）”和“DNLKADJST(下行流量调整)”填充扩展比特率。<br>系统初始设置值：YES(是) |
| LIMITMBR | 限制MBR | 可选必选说明：可选参数<br>参数含义：该参数用于控制<br>UNC<br>系统无UE的具体带宽能力信息时，UE请求了R5 QoS特征参数（Signalling Indication和Source Statistics Descriptor），但是未请求大于16Mbps的带宽，<br>UNC<br>系统是否限制UE的带宽能力为16Mbps。<br>数据来源：本端规划<br>取值范围：<br>- “YES(限制上下行速率)”：UNC系统限制UE只能使用小于等于16Mbps的下行速率和小于等于8Mbps的上行速率。<br>- “NO(不限制下行速率)”：UNC系统不限制UE只能使用小于等于16Mbps的下行速率，但限制UE只能使用小于等于8Mbps的上行速率。<br>- “NO_LIMIT_BOTH(不限制上下行速率)”：UNC系统不限制UE的上下行速率。<br>系统初始设置值：NO(不限制下行速率)<br>说明：- 选择“NO(不限制下行速率)”或“NO_LIMIT_BOTH(不限制上下行速率)”后，当UNC给UE下发大于16Mbps的下行带宽或大于8Mbps的上行带宽时，如果UE不支持，会发起原因值为QoS Not Accept的去激活流程。UNC记录该信息，后续会限制该UE只能使用小于等于16Mbps的下行带宽和小于等于8Mbps的上行带宽，避免网络反复下发UE不支持的带宽，UE无法进行业务。当用户使用的IMEI/IMEISV发生变化，即用户更换了终端后，系统将重新探测UE的QoS能力，因此建议通过[**ADD GBIMEICFG**](../../../业务安全管理/设备检查管理/Gb模式IMEI配置/增加Gb模式IMEI配置(ADD GBIMEICFG)_26145632.md)和[**ADD IUIMEICFG**](../../../业务安全管理/设备检查管理/Iu模式IMEI配置/增加Iu模式IMEI配置(ADD IUIMEICFG)_72225315.md)命令打开系统获取IMEI/IMEISV的开关。 |
| WTL | WCDMA到LTE网络优选 | 可选必选说明：可选参数<br>参数含义：该参数用于指示是否支持WCDMA到LTE网络优选。<br>数据来源：本端规划<br>取值范围：<br>- “YES(是)”：如果运营商允许SGSN携带E-UTRAN Service Handover信元给RNC，则配置为“YES(是)”。<br>- “NO(否)”<br>系统初始设置值：NO(否) |
| GTL | GPRS到LTE网络优选 | 可选必选说明：可选参数<br>参数含义：该参数用于指示是否支持GPRS到LTE网络优选。<br>数据来源：本端规划<br>取值范围：<br>- “YES(是)”：如果运营商允许SGSN携带含Service UTRAN CCO Value part的Service UTRAN CCO的信元给BSC，则配置为“YES(是)”。<br>- “NO(否)”<br>系统初始设置值：NO(否) |
| EPSQOSEXT2 | 发送EPS QoS Extended-2 | 可选必选说明：可选参数<br>参数含义：该参数用于指定当P-GW或PCC决策的承载速率大于256M时，MME是否在给UE发送的EPS QoS中携带Extended-2。<br>说明：根据协议3GPP TS 24.301，Extended-2信元包括:<br>- Maximum bit rate for uplink (extended-2)<br>- Maximum bit rate for downlink (extended-2)<br>- Guaranteed bit rate for uplink (extended-2)<br>- Guaranteed bit rate for downlink (extended-2)<br>数据来源：全网规划<br>取值范围：<br>- “YES(是)”：当P-GW或PCC决策的承载速率大于256M时，MME把该速率直接发送给终端，在给UE发送的EPS QoS中携带Extended-2。<br>- “NO(否)”：当P-GW或PCC决策的承载速率大于256M时，MME把该速率转换为256M，在给UE发送的EPS QoS中不携带Extended-2。<br>系统初始设置值：NO(否) |
| GTPV2EXTQCI | GTPV2通道发送扩展QCI | 可选必选说明：可选参数<br>参数含义：该参数用于控制Old MME/S4-SGSN向New MME/S4-SGSN发送的消息中携带扩展QCI还是标准QCI。确保当用户在MME/S4-SGSN间移动时，与对端设备兼容。<br>数据来源：全网规划<br>取值范围：<br>- “NOT_SUPPORT(不支持)”：把扩展QCI转换为标准QCI后发送给New MME/S4-SGSN。适用于New MME/S4-SGSN不支持扩展QCI的场景。<br>- “SUPPORT(支持)”：把扩展QCI直接发送给New MME/S4-SGSN。适用于New MME/S4-SGSN支持扩展QCI的场景。<br>- “SAMEPLMN_SUPPORT(同PLMN间支持)”：用户在同PLMN间移动时，把扩展QCI直接发送给New MME/S4-SGSN；用户在跨PLMN间移动时，把扩展QCI转换为标准QCI后发送给New MME/S4-SGSN。适用于同PLMN支持扩展QCI，异PLMN不支持扩展QCI的场景。<br>系统初始设置值：SUPPORT(支持) |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@COMPATIBILITY]] · QoS兼容性配置（COMPATIBILITY）

## 使用实例

设置 “QoS映射规则” 选择 “STANDARD” ， “QoS纠正” 选择 “NO” ， “流量等级调整” 选择 “NO” ， “Iu模式Service Handover” 选择 “NOT_SUPPORT” ， “发送EPS QoS Extended-2” 选择 “YES” ，配置格式如下：

SET COMPATIBILITY: QOSMAP=STANDARD, QOSCRCT=NO, TCADJST=NO, SRVHANDOVER3G=NOT_SUPPORT, EPSQOSEXT2=YES;

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-COMPATIBILITY.md`
