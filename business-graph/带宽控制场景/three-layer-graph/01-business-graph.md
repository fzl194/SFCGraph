# 带宽控制场景业务图谱（新 Schema，v0.1）

> 范围：仅描述带宽控制场景（业务感知套餐2）在新三层图谱 schema 下的业务图谱部分。
> 约束：对象、关系、属性命名严格服从 `三层图谱Schema-最终版-v0.1.md` §8 业务图谱 Schema。
> 来源：基于 `cross-topic-analysis.md`（32批次317份源文档综合分析）和 `cross-feature-analysis.md`（24特性横向分析）。
> 与计费场景的关系：共享 `业务感知` BusinessDomain 根对象，但 ConfigurationSolution/DecisionPoint/BusinessRule/SemanticObject 全部独立实例化。

---

## 0. 适用定义与来源

### 0.1 根定义

- `三层图谱本体标准定义.md`
- `三层图谱Schema-最终版-v0.1.md`

### 0.2 带宽控制场景直接来源

- `business-graph/带宽控制场景/cross-topic-analysis.md`（§1.1 场景定位、§6.2 五大维度、§8.4 九场景汇总）
- `business-graph/带宽控制场景/cross-feature-analysis.md`（§4.3 协作链路、§4.4 场景组合）
- `business-graph/带宽控制场景/feature-knowledge/*.md`（24个特性知识文档）
- `business-graph/带宽控制场景/topic-knowledge/Batch-*.md`（32个主题知识批次）

### 0.3 本文件保留对象

| 对象 | 中文名 | 实例数 |
| --- | --- | --- |
| `BusinessDomain` | 业务域 | 1 |
| `NetworkScenario` | 现网场景 | 1 |
| `ConfigurationSolution` | 配置方案 | 7 |
| `DecisionPoint` | 决策点 | 8 |
| `BusinessRule` | 业务规则 | 6 |
| `SemanticObject` | 语义对象 | 8 |

子对象：`Scope`、`Participant`。
外部引用对象：`Feature`、`ConfigTask`（在特性图谱/任务原子层展开）。
本文件不展开：`ConfigObject`、`MMLCommand`、`CommandParameter`、`License`、`FeatureRule`、`TaskRule`、`CommandRule`。

---

## 1. BusinessDomain

带宽控制场景与计费场景共享同一业务域根对象 `业务感知`。

| 字段 | 值 |
| --- | --- |
| `domain_id` | `BD-BW-01` |
| `domain_name` | `业务感知` |
| `domain_summary` | 在用户会话过程中，对用户的数据报文进行解析，从而区分出用户使用的不同业务，以实现策略控制和计费控制 |
| `status` | `active` |
| `source_evidence_ids` | `EV-CFA`, `EV-CTA`, `EV-FK-110101` |

> 注：该 BusinessDomain 与计费场景共享。计费场景作为套餐1，带宽控制场景作为套餐2，均挂在该域下。

---

## 2. NetworkScenario

| 字段 | 值 |
| --- | --- |
| `scenario_id` | `NS-BW-01` |
| `scenario_name` | `带宽控制场景` |
| `scenario_summary` | 对用户流量按业务类型、用户等级、套餐配额、应用类型、位置区域等维度进行差异化的带宽分配与限速控制 |
| `judgment_basis` | 需按业务类型/用户等级/套餐配额/应用类型/位置区域等维度进行差异化带宽分配与限速；或需对超额流量执行降速/整形/门控；或需对高价值业务执行 GBR 带宽保证 |
| `typical_outcome` | 实现 BWM 限速(CAR)、Shaping 整形、FUP 降速、GBR 保证、门控阻断等差异化带宽管理；上下行带宽可独立控制；与无线侧调度联动优化 |
| `status` | `active` |
| `source_evidence_ids` | `EV-CTA`, `EV-CFA`, `EV-TK-19`, `EV-TK-18` |

### 2.1 场景边界

