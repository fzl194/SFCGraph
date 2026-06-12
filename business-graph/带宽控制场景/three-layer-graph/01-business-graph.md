# 带宽控制场景三层图谱 · 第1层：业务图谱

> **文件定位**：`three-layer-graph/01-business-graph.md`
> **Schema参考**：`三层图谱Schema-最终版-v0.1.md` §8 业务图谱
> **本体参考**：`三层图谱本体标准定义.md`
> **作用**：实例化带宽控制场景业务层对象（BD/NS/CS/DP/BR/SO）及其关系边
> **与现有旧版的关系**：本文件为按计费场景7文件结构对齐重构的完整版，CS从1个拆分为7个方案闭包，补充完整字段定义，不修改原文件。

---

## 0. 适用定义与来源

### 0.1 根定义
- `三层图谱本体标准定义.md`
- `三层图谱Schema-最终版-v0.1.md`

### 0.2 带宽控制场景知识来源
- `business-graph/带宽控制场景/cross-topic-analysis.md`（862行，32批次317份源文档综合分析）
- `business-graph/带宽控制场景/cross-feature-analysis.md`（1119行，24特性横向分析）
- `business-graph/带宽控制场景/feature-knowledge/*.md`（24个特性知识文档）
- `business-graph/带宽控制场景/topic-knowledge/Batch-*.md`（32个主题知识批次）

---

## 1. BusinessDomain + NetworkScenario

### 1.1 BusinessDomain

| 字段 | 值 |
|------|---|
| `domain_id` | `BD-BW-01` |
| `domain_name` | `业务感知` |
| `domain_summary` | 在用户会话过程中，对用户的数据报文进行解析，从而区分出用户使用的不同业务，以实现策略控制和计费控制 |
| `status` | `active` |
| `source_evidence_ids` | `EV-FK-BW-SA-Basic`, `EV-CA-02`, `EV-CA-01` |

> **共享说明**：BD-BW-01 与计费场景 BD-CH-01 共享同一根对象 `业务感知`。计费、带宽控制、访问限制三场景均挂在此域下。

### 1.2 NetworkScenario

| 字段 | 值 |
|------|---|
| `scenario_id` | `NS-BW-01` |
| `scenario_name` | `带宽控制场景` |
| `scenario_summary` | 对用户流量按业务类型、用户等级、套餐配额、应用类型、位置区域等维度进行差异化的带宽分配与限速控制 |
| `judgment_basis` | 需按业务类型/用户等级/套餐配额/应用类型/位置区域等维度进行差异化带宽分配与限速；或需对超额流量执行降速/整形/门控；或需对高价值业务执行GBR带宽保证 |
| `typical_outcome` | 实现BWM CAR限速/Shaping整形/FUP降速/GBR保证等差异化带宽管理；上下行带宽可独立控制；与无线侧调度联动优化 |
| `status` | `active` |
| `source_evidence_ids` | `EV-CA-02`, `EV-CA-01`, `EV-TK-19`, `EV-TK-18` |

#### 场景边界

**覆盖范围**：
- 产品：UDG（用户面，16特性）+ UNC（控制面，8特性）
- 网元：SGW-U/PGW-U/UPF（UDG）、SMF/PGW-C/AMF/GGSN-C（UNC）
- 接口：Gx（2/3/4G）、N7（5G）、N4（PFCP）、GTP-U扩展头
- 控制维度：套餐配额、应用类型、位置区域、用户等级、时间窗口

**不覆盖范围**（相邻场景）：
- 计费场景（套餐1）：差异化计费、免费业务、配额计费动作（由计费场景图谱承载）
- 访问限制场景（套餐3）：URL过滤、重定向阻断、接入控制（由访问限制场景图谱承载）

---

## 2. ConfigurationSolution（7个方案闭包）

> **拆分依据**：`cross-topic-analysis.md` §6.2（五大维度）+ §8.4（九场景）归纳合并，结合 `cross-feature-analysis.md` §4.4（场景组合链路）。
> 7个方案闭包按控制机制划分：BWM基础限速、FUP配额降速、GBR带宽保证、ADC应用感知、小区负荷、位置区域、无线优化标记。

### 2.1 CS-BW-01 SA-BWM带宽控制方案

