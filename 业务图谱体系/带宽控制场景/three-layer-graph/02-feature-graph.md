# 带宽控制场景三层图谱 · 第2层：特性图谱

> **文件定位**：`three-layer-graph/02-feature-graph.md`
> **Schema参考**：`三层图谱Schema-最终版-v0.1.md` §9 特性图谱
> **本体参考**：`三层图谱本体标准定义.md`
> **作用**：实例化带宽控制场景24个Feature + depends_on边 + requires_license边 + FeatureRule + FeatureTaskOrderEdge
> **数据来源**：`feature-knowledge/cross-feature-analysis.md`（1,119行）、24个特性知识文件（~31,000行）

---

## 0. 特性图谱总览

### 0.1 24 Feature 分组

| 分组 | UDG特性 | UNC特性 | 小计 |
|------|---------|---------|------|
| 基础感知 | GWFD-110101 SA-Basic, GWFD-111600 SA特征库更新管控 | — | 2 |
| PCC框架 | GWFD-020351 PCC基本功能 | WSFD-109101 PCC基本功能 | 2 |
| 核心带宽控制 | GWFD-110311 基于业务感知的带宽控制 | WSFD-211005 基于业务感知的带宽控制 | 2 |
| Shaping整形 | GWFD-020354 基于业务的Shaping, GWFD-110313 智能Shaping组级带宽控制 | — | 2 |
| FUP累计流量 | GWFD-020353 基于累计流量的策略控制, GWFD-110312 基于业务累计流量的策略控制 | WSFD-109104 基于累计流量的策略控制, WSFD-211009 基于业务累计流量的策略控制 | 4 |
| QoS保证 | GWFD-020358 业务触发的QoS保证, GWFD-110302 基于上下行解耦的视频承载信令控制 | WSFD-109107 业务触发的QoS保证 | 3 |
| ADC检测 | GWFD-020357 增强的ADC基本功能 | WSFD-109102 ADC基本功能 | 2 |
| 无线优化 | GWFD-020359 IM类业务无线资源管控, GWFD-110301 基于终端系统的码率差异化控制, GWFD-110331 基于业务流标识的无线资源优化, GWFD-110332 基于小区负荷上报的无线资源优化 | WSFD-211101 基于小区负荷上报的无线资源优化 | 5 |
| 位置感知 | — | WSFD-109108 基于接入点策略控制 | 1 |
| 异常检测 | GWFD-020305 终端异常下行流量检测 | — | 1 |
| **合计** | **16** | **8** | **24** |

### 0.2 License 总览

| 产品 | License数 | 说明 |
|------|----------|------|
| UDG | 16 | 每个特性1个独立License，基础层3个（SA-Basic + PCC + SA特征库管控），功能层13个 |
| UNC | 8 | 每个特性1个独立License，基础层1个（PCC SMF/PGW-C），功能层7个 |
| 无无需License特性 | 0 | 所有24个特性均有独立License控制项 |

### 0.3 全局字段声明（status）

> **适用范围**：本文件 §1（24个Feature）和 §3（24个License）所有对象。
> **声明**：除非特别标注，本文件所有 Feature（GWFD/WSFD-*）和 License（LKV*）的 `status` 字段值均为 `active`。
> **依据**：Schema §9.4（Feature.status 必备）和 §9.5（License.status 必备）。带宽控制场景所有特性和 License 均处于正式启用状态。
> **例外**：无。所有对象当前均为 `active`，无 `deprecated` 或 `planned` 状态。

---

## 1. Feature 实例化（24个）

### 1.1 基础感知

#### GWFD-110101 SA-Basic（业务感知基本功能）

| 字段 | 值 |
|------|---|
| `feature_id` | `GWFD-110101` |
| `feature_name` | `SA-Basic` |
| `feature_summary` | L3/L4/L7业务识别基础引擎，提供SVC/APP识别能力，是整个带宽控制场景的数据基础，被12个特性直接或间接依赖 |
| `feature_group` | `基础感知` |
| `variant_dimensions` | `["识别层级(L3/L4/L7)", "特征库版本"]` |
| `applicable_nf_map` | `{"UDG": ["SGW-U", "PGW-U", "UPF"]}` |
| `first_release` | `UDG 20.0.0` |
| `requires_license` | `LKV3G5SABS01` |
| `key_capabilities` | ① L3/L4五元组解析（IP/端口/协议）② 协议识别（知名端口+签名匹配）③ L7 URL/Method/Response Code解析 ④ SVC（业务大类）+ APP（具体应用）标识输出 ⑤ SET REFRESHSRV策略刷新 ⑥ CP/UP配置一致性检查 |
| `source_evidence_ids` | `EV-FK-01`, `EV-CA-01` |

#### GWFD-111600 SA特征库更新管控

| 字段 | 值 |
|------|---|
| `feature_id` | `GWFD-111600` |
| `feature_name` | `SA特征库更新管控` |
| `feature_summary` | SA特征库版本License管理，维护SA-Basic使用的特征库数据，通过LOD SIGNATUREDB加载 |
| `feature_group` | `基础感知` |
| `variant_dimensions` | `["特征库版本"]` |
| `applicable_nf_map` | `{"UDG": ["SGW-U", "PGW-U", "UPF"]}` |
| `first_release` | `UDG 20.12.2` |
| `requires_license` | `LKV3G5SSDUC1` |
| `key_capabilities` | ① SA特征库版本License控制 ② LOD SIGNATUREDB/LOD PARSERDB加载管理 ③ 维护SA-Basic引擎使用的特征库数据 |
| `source_evidence_ids` | `EV-FK-02`, `EV-CA-01` |

### 1.2 PCC框架

#### GWFD-020351 PCC基本功能（UDG）

| 字段 | 值 |
|------|---|
| `feature_id` | `GWFD-020351` |
| `feature_name` | `PCC基本功能` |
| `feature_summary` | UDG侧PCC基础，接收N4规则（PDR/FAR/QER/URR/BAR），执行MBR限速/GBR保障/Gate门控，是所有UDG侧策略特性的前置依赖 |
| `feature_group` | `PCC框架` |
| `variant_dimensions` | `["规则来源(动态/预定义/本地)", "有无PCRF"]` |
| `applicable_nf_map` | `{"UDG": ["SGW-U", "PGW-U", "UPF"]}` |
| `first_release` | `UDG 20.0.0` |
| `requires_license` | `LKV3G5PCCB01` |
| `key_capabilities` | ① 接收PCRF/PCF策略（经N4）② N4规则体系（PDR/FAR/QER/URR/BAR）③ 动态/预定义/本地规则三种模式 ④ SET REFRESHSRV策略刷新（PROTBINDFLOWF 60s延迟）⑤ MBR限速 + GBR保障 + Gate门控执行 |
| `source_evidence_ids` | `EV-FK-03`, `EV-CA-01` |

#### WSFD-109101 PCC基本功能（UNC）

