---
id: UNC@20.15.2@MMLCommand@SET PSCSPLCY
type: MMLCommand
name: SET PSCSPLCY（设置联合接入策略）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: PSCSPLCY
command_category: 配置类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 电路域联合业务
- 联合接入管理
status: active
---

# SET PSCSPLCY（设置联合接入策略）

## 功能

**适用网元：MME**

该命令用于设置联合接入策略。

## 注意事项

- 此命令执行后立即生效。
- 此命令优先级高于[ADD PROCLMTPLCY](../../移动性管理/流程限制管理/增加流程限制策略(ADD PROCLMTPLCY)_72225309.md)和[BYTE_EX_B68 BIT8](../../../../../../../软件参数/UNC软件参数/业务软件参数/软件参数（SGSN_MME）/参数说明/移动性管理/BYTE_EX_B68 BIT8 控制系统是否对存在IMS PDN的4G用户进行CS域去注册_05451097.md)。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| COMACCSW | 是否开启联合接入限制功能 | 可选必选说明：可选参数<br>参数含义：该参数用于指定对联合接入流程（包括联合附着流程和联合TAU流程，下文同理）是否开启CS注册限制。<br>数据来源：整网规划<br>取值范围：<br>- “YES(是)”:表示功能开启<br>- “NO(否)”:表示功能禁止<br>默认值：NO(否) |
| COMACCCOND | 联合接入限制通用条件 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定对联合接入流程开启CS注册限制时的用户识别通用条件。<br>前提条件：该参数在“COMACCSW”配置为“YES”时为可选参数。<br>数据来源：本端规划<br>取值范围：<br>- “STNSR(STNSR)”：表示用户签约STNSR为非预设值。<br>- “IMSAPN(IMS APN)”：表示用户签约支持IMS APN。<br>- “IMSCAP(IMSCAP)”：表示终端能力支持IMS。<br>系统初始设置值：STNSR-1&IMSAPN-1&IMSCAP-1 |
| PRESTNSR | 预设STN-SR值 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定HSS的预设STN-SR。<br>前提条件：该参数在“COMACCSW”配置为“YES”时为可选参数。<br>数据来源：对端协商<br>取值范围：字符串类型，输入长度范围为1-16位的十六进制数<br>系统初始设置值：无<br>说明：- 当“联合接入限制通用条件”参数勾选“STNSR(STNSR)”条件时功能生效。<br>- 当“预设STN-SR值”未配置时，限制联合接入功能不生效。 |
| SUBPLCY | 白名单策略 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定白名单选择策略。<br>前提条件：该参数在“COMACCSW”配置为“YES”时为可选参数。<br>数据来源：本端规划<br>取值范围：<br>- “HSS_IDENT (HSS标识)”<br>- “IMSI_IDENT (IMSI标识)”<br>默认值：“HSS_IDENT (HSS标识)”<br>配置原则：<br>- 当SUBPLCY取值为HSS_IDENT时，只对ADD PSCSHSS配置范围内的用户生效。<br>- 当取值为IMSI_IDENT时，只对ADD PSCSIMSI配置范围内的用户生效。<br>- 如果ADD PSCSHSS和ADD PSCSIMSI未配置任何数据，表示没有用户在白名单内，限制联合接入功能不生效。<br>说明：白名单表示是否对指定范围的用户开启联合接入限制功能，即联合接入限制功能只对白名单用户生效。 |
| COMATTSW | 是否开启联合附着限制功能 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定对联合附着流程是否开启CS注册限制。<br>前提条件：该参数在“COMACCSW”配置为“YES”时为可选参数。<br>数据来源：整网规划<br>取值范围：<br>- “YES(是)”:表示功能开启<br>- “NO(否)”:表示功能禁止<br>默认值：NO(否) |
| COMTAUSW | 是否开启联合TAU限制功能 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定对联合TAU流程(包含周期性TAU)是否开启CS注册限制。<br>前提条件：该参数在“COMACCSW”配置为“YES”时为可选参数。<br>数据来源：整网规划<br>取值范围：<br>- “YES(是)”:表示功能开启<br>- “NO(否)”:表示功能禁止<br>默认值：NO(否)<br>说明：该参数设置为“YES(是)”后，UNC默认会限制周期性联合TAU流程。将软参<br>**BYTE_EX_B124 BIT2**<br>设置为“1”可以解除UNC对周期性联合TAU流程的限制。 |
| IMSPDNCOND | 无IMS PDN连接时是否限制联合TAU | 可选必选说明：条件可选参数<br>参数含义：该参数用于控制在联合TAU流程中，如果用户未建立IMS的PDN连接，是否限制CS注册。<br>前提条件：该参数在“COMTAUSW”配置为“YES”时为可选参数。<br>数据来源：整网规划<br>取值范围：<br>- “YES(是)”<br>- “NO(否)”<br>默认值：NO(否) |
| ACCSUCC | 联合接入是否响应成功 | 可选必选说明：条件可选参数<br>参数含义：该参数用于联合接入流程中CS注册受限后，MME是否向UE返回联合接入成功的Attach/TAU Accept消息。<br>前提条件：该参数在“COMACCSW”配置为“YES”时为可选参数。<br>数据来源：整网规划<br>取值范围：<br>- “YES(是)”<br>- “NO(否)”<br>默认值：YES(是) |
| CSSRVPROC | UE发起CS业务时是否驻留4G | 可选必选说明：条件可选参数<br>参数含义：该参数用于联合附着和联合TAU流程中CS注册受限后，Attach/TAU Accept按联合接入成功响应UE，后续UE发起Extended Service Request流程时，MME是否保持UE驻留4G，不回落CS域。<br>前提条件：该参数在“ACCSUCC”配置为“YES”时为可选参数。<br>数据来源：整网规划<br>取值范围：<br>- “YES(是)” ：不允许回落，驻留4G。<br>- “NO(否)”：允许回落，不驻留4G。<br>系统初始设置值：“NO(否)”<br>配置原则：<br>- 当运营商规划有CS网络覆盖时，建议配置“NO(否)”。<br>- 当运营商未规划CS网络覆盖时，建议配置“YES(是)”。<br>说明：- 用户驻留4G主要通过如下方式实现：MME收到Extended service request消息后返回携带#39 CS service temporarily not available原因值和T3442 value信元的Service reject消息。<br>- 用户驻留4G功能主要用于HSS全部故障，且开启HSS全故障业务保活。当前现网HSS/HLR多为融合设备，在HSS/HLR同时故障时，用户回落CS域进行语音业务会失败，对于语音优先的终端，可能导致脱网。为了避免终端脱网，让其驻留4G做惯性运行。因此驻留功能开启时，建议同时开启HSS全故障业务保活，License编码LKV2HSSBP01。 |
| CSSRVHSS | 手动HSS Bypass时用户是否驻留4G | 可选必选说明：条件可选参数<br>参数含义：通过<br>[增加故障状态HSS(ADD HSSBPOFC)](../../业务安全管理/可靠性管理/HSS故障BYPASS功能/增加故障状态HSS(ADD HSSBPOFC)_70093526.md)<br>添加故障HSS后，归属于该HSS的假联合成功的用户在发起Extended service request流程时，MME是否让UE进入Bypass状态。<br>前提条件：该参数在“CSSRVPROC”配置为“NO”时为可选参数。<br>数据来源：整网规划<br>取值范围：<br>- “YES(是)” ：进入Bypass状态。<br>- “NO(否)” ：不进入Bypass状态。<br>系统初始设置值：“NO(否)”<br>说明：- 当HSS已经故障但MME还未检测到时，通过[增加故障状态HSS(ADD HSSBPOFC)](../../业务安全管理/可靠性管理/HSS故障BYPASS功能/增加故障状态HSS(ADD HSSBPOFC)_70093526.md)配置故障的HSS，以便用户可以进入HSS Bypass状态。该参数配置为“YES(是)”时，用户触发的ESR消息也会让用户进入HSS Bypass状态，并执行驻留4G的策略。<br>- 驻留功能开启时，建议同时开启HSS全故障业务保活，License编码LKV2HSSBP01。 |
| CSCAUSE | 联合接入限制原因值 | 可选必选说明：条件可选参数<br>参数含义：该参数用于联合附着和联合TAU流程中CS注册受限后，响应UE的原因值。<br>前提条件：该参数在“ACCSUCC”配置为“NO”时为可选参数。<br>数据来源：整网规划<br>取值范围：<br>- MSC_TEMPORARILY_NOT_REACHABLE(#16 MSC temporarily not reachable)<br>- CS_DOMAIN_NOT_AVAILABLE(#18 CS domain not available)<br>默认值：CS_DOMAIN_NOT_AVAILABLE(#18 CS domain not available)<br>说明：EMM CAUSE中的失败原因值，请参考3GPP TS 24.301进行输入。 |
| NOCSPLCY | 是否开启无CS控制策略 | 可选必选说明：可选参数<br>参数含义：该参数用于指定运营商是否开启未规划CS网络场景下的控制策略。<br>数据来源：整网规划<br>取值范围：<br>- “YES(是)”<br>- “NO(否)”<br>系统初始设置值：“NO(否)” |
| NOCSIDENT | 无CS规划识别条件 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定运营商针对某个用户未规划CS网络的匹配条件。<br>前提条件：该参数在“NOCSPLCY”配置为“YES”时为可选参数。<br>数据来源：整网规划<br>取值范围：<br>- “TAILAI（TAILAI）”：表示根据ADD TAILAI进行匹配，如果匹配失败，即为运营商针对该用户未规划CS网络。 |
| NOCSUEIDENT | 用户识别条件 | 可选必选说明：条件可选参数<br>参数含义：针对未规划CS网络的用户，该参数用于指定实施特定策略的用户匹配条件。<br>前提条件：该参数在“NOCSPLCY”配置为“YES”时为可选参数。<br>数据来源：整网规划<br>取值范围：<br>- “IMSAPN(IMS APN)”：表示用户签约支持IMS APN。<br>- “IMSCAP(IMSCAP)”：表示终端能力支持IMS。<br>系统初始设置值：IMSAPN-1&IMSCAP-1 |
| NOCSFAKEACC | 无CS规划用户是否响应联合接入假成功 | 可选必选说明：条件可选参数<br>参数含义：该参数用于运营商未规划CS网络场景下，用户发起联合附着和联合TAU流程中CS注册受限后，MME是否向UE返回联合接入成功的Attach/TAU Accept消息。<br>前提条件：该参数在“NOCSPLCY”配置为“YES”时为可选参数。<br>数据来源：整网规划<br>取值范围：<br>- “YES(是)”<br>- “NO(否)”<br>系统初始设置值：“NO(否)” |
| NOCSSRVPROC | 无CS规划的UE发起CS业务时是否驻留4G | 可选必选说明：条件可选参数<br>参数含义：该参数用于控制联合附着和联合TAU流程中CS注册受限后（无CS规划导致），Attach/TAU Accept按联合接入成功响应UE，后续UE发起Extended service request流程时，MME是否让UE驻留4G，不回落CS域。<br>前提条件：该参数在“NOCSFAKEACC”配置为“YES”时为可选参数。<br>数据来源：整网规划<br>取值范围：<br>- “YES(是)”：不允许回落，驻留4G。<br>- “NO(否)”：允许回落，不驻留4G。<br>系统初始设置值：“YES(是)”<br>配置原则：<br>- 当运营商规划有CS网络覆盖时，建议配置“NO(否)”。<br>- 当运营商未规划CS网络覆盖时，建议配置“YES(是)”。<br>说明：- 用户驻留4G主要通过如下方式实现：MME收到Extended service request消息后返回携带#39 CS service temporarily not available原因值和T3442 value信元的Service reject消息。<br>- 用户驻留4G功能主要用于HSS故障，且开启HSS全故障业务保活。当前现网HSS/HLR多为融合设备，在HSS/HLR同时故障时，用户回落CS域进行语音业务会失败，对于语音优先的终端，可能导致脱网。为了避免终端脱网，让其驻留4G做惯性运行。因此驻留功能开启时，建议同时开启HSS全故障业务保活，License编码LKV2HSSBP01。 |
| NOCSCAUSE | 无CS规划的联合接入限制原因值 | 可选必选说明：条件可选参数<br>参数含义：该参数用于表示无CS规划场景下，联合附着和联合TAU流程中CS注册受限后，响应UE的原因值。<br>前提条件：该参数在“NOCSFAKEACC”配置为“NO”时为可选参数。<br>数据来源：整网规划<br>取值范围：<br>- MSC_TEMPORARILY_NOT_REACHABLE(#16 MSC temporarily not reachable)<br>- CS_DOMAIN_NOT_AVAILABLE(#18 CS domain not available)<br>默认值：CS_DOMAIN_NOT_AVAILABLE(#18 CS domain not available)<br>说明：EMM CAUSE中的失败原因值，请参考3GPP TS 24.301进行输入。 |
| FAKELAIPLCY | 联合接入响应假成功时LAI填写策略 | 可选必选说明：可选参数<br>参数含义：该参数用于控制联合附着/TAU流程CS注册受限后，Attach Accept/TAU Accept按联合附着成功响应UE时携带的LAI策略。<br>数据来源：整网规划<br>取值范围：<br>- “TAILAI(TAI映射)” ：通过TAI映射。<br>- “FAKELAI(固定值)”：取配置的固定值。<br>系统初始设置值：TAILAI(TAI映射)<br>说明：当取值为“TAILAI(TAI映射)”时，如果ADD TAILAI配置中没有匹配记录，不携带。如果ADD TAILAI配置中有匹配记录，且TAI映射的LAI不为全F并且和联合附着/TAU请求消息中携带的LAI不一致，取TAI映射的LAI值，否则不携带。 |
| FAKELAI | LAI固定填充值 | 可选必选说明：条件可选参数<br>参数含义：该参数用于控制联合附着/TAU流程CS注册受限后，Attach Accept/TAU Accept按联合附着成功响应UE时携带的LAI。<br>前提条件：该参数在“FAKELAIPLCY”配置为“FAKELAI”时为可选参数。<br>数据来源：整网规划<br>取值范围：9～10位的字符串<br>默认值：无<br>配置原则：<br>- LAI由MCC，MNC，LAC组成。<br>- MCC为3个BCD码字符，MNC为2个或者3个BCD码字符，填写时请遵循实际长度。<br>- LAC编码为16进制数，固定为4位，不足补0。<br>- LAI可以重复，一个LAI可对应多个TAI区间。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@PSCSPLCY]] · 联合接入策略（PSCSPLCY）