| 字段 | 值 |
|------|---|
| `solution_id` | `CS-BW-01` |
| `solution_name` | `SA-BWM带宽控制方案` |
| `solution_summary` | 通过SA识别业务类型，在UDG用户面执行BWM三级控制（用户级/组级/全局级），实现基于业务感知的差异化限速 |
| `design_intent` | 解决"按业务类型差异化限速"问题：低价值业务（P2P）限速，高价值业务保障 |
| `core_mechanism_combo` | `SA识别(SVC/APP) → BWM规则匹配 → CAR令牌桶(CIR/PIR/CBS/PBS) / SHAPING整形(RATE/QUEDEPTH)` |
| `status` | `active` |
| `source_evidence_ids` | `EV-FK-BW-BWM`, `EV-FK-BW-SA-Basic`, `EV-FK-BW-PCC-UDG`, `EV-FK-BW-PCC-UNC`, `EV-FK-BW-BWM-UNC`, `EV-FK-BW-Shaping`, `EV-FK-BW-Shaping-UNC`, `EV-CA-01` |

**scopes**: subscriber（单用户特定业务限速）、service_selection（按SVC/APP分类限速）

**participants**:
- UDG/UPF（用户面执行BWM限速，user_plane）
- UNC/SMF（控制面规则下发与策略编排，control_plane）
- PCRF/PCF（策略决策源，external_system）

**uses_feature**: GWFD-110311, GWFD-110101, GWFD-020351, WSFD-109101, WSFD-211005, GWFD-020354, GWFD-110313
**uses_semantic_object**: SO-BW-01（带宽控制策略）, SO-BW-02（业务识别条件）, SO-BW-04（限速等级）
**constrained_by**: BR-BW-01, BR-BW-03, BR-BW-04, BR-BW-05, BR-BW-06

### 2.2 CS-BW-02 FUP配额降速方案

| 字段 | 值 |
|------|---|
| `solution_id` | `CS-BW-02` |
| `solution_name` | `FUP配额降速方案` |
| `solution_summary` | 通过URR累计用户流量，配额耗尽后由PCRF/PCF下发高优先级降速规则覆盖原规则，实现套餐超量降速 |
| `design_intent` | 解决"套餐配额超量后降速"问题：月套餐20GB后从100Mbps降至1Mbps |
| `core_mechanism_combo` | `URR流量累计 → 配额耗尽触发 → PCRF下发新QoS(MBR降低) / 预定义降速规则高优先级覆盖` |
| `status` | `active` |
| `source_evidence_ids` | `EV-FK-BW-FUP-UDG`, `EV-FK-BW-FUP-UNC`, `EV-FK-BW-FUP-Biz`, `EV-FK-BW-FUP-Biz-UNC`, `EV-TK-01`, `EV-TK-22`, `EV-CA-01`, `EV-CA-02` |

**scopes**: subscription（会话级FUP：整会话所有流量累计）、subscriber（用户级配额）

**participants**:
- UDG/UPF（流量计数与上报，user_plane）
- UNC/SMF（URR下发与上报转发，control_plane）
- PCRF/PCF（配额管理与降速决策，external_system）

**uses_feature**: GWFD-020353, WSFD-109104, GWFD-110312, WSFD-211009
**uses_semantic_object**: SO-BW-03（流量配额）, SO-BW-04（限速等级）
**constrained_by**: BR-BW-01, BR-BW-02, BR-BW-04, BR-BW-05, BR-BW-06

### 2.3 CS-BW-03 GBR带宽保证方案

| 字段 | 值 |
|------|---|
| `solution_id` | `CS-BW-03` |
| `solution_name` | `GBR带宽保证方案` |
| `solution_summary` | 通过SA识别高价值业务，触发专有承载/QoS Flow建立，分配专用资源保证带宽下限（GBR） |
| `design_intent` | 解决"高价值业务带宽下限保证"问题：视频/语音业务保证不低于GBR |
| `core_mechanism_combo` | `SA识别高价值业务 → URR(QOS模式)上报 → UNC发起专有承载/QoS Flow → GBR资源预留(GBR-UL/DL)` |
| `status` | `active` |
| `source_evidence_ids` | `EV-FK-BW-QoS`, `EV-FK-BW-QoS-UNC`, `EV-CA-01`, `EV-CA-02` |

**scopes**: service_selection（特定业务GBR保证）

