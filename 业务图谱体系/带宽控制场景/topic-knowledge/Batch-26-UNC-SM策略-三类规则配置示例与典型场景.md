# Batch-26: UNC SM策略 - 三类规则配置示例与典型场景

## 1. 概述

本批次文档来自"5G PCC之SM策略解决方案"业务专题（UNC侧），覆盖SM策略在5G场景下的三类规则配置方式及其典型业务应用，具体包含以下7个子主题：

- **动态规则配置示例**：以FUP（Fair Usage Policy）场景为例，展示PCF侧全动态规则从配额到条件组、动作组、规则、策略、业务的完整配置链路，以及SMF侧的PCC功能开关和License配置。
- **预定义规则/规则组配置**：分为业务配置逻辑、概述、配置示例三个维度。预定义规则表示由PCF下发规则名、SMF/UPF定义实际策略内容，是动态PCC策略的第二种实现方式。
- **本地PCC策略配置**：分为业务配置逻辑、概述、配置示例三个维度。本地PCC表示策略完全由SMF/UPF配置生成，不经过PCF，作为PCF不可用时的兜底方案。
- **典型业务场景**：将SM策略业务场景划分为"通用业务"和"定向业务"两大类，并给出各类场景对应的规则配置路径。
- **5GC网元调测版本配套说明**：明确E2E方案设计基于UNC 20.6.2 / UDG 20.6.2 / UPCF 20.6.2版本进行配置与调测。
- **业务重定向方案E2E调测（动态规则场景）**：以业务重定向场景为例，展示动态规则从用户上线到配额耗尽的完整信令调测方法，涵盖PCF/SMF/UPF三侧的信令验证。

---

## 2. 核心知识点

### 2.1 SM策略的三种规则配置方式

SM策略有三种规则配置方式，它们的本质区别在于策略内容定义的位置和下发路径：

| 维度 | 动态规则 | 预定义规则/规则组 | 本地PCC策略 |
|------|----------|-------------------|-------------|
| **策略内容定义方** | PCF定义完整策略内容 | PCF下发规则名，SMF/UPF定义实际QoS/流描述等 | SMF/UPF完全定义策略 |
| **策略下发路径** | PCF -> SMF -> UPF | PCF（下发规则名）-> SMF/UPF（匹配预定义内容）| SMF -> UPF（不经PCF）|
| **涉及网元** | PCF + SMF + UPF | PCF + SMF + UPF | SMF + UPF（不涉及PCF）|
| **灵活度** | 最高（可基于用户等级、配额状态、位置等动态调整）| 中等（规则名协商一致，内容在SMF/UPF侧固定）| 最低（仅基于APN激活，提供固定QoS）|
| **典型用途** | FUP带宽分档控制、重定向、动态QoS | 定向业务识别、带宽控制 | PCF不可用时的兜底策略、基本QoS保障 |
| **配额支持** | 支持（PCF侧配额累积和条件判断）| 支持（PCF侧配额累积，SMF/UPF侧QoS执行）| 不支持（无法定义配额相关属性）|

### 2.2 动态规则配置示例：FUP三档带宽控制

动态规则配置示例以典型FUP场景展示完整的PCF侧业务配置流程：

- **需求场景**：5G用户月配额200GB，按配额消耗分三档控制带宽：
  - 消耗 <60%：上行100 Mbps / 下行200 Mbps
  - 消耗 >=60% 且 <100%：上行60 Mbps / 下行80 Mbps
  - 消耗 >=100%：上行10 Mbps / 下行20 Mbps
- **配置链路**（PCF侧，严格有序）：
  1. **配额**（Quota）：定义流量配额200GB、会话级、监控键值101、月复位、Level1阈值60%
  2. **条件组**（ConditionGroup）：3个条件组，分别匹配QuotaStatus为Normal/Level1/Exhaust
  3. **5G动作组**（ActionGroup）：11个动作组，包含FlowDescription、FlowInformation、Arp、UsageMonitoringData、TrafficControlData、3组QoSData（对应三档带宽）、3组DynamicPccRule
  4. **规则**（Rule）：3条5G Smf Pcc Rule，类型为Change Rule，分别关联条件组和动作组
  5. **策略**（Policy）：N7 Policy类型，触发器IPCAN_EST + US_RE
  6. **业务**（Service）：BASIC_SERVICE类型，激活方式PCEF，QoS模式替换
