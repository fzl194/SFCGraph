---
id: UNC@20.15.2@MMLCommand@DSP SBIPEERNF
type: MMLCommand
name: DSP SBIPEERNF（显示服务化接口对端NF信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: SBIPEERNF
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- HTTP功能管理
- SBI管理
- 服务化接口对端NF管理
status: active
---

# DSP SBIPEERNF（显示服务化接口对端NF信息）

## 功能

该命令用于显示服务化接口中的对端NF的信息。该对端NF来源有NF服务发现、CallbackURI携带、Location头域携带或静态配置。通过本命令可以查询出不同的对端NF的具体信息，包括该NF的实例ID、NF类型、NF的服务名称、NF服务实例ID等，主要用于观察对端NF的详细信息，可以在出现和对端NF的服务的通讯问题时用于协助问题的定位。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PEERTYPE | 对端来源类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定对端NF的类型。该类型基于对端NF的来源区分，如果该NF为NRF发现，则类型为动态；如果该NF为通过callback回调生成或通过Location生成则类型为直接地址；如果改NF为配置添加，则类型为静态。直接地址是指，callback情况下在callbackURI中携带的消息通知的目的主机信息，或location情况下在HTTP响应报文Location头域中携带的目的资源所在的实际目的主机信息。<br>数据来源：全网规划<br>取值范围：<br>- “Discovery（动态发现）”：通过NRF动态发现。<br>- “Callback（直接地址）”：通过callbackURI获取或通过LocationURI获取。当前无法区分这两种情况，都返回callback。<br>- “Location（Location）”：通过callbackURI获取或通过LocationURI获取。当前无法区分这两种情况，都返回callback。<br>- “Config（本地配置）”：通过静态配置。<br>默认值：无<br>配置原则：无 |
| PEERNFTYPE | 对端NF类型 | 可选必选说明：该参数在"PEERTYPE"配置为"Discovery"、"Config"时为条件可选参数。<br>参数含义：该参数用于指定目的NF的类型。当NF类型为callback或Location时，该项为空。<br>数据来源：本端规划<br>取值范围：<br>- “INVALID（INVALID）”：无效值<br>- “NFTypeNRF（NFTypeNRF）”：NF类型为NRF<br>- “NFTypeUDM（NFTypeUDM）”：NF类型为UDM<br>- “NFTypeAMF（NFTypeAMF）”：NF类型为AMF<br>- “NFTypeSMF（NFTypeSMF）”：NF类型为SMF<br>- “NFTypeAUSF（NFTypeAUSF）”：NF类型为AUSF<br>- “NFTypeNEF（NFTypeNEF）”：NF类型为NEF<br>- “NFTypePCF（NFTypePCF）”：NF类型为PCF<br>- “NFTypeSMSF（NFTypeSMSF）”：NF类型为SMSF<br>- “NFTypeNSSF（NFTypeNSSF）”：NF类型为NSSF<br>- “NFTypeUDR（NFTypeUDR）”：NF类型为UDR<br>- “NFTypeLMF（NFTypeLMF）”：NF类型为LMF<br>- “NFTypeGMLC（NFTypeGMLC）”：NF类型为GMLC<br>- “NFType5GEIR（NFType5GEIR）”：NF类型为5GEIR<br>- “NFTypeSEPP（NFTypeSEPP）”：NF类型为SEPP<br>- “NFTypeUPF（NFTypeUPF）”：NF类型为UPF<br>- “NFTypeN3IWF（NFTypeN3IWF）”：NF类型为N3IWF<br>- “NFTypeAF（NFTypeAF）”：NF类型为AF<br>- “NFTypeUDSF（NFTypeUDSF）”：NF类型为UDSF<br>- “NFTypeBSF（NFTypeBSF）”：NF类型为BSF<br>- “NFTypeCHF（NFTypeCHF）”：NF类型为CHF<br>- “NFTypeCUSTOM_OCS（NFTypeCUSTOM_OCS）”：NF类型为OCS<br>- “NFTypeSCP（NFTypeSCP）”：NF类型为SCP<br>- “NFTypeMBSMF（NFTypeMB_SMF）”：NF类型为MB_SMF<br>- “NFTypeNWDAF（NFTypeNWDAF）”：NF类型为NWDAF<br>- “NFTypeUDN（NFTypeUDN）”：NF类型为UDN<br>- “NFTypeSFC（NFTypeSFC）”：NF类型为SFC<br>- “NFTypeUCBC（NFTypeUCBC）”：NF类型为UCBC<br>- “NFTypeCBE（NFTypeCBE）”：NF类型为CBE<br>默认值：无<br>配置原则：无 |
| PEERNFINSTID | 对端NF实例ID | 可选必选说明：该参数在"PEERTYPE"配置为"Discovery"、"Config"时为条件可选参数。<br>参数含义：该参数用于指定对端NF的实例ID信息。NF实例ID是全网唯一，用于标识一个NF。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~256。<br>默认值：无<br>配置原则：无 |
| PEERNFSRVNAME | 对端NF服务名称 | 可选必选说明：该参数在"PEERTYPE"配置为"Discovery"、"Config"时为条件可选参数。<br>参数含义：该参数用于指定对端NF服务的名称。NF服务名称为协议定义的一个NF的可提供的服务的名称。<br>数据来源：全网规划<br>取值范围：<br>- “Nnrf_nfm（Nrf_NFManagement）”：NRF提供的Nrf_NFManagement服务<br>- “Nnrf_disc（Nnrf_NFDiscovery）”：NRF提供的Nnrf_NFDiscovery服务<br>- “Nudm_sdm（Nudm_SubscriberDataManagement）”：UDM提供的Nudm_SubscriberDataManagement服务<br>- “Nudm_uecm（Nudm_UEContextManagement）”：UDM提供的Nudm_UEContextManagement服务<br>- “Nudm_ee（Nudm_EventExposure）”：UDM提供的Nudm_EventExposure Service offered by the UDM服务<br>- “Nudm_ueau（Nudm_UEAuthentication）”：UEM提供的Nudm_UEAuthentication服务<br>- “Nudm_pp（Nudm_ParameterProvision）”：UDM提供的Nudm_ParameterProvision服务<br>- “Namf_comm（Namf_Communication）”：AMF提供的Namf_Communication<br>- “Namf_evts（Namf_EventExposure）”：AMF提供的Namf_EventExposure服务<br>- “Namf_mt（Namf_MT）”：AMF提供的Namf_MT服务<br>- “Namf_loc（Namf_Location）”：AMF提供的Namf_Location服务<br>- “Nsmf_pdusession（Nsmf_PDUSession）”：SMF提供的Nsmf_PDUSession服务<br>- “Nsmf_ee（Nsmf_EventExposure）”：SMF提供的Nsmf_EventExposure服务<br>- “Nausf_auth（Nausf_UEAuthentication）”：AUSF提供的Nausf_UEAuthentication服务<br>- “Nausf_sorprotection（Nausf_SoRProtection）”：AUSF提供的Nausf_SoRProtection服务<br>- “Nausf_upuprotection（Nausf_UPUProtection）”：AUSF提供的Nausf_UPUProtection服务<br>- “Nnef_pfdmanagement（Nnef_PFDManagement ）”：NEF提供的Nnef_PFDManagement服务<br>- “Npcf_am_policy_control（Npcf_AMPolicyControl ）”：PCF提供的Npcf_AMPolicyControl服务<br>- “Npcf_smpolicyControl（Npcf_SMPolicyControl）”：PCF提供的Npcf_SMPolicyControl服务<br>- “Npcf_policyauthorization（Npcf_PolicyAuthorization ）”：PCF提供的Npcf_PolicyAuthorization服务<br>- “Npcf_bdtpolicyControl（Npcf_BDTPolicyControl ）”：PCF提供的Npcf_BDTPolicyControl服务<br>- “Npcf_eventexposure（Npcf_EventExposure ）”：PCF提供的Npcf_EventExposure服务<br>- “Npcf_ue_policy_control（Npcf_UEPolicyControl ）”：PCF提供的Npcf_UEPolicyControl服务<br>- “Nsmsf_sms（Nsmsf_SMService ）”：SMSF提供的Nsmsf_SMService服务<br>- “Nnssf_nsselection（Nnssf_NSSelection ）”：NSSF提供的Nnssf_NSSelection服务<br>- “Nnssf_nssaiavailability（Nnssf_NSSAIAvailability ）”：NSSF提供的Nnssf_NSSAIAvailability服务<br>- “Nudr_dr（Nudr_DataRepository）”：UDR提供的Nudr_DataRepository服务<br>- “Nlmf_loc（Nlmf_Location ）”：LMF提供的Nlmf_Location服务<br>- “N5g_eir_eic（N5g-eir_EquipmentIdentityCheck）”：5G-EIR提供的N5g-eir_EquipmentIdentityCh服务eck<br>- “Nbsf_management（Nbsf_Management ）”：BSF提供的Nbsf_Management服务<br>- “Nchf_spendinglimitcontrol（Nchf_SpendingLimitControl ）”：Nchf_SpendingLimitControl Service offered by the CHF<br>- “Nchf_convergedcharging（Nchf_Converged_Charging ）”：CHF提供的Nchf_Converged_Charging服务<br>- “Nnwdaf_eventssubscription（Nnwdaf_EventsSubscription ）”：NWDAF提供的Nnwdaf_EventsSubscription服务<br>- “Nnwdaf_analyticsinfo（Nnwdaf_AnalyticsInfo）”：NWDAF提供的Nnwdaf_AnalyticsInfo服务<br>- “Ncustom_ocs_spendinglimitcontrol（Ncustom_ocs_SpendingLimitControl）”：CUSTOM_OCS提供的Ncustom_ocs_SpendingLimitControl服务<br>- “Ncustom_ocs_convergedcharging（Ncustom_ocs_ConvergedCharging）”：CUSTOM_OCS提供的Ncustom_ocs_ConvergedCharging服务<br>- “Invalid（Invalid）”：无效服务<br>- “Ngmlc_loc（Ngmlc_Location）”：GMLC提供的Ngmlc_Location服务<br>- “Nmbsmf_tmgi（Nmbsmf_TMGI）”：MB_SMF提供的Nmbsmf_TMGI服务<br>- “Nmbsmf_mbssession（Nmbsmf_MBSSession）”：MB_SMF提供的Nmbsmf_MBSSession服务<br>- “Namf_mbs_bc（Namf_MBSBroadcast）”：AMF提供的Namf_MBSBroadcast服务<br>- “Nnef_3gpp_traffic_influence（Nnef_3gpp_traffic_influence）”：NEF提供的3gpp_traffic_influence服务<br>- “Nnef_3gpp_chargeable_party（Nnef_3gpp_chargeable_party）”：NEF提供的3gpp_chargeable_party服务<br>- “Nupf_eventexposure（Nupf_eventexposure）”：UPF提供的Nupf_EventExposure服务<br>- “Nudn_datamanagement（Nudn_datamanagement）”：UDN提供的Nudn_datamanagement服务<br>- “Nnef_smcontext（Nnef_smcontext）”：NEF提供的Nnef_smcontext服务<br>- “Nsfc_sense（Nsfc_sense）”：SFC提供的Nsfc_sense服务<br>- “Namf_sense（Namf_sense）”：AMF提供的Namf_sense服务<br>- “Nnwdaf_datamanagement（Nnwdaf_datamanagement）”：NWDAF提供的Nnwdaf_datamanagement服务<br>默认值：无<br>配置原则：无 |
| PEERNFSRVINSTID | 对端NF服务实例ID | 可选必选说明：该参数在"PEERTYPE"配置为"Discovery"、"Config"时为条件可选参数。<br>参数含义：该参数用于指定对端NF服务的实例ID。一个NF提供多个NF服务，通过NF服务名称区别不同的NF服务，同时需要指定NF服务实例ID，通过NF服务实例ID区分相同名称的不同NF服务实例。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~256。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SBIPEERNF]] · 服务化接口对端NF信息（SBIPEERNF）

## 使用实例

- 若运营商想查询通过服务发现的并且类型为SMF的对端NF信息，执行如下命令：
  ```
  DSP SBIPEERNF: PEERTYPE=Discovery, PEERNFTYPE=NFTypeSMF;
  ```
- 若运营商想查询通过CallbackURI携带的对端NF信息，执行如下命令：
  ```
  DSP SBIPEERNF: PEERTYPE=Callback;
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示服务化接口对端NF信息（DSP-SBIPEERNF）_29291767.md`