**participants**:
- UDG/UPF（业务识别与QoS事件上报，user_plane）
- UNC/SMF（专有承载/QoS Flow建立信令，control_plane）
- RAN/AMF/MME（无线侧资源分配，access_side）

**uses_feature**: GWFD-020358, WSFD-109107
**uses_semantic_object**: SO-BW-05（QoS参数集）, SO-BW-02（业务识别条件）
**constrained_by**: BR-BW-03, BR-BW-04, BR-BW-06

### 2.4 CS-BW-04 ADC应用感知动态带宽方案

| 字段 | 值 |
|------|---|
| `solution_id` | `CS-BW-04` |
| `solution_name` | `ADC应用感知动态带宽方案` |
| `solution_summary` | 通过ADC检测应用启动/停止事件（APP_STA/APP_STO），动态切换三策略组（Normal/Start/Stop）实现应用级带宽调整，无需用户重连 |
| `design_intent` | 解决"按应用类型实时调整带宽"问题：视频APP激活时分配GBR，停止时恢复Non-GBR |
| `core_mechanism_combo` | `ADC检测(APP_STA/APP_STO) → PCF决策 → 三策略组动态切换(Normal/Start/Stop) → QoS参数变更` |
| `status` | `active` |
| `source_evidence_ids` | `EV-FK-BW-ADC`, `EV-FK-BW-ADC-UNC`, `EV-TK-27`, `EV-TK-28`, `EV-CA-02` |

**scopes**: service_selection（应用级带宽，per APP）

**participants**:
- UDG/UPF（L7 DPI引擎，应用检测，user_plane）
- UNC/SMF（事件转发与策略映射，control_plane）
- PCRF/PCF（ADC策略决策，external_system）

**uses_feature**: GWFD-020357, WSFD-109102
**uses_semantic_object**: SO-BW-06（应用检测事件）, SO-BW-05（QoS参数集）
**constrained_by**: BR-BW-01, BR-BW-04, BR-BW-06

### 2.5 CS-BW-05 小区负荷动态带宽方案

| 字段 | 值 |
|------|---|
| `solution_id` | `CS-BW-05` |
| `solution_name` | `小区负荷动态带宽方案` |
| `solution_summary` | 通过RAN上报小区负荷等级（Level 0-3），UDG转发至UNC/PCRF，PCRF下发动态带宽策略，实现拥塞时动态调整BWM |
| `design_intent` | 解决"小区拥塞时动态限速"问题：拥塞时对低优先级用户限速，保障高价值用户 |
| `core_mechanism_combo` | `RAN负荷上报 → UDG转发(GTP-U扩展头) → UNC上报PCRF → PCRF动态BWM策略下发` |
| `status` | `active` |
| `source_evidence_ids` | `EV-FK-BW-CellLoad`, `EV-FK-BW-CellLoad-UNC`, `EV-CA-01`, `EV-CA-02` |

**scopes**: access（小区级负荷感知）

**participants**:
- RAN（负荷感知与上报，access_side）
- UDG/UPF（负荷信息转发，user_plane）
- UNC/SMF（事件上报PCRF，control_plane）
- PCRF/PCF（动态策略决策，external_system）

**uses_feature**: GWFD-110332, WSFD-211101
**uses_semantic_object**: SO-BW-07（小区负荷等级）, SO-BW-01（带宽控制策略）
**constrained_by**: BR-BW-04, BR-BW-06

### 2.6 CS-BW-06 位置区域差异化带宽方案

| 字段 | 值 |
|------|---|
| `solution_id` | `CS-BW-06` |
| `solution_name` | `位置区域差异化带宽方案` |
| `solution_summary` | 通过感知用户位置变化（WiFi接入点/PLMN/漫游区域），激活预定义差异化带宽规则，实现按位置区域限速 |
| `design_intent` | 解决"按位置区域差异化限速"问题：漫游时限制最大带宽为10Mbps |
| `core_mechanism_combo` | `位置变化感知(UE_LOCAL_IP/PLMN_CH) → 预定义规则激活 → 位置差异化带宽(PIR限速)` |
| `status` | `active` |
| `source_evidence_ids` | `EV-FK-BW-APN-Policy`, `EV-TK-28`, `EV-TK-29`, `EV-CA-02` |

**scopes**: location（位置区域感知）、access（WiFi接入点）

**participants**:
- UNC/SMF（位置变化感知与规则激活，control_plane）
- PCRF/PCF（位置条件策略决策，external_system）