- **SMF侧配置**（仅功能开关）：
  - 开启License：`SET LICENSESWITCH:LICITEM="LKV2FUPSAT01",SWITCH=ENABLE;`
  - 开启动态PCC功能：`SET PCCFUNC:HOMEPCCSWITCH=ENABLE;`
- **关键特征**：QoS参数（5QI、ARP、maxbrUl、maxbrDl）由PCF通过DynamicPccRule动作完整下发，SMF/UPF侧无需配置具体QoS内容。

### 2.3 预定义规则/规则组配置

预定义规则的核心特征是**PCF和SMF/UPF分工协作**：PCF负责配额管理和条件判断，SMF/UPF负责实际的QoS和流信息定义。

- **概述要点**：
  - 预定义规则名在PCF/SMF/UPF三网元上须**协商一致**
  - PCF仅下发预定义规则名，实际策略内容（5QI、ARP、流描述、MBR等）由SMF/UPF配置提供
  - 涉及网元：UPF + SMF + PCF（UE/NR/RAN/UDM/Provisioning System不涉及）

- **配置逻辑**：
  - PCF侧：配额 -> 条件组 -> 5G动作组（PredefinedPccRule类型）-> 规则 -> 策略 -> 业务
  - SMF侧：License -> PCC开关 -> URR（监控键值绑定）-> URRGROUP -> QOSPROP -> PCCPOLICYGRP -> RULE（预定义规则名）
  - UPF侧：FILTER -> FLOWFILTER -> FLTBINDFLOWF -> URR -> URRGROUP -> QOSPROP -> PCCPOLICYGRP -> RULE（预定义规则名+流过滤器绑定）

- **配置示例**（FUP两档带宽控制）：
  - 需求：配额10GB，未耗尽时上下行各100 Mbit/s，耗尽后上下行各1 Mbit/s
  - PCF侧动作组类型为**PredefinedPccRule**（而非DynamicPccRule），pccRuleId值为"Predefined1"/"Predefined2"
  - SMF侧需配置两套QoS参数和两条预定义规则：
    ```
    // 配额耗尽前
    ADD QOSPROP:QOSPROPNAME="qosprop_5qi5_arp1_100",MBRUPLKVALUE=100000,MBRDNLKVALUE=100000,...;
    ADD RULE:RULENAME="Predefined1",POLICYTYPE=PCC,PRIORITY=20,POLICYNAME="pccfuppolicy_nomal";
    // 配额耗尽后
    ADD QOSPROP:QOSPROPNAME="qosprop_5qi5_arp1_1",MBRUPLKVALUE=1000,MBRDNLKVALUE=1000,...;
    ADD RULE:RULENAME="Predefined2",POLICYTYPE=PCC,PRIORITY=30,POLICYNAME="pccfuppolicy_exha";
    ```
  - UPF侧需配置流过滤器并绑定到预定义规则：
    ```
    ADD RULE:RULENAME="Predefined1",POLICYTYPE=PCC,FILTERINGMODE=FLOWFILTER,
    FLOWFILTERNAME="flowfliter_service_normal",PRIORITY=10,POLICYNAME="pccfuppolicy_nomal";
    ```

### 2.4 本地PCC策略配置

本地PCC策略的核心特征是**完全不经过PCF**，策略内容由SMF/UPF自行配置，适用于PCF不可用或链路异常场景。

- **概述要点**：
  - 策略完全由SMF/UPF配置生成，不经PCF网元
  - 涉及网元：UPF + SMF（PCF不涉及）
  - 无法定义配额相关属性（配额大小、复位时间等）
  - 通常作为PCF下发规则失效时的**兜底规则**，保证业务连续

