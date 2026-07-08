---
id: UDG@20.15.2@MMLCommand@SET HTTPFIXEDFCMSG
type: MMLCommand
name: SET HTTPFIXEDFCMSG（设置HTTP指定消息类型固定速率流控信息）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: HTTPFIXEDFCMSG
command_category: 配置类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- HTTP功能管理
- HTTP流控管理
- HTTP指定消息类型固定速率流控管理
status: active
---

# SET HTTPFIXEDFCMSG（设置HTTP指定消息类型固定速率流控信息）

## 功能

![](设置HTTP指定消息类型固定速率流控信息（SET HTTPFIXEDFCMSG）_84132110.assets/notice_3.0-zh-cn.png)

流控阈值设置过低可能会导致流程失败，设置过高可能导致系统不能对消息进行合理流控。

该命令用于设置指定消息类型的固定速率门限，减少其它网元对本网元的冲击，以及本网元对其它网元的冲击。

> **说明**
> - 该命令执行后立即生效。
>
> - 该命令针对NSMSF_SMSERVICESERVICEAPI_SENDSMS消息类型的配置，实际流控功能不起作用。
> - 当业务pod或sbim-pod进行扩容或缩容操作时，需要评估此阈值是否需要刷新。
>
> - 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：
>
> > **说明**
> > 此处仅展示前20条初始记录值，您可以通过相关查询命令查看全部记录值。
>
> | MSGTYPE | FCSWITCH | THRESHOLD |
> | --- | --- | --- |
> | NSMF_PDUSESSION_SMCONTEXTSCREATE | ON | 1200 |
> | NSMF_PDUSESSION_RETRIEVESMCONTEXT | ON | 1200 |
> | NNRF_NFMANAGEMENTSERVICE_NFSTATUSEVENTNOTIFY | OFF | 0 |
> | NAMF_COMMUNICATION_UECONTEXTTRANSFER | ON | 4000 |
> | NNRF_NFDISCOVERYSERVICE_SEARCHNFINSTANCES | OFF | 0 |
> | NNRF_NFMANAGEMENTSERVICE_REGISTERNFINSTANCE | OFF | 0 |
> | NNRF_NFMANAGEMENTSERVICE_GETNFINSTANCES | OFF | 0 |
> | NNRF_NFMANAGEMENTSERVICE_GETNFINSTANCE | OFF | 0 |
> | NNRF_NFMANAGEMENTSERVICE_CREATESUBSCRIPTION | OFF | 0 |
> | NNRF_NFMANAGEMENTSERVICE_UPDATESUBSCRIPTION | OFF | 0 |
> | NNSSF_NSSELECTION_NSSELECTIONGET | OFF | 0 |
> | NNSSF_NSSAIAVAILABILITY_NSSAIAVAILABILITYPATCH | OFF | 0 |
> | NNSSF_NSSAIAVAILABILITY_NSSAIAVAILABILITYPUT | OFF | 0 |
> | NNSSF_NSSAIAVAILABILITY_NSSAIAVAILABILITYPOST | OFF | 0 |
> | NSMSF_SMSERVICESERVICEAPI_SMSERVICEACTIVATION | OFF | 0 |
> | NSMSF_SMSERVICESERVICEAPI_SENDSMS | OFF | 0 |
> | NCHF_CONVERGEDCHARGING_CHARGINGDATACREATE | OFF | 0 |
> | NCHF_CONVERGEDCHARGING_CHARGINGDATAREFCREATE | OFF | 0 |
> | NNWDAF_EVENTSSUBSCRIPTION_SUBSCRIBE | ON | 2000 |
> | NUPF_EVENTEXPOSURE_NOTIFY | OFF | 0 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MSGTYPE | 流控消息类型 | 可选必选说明：必选参数<br>参数含义：该参数用于设置HTTP接口被流控的消息类型。<br>数据来源：全网规划<br>取值范围：<br>- “NSMF_PDUSESSION_SMCONTEXTSCREATE（Nsmf_PDUSession_SmContextsCreate消息）”：SMF收到的AMF发出的Nsmf_PDUSession_SmContextsCreate消息需要被流控。<br>- “NSMF_PDUSESSION_RETRIEVESMCONTEXT（Nsmf_PDUSession_RetrieveSmContext消息）”：SMF收到的AMF发出的Nsmf_PDUSession_RetrieveSmContext消息需要被流控。<br>- “NNRF_NFMANAGEMENTSERVICE_NFSTATUSEVENTNOTIFY（Nnrf_NFManagementService_NFStatusEventNotify消息）”：NF收到的Nnrf_NFManagementService_NFStatusEventNotify消息需要被流控。<br>- “NAMF_COMMUNICATION_UECONTEXTTRANSFER（Namf_Communication_UEContextTransfer消息）”：AMF收到的Namf_Communication_UEContextTransfer消息需要被流控。<br>- “NNRF_NFDISCOVERYSERVICE_SEARCHNFINSTANCES（Nnrf_NFDiscoveryService_SearchNFInstances消息）”：NRF收到的Nnrf_NFDiscoveryService_SearchNFInstances消息需要被流控。<br>- “NNRF_NFMANAGEMENTSERVICE_REGISTERNFINSTANCE（Nnrf_NFManagementService_RegisterNFInstance消息）”：NRF收到的Nnrf_NFManagementService_RegisterNFInstance消息需要被流控。<br>- “NNRF_NFMANAGEMENTSERVICE_GETNFINSTANCES（Nnrf_NFManagementService_GetNFInstances消息）”：NRF收到的Nnrf_NFManagementService_GetNFInstances消息需要被流控。<br>- “NNRF_NFMANAGEMENTSERVICE_GETNFINSTANCE（Nnrf_NFManagementService_GetNFInstance消息）”：NRF收到的Nnrf_NFManagementService_GetNFInstance消息需要被流控。<br>- “NNRF_NFMANAGEMENTSERVICE_CREATESUBSCRIPTION（Nnrf_NFManagementService_CreateSubscription消息）”：NRF收到的Nnrf_NFManagementService_CreateSubscription消息需要被流控。<br>- “NNRF_NFMANAGEMENTSERVICE_UPDATESUBSCRIPTION（Nnrf_NFManagementService_UpdateSubscription消息）”：NRF收到的Nnrf_NFManagementService_UpdateSubscription消息需要被流控。<br>- “NNSSF_NSSELECTION_NSSELECTIONGET（Nnssf_NSSelection_NSSelectionGet消息）”：NSSF收到的Nnssf_NSSelection_NSSelectionGet消息需要被流控。<br>- “NNSSF_NSSAIAVAILABILITY_NSSAIAVAILABILITYPATCH（Nnssf_NSSAIAvailability_NSSAIAvailabilityPatch消息）”：NSSF收到的Nnssf_NSSAIAvailability_NSSAIAvailabilityPatch消息需要被流控。<br>- “NNSSF_NSSAIAVAILABILITY_NSSAIAVAILABILITYPUT（Nnssf_NSSAIAvailability_NSSAIAvailabilityPut消息）”：NRF收到的Nnssf_NSSAIAvailability_NSSAIAvailabilityPut消息需要被流控。<br>- “NNSSF_NSSAIAVAILABILITY_NSSAIAVAILABILITYPOST（Nnssf_NSSAIAvailability_NSSAIAvailabilityPost消息）”：NSSF收到的Nnssf_NSSAIAvailability_NSSAIAvailabilityPost消息需要被流控。<br>- “NSMSF_SMSERVICESERVICEAPI_SMSERVICEACTIVATION（Nsmsf_SMServiceServiceAPI_SMServiceActivation消息）”：SMSF收到的Nsmsf_SMServiceServiceAPI_SMServiceActivation消息需要被流控。<br>- “NSMSF_SMSERVICESERVICEAPI_SENDSMS（Nsmsf_SMServiceServiceAPI_SendSMS消息）”：SMSF收到的Nsmsf_SMServiceServiceAPI_SendSMS消息需要被流控。<br>- “NCHF_CONVERGEDCHARGING_CHARGINGDATACREATE（Nchf_ConvergedCharging_ChargingDataCreate消息）”：CHF收到的Nchf_ConvergedCharging_ChargingDataCreate消息需要被流控。<br>- “NCHF_CONVERGEDCHARGING_CHARGINGDATAREFCREATE（Nchf_ConvergedCharging_ChargingDataRefCreate消息）”：CHF收到的Nchf_ConvergedCharging_ChargingDataRefCreate消息需要被流控。<br>- “NNWDAF_EVENTSSUBSCRIPTION_SUBSCRIBE（Nnwdaf_EventsSubscription_Subscribe消息）”：UDC收到的Nnwdaf_EventsSubscription_Subscribe消息需要被流控。<br>- “NUPF_EVENTEXPOSURE_NOTIFY（Nupf_EventExposure_Notify消息）”：UDC收到的Nupf_EventExposure_Notify消息需要被流控。<br>- “NSMF_EVENTEXPOSURE_NOTIFY（Nsmf_EventExposure_Notify消息）”：UDC收到的Nsmf_EventExposure_Notify消息需要被流控。<br>默认值：无。<br>配置原则：无 |
| FCSWITCH | 固定速率流控开关 | 可选必选说明：必选参数<br>参数含义：该参数用于控制HTTP接口指定消息类型固定速率流控功能。<br>数据来源：全网规划<br>取值范围：<br>- “ON（开启）”：开启HTTP接口的固定速率流控功能。<br>- “OFF（关闭）”：关闭HTTP接口的固定速率流控功能。<br>默认值：无。<br>配置原则：<br>当希望开启指定消息类型流控功能时，设置为"ON"；当希望关闭指定消息类型流控功能时，设置为"OFF"。 |
| THRESHOLD | 流控速率门限(个/秒) | 可选必选说明：该参数在"FCSWITCH"配置为"ON"时为条件可选参数。<br>参数含义：该参数用于设置HTTP接口指定消息的接收流控速率上限。<br>此阈值会均分到HTTP进程，单HTTP进程流控阈值计算公式为：单HTTP进程平均门限=消息所属业务Pod数*设置流控阈值/sbim-pod数/单sbim-pod内HTTP进程数并向上取整。<br>比如NSMF_PDUSESSION_SMCONTEXTSCREATE消息由vsm-pod处理，则单HTTP进程平均门限=vsm-pod数*设置流控阈值/sbim-pod数/单sbim-pod内HTTP进程数并向上取整。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~1000000，单位是个每秒。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST HTTPFIXEDFCMSG查询当前参数配置值。<br>配置原则：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@HTTPFIXEDFCMSG]] · HTTP指定消息类型固定速率流控信息（HTTPFIXEDFCMSG）

## 使用实例

针对的NSMF_PDUSESSION_SMCONTEXTSCREATE开启固定速率流控，速率门限是4000个/秒。执行如下命令:

```
SET HTTPFIXEDFCMSG: MSGTYPE=NSMF_PDUSESSION_SMCONTEXTSCREATE, FCSWITCH=ON, THRESHOLD=4000;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/SET-HTTPFIXEDFCMSG.md`
