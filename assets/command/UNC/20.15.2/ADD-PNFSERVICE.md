---
id: UNC@20.15.2@MMLCommand@ADD PNFSERVICE
type: MMLCommand
name: ADD PNFSERVICE（增加对端NF服务实例信息）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: PNFSERVICE
command_category: 配置类
applicable_nf:
- AMF
- SMF
- NSSF
- SMSF
- NCG
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 服务化接口管理
- 注册与服务发现
- 本地NRF功能管理
- 对端服务实例信息管理
status: active
---

# ADD PNFSERVICE（增加对端NF服务实例信息）

## 功能

**适用NF：AMF、SMF、NSSF、SMSF、NCG**

该命令用于增加本地配置对端NF实例支持的服务实例信息。该命令用于在网络中没有部署NRF，或对端NF没有注册到NRF，或网络中存在NRF但需基于运营商策略本地配置周边NF的场景下，配置对端NF实例相关的信息。

## 注意事项

- 该命令执行后立即生效。

- 由于SCP不需要提供服务，当配置中的NF实例类型为NFSCP时，命令会执行失败。

- 最多可输入1024条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFINSTANCEID | NF实例标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定NF实例标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~50。NFINSTANCEID参数建议满足以下约束规则：1.如果输入为uuid格式（格式例如：a6a61c6f-0d3a-4221-b1da-424eda3ccf67）只能为A-F、a-f、0-9和“-”的字符。2.如果输入不为uuid格式，长度不能超过18且不允许输入只包含0-9和“.”的字符串，例如：1.2.3.4、不允许输入只包含十六进制数（A-F、a-f、0-9）和“:”的字符串，例如：1::2、FBFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF。<br>默认值：无<br>配置原则：<br>本参数取值与ADD PNFPROFILE命令中的“NF实例标识”参数取值保持一致时，关联关系生效。 |
| SRVINSTANCEID | 服务实例标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定服务实例标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~50。大小写不敏感。<br>默认值：无<br>配置原则：无 |
| SERVICENAME | 服务名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定服务名称。<br>数据来源：全网规划<br>取值范围：<br>- NrfNfm（NRF提供的Nnrf_NFManagement服务）<br>- NnrfDisc（NRF提供的Nnrf_NFDiscovery服务）<br>- NudmSdm（UDM提供的Nudm_SubscriberDataManagement服务）<br>- NudmUecm（UDM提供的Nudm_UEContextManagement服务）<br>- NudmUeau（UDM提供的Nudm_UEAuthentication服务）<br>- NudmEe（UDM提供的Nudm_EventExposure服务）<br>- NudmPp（UDM提供的Nudm_ParameterProvision服务）<br>- NamfComm（AMF提供的Namf_Communication Service服务）<br>- NamfEvts（AMF提供的Namf_EventExposure服务）<br>- NamfMt（AMF提供的Namf_MT服务）<br>- NamfLoc（AMF提供的Namf_Location服务）<br>- NsmfPduSes（SMF提供的Nsmf_PDUSession服务）<br>- NsmfEventExp（SMF提供的Nsmf_EventExposure服务）<br>- NausfAuth（AUSF提供的Nausf_UEAuthentication服务）<br>- NausfSorprot（AUSF提供的Nausf_SoRPProtection服务）<br>- NnefPfdMgnt（NEF提供的Nnef_PFDManagement）<br>- NpcfAmPlcCtrl（PCF提供的Npcf_AMPolicyControl服务）<br>- NpcfSmplcCtrl（PCF提供的Npcf_SMPolicyControl服务）<br>- NpcfPlcAuth（PCF提供的Npcf_PolicyAuthorization服务）<br>- NpcfBdtplcCtrl（PCF提供的Npcf_BDTPolicyControl服务）<br>- NpcfEventEx（PCF提供的Npcf_EventExposure服务）<br>- NpcfUePcy（PCF提供的Npcf_UEPolicyControl服务）<br>- NsmsfSms（SMSF提供的Nsmsf_SMService服务）<br>- NnssfNsSel（NSSF提供的Nnssf_NSSelection服务）<br>- NnssfNssaiAvai（NSSF提供的Nnssf_NSSAIAvailability服务）<br>- NudrDr（UDR提供的Nudr_DataRepository服务）<br>- NlmfLoc（LMF提供的Nlmf_Location服务）<br>- N5gEirEic（5G-EIR提供的N5g-eir_EquipmentIdentityCheck服务）<br>- NbsfMgnt（BSF提供的Nbsf_Management服务）<br>- NchfSpdlmtCtrl（CHF提供的Nchf_SpendingLimitControl服务）<br>- NchfConvCharg（CHF提供的Nchf_Converged_Charging服务）<br>- NnwdafEvntSubs（NWDAF提供的Nnwdaf_EventsSubscription服务）<br>- NnwdafAnalInfo（NWDAF提供的Nnwdaf_AnalyticsInfo服务）<br>- NocsSpdLmtCtrl（NocsSpdLmtCtrl）<br>- NocsConvCharg（NocsConvCharg）<br>- NgmlcLoc（GMLC提供的Ngmlc_Location Service）<br>- SrvNameINVALID（Invalid Service Name）<br>- SrvNameMAX（Max Service Name）<br>- NamfMbsBroadcast（AMF提供的Namf_MbsBroadcast服务）<br>- NmbSmfTmgi（MBSMF提供的NmbSmf_Tmgi服务）<br>- NmbSmfMbssession（MBSMF提供的NmbSmf_Mbssession服务）<br>- NudnDm（UDN提供的Nudn_DataManagement服务）<br>- NnefSmCtx（NEF提供的Nnef_SMContext服务）<br>- NnwdafDataManagement（NWDAF提供的Nnwdaf_DataManagement服务）<br>默认值：无<br>配置原则：无 |
| SCHEMA | 协议模式 | 可选必选说明：必选参数<br>参数含义：该参数用于指定协议模式。<br>数据来源：全网规划<br>取值范围：<br>- “UriSchemeINVALID（SchemaInvalid）”：已废弃。<br>- “http（http）”：http<br>- “https（https）”：https<br>- “UriSchemeMAX（SchemaMax）”：已废弃。<br>默认值：无<br>配置原则：<br>本端和对端要配置保持一致，如不一致，会导致HTTP的链路建立失败。 |
| NFSERVICESTATUS | 服务实例状态 | 可选必选说明：可选参数<br>参数含义：该参数用于指定服务实例状态。<br>数据来源：全网规划<br>取值范围：<br>- “INVALID（INVALID）”：表示当前NFS实例处于无效态，如果配置成该值，NF选择时不会选择此类NFS。<br>- “REGISTERED（REGISTERED）”：表示当前NFS实例处于注册态，如果配置成该值，NF选择时只会选择此类NFS。<br>- “SUSPENDED（SUSPENDED）”：表示当前NFS实例处于挂起态。当NFS实例处于运维状态下，比如正在进行用户迁移等，不希望在NF发现流程中被选中时，可以置为此状态，迁移完毕后通过该命令对应的MOD命令修改为注册态即可。<br>- “DEREGISTERED（DEREGISTERED）”：表示当前NFS实例处于去注册态，如果配置成该值，NF选择时不会选择此类NFS。<br>- “UNDISCOVERABLE（UNDISCOVERABLE）”：表示当前NFS实例处于不可被发现状态，如果配置成该值，NF选择时不会选择此类NFS。<br>默认值：REGISTERED<br>配置原则：<br>建议配置成Registered，如果配置成其它状态NF服务发现时不会被选中。 |
| FQDN | 域名 | 可选必选说明：可选参数<br>参数含义：该参数用于指定NF服务实例的域名。本参数指定的域名中可以不包含PLMN信息，主要用于本网内的域名查询场景。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~255。不区分大小写。<br>默认值：无<br>配置原则：<br>- FQDN由一个或多个LABEL构成，各LABEL间用“.”间隔。<br>- 每个LABEL的构成字符只能是字母A～Z或a～z、数字0～9和中划线“-”。<br>- 例如，amf1.cluster1.net2.amf.5gc.mnc012.mcc345.3gppnetwork.org |
| INTERPLMNFQDN | PLMN间域名 | 可选必选说明：可选参数<br>参数含义：该参数用于指定PLMN间域名。当NF涉及跨PLMN网络间的NFS发现时，需要为NFS配置“PLMN间域名”。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~255。不区分大小写。<br>默认值：无<br>配置原则：<br>- INTERPLMNFQDN由一个或多个LABEL构成，各LABEL间用“.”间隔。<br>- 每个LABEL的构成字符只能是字母A～Z或a～z、数字0～9、中划线“-”和下划线"_"。<br>- 例如，amf1.cluster1.net2.amf.5gc.mnc012.mcc345.3gppnetwork.org |
| APIPREFIX | API路径前缀 | 可选必选说明：可选参数<br>参数含义：本参数用于指定服务实例的API路径前缀。以满足特殊场景下其他NF以API root路径直接访问该NFS。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~150。<br>默认值：无<br>配置原则：<br>本参数的构成字符只能是字母A～Z或a～z、数字0～9。 |
| PRIORITY | 优先级 | 可选必选说明：可选参数<br>参数含义：本参数用于指定服务实例的优先级（与其他同类型NF实例的NFS相比）。在NF选择过程中，NF会选择高优先级的NFS，如果两个或多个NFS的优先级一样，NF则会根据“容量”做进一步的判断。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~65535。值越小优先级越高。<br>默认值：无<br>配置原则：无 |
| CAPACITY | 容量 | 可选必选说明：可选参数<br>参数含义：本参数用于指定NFS的相对权重（与其他同类型NF实例的NFS相比）。特别地，如果NFS容量的绝对值不超过本参数的取值范围，那么本参数可以直接取用容量绝对值。例如AMF可接入的用户数是50000，那么该AMF的容量就可以用50000表示。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~65535。值越大表示容量越大。<br>默认值：100<br>配置原则：无 |
| LOAD | 负载 | 可选必选说明：可选参数<br>参数含义：本参数用于指定NFS的负载。系统可能会将此参数作为NF选择的依据。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~100。值越大表示负载越大。<br>默认值：无<br>配置原则：无 |
| SUPFEATURES | 支持的功能 | 可选必选说明：可选参数<br>参数含义：该参数用于指定服务支持的功能。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~150。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/PNFSERVICE]] · 对端NF服务实例信息（PNFSERVICE）

## 使用实例

增加对端NF的服务实例信息，NF实例标识为SMF_Instance_0，服务实例标识为Service_Instance_0，服务名为NsmfPduSes，支持的协议为http。

```
ADD PNFSERVICE: NFINSTANCEID="SMF_Instance_0", SRVINSTANCEID="Service_Instance_0", SERVICENAME=NsmfPduSes, SCHEMA=http, NFSERVICESTATUS=REGISTERED;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加对端NF服务实例信息（ADD-PNFSERVICE）_09652978.md`
