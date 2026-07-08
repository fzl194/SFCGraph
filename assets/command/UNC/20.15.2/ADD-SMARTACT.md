---
id: UNC@20.15.2@MMLCommand@ADD SMARTACT
type: MMLCommand
name: ADD SMARTACT（增加激活抑制规则）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: SMARTACT
command_category: 配置类
applicable_nf:
- SGSN
effect_mode: 立即生效
is_dangerous: false
max_records: 17
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 业务安全管理
- Smartphone管理
- 异常信令节省
- 激活抑制规则管理
status: active
---

# ADD SMARTACT（增加激活抑制规则）

## 功能

**适用网元：SGSN**

此命令用于添加基于用户终端类型的激活抑制规则。用户激活异常时，按照配置的激活抑制规则对其进行抑制。

当需要对频繁激活的用户进行信令抑制，减少SGSN信令负载时，需要执行此命令。

## 注意事项

- 此命令最大记录数为17条（每种终端类型最多1条）。
- 此命令执行后立即生效。
- 此特性为可选特性，需要加载支持该特性的License，对应的License项为“Smartphone异常信令节省”。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| UETYPE | 终端类型 | 可选必选说明：必选参数<br>参数含义：该参数用于设置用户的终端类型。<br>数据来源：本端规划<br>取值范围：<br>- “ANDROID(Android)”<br>- “BLACKBERRY(Black Berry)”<br>- “IOS(iOS)”<br>- “WINDOWS(Windows)”<br>- “CUSTOM_TYPE_1(自定义类型1)”<br>- “CUSTOM_TYPE_2(自定义类型2)”<br>- “CUSTOM_TYPE_3(自定义类型3)”<br>- “CUSTOM_TYPE_4(自定义类型4)”<br>- “CUSTOM_TYPE_5(自定义类型5)”<br>- “CUSTOM_TYPE_6(自定义类型6)”<br>- “CUSTOM_TYPE_7(自定义类型7)”<br>- “CUSTOM_TYPE_8(自定义类型8)”<br>- “CUSTOM_TYPE_9(自定义类型9)”<br>- “CUSTOM_TYPE_10(自定义类型10)”<br>- “CUSTOM_TYPE_11(自定义类型11)”<br>- “CUSTOM_TYPE_12(自定义类型12)”<br>- “UNKNOWN_TYPE(未知类型)”<br>默认值：无<br>说明：“UNKNOWN_TYPE(未知类型)”<br>是指没有对应的IMEILIB或APNNILIB配置的终端类型。除<br>“UNKNOWN_TYPE(未知类型)”<br>以外的终端类型，可通过<br>[**ADD IMEILIB**](../../终端类型识别/IMEI库管理/增加IMEI库记录（ADD IMEILIB）_26145734.md)<br>或<br>[**ADD APNNILIB**](../../终端类型识别/APNNI库管理/增加APNNI库记录（ADD APNNILIB）_26145736.md)<br>命令设置。 |
| SPECCAUSESW | 特定原因值拒绝激活功能开关 | 可选必选说明：可选参数<br>参数含义：该参数用于设置特定原因值拒绝激活功能开关，控制是否开启特定原因值拒绝激活功能。<br>数据来源：本端规划<br>取值范围：<br>- “OFF(关闭)”<br>- “ON(开启)”<br>默认值：无<br>配置原则：建议值为<br>“OFF(关闭)”<br>。 |
| BACKOFFSW | Backoff Timer分配开关 | 可选必选说明：可选参数<br>参数含义：该参数用于设置<br>“Backoff Timer分配开关”<br>。<br>数据来源：整网规划<br>取值范围：<br>- “OFF(关闭)”<br>- “ON(开启)”<br>默认值 ：无<br>配置原则：<br>- 当SGSN收到的异常终端的PDP激活次数达到[**SET SMARTACTPARA**](../激活抑制参数管理/设置激活抑制参数（SET SMARTACTPARA）_26305550.md)命令中的“识别异常激活行为的门限(times/h)”，该开关生效。<br>- 当该开关开启时，SGSN收到异常终端的PDP激活消息后，在PDP激活拒绝消息中分配Backoff Timer。Backoff Timer为UE和网络启动的定时器，在该定时器时间内，UE不允许发起PDP激活流程。如果UE在定时器时间内仍然发起了PDP激活流程，SGSN会拒绝该流程。<br>- 当该开关关闭时，SGSN收到异常终端的PDP激活消息后，在PDP激活拒绝消息中不分配Backoff Timer。<br>说明：- Backoff Timer的取值范围为11~50分钟，每个用户的定时器时长有差异，便于将用户的重试分散开。 |
| MINBOT | Back off timer最小值（秒） | 可选必选说明：条件可选参数<br>参数含义：本参数用于设置Back off timer的最小值，用于计算发给终端的附着拒绝消息中的Back off timer时长。<br>前提条件：该参数在<br>“Backoff Timer分配开关”<br>参数配置为<br>“ON(开)”<br>后生效。<br>数据来源：本端规划<br>取值范围：1～1116000<br>默认值：660 |
| MAXBOT | Back off timer最大值（秒） | 可选必选说明：条件可选参数<br>参数含义：本参数用于设置Back off timer的最大值，用于计算发给终端的附着拒绝消息中的Back off timer时长。<br>前提条件：该参数在<br>“Backoff Timer分配开关”<br>参数配置为<br>“ON(开)”<br>后生效。<br>数据来源：本端规划<br>取值范围：1～1116000<br>默认值：3000<br>配置原则：该参数的取值必须大于等于<br>“Back off timer最小值”<br>的取值。 |
| PARKINGAPNSW | Parking APN假激活功能开关 | 可选必选说明：可选参数<br>参数含义：该参数用于设置Parking APN假激活功能的开关，控制是否开启Parking APN假激活功能。<br>数据来源：本端规划<br>取值范围：<br>- “OFF(关闭)”<br>- “ON(开启)”<br>默认值：无<br>配置原则：建议值为<br>“OFF(关闭)”<br>。 |
| DETACHSW | 主动分离用户功能开关 | 可选必选说明：可选参数<br>参数含义：该参数用于设置主动分离用户功能开关，控制是否开启主动分离用户功能。<br>数据来源：本端规划<br>取值范围：<br>- “OFF(关闭)”<br>- “ON(开启)”<br>默认值：无<br>配置原则：建议值为<br>“OFF(关闭)”<br>。 |
| SMARTACTREJCAUSE | 激活拒绝原因值 | 可选必选说明：可选参数<br>参数含义：该参数用于设置激活拒绝原因值。<br>数据来源：本端规划<br>取值范围：<br>- “OPERATOR_DETERMINED_BARRING_8(Operator determined barring 8)”<br>- “INSUFFICIENT_RESOURCES_26(Insufficient resources 26)”<br>- “MISSING_OR_UNKNOWN_APN_27(Missing or unknown APN 27)”<br>- “UNKNOWN_PDP_ADDR_OR_TYPE_28(Unknown PDP address or PDP type 28)”<br>- “USER_AUTHENTICATION_FAILED_29(User authentication failed 29)”<br>- “ACTIVATION_REJECTED_BY_GGSN_30(Activation rejected by GGSN 30)”<br>- “ACTIVATION_REJECTED_31(Activation rejected, unspecified 31)”<br>- “SERVICE_OPT_NOT_SUPPORTED_32(Service option not supported 32)”<br>- “REQ_SERV_OPTION_NOT_SUB_33(Requested service option not subscribed 33)”<br>- “NETWORK_FAILURE_38(Network failure 38)”<br>- “INVALID_MANDATORY_INFO_96(Invalid mandatory information 96)”<br>- “PROTOCOL_ERROR_UNSPECIFIED_111(Protocol error, unspecified 111)”<br>默认值：<br>“REQ_SERV_OPTION_NOT_SUB_33(Requested service option not subscribed 33)”<br>说明：当<br>“特定原因值拒绝激活功能开关”<br>为<br>“ON(开启)”<br>时此参数才生效。 |
| SMARTDETACHCAUSE | 分离原因值 | 可选必选说明：可选参数<br>参数含义：该参数用于设置分离原因值。<br>数据来源：本端规划<br>取值范围：<br>- “NO_CAUSE_0(No Cause 0)”<br>- “GPRS_SERVICES_NOT_ALLOWED_7(GPRS services not allowed 7)”<br>- “PLMN_NOT_ALLOWED_11(PLMN not allowed 11)”<br>- “GPRS_SERV_NOT_ALLOW_PLMN_14(GPRS services not allowed in this PLMN 14)”<br>- “PROTOCOL_ERROR_UNSPECIFIED_111(Protocol error, unspecified 111)”<br>默认值：<br>“GPRS_SERVICES_NOT_ALLOWED_7(GPRS services not allowed 7)”<br>说明：当<br>“主动分离用户功能开关”<br>为<br>“ON(开启)”<br>时此参数生效。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@SMARTACT]] · 激活抑制规则（SMARTACT）

## 使用实例

增加终端类型为IOS用户的激活抑制规则： “特定原因值拒绝激活功能开关” 设置为 “OFF（关闭）” ， “Parking APN假激活功能开关” 设置为 “ON（开启）” 。

ADD SMARTACT: UETYPE=IOS, SPECCAUSESW=OFF, PARKINGAPNSW=ON;

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-SMARTACT.md`
