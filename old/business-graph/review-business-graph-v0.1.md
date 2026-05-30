# 业务图谱最小闭包审查报告 v0.1

**审查人**: 高级审查 Agent（独立于构建 Agent）
**审查范围**: business-graph/ 全部文档 + work/business-awareness-result/ 原始设计 + 产品文档验证
**审查粒度**: 找错 + 疑问标记
**日期**: 2026-05-14
**最后更新**: 2026-05-15（标注构建 Agent 修复状态）

---

## 一、总体判断

构建 Agent 的方向是对的。Schema 层和构建方法没有根本性设计错误。数据层面的 ID 引用完整性良好，无孤立引用、无重复条目。

**当前最小闭包的核心问题不是"抽错了"，而是"抽浅了"和"三层之间的桥接层缺 CSV 落地"。**

构建 Agent 自己的自审（11号文档）已经识别了大部分结构性缺口（RuntimeFlow、ValidationPlan 等）。以下是自审未覆盖的、或需要你决策的问题。

> **v0.2 更新说明**：构建 Agent 已根据本报告完成大量修复工作，自审文档升级到 v0.2，数据目录从扁平 CSV 重组为 11 个子目录。各问题修复状态见下方 `[v0.2 状态]` 标注。

---

## 二、ERROR（明确错误）

### E-01: DomainSemanticObject / Feature / ConfigObject 无 CSV 落地

**来源**: CSV 一致性检查 vs `07` MD 文档

`07` MD 文档第 3.5-3.9 节明确定义了：
- 6 个 DomainSemanticObject 实例
- 4 个 Feature 实例
- 17 个 ConfigObject 实例

以及 5 类关系（`uses_semantic_object`、`instantiates_semantic_object`、`semantic_realized_by_config`、`implemented_by_feature`、`realized_by_config`）。

**但这些在 `data/` 目录下完全没有对应的 CSV 文件。**

这意味着跨层映射的核心桥接数据只存在于 MD 文档中，无法被程序化验证和消费。如果这是"第一阶段的简化"，需要明确标注；如果不是，则需要补建这些 CSV。

**严重程度**: ERROR — 跨层映射是三层图谱的核心价值，没有数据落地就等于没有映射。

> **[v0.2 状态: 已修复]** 构建 Agent 已补齐所有缺失的 CSV 实体表：
> - `data/03-semantic-entities/domain_semantic_objects.csv` — 15 个语义对象（含 SubjectSemantics），其中 12 个 accepted、3 个 reserved
> - `data/05-feature-entities/features.csv` — 6 个特性（新增 WSFD-109101 PCC基本功能）
> - `data/07-command-entities/config_objects.csv` — 25 个配置对象（含 FltBindFlowF、ProtBindFlowF 绑定型对象）
> - `data/07-command-entities/mml_commands.csv` — 新增
> - `data/04-semantic-bridges/` 下 5 个桥接表（scenario_semantic_mapping、delivery_solution_semantic_mapping、semantic_capability_mapping、semantic_config_mapping、semantic_evidence_mapping）
> - `data/09-runtime-validation-risk/` 下 8 个表（runtime_flows、validation_plans、diagnosis_rules、risk_constraints + 4 个 mapping）
> - `data/10-evidence/evidence_claims.csv` — 15 条字段级证据断言

---

## 三、WARNING（逻辑疑问 / 潜在问题）

### W-01: BA.SubjectSemantics 在 Phase1 中缺失

**来源**: `work/02-business-awareness-semantic-profile.md` vs `business-graph/07`

`work/02` 定义了 RuleSemantics 的组合规则：

```
BA.SubjectSemantics + BA.TrafficRecognitionSemantics + BA.PolicyActionSemantics
  + BA.ActivationSemantics + BA.BindingSemantics + BA.PrioritySemantics
  -> BA.RuleSemantics
```

但 Phase1 中 NS-BA-001 使用了 RuleSemantics，却没有使用 SubjectSemantics、PolicyActionSemantics、ActivationSemantics。

对于纯计费场景，可以论证 PolicyActionSemantics 和 ActivationSemantics 不需要（动作就是计费，始终启用）。但 **SubjectSemantics**（"对谁生效"）在计费场景中是核心语义——DeliverySolution 的"生效对象"字段就是在回答这个问题。