> 注：位置区域控制只能使用预定义规则（位置信息在SMF侧，PCF无L7识别能力）。

**uses_feature**: WSFD-109108
**uses_semantic_object**: SO-BW-08（位置区域标识）
**constrained_by**: BR-BW-01, BR-BW-04, BR-BW-06

### 2.7 CS-BW-07 无线资源优化标记方案

| 字段 | 值 |
|------|---|
| `solution_id` | `CS-BW-07` |
| `solution_name` | `无线资源优化标记方案` |
| `solution_summary` | 通过DSCP/FPI标记或终端OS差异化，影响无线侧调度优先级（非直接用户面限速），间接优化带宽体验 |
| `design_intent` | 解决"无线侧调度优化"问题：通过标记影响基站队列调度，间接提升业务带宽体验 |
| `core_mechanism_combo` | `SA识别业务 → DSCP/FPI标记 / OSTYPE差异化 → RAN调度队列优化（非UPF限速）` |
| `status` | `active` |
| `source_evidence_ids` | `EV-FK-BW-RadioOpt`, `EV-FK-BW-Video-1`, `EV-FK-BW-Video-2`, `EV-FK-BW-WirelessOpt`, `EV-CA-01` |

**scopes**: service_selection（按业务类型标记）

**participants**:
- UDG/UPF（业务识别与标记，user_plane）
- RAN/BSC（无线侧调度执行，access_side）

> 注：异常流量检测(GWFD-020305)和SA特征库管控(GWFD-111600)作为辅助能力，通过Feature依赖和BusinessRule表达，不单独建方案。

**uses_feature**: GWFD-020359, GWFD-110301, GWFD-110302, GWFD-110331
**uses_semantic_object**: SO-BW-02（业务识别条件）
**constrained_by**: BR-BW-04, BR-BW-05, BR-BW-06

---

## 3. DecisionPoint（8个）

| `decision_id` | `owner_layer` | `owner_ref_type` | `owner_ref` | `decision_name` | `decision_question` | `option_set` | `trigger_condition` | `impact_summary` | `status` | `source_evidence_ids` |
|---------------|---------------|-------------------|-------------|-----------------|---------------------|--------------|---------------------|------------------|----------|----------------------|
| `DP-BW-01` | `L1_business` | `Namespace` | `NS-BW-01` | 带宽控制机制选择 | 当前业务流应采用哪种带宽控制机制 | `["CAR限速","Shaping整形","GBR保证","FUP降速","门控阻断"]` | 进入带宽控制配置时 | 决定使用哪些CS（CS-BW-01~05）和Feature；决定BWMCONTROLLER.CTRLTYPE或QOSPROP路径 | `active` | `EV-CA-01`, `EV-CA-02` |
| `DP-BW-02` | `L1_business` | `Namespace` | `NS-BW-01` | 控制粒度选择 | 带宽控制应作用于哪个粒度 | `["会话级","业务级","用户组级","全局级"]` | 确定控制机制后 | 决定BWMRULETYPE（SUBSCRIBER_SPECIFIC/GROUP_SPECIFIC/GLOBAL）和URR绑定方式 | `active` | `EV-CA-01` |
| `DP-BW-03` | `L1_business` | `Namespace` | `NS-BW-01` | 规则类型选择 | 当前场景应使用哪种PCC规则类型 | `["动态规则","预定义规则","本地规则"]` | 确定控制粒度后 | 决定配置路径和三网元一致性要求；定向业务必须用预定义（PCF无L7能力） | `active` | `EV-CA-02`, `EV-TK-26` |
| `DP-BW-04` | `L1_business` | `Namespace` | `NS-BW-01` | 接口代际选择 | 当前部署是4G还是5G | `["Gx(4G)","N7(5G)"]` | 进入UNC侧配置时 | 决定参数体系（QCI/MBR vs 5QI/Session-AMBR）和信令映射；FUP Gx需额外配置UMCH | `active` | `EV-CA-01`, `EV-CA-02` |
| `DP-BW-05` | `L1_business` | `Namespace` | `NS-BW-01` | BWM控制类型选择 | BWM控制器采用CAR还是Shaping | `["CAR-CIR保障","CAR-PIR限速","SHAPING整形"]` | 选择BWM机制后 | 决定BWMCONTROLLER参数模式（CIR/PIR/CBS/PBS vs RATE/QUEDEPTH）；决定超额报文丢弃还是缓存 | `active` | `EV-CA-01` |
| `DP-BW-06` | `L1_business` | `Namespace` | `NS-BW-01` | FUP累计粒度选择 | FUP监控按会话还是按业务累计 | `["会话级FUP","业务级FUP"]` | 选择FUP降速机制后 | 决定URR的Monitoring-Level（SESSION_LEVEL vs PCC_RULE_LEVEL）和SA依赖；业务级FUP依赖SA+BWM | `active` | `EV-CA-01`, `EV-TK-01` |
| `DP-BW-07` | `L1_business` | `Namespace` | `NS-BW-01` | 应用识别需求 | 当前场景是否需要L7应用识别 | `["需L7识别→预定义规则","仅L3L4→可用动态规则"]` | 选择规则类型前 | 决定规则类型和SA依赖；定向业务/ADC必须用预定义规则 | `active` | `EV-CA-02` |
| `DP-BW-08` | `L1_business` | `Namespace` | `NS-BW-01` | 产品面配置分工 | 配置应在UDG、UNC还是双产品协作 | `["UDG执行面","UNC控制面","双产品协作"]` | 进入配置实施时 | 决定配置入口和N4下发链路；BWM在UDG配置执行参数，在UNC配置策略规则 | `active` | `EV-CA-01` |

