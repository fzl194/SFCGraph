# Batch-07: 重点业务保障 - UNC侧配置与UPCF侧配置、数据规划与调测

## 1. 概述

本批文档聚焦"5G Core 重点业务保障解决方案"中初始业务配置阶段的 UNC侧（SMF）和 UPCF侧的配置操作，以及跨网元的数据规划与端到端调测。核心解决以下问题：

- **智能UPF选择**：SMF如何选择支持质差分析的智能UPF，使重点业务保障功能能够采集用户体验质量数据。典型场景下由PCF指示触发，异厂商PCF场景下由SMF预定义规则触发。
- **智能PCF选择**：异厂商PCF场景下，SMF如何建立"双N7会话"——即同时对接异厂商PCF（标准PCF）和华为智能PCF，使策略控制分流到智能PCF进行QoS分析订阅。
- **实时位置上报**：UNC侧配置SMF支持基于实时位置的策略控制，包含4G/5G互操作的位置变更订阅。
- **UPCF侧策略配置**：典型场景配置条件组-动作组-规则-策略-业务五层模型；异厂商PCF场景配置简化的N23策略。
- **全局业务数据规划**：应用大类(appId)、应用小类(subAppId)、三层协议、体验基线KPI、大流判断、5QI/GBR/MBR保障建议等需要跨UPCF/UDC/UDG三网元统一规划的数据。
- **GBR保障 vs Non-GBR保障调测**：两种保障类型的端到端信令验证流程差异——GBR建立专载（5qi=4、AF携带带宽参数），Non-GBR仅下发QoS策略不建立专载。

**文档来源**：4个UNC侧配置 + 2个UPCF侧配置 + 2个数据规划 + 2个调测文档。

---

## 2. 核心知识点

### K-01: 智能UPF选择的两种模式——PCF指示 vs 预定义规则

重点业务保障要求SMF选择支持质差分析的智能UPF。根据PCF厂商不同，SMF有两种触发方式：

| 维度 | 典型场景（PCF指示模式） | 异厂商PCF场景（预定义规则模式） |
|------|------------------------|-------------------------------|
| **触发源** | PCF下发`UpfSelectRule`动作，SMF被动执行UPF选择 | SMF本地预定义用户模板，主动匹配用户套餐 |
| **关键命令** | `ADD UPFBINDSELRULE` + `ADD SELECTRULEINFO`(RULEFUNC=QOSANA) | `ADD USERPROFILE`(UPTYPE=UPSELECT) + `ADD SELECTRULEINFO`(RULEFUNC=QOSANA-1&QOSEXP-1) |
| **规则功能** | `QOSANA` | `QOSANA-1 & QOSEXP-1`（含体验感知） |
| **PFCP私有信元** | `SET PFCPPVTEXT: FEATURE=Qos_Analysis` | `SET PFCPPVTEXT: FEATURE=Qos_Analysis` + `FEATURE=Qos_Experience` |
| **UPF权重配置** | `MOD PNFPROFILE: CAPACITY=60`（需按公式计算） | 无显式权重配置（通过UPF实例名称绑定） |
| **DELIVERSW参数** | 不涉及 | `DISABLE`（不下发给UPF） |
| **UPF选择优先级** | 双域+智能UPF > 双域UPF > 智能UPF > 普通UPF | 同左（文档未重复说明，属全局规则） |

**证据**：
- 典型场景：`ADD SELECTRULEINFO` 的 RULEFUNC 仅配置 `QOSANA`；UPF绑定通过 `ADD UPFBINDSELRULE` 使用索引+UPF实例名称+规则名称。
- 异厂商场景：`ADD SELECTRULEINFO` 的 RULEFUNC 配置 `QOSANA-1&QOSEXP-1`，且新增 `PRIORITY=0` 和 `DELIVERSW=DISABLE` 参数；UPF绑定通过 `ADD UPFBINDSELRULE` 使用相同的命令但参数项更精简。

**典型场景完整MML示例**：
```
SET SMCOMMFUNC: QOSANASW=Support;
ADD UPFBINDSELRULE: INDEX=1, NFINSTANCENAME="upf_instance_1", RULENAME="select_ai_upf";
ADD UPFBINDSELRULE: INDEX=2, NFINSTANCENAME="upf_instance_2", RULENAME="select_ai_upf";
ADD SELECTRULEINFO: RULENAME="select_ai_upf", RULEFUNC=QOSANA;
SET PFCPPVTEXT: FEATURE=Qos_Analysis, SWITCH=ENABLE;
MOD PNFPROFILE: NFINSTANCEID="upf_instance_1", CAPACITY=60;
MOD PNFPROFILE: NFINSTANCEID="upf_instance_2", CAPACITY=60;
```

**异厂商场景完整MML示例**：
```
SET SMCOMMFUNC: QOSANASW=Support;
SET SMFFUNC: EVENTEXPOSURE=Support;
ADD USERPROFILE: USERPROFILENAME="testruleupf", UPTYPE=UPSELECT;
ADD SELECTRULEINFO: RULENAME="testruleupf", RULEFUNC=QOSANA-1&QOSEXP-1, PRIORITY=0, DELIVERSW=DISABLE;
ADD UPFBINDSELRULE: INDEX=0, NFINSTANCENAME="a6a61c6f-0d3a-4221-b1da-123eda3ccf76", RULENAME="testruleupf";
SET PFCPPVTEXT: FEATURE=Qos_Analysis, SWITCH=ENABLE;
SET PFCPPVTEXT: FEATURE=Qos_Experience, SWITCH=ENABLE;
```

**UPF权重计算公式**（仅典型场景需要）：
```
权重 = (智能板UPF规划的普通用户流量) / (非智能板UPF规划的普通用户流量) * (非智能板UPF的权重)
```
建议具备智能板的UPF权重不高于此计算值，以避免普通用户流量过度集中到智能UPF。

**双域+智能UPF的优先级规则**：
双域多DNN策略优先级高于智能策略，SMF选择UPF优先级顺序为：
`双域+智能UPF > 双域UPF > 智能UPF > 普通UPF`
为支持同时签约双域智能分流和重点业务保障的用户同时享有两种服务，至少一对智能UPF必须支持双域智能分流业务。

