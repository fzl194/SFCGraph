---
id: UDG@20.15.2@MMLCommand@DSP SBILINKSET
type: MMLCommand
name: DSP SBILINKSET（显示服务化接口链路集信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: SBILINKSET
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- HTTP功能管理
- SBI管理
- 服务化接口链路集管理
status: active
---

# DSP SBILINKSET（显示服务化接口链路集信息）

## 功能

该命令用于显示服务化接口的链路集信息，链路集是指到对端NF的多条链路的集合。显示信息包括了链路集的本对端信息和该链路集下的链路的ID信息。指定链路集下的链路详细信息可以通过查看链路状态获取。

> **说明**
> - 链路集下的链路ID最多显示10个，如果超过10个后面显示“...”。
> - 当用户仅输入服务化接口本端实体索引或本端服务类型或两者都输入时，可查询本端为该服务实体的所有链路集信息；
> - 当用户仅输入对端NF实体类型时，可查询出指定对端类型的所有链路集信息；
> - 当用户仅输入对端NF实例ID时，可查询出指定对端NF实例ID下的所有链路集信息；
> - 当用户输入对端NF实例ID、对端NF服务名称和对端NF服务ID时，可查询该指定对端的链路集信息。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SBIAPLEIDX | 服务化接口本端实体索引 | 可选必选说明：可选参数<br>参数含义：该参数用于指定服务化接口本端实体索引。该本端实体索引是通过<br>[**ADD SBIAPLE**](../服务化接口本端实体管理/增加服务化接口本端实体（ADD SBIAPLE）_28971835.md)<br>命令配置。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~128。<br>默认值：无<br>配置原则：无 |
| LOCALNFTYPE | 本端NF类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定本端NF的类型。<br>数据来源：全网规划<br>取值范围：<br>- “INVALID（INVALID）”：无效值<br>- “NFTypeNRF（NFTypeNRF）”：NF类型为NRF<br>- “NFTypeUDM（NFTypeUDM）”：NF类型为UDM<br>- “NFTypeAMF（NFTypeAMF）”：NF类型为AMF<br>- “NFTypeSMF（NFTypeSMF）”：NF类型为SMF<br>- “NFTypeAUSF（NFTypeAUSF）”：NF类型为AUSF<br>- “NFTypeNEF（NFTypeNEF）”：NF类型为NEF<br>- “NFTypePCF（NFTypePCF）”：NF类型为PCF<br>- “NFTypeSMSF（NFTypeSMSF）”：NF类型为SMSF<br>- “NFTypeNSSF（NFTypeNSSF）”：NF类型为NSSF<br>- “NFTypeUDR（NFTypeUDR）”：NF类型为UDR<br>- “NFTypeLMF（NFTypeLMF）”：NF类型为LMF<br>- “NFTypeGMLC（NFTypeGMLC）”：NF类型为GMLC<br>- “NFType5GEIR（NFType5GEIR）”：NF类型为5GEIR<br>- “NFTypeSEPP（NFTypeSEPP）”：NF类型为SEPP<br>- “NFTypeUPF（NFTypeUPF）”：NF类型为UPF<br>- “NFTypeN3IWF（NFTypeN3IWF）”：NF类型为N3IWF<br>- “NFTypeAF（NFTypeAF）”：NF类型为AF<br>- “NFTypeUDSF（NFTypeUDSF）”：NF类型为UDSF<br>- “NFTypeBSF（NFTypeBSF）”：NF类型为BSF<br>- “NFTypeCHF（NFTypeCHF）”：NF类型为CHF<br>- “NFTypeCUSTOM_OCS（NFTypeCUSTOM_OCS）”：NF类型为OCS<br>- “NFTypeSCP（NFTypeSCP）”：NF类型为SCP<br>- “NFTypeMBSMF（NFTypeMB_SMF）”：NF类型为MB_SMF<br>- “NFTypeNWDAF（NFTypeNWDAF）”：NF类型为NWDAF<br>- “NFTypeUDN（NFTypeUDN）”：NF类型为UDN<br>- “NFTypeSFC（NFTypeSFC）”：NF类型为SFC<br>- “NFTypeUCBC（NFTypeUCBC）”：NF类型为UCBC<br>- “NFTypeCBE（NFTypeCBE）”：NF类型为CBE<br>默认值：无<br>配置原则：无 |
| PEERNFTYPE | 目的NF实体类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定对端NF的类型。<br>数据来源：全网规划<br>取值范围：<br>- “INVALID（INVALID）”：无效值<br>- “NFTypeNRF（NFTypeNRF）”：NF类型为NRF<br>- “NFTypeUDM（NFTypeUDM）”：NF类型为UDM<br>- “NFTypeAMF（NFTypeAMF）”：NF类型为AMF<br>- “NFTypeSMF（NFTypeSMF）”：NF类型为SMF<br>- “NFTypeAUSF（NFTypeAUSF）”：NF类型为AUSF<br>- “NFTypeNEF（NFTypeNEF）”：NF类型为NEF<br>- “NFTypePCF（NFTypePCF）”：NF类型为PCF<br>- “NFTypeSMSF（NFTypeSMSF）”：NF类型为SMSF<br>- “NFTypeNSSF（NFTypeNSSF）”：NF类型为NSSF<br>- “NFTypeUDR（NFTypeUDR）”：NF类型为UDR<br>- “NFTypeLMF（NFTypeLMF）”：NF类型为LMF<br>- “NFTypeGMLC（NFTypeGMLC）”：NF类型为GMLC<br>- “NFType5GEIR（NFType5GEIR）”：NF类型为5GEIR<br>- “NFTypeSEPP（NFTypeSEPP）”：NF类型为SEPP<br>- “NFTypeUPF（NFTypeUPF）”：NF类型为UPF<br>- “NFTypeN3IWF（NFTypeN3IWF）”：NF类型为N3IWF<br>- “NFTypeAF（NFTypeAF）”：NF类型为AF<br>- “NFTypeUDSF（NFTypeUDSF）”：NF类型为UDSF<br>- “NFTypeBSF（NFTypeBSF）”：NF类型为BSF<br>- “NFTypeCHF（NFTypeCHF）”：NF类型为CHF<br>- “NFTypeCUSTOM_OCS（NFTypeCUSTOM_OCS）”：NF类型为OCS<br>- “NFTypeSCP（NFTypeSCP）”：NF类型为SCP<br>- “NFTypeMBSMF（NFTypeMB_SMF）”：NF类型为MB_SMF<br>- “NFTypeNWDAF（NFTypeNWDAF）”：NF类型为NWDAF<br>- “NFTypeUDN（NFTypeUDN）”：NF类型为UDN<br>- “NFTypeSFC（NFTypeSFC）”：NF类型为SFC<br>- “NFTypeUCBC（NFTypeUCBC）”：NF类型为UCBC<br>- “NFTypeCBE（NFTypeCBE）”：NF类型为CBE<br>其中，INVALID为无效值，系统支持下发，但实际不生效。<br>默认值：无<br>配置原则：无 |
| PEERNFINSTID | 对端NF实例ID | 可选必选说明：可选参数<br>参数含义：对端NF实例ID，用来唯一标识一个NF网元。该标识要求全网唯一。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~255。<br>默认值：无<br>配置原则：无 |
| PEERNFSRVNAME | 对端NF服务名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定对端NF提供的服务的名称，一个NF可以提供多个不同的服务，如AMF可以提供Namf_Communication、Namf_EventExposure等服务。<br>数据来源：全网规划<br>取值范围：<br>- “Nnrf_nfm（Nrf_NFManagement）”：NRF提供的Nrf_NFManagement服务<br>- “Nnrf_disc（Nnrf_NFDiscovery）”：NRF提供的Nnrf_NFDiscovery服务<br>- “Nudm_sdm（Nudm_SubscriberDataManagement）”：UDM提供的Nudm_SubscriberDataManagement服务<br>- “Nudm_uecm（Nudm_UEContextManagement）”：UDM提供的Nudm_UEContextManagement服务<br>- “Nudm_ee（Nudm_EventExposure）”：UDM提供的Nudm_EventExposure Service offered by the UDM服务<br>- “Nudm_ueau（Nudm_UEAuthentication）”：UEM提供的Nudm_UEAuthentication服务<br>- “Nudm_pp（Nudm_ParameterProvision）”：UDM提供的Nudm_ParameterProvision服务<br>- “Namf_comm（Namf_Communication）”：AMF提供的Namf_Communication<br>- “Namf_evts（Namf_EventExposure）”：AMF提供的Namf_EventExposure服务<br>- “Namf_mt（Namf_MT）”：AMF提供的Namf_MT服务<br>- “Namf_loc（Namf_Location）”：AMF提供的Namf_Location服务<br>- “Nsmf_pdusession（Nsmf_PDUSession）”：SMF提供的Nsmf_PDUSession服务<br>- “Nsmf_ee（Nsmf_EventExposure）”：SMF提供的Nsmf_EventExposure服务<br>- “Nausf_auth（Nausf_UEAuthentication）”：AUSF提供的Nausf_UEAuthentication服务<br>- “Nausf_sorprotection（Nausf_SoRProtection）”：AUSF提供的Nausf_SoRProtection服务<br>- “Nausf_upuprotection（Nausf_UPUProtection）”：AUSF提供的Nausf_UPUProtection服务<br>- “Nnef_pfdmanagement（Nnef_PFDManagement ）”：NEF提供的Nnef_PFDManagement服务<br>- “Npcf_am_policy_control（Npcf_AMPolicyControl ）”：PCF提供的Npcf_AMPolicyControl服务<br>- “Npcf_smpolicyControl（Npcf_SMPolicyControl）”：PCF提供的Npcf_SMPolicyControl服务<br>- “Npcf_policyauthorization（Npcf_PolicyAuthorization ）”：PCF提供的Npcf_PolicyAuthorization服务<br>- “Npcf_bdtpolicyControl（Npcf_BDTPolicyControl ）”：PCF提供的Npcf_BDTPolicyControl服务<br>- “Npcf_eventexposure（Npcf_EventExposure ）”：PCF提供的Npcf_EventExposure服务<br>- “Npcf_ue_policy_control（Npcf_UEPolicyControl ）”：PCF提供的Npcf_UEPolicyControl服务<br>- “Nsmsf_sms（Nsmsf_SMService ）”：SMSF提供的Nsmsf_SMService服务<br>- “Nnssf_nsselection（Nnssf_NSSelection ）”：NSSF提供的Nnssf_NSSelection服务<br>- “Nnssf_nssaiavailability（Nnssf_NSSAIAvailability ）”：NSSF提供的Nnssf_NSSAIAvailability服务<br>- “Nudr_dr（Nudr_DataRepository）”：UDR提供的Nudr_DataRepository服务<br>- “Nlmf_loc（Nlmf_Location ）”：LMF提供的Nlmf_Location服务<br>- “N5g_eir_eic（N5g-eir_EquipmentIdentityCheck）”：5G-EIR提供的N5g-eir_EquipmentIdentityCh服务eck<br>- “Nbsf_management（Nbsf_Management ）”：BSF提供的Nbsf_Management服务<br>- “Nchf_spendinglimitcontrol（Nchf_SpendingLimitControl ）”：Nchf_SpendingLimitControl Service offered by the CHF<br>- “Nchf_convergedcharging（Nchf_Converged_Charging ）”：CHF提供的Nchf_Converged_Charging服务<br>- “Nnwdaf_eventssubscription（Nnwdaf_EventsSubscription ）”：NWDAF提供的Nnwdaf_EventsSubscription服务<br>- “Nnwdaf_analyticsinfo（Nnwdaf_AnalyticsInfo）”：NWDAF提供的Nnwdaf_AnalyticsInfo服务<br>- “Ncustom_ocs_spendinglimitcontrol（Ncustom_ocs_SpendingLimitControl）”：CUSTOM_OCS提供的Ncustom_ocs_SpendingLimitControl服务<br>- “Ncustom_ocs_convergedcharging（Ncustom_ocs_ConvergedCharging）”：CUSTOM_OCS提供的Ncustom_ocs_ConvergedCharging服务<br>- “Invalid（Invalid）”：无效服务<br>- “Ngmlc_loc（Ngmlc_Location）”：GMLC提供的Ngmlc_Location服务<br>- “Nmbsmf_tmgi（Nmbsmf_TMGI）”：MB_SMF提供的Nmbsmf_TMGI服务<br>- “Nmbsmf_mbssession（Nmbsmf_MBSSession）”：MB_SMF提供的Nmbsmf_MBSSession服务<br>- “Namf_mbs_bc（Namf_MBSBroadcast）”：AMF提供的Namf_MBSBroadcast服务<br>- “Nnef_3gpp_traffic_influence（Nnef_3gpp_traffic_influence）”：NEF提供的3gpp_traffic_influence服务<br>- “Nnef_3gpp_chargeable_party（Nnef_3gpp_chargeable_party）”：NEF提供的3gpp_chargeable_party服务<br>- “Nupf_eventexposure（Nupf_eventexposure）”：UPF提供的Nupf_EventExposure服务<br>- “Nudn_datamanagement（Nudn_datamanagement）”：UDN提供的Nudn_datamanagement服务<br>- “Nnef_smcontext（Nnef_smcontext）”：NEF提供的Nnef_smcontext服务<br>- “Nsfc_sense（Nsfc_sense）”：SFC提供的Nsfc_sense服务<br>- “Namf_sense（Namf_sense）”：AMF提供的Namf_sense服务<br>- “Nnwdaf_datamanagement（Nnwdaf_datamanagement）”：NWDAF提供的Nnwdaf_datamanagement服务<br>默认值：无<br>配置原则：无 |
| PEERNFSRVINSID | 对端NF服务实例ID | 可选必选说明：可选参数<br>参数含义：该参数用于指定对端NF服务的实例ID，用于唯一标识一个NF中的服务，该标识在NF内唯一。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~255。<br>默认值：无<br>配置原则：无 |
| LINKSETSTATUS | 链路集状态 | 可选必选说明：可选参数<br>参数含义：该参数用于显示链路集的当前状态。当链路集下所有链路均故障时，链路集状态为故障；当链路集下有一条链路状态恢复为正常以后，该链路集状态即为正常；如果人工闭塞链路集，则该链路集下的所有链路均会闭塞，且该链路集不可用。<br>数据来源：全网规划<br>取值范围：<br>- “Active（正常）”：链路正常传输数据业务<br>- “Inactive（故障）”：链路不可用无法传输数据业务<br>- “Initial（初始态）”：链路新增即将被建立<br>- “Aging（老化）”：链路在老化定时器超时时间内无数据业务<br>- “Overload（过载）”：链路在单位时间内的数据传输量过大，传输数据业务受控<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@SBILINKSET]] · 服务化接口链路集（SBILINKSET）

## 使用实例

- 若运营商想查询本端NF类型为AMF，对端NF类型为SMF的链路集信息，执行如下命令：
  ```
  DSP SBILINKSET: LOCALNFTYPE=NFTypeAMF, PEERNFTYPE=NFTypeSMF;
  ```
- 若运营商想查询对端NF实例ID为4947a69a-f61b-4bc1-b9da-47c9c5d14b64的链路集信息，执行如下命令：
  ```
  DSP SBILINKSET: PEERNFINSTID="4947a69a-f61b-4bc1-b9da-47c9c5d14b64";
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-SBILINKSET.md`
