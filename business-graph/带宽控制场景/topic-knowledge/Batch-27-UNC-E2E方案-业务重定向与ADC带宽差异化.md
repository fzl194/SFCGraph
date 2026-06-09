# Batch-27: UNC E2E方案 -- 业务重定向与ADC带宽差异化控制

> 来源：UNC 20.15.2 产品文档 - 5G PCC之SM策略解决方案/典型业务场景E2E方案设计

---

## 1. 概述

本批次覆盖10个产品文档，来自UNC产品文档中"5G PCC之SM策略解决方案"专题下的两个典型E2E方案：

**方案一：业务重定向方案（预定义+动态规则）**
完整覆盖从需求描述到E2E调测的全链条，包括：
- 需求描述与整体方案设计
- PCF侧业务配置（动态规则版 + 预定义规则版）
- SMF侧业务配置（预定义规则版）
- UPF侧业务配置（预定义规则版）
- E2E业务调测（动态规则快速调测 + 预定义规则信令调测 + 预定义规则快速调测）

**方案二：基于业务类别的带宽差异化控制方案（ADC）**
- ADC方案的E2E信令调测方法

这两个方案均属于带宽控制场景的典型E2E实现。业务重定向方案展示的是"配额耗尽触发带宽降速+重定向"的FUP（Fair Usage Policy）类控制；ADC方案展示的是"基于应用检测实现不同业务不同带宽"的差异化控制，是带宽控制子场景的核心E2E方案。

---

## 2. 核心知识点

### 2.1 业务重定向方案的需求与整体设计

**需求场景**：当5G用户配额（如月流量20GB）耗尽时，运营商需要同时执行三个动作：
1. 将上下行带宽从100 Mbit/s降至1 Kbit/s
2. 向用户发送短信通知
3. 将用户重定向到套餐充值页面（http://www.example.com）

**整体设计方法论**（五步法）：

| 步骤 | 名称 | 说明 |
|------|------|------|
| 1 | 抽取 | 按"在XX条件下，实现XX控制"的逻辑抽取业务条件 |
| 2 | 合并 | 将"动作"相同或"条件组"相同的逻辑语句合并 |
| 3 | 排查 | 排查条件完备性，确认是否有边缘场景未覆盖 |
| 4 | 规则类型判断 | 选择动态规则或预定义规则 |
| 5 | 触发器选择 | 配置触发器配合规则进行策略匹配 |

**条件完备性分析**：配额未耗尽 + 配额耗尽 = 用户全部配额状态，场景齐全。

**触发器选择**：
- `IPCAN_EST`：用户从N7接口上线时触发PCF做策略计算
- `US_RE`：用户消耗配额时PCF根据配额状态做策略计算

**两种实现路径**：
- **动态规则**：PCF通过Npcf接口直接下发完整PCC规则内容（含QoS参数、重定向信息等），SMF/UPF无需额外配置
- **预定义规则**：PCF仅下发规则标识名，具体规则内容在SMF/UPF侧预定义，三侧需协同配置

### 2.2 PCF侧业务配置（动态规则版）

动态规则方案下，PCF侧需配置11步：配额 > 通知模板 > 消息通知 > 条件组 > 5G动作组 > 规则 > 策略 > 业务 > 开户 > 业务发放。

**核心配置对象**：

| 对象 | 名称 | 关键参数 |
|------|------|----------|
| 配额 | Quota_20GB | 流量配额，20GB(20,971,520 KB)，监控键值101，月度复位 |
| 条件组 | CG_Normal / CG_Exhaust | Quota.QuotaStatus = Normal / Exhaust |
| QoS动作组 | AG_Qos_Normal / AG_Qos_Exhaust | maxbrUL/DL: 100Mbps/1Kbps，5qi/arp取上线请求值 |
| 重定向动作组 | AG_Redinfo | RedirectEnabled=True, AddressType=URL, ServerAddress=http://www.example.com |
| 流量控制动作组 | AG_TraCtrl_Exhaust | flowStatus=ENABLED + 关联重定向 |
| 流信息动作组 | AG_FlowInfo + AG_FlowDesc | permit out ip from any to any, BIDIRECTIONAL |
| 使用量监控 | AG_usg | umId=101（与配额监控键值一致） |
| DynamicPccRule | AG_Normal / AG_Exhaust | 关联QoS+流量控制+流信息+使用量监控 |
| 规则 | Rule_Normal / Rule_Exhaust | 分别关联Normal和Exhaust条件组及动作组 |
| 策略 | Policy_Redirection | N7 Policy，触发器IPCAN_EST + US_RE |