**覆盖范围**：
- 产品：UDG（用户面，16特性）+ UNC（控制面，8特性）
- 网元：SGW-U/PGW-U/UPF（UDG）、SMF/PGW-C/AMF/GGSN-C（UNC）
- 接口：Gx（2/3/4G）、N7（5G）、N4（PFCP）、GTP-U扩展头
- 控制维度：套餐配额、应用类型、位置区域、用户等级、时间窗口

**不覆盖范围**（相邻场景）：
- 计费场景（套餐1）：差异化计费、免费业务、配额计费动作（由计费场景图谱承载）
- 访问限制场景（套餐3）：URL 过滤、重定向阻断、接入控制（由访问限制场景图谱承载）

---

## 3. ConfigurationSolution

带宽控制场景收敛为 7 个稳定方案闭包。来源：`cross-topic-analysis.md` §6.2（五大维度）+ §8.4（九场景）归纳合并。

### 3.1 CS-BW-01: SA-BWM 带宽控制方案

| 字段 | 值 |
| --- | --- |
| `solution_id` | `CS-BW-01` |
| `solution_name` | `SA-BWM 带宽控制方案` |
| `solution_summary` | 通过 SA 识别业务类型，在 UDG 用户面执行 BWM 三级控制（用户级/组级/全局级），实现基于业务感知的差异化限速 |
| `design_intent` | 解决"按业务类型差异化限速"问题：低价值业务（P2P）限速，高价值业务保障 |
| `core_mechanism_combo` | `SA识别(SVC/APP) → BWM规则匹配 → CAR令牌桶(CIR/PIR/CBS/PBS) / SHAPING整形(RATE/QUEDEPTH)` |
| `status` | `active` |
| `source_evidence_ids` | `EV-FK-110311`, `EV-FK-211005`, `EV-TK-19`, `EV-CFA-§4.4链路1` |

`scopes`:
- subscriber（单用户特定业务限速）
- service_selection（按 SVC/APP 分类限速）

`participants`:
- UDG/UPF（用户面执行，plane=user_plane）
- UNC/SMF（控制面规则下发，plane=control_plane）
- PCRF/PCF（策略决策源，type=external_system）

### 3.2 CS-BW-02: FUP 配额降速方案

| 字段 | 值 |
| --- | --- |
| `solution_id` | `CS-BW-02` |
| `solution_name` | `FUP 配额降速方案` |
| `solution_summary` | 通过 URR 累计用户流量，配额耗尽后由 PCRF/PCF 下发高优先级降速规则覆盖原规则，实现套餐超量降速 |
| `design_intent` | 解决"套餐配额超量后降速"问题：月套餐20GB后从100Mbps降至1Mbps |
| `core_mechanism_combo` | `URR流量累计 → 配额耗尽触发 → PCRF下发新QoS(MBR降低) / 预定义降速规则高优先级覆盖` |
| `status` | `active` |
| `source_evidence_ids` | `EV-FK-020353`, `EV-FK-109104`, `EV-FK-110312`, `EV-FK-211009`, `EV-TK-01`, `EV-TK-22`, `EV-CFA-§4.4链路2`, `EV-CTA-§7.4` |

`scopes`:
- subscription（会话级 FUP：整会话所有流量累计）
- subscriber（用户级配额）

`participants`:
- UDG/UPF（流量计数与上报）
- UNC/SMF（URR 下发与上报转发）
- PCRF/PCF（配额管理与降速决策）

### 3.3 CS-BW-03: GBR 带宽保证方案

| 字段 | 值 |
| --- | --- |
| `solution_id` | `CS-BW-03` |
| `solution_name` | `GBR 带宽保证方案` |
| `solution_summary` | 通过 SA 识别高价值业务，触发专有承载/QoS Flow 建立，分配专用资源保证带宽下限（GBR） |
| `design_intent` | 解决"高价值业务带宽下限保证"问题：视频/语音业务保证不低于 GBR |
| `core_mechanism_combo` | `SA识别高价值业务 → URR(QOS模式)上报 → UNC发起专有承载/QoS Flow → GBR资源预留(GBR-UL/DL)` |
| `status` | `active` |
| `source_evidence_ids` | `EV-FK-020358`, `EV-FK-109107`, `EV-CFA-§4.4链路3`, `EV-CTA-§3.5` |