- **配置逻辑**：SMF侧 -> PCC开关（关闭）-> PCC模板 -> APN级PCC开关 -> QoS属性 -> PCC策略组 -> 本地规则 -> UserProfile -> RuleBinding -> UserProfileGroup -> APN绑定

- **配置示例**（APN级固定带宽控制）：
  - 需求：APN1上线用户获得上下行各10 Mbit/s带宽，无配额控制
  - SMF侧配置关键差异：**关闭PCC功能**（与动态/预定义规则相反）
    ```
    SET PCCFUNC:HOMEPCCSWITCH=DISABLE,ROAMPCCSWITCH=DISABLE,VISITPCCSWITCH=DISABLE;
    ```
  - SMF侧通过UserProfile体系绑定规则到APN：
    ```
    ADD USERPROFILE:USERPROFILENAME="up_test",UPTYPE=PCC;
    ADD RULEBINDING:USERPROFILENAME="up_test",RULENAME="rule_test";
    ADD USRPROFGROUP:USERPROFGNAME="upg_test";
    ADD UPBINDUPG:USERPROFGNAME="upg_test",UPBINDTYPE=DEFAULT,USERPROFILENAME="up_test";
    ADD APNUSRPROFG:APN="apn1",USERPROFGNAME="upg_test";
    ```
  - UPF侧配置与预定义规则类似，但需额外配置UserProfile绑定关系

### 2.5 典型业务场景分类

SM策略业务场景按是否需要业务识别分为两大类：

| 场景分类 | 特点 | PCC开关打开时 | PCC开关关闭时 |
|----------|------|---------------|---------------|
| **通用业务** | 不涉及具体业务识别（如固定月套餐） | 动态规则 或 预定义规则/规则组 | 本地PCC策略 |
| **定向业务** | 需识别具体业务（如特定视频APP流量包）| 预定义规则/规则组（SMF/UPF具备业务识别能力，PCF不具备）| 本地PCC策略 |

关键结论：
- 定向业务场景下，因PCF不具备业务识别能力，**即使PCC开关打开也不能使用纯动态规则**，必须使用预定义规则/规则组
- 通用业务场景下，PCC开关打开时可自由选择动态规则或预定义规则
- 两种场景在PCC开关关闭时都只能使用本地PCC策略

### 2.6 5GC网元版本配套

E2E方案设计基于以下版本进行配置与调测：

| 产品/网元名称 | 版本号 |
|---------------|--------|
| UNC（SMF）| 20.6.2 |
| UDG（UPF）| 20.6.2 |
| UPCF（PCF）| 20.6.2 |

三个网元版本号一致，表明E2E方案要求三网元配套使用同版本。

### 2.7 业务重定向方案E2E信令调测

业务重定向方案（预定义+动态）的动态规则场景调测展示了完整的信令交互验证方法：

- **调测目标**：验证策略下发与执行是否符合3GPP协议要求及华为UPCF/UNC/UDG策略逻辑
- **验证维度**：
  1. 策略内容验证完备性：UPCF签约业务中定义的动作组须全量覆盖测试
  2. 消息流程正确性：策略下发、执行、更新、事件上报符合协议
  3. 消息内容正确性：策略下发消息携带内容与策略逻辑定义一致

- **配额未耗尽时的信令流程**：
  1. 用户发起PDU会话建立 -> SMF向PCF发送Npcf_SMPolicyControl_Create Request
  2. PCF查询用户签约"Redirection_Service"，匹配Normal状态，下发AG_Normal动态规则
  3. 规则内容包含：pccRuleId=AG_Normal、flowDescription=permit out ip from any to any、5qi=9、maxbrUl/Dl=100000000 bps
  4. SMF通过N4接口PFCP Session Establishment Request将策略下发给UPF

- **配额耗尽后的信令流程**：
  1. UPF检测配额耗尽，通过PFCP Session Report Request向SMF上报US_RE事件
  2. SMF通过Npcf_SMPolicyControl_Update Request向PCF上报配额消耗（accuUsageReports携带volUsage/volUsageDownlink/volUsageUplink）
  3. PCF决策后通过Npcf_SMPolicyControl_Update Response删除旧规则AG_Normal（设为null）、安装新规则AG_Exhaust
  4. 规则切换通过pccRules中的null/对象配对实现