**关键设计要点**：
- Rule_Exhaust需挂载消息通知（配额耗尽时发短信）
- 消息通知的"唯一键"为Quota.QuotaStatus，用于抑制重复发送
- 5QI和ARP取值类型为Object Attribute（SmfSession.SubsDefQos5qi等），表示PCF直接取用户上线请求值

### 2.3 PCF侧业务配置（预定义规则版）

预定义规则方案下，PCF侧的5G动作组类型从`DynamicPccRule`变为`PredefinedPccRule`，不再包含QoSData、TrafficControlData、RedirectInformation等具体内容，仅下发规则标识名。

**与动态规则版的关键差异**：

| 对比维度 | 动态规则版 | 预定义规则版 |
|----------|------------|------------|
| 动作组类型 | DynamicPccRule | PredefinedPccRule |
| 动作组内容 | 含QoS+流信息+流量控制+重定向 | 仅含pccRuleId（规则名） |
| QoS参数 | PCF侧定义（maxbrUL/DL等） | SMF/UPF侧定义（MBRUPLKVALUE等） |
| 重定向信息 | PCF侧定义RedirectInformation | UPF侧通过ADD REDIRECT定义 |
| SMF/UPF配置 | 无需配置 | 必须三侧协同配置 |
| pccRuleId值 | AG_Normal / AG_Exhaust | Rule_Normal / up_Exhaust（需与SMF/UPF协商一致） |

**共同点**：配额、通知模板、消息通知、条件组的配置完全相同。

### 2.4 SMF侧业务配置（预定义规则版）

SMF侧配置流程：License开关 > PCC功能开关 > (APN PCC开关) > QoS URR + MK URR > URR Group > QoS属性 > PCC策略组 > 预定义规则 > (用户模板 + 规则绑定)。

**关键MML命令序列**：

```
-- 1. 开启License与PCC功能
SET LICENSESWITCH: LICITEM="LKV2FUPSAT01", SWITCH=ENABLE;
SET PCCFUNC: HOMEPCCSWITCH=ENABLE;

-- 2. 配置QoS URR与MK URR
ADD URR: URRNAME="urr_QoS2", URRID=2, USAGERPTMODE=QOS;
ADD URR: URRNAME="urr_QoS3", URRID=3, USAGERPTMODE=QOS;
ADD URR: URRNAME="urr_MK", URRID=32, USAGERPTMODE=MONITORINGKEY, MONITORINGKEY="101";

-- 3. 配置URR Group（关联MK URR）
ADD URRGROUP: URRGROUPNAME="urrg_qos_service", UPURRNAME1="urr_MK", DOWNURRNAME1="urr_MK";

-- 4. 配置QoS属性（配额未耗尽100M）
ADD QOSPROP: QOSPROPNAME="qosprop_5qi5_arp2_100M", MBRUPLKVALUE=100000, MBRDNLKVALUE=100000, QOSTYPE=QOS_FLOW_PARA, ARPVALUE=2, FQI=5, QOSURRNAME="urr_QoS2";

-- 4b. 配置QoS属性（配额耗尽1K）
ADD QOSPROP: QOSPROPNAME="qosprop_5qi5_arp2_1K", MBRUPLKVALUE=1, MBRDNLKVALUE=1, QOSTYPE=QOS_FLOW_PARA, ARPVALUE=2, FQI=5, QOSURRNAME="urr_QoS3";

-- 5. 配置PCC策略组
ADD PCCPOLICYGRP: PCCPOLICYGRPNM="pccfuppolicy_100M", URRGROUPNAME="urrg_qos_service", QOSPROPNAME="qosprop_5qi5_arp2_100M";
ADD PCCPOLICYGRP: PCCPOLICYGRPNM="pccfuppolicy_1K", URRGROUPNAME="urrg_qos_service", QOSPROPNAME="qosprop_5qi5_arp2_1K";
ADD PCCPOLICYGRP: PCCPOLICYGRPNM="pccfuppolicy_Redir";

-- 6. 配置预定义规则
ADD RULE: RULENAME="Rule_Normal", POLICYTYPE=PCC, PRIORITY=10, POLICYNAME="pccfuppolicy_100M";
ADD RULE: RULENAME="Rule_Exhaust", POLICYTYPE=PCC, PRIORITY=20, POLICYNAME="pccfuppolicy_1K";
ADD RULE: RULENAME="Rule_Redirection", POLICYTYPE=PCC, PRIORITY=20, POLICYNAME="pccfuppolicy_Redir";

-- 7. 配置预定义规则组（配额耗尽场景）
ADD USERPROFILE: USERPROFILENAME="up_Exhaust", UPTYPE=PCC;
ADD RULEBINDING: USERPROFILENAME="up_Exhaust", RULENAME="Rule_Exhaust";
ADD RULEBINDING: USERPROFILENAME="up_Exhaust", RULENAME="Rule_Redirection";
```