### K-02: 智能PCF选择——双N7会话机制（异厂商PCF场景专属）

当PCF为异厂商时，标准N7接口可能不支持重点业务保障的智能策略。解决方案是让SMF同时对接异厂商PCF（标准策略）和华为智能PCF（智能策略），建立"双N7会话"。

**核心配置链**：
1. **开启功能**：`SET IPEN7SESSFUNC: IPEN7SESSFUNC=ENABLE`
2. **配置智能PCF组**：`ADD TNFGRP`（目标NF组）→ `ADD TNFINS`（目标NF实例，含FQDN）→ `ADD TNFINSIP`（IP+端口）→ `ADD TNFBINDGRP`（绑定组，含PRIORITY和WEIGHT）
3. **指定主智能PCF组**：`SET DFTIPEPCFGRP: PRIMIPEPCFGRP="IPE_PCF_GROUP_0"`
4. **配置业务策略规则**：`ADD RULE`（POLICYTYPE=PCC，NWDAFEVENTS=QOS_ANALYSIS）
5. **配置智能业务后缀**：`ADD IPEN7SUFFIX`（INTELLISUFFIX + INTELLINAME）

**匹配机制**：SMF根据用户套餐和`ADD RULE`配置的规则名匹配，匹配成功后与智能PCF建立第二个N7会话。后缀（INTELLISUFFIX）用于与PCF下发的rulename后缀进行二次匹配。

**IPERULEDELYSW开关**：如果UPF上没有预定义规则对应的 `ADD USERPROFILE/ADD RULE/ADD RULEBINDING` 配置记录，需要设置 `IPERULEDELYSW=DISABLE` 关闭智能规则传递。

**完整MML示例**：
```
SET IPEN7SESSFUNC: IPEN7SESSFUNC=ENABLE;

ADD TNFGRP: TNFGRPINDEX=0, TNFTYPE=PCF, TNFGRPNAME="IPE_PCF_GROUP_0";
ADD TNFINS: TNFINSINDEX=1, TNFTYPE=PCF, TNFINSNAME="a6a61c6f-0d3a-4221-b1da-306eda3ccf67",
  SCHEMA=http, FQDN="pcf1.cluster1.net2.pcf.5gc.mnc012.mcc345.3gppnetwork.org", NFDESCNAME="IPE_PCF";
ADD TNFINSIP: TNFINSINDEX=1, IPTYPE=IPV4, IPV4ADDR="10.10.12.3", PORT=1234;
ADD TNFBINDGRP: TNFGRPINDEX=0, TNFINSINDEX=1, PRIORITY=1, WEIGHT=50;

SET DFTIPEPCFGRP: PRIMIPEPCFGRP="IPE_PCF_GROUP_0";

ADD RULE: RULENAME="testrulepcf", POLICYTYPE=PCC, POLICYNAME="pccprop_test",
  NWDAFEVENTS=QOS_ANALYSIS, IPERULEDELYSW=DISABLE;

ADD IPEN7SUFFIX: INTELLISUFFIX="rulepcf", INTELLINAME="LIVE_VIDEO";
```

**智能PCF实例的关键参数说明**：
- `TNFGRPINDEX`：目标NF组索引，需与TNFBINDGRP中的TNFGRPINDEX对应
- `TNFINSNAME`：NF实例名称，通常是UUID格式，需全网唯一
- `FQDN`：全限定域名，格式为`pcf实例名.cluster.网络域.5gc.mncXXX.mccXXX.3gppnetwork.org`
- `PRIORITY`：同组内PCF实例的优先级，数字越小优先级越高
- `WEIGHT`：同优先级实例间的负载分担权重

### K-03: 实时位置上报配置要素

实时位置上报支撑基于位置的策略控制和质差分析。配置分为四个层次：

| 层次 | 关键参数 | 说明 |
|------|---------|------|
| **License开关** | `SET LICENSESWITCH: LICITEM=LKV2PYCTRL1, SWITCH=ENABLE` | 开启基于实时位置的策略控制功能 |
| **事件订阅能力** | `SET SMFFUNC: EVENTEXPOSURE=Support` | 开启SMF事件订阅与上报功能 |
| **位置变更订阅** | `SET SMCOMMFUNC: LOCATIONCHSW=Support` | 开启位置变更事件订阅（SCELL_CH、SAREA_CH、SCNN_CH） |
| **能力开放位置上报** | `ADD APN: EXPOSURELOCRPT=ENABLE` | 指定APN开启能力开放触发位置上报 |
| **4G重点业务保障** | `SET MMFUNC: LOCRPTTIMER=600`（秒） | 实时位置上报最小间隔 |
| | `SET LOCATIONREPORT: MSINFOTIMER=600`（秒） | 位置更新消息上报迟滞控制时长 |
| | `SET POLICYMODE: BY5GSIWKI=ENABLE` | 按5GS互操作指示选择策略接口 |
| | `SET POLICYMODE: BYIWKUEN5GR4G=ENABLE` | 非5G终端4G接入按5GS互操作指示选择策略接口 |
| | `SET POLICYMODE: TMACCTYPE` | 指定终端和接入类型（UE5G_RAT4G / UENON5G_RAT4G） |

**注意**：修改`LOCRPTTIMER`和`MSINFOTIMER`对网元性能有较大影响，需联系华为技术支持评估。

### K-04: UPCF侧配置——典型场景的五层模型

典型场景下UPCF侧采用"条件组→动作组→规则→策略→业务"的五层配置模型，支撑两类业务：

**业务1: N23_Service01（Activated By PCEF）**——保障用户基于签约触发N23事件订阅：
- 策略：N23_Policy01，触发器 `RAT_TY_CH` + `IPCAN_EST`
- 规则链：N23_Rule01（UpfSelectRule动作→选择智能UPF）→ N23_Rule02（5G NR接入→CmdN23EventSubscription status=NORMAL）→ N23_Rule03（4G/2G接入→CmdN23EventSubscription status=SUSPEND）
- 关键条件：`SmfSession.upfActive=select_ai_upf`（智能UPF选择成功）、`SmfSession.RatType`（制式判断）、`SmfSession.initEutraTac/initNRTac`（TAC区域过滤）

