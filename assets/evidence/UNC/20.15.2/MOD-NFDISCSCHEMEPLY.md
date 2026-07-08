# 修改服务发现Scheme优选策略（MOD NFDISCSCHEMEPLY）

- [命令功能](#ZH-CN_MMLREF_0000001357496929__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0000001357496929__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0000001357496929__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0000001357496929__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0000001357496929)

**适用NF：AMF、SMF、NSSF、SMSF、NCG**

该命令用于修改服务发现时的Scheme优选策略。

## [注意事项](#ZH-CN_MMLREF_0000001357496929)

该命令执行后立即生效。

#### [操作用户权限](#ZH-CN_MMLREF_0000001357496929)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0000001357496929)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| INFOTYPE | 信息类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定信息类型。<br>数据来源：本端规划<br>取值范围：<br>- “BYNFTYPE（使用NF类型）”：输入NF类型<br>- “BYNFID（使用NF实例标识）”：输入NF实例标识<br>默认值：无<br>配置原则：无 |
| NFTYPE | NF类型 | 可选必选说明：该参数在"INFOTYPE"配置为"BYNFTYPE"时为条件必选参数。<br>参数含义：该参数用于指定NF类型。<br>数据来源：全网规划<br>取值范围：<br>- “NfInvalid（NfInvalid）”：NfInvalid<br>- “NfNRF（NfNRF）”：NfNRF<br>- “NfUDM（NfUDM）”：NfUDM<br>- “NfAMF（NfAMF）”：NfAMF<br>- “NfSMF（NfSMF）”：NfSMF<br>- “NfAUSF（NfAUSF）”：NfAUSF<br>- “NfNEF（NfNEF）”：NfNEF<br>- “NfPCF（NfPCF）”：NfPCF<br>- “NfSMSF（NfSMSF）”：NfSMSF<br>- “NfNSSF（NfNSSF）”：NfNSSF<br>- “NfUDR（NfUDR）”：NfUDR<br>- “NfLMF（NfLMF）”：NfLMF<br>- “NfGMLC（NfGMLC）”：NfGMLC<br>- “Nf5G_EIR（Nf5G_EIR）”：Nf5G_EIR<br>- “NfSEPP（NfSEPP）”：NfSEPP<br>- “NfUPF（NfUPF）”：NfUPF<br>- “NfN3IWF（NfN3IWF）”：NfN3IWF<br>- “NfAF（NfAF）”：NfAF<br>- “NfUDSF（NfUDSF）”：NfUDSF<br>- “NfBSF（NfBSF）”：NfBSF<br>- “NfCHF（NfCHF）”：NfCHF<br>- “NfCUSTOM_OCS（NfCUSTOM_OCS）”：NfCUSTOM_OCS<br>- “NfSCP（NfSCP）”：NfSCP<br>- “NfPCSCF（NfPCSCF）”：NfPCSCF<br>- “NfMBSMF（NfMBSMF）”：NfMBSMF<br>- “NfUDN（NfUDN）”：NfUDN<br>- “NfNWDAF（NfNWDAF）”：NfNWDAF<br>默认值：无<br>配置原则：无 |
| NFINSTANCEID | NF实例标识 | 可选必选说明：该参数在"INFOTYPE"配置为"BYNFID"时为条件必选参数。<br>参数含义：该参数用于指定NF实例标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~36。NFINSTANCEID参数必须满足以下约束规则：1.如果输入为uuid格式（格式例如：a6a61c6f-0d3a-4221-b1da-424eda3ccf67）只能为A-F、a-f、0-9和“-”的字符。2.如果输入不为uuid格式，长度不能超过18且不允许输入只包含0-9和“.”的字符串，例如：1.2.3.4、不允许输入只包含十六进制数（A-F、a-f、0-9）和“:”的字符串，例如：1::2、FBFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF。3.不区分大小写。<br>默认值：无<br>配置原则：无 |
| SERVICENAME | 服务名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定ServiceName。<br>数据来源：全网规划<br>取值范围：<br>- SrvNameALL（SrvNameALL）<br>- NudmSdm（UDM提供的Nudm_SubscriberDataManagement服务）<br>- NudmUecm（UDM提供的Nudm_UEContextManagement服务）<br>- NudmUeau（UDM提供的Nudm_UEAuthentication服务 ）<br>- NudmEe（UDM提供的Nudm_EventExposure服务）<br>- NudmPp（UDM提供的Nudm_ParameterProvision服务）<br>- NamfComm（AMF提供的Namf_Communication Service服务）<br>- NamfEvts（AMF提供的Namf_EventExposure服务）<br>- NamfMt（AMF提供的Namf_MT服务）<br>- NamfLoc（AMF提供的Namf_Location服务）<br>- NsmfPduSes（SMF提供的Nsmf_PDUSession服务）<br>- NsmfEventExp（SMF提供的Nsmf_EventExposure服务）<br>- NausfAuth（AUSF提供的Nausf_UEAuthentication服务）<br>- NausfSorprot（AUSF提供的Nausf_SoRPProtection服务）<br>- NnefPfdMgnt（NEF提供的Nnef_PFDManagement）<br>- NpcfAmPlcCtrl（PCF提供的Npcf_AMPolicyControl服务）<br>- NpcfSmplcCtrl（PCF提供的Npcf_SMPolicyControl服务）<br>- NpcfPlcAuth（PCF提供的Npcf_PolicyAuthorization服务）<br>- NpcfBdtplcCtrl（PCF提供的Npcf_BDTPolicyControl服务）<br>- NpcfEventEx（PCF提供的Npcf_EventExposure服务）<br>- NpcfUePcy（PCF提供的Npcf_UEPolicyControl服务）<br>- NsmsfSms（SMSF提供的Nsmsf_SMService服务）<br>- NnssfNsSel（NSSF提供的Nnssf_NSSelection服务）<br>- NnssfNssaiAvai（NSSF提供的Nnssf_NSSAIAvailability服务）<br>- NudrDr（UDR提供的Nudr_DataRepository服务）<br>- NlmfLoc（LMF提供的Nlmf_Location服务）<br>- N5gEirEic（5G-EIR提供的N5g-eir_EquipmentIdentityCheck服务）<br>- NbsfMgnt（BSF提供的Nbsf_Management服务）<br>- NchfSpdlmtCtrl（CHF提供的Nchf_SpendingLimitControl服务）<br>- NchfConvCharg（CHF提供的Nchf_Converged_Charging服务）<br>- NnwdafEvntSubs（NWDAF提供的Nnwdaf_EventsSubscription服务）<br>- NnwdafAnalInfo（NWDAF提供的Nnwdaf_AnalyticsInfo服务）<br>- NocsSpdLmtCtrl（NocsSpdLmtCtrl）<br>- NocsConvCharg（NocsConvCharg）<br>- NgmlcLoc（GMLC提供的Ngmlc_Location Service）<br>- NamfMbsBroadcast（AMF提供的Namf_MbsBroadcast服务）<br>- NmbSmfTmgi（MBSMF提供的NmbSmf_Tmgi服务）<br>- NmbSmfMbssession（MBSMF提供的NmbSmf_Mbssession服务）<br>- NudnDm（UDN提供的Nudn_DataManagement服务）<br>默认值：无<br>配置原则：无 |
| POLICY | 策略 | 可选必选说明：必选参数<br>参数含义：该参数用于指定Scheme优选策略。<br>数据来源：全网规划<br>取值范围：<br>- “NO_DIFF（无差别）”：无差别选择使用HTTP或HTTPS的服务<br>- “HTTP_ONLY（仅HTTP）”：仅选择使用HTTP的服务<br>- “HTTPS_ONLY（仅HTTPS）”：仅选择使用HTTPS的服务<br>- “HTTP_FIRST（HTTP优先）”：优先选择使用HTTP的服务<br>- “HTTPS_FIRST（HTTPS优先）”：优先选择使用HTTPS的服务<br>默认值：无<br>配置原则：<br>仅在本端网元作为客户端支持HTTP或HTTPS时，才能将策略配置为“HTTP_ONLY”或“HTTPS_ONLY”；仅在本端网元作为客户端支持HTTP及HTTPS时，才能将策略配置为“HTTP_FIRST”或“HTTPS_FIRST”。 |

## [使用实例](#ZH-CN_MMLREF_0000001357496929)

- 修改NF类型为UDM，服务名称为NudmSdm的Scheme优选策略记录，将策略设置为HTTP_FIRST。
  ```
  %%MOD NFDISCSCHEMEPLY: INFOTYPE=BYNFTYPE, NFTYPE=NfUDM, SERVICENAME=NudmSdm, POLICY=HTTP_FIRST;%%
  RETCODE = 0  操作成功

  ---    END
  ```
- 修改NF实例标识为smf_Instance_0，服务名称为NudmSdm的Scheme优选策略记录，将策略设置为HTTPS_FIRST。
  ```
  %%MOD NFDISCSCHEMEPLY: INFOTYPE=BYNFID, NFINSTANCEID="smf_instance_0", SERVICENAME=NsmfPduSes, POLICY=HTTPS_FIRST;%%
  RETCODE = 0  操作成功

  ---    END
  ```