---

## 3. 配置调测要点

### 3.1 动态规则配置完整流程

**PCF侧（UPCF Web UI）配置顺序**（带配额场景）：

```
配额(Quota) -> 条件组(ConditionGroup) -> 5G动作组(ActionGroup) -> 规则(Rule) -> 策略(Policy) -> 业务(Service) -> 开户(ADD PSUB) -> 业务发放(ADD PSRV)
```

**5G动作组类型及引用关系**（动态规则场景）：

| 动作组类型 | 用途 | 是否可共用 |
|------------|------|------------|
| FlowDescription | 定义流描述（action/direction/protocol/sourceIP/destinationIP）| 可共用 |
| FlowInformation | 定义流信息（引用FlowDescription）| 可共用 |
| Arp | 定义ARP优先级/抢占能力/抢占脆弱性 | 可共用 |
| UsageMonitoringData | 定义使用量监控（umId/volumeThreshold）| 可共用 |
| TrafficControlData | 定义门限控制（flowStatus=ENABLED/DISABLED）| 可共用 |
| QoSData | 定义QoS参数（5qi/arp/maxbrUl/maxbrDl）| **不可共用**（不同档位带宽不同）|
| DynamicPccRule | 组装以上子动作，引用FlowInformation/QoSData/TrafficControlData/UsageMonitoringData | 每个档位一条 |

**SMF侧配置**（仅功能开关）：

```
SET LICENSESWITCH:LICITEM="LKV2FUPSAT01",SWITCH=ENABLE;
SET PCCFUNC:HOMEPCCSWITCH=ENABLE;
```

### 3.2 预定义规则配置完整流程

**三网元配置映射关系**：

| PCF侧配置 | SMF侧配置 | UPF侧配置 |
|-----------|-----------|-----------|
| 配额（监控键值99）| URR（MONITORINGKEY=99）| URR（MONITORINGKEY对应）|
| 条件组（Normal/Exhaust）| - | - |
| 5G动作组（PredefinedPccRule，pccRuleId=Predefined1/2）| QOSPROP（MBR/QoS参数）| QOSPROP（MBR/QoS参数）|
| 规则（关联条件组+动作组）| PCCPOLICYGRP（关联URRGROUP+QOSPROP）| PCCPOLICYGRP（关联URRGROUP+QOSPROP）|
| 策略（N7 Policy）| RULE（RULENAME=Predefined1/2）| RULE（RULENAME=Predefined1/2+FLOWFILTER）|

**SMF侧关键命令序列**：

```
// 1. License和PCC开关
SET LICENSESWITCH:LICITEM="LKV2FUPSAT01",SWITCH=ENABLE;
SET PCCFUNC:HOMEPCCSWITCH=ENABLE;

// 2. URR配置（MK URR + QoS URR）
ADD URR:URRNAME="urr_01",URRID=1,USAGERPTMODE=MONITORINGKEY,MONITORINGKEY="99";
ADD URR:URRNAME="urr_QoS2",URRID=2,USAGERPTMODE=QOS;
ADD URR:URRNAME="urr_QoS3",URRID=3,USAGERPTMODE=QOS;

// 3. URRGROUP（上下行流量累计）
ADD URRGROUP:URRGROUPNAME="urrg_fup_service",UPURRNAME1="urr_01",DOWNURRNAME1="urr_01";

// 4. QoS属性（两档带宽）
ADD QOSPROP:QOSPROPNAME="qosprop_5qi5_arp1_100",MBRUPLKVALUE=100000,MBRDNLKVALUE=100000,...;
ADD QOSPROP:QOSPROPNAME="qosprop_5qi5_arp1_1",MBRUPLKVALUE=1000,MBRDNLKVALUE=1000,...;

// 5. PCC策略组（两档）
ADD PCCPOLICYGRP:PCCPOLICYGRPNM="pccfuppolicy_nomal",URRGROUPNAME="urrg_fup_service",QOSPROPNAME="qosprop_5qi5_arp1_100";
ADD PCCPOLICYGRP:PCCPOLICYGRPNM="pccfuppolicy_exha",URRGROUPNAME="urrg_fup_service",QOSPROPNAME="qosprop_5qi5_arp1_1";

// 6. 预定义规则（名称须与PCF协商一致）
ADD RULE:RULENAME="Predefined1",POLICYTYPE=PCC,PRIORITY=20,POLICYNAME="pccfuppolicy_nomal";
ADD RULE:RULENAME="Predefined2",POLICYTYPE=PCC,PRIORITY=30,POLICYNAME="pccfuppolicy_exha";
```

