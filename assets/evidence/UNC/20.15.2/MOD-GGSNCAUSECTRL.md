# 修改GGSN-C原因值控制参数（MOD GGSNCAUSECTRL）

- [命令功能](#ZH-CN_MMLREF_0225121196__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0225121196__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0225121196__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0225121196__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0225121196)

**适用NF：GGSN**

该命令用于修改GGSN-C的原因值控制参数。当用户接入GGSN-C时，UNC可通过该命令控制SM流程特殊场景下指定的原因值下发，以满足运营商实现对现网设备兼容性特殊控制的需求。

## [注意事项](#ZH-CN_MMLREF_0225121196)

- 该命令执行后立即生效。

- 配置下发的原因值可能会对SGSN行为产生影响，在配置前评估影响。
- 关于不同原因值的含义及对SGSN行为的影响请参见协议3GPP TS 29.060。

#### [操作用户权限](#ZH-CN_MMLREF_0225121196)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0225121196)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROCEDURETYPE | 流程类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定流程类型，要根据场景来配置相应的流程。<br>数据来源：本端规划<br>取值范围：<br>- CRT_PDP_PROC（创建PDP流程）<br>- UPD_PDP_PROC（更新PDP流程）<br>默认值：无<br>配置原则：无 |
| CAUSESOURCE | 异常来源 | 可选必选说明：必选参数<br>参数含义：该参数用于描述发生异常的来源。<br>数据来源：本端规划<br>取值范围：<br>- UPF（UPF）<br>- POLICY_PCRF（PCRF策略）<br>- CHG_3GPP（3GPP计费）<br>- RADIUS_AUTH（Radius鉴权）<br>- INNER（内部异常）<br>- RADIUS_CHG（Radius计费）<br>- POLICY_PCF（PCF策略）<br>- CHF_3GPP（3GPP CHF）<br>默认值：无<br>配置原则：<br>POLICY_PCF以及CHF_3GPP网元类型仅在2G用户下生效。 |
| CAUSEREJGROUPID | NE拒绝导致流程拒绝原因值组号 | 可选必选说明：该参数在"CAUSESOURCE"配置为"UPF"、"CHG_3GPP"、"RADIUS_AUTH"、"POLICY_PCRF"、"RADIUS_CHG"、"POLICY_PCF"、"CHF_3GPP"时为条件可选参数。<br>参数含义：该参数用于设置因周边网元返回拒绝而导致流程拒绝时，下发给左侧网元（SGSN）的GTPv1消息中拒绝原因值采用的映射规则。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~127。<br>默认值：无<br>配置原则：<br>该参数的取值必须在SMCAUSEGRP中存在，否则系统提示没有此原因值标识。建议在执行本命令之前可以先执行LST SMCAUSEGRP来确定“CAUSEGRPID”是否存在。<br>设置为0时，表示不使用特殊指定原因值。<br>如果该参数取值不为0，必须为ADD SMCAUSEGRP中已经存在的“SMCAUSEGPID”。需要在ADD SMCAUSEMAP中根据NF不同的拒绝原因值配置具体的原因值映射规则。这样就会改变此参数所控制的异常场景中下发给终端的原因值，从而导致相应拒绝类话统指标的变化。<br>当“CAUSESOURCE”配置为UPF时，该参数表示对应的ADD SMCAUSEMAP命令中的“BGCAUSE”和“EDCAUSE”为N4接口原因值，参见协议3GPP TS 29.244原因值描述表。<br>当“CAUSESOURCE”配置为POLICY_PCRF时，该参数表示对应的ADD SMCAUSEMAP命令中的“BGCAUSE”和“EDCAUSE”为PCRF原因值，参见协议3GPP TS 29.212原因值描述表。<br>当“CAUSESOURCE”配置为CHG_3GPP时，如果ADD PDUSCACT命令配置了GTPv1原因值，则GTPC消息中携带的原因值以ADD PDUSCACT的设置为准，否则以本参数的对应的SMCAUSEMAP映射出的原因值为准。该参数表示对应的ADD SMCAUSEMAP命令中的“BGCAUSE”和“EDCAUSE”参数为SMF内部模块（SMC与CM）间的原因值，含义如下：<br>65： CM回成功响应码。<br>70： CDRF内部处理异常。<br>71： GU->L时话单版本配置错误。<br>75： ACCT内部异常去活用户。<br>76： ACCT模块未收到计费应答发起的用户去活未收到计费应答。<br>77： WAL特性AAA计费消息达到流控上限，去活用户。<br>78： AAA计费服务器不可用时超过阈值导致激活失败的原因值。<br>79： CCA消息信元错误导致去活。<br>80： OCSC内部异常。<br>81： OCS异常发起去活（无响应）。<br>82： OCS通过返回码去活用户。<br>83： OCS NO_BALANCE 去活用户。<br>84： OCS ASR发起去活。<br>85： OCS holding timeout发起去活。<br>86： OCS CCFH terminate去活。<br>87： OCS CCFH retry&terminate去活。<br>88： WAL特性在线计费计费消息达到流控上限，去活用户。<br>89： 因收到OCS Command层或MSCC层的结果码为4206、4212、4301、4302、4231、4207、5003导致的用户去活。<br>90： PCRFC内部异常。<br>104：PCC holding timeout发起去活。<br>105：在线计费异常返回码去活用户。<br>106： 在线计费异常返回码4012去活用户。<br>120：收到OCS/CHF错误的响应消息。<br>299：CM等待UPF上报超时。<br>300：5G计费内部异常。<br>当“CAUSESOURCE”配置为RADIUS_AUTH时该参数表示对应的ADD SMCAUSEMAP命令中的“BGCAUSE”和“EDCAUSE”原因值定义如下：<br>1：AAA鉴权返回失败。<br>2：AAA服务器无响应。<br>3：服务器故障或服务器通信异常。<br>4：发送消息时无可用接口。<br>5：APN下没有绑定Radius-server-group。<br>6：因server流控导致没有server可选。<br>7：系统错误。<br>当“CAUSESOURCE”配置为RADIUS_CHG时，该参数表示对应的ADD SMCAUSEMAP命令中的“BGCAUSE”和“EDCAUSE”的原因值和当“CAUSESOURCE”配置为CHG_3GPP时定义的原因值定义相同。<br>当“CAUSESOURCE”配置为POLICY_PCF或者CHF_3GPP时，该参数表示对应的ADD SMCAUSEMAP命令中的“BGCAUSE”和“EDCAUSE”为Http Status Code原因值。 |
| CAUSEEXPIRATION | 响应超时导致流程拒绝的GTPv1原因值 | 可选必选说明：该参数在"CAUSESOURCE"配置为"UPF"、"CHG_3GPP"、"RADIUS_AUTH"、"POLICY_PCRF"、"RADIUS_CHG"、"POLICY_PCF"、"CHF_3GPP"时为条件可选参数。<br>参数含义：该参数用于设置因周边网元响应超时而导致流程拒绝时，下发给左侧网元（SGSN）的GTPv1消息中的拒绝原因值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~255。<br>默认值：无<br>配置原则：<br>设置为0时，表示不使用特殊指定原因值。仅在"CAUSESOURCE"配置为"RADIUS_AUTH"时，发生该异常时系统将下发“#209 User auth failed”原因值。在"CAUSESOURCE"配置为"UPF、CHG_3GPP、POLICY_PCRF、RADIUS_CHG、POLICY_PCF、CHF_3GPP"时，发生该异常时系统将下发“#204 System failure”原因值。<br>参数设置为非0值，会改变此参数所控制的异常场景中下发给左侧网元（SGSN）的拒绝原因值，从而导致相应拒绝类话统指标的变化 。<br>不同原因值的含义及对SGSN行为的影响请参见协议3GPP TS 29.060原因值描述表。非协议定义原因值，不建议使用。 |
| CAUSEAPNLOCK | APN锁定或整机锁定导致流程拒绝的GTPv1原因值 | 可选必选说明：该参数在"CAUSESOURCE"配置为"INNER"时为条件可选参数。<br>参数含义：该参数用于指示因为APN锁定或整机锁定导致创建PDP流程失败，发送的Create PDP Context Response消息中携带的GTPv1原因值。<br>数据来源：本端规划<br>取值范围：<br>- SRVNOTSUPPORTED（#200 服务不支持）<br>- APNCONGESTION（#229 APN拥塞）<br>- NORESOURCESAVAILABLE（#199 无资源可用）<br>默认值：无<br>配置原则：无 |
| CAUSEIPOCCUPIED | IP地址耗尽导致流程拒绝的GTPv1原因值 | 可选必选说明：该参数在"CAUSESOURCE"配置为"INNER"时为条件可选参数。<br>参数含义：该参数用于指示因为IP地址耗尽导致创建PDP流程失败，发送的Create PDP Context Response消息中携带的GTPv1原因值。<br>数据来源：本端规划<br>取值范围：<br>- APNCONGESTION（#229 APN拥塞）<br>- ALLIPOCCUPIED（#211 无动态PDP地址）<br>默认值：无<br>配置原则：<br>该参数仅在“流程类型”为“创建PDP流程”时生效。 |
| CAUSEFC | 发送消息流控导致流程拒绝的GTPv1原因值 | 可选必选说明：该参数在"CAUSESOURCE"配置为"POLICY_PCRF"、"POLICY_PCF"时为条件可选参数。<br>参数含义：该参数用于指示因为发送消息流控导致创建PDP流程失败，发送的Create PDP Context Response消息中携带的GTPv1原因值。<br>数据来源：本端规划<br>取值范围：<br>- USERAUTHFAILED（#209 用户鉴权失败）<br>- NORESOURCESAVAILABLE（#199 无资源可用）<br>默认值：无<br>配置原则：<br>该参数仅在“流程类型”为“创建PDP流程”时生效。 |
| CAUSEBRLIMIT | 承载受限原因值 | 可选必选说明：该参数在"CAUSESOURCE"配置为"INNER"时为条件可选参数。<br>参数含义：该参数用来控制承载受限导致流程拒绝的原因值。<br>数据来源：本端规划<br>取值范围：<br>- NORESOURCESAVAILABLE（#199 无资源可用）<br>- APNCONGESTION（#229 APN拥塞）<br>默认值：无<br>配置原则：<br>如果期望在响应中携带Back-Off Time给UE，原因值设成APNCONGESTION。 |
| CAUSESELFFC | CPU过载原因值 | 可选必选说明：该参数在"CAUSESOURCE"配置为"INNER"时为条件可选参数。<br>参数含义：该参数用来控制CPU过载或APN流控导致流程拒绝的原因值。<br>数据来源：本端规划<br>取值范围：<br>- NORESOURCESAVAILABLE（#199 无资源可用）<br>- SRVNOTSUPPORTED（#200 服务不支持）<br>默认值：无<br>配置原则：<br>取值为NORESOURCESAVAILABLE时，表示返回码为NORESOURCESAVAILABLE；取值为SRVNOTSUPPORTED时，表示返回码为SRVNOTSUPPORTED。 |

## [使用实例](#ZH-CN_MMLREF_0225121196)

修改创建PDP流程UPF异常的流程控制配置。

```
MOD GGSNCAUSECTRL: PROCEDURETYPE=CRT_PDP_PROC, CAUSESOURCE=UPF, CAUSEEXPIRATION=31;
```