**SMF与PCF映射关系**：
- PCF下发预定义规则名"Rule_Normal" -> SMF识别为预定义规则（单规则）
- PCF下发预定义规则组名"up_Exhaust" -> SMF识别为预定义规则组（含Rule_Exhaust + Rule_Redirection）

### 2.5 UPF侧业务配置（预定义规则版）

UPF侧配置最为复杂，包含三大流程：流过滤器配置、PCC策略配置、规则与规则组配置。

**关键配置对象**：

**a) 流过滤器（3/4层）**：
```
-- 配额未耗尽场景
ADD FILTER: FILTERNAME="f_fup_service_100M", L34PROTTYPE=STRING, L34PROTOCOL=ANY;
ADD FLOWFILTER: FLOWFILTERNAME="flowfliter_service_100M";
ADD FLTBINDFLOWF: FLOWFILTERNAME="flowfliter_service_100M", FILTERNAME="f_fup_service_100M";

-- 配额耗尽场景
ADD FILTER: FILTERNAME="f_fup_service_1K", L34PROTTYPE=STRING, L34PROTOCOL=ANY;
ADD FLOWFILTER: FLOWFILTERNAME="flowfliter_service_1K";
ADD FLTBINDFLOWF: FLOWFILTERNAME="flowfliter_service_1K", FILTERNAME="f_fup_service_1K";
```

**b) 重定向流过滤器（7层或3/4层二选一）**：
```
-- 方式1：7层流过滤（推荐）
ADD L7FILTER: L7FILTERNAME="f_Redirection", SUBL7FLTNAME="f_SubRedirection";
ADD FLOWFILTER: FLOWFILTERNAME="flowfliter_Redirection", TETHERDETFLAG=FILTER;
ADD PROTBINDFLOWF: FLOWFILTERNAME="flowfliter_Redirection", PROTOCOLNAME="http", L7FILTERNAME="f_Redirection";

-- 方式2：3/4层流过滤
ADD FILTER: FILTERNAME="f_Redirection", L34PROTTYPE=STRING, L34PROTOCOL=ANY;
ADD FLOWFILTER: FLOWFILTERNAME="flowfliter_Redirection", TETHERDETFLAG=FILTER;
ADD PROTBINDFLOWF: FLOWFILTERNAME="flowfliter_Redirection", PROTOCOLNAME="http";
```

**c) 重定向URL配置**：
```
ADD REDIRECT: REDIRECTNAME="Redirect_Name", URL="www.example.com";
ADD PCCACTIONPROP: PCCACTPROPNAME="PCCAction_Name", UPINITREDIRNM="Redirect_Name", UPINITUPGATE=PASS, UPINITDNGATE=PASS, DNINITUPGATE=DISCARD, DNINITDNGATE=DISCARD;
```