**业务2: AFQos_Service01（Activated By AF）**——AF请求业务高带宽时建立专有QoS Flow：
- 策略：AFQos_Policy01，触发器 `AFSessionAuthorization`
- 规则：AFQos_Rule01（DynamicPccRuleIMS类型），条件 `AfSession.MediaType=Application`
- 动作链：DynamicPccRule → QoSData(5qi=4, maxbrDl/Ul, gbrDl/Ul来自AfSession) → Arp(priorityLevel=1) → TrafficControlData → ChargingData（可选）

**N23事件订阅的关键约束**：
- 只允许5G Smf Pcc Rule、Non-PCC规则关联CmdN23EventSubscription动作
- 同一规则只能关联一个CmdN23EventSubscription动作
- 一个CmdN23EventSubscription仅支持一个event事件
- 系统所有QOS_ANALYSIS事件的appIds最大40个，所有appIds总计不超过255个

**典型场景条件组详情（6组）**：

| 条件组 | 名称 | 关系 | 核心条件 |
|--------|------|------|---------|
| 条件组1 | SubscriberStatus_CG01 | AND | Subscriber.SubscriberIdentifier != System.Null（用户签约ID不为空=恒真条件） |
| 条件组2 | N23_CG01 | AND | SmfSession.upfActive=select_ai_upf AND SmfSession.SmfId=指定SMF实例ID |
| 条件组3 | SmfSessionRatType_CG01 | AND | SmfSession.RatType=NR（5G接入） |
| 条件组4 | SmfSessionRatType_CG02 | OR | SmfSession.RatType=EUTRA OR GERA（4G/2G接入） |
| 条件组5 | SmfSessionTac_CG01 | OR | SmfSession.initEutraTac=4305 OR SmfSession.initNRTac=63F84B（TAC区域过滤） |
| 条件组6 | AfSessionMediaType_CG01 | AND | AfSession.MediaType=Application（AF会话媒体类型=应用） |

**规则与条件组的映射关系**：
- N23_Rule01（选UPF）：条件组1（恒真）→ 动作UpfSelectRule
- N23_Rule02（5G触发N23订阅）：条件组2+3+5 → 动作CmdN23EventSubscription(status=NORMAL)
- N23_Rule03（4G暂停N23订阅）：条件组2+4+5 → 动作CmdN23EventSubscription(status=SUSPEND)
- AFQos_Rule01（AF带宽保障）：条件组6 → 动作DynamicPccRuleIMS

**注意**：4G和5G的TAC都需要配置（条件组5使用OR关系），否则跨制式切换时无法匹配。N23_Rule03的status=SUSPEND用于4G/2G接入时暂停N23事件订阅，因为质差分析在5G NR下才有效。

**UPCF MML脚本示例（典型场景核心部分）**：
```
// 条件组
ADD CONDITIONGROUP:CONDITIONGROUPNAME="SubscriberStatus_CG01",RELATION=AND,USETIMEZONE=No;
ADD CONDITIONGROUP:CONDITIONGROUPNAME="N23_CG01",RELATION=AND,USETIMEZONE=No;
ADD CONDITIONGROUP:CONDITIONGROUPNAME="SmfSessionTac_CG01",RELATION=OR,USETIMEZONE=No;
ADD CONDITION:CONDITIONGROUPNAME="SubscriberStatus_CG01",CONDITIONNAME="SubscriberStatus_C01",
  OBJECTATTRIBUTE="Subscriber.SubscriberIdentifier",OPERATOR=Not Equal,
  RIGHTVALUETYPE=Attribute,RIGHTOBJECTATTRIBUTE="System.Null";
ADD CONDITION:CONDITIONGROUPNAME="N23_CG01",CONDITIONNAME="N23_C01",
  OBJECTATTRIBUTE="SmfSession.upfActive",OPERATOR=Equal,
  RIGHTVALUETYPE=Value,RIGHTVALUE="select_ai_upf";

// 动作组 - 选择智能UPF
ADD NGACTION:ACTIONNAME="UpfSelect_AG01",TYPE="UpfSelectRule";
ADD NGACTIONATTR:ACTIONNAME="UpfSelect_AG01",ATTRNAME="reportInd",TYPE=Value,VALUE="True";
ADD NGACTIONATTR:ACTIONNAME="UpfSelect_AG01",ATTRNAME="upfSelectId",TYPE=Value,VALUE="select_ai_upf";

// 动作组 - N23订阅(5G激活)
ADD NGACTION:ACTIONNAME="CmdN23Event_AG01",TYPE="CmdN23EventSubscription";
ADD NGACTIONATTR:ACTIONNAME="CmdN23Event_AG01",ATTRNAME="status",TYPE=Value,VALUE="NORMAL";
ADD NGACTIONATTR:ACTIONNAME="CmdN23Event_AG01",ATTRNAME="appIds",TYPE=Value,VALUE="appgroup1";
ADD NGACTIONATTR:ACTIONNAME="CmdN23Event_AG01",ATTRNAME="event",TYPE=Value,VALUE="QOS_ANALYSIS";

// 动作组 - N23订阅(4G暂停)
ADD NGACTION:ACTIONNAME="CmdN23Event_AG02",TYPE="CmdN23EventSubscription";
ADD NGACTIONATTR:ACTIONNAME="CmdN23Event_AG02",ATTRNAME="status",TYPE=Value,VALUE="SUSPEND";
ADD NGACTIONATTR:ACTIONNAME="CmdN23Event_AG02",ATTRNAME="appIds",TYPE=Value,VALUE="appgroup1";
ADD NGACTIONATTR:ACTIONNAME="CmdN23Event_AG02",ATTRNAME="event",TYPE=Value,VALUE="QOS_ANALYSIS";
```