| 字段 | 值 |
|------|---|
| `feature_id` | `WSFD-109101` |
| `feature_name` | `PCC基本功能` |
| `feature_summary` | UNC(SMF/PGW-C)侧PCC基础，接收PCRF/PCF的QCI/5QI/MBR/GBR/ARP策略，管理PCC规则生命周期，通过N4下发给UDG执行 |
| `feature_group` | `PCC框架` |
| `variant_dimensions` | `["接口(Gx/N7)", "PCRF冗余模式"]` |
| `applicable_nf_map` | `{"UNC": ["SMF", "PGW-C", "AMF", "GGSN"]}` |
| `first_release` | `UNC 20.0.0` |
| `requires_license` | `LKV3W9SPCC11` |
| `key_capabilities` | ① Gx接口Diameter信令（2/3/4G）② N7/N15服务化接口（5G）③ IP-CAN会话管理（CCR-I/U/T）④ PCRF冗余（主备/轮询/百分比+Failover）⑤ Event Triggers（USAGE_REPORT/QOS_CHANGE/APP_STA/STO等） |
| `source_evidence_ids` | `EV-FK-17`, `EV-CA-01` |

### 1.3 核心带宽控制

#### GWFD-110311 基于业务感知的带宽控制（UDG）

| 字段 | 值 |
|------|---|
| `feature_id` | `GWFD-110311` |
| `feature_name` | `基于业务感知的带宽控制` |
| `feature_summary` | UDG侧核心带宽控制特性，定义独有的三级BWM控制体系（用户级/组级/全局级），通过SA识别业务后执行CAR限速或Shaping整形 |
| `feature_group` | `核心带宽控制` |
| `variant_dimensions` | `["控制层级(用户/组/全局)", "CTRLTYPE(CAR/SHAPING)", "BWMRULETYPE"]` |
| `applicable_nf_map` | `{"UDG": ["SGW-U", "PGW-U", "UPF"]}` |
| `first_release` | `UDG 20.9.0`（v02） |
| `requires_license` | `LKV3G5TCSA01` |
| `key_capabilities` | ① 三级BWM控制：用户级（SUBSCRIBER_SPECIFIC）/ 组级（GROUP_SPECIFIC）/ 全局级（GLOBAL）② CAR限速（令牌桶直接丢弃超额报文）③ Shaping整形（GTS队列缓冲）④ 三色标记（GREEN/YELLOW/RED）⑤ BWMSERVICE→BWMCONTROLLER→BWMUSERGROUP→BWMRULE四级配置 ⑥ BWMRULEGLOBAL全局级规则 ⑦ APN绑定（APNBINDBWMUSRG） |
| `source_evidence_ids` | `EV-FK-04`, `EV-CA-01` |

#### WSFD-211005 基于业务感知的带宽控制（UNC）

| 字段 | 值 |
|------|---|
| `feature_id` | `WSFD-211005` |
| `feature_name` | `基于业务感知的带宽控制` |
| `feature_summary` | UNC侧BWM规则管理，通过ADD RULE(POLICYTYPE=BWM)定义BWM策略，N4下发给UDG执行；POLICYTYPE=BWM是UNC侧独有标识 |
| `feature_group` | `核心带宽控制` |
| `variant_dimensions` | `["接口(Gx/N7)"]` |
| `applicable_nf_map` | `{"UNC": ["GGSN", "PGW-C", "SMF"]}` |
| `first_release` | `UNC 20.5.0` |
| `requires_license` | `LKV3TCBSA01` |
| `key_capabilities` | ① POLICYTYPE=BWM策略类型标识（UNC独有）② RULE→USERPROFILE→RULEBINDING规则绑定 ③ USRPROFGROUP→UPBINDUPG→APNUSRPROFG APN级生效绑定链 ④ RULENAME全网一致性要求（PCRF/PCF+UNC+UDG） |
| `source_evidence_ids` | `EV-FK-19`, `EV-CA-01` |

### 1.4 Shaping整形

#### GWFD-020354 基于业务的Shaping

| 字段 | 值 |
|------|---|
| `feature_id` | `GWFD-020354` |
| `feature_name` | `基于业务的Shaping` |
| `feature_summary` | 用户级令牌桶整形，缓冲超额报文到GTS队列延迟转发，TCP友好（适合视频等抖动敏感业务），仅支持用户级（SUBSCRIBER_SPECIFIC） |
| `feature_group` | `Shaping整形` |
| `variant_dimensions` | `["RATE", "QUEDEPTH"]` |
| `applicable_nf_map` | `{"UDG": ["SGW-U", "PGW-U", "UPF"]}` |
| `first_release` | `UDG 20.1.0` |
| `requires_license` | `LKV3G5SBTS01` |
| `key_capabilities` | ① CTRLTYPE=SHAPING（固定）② RATE限速速率 + QUEDEPTH队列深度配置 ③ GTS队列缓冲超额报文 ④ 平滑输出减少TCP重传 ⑤ 仅用户级（BWMRULETYPE=SUBSCRIBER_SPECIFIC）⑥ 依赖SA识别业务类型 |
| `source_evidence_ids` | `EV-FK-05`, `EV-CA-01` |

#### GWFD-110313 智能Shaping组级带宽控制

| 字段 | 值 |
|------|---|
| `feature_id` | `GWFD-110313` |
| `feature_name` | `智能Shaping组级带宽控制` |
| `feature_summary` | 组级智能整形，在普通Shaping基础上增加AUTO模式自动调优，按ServiceLevel差异化分配带宽，依赖BWM+Shaping双License |
| `feature_group` | `Shaping整形` |
| `variant_dimensions` | `["WORKMODE(AUTO/MANUAL)", "ASSUREMODE(EXPFIRST/RATEFIRST)"]` |
| `applicable_nf_map` | `{"UDG": ["SGW-U", "PGW-U", "UPF"]}` |
| `first_release` | `UDG 20.7.0` |
| `requires_license` | `LKV3G5FSHP01` |
| `key_capabilities` | ① WORKMODE=AUTO/MANUAL（自动/手动调优）② ASSUREMODE=EXPFIRST/RATEFIRST（体验优先/速率优先）③ BCSRVLEVELPLY按ServiceLevel差异化带宽 ④ PKTLOSTRATEDTL丢包率差值自动调整 ⑤ USERFAIREN用户公平使能 ⑥ BWMRULETYPE=GROUP_SPECIFIC（组级） |
| `source_evidence_ids` | `EV-FK-06`, `EV-CA-01` |

### 1.5 FUP累计流量

#### GWFD-020353 基于累计流量的策略控制（会话级FUP，UDG）

| 字段 | 值 |
|------|---|
| `feature_id` | `GWFD-020353` |
| `feature_name` | `基于累计流量的策略控制` |
| `feature_summary` | UDG侧会话级FUP，URR流量阈值监控，per Session累计所有流量，不依赖SA识别，达阈值后PCRF/PCF下发新QoS降速 |
| `feature_group` | `FUP累计流量` |
| `variant_dimensions` | `["USAGERPTMODE(ONLINE/MONITORINGKEY)", "接口(Gx/N7)"]` |
| `applicable_nf_map` | `{"UDG": ["SGW-U", "PGW-U", "UPF"]}` |
| `first_release` | `UDG 20.2.0` |
| `requires_license` | `LKV3G5PCBT01` |
| `key_capabilities` | ① URR流量计数（USAGERPTMODE=ONLINE/MONITORINGKEY）② per Session全流量累计 ③ VOLTH流量阈值耗尽上报 ④ Gx UM Level=SESSION_LEVEL(0) ⑤ URR关联所有Create PDRs ⑥ 不依赖SA（不需要业务识别） |
| `source_evidence_ids` | `EV-FK-07`, `EV-CA-01` |

