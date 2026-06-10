# 计费场景三层图谱 · 第1层：业务图谱

> **文件定位**：`three-layer-graph/01-business-graph.md`
> **Schema参考**：`三层图谱Schema-最终版-v0.1.md` §8 业务图谱
> **本体参考**：`三层图谱本体标准定义.md`
> **作用**：实例化计费场景业务层对象（BD/NS/CS/DP/BR/SO）及其关系边
> **与现有 `新三层图谱/01-计费场景-业务图谱-新schema-v0.1.md` 的关系**：本文件为按带宽场景7文件结构重构的完整版，CS从1个拆分为7个方案闭包，补充协议知识SemanticObject，不修改原文件。

---

## 0. 适用定义与来源

### 0.1 根定义
- `三层图谱本体标准定义.md`
- `三层图谱Schema-最终版-v0.1.md`

### 0.2 计费场景知识来源
- `business-graph/计费场景/01计费场景业务图谱.md`（757行，旧业务图谱）
- `business-graph/计费场景/计费场景统一知识库.md`（3232行，统一知识库 K001-K261）
- `business-graph/计费场景/SKILL/knowledge/计费场景业务图谱.md`（624行）
- `business-graph/计费场景/SKILL/knowledge/业务感知业务图谱.md`（1628行，业务感知全景）
- `business-graph/计费场景/SKILL/knowledge/协议知识-Ga-Gy-DCC.md`（680行）
- `business-graph/计费场景/SKILL/knowledge/协议知识-N40-PFCP-Gx.md`（742行）
- `business-graph/计费场景/feature-knowledge/cross-feature-analysis.md`（580行）

---

## 1. BusinessDomain + NetworkScenario

### 1.1 BusinessDomain

| 字段 | 值 |
|------|---|
| `domain_id` | `BD-CH-01` |
| `domain_name` | `业务感知` |
| `domain_summary` | 在用户会话过程中，对用户的数据报文进行解析，从而区分出用户使用的不同业务，以实现策略控制和计费控制 |
| `status` | `active` |
| `source_evidence_ids` | `EV-KB-001`, `EV-BSA-全景`, `EV-FK-SA-Basic` |

> **共享说明**：BD-CH-01 与带宽场景 BD-BW-01 共享同一根对象 `业务感知`。计费、带宽控制、访问限制三场景均挂在此域下。

### 1.2 NetworkScenario

| 字段 | 值 |
|------|---|
| `scenario_id` | `NS-CH-01` |
| `scenario_name` | `计费场景` |
| `scenario_summary` | 对不同业务流采用不同计费方式，结合默认计费、免费业务和配额动作完成计费闭环 |
| `judgment_basis` | 用户需要按业务粒度差异化计费（离线/在线/融合），或需要按流量/时长/事件统计特定业务的使用量 |
| `typical_outcome` | 专项业务单独计费、免费业务不计费、普通业务默认计费，配额耗尽后切换到阻断或重定向 |
| `status` | `active` |
| `source_evidence_ids` | `EV-KB-001`, `EV-BS-001` |

#### 场景边界

**覆盖范围**：
- 产品：UDG（用户面）+ UNC（控制面）
- 网元：SGW-U/PGW-U/UPF（UDG）、SMF/PGW-C（UNC）
- 接口：Ga（离线）、Gy/DCC（在线）、N40/Nchf（融合）、N4/PFCP（SMF↔UPF）、Gx/N7（PCF↔SMF）
- 控制维度：业务类型（RG/SID）、计量方式（流量/时长/事件）、计费方式（离线/在线/融合）、配额动作（BLOCK/REDIRECT/FORWARD）

**不覆盖范围**（相邻场景）：
- 带宽控制场景（套餐2）：差异化限速、整形、FUP降速、GBR保证
- 访问限制场景（套餐3）：URL过滤、重定向阻断、接入控制

---

## 2. ConfigurationSolution（7个方案闭包）

> **拆分依据**：统一知识库 K004（三种计费系统对比）、K013（计费粒度分类）、K014（多维分类）、K016（组合规则）、K027（计量方式）、K037（配额耗尽动作）。
> 原 `新三层图谱` 中只有1个 DS-01 大方案，本版拆分为7个稳定方案闭包。

### 2.1 CS-CH-01 离线计费方案

