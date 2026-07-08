---
id: UNC@20.15.2@MMLCommand@MOD QOSCAP
type: MMLCommand
name: MOD QOSCAP（修改Non-GBR承载QoS限制配置）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: QOSCAP
command_category: 配置类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- QoS管理
- EPS QoS
- QoS限制配置
- Non-GBR承载QoS限制
status: active
---

# MOD QOSCAP（修改Non-GBR承载QoS限制配置）

## 功能

**适用网元：MME**

该命令用于修改一条QoS限制配置记录。

## 注意事项

- 该命令执行后立即生效。
- 该命令不能修改IMSI前缀。
- 同一网络内，所有MME/SGSN的QoS限制配置参数应保持一致。
- 当UNC作为MME/SGSN网元时，对应用户群的QoS信息将会被配置中的QoS信息限制。
- 如果想取消对某一QoS参数的限制，需要执行本命令将相应QoS参数修改为无效值。
- 配置变更时，如果当前用户正在进行业务流程，配置限制不会实时生效，在下一个流程中生效。
- QoS各参数的取值及含义具体请参见3GPP TS 23.107（QoS协议）。
- 此配置涉及基于IMSI号段的QoS控制特性（特性编号：WSFD-105104，License部件编码：LKV2IMSIQOS02），执行命令请使用[**DSP LICENSE**](../../../../../../../平台服务管理/操作维护/License管理/显示License(DSP LICENSE)_00360098.md)命令确认对应特性License是否得到授权，执行[**LST LICENSESWITCH**](../../../../../../../平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md)命令确认特性开关状态为“ENABLE（打开）”。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RATTYPE | RAT类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定用户的接入类型，系统优先匹配与当前用户所处网络类型相同的配置数据，当相同RAT类型配置中不包含该用户时，再进行<br>“ALL”<br>类型的匹配。<br>数据来源：整网规划<br>取值范围：<br>- “ALL(ALL)”<br>- “GERAN(GERAN)”<br>- “UTRAN(UTRAN)”<br>- “E-UTRAN(E-UTRAN)”<br>- “NB-IoT(NB-IoT)”<br>默认值：无 |
| SUBRANGE | 用户范围 | 可选必选说明：必选参数<br>参数含义：该参数用于指定待增加Non-GBR承载QoS限制配置的用户范围。<br>数据来源：整网规划<br>取值范围：<br>- “ALL_USER（所有用户）”<br>- “HOME_USER（本网用户）”<br>- “FOREIGN_USER（外网用户）”<br>- “IMSI_PREFIX（指定IMSI前缀）”<br>默认值：无 |
| NOID | 运营商标识 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定运营商标识。<br>前提条件：该参数必须先由<br>[**ADD QOSCAP**](增加Non-GBR承载QoS限制配置(ADD QOSCAP)_72225897.md)<br>命令定义，才能在此处引用。<br>数据来源：整网规划<br>取值范围：0～64，128～254<br>默认值：无<br>配置原则：<br>- 若该参数需要配置为0或128～254之间的值时，须先在[**ADD MNO**](../../../../网络管理/归属网络运营商管理/MNO管理/MNO配置表/增加MNO配置信息(ADD MNO)_72345671.md)中配置取值相同的“MNOID”参数。<br>- 若该参数需要配置为1～64之间的值时，须先在[**ADD MVNO**](../../../../网络管理/归属网络运营商管理/MVNO管理/MVNO配置表/增加MVNO配置信息(ADD MVNO)_72225747.md)中配置取值相同的“MVNOID”参数。 |
| IMSIPRE | IMSI前缀 | 可选必选说明：条件必选参数<br>参数含义：该参数用于系统根据对用户的IMSI进行匹配，从而区分不同的用户群。<br>前提条件：该参数必须先由<br>[**ADD QOSCAP**](增加Non-GBR承载QoS限制配置(ADD QOSCAP)_72225897.md)<br>命令定义，才能在此处引用。<br>数据来源：整网规划<br>取值范围：5～15位数字<br>默认值：无 |
| UEAMBRULK | 上行UE AMBR （kbps） | 可选必选说明：可选参数<br>参数含义：该参数用于指定系统对用户Non-GBR承载的上行UE-AMBR限制。<br>数据来源：整网规划<br>取值范围：0kbps～65000000kbps<br>默认值：无<br>配置原则：如果同时配置了<br>“上行UE AMBR（kbps）”<br>和<br>“上行APN AMBR（kbps）”<br>，<br>“上行UEAMBR（kbps）”<br>必须大于等于<br>“上行APN AMBR（kbps）”<br>。<br>说明：0kbps为无效值，表示不对<br>“上行UE AMBR（kbps）”<br>进行限制。 |
| UEAMBRDLK | 下行UE AMBR （kbps） | 可选必选说明：可选参数<br>参数含义：该参数用于指定系统对用户Non-GBR承载的下行UE-AMBR限制。<br>数据来源：整网规划<br>取值范围：0kbps～65000000kbps<br>默认值：无<br>配置原则：如果同时配置了<br>“下行UE AMBR（kbps）”<br>和<br>“下行APN AMBR（kbps）”<br>，<br>“下行UE AMBR（kbps）”<br>必须大于等于<br>“下行APN AMBR（kbps）”<br>。<br>说明：0kbps为无效值，表示不对<br>“下行UE AMBR （kbps）”<br>进行限制。 |
| APNAMBRULK | 上行APN AMBR （kbps） | 可选必选说明：可选参数<br>参数含义：该参数用于指定系统对用户Non-GBR承载的上行APN-AMBR限制。<br>数据来源：整网规划<br>取值范围：0kbps～65000000kbps<br>默认值：无<br>配置原则：如果同时配置了<br>“上行UE AMBR（kbps）”<br>和<br>“上行APN AMBR（kbps）”<br>，<br>“上行UE AMBR（kbps）”<br>必须大于等于<br>“上行APN AMBR（kbps）”<br>。<br>说明：0kbps为无效值，表示不对<br>“上行APN AMBR（kbps）”<br>进行限制。 |
| APNAMBRDLK | 下行APN AMBR （kbps） | 可选必选说明：可选参数<br>参数含义：该参数用于指定系统对用户Non-GBR承载的下行APN-AMBR限制。<br>数据来源：整网规划<br>取值范围：0kbps～65000000kbps<br>默认值：无<br>配置原则：如果同时配置了<br>“下行UE AMBR（kbps）”<br>和<br>“下行APN AMBR（kbps）”<br>，<br>“下行UE AMBR（kbps）”<br>必须大于等于<br>“下行APN AMBR（kbps）”<br>。<br>说明：0kbps为无效值，表示不对<br>“下行APN AMBR（kbps）”<br>进行限制。 |
| QCI | QCI（Non-GBR承载） | 可选必选说明：可选参数<br>参数含义：该参数用于指定系统对用户Non-GBR承载的QCI限制。<br>数据来源：整网规划<br>取值范围：0，5～9<br>默认值：无<br>说明：- 0为无效值，表示不对“QCI（Non-GBR承载）”进行限制。<br>- 如果网络下发扩展QCI，系统按照网络侧提升了QoS处理，即按照“网络提升Non-GBR承载QoS”的取值来处理。 |
| ARPPRL | ARP的优先级别（Non-GBR承载） | 可选必选说明：可选参数<br>参数含义：该参数用于指定系统对用户Non-GBR承载的ARP优先级别限制。<br>数据来源：整网规划<br>取值范围：0～15<br>默认值：无<br>说明：0为无效值，表示不对<br>“ARP的优先级别（Non-GBR承载）”<br>进行限制。<br>取值越小，优先级越高。 |
| ARPPCI | ARP的抢占能力（Non-GBR承载） | 可选必选说明：可选参数<br>参数含义：该参数用于指定系统对用户Non-GBR承载的ARP抢占能力限制。<br>数据来源：整网规划<br>取值范围：<br>- “ENABLE（启用）”：允许该承载抢占其他ARP的优先级别较低的承载的资源。<br>- “DISABLE（未启用）”：不允许该承载抢占其他ARP的优先级别较低的承载的资源。<br>- “INVALID（无效值）”：本命令将不对“ARP的抢占能力”进行限制。<br>默认值：无 |
| ARPPVI | ARP的被抢占能力（Non-GBR承载） | 可选必选说明：可选参数<br>参数含义：该参数用于指定系统对用户Non-GBR承载的ARP被抢占能力限制。<br>数据来源：整网规划<br>取值范围：<br>- “ENABLE（启用）”：允许其他优先级别较高的承载抢占该承载的资源。<br>- “DISABLE（未启用）”：不允许其他优先级别较高的承载抢占该承载的资源。<br>- “INVALID（无效值）”：本命令将不对“ARP的被抢占能力”进行限制。<br>默认值：无 |
| SUBQOS | 仅使用配置QoS限制 | 可选必选说明：可选参数<br>参数含义：该参数用于指定系统如何对用户缺省承载的QoS进行限制：仅使用配置QoS进行限制，或综合考虑配置QoS和签约QoS进行限制。按照3GPP协议定义，缺省承载都是Non-GBR承载。<br>数据来源：整网规划<br>取值范围：<br>- “YES（是）”：系统仅使用配置的QoS对用户的缺省承载QoS进行限制。<br>- “NO（否）”：系统综合考虑配置QoS和签约QoS，选取两者中较为严格的QoS参数对用户的缺省承载QoS进行限制。<br>默认值：无<br>说明：- 当该参数配置为“YES（是）”时，将使用配置中的QoS值对用户签约数据中的QoS信息进行覆盖。<br>- 当该参数配置为“NO（否）”时，满足如下条件的情况下，不使用配置中的QoS值对用户进行限制；其余情况下，将使用配置中的QoS值对用户的签约数据进行覆盖：- 签约的UL/DL APN AMBR/UL/DL UE AMBR的值比配置的数值小。<br>- 签约的标准non GBR QCI比配置的QCI数值大（QCI的处理只支持标准non GBR QCI的判断，如果用户签约了扩展QCI，则采用配置的QCI进行覆盖）。<br>- 签约的ARP的优先级别（ARP）比配置的数值大。<br>- 签约的ARP的抢占能力（ARP Preemption Capability）是“DISABLE”，配置的抢占能力（ARP Preemption Capability）是“ENABLE”。<br>- 签约的ARP的被抢占能力（ARP Preemption Vulnerability）是“ENABLE”，配置的被抢占能力（ARP Preemption Vulnerability）是“DISABLE”。 |
| CTRLNWQOS | 网络提升Non-GBR承载QoS | 可选必选说明：可选参数<br>参数含义：该参数用于指定<br>UNC<br>接收到网络下发的Non-GBR承载QoS参数超出限制时的处理方法。<br>数据来源：整网规划<br>取值范围：<br>- “ACCEPT（接受QoS）”：使用网络侧下发的QoS信息进行相应的流程。<br>- “RESTRICT（限制QoS）”：使用配置和签约决策出的QoS信息进行相应的流程。<br>- “REJECT（拒绝QoS） ”：拒绝相关的业务流程。<br>默认值：无 |
| PDNREJCAUSE | PDN连接建立拒绝原因值 | 可选必选说明：条件可选参数<br>参数含义：该参数指定了系统因为QoS限制拒绝UE请求的PDN连接/PDP上下文激活时使用的原因值。<br>前提条件：该参数在<br>“网络提升Non-GBR承载QoS”<br>参数设置为<br>“REJECT（拒绝QoS）”<br>时，才需要配置。<br>数据来源：整网规划<br>取值范围：1～127<br>默认值：无<br>说明：- 系统作为MME，在PDN Connectivity Reject消息的ESM Cause信元中携带该原因值，请参见3GPP TS 24.301。<br>- 系统作为SGSN，在Activate PDP Context Reject消息的SM Cause信元中携带该原因值，请参见3GPP TS 24.008。<br>- 各拒绝原因值的具体含义请参见3GPP TS 24.301和3GPP TS 24.008。建议使用系统默认值，可以根据终端的具体行为进行调整。<br>- 终端收到拒绝后的行为依赖于各厂商的实现。<br>- “CTRLNWQOS（网络提升Non-GBR承载QoS）”参数从非“REJECT（拒绝）”修改为“REJECT（拒绝）”，但是未输入本参数，系统自动设置本参数的取值为[**ADD QOSCAP**](增加Non-GBR承载QoS限制配置(ADD QOSCAP)_72225897.md)命令中本参数的默认值：32（Service option not supported）。 |
| NGBRREJNASCAUSE | 拒绝Non-GBR承载建立/修改NAS原因值 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定系统因为QoS限制拒绝UE请求的Non-GBR承载资源建立/修改时使用的NAS原因值。<br>前提条件：该参数在<br>“网络提升Non-GBR承载QoS”<br>参数设置为<br>“REJECT（拒绝QoS）”<br>时，才需要配置。<br>数据来源：整网规划<br>取值范围：1～127<br>默认值：无<br>说明：- 系统作为MME，在发送给UE的Bearer Resource Allocatio/Modification Reject消息的ESM Cause信元中携带该原因值，请参见3GPP TS 24.301。<br>- 各拒绝原因值的具体含义请参见3GPP TS 24.301和3GPP TS 24.008。建议使用系统默认值，可以根据终端的具体行为进行调整。<br>- 终端收到拒绝后的行为依赖于各厂商的实现。<br>- “CTRLNWQOS（网络提升Non-GBR承载QoS）”参数从非“REJECT（拒绝QoS）”修改为“REJECT（拒绝QoS）”，但是未输入本参数，系统自动设置本参数的取值为[**ADD QOSCAP**](增加Non-GBR承载QoS限制配置(ADD QOSCAP)_72225897.md)命令中本参数的默认值：37（QoS not accepted）。 |
| NGBRGTPCREJCAUSE | 拒绝Non-GBR承载建立/修改GTPC原因值 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定系统因为QoS限制拒绝网络侧请求的Non-GBR承载建立/修改时使用的GTPC原因值。<br>前提条件：该参数在<br>“网络提升Non-GBR承载QoS”<br>参数设置为<br>“REJECT（拒绝QoS）”<br>时，才需要配置。<br>数据来源：整网规划<br>取值范围：1～255<br>默认值：无<br>说明：- 系统作为MME/SGSN，在发送给S-GW/P-GW的Create/Update Bearer Response消息的Cause信元中携带该原因值，请参见3GPP TS 29.274。<br>- 各拒绝原因值的具体含义请参见3GPP TS 29.274。建议使用系统默认值，可以根据S-GW/P-GW的具体行为进行调整。<br>- “CTRLNWQOS（网络提升Non-GBR承载QoS）”参数从非“REJECT（拒绝QoS）”修改为“REJECT（拒绝QoS）”，但是未输入本参数，系统自动设置本参数的取值为[**ADD QOSCAP**](增加Non-GBR承载QoS限制配置(ADD QOSCAP)_72225897.md)命令中本参数的默认值：88（UE refuses）。 |
| DEDBEARER | Non-GBR专有承载控制策略 | 可选必选说明：可选参数<br>参数含义：该参数用于指定Non-GBR专有承载的承载级QoS参数（QCI和ARP）的控制策略。<br>数据来源：整网规划<br>取值范围：<br>- “NO_CTRL（不控制）”：系统不控制Non-GBR专有承载的承载级QoS参数。<br>- “DEFAULT（同缺省承载）”：系统控制Non-GBR专有承载的承载级QoS参数，采用与缺省承载相同的控制策略。具体策略由“QCI（QCI（Non-GBR承载））”、“ARPPRL（ARP的优先级别（Non-GBR承载））”、“ARPPCI（ARP的抢占能力（Non-GBR承载））”“ARPPVI（ARP的被抢占能力（Non-GBR承载））”和“CTRLNWQOS（网络提升Non-GBR承载QoS）”参数定义。<br>默认值：无 |
| MNNAME | 移动网络名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定对应的移动网络名称。<br>数据来源：整网规划<br>取值范围：1～32位字符串<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@QOSCAP]] · Non-GBR承载QoS限制配置（QOSCAP）