**AF QoS保障的动作组链（DynamicPccRule完整链）**：
```
// Arp - 优先级与抢占
ADD NGACTIONATTR:ACTIONNAME="Arp_AG01",ATTRNAME="priorityLevel",TYPE=Value,VALUE="1";
ADD NGACTIONATTR:ACTIONNAME="Arp_AG01",ATTRNAME="preemptCap",TYPE=Value,VALUE="NOT_PREEMPT";
ADD NGACTIONATTR:ACTIONNAME="Arp_AG01",ATTRNAME="preemptVuln",TYPE=Value,VALUE="NOT_PREEMPTABLE";

// QoSData - 带宽参数（来源AF会话对象属性）
ADD NGACTIONATTR:ACTIONNAME="QoSData_AG01",ATTRNAME="5qi",TYPE=Value,VALUE="4";
ADD NGACTIONATTR:ACTIONNAME="QoSData_AG01",ATTRNAME="maxbrDl",TYPE=Object Attribute,VALUE="AfSession.MediaMaxBandwidthDL";
ADD NGACTIONATTR:ACTIONNAME="QoSData_AG01",ATTRNAME="maxbrUl",TYPE=Object Attribute,VALUE="AfSession.MediaMaxBandwidthUL";
ADD NGACTIONATTR:ACTIONNAME="QoSData_AG01",ATTRNAME="gbrDl",TYPE=Object Attribute,VALUE="AfSession.MediaMirBandwidthDL";
ADD NGACTIONATTR:ACTIONNAME="QoSData_AG01",ATTRNAME="gbrUl",TYPE=Object Attribute,VALUE="AfSession.MediaMirBandwidthUL";
ADD NGACTIONATTR:ACTIONNAME="QoSData_AG01",ATTRNAME="arp",TYPE=Reference ActionGroup,VALUE="Arp_AG01";

// DynamicPccRule - 动态PCC规则组合
ADD NGACTIONATTR:ACTIONNAME="DynamicPccRule_AG01",ATTRNAME="pccRuleId",TYPE=Value,VALUE="N5_Pcc01";
ADD NGACTIONATTR:ACTIONNAME="DynamicPccRule_AG01",ATTRNAME="refQosData",TYPE=Reference ActionGroup,VALUE="QoSData_AG01";
ADD NGACTIONATTR:ACTIONNAME="DynamicPccRule_AG01",ATTRNAME="refTcData",TYPE=Reference ActionGroup,VALUE="TCData_AG01";
ADD NGACTIONATTR:ACTIONNAME="DynamicPccRule_AG01",ATTRNAME="refChgData",TYPE=Reference ActionGroup,VALUE="ChargingData_AG01";
```

**QoSData带宽参数来源说明**：AF请求中携带的带宽参数（maxbrUl/Dl来自AfSession.MediaMaxBandwidthUL/DL，gbrUl/Dl来自AfSession.MediaMirBandwidthUL/DL）直接注入QoSData动作组，决定专载的GBR和MBR值。

### K-05: UPCF侧配置——异厂商PCF场景的简化N23策略

异厂商PCF场景下，UPCF侧配置大幅简化，核心是通过`NeedN23Subs`条件触发N23订阅：

| 配置层 | 典型场景 | 异厂商PCF场景 |
|--------|---------|-------------|
| **条件组** | 6组（SubscriberStatus、N23_CG01含upfActive+SmfId、RatType×2、Tac、AfSessionMediaType） | 1组（IPEQos_CG：`SmfSession.NeedN23Subs = QOS_ANALYSIS`） |
| **动作组** | 8组（UpfSelectRule、CmdN23×2、TCData、Arp、QoSData、ChargingData、DynamicPccRule） | 1组（CmdN23EventSubscription：event=QOS_ANALYSIS, appIds=appgroup1） |
| **规则** | 4条（N23_Rule01-03 + AFQos_Rule01），含5G Smf Pcc Rule和5G Smf Pcc Rule for IMS | 1条（IPEQos_Rule，类型=Non-PCC） |
| **策略** | 2个（N23_Policy01触发RAT_TY_CH+IPCAN_EST，AFQos_Policy01触发AFSessionAuthorization） | 1个（IPEQos_Policy，类型=N7 Policy，触发IPCAN_EST） |
| **业务** | 2个（PCEF激活+AF激活），AF业务`签约后才能使用=否` | 1个（PCEF激活），`签约后才能使用=是` |
| **应用映射** | `ADD APPLICATIONSERVICEMAPPING: APPID=appgroup1` | 无应用映射（N23订阅直接携带appIds） |

**关键差异**：异厂商场景不配置AF业务（因为异厂商PCF自身处理AF请求），只配置PCEF业务触发N23订阅；规则类型用`Non-PCC`而非`5G Smf Pcc Rule`。

**异厂商场景UPCF N23策略完整MML脚本**：
```
// 条件组 - 基于NeedN23Subs条件触发
ADD CONDITIONGROUP:CONDITIONGROUPNAME="IPEQos_CG",RELATION=AND,USETIMEZONE=No;
ADD CONDITION:CONDITIONGROUPNAME="IPEQos_CG",CONDITIONNAME="IPEQos_C",
  OBJECTATTRIBUTE="SmfSession.NeedN23Subs",OPERATOR=Equal,
  RIGHTVALUETYPE=Value,RIGHTVALUE="QOS_ANALYSIS";

// 动作组 - N23事件订阅
ADD NGACTION:ACTIONNAME="IPEQos_AG",TYPE="CmdN23EventSubscription";
ADD NGACTIONATTR:ACTIONNAME="IPEQos_AG",ATTRNAME="event",TYPE=Value,VALUE="QOS_ANALYSIS";
ADD NGACTIONATTR:ACTIONNAME="IPEQos_AG",ATTRNAME="appIds",TYPE=Value,VALUE="appgroup1";

// 规则 - Non-PCC类型
ADD RULE:RULENAME="IPEQos_Rule",TYPE=Non-PCC,VOLUMEUSAGEROUNDING=No,EDR=OFF,RELATION=AND;
ADD RULECONDITIONGROUP:RULENAME="IPEQos_Rule",CONDITIONGROUPNAME="IPEQos_CG";
ADD RULENGACTION:RULENAME="IPEQos_Rule",ACTIONNAME="IPEQos_AG";

// 策略 - N7 Policy
ADD POLICY:POLICYNAME="IPEQos_Policy",TYPE=N7 Policy;
ADD POLICYRULE:POLICYNAME="IPEQos_Policy",RULENAME="IPEQos_Rule";
ADD POLICYTRIGGER:POLICYNAME="IPEQos_Policy",TRIGGERNAME="IPCAN_EST";

// 业务 - PCEF激活，需签约
ADD SERVICE:SERVICENAME="IPEQos_Service",SERVICETYPE=VALUE_ADDED_SERVICE,
  ACTIVATEDBY=PCEF,PRECEDENCE=0,QOSMODE=Replace,SUBSCRIPTIONFORCED=Yes,
  PROBILLDATE=No,QUOTAALLOCATIONMODE=None;
ADD SERVICEPOLICY:SERVICENAME="IPEQos_Service",POLICYNAME="IPEQos_Policy";
```