**疑问**: SubjectSemantics 是否应纳入 Phase1 的语义对象列表？还是说它被 BindingSemantics 隐含覆盖了？

> **[v0.2 状态: 已修复]** `domain_semantic_objects.csv` 已包含 `BA.SubjectSemantics`，状态为 accepted。构建 Agent v0.2 自审明确采纳此建议，Phase1/Phase2 显式使用 SubjectSemantics。

---

### W-02: 产品文档中的 ConfigObject 遗漏

**来源**: 产品文档验证 vs `business-graph/07`

产品文档"套餐1：计费场景"中明确出现的 ConfigObject：

| 对象 | MML 命令 | 是否在 Phase1 实例中 |
|---|---|---|
| FLTBINDFLOWF | ADD FLTBINDFLOWF | **缺失** |
| PROTBINDFLOWF | ADD PROTBINDFLOWF | **缺失** |
| REFRESHSRV | SET REFRESHSRV | **缺失** |
| FLOWFILTERGRP | ADD FLOWFILTERGRP | ✅ 有 |

FLTBINDFLOWF 和 PROTBINDFLOWF 是过滤器绑定的中间对象，虽然"功能上"是 FlowFilter 的内部组装，但产品文档中是独立的配置步骤。REFRESHSRV 是激活刷新命令。

**疑问**: 这些对象是否应列入 ConfigObject 实例？如果认为它们属于 FlowFilter 的内部实现细节而不单列，需要在文档中显式说明排除理由。

> **[v0.2 状态: 大部分已修复]** `config_objects.csv` 现在包含：
> - `ConfigObject:UDG:FltBindFlowF`（binding 型）— 已补
> - `ConfigObject:UDG:ProtBindFlowF`（binding 型）— 已补
> - REFRESHSRV — 构建 Agent v0.2 自审决定归为操作型命令/激活步骤，不放入持久配置对象（合理决策）
> - 新增 `object_category` 字段区分 `persistent` / `binding` / `operation_anchor` 三类

---

### W-03: NetworkScenario 分拆粒度与产品文档不一致

**来源**: 产品文档 vs `work/03` vs `business-graph/07`

产品文档"套餐1：计费场景"将以下内容作为一个整体场景：
- 按 URL 的专项计费
- 按协议的专项计费
- 免费（零费率）流量
- 默认/回退计费

`work/03` 将其定义为 1 个场景：BA-SC-001 "差异化计费与免流"
`business-graph/07` 拆为 3 个场景：NS-BA-001 差异化计费、NS-BA-002 免费业务、NS-BA-003 默认兜底计费

从 Agent 使用角度看，拆分可能更利于检索和匹配（"客户要免流"可以直接命中 NS-BA-002）。但从业务逻辑角度看，这三者是一个整体——没有差异化计费就不需要兜底，免费是差异化计费的一种费率策略。

构建 Agent 的自审也承认了这个张力（"免费业务未来可考虑作为差异化计费的子场景"）。

**疑问**: 当前的三拆分是最终方案还是临时方案？如果保留三拆分，DS-BA-001 同时覆盖三者，那 NS-BA-002 和 NS-BA-003 作为独立场景的价值是什么？

> **[v0.2 状态: 已决策]** 构建 Agent v0.2 自审决定短期保留三拆分但标注为"场景切片"，后续考虑新增 `scenario_part_of` / `scenario_refines` 关系。同样逻辑也适用于 NS-BA-004/005/006 的关系。此决策合理。

---

### W-04: EngineeringTask 列表与 work/ 原始设计有结构性差异

**来源**: `work/03` vs `business-graph/07` vs `data/engineering_tasks.csv`

| work/03 定义 | business-graph/07 | data/ CSV（含第二条闭包） |
|---|---|---|
| BA-TASK-001 规划生效范围 | 无对应 | 无对应 |
| BA-TASK-002 规划流量识别条件 | TASK-BA-002 设计识别条件 | ✅ |
| BA-TASK-003 规划 Rule 与优先级 | TASK-BA-004 设计 Rule 与优先级 | ✅ |
| BA-TASK-004 规划计费对象 | TASK-BA-003 设计计费动作 | ✅ |
| BA-TASK-005 规划配额耗尽动作 | 无对应(Phase1) | TASK-BA-008 ✅ |
| BA-TASK-006 配置 UserProfile 绑定 | TASK-BA-005 设计套餐绑定 | ✅ |
| BA-TASK-007 验证 CP/UP 一致性 | TASK-BA-006 CP/UP 验收 | ✅ |
| BA-TASK-008 验证终端体验 | 无对应 | TASK-BA-011 ✅ |
| 无 | TASK-BA-001 划分业务类别和优先级 | ✅（新增） |