`scopes`:
- service_selection（特定业务 GBR 保证）

`participants`:
- UDG/UPF（业务识别与 QoS 事件上报）
- UNC/SMF（专有承载/QoS Flow 建立信令）
- RAN/AMF/MME（无线侧资源分配）

### 3.4 CS-BW-04: ADC 应用感知动态带宽方案

| 字段 | 值 |
| --- | --- |
| `solution_id` | `CS-BW-04` |
| `solution_name` | `ADC 应用感知动态带宽方案` |
| `solution_summary` | 通过 ADC 检测应用启动/停止事件（APP_STA/APP_STO），动态切换三策略组（Normal/Start/Stop）实现应用级带宽调整，无需用户重连 |
| `design_intent` | 解决"按应用类型实时调整带宽"问题：视频APP激活时分配GBR，停止时恢复Non-GBR |
| `core_mechanism_combo` | `ADC检测(APP_STA/APP_STO) → PCF决策 → 三策略组动态切换(Normal/Start/Stop) → QoS参数变更` |
| `status` | `active` |
| `source_evidence_ids` | `EV-FK-020357`, `EV-FK-109102`, `EV-TK-27`, `EV-TK-28`, `EV-CTA-§7.5` |

`scopes`:
- service_selection（应用级带宽，per APP）

`participants`:
- UDG/UPF（L7 DPI 引擎，应用检测）
- UNC/SMF（事件转发与策略映射）
- PCRF/PCF（ADC 策略决策）

### 3.5 CS-BW-05: 小区负荷动态带宽方案

| 字段 | 值 |
| --- | --- |
| `solution_id` | `CS-BW-05` |
| `solution_name` | `小区负荷动态带宽方案` |
| `solution_summary` | 通过 RAN 上报小区负荷等级（Level 0-3），UDG 转发至 UNC/PCRF，PCRF 下发动态带宽策略，实现拥塞时动态调整 BWM |
| `design_intent` | 解决"小区拥塞时动态限速"问题：拥塞时对低优先级用户限速，保障高价值用户 |
| `core_mechanism_combo` | `RAN负荷上报 → UDG转发(GTP-U扩展头) → UNC上报PCRF → PCRF动态BWM策略下发` |
| `status` | `active` |
| `source_evidence_ids` | `EV-FK-110332`, `EV-FK-211101`, `EV-CFA-§4.4场景6`, `EV-CTA-§6.2维度补充` |

`scopes`:
- access（小区级负荷感知）

`participants`:
- RAN（负荷感知与上报）
- UDG/UPF（负荷信息转发）
- UNC/SMF（事件上报 PCRF）
- PCRF/PCF（动态策略决策）

### 3.6 CS-BW-06: 位置区域差异化带宽方案

| 字段 | 值 |
| --- | --- |
| `solution_id` | `CS-BW-06` |
| `solution_name` | `位置区域差异化带宽方案` |
| `solution_summary` | 通过感知用户位置变化（WiFi接入点/PLMN/漫游区域），激活预定义差异化带宽规则，实现按位置区域限速 |
| `design_intent` | 解决"按位置区域差异化限速"问题：漫游时限制最大带宽为10Mbps |
| `core_mechanism_combo` | `位置变化感知(UE_LOCAL_IP/PLMN_CH) → 预定义规则激活 → 位置差异化带宽(PIR限速)` |
| `status` | `active` |
| `source_evidence_ids` | `EV-FK-109108`, `EV-TK-28`, `EV-TK-29`, `EV-CTA-§6.2维度3` |

`scopes`:
- location（位置区域感知）
- access（WiFi接入点）

`participants`:
- UNC/SMF（位置变化感知与规则激活）
- PCRF/PCF（位置条件策略决策）

> 注：位置区域控制只能使用预定义规则（位置信息在 SMF 侧，PCF 无 L7 识别能力）。

### 3.7 CS-BW-07: 无线资源优化标记方案