| 字段 | 值 |
|------|---|
| `solution_id` | `CS-CH-01` |
| `solution_name` | `离线计费方案` |
| `solution_summary` | 通过RG标识业务，UPF侧URR累计流量/时长/事件，控制面按计费规则格式化为话单，通过Ga接口发送到CG，CG完成存储/标准化后定期上传BD域 |
| `design_intent` | 解决"按业务差异化离线计费"问题：特定业务单独RG，免费业务不计费，普通业务默认费率 |
| `core_mechanism_combo` | `RG标识(URR.RG) → URR累计(USAGERPTMODE=OFFLINE) → Ga接口/GTP' → CG(话单预处理) → BD(营帐结算)` |
| `status` | `active` |
| `source_evidence_ids` | `EV-KB-001`(K001-K004), `EV-KB-001`(K012), `EV-KB-002`(K015), `EV-BS-001` |

**scopes**: subscriber（按用户粒度计费）、subscription（PDU会话级承载计费）

**participants**:
- UDG/UPF（流量统计与URR执行，user_plane）
- UNC/SMF（话单格式化与Ga发送，control_plane）
- CG（CDR接收/预处理，external_system）
- BD（营帐结算，external_system）

**uses_feature**: GWFD-010171、GWFD-020301、WSFD-011201
**uses_semantic_object**: SO-CH-08（计费语义）、SO-CH-10（Ga/Gy协议栈）
**constrained_by**: BR-CH-01、BR-CH-05、BR-CH-06、BR-CH-07

### 2.2 CS-CH-02 在线计费方案

| 字段 | 值 |
|------|---|
| `solution_id` | `CS-CH-02` |
| `solution_name` | `在线计费方案` |
| `solution_summary` | SMF通过Gy接口/DCC协议实时向OCS申请配额，配额耗尽触发重授权或执行耗尽动作；实现实时信用控制和配额管理 |
| `design_intent` | 解决"实时余额控制"问题：预付费用户配额耗尽即阻断或重定向 |
| `core_mechanism_combo` | `Gy接口/DCC协议 → CCR-I/U/T三阶段 → OCS配额分配(GSU) → 实时扣费 → 配额耗尽触发Final-Unit-Action(BLOCK/REDIRECT/RESTRICT)` |
| `status` | `active` |
| `source_evidence_ids` | `EV-KB-001`(K028-K048), `EV-KB-002`(K015), `EV-KB-001`(K037, K043-K045) |

**scopes**: subscriber（预付费用户）、subscription（配额粒度）

**participants**:
- UNC/SMF（CTF角色，DCC客户端，control_plane）
- OCS（OCF/ABMF/RF，DCC服务器，external_system）
- UDG/UPF（UPF侧URR执行配额阈值上报，user_plane）

**uses_feature**: GWFD-020300、GWFD-020301、GWFD-020306
**uses_semantic_object**: SO-CH-09（配额语义）、SO-CH-10（Ga/Gy协议栈）
**constrained_by**: BR-CH-01、BR-CH-09

### 2.3 CS-CH-03 融合计费方案

| 字段 | 值 |
|------|---|
| `solution_id` | `CS-CH-03` |
| `solution_name` | `融合计费方案` |
| `solution_summary` | 5G SA场景下SMF通过N40/Nchf服务化接口与CHF交互，同一PDU会话中在线RG和离线RG共存，由CCT模板控制RG来源和配额闭环；CHF融合CG的CGF和OCS的ABMF+RF |
| `design_intent` | 解决"在线+离线统一"问题：同一用户部分业务在线计费、部分离线计费，数据归一避免不一致 |
| `core_mechanism_combo` | `N40/Nchf服务化接口 → ChargingData Create/Update/Release三阶段 → CCT模板(RG来源+配额阈值) → 在线RG(GSU配额)+离线RG(仅参数)共存 → CHF生成CHF-CDR` |
| `status` | `active` |
| `source_evidence_ids` | `EV-KB-001`(K001, K101-K121, K201, K202, K105) |

**scopes**: subscriber（融合计费用户）、subscription（PDU会话级）

**participants**:
- UNC/SMF（Nchf消费者，配额管理，control_plane）
- CHF（Nchf提供者，配额+话单，external_system）
- PCF（通过N7下发chargingInfo含CHF地址，control_plane）
- NRF（CHF发现，control_plane）
- UDG/UPF（PFCP URR执行，user_plane）

**uses_feature**: GWFD-010173、WSFD-011206、GWFD-020301
**uses_semantic_object**: SO-CH-09（配额语义）、SO-CH-11（N40/PFCP协议栈）
**constrained_by**: BR-CH-01、BR-CH-10、BR-CH-11、BR-CH-12

### 2.4 CS-CH-04 内容计费基础方案

