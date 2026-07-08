---
id: UNC@20.15.2@MMLCommand@MOD IMSISMCHAR
type: MMLCommand
name: MOD IMSISMCHAR（修改QoS协商参数）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: IMSISMCHAR
command_category: 配置类
applicable_nf:
- SGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- QoS管理
- Pre-R8 QoS
- QoS协商控制
- QoS协商参数管理
status: active
---

# MOD IMSISMCHAR（修改QoS协商参数）

## 功能

**适用网元：SGSN**

该命令用于修改SM属性配置：

- 当用户使用GPRS接入网接入并进行PDP激活时，分以下三种场景进行处理：
    - 如果用户所在的IMSI号段或用户归属地在该表中配置，并且“是否配置2G QoS”参数配置为“是”，系统使用该表中配置的2G QoS参数对PDP上下文使用的QoS进行限制。
    - 如果用户所在的IMSI号段或用户归属地在该表中配置，但是“是否配置2G QoS”参数配置为“否”，系统将为该条配置指定默认的2G QoS参数，系统使用匹配到“用户范围”为“ALL_USER（所有用户）”记录中所配置的默认QoS参数对PDP上下文使用的QoS进行限制。
    - 如果用户所在的IMSI号段和用户归属地未在该表中配置，系统使用该命令“用户范围”为“所有用户”记录中配置的QoS参数对PDP上下文使用的QoS进行限制。
- 当用户使用UMTS接入网接入并进行PDP激活时，分以下三种场景进行处理：
    - 如果用户所在的IMSI号段或用户归属地在该表中配置，并且“是否配置3G QoS”参数配置为“是”，系统使用该表中配置的3G QoS参数对PDP上下文使用的QoS进行限制。
    - 如果用户所在的IMSI号段或用户归属地在该表中配置，但是“是否配置3G QoS”参数配置为“否”，系统将为该条配置指定默认的3G QoS参数，系统使用匹配到“用户范围”为“ALL_USER（所有用户）”记录中所配置的默认QoS参数对PDP上下文使用的QoS进行限制。
    - 如果用户所在的IMSI号段和用户归属地未在该表中配置，系统使用该命令“用户范围”为“所有用户”记录中配置的QoS参数对PDP上下文使用的QoS进行限制。
- QoS各参数的取值及含义具体请参见3GPP TS 23.107（QoS协议）。
- 对于2G和3G QoS参数，当“协商方式”为“NET_NEGO_QOS（网络侧协商QoS）”或“MIX_QOS（混合模式）”时生效。

## 注意事项