## 使用实例

1、存在CS规划的配置实例。

SET PSCSPLCY: COMACCSW=YES, COMACCCOND=IMSAPN-1&IMSCAP-1&STNSR-1, PRESTNSR="123456", SUBPLCY=HSS_IDENT, COMATTSW=YES, COMTAUSW=YES, IMSPDNCOND=YES, ACCSUCC=YES, CSSRVPROC=NO, FAKELAIPLCY=TAILAI;

2、存在CS规划，并且当HSS故障时，用户也能够进入HSS Bypass状态，保证用户不会回落2/3G。

SET PSCSPLCY: COMACCSW=YES, COMACCCOND=IMSAPN-1&IMSCAP-1&STNSR-1, PRESTNSR="123456", SUBPLCY=HSS_IDENT, COMATTSW=YES, COMTAUSW=YES, IMSPDNCOND=YES, ACCSUCC=YES, CSSRVPROC=NO, CSSRVHSS=YES, NOCSPLCY=NO, FAKELAIPLCY=TAILAI;

3、不存在CS规划的配置实例。

SET PSCSPLCY: COMACCSW=NO, NOCSPLCY=YES, NOCSIDENT=TAILAI, NOCSUEIDENT=IMSAPN-1&IMSCAP-1, NOCSFAKEACC=YES, NOCSSRVPROC=YES, FAKELAIPLCY=FAKELAI, FAKELAI="123031234";

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-PSCSPLCY.md`
