# 业务图谱使用场景分析

## 1. 分析目的

Schema 设计不能脱离使用场景。不同的使用方式对结构的要求不同：

- 如果主要用于**人类阅读理解**，那扁平的文档式结构就够了
- 如果主要用于 **Agent 配置生成**，那 Task → ConfigObject 的映射必须精确
- 如果主要用于 **Agent 配置核查**，那 ValidationPlan / DiagnosisRule 必须可程序执行
- 如果主要用于**方案设计**，那 DecisionPoint / Scope 必须独立且可组合

## 2. 业务图谱定位

### 2.1 核心资产

业务图谱不是辅助知识库，是**核心资产**。它同时服务于配置核查和配置生成，二者并重：

- **配置核查**：给定配置，验证是否满足业务意图
- **配置生成**：给定业务需求，生成完整配置

### 2.2 双通道使用模型

```
                    ┌─────────────────────┐
                    │     业务图谱         │
                    │   (核心资产)          │
                    └────────┬────────────┘
                             │
                ┌────────────┼────────────┐
                ▼            ▼            ▼
         ┌──────────┐ ┌──────────┐ ┌──────────┐
         │ 代码底座  │ │ Agent接口 │ │ 人类界面  │
         └──────────┘ └──────────┘ └──────────┘
```

**代码底座**（可沉淀为代码的能力）：
- 配置核查规则引擎（ValidationPlan → 可执行检查脚本）
- 对象链遍历器（ConfigObject 链路完整性检查）
- 参数填充模板（ConfigObject → 参数 → 值域）
- 约束断言器（RiskConstraint → 可执行断言）

**Agent 接口**（需要 LLM 推理的能力）：
- 业务意图解析（自然语言 → DomainSemanticObject）
- 方案推荐与决策遍历
- 故障定位推理（异常现象 → 排障路径）
- 知识问答（语义关系查询）

**关键原则**：代码底座是 Agent 和人类的共享能力层。Agent 不重复实现代码底座已覆盖的能力，而是调用它们。

### 2.3 原始语料入口

业务图谱的原始语料来自两套产品文档：

| 产品 | 命令入口 | 特性入口 |
|------|----------|----------|
| UDG（用户面） | `output/UDG_.../OM参考/命令/UDG MML命令` | `output/UDG_.../特性部署/特性指南` |
| UNC（控制面） | `output/UNC_.../OM参考/命令/UNC MML命令` | `output/UNC_.../网络部署/特性部署` |

Schema 设计必须能从这些原始语料中系统性地抽取知识。

## 3. 使用者分析

### 3.1 人类使用者

| 角色 | 需要什么 | 对 schema 的影响 |
|------|----------|-----------------|
| 一线工程师 | "我要做一个差异化计费，该怎么做？" | Scenario → Solution → Task 的链路必须清晰，Task 必须包含可执行步骤 |
| 方案设计师 | "这个场景有哪些决策点？选不同分支会怎样？" | DecisionPoint 必须独立，选项和影响必须明确 |
| 运维工程师 | "业务没按预期生效，先查哪里？" | DiagnosisRule 必须按异常现象组织，检查点必须具体到对象 |
| 技术Leader | "业务感知这个域能力全景是什么？" | Domain → Scenario → Feature 的覆盖面必须完整 |

### 2.2 Agent 使用者

| 场景 | 需要什么 | 对 schema 的影响 | 访问方式 |
|------|----------|-----------------|----------|
| 配置生成 | "给定一个业务需求描述，生成配置脚本" | DomainSemanticObject 的语义映射必须精确，ConfigObject 对象链必须完整 | 代码底座 + Agent |
| 配置核查 | "给定一段配置，检查是否满足业务意图" | ValidationPlan 必须可程序化执行，RiskConstraint 必须可检查 | 代码底座 + Agent |
| 方案推荐 | "给定一线需求，推荐最合适的方案" | Scenario → Solution 的映射必须完整，DecisionPoint 必须可遍历 | Agent |
| 故障定位 | "给定异常现象，给出排障路径" | DiagnosisRule 必须结构化（现象→检查点→判断逻辑） | 代码底座 + Agent |
| 知识问答 | "SA 的 Filter 和 L7Filter 是什么关系？" | DomainSemanticObject 之间的关系必须可表达 | Agent |