**d) PCC策略组（含重定向绑定）**：
```
ADD PCCPOLICYGRP: PCCPOLICYGRPNM="pccfuppolicy_Redir", PCCACTPROPNAME="PCCAction_Name";
```

**e) 配置生效**：
```
SET REFRESHSRV: REFRESHTYPE=ALL;
```

**关键设计要点**：
- UPF侧URR配置必须与SMF侧严格一致（URRID、MONITORINGKEY等）
- 重定向场景需配置门控：上行PASS + 下行DISCARD（拦截下行触发重定向）
- 预定义规则组的Rule_Exhaust和Rule_Redirection通过USERPROFILE+RULEBINDING绑定

### 2.6 E2E调测方法对比

本批次包含三种调测方法，覆盖动态规则和预定义规则两种实现：

| 调测方法 | 适用场景 | 核心工具 | 优势 |
|----------|----------|----------|------|
| 动态规则快速调测 | 动态规则配置 | MML命令查询 | 快捷直观 |
| 预定义规则信令调测 | 预定义规则配置 | 消息跟踪 | 精确到每条信令 |
| 预定义规则快速调测 | 预定义规则配置 | MML命令查询 | 快捷直观 |

**快速调测通用流程**（10步）：
1. LST PSRV 检查用户签约
2. LST PQUOTA 检查配额初始值
3. DSP PCCSESSINFO 检查SMF安装的规则（配额未耗尽时）
4. DSP SESSIONQOSINFO 检查会话QoS参数
5. DSP SESSIONINFO 检查UPF用户上下文
6. 测速验证100Mbit/s体验
7. 持续消耗流量直到配额耗尽
8. LST PQUOTA 确认配额耗尽
9. LST PNTFLOG 确认短信通知已发送
10. DSP PCCSESSINFO 确认规则切换（AG_Exhaust / up_Exhaust）
11. 测速验证1Kbit/s体验 + 重定向

**信令调测核心流程**：
- PCF侧：Npcf_SMPolicyControl_Create/Update Request/Response消息分析
- SMF/UPF侧：PFCP Session Establishment/Modification/Report Request消息分析
- 关注点：策略下发、策略执行、策略更新、事件上报是否符合3GPP协议

### 2.7 基于业务类别的带宽差异化控制方案（ADC） -- 核心E2E方案

**ADC方案是带宽控制子场景的核心E2E方案**，实现了"不同业务不同带宽"的差异化控制。

**业务场景**：当用户访问特定视频应用（如https://www.example.com）时，为其建立专用QoS Flow，提供更高的带宽保障（如100Mbit/s GBR）；当用户不访问该应用时，使用默认QoS参数（如1Mbit/s MBR）。

**核心机制**：基于应用检测（ADC, Application Detection and Control）触发动态策略调整。

**ADC方案的PCC策略下发逻辑**：

| 阶段 | 触发条件 | PCF下发内容 | QoS参数 |
|------|----------|------------|---------|
| 初始上线 | PDU会话建立 | AG_ADC_AppId + AG_ADC_Normal | 5QI=9, maxbr=1Mbps, ARP优先级=1 |
| 访问特定视频流 | APP_STA事件上报 | AG_ADC_Special（新增） | 5QI=4, GBR=100Mbps, ARP优先级=2, 可抢占 |
| 停止访问特定视频流 | APP_STO事件上报 | 删除AG_ADC_Special | 恢复默认QoS |

**关键触发器**：
- `APP_STA`：应用开始检测事件，UPF检测到特定应用流时上报
- `APP_STO`：应用停止检测事件，UPF检测到特定应用流停止时上报

**ADC动态规则信令流程**：

```
用户上线：
  SMF -> PCF: Npcf_SMPolicyControl_Create Request
  PCF -> SMF: Npcf_SMPolicyControl_Create Response
    下发 AG_ADC_AppId (appId=flow_ADC, 触发器APP_STA/APP_STO)
    下发 AG_ADC_Normal (permit out ip from any to any)

用户访问特定视频流：
  UPF -> SMF: PFCP Session Report Request (APP_STA)
  SMF -> PCF: Npcf_SMPolicyControl_Update Request (appDetectionInfos)
  PCF -> SMF: Npcf_SMPolicyControl_Update Response
    下发 AG_ADC_Special (appId=flow_ADC, QoS=5QI4/GBR100Mbps)

用户停止访问特定视频流：
  UPF -> SMF: PFCP Session Report Request (APP_STO)
  SMF -> PCF: Npcf_SMPolicyControl_Update Request (APP_STO)
  PCF -> SMF: Npcf_SMPolicyControl_Update Response
    删除 AG_ADC_Special
```