关键差异：
1. **"规划生效范围"在 business-graph 中消失了** — work/ 认为这是第一个任务（对谁生效），但 business-graph 没有这个任务
2. **"验证终端体验"在 Phase1 中消失了** — 后续在 CSV 中补回为 TASK-BA-011
3. **"划分业务类别和优先级"是 business-graph 新增的** — work/ 中没有这个独立任务

**疑问**: "规划生效范围"是否被吸收进了"设计套餐绑定"（TASK-BA-005）？如果是，是否应该显式标注这种吸收关系？

> **[v0.2 状态: 部分修复]** 构建 Agent v0.2 自审接受此问题，计划用 SubjectSemantics + 后续 Scope/DecisionPoint 补齐。当前 TASK-BA-005 仍然承载了生效范围语义，但有了 SubjectSemantics 的显式实例化，此问题可缓解。

---

### W-05: ID 命名规范不一致

**来源**: `work/03` vs `business-graph/07` vs `data/`

| 对象类型 | work/ 格式 | business-graph 格式 |
|---|---|---|
| NetworkScenario | `BA-SC-001` | `NS-BA-001` |
| ReferencePattern | `BA-RP-001` | `RP-BA-001` |
| DeliverySolution | `BA-DS-001` | `DS-BA-001` |
| EngineeringTask | `BA-TASK-001` | `TASK-BA-001` |

两套命名规范都合理（领域前缀 vs 类型前缀），但混用会造成跨文档引用混乱。CSV 数据使用的是 business-graph 的命名规范。

**建议**: 统一为一套。类型前缀更适合程序化处理（按前缀分文件），建议以 business-graph 的为准，work/ 中标注为历史命名。

> **[v0.2 状态: 已决策]** 构建 Agent v0.2 自审采纳此建议：business-graph 采用类型前缀，work/ 标注为历史命名。

---

### W-06: 5 个 Evidence 条目悬空

**来源**: CSV 一致性检查

以下 Evidence 在 `evidence.csv` 中有定义但未被任何场景/方案/任务/能力/范式引用：

| evidence_id | 标题 |
|---|---|
| EVI-UDG-FEAT-90197552 | GWFD-110101 SA-Basic参考信息 |
| EVI-UDG-BA-92407879 | 业务感知定义 |
| EVI-UDG-BA-92464022 | 规则配置实例 |
| EVI-UDG-BA-94838085 | 套餐2：带宽控制 |
| EVI-UNC-FEAT-74013177 | 激活内容计费 |

其中 `EVI-UDG-FEAT-90197552` 在 MD 文档第 3.10 节被列为第一条闭包使用的证据，但 CSV 体系中无引用——这是 **MD 与 CSV 的不一致**，可能是 CSV 构建时的遗漏。

其余 4 条可能是预定义的（为带宽控制等后续场景准备），如果是这样应标注 `status: reserved`。

> **[v0.2 状态: 已修复]** `evidence.csv` 从 22 行更新到 23 行，状态标注已完善：
> - `EVI-UDG-FEAT-90197552` — 已补引用，在 `evidence_support_mapping.csv` 中有 SUP-034/035/036/037 四条支撑
> - `EVI-UDG-BA-92407879` — 标为 `reserved`
> - `EVI-UDG-BA-92464022` — 标为 `reserved`
> - `EVI-UDG-BA-94838085` — 标为 `reserved`
> - `EVI-UNC-FEAT-74013177` — 已补引用，SUP-038 支撑 WSFD-109002 的 License 约束

---

### W-07: 证据粒度偏"页面摘要"，不支持字段级可复核性

**来源**: 构建自审（11号）+ 审查补充

当前 `evidence.csv` 记录的是一页文档的摘要。对于审查者或 Agent 来说，无法验证某个具体字段值（如"Rule.PRIORITY"的取值范围）是否真的来自该文档。