## 使用实例

修改一条QoS限制配置，对于 “RAT类型” 为 “ALL” ， “用户范围” 为 “IMSI_PREFIX” ， “IMSI前缀” 为 “3080107000” （即IMSI号范围在308010700000000～308010700099999内）的用户，将 “上行UE AMBR（kbps）” 限制改为 “10000kbps” ， “下行UE AMBR（kbps）” 限制改为 “20000kbps” ， “上行APN AMBR（kbps）” 限制改为 “5000kbps” ， “下行APN AMBR（kbps）” 限制改为 “10000kbps” ，QCI限制改为8，ARP的优先级别限制改为10， “ARP的抢占能力” 限制改为 “DISABLE” ， “ARP的被抢占能力” 限制改为 “ENABLE” ，覆盖QoS设置改为 “YES” ，网络提升QoS的控制方法设置改为 “接受QoS” ，移动网络名称改为 “MobileNet1” ：

MOD QOSCAP: RATTYPE=ALL,SUBRANGE=IMSI_PREFIX,IMSIPRE="3080107000",UEAMBRULK=10000,UEAMBRDLK=20000,APNAMBRULK=5000,APNAMBRDLK=10000,QCI=8,ARPPRL=10,ARPPCI=DISABLE,ARPPVI=ENABLE,SUBQOS=YES,CTRLNWQOS=ACCEPT,MNNAME="MobileNet1";

## 证据

- 原始手册：`evidence/UNC/20.15.2/MOD-QOSCAP.md`