#### WSFD-109104 基于累计流量的策略控制（会话级FUP，UNC）

| 字段 | 值 |
|------|---|
| `feature_id` | `WSFD-109104` |
| `feature_name` | `基于累计流量的策略控制` |
| `feature_summary` | UNC侧会话级FUP，接收PCRF阈值，N4 URR下发给UDG；Gx场景需额外配置PCCFUNC/PCRF/PCCPOLICYGRP，N7场景仅需License |
| `feature_group` | `FUP累计流量` |
| `variant_dimensions` | `["接口(Gx/N7)", "UMCH拥塞处理"]` |
| `applicable_nf_map` | `{"UNC": ["GGSN-C", "PGW-C", "SMF"]}` |
| `first_release` | `UNC 20.3.0` |
| `requires_license` | `LKV3W9PCBT12` |
| `key_capabilities` | ① Gx场景：SET PCCFUNC + MOD PCRF(UMCH) + MOD PCCPOLICYGRP(FUPSESSIONEXC) ② N7场景：仅需License，阈值由PCF umDecs配置 ③ URR + URRGROUP + PCCPOLICYGRP UNC侧配置 ④ Usage-Monitoring-Information AVP（Gx）/ volumeThreshold（N7）阈值下发 |
| `source_evidence_ids` | `EV-FK-18`, `EV-CA-01` |

#### GWFD-110312 基于业务累计流量的策略控制（业务级FUP，UDG）

| 字段 | 值 |
|------|---|
| `feature_id` | `GWFD-110312` |
| `feature_name` | `基于业务累计流量的策略控制` |
| `feature_summary` | UDG侧业务级FUP，per SVC/per APP独立累计流量，依赖SA识别+BWM规则匹配，Monitoring-Key标识不同业务 |
| `feature_group` | `FUP累计流量` |
| `variant_dimensions` | `["累计粒度(per SVC/per APP)", "Monitoring-Key"]` |
| `applicable_nf_map` | `{"UDG": ["SGW-U", "PGW-U", "UPF"]}` |
| `first_release` | `UDG 20.5.0` |
| `requires_license` | `LKV3G5FPBS01` |
| `key_capabilities` | ① per SVC/per APP独立累计（区别于会话级FUP的全量累计）② Gx UM Level=PCC_RULE_LEVEL(1) ③ Monitoring-Key标识业务类型 ④ URR只绑定指定业务流的PDRs ⑤ 依赖SA识别（GWFD-110101）+ BWM规则匹配（GWFD-110311） |
| `source_evidence_ids` | `EV-FK-08`, `EV-CA-01` |

#### WSFD-211009 基于业务累计流量的策略控制（业务级FUP，UNC）

| 字段 | 值 |
|------|---|
| `feature_id` | `WSFD-211009` |
| `feature_name` | `基于业务累计流量的策略控制` |
| `feature_summary` | UNC侧业务级FUP，URR绑定指定业务流的PDRs，依赖BWM(UNC)配合，通过Monitoring-Key标识不同业务 |
| `feature_group` | `FUP累计流量` |
| `variant_dimensions` | `["接口(Gx/N7)"]` |
| `applicable_nf_map` | `{"UNC": ["GGSN", "PGW-C", "SMF"]}` |
| `first_release` | `UNC 20.3.0` |
| `requires_license` | `LKV2FUPSAT01` |
| `key_capabilities` | ① URR + URRGROUP + PCCPOLICYGRP UNC侧配置 ② Monitoring-Key标识业务 ③ URR只绑定指定业务流PDRs ④ 依赖BWM(UNC)（WSFD-211005）配合 |
| `source_evidence_ids` | `EV-FK-20`, `EV-CA-01` |

### 1.6 QoS保证

#### GWFD-020358 业务触发的QoS保证（UDG）

| 字段 | 值 |
|------|---|
| `feature_id` | `GWFD-020358` |
| `feature_name` | `业务触发的QoS保证` |
| `feature_summary` | UDG侧GBR保证，SA识别高价值业务→URR(QOS模式)上报QoS事件→触发专有承载(2/3/4G)/专有QoS Flow(5G)建立，保证带宽下限 |
| `feature_group` | `QoS保证` |
| `variant_dimensions` | `["USAGERPTMODE(QOS)", "QOSTYPE(QOS_FLOW_PARA/QOS_BEARER_PARA)"]` |
| `applicable_nf_map` | `{"UDG": ["SGW-U", "PGW-U", "UPF"]}` |
| `first_release` | `UDG 20.2.0` |
| `requires_license` | `LKV3G5STQE01` |
| `key_capabilities` | ① USAGERPTMODE=QOS（区别于FUP的ONLINE/MONITORINGKEY）② SA识别业务→PFCP Session Report上报QoS事件 ③ 触发UNC侧专有承载/QoS Flow建立 ④ GBR-UL/DL带宽下限保证 ⑤ 每用户10个专有承载/63个QoS Flow |
| `source_evidence_ids` | `EV-FK-10`, `EV-CA-01` |

#### WSFD-109107 业务触发的QoS保证（UNC）

| 字段 | 值 |
|------|---|
| `feature_id` | `WSFD-109107` |
| `feature_name` | `业务触发的QoS保证` |
| `feature_summary` | UNC侧GBR保证，接收QoS事件，发起专有承载(2/3/4G)/专有QoS Flow(5G)建立，配置QOSPROP(GBR/MBR/5QI/QCI/ARP) |
| `feature_group` | `QoS保证` |
| `variant_dimensions` | `["接口(Gx/N7)", "QOSTYPE"]` |
| `applicable_nf_map` | `{"UNC": ["GGSN-C", "PGW-C", "SMF"]}` |
| `first_release` | `UNC 20.5.0` |
| `requires_license` | `LKV3W9STQE11` |
| `key_capabilities` | ① QOSPROP配置（QOSTYPE=QOS_FLOW_PARA(5G)/QOS_BEARER_PARA(2/3/4G)）② GBR-UL/DL + MBR-UL/DL + QCI/5QI + ARP参数 ③ SET APNIDLETIME专有QoS Flow空闲定时器 ④ ADD APNDEACTQFPLCY去活策略（DELAY_RELEASE）⑤ 专有承载方向性控制 |
| `source_evidence_ids` | `EV-FK-22`, `EV-CA-01` |

#### GWFD-110302 基于上下行解耦的视频承载信令控制