---

## 4. BusinessRule（6条）

| `rule_id` | `rule_name` | `rule_type` | `rule_expression_mode` | `rule_source_kind` | `rule_logic` | `violation_effect` | `status` | `source_evidence_ids` |
|-----------|-------------|-------------|------------------------|--------------------|--------------|---------------------|----------|----------------------|
| `BR-BW-01` | 预定义规则三网元一致性 | `design_rule` | `explicit` | `design` | 凡涉及动态PCC（PCRF/PCF下发预定义规则名）的特性，SMF/UPF/PCF规则名+参数+FlowFilter必须完全一致 | 规则匹配失败，带宽控制不生效 | `active` | `EV-CA-01`, `EV-CA-02`, `EV-TK-26`, `EV-TK-15` |
| `BR-BW-02` | 超额降速优先级覆盖 | `design_rule` | `explicit` | `design` | FUP降速规则必须使用最高优先级，且FlowFilter必须完全覆盖原保障规则（端口号范围一致） | 部分流量降速、部分不受影响，降速不彻底 | `active` | `EV-CA-02`, `EV-TK-19` |
| `BR-BW-03` | BWM与PCC独立匹配 | `design_rule` | `explicit` | `principle` | BWM规则与PCC规则在SA七步流程中独立匹配互不干扰，可叠加执行（BWM管有线侧，PCC管无线侧） | 误以为冲突而删除其一，导致某一段带宽失控 | `active` | `EV-CA-02`, `EV-TK-18` |
| `BR-BW-04` | RULENAME跨策略类型不冲突 | `selection_rule` | `explicit` | `config` | 同一产品内PCC类型与QOS类型的RULENAME不能相同；BWM与CHARGING可同名 | 规则创建冲突或匹配混乱 | `active` | `EV-CA-01` |
| `BR-BW-05` | REFRESHSRV必须最后执行 | `acceptance_rule` | `explicit` | `ops` | UDG侧策略变更后必须执行SET REFRESHSRV，且执行后约60秒（PROTBINDFLOWF定时器）策略才完全下发 | 策略配置完成但未生效，验证失败 | `active` | `EV-CA-01`, `EV-TK-20`, `EV-TK-21` |
| `BR-BW-06` | License前置门控 | `scope_rule` | `explicit` | `config` | BWM策略类型未启用License时，配置不生效；UDG/UNC需分别获取对应License | 配置命令成功但功能不生效，难以排查 | `active` | `EV-CA-01`, `EV-FK-BW-BWM` |

> **rule_type说明**：严格服从Schema §8.9标准枚举。`scope_rule`=范围约束，`design_rule`=设计规则，`selection_rule`=选择规则，`acceptance_rule`=验收规则。原文件中 `consistency_rule`/`naming_rule`/`ops_rule` 等非标准枚举值已按语义归并到标准枚举。

---

## 5. SemanticObject（8个）