构建自审已建议引入 `evidence_claims.csv` 做字段级证据。这个建议是合理的，但在当前 MVP 阶段不是阻塞项。

> **[v0.2 状态: 已修复]** `data/10-evidence/evidence_claims.csv` 已创建，包含 15 条字段级断言（CLM-001 到 CLM-015），覆盖 NetworkScenario、Capability、ConfigObject、RiskConstraint、RuntimeFlow、Feature、Evidence 等对象的字段级支撑。每条标注了 `support_level`（direct/inferred/weak）和 `raw_quote_hint`。

---

## 四、QUESTION（需要你判断的设计决策点）

### Q-01: Schema 对象的"最小闭包"边界在哪里？

work/ 定义了 13 个业务图谱对象，但实际实例化的只有 5 个（BusinessDomain、NetworkScenario、ReferencePattern、DeliverySolution、EngineeringTask）。

以下 8 个对象有定义无实例：
- **BusinessGoal** — 目标只作为文本字段出现在 DeliverySolution 中
- **Participant** — 定义了 7 个参与方，但 `involves` 关系从未使用
- **Scope** — 作用范围只出现在 DeliverySolution 文本字段中
- **DecisionPoint** — 完全缺失
- **RuntimeFlow** — 自审承认是"最大 schema 缺口"
- **ValidationPlan** — 验收只作为 EngineeringTask 的语义出现
- **DiagnosisRule** — 同上
- **RiskConstraint** — 风险只出现在 DeliverySolution 的文本字段中

**问题**: 第一阶段的最小闭包是否应该把 RuntimeFlow、ValidationPlan 至少先实例化？因为验收是工程闭环的必要环节，不是可选增强。

> **[v0.2 状态: 已决策并实施]** 构建 Agent 已完成实例化：
> - `runtime_flows.csv` — 2 条（RF-BA-001 计费链运行流程、RF-BA-002 配额耗尽后规则切换流程）
> - `validation_plans.csv` — 4 条（VP-BA-001 计费命中验收、VP-BA-002 默认兜底验收、VP-BA-003 配额耗尽动作验收、VP-BA-004 七层重定向验收）
> - `diagnosis_rules.csv` — 4 条（Rule 未命中、命中未计费、耗尽未重定向、CP/UP 不一致）
> - `risk_constraints.csv` — 4 条（新激活用户生效、刷新约束、CCT 粒度优先级、PCC 性能影响）
> - 4 个 mapping 表全部补齐（delivery_solution_runtime/validation/diagnosis/risk_mapping）
> - BusinessGoal / Participant / Scope / DecisionPoint 仍暂不实例化（合理）

---

### Q-02: Capability 粒度是否需要收敛？

当前 8 个 Capability 中，前 4 个（TrafficRecognition、ContentChargingUP/CP、ConvergedCharging）粒度合理。后 4 个（PccPolicyControlCP、PccPolicyExecutionUP、QuotaExhaustAction、RedirectActionUP）的粒度不一致：
- PccPolicyControlCP/UP 按网元拆分（CP vs UP）
- QuotaExhaustAction 按功能命名（配额耗尽动作）
- RedirectActionUP 按功能+网元命名

构建自审也指出了这个风险。**问题**: Capability 的命名规范是否需要统一？

> **[v0.2 状态: 已决策，延后执行]** 构建 Agent v0.2 自审采纳但不阻塞 P0。建议统一为"动作/控制能力 + 可选网元侧后缀"。当前粒度可支撑闭包审查。

---

### Q-03: 第二条闭包（配额耗尽重定向）的证据强度

构建自审明确指出：

> "这三者共同支撑'配额耗尽后重定向'这个业务理解，但产品文档没有在单页内完整声明它们是一条唯一方案。"

也就是说 DS-BA-002 是跨文档归纳的结果，不是产品文档给出的标准配置模板。

**问题**: 这种"多文档归纳"的 DeliverySolution 在业务图谱中应该标记什么置信度？是否需要区分"产品文档标准模板"和"多文档归纳候选"？

> **[v0.2 状态: 已决策，待实施]** 构建 Agent v0.2 自审采纳，计划给 `delivery_solutions.csv` 增加 `source_type`、`confidence_level`、`evidence_strength_notes` 三个字段。但当前 CSV 中尚未看到这些字段的实际落地。