| 字段 | 值 |
|------|---|
| `feature_id` | `GWFD-110302` |
| `feature_name` | `基于上下行解耦的视频承载信令控制` |
| `feature_summary` | 视频业务上下行解耦，只为下行建专载、上行走缺省，复用QoS保证的QOSPROP增加DECOUPLINGSW参数 |
| `feature_group` | `QoS保证` |
| `variant_dimensions` | `["DECOUPLINGSW(ENABLE/DISABLE)"]` |
| `applicable_nf_map` | `{"UDG": ["SGW-U", "PGW-U", "UPF"]}` |
| `first_release` | `UDG 20.9.0` |
| `requires_license` | `LKV3G5SCUD01` |
| `key_capabilities` | ① DECOUPLINGSW=ENABLE（上下行解耦开关）② 复用QoS保证的QOSPROP对象 ③ 仅下行建专载（节省上行资源）④ 依赖QoS保证（GWFD-020358）⑤ 适用于直播/点播下行高带宽场景 |
| `source_evidence_ids` | `EV-FK-12`, `EV-CA-01` |

### 1.7 ADC检测

#### GWFD-020357 增强的ADC基本功能（UDG）

| 字段 | 值 |
|------|---|
| `feature_id` | `GWFD-020357` |
| `feature_name` | `增强的ADC基本功能` |
| `feature_summary` | UDG侧ADC，基于SA的L7 DPI引擎检测应用，上报APPLICATION_START/STOP(Gx)/APP_STA/STO(N7)触发PCRF动态策略 |
| `feature_group` | `ADC检测` |
| `variant_dimensions` | `["接口(Gx/N7)", "Event Triggers"]` |
| `applicable_nf_map` | `{"UDG": ["SGW-U", "PGW-U", "UPF"]}` |
| `first_release` | `UDG 20.1.0` |
| `requires_license` | `LKV3G5ADCF01` |
| `key_capabilities` | ① SA L7 DPI引擎应用检测 ② APPLICATION_START/STOP事件上报（Gx）③ APP_STA/STO事件上报（N7）④ ADCPARA参数配置 ⑤ FLOWFILTERNAME/appid全网一致性要求 |
| `source_evidence_ids` | `EV-FK-09`, `EV-CA-01` |

#### WSFD-109102 ADC基本功能（UNC）

| 字段 | 值 |
|------|---|
| `feature_id` | `WSFD-109102` |
| `feature_name` | `ADC基本功能` |
| `feature_summary` | UNC侧ADC，转发PCRF/PCF应用检测事件，承载管理，三策略组（Normal/Start/Stop），FLOWFILTER+ADCPARA三网元一致性 |
| `feature_group` | `ADC检测` |
| `variant_dimensions` | `["接口(Gx/N7)"]` |
| `applicable_nf_map` | `{"UNC": ["GGSN-C", "PGW-C", "SMF"]}` |
| `first_release` | `UNC 20.5.0` |
| `requires_license` | `LKV2BADCF01` |
| `key_capabilities` | ① 三策略组（Normal/Start/Stop）② FLOWFILTER+ADCPARA三网元一致性 ③ 承载管理（专载建立/更新/释放）④ PCRF/PCF应用检测事件转发 |
| `source_evidence_ids` | `EV-FK-21`, `EV-CA-01` |

### 1.8 无线优化

#### GWFD-020359 IM类业务无线资源管控

| 字段 | 值 |
|------|---|
| `feature_id` | `GWFD-020359` |
| `feature_name` | `IM类业务无线资源管控` |
| `feature_summary` | SA识别IM业务（QQ/MSN/Fetion），映射DSCP值影响BSC/RNC无线调度，优化心跳保活 |
| `feature_group` | `无线优化` |
| `variant_dimensions` | `["DSCP映射(QQ=12/MSN=14/Fetion=18)"]` |
| `applicable_nf_map` | `{"UDG": ["SGW-U", "PGW-U", "UPF"]}` |
| `first_release` | `UDG 20.7.0` |
| `requires_license` | `LKV3G5ITSR01` |
| `key_capabilities` | ① SA识别IM业务类型 ② DSCP映射（QQ=12, MSN=14, Fetion=18）③ 影响2/3G BSC/RNC无线调度 ④ 心跳保活优化 |
| `source_evidence_ids` | `EV-FK-13`, `EV-CA-01` |

#### GWFD-110301 基于终端系统的码率差异化控制

| 字段 | 值 |
|------|---|
| `feature_id` | `GWFD-110301` |
| `feature_name` | `基于终端系统的码率差异化控制` |
| `feature_summary` | SA识别终端OS（Android/iOS/Windows），通过BWM框架增加OSTYPE维度实现码率差异化，适配不同编码格式 |
| `feature_group` | `无线优化` |
| `variant_dimensions` | `["OSTYPE"]` |
| `applicable_nf_map` | `{"UDG": ["SGW-U", "PGW-U", "UPF"]}` |
| `first_release` | `UDG 20.9.0` |
| `requires_license` | `LKV3G5RDSC01` |
| `key_capabilities` | ① SA识别终端OS类型 ② SET APNOSLELBWMSW终端OS BWM开关 ③ 通过BWM框架增加OSTYPE维度 ④ 差异化BWM策略 ⑤ 适用于视频OTT不同编码格式适配 |
| `source_evidence_ids` | `EV-FK-11`, `EV-CA-01` |

#### GWFD-110331 基于业务流标识的无线资源优化

| 字段 | 值 |
|------|---|
| `feature_id` | `GWFD-110331` |
| `feature_name` | `基于业务流标识的无线资源优化` |
| `feature_summary` | SA识别业务流→匹配FPI规则→标记FPI/DSCP/GTP-U扩展头→基站按队列调度，FPI值范围0-255映射7个队列 |
| `feature_group` | `无线优化` |
| `variant_dimensions` | `["FPI值范围(0-255)", "队列映射(0-6)"]` |
| `applicable_nf_map` | `{"UDG": ["SGW-U", "PGW-U", "UPF"]}` |
| `first_release` | `UDG 20.7.0` |
| `requires_license` | `LKV3G5WOFR01` |
| `key_capabilities` | ① FPI值0-255标记 ② 7个队列映射（0-6），队列1权重为1（规划风险）③ DSCP标记 ④ GTP-U扩展头携带 ⑤ 全业务类型无线调度优化 |
| `source_evidence_ids` | `EV-FK-14`, `EV-CA-01` |

> **规划风险**: FPI值8~15映射的队列1调度权重仅为1（其他队列为10），在空口资源紧张时几乎得不到调度机会。配置时需特别注意避免将高价值业务映射到此范围。

#### GWFD-110332 基于小区负荷上报的无线资源优化（UDG）

| 字段 | 值 |
|------|---|
| `feature_id` | `GWFD-110332` |
| `feature_name` | `基于小区负荷上报的无线资源优化` |
| `feature_summary` | UDG侧小区负荷感知，RAN上报负荷等级（Level 0-3）→UDG转发→UNC上报PCRF→动态调整BWM策略 |
| `feature_group` | `无线优化` |
| `variant_dimensions` | `["负荷等级(Invalid/Normal/Congestion/Overload)"]` |
| `applicable_nf_map` | `{"UDG": ["SGW-U", "PGW-U", "UPF"]}` |
| `first_release` | `UDG 20.8.2` |
| `requires_license` | `LKV3G5WOCR01` |
| `key_capabilities` | ① GTP-U扩展头接收小区负荷信息 ② 负荷等级（0=Invalid/1=Normal/2=Congestion/3=Overload）③ PFCP Session Report上报UNC ④ CELL_CONGESTION_CHANGE Event Trigger ⑤ 不直接依赖SA但需BWM配合执行 |
| `source_evidence_ids` | `EV-FK-15`, `EV-CA-01` |