**UPF侧关键命令序列**：

```
// 1. License
SET LICENSESWITCH:LICITEM="LKV3G5PCCB01",SWITCH=ENABLE;

// 2. 流过滤器（两档各一组）
ADD FILTER:FILTERNAME="f_fup_service_normal",L34PROTTYPE=STRING,L34PROTOCOL=ANY;
ADD FLOWFILTER:FLOWFILTERNAME="flowfliter_service_normal";
ADD FLTBINDFLOWF:FLOWFILTERNAME="flowfliter_service_normal",FILTERNAME="f_fup_service_normal";
SET REFRESHSRV:REFRESHTYPE=ALL;

// 3. URR（与SMF侧严格一致）
ADD URR:URRNAME="urr_01",URRID=1,USAGERPTMODE=MONITORINGKEY;
ADD URRGROUP:URRGROUPNAME="urrg_fup_service",UPURRNAME1="urr_01",DOWNURRNAME1="urr_01";

// 4. QoS属性和PCC策略组（与SMF侧严格一致）
ADD QOSPROP:QOSPROPNAME="qosprop_5qi5_arp1_100",...;
ADD PCCPOLICYGRP:PCCPOLICYGRPNM="pccfuppolicy_nomal",URRGROUPNAME="urrg_fup_service",QOSPROPNAME="qosprop_5qi5_arp1_100",...;

// 5. 规则（绑定流过滤器+PCC策略组）
ADD RULE:RULENAME="Predefined1",POLICYTYPE=PCC,FILTERINGMODE=FLOWFILTER,FLOWFILTERNAME="flowfliter_service_normal",PRIORITY=10,POLICYNAME="pccfuppolicy_nomal";
```

### 3.3 本地PCC策略配置完整流程

**SMF侧配置顺序**：

```
License -> 全局PCC开关(关闭) -> PCC模板 -> APN级PCC开关 -> QoS属性 -> PCC策略组 -> 本地规则 -> UserProfile -> RuleBinding -> UserProfileGroup -> UP绑定到UPG -> UPG绑定到APN
```

**SMF侧关键命令**：

```
// License（注意：本地PCC使用PCC基本功能License，不同于FUP License）
SET LICENSESWITCH:LICITEM="LKV3W9SPCC11",SWITCH=ENABLE;

// 关闭PCC功能（与动态/预定义规则相反）
SET PCCFUNC:HOMEPCCSWITCH=DISABLE,ROAMPCCSWITCH=DISABLE,VISITPCCSWITCH=DISABLE;

// PCC模板（定义策略获取失败时的行为）
ADD PCCTEMPLATE:PCCTEMPNAME="pcctemplate",INITIALFAILACT=FORBIDDEN,UPDATEFAILACT=INHERIT;

// QoS属性（固定带宽）
ADD QOSPROP:QOSPROPNAME="qos_property1",MBRUPLKVALUE=1000,MBRDNLKVALUE=1000,QOSTYPE=QOS_BEARER_PARA,QCIVALUE=5,ARPVALUE=1;

// PCC策略组和本地规则
ADD PCCPOLICYGRP:PCCPOLICYGRPNM="pccpolicy_group",QOSPROPNAME="qos_property1";
ADD RULE:RULENAME="rule_test",POLICYTYPE=PCC,POLICYNAME="pccpolicy_group";

// UserProfile绑定体系
ADD USERPROFILE:USERPROFILENAME="up_test",UPTYPE=PCC;
ADD RULEBINDING:USERPROFILENAME="up_test",RULENAME="rule_test";
ADD USRPROFGROUP:USERPROFGNAME="upg_test";
ADD UPBINDUPG:USERPROFGNAME="upg_test",UPBINDTYPE=DEFAULT,USERPROFILENAME="up_test";
ADD APNUSRPROFG:APN="apn1",USERPROFGNAME="upg_test";
```