## 3. 从使用场景反推 schema 需求

### 3.1 "配置生成"对 schema 的硬要求

配置生成是最严格的使用场景。它要求：

1. **业务意图 → 语义对象**的映射必须无歧义
   - "A 网站视频免费" → `BA.FilterCondition` + `BA.Charging`
   - 如果 DomainSemanticObject 定义不清，Agent 无法判断该用哪个语义单元

2. **语义对象 → Feature** 的承载关系必须明确
   - `BA.FilterCondition` 由 `SA-Basic` 承载
   - `BA.Charging` 由 `PCC基本功能 + 内容计费 + 融合计费` 共同承载

3. **Feature → ConfigObject** 的对象链必须可遍历
   - `融合计费` → `CCT → CHFINIT → CTXSTARTRATING → URR → URRGroup → PCCPolicyGrp → Rule`
   - 如果对象链断裂，生成的配置就不完整

4. **ConfigObject 的参数必须可填充**
   - 当前 schema 只有对象名（如 `URR`），没有参数（如 `URR.ID`、`URR.USAGERPTMODE`）
   - `12-schema-alignment-audit` 也指出了 `CommandParameter` "未对齐"

**结论**: 如果要支持配置生成，当前 schema 在 ConfigObject 层的粒度不够。

### 3.2 "配置核查"对 schema 的硬要求

配置核查要求 ValidationPlan 和 RiskConstraint 可程序化：

1. **ValidationPlan 必须可转为检查脚本**
   - "差异化计费验证" → 检查 Rule 是否绑定 URR，URR 是否绑定正确费率
   - 当前 ValidationPlan 是自然语言描述，Agent 需要额外推理才能转为检查步骤

2. **RiskConstraint 必须可转为断言**
   - "CP/UP URR 配置必须一致" → 比对两侧 URR 名称和属性
   - 当前 RiskConstraint 也是自然语言

3. **DiagnosisRule 必须可转为排障流程**
   - "业务流未进入专项计费" → 先查 Rule→PCCPolicyGrp→URRGroup→URR 链
   - 当前 DiagnosisRule 有"优先检查点"字段，方向对但不够精确

**结论**: 如果要支持配置核查，ValidationPlan / DiagnosisRule / RiskConstraint 需要更结构化的表达。

### 3.3 "方案推荐"对 schema 的硬要求

方案推荐要求：

1. **Scenario → Solution 映射完整**
   - 每个场景至少有一个推荐方案
   - 场景之间的交叉（如 NS-04 + NS-01）必须可表达

2. **DecisionPoint 可遍历**
   - Agent 需要按序遍历每个决策点，给出推荐选项
   - 当前 DecisionPoint 的选项是枚举的，但"推荐默认值"缺失

3. **Scope 可匹配**
   - Agent 需要把一线需求中的"对谁生效"匹配到具体 Scope
   - 当前 Scope 只有类型枚举，没有匹配规则

### 3.4 "知识问答"对 schema 的硬要求

知识问答要求：

1. **对象之间的语义关系可查询**
   - "Filter 和 L7Filter 什么关系？" → 需要 DomainSemanticObject 之间的关系
   - 当前语义对象之间没有正式关系表

2. **Evidence 可追溯**
   - "这个结论的依据是什么？" → 需要对象 → Evidence 的映射
   - 当前有 `evidence_support_mapping.csv`，但粒度偏粗

## 4. 使用场景优先级

业务图谱是核心资产，配置核查和配置生成**并重**。Schema 设计必须同时满足两者的要求。