#### WSFD-211101 基于小区负荷上报的无线资源优化（UNC）

| 字段 | 值 |
|------|---|
| `feature_id` | `WSFD-211101` |
| `feature_name` | `基于小区负荷上报的无线资源优化` |
| `feature_summary` | UNC侧负荷信息转发，接收UDG上报的小区负荷等级，通过Gx接口转发PCRF，SET APNREPORTATTR配置拥塞上报属性 |
| `feature_group` | `无线优化` |
| `variant_dimensions` | `["接口(Gx)"]` |
| `applicable_nf_map` | `{"UNC": ["GGSN-C", "PGW-C"]}` |
| `first_release` | `UNC 20.7.0` |
| `requires_license` | `LKV3W9WOCR11` |
| `key_capabilities` | ① CELL_CONGESTION_CHANGE Event Trigger上报PCRF ② SET APNREPORTATTR APN拥塞上报属性 ③ Gx接口转发负荷信息 ④ 触发PCRF动态调整BWM策略 |
| `source_evidence_ids` | `EV-FK-24`, `EV-CA-01` |

### 1.9 位置感知

#### WSFD-109108 基于接入点策略控制

| 字段 | 值 |
|------|---|
| `feature_id` | `WSFD-109108` |
| `feature_name` | `基于接入点策略控制` |
| `feature_summary` | WiFi用户位置变化感知（UE_LOCAL_IP_ADDRESS_CHANGE, Trigger=43），激活预定义差异化带宽规则，适用于WiFi分流场景 |
| `feature_group` | `位置感知` |
| `variant_dimensions` | `["位置条件(PLMN/接入点)"]` |
| `applicable_nf_map` | `{"UNC": ["PGW-C"]}` |
| `first_release` | `UNC 20.5.0` |
| `requires_license` | `LKV3WPWULI11` |
| `key_capabilities` | ① UE_LOCAL_IP_ADDRESS_CHANGE事件检测 ② Trigger=43位置变化触发 ③ 激活预定义差异化带宽规则 ④ WiFi接入点位置感知 ⑤ Gx接口Event-Trigger上报 |
| `source_evidence_ids` | `EV-FK-23`, `EV-CA-01` |

### 1.10 异常检测

#### GWFD-020305 终端异常下行流量检测

| 字段 | 值 |
|------|---|
| `feature_id` | `GWFD-020305` |
| `feature_name` | `终端异常下行流量检测` |
| `feature_summary` |异常流量检测，SA辅助识别异常模式，阈值计数触发阻断恶意终端，门控阻断或告警 |
| `feature_group` | `异常检测` |
| `variant_dimensions` | `["检测阈值", "阻断动作"]` |
| `applicable_nf_map` | `{"UDG": ["SGW-U", "PGW-U", "UPF"]}` |
| `first_release` | `UDG 20.5.0` |
| `requires_license` | `LKV3G5ADTD01` |
| `key_capabilities` | ① 异常流量模式检测 ② SA辅助识别（间接依赖）③ 阈值计数触发 ④ 阻断恶意终端 ⑤ 告警通知 |
| `source_evidence_ids` | `EV-FK-16`, `EV-CA-01` |

---

## 2. Feature depends_on 关系边（26条）

### 2.1 UDG侧依赖（20条）

| 源Feature | 关系 | 目标Feature | 依赖类型 | 依赖理由 |
|-----------|------|-------------|----------|----------|
| GWFD-111600 (SA特征库管控) | `depends_on` | GWFD-110101 (SA-Basic) | data_maintenance | 维护SA-Basic使用的特征库数据 |
| GWFD-020351 (PCC) | `depends_on` | GWFD-110101 (SA-Basic) | mandatory | PCC前置条件：完成业务感知配置 |
| GWFD-110311 (BWM) | `depends_on` | GWFD-110101 (SA-Basic) | mandatory | BWM依赖SA识别业务→BWM规则匹配 |
| GWFD-110311 (BWM) | `depends_on` | GWFD-020351 (PCC) | mandatory | BWM依赖PCC规则体系 |
| GWFD-020354 (Shaping) | `depends_on` | GWFD-110101 (SA-Basic) | mandatory | Shaping依赖SA识别业务 |
| GWFD-110313 (智能Shaping) | `depends_on` | GWFD-110311 (BWM) | mandatory | 智能Shaping依赖BWM框架 |
| GWFD-110313 (智能Shaping) | `depends_on` | GWFD-020354 (Shaping) | mandatory | 智能Shaping依赖Shaping基础能力 |
| GWFD-110312 (业务FUP) | `depends_on` | GWFD-110101 (SA-Basic) | mandatory | 业务FUP依赖SA识别才能per SVC/per APP累计 |
| GWFD-110312 (业务FUP) | `depends_on` | GWFD-110311 (BWM) | mandatory | 业务FUP依赖BWM规则匹配 |
| GWFD-020353 (会话FUP) | `depends_on` | GWFD-020351 (PCC) | mandatory | 会话FUP依赖PCC URR上报机制 |
| GWFD-020358 (QoS保证) | `depends_on` | GWFD-110101 (SA-Basic) | mandatory | QoS保证依赖SA识别触发专载 |
| GWFD-020358 (QoS保证) | `depends_on` | GWFD-020351 (PCC) | mandatory | QoS保证依赖PCC专载信令 |
| GWFD-110302 (视频解耦) | `depends_on` | GWFD-020358 (QoS保证) | mandatory | 视频解耦是QoS保证的增强版，复用QOSPROP |
| GWFD-020357 (ADC) | `depends_on` | GWFD-110101 (SA-Basic) | mandatory | ADC使用SA的L7 DPI引擎 |
| GWFD-020305 (异常检测) | `depends_on` | GWFD-110101 (SA-Basic) | optional | SA辅助识别异常流量模式 |
| GWFD-020359 (IM管控) | `depends_on` | GWFD-110101 (SA-Basic) | mandatory | IM管控依赖SA识别IM业务类型 |
| GWFD-110301 (码率差异化) | `depends_on` | GWFD-110101 (SA-Basic) | mandatory | 码率差异化依赖SA识别终端OS |
| GWFD-110301 (码率差异化) | `depends_on` | GWFD-110311 (BWM) | optional | 码率差异化复用BWM框架 |
| GWFD-110331 (FPI标记) | `depends_on` | GWFD-110101 (SA-Basic) | mandatory | FPI标记依赖SA识别业务流 |
| GWFD-110332 (小区负荷) | `depends_on` | GWFD-110311 (BWM) | optional | 小区负荷需BWM配合执行动态策略 |

### 2.2 UNC侧依赖（6条）