**异厂商场景前提条件**：需先完成UPCF与NWDAF的对接数据配置（不同于典型场景需要UPCF与NRF+NWDAF对接）。

### K-06: 全局业务数据规划——跨网元统一数据

全局数据规划确保UPCF、UDC、UDG三个网元的应用标识、QoS参数、保障建议一致。

**数据规划层次**：

| 数据对象 | UPCF侧 | UDC侧 | UDG侧 | 统一取值 |
|---------|--------|-------|-------|---------|
| **应用大类(appId)** | ADD NGACTIONATTR(appIds的VALUE) | ADD APPGROUP(APPGROUPNAME) | ADD APPPOLICYCTRL(APPIDNAME) | appgroup1（如live_streaming） |
| **应用小类(subAppId)** | 不涉及 | ADD APP(APPNAME) | ADD APPPOLICYCTRL(SUBAPPIDNAME) | app1（如kuaishou_live） |
| **三层协议** | 不涉及 | 不涉及 | ADD SSUPROTCOLGROUP(PROTOCOLNAME) | 如taobao_openlive |
| **体验基线KPI** | 不涉及 | 不涉及 | ADD POLICYCONDITION(UPLINKAVGRATE/DOWNLINKAVGRATE) | 如300（Kbps） |
| **大流判断方向** | 不涉及 | 不涉及 | ADD SSUPROTCOLGROUP(QOEDETECTCOND) | UP_BIGFLOW_CHECK |
| **大流判断阈值** | 不涉及 | 不涉及 | ADD POLICYCONDITION(UPFLOWTHRD/DNFLOWTHRD) | 如15（Kbps） |
| **5QI** | ADD NGACTIONATTR(5qi的VALUE) | ADD APPGROUP(FQI) | 不涉及 | 4（直播/会议/视频）；3（游戏） |
| **GBR上行/下行** | 不涉及 | ADD APPGROUP/APP(GBRULVALUE/GBRDLVALUE) | 不涉及 | 如3000/1000（Kbps） |
| **MBR上行/下行** | 不涉及 | ADD APPGROUP/APP(MBRULVALUE/MBRDLVALUE) | 不涉及 | 如1000000/1000000（Kbps） |

**重要规则**：`ADD APP`的优先级高于`ADD APPGROUP`——同一应用组下不同应用可设置不同GBR/MBR值，但5QI和ARP必须统一。

**预定义规则规划（异厂商场景专属）**：选择智能UPF的USERPROFILE名称与选择智能PCF的RULE名称不能相同（如`testruleupf` vs `testrulepcf`），否则会产生匹配冲突。

**典型场景保障应用推荐值表（部分）**：

| 应用大类 | appId推荐值 | 应用小类 | subAppId推荐值 | 5QI | GBR上行 | GBR下行 | 体验基线(上行) | 大流方向 | 大流阈值 |
|---------|-----------|---------|--------------|------|---------|---------|-------------|---------|---------|
| 直播 | live_streaming | 快手 | kuaishou_live | 4 | 3000 | 1000 | 1750Kbps | 大上行 | 120Kbps |
| 直播 | live_streaming | 抖音 | douyin_live | 4 | 4000 | 1000 | 2000Kbps | 大上行 | 256Kbps |
| 直播 | live_streaming | 虎牙 | huya_live | 4 | 6000 | 1000 | 4000Kbps | 大上行 | 120Kbps |
| 会议 | meeting | 腾讯会议 | tencent_meeting | 4 | 1500 | 1500 | 1000Kbps | 大上行 | 100Kbps |
| 会议 | meeting | 飞书 | feishu_meeting | 4 | 3000 | 3000 | 2000Kbps | 大上行 | 100Kbps |
| 视频 | vod_streaming | 优酷 | youku_vod | 4 | 1000 | 3000 | 2000Kbps(下行) | 大下行 | 400Kbps |
| 视频 | vod_streaming | 哔哩哔哩 | bilibili_vod | 4 | 1000 | 5000 | 3000Kbps(下行) | 大下行 | 400Kbps |
| 游戏 | mobile_game | 和平精英 | hepingjingying_game | 3 | 1000 | 1000 | 512Kbps(下行) | 双向 | 0Kbps |
| 游戏 | mobile_game | 王者荣耀 | wangzherongyao_game | 3 | 1000 | 1000 | 512Kbps(下行) | 双向 | 0Kbps |
| 即时通讯 | instant_message | 微信IM | weixin_im | 4 | 5000 | 5000 | 4000Kbps(上行) | 大上行 | 160Kbps |
| 即时通讯 | voip | 微信VOIP | weixin_voip | 4 | 3000 | 3000 | 1500Kbps(上行) | 大上行 | 100Kbps |

> 注：上述为推荐值，实际取值以运营商规划与设计为准。MBR上下行通常为1000000Kbps（约1Gbps），对保障流量不设上限。