| 字段 | 值 |
|------|---|
| `solution_id` | `CS-CH-04` |
| `solution_name` | `内容计费基础方案` |
| `solution_summary` | 通过SA识别业务类型（L34或L7），将匹配条件与PCC计费链绑定，按RG实现不同业务差异化费率；每条业务一套独立的URR→URRGROUP→PCCPOLICYGRP三件套 |
| `design_intent` | 解决"按业务差异化计费"问题：视频业务RG=100、游戏业务RG=200、默认RG=999 |
| `core_mechanism_combo` | `SA识别(FILTER/L7FILTER/PROTBINDFLOWF) → FLOWFILTER组合匹配 → RULE(POLICYTYPE=PCC)优先级裁决 → PCCPOLICYGRP→URRGROUP→URR(RG标识) → 计费链执行` |
| `status` | `active` |
| `source_evidence_ids` | `EV-KB-001`(K013, K020-K022, K136-K146), `EV-BS-001`, `EV-KB-002`(K214) |

**scopes**: service_selection（按业务类型差异化计费）、subscriber（用户级策略绑定）

**participants**:
- UDG/UPF（业务识别与计费执行，user_plane）
- UNC/SMF（规则下发与配额管理，control_plane）

**uses_feature**: GWFD-110101、GWFD-020301、GWFD-020351、WSFD-109101、WSFD-109002
**uses_semantic_object**: SO-CH-01、SO-CH-03、SO-CH-04、SO-CH-05、SO-CH-08
**constrained_by**: BR-CH-02、BR-CH-03、BR-CH-04

### 2.5 CS-CH-05 计量形态增强方案

| 字段 | 值 |
|------|---|
| `solution_id` | `CS-CH-05` |
| `solution_name` | `计量形态增强方案` |
| `solution_summary` | 在内容计费基础上，按业务特性选择流量(VOLUME)、时长(DURATION)或事件(EVENT)计量方式；时长计费支持CTP/QCT两种模式，事件计费仅限在线SCUR |
| `design_intent` | 解决"按资源类型差异化计量"问题：视频按流量、语音按时长、短信按事件 |
| `core_mechanism_combo` | `URR.METERINGTYPE(VOLUME/DURATION/EVENT) → QCT(配额空耗时间,CTP/QCT两种模式) → 在线:GSU携带CC-Time/CC-Total-Octets → 离线:仅累计上报` |
| `status` | `active` |
| `source_evidence_ids` | `EV-KB-001`(K014, K024, K126-K128, K140), `EV-BS-001` |

**scopes**: service_selection（按业务类型选计量方式）

**participants**:
- UDG/UPF（Measurement执行，user_plane）
- UNC/SMF（Metering参数下发，control_plane）

**uses_feature**: GWFD-020301、GWFD-020302、GWFD-020303、GWFD-020306
**uses_semantic_object**: SO-CH-08（计费语义）、SO-CH-09（配额语义）
**constrained_by**: BR-CH-01（License前置门控）

### 2.6 CS-CH-06 配额降速与体验切换方案

| 字段 | 值 |
|------|---|
| `solution_id` | `CS-CH-06` |
| `solution_name` | `配额降速与体验切换方案` |
| `solution_summary` | 在线/融合计费配额耗尽后，通过高优先级降速规则覆盖原保障规则，或执行BLOCK/REDIRECT动作，实现套餐超量体验切换 |
| `design_intent` | 解决"配额耗尽后用户体验切换"问题：月套餐用完后从高速降至低速或阻断 |
| `core_mechanism_combo` | `配额耗尽触发(QUOTA_EXHAUSTED/Final-Unit-Indication) → Final-Unit-Action(BLOCK/REDIRECT/RESTRICT) 或 PCF下发高优先级降速PCC规则覆盖 → URRGRPBINDING.DFTURRGRPNAME兜底` |
| `status` | `active` |
| `source_evidence_ids` | `EV-KB-001`(K037, K110), `EV-BS-001`, `EV-KB-001`(K214) |

**scopes**: subscription（配额控制会话级）、subscriber（用户级配额）

**participants**:
- UNC/SMF（配额管理与耗尽触发，control_plane）
- OCS/CHF（配额分配与Final-Unit-Action下发，external_system）
- UDG/UPF（降速执行或阻断执行，user_plane）

**uses_feature**: GWFD-020300、GWFD-010173、WSFD-011206
**uses_semantic_object**: SO-CH-06（优先级语义）、SO-CH-09（配额语义）
**constrained_by**: BR-CH-09

### 2.7 CS-CH-07 兜底默认计费方案

