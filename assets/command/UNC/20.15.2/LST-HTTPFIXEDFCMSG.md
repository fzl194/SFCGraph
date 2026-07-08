---
id: UNC@20.15.2@MMLCommand@LST HTTPFIXEDFCMSG
type: MMLCommand
name: LST HTTPFIXEDFCMSG（查询HTTP指定消息类型固定速率流控信息）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: HTTPFIXEDFCMSG
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- HTTP功能管理
- HTTP流控管理
- HTTP指定消息类型固定速率流控管理
status: active
---

# LST HTTPFIXEDFCMSG（查询HTTP指定消息类型固定速率流控信息）

## 功能

该命令用于查询指定消息类型的固定速率流控信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MSGTYPE | 流控消息类型 | 可选必选说明：可选参数<br>参数含义：该参数用于设置HTTP接口被流控的消息类型。<br>数据来源：全网规划<br>取值范围：<br>- “NSMF_PDUSESSION_SMCONTEXTSCREATE（Nsmf_PDUSession_SmContextsCreate消息）”：SMF收到的AMF发出的Nsmf_PDUSession_SmContextsCreate消息需要被流控。<br>- “NSMF_PDUSESSION_RETRIEVESMCONTEXT（Nsmf_PDUSession_RetrieveSmContext消息）”：SMF收到的AMF发出的Nsmf_PDUSession_RetrieveSmContext消息需要被流控。<br>- “NNRF_NFMANAGEMENTSERVICE_NFSTATUSEVENTNOTIFY（Nnrf_NFManagementService_NFStatusEventNotify消息）”：NF收到的Nnrf_NFManagementService_NFStatusEventNotify消息需要被流控。<br>- “NAMF_COMMUNICATION_UECONTEXTTRANSFER（Namf_Communication_UEContextTransfer消息）”：AMF收到的Namf_Communication_UEContextTransfer消息需要被流控。<br>- “NNRF_NFDISCOVERYSERVICE_SEARCHNFINSTANCES（Nnrf_NFDiscoveryService_SearchNFInstances消息）”：NRF收到的Nnrf_NFDiscoveryService_SearchNFInstances消息需要被流控。<br>- “NNRF_NFMANAGEMENTSERVICE_REGISTERNFINSTANCE（Nnrf_NFManagementService_RegisterNFInstance消息）”：NRF收到的Nnrf_NFManagementService_RegisterNFInstance消息需要被流控。<br>- “NNRF_NFMANAGEMENTSERVICE_GETNFINSTANCES（Nnrf_NFManagementService_GetNFInstances消息）”：NRF收到的Nnrf_NFManagementService_GetNFInstances消息需要被流控。<br>- “NNRF_NFMANAGEMENTSERVICE_GETNFINSTANCE（Nnrf_NFManagementService_GetNFInstance消息）”：NRF收到的Nnrf_NFManagementService_GetNFInstance消息需要被流控。<br>- “NNRF_NFMANAGEMENTSERVICE_CREATESUBSCRIPTION（Nnrf_NFManagementService_CreateSubscription消息）”：NRF收到的Nnrf_NFManagementService_CreateSubscription消息需要被流控。<br>- “NNRF_NFMANAGEMENTSERVICE_UPDATESUBSCRIPTION（Nnrf_NFManagementService_UpdateSubscription消息）”：NRF收到的Nnrf_NFManagementService_UpdateSubscription消息需要被流控。<br>- “NNSSF_NSSELECTION_NSSELECTIONGET（Nnssf_NSSelection_NSSelectionGet消息）”：NSSF收到的Nnssf_NSSelection_NSSelectionGet消息需要被流控。<br>- “NNSSF_NSSAIAVAILABILITY_NSSAIAVAILABILITYPATCH（Nnssf_NSSAIAvailability_NSSAIAvailabilityPatch消息）”：NSSF收到的Nnssf_NSSAIAvailability_NSSAIAvailabilityPatch消息需要被流控。<br>- “NNSSF_NSSAIAVAILABILITY_NSSAIAVAILABILITYPUT（Nnssf_NSSAIAvailability_NSSAIAvailabilityPut消息）”：NRF收到的Nnssf_NSSAIAvailability_NSSAIAvailabilityPut消息需要被流控。<br>- “NNSSF_NSSAIAVAILABILITY_NSSAIAVAILABILITYPOST（Nnssf_NSSAIAvailability_NSSAIAvailabilityPost消息）”：NSSF收到的Nnssf_NSSAIAvailability_NSSAIAvailabilityPost消息需要被流控。<br>- “NSMSF_SMSERVICESERVICEAPI_SMSERVICEACTIVATION（Nsmsf_SMServiceServiceAPI_SMServiceActivation消息）”：SMSF收到的Nsmsf_SMServiceServiceAPI_SMServiceActivation消息需要被流控。<br>- “NSMSF_SMSERVICESERVICEAPI_SENDSMS（Nsmsf_SMServiceServiceAPI_SendSMS消息）”：SMSF收到的Nsmsf_SMServiceServiceAPI_SendSMS消息需要被流控。<br>- “NCHF_CONVERGEDCHARGING_CHARGINGDATACREATE（Nchf_ConvergedCharging_ChargingDataCreate消息）”：CHF收到的Nchf_ConvergedCharging_ChargingDataCreate消息需要被流控。<br>- “NCHF_CONVERGEDCHARGING_CHARGINGDATAREFCREATE（Nchf_ConvergedCharging_ChargingDataRefCreate消息）”：CHF收到的Nchf_ConvergedCharging_ChargingDataRefCreate消息需要被流控。<br>- “NNWDAF_EVENTSSUBSCRIPTION_SUBSCRIBE（Nnwdaf_EventsSubscription_Subscribe消息）”：UDC收到的Nnwdaf_EventsSubscription_Subscribe消息需要被流控。<br>- “NUPF_EVENTEXPOSURE_NOTIFY（Nupf_EventExposure_Notify消息）”：UDC收到的Nupf_EventExposure_Notify消息需要被流控。<br>- “NSMF_EVENTEXPOSURE_NOTIFY（Nsmf_EventExposure_Notify消息）”：UDC收到的Nsmf_EventExposure_Notify消息需要被流控。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [HTTP指定消息类型固定速率流控信息（HTTPFIXEDFCMSG）](configobject/UNC/20.15.2/HTTPFIXEDFCMSG.md)

## 使用实例

查询所有流控消息类型流控信息，执行如下命令：

```
+++    UNC/*MEID:0 MENAME:APP-TESTsxAMF127BHW-01BHW011*/
O&M    #7016
%%LST HTTPFIXEDFCMSG: MSGTYPE=NSMF_PDUSESSION_SMCONTEXTSCREATE;%%
RETCODE = 0  操作成功

结果如下
--------
       流控消息类型  =  Nsmf_PDUSession_SmContextsCreate消息
   固定速率流控开关  =  开启
流控速率门限(个/秒)  =  1200
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询HTTP指定消息类型固定速率流控信息（LST-HTTPFIXEDFCMSG）_83972186.md`