**关键观察**：
- 直播类应用上行带宽需求远高于下行（主播上传为主），GBR上行普遍3000-6000Kbps
- 视频点播类相反，下行带宽需求高，GBR下行3000-6000Kbps
- 游戏类5QI=3（低延迟），GBR仅1000Kbps，大流阈值为0（游戏流量较小但需低延迟保障）
- 会议类上下行对称（双向音视频），GBR上下行相同

### K-07: GBR保障 vs Non-GBR保障的调测差异

两种保障类型的端到端信令流程高度相似，核心差异在保障动作和验证点：

**共同流程（9步）**：
1. 设置质差检测条件（`ADD POLICYCONDITION`调高速率基线/调低时延基线）
2. PCF→NWDAF：QoS分析订阅（Nnwdaf_EventsSubscription_Subscribe Request）
3. NWDAF→PCF：订阅响应（201 Created，event=QOS_ANALYSIS）
4. NWDAF→SMF：订阅请求（Nsmf_EventExposure，event=QOS_ANA）
5. SMF→UPF：订阅请求（PFCP_Session_Modification_Request，SRR信元携带app-id）
6. SMF→NWDAF：订阅成功响应（201 Created，subId+appIds）
7. UPF→NWDAF：质差事件上报（Nupf_EventExposure，subAppQosQuality=QOE_QUALITY1）
8. NWDAF→PCF：QoS保障请求（Npcf_PolicyAuthorization_PostAppSessions）
9. PCF→NWDAF：保障成功通知（event=SUCCESSFUL_RESOURCES_ALLOCATION）

**关键差异点**：

| 差异维度 | GBR保障 | Non-GBR保障 |
|---------|---------|-------------|
| **NWDAF→PCF请求参数** | 携带mirBwUl/mirBwDl为保障带宽值 | mirBwUl=0, mirBwDl=0 |
| **保障类型标识** | DSP SUBCTX显示 `保障类型 = GBR` | DSP SUBCTX显示 `保障类型 = Non-GBR` |
| **资源类型** | 建立专有承载（专载） | 仅下发QoS策略，不建专载 |
| **小区容量检查** | 需要执行 `DSP CELLCTX` 查看小区已分配GBR | 不需要（不占用GBR资源） |
| **UDN交互（可选）** | NWDAF→UDN请求小区容量和PRB利用率 | 无UDN交互步骤 |
| **质差未保障原因** | 可能因"小区拥塞"阻塞 | 可能因"小区拥塞"阻塞 |
| **5QI** | 4（直播/会议/视频）、3（游戏） | 不涉及5QI分配 |

**调测技巧**：如果质差未触发，需重新执行步骤1调整质差检测条件（速率类调高、时延类调低），并重新激活用户。

**DSP SUBCTX输出关键字段解读**：

| 字段 | 说明 | 调测用途 |
|------|------|---------|
| 订阅事件 = QOS_ANALYSIS | 确认PCF已发起NWDAF订阅 | 验证订阅链路建立 |
| QoS保障状态 = TRUE/FALSE | 当前是否在保障中 | 判断保障是否已生效 |
| 质差状态 = TRUE/FALSE | 当前是否处于质差 | 判断质差检测是否触发 |
| 质差未保障原因 | 如"小区拥塞" | 诊断保障未生效的根因 |
| 保障类型 = GBR/Non-GBR | 保障资源类型 | 验证保障类型是否符合预期 |
| 历史QoS保障次数 | 历史保障计数 | 判断保障是否曾成功 |
| 小区级保障失败阻塞结束时间 | 小区级阻塞时间窗 | GBR场景小区拥塞时的阻塞计时 |
| 会话级保障失败阻塞结束时间 | 会话级阻塞时间窗 | 会话级保障失败的阻塞计时 |
| 向SMF订阅的事件 = QOS_ANA | NWDAF向SMF订阅的事件 | 确认NWDAF→SMF订阅链路 |

**常见调测问题与处理**：

| 问题 | 可能原因 | 处理方法 |
|------|---------|---------|
| PCF未发起NWDAF订阅 | UPCF业务未签约或策略未匹配 | 检查PSUB/PSRV签约、条件组匹配 |
| NWDAF订阅响应失败 | NWDAF与UPCF对接数据异常 | 检查UPCF与NRF/NWDAF对接配置 |
| SMF未向UPF下发订阅 | SMF侧QOSANASW未开启或UPF非智能 | 检查SET SMCOMMFUNC和UPFBINDSELRULE |
| UPF未上报质差事件 | 质差检测条件设置不当 | 调高速率基线/调低时延基线，重新激活用户 |
| NWDAF未发起保障请求 | 小区拥塞阻塞或保障条件不满足 | 查DSP SUBCTX的质差未保障原因 |
| 保障建立失败 | 小区GBR资源不足（GBR场景） | 查DSP CELLCTX小区可用容量 |

**GBR场景的UDN交互**（可选步骤）：
- NWDAF携带nrCell_Id和plmnId向UDN申请小区容量信息
- 如果UDC侧开启了 `SET QOSGUARCOND` 中"小区拥塞是否为保障条件"为ENABLE，NWDAF还会请求PRB利用率
- UDN向NWDAF回复小区容量信息后，NWDAF综合判断是否满足GBR资源条件

---

## 3. 配置调测要点

### 3.1 UNC侧（SMF）关键MML命令清单