> 带宽控制场景无独立协议层SemanticObject（无Ga/Gy/N40），这是与计费场景的关键差异。

| `semantic_object_id` | `semantic_object_name` | `semantic_summary` | `applicable_layer` | `realized_by` | `source_evidence_ids` |
|----------------------|------------------------|--------------------|---------------------|---------------|-----------------------|
| `SO-BW-01` | 带宽控制策略 | CIR/PIR/RATE参数集，定义带宽上限/下限/整形速率 | `cross_layer` | BWMCONTROLLER | `EV-FK-BW-BWM`, `EV-TK-19` |
| `SO-BW-02` | 业务识别条件 | SVC/APP识别结果，定义"对什么业务做控制" | `cross_layer` | CATEGORYPROP, FILTER, L7FILTER | `EV-FK-BW-SA-Basic`, `EV-TK-17` |
| `SO-BW-03` | 流量配额 | FUP VolumeThreshold，定义"累计多少流量后触发" | `cross_layer` | URR, URRGROUP | `EV-FK-BW-FUP-UDG`, `EV-TK-01` |
| `SO-BW-04` | 限速等级 | 高速/限速/整形/默认/降速五模式，由BWMRULE.PRIORITY决定 | `cross_layer` | BWMRULE | `EV-FK-BW-BWM`, `EV-CA-02` |
| `SO-BW-05` | QoS参数集 | 5QI/MBR/GBR/ARP，定义无线侧QoS等级 | `cross_layer` | QOSPROP | `EV-FK-BW-QoS`, `EV-TK-24` |
| `SO-BW-06` | 应用检测事件 | APP_STA/APP_STO，定义"应用启动/停止触发" | `cross_layer` | ADCPARA, RULE(POLICYTYPE=ADC) | `EV-FK-BW-ADC`, `EV-TK-27` |
| `SO-BW-07` | 小区负荷等级 | Level 0-3（Invalid/Normal/Congestion/Overload），定义拥塞程度 | `cross_layer` | SET APNREPORTATTR | `EV-FK-BW-CellLoad`, `EV-CA-01` |
| `SO-BW-08` | 位置区域标识 | PLMN/Location/WiFi接入点，定义"在哪儿" | `cross_layer` | RULE(Predefined, PLMN条件) | `EV-FK-BW-APN-Policy`, `EV-TK-28` |

---

## 6. Scope（子对象）

| `scope_name` | `scope_type` | `scope_summary` | 关联方案 |
|--------------|--------------|-----------------|----------|
| 用户级范围 | `subscriber` | 单用户特定业务限速或配额控制 | CS-BW-01, CS-BW-02 |
| APN/DNN范围 | `access` | 按接入点或小区级负荷感知生效 | CS-BW-05, CS-BW-06 |
| 会话承载范围 | `subscription` | PDU会话级FUP流量累计 | CS-BW-02 |
| 业务选择范围 | `service_selection` | 按业务类型(SVC/APP)差异化限速或GBR保证 | CS-BW-01, CS-BW-03, CS-BW-04, CS-BW-07 |
| 位置区域范围 | `location` | 按PLMN/WiFi接入点/漫游区域激活差异化规则 | CS-BW-06 |

---

## 7. Participant（子对象）

| `participant_name` | `participant_type` | `plane_or_side` | `responsibility_summary` | 关联方案 |
|--------------------|--------------------|-----------------|--------------------------|----------|
| UPF | `network_function` | `user_plane` | 业务识别、BWM限速执行、流量统计上报、DSCP/FPI标记 | CS-BW-01~07 |
| SMF | `network_function` | `control_plane` | 策略编排、规则下发、专有承载建立、URR管理、位置感知 | CS-BW-01~06 |
| PCRF/PCF | `external_system` | `external` | 策略决策、动态PCC下发、配额管理、ADC策略、负荷策略 | CS-BW-01~06 |
| RAN/AMF/MME | `access_side` | `access_side` | 小区负荷上报、无线资源分配、调度队列优化、GBR资源预留 | CS-BW-03, CS-BW-05, CS-BW-07 |
| UE/用户 | `endpoint` | `terminal_side` | 发起会话与业务访问，产生待控制业务流 | CS-BW-01~07 |

---

## 8. 与计费场景业务图谱的对比