**ADC方案的QoS差异化对比**：

| 业务状态 | 规则 | 5QI | ARP | 带宽 | 流类型 |
|----------|------|------|-----|------|--------|
| 非特定业务 | AG_ADC_Normal | 9 | 1/NOT_PREEMPT/PREEMPTABLE | MBR 1Mbps | permit any to any |
| 特定视频应用 | AG_ADC_Special | 4 | 2/MAY_PREEMPT/NOT_PREEMPTABLE | GBR 100Mbps | appId=flow_ADC |

**ADC方案与业务重定向方案的差异**：

| 对比维度 | 业务重定向方案 | ADC带宽差异化方案 |
|----------|---------------|-------------------|
| 控制目标 | 配额耗尽触发降速+重定向 | 不同业务不同带宽 |
| 触发机制 | 配额状态（US_RE） | 应用检测（APP_STA/APP_STO） |
| 规则切换 | 配额Normal/Exhaust切换 | 应用开始/停止访问切换 |
| QoS差异 | 100Mbps vs 1Kbps（数量级差异） | 1Mbps vs 100Mbps GBR（业务级差异） |
| 重定向 | 有（配额耗尽时） | 无 |
| 适用场景 | FUP流量管控 | 业务质量保障 |

---

## 3. 配置调测要点

### 3.1 动态规则方案 -- 仅PCF侧配置

动态规则方案的优势在于SMF/UPF无需额外配置，全部由PCF通过Npcf接口下发。PCF侧配置要点：
- 配置完整的5G动作组链：FlowDescription -> FlowInformation -> RedirectInformation -> TrafficControlData -> QoSData -> UsageMonitoringData -> DynamicPccRule
- Normal场景和Exhaust场景分别配置独立的DynamicPccRule
- Rule_Exhaust需挂载消息通知

### 3.2 预定义规则方案 -- 三侧协同配置

预定义规则方案的三侧配置索引关系：

```
PCF侧                           SMF侧                           UPF侧
------                          ------                          ------
PredefinedPccRule:              RULE:                           RULE:
  pccRuleId="Rule_Normal"  <---> RULENAME="Rule_Normal"  <---> RULENAME="Rule_Normal"
  pccRuleId="up_Exhaust"   <---> USERPROFILE="up_Exhaust" <---> USERPROFILE="up_Exhaust"
                                     RULEBINDING:                   RULEBINDING:
                                       Rule_Exhaust                   Rule_Exhaust
                                       Rule_Redirection               Rule_Redirection
```

**三侧URR一致性要求**：URRID和MONITORINGKEY必须跨网元协商一致。SMF侧和UPF侧的ADD URR命令中URRID取值必须完全相同。

### 3.3 UPF侧重定向配置要点

重定向配置有两种实现方式：

**方式1（7层流过滤，推荐）**：
```
ADD L7FILTER: L7FILTERNAME="f_Redirection", SUBL7FLTNAME="f_SubRedirection";
ADD FLOWFILTER: FLOWFILTERNAME="flowfliter_Redirection", TETHERDETFLAG=FILTER;
ADD PROTBINDFLOWF: ..., PROTOCOLNAME="http", L7FILTERNAME="f_Redirection";
ADD REDIRECT: REDIRECTNAME="Redirect_Name", URL="www.example.com";
```

**方式2（3/4层流过滤）**：
```
ADD FILTER: FILTERNAME="f_Redirection", L34PROTTYPE=STRING, L34PROTOCOL=ANY;
ADD FLOWFILTER: FLOWFILTERNAME="flowfliter_Redirection", TETHERDETFLAG=FILTER;
ADD PROTBINDFLOWF: ..., PROTOCOLNAME="http";
ADD REDIRECT: REDIRECTNAME="Redirect_Name", URL="http://172.30.26.103:8080";
```

