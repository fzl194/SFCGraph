---
id: UDG@20.15.2@MMLCommand@DSP SBILINKSTATUS
type: MMLCommand
name: DSP SBILINKSTATUS（查询服务化接口链路状态）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: SBILINKSTATUS
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- HTTP功能管理
- SBI管理
- 服务化接口链路管理
status: active
---

# DSP SBILINKSTATUS（查询服务化接口链路状态）

## 功能

![](查询服务化接口链路状态（DSP SBILINKSTATUS）_29213281.assets/notice_3.0-zh-cn.png)

当链路数较多时，执行该命令会占用运维平台较长时间，进而导致用户无法继续使用该运维平台。对于业务负载较高的设备，建议查询时加上网元类型、链路状态、全局进程标识、POD名称等参数减少命令查询的链路数，避免对设备造成冲击影响业务。

该命令用于查询服务化接口的链路状态。可支持服务端和客户端链路查询。当系统角色为服务端时，可在系统中查询由客户端发起建立的链路的基本信息。当系统为客户端时，可在系统中查询由本端发起建立的链路的详细信息。

> **说明**
> - 如果是客户端链路，本命令会显示该链路所属的链路集标识，此信息可用于[**DSP SBILINKSET**](../服务化接口链路集管理/显示服务化接口链路集信息（DSP SBILINKSET）_84132098.md)命令基于该链路集标识查询对应的链路集信息。
> - 如果是服务端链路，链路集标识显示为空，服务端链路不做链路集管理。
> - 当输入链路ID查询链路详细信息时必须同时输入链路集ID。
> - 该命令执行之后，会查询满足输入参数条件的所有链路。在链路数比较多的情况下，查询客户端或服务端的全部链路会有一定的资源消耗。
> - 当[**DSP HTTPPROCESS**](../../HTTP管理/HTTP进程状态管理/显示HTTP进程信息（DSP HTTPPROCESS）_29053327.md)命令查询的CPU结果超过95%时，可能无法查询到所有的客户端链路。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ENTITYTYPE | 本端NF角色 | 可选必选说明：必选参数<br>参数含义：该参数用于指定本端NF角色，有客户端和服务端两种。<br>数据来源：全网规划<br>取值范围：<br>- “Client（Client）”：客户端<br>- “Server（Server）”：服务端<br>默认值：无<br>配置原则：无 |
| LINKSETID | 链路集标识 | 可选必选说明：该参数在"ENTITYTYPE"配置为"Client"时为条件可选参数。<br>参数含义：该参数用于指定链路所在的链路集。输入该链路集标识，可以查询出该链路集下的所有链路的详细信息。输入链路集标识和链路ID可以查询出一条该链路集下的链路的详细信息。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~256。<br>默认值：无<br>配置原则：无 |
| LINKID | 链路ID | 可选必选说明：该参数在"ENTITYTYPE"配置为"Client"时为条件可选参数。<br>参数含义：该参数用于指定链路的标识，用于唯一确定一条一个链路集下的链路。当输入链路ID查询链路详细信息时必须同时输入链路集ID。该链路ID同Linkset中记录的LinkID为同一值。可基于链路集ID和该LinkID查询出一条链路的详细信息。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~4294967295。<br>默认值：无<br>配置原则：无 |
| LINKTYPE | 链路类型 | 可选必选说明：该参数在"ENTITYTYPE"配置为"Client"时为条件可选参数。<br>参数含义：该参数用于指定查询的链路类型，是动态链路还是静态链路。<br>数据来源：全网规划<br>取值范围：<br>- “Dynamic（Dynamic）”：动态学习<br>- “Static（Static）”：静态配置<br>默认值：无<br>配置原则：无 |
| LOCALNFTYPE | 本端NF类型 | 可选必选说明：该参数在"ENTITYTYPE"配置为"Client"时为条件可选参数。<br>参数含义：该参数用于指定本端NF类型。<br>数据来源：本端规划<br>取值范围：<br>- “INVALID（INVALID）”：无效值<br>- “NFTypeNRF（NFTypeNRF）”：NF类型为NRF<br>- “NFTypeUDM（NFTypeUDM）”：NF类型为UDM<br>- “NFTypeAMF（NFTypeAMF）”：NF类型为AMF<br>- “NFTypeSMF（NFTypeSMF）”：NF类型为SMF<br>- “NFTypeAUSF（NFTypeAUSF）”：NF类型为AUSF<br>- “NFTypeNEF（NFTypeNEF）”：NF类型为NEF<br>- “NFTypePCF（NFTypePCF）”：NF类型为PCF<br>- “NFTypeSMSF（NFTypeSMSF）”：NF类型为SMSF<br>- “NFTypeNSSF（NFTypeNSSF）”：NF类型为NSSF<br>- “NFTypeUDR（NFTypeUDR）”：NF类型为UDR<br>- “NFTypeLMF（NFTypeLMF）”：NF类型为LMF<br>- “NFTypeGMLC（NFTypeGMLC）”：NF类型为GMLC<br>- “NFType5GEIR（NFType5GEIR）”：NF类型为5GEIR<br>- “NFTypeSEPP（NFTypeSEPP）”：NF类型为SEPP<br>- “NFTypeUPF（NFTypeUPF）”：NF类型为UPF<br>- “NFTypeN3IWF（NFTypeN3IWF）”：NF类型为N3IWF<br>- “NFTypeAF（NFTypeAF）”：NF类型为AF<br>- “NFTypeUDSF（NFTypeUDSF）”：NF类型为UDSF<br>- “NFTypeBSF（NFTypeBSF）”：NF类型为BSF<br>- “NFTypeCHF（NFTypeCHF）”：NF类型为CHF<br>- “NFTypeCUSTOM_OCS（NFTypeCUSTOM_OCS）”：NF类型为OCS<br>- “NFTypeSCP（NFTypeSCP）”：NF类型为SCP<br>- “NFTypeMBSMF（NFTypeMB_SMF）”：NF类型为MB_SMF<br>- “NFTypeNWDAF（NFTypeNWDAF）”：NF类型为NWDAF<br>- “NFTypeUDN（NFTypeUDN）”：NF类型为UDN<br>- “NFTypeSFC（NFTypeSFC）”：NF类型为SFC<br>- “NFTypeUCBC（NFTypeUCBC）”：NF类型为UCBC<br>- “NFTypeCBE（NFTypeCBE）”：NF类型为CBE<br>默认值：无<br>配置原则：无 |
| PEERNFTYPE | 对端NF类型 | 可选必选说明：该参数在"ENTITYTYPE"配置为"Client"时为条件可选参数。<br>参数含义：该参数用于指定对端NF类型。<br>数据来源：本端规划<br>取值范围：<br>- “INVALID（INVALID）”：无效值<br>- “NFTypeNRF（NFTypeNRF）”：NF类型为NRF<br>- “NFTypeUDM（NFTypeUDM）”：NF类型为UDM<br>- “NFTypeAMF（NFTypeAMF）”：NF类型为AMF<br>- “NFTypeSMF（NFTypeSMF）”：NF类型为SMF<br>- “NFTypeAUSF（NFTypeAUSF）”：NF类型为AUSF<br>- “NFTypeNEF（NFTypeNEF）”：NF类型为NEF<br>- “NFTypePCF（NFTypePCF）”：NF类型为PCF<br>- “NFTypeSMSF（NFTypeSMSF）”：NF类型为SMSF<br>- “NFTypeNSSF（NFTypeNSSF）”：NF类型为NSSF<br>- “NFTypeUDR（NFTypeUDR）”：NF类型为UDR<br>- “NFTypeLMF（NFTypeLMF）”：NF类型为LMF<br>- “NFTypeGMLC（NFTypeGMLC）”：NF类型为GMLC<br>- “NFType5GEIR（NFType5GEIR）”：NF类型为5GEIR<br>- “NFTypeSEPP（NFTypeSEPP）”：NF类型为SEPP<br>- “NFTypeUPF（NFTypeUPF）”：NF类型为UPF<br>- “NFTypeN3IWF（NFTypeN3IWF）”：NF类型为N3IWF<br>- “NFTypeAF（NFTypeAF）”：NF类型为AF<br>- “NFTypeUDSF（NFTypeUDSF）”：NF类型为UDSF<br>- “NFTypeBSF（NFTypeBSF）”：NF类型为BSF<br>- “NFTypeCHF（NFTypeCHF）”：NF类型为CHF<br>- “NFTypeCUSTOM_OCS（NFTypeCUSTOM_OCS）”：NF类型为OCS<br>- “NFTypeSCP（NFTypeSCP）”：NF类型为SCP<br>- “NFTypeMBSMF（NFTypeMB_SMF）”：NF类型为MB_SMF<br>- “NFTypeNWDAF（NFTypeNWDAF）”：NF类型为NWDAF<br>- “NFTypeUDN（NFTypeUDN）”：NF类型为UDN<br>- “NFTypeSFC（NFTypeSFC）”：NF类型为SFC<br>- “NFTypeUCBC（NFTypeUCBC）”：NF类型为UCBC<br>- “NFTypeCBE（NFTypeCBE）”：NF类型为CBE<br>默认值：无<br>配置原则：无 |
| PEERNFINSTID | 对端NF实例ID | 可选必选说明：该参数在"ENTITYTYPE"配置为"Client"时为条件可选参数。<br>参数含义：该参数用于指定对端NF实例ID。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~255。<br>默认值：无<br>配置原则：无 |
| PEERNFSRVNAME | 对端NF服务名称 | 可选必选说明：该参数在"ENTITYTYPE"配置为"Client"时为条件可选参数。<br>参数含义：该参数用于指定对端NF服务名称。<br>数据来源：本端规划<br>取值范围：<br>- “Nnrf_nfm（Nrf_NFManagement）”：NRF提供的Nrf_NFManagement服务<br>- “Nnrf_disc（Nnrf_NFDiscovery）”：NRF提供的Nnrf_NFDiscovery服务<br>- “Nudm_sdm（Nudm_SubscriberDataManagement）”：UDM提供的Nudm_SubscriberDataManagement服务<br>- “Nudm_uecm（Nudm_UEContextManagement）”：UDM提供的Nudm_UEContextManagement服务<br>- “Nudm_ee（Nudm_EventExposure）”：UDM提供的Nudm_EventExposure Service offered by the UDM服务<br>- “Nudm_ueau（Nudm_UEAuthentication）”：UEM提供的Nudm_UEAuthentication服务<br>- “Nudm_pp（Nudm_ParameterProvision）”：UDM提供的Nudm_ParameterProvision服务<br>- “Namf_comm（Namf_Communication）”：AMF提供的Namf_Communication<br>- “Namf_evts（Namf_EventExposure）”：AMF提供的Namf_EventExposure服务<br>- “Namf_mt（Namf_MT）”：AMF提供的Namf_MT服务<br>- “Namf_loc（Namf_Location）”：AMF提供的Namf_Location服务<br>- “Nsmf_pdusession（Nsmf_PDUSession）”：SMF提供的Nsmf_PDUSession服务<br>- “Nsmf_ee（Nsmf_EventExposure）”：SMF提供的Nsmf_EventExposure服务<br>- “Nausf_auth（Nausf_UEAuthentication）”：AUSF提供的Nausf_UEAuthentication服务<br>- “Nausf_sorprotection（Nausf_SoRProtection）”：AUSF提供的Nausf_SoRProtection服务<br>- “Nausf_upuprotection（Nausf_UPUProtection）”：AUSF提供的Nausf_UPUProtection服务<br>- “Nnef_pfdmanagement（Nnef_PFDManagement ）”：NEF提供的Nnef_PFDManagement服务<br>- “Npcf_am_policy_control（Npcf_AMPolicyControl ）”：PCF提供的Npcf_AMPolicyControl服务<br>- “Npcf_smpolicyControl（Npcf_SMPolicyControl）”：PCF提供的Npcf_SMPolicyControl服务<br>- “Npcf_policyauthorization（Npcf_PolicyAuthorization ）”：PCF提供的Npcf_PolicyAuthorization服务<br>- “Npcf_bdtpolicyControl（Npcf_BDTPolicyControl ）”：PCF提供的Npcf_BDTPolicyControl服务<br>- “Npcf_eventexposure（Npcf_EventExposure ）”：PCF提供的Npcf_EventExposure服务<br>- “Npcf_ue_policy_control（Npcf_UEPolicyControl ）”：PCF提供的Npcf_UEPolicyControl服务<br>- “Nsmsf_sms（Nsmsf_SMService ）”：SMSF提供的Nsmsf_SMService服务<br>- “Nnssf_nsselection（Nnssf_NSSelection ）”：NSSF提供的Nnssf_NSSelection服务<br>- “Nnssf_nssaiavailability（Nnssf_NSSAIAvailability ）”：NSSF提供的Nnssf_NSSAIAvailability服务<br>- “Nudr_dr（Nudr_DataRepository）”：UDR提供的Nudr_DataRepository服务<br>- “Nlmf_loc（Nlmf_Location ）”：LMF提供的Nlmf_Location服务<br>- “N5g_eir_eic（N5g-eir_EquipmentIdentityCheck）”：5G-EIR提供的N5g-eir_EquipmentIdentityCh服务eck<br>- “Nbsf_management（Nbsf_Management ）”：BSF提供的Nbsf_Management服务<br>- “Nchf_spendinglimitcontrol（Nchf_SpendingLimitControl ）”：Nchf_SpendingLimitControl Service offered by the CHF<br>- “Nchf_convergedcharging（Nchf_Converged_Charging ）”：CHF提供的Nchf_Converged_Charging服务<br>- “Nnwdaf_eventssubscription（Nnwdaf_EventsSubscription ）”：NWDAF提供的Nnwdaf_EventsSubscription服务<br>- “Nnwdaf_analyticsinfo（Nnwdaf_AnalyticsInfo）”：NWDAF提供的Nnwdaf_AnalyticsInfo服务<br>- “Ncustom_ocs_spendinglimitcontrol（Ncustom_ocs_SpendingLimitControl）”：CUSTOM_OCS提供的Ncustom_ocs_SpendingLimitControl服务<br>- “Ncustom_ocs_convergedcharging（Ncustom_ocs_ConvergedCharging）”：CUSTOM_OCS提供的Ncustom_ocs_ConvergedCharging服务<br>- “Invalid（Invalid）”：无效服务<br>- “Ngmlc_loc（Ngmlc_Location）”：GMLC提供的Ngmlc_Location服务<br>- “Nmbsmf_tmgi（Nmbsmf_TMGI）”：MB_SMF提供的Nmbsmf_TMGI服务<br>- “Nmbsmf_mbssession（Nmbsmf_MBSSession）”：MB_SMF提供的Nmbsmf_MBSSession服务<br>- “Namf_mbs_bc（Namf_MBSBroadcast）”：AMF提供的Namf_MBSBroadcast服务<br>- “Nnef_3gpp_traffic_influence（Nnef_3gpp_traffic_influence）”：NEF提供的3gpp_traffic_influence服务<br>- “Nnef_3gpp_chargeable_party（Nnef_3gpp_chargeable_party）”：NEF提供的3gpp_chargeable_party服务<br>- “Nupf_eventexposure（Nupf_eventexposure）”：UPF提供的Nupf_EventExposure服务<br>- “Nudn_datamanagement（Nudn_datamanagement）”：UDN提供的Nudn_datamanagement服务<br>- “Nnef_smcontext（Nnef_smcontext）”：NEF提供的Nnef_smcontext服务<br>- “Nsfc_sense（Nsfc_sense）”：SFC提供的Nsfc_sense服务<br>- “Namf_sense（Namf_sense）”：AMF提供的Namf_sense服务<br>- “Nnwdaf_datamanagement（Nnwdaf_datamanagement）”：NWDAF提供的Nnwdaf_datamanagement服务<br>默认值：无<br>配置原则：无 |
| PEERNFSRVINSTID | 对端服务实例ID | 可选必选说明：该参数在"ENTITYTYPE"配置为"Client"时为条件可选参数。<br>参数含义：该参数用于指定对端服务实例ID。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~255。<br>默认值：无<br>配置原则：无 |
| LOCALADDR | 本端地址 | 可选必选说明：该参数在"ENTITYTYPE"配置为"Server"时为条件可选参数。<br>参数含义：该参数用于指定本端地址。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~255。需填写IP地址，或者IP地址及端口号，中间以“:”分割，例如：192.168.0.1或192.168.0.1:8888或fe80::1或[fe80::1]:8888。<br>默认值：无<br>配置原则：无 |
| PEERADDR | 对端地址 | 可选必选说明：该参数在"ENTITYTYPE"配置为"Server"、"Client"时为条件可选参数。<br>参数含义：该参数用于指定对端地址。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~255。需填写IP地址，或者IP地址及端口号，中间以“:”分割，例如：192.168.0.1或192.168.0.1:8888或fe80::1或[fe80::1]:8888。<br>默认值：无<br>配置原则：无 |
| STATUS | 链路状态 | 可选必选说明：该参数在"ENTITYTYPE"配置为"Client"时为条件可选参数。<br>参数含义：该参数用于指定链路状态。<br>数据来源：全网规划<br>取值范围：<br>- “Active（正常）”：链路正常传输数据业务<br>- “Inactive（故障）”：链路不可用无法传输数据业务<br>- “Initial（初始态）”：链路新增即将被建立<br>- “Aging（老化）”：链路在老化定时器超时时间内无数据业务<br>- “Overload（过载）”：链路在单位时间内的数据传输量过大，传输数据业务受控<br>默认值：无<br>配置原则：无 |
| GLOBALPROCESSID | 全局进程标识 | 可选必选说明：该参数在"ENTITYTYPE"配置为"Server"、"Client"时为条件可选参数。<br>参数含义：该参数用于指定HTTP进程的全局进程标识。输入HTTP进程标识，可以查询该进程上的链路信息。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~16。<br>默认值：无<br>配置原则：无 |
| PODNAME | POD名称 | 可选必选说明：该参数在"ENTITYTYPE"配置为"Server"、"Client"时为条件可选参数。<br>参数含义：该参数用于指定POD名称。输入SBIM POD名称，可以查询该POD上的链路信息。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~255。<br>默认值：无<br>配置原则：无 |
| PSKGRPIDX | 预共享密钥组索引 | 可选必选说明：该参数在"ENTITYTYPE"配置为"Server"、"Client"时为条件可选参数。<br>参数含义：在使用预共享密钥认证情况下，该参数指定了链路所关联的预共享密钥组。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~128。<br>默认值：无<br>配置原则：无 |
| PSKID | 预共享密钥标识 | 可选必选说明：该参数在"ENTITYTYPE"配置为"Server"、"Client"时为条件可选参数。<br>参数含义：在使用预共享密钥认证情况下，该参数指定了链路所关联的预共享密钥标识。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~128。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/SBILINKSTATUS]] · 服务化接口链路状态（SBILINKSTATUS）