**UPF侧配置**：与预定义规则类似（FILTER/FLOWFILTER/QOSPROP/PCCPOLICYGRP/RULE），但额外需配置UserProfile绑定。

### 3.4 版本配套要求

| 网元 | 版本 | License项 |
|------|------|-----------|
| UNC（SMF）| 20.6.2 | LKV2FUPSAT01（FUP）/ LKV3W9SPCC11（PCC基本功能）|
| UDG（UPF）| 20.6.2 | LKV3G5PCCB01（基本PCC功能）|
| UPCF（PCF）| 20.6.2 | - |

### 3.5 信令调测关键步骤

1. **建立消息跟踪**：在PCF/SMF/UPF三网元建立用户消息跟踪任务
2. **验证签约**：执行`LST PSRV`确认用户签约业务名称正确
3. **初始上线验证**：观察Npcf_SMPolicyControl_Create Request/Response消息，验证规则下发内容
4. **N4接口验证**：观察PFCP Session Establishment Request消息，验证SMF到UPF的策略传递
5. **配额耗尽验证**：观察PFCP Session Report Request（US_RE事件上报）和Npcf_SMPolicyControl_Update Request/Response，验证规则切换（旧规则null + 新规则install）

---

## 4. 与带宽控制的关系

### 4.1 三种规则配置是带宽控制策略下发的不同方式

带宽控制（通过QoS参数maxbrUl/maxbrDl实现）是SM策略的核心能力之一。三种规则配置方式对应不同的带宽控制下发路径：

- **动态规则**：带宽参数由PCF在DynamicPccRule -> QoSData中完整定义，支持根据配额状态动态切换带宽档位（如FUP三档控制），**灵活度最高**，是带宽控制场景的首选方案。
- **预定义规则**：带宽参数由SMF/UPF在QOSPROP中定义，PCF仅触发规则名切换，适用于需要业务识别的定向带宽控制场景（如特定APP限速）。
- **本地PCC策略**：带宽参数固定在SMF/UPF的QOSPROP中，无法根据配额或业务状态动态调整，仅提供**基础带宽保障**，作为兜底方案。

### 4.2 典型业务场景中的带宽控制

- **通用业务FUP带宽分档**：使用动态规则，PCF根据配额消耗（Normal/Level1/Exhaust）下发不同QoSData，实现三档甚至多档带宽切换。
- **定向业务带宽控制**：使用预定义规则，SMF/UPF识别特定业务流后应用对应的预定义QoS策略，实现定向限速。
- **兜底带宽保障**：使用本地PCC策略，为特定APN用户提供固定的上下行带宽（如10 Mbit/s），保证PCF不可用时业务连续。

### 4.3 带宽控制的关键参数

无论哪种规则配置方式，带宽控制最终通过以下参数实现：

| 参数 | 说明 | 配置位置 |
|------|------|----------|
| maxbrUl（MBRUPLKVALUE）| 上行最大比特率 | PCF: QoSData / SMF+UPF: QOSPROP |
| maxbrDl（MBRDNLKVALUE）| 下行最大比特率 | PCF: QoSData / SMF+UPF: QOSPROP |
| 5qi（FQI/QCIVALUE）| 5G QoS标识 | PCF: QoSData / SMF+UPF: QOSPROP |
| ARP（ARPVALUE）| 分配保留优先级 | PCF: QoSData / SMF+UPF: QOSPROP |

### 4.4 配额驱动的带宽切换机制

动态规则和预定义规则场景中，带宽切换由配额状态驱动：