| 源Feature | 关系 | 目标Feature | 依赖类型 | 依赖理由 |
|-----------|------|-------------|----------|----------|
| WSFD-211005 (BWM UNC) | `depends_on` | WSFD-109101 (PCC UNC) | mandatory | BWM(UNC)依赖PCC(UNC)规则体系 |
| WSFD-109104 (会话FUP UNC) | `depends_on` | WSFD-109101 (PCC UNC) | mandatory | 会话FUP(UNC)依赖PCC(UNC) |
| WSFD-211009 (业务FUP UNC) | `depends_on` | WSFD-109101 (PCC UNC) | mandatory | 业务FUP(UNC)依赖PCC(UNC) |
| WSFD-211009 (业务FUP UNC) | `depends_on` | WSFD-211005 (BWM UNC) | mandatory | 业务FUP(UNC)依赖BWM(UNC)配合 |
| WSFD-109107 (QoS保证 UNC) | `depends_on` | WSFD-109101 (PCC UNC) | mandatory | QoS保证(UNC)依赖PCC(UNC) |
| WSFD-211101 (小区负荷 UNC) | `depends_on` | WSFD-109101 (PCC UNC) | mandatory | 小区负荷(UNC)依赖PCC(UNC) Gx上报 |

---

## 3. License 实例化（24个：UDG 16 + UNC 8）

### 3.1 UDG侧License（16个）

| `license_id` | `license_name` | 对应Feature | `status` | 说明 |
|---------------|----------------|-------------|----------|------|
| `LKV3G5SABS01` | SA-Basic (82209749) | GWFD-110101 | `active` | 业务感知基础License（基础层） |
| `LKV3G5PCCB01` | PCC基本功能 (82209825) | GWFD-020351 | `active` | PCC框架License（基础层） |
| `LKV3G5SSDUC1` | SA特征库管控 (81203996) | GWFD-111600 | `active` | SA特征库版本License（基础层） |
| `LKV3G5TCSA01` | BWM (82209832) | GWFD-110311 | `active` | 核心带宽控制License（功能层） |
| `LKV3G5SBTS01` | Shaping (82200AFN) | GWFD-020354 | `active` | 用户级整形License（功能层） |
| `LKV3G5FSHP01` | 智能Shaping (82200FNS) | GWFD-110313 | `active` | 组级智能整形License（功能层） |
| `LKV3G5PCBT01` | 会话级FUP (82200AFM) | GWFD-020353 | `active` | 会话级流量累计License（功能层） |
| `LKV3G5FPBS01` | 业务级FUP (82209776) | GWFD-110312 | `active` | 业务级流量累计License（功能层） |
| `LKV3G5STQE01` | QoS保证 (82200AFP) | GWFD-020358 | `active` | GBR保证License（功能层） |
| `LKV3G5SCUD01` | 上下行解耦 (82200EBQ) | GWFD-110302 | `active` | 视频解耦License（功能层） |
| `LKV3G5ADCF01` | ADC (82200AFK) | GWFD-020357 | `active` | 应用检测License（功能层） |
| `LKV3G5ADTD01` | 异常检测 (82200BAJ) | GWFD-020305 | `active` | 异常流量检测License（功能层） |
| `LKV3G5ITSR01` | IM管控 (82200BLD) | GWFD-020359 | `active` | IM业务管控License（功能层） |
| `LKV3G5RDSC01` | 码率差异化 (82209784) | GWFD-110301 | `active` | 终端OS差异化License（功能层） |
| `LKV3G5WOFR01` | FPI标记 (82200DHE) | GWFD-110331 | `active` | FPI无线调度标记License（功能层） |
| `LKV3G5WOCR01` | 小区负荷 (82200DHW) | GWFD-110332 | `active` | 小区负荷感知License（功能层） |

### 3.2 UNC侧License（8个）

| `license_id` | `license_name` | 对应Feature | `status` | 说明 |
|---------------|----------------|-------------|----------|------|
| `LKV3W9SPCC11` | PCC基本功能 (82207979) | WSFD-109101 | `active` | UNC PCC框架License（含SMF/PGW-C和AMF，基础层） |
| `LKV3TCBSA01` | BWM(UNC) (82200CQU) | WSFD-211005 | `active` | UNC BWM规则管理License（功能层） |
| `LKV3W9PCBT12` | 会话级FUP(UNC) (82207980) | WSFD-109104 | `active` | UNC会话级FUP License（功能层） |
| `LKV2FUPSAT01` | 业务级FUP(UNC) (82200BNU) | WSFD-211009 | `active` | UNC业务级FUP License（功能层） |
| `LKV3W9STQE11` | QoS保证(UNC) (82208819) | WSFD-109107 | `active` | UNC QoS保证License（功能层） |
| `LKV2BADCF01` | ADC(UNC) (82200BNK) | WSFD-109102 | `active` | UNC ADC License（功能层） |
| `LKV3WPWULI11` | 接入点策略(UNC) (82209475) | WSFD-109108 | `active` | UNC接入点策略License（功能层） |
| `LKV3W9WOCR11` | 小区负荷(UNC) (82209457) | WSFD-211101 | `active` | UNC小区负荷License（功能层） |

### 3.3 License依赖链

```
基础License（必须先开启）
├── UDG: LKV3G5SABS01 (SA-Basic) + LKV3G5PCCB01 (PCC) + LKV3G5SSDUC1 (SA特征库管控)
└── UNC: LKV3W9SPCC11 (PCC SMF/PGW-C)
        │
        ▼
功能License（在基础License之上叠加）
├── UDG: 13个功能License（BWM/Shaping/智能Shaping/会话FUP/业务FUP/QoS/ADC/异常检测/IM/码率/FPI/小区负荷/视频解耦）
└── UNC: 7个功能License（BWM/会话FUP/业务FUP/QoS/ADC/接入点/小区负荷）
```

---

## 4. License → Feature 映射（requires_license边，24条）

> 每个Feature恰好对应1个主要License。License通过 `SET LICENSESWITCH` 命令开启。

| Feature | `requires_license` | 产品 |
|---------|-------------------|------|
| GWFD-110101 | `LKV3G5SABS01` | UDG |
| GWFD-111600 | `LKV3G5SSDUC1` | UDG |
| GWFD-020351 | `LKV3G5PCCB01` | UDG |
| GWFD-110311 | `LKV3G5TCSA01` | UDG |
| GWFD-020354 | `LKV3G5SBTS01` | UDG |
| GWFD-110313 | `LKV3G5FSHP01` | UDG |
| GWFD-020353 | `LKV3G5PCBT01` | UDG |
| GWFD-110312 | `LKV3G5FPBS01` | UDG |
| GWFD-020358 | `LKV3G5STQE01` | UDG |
| GWFD-110302 | `LKV3G5SCUD01` | UDG |
| GWFD-020357 | `LKV3G5ADCF01` | UDG |
| GWFD-020305 | `LKV3G5ADTD01` | UDG |
| GWFD-020359 | `LKV3G5ITSR01` | UDG |
| GWFD-110301 | `LKV3G5RDSC01` | UDG |
| GWFD-110331 | `LKV3G5WOFR01` | UDG |
| GWFD-110332 | `LKV3G5WOCR01` | UDG |
| WSFD-109101 | `LKV3W9SPCC11` | UNC |
| WSFD-211005 | `LKV3TCBSA01` | UNC |
| WSFD-109104 | `LKV3W9PCBT12` | UNC |
| WSFD-211009 | `LKV2FUPSAT01` | UNC |
| WSFD-109107 | `LKV3W9STQE11` | UNC |
| WSFD-109102 | `LKV2BADCF01` | UNC |
| WSFD-109108 | `LKV3WPWULI11` | UNC |
| WSFD-211101 | `LKV3W9WOCR11` | UNC |

