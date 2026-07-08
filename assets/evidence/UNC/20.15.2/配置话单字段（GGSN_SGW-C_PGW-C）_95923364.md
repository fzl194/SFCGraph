# 配置话单字段（GGSN/SGW-C/PGW-C）

- [操作场景](#ZH-CN_OPI_0295923364__1.3.1)
- [必备事项](#ZH-CN_OPI_0295923364__1.3.2)
- [操作步骤](#ZH-CN_OPI_0295923364__1.3.3)
- [任务示例](#ZH-CN_OPI_0295923364__1.3.4)

## [操作场景](#ZH-CN_OPI_0295923364)

对于话单中标识为可选（C）或条件可选（O <sub>C</sub> ）或条件必选（O <sub>M</sub> ）的字段，GGSN/SGW-C/PGW-C支持自定义配置是否携带该字段，运营商可根据需要选择配置。

话单可选字段可以基于APN、全局进行配置， 它们的优先级顺序是APN > 全局配置 > 默认值。 如果高级别的没有配置，则取用低级别的话单字段模板，否则取用默认值。

GGSN/SGW-C/PGW-C支持为不同的话单类型绑定不同的CDRFieldTemp话单字段模板，可以分别独立控制SGW-CDR、PGW-CDR、G-CDR话单携带的字段，增强话单字段的灵活度。

> **说明**
> - 适用于SGW-C、PGW-C、GGSN。
> - 系统升级时，需注意先升级CG，再升级GGSN/SGW-C/PGW-C，以防止GGSN/SGW-C/PGW-C先升级后话单中有CG不识别的字段。

## [必备事项](#ZH-CN_OPI_0295923364)

前提条件

- 请仔细阅读[Ga/Gy接口离线/在线计费](../../../../../业务专题/5G Core 计费解决方案/计费解决方案概述/计费原理/Ga_Gy接口离线_在线计费_87165686.md)。
- 完成[配置到CG的数据（GGSN/SGW-C/PGW-C）](配置到CG的数据（GGSN_SGW-C_PGW-C）_95923479.md)。

数据

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| **ADD CDRFIELDTEMP** | 话单字段模板名（TEMPLATENAME） | cdrfield-test | 本端规划 | 配置单字段模板，控制话单中是否携带对应字段。 |
| **ADD CDRFIELDTEMP** | apn-network-identifier（APNNETWORKID） | DISABLE | 本端规划 | 配置话单中是否包含APN网络节点标识信息，默认值是<br>**ENABLE**<br>。 |
| **ADD CDRFIELDTEMP** | ms-time-zone（MSTIMEZONE） | DISABLE | 与对端协商 | 配置话单中是否携带ms-time-zone字段，默认值是<br>**ENABLE**<br>。 |
| **SET GLBCDRFLDTEMP** | PGW-CDR话单字段模板名（PGWCDRTEMPLATE） | cdrfield-test | 全网规划 | 配置全局绑定话单字段模板 |
| **ADD APN** | APN名称（APN） | apn-test | 本端规划 | 配置APN，可以使用命令<br>**LST APN**<br>查询。 |
| **SET APNCHARGECTRL** | APN名称（APN） | apn-test | 已配置数据中获取 | 为APN实例绑定话单字段模板。 |
| **SET APNCHARGECTRL** | PGW-CDR话单字段模板名（PGWCDRTEMPLATE） | cdrfield-test | 本端规划 | 为APN实例绑定话单字段模板。 |

## [操作步骤](#ZH-CN_OPI_0295923364)

1. 配置话单字段。
  > **说明**
  > GGSN/SGW-C/PGW-C默认携带话单可选字段，如果不需要携带某个字段，将对应字段设置为 **DISABLE** 。
    a. 配置话单中携带用户信息字段，如 [表1](#ZH-CN_OPI_0295923364__tab1) 所示。
      *表1 话单中用户信息字段*

      | 类别 | 话单字段 | 字段解释 |
      | --- | --- | --- |
      | **ADD CDRFIELDTEMP** | MSISDN字段 | 该字段记录用户的MSISDN号。 |
      | **ADD CDRFIELDTEMP** | served-imeisv字段 | 该字段记录用户的IMEISV号。 |
      | **ADD CDRFIELDTEMP** | CCSeletionMode字段 | 该字段记录计费属性Charging Characteristics的选择模式，是使用用户激活消息中所携带的<br>SGSN/S-GW<br>/MME计费属性，还是使用GGSN/SGW-C/PGW-C所配置的计费属性。 |
      | **BIT836 控制是否携带华为CG的5G定制字段** | user5GFlag字段 | 该字段记录用户是否为5G用户。<br>说明：当和华为CG对接时，此软参需设置为1，其他场景设置为0。 |
    b. 配置话单中携带接入信息字段，如 [表2](#ZH-CN_OPI_0295923364__tab2) 所示。
      *表2 话单中接入信息字段*

      | 类别 | 话单字段 | 字段解释 |
      | --- | --- | --- |
      | **ADD CDRFIELDTEMP** | ApnNetworkId字段 | 该字段记录APN中的网络节点标识信息。 |
      | **ADD CDRFIELDTEMP** | ApnSelectMode字段 | 该字段记录<br>SGSN/MME<br>的APN选择模式。 |
      | **ADD CDRFIELDTEMP** | PDPType字段 | 该字段记录PDP类型，IP或者PPP。 |
      | **ADD CDRFIELDTEMP** | SGSNSGWPLMNId字段 | 该字段记录<br>SGSN/S-GW<br>/MME的PLMN。 |
      | **ADD CDRFIELDTEMP** | ServedPDPAddr字段 | 该字段记录用户地址。 |
      | **ADD CDRFIELDTEMP** | DynAddrFlag字段 | 该字段标识用户地址是动态分配地址。<br>说明：对于单栈用户，该字段用于标识IPv4或IPv6类型的动态地址。 |
      | **ADD CDRFIELDTEMP** | ULI字段 | 该字段记录3GPP用户位置信息。<br>说明：3GPP用户接入时，只有<br>SGSN/S-GW<br>和SGW-C/PGW-C都支持user-location-information字段，在话单格式里配置此字段该字段才会生效，否则配置无效。 |
      | **ADD CDRFIELDTEMP** | RATType字段 | 该字段记录用户的无线接入技术类型，取值有<br>**UTRAN**<br>、<br>**GERAN**<br>、<br>**GAN**<br>、<br>**UTRAN**<br>和<br>**HSPA Evolution**<br>。<br>说明：只有<br>SGSN/S-GW<br>/SGW-C/MME和PGW-C都支持携带RATType字段，在话单格式里配置此字段该字段才会生效，否则配置无效。 |
      | **ADD CDRFIELDTEMP** | MSTimeZone字段 | 该字段记录用户所在时区。<br>说明：只有<br>SGSN/S-GW<br>/SGW-C和PGW-C都支持携带ms-time-zone字段，在话单格式里配置此字段该字段才会生效，否则配置无效。 |
      | **ADD CDRFIELDTEMP** | PGWAddressUsed字段 | 该字段记录P-GW的控制面地址，该字段记录IPv4地址。 |
      | **ADD CDRFIELDTEMP** | PGWAddressIPv6字段 | 该字段记录P-GW或S5/S8接口的IPv6地址。<br>说明：该字段协议定义仅R9、R10版本的PGW-CDR支持。 |
      | **ADD CDRFIELDTEMP** | PGWPLMNId字段 | 该字段记录P-GW的PLMN。 |
      | **ADD CDRFIELDTEMP** | NodeId字段 | 该字段记录GGSN/SGW-C/PGW-C的节点标识，节点标识名称通过命令<br>**SET OFCCDRPARA**<br>进行设置。 |
      | **ADD CDRFIELDTEMP** | NetInitPDPCont | 该字段记录用户<br>PDP上下文/EPS承载<br>是由网络侧激活的。 |
      | **ADD CDRFIELDTEMP** | PDNConnectionId字段 | 该字段记录缺省承载的计费标识，以此可以识别出同一个PDN连接内的话单。<br>说明：**ADD CDRFIELDTEMP**<br>命令设置的字段对应于话单中的pdn-connection-charging-id字段。 |
      | **ADD CDRFIELDTEMP** | msiUnauthFlag字段 | 该字段记录用户的IMSI是否未鉴权。<br>说明：通过GTPv2接入的紧急呼叫用户如果IMSI未鉴权，GGSN/SGW-C/PGW-C向CG上报R9及之后版本话单时携带该字段。 |
    c. 配置话单中携带业务信息字段，如 [表3](#ZH-CN_OPI_0295923364__tab3) 所示。
      *表3 话单中业务信息字段*

      | 类别 | 话单字段 | 字段解释 |
      | --- | --- | --- |
      | **SET OFCCDRPARA** | List of Traffic Volume | 配置PGW-CDR的字段携带方式。可以控制PGW-CDR是否携带流量容器（ListOfTrafficVolume）。 |
      | **SET OFCCDRPARA** | RAT Type | 配置PGW-CDR的字段携带方式。可以控制PGW-CDR的业务容器（ListOfServiceData）是否携带RAT Type。 |
      | **SET OFCCDRPARA** | APN-AMBR | 配置PGW-CDR的字段携带方式。可以控制PGW-CDR的业务容器（ListOfServiceData）是否携带APN-AMBR。 |
      | **ADD CDRFIELDTEMP** | LoTV字段 | 该字段记录用户上下行流量信息。 |
      | **ADD CDRFIELDTEMP** | LoSD字段 | 该字段记录业务上下行流量信息。<br>说明：R6版本以后的eG-CDR话单中支持该字段。<br>R8版本以后的PGW-CDR和SGW-CDR话单中支持该字段。 |
      | **ADD CDRFIELDTEMP** | RecordExtention字段 | 该字段记录运营商或设备制造商定义的扩展信息。<br>说明：内容计费G-CDR话单需要扩展RecordExtention字段，普通计费G-CDR话单不需要扩展该字段。R4及之后版本的G-CDR话单以及R6及之后版本的eG-CDR才支持该字段。<br>说明：当参数<br>“record-extensions-operator”<br>设置为<br>“glb”<br>时：<br>- 若同时开启AAA RADIUS计费功能，则可在PGW-CDR话单扩展字段（record-extensions）中携带RADIUS Acct-Session-ID、Termination-Cause字段。<br>- 若同时开启内容计费功能，则可在PGW-CDR话单扩展字段（record-extensions）中携带各业务（RG+SID）上下行报文数。 |
      | **ADD CDRFIELDTEMP** | ImsSigContext字段 | 该字段用户标识是IMS信令专用上下文。 |
      | **ADD CDRFIELDTEMP** | StartTime字段 | 该字段记录<br>PDP上下文/EPS承载<br>激活的时间。 |
      | **ADD CDRFIELDTEMP** | StopTime字段 | 该字段记录<br>PDP上下文/EPS承载<br>去激活的时间。 |
    d. 配置话单中其他信息字段，如 [表4](#ZH-CN_OPI_0295923364__tab4) 所示。
      *表4 话单中其他信息字段*

      | 类别 | 话单字段 | 字段解释 |
      | --- | --- | --- |
      | **ADD CDRFIELDTEMP** | Diagnostics字段 | 该字段记录用户去激活的原因。 |
      | **ADD CDRFIELDTEMP** | RecSeqNumber字段 | 该字段记录同一<br>PDP上下文/EPS承载<br>中产生的话单的帧序列号。 |
      | **ADD CDRFIELDTEMP** | LocalRecSeqNum字段 | 该字段记录GGSN/SGW-C/PGW-C重启后分配的话单顺序号。 |
      | **ADD CDRFIELDTEMP** | PSFCI字段 | 该字段记录运营商或设备制造商定义的信息。 |
2. 配置全局话单字段模板。
  **SET GLBCDRFLDTEMP**
3. 配置APN实例的话单字段模板。
    a. 配置APN实例。如已配置APN，请跳过该步骤。
      **ADD APN**
    b. 配置APN实例绑定话单字段模板。
      **SET APNCHARGECTRL**

## [任务示例](#ZH-CN_OPI_0295923364)

任务描述

任务一：配置全局话单字段模板，配置GGSN/SGW-C/PGW-C话单中不携带apn network identifier字段和ms time zone字段。

任务二：配置APN实例的话单字段模板，配置GGSN/SGW-C/PGW-C话单中不携带apn network identifier字段和ms time zone字段。

脚本

//任务一：配置全局话单字段模板，配置话单中不支持apn network identifier字段和ms time zone字段。

```
ADD CDRFIELDTEMP: TEMPLATENAME="cdrfield-test",APNNETWORKID=DISABLE,MSTIMEZONE=DISABLE,ULI=ENABLE,RECORDEXTENTION=DISABLE;
```

```
SET GLBCDRFLDTEMP: PGWCDRTEMPLATE="cdrfield-test";
```

//任务二：配置APN实例的话单字段模板，配置GGSN/SGW-C/PGW-C话单中不携带apn network identifier字段和ms time zone字段。

```
ADD CDRFIELDTEMP: TEMPLATENAME="cdrfield-test",APNNETWORKID=DISABLE,MSTIMEZONE=DISABLE,ULI=ENABLE,RECORDEXTENTION=DISABLE;
```

```
ADD APN: APN="apn-test";
```

```
SET APNCHARGECTRL: APN="apn-test",PGWCDRTEMPLATE="cdrfield-test";
```