1. UPCF定义配额及阈值（如Level1=60%）
2. UPF/SMF累计用户流量，当达到阈值时上报US_RE事件
3. PCF根据QuotaStatus（Normal/Level1/Exhaust）匹配条件组
4. PCF下发对应规则（动态规则直接含QoS参数，预定义规则下发规则名由SMF/UPF匹配）
5. SMF通过N4接口更新UPF的PDR/QER/URR，实现带宽切换

---

## 5. 关键术语

| 术语 | 全称/含义 |
|------|-----------|
| **SM策略** | Session Management Policy，5G会话管理策略，控制PDU会话的QoS、计费、带宽等 |
| **PCC** | Policy and Charging Control，策略与计费控制 |
| **PCF** | Policy Control Function，策略控制功能网元 |
| **SMF** | Session Management Function，会话管理功能网元（华为产品名UNC）|
| **UPF** | User Plane Function，用户面功能网元（华为产品名UDG）|
| **UPCF** | Unified Policy Control Function，华为统一策略控制功能（即PCF产品）|
| **FUP** | Fair Usage Policy，公平使用策略，基于配额的流量管理机制 |
| **动态规则（DynamicPccRule）** | PCF定义完整策略内容并动态下发的PCC规则 |
| **预定义规则（PredefinedPccRule）** | PCF下发规则名、SMF/UPF定义实际内容的PCC规则 |
| **本地PCC策略** | 完全由SMF/UPF配置的策略，不经PCF |
| **URR** | Usage Reporting Rule，使用量上报规则 |
| **URRGROUP** | URR组，配置上下行流量累计原则 |
| **QOSPROP** | QoS属性，包含MBR/GBR/5QI/ARP等参数 |
| **PCCPOLICYGRP** | PCC策略组，关联URRGROUP和QoS属性 |
| **QuotaStatus** | 配额状态，取值Normal（未达阈值）/Level1（达到阈值未耗尽）/Exhaust（耗尽）|
| **N7接口** | PCF与SMF之间的策略控制接口（Npcf_SMPolicyControl）|
| **N4接口** | SMF与UPF之间的接口（PFCP协议）|
| **PFCP** | Packet Forwarding Control Protocol，N4接口信令协议 |
| **US_RE** | Usage Report Event，使用量上报事件触发器 |
| **IPCAN_EST** | IP-CAN Session Establishment，IP-CAN会话建立触发器 |
| **UserProfile** | 用户模板，用于绑定本地PCC规则到APN |
| **APN/DNN** | Access Point Name / Data Network Name，接入点名称/数据网络名称 |
| **5QI** | 5G QoS Identifier，5G QoS标识符 |
| **ARP** | Allocation and Retention Priority，分配保留优先级 |
| **MBR** | Maximum Bit Rate，最大比特率 |
| **ADD PSUB** | 增加签约用户（UPCF开户命令）|
| **ADD PSRV** | 签约业务（UPCF业务发放命令）|

---

## 6. 知识来源

| 序号 | 文件名 | 内容主题 |
|------|--------|----------|
| 1 | 配置示例_18009858.md | 动态规则配置示例（FUP三档带宽控制）|
| 2 | 业务配置逻辑_65059427.md | 预定义规则/规则组配置逻辑 |
| 3 | 概述_18099670.md | 预定义规则/规则组概述 |
| 4 | 配置示例_18259562.md | 预定义规则配置示例（FUP两档带宽控制）|
| 5 | 业务配置逻辑_66336491.md | 本地PCC策略配置逻辑 |
| 6 | 概述_66416527.md | 本地PCC策略概述 |
| 7 | 配置示例_19416800.md | 本地PCC策略配置示例（APN级固定带宽）|
| 8 | 典型业务场景_59651633.md | SM策略典型业务场景分类 |
| 9 | 5GC网元调测版本配套说明_30866774.md | 5GC网元版本配套关系 |
| 10 | 信令调测方法_08571768.md | 业务重定向方案动态规则场景E2E信令调测 |

---

> **批次信息**：Batch-26 | 主题：UNC SM策略三类规则配置示例与典型场景 | 来源：5G PCC之SM策略解决方案业务专题 | 文件数：10 | 产出日期：2026-06-09