**PCC动作属性门控设计**：
- UPINITUPGATE=PASS（上行初始上行门控=放通）
- UPINITDNGATE=PASS（上行初始下行门控=放通）
- DNINITUPGATE=DISCARD（下行初始上行门控=丢弃）
- DNINITDNGATE=DISCARD（下行初始下行门控=丢弃）

### 3.4 快速调测核心命令清单

| 网元 | 命令 | 用途 |
|------|------|------|
| UPCF | LST PSRV | 查询用户签约业务 |
| UPCF | LST PQUOTA | 查询用户配额状态 |
| UPCF | LST PNTFLOG | 查询通知发送记录 |
| SMF | DSP PCCSESSINFO | 查询PCC会话信息（含规则名、QoS参数） |
| SMF | DSP SESSIONQOSINFO | 查询会话级QoS参数 |
| SMF | LST USERPROFILE | 查询用户模板 |
| SMF | LST RULEBINDING | 查询规则绑定关系 |
| UPF | DSP SESSIONINFO | 查询用户上下文（含PDR/FAR/QER/URR详情） |

### 3.5 信令调测关键消息

**PCF侧**：
- `Npcf_SMPolicyControl_Create Request/Response` -- 用户初始上线策略下发
- `Npcf_SMPolicyControl_Update Request/Response` -- 策略更新（配额耗尽/应用检测）

**SMF/UPF侧**：
- `PFCP Session Establishment Request` -- 初始会话建立
- `PFCP Session Modification Request` -- 策略修改（规则切换）
- `PFCP Session Report Request` -- 事件上报（US_RE/APP_STA/APP_STO）

---

## 4. 与带宽控制的关系

### 4.1 业务重定向方案 -- FUP类带宽控制的E2E实现

业务重定向方案本质上是FUP（Fair Usage Policy）的E2E实现，属于带宽控制场景中"基于配额使用量的带宽控制"子类。其与带宽控制的关系：

- **带宽控制维度**：基于用户配额状态（Normal vs Exhaust）实施差异化带宽（100Mbps vs 1Kbps）
- **控制触发**：UPCFR的配额累积与耗尽检测
- **控制执行**：PCF通过PCC规则下发QoS参数，SMF/UPF执行限速
- **重定向附加**：配额耗尽时不仅限速，还重定向到充值页面（访问限制子场景与带宽控制子场景的交叉）

### 4.2 ADC方案 -- 带宽控制子场景的核心E2E方案

ADC（Application Detection and Control）方案是带宽控制子场景中"基于业务类别的差异化控制"的典型E2E实现，具有核心地位：

- **核心价值**：不同业务应用获得不同带宽保障，实现精细化的带宽分配
- **技术基础**：基于应用检测（ADC），UPF识别特定应用流后触发策略调整
- **带宽控制机制**：
  - 非特定业务：低保障带宽（MBR 1Mbps, 5QI=9, 非保证比特率）
  - 特定业务：高保障带宽（GBR 100Mbps, 5QI=4, 保证比特率）
- **动态调整**：应用开始/停止时自动建立/释放专用QoS Flow

**ADC方案与特性知识库的对应关系**：
- 对应UDG特性 GWFD-110311（BWM带宽管理）和GWFD-020357（ADC应用检测控制）
- 对应UNC特性 WSFD-211005（BWM）和WSFD-109102（ADC）
- ADC是BWM的前置能力：BWM需要ADC提供应用识别结果才能实施差异化限速

### 4.3 两个方案在带宽控制场景中的定位

```
带宽控制场景
  |
  +-- 基于配额的带宽控制（FUP）
  |     |-- 业务重定向方案（本批次）：配额耗尽 -> 降速 + 重定向 + 通知
  |     |-- 纯FUP限速方案：配额耗尽 -> 仅降速
  |
  +-- 基于业务类别的带宽控制（ADC）
  |     +-- ADC带宽差异化方案（本批次）：不同应用 -> 不同QoS/带宽
  |
  +-- 基于位置区域的带宽控制
  +-- 基于用户等级的带宽控制
  +-- 基于时间时段的带宽控制
```