| 场景 | 命令 | 用途 |
|------|------|------|
| 通用 | `SET LICENSESWITCH` | 开启License（LKV2USBL01LKV3W9SPCC11或LKV2PYCTRL1） |
| 通用 | `SET SMCOMMFUNC: QOSANASW=Support` | 开启QoS质差分析 |
| 通用 | `SET SMFFUNC: EVENTEXPOSURE=Support` | 开启事件订阅与上报（能力开放场景必需） |
| 通用 | `SET PFCPPVTEXT: FEATURE=Qos_Analysis/Qos_Experience, SWITCH=ENABLE` | PFCP私有信元携带 |
| 典型场景 | `ADD UPFBINDSELRULE: INDEX, NFINSTANCENAME, RULENAME` | 智能规则与UPF绑定 |
| 典型场景 | `ADD SELECTRULEINFO: RULENAME, RULEFUNC=QOSANA` | UPF选择规则（功能=QOSANA） |
| 典型场景 | `MOD PNFPROFILE: NFINSTANCEID, CAPACITY` | UPF权重调整 |
| 异厂商UPF | `ADD USERPROFILE: USERPROFILENAME, UPTYPE=UPSELECT` | 用户模板（预定义规则选UPF） |
| 异厂商UPF | `ADD SELECTRULEINFO: RULENAME, RULEFUNC=QOSANA-1&QOSEXP-1, PRIORITY, DELIVERSW=DISABLE` | UPF选择规则（含体验感知+优先级+不下发） |
| 异厂商PCF | `SET IPEN7SESSFUNC: IPEN7SESSFUNC=ENABLE` | 开启智能双N7会话 |
| 异厂商PCF | `ADD TNFGRP / ADD TNFINS / ADD TNFINSIP / ADD TNFBINDGRP` | 智能PCF组/实例/IP/绑定配置 |
| 异厂商PCF | `SET DFTIPEPCFGRP: PRIMIPEPCFGRP` | 主智能PCF组 |
| 异厂商PCF | `ADD RULE: RULENAME, POLICYTYPE=PCC, POLICYNAME, NWDAFEVENTS=QOS_ANALYSIS` | 业务策略规则（可选IPERULEDELYSW=DISABLE） |
| 异厂商PCF | `ADD IPEN7SUFFIX: INTELLISUFFIX, INTELLINAME` | 智能业务后缀匹配 |
| 位置上报 | `SET SMCOMMFUNC: LOCATIONCHSW=Support` | 位置变更订阅开关 |
| 位置上报 | `ADD APN: EXPOSURELOCRPT=ENABLE` | APN能力开放位置上报 |
| 位置上报 | `SET MMFUNC: LOCRPTTIMER=600` | 实时位置上报最小间隔（秒） |
| 位置上报 | `SET LOCATIONREPORT: MSINFOTIMER=600` | 位置更新迟滞控制时长（秒） |
| 位置上报 | `SET POLICYMODE: BY5GSIWKI=ENABLE, BYIWKUEN5GR4G=ENABLE` | 5GS互操作策略接口 |

### 3.2 UPCF侧配置要素

UPCF通过WebUI配置，导航入口：策略管理 > 策略 > [条件组/5G动作组/规则/策略] + 业务管理 > 业务 > [业务/应用业务映射]。

**典型场景核心动作类型**：

| 动作类型 | 用途 | 关键属性 |
|---------|------|---------|
| `UpfSelectRule` | 指示SMF选择智能UPF | upfSelectId=select_ai_upf, reportInd=True |
| `CmdN23EventSubscription` | N23事件订阅（NORMAL=激活/SUSPEND=暂停） | event=QOS_ANALYSIS, appIds=appgroup1, status |
| `QoSData` | QoS参数下发 | qosId, 5qi=4, maxbrUl/Dl, gbrUl/Dl, arp(引用) |
| `Arp` | 优先级与抢占 | priorityLevel=1, preemptCap=NOT_PREEMPT, preemptVuln=NOT_PREEMPTABLE |
| `TrafficControlData` | 门控 | tcId, flowStatus(引用AfSession.FlowStatus) |
| `ChargingData` | 计费控制（可选） | chgId, ratingGroup(引用AfSession), serviceId(引用AfSession) |
| `DynamicPccRuleIMS` | 动态PCC规则 | pccRuleId, refQosData, refTcData, refChgData |

**计费方案选择**：
- 方案一（保障流量独立计费）：需配置ChargingData动作（refChgData引用），要求华为SMF/UPF升级到20.13.2.36版本
- 方案二（保障流量归一化计费）：不配置ChargingData动作

**用户发放**：
```
ADD PSUB: USRIDENTIFIER="IMSI", USRMSISDN, USRSTATE=Normal, USRSTATION=Master, USRSUBNETTYPE=eMBB-SA;
ADD PSRV: USRIDENTIFIER="IMSI", SRVNAME="N23_Service01", SRVUSAGESTATE=Normal;
```

### 3.3 调测检查点

| 检查点 | 命令/消息 | 预期结果 |
|--------|----------|---------|
| PCF发起订阅 | Nnwdaf_EventsSubscription_Subscribe Request | 可观测到请求 |
| NWDAF订阅响应 | Nnwdaf_EventsSubscription_Subscribe Response | 201 Created，event=QOS_ANALYSIS |
| NWDAF→SMF订阅 | Nsmf_EventExposure_SmEventExposureSubscribe Request | 携带appIds和event=QOS_ANA |
| SMF→UPF订阅 | PFCP_Session_Modification_Request | SRR信元携带app-id |
| SMF→NWDAF响应 | 订阅成功响应 | 201 Created，subId+appIds |
| UPF质差上报 | Nupf_EventExposureService_EventNotification Request | subAppQosQuality=QOE_QUALITY1 |
| NWDAF→PCF保障请求 | Npcf_PolicyAuthorizationServiceAPI_PostAppSessions Request | GBR携带带宽值；Non-GBR携带mirBw=0 |
| PCF保障通知 | PostAppSessionEventNotify Request | event=SUCCESSFUL_RESOURCES_ALLOCATION |
| 保障上下文查询 | `DSP SUBCTX: QUERYTYPE=IMSI, IMSI=...` | 保障类型=GBR/Non-GBR，质差状态=TRUE |
| 小区容量查询 | `DSP CELLCTX` | GBR场景已分配GBR增加 |

---

## 4. 与带宽控制的关系

这批文档直接支撑带宽控制场景的核心机制：

### 4.1 智能UPF选择是带宽控制的执行前提
带宽控制策略（QoS加速、GBR保障）最终在UPF执行。智能UPF具备质差分析能力，能采集体验感知数据，这是闭环带宽控制的基础——只有知道用户体验差了，才能触发带宽保障。SMF选择智能UPF的两种模式（PCF指示/预定义规则）决定了保障能力的触发路径。