| 字段 | 值 |
| --- | --- |
| `solution_id` | `CS-BW-07` |
| `solution_name` | `无线资源优化标记方案` |
| `solution_summary` | 通过 DSCP/FPI 标记或终端OS差异化，影响无线侧调度优先级（非直接用户面限速），间接优化带宽体验 |
| `design_intent` | 解决"无线侧调度优化"问题：通过标记影响基站队列调度，间接提升业务带宽体验 |
| `core_mechanism_combo` | `SA识别业务 → DSCP/FPI标记 / OSTYPE差异化 → RAN调度队列优化（非UPF限速）` |
| `status` | `active` |
| `source_evidence_ids` | `EV-FK-020359`, `EV-FK-110301`, `EV-FK-110302`, `EV-FK-110331`, `EV-CFA-附录G` |

`scopes`:
- service_selection（按业务类型标记）

`participants`:
- UDG/UPF（业务识别与标记）
- RAN/BSC（无线侧调度执行）

> 注：异常流量检测(GWFD-020305)和SA特征库管控(GWFD-111600)作为辅助能力，通过 Feature 依赖和 BusinessRule 表达，不单独建方案。

---

## 4. DecisionPoint

带宽控制场景包含 8 个业务层稳定决策点。

| `decision_id` | `decision_name` | `decision_question` | `option_set` | `trigger_condition` | `impact_summary` | `status` | `source_evidence_ids` |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `DP-BW-01` | 带宽控制机制选择 | 当前业务流应采用哪种带宽控制机制 | `["CAR限速","Shaping整形","GBR保证","FUP降速","门控阻断"]` | 进入带宽控制配置时 | 决定使用哪些 CS（CS-BW-01~05）和 Feature；决定 BWMCONTROLLER.CTRLTYPE 或 QOSPROP 路径 | `active` | `EV-CFA-§1.4`, `EV-CTA-§3.5` |
| `DP-BW-02` | 控制粒度选择 | 带宽控制应作用于哪个粒度 | `["会话级","业务级","用户组级","全局级"]` | 确定控制机制后 | 决定 BWMRULETYPE（SUBSCRIBER_SPECIFIC/GROUP_SPECIFIC/GLOBAL）和 URR 绑定方式 | `active` | `EV-CFA-§3.2`, `EV-CFA-§3.4` |
| `DP-BW-03` | 规则类型选择 | 当前场景应使用哪种 PCC 规则类型 | `["动态规则","预定义规则","本地规则"]` | 确定控制粒度后 | 决定配置路径和三网元一致性要求；定向业务必须用预定义（PCF无L7能力） | `active` | `EV-CTA-§7.2`, `EV-TK-26` |
| `DP-BW-04` | 接口代际选择 | 当前部署是 4G 还是 5G | `["Gx(4G)","N7(5G)"]` | 进入 UNC 侧配置时 | 决定参数体系（QCI/MBR vs 5QI/Session-AMBR）和信令映射；FUP Gx 需额外配置 UMCH | `active` | `EV-CFA-§3.3`, `EV-CTA-§3.3` |
| `DP-BW-05` | BWM 控制类型选择 | BWM 控制器采用 CAR 还是 Shaping | `["CAR-CIR保障","CAR-PIR限速","SHAPING整形"]` | 选择 BWM 机制后 | 决定 BWMCONTROLLER 参数模式（CIR/PIR/CBS/PBS vs RATE/QUEDEPTH）；决定超额报文丢弃还是缓存 | `active` | `EV-CFA-§4.2`, `EV-CFA-§4.3`, `EV-CFA-附录F` |
| `DP-BW-06` | FUP 累计粒度选择 | FUP 监控按会话还是按业务累计 | `["会话级FUP","业务级FUP"]` | 选择 FUP 降速机制后 | 决定 URR 的 Monitoring-Level（SESSION_LEVEL vs PCC_RULE_LEVEL）和 SA 依赖；业务级 FUP 依赖 SA+BWM | `active` | `EV-CFA-§3.4`, `EV-TK-01` |
| `DP-BW-07` | 应用识别需求 | 当前场景是否需要 L7 应用识别 | `["需L7识别→预定义规则","仅L3L4→可用动态规则"]` | 选择规则类型前 | 决定规则类型和 SA 依赖；定向业务/ADC 必须用预定义规则 | `active` | `EV-CTA-§7.2决策树` |
| `DP-BW-08` | 产品面配置分工 | 配置应在 UDG、UNC 还是双产品协作 | `["UDG执行面","UNC控制面","双产品协作"]` | 进入配置实施时 | 决定配置入口和 N4 下发链路；BWM 在 UDG 配置执行参数，在 UNC 配置策略规则 | `active` | `EV-CFA-§3.1`, `EV-CFA-§5.6` |