| 字段 | 值 |
|------|---|
| `solution_id` | `CS-CH-07` |
| `solution_name` | `兜底默认计费方案` |
| `solution_summary` | 通过DFTURRGRPNAME+DFTSIGURRGNAME双重兜底，确保未命中任何RULE的流量仍按默认费率计费；异常流量通过SIGURRGRPNAME引用异常URRGROUP单独计费 |
| `design_intent` | 解决"未匹配流量漏计费"问题：默认所有流量都有RG标识，无遗漏 |
| `core_mechanism_combo` | `USERPROFILE.DFTURRGRPNAME(默认计费URR组) + DFTSIGURRGNAME(异常信令URR组) → 未命中RULE的流量自动走默认URR组 → SET SPECTRAFURRGRP(全局特殊流量兜底)` |
| `status` | `active` |
| `source_evidence_ids` | `EV-KB-002`(K216), `EV-BS-001` |

**scopes**: subscription（UserProfile级兜底）

**participants**:
- UDG/UPF（默认URR组执行，user_plane）
- UNC/SMF（默认计费规则下发，control_plane）

**uses_feature**: GWFD-020301、GWFD-020351
**uses_semantic_object**: SO-CH-07（绑定语义）、SO-CH-08（计费语义）
**constrained_by**: BR-CH-06、BR-CH-08

---

## 3. DecisionPoint（8个）

| `decision_id` | `decision_name` | `decision_question` | `option_set` | `trigger_condition` | `impact_summary` |
|---------------|-----------------|---------------------|--------------|---------------------|------------------|
| `DP-CH-01` | 计费方式选择 | 当前计费场景采用哪种计费方式 | `["离线计费","在线计费","融合计费"]` | 进入计费场景时 | 决定URR的USAGERPTMODE、是否需要CCT模板、配额控制机制、CHF/OCS/CG交互模式；选择CS-CH-01/02/03 |
| `DP-CH-02` | 配置网元范围选择 | 本次计费配置需要覆盖哪些网元 | `["UPF+SMF","UPF only","SMF only"]` | 进入计费配置生成或核查任务时 | 决定生成UPF执行链、SMF编排链，还是双侧协同链；影响跨网元一致性核查范围 |
| `DP-CH-03` | 匹配层次选择 | 业务流通过哪层匹配 | `["L34层匹配","L7-URL匹配","L7-协议匹配","L34+L7混合匹配"]` | 规划识别条件时 | 决定是否需要L7FILTER和PROTBINDFLOWF，影响配置对象链长度和Rule类型选择 |
| `DP-CH-04` | 配额耗尽动作选择 | 在线/融合计费配额耗尽后如何处理 | `["BLOCK","REDIRECT","FORWARD"]` | 在线/融合计费配额耗尽 | 决定是否配置QUOTAEXHAUSTACT/REDIRECT或放行；影响用户体验切换路径 |
| `DP-CH-05` | 计费粒度选择 | 计费策略作用于哪个粒度 | `["会话级(普通计费)","业务级(内容计费)","QoS flow级(漫游计费)"]` | 确定计费方式后 | 决定是否需要SA识别和RG差异化；影响URR绑定方式和Feature选择 |
| `DP-CH-06` | 计量方式选择 | 业务使用量按什么维度计量 | `["VOLUME(流量)","DURATION(时长)","EVENT(事件)"]` | 确定计费粒度后 | 决定URR.METERINGTYPE参数和Feature选择(GWFD-020302/020303/020306)；事件计费仅限在线SCUR |
| `DP-CH-07` | 兜底策略选择 | 未命中规则流量如何计费 | `["默认URR组(DFTURRGRPNAME)","异常费率(SIGURRGRPNAME)","SPECTRAFURRGRP全局兜底"]` | 规划兜底策略时 | 决定DFTURRGRPNAME和DFTSIGURRGNAME绑定方案；影响计费完整性 |
| `DP-CH-08` | 跨网元一致性策略 | CP和UP参数如何对齐 | `["双产品协同(UPF+SMF)","仅UPF本地规则","SMF动态下发"]` | 双产品部署或动态PCC场景 | 决定配置路径（预定义/动态/本地规则）、USERPROFILE/RULENAME/URRID跨侧一致性要求 |

---

## 4. BusinessRule（12条）