### 4.1 核心使用场景（必须同时支撑）

| 使用场景 | 核心要求 | 代码底座能力 | Agent 能力 |
|----------|----------|-------------|-----------|
| **配置核查** | ValidationPlan / DiagnosisRule / RiskConstraint 可程序执行 | 核查规则引擎、对象链遍历器、约束断言器 | 推理核查结果、定位异常根因 |
| **配置生成** | 业务意图 → 语义对象 → Feature → ConfigObject 全链路精确 | 参数填充模板、对象链组装器、配置语法生成 | 意图解析、方案选择、参数推理 |

### 4.2 辅助使用场景（Schema 必须支持但不作为主要设计驱动力）

| 使用场景 | 核心要求 |
|----------|----------|
| 方案推荐 | Scenario → Solution → DecisionPoint → Scope 链路完整 |
| 知识问答 | 对象关系可查询、Evidence 可追溯 |
| 故障定位 | DiagnosisRule 结构化（现象 → 检查点 → 判断逻辑） |

### 4.3 设计原则

1. **配置核查**和**配置生成**共享大部分 schema 对象，区别在于使用方式：
   - 核查：从 ConfigObject 反向遍历到业务意图
   - 生成：从业务意图正向遍历到 ConfigObject
2. 代码底座优先：能沉淀为代码的能力，不依赖 LLM
3. Schema 必须是**双向可遍历的**：既支持正向（生成），也支持反向（核查）

## 5. 从使用场景反推的 schema 改进建议

### 5.1 必须改进（支撑配置核查 + 配置生成）

配置核查和配置生成共享同一套 schema，要求正向和反向都可遍历：

1. **ConfigObject 参数级展开**：对象 → 参数 → 值域
   - 核查需要：检查参数值是否合规
   - 生成需要：填充参数值
2. **对象链可执行化**：对象间的 references/binds/contains 关系精确到参数级
   - 核查需要：验证链路完整性
   - 生成需要：按序组装对象
3. **DomainSemanticObject 语义映射精确化**：业务意图 ↔ 语义对象 ↔ Feature 无歧义
   - 核查需要：从配置反推业务意图
   - 生成需要：从业务意图正推配置
4. **ValidationPlan 结构化**：从自然语言拆成"观察什么对象 → 判断什么条件 → 预期什么结果"
   - 可沉淀为代码底座的核查规则引擎
5. **RiskConstraint 结构化**：从自然语言拆成"约束条件 → 影响范围 → 检查方法"
   - 可沉淀为代码底座的约束断言器
6. **DecisionPoint 独立化**：允许挂在 Scenario / Solution / Domain 级别
   - 正向：方案推荐时遍历决策点
   - 反向：从已有配置推断决策路径

### 5.2 建议改进（提升易用性）

1. **DiagnosisRule 结构化**：从自然语言拆成"异常现象 → 检查步骤序列 → 判断逻辑"
2. **Scope 匹配规则**：不只是枚举类型，还要有"如何从需求描述匹配到 Scope"
3. **Scenario → Solution 映射完整性**：每个场景至少一个方案
4. **Evidence 粒度细化**：从文档级到段落级，支撑可追溯性

### 5.3 代码底座能力规划

根据 schema 改进方向，可以沉淀为代码的底座能力：

| 代码底座能力 | 依赖的 schema 改进 | 服务于 |
|-------------|-------------------|--------|
| 配置核查规则引擎 | ValidationPlan 结构化、RiskConstraint 结构化 | 配置核查 |
| 对象链遍历器 | 对象链可执行化 | 配置核查 + 配置生成 |
| 参数填充模板 | ConfigObject 参数级展开 | 配置生成 |
| 约束断言器 | RiskConstraint 结构化 | 配置核查 |
| 配置语法生成器 | ConfigObject 参数级展开 + 对象链可执行化 | 配置生成 |