---

## 5. BusinessRule

带宽控制场景包含 6 条关键业务规则。

| `rule_id` | `rule_name` | `rule_type` | `rule_expression_mode` | `rule_source_kind` | `rule_logic` | `violation_effect` | `status` | `source_evidence_ids` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `BR-BW-01` | 预定义规则三网元一致性 | `consistency_rule`→`design_rule` | `explicit` | `design` | 凡涉及动态PCC（PCRF/PCF下发预定义规则名）的特性，SMF/UPF/PCF 规则名+参数+FlowFilter必须完全一致 | 规则匹配失败，带宽控制不生效 | `active` | `EV-CFA-§5.7`, `EV-TK-26`, `EV-TK-15` |
| `BR-BW-02` | 超额降速优先级覆盖 | `design_rule` | `explicit` | `design` | FUP降速规则必须使用最高优先级，且 FlowFilter 必须完全覆盖原保障规则（端口号范围一致） | 部分流量降速、部分不受影响，降速不彻底 | `active` | `EV-CTA-§7.4`, `EV-TK-19` |
| `BR-BW-03` | BWM与PCC独立匹配 | `design_rule` | `explicit` | `principle` | BWM规则与PCC规则在SA七步流程中独立匹配互不干扰，可叠加执行（BWM管有线侧，PCC管无线侧） | 误以为冲突而删除其一，导致某一段带宽失控 | `active` | `EV-CTA-§7.1`, `EV-TK-18` |
| `BR-BW-04` | RULENAME跨策略类型不冲突 | `naming_rule`→`selection_rule` | `explicit` | `config` | 同一产品内 PCC 类型与 QOS 类型的 RULENAME 不能相同；BWM 与 CHARGING 可同名 | 规则创建冲突或匹配混乱 | `active` | `EV-CFA-§5.1`, `EV-CFA-§H.4` |
| `BR-BW-05` | REFRESHSRV 必须最后执行 | `ops_rule`→`acceptance_rule` | `explicit` | `ops` | UDG 侧策略变更后必须执行 SET REFRESHSRV，且执行后约 60 秒（PROTBINDFLOWF定时器）策略才完全下发 | 策略配置完成但未生效，验证失败 | `active` | `EV-CFA-§5.5`, `EV-TK-20`, `EV-TK-21` |
| `BR-BW-06` | License 前置门控 | `scope_rule` | `explicit` | `config` | BWM 策略类型未启用 License 时，配置不生效；UDG/UNC 需分别获取对应 License | 配置命令成功但功能不生效，难以排查 | `active` | `EV-CFA-§2.3`, `EV-FK-110311` |

> 注：`rule_type` 中 `consistency_rule`/`naming_rule`/`ops_rule` 不在 BusinessRule 的标准 enum（`selection_rule/scope_rule/design_rule/acceptance_rule/diagnosis_rule`）内，此处按语义归并为 `design_rule`/`selection_rule`/`acceptance_rule`，原标签保留于 `rule_name` 旁注释。

---

## 6. SemanticObject

带宽控制场景包含 8 个语义桥接对象，承接"业务意图→语义单元→特性/task/命令对象"。

