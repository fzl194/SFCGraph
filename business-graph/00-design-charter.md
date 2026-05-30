# 业务图谱结构设计讨论

## 1. 讨论目标

本目录要完成以下工作：

1. **确定保留哪些对象类型** — 哪些节点是图谱必需的，哪些应该删除或合并
2. **定义每个对象之间的关系（边）** — 对象之间有哪些连接，边的方向和含义
3. **定义每个对象的内部 schema（属性）** — 每个对象类型有哪些字段，字段类型和约束
4. **明确业务图谱如何被使用** — 谁用、怎么用、用于配置核查和配置生成

讨论结束后应产出完整的 schema 定义（对象 + 边 + 属性），而非继续在"业务感知"单一域上迭代。

## 2. 为什么现在需要讨论

业务图谱当前的 17 个对象类型是在"业务感知"单一域上迭代出来的（v1→v10→final_v2）。迭代过程中发现了若干结构性问题：

1. ReferencePattern 与 DeliverySolution 边界模糊
2. EngineeringTask 全部偏规划态
3. DecisionPoint 被硬挂在 DeliverySolution 下但实际跨方案
4. RuntimeFlow 只有一条中性主链，场景差异被注释掩盖
5. Participant / Scope / DecisionPoint 在 CSV 数据层未独立实体化

这些问题在"业务感知"单一域内还能容忍，但如果业务图谱要面向多个域（故障管理、切片管理、安全防护等），就必须回答：

> 当前结构是"通用骨架"还是"业务感知专属模板"？

## 3. 输入材料

### 3.1 已有图谱材料

| 材料 | 位置 | 提供什么 |
|------|------|----------|
| 当前 schema 定义与实例 | `myoutput/business-awareness-graph/19-*-final_v2.md` | 17 个对象、关系、业务感知实例 |
| 单案例实例化验证 | `myoutput/business-awareness-graph/21-*-single-case-by-schema.md` | 用真实案例走一遍 schema |
| schema 对齐审计 | `business-graph/12-schema-alignment-audit-v0.1.md` | 哪些对象落地了、哪些没落地 |
| 自查与演进方案 | `business-graph/11-business-awareness-graph-self-audit-v0.2.md` | 当前状态、已确认错误、设计决策点 |
| 构建策略 | `business-graph/01-business-graph-build-strategy-v0.1.md` | 业务图谱构建方法论 |
| 初始骨架 | `myoutput/business-awareness-graph/03-global-graph-skeleton.md` | 最早期的骨架设计 |

### 3.2 原始语料入口

| 路径 | 类型 | 说明 |
|------|------|------|
| `output/UDG_Product_Documentation_CH_20.15.2` | 原始语料目录 | UDG 产品文档（用户面） |
| `output/UDG_Product_Documentation_CH_20.15.2/OM参考/命令/UDG MML命令` | 命令目录 | UDG 正式命令入口 |
| `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南` | 特性目录 | UDG 正式特性入口 |
| `output/UNC 20.15.2 产品文档(裸机容器) 05` | 原始语料目录 | UNC 产品文档（控制面） |
| `output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令` | 命令目录 | UNC 正式命令入口 |
| `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署` | 特性目录 | UNC 正式特性入口 |

## 4. 讨论文件索引

| 文件 | 状态 | 内容 |
|------|------|------|
| `01-current-structure-analysis.md` | 已完成 | 对当前 17 个对象的结构性分析（合理性 + 普适性） |
| `02-usage-scenarios.md` | 已完成 | 业务图谱的使用场景与使用者分析 |
| `03-schema-design.md` | 待建 | 逐对象讨论：保留/删除决策、边定义、内部属性定义 |
| `04-schema-final.md` | 待建 | 最终 schema 定义（对象 + 边 + 属性） |

## 5. 业务图谱定位

业务图谱是**核心资产**，同时服务于配置核查和配置生成，不是只供人类阅读的知识库。

### 5.1 双通道使用模型

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

- **代码底座**：能沉淀为代码的能力，封装为可复用的代码模块（如配置核查规则、对象链遍历、参数填充模板）
- **Agent 接口**：无法用代码表达的语义理解、推理、判断，通过 LLM Agent 使用
- **人类界面**：Agent 和人类都可复用代码底座的能力

### 5.2 使用场景优先级

配置核查和配置生成**并重**，不存在先后顺序。Schema 设计必须同时满足两者的要求：

| 使用场景 | 核心要求 | 访问方式 |
|----------|----------|----------|
| 配置核查 | ValidationPlan / DiagnosisRule / RiskConstraint 可程序执行 | 代码底座 + Agent |
| 配置生成 | DomainSemanticObject → Feature → ConfigObject 映射精确 | 代码底座 + Agent |
| 方案推荐 | Scenario → Solution → DecisionPoint 链路完整 | Agent + 人类 |
| 知识问答 | 对象关系可查询、Evidence 可追溯 | Agent + 人类 |

## 6. 约束

1. 讨论必须结合项目中的真实材料，不空谈
2. 每个结论都要说明依据来自哪个文件
3. "普适性"不是要求所有域完全一致，而是要求核心结构可复用、域差异可扩展
4. 最终 schema 必须能回答"怎么用"的问题，不能只有结构定义
5. Schema 设计必须同时支撑代码底座和 Agent 接口两种使用方式