| `rule_id` | `rule_name` | `rule_type` | `rule_logic` | `violation_effect` |
|-----------|-------------|-------------|--------------|---------------------|
| `BR-CH-01` | SA基础License开启断言 | `scope_rule` | LKV3G5SABS01 + LKV3G5BCBC01 + LKV3G5PCCB01必须为ENABLE | 业务感知计费能力不可用 |
| `BR-CH-02` | 配置链逐层一致性校验 | `acceptance_rule` | RULEBINDING→RULE→PCCPOLICYGRP→URRGROUP→URR→FLOWFILTER→FILTER各层名称、绑定关系与规划值一致 | 配置链断裂导致计费不生效 |
| `BR-CH-03` | PFCP Usage Report一致性校验 | `acceptance_rule` | Usage Report中URR ID与UPF配置一致；UR-SEQN唯一 | 计费流量无法正确关联和上报 |
| `BR-CH-04` | CP/UP URR一致性诊断 | `diagnosis_rule` | SMF侧URR与UPF侧URR的URRID、RG、USAGERPTMODE、METERINGTYPE必须一致 | ALM-81026/81054告警，计费异常 |
| `BR-CH-05` | URRID全局唯一约束 | `scope_rule` | URRID在所有URR对象中唯一 | PFCP Session Report无法关联 |
| `BR-CH-06` | 默认URR组必须配置 | `design_rule` | DFTURRGRPNAME和DFTSIGURRGNAME必须同时配置 | 未命中RULE的流量不会计费 |
| `BR-CH-07` | RG值跨侧一致性约束 | `design_rule` | UDG.ADD URR.RG = UNC.ADD URR.RG | 报表与实际计费不一致 |
| `BR-CH-08` | REFRESHSRV时序约束 | `runtime_check_rule` | REFRESHSRV必须在所有ADD/SET完成后最后执行；PROTBINDFLOWF配置后需等待60秒再执行REFRESHSRV | 部分配置不生效 |
| `BR-CH-09` | 配额降速优先级覆盖 | `design_rule` | 在线配额耗尽后的降速规则必须使用最高优先级，且覆盖原保障规则的匹配范围 | 部分流量降速不彻底 |
| `BR-CH-10` | SMF融合计费三联前置约束 | `scope_rule` | 融合计费需满足CHGMODE=NchfMode、CHARGECTRL或USRPROFCHARGE/APNCHARGECTRL使能、CHFINIT=SENDREQ三条件 | 不发送Initial或Initial不携带预期RG |
| `BR-CH-11` | PROTBINDFLOWF协议匹配约束 | `selection_rule` | PROTOCOLNAME必须与目标网站实际协议一致（https网站必须配https）；执行后60s才生效 | L7匹配失败，流量不会被识别为指定业务 |
| `BR-CH-12` | License前置门控 | `scope_rule` | 内容计费需UDG侧LKV3G5BCBC01+UNC侧LKV3W9BCC12双License同时开启；融合计费需WSFD-011206 License | 配置命令成功但功能不生效，难以排查 |

> **rule_type说明**：与带宽场景对齐Schema标准枚举。`scope_rule`=范围约束，`acceptance_rule`=验收规则，`design_rule`=设计规则，`diagnosis_rule`=诊断规则，`selection_rule`=选择规则。

---

## 5. SemanticObject（12个）

> **协议知识补强**：本版新增 SO-CH-10（Ga/Gy/DCC协议栈）和 SO-CH-11（N40/PFCP/Gx协议栈），确保1,422行协议知识不丢失。