| `semantic_object_id` | `semantic_object_name` | `semantic_summary` | `semantic_layer_hint` | `realized_by`（ConfigObject） | `status` | `source_evidence_ids` |
| --- | --- | --- | --- | --- | --- | --- |
| `SO-BW-01` | 带宽控制策略 | CIR/PIR/RATE 参数集，定义带宽上限/下限/整形速率 | `cross_layer` | `BWMCONTROLLER` | `active` | `EV-FK-110311`, `EV-TK-19` |
| `SO-BW-02` | 业务识别条件 | SVC/APP 识别结果，定义"对什么业务做控制" | `cross_layer` | `CATEGORYPROP`, `FILTER`, `L7FILTER` | `active` | `EV-FK-110101`, `EV-TK-17` |
| `SO-BW-03` | 流量配额 | FUP VolumeThreshold，定义"累计多少流量后触发" | `cross_layer` | `URR`, `URRGROUP` | `active` | `EV-FK-020353`, `EV-TK-01` |
| `SO-BW-04` | 限速等级 | 高速/限速/整形/默认/降速五模式，由 BWMRULE.PRIORITY 决定 | `cross_layer` | `BWMRULE` | `active` | `EV-FK-110311`, `EV-CTA-§7.4` |
| `SO-BW-05` | QoS 参数集 | 5QI/MBR/GBR/ARP，定义无线侧 QoS 等级 | `cross_layer` | `QOSPROP` | `active` | `EV-FK-020358`, `EV-TK-24` |
| `SO-BW-06` | 应用检测事件 | APP_STA/APP_STO，定义"应用启动/停止触发" | `cross_layer` | `ADCPARA`, `RULE(POLICYTYPE=ADC)` | `active` | `EV-FK-020357`, `EV-TK-27` |
| `SO-BW-07` | 小区负荷等级 | Level 0-3（Invalid/Normal/Congestion/Overload），定义拥塞程度 | `cross_layer` | `SET APNREPORTATTR` | `active` | `EV-FK-110332`, `EV-CFA-附录G` |
| `SO-BW-08` | 位置区域标识 | PLMN/Location/WiFi接入点，定义"在哪儿" | `cross_layer` | `RULE(Predefined, PLMN条件)` | `active` | `EV-FK-109108`, `EV-TK-28` |

---

## 7. 业务图谱关系边

### 7.1 层级包含关系

| 起点 | 关系 | 终点 | 说明 |
| --- | --- | --- | --- |
| `BD-BW-01` | `contains` | `NS-BW-01` | 业务域包含带宽控制场景 |
| `NS-BW-01` | `instantiated_as` | `CS-BW-01`~`CS-BW-07` | 场景收敛为 7 个方案 |

### 7.2 方案使用特性（uses_feature）

> 完整 CS→Feature 映射见 `05-cross-layer-mapping.md`。此处列概要。

| 起点 | 关系 | 终点 |
| --- | --- | --- |
| `CS-BW-01` | `uses_feature` | `GWFD-110311`, `WSFD-211005`, `GWFD-110101`, `GWFD-020351`, `WSFD-109101`, `GWFD-020354`, `GWFD-110313` |
| `CS-BW-02` | `uses_feature` | `GWFD-020353`, `WSFD-109104`, `GWFD-110312`, `WSFD-211009` |
| `CS-BW-03` | `uses_feature` | `GWFD-020358`, `WSFD-109107` |
| `CS-BW-04` | `uses_feature` | `GWFD-020357`, `WSFD-109102` |
| `CS-BW-05` | `uses_feature` | `GWFD-110332`, `WSFD-211101` |
| `CS-BW-06` | `uses_feature` | `WSFD-109108` |
| `CS-BW-07` | `uses_feature` | `GWFD-020359`, `GWFD-110301`, `GWFD-110302`, `GWFD-110331` |

### 7.3 方案使用 task（uses_task）

> 完整 CS→Task 映射见 `05-cross-layer-mapping.md`。

| 起点 | 关系 | 终点 |
| --- | --- | --- |
| `CS-BW-01` | `uses_task` | `T-007`, `T-008`, `T-101`~`T-106`, `T-006` |
| `CS-BW-02` | `uses_task` | `T-007`, `T-201`~`T-205`, `T-003`~`T-005` |
| `CS-BW-03` | `uses_task` | `T-007`, `T-301`~`T-303`, `T-003`~`T-005` |
| `CS-BW-04` | `uses_task` | `T-007`, `T-401`, `T-402`, `T-003`~`T-005` |
| `CS-BW-05` | `uses_task` | `T-007`, `T-603`, `T-103`~`T-105` |
| `CS-BW-06` | `uses_task` | `T-007`, `T-501`~`T-504`, `T-003`~`T-005` |
| `CS-BW-07` | `uses_task` | `T-007`, `T-601`, `T-602` |