| 维度 | 计费场景 | 带宽控制场景 |
|------|---------|------------|
| BusinessDomain | 共享 `业务感知`（BD-CH-01 = BD-BW-01） | 共享 `业务感知` |
| NetworkScenario | `NS-CH-01 计费场景`（独立） | `NS-BW-01 带宽控制场景`（独立） |
| ConfigurationSolution | 7个（CS-CH-01~07，按计费方式/计量/兜底分） | 7个（CS-BW-01~07，按控制机制分） |
| 核心机制 | SA识别→Rule→PCC/URR计费链→Ga/Gy/N40上报→配额闭环 | SA识别→BWM限速→CAR/Shaping/FUP/GBR |
| 独有对象族 | 计费三件套(URR/URRGROUP/PCCPOLICYGRP)、SMF融合计费对象(CCT/CHFINIT/CHARGECTRL) | BWM(BWMSERVICE/BWMCONTROLLER/BWMUSERGROUP/BWMRULE) |
| 独有协议知识 | Ga/Gy/DCC/N40/PFCP/Gx（6个协议接口，SO-CH-10/11） | 无独立协议层SemanticObject |
| DecisionPoint | 8个（DP-CH-01~08） | 8个（DP-BW-01~08） |
| BusinessRule | 16条（BR-CH-01~16） | 6条（BR-BW-01~06） |
| SemanticObject | 12个（SO-CH-01~12，含协议栈2个） | 8个（SO-BW-01~08，无协议栈） |

> 两场景图谱独立构建，不互相依赖；共享部分限于 `业务感知` 根对象、通用ConfigTask（流过滤、PCC规则、用户模板）、通用ConfigObject（RULE, USERPROFILE, PCCPOLICYGRP, FLOWFILTER, URR）。

---

## 9. 业务图谱关系边

### 9.1 层级包含

| 起点 | 关系 | 终点 |
|------|------|------|
| `BD-BW-01` | `contains` | `NS-BW-01` |
| `NS-BW-01` | `instantiated_as` | `CS-BW-01` ~ `CS-BW-07` |

### 9.2 方案使用特性（uses_feature，共20条边）

| 起点 | 关系 | 终点 |
|------|------|------|
| `CS-BW-01` | `uses_feature` | `GWFD-110311`, `GWFD-110101`, `GWFD-020351`, `WSFD-109101`, `WSFD-211005`, `GWFD-020354`, `GWFD-110313` |
| `CS-BW-02` | `uses_feature` | `GWFD-020353`, `WSFD-109104`, `GWFD-110312`, `WSFD-211009` |
| `CS-BW-03` | `uses_feature` | `GWFD-020358`, `WSFD-109107` |
| `CS-BW-04` | `uses_feature` | `GWFD-020357`, `WSFD-109102` |
| `CS-BW-05` | `uses_feature` | `GWFD-110332`, `WSFD-211101` |
| `CS-BW-06` | `uses_feature` | `WSFD-109108` |
| `CS-BW-07` | `uses_feature` | `GWFD-020359`, `GWFD-110301`, `GWFD-110302`, `GWFD-110331` |

### 9.3 决策点归属（has_decision）

| 起点 | 关系 | 终点 |
|------|------|------|
| `NS-BW-01` | `has_decision` | `DP-BW-01`, `DP-BW-04`, `DP-BW-08` |
| `CS-BW-01` | `has_decision` | `DP-BW-02`, `DP-BW-05`, `DP-BW-07` |
| `CS-BW-02` | `has_decision` | `DP-BW-03`, `DP-BW-06` |
| `CS-BW-04` | `has_decision` | `DP-BW-07` |

### 9.4 业务规则约束（constrained_by）

| 起点 | 关系 | 终点 |
|------|------|------|
| `CS-BW-01` ~ `CS-BW-07` | `constrained_by` | `BR-BW-06`（License前置门控，全部方案） |
| `CS-BW-01` ~ `CS-BW-07` | `constrained_by` | `BR-BW-04`（RULENAME不冲突，全部方案） |
| `CS-BW-01`, `CS-BW-02`, `CS-BW-04`, `CS-BW-06` | `constrained_by` | `BR-BW-01`（预定义规则三网元一致性） |
| `CS-BW-02` | `constrained_by` | `BR-BW-02`（超额降速优先级覆盖） |
| `CS-BW-01`, `CS-BW-03` | `constrained_by` | `BR-BW-03`（BWM与PCC独立匹配） |
| `CS-BW-01`, `CS-BW-02`, `CS-BW-07` | `constrained_by` | `BR-BW-05`（REFRESHSRV最后执行） |

