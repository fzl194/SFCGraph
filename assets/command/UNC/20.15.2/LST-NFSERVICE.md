---
id: UNC@20.15.2@MMLCommand@LST NFSERVICE
type: MMLCommand
name: LST NFSERVICE（查询NF服务实例）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NFSERVICE
command_category: 查询类
applicable_nf:
- AMF
- SMF
- NSSF
- NRF
- NCG
- SMSF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 服务化接口管理
- 注册与服务发现
- NF服务配置管理
status: active
---

# LST NFSERVICE（查询NF服务实例）

## 功能

**适用NF：AMF、SMF、NSSF、NRF、NCG、SMSF**

该命令用于查询NF实例下的NFS实例信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFINSTANCENAME | NF实例名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定NFS实例所归属的NF实例名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~50。<br>默认值：无<br>配置原则：<br>本参数来源于ADD NFUUID命令中的“NF实例名称”参数。 |
| SRVINSTANCEID | 服务实例标识 | 可选必选说明：可选参数<br>参数含义：本参数用于指定NFS实例标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~50。<br>默认值：无<br>配置原则：<br>本参数构成字符只能是字母A～Z或a～z、数字0～9、中划线“-”和下划线“_”，例如，Service_Instance_0。 |
| SERVICENAME | 服务名称 | 可选必选说明：可选参数<br>参数含义：本参数用于指定服务名称。<br>数据来源：全网规划<br>取值范围：<br>- SrvNameINVALID（Invalid Service Name）<br>- NrfNfm（NRF提供的Nnrf_NFManagement服务）<br>- NnrfDisc（NRF提供的Nnrf_NFDiscovery服务）<br>- NudmSdm（UDM提供的Nudm_SubscriberDataManagement服务）<br>- NudmUecm（UDM提供的Nudm_UEContextManagement服务）<br>- NudmUeau（UDM提供的Nudm_UEAuthentication服务）<br>- NudmEe（UDM提供的Nudm_EventExposure服务）<br>- NudmPp（UDM提供的Nudm_ParameterProvision服务）<br>- NamfComm（AMF提供的Namf_Communication Service服务）<br>- NamfEvts（AMF提供的Namf_EventExposure服务）<br>- NamfMt（AMF提供的Namf_MT服务）<br>- NamfLoc（AMF提供的Namf_Location服务）<br>- NsmfPduSes（SMF提供的Nsmf_PDUSession服务）<br>- NsmfEventExp（SMF提供的Nsmf_EventExposure服务）<br>- NausfAuth（AUSF提供的Nausf_UEAuthentication服务）<br>- NausfSorprot（AUSF提供的Nausf_SoRPProtection服务）<br>- NnefPfdMgnt（NEF提供的Nnef_PFDManagement）<br>- NpcfAmPlcCtrl（PCF提供的Npcf_AMPolicyControl服务）<br>- NpcfSmPlcCtrl（PCF提供的Npcf_SMPolicyControl服务）<br>- NpcfPlcauth（PCF提供的Npcf_PolicyAuthorization服务）<br>- NpcfBdtplcCtrl（PCF提供的Npcf_BDTPolicyControl服务）<br>- NpcfEventEx（PCF提供的Npcf_EventExposure服务）<br>- NpcfUePcy（PCF提供的Npcf_UEPolicyControl服务）<br>- NsmsfSms（SMSF提供的Nsmsf_SMService服务）<br>- NnssfNsSel（NSSF提供的Nnssf_NSSelection服务）<br>- NnssfNssaiAvai（NSSF提供的Nnssf_NSSAIAvailability服务）<br>- NudrDr（UDR提供的Nudr_DataRepository服务）<br>- NlmfLoc（LMF提供的Nlmf_Location服务）<br>- N5gEirEic（5G-EIR提供的N5g-eir_EquipmentIdentityCheck服务）<br>- NbsfMgmt（BSF提供的Nbsf_Management服务）<br>- NchfSpdlmtCtrl（CHF提供的Nchf_SpendingLimitControl服务）<br>- NchfConvCharg（CHF提供的Nchf_Converged_Charging服务）<br>- NnwdafEvntSubs（NWDAF提供的Nnwdaf_EventsSubscription服务）<br>- NnwdafAnalInfo（NWDAF提供的Nnwdaf_AnalyticsInfo服务）<br>- “SrvNameMAX（Max Service Name）”：已废弃。<br>- NamfMbsBroadcast（AMF提供的Namf_MbsBroadcast服务）<br>- NmbSmfTmgi（MBSMF提供的NmbSmf_Tmgi服务）<br>- NmbSmfMbssession（MBSMF提供的NmbSmf_Mbssession服务）<br>- Nnef3gppAsSessionWithQos（NEF提供的Nnef_3gppAsSessionWithQos服务）<br>- Nnef3gppMonEvent（NEF提供的Nnef_3gppMonEvent服务）<br>- NnwdafDataManagement（NWDAF提供的Nnwdaf_DataManagement服务）<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NFSERVICE]] · NF服务实例（NFSERVICE）

## 使用实例

运营商A需要查询配置的服务实例信息。

```
%%LST NFSERVICE:;%%
RETCODE = 0  操作成功

结果如下
--------
  NF实例名称  =  SMF_Instance_0
服务实例标识  =  Service_Instance_0
    服务名称  =  SMF提供的Nsmf_PDUSession服务
支持的NF类型  =  NULL
服务实例状态  =  REGISTERED
        域名  =  NULL
  PLMN间域名  =  NULL
 API路径前缀  =  NULL
      优先级  =  0
        容量  =  100
        负载  =  0
    支持功能  =  NULL
     Scheme  =  AUTO
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-NFSERVICE.md`
