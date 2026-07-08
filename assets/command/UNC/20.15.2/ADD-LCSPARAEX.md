---
id: UNC@20.15.2@MMLCommand@ADD LCSPARAEX
type: MMLCommand
name: ADD LCSPARAEX（增加LCS扩展参数）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: LCSPARAEX
command_category: 配置类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
max_records: 192
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 业务安全管理
- LCS
- LCS扩展参数
status: active
---

# ADD LCSPARAEX（增加LCS扩展参数）

## 功能

**适用网元：MME**

该命令用于基于运营商设置LCS扩展参数。包括VoLTE紧急呼叫触发的NI-LR流程的一些参数。

## 注意事项

- 该命令执行后立即生效。
- 此命令最大记录数为192。
- 此配置涉及位置定位服务（LCS）特性（特性编号：WSFD-106401，license部件编码：LKV2LCS02）、VoLTE紧急呼叫特性（特性编号：WSFD-106401，license部件编码：LKV2VLEC01）和VoLTE紧急呼叫的定位（NI-LR）特性（特性编号：WSFD-102102，license部件编码：LKV2NVEC01），请在设置参数前使用[**DSP LICENSE**](../../../../../../平台服务管理/操作维护/License管理/显示License(DSP LICENSE)_00360098.md)命令确认对应特性license是否得到授权，执行[**LST LICENSESWITCH**](../../../../../../平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md)命令确认特性开关状态为“ENABLE(打开)”。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NOID | 运营商标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定运营商标识。<br>数据来源：整网规划<br>取值范围：0~64,128~254<br>默认值：无<br>配置原则：<br>- 若该参数需要配置为0或128～254之间的值时，请先在[**ADD MNO**](../../../网络管理/归属网络运营商管理/MNO管理/MNO配置表/增加MNO配置信息(ADD MNO)_72345671.md)中配置取值相同的“MNOID”参数。<br>- 若该参数需要配置为1～64之间的值时，请先在[**ADD MVNO**](../../../网络管理/归属网络运营商管理/MVNO管理/MVNO配置表/增加MVNO配置信息(ADD MVNO)_72225747.md)中配置取值相同的“MVNOID”参数。 |
| NILRSWITCH | 紧急呼叫NI-LR支持开关 | 可选必选说明：必选参数<br>参数含义：该参数用于控制紧急呼叫流程是否发起NI-LR流程。<br>数据来源：整网规划<br>取值范围：<br>- OFF（关）：表示紧急呼叫流程不发起NI-LR流程。<br>- ON（开）：表示紧急呼叫流程发起NI-LR流程。<br>默认值：无<br>说明：该参数与VoLTE紧急呼叫特性license和VoLTE紧急呼叫的定位（NI-LR）特性license共同完成紧急呼叫NI-LR功能的开启。 |
| GMLCGRPID | GMLC选择策略组索引 | 可选必选说明：条件必选参数<br>参数含义：该参数用于在系统范围内标识一个GMLC选择策略组。<br>前提条件：该参数在"紧急呼叫NI-LR支持开关"参数配置为"开"后生效。<br>数据来源：本端规划<br>取值范围：0~191<br>默认值：无<br>配置原则：<br>- 该参数需要在[**ADD GMLCSELGRP**](../GMLC选择策略组/增加GMLC选择策略组(ADD GMLCSELGRP)_26145810.md)中事先配置，可执行[**LST GMLCSELGRP**](../GMLC选择策略组/查询GMLC选择策略组(LST GMLCSELGRP)_72345411.md)进行查看。<br>- 同一GMLC选择策略组索引只能被[**ADD LCSPARAEX**](增加LCS扩展参数(ADD LCSPARAEX)_26305624.md)引用一次。 |
| RPTTYPE | 上报类型 | 可选必选说明：条件可选参数<br>参数含义：该参数用于配置紧急呼叫场景触发NI-LR流程的上报方式。<br>前提条件：该参数在"紧急呼叫NI-LR支持开关"参数配置为"开"后生效。<br>数据来源：整网规划<br>取值范围：<br>- IMMEDIATELY（立刻上报）：当MME识别出紧急呼叫时，立刻发送Subscriber Location Report消息给GMLC，消息中的定位信息只有ECGI。<br>- LOCATE（定位上报）：当MME识别出紧急呼叫时，MME获取E-SMLC的定位信息后再上报给GMLC。<br>默认值：LOCATE（定位上报）<br>配置原则：无卡用户MT-LR流程中，LRF/GMLC选择MME依赖于NI-LR流程中上报的信息。如果在做MT-LR时，LRF/GMLC还没收到NI-LR流程的上报信息，则会导致MT-LR流程失败。所以当网络中定位时延较大时，建议勾选"立刻上报"。<br>说明：- 配置时，至少要勾选一种上报类型。<br>- 当同时勾选“立即上报”和“定位上报”时，NI-LR流程中可能会给GMLC发送两次Subscriber Location Report。 |
| SPTDFTBRCALL | 是否支持缺省承载呼叫 | 可选必选说明：条件可选参数<br>参数含义：该参数表示网络中是否支持使用缺省承载进行紧急呼叫。<br>前提条件：该参数在"紧急呼叫NI-LR支持开关"参数配置为"开"后生效。<br>数据来源：整网规划<br>取值范围：<br>- NO（不支持）<br>- YES（支持）<br>默认值：NO（不支持）<br>配置原则：紧急专有承载创建失败时，如果网络侧允许使用紧急缺省承载进行通话，将本参数设置为YES（支持）。 |
| CRTBRTMINTERVAL | 创建承载时间间隔（秒） | 可选必选说明：条件可选参数<br>参数含义：该参数表示紧急缺省承载和紧急专有承载创建的最大时间间隔。如果紧急附着或者PDN连接建立流程创建紧急缺省承载后，网络侧在该时间间隔内没有发起紧急专有承载创建，则认为使用了紧急缺省承载通话。<br>前提条件：该参数在"是否支持缺省承载呼叫"参数配置为"支持"后生效。<br>数据来源：整网规划<br>取值范围：2~15<br>默认值：2<br>配置原则：根据系统中紧急呼叫流程，紧急专有承载和紧急缺省承载创建的实测的时间间隔来配置。 |
| RLSRPT | 紧急呼叫释放是否触发上报 | 可选必选说明：条件可选参数<br>参数含义：该参数用于控制紧急呼叫释放场景是否触发NI-LR上报。<br>前提条件：该参数在"紧急呼叫NI-LR支持开关"参数配置为"开"后生效。<br>数据来源：整网规划<br>取值范围：<br>- NO（否）：紧急呼叫释放场景不触发NI-LR流程。<br>- YES（是）：急呼叫释放场景触发NI-LR流程。<br>默认值：NO（否）<br>说明：缺省承载通话场景，呼叫释放MME无法识别，本参数只对专有承载通话释放场景生效。 |
| HORPTTYPE | HO上报类型 | 可选必选说明：条件必选参数<br>参数含义：该参数用于控制由Handover/SRVCC/TAU流程触发NI-LR流程时，由源侧MME还是目标侧MME/MSC/AMF上报定位信息。<br>前提条件：该参数在"紧急呼叫NI-LR支持开关"参数配置为"开"后生效。<br>数据来源：整网规划<br>取值范围：<br>- SOURCE（源侧上报）：由源侧MME上报。<br>- TARGET（目标侧上报）：由目标侧MME/MSC/AMF上报。<br>默认值：无<br>配置原则：<br>- 协议规定源侧或者目标侧只能有一侧进行上报，该参数在整网MME/MSC/AMF中需要配置一致。<br>- 若用户Handover/TAU/SRVCC到新侧，目标MME/MSC/AMF不能识别并触发紧急呼叫NI-LR，则配置成SOURCE（由源侧上报）。<br>- 当此参数配置成SOURCE（由源侧上报）时，为了GMLC直接定位到用户所在MME或MSC，需配置MME为携带MME Identifier和MSC-Number信元，相关配置参考[**ADD MMECHARACT**](../../../GTP-C接口管理/GnGp-SGSN_S10_S16_S3接口管理/MME属性/增加MME属性配置信息（ADD MMECHARACT）_26305766.md)的“MMEIDIE”参数及[**ADD MSCPARA**](../../../GTP-C接口管理/Sv接口管理/MSC参数/增加MSC参数(ADD MSCPARA)_72225657.md)命令。 |
| LRCBEFOREESMLC | 和E-SMLC交互前是否启动LRC流程 | 可选必选说明：条件可选参数<br>参数含义：该参数用于控制MME在发送Location Request给E-SMLC之前，是否通过Location Report Control消息获取最新的ECGI。<br>前提条件：该参数在"紧急呼叫NI-LR支持开关"参数配置为"开"且"上报类型"参数勾选了"定位上报"后生效。<br>数据来源：整网规划<br>取值范围：<br>- NO（否）：不触发Location Report Control消息。<br>- YES（是）：触发Location Report Control消息。<br>默认值：YES（是）<br>配置原则：E-SMLC使用ECGI信息做辅助定位。<br>说明：当参数设置为“YES（是）”时，“ 小区位置信息上报功能（S11接口）”特性的相关license授权并开启后，此参数配置才生效（特性编号：WSFD-<br>106403<br>，license部件编码：LKV2LCR01）。 |
| LRCAFTERESMLC | 和E-SMLC交互后是否启动LRC流程 | 可选必选说明：条件可选参数<br>参数含义：该参数用于控制E-SMLC响应Location Response超时或者失败时，是否通过Location Report Control消息获取最新的ECGI。<br>前提条件：该参数在"紧急呼叫NI-LR支持开关"参数配置为"开"且"上报类型"参数勾选了"定位上报"后生效。<br>数据来源：整网规划<br>取值范围：<br>- NO（否）：不触发Location Report Control消息。<br>- YES（是）：触发Location Report Control消息。<br>默认值：YES（是）<br>配置原则：紧急呼叫中心使用ECGI信息做辅助定位。<br>说明：当参数设置为“YES（是）”时，“ 小区位置信息上报功能（S11接口）”特性的相关license授权并开启后，此参数配置才生效（特性编号：WSFD-<br>106403<br>，license部件编码：LKV2LCR01）。 |
| HA | 水平精度 | 可选必选说明：条件可选参数<br>参数含义：Location Request消息中的LCS QoS信元中的“Horizontal Accuracy”字段。<br>前提条件：该参数在"紧急呼叫NI-LR支持开关"参数配置为"开"且"上报类型"参数勾选了"定位上报"后生效。<br>数据来源：整网规划<br>取值范围：0~127<br>默认值：19<br>配置原则：根据协议3GPP TS 23.032 V13.0.0，水平距离r（米）和K（水平精度）之间的关系为r = 10*(1.1<br>K<br>-1)。例如，当K设置为19时，r的取值为51米。 |
| RT | 响应时间 | 可选必选说明：条件可选参数<br>参数含义：Location Request消息中的LCS QoS信元中的“Response Time”字段。<br>前提条件：该参数在"紧急呼叫NI-LR支持开关"参数配置为"开"且"上报类型"参数勾选了"定位上报"后生效。<br>数据来源：整网规划<br>取值范围：<br>- LOW_DELAY（低时延）<br>- DELAY_TOLERANT（时延可接受）<br>默认值：LOW_DELAY（低时延） |
| IV | 移动速度 | 可选必选说明：条件可选参数<br>参数含义：Location Request消息中的Include Velocity信元。<br>前提条件：该参数在"紧急呼叫NI-LR支持开关"参数配置为"开"且"上报类型"参数勾选了"定位上报"后生效。<br>数据来源：整网规划<br>取值范围：<br>- NOT_REQUESTED（不请求）：不请求移动速度。<br>- REQUESTED（请求）：请求移动速度。<br>默认值：NOT_REQUESTED（不请求） |
| DESC | 描述 | 可选必选说明：可选参数<br>参数含义：该参数用于指定LCS扩展软件参数表的描述信息。<br>数据来源：本端规划<br>取值范围：0~32位字符串<br>默认值：noname |

## 操作的配置对象

- [LCS扩展参数（LCSPARAEX）](configobject/UNC/20.15.2/LCSPARAEX.md)

## 使用实例

增加一条LCS扩展参数配置，打开NOID为0的运营商的紧急呼叫NI-LR功能，并将定位信息上报到指定的GMLC，该GMLC在索引为1的GMLC选择策略组内。

ADD LCSPARAEX: NOID=0, NILRSWITCH=ON, GMLCGRPID=1, SPTDFTBRCALL=NO, HORPTTYPE=SOURCE;

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加LCS扩展参数(ADD-LCSPARAEX)_26305624.md`
