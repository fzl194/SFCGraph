# 测试服务发现的NF信息（TST NRF）

- [命令功能](#ZH-CN_MMLREF_0000001146812823__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0000001146812823__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0000001146812823__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0000001146812823__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0000001146812823)

**适用NF：AMF、SMF、SMSF、NCG、NSSF**

该命令用于查询服务发现的NF信息。如果使用NFInstanceID查询，则选择NFTYPE，其他参数不填，返回该NF Profile；否则输入NFSELECT和其他参数，返回匹配的NF列表。

## [注意事项](#ZH-CN_MMLREF_0000001146812823)

- 不要仅以NFSELECT、SERVICENAME为输入参数测试服务发现，必须携带额外的参数，防止向NRF测试服务发现后，NRF需要返回所有满足条件的对端网元，造成突发大包，影响性能。
- 当服务发现类型为SCP时，需要将SERVICENAME设置为“SrvNameINVALID”。
- 当QUERYTYPE为BYPARAS时，按以下规则判断是否能服务发现。
- 如果TAILIST不为空，或者当DATASOURCE既不为NORMAL也不为NRF_ONLY，或者软参DWORD4 BIT28的值为0，能正常服务发现。
- 如果以上条件都不满足时，NFSELECT中不同NFTYPE根据以下规则判断是否能服务发现。

- 1.当NFSELECT设置为BSF时，IPV4和IPV6不能同时为空，否则无法进行服务发现。
- 2. 当NFSELECT设置为SMF时，FQDN，TAI，SERVINGSCOPE和PGWFQDN不能同时为空，否则无法进行服务发现。
- 3. 当NFSELECT设置为UDM时，SUPI不能为空，否则无法进行服务发现。
- 4. 当NFSELECT设置为SMSF，SCP或者NWDAF时，都能进行服务发现。
- 5. 当NFSELECT设置为PCF时
- 5.1. 如果SERVINGSCOPE不为空，能进行服务发现。
- 5.2. 如果SERVINGSCOPE为空时，根据软参DWORD4 BIT29 判断是否限制根据SUPI或GPSI查询PCF。
- 5.2.1 如果软参值为0时，只允许GPSI查询PCF，GPSI不能为空，否则无法进行服务发现。
- 5.2.2 如果软参值为1时，只允许SUPI查询PCF，SUPI不能为空，否则无法进行服务发现。
- 6. 当NFSELECT设置为其他NFTYPE时，SUPI，GPSI，FQDN，TAI，GUAMI，AMFREGIONID，SERVINGSCOPE，PGWFQDN，IPV4，IPV6，IPDOMAIN，ROUTINGID和AMFSETID不能同时为空，否则无法进行服务发现。

#### [操作用户权限](#ZH-CN_MMLREF_0000001146812823)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## [参数说明](#ZH-CN_MMLREF_0000001146812823)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DATASOURCE | 服务发现数据源 | 可选必选说明：必选参数<br>参数含义：该参数用于指定服务发现的数据源。<br>数据来源：本端规划<br>取值范围：<br>- “NORMAL（标准服务发现）”：根据NFDISCPLCY配置的服务发现策略查询。<br>- LOCAL_ONLY（仅在本地配置上查找）<br>- CACHE_ONLY（仅在cache上查找）<br>- NRF_ONLY（仅在远端NRF查询）<br>默认值：无<br>配置原则：<br>若按照标准服务发现策略，如果在某一数据来源中首次找到匹配服务发现条件的网元，则返回结果，不继续查找。<br>若配置了参数TAILIST，该参数不能配置为NRF_ONLY，当配置为NORMAL时，服务发现策略和NFDISCPLCY的参数MBSMFPOLICY保持一致。 |
| QUERYTYPE | 查询方式 | 可选必选说明：必选参数<br>参数含义：该参数用于指定查询策略。<br>数据来源：本端规划<br>取值范围：<br>- “BYNFID（使用NF InstanceID查询）”：输入NFInstanceID和NFType。<br>- “BYPARAS（使用参数组合进行查询）”：使用NFType和其他参数组合查询，不需要输入NFInstanceID。<br>默认值：无<br>配置原则：<br>使用NF InstanceID查询方式：输入NFInstanceID和NFType。使用参数组合进行查询方式：使用NFType和其他参数组合查询，不需要输入NFInstanceID。 |
| DEBUGSWITCH | 调测定位开关 | 可选必选说明：该参数在"QUERYTYPE"配置为"BYPARAS"时为条件可选参数。<br>参数含义：该参数用于指定查询策略为NFPARAS时是否输出辅助日志。设置此参数为ON即会输出参数过滤环节的debug结果，概述每个参数过滤后的剩余网元概况。设置此参数为OFF，则不输出结果。<br>数据来源：本端规划<br>取值范围：<br>- “OFF（OFF）”：功能关闭<br>- “ON（ON）”：功能开启<br>默认值：OFF<br>配置原则：无 |
| NFSELECT | 网元类型 | 可选必选说明：该参数在"QUERYTYPE"配置为"BYPARAS"时为条件必选参数。<br>参数含义：该参数用于指定待查询的NF类型。<br>数据来源：全网规划<br>取值范围：<br>- UDM（UDM）<br>- PCF（PCF）<br>- AMF（AMF）<br>- SMF（SMF）<br>- BSF（BSF）<br>- SMSF（SMSF）<br>- AUSF（AUSF）<br>- NSSF（NSSF）<br>- SCP（SCP）<br>- LMF（LMF）<br>- NWDAF（NWDAF）<br>默认值：无<br>配置原则：无 |
| NFTYPE | 网元类型 | 可选必选说明：该参数在"QUERYTYPE"配置为"BYNFID"时为条件必选参数。<br>参数含义：该参数用于指定待查询的NF类型。<br>数据来源：全网规划<br>取值范围：<br>- UDM（UDM）<br>- PCF（PCF）<br>- AMF（AMF）<br>- SMF（SMF）<br>- BSF（BSF）<br>- SMSF（SMSF）<br>- AUSF（AUSF）<br>- NSSF（NSSF）<br>- SCP（SCP）<br>- LMF（LMF）<br>- NWDAF（NWDAF）<br>默认值：无<br>配置原则：无 |
| SERVICENAME | SERVICENAME | 可选必选说明：该参数在"QUERYTYPE"配置为"BYNFID"、"BYPARAS"时为条件必选参数。<br>参数含义：该参数用于指定服务名称。<br>数据来源：本端规划<br>取值范围：<br>- NrfNfm（NRF提供的Nnrf_NFManagement服务）<br>- NnrfDisc（NRF提供的Nnrf_NFDiscovery服务）<br>- NudmSdm（UDM提供的Nudm_SubscriberDataManagement服务）<br>- NudmUecm（UDM提供的Nudm_UEContextManagement服务）<br>- NudmUeau（UDM提供的Nudm_UEAuthentication服务）<br>- NudmEe（UDM提供的Nudm_EventExposure服务）<br>- NudmPp（UDM提供的Nudm_ParameterProvision服务）<br>- NamfComm（AMF提供的Namf_Communication Service服务）<br>- NamfEvts（AMF提供的Namf_EventExposure服务）<br>- NamfMt（AMF提供的Namf_MT服务）<br>- NamfLoc（AMF提供的Namf_Location服务）<br>- NsmfPduSes（SMF提供的Nsmf_PDUSession服务）<br>- NsmfEventExp（SMF提供的Nsmf_EventExposure服务）<br>- NausfAuth（AUSF提供的Nausf_UEAuthentication服务）<br>- NausfSorprot（AUSF提供的Nausf_SoRPProtection服务）<br>- NnefPfdMgnt（NEF提供的Nnef_PFDManagement）<br>- NpcfAmPlcCtrl（PCF提供的Npcf_AMPolicyControl服务）<br>- NpcfSmplcCtrl（PCF提供的Npcf_SMPolicyControl服务）<br>- NpcfPlcAuth（PCF提供的Npcf_PolicyAuthorization服务）<br>- NpcfBdtplcCtrl（PCF提供的Npcf_BDTPolicyControl服务）<br>- NpcfEventEx（PCF提供的Npcf_EventExposure服务）<br>- NpcfUePcy（PCF提供的Npcf_UEPolicyControl服务）<br>- NsmsfSms（SMSF提供的Nsmsf_SMService服务）<br>- NnssfNsSel（NSSF提供的Nnssf_NSSelection服务）<br>- NnssfNssaiAvai（NSSF提供的Nnssf_NSSAIAvailability服务）<br>- NudrDr（UDR提供的Nudr_DataRepository服务）<br>- NlmfLoc（LMF提供的Nlmf_Location服务）<br>- N5gEirEic（5G-EIR提供的N5g-eir_EquipmentIdentityCheck服务）<br>- NbsfMgnt（BSF提供的Nbsf_Management服务）<br>- NchfSpdlmtCtrl（CHF提供的Nchf_SpendingLimitControl服务）<br>- NchfConvCharg（CHF提供的Nchf_Converged_Charging服务）<br>- NnwdafEvntSubs（NWDAF提供的Nnwdaf_EventsSubscription服务）<br>- NnwdafAnalInfo（NWDAF提供的Nnwdaf_AnalyticsInfo服务）<br>- NocsSpdLmtCtrl（NocsSpdLmtCtrl）<br>- NocsConvCharg（NocsConvCharg）<br>- NgmlcLoc（GMLC提供的Ngmlc_Location Service）<br>- SrvNameINVALID（Invalid Service Name）<br>- SrvNameMAX（Max Service Name）<br>- NamfMbsBroadcast（AMF提供的Namf_MbsBroadcast服务）<br>- NmbSmfTmgi（MBSMF提供的NmbSmf_Tmgi服务）<br>- NmbSmfMbssession（MBSMF提供的NmbSmf_Mbssession服务）<br>- NudnDm（UDN提供的Nudn_DataManagement服务）<br>- NnefSmCtx（NEF提供的Nnef_SMContext服务）<br>- NnwdafDataManagement（NWDAF提供的Nnwdaf_DataManagement服务）<br>默认值：无<br>配置原则：无 |
| NFINSTANCEID | NF实例标识 | 可选必选说明：该参数在"QUERYTYPE"配置为"BYNFID"时为条件必选参数。<br>参数含义：该参数用于指定NF实例标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~50。<br>默认值：无<br>配置原则：<br>NFINSTANCEID参数建议满足以下约束规则：<br>- 如果输入为uuid格式（格式例如：a6a61c6f-0d3a-4221-b1da-424eda3ccf67）只能为A-F、a-f、0-9的字符。<br>- 如果输入不为uuid格式，长度不能超过18且不允许输入只包含0-9和“.”的字符串，例如：1.2.3.4、不允许输入只包含十六进制数（A-F、a-f、0-9）和“:”的字符串，例如：1::2、FBFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF。 |
| SUPI | SUPI | 可选必选说明：该参数在"NFSELECT"配置为"PCF"、"NSSF"、"UDM"、"SMF"、"AUSF"、"SMSF"、"LMF"时为条件可选参数。<br>参数含义：该参数用于指定SUPI。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是5~15。<br>默认值：无<br>配置原则：无 |
| GPSI | GPSI | 可选必选说明：该参数在"NFSELECT"配置为"PCF"、"NSSF"、"UDM"、"SMF"、"SMSF"、"LMF"时为条件可选参数。<br>参数含义：该参数用于指定GPSI。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是5~15。<br>默认值：无<br>配置原则：无 |
| PLMN | 目标方PLMN | 可选必选说明：该参数在"QUERYTYPE"配置为"BYNFID"时为条件可选参数。该参数在"NFSELECT"配置为"PCF"、"BSF"、"NSSF"、"UDM"、"SMF"、"AUSF"、"SMSF"、"AMF"、"LMF"时为条件可选参数。<br>参数含义：该参数用于指定待查询NF所在的PLMN。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是5~6。<br>默认值：无<br>配置原则：<br>PLMN由MCC和MNC组成，MCC为3个十进制数字，MNC为2~3个十进制数字。例如PLMN=“12345”，其中MCC=“123”， MNC=“45”。 |
| REQPLMN | 请求方PLMN | 可选必选说明：该参数在"QUERYTYPE"配置为"BYNFID"时为条件可选参数。该参数在"NFSELECT"配置为"PCF"、"BSF"、"NSSF"、"UDM"、"SMF"、"AUSF"、"SMSF"、"AMF"、"LMF"时为条件可选参数。<br>参数含义：该参数用于指定发起请求的NF所在的PLMN。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是5~6。<br>默认值：无<br>配置原则：<br>PLMN由MCC和MNC组成，MCC为3个十进制数字，MNC为2~3个十进制数字。例如PLMN=“12345”，其中MCC=“123”， MNC=“45”。 |
| FQDN | FQDN | 可选必选说明：该参数在"NFSELECT"配置为"SMF"、"AMF"时为条件可选参数。<br>参数含义：该参数用于指定NF的域名。本参数指定的域名中可以不包含PLMN信息，主要用于本网内的域名查询场景。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~255。<br>默认值：无<br>配置原则：<br>FQDN由一个或多个LABEL构成，各LABEL间用“.”间隔。每个LABEL的构成字符只能是字母A～Z或a～z、数字0～9和中划线“-”。例如，amf1.cluster1.net2.amf.5gc.mnc012.mcc345.3gppnetwork.org。 |
| PGWFQDN | PGWFQDN | 可选必选说明：该参数在"NFSELECT"配置为"SMF"时为条件可选参数。<br>参数含义：当SMF与PGW-C合一部署时，该参数表示PGW-C的FQDN名称，用于用户从4G和5G互操作流程中，帮助AMF找到融合SMF+PGW-C。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~255。<br>默认值：无<br>配置原则：无 |
| SNSSAI | SNSSAI | 可选必选说明：该参数在"NFSELECT"配置为"PCF"、"UDM"、"SMF"、"AMF"时为条件可选参数。<br>参数含义：该参数用于指定单网络切片选择支撑信息。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是8~10。<br>默认值：无<br>配置原则：<br>Snssai由SST和SD组成，SST取值为0-255，SD取值为6位十六进制数字。若SST为255，SD为19CDE0，则Snssai输入字符串为 255-19CDE0。 |
| TAI | TAI | 可选必选说明：该参数在"NFSELECT"配置为"SMF"、"AMF"、"NWDAF"时为条件可选参数。<br>参数含义：该参数用于指定跟踪区标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是9~12。<br>默认值：无<br>配置原则：<br>5G TAI : 输入长度范围是11~12。后6位为16进制数，其余为10进制数。4G TAI：输入长度范围是9~10。后4位为16进制数，其余为10进制数。 |
| DNN | DNN | 可选必选说明：该参数在"NFSELECT"配置为"PCF"、"BSF"、"SMF"时为条件可选参数。<br>参数含义：该参数用于指定待查询NF实例支持的数据网络名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~66。<br>默认值：无<br>配置原则：无 |
| IPV4 | IPv4地址 | 可选必选说明：该参数在"NFSELECT"配置为"BSF"、"LMF"时为条件可选参数。<br>参数含义：该参数用于指定IPv4类型地址。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~255。<br>默认值：无<br>配置原则：<br>地址取值范围为0.0.0.0~255.255.255.255。 |
| IPV6 | IPv6地址 | 可选必选说明：该参数在"NFSELECT"配置为"BSF"、"LMF"时为条件可选参数。<br>参数含义：该参数用于指定IPv6类型地址。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~255。<br>默认值：无<br>配置原则：无 |
| AMFREGIONID | AMF区域标识 | 可选必选说明：该参数在"NFSELECT"配置为"AMF"时为条件可选参数。<br>参数含义：该参数用于指定对端AMF所在区域的标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~50。本参数的构成字符建议由字母A～F或a～f、数字0～9组成。<br>默认值：无<br>配置原则：无 |
| AMFSETID | AMF组标识 | 可选必选说明：该参数在"NFSELECT"配置为"AMF"时为条件可选参数。<br>参数含义：该参数用于指定对端AMF所在集合（即Pool）的标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~50。本参数的构成字符建议是字母A～F或a～f、数字0～9，且第一个字符是数字0-3。<br>默认值：无<br>配置原则：无 |
| GUAMI | GUAMI | 可选必选说明：该参数在"NFSELECT"配置为"AMF"时为条件可选参数。<br>参数含义：该参数用于指示AMF的GUAMI信息。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是11~12。<br>默认值：无<br>配置原则：<br>GUAMI输入长度范围为11~12，由MCC、MNC和AMFID组成。 |
| SERVINGSCOPE | 服务区域 | 可选必选说明：该参数在"NFSELECT"配置为"PCF"、"SMF"时为条件可选参数。<br>参数含义：该参数用于指定支持的服务区域。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~50。<br>默认值：无<br>配置原则：无 |
| ROUTINGID | 路由标识 | 可选必选说明：该参数在"NFSELECT"配置为"NSSF"、"AUSF"时为条件可选参数。<br>参数含义：该参数用于指定待查询的NF的路由指示信息。路由指示器是SUCI组成的一部分，用于使用SUCI进行AUSF和UDM的选择。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~4。<br>默认值：无<br>配置原则：无 |
| IPDOMAIN | IP domain | 可选必选说明：该参数在"NFSELECT"配置为"BSF"时为条件可选参数。<br>参数含义：该参数用于指定IP domain。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~50。<br>默认值：无<br>配置原则：无 |
| GROUPID | GROUPID | 可选必选说明：该参数在"NFSELECT"配置为"SMSF"、"LMF"时为条件可选参数。<br>参数含义：该参数用于指定对端NF服务的群组标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~50。<br>默认值：无<br>配置原则：无 |
| SCPDOMAIN | SCPDOMAIN | 可选必选说明：该参数在"NFSELECT"配置为"SCP"时为条件可选参数。<br>参数含义：该参数用于指定SCPDOMAIN。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~255。<br>默认值：无<br>配置原则：无 |
| TAILIST | 跟踪区标识列表 | 可选必选说明：该参数在"NFSELECT"配置为"AMF"时为条件可选参数。<br>参数含义：该参数用于指定跟踪区标识列表。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~200。1. 该参数由多个TAC号段组成，起始号段和终止号段之间用“_”分隔，不同TAC号段之间用“-”分隔。例如“0002_0003-0004_0005”。2. TAC的起始号段以及终止号段仅可以配置为4位或6位，按十六进制取值。3. TAC的终止号段需要不小于TAC的起始号段，且结束值和开始值长度需相等。<br>默认值：无<br>配置原则：<br>配置该参数时，需要同时配置PLMN，配置SERVICENAME为“NamfMbsBroadcast”，以及配置NFSELECT和NFTYPE为“AMF”。除必选参数外，不能选择其他参数。 |
| LMFID | LMFID | 可选必选说明：该参数在"NFSELECT"配置为"LMF"时为条件可选参数。<br>参数含义：该参数用于指定对端NF的LMF ID。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~255。本参数的构成字符只能是字母A～Z或a～z、数字0～9、中划线"-"和下划线"_"组成的字符串。<br>默认值：无<br>配置原则：无 |
| CLIENTTYPE | CLIENTTYPE | 可选必选说明：该参数在"NFSELECT"配置为"LMF"时为条件可选参数。<br>参数含义：该参数用于指定对端NF的Client Type。<br>数据来源：本端规划<br>取值范围：<br>- EMERGENCY_SERVICES（紧急服务的外部客户端）<br>- VALUE_ADDED_SERVICES（增值业务外部客户端）<br>- PLMN_OPERATOR_SERVICES（PLMN运营商业务外部客户端）<br>- LAWFUL_INTERCEPT_SERVICES（合法拦截服务的外部客户端）<br>- PLMN_OPERATOR_BROADCAST_SERVICES（PLMN运营商广播业务外部客户端）<br>- PLMN_OPERATOR_OM（PLMN运营商运维外部客户端）<br>- PLMN_OPERATOR_ANONYMOUS_STATISTI（PLMN操作员匿名统计外部客户端）<br>- PLMN_OPERATOR_TARGET_MS_SERVICE_SUPPORT（PLMN运营商目标MS服务支持的外部客户端）<br>默认值：无<br>配置原则：无 |
| CUSTOMTYPE | CUSTOMTYPE | 可选必选说明：该参数在"QUERYTYPE"配置为"BYPARAS"时为条件可选参数。<br>参数含义：该参数用于指示服务发现流程的特殊处理。具体取值配置原则见下。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~9223372036854775807。0：无特殊处理。其他取值：参照NFDiscoveryReq中，SearchPara中的CustomType字段。<br>默认值：无<br>配置原则：无 |
| NWDAFEVENTS | NWDAF数据分析事件 | 可选必选说明：该参数在"NFSELECT"配置为"NWDAF"时为条件可选参数。<br>参数含义：该参数用于指定NWDAF支持的分析事件类型。<br>数据来源：本端规划<br>取值范围：<br>- QOS_ANALYSIS（QOS分析）<br>- QOS_EXP_ANALYSIS（体验感知信息分析）<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0000001146812823)

在远端NRF中查询NFType为SMF，SERVICENAME为NsmfPduSes， PGWFQDN为"huawei1.com.apn.epc.mnc001.mcc308.3gppnetwork.org"的NF信息。

```
%%TST NRF: DATASOURCE=NRF_ONLY, QUERYTYPE=BYPARAS, NFSELECT=SMF, SERVICENAME=NsmfPduSes, PGWFQDN="huawei1.com.apn.epc.mnc001.mcc308.3gppnetwork.org";%%
RETCODE = 0  操作成功

结果如下
--------
      网元类型  =  SMF
    NF实例标识  =  00000000-0000-0000-0000-000000000012
         PODID  =  NULL
服务发现数据源  =  仅在远端NRF查询
(结果个数 = 1)

---    END
```