| `semantic_object_id` | `semantic_object_name` | `semantic_summary` | `realized_by` | `source_evidence_ids` |
|----------------------|------------------------|--------------------|--------------|-----------------------|
| `SO-CH-01` | 报文解析 | L34协议解析和L7 URL解析，是计费匹配的前置能力 | FILTER, L7FILTER | —（批次3 U-M-14补） |
| `SO-CH-02` | 协议识别 | 识别协议/应用（如http/https/IM协议组），用于计费分流 | PROTBINDFLOWF | —（批次3 U-M-14补） |
| `SO-CH-03` | 过滤条件 | 将业务描述翻译为可匹配的FILTER/FLOWFILTER/FLOWFILTERGRP组合 | FILTER, FLOWFILTER, FLOWFILTERGRP, FLTBINDFLOWF | —（批次3 U-M-14补） |
| `SO-CH-04` | 规则语义 | 将匹配条件与计费动作绑定为RULE，计费场景POLICYTYPE固定为PCC | RULE(POLICYTYPE=PCC) | —（批次3 U-M-14补） |
| `SO-CH-05` | 策略语义 | 计费场景固定为PCC策略类型，封装URRGROUP为可被RULE引用的策略组 | PCCPOLICYGRP | —（批次3 U-M-14补） |
| `SO-CH-06` | 优先级语义 | 多规则同时命中时按PRIORITY裁决（越小越高），特定业务优先于兜底 | RULE.PRIORITY | —（批次3 U-M-14补） |
| `SO-CH-07` | 绑定语义 | UserProfile承载规则绑定(RULEBINDING)和默认计费组(URRGRPBINDING) | USERPROFILE, RULEBINDING, URRGRPBINDING | —（批次3 U-M-14补） |
| `SO-CH-08` | 计费语义 | 差异化计费(RG)、免费业务(FREE RG)、默认计费(兜底)；核心三件套URR→URRGROUP→PCCPOLICYGRP | URR, URRGROUP, PCCPOLICYGRP | —（批次3 U-M-14补） |
| `SO-CH-09` | 配额语义 | 在线/融合计费的配额控制(GSU/Requested-Unit)、阈值触发和耗尽动作(Final-Unit-Action) | CCT, QUOTAEXHAUSTACT, DCCTEMPLATE | —（批次3 U-M-14补） |
| `SO-CH-10` | 计费协议栈-Ga/Gy ★ | Ga接口(离线,GTP')、Gy接口(在线,DCC/Diameter)、DCC会话(CCR-I/U/T)、MSCC多业务信用控制 | CG配置对象, OCS配置对象, DIAMCONNGRP | `EV-PK-Ga-Gy-DCC` |
| `SO-CH-11` | 计费协议栈-N40/PFCP ★ | N40接口(融合,Nchf/HTTP2)、PFCP协议(N4,Usage Report)、Gx接口(4G,PCRF↔SMF) | HTTPLEGRP/HTTPLE/SBIAPLE, TNFINS/TNFGRP, SELECTCHFGBYCC, PFCP Session Report | `EV-PK-N40-PFCP-Gx` |
| `SO-CH-12` | 核查与诊断语义 | 配置链逐层LST回查、PFCP Usage Report验证、EMS_CtfErrorRpt信令跟踪、告警诊断(ALM-81026/81054/100530) | LST全链路命令集, PFCP Session Report, EMS_CtfErrorRpt | —（批次3 U-M-14补） |

> ★ 为本版新增协议知识映射对象，确保协议层知识完整入图谱。

---

## 6. Scope（子对象，5个）

| `scope_name` | `scope_type` | `scope_summary` | 关联方案 |
|--------------|--------------|-----------------|----------|
| 用户级范围 | `subscriber` | 计费策略按用户粒度生效 | CS-CH-01~07 |
| APN/DNN范围 | `access` | 计费策略按接入点或数据网名称生效 | CS-CH-01~04 |
| UserProfile承载范围 | `subscription` | 承载规则绑定和默认计费组，是计费策略的最终生效边界 | CS-CH-04, CS-CH-07 |
| 业务选择范围 | `service_selection` | 按业务类型(RG/SID)差异化计费 | CS-CH-04, CS-CH-05 |
| 用户档案 | `user_profile` | UserProfile作为计费策略容器，承载CC属性绑定 | CS-CH-03, CS-CH-07 |

---

## 7. Participant（子对象，10个）

| `participant_name` | `participant_type` | `plane_or_side` | `responsibility_summary` | 关联方案 |
|--------------------|--------------------|-----------------|--------------------------|----------|
| SMF | `network_function` | `control_plane` | 编排计费策略、与CHF/OCS交互、下发计费规则到UPF、配额管理 | CS-CH-01~07 |
| UPF | `network_function` | `user_plane` | 业务识别、流量统计、执行计费规则、上报Usage Report | CS-CH-01~07 |
| CHF | `external_system` | `external` | 融合计费服务提供者：配额管理、批价扣费、CHF-CDR生成、重授权触发 | CS-CH-03, CS-CH-06 |
| OCS | `external_system` | `external` | 在线计费系统：实时余额管理、配额分配、信用控制 | CS-CH-02, CS-CH-06 |
| CG | `external_system` | `external` | 离线计费网关：CDR接收/预处理/持久存储/Bx上传 | CS-CH-01 |
| PCF | `network_function` | `control_plane` | 通过N7/Gx下发计费策略(chargingInfo)、动态PCC规则、CHF地址 | CS-CH-03, CS-CH-04 |
| UE/用户 | `endpoint` | `terminal_side` | 发起会话与业务访问，产生待计费业务流 | CS-CH-01~07 |
| UDM | `network_function` | `control_plane` | 通过CC计费特性传递签约数据到SMF | CS-CH-03 |
| NRF | `network_function` | `control_plane` | NF注册/发现；SMF通过NRF发现CHF | CS-CH-03 |
| BD | `external_system` | `external` | 运营商计费营帐系统：最终话单结算 | CS-CH-01 |

---

## 8. 业务图谱关系边

### 8.1 层级包含

| 起点 | 关系 | 终点 |
|------|------|------|
| `BD-CH-01` | `contains` | `NS-CH-01` |
| `NS-CH-01` | `instantiated_as` | `CS-CH-01` ~ `CS-CH-07` |

### 8.2 方案使用特性（uses_feature，共22条边）

| 起点 | 关系 | 终点 |
|------|------|------|
| `CS-CH-01` | `uses_feature` | `GWFD-010171`, `GWFD-020301`, `WSFD-011201` |
| `CS-CH-02` | `uses_feature` | `GWFD-020300`, `GWFD-020301`, `GWFD-020306` |
| `CS-CH-03` | `uses_feature` | `GWFD-010173`, `WSFD-011206`, `GWFD-020301` |
| `CS-CH-04` | `uses_feature` | `GWFD-110101`, `GWFD-020301`, `GWFD-020351`, `WSFD-109101`, `WSFD-109002` |
| `CS-CH-05` | `uses_feature` | `GWFD-020301`, `GWFD-020302`, `GWFD-020303`, `GWFD-020306` |
| `CS-CH-06` | `uses_feature` | `GWFD-020300`, `GWFD-010173`, `WSFD-011206` |
| `CS-CH-07` | `uses_feature` | `GWFD-020301`, `GWFD-020351` |

### 8.3 决策点归属（has_decision）

| 起点 | 关系 | 终点 |
|------|------|------|
| `NS-CH-01` | `has_decision` | `DP-CH-01`, `DP-CH-02`, `DP-CH-05` |
| `CS-CH-01` | `has_decision` | `DP-CH-07` |
| `CS-CH-02` | `has_decision` | `DP-CH-04` |
| `CS-CH-03` | `has_decision` | `DP-CH-04`, `DP-CH-08` |
| `CS-CH-04` | `has_decision` | `DP-CH-03`, `DP-CH-05` |
| `CS-CH-05` | `has_decision` | `DP-CH-06` |
| `CS-CH-06` | `has_decision` | `DP-CH-04` |
| `CS-CH-07` | `has_decision` | `DP-CH-07` |

### 8.4 业务规则约束（constrained_by）

| 起点 | 关系 | 终点 |
|------|------|------|
| `CS-CH-01` ~ `CS-CH-07` | `constrained_by` | `BR-CH-01`, `BR-CH-05`, `BR-CH-12` |
| `CS-CH-01`, `CS-CH-04` | `constrained_by` | `BR-CH-02` |
| `CS-CH-04`, `CS-CH-07` | `constrained_by` | `BR-CH-06` |
| `CS-CH-01`, `CS-CH-03`, `CS-CH-04` | `constrained_by` | `BR-CH-07` |
| `CS-CH-04`, `CS-CH-07` | `constrained_by` | `BR-CH-08` |
| `CS-CH-02`, `CS-CH-06` | `constrained_by` | `BR-CH-09` |
| `CS-CH-03` | `constrained_by` | `BR-CH-10` |
| `CS-CH-03`, `CS-CH-04` | `constrained_by` | `BR-CH-11` |

### 8.5 语义对象使用（uses_semantic_object）

| 起点 | 关系 | 终点 |
|------|------|------|
| `CS-CH-01` | `uses_semantic_object` | `SO-CH-08`, `SO-CH-10` |
| `CS-CH-02` | `uses_semantic_object` | `SO-CH-09`, `SO-CH-10` |
| `CS-CH-03` | `uses_semantic_object` | `SO-CH-09`, `SO-CH-11` |
| `CS-CH-04` | `uses_semantic_object` | `SO-CH-01`, `SO-CH-03`, `SO-CH-04`, `SO-CH-05`, `SO-CH-08` |
| `CS-CH-05` | `uses_semantic_object` | `SO-CH-08`, `SO-CH-09` |
| `CS-CH-06` | `uses_semantic_object` | `SO-CH-06`, `SO-CH-09` |
| `CS-CH-07` | `uses_semantic_object` | `SO-CH-07`, `SO-CH-08` |

### 8.6 决策点影响（selects / sets_value_pattern）

| 起点 | 关系 | 终点 | 说明 |
|------|------|------|------|
| `DP-CH-01` | `selects` | `CS-CH-01`/`CS-CH-02`/`CS-CH-03` | 计费方式选择决定方案闭包 |
| `DP-CH-03` | `sets_value_pattern` | `URR.FILTER层次` | L34→FILTER；L7→L7FILTER+PROTBINDFLOWF |
| `DP-CH-04` | `sets_value_pattern` | `QUOTAEXHAUSTACT.ACTION` | BLOCK/REDIRECT/FORWARD |
| `DP-CH-06` | `sets_value_pattern` | `URR.METERINGTYPE` | VOLUME/DURATION/EVENT |

---

## 9. 与带宽场景图谱的差异说明

| 维度 | 计费场景 | 带宽控制场景 |
|------|---------|------------|
| BusinessDomain | 共享 `业务感知`（BD-CH-01 = BD-BW-01） | 共享 `业务感知` |
| NetworkScenario | `NS-CH-01 计费场景`（独立） | `NS-BW-01 带宽控制场景`（独立） |
| ConfigurationSolution | 7个（CS-CH-01~07，按计费方式/计量/兜底分） | 7个（CS-BW-01~07，按控制机制分） |
| 核心机制 | SA识别→Rule→PCC/URR计费链→Ga/Gy/N40上报→配额闭环 | SA识别→BWM限速→CAR/Shaping/FUP/GBR |
| 独有对象族 | 计费三件套(URR/URRGROUP/PCCPOLICYGRP)、SMF融合计费对象(CCT/CHFINIT/CHARGECTRL) | BWM(BWMSERVICE/BWMCONTROLLER/BWMRULE) |
| 独有协议知识 | Ga/Gy/DCC/N40/PFCP/Gx（6个协议接口，SO-CH-10/11） | 无独立协议层 |
| DecisionPoint | 8个（DP-CH-01~08） | 8个（DP-BW-01~08） |
| BusinessRule | 12条（BR-CH-01~12） | 6条（BR-BW-01~06） |
| SemanticObject | 12个（SO-CH-01~12，含协议栈2个） | 8个（SO-BW-01~08） |

> 两场景图谱独立构建，不互相依赖；共享部分限于 `业务感知` 根对象、通用ConfigTask（流过滤、PCC规则、用户模板）、通用ConfigObject（RULE, USERPROFILE, PCCPOLICYGRP, FLOWFILTER, URR）。

---

## 10. 端到端方案链路（跨层映射依据）

### 10.1 CS-CH-01 离线计费端到端
```
SA识别(FILTER/L7FILTER) → FLOWFILTER组合 → RULE(PRIORITY裁决)
→ PCCPOLICYGRP → URRGROUP → URR(RG=offline, USAGERPTMODE=OFFLINE)
→ UPF累计流量/时长 → Ga接口/GTP' → CG(话单预处理) → Bx → BD(营帐结算)
```

### 10.2 CS-CH-02 在线计费端到端
```
SA识别 → FLOWFILTER → RULE → PCCPOLICYGRP → URRGROUP
→ URR(RG=online, USAGERPTMODE=ONLINE)
→ SMF(CTF角色) → Gy接口/DCC协议 → OCS
→ CCR-I(申请配额) → CCA-I(GSU授权配额)
→ 配额使用 → CCR-U(上报+申请新配额)
→ 配额耗尽 → Final-Unit-Action(BLOCK/REDIRECT/RESTRICT)
```

### 10.3 CS-CH-03 融合计费端到端
```
CHGMODE=NchfMode + CHARGECTRL使能 + CHFINIT=SENDREQ(三联前置)
→ CCT模板配置(RG来源/配额阈值/VT)
→ CHF选择(SELECTCHFGBYCC → TNFGRP → TNFINS)
→ SMF → N40/Nchf → CHF
→ ChargingData Create[Initial](含requestedUnit=在线, 不含=离线)
→ Response(grantedUnit + triggers + thresholds)
→ SMF → N4/PFCP → UPF(Create URR含配额)
→ UPF累计 → Usage Report → SMF → ChargingData Update → CHF
→ CHF生成CHF-CDR(在线扣费+离线记录统一)
```

### 10.4 CS-CH-06 配额降速端到端
```
在线配额使用中 → QUOTA_EXHAUSTED/VOLQU触发
→ Final-Unit-Indication → Final-Unit-Action
→ 路径A: BLOCK → QUOTAEXHAUSTACT(BLOCK) → UPF执行DISCARD
→ 路径B: REDIRECT → QUOTAEXHAUSTACT(REDIRECT) → UPF执行重定向
→ 路径C: FORWARD → 无动作, 走DFTURRGRPNAME默认费率
→ 路径D(融合): CHF Notify(REAUTHORIZATION) → SMF查询UPF用量 → 新配额下发
```

---

## 11. 对象计数汇总

| 对象类型 | 数量 | 编号范围 |
|---------|------|---------|
| BusinessDomain | 1 | BD-CH-01 |
| NetworkScenario | 1 | NS-CH-01 |
| ConfigurationSolution | 7 | CS-CH-01~07 |
| DecisionPoint | 8 | DP-CH-01~08 |
| BusinessRule | 12 | BR-CH-01~12 |
| SemanticObject | 12 | SO-CH-01~12 |
| Scope（子对象） | 5 | - |
| Participant（子对象） | 10 | - |
| **业务层对象总计** | **56** | - |

---

> 本文件为计费场景三层图谱第1层。第2层特性图谱、第3层任务原子层、第4层命令图谱、第5层跨层映射、第6层证据索引见同目录其他文件。
