---
id: UNC@20.15.2@MMLCommand@MOD S1SMARTRULE
type: MMLCommand
name: MOD S1SMARTRULE（修改S1模式信令抑制规则）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: S1SMARTRULE
command_category: 配置类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 业务安全管理
- Smartphone管理
- 异常信令节省
- S1模式信令抑制规则管理
status: active
---

# MOD S1SMARTRULE（修改S1模式信令抑制规则）

## 功能

**适用网元：MME**

该命令用于修改已配置的基于终端类型的S1模式信令抑制规则。

## 注意事项

- 此命令执行后立即生效。
- 此命令涉及LTE UE信令控制特性（特性编号：WSFD-206002，license部件编码：LKV2LUSC01），执行命令前请使用[**DSP LICENSE**](../../../../../../../平台服务管理/操作维护/License管理/显示License(DSP LICENSE)_00360098.md)命令确认对应特性license是否得到授权，执行[**LST LICENSESWITCH**](../../../../../../../平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md)命令确认特性开关状态为“ENABLE(打开)”。
- 在部署VOLTE特性时，请谨慎配置网络侧分离的抑制措施和唤醒措施。具体请参考命令参数描述。

## 权限

manage-ug; system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| UETYPE | 终端类型 | 可选必选说明：必选参数<br>参数含义：该参数用于设置用户的终端类型。<br>数据来源：整网规划<br>取值范围：<br>- “ANDROID(Android)”<br>- “BLACKBERRY(Black Berry)”<br>- “IOS(iOS)”<br>- “WINDOWS(Windows)”<br>- “CUSTOM_TYPE_1(自定义类型1)”<br>- “CUSTOM_TYPE_2(自定义类型2)”<br>- “CUSTOM_TYPE_3(自定义类型3)”<br>- “CUSTOM_TYPE_4(自定义类型4)”<br>- “CUSTOM_TYPE_5(自定义类型5)”<br>- “CUSTOM_TYPE_6(自定义类型6)”<br>- “CUSTOM_TYPE_7(自定义类型7)”<br>- “CUSTOM_TYPE_8(自定义类型8)”<br>- “CUSTOM_TYPE_9(自定义类型9)”<br>- “CUSTOM_TYPE_10(自定义类型10)”<br>- “CUSTOM_TYPE_11(自定义类型11)”<br>- “CUSTOM_TYPE_12(自定义类型12)”<br>- “UNKNOWN_TYPE(未知类型)”<br>默认值：无<br>说明：“UNKNOWN_TYPE(未知类型)”：未获取到IMEI的终端类型或者没有匹配的<br>[**ADD IMEILIB**](../../终端类型识别/IMEI库管理/增加IMEI库记录（ADD IMEILIB）_26145734.md)<br>配置的终端类型。 |
| ATTACHCTRLRULE | 附着抑制措施 | 可选必选说明：可选参数<br>参数含义：该参数用于设置当系统检测到终端发起的附着行为异常后采取的抑制措施。<br>数据来源：整网规划<br>取值范围：<br>- “SPECCAUSEREJ(特定原因拒绝)”<br>- “PARKAPNACT(Parking APN激活)”<br>- “DISCARD(丢弃)”<br>默认值：无<br>配置原则：由于不同类型终端的行为有差异，需要结合终端行为选择一种或多种抑制措施。<br>说明：- 抑制措施说明- 特定原因拒绝：当系统检测到终端的附着行为异常后，给终端发送附着拒绝消息，携带配置的协议原因值。<br>- Parking APN激活：由于缺省承载建立失败可能会导致终端频繁附着，当系统检测到终端的附着行为异常后，使用配置的Parking APN建立缺省承载。<br>- 丢弃：当系统检测到终端的附着行为异常后，直接丢弃附着请求消息。异常服务请求或异常PDN连接流程中执行网络侧分离的抑制措施后，若配置了丢弃的抑制措施，在[**SET S1SMARTPARA**](../S1模式信令抑制参数管理/设置S1模式信令抑制参数(SET S1SMARTPARA)_72225427.md)中“附着异常抑制时长(分钟) ”参数设置的抑制时间内，终端发起的附着请求消息也会被丢弃。抑制措施的优先级由高到低依次为：特定原因拒绝、Parking APN激活、丢弃。<br>- 1小时内，终端发起的附着请求次数到达预设阈值后，可判断是异常行为，采取配置的第一种抑制措施进行抑制。阈值由命令[**SET S1SMARTPARA**](../S1模式信令抑制参数管理/设置S1模式信令抑制参数(SET S1SMARTPARA)_72225427.md)中“附着异常识别门限(次/小时)”参数设置。<br>- 已经被抑制的终端，如果在抑制时间内再发起一次附着请求，系统会采取下一种抑制措施，无下一种抑制措施时，继续使用当前抑制措施进行抑制。抑制时长由命令[**SET S1SMARTPARA**](../S1模式信令抑制参数管理/设置S1模式信令抑制参数(SET S1SMARTPARA)_72225427.md)中“附着异常抑制时长(分钟)”参数设置。<br>- 选择“Parking APN激活”的抑制措施时，需要通过[**SET S1SMARTPARA**](../S1模式信令抑制参数管理/设置S1模式信令抑制参数(SET S1SMARTPARA)_72225427.md)中“Parking APN”参数设置Parking APN， 同时在本地DNS或DNS服务器上配置Parking APN域名记录，另外S-GW/P-GW上也要配置并启用Parking APN功能。 |
| ATTACHREJCAUSE | 附着拒绝原因 | 可选必选说明：可选参数<br>参数含义：该参数用于设置当采取特定原因拒绝的抑制措施时，系统给终端发送的附着拒绝消息中携带的协议原因值。<br>数据来源：整网规划<br>取值范围：<br>- “IMSI_UNKNOWN_IN_HSS(IMSI_UNKNOWN_IN_HSS_2)”<br>- “ILLEGAL_UE(ILLEGAL_UE_3)”<br>- “ILLEGAL_ME(ILLEGAL_ME_6)”<br>- “EPS_SERVICE_NOT_ALLOWED(EPS_SERVICE_NOT_ALLOWED_7)”<br>- “EPS_NONEPS_SRV_NOT_ALLOWED(EPS_NONEPS_SRV_NOT_ALLOWED_8)”<br>- “IMPLICITLY_DETACHED(IMPLICITLY_DETACHED_10)”<br>- “PLMN_NOT_ALLOWED(PLMN_NOT_ALLOWED_11)”<br>- “TA_NOT_ALLOWED(TA_NOT_ALLOWED_12)”<br>- “ROAMING_NOT_ALLOWED_IN_TA(ROAMING_NOT_ALLOWED_IN_TA_13)”<br>- “EPS_SRV_NOT_ALLOWED_IN_PLMN(EPS_SRV_NOT_ALLOWED_IN_PLMN_14)”<br>- “NO_SUITABLE_CELLS_IN_TA(NO_SUITABLE_CELLS_IN_TA_15)”<br>- “CONGESTION(CONGESTION_22)”<br>- “PROTOCOL_ERROR_UNSPEC(PROTOCOL_ERROR_UNSPEC_111)”<br>默认值：无<br>说明：- 拒绝原因对终端行为的影响请参考[表1](#ZH-CN_MMLREF_0000001172225425__tab1)，详细内容参见协议3GPP TS 24.301-5.5.1.2.5 Attach not accepted by the network章节描述。具体终端的响应行为可能会随终端品牌和型号有所不同。 |
| SRVREQCTRLRULE | 服务请求抑制措施 | 可选必选说明：可选参数<br>参数含义：该参数用于设置当系统检测到终端发起的服务请求行为异常后采取的抑制措施。<br>数据来源：整网规划<br>取值范围：<br>- “SPECCAUSEREJ(特定原因拒绝)”<br>- “CNDETACH(网络侧分离)”<br>默认值：无<br>配置原则：由于不同类型终端的行为有差异，需要结合终端行为选择一种或多种抑制措施。<br>说明：- 抑制措施说明- 特定原因拒绝:当系统检测到终端的服务请求行为异常后，给终端发送服务请求拒绝消息，携带配置的协议原因值。<br>- 网络侧分离：当系统检测到终端的服务请求行为异常后，给终端发送分离请求消息，其中分离类型为“re-attach not required”。系统采取网络侧分离的抑制措施后，若附着流程配置了丢弃的抑制措施，在[**SET S1SMARTPARA**](../S1模式信令抑制参数管理/设置S1模式信令抑制参数(SET S1SMARTPARA)_72225427.md)中“附着异常抑制时长(分钟) ”参数设置的抑制时间内，终端的附着请求消息会被丢弃。抑制措施的优先级由高到低依次为：特定原因拒绝、网络侧分离。<br>- 1小时内，终端发起的服务请求次数到达预设阈值后，可判断为异常行为，采取配置的第一种抑制措施进行抑制。阈值由命令[**SET S1SMARTPARA**](../S1模式信令抑制参数管理/设置S1模式信令抑制参数(SET S1SMARTPARA)_72225427.md)中“服务请求异常识别门限(次/小时)”参数设置。<br>- 已经被抑制的终端，如果在抑制时间内再发起一次服务请求，系统会采取下一种抑制措施，无下一种抑制措施时，继续使用当前抑制措施进行抑制。抑制时长由命令[**SET S1SMARTPARA**](../S1模式信令抑制参数管理/设置S1模式信令抑制参数(SET S1SMARTPARA)_72225427.md)中“服务请求异常抑制时长(分钟)”参数设置。 |
| SRVREJCAUSE | 服务请求拒绝原因 | 可选必选说明：可选参数<br>参数含义：该参数用于设置当采取特定原因拒绝的抑制措施时，系统给终端发送的服务请求拒绝消息中携带的协议原因值。<br>数据来源：整网规划<br>取值范围：<br>- “IMSI_UNKNOWN_IN_HSS(IMSI_UNKNOWN_IN_HSS_2)”<br>- “ILLEGAL_UE(ILLEGAL_UE_3)”<br>- “ILLEGAL_ME(ILLEGAL_ME_6)”<br>- “EPS_SERVICE_NOT_ALLOWED(EPS_SERVICE_NOT_ALLOWED_7)”<br>- “EPS_NONEPS_SRV_NOT_ALLOWED(EPS_NONEPS_SRV_NOT_ALLOWED_8)”<br>- “IMPLICITLY_DETACHED(IMPLICITLY_DETACHED_10)”<br>- “PLMN_NOT_ALLOWED(PLMN_NOT_ALLOWED_11)”<br>- “TA_NOT_ALLOWED(TA_NOT_ALLOWED_12)”<br>- “ROAMING_NOT_ALLOWED_IN_TA(ROAMING_NOT_ALLOWED_IN_TA_13)”<br>- “EPS_SRV_NOT_ALLOWED_IN_PLMN(EPS_SRV_NOT_ALLOWED_IN_PLMN_14)”<br>- “NO_SUITABLE_CELLS_IN_TA(NO_SUITABLE_CELLS_IN_TA_15)”<br>- “CONGESTION(CONGESTION_22)”<br>- “PROTOCOL_ERROR_UNSPEC(PROTOCOL_ERROR_UNSPEC_111)”<br>默认值：无<br>说明：- 拒绝原因对终端行为的影响请参考[表1](#ZH-CN_MMLREF_0000001172225425__tab1)，详细内容参见协议3GPP TS 24.301-5.6.1.5 Service request procedure not accepted by the network章节描述。具体终端的响应行为可能会随终端品牌和型号有所不同。 |
| CPSRVREQCTRLRULE | 控制面服务请求抑制措施 | 可选必选说明：可选参数<br>参数含义：该参数用于设置当系统检测到终端发起的控制面服务请求(CPSR)行为异常后采取的抑制措施。<br>数据来源：全网规划<br>取值范围：<br>- “SPECCAUSEREJ(特定原因拒绝)”<br>- “CNDETACH(网络侧分离)”<br>默认值：无<br>配置原则：由于不同类型终端的行为有差异，需要结合终端行为选择一种或多种抑制措施。<br>说明：- 抑制措施说明- 特定原因拒绝：当系统检测到终端的控制面服务请求行为异常后，给终端发送控制面服务请求拒绝消息，携带配置的协议原因值。<br>- 网络侧分离：当系统检测到终端的控制面服务请求行为异常后，给终端发送分离请求消息，其中分离类型为“re-attach not required”。系统采取网络侧分离的抑制措施后，若附着流程配置了丢弃的抑制措施，在[**SET S1SMARTPARA**](../S1模式信令抑制参数管理/设置S1模式信令抑制参数(SET S1SMARTPARA)_72225427.md)中“附着异常抑制时长(分钟) ”参数设置的抑制时间内，终端的附着请求消息会被丢弃。抑制措施的优先级由高到低依次为：特定原因拒绝、网络侧分离。<br>- 一个测量周期内，终端发起的控制面服务请求次数到达预设阈值后，可判断为异常行为，采取配置的第一种抑制措施进行抑制。阈值由命令[**SET S1SMARTPARA**](../S1模式信令抑制参数管理/设置S1模式信令抑制参数(SET S1SMARTPARA)_72225427.md)中“控制面服务请求异常识别门限(次/小时)”和“控制面服务请求异常测量周期(秒)”参数设置。<br>- 已经被抑制的终端，如果在抑制时间内再发起一次控制面服务请求，系统会采取下一种抑制措施，无下一种抑制措施时，继续使用当前抑制措施进行抑制。抑制时长由命令[**SET S1SMARTPARA**](../S1模式信令抑制参数管理/设置S1模式信令抑制参数(SET S1SMARTPARA)_72225427.md)中“控制面服务请求异常抑制时长(分钟)”参数设置。 |
| CPSRVREJCAUSE | 控制面服务请求拒绝原因 | 可选必选说明：可选参数<br>参数含义：该参数用于设置当采取特定原因拒绝的抑制措施时，系统给终端发送的控制面服务请求拒绝消息中携带的协议原因值。<br>数据来源：全网规划<br>取值范围：<br>- “IMSI_UNKNOWN_IN_HSS(IMSI_UNKNOWN_IN_HSS_2)”<br>- “ILLEGAL_UE(ILLEGAL_UE_3)”<br>- “ILLEGAL_ME(ILLEGAL_ME_6)”<br>- “EPS_SERVICE_NOT_ALLOWED(EPS_SERVICE_NOT_ALLOWED_7)”<br>- “EPS_NONEPS_SRV_NOT_ALLOWED(EPS_NONEPS_SRV_NOT_ALLOWED_8)”<br>- “IMPLICITLY_DETACHED(IMPLICITLY_DETACHED_10)”<br>- “PLMN_NOT_ALLOWED(PLMN_NOT_ALLOWED_11)”<br>- “TA_NOT_ALLOWED(TA_NOT_ALLOWED_12)”<br>- “ROAMING_NOT_ALLOWED_IN_TA(ROAMING_NOT_ALLOWED_IN_TA_13)”<br>- “EPS_SRV_NOT_ALLOWED_IN_PLMN(EPS_SRV_NOT_ALLOWED_IN_PLMN_14)”<br>- “NO_SUITABLE_CELLS_IN_TA(NO_SUITABLE_CELLS_IN_TA_15)”<br>- “CONGESTION(CONGESTION_22)”<br>- “PROTOCOL_ERROR_UNSPEC(PROTOCOL_ERROR_UNSPEC_111)”<br>默认值：无 |
| PDNCONNCTRLRULE | PDN连接抑制措施 | 可选必选说明：可选参数<br>参数含义：该参数用于设置当系统检测到终端发起的PDN连接建立行为异常后采取的抑制措施。<br>数据来源：整网规划<br>取值范围：<br>- “SPECCAUSEREJ(特定原因拒绝)”<br>- “PARKAPNACT(Parking APN激活)”<br>- “CNDETACH(网络侧分离)”<br>默认值：无<br>配置原则：由于不同类型终端的行为有差异，需要结合终端行为选择一种或多种抑制措施。<br>说明：- 抑制措施说明- 特定原因拒绝:当系统检测到终端的PDN连接建立行为异常后，给终端发送PDN连接拒绝消息，携带配置的协议原因值。<br>- Parking APN激活：当系统检测到终端的PDN连接建立行为异常后，使用配置的Parking APN建立一个假承载。<br>- 网络侧分离：当系统检测到终端的PDN连接建立行为异常后，给终端发送分离请求消息，其中分离类型为“re-attach not required”。这种抑制方式对其他PDN连接有影响，不建议使用。系统采取网络侧分离的抑制措施后，若附着流程配置了丢弃的抑制措施，在[**SET S1SMARTPARA**](../S1模式信令抑制参数管理/设置S1模式信令抑制参数(SET S1SMARTPARA)_72225427.md)中“附着异常抑制时长(分钟) ”参数设置的抑制时间内，终端的附着请求消息会被丢弃。抑制措施的优先级由高到低依次为：特定原因拒绝、Parking APN激活、网络侧分离。<br>- 系统以APN为粒度统计终端发起的PDN连接建立请求次数，1小时内，终端发起的PDN连接建立次数到达预设阈值后，可判断是异常行为，采取配置的第一种抑制措施进行抑制。阈值由命令[**SET S1SMARTPARA**](../S1模式信令抑制参数管理/设置S1模式信令抑制参数(SET S1SMARTPARA)_72225427.md)中“PDN连接异常识别门限(次/小时)”参数设置。<br>- 已经被抑制的终端，如果在抑制时间内再发起1次PDN连接请求，系统会采取下一种抑制措施，无下一种抑制措施时，继续使用当前抑制措施进行抑制。抑制时长由命令[**SET S1SMARTPARA**](../S1模式信令抑制参数管理/设置S1模式信令抑制参数(SET S1SMARTPARA)_72225427.md)中“PDN连接异常抑制时长(分钟)”参数设置。<br>- 选择“Parking APN激活”的抑制措施时，需要通过[**SET S1SMARTPARA**](../S1模式信令抑制参数管理/设置S1模式信令抑制参数(SET S1SMARTPARA)_72225427.md)中“Parking APN”参数设置Parking APN， 同时在本地DNS或DNS服务器上配置Parking APN域名记录，另外S-GW/P-GW上也要配置并启用Parking APN功能。 |
| PDNCONNREJCAUSE | PDN连接拒绝原因 | 可选必选说明：可选参数<br>参数含义：该参数用于设置当采取特定原因拒绝的抑制措施时，系统给终端发送的PDN连接拒绝消息中携带的协议原因值。<br>数据来源：整网规划<br>取值范围：<br>- “ODB(ODB_8)”<br>- “INSUFFICIENT_RESOURCES(INSUFFICIENT_RESOURCES_26)”<br>- “UNKNOWN_OR_MISSING_APN(UNKNOWN_OR_MISSING_APN_27)”<br>- “USER_AUTH_FAILED(USER_AUTH_FAILED_29)”<br>- “REQUEST_REJECT_BY_SGW_OR_PGW(REQUEST_REJECT_BY_SGW_OR_PGW_30)”<br>- “SERVICE_OPTION_NOT_SUPPORTED(SERVICE_OPTION_NOT_SUPPORTED_32)”<br>- “REQUEST_SERVICE_NOT_SUBCRIBED(REQUEST_SERVICE_OPTION_NOT_SUBCRIBED_33)”<br>- “NETWORK_FAILURE(NETWORK_FAILURE_38)”<br>- “MULTI_PDN_FOR_APN_NOT_ALLOWED(MULTI_PDN_FOR_APN_NOT_ALLOWED_55)”<br>- “PROTOCOL_ERROR_UNSPECIFED(PROTOCOL_ERROR_UNSPECIFED_111)”<br>默认值：无<br>说明：- 拒绝原因对终端行为的影响请参见协议3GPP TS 24.301-6.5.1.4 UE requested PDN connectivity procedure not accepted by the network章节描述，具体终端的响应行为可能会随终端品牌和型号有所不同。 |
| BACKOFFSW | Backoff Timer分配开关 | 可选必选说明：可选参数<br>参数含义：该参数用于设置PDN连接拒绝消息中是否携带Backoff Timer信息。<br>数据来源：整网规划<br>取值范围：<br>- “OFF(关闭)”：当系统检测到终端的PDN连接建立行为异常后，给终端发送PDN连接拒绝消息，在消息中不携带Backoff Timer。<br>- “ON(开启)”：当系统检测到终端的PDN连接建立行为异常后，给终端发送PDN连接拒绝消息，在消息中携带Backoff Timer。<br>默认值：无<br>说明：- Backoff Timer为UE和网络启动的定时器，在该定时器时间内，UE不允许发起PDN连接流程。如果UE在定时器时间内仍然发起了PDN连接流程，系统会拒绝该流程。Backoff Timer的定义参考协议3GPP TS 24.008中关于GPRS timer 3的章节描述。<br>- Backoff Timer的取值范围为11~50分钟，每个用户的定时器时长有差异，便于将用户的重试分散开。 |
| MINBOT | Back off timer最小值（秒） | 可选必选说明：条件可选参数<br>参数含义：本参数用于设置Back off timer的最大值，用于计算发给终端的附着拒绝消息中的Back off timer时长。<br>前提条件：该参数在<br>“Backoff Timer分配开关”<br>参数配置为<br>“ON(开)”<br>后生效。<br>数据来源：本端规划<br>取值范围：1～1116000<br>默认值：无 |
| MAXBOT | Back off timer最大值（秒） | 可选必选说明：条件可选参数<br>参数含义：本参数用于设置Back off timer的最大值，用于计算发给终端的附着拒绝消息中的Back off timer时长。<br>前提条件：该参数在<br>“Backoff Timer分配开关”<br>参数配置为<br>“ON(开)”<br>后生效。<br>数据来源：本端规划<br>取值范围：1～1116000<br>默认值：无<br>配置原则：该参数的取值必须大于等于<br>“Back off timer最小值”<br>的取值。 |
| DETACHCAUSE | 抑制分离原因 | 可选必选说明：可选参数<br>参数含义：该参数用于设置网络侧发起的分离请求消息中携带的协议原因值。当系统检测到终端的服务请求或PDN连接建立行为异常， 并且采取网络侧分离的抑制措施时，给终端发送的分离请求消息（分离类型为“re-attach not required”）中携带此原因值。<br>数据来源：整网规划<br>取值范围：<br>- “IMSI_UNKNOWN_IN_HSS(IMSI_UNKNOWN_IN_HSS_2)”<br>- “ILLEGAL_UE(ILLEGAL_UE_3)”<br>- “ILLEGAL_ME(ILLEGAL_ME_6)”<br>- “EPS_SERVICE_NOT_ALLOWED(EPS_SERVICE_NOT_ALLOWED_7)”<br>- “EPS_NONEPS_SRV_NOT_ALLOWED(EPS_NONEPS_SRV_NOT_ALLOWED_8)”<br>- “IMPLICITLY_DETACHED(IMPLICITLY_DETACHED_10)”<br>- “PLMN_NOT_ALLOWED(PLMN_NOT_ALLOWED_11)”<br>- “TA_NOT_ALLOWED(TA_NOT_ALLOWED_12)”<br>- “ROAMING_NOT_ALLOWED_IN_TA(ROAMING_NOT_ALLOWED_IN_TA_13)”<br>- “EPS_SRV_NOT_ALLOWED_IN_PLMN(EPS_SRV_NOT_ALLOWED_IN_PLMN_14)”<br>- “NO_SUITABLE_CELLS_IN_TA(NO_SUITABLE_CELLS_IN_TA_15)”<br>- “CONGESTION(CONGESTION_22)”<br>- “PROTOCOL_ERROR_UNSPEC(PROTOCOL_ERROR_UNSPEC_111)”<br>默认值：无<br>说明：由于不同类型终端的行为可能有差异，需要结合终端行为来选择分离原因，分离原因对终端行为的影响请参考<br>[表1](#ZH-CN_MMLREF_0000001172225425__tab1)<br>，详细内容参见协议3GPP TS 24.301-5.5.2.3 Network initiated detach procedure章节描述。 |
| PARKAPNWAKEUPRULE | Parking APN唤醒措施 | 可选必选说明：可选参数<br>参数含义：该参数用于设置当对用户进行Parking APN激活抑制的时间超时后，系统通知用户重新接入业务的方式。<br>数据来源：整网规划<br>取值范围：<br>- “CNDEACT(网络侧去激活)”：系统发起网络侧去激活流程，去激活Parking APN建立的承载，去激活请求消息中携带原因值为“reactivation requested”（软参DWORD_EX12 BIT30设为1）或者“regular deactivation”（软参DWORD_EX12 BIT30设为0）。<br>- “CNDETACH(网络侧分离)”：系统发起网络侧分离流程，分离类型为“re-attach required”。<br>默认值：无<br>说明：- 附着流程和PDN连接建立流程中都可能使用Parking APN建立承载。<br>- 系统唤醒附着流程中使用Parking APN建立的缺省承载时，同时唤醒用户所有使用Parking APN建立的承载。<br>- 系统唤醒PDN连接流程中使用Parking APN建立的承载时，将同一APN粒度并且使用Parking APN建立的承载全部唤醒。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/S1SMARTRULE]] · S1模式信令抑制规则（S1SMARTRULE）

## 使用实例

运营商A在配置ANDROID类型终端的服务请求和PDN连接流程的抑制措施时选择了网络侧分离的抑制措施，由于网络侧分离可能对语音业务或其他正常PDN连接有影响，因此关闭服务请求流程和PDN连接流程的“网络侧分离”抑制措施，同时由于ANDROID类型终端支持Backoff Timer，开启“Backoff Timer分配开关”：

MOD S1SMARTRULE: UETYPE=ANDROID, SRVREQCTRLRULE=CNDETACH-0, PDNCONNCTRLRULE=CNDETACH-0, BACKOFFSW=ON;

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改S1模式信令抑制规则(MOD-S1SMARTRULE)_72225425.md`