---

## 5. 关键术语

| 术语 | 简释 |
|------|------|
| **ADC** | Application Detection and Control，应用检测与控制。UPF识别特定应用流量并触发策略调整的技术 |
| **APP_STA** | Application Start，应用开始检测事件。UPF检测到特定应用流开始时上报 |
| **APP_STO** | Application Stop，应用停止检测事件。UPF检测到特定应用流停止时上报 |
| **DynamicPccRule** | 动态PCC规则。PCF通过Npcf接口直接下发完整规则内容 |
| **PredefinedPccRule** | 预定义PCC规则。PCF仅下发规则标识名，具体内容在SMF/UPF预定义 |
| **UserProfile** | 用户模板（预定义规则组）。将多个预定义规则组合在一起，通过RULEBINDING绑定 |
| **US_RE** | Usage Report，使用量上报触发器。UPF向SMF/PCF上报配额消耗情况 |
| **IPCAN_EST** | IP-CAN Session Establishment，IP连通接入网会话建立触发器 |
| **QoSData** | QoS数据动作组。包含5QI、ARP、maxbrUL/DL等QoS参数 |
| **TrafficControlData** | 流量控制数据动作组。包含门控状态(flowStatus)和重定向信息(redirectInfo) |
| **RedirectInformation** | 重定向信息动作组。包含重定向开关、地址类型和服务器地址 |
| **UsageMonitoringData** | 使用量监控数据动作组。包含监控键值(umId)，与配额监控键值关联 |
| **URR** | Usage Reporting Rule，使用量上报规则。分为QoS URR（带宽控制上报）和MK URR（监控键值上报） |
| **URR Group** | 使用量上报规则组。关联多个URR，用于QoS控制和使用量监控 |
| **QoSProp** | QoS属性。SMF/UPF侧定义的QoS参数集合，包含MBRUL/DL、5QI、ARP等 |
| **PCCPOLICYGRP** | PCC策略组。关联URR Group和QoS属性，作为预定义规则的策略载体 |
| **RULEBINDING** | 规则绑定关系。将预定义规则绑定到用户模板(UserProfile) |
| **GBR** | Guaranteed Bit Rate，保证比特率。5QI=4对应GBR类型QoS Flow |
| **Non-GBR** | 非保证比特率。5QI=9对应Non-GBR类型QoS Flow |
| **5QI** | 5G QoS Identifier，5G QoS标识符。不同值对应不同QoS特性 |
| **PCCP Session Report** | PFCP会话报告。UPF通过此消息向SMF上报事件（使用量、应用检测等） |

---

## 6. 知识来源

| 序号 | 文件名 | 主题 |
|------|--------|------|
| 1 | 需求描述_08571766.md | 业务重定向方案需求描述 |
| 2 | 整体方案设计_08571784.md | 业务重定向方案整体设计（含动态+预定义） |
| 3 | PCF侧业务配置_08571786.md | PCF侧动态规则配置 |
| 4 | PCF侧业务配置_71193959.md | PCF侧预定义规则配置 |
| 5 | SMF侧业务配置_71233849.md | SMF侧预定义规则配置 |
| 6 | UPF侧业务配置_24674050.md | UPF侧预定义规则配置（含重定向） |
| 7 | 快速调测方法_08571789.md | 动态规则场景快速调测 |
| 8 | 信令调测方法_24674052.md | 预定义规则场景信令调测 |
| 9 | 快速调测方法_71233851.md | 预定义规则场景快速调测 |
| 10 | 信令调测方法_08571742.md | ADC带宽差异化方案信令调测 |

**文档路径前缀**：
- 文件1-9: `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/业务专题/5G PCC之SM策略解决方案/典型业务场景E2E方案设计/业务重定向方案（预定义+动态）/`
- 文件10: `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/业务专题/5G PCC之SM策略解决方案/典型业务场景E2E方案设计/基于业务类别的带宽差异化控制方案设计（ADC）/E2E业务调测/`
