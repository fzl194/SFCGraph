---
id: UNC@20.15.2@MMLCommand@ADD TNFINS
type: MMLCommand
name: ADD TNFINS（增加目标NF实例）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: TNFINS
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
- 目标NF实例管理
status: active
---

# ADD TNFINS（增加目标NF实例）

## 功能

**适用NF：AMF、SMF、NSSF、SMSF、NCG**

该命令用于增加目标NF实例的配置。

## 注意事项

- 该命令执行后立即生效。

- 该命令配置时，如果在ADD PNFPROFILE中配置了相同的CHF，即ADD TNFINS中的参数TNFINSNAME和ADD PNFPROFILE中的参数NFINSTANCEID取值相同，则该命令关联的ADD TNFINSIP下配置的所有IP，需要被ADD PNFPROFILE中配置的CHF的IP包含。
- 当命令中的SRVINSID为空时，判断命令中TNFINSNAME的长度，长度小于等于50则使用TNFINSNAME的值填入SRVINSID中，否则将SRVINSID置为NULL。

- 最多可输入2048条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TNFINSINDEX | 目标NF实例索引 | 可选必选说明：必选参数<br>参数含义：本参数用于指定目标NF实例索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~2047。<br>默认值：无<br>配置原则：无 |
| TNFTYPE | 目标NF类型 | 可选必选说明：必选参数<br>参数含义：本参数用于指定目标NF类型。<br>数据来源：全网规划<br>取值范围：<br>- “CHF（CHF）”：CHF<br>- “UPF（UPF）”：UPF<br>- “PCSCF（PCSCF）”：PCSCF<br>- “PCF（PCF）”：PCF<br>默认值：无<br>配置原则：无 |
| TNFINSNAME | 目标NF实例名称 | 可选必选说明：必选参数<br>参数含义：本参数用于指定目标NF实例名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~63。<br>默认值：无<br>配置原则：<br>- 该参数不允许配置完全重复的记录。<br>- UUID格式为32个BCD码，不包含连字号。即以连字号分为五段，形式为8-4-4-4-12的16进制的32位字符串。例如，a6a61c6f-0d3a-4221-b1da-424eda3ccf67。<br>- 该参数不允许配置非UUID格式的前18位字符与数据库中所有存储的非UUID格式的TNFINSNAME的相同的记录。<br>- 此参数不区分大小写。<br>- 该参数与PNFPROFILE命令中的NFINSTANCEID参数一致时，关联关系生效。 |
| SRVNAME | 服务名称 | 可选必选说明：可选参数<br>参数含义：本参数用于指定目标NF的服务名称。<br>数据来源：全网规划<br>取值范围：<br>- NrfNfm（NRF提供的Nnrf_NFManagement服务）<br>- NnrfDisc（NRF提供的Nnrf_NFDiscovery服务）<br>- NudmSdm（UDM提供的Nudm_SubscriberDataManagement服务）<br>- NudmUecm（UDM提供的Nudm_UEContextManagement服务）<br>- NudmUeau（UDM提供的Nudm_UEAuthentication服务）<br>- NudmEe（UDM提供的Nudm_EventExposure服务）<br>- NudmPp（UDM提供的Nudm_ParameterProvision服务）<br>- NamfComm（AMF提供的Namf_Communication Service服务）<br>- NamfEvts（AMF提供的Namf_EventExposure服务）<br>- NamfMt（AMF提供的Namf_MT服务）<br>- NamfLoc（AMF提供的Namf_Location服务）<br>- NsmfPduSes（SMF提供的Nsmf_PDUSession服务）<br>- NsmfEventExp（SMF提供的Nsmf_EventExposure服务）<br>- NausfAuth（AUSF提供的Nausf_UEAuthentication服务）<br>- NausfSorprot（AUSF提供的Nausf_SoRPProtection服务）<br>- NnefPfdMgnt（NEF提供的Nnef_PFDManagement）<br>- NpcfAmPlcCtrl（PCF提供的Npcf_AMPolicyControl服务）<br>- NpcfSmplcCtrl（PCF提供的Npcf_SMPolicyControl服务）<br>- NpcfPlcAuth（PCF提供的Npcf_PolicyAuthorization服务）<br>- NpcfBdtplcCtrl（PCF提供的Npcf_BDTPolicyControl服务）<br>- NpcfEventEx（PCF提供的Npcf_EventExposure服务）<br>- NpcfUePcy（PCF提供的Npcf_UEPolicyControl服务）<br>- NsmsfSms（SMSF提供的Nsmsf_SMService服务）<br>- NnssfNsSel（NSSF提供的Nnssf_NSSelection服务）<br>- NnssfNssaiAvai（NSSF提供的Nnssf_NSSAIAvailability服务）<br>- NudrDr（UDR提供的Nudr_DataRepository服务）<br>- NlmfLoc（LMF提供的Nlmf_Location服务）<br>- N5gEirEic（5G-EIR提供的N5g-eir_EquipmentIdentityCheck服务）<br>- NbsfMgnt（BSF提供的Nbsf_Management服务）<br>- NchfSpdlmtCtrl（CHF提供的Nchf_SpendingLimitControl服务）<br>- NchfConvCharg（CHF提供的Nchf_Converged_Charging服务）<br>- NnwdafEvntSubs（NWDAF提供的Nnwdaf_EventsSubscription服务）<br>- NnwdafAnalInfo（NWDAF提供的Nnwdaf_AnalyticsInfo服务）<br>- NocsSpdLmtCtrl（NocsSpdLmtCtrl）<br>- NocsConvCharg（NocsConvCharg）<br>- NgmlcLoc（GMLC提供的Ngmlc_Location Service）<br>- SrvNameINVALID（Invalid Service Name）<br>- SrvNameMAX（Max Service Name）<br>- NamfMbsBroadcast（AMF提供的Namf_MbsBroadcast服务）<br>- NmbSmfTmgi（MBSMF提供的NmbSmf_Tmgi服务）<br>- NmbSmfMbssession（MBSMF提供的NmbSmf_Mbssession服务）<br>- NudnDm（UDN提供的Nudn_DataManagement服务）<br>- NnefSmCtx（NEF提供的Nnef_SMContext服务）<br>- NnwdafDataManagement（NWDAF提供的Nnwdaf_DataManagement服务）<br>默认值：无<br>配置原则：无 |
| SRVINSID | 服务实例标识 | 可选必选说明：可选参数<br>参数含义：本参数用于指定目标NF的服务实例标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~50。<br>默认值：无<br>配置原则：无 |
| SCHEMA | 协议模式 | 可选必选说明：可选参数<br>参数含义：本参数用于指定目标NF通信的协议模式。<br>数据来源：全网规划<br>取值范围：<br>- “UriSchemeINVALID（SchemaInvalid）”：已废弃。<br>- “http（http）”：http<br>- “https（https）”：https<br>- “UriSchemeMAX（SchemaMax）”：已废弃。<br>默认值：无<br>配置原则：<br>建议本端和对端的协议模式一致。否则，无法建立HTTP链接。注意：当设置为“UriSchemeINVALID”和“UriSchemeMAX”时，协议模式默认以“http”方式生效。 |
| FQDN | 域名 | 可选必选说明：可选参数<br>参数含义：本参数用于指定目标NF的域名。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~127。不区分大小写。<br>默认值：无<br>配置原则：<br>- FQDN由一个或多个LABEL构成，各LABEL间用“.”间隔。<br>- 每个LABEL的构成字符只能是字母A～Z或a～z、数字0～9和中划线“-”。例如：amf1.cluster1.net2.amf.5gc.mnc012.mcc345.3gppnetwork.org |
| NFDESCNAME | NF描述名称 | 可选必选说明：可选参数<br>参数含义：该参数用于表示NF实例的描述信息。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~255。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@TNFINS]] · 目标NF实例（TNFINS）

## 使用实例

运营商A需要添加目标NF实例:索引为1，NF类型为CHF，支持的协议为http，目标NF实例名称为target_chf_0，域名为huawei.com。

```
ADD TNFINS: TNFINSINDEX=1, TNFTYPE=CHF, SCHEMA=http,TNFINSNAME="target_chf_0",FQDN="huawei.com";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-TNFINS.md`