## 使用实例

运营商想查询本端NF角色是客户端的所有链路信息。

```
DSP SBILINKSTATUS: ENTITYTYPE=Client;

%%DSP SBILINKSTATUS: ENTITYTYPE=Client;%%
RETCODE = 0  操作成功

结果如下
--------
      本端NF角色  =  Client
      链路集标识  =  35_4_5ec90af147e52032af99030000000001_8_aef006bd
          链路ID  =  0
        链路类型  =  Dynamic
      本端NF类型  =  NFTypeSMF
      对端NF类型  =  NFTypeAMF
    对端NF实例ID  =  5ec90af1-47e5-2032-af99-030000000001
  对端NF服务名称  =  Invalid
  对端服务实例ID  =  NULL
        本端地址  =  192.168.186.106:24790
        对端地址  =  192.168.186.5:5001
            模式  =  HTTPS
        链路状态  =  正常
当前已用StreamId  =  6563
    最大StreamId  =  0
            策略  =  turns
            权重  =  0
    链路重建次数  =  0
          优先级  =  0
        链路负载  =  20
    全局进程标识  =  3
         POD名称  =  vusn-pod-0
预共享密钥组索引  =  0
  预共享密钥标识  =  NULL
      证书序列号  =  NULL
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询服务化接口链路状态（DSP-SBILINKSTATUS）_29213281.md`