该命令部分参数与相关特性license共同完成该特性的开启，请在设置参数前使用 [**DSP LICENSE**](../../../../../../../平台服务管理/操作维护/License管理/显示License(DSP LICENSE)_00360098.md) 命令确认对应特性license是否得到授权，执行 [**LST LICENSESWITCH**](../../../../../../../平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md) 命令确认特性开关状态为 “ENABLE(打开)” ，具体相关特性请参考参数的说明。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGE | 用户范围 | 可选必选说明：必选参数<br>参数含义：该参数用于指定所包含的用户范围。<br>数据来源：整网规划<br>取值范围：<br>- “ALL_USER（所有用户）”<br>- “IMSI_PREFIX（指定IMSI前缀）”<br>- “IMSI_RANGE（指定IMSI范围）”<br>- “FOREIGN_USER（外网用户）”<br>- “HOME_USER（本网用户）”<br>默认值：无<br>说明：- 当参数设置为“IMSI_PREFIX（指定IMSI前缀）”或“IMSI_RANGE（指定IMSI范围）”时，“基于IMSI号段的QoS控制”特性的相关license授权并开启后，此参数配置才生效（特性编号：WSFD-105104，License部件编码：LKV2IMSIQOS02）。 |
| IMSIPRE | IMSI前缀 | 可选必选说明：条件必选参数<br>参数含义：该参数用于系统对用户的IMSI进行匹配，从而区分不同的用户群。<br>前提条件：该参数在<br>“用户范围”<br>参数配置为<br>“IMSI_PREFIX（指定IMSI前缀）”<br>后生效。<br>数据来源：整网规划<br>取值范围：1～15位十进制字符串<br>默认值：无<br>说明：IMSI前缀的匹配方式采取由前向后的最长匹配，即若对于用户可以匹配到多个用户群，则使用IMSI前缀最长的用户群配置。 |
| IMSI | IMSI | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定IMSI，对该IMSI所在号段进行修改。<br>前提条件：只有<br>“用户范围”<br>为<br>“IMSI_RANGE（指定IMSI范围）”<br>时，该参数才有效。<br>数据来源：整网规划<br>取值范围：1～15位十进制字符串<br>默认值：无 |
| NOID | 运营商标识 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定运营商标识。<br>前提条件：该参数在“用户范围”参数配置为“外网用户”或“本网用户”后生效。 对于外网用户，该参数是外网用户对应的签订互联PLMN漫游协议的运营商标识，对于本网用户，该参数是本网用户对应的运营商标识。<br>数据来源：整网规划<br>取值范围：0～64，128～254<br>默认值：无<br>说明：- 若该参数需要配置为0或128～254之间的值时，请先在[**ADD MNO**](../../../../网络管理/归属网络运营商管理/MNO管理/MNO配置表/增加MNO配置信息(ADD MNO)_72345671.md)中配置取值相同的“MNOID”参数。<br>- 若该参数需要配置为1～64之间的值时，须先在[**ADD MVNO**](../../../../网络管理/归属网络运营商管理/MVNO管理/MVNO配置表/增加MVNO配置信息(ADD MVNO)_72225747.md)中配置取值相同的“MVNOID”参数。 |
| USERSUBTYPE | 用户子类 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定本网用户子类，控制用户QoS参数。<br>UNC<br>将签约数据中获取的用户子类和本参数的配置进行匹配，选择匹配用户子类对应的QoS参数。<br>签约数据中心接口为Gr时，<br>UNC<br>能够获取HLR Number，通过HLR Number可以细分本网用户为本地用户或异地用户；当签约数据中心接口为S6d时，<br>UNC<br>不能对本网用户细分为本地用户或异地用户，统一确认为本网所有用户。<br>前提条件：该参数在<br>“SUBRANGE（用户范围）”<br>参数配置为<br>“HOME_USER（本网用户）”<br>时生效。<br>数据来源：整网规划<br>取值范围：<br>- “HOME_ALL_USER(本网所有用户)”<br>- “HOME_LOCAL_USER(本网本地用户)”<br>- “HOME_UNLOCAL_USER(本网异地用户)”<br>默认值：无<br>说明：用户子类对应的QoS参数优先级从高到低为：<br>“本网本地用户(Home Local User)”<br>或<br>“本网异地用户(Home Unlocal User)”<br>，<br>“本网所有用户(Home All User)”<br>。 |
| APNNI | APN网络标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定APN网络标识。<br>数据来源：整网规划<br>长度范围：1～62<br>默认值：无<br>说明：- “APNNI”（APN网络标识）由一个或多个LABEL构成，各LABEL间用“.”间隔。每个LABEL的构成字符只能是字母A～Z或a～z、数字0～9和中划线“-”，字母不区分大小写。APN网络标识地址不能以“rac”、“lac”、“sgsn”或“rnc”开头，不能以“.gprs”结尾。“*”表示通配符，如果根据用户使用的APNNI无法匹配到对应的记录，则使用根据IMSI、UE接入能力与通配符“*”查询到的配置记录。<br>- GGSN/P-GW采取何种PCC策略是以APN为粒度的，如果网关侧下发QoS策略使用PCRF，UNC建议用网络侧控制模式，以PCRF的策略优先；如果网关没有部署PCRF，UNC则建议用QoS协商模式。<br>- 不支持输入*和其他字符组合。 |
| UEACCCAP | UE接入能力 | 可选必选说明：必选参数<br>参数含义：该参数用于指定UE接入能力。<br>数据来源：整网规划<br>取值范围：<br>- “ALL_UE（所有UE ）”<br>- “EUTRAN_INCAPABLE_UE（无E-UTRAN接入能力的UE ）”<br>- “EUTRAN_CAPABLE_UE（有E-UTRAN接入能力的UE ）”<br>默认值：无<br>说明：- GERAN/UTRAN接入模式下SGSN通过GnGp接口连接到传统的GGSN，网络通常不部署PCRF，融合GGSN/P-GW通常会部署PCRF，UNC会根据UE接入能力参数配合网关不同的PCRF策略。 |
| EARP | 使用演进ARP | 可选必选说明：可选参数<br>参数含义：该参数用于指定是否使用演进ARP。<br>数据来源：整网规划<br>取值范围：<br>- “NO(否)”<br>- “YES(是)”<br>说明：- 当取值“YES(是)”时，UNC作为GnGp SGSN支持Evolved ARP，SGSN在发送给GGSN的Create PDP Context Request消息中会携带Evolved ARP信元，通知GGSN自己支持Evolved ARP，GGSN在Create PDP Context Response消息中指配Evolved ARP，SGSN会将该Evolved ARP直接作为下发给RAN的ARP参数。<br>- 当取值“NO(否)”时，UNC作为GnGp SGSN不支持Evolved ARP，SGSN在发送给GGSN的Create PDP Context Request消息中不携带Evolved ARP信元，通知GGSN自己不支持Evolved ARP，GGSN在Create PDP Context Response消息中无需指配Evolved ARP，SGSN根据[**ADD ARPPARA**](../../QoS应用/ARP转换/增加ARP策略参数配置(ADD ARPPARA)_72225903.md)命令的配置转换出ARP参数，下发给RAN。<br>默认值：无 |
| NTYPE | 协商方式 | 可选必选说明：可选参数<br>参数含义：该参数用于指定协商方式。<br>数据来源：整网规划<br>取值范围：<br>- “NET_NEGO_QOS（网络侧协商QoS）”：UNC作为SGSN根据签约QoS、UE请求的QoS、自身的QoS等一起进行协商，只允许其它网元协商降低QoS，不允许其它网元升高QoS。<br>- “NET_CTRL_QOS（网络侧控制QoS）”：UNC作为SGSN把签约QoS传递给GGSN，由PCRF决策用户使用的QoS，SGSN允许PCRF升高QoS。<br>- “MIX_QOS（混合模式）”：UNC作为SGSN按照“NET_NEGO_QOS（网络侧协商QoS）”协商QoS，但是允许网络侧提升QoS，这样：对于PCC用户，PCRF可以决策用户使用的QoS；对于非PCC用户，仍然由SGSN决策用户使用的QoS。<br>默认值：无<br>说明：- 当网络中未部署PCC策略时，该场景推荐选择“NET_NEGO_QOS（网络侧协商QoS）”。<br>- 当网络中部署了PCC策略，该场景推荐选择<br>“NET_CTRL_QOS（网络侧控制QoS）”<br>。在这种模式下，要求网关/PCRF具备QoS控制功能，使得UE收到的QoS符合网络规范，并兼顾GUL互操作的要求，否则，推荐选择<br>“NET_MIX_QOS（混合模式）”<br>。QoS网络规范举例如下：<br>- Delivery Order，根据3GPP TS 23.107，PDP Type为IP类型时，该参数取值应为Without Delivery Order。<br>- 2G使用LLC确认模式可能导致数传速率下降。建议SDU Error Ratio取值大于等于10—4，Reliability Class取值大于2，避免使用LLC确认模式。GUL互操作要求举例如下：<br>- 需要限制缺省承载为Non-GBR承载，防止用户从GU网络切换到LTE网络后，EPC网络不允许缺省承载为GBR承载而导致承载创建失败。<br>- 如果网络中同时存在PCC用户和非PCC用户，推荐选择“NET_MIX_QOS（混合模式）”。“PCC模式的本地QoS策略控制”特性相关License授权并开启后，此参数配置才生效（特性编号：WSFD-105105，License部件编码：LKV2NQOS01），否则，UNC按照“NET_NEGO_QOS（网络侧协商QoS）”处理。 |
| PROCMODE | 流程模式 | 可选必选说明：可选参数<br>参数含义：该参数用于指定流程模式。<br>数据来源：整网规划<br>前提条件：该参数在<br>“协商方式”<br>配置为<br>“NET_CTRL_QOS（网络侧控制QoS）”<br>时生效。<br>取值范围：<br>- “GPRS（GPRS模式）”<br>- “EPS（EPS模式）”<br>默认值：无<br>说明：- “EPS模式”下，UNC作为GnGp SGSN对流程的整体处理原则与S4 SGSN或MME类似：- PDP Context激活流程中如果有网元无法满足GGSN指定的QoS，UNC作为SGSN会拒绝相关PDP Context的激活请求。<br>- RAB被释放，UNC作为SGSN，会去激活实时类PDP Context。<br>- RAB重建失败，UNC作为SGSN，会去激活相关的PDP Context。<br>- “GPRS模式”下，UNC作为GnGp SGSN对流程的整体处理原则与"网络侧协商QoS模式"类似：- PDP Context激活流程中如果有网元无法满足GGSN指定的QoS，UNC作为SGSN不直接拒绝相关PDP Context的激活请求，而是通知GGSN，由GGSN进行处理决策。<br>- RAB释放时，UNC作为SGSN，会根据[**SET IUSMPROCTRL**](../../../../业务安全管理/会话管理/SM流程管理/Iu模式SM流程控制参数/设置Iu模式SM流程控制参数（SET IUSMPROCTRL）_72345289.md)中的“PPU（是否使用保留过程）”参数的配置决定对实时类PDP Context的处理。<br>- RAB重建失败，UNC作为SGSN，不会去激活相关的PDP Context。 |
| GBLOCCHANGE | Gb模式QoS协商 | 可选必选说明：可选参数<br>参数含义：该参数用于指定Gb模式下，当CN节点、RAT、RA或者小区更新时是否进行QoS协商。<br>数据来源：整网规划<br>前提条件：该参数在<br>“协商方式”<br>配置为<br>“NET_NEGO_QOS（网络侧协商QoS）”<br>或<br>“MIX_QOS（混合模式）”<br>时生效。<br>取值范围：<br>- “CN_NODE_CHGD(CN节点更新)”：表示在Inter CN节点，新侧为Gb模式的流程中，UNC作为新侧CN节点，是否需要重新协商QoS。<br>- “RAT_CHGD(RAT更新)”：表示在IntraUNC节点，新侧为Gb模式的Inter System change流程中，UNC是否需要重新协商QoS。<br>- “RA_UPD(RA更新)”：表示在IntraUNC节点，新侧为Gb模式的RAU流程中，UNC是否需要重新协商QoS。<br>- “CELL_UPD(Cell更新)”：表示在小区更新流程中，对于只支持R97或R98 QoS版本的UE，UNC是否需要重新协商QoS。<br>默认值：无 |
| IULOCCHANGE | Iu模式QoS协商 | 可选必选说明：可选参数<br>参数含义：该参数用于指定Iu模式下，当CN节点、RAT、RA或者RNC更新时是否进行QoS协商。<br>数据来源：整网规划<br>前提条件：该参数在<br>“协商方式”<br>配置为<br>“NET_NEGO_QOS（网络侧协商QoS）”<br>或<br>“MIX_QOS（混合模式）”<br>时生效。<br>取值范围：<br>- “CN_NODE_CHGD(CN节点更新)”：表示在Inter CN节点，新侧为Iu模式的流程中，UNC作为新侧CN节点，是否需要重新协商QoS。<br>- “RAT_CHGD(RAT更新)”：表示在IntraUNC节点，新侧为Iu模式的Inter System change流程中，UNC是否需要重新协商QoS。<br>- “RA_UPD(RA更新)”：表示在IntraUNC节点，新侧为Iu模式的RAU或Relocation流程中，如果RA发生了变化，UNC是否需要重新协商QoS。<br>- “RNC_CHGD(RNC更新)”：表示在RNC改变的流程中，UNC是否需要为UE重新协商QoS。<br>默认值：无 |
| SUBQOS | 覆盖签约QoS | 可选必选说明：可选参数<br>参数含义：该参数用于指定是否使用SGSN默认QoS覆盖签约QoS。SGSN默认QoS是指配置的QoS参数，签约QoS是指SGSN从HSS或HLR上获取的QoS。<br>数据来源：整网规划<br>取值范围：<br>- “NO(否)”<br>- “YES(是)”<br>默认值：无<br>说明：<br>- 参数配置为“NO(否)”表示用户签约数据中的QoS信息不变。<br>- 参数配置为“YES(是)”表示使用配置中的QoS值对用户签约数据中的QoS信息进行覆盖。 |
| QOS2G | 是否配置2G QoS | 可选必选说明：可选参数<br>参数含义：该参数用于指定是否配置2G QoS。<br>数据来源：整网规划<br>取值范围：<br>- “NO(否)”<br>- “YES(是)”<br>默认值：无<br>配置原则：<br>- 当该IMSI号段用户使用GPRS接入网接入并进行PDP激活，且系统使用该表中配置的2G QoS参数对PDP上下文使用的QoS进行限制时，选择“YES(是)”。<br>- 当该IMSI号段用户使用GPRS接入网接入并进行PDP激活，且系统使用2G QoS的默认参数对PDP上下文使用的QoS进行限制时，选择“NO(否)”。<br>- 用户范围为“ALL_USER（所有用户）”时，该表中的2G QoS参数不能配置为“NO(否)”。 |
| RC2G | 2G QoS可靠性 | 可选必选说明：可选参数<br>参数含义：该参数用于指定SGSN支持的缺省QoS可靠性等级（Reliability Class），可靠性指示了一个应用对传输特性的要求。<br>数据来源：整网规划<br>前提条件：该参数在<br>“是否配置2G QoS”<br>配置为<br>“YES(是)”<br>时生效。<br>取值范围：<br>- “ACKGTP(Ack GTP/LLC/RLC Protected)”：表示GTP、LLC、RLC被确认，数据被保护。<br>- “NACKGTP(Unack GTP Ack LLC/RLC Protected)”：表示GTP未被确认，LLC、RLC被确认，数据被保护。<br>- “NGTPLLC(Unack GTP/LLC Ack RLC Protected)”：表示GTP、LLC未被确认，RLC被确认，数据被保护。<br>- “NGTPLLCRLCP(Unack GTP/LLC/RLC Protected)”：表示GTP、LLC、RLC未被确认，数据被保护。<br>- “NGTPLLCRLCU(Unack GTP/LLC/RLC Unprotected)”：表示GTP、LLC、RLC未被确认，数据未被保护。<br>默认值：无<br>配置原则：建议值为<br>“NGTPLLC(Unack GTP/LLC Ack RLC Protected)”<br>。 |
| PRI2G | 2G QoS优先级 | 可选必选说明：可选参数<br>参数含义：该参数用于指定SGSN支持的缺省QoS优先级（Precedence Class），优先级定义了业务处理的相对顺序，例如，在异常情况（例如拥塞）下，低优先级的业务数据包将首先被丢弃。<br>数据来源：整网规划<br>前提条件：该参数在<br>“是否配置2G QoS”<br>配置为<br>“YES(是)”<br>时生效。<br>取值范围：<br>- “HPRI(High priority)”：表示高优先级。<br>- “NPRI(Normal priority)”：表示普通优先级。<br>- “LPRI(Low priority)”：表示低优先级。<br>默认值：无<br>配置原则：建议值为<br>“HPRI(High priority)” |
| DC2G | 2G QoS延迟等级 | 可选必选说明：可选参数<br>参数含义：该参数用于指定SGSN支持的缺省QoS延迟等级（QoS-Deley Class），延迟等级参数定义了在GPRS网络中传输数据时引入的平均延迟和95%延迟的最大值。<br>数据来源：整网规划<br>前提条件：该参数在<br>“是否配置2G QoS”<br>配置为<br>“YES(是)”<br>时生效。<br>取值范围：<br>- “DC1(Delay class 1)”<br>- “DC2(Delay class 2)”<br>- “DC3(Delay class 3)”<br>- “DC4(Best effort)”<br>默认值：无<br>配置原则：请参考<br>[表1](#ZH-CN_MMLREF_0000001126146230__tab1)<br>。 |
| PT2G | 2G QoS最大吞吐量（octet/s） | 可选必选说明：可选参数<br>参数含义：该参数用于指定SGSN支持的缺省QoS平均吞吐量（QoS-Mean Throughput）。<br>数据来源：整网规划<br>前提条件：该参数在<br>“是否配置2G QoS”<br>配置为<br>“YES(是)”<br>时生效。<br>取值范围：<br>- “PT1(Up to 1000)”<br>- “PT2(Up to 2000)”<br>- “PT3(Up to 4000)”<br>- “PT4(Up to 8000)”<br>- “PT5(Up to 16000)”<br>- “PT6(Up to 32000)”<br>- “PT7(Up to 64000)”<br>- “PT8(Up to 128000)”<br>- “PT9(Up to 256000)”<br>默认值：无<br>配置原则：PT1到PT9代表的吞吐量逐渐增大。 |
| MT2G | 2G QoS平均吞吐量（octet/h） | 可选必选说明：可选参数<br>参数含义：该参数用于指定SGSN支持的缺省QoS平均吞吐量（QoS-Mean Throughput）。<br>数据来源：整网规划<br>前提条件：该参数在<br>“是否配置2G QoS”<br>配置为<br>“YES(是)”<br>时生效。<br>取值范围：<br>- “MT1(100)”<br>- “MT2(200)”<br>- “MT3(500)”<br>- “MT4(1000)”<br>- “PT5(2000)”<br>- “MT6(5000)”<br>- “MT7(10000)”<br>- “MT8(20000)”<br>- “MT9(50000)”、<br>- “MT10(100 000)”<br>- “MT11(200 000)”<br>- “MT12(500 000)”<br>- “MT13(1000 000)”<br>- “MT14(2000 000)”<br>- “MT15(5000 000)”<br>- “MT16(10 000 000)”<br>- “MT17(20 000 000)”<br>- “MT18(50 000 000)”<br>- “MT31(Best effort)”<br>默认值：无<br>配置原则：MT1到MT18表示的平均吞吐量逐渐增大。 |
| TC2G | 2G QoS流量等级 | 可选必选说明：可选参数<br>参数含义：该参数用于指定SGSN支持的缺省QoS流量等级（QoS-Traffic Class）。<br>数据来源：整网规划<br>前提条件：该参数在<br>“是否配置2G QoS”<br>配置为<br>“YES(是)”<br>时生效。<br>取值范围：<br>- “CC(Conversational class)”：表示会话类。<br>- “SC(Streaming class)”：表示流类。<br>- “IC(Interactive class)”：表示交互类。<br>- “BC(Background class)”：表示背景类。<br>默认值：无 |
| MAXSDU2G | 2G QoS最大SDU长度 | 可选必选说明：可选参数<br>参数含义：该参数用于指定SGSN支持的缺省QoS最大SDU长度（QoS-Maximum SDU size）。<br>数据来源：整网规划<br>前提条件：该参数在<br>“是否配置2G QoS”<br>配置为<br>“YES(是)”<br>时生效。<br>取值范围：1～153<br>默认值：无<br>配置原则：<br>- 建议值为151。<br>- 1～150表示10～1500 octets。<br>- 151表示1502 octets。<br>- 152表示1510 octets。<br>- 153表示1520 octets。 |
| MBRUPLK2G | 2G QoS上行最大速率 | 可选必选说明：可选参数<br>参数含义：该参数用于指定SGSN支持的缺省QoS上行最大速率（QoS-Maximum bit rate for uplink）。<br>数据来源：整网规划<br>前提条件：该参数在<br>“是否配置2G QoS”<br>配置为<br>“YES(是)”<br>时生效。<br>取值范围：1～255<br>默认值：无<br>配置原则：<br>- 1～63表示1～63kbit/s，以1kbit/s递增。<br>- 64～127表示64～568kbit/s，以8kbit/s递增。<br>- 128～254表示576～8640kbit/s，以64kbit/s递增。<br>- 255表示0kbit/s。<br>- 建议值为254。 |
| GBRUPLK2G | 2G QoS上行保证速率 | 可选必选说明：可选参数<br>参数含义：该参数用于指定SGSN支持的缺省QoS上行保证速率（QoS-Guaranteed bit rate for uplink）。<br>数据来源：整网规划<br>前提条件：该参数在<br>“是否配置2G QoS”<br>配置为<br>“YES(是)”<br>时生效。<br>取值范围：1～255<br>默认值：无<br>配置原则：<br>- 1～63表示1～63kbit/s，以1kbit/s递增。<br>- 64～127表示64～568kbit/s，以8kbit/s递增。<br>- 128～254表示576～8640kbit/s，以64kbit/s递增。<br>- 255表示0kbit/s。<br>- 建议值为254。 |
| MBRDNLK2G | 2G QoS下行最大速率 | 可选必选说明：可选参数<br>参数含义：该参数用于指定SGSN支持的缺省QoS下行最大速率（QoS-Maximum bit rate for downlink）。<br>数据来源：整网规划<br>前提条件：该参数在<br>“是否配置2G QoS”<br>配置为<br>“YES(是)”<br>时生效。<br>取值范围：1～255<br>默认值：无<br>配置原则：<br>- 1～63表示1～63kbit/s，以1kbit/s递增。<br>- 64～127表示64～568kbit/s，以8kbit/s递增。<br>- 128～254表示576～8640kbit/s，以64kbit/s递增。<br>- 255表示0kbit/s。<br>- 建议值为254。 |
| GBRDNLK2G | 2G QoS下行保证速率 | 可选必选说明：可选参数<br>参数含义：该参数用于指定SGSN支持的缺省QoS下行保证速率（QoS-Guaranteed bit rate for downlink）。<br>数据来源：整网规划<br>前提条件：该参数在<br>“是否配置2G QoS”<br>配置为<br>“YES(是)”<br>时生效。<br>取值范围：1～255<br>默认值：无<br>配置原则：<br>- 1～63表示1～63kbit/s，以1kbit/s递增。<br>- 64～127表示64～568kbit/s，以8kbit/s递增。<br>- 128～254表示576～8640kbit/s，以64kbit/s递增。<br>- 255表示0kbit/s。<br>- 建议值为254。 |
| DO2G | 2G QoS发送次序 | 可选必选说明：可选参数<br>参数含义：该参数用于指定SGSN支持的缺省QoS发送次序（QoS-Delivery Order）。<br>数据来源：整网规划<br>前提条件：该参数在<br>“是否配置2G QoS”<br>配置为<br>“YES(是)”<br>时生效。<br>取值范围：<br>- “ORDER(With delivery order)”<br>- “NORDER(Without delivery order)”<br>默认值：无<br>配置原则：建议值为<br>“NORDER(Without delivery order)”<br>。 |
| DESDU2G | 2G QoS发送错误SDU | 可选必选说明：可选参数<br>参数含义：该参数用于指定SGSN支持的缺省QoS发送错误SDU（QoS-Delivery of erroneous SDU）。<br>数据来源：整网规划<br>前提条件：该参数在<br>“是否配置2G QoS”<br>配置为<br>“YES(是)”<br>时生效。<br>取值范围：<br>- “NODT(No detect)”<br>- “DELIVE(Erroneous SDUs are delivered)”<br>- “NDELIVE(Erroneous SDUs are not delivered)”<br>默认值：无<br>配置原则：建议值为<br>“NODT(No detect)”<br>。 |
| RBER2G | 2G QoS保留BER | 可选必选说明：可选参数<br>参数含义：该参数用于指定SGSN支持的缺省QoS保留BER （QoS-Residual Bit Error Ratio）。<br>数据来源：整网规划<br>前提条件：该参数在<br>“是否配置2G QoS”<br>配置为<br>“YES(是)”<br>时生效。<br>取值范围：<br>- “RBER1(5*10^-2)”<br>- “RBER2(1*10^-2)”<br>- “RBER3(5*10^-3)”<br>- “RBER4(4*10^-3)”<br>- “RBER5(1*10^-3)”<br>- “RBER6(1*10^-4)”<br>- “RBER7(1*10^-5)”<br>- “RBER8(1*10^-6)”<br>- “RBER9(6*10^-8)”<br>默认值：无<br>配置原则：建议值为<br>“RBER9(6*10^-8)”<br>。 |
| SDUER2G | 2G QoSSDU误码率 | 可选必选说明：可选参数<br>参数含义：该参数用于指定SGSN支持的缺省QoS SDU误码率（QoS-SDU error ratio）。<br>数据来源：整网规划<br>前提条件：该参数在<br>“是否配置2G QoS”<br>配置为<br>“YES(是)”<br>时生效。<br>取值范围：<br>- “SDUER1(1*10^-2)”<br>- “SDUER2(7*10^-3)”<br>- “SDUER3(1*10^-3)”<br>- “SDUER4(1*10^-4)”<br>- “SDUER5(1*10^-5)”<br>- “SDUER6(1*10^-6)”<br>- “SDUER7(1*10^-1)”<br>默认值：无<br>配置原则：建议值为<br>“SDUER4(1*10^-4)”<br>。 |
| THPRI2G | 2G QoS发送控制优先级 | 可选必选说明：可选参数<br>参数含义：该参数用于指定SGSN支持的缺省QoS发送控制优先级（QoS-Traffic Handling Priority）。<br>数据来源：整网规划<br>前提条件：该参数在<br>“是否配置2G QoS”<br>配置为<br>“YES(是)”<br>时生效。<br>取值范围：<br>- “THPRI1(Priority level 1)”<br>- “THPRI2(Priority level 2)”<br>- “THPRI3(Priority level 3)”<br>默认值：无<br>配置原则：建议值为<br>“THPRI1(Priority level 1)”<br>。 |
| TD2G | 2G QoS传递时延 | 可选必选说明：可选参数<br>参数含义：该参数用于指定SGSN支持的缺省QoS传递时延（QoS-Transfer Delay）。<br>数据来源：整网规划<br>前提条件：该参数在<br>“是否配置2G QoS”<br>配置为<br>“YES(是)”<br>时生效。<br>取值范围：1～62（数值型）<br>默认值：无<br>配置原则：<br>- 建议值为10。<br>- 1～15表示10～150ms，以10ms递增。<br>- 16～31表示200～950ms，以50ms递增。<br>- 32～62表示1000～4000ms，以100ms递增。<br>- 只在Traffic Class为实时类（Conversational，Streaming）时有效。 |
| ARPRI2G | 2G QoS分配保留优先级 | 可选必选说明：可选参数<br>参数含义：该参数用于指定SGSN支持的缺省分配保留优先级（QoS-Allocation/Retention Priority）。<br>数据来源：整网规划<br>前提条件：该参数在<br>“是否配置2G QoS”<br>配置为<br>“YES(是)”<br>时生效。<br>取值范围：<br>- “HIGHLEVELUSER(高端用户)”<br>- “NORMALUSER(普通用户)”<br>- “LOWLEVELUSER(低端用户)”<br>默认值：无<br>配置原则：建议为<br>“HIGHLEVELUSER(高端用户)”<br>。 |
| RADIOPRI2G | 2G QoS无线优先级 | 可选必选说明：可选参数<br>参数含义：该参数用于指定SGSN支持的缺省QoS无线优先级（QoS-Radio Priority）。<br>数据来源：整网规划<br>前提条件：该参数在<br>“是否配置2G QoS”<br>配置为<br>“YES(是)”<br>时生效。<br>取值范围：1～4<br>默认值：无<br>配置原则：<br>- 建议值为2。<br>- 1～4表示优先级从高到低。 |
| QOS3G | 是否配置3G QoS | 可选必选说明：可选参数<br>参数含义：该参数用于指定是否配置3G QoS。<br>数据来源：整网规划<br>取值范围：<br>- “NO(否)”<br>- “YES(是)”<br>默认值：无<br>配置原则：<br>- 当该IMSI号段用户使用UMTS接入网接入并进行PDP激活，且系统使用该表中配置的3G QoS参数对PDP上下文使用的QoS进行限制时，选择“YES(是)”。<br>- 当该IMSI号段用户使用UMTS接入网接入并进行PDP激活，且系统使用3G QoS的默认参数对PDP上下文使用的QoS进行限制时，选择“NO(否)”。<br>- 用户范围为“ALL_USER（所有用户）”时，该表中的3G QoS参数不能配置为“NO(否)”。 |
| RC3G | 3G QoS可靠性 | 可选必选说明：可选参数<br>参数含义：该参数用于指定SGSN支持的缺省QoS可靠性等级（Reliability Class），可靠性指示了一个应用对传输特性的要求。<br>数据来源：整网规划<br>前提条件：该参数在<br>“是否配置3G QoS”<br>配置为<br>“YES(是)”<br>时生效。<br>取值范围：<br>- “ACKGTP(Ack GTP/LLC/RLC Protected)”：表示GTP、LLC、RLC被确认，数据被保护。<br>- “NACKGTP(Unack GTP Ack LLC/RLC Protected)”：表示GTP未被确认，LLC、RLC被确认，数据被保护。<br>- “NGTPLLC(Unack GTP/LLC Ack RLC Protected)”：表示GTP、LLC未被确认，RLC被确认，数据被保护。<br>- “NGTPLLCRLCP(Unack GTP/LLC/RLC Protected)”：表示GTP、LLC、RLC未被确认，数据被保护。<br>- “NGTPLLCRLCU(Unack GTP/LLC/RLC Unprotected)”：表示GTP、LLC、RLC未被确认，数据未被保护。<br>默认值：无<br>配置原则：建议值为<br>“NGTPLLC(Unack GTP/LLC Ack RLC Protected)”<br>。 |
| PRI3G | 3G QoS优先级 | 可选必选说明：可选参数<br>参数含义：该参数用于指定SGSN支持的缺省QoS优先级（Precedence Class），优先级定义了业务处理的相对顺序，例如，在异常情况（例如拥塞）下，低优先级的业务数据包将首先被丢弃。<br>数据来源：整网规划<br>前提条件：该参数在<br>“是否配置3G QoS”<br>配置为<br>“YES(是)”<br>时生效。<br>取值范围：<br>- “HPRI(High priority)”：表示高优先级。<br>- “NPRI(Normal priority)”：表示普通优先级。<br>- “LPRI(Low priority)”：表示低优先级。<br>默认值：无<br>配置原则：建议值为<br>“HPRI(High priority)” |
| DC3G | 3G QoS延迟等级 | 可选必选说明：可选参数<br>参数含义：该参数用于指定SGSN支持的缺省QoS延迟等级（QoS-Deley Class），延迟等级参数定义了在GPRS网络中传输数据时引入的平均延迟和95%延迟的最大值。<br>数据来源：整网规划<br>前提条件：该参数在<br>“是否配置3G QoS”<br>配置为<br>“YES(是)”<br>时生效。<br>取值范围：<br>- “DC1(Delay class 1)”<br>- “DC2(Delay class 2)”<br>- “DC3(Delay class 3)”<br>- “DC4(Best effort)”<br>默认值：无<br>配置原则：请参考<br>[表1](#ZH-CN_MMLREF_0000001126146230__tab1)<br>。 |
| PT3G | 3G QoS最大吞吐量（octet/s） | 可选必选说明：可选参数<br>参数含义：该参数用于指定SGSN支持的缺省QoS最大吞吐量（QoS-Peak Throughput）。<br>数据来源：整网规划<br>前提条件：该参数在<br>“是否配置3G QoS”<br>配置为<br>“YES(是)”<br>时生效。<br>取值范围：<br>- “PT1(Up to 1000)”<br>- “PT2(Up to 2000)”<br>- “PT3(Up to 4000)”<br>- “PT4(Up to 8000)”<br>- “PT5(Up to 16000)”<br>- “PT6(Up to 32000)”<br>- “PT7(Up to 64000)”<br>- “PT8(Up to 128000)”<br>- “PT9(Up to 256000)”<br>默认值：无<br>配置原则：PT1到PT9表示吞吐量从小到大，需要根据实际需求进行选择配置。 |
| MT3G | 3G QoS平均吞吐量（octet/h） | 可选必选说明：可选参数<br>参数含义：该参数用于指定SGSN支持的缺省QoS平均吞吐量（QoS-Mean Throughput）。<br>数据来源：整网规划<br>前提条件：该参数在<br>“是否配置3G QoS”<br>配置为<br>“YES(是)”<br>时生效。<br>取值范围：<br>- “MT1(100)”<br>- “MT2(200)”<br>- “MT3(500)”<br>- “MT4(1000)”<br>- “MT5(2000)”<br>- “MT6(5000)”<br>- “MT7(10000)”<br>- “MT8(20000)”<br>- “MT9(50000)”<br>- “MT10(100 000)”<br>- “MT11(200 000)”<br>- “MT12(500 000)”<br>- “MT13(1000 000)”<br>- “MT14(2000 000)”<br>- “MT15(5000 000)”<br>- “MT16(10 000 000)”<br>- “MT17(20 000 000)”<br>- “MT18(50 000 000)”<br>- “MT31(Best effort)”<br>默认值：无<br>配置原则：建议值<br>“MT18(50 000 000)”<br>。 |
| TC3G | 3G QoS流量等级 | 可选必选说明：可选参数<br>参数含义：该参数用于指定SGSN支持的缺省QoS流量等级（QoS-Traffic Class）。<br>数据来源：整网规划<br>前提条件：该参数在<br>“是否配置3G QoS”<br>配置为<br>“YES(是)”<br>时生效。<br>取值范围：<br>- “CC(Conversational class)”：表示会话类。<br>- “SC(Streaming class)”：表示流类。<br>- “IC(Interactive class)”：表示交互类。<br>- “BC(Background class)”：表示背景类。<br>默认值：无 |
| MAXSDU3G | 3G QoS最大SDU长度 | 可选必选说明：可选参数<br>参数含义：该参数用于指定SGSN支持的缺省QoS最大SDU长度（QoS-Maximum SDU size）。<br>数据来源：整网规划<br>前提条件：该参数在<br>“是否配置3G QoS”<br>配置为<br>“YES(是)”<br>时生效。<br>取值范围：1～153<br>默认值：无<br>配置原则：<br>- 建议值151。<br>- 1～150表示10～1500 octets。<br>- 151表示1502 octets。<br>- 152表示1510 octets。<br>- 153表示1520 octets。 |
| MBRUPLK3G | 3G QoS上行最大速率 | 可选必选说明：可选参数<br>参数含义：该参数用于指定SGSN支持的缺省QoS上行最大速率（QoS-Maximum bit rate for uplink）。<br>数据来源：整网规划<br>前提条件：该参数在<br>“是否配置3G QoS”<br>配置为<br>“YES(是)”<br>时生效。<br>取值范围：1～255<br>默认值：无<br>配置原则：<br>- 1～63表示1～63kbit/s，以1kbit/s递增。<br>- 64～127表示64～568kbit/s，以8kbit/s递增。<br>- 128～254表示576～8640kbit/s，以64kbit/s递增。<br>- 255表示0kbit/s。<br>- 建议值为254。 |
| GBRUPLK3G | 3G QoS上行保证速率 | 可选必选说明：可选参数<br>参数含义：该参数用于指定SGSN支持的缺省QoS上行保证速率（QoS-Guaranteed bit rate for uplink）。<br>数据来源：整网规划<br>前提条件：该参数在<br>“是否配置3G QoS”<br>配置为<br>“YES(是)”<br>时生效。<br>取值范围：1～255<br>默认值：无<br>配置原则：<br>- 1～63表示1～63kbit/s，以1kbit/s递增。<br>- 64～127表示64～568kbit/s，以8kbit/s递增。<br>- 128～254表示576～8640kbit/s，以64kbit/s递增。<br>- 255表示0kbit/s。<br>- 建议值为254。 |
| MBRDNLK3G | 3G QoS下行最大速率 | 可选必选说明：可选参数<br>参数含义：该参数用于指定SGSN支持的缺省QoS下行最大速率（QoS-Maximum bit rate for downlink）。<br>数据来源：整网规划<br>取值范围：1～255<br>前提条件：该参数在<br>“是否配置3G QoS”<br>配置为<br>“YES(是)”<br>时生效。<br>默认值：无<br>配置原则：<br>- 1～63表示1～63kbit/s，以1kbit/s递增。<br>- 64～127表示64～568kbit/s，以8kbit/s递增。<br>- 128～254表示576～8640kbit/s，以64kbit/s递增。<br>- 255表示0kbit/s。<br>- 建议值为254。 |
| GBRDNLK3G | 3G QoS下行保证速率 | 可选必选说明：可选参数<br>参数含义：该参数用于指定SGSN支持的缺省QoS下行保证速率（QoS-Guaranteed bit rate for downlink）。<br>数据来源：整网规划<br>前提条件：该参数在<br>“是否配置3G QoS”<br>配置为<br>“YES(是)”<br>时生效。<br>取值范围：1～255<br>默认值：无<br>配置原则：<br>- 1～63表示1～63kbit/s，以1kbit/s递增。<br>- 64～127表示64～568kbit/s，以8kbit/s递增。<br>- 128～254表示576～8640kbit/s，以64kbit/s递增。<br>- 255表示0kbit/s。<br>- 建议值为254。 |
| DO3G | 3G QoS发送次序 | 可选必选说明：可选参数<br>参数含义：该参数用于指定SGSN支持的缺省QoS发送次序（QoS-Delivery Order）。<br>数据来源：整网规划<br>前提条件：该参数在<br>“是否配置3G QoS”<br>配置为<br>“YES(是)”<br>时生效。<br>取值范围：<br>- “ORDER(With delivery order)”<br>- “NORDER(Without delivery order)”<br>默认值：无<br>配置原则：建议值为<br>“NORDER(Without delivery order)”<br>。 |
| DESDU3G | 3G QoS发送错误SDU | 可选必选说明：可选参数<br>参数含义：该参数用于指定SGSN支持的缺省QoS发送错误SDU（QoS-Delivery of erroneous SDU）。<br>数据来源：整网规划<br>前提条件：该参数在<br>“是否配置3G QoS”<br>配置为<br>“YES(是)”<br>时生效。<br>取值范围：<br>- “NODT(No detect)”<br>- “DELIVE(Erroneous SDUs are delivered)”<br>- “NDELIVE(Erroneous SDUs are not delivered)”<br>默认值：无<br>配置原则：建议值为<br>“NODT(No detect)”<br>。 |
| RBER3G | 3G QoS保留BER | 可选必选说明：可选参数<br>参数含义：该参数用于指定SGSN支持的缺省QoS保留BER （QoS-Residual Bit Error Ratio）。<br>数据来源：整网规划<br>前提条件：该参数在<br>“是否配置3G QoS”<br>配置为<br>“YES(是)”<br>时生效。<br>取值范围：<br>- “RBER1(5*10^-2)”<br>- “RBER2(1*10^-2)”<br>- “RBER3(5*10^-3)”<br>- “RBER4(4*10^-3)”<br>- “RBER5(1*10^-3)”<br>- “RBER6(1*10^-4)”<br>- “RBER7(1*10^-5)”<br>- “RBER8(1*10^-6)”<br>- “RBER9(6*10^-8)”<br>默认值：无<br>配置原则：建议值为<br>“RBER9(6*10^-8)”<br>。 |
| SDUER3G | 3G QoSSDU误码率 | 可选必选说明：可选参数<br>参数含义：该参数用于指定SGSN支持的缺省QoS SDU误码率（QoS-SDU error ratio）。<br>数据来源：整网规划<br>前提条件：该参数在<br>“是否配置3G QoS”<br>配置为<br>“YES(是)”<br>时生效。<br>取值范围：<br>- “SDUER1(1*10^-2)”<br>- “SDUER2(7*10^-3)”<br>- “SDUER3(1*10^-3)”<br>- “SDUER4(1*10^-4)”<br>- “SDUER5(1*10^-5)”<br>- “SDUER6(1*10^-6)”<br>- “SDUER7(1*10^-1)”<br>默认值：无<br>配置原则：建议值为<br>“SDUER4(1*10^-4)”<br>。 |
| THPRI3G | 3G QoS发送控制优先级 | 可选必选说明：可选参数<br>参数含义：该参数用于指定SGSN支持的缺省QoS发送控制优先级（QoS-Traffic Handling Priority）。<br>数据来源：整网规划<br>前提条件：该参数在<br>“是否配置3G QoS”<br>配置为<br>“YES(是)”<br>时生效。<br>取值范围：<br>- “THPRI1(Priority level 1)”<br>- “THPRI2(Priority level 2)”<br>- “THPRI3(Priority level 3)”<br>默认值：无<br>配置原则：建议值为<br>“THPRI1(Priority level 1)”<br>。 |
| TD3G | 3G QoS传递时延 | 可选必选说明：可选参数<br>参数含义：该参数用于指定SGSN支持的缺省QoS传递时延（QoS-Transfer Delay）。<br>数据来源：整网规划<br>前提条件：该参数在<br>“是否配置3G QoS”<br>配置为<br>“YES(是)”<br>时生效。<br>取值范围：1～62（数值型）<br>默认值：无<br>配置原则：<br>- 建议值为10。<br>- 1～15表示10～150ms，以10ms递增。<br>- 16～31表示200～950ms，以50ms递增。<br>- 32～62表示1000～4000ms，以100ms递增。<br>- 只在Traffic Class为实时类（Conversational，Streaming）时有效。 |
| MBRDNLKEX3G | 3G QoS扩展下行最大速率 | 可选必选说明：可选参数<br>参数含义：该参数用于指定SGSN支持的扩展下行最大速率（QoS-Extended Maximum bit rate for downlink）。<br>数据来源：整网规划<br>前提条件：该参数在<br>“是否配置3G QoS”<br>配置为<br>“YES(是)”<br>时生效。<br>取值范围：0～250<br>默认值：无<br>配置原则：<br>- 0～74，8600～16000kbit/s，以100kbit/s递增。<br>- 75～186，17000～128000kbit/s，以1000kbit/s递增。<br>- 187～250，130000～256000kbit/s，以2000kbit/s递增。<br>- 当本参数的取值为0时，上行最大速率的限制取决于“上行最大速率”参数的取值。<br>- 当本参数的取值不为0时，上行最大速率的限制取决于本参数的取值，“上行最大速率”参数的取值被忽略。 |
| GBRDNLKEX3G | 3G QoS扩展下行保证速率 | 可选必选说明：可选参数<br>参数含义：该参数用于指定SGSN支持的扩展下行保证速率（QoS-Extended Guaranteed bit rate for downlink）。<br>数据来源：整网规划<br>前提条件：该参数在<br>“是否配置3G QoS”<br>配置为<br>“YES(是)”<br>时生效。<br>取值范围：0～250<br>默认值：无<br>配置原则：<br>- 0～74，8600～16000kbit/s，以100kbit/s递增。<br>- 75～186，17000～128000kbit/s，以1000kbit/s递增。<br>- 187～250，130000～256000kbit/s，以2000kbit/s递增。<br>- 当本参数的取值为0时，下行保证速率的限制取决于“下行保证速率”参数的取值。<br>- 当本参数的取值不为0时，下行保证速率的限制取决于本参数的取值，“下行保证速率”参数的取值被忽略。 |
| MBRUPLKEX3G | 3G QoS扩展上行最大速率 | 可选必选说明：可选参数<br>参数含义：该参数用于指定SGSN支持的扩展上行最大速率（QoS-Extended Maximum bit rate for uplink）。<br>数据来源：整网规划<br>前提条件：该参数在<br>“是否配置3G QoS”<br>配置为<br>“YES(是)”<br>时生效。<br>取值范围：0～250<br>默认值：无<br>配置原则：<br>- 建议值为0<br>- 0～74，8600～16000kbit/s，以100kbit/s递增。<br>- 75～186，17000～128000kbit/s，以1000kbit/s递增。<br>- 187～250，130000～256000kbit/s，以2000kbit/s递增。<br>- 当本参数的取值为0时，上行最大速率的限制取决于“上行最大速率”参数的取值。<br>- 当本参数的取值不为0时，上行最大速率的限制取决于本参数的取值，“上行最大速率”参数的取值被忽略。 |
| GBRUPLKEX3G | 3G QoS扩展上行保证速率 | 可选必选说明：可选参数<br>参数含义：该参数用于指定SGSN支持的扩展上行保证速率（QoS-Extended Guaranteed bit rate for uplink）。<br>数据来源：整网规划<br>前提条件：该参数在<br>“是否配置3G QoS”<br>配置为<br>“YES(是)”<br>时生效。<br>取值范围：0～250<br>默认值：无<br>配置原则：<br>- 建议值为0。<br>- 0～74，8600～16000kbit/s，以100kbit/s递增。<br>- 75～186，17000～128000kbit/s，以1000kbit/s递增。<br>- 187～250，130000～256000kbit/s，以2000kbit/s递增。<br>- 当本参数的取值为0时，上行保证速率的限制取决于“上行最大速率”参数的取值。<br>- 当本参数的取值不为0时，上行保证速率的限制取决于本参数的取值，“上行保证速率”参数的取值被忽略。 |
| ARPRI3G | 3G QoS分配保留优先级 | 可选必选说明：可选参数<br>参数含义：该参数用于指定SGSN支持的缺省分配保留优先级（QoS-Allocation/Retention Priority）。<br>数据来源：整网规划<br>前提条件：该参数在<br>“是否配置3G QoS”<br>配置为<br>“YES(是)”<br>时生效。<br>取值范围：<br>- “HIGHLEVELUSER(高端用户)”<br>- “NORMALUSER(普通用户)”<br>- “LOWLEVELUSER(低端用户)”<br>默认值：无<br>配置原则：建议为<br>“HIGHLEVELUSER(高端用户)”<br>。 |
| RADIOPRI3G | 3G QoS无线优先级 | 可选必选说明：可选参数<br>参数含义：该参数用于指定SGSN支持的缺省QoS无线优先级（QoS-Radio Priority）。<br>数据来源：整网规划<br>前提条件：该参数在<br>“是否配置3G QoS”<br>配置为<br>“YES(是)”<br>时生效。<br>取值范围：1～4<br>默认值：无<br>配置原则：<br>- 建议值为2。<br>- 1～4表示优先级从高到低。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/IMSISMCHAR]] · QoS协商参数（IMSISMCHAR）

## 使用实例

修改一条SM属性配置记录，用户范围为IMSI_PREFIX，IMSI前缀为123456，APN网络标识为00001，UE接入能力为ALL_UE，协商方式为NET_CTRL_QOS，覆盖签约QoS为YES，是否配置2G QoS为YES，是否配置3G QoS为NO：

MOD IMSISMCHAR: SUBRANGE=IMSI_PREFIX, IMSIPRE="123456", APNNI="00001", UEACCCAP=ALL_UE, NTYPE=NET_CTRL_QOS, SUBQOS=YES, QOS2G=YES, QOS3G=NO;

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改QoS协商参数(MOD-IMSISMCHAR)_26146230.md`