---

### Q-04: MD 文档与 CSV 数据的职责边界

当前 MD 文档承载了语义关系（`uses_semantic_object`、`semantic_realized_by_config` 等），CSV 只承载实体和简单映射。这导致跨层映射的核心数据只在 MD 中，无法程序化验证。

**问题**: 是否应该把 MD 中的关系数据也落入 CSV？如果是，是否在第一阶段就做？

> **[v0.2 状态: 已决策并实施]** 构建 Agent v0.2 自审决策：核心实体和关系必须 CSV 化，MD 负责解释。当前 `data/` 下已有 11 个子目录、40 个 CSV 文件，MD 中描述的所有跨层关系（包括 `semantic_realized_by_config`、`semantic_requires_capability`、`semantic_verified_by`）均已通过 `04-semantic-bridges/` 和 `08-cross-layer-relations/` 落入 CSV。

---

## 五、确认正确的部分

以下方面经审查确认无误：

1. **Schema 设计方向正确** — 4 子图结构（业务/语义/特性/命令运行）的分层是合理的
2. **DomainSemanticObject 承载机制有效** — 15 个语义对象的定义覆盖了业务感知的主要语义类别
3. **DeliverySolution 不直接连 Feature/ConfigObject 的决策正确** — 通过 Capability 和 EngineeringTask 过渡，避免了业务直接绑定实现的耦合
4. **构建方法论与 Schema 一致** — 01-06 方法论文档没有发明新的 schema 对象，严格遵循 work/ 的设计
5. **CSV 数据 ID 引用完整性** — 所有引用 ID 均有定义，无孤立引用、无重复
6. **配置对象链（UDG/UNC 两侧）正确** — 与产品文档验证一致
7. **第一条闭包（计费主线）的核心结构"较稳"** — 构建自审的判断与本次审查一致

---

## 六、建议优先级（含 v0.2 修复状态）

| 优先级 | 问题编号 | 行动 | v0.2 状态 |
|---|---|---|---|
| **P0 立即修复** | E-01 | 为 DomainSemanticObject、Feature、ConfigObject 及其关系建立 CSV 文件 | **已修复** |
| **P1 本轮补齐** | W-01 | 明确 SubjectSemantics 在 Phase1 中的定位 | **已修复** |
| **P1 本轮补齐** | W-06 | 修复 EVI-UDG-FEAT-90197552 在 CSV 中的缺失引用 | **已修复** |
| **P2 设计确认** | Q-01 | 你决定 RuntimeFlow/ValidationPlan 是否纳入最小闭包 | **已决策并实施** |
| **P2 设计确认** | W-03 | 你决定场景分拆粒度是最终方案还是临时方案 | **已决策（场景切片+后续加关系）** |
| **P3 后续统一** | W-05 | 统一 ID 命名规范 | **已决策** |
| **P3 后续统一** | W-02 | 补齐或显式排除遗漏的 ConfigObject | **大部分已修复** |
| **P3 后续统一** | Q-02/Q-03 | 收敛 Capability 命名规范和证据强度标注 | **已决策，Q-03 待字段落地** |

---

## 七、v0.2 审查总结

构建 Agent 在审查后做了大量高质量修复，v0.2 自审文档（`11-business-awareness-graph-self-audit-v0.2.md`）逐条回应了本报告的所有发现。

### 已完成
- CSV 数据从扁平结构重组为 11 个子目录、40 个文件
- 所有桥接实体（DomainSemanticObject/Feature/ConfigObject/MMLCommand）均已有 CSV 实体表
- 工程闭环对象（RuntimeFlow/ValidationPlan/DiagnosisRule/RiskConstraint）已实例化并有 mapping
- 字段级证据（evidence_claims）已建立
- Evidence 悬空问题已修复，reserved 状态已标注

### 仍需关注
1. **Q-03 待落地**：`delivery_solutions.csv` 尚未增加 `source_type`/`confidence_level` 字段
2. **Q-02 延后**：Capability 命名规范统一未执行，当前粒度可支撑审查但不适合长期维护
3. **可视化需同步**：`visualization.html` 基于旧数据构建，需要用新的 40 个 CSV 文件重新生成节点和边
