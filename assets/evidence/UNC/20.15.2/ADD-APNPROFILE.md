# 增加APN配置（ADD APNPROFILE）

- [命令功能](#ZH-CN_MMLREF_0000001467235537__1.3.1.1)
- [注意事项](#ZH-CN_MMLREF_0000001467235537__1.3.2.1)
- [本地用户权限](#ZH-CN_MMLREF_0000001467235537__1.3.3.1)
- [网管用户权限](#ZH-CN_MMLREF_0000001467235537__1.3.4.1)
- [参数说明](#ZH-CN_MMLREF_0000001467235537__1.3.5.1)
- [使用实例](#ZH-CN_MMLREF_0000001467235537__1.3.6.1)

#### [命令功能](#ZH-CN_MMLREF_0000001467235537)

**适用网元：SGSN**

该命令用于新增APN的APN的概要信息，如QOS，计费属性等。

当用户使用GPRS/UMTS接入网接入并进行PDP激活时，如果使用 [ADD SMACTCTRL](../激活过程管理/增加激活过程控制参数（ADD SMACTCTRL）_26305472.md) 命令纠正用户激活的APNNI为回落APNNI时，如果回落APNNI未签约，使用本配置指定该APN的概要信息。

#### [注意事项](#ZH-CN_MMLREF_0000001467235537)

该命令执行后立即生效。

该表最多可以输入32条记录。

#### [本地用户权限](#ZH-CN_MMLREF_0000001467235537)

manage-ug；system-ug

#### [网管用户权限](#ZH-CN_MMLREF_0000001467235537)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_MMLREF_0000001467235537)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APNNI | APN网络标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定APN网络标识。<br>数据来源：整网规划<br>取值范围：1~62位字符串<br>默认值： 无<br>配置原则：<br>- APN网络标识地址由一个或多个LABEL构成，各LABEL间用“.”间隔。<br>- 每个LABEL的构成字符只能是字母A～Z或a～z、数字0～9和中划线“-”。<br>- APN网络标识地址不能以“rac”、“lac”、“sgsn”或“rnc”开头，不能以“.gprs”结尾。说明：- APN网络标识不区分大小写。<br>- APNNI在APN中所处的位置，例如：example1.com.mnc123.mcc123.gprs，其中NI= example1.com， OI= mnc123.mcc123.gprs。 |
| RC | QoS可靠性 | 可选必选说明：可选参数<br>参数含义：该参数用于指定该APNNI的缺省QoS可靠性等级（Reliability Class），可靠性指示了一个应用对传输特性的要求。<br>数据来源：整网规划<br>取值范围：<br>- “ACKGTP(Ack GTP/LLC/RLC Protected)”：表示GTP、LLC、RLC被确认，数据被保护。<br>- “NACKGTP(Unack GTP Ack LLC/RLC Protected)”：表示GTP未被确认，LLC、RLC被确认，数据被保护。<br>- “NGTPLLC(Unack GTP/LLC Ack RLC Protected)”：表示GTP、LLC未被确认，RLC被确认，数据被保护。<br>- “NGTPLLCRLCP(Unack GTP/LLC/RLC Protected)”：表示GTP、LLC、RLC未被确认，数据被保护。<br>- “NGTPLLCRLCU(Unack GTP/LLC/RLC Unprotected)”：表示GTP、LLC、RLC未被确认，数据未被保护。<br>默认值：<br>“NGTPLLC(Unack GTP/LLC Ack RLC Protected)”<br>配置原则：建议值为<br>“NGTPLLC(Unack GTP/LLC Ack RLC Protected)”<br>。 |
| PRI | QoS优先级 | 可选必选说明：可选参数<br>参数含义：该参数用于指定该APNNI的缺省QoS优先级（Precedence Class），优先级定义了业务处理的相对顺序，例如，在异常情况（例如拥塞）下，低优先级的业务数据包将首先被丢弃。<br>数据来源：整网规划<br>取值范围：<br>- “HPRI(High priority)”：表示高优先级。<br>- “NPRI(Normal priority)”：表示普通优先级。<br>- “LPRI(Low priority)”：表示低优先级。<br>默认值：<br>“HPRI(High priority)”<br>配置原则：建议值为<br>“HPRI(High priority)” |
| DC | QoS延迟等级 | 可选必选说明：可选参数<br>参数含义：该参数用于指定该APNNI的缺省QoS延迟等级（QoS-Deley Class），延迟等级参数定义了在GPRS网络中传输数据时引入的平均延迟和95%延迟的最大值。<br>数据来源：整网规划<br>取值范围：<br>- “DC1(Delay class 1)”<br>- “DC2(Delay class 2)”<br>- “DC3(Delay class 3)”<br>- “DC4(Best effort)”<br>默认值：<br>“DC1(Delay class 1)”<br>配置原则：无 |
| PT | QoS最大吞吐量（octet/s） | 可选必选说明：可选参数<br>参数含义：该参数用于指定该APNNI的缺省QoS最大吞吐量（QoS-Peak Throughput）。<br>数据来源：整网规划<br>取值范围：<br>- “PT1(Up to 1000)”<br>- “PT2(Up to 2000)”<br>- “PT3(Up to 4000)”<br>- “PT4(Up to 8000)”<br>- “PT5(Up to 16000)”<br>- “PT6(Up to 32000)”<br>- “PT7(Up to 64000)”<br>- “PT8(Up to 128000)”<br>- “PT9(Up to 256000)”<br>默认值：<br>“PT9(Up to 256000)”<br>配置原则：PT1到PT9代表的吞吐量逐渐增大。 |
| MT | QoS平均吞吐量（octet/h） | 可选必选说明：可选参数<br>参数含义：该参数用于指定该APNNI的缺省QoS平均吞吐量（QoS-Mean Throughput）。<br>数据来源：整网规划<br>取值范围：<br>- “MT1(100)”<br>- “MT2(200)”<br>- “MT3(500)”<br>- “MT4(1000)”<br>- “PT5(2000)”<br>- “MT6(5000)”<br>- “MT7(10000)”<br>- “MT8(20000)”<br>- “MT9(50000)”<br>- “MT10(100 000)”<br>- “MT11(200 000)”<br>- “MT12(500 000)”<br>- “MT13(1000 000)”<br>- “MT14(2000 000)”<br>- “MT15(5000 000)”<br>- “MT16(10 000 000)”<br>- “MT17(20 000 000)”<br>- “MT18(50 000 000)”<br>- “MT31(Best effort)”<br>默认值：<br>“MT18(50 000 000)”<br>配置原则：MT1到MT18表示的平均吞吐量逐渐增大。 |
| TC | QoS流量等级 | 可选必选说明：可选参数<br>参数含义：该参数用于指定该APNNI的缺省QoS流量等级（QoS-Traffic Class）。<br>数据来源：整网规划<br>取值范围：<br>- “CC(Conversational class)”：表示会话类。<br>- “SC(Streaming class)”：表示流类。<br>- “IC(Interactive class)”：表示交互类。<br>- “BC(Background class)”：表示背景类。<br>默认值：<br>“CC(Conversational class)” |
| MAXSDU | QoS最大SDU长度 | 可选必选说明：可选参数<br>参数含义：该参数用于指定该APNNI的缺省QoS最大SDU长度（QoS-Maximum SDU size）。<br>数据来源：整网规划<br>取值范围：1～153<br>默认值：151<br>配置原则：<br>- 建议值为151。<br>- 1～150表示10～1500 octets。<br>- 151表示1502 octets。<br>- 152表示1510 octets。<br>- 153表示1520 octets。 |
| MBRUPLK | QoS上行最大速率 | 可选必选说明：可选参数<br>参数含义：该参数用于指定该APNNI的缺省QoS上行最大速率（QoS-Maximum bit rate for uplink）。<br>数据来源：整网规划<br>取值范围：1～255<br>默认值：254<br>配置原则：<br>- 1～63表示1～63kbit/s，以1kbit/s递增。<br>- 64～127表示64～568kbit/s，以8kbit/s递增。<br>- 128～254表示576～8640kbit/s，以64kbit/s递增。<br>- 255表示0kbit/s。<br>- 建议值为254。 |
| GBRUPLK | QoS上行保证速率 | 可选必选说明：可选参数<br>参数含义：该参数用于指定该APNNI的缺省QoS上行保证速率（QoS-Guaranteed bit rate for uplink）。<br>数据来源：整网规划<br>取值范围：1～255<br>默认值：254<br>配置原则：<br>- 1～63表示1～63kbit/s，以1kbit/s递增。<br>- 64～127表示64～568kbit/s，以8kbit/s递增。<br>- 128～254表示576～8640kbit/s，以64kbit/s递增。<br>- 255表示0kbit/s。<br>- 建议值为254。 |
| MBRDNLK | QoS下行最大速率 | 可选必选说明：可选参数<br>参数含义：该参数用于指定该APNNI的缺省QoS下行最大速率（QoS-Maximum bit rate for downlink）。<br>数据来源：整网规划<br>取值范围：1～255<br>默认值：254<br>配置原则：<br>- 1～63表示1～63kbit/s，以1kbit/s递增。<br>- 64～127表示64～568kbit/s，以8kbit/s递增。<br>- 128～254表示576～8640kbit/s，以64kbit/s递增。<br>- 255表示0kbit/s。<br>- 建议值为254。 |
| GBRDNLK | QoS下行保证速率 | 可选必选说明：可选参数<br>参数含义：该参数用于指定该APNNI的缺省QoS下行保证速率（QoS-Guaranteed bit rate for downlink）。<br>数据来源：整网规划。<br>取值范围：1～255<br>默认值：254<br>配置原则：<br>- 1～63表示1～63kbit/s，以1kbit/s递增。<br>- 64～127表示64～568kbit/s，以8kbit/s递增。<br>- 128～254表示576～8640kbit/s，以64kbit/s递增。<br>- 255表示0kbit/s。<br>- 建议值为254。 |
| DO | QoS发送次序 | 可选必选说明：可选参数<br>参数含义：该参数用于指定该APNNI的缺省QoS发送次序（QoS-Delivery Order）。<br>数据来源：整网规划<br>取值范围：<br>- “ORDER(With delivery order)”<br>- “NORDER(Without delivery order)”<br>默认值：<br>“NORDER(Without delivery order)”<br>配置原则：建议值为<br>“NORDER(Without delivery order)”<br>。 |
| DESDU | QoS发送错误SDU | 可选必选说明：可选参数<br>参数含义：该参数用于指定该APNNI的缺省QoS发送错误SDU（QoS-Delivery of erroneous SDU）。<br>数据来源：整网规划<br>取值范围：<br>- “NODT(No detect)”<br>- “DELIVE(Erroneous SDUs are delivered)”<br>- “NDELIVE(Erroneous SDUs are not delivered)”<br>默认值：<br>“NODT(No detect)”<br>配置原则：建议值为<br>“NODT(No detect)”<br>。 |
| RBER | QoS保留BER | 可选必选说明：可选参数<br>参数含义：该参数用于指定该APNNI的缺省QoS保留BER （QoS-Residual Bit Error Ratio）。<br>数据来源：整网规划<br>取值范围：<br>- “RBER1(5*10^-2)”<br>- “RBER2(1*10^-2)”<br>- “RBER3(5*10^-3)”<br>- “RBER4(4*10^-3)”<br>- “RBER5(1*10^-3)”<br>- “RBER6(1*10^-4)”<br>- “RBER7(1*10^-5)”<br>- “RBER8(1*10^-6)”<br>- “RBER9(6*10^-8)”<br>默认值：<br>“RBER9(6*10^-8)”<br>配置原则：建议值为<br>“RBER9(6*10^-8)”<br>。 |
| SDUER | QoSSDU误码率 | 可选必选说明：可选参数<br>参数含义：该参数用于指定该APNNI的缺省QoS SDU误码率（QoS-SDU error ratio）。<br>数据来源：整网规划<br>取值范围：<br>- “SDUER1(1*10^-2)”<br>- “SDUER2(7*10^-3)”<br>- “SDUER3(1*10^-3)”<br>- “SDUER4(1*10^-4)”<br>- “SDUER5(1*10^-5)”<br>- “SDUER6(1*10^-6)”<br>- “SDUER7(1*10^-1)”<br>默认值：<br>“SDUER4(1*10^-4)”<br>配置原则：建议值为<br>“SDUER4(1*10^-4)”<br>。 |
| THPRI | QoS发送控制优先级 | 可选必选说明：可选参数<br>参数含义：该参数用于指定该APNNI的缺省QoS发送控制优先级（QoS-Traffic Handling Priority）。<br>数据来源：整网规划<br>取值范围：<br>- “THPRI1(Priority level 1)”<br>- “THPRI2(Priority level 2)”<br>- “THPRI3(Priority level 3)”<br>默认值：<br>“THPRI1(Priority level 1)”<br>配置原则：建议值为<br>“THPRI1(Priority level 1)”<br>。 |
| TD | QoS传递时延 | 可选必选说明：可选参数<br>参数含义：该参数用于指定该APNNI的缺省QoS传递时延（QoS-Transfer Delay）。<br>数据来源：整网规划<br>取值范围：1～62（数值型）<br>默认值：10<br>配置原则：<br>- 建议值为10。<br>- 1～15表示10～150ms，以10ms递增。<br>- 16～31表示200～950ms，以50ms递增。<br>- 32～62表示1000～4000ms，以100ms递增。<br>- 只在Traffic Class为实时类（Conversational，Streaming）时有效。 |
| ARPRI | QoS分配保留优先级 | 可选必选说明：可选参数<br>参数含义：该参数用于指定该APNNI的缺省分配保留优先级（QoS-Allocation/Retention Priority）。<br>数据来源：整网规划<br>取值范围：<br>- “HIGHLEVELUSER(高端用户)”<br>- “NORMALUSER(普通用户)”<br>- “LOWLEVELUSER(低端用户)”<br>默认值：<br>“HIGHLEVELUSER(高端用户)”<br>配置原则：建议值为<br>“HIGHLEVELUSER(高端用户)”<br>。 |
| CC | 计费属性 | 可选必选说明：可选参数<br>参数含义：该参数用于指定该APN的计费属性。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为0000~FFFF<br>默认值：无<br>配置原则：无 |

#### [使用实例](#ZH-CN_MMLREF_0000001467235537)

新增一条APNNI的概要配置，APNNI为INTERNET，QoS优先级为高优先级，QoS延迟等级为DC1，可以用如下命令：

```
ADD APNPROFILE: APNNI="INTERNET", PRI=HPRI, DC=DC1;
```
