---
id: UNC@20.15.2@MMLCommand@MOD SPGWCAUSECTRL
type: MMLCommand
name: MOD SPGWCAUSECTRL（修改SGW-C/PGW-C原因值控制参数）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: SPGWCAUSECTRL
command_category: 配置类
applicable_nf:
- PGW-C
- SGW-C
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- SM原因值管理
- GTPv2会话流程原因值控制
status: active
---

# MOD SPGWCAUSECTRL（修改SGW-C/PGW-C原因值控制参数）

## 功能

**适用NF：PGW-C、SGW-C**

该命令用于修改PGW-C或融合的SGW-C/PGW-C的原因值控制参数。当用户接入PGW-C或融合的SGW-C/PGW-C时，可通过该命令控制SM流程特殊场景下指定的原因值下发，以满足运营商实现对现网设备兼容性特殊控制的需求。

## 注意事项

- 该命令执行后立即生效。

- 配置下发的原因值可能会对MME或SGW-C行为产生影响，在配置前请参见协议3GPP TS 29.274评估影响。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROCEDURETYPE | 流程类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定流程类型。<br>数据来源：本端规划<br>取值范围：<br>- CRT_SES_PROC（初始会话创建流程）<br>- MOD_BR_PROC（承载修改流程）<br>默认值：无<br>配置原则：无 |
| CAUSESOURCE | 异常来源 | 可选必选说明：必选参数<br>参数含义：该参数用于指定发生异常的来源。<br>数据来源：本端规划<br>取值范围：<br>- UPF（UPF）<br>- POLICY_PCF（PCF策略）<br>- CHG_3GPP（3GPP计费）<br>- POLICY_PCRF（PCRF策略）<br>- RADIUS_AUTH（Radius鉴权）<br>- INNER（内部异常）<br>- RADIUS_CHG（Radius计费）<br>- DIAMETER_AAA（Diameter AAA）<br>- CHF_3GPP（3GPP CHF）<br>默认值：无<br>配置原则：无 |
| CAUSEREJGROUPID | 周边网元拒绝导致流程拒绝原因值组号 | 可选必选说明：该参数在"CAUSESOURCE"配置为"UPF"、"CHG_3GPP"、"RADIUS_AUTH"、"POLICY_PCF"、"POLICY_PCRF"、"RADIUS_CHG"、"DIAMETER_AAA"、"CHF_3GPP"时为条件可选参数。<br>参数含义：该参数用于指定因周边网元返回拒绝而导致流程拒绝时，下发给MME或SGW-C的GTPv2消息中拒绝原因值采用的原因值映射组。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~127。<br>默认值：无<br>配置原则：<br>该参数的取值必须在SM原因值映射组中存在，否则系统提示没有此原因值标识。建议在执行本命令之前可以先执行LST SMCAUSEGRP来确定“CAUSEGRPID”是否存在。<br>- 当取值为0时，表示不使用特殊指定原因值。<br>- 如果该参数取值不为0，必须为ADD SMCAUSEGRP中已经存在的“SMCAUSEGPID”。需要在ADD SMCAUSEMAP中根据NF不同的拒绝原因值配置具体的原因值映射规则。这样就会改变此参数所控制的异常场景中下发给终端的原因值，从而导致相应拒绝类话统指标的变化。<br>- 当“CAUSESOURCE”配置为UPF时，该参数表示对应的ADD SMCAUSEMAP命令中的“BGCAUSE”和“EDCAUSE”为N4接口原因值，参见协议3GPP TS 29.244原因值描述表。<br>- 当“CAUSESOURCE”配置为POLICY_PCF时，该参数表示对应的ADD SMCAUSEMAP命令中的“BGCAUSE”和“EDCAUSE”为Npcf原因值，参见协议3GPP TS 29.500原因值描述表。<br>- 当“CAUSESOURCE”配置为POLICY_PCRF时，该参数表示对应的ADD SMCAUSEMAP命令中的“BGCAUSE”和“EDCAUSE”为Npcrf原因值，参见协议3GPP TS 29.212原因值描述表。<br>- 当“CAUSESOURCE”配置为CHG_3GPP时，如果ADD PDUSCACT命令配置了GTPv2原因值，则GTPC消息中携带的原因值以ADD PDUSCACT的设置为准，否则以本参数的对应的SMCAUSEMAP映射出的原因值为准。该参数表示对应的ADD SMCAUSEMAP命令中的“BGCAUSE”和“EDCAUSE”参数为SMF内部模块（SMC与CM）间的原因值，含义如下：65： CM回成功响应码70： CDRF内部处理异常71： GU->L时话单版本配置错误75： ACCT内部异常去活用户76： ACCT模块未收到计费应答发起的用户去活未收到计费应答77： WAL特性AAA计费消息达到流控上限，去活用户78： AAA计费服务器不可用时超过阈值导致激活失败的原因值79： CCA消息信元错误导致去活80： OCSC内部异常81： OCS异常发起去活（无响应）82： OCS通过返回码去活用户83： OCS NO_BALANCE 去活用户84： OCS ASR发起去活85： OCS holding timeout发起去活86： OCS CCFH terminate去活87： OCS CCFH retry&terminate去活88： WAL特性在线计费计费消息达到流控上限，去活用户89： 因收到OCS Command层或MSCC层的结果码为4206、4212、4301、4302、4231、4207、5003导致的用户去活90： PCRFC内部异常104：PCC holding timeout发起去活105：在线计费异常返回码去活用户106： 在线计费异常返回码4012去活用户120：收到OCS/CHF错误的响应消息299：CM等待UPF上报超时300：5G计费内部异常<br>- 当“CAUSESOURCE”配置为RADIUS_AUTH时，该参数表示对应的ADD SMCAUSEMAP命令中的“BGCAUSE”和“EDCAUSE”的原因值定义如下：1：AAA鉴权返回失败2：AAA服务器无响应3：服务器故障或服务器通信异常4：发送消息时无可用接口5：APN下没有绑定Radius-server-group6：因server流控导致没有server可选7：系统错误<br>- 当“CAUSESOURCE”配置为RADIUS_CHG时，该参数表示对应的ADD SMCAUSEMAP命令中的“BGCAUSE”和“EDCAUSE”的原因值与当“CAUSESOURCE”配置为CHG_3GPP时定义的原因值定义相同。<br>- 当“CAUSESOURCE”配置为DIAMETER_AAA时，该参数表示对应的ADD SMCAUSEMAP命令中的“BGCAUSE”和“EDCAUSE”的原因值为S6b接口原因值。<br>- 当“NFTYPE”配置为CHF_3GPP时，该参数表示对应的ADD SMCAUSEMAP命令中的“BGCAUSE”和“EDCAUSE”为Http Status Code原因值。 |
| CAUSEEXPIRATION | 周边网元响应超时导致流程拒绝的原因值 | 可选必选说明：该参数在"CAUSESOURCE"配置为"UPF"、"CHG_3GPP"、"RADIUS_AUTH"、"POLICY_PCF"、"POLICY_PCRF"、"RADIUS_CHG"、"DIAMETER_AAA"、"CHF_3GPP"时为条件可选参数。<br>参数含义：该参数用于指定因周边网元响应超时而导致流程拒绝时，下发给MME或SGW-C的GTPv2消息中的拒绝原因值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~255。<br>默认值：无<br>配置原则：<br>设置为0时，表示不使用特殊指定原因值。仅在"CAUSESOURCE"配置为"RADIUS_AUTH"时，发生该异常时系统将下发“#92 User auth failed”原因值。在"CAUSESOURCE"配置为"UPF、CHG_3GPP、POLICY_PCF、POLICY_PCRF、RADIUS_CHG、DIAMETER_AAA、CHF_3GPP"时，发生该异常时系统将下发“#72 System failure”原因值。<br>参数设置为非0值，会改变此参数所控制的异常场景中下发给MME或SGW-C的拒绝原因值，从而导致相应拒绝类话统指标的变化 。<br>不同原因值的含义及对MME或SGW-C行为的影响请参见协议3GPP TS 29.274原因值描述表，非协议定义原因值，不建议使用。 |
| CAUSEAPNLOCK | APN锁定或整机锁定导致流程拒绝的GTPv2原因值 | 可选必选说明：该参数在"CAUSESOURCE"配置为"INNER"时为条件可选参数。<br>参数含义：该参数用于指示因为APN锁定或整机锁定导致初始会话创建流程失败，发送的Create Session Response消息中携带的GTPv2原因值。<br>数据来源：本端规划<br>取值范围：<br>- SRVNOTSUPPORTED（#68 服务不支持）<br>- APNCONGESTION（#113 APN拥塞）<br>- NORESOURCESAVAILABLE（#73 无资源可用）<br>默认值：无<br>配置原则：无 |
| CAUSEIPOCCUPIED | IP地址耗尽导致流程拒绝的GTPv2原因值 | 可选必选说明：该参数在"CAUSESOURCE"配置为"INNER"时为条件可选参数。<br>参数含义：该参数用于指示因为IP地址耗尽导致初始会话创建流程失败，发送的Create Session Response消息中携带的GTPv2原因值。<br>数据来源：本端规划<br>取值范围：<br>- APNCONGESTION（#113 APN拥塞）<br>- ALLIPOCCUPIED（#84 无动态地址）<br>默认值：无<br>配置原则：<br>该参数仅在“流程类型”为“初始会话创建流程”时生效。 |
| CAUSEFC | 发送消息流控导致流程拒绝的GTPv2原因值 | 可选必选说明：该参数在"CAUSESOURCE"配置为"POLICY_PCF"、"POLICY_PCRF"时为条件可选参数。<br>参数含义：该参数用于指示因为发送消息流控导致初始会话创建流程失败，发送的Create Session Response消息中携带的GTPv2原因值。<br>数据来源：本端规划<br>取值范围：<br>- USERAUTHFAILED（#92 用户鉴权失败）<br>- NORESOURCESAVAILABLE（#73 无资源可用）<br>默认值：无<br>配置原则：<br>该参数仅在“流程类型”为“初始会话创建流程”时生效。 |
| CAUSEBRLIMIT | 承载受限原因值 | 可选必选说明：该参数在"CAUSESOURCE"配置为"INNER"时为条件可选参数。<br>参数含义：该参数用来控制承载受限导致流程拒绝的原因值。<br>数据来源：本端规划<br>取值范围：<br>- NORESOURCESAVAILABLE（#73 无资源可用）<br>- APNCONGESTION（#113 APN拥塞）<br>默认值：无<br>配置原则：<br>如果期望在响应中携带Back-Off Time给UE，原因值设成APNCONGESTION。 |
| CAUSESELFFC | CPU过载原因值 | 可选必选说明：该参数在"CAUSESOURCE"配置为"INNER"时为条件可选参数。<br>参数含义：该参数用来控制CPU过载或APN流控导致流程拒绝的原因值。<br>数据来源：本端规划<br>取值范围：<br>- NORESOURCESAVAILABLE（#73 无资源可用）<br>- SRVNOTSUPPORTED（#68 服务不支持）<br>默认值：无<br>配置原则：<br>取值为NORESOURCESAVAILABLE时，表示返回码为NORESOURCESAVAILABLE；取值为SRVNOTSUPPORTED时，表示返回码为SRVNOTSUPPORTED。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SPGWCAUSECTRL]] · SGW-C/PGW-C原因值控制参数（SPGWCAUSECTRL）

## 使用实例

修改会话创建流程，指定异常来源为UPF，修改原因值为#31 Request rejected, unspecified，执行如下命令：

```
MOD SPGWCAUSECTRL: PROCEDURETYPE=CRT_SES_PROC, CAUSESOURCE=UPF, CAUSEEXPIRATION=31;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/MOD-SPGWCAUSECTRL.md`
