# 离线计费话单（GGSN/SGW-C/PGW-C）

- [话单描述](#ZH-CN_TOPIC_0292172742__1.3.1.1)
- [话单类型和话单版本](#ZH-CN_TOPIC_0292172742__1.3.2.1)
- [话单容器](#ZH-CN_TOPIC_0292172742__1.3.3.1)
- [话单的生成和传输](#ZH-CN_TOPIC_0292172742__1.3.4.1)
- [话单可靠性](#ZH-CN_TOPIC_0292172742__1.3.5.1)

#### [话单描述](#ZH-CN_TOPIC_0292172742)

话单涉及 [图1](#ZH-CN_TOPIC_0292172742__fig11791513113110) 所示的内容，本章节分别进行详细描述。

**图1** 话单描述

<br>

![](离线计费话单（GGSN_SGW-C_PGW-C）_92172742.assets/zh-cn_image_0292358299_2.png)

#### [话单类型和话单版本](#ZH-CN_TOPIC_0292172742)

GGSN/SGW-C/PGW-C与CG可以产生 [表1](#ZH-CN_TOPIC_0292172742__table_03C48215) 所示的多种类型的话单（通过 **ADD OFCTEMPLATE** 配置）。

*表1 话单类型、话单版本及其描述*

| 话单类型 | 话单版本 | 话单描述 |
| --- | --- | --- |
| G-CDR（GGSN-Charging Data Record） | R98、R99、R4、R5、R6、R7 | 用于GPRS/UMTS用户计费。<br>G-CDR是3GPP协议早期定义的话单格式，其内容主要包括用户基础信息（IMSI、MSISDN、IP地址）和PDP级的业务使用信息（流量、持续时间），不支持内容计费。 |
| eG-CDR（enhanced GGSN Charging Data Record） | R6、R7 | 用于GPRS/UMTS用户计费。eG-CDR话单在G-CDR话单的基础上增加了内容计费字段。<br>eG-CDR话单在G-CDR话单的基础上增加了部分内容计费字段，可以在同一张话单中同时记录多个业务的使用信息。 |
| SGW-CDR | R8、R9、R10 | 用于LTE用户计费，UNC作为SGW-C网元形态时产生。<br>SGW-CDR中大部分内容和G-CDR类似，同时还包括EPC网络独有的信息。SGW-CDR记录用户级计费信息，不支持内容计费。UNC作为SGW-C网元形态时，可以配置产生SGW-CDR。 |
| PGW-CDR | R8、R9、R10 | 用于LTE、EPC融合用户计费，UNC作为PGW-C网元形态时产生。<br>PGW-CDR中大部分内容和eG-CDR类似，支持内容计费，同时还包括EPC网络独有的信息。UNC作为P-GW或融合网关时，可以为EPC用户、GU用户产生PGW-CDR。EPC网络中SGW-C和PGW-C合设时可以只产生PGW-CDR。 |

> **说明**
> GPRS/UMTS网络下可以采用上述任意类型话单，EPC融合组网下必须采用PGW-CDR以保持GUL切换前后话单类型一致。

#### [话单容器](#ZH-CN_TOPIC_0292172742)

容器产生的背景：网络设计者希望话单能够记录足够的信息，包括各种计费条件改变时的计费信息，这会导致生成的话单较大，所以引入容器概念。容器记录计费条件改变时相关的计费信息，一张话单可以包括多个容器，从而在不增加话单量的情况下记录充分多的计费信息。

容器的分类：UNC与CG支持按照承载粒度（使用流量容器）或业务粒度（使用业务容器）统计用户访问流量，可通过 **SET CONTAINERTRIGGER** 命令配置，如 [表2](#ZH-CN_TOPIC_0292172742__table_03D3EB65) 所示。

*表2 话单容器描述*

| 容器类型 | 描述 |
| --- | --- |
| 流量容器 | 用于记录用户在一段时间内的流量、时长信息，不区分业务。用户开始使用业务时，GGSN/SGW-C/PGW-C向流量容器中记录流量、时长信息，满足如下任一条件时GGSN/SGW-C/PGW-C产生新的流量容器：<br>- QoS改变<br>- 费率时段改变<br>- 用户位置改变<br>- 产生话单 |
| 业务容器 | 用于记录用户的某个业务在一段时间内的流量、时长信息。用户开始使用业务时，GGSN/SGW-C/PGW-C向业务容器中记录流量、时长信息，满足如下任一条件时GGSN/SGW-C/PGW-C产生新的业务容器：<br>- IP-CAN承载修改<br>- 费率时段改变<br>- 在线计费处理失败（受**ADD DCCTEMPLATE**控制，参数“CCFH”取值为**CONTINUE**）<br>- 产生话单 |

流量容器/业务容器与话单的关联关系：当满足话单产生条件时，GGSN/SGW-C/PGW-C累加所有流量容器/业务容器中记录的流量、时长信息，同时产生新的流量容器/业务容器继续记录用户使用的流量、时长信息。

#### [话单的生成和传输](#ZH-CN_TOPIC_0292172742)

GGSN/SGW-C/PGW-C基于承载产生话单，包括GPRS/UMTS网络的一次PDP上下文、二次PDP上下文和EPC网络的缺省承载、专有承载。话单中包括用户静态信息，如MSISDN、IMSI、APN等；也包括动态信息，如用户使用的流量、承载的持续时间等。内容计费话单中还包括计费规格组名称（Charging Rule Base Name）、费率组、业务标识、业务使用量和业务使用时间等信息。

话单的产生过程包括创建话单、生成部分话单、关闭话单、话单编码和话单发送五个阶段。

*表3 话单生成过程*

| 话单生成阶段 | 实现描述 |
| --- | --- |
| 创建话单 | 用户激活时或部分话单生成后会触发创建新的话单，GGSN/SGW-C/PGW-C收集后续的计费信息并记录在话单中。 |
| 生成部分话单 | 用户进行业务的过程中，当满足特定的条件时（如<br>[表4](#ZH-CN_TOPIC_0292172742__tab55)<br>所示），GGSN/SGW-C/PGW-C会产生部分话单。这些特定的条件包括时间、流量、费率或计费条件变更次数达到设置的阈值等。 |
| 关闭话单 | 用户去激活时，GGSN/SGW-C/PGW-C会关闭用户的话单，生成最后话单。如<br>[表4](#ZH-CN_TOPIC_0292172742__tab55)<br>所示。 |
| 话单编码 | 话单关闭后GGSN/SGW-C/PGW-C对话单进行编码，产生二进制格式的话单数据，存入话单池中。GGSN/SGW-C/PGW-C按照ASN.1（Abstract Syntax Notation One）定义生成话单，话单编码采用BER（Basic Encoding Rules）方式。<br>GGSN/SGW-C/PGW-C采用的ASN.1定义符合3GPP协议TS 32.298标准。话单字段组成包括TS 32.298定义的全部必选字段和大部分可选字段。<br>可选字段是否包含在话单中可通过命令进行设置（参见<br>[配置话单字段（GGSN/SGW-C/PGW-C）](../激活离线计费/配置话单字段（GGSN_SGW-C_PGW-C）_95923364.md)<br>）。<br>说明：不同类型、不同版本或者不同接入网络的话单的详细编码和字段组成信息请参考<br>“话单接口说明书”<br>，可以联系华为技术支持工程师获取。 |
| 话单发送 | GGSN/SGW-C/PGW-C将编码后的话单数据从话单池中取出，封装到GTP’消息中，通过Ga接口发送给CG。 |

*表4 话单产生条件*

| 话单类型 | 话单产生条件 | GGSN/SGW-C/PGW-C的实现 | 备注 |
| --- | --- | --- | --- |
| 部分话单 | 按时间产生话单 | MS/UE<br>长时间连接时，超出设置的时间间隔（<br>**SET OFCTHRESHOLD**<br>）后，GGSN/SGW-C/PGW-C将所收集的计费信息生成一张话单。 | 配置步骤请参见<br>[配置离线计费参数（GGSN/SGW-C/PGW-C）](../激活离线计费/配置离线计费参数（GGSN_SGW-C_PGW-C）_95923590.md)<br>。 |
| 部分话单 | 按流量产生话单 | 当所传输的数据流量达到预先设置的流量阈值（<br>**SET OFCTHRESHOLD**<br>）时，GGSN/SGW-C/PGW-C就生成一张话单。 | 配置步骤请参见<br>[配置离线计费参数（GGSN/SGW-C/PGW-C）](../激活离线计费/配置离线计费参数（GGSN_SGW-C_PGW-C）_95923590.md)<br>。 |
| 部分话单 | 按计费条件改变产生话单 | 通过<br>**SET CDRTRIGGER**<br>控制计费条件改变是否产生话单。<br>- 当QoS、ULI以及费率改变次数之和达到设置的阈值（通过<br>**SET OFCTHRESHOLD**<br>命令配置）时，GGSN/SGW-C/PGW-C触发生成话单。<br>- 当RAT、服务节点PLMN ID、<br>MS/UE<br>Time Zone更新时生成话单。<br>- 当<br>MS/UE<br>一次连接过程中，服务节点（SGSN/S-GW/MME）的IP地址改变次数达到设置的阈值后，触发产生话单。 | 配置步骤请参见<br>[配置离线计费参数（GGSN/SGW-C/PGW-C）](../激活离线计费/配置离线计费参数（GGSN_SGW-C_PGW-C）_95923590.md)<br>。 |
| 部分话单 | 强制产生话单 | 当GGSN/SGW-C/PGW-C设置的话单条件还未达到，不具备生成话单的情况下，可通过命令<br>**FOC GENERATECDR**<br>强制产生话单。<br>这种情况主要用来测试计费系统是否正常。 | 配置步骤请参见<br>[配置话单可选功能（GGSN/SGW-C/PGW-C）](../激活离线计费/配置话单可选功能（GGSN_SGW-C_PGW-C）_95923448.md)<br>。 |
| 最后话单 | MS/UE<br>去激活产生话单 | 分组数据业务会话结束，GGSN/SGW-C/PGW-C触发产生话单。 | - |

具体话单内容样例：

如下所示eG-CDR话单中，ListofServiceData中只包含一个业务容器，其费率组RatingGroup为0，计费中心根据RG0得到流量/时间与用户费用的对应关系，然后进行扣费。

```
                    recordType  =  EG-CDR
```

```
             networkInitiation  =  0
```

```
                    servedIMSI  =  123020000000000
```

```
                   ggsnAddress  =  192.168.1.1
```

```
                    chargingID  =  788541156
```

```
                   sgsnAddress  =  {{192.168.10.1}}
```

```
             accessPointNameNI  =  water
```

```
                       pdpType  =  0x0121
```

```
              servedPDPAddress  =  10.10.10.1
```

```
            dynamicAddressFlag  =  1
```

```
          listOfTrafficVolumes  =  {{QoSNeg:ReliabClass(Unack GTP; Ack LLC,RLC,Protected data)DelayClass(1)PrecedClass(High)PeakThrput(256000octet/s)MeanThrput(Best Effort)DelivErrSDUs(-)DelivOrder(Yes)TraffClass(Interactive)MaxSDUSize(1520octets)MaxBRUpLk(8640kbps)MaxBRDnLk(8640kbps)SDUErrRatio(1*10-6)ResidBER(6*10-8)TraffPrior(1)TransDelay(10ms)GntBRUpLk(8640kbps)GntBRDnLk(8640kbps) VolUpLk:0xBA0 VolDnLk:0x476 ChangeCon:Record Closure ChangeTime:2009-02-23 15:17:46+01:00 failureHandlingContinue:1}}
```

```
             recordOpeningTime  =  2009-02-23 15:16:38+01:00
```

```
                      duration  =  68
```

```
            causeForRecClosing  =  Normal Release
```

```
                   diagnostics  =  ManufacturerSpecificCause:1
```

```
          recordSequenceNumber  =  1
```

```
                        nodeID  =  apn1
```

```
              recordExtensions  =  Empty value
```

```
           localSequenceNumber  =  1
```

```
              apnSelectionMode  =  MS or Network Provided Subscription Verified
```

```
                  servedMSISDN  =  111111111111111
```

```
       chargingCharacteristics  =  Prepaid service
```

```
             chChSelectionMode  =  sGSNSupplied
```

```
           iMSsignalingContext  =  Empty value
```

```
            externalChargingID  =  Empty value
```

```
            sgsnPLMNIdentifier  =  12303
```

```
  pSFurnishChargingInformation  =  Empty value
```

```
                  servedIMEISV  =  Empty value
```

```
                       rATType  =  Empty value
```

```
                    mSTimeZone  =  Empty value
```

```
       userLocationInformation  =  Empty value
```

```
      cAMELChargingInformation  =  Empty value
```

```
listOfServiceData  =  {{ratingGroup:0 chargingRuleBaseName:http-up localSequenceNumber:2 timeOfFirstUsage:2009-02-23 15:16:44+01:00 timeOfLastUsage:2009-02-23 15:17:25+01:00 timeUsage:41 serviceConditionChange:pDPContextRelease qoSInformationNeg:ReliabClass(Unack GTP; Ack LLC,RLC,Protected data)DelayClass(1)PrecedClass(High)PeakThrput(256000octet/s)MeanThrput(Best Effort)DelivErrSDUs(-)DelivOrder(Yes)TraffClass(Interactive)MaxSDUSize(1520octets)MaxBRUpLk(8640kbps)MaxBRDnLk(8640kbps)SDUErrRatio(1*10-6)ResidBER(6*10-8)TraffPrior(1)TransDelay(10ms)GntBRUpLk(8640kbps)GntBRDnLk(8640kbps) sgsn_Address:192.168.10.1 sGSNPLMNIdentifier:12303 datavolumeFBCUplink:0xBA0 datavolumeFBCDownlink:0x476 timeOfReport:2009-02-23 15:17:46+01:00 failureHandlingContinue:1}}
```

#### [话单可靠性](#ZH-CN_TOPIC_0292172742)

GGSN/SGW-C/PGW-C提供了多种机制，保证话单数据的可靠性。

*表5 话单可靠性*

| 类别 | 描述 |
| --- | --- |
| 预防重复话单 | 话单数据通过GTP’消息发送给主用CG后，如果GGSN/SGW-C/PGW-C未得到主用CG的响应，则会将相同的数据发送给备用CG。为了防止计费中心收到重复话单，发送给备用CG的GTP’消息中会携带话单数据可能重复（Send possible duplicated Data Record Packet）的标记。 |
| 缓存话单信息 | 当UNC与CG组中的所有CG间的链路都处于阻塞态时，UNC会将话单暂时缓存，根据CG组、话单版本、CG IP分目录缓存。<br>话单缓存的主目录是charge1，备目录是charge2，当主目录锁定的时候会使用备目录。<br>当缓存的话单超出<br>**SET CDRSTORAGECTRL**<br>设置的时间后，会产生<br>**ALM-81059 超期话单缓存**<br>，提醒操作维护人员尽快处理超期话单。 |
| 抑制零流量话单 | 为减少无效话单的数量，如果用户一段时间内未进行业务，即业务访问流量为零，则忽略本次产生话单的计费事件，不产生中间话单。<br>如下计费事件作为例外，不进行抑制：<br>- 用户去激活产生话单，否则对于用户上线后没有进行业务的情况无话单产生可能会引起运营商质疑。<br>- 使用命令强制产生话单，否则不符合强制产生话单的功能。 |
| 抑制话单产生 | 当话单池容量占用率达到告警门限<br>**ALM-81005 话单池空间不足**<br>时，即意味着当前产生的话单速度超过UNC的处理能力，可以采取抑制部分话单产生和控制用户接入数的办法减少话单数量。<br>- 抑制部分话单产生对更新类的trigger（如流量阈值到、终端时区改变等）只产生流量容器listOfTrafficVolumes字段，不产生话单，从而抑制部分话单的数量。<br>- 控制用户接入数量当发生告警<br>**ALM-81005 话单池空间不足**<br>时，GGSN/SGW-C/PGW-C将禁止所有新用户接入或者允许用户接入但是不计费，直到话单池恢复告警后再修改用户接入控制比例为拒绝20%的用户接入，当话单池使用率小于50%时修改用户接入控制比例为0，即不做接入控制。 |
| 备份计费信息 | GGSN/SGW-C/PGW-C将用户的计费信息定时备份到CSDB_VNFC上。当发生计费POD故障时，其他计费POD可以立即获取用户计费信息，并接替故障计费POD继续产生话单，保证计费不中断。 |