### 9.5 语义对象使用（uses_semantic_object）

| 起点 | 关系 | 终点 |
|------|------|------|
| `CS-BW-01` | `uses_semantic_object` | `SO-BW-01`, `SO-BW-02`, `SO-BW-04` |
| `CS-BW-02` | `uses_semantic_object` | `SO-BW-03`, `SO-BW-04` |
| `CS-BW-03` | `uses_semantic_object` | `SO-BW-05`, `SO-BW-02` |
| `CS-BW-04` | `uses_semantic_object` | `SO-BW-06`, `SO-BW-05` |
| `CS-BW-05` | `uses_semantic_object` | `SO-BW-07`, `SO-BW-01` |
| `CS-BW-06` | `uses_semantic_object` | `SO-BW-08` |
| `CS-BW-07` | `uses_semantic_object` | `SO-BW-02` |

### 9.6 决策点影响（selects / sets_value_pattern）

| 起点 | 关系 | 终点 | 说明 |
|------|------|------|------|
| `DP-BW-01` | `selects` | `CS-BW-01`/`CS-BW-02`/`CS-BW-03`/`CS-BW-05` | 带宽控制机制选择决定方案闭包 |
| `DP-BW-05` | `sets_value_pattern` | `BWMCONTROLLER.CTRLTYPE` | CAR-CIR/CAR-PIR/SHAPING三种控制类型 |
| `DP-BW-06` | `sets_value_pattern` | `URR.Monitoring-Level` | SESSION_LEVEL vs PCC_RULE_LEVEL |

---

## 10. 端到端方案链路（跨层映射依据）

### 10.1 CS-BW-01 SA-BWM带宽控制端到端
```
SA识别(SVC/APP → CATEGORYPROP/FILTER/L7FILTER) → FLOWFILTER组合匹配
→ RULE(POLICYTYPE=QOS, PRIORITY裁决) → BWMUSERGROUP绑定
→ BWMCONTROLLER(CIR/PIR/CBS/PBS 或 RATE/QUEDEPTH)
→ BWMRULE执行 → UPF令牌桶限速/整形
→ SET REFRESHSRV(60秒生效)
```

### 10.2 CS-BW-02 FUP配额降速端到端
```
URR累计流量(SESSION_LEVEL或PCC_RULE_LEVEL)
→ 配额耗尽触发(VolumeThreshold) → SMF上报PCRF
→ PCRF下发高优先级降速QoS规则(MBR降低)
→ 新PCC规则覆盖原规则(FlowFilter完全覆盖)
→ UPF执行降速 → 用户带宽降低
```

### 10.3 CS-BW-03 GBR带宽保证端到端
```
SA识别高价值业务 → URR(QOS模式)检测上报
→ SMF触发专有承载/QoS Flow建立
→ QOSPROP(5QI+GBR-UL/DL+ARP)下发
→ RAN侧预留GBR资源 → UPF标记DSCP/FPI
→ 无线侧优先调度 → 带宽下限保证
```

### 10.4 CS-BW-04 ADC应用感知端到端
```
ADC检测应用启动(APP_STA) → SMF上报PCF
→ PCF下发Start策略组(GBR QoS)
→ UPF执行高带宽保障
→ ADC检测应用停止(APP_STO) → PCF下发Stop策略组
→ 恢复Normal策略组(Non-GBR)
→ 三策略组动态切换，用户无感知
```

---

## 11. 对象计数汇总

| 对象类型 | 数量 | 编号范围 |
|---------|------|---------|
| BusinessDomain | 1 | BD-BW-01 |
| NetworkScenario | 1 | NS-BW-01 |
| ConfigurationSolution | 7 | CS-BW-01~07 |
| DecisionPoint | 8 | DP-BW-01~08 |
| BusinessRule | 6 | BR-BW-01~06 |
| SemanticObject | 8 | SO-BW-01~08 |
| Scope（子对象） | 5 | - |
| Participant（子对象） | 5 | - |
| **业务层对象总计** | **41** | - |

---

> 本文件为带宽控制场景三层图谱第1层。第2层特性图谱、第3层任务原子层、第4层命令图谱、第5层跨层映射、第6层证据索引见同目录其他文件。