---

## 5. FeatureRule（5条）

| `rule_id` | 所属Feature | `rule_name` | `rule_type` | `rule_logic` | `severity` |
|-----------|------------|-------------|-------------|--------------|------------|
| `FR-BW-01` | GWFD-110311（BWM） | BWM三级控制层级不叠加 | `restriction_rule` | 用户级/组级/全局级 BWM 控制不可在同一对象上叠加；同一业务流只能匹配一个层级的 BWMRULE。三级控制的对象类型不同（SUBSCRIBER_SPECIFIC vs GROUP_SPECIFIC vs GLOBAL），不可混用 | critical |
| `FR-BW-02` | GWFD-110313（智能Shaping） | 智能Shaping依赖链 | `dependency_rule` | 智能Shaping需 BWM(LKV3G5TCSA01) + Shaping(LKV3G5SBTS01) 双License同时开启，缺一功能不可用 | critical |
| `FR-BW-03` | WSFD-211005（BWM UNC） | POLICYTYPE=BWM仅UNC侧 | `naming_rule` | `ADD RULE(POLICYTYPE=BWM)` 是 UNC 侧独有策略标识；UDG 侧使用 BWM 专有命令体系（BWMSERVICE/BWMCONTROLLER/BWMUSERGROUP/BWMRULE），不使用POLICYTYPE=BWM。侧别配置错误将导致规则无法生效 | warning |
| `FR-BW-04` | GWFD-110312（业务FUP） | 业务FUP依赖SA识别 | `dependency_rule` | 业务级FUP需SA识别才能per SVC/per APP独立累计；会话级FUP(GWFD-020353)不依赖SA。无SA识别时业务级FUP不生效 | warning |
| `FR-BW-05` | GWFD-020358（QoS保证） | QoS保证URR模式 | `validation_rule` | QoS保证的URR.USAGERPTMODE必须为QOS（区别于FUP的ONLINE/MONITORINGKEY）。模式错误将导致QoS事件无法上报，专载不建立 | critical |

---

## 6. FeatureTaskOrderEdge（核心Feature的Task展开顺序）

> **Schema参考**：Schema §11.4 FeatureTaskOrderEdge。详细Task定义见 `03-task-layer.md`。
> **关系类型**：本场景所有FTOE均为 `sequential`（顺序执行），因带宽控制配置链存在严格前后依赖。
> **说明**：SET REFRESHSRV 等内联命令步骤归入其所属Task（如T-006），不单独建边。
> **ID前缀**：FTOE-BW-，顺序编号。

### 6.1 GWFD-110311 BWM（UDG侧配置链，8条边）

| `edge_id` | `owner_ref_type` | `owner_ref` | `from_task_ref` | `to_task_ref` | `relation_type` | `source_evidence_ids` |
|-----------|-----------------|-------------|-----------------|---------------|-----------------|----------------------|
| `FTOE-BW-001` | `Feature` | `GWFD-110311` | `T-007` | `T-008` | `sequential` | `EV-FK-04, EV-CA-01` |
| `FTOE-BW-002` | `Feature` | `GWFD-110311` | `T-008` | `T-101` | `sequential` | `EV-FK-04, EV-CA-01` |
| `FTOE-BW-003` | `Feature` | `GWFD-110311` | `T-101` | `T-102` | `sequential` | `EV-FK-04, EV-CA-01` |
| `FTOE-BW-004` | `Feature` | `GWFD-110311` | `T-102` | `T-103` | `sequential` | `EV-FK-04, EV-CA-01` |
| `FTOE-BW-005` | `Feature` | `GWFD-110311` | `T-103` | `T-104` | `sequential` | `EV-FK-04, EV-CA-01` |
| `FTOE-BW-006` | `Feature` | `GWFD-110311` | `T-104` | `T-105` | `sequential` | `EV-FK-04, EV-CA-01` |
| `FTOE-BW-007` | `Feature` | `GWFD-110311` | `T-105` | `T-106` | `sequential` | `EV-FK-04, EV-CA-01` |
| `FTOE-BW-008` | `Feature` | `GWFD-110311` | `T-106` | `T-006` | `sequential` | `EV-FK-04, EV-CA-01` |

> **Task说明**：T-007=License开启, T-008=SA特征库加载, T-101=规划BWM策略, T-102=ADD BWMSERVICE, T-103=ADD BWMCONTROLLER, T-104=ADD BWMUSERGROUP, T-105=ADD BWMRULE, T-106=APN绑定(APNBINDBWMUSRG), T-006=SET REFRESHSRV

### 6.2 GWFD-020353 会话级FUP（UDG侧配置链，5条边）

| `edge_id` | `owner_ref_type` | `owner_ref` | `from_task_ref` | `to_task_ref` | `relation_type` | `source_evidence_ids` |
|-----------|-----------------|-------------|-----------------|---------------|-----------------|----------------------|
| `FTOE-BW-009` | `Feature` | `GWFD-020353` | `T-007` | `T-201` | `sequential` | `EV-FK-07, EV-CA-01` |
| `FTOE-BW-010` | `Feature` | `GWFD-020353` | `T-201` | `T-202` | `sequential` | `EV-FK-07, EV-CA-01` |
| `FTOE-BW-011` | `Feature` | `GWFD-020353` | `T-202` | `T-203` | `sequential` | `EV-FK-07, EV-CA-01` |
| `FTOE-BW-012` | `Feature` | `GWFD-020353` | `T-203` | `T-204` | `sequential` | `EV-FK-07, EV-CA-01` |
| `FTOE-BW-013` | `Feature` | `GWFD-020353` | `T-204` | `T-006` | `sequential` | `EV-FK-07, EV-CA-01` |

> **Task说明**：T-007=License开启, T-201=FUP策略规划, T-202=ADD URR, T-203=ADD URRGROUP, T-204=ADD PCCPOLICYGRP, T-006=SET REFRESHSRV

### 6.3 WSFD-211005 BWM（UNC侧配置链，4条边）

| `edge_id` | `owner_ref_type` | `owner_ref` | `from_task_ref` | `to_task_ref` | `relation_type` | `source_evidence_ids` |
|-----------|-----------------|-------------|-----------------|---------------|-----------------|----------------------|
| `FTOE-BW-014` | `Feature` | `WSFD-211005` | `T-007` | `T-501` | `sequential` | `EV-FK-19, EV-CA-01` |
| `FTOE-BW-015` | `Feature` | `WSFD-211005` | `T-501` | `T-003` | `sequential` | `EV-FK-19, EV-CA-01` |
| `FTOE-BW-016` | `Feature` | `WSFD-211005` | `T-003` | `T-004` | `sequential` | `EV-FK-19, EV-CA-01` |
| `FTOE-BW-017` | `Feature` | `WSFD-211005` | `T-004` | `T-005` | `sequential` | `EV-FK-19, EV-CA-01` |