### 4.2 GBR保障与Non-GBR保障是带宽控制的核心动作
- **GBR保障**：建立专有承载，分配保证带宽（GBR上下行），是"硬带宽控制"——5qi=4的QoS Flow确保带宽下限。
- **Non-GBR保障**：下发QoS策略但不建专载，mirBw=0表示不限制最低速率，是"软带宽控制"——通过ARP优先级提升和QoS参数调整间接保障。
- 两种模式的参数差异（NWDAF→PCF请求中的mirBw值）直接决定保障强度。

### 4.3 N23事件订阅链路是带宽控制的触发通道
N23事件订阅（CmdN23EventSubscription）建立了 PCF→NWDAF→SMF→UPF 的质差分析订阅链路。UPF上报质差后，NWDAF分析判断是否需要保障，向PCF发起保障请求。这条链路是"体验感知→带宽保障"闭环的关键。

### 4.4 全局数据规划确保带宽参数跨网元一致
5QI、GBR、MBR等带宽控制参数在UPCF（动作下发）、UDC（应用配置）、UDG（质差检测）三网元必须统一规划。典型场景的推荐值（如直播5qi=4、GBR上行3000Kbps）直接定义了带宽控制的量化指标。

### 4.5 实时位置上报支撑基于位置的带宽策略
位置变更订阅（SCELL_CH、SAREA_CH）使SMF能感知用户移动，配合`SET POLICYMODE`的互操作开关，支持4G/5G混合网络下的跨制式带宽策略一致性。

---

## 5. 关键术语

| 术语 | 简释 |
|------|------|
| **智能UPF** | 支持质差分析和体验感知数据采集的UPF，是重点业务保障的用户面执行节点 |
| **智能PCF** | 华为UPCF（Unified PCF），在异厂商场景下作为第二个PCF提供智能策略控制 |
| **双N7会话** | SMF同时与异厂商PCF和智能PCF建立两个N7接口会话，分别处理标准策略和智能策略 |
| **N23接口** | PCF（UPCF）与NWDAF之间的接口，用于事件订阅和QoS分析数据交互 |
| **QOS_ANALYSIS** | NWDAF数据分析事件类型，触发质差分析和保障建议计算 |
| **CmdN23EventSubscription** | UPCF侧动作类型，向NWDAF发起N23事件订阅（NORMAL=激活，SUSPEND=暂停） |
| **UpfSelectRule** | UPCF侧动作类型，指示SMF基于规则选择智能UPF |
| **DynamicPccRuleIMS** | UPCF侧动作类型，动态PCC规则（IMS类型），用于AF触发的QoS Flow建立 |
| **appId / subAppId** | 应用大类（如live_streaming）/应用小类（如kuaishou_live），跨网元统一规划 |
| **体验基线KPI** | 应用体验质量的基线值（Kbps），超基线触发质差检测 |
| **大流判断** | 基于流量阈值判断是否为"大流"用户（如UP_BIGFLOW_CHECK），大流用户才触发保障 |
| **5QI** | 5G QoS Identifier，标识QoS特征（4=非GBR保证流量，3=低延迟信号类） |
| **GBR / MBR** | Guaranteed Bit Rate（保证比特速率）/ Maximum Bit Rate（最大比特速率） |
| **AFSessionAuthorization** | UPCF策略触发器，AF请求业务高带宽时触发策略匹配 |
| **IPCAN_EST** | UPCF策略触发器，IP-CAN会话建立时触发 |
| **RAT_TY_CH** | UPCF策略触发器，无线接入技术类型变更时触发（如4G↔5G切换） |
| **NeedN23Subs** | 异厂商PCF场景的条件属性（SmfSession.NeedN23Subs），SMF侧指示需要N23订阅 |
| **IPERULEDELYSW** | 智能规则传递开关，UPF无预定义规则时需DISABLE |
| **LOCRPTTIMER / MSINFOTIMER** | 实时位置上报最小间隔 / 位置更新迟滞控制时长（秒） |

---

## 6. 知识来源

| 序号 | 文件名 | 核心内容 |
|------|--------|---------|
| 1 | 配置SMF基于PCF指示选择智能UPF及下发订阅策略（典型场景）_25346953.md | 典型场景SMF侧智能UPF选择（PCF指示模式）、License、UPF绑定规则、权重计算 |
| 2 | 配置SMF基于预定义规则选择智能UPF及下发订阅策略（异厂商PCF场景）_76485152.md | 异厂商场景SMF侧智能UPF选择（预定义规则模式）、USERPROFILE、QOSANA-1&QOSEXP-1 |
| 3 | 配置SMF选择智能PCF及下发订阅策略（异厂商PCF场景）_06831997.md | 异厂商场景SMF侧智能PCF选择、双N7会话、TNFGRP/TNFINS/TNFBINDGRP、IPEN7SUFFIX |
| 4 | 配置实时位置上报_12027850.md | UNC侧实时位置上报（License、事件订阅、位置变更、4G互操作策略接口） |
| 5 | UPCF侧配置（典型场景）_32788309.md | UPCF典型场景五层配置模型（条件组-动作组-规则-策略-业务）、N23订阅+AF QoS |
| 6 | 配置N23策略（异厂商PCF场景）_70582966.md | UPCF异厂商场景简化N23策略（NeedN23Subs条件、Non-PCC规则） |
| 7 | 典型场景全局业务数据规划_24938201.md | 跨网元数据规划（appId/subAppId/三层协议/基线KPI/大流/5QI/GBR/MBR）、推荐值表 |
| 8 | 异厂商场景全局业务数据规划_08406001.md | 异厂商预定义规则规划（USERPROFILE/RULE/IPEN7SUFFIX名称不可冲突） |
| 9 | 调测应用GBR保障功能_72657226.md | GBR保障端到端调测（9步信令验证+UDN交互+小区容量检查） |
| 10 | 调测应用Non-GBR保障功能_27810673.md | Non-GBR保障端到端调测（mirBw=0、不建专载、无UDN交互） |
