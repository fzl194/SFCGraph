---
id: UNC@20.15.2@MMLCommand@ADD GTPCCMPT
type: MMLCommand
name: ADD GTPCCMPT（增加GTP-C V0/V1协议兼容性配置）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: GTPCCMPT
command_category: 配置类
applicable_nf:
- SGSN
- MME
effect_mode: 立即生效
is_dangerous: false
max_records: 512
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- GTP-C接口管理
- GTP-C协议管理
- GTP-C V0 V1协议兼容性
status: active
---

# ADD GTPCCMPT（增加GTP-C V0/V1协议兼容性配置）

## 功能

**适用网元：SGSN、MME**

- 此命令用于增加GTP-C V0/V1协议兼容性配置，用于控制在SGSN或者MME发送的GTP消息中，是否允许携带特定的可选信元。

## 注意事项

- 此命令执行后立即生效。
- 此命令最大记录数为512条。
- Forward Srns Context消息仅在SGSN发送。
- SGSN发送GTP消息SGSN Context Response、Forward Relocation Request时，可以控制在GTP消息中是否允许携带R4协议版本新增加的可选信元RAB Context、Charging Characteristics等。当对端GGSN不支持这些R4版本的新信元时，可以通过[**ADD GTPCCMPT**](增加GTP-C V0_V1协议兼容性配置(ADD GTPCCMPT)_72225601.md)命令进行配置，使GTP消息中不携带这些信元。一般情况下，只要不是特别老的对端设备，应该都支持这些新特性的，所以一般建议在GTP消息中携带这些信元。
- 当没有指定在GTP消息中，是否允许携带特定的可选信元时，系统默认情况下将在GTP消息中携带这些可选信元。
- “消息分类”、“消息类型”和“信元类型”三个参数唯一确定一条记录。
- 消息类型、信元类型和携带方式的映射关系：
  *表1 消息类型、信元类型和携带方式的映射关系*

  | 消息类型 | 信元类型 | 携带方式 |
  | --- | --- | --- |
  | SGSN Context Response | RAB Context | - 不携带<br>- 按协议定义携带<br>- 按自定义携带 |
  | SGSN Context Response | Charging Characteristics | - 不携带<br>- 按协议定义携带<br>- 按自定义携带 |
  | SGSN Context Response | IMEISV | - 不携带<br>- 按协议定义携带<br>- 按自定义携带 |
  | SGSN Context Response | PDP_CONTEXT | - 不携带<br>- 按协议定义携带<br>- 按自定义携带 |
  | SGSN Context Response | PDP Context Prioritization | - 不携带<br>- 按协议定义携带<br>- 按自定义携带 |
  | SGSN Context Response | Evolved Allocation/Retention Priority II | - 不携带<br>- 按协议定义携带<br>- 按自定义携带 |
  | SGSN Context Response | Co-located GGSN-PGW FQDN | - 不携带<br>- 按协议定义携带<br>- 按自定义携带 |
  | SGSN Context Response | IMSI | - 不携带<br>- 按协议定义携带<br>- 按自定义携带 |
  | Forward Relocation Request | Charging Characteristics | - 不携带<br>- 按协议定义携带<br>- 按自定义携带 |
  | Forward Relocation Request | IMEISV | - 不携带<br>- 按协议定义携带<br>- 按自定义携带 |
  | Forward Relocation Request | PDP Context Prioritization | - 不携带<br>- 按协议定义携带<br>- 按自定义携带 |
  | Forward Relocation Request | Evolved Allocation/Retention Priority II | - 不携带<br>- 按协议定义携带<br>- 按自定义携带 |
  | Forward Relocation Request | Selected PLMN ID | - 不携带<br>- 按协议定义携带<br>- 按自定义携带 |
  | Forward Relocation Request | Co-located GGSN-PGW FQDN | - 不携带<br>- 按协议定义携带<br>- 按自定义携带 |
  | Forward Relocation Request | UE Network Capability | - 不携带<br>- 按协议定义携带<br>- 按自定义携带 |
  | Forward Relocation Request | Additional MM context for SRVCC | - 不携带<br>- 按协议定义携带<br>- 按自定义携带 |
  | Forward Relocation Request | Additional flags for SRVCC | - 不携带<br>- 按协议定义携带<br>- 按自定义携带 |
  | Forward Relocation Request | Session Transfer Number for SRVCC | - 不携带<br>- 按协议定义携带<br>- 按自定义携带 |
  | Forward Relocation Request | Correlation MSISDN | - 不携带<br>- 按协议定义携带<br>- 按自定义携带 |
  | Forward Relocation Request | Extended RANAP Cause | - 不携带<br>- 按协议定义携带<br>- 按自定义携带 |
  | Forward Relocation Request | eNodeB ID | - 不携带<br>- 按协议定义携带<br>- 按自定义携带 |
  | Forward Srns Context | Source RNC PDCP Context | - 不携带<br>- 按协议定义携带<br>- 按自定义携带 |
  | Update PDP Context Response | User Location Information | - 不携带<br>- 按协议定义携带<br>- 按自定义携带 |
  | Update PDP Context Response | MS Time Zone | - 不携带<br>- 按协议定义携带<br>- 按自定义携带 |
  | Delete PDP Context Response | User Location Information | - 不携带<br>- 按协议定义携带<br>- 按自定义携带 |
  | Delete PDP Context Response | MS Time Zone | - 不携带<br>- 按协议定义携带<br>- 按自定义携带 |
  | Delete PDP Context Request | User Location Information | - 不携带<br>- 按协议定义携带<br>- 按自定义携带 |
  | Delete PDP Context Request | MS Time Zone | - 不携带<br>- 按协议定义携带<br>- 按自定义携带 |
  *表2 消息类型、信元类型和APNOI大小写的映射关系*

  | 消息类型 | 信元类型 | APNOI大小写 |
  | --- | --- | --- |
  | SGSN Context Response | PDP Context | - 缺省值<br>- SGSN小写<br>- SGSN和MME小写 |
  | Forward Relocation Request | PDP Context | - 缺省值<br>- SGSN小写<br>- SGSN和MME小写 |
  *表3 消息类型、信元类型和是否支持COMMON FLAGS的映射关系*

  | 消息类型 | 信元类型 | 是否支持COMMON FLAGS |
  | --- | --- | --- |
  | Create PDP Context Request | Common Flags | - NO<br>- YES |
  | Update PDP Context Request | Common Flags | - NO<br>- YES |

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IDX | 索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定唯一标识特定的可选信元的索引。<br>数据来源：整网规划<br>取值范围：0～511<br>默认值：无 |
| MSGCLS | 消息分类 | 可选必选说明：必选参数<br>参数含义：该参数用于指示消息分类。<br>数据来源：整网规划<br>取值范围：<br>- “PM(路径管理)”<br>- “TM(隧道管理)”<br>- “MM(移动管理)”<br>默认值：无<br>配置原则：根据对端设备能力进行设置。<br>说明：暂时不支持<br>“PM(路径管理)”<br>的消息类别。 |
| MMMSGTYPE | 消息类型 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指示消息分类为移动管理时的消息类型。<br>前提条件：当<br>“MSGCLS”<br>取值为<br>“MM(移动管理)”<br>时，该参数有效。<br>数据来源：整网规划<br>取值范围：<br>- “SGSN_CONTEXT_RESP(SGSN Context Response)”<br>- “FWD_RLC_REQ(Forward Relocation Request)”<br>- “FORWARD_SRNS_CONTEXT(Forward Srns Context)”<br>默认值：无<br>配置原则：根据对端设备能力进行设置。 |
| TMMSGTYPE | 消息类型 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指示消息分类为隧道管理时的消息类型。<br>前提条件：当<br>“MSGCLS”<br>取值为<br>“TM(隧道管理)”<br>时，该参数有效。<br>数据来源：整网规划<br>取值范围：<br>- “CREATE_PDP_CONTEXT_REQUEST(Create PDP Context Request)”<br>- “UPDATE_PDP_CONTEXT_REQUEST(Update PDP Context Request)”<br>- “UPDATE_PDP_CONTEXT_RESPONSE(Update PDP Context Response)”<br>- “DELETE_PDP_CONTEXT_RESPONSE(Delete PDP Context Response)”<br>- “DELETE_PDP_CONTEXT_REQUEST(Delete PDP Context Request)”<br>默认值：无 |
| CTXRSP | SGSN Context Response的信元类型 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指示消息类型为SGSN Context Response时的信元类型。<br>前提条件：当<br>“MMMSGTYPE”<br>取值为<br>“SGSN_CONTEXT_RESP(SGSN Context Response)”<br>时，该参数有效。<br>数据来源：整网规划<br>取值范围：<br>- “RAB_CONTEXT(RAB Context)”<br>- “CHR_CHARACTER(Charging Characteristics)”<br>- “IMEISV(IMEISV)”<br>- “PDP_CONTEXT(PDP Context)”<br>- “PDP_CONTEXT_PRIORITIZATION(PDP Context Prioritization)”<br>- “EVOL_ALLOC_RET_PRIORITY_II(Evolved Allocation/Retention Priority II)”<br>- “CO_LOC_GGSN_PGW_FQDN(Co-located GGSN-PGW FQDN)”<br>- “IMSI(IMSI)”<br>默认值：无<br>配置原则：根据对端设备能力进行设置。<br>说明：“IMSI(IMSI)”<br>用于控制当旧侧SGSN向新侧SGSN发送带PTMSI签名不匹配原因值的SGSN Context Response/Context Response消息时，是否携带IMSI信元。 |
| FWDRLCREQ | Forward Relocation Request的信元类型 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指示消息类型为Forward Relocation Request时的信元类型。<br>前提条件：当<br>“MMMSGTYPE”<br>取值为<br>“FWD_RLC_REQ(Forward Relocation Request)”<br>时，该参数有效。<br>数据来源：整网规划<br>取值范围：<br>- “CHR_CHARACTER(Charging Characteristics)”<br>- “IMEISV(IMEISV)”<br>- “PDP_CONTEXT(PDP Context)”<br>- “PDP_CONTEXT_PRIORITIZATION(PDP Context Prioritization)”<br>- “SELECTED_PLMN_ID(Selected PLMN ID)”：控制LTE到UMTS的系统切换流程，Forward Relocation Request消息是否携带Selected PLMN字段。<br>- “EVOL_ALLOC_RET_PRIORITY_II(Evolved Allocation/Retention Priority II)”<br>- “CO_LOC_GGSN_PGW_FQDN(Co-located GGSN-PGW FQDN)”<br>- “UE_NETWORK_CAPABILITY(UE Network Capability)”<br>- “SRVCCMMCTXT(Additional MM context for SRVCC)”<br>- “SRVCCFLG(Additional flags for SRVCC)”<br>- “STN-SR(Session Transfer Number for SRVCC)”<br>- “C-MSISDN(Correlation MSISDN)”<br>- “EXTENDED_RANAP_CAUSE(Extended RANAP Cause)”<br>- “ENODEB_ID(eNodeB ID)”<br>默认值：无 |
| FWDSRNSCTX | Forward Srns Context的信元类型 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指示Intra Relocation流程消息类型为Forward Srns Context时的信元类型。<br>前提条件：当<br>“MMMSGTYPE”<br>取值为<br>“FORWARD_SRNS_CONTEXT(Forward Srns Context)”<br>时，该参数有效。<br>数据来源：整网规划<br>取值范围：<br>“SOURCE_RNC_PDCP_CONTEXT(Source RNC PDCP Context)”<br>默认值：无 |
| CRTPDPREQ | Create PDP Context Request信元类型 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指示消息类型为Create PDP Context Request时的信元类型。<br>前提条件：当<br>“TMMSGTYPE”<br>取值为<br>“CREATE_PDP_CONTEXT_REQUEST(Create PDP Context Request)”<br>时，该参数有效。<br>数据来源：整网规划<br>取值范围：<br>- “COMMON_FLAGS(Common Flags)”<br>- “UPSELIND(UP Function Selection Indication Flag)”<br>默认值：无 |
| UPDPDPREQ | Update PDP Context Request信元类型 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指示消息类型为Update PDP Context Request时的信元类型。<br>前提条件：当<br>“TMMSGTYPE”<br>取值为<br>“UPDATE_PDP_CONTEXT_REQUEST(Update PDP Context Request)”<br>时，该参数有效。<br>数据来源：整网规划<br>取值范围：<br>“COMMON_FLAGS(Common Flags)”<br>默认值：无 |
| UPDPDPRES | Update PDP Context Response信元类型 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指示消息类型为Update PDP Context Response时的信元类型。<br>前提条件：当<br>“TMMSGTYPE”<br>取值为<br>“UPDATE_PDP_CONTEXT_RESPONSE(Update PDP Context Response)”<br>时，该参数有效。<br>数据来源：整网规划<br>取值范围：<br>- ULI(User Location Information)<br>- TZ(MS Time Zone)<br>默认值：无 |
| DELPDPRES | Delete PDP Context Response信元类型 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指示消息类型为Delete PDP Context Response时的信元类型。<br>前提条件：当<br>“TMMSGTYPE”<br>取值为<br>“DELETE_PDP_CONTEXT_RESPONSE(Delete PDP Context Response)”<br>时，该参数有效。<br>数据来源：整网规划<br>取值范围：<br>- ULI(User Location Information)<br>- TZ(MS Time Zone)<br>默认值：无 |
| DELPDPREQ | Delete PDP Context Request信元类型 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指示消息类型为Delete PDP Context Request时的信元类型。<br>前提条件：当<br>“TMMSGTYPE”<br>取值为<br>“DELETE_PDP_CONTEXT_REQUEST(Delete PDP Context Request)”<br>时，该参数有效。<br>数据来源：整网规划<br>取值范围：<br>- TZ(MS Time Zone)<br>默认值：无 |
| INCLUDE | 携带方式 | 可选必选说明：条件必选参数<br>参数含义：该参数用于控制在SGSN发送的GTP消息中，是否允许携带特定的可选信元。<br>前提条件：当<br>“FWDSRNSCTX”<br>取值为<br>“SOURCE_RNC_PDCP_CONTEXT(Source RNC PDCP Context)”<br>，或者<br>“CTXRSP”<br>取值不为<br>“PDP_CONTEXT(PDP Context)”<br>，或者<br>“FWDRLCREQ”<br>取值不为<br>“PDP_CONTEXT(PDP Context)”<br>，或者<br>“UPDPDPRES”<br>取值为<br>“ULI(User Location Information)”<br>、<br>“TZ(MS Time Zone)”<br>，或者<br>“DELPDPRES”<br>取值为<br>“ULI(User Location Information)”<br>、<br>“TZ(MS Time Zone)”<br>，或者<br>“DELPDPREQ”<br>取值为<br>“TZ(MS Time Zone)”<br>时，该参数有效。<br>数据来源：整网规划<br>取值范围：<br>- “NOT_CARRY(不携带)”<br>- “PRO_DEFINE(按协议定义携带)”<br>- “SELF_DEFINE(按自定义携带)”<br>默认值：无<br>配置原则：<br>- 取值为“NOT_CARRY(不携带)”时，表示在SGSN发送的GTP消息中，不携带特定的可选信元。<br>- 取值为“PRO_DEFINE(按协议定义携带)”时，表示在SGSN发送的GTP消息中，携带特定的可选信元。<br>- 取值为“SELF_DEFINE(按自定义携带)”时，UNC暂时不支持这种携带方式。 |
| APNOICASE | APNOI大小写 | 可选必选说明：条件必选参数<br>参数含义：该参数用于控制Inter RAU或Relocation流程中，是否将旧侧SGSN或旧侧MME在发送给新侧的GTP-C V0/V1协议消息SGSN Context Response或Forward Relocation Request中携带的APNOI强制转换成小写格式。<br>前提条件：当<br>“CTXRSP”<br>或者<br>“FWDRLCREQ”<br>取值为<br>“PDP_CONTEXT(PDP Context)”<br>时，该参数有效。<br>数据来源：整网规划<br>取值范围：<br>- “DEFAULT(缺省值)”<br>- “LOWERCASE(SGSN小写)”<br>- “LOWERCASEGUL(SGSN和MME小写)”<br>默认值：无<br>配置原则：<br>- 取值为“DEFAULT(缺省值)”时，旧侧SGSN和旧侧MME均不转换成小写，其大小写格式根据系统配置情况发送。<br>- 取值为“LOWERCASE(SGSN小写)”时，旧侧SGSN发送GTP-C V0/V1协议消息SGSN Context Response或Forward Relocation Request时将APNOI转换成小写。MME不转换，MME的大小写格式根据系统配置情况发送。<br>- 取值为“LOWERCASEGUL(SGSN和MME小写)”时，旧侧SGSN和旧侧MME发送GTP-C V0/V1协议消息SGSN Context Response或Forward Relocation Request时均将APNOI转换成小写。 |
| CMFLG | 是否支持Common Flags信元 | 可选必选说明：条件必选参数<br>参数含义：该参数用于控制在SGSN发送的GTP消息中，是否支持Common Flags信元。<br>前提条件：当<br>“CRTPDPREQ”<br>或者<br>“UPDPDPREQ”<br>取值为<br>“COMMON_FLAGS(Common Flags)”<br>时，该参数有效。<br>数据来源：整网规划<br>取值范围：<br>- “NO(No)”<br>- “YES(Yes)”<br>默认值：无 |
| UPSELFLAG | UP Function Selection Indication Flags | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定信元类型为UP Function Selection Indication Flag时允许携带的标志位。<br>前提条件：当<br>“CRTPDPREQ”<br>取值为<br>“UPSELIND(UP Function Selection Indication Flag)”<br>时，该参数有效。<br>数据来源：整网规划<br>取值范围：<br>“DCNR(Dual connectivity with NR) ”<br>默认值：无 |

## 操作的配置对象

- [GTP-C V0/V1协议兼容性配置（GTPCCMPT）](configobject/UNC/20.15.2/GTPCCMPT.md)

## 使用实例

加一条GTP-C V0/V1协议兼容性配置，设置在消息类型为SGSN_CONTEXT_RESP(SGSN Context Response)的消息中（归属于MM(移动管理)）， 按协议定义携带RAB Context信元：

ADD GTPCCMPT: IDX=0, MSGCLS=MM, MMMSGTYPE=SGSN_CONTEXT_RESP, CTXRSP=RAB_CONTEXT, INCLUDE=PRO_DEFINE;

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加GTP-C-V0_V1协议兼容性配置(ADD-GTPCCMPT)_72225601.md`