> **Task说明**：T-007=License开启, T-501=PCRF组配置, T-003=ADD RULE(POLICYTYPE=BWM), T-004=ADD USERPROFILE+RULEBINDING, T-005=ADD USRPROFGROUP+UPBINDUPG+APNUSRPROFG绑定链

### 6.4 GWFD-020358 QoS保证（UDG侧配置链，5条边）

| `edge_id` | `owner_ref_type` | `owner_ref` | `from_task_ref` | `to_task_ref` | `relation_type` | `source_evidence_ids` |
|-----------|-----------------|-------------|-----------------|---------------|-----------------|----------------------|
| `FTOE-BW-018` | `Feature` | `GWFD-020358` | `T-007` | `T-008` | `sequential` | `EV-FK-10, EV-CA-01` |
| `FTOE-BW-019` | `Feature` | `GWFD-020358` | `T-008` | `T-301` | `sequential` | `EV-FK-10, EV-CA-01` |
| `FTOE-BW-020` | `Feature` | `GWFD-020358` | `T-301` | `T-302` | `sequential` | `EV-FK-10, EV-CA-01` |
| `FTOE-BW-021` | `Feature` | `GWFD-020358` | `T-302` | `T-303` | `sequential` | `EV-FK-10, EV-CA-01` |
| `FTOE-BW-022` | `Feature` | `GWFD-020358` | `T-303` | `T-006` | `sequential` | `EV-FK-10, EV-CA-01` |

> **Task说明**：T-007=License开启, T-008=SA特征库加载, T-301=规划QoS策略, T-302=ADD URR(USAGERPTMODE=QOS), T-303=ADD RULE+FILTER+FLOWFILTER绑定, T-006=SET REFRESHSRV

### 6.5 GWFD-110313 智能Shaping（UDG侧配置链，3条边）

| `edge_id` | `owner_ref_type` | `owner_ref` | `from_task_ref` | `to_task_ref` | `relation_type` | `source_evidence_ids` |
|-----------|-----------------|-------------|-----------------|---------------|-----------------|----------------------|
| `FTOE-BW-023` | `Feature` | `GWFD-110313` | `T-007` | `T-103` | `sequential` | `EV-FK-06, EV-CA-01` |
| `FTOE-BW-024` | `Feature` | `GWFD-110313` | `T-103` | `T-107` | `sequential` | `EV-FK-06, EV-CA-01` |
| `FTOE-BW-025` | `Feature` | `GWFD-110313` | `T-107` | `T-006` | `sequential` | `EV-FK-06, EV-CA-01` |

> **Task说明**：T-007=双License开启(BWM+Shaping), T-103=ADD BWMCONTROLLER(CTRLTYPE=SHAPING, WORKMODE=AUTO), T-107=ADD BCSRVLEVELPLY(ServiceLevel策略), T-006=SET REFRESHSRV

> **FTOE统计**：5个核心Feature x 25条顺序边。License开启(T-007)为所有链路起点，SET REFRESHSRV(T-006)或APN绑定链(T-005)为终点。

---

## 7. 关系边汇总

| 关系类型 | 数量 | 说明 |
|---------|------|------|
| `depends_on` | 26 | UDG侧20 + UNC侧6 |
| `requires_license` | 24 | UDG 16 + UNC 8（1:1映射） |
| `constrained_by`（FeatureRule） | 5 | FR-BW-01~FR-BW-05 |
| `task_order`（FeatureTaskOrderEdge） | 25 | FTOE-BW-001~025（5个核心Feature） |
| `decomposes_to`（Feature→ConfigTask） | 24 | 见`05-cross-layer-mapping.md` |
| **特性层对象总计** | **24 Feature + 24 License + 5 FeatureRule + 25 FTOE** | — |

---

## 8. 与计费场景特性图谱的对比

| 维度 | 计费场景 | 带宽控制场景 |
|------|---------|------------|
| Feature数量 | 14（UDG 9 + UNC 5） | 24（UDG 16 + UNC 8） |
| 核心特性族 | 计费三件套（URR/URRGROUP/PCCPOLICYGRP）+ 协议栈（Ga/Gy/N40） | BWM三级控制体系（BWMSERVICE/BWMCONTROLLER/BWMUSERGROUP/BWMRULE） |
| 独有Feature | GWFD-010171/010173/020300/020302/020303/020306, WSFD-011201/011202/011206/109002 | GWFD-110311/110312/110313/020354/020357/020358/020359/110301/110302/110331/110332/020305, WSFD-211005/109104/211009/109107/109102/109108/211101 |
| 共享Feature | GWFD-110101(SA-Basic), GWFD-020351/WSFD-109101(PCC) | 同左 |
| License数量 | 11（4个无需License） | 24（全部需License，UDG 16 + UNC 8） |
| 依赖链核心 | SA-Basic→PCC→内容计费→[在线/离线/融合/计量增强] | SA-Basic→PCC→BWM→[Shaping/FUP/QoS/ADC/无线优化] |
| 特性辐射中心 | SA-Basic（8个依赖）+ PCC（全依赖） | SA-Basic（12个依赖）+ PCC（22/24依赖） |
| 独有FeatureRule | 9条（计费三件套约束+RGAPPLIED+QCT优先级+事件计费点） | 5条（BWM层级+智能Shaping依赖+POLICYTYPE侧别+FUP SA依赖+URR模式） |
| UDG-UNC配对 | 6对 | 8对 |
| Task链复杂度 | 52条FTOE（5个核心Feature） | 25条FTOE（5个核心Feature） |

> 两场景共享SA-Basic和PCC框架基础。计费场景在内容计费基础上向"计量方式+计费方式"两个维度扩展；带宽场景在PCC基础上向"控制机制"维度扩展，覆盖限速/整形/GBR保证/FUP降速/DSCP标记/码率差异化/位置差异化等多种控制方式。

---

## 9. 对象计数汇总

| 对象类型 | 数量 | 编号范围 |
|---------|------|---------|
| Feature | 24 | GWFD-110101/020351/110311/110312/110313/020353/020354/020358/020357/020305/020359/110301/110302/110331/110332/111600 + WSFD-109101/109102/109104/109107/109108/211005/211009/211101 |
| License | 24 | UDG: LKV3G5*(15) + LKV3G5SSDUC1(1); UNC: LKV3W9*(4) + LKV2*(2) + LKV3TC*(1) + LKV3WP*(1) |
| FeatureRule | 5 | FR-BW-01~FR-BW-05 |
| depends_on边 | 26 | UDG 20 + UNC 6 |
| FTOE边 | 25 | FTOE-BW-001~FTOE-BW-025 |
| **特性层对象总计** | **104** | — |

---

> 本文件为带宽控制场景三层图谱第2层。第1层业务图谱见 `01-business-graph.md`，第3层任务原子层、第4层命令图谱、第5层跨层映射、第6层证据索引见同目录其他文件。