### 7.4 决策点归属（has_decision）

| 起点 | 关系 | 终点 |
| --- | --- | --- |
| `NS-BW-01` | `has_decision` | `DP-BW-01`, `DP-BW-04`, `DP-BW-08` |
| `CS-BW-01` | `has_decision` | `DP-BW-02`, `DP-BW-05`, `DP-BW-07` |
| `CS-BW-02` | `has_decision` | `DP-BW-03`, `DP-BW-06` |
| `CS-BW-04` | `has_decision` | `DP-BW-07` |

### 7.5 业务规则约束（constrained_by）

| 起点 | 关系 | 终点 |
| --- | --- | --- |
| `CS-BW-01`~`CS-BW-07` | `constrained_by` | `BR-BW-06`（License 前置门控，全部方案） |
| `CS-BW-01`, `CS-BW-02`, `CS-BW-04` | `constrained_by` | `BR-BW-01`（预定义规则三网元一致性） |
| `CS-BW-02` | `constrained_by` | `BR-BW-02`（超额降速优先级覆盖） |
| `CS-BW-01`, `CS-BW-03` | `constrained_by` | `BR-BW-03`（BWM与PCC独立匹配） |
| `CS-BW-01`~`CS-BW-07` | `constrained_by` | `BR-BW-04`（RULENAME 不冲突） |
| `CS-BW-01`, `CS-BW-02`, `CS-BW-07` | `constrained_by` | `BR-BW-05`（REFRESHSRV 最后执行） |

### 7.6 语义对象使用（uses_semantic_object）

| 起点 | 关系 | 终点 |
| --- | --- | --- |
| `CS-BW-01` | `uses_semantic_object` | `SO-BW-01`, `SO-BW-02`, `SO-BW-04` |
| `CS-BW-02` | `uses_semantic_object` | `SO-BW-03`, `SO-BW-04` |
| `CS-BW-03` | `uses_semantic_object` | `SO-BW-05`, `SO-BW-02` |
| `CS-BW-04` | `uses_semantic_object` | `SO-BW-06`, `SO-BW-05` |
| `CS-BW-05` | `uses_semantic_object` | `SO-BW-07`, `SO-BW-01` |
| `CS-BW-06` | `uses_semantic_object` | `SO-BW-08` |
| `CS-BW-07` | `uses_semantic_object` | `SO-BW-02` |

### 7.7 证据支撑（supported_by）

| 起点 | 关系 | 终点 |
| --- | --- | --- |
| `BD-BW-01` | `supported_by` | `EV-CFA`, `EV-CTA`, `EV-FK-110101` |
| `NS-BW-01` | `supported_by` | `EV-CTA`, `EV-CFA`, `EV-TK-19`, `EV-TK-18` |
| `CS-BW-01`~`CS-BW-07` | `supported_by` | 见各方案 `source_evidence_ids` 字段 |

---

## 8. 与计费场景图谱的差异说明

本场景业务图谱与计费场景业务图谱（`计费场景/新三层图谱/01-计费场景-业务图谱-新schema-v0.1.md`）的关系：

| 维度 | 计费场景 | 带宽控制场景 |
| --- | --- | --- |
| BusinessDomain | 共享 `业务感知`（BD-BW-01 = service-awareness） | 共享 `业务感知` |
| NetworkScenario | `NS-01 计费场景` | `NS-BW-01 带宽控制场景`（独立） |
| ConfigurationSolution | 1个（DS-01 差异化计费组合方案） | 7个（CS-BW-01~07，按控制机制分） |
| 核心机制 | PCC/URR 计费链 + 配额动作切换 | BWM 三级控制 + CAR/Shaping/FUP/GBR |
| 独有对象族 | 无 | BWM（BWMSERVICE/BWMCONTROLLER/BWMUSERGROUP/BWMRULE） |

两者不共享 ConfigurationSolution、DecisionPoint、BusinessRule、SemanticObject 实例。
