# 业务感知业务图谱构建策略 v0.1

## 1. 前提判断

业务图谱和命令图谱、特性图谱不一样。

命令图谱和特性图谱有较稳定的文档章节结构：

- 命令有：
  - 命令功能
  - 参数说明
  - 使用实例
- 特性有：
  - 特性概述
  - 激活
  - 配置/部署
  - 调测
  - 参考信息

但业务图谱没有一套固定章节可以直接抽。

尤其对“业务感知”来说，业务知识会散落在：

- 业务专题
- 5G 基础知识 / 一望5G
- UDG 业务感知相关特性
- UNC PCC/计费/融合计费/热计费/离线计费特性
- 命令对象链
- 参考信息、软参、告警

所以业务图谱不应该理解成：

```text
把业务专题里的章节改写成图谱
```

而应该理解成：

```text
一线工程师基于多处文档知识，归纳出的业务实现认知
```

同时要明确：

```text
最终目标不是一个最小MVP，
而是“业务感知”这个场景下尽可能完整的业务图谱。
```

只是当前不能一次性构建完整全景，所以必须采用：

```text
全景目标明确
但按小步闭包迭代扩展
```

## 2. 当前业务图谱的输入

当前业务图谱建立在三类输入之上。

### 2.1 来自命令图谱的输入

提供：

- 配置对象族
- 命令对象链
- 对象间关系
- 哪些对象可以形成一条可执行配置闭包

例如：

```text
FlowFilter / L7Filter / Rule / RuleBinding / UserProfile
URR / URRGroup / PccPolicyGrp / Rule / RuleBinding / UserProfile
```

这里以原始命令文档为最终依据。  
命令图谱已有结果只能作为候选索引和回查线索，不能替代原始语料。

当前可作为回查线索：

- `work/business-awareness-result/09-command-graph-build-plan-v0.2.md`
- `work/business-awareness-result/10-command-graph-extraction-pipeline-v0.1.md`
- `command-graph/` 目录下已有代码和 `stage1` 结果

### 2.2 来自特性图谱的输入

提供：

- 哪些特性与业务感知相关
- 特性能力
- 特性可获得性
- 典型配置路径
- 依赖和限制

例如：

- `GWFD-110101 SA-Basic`
- `GWFD-020301 内容计费基本功能`
- `WSFD-011206 支持融合计费`
- `WSFD-011202 支持热计费功能`
- `WSFD-011201 支持离线计费`

这里同样以原始特性文档为最终依据。  
特性图谱已有结果只能作为候选索引和回查线索，不能替代原始语料。

当前可作为回查线索：

- `work/business-awareness-result/11-feature-layer-corrections-v0.1.md`
- `work/business-awareness-result/12-feature-graph-extraction-pipeline-v0.1.md`
- `work/business-awareness-result/16-feature-tree-index-plan-v0.1.md`

### 2.3 来自业务感知语义层的输入

提供：

- 流量识别语义
- 规则语义
- 计费语义
- 配额语义
- 动作语义
- 验收/诊断语义

这些定义见：

- [work/business-awareness-result/02-business-awareness-semantic-profile.md](../work/business-awareness-result/02-business-awareness-semantic-profile.md)

## 3. 业务图谱当前不应该先做什么

### 3.1 不做“业务感知全景图”成品

因为当前没有足够稳定的边界，直接画全景只会很虚。

### 3.2 不做“业务专题目录 = 业务图谱”

因为业务专题只是产品文档里的参考材料，不是现网业务全景。

### 3.3 不先做“跨网元终极方案库”

因为当前只有 UDG/UNC 两个网元文档，且没有专家现网方案和配置指导手册。

### 3.4 不把第一条最小闭包误当成最终范围

第一条闭包只是起步样板，不是业务感知业务图谱的最终边界。

## 4. 当前业务图谱先构建什么

当前先构建 5 类核心内容。

### 4.1 `NetworkScenario`

也就是业务子场景。

对业务感知，第一批建议只收：

- 差异化计费
- 默认兜底计费
- 配额耗尽重定向
- URL/域名访问限制
- 带宽控制

这些不是最终方案，只是业务感知下稳定可讨论的场景类型。

### 4.2 `DomainSemanticObject` 的场景化实例

也就是把语义对象真正落到场景里。

例如对“差异化计费”这个场景：

- 流量识别语义：某类 URL / Host / App / IP 流
- 规则语义：识别条件 + 优先级 + 命中动作
- 计费语义：独立 RG / 默认 RG / 免费 / 兜底
- 绑定语义：用户模板 / DNN / 用户范围

### 4.3 `DeliverySolution` 候选

不是现网定稿，而是：

```text
基于产品文档归纳的可落地方案候选
```

例如：

- UDG 负责识别和执行
- UNC 负责 PCC/计费/融合计费控制
- 使用哪条对象链
- 需要哪些特性
- 如何验收

### 4.4 `EngineeringTask`

也就是一线真正能执行的任务。

例如：

- 规划业务识别范围
- 规划默认策略和差异策略
- 选择 UDG 识别路径
- 选择 UNC 计费路径
- 配置对象链
- 验收 N4/N40/话单/现象

### 4.5 业务感知相关特性/命令覆盖面

除了场景、语义、方案、任务，还要逐步形成：

```text
业务感知场景 -> 相关特性集合
业务感知场景 -> 相关命令/对象链集合
```

它们不是重新定义特性图谱和命令图谱，而是从全景结果中筛出业务感知主线子集。

## 5. 当前业务图谱的模块划分

当前先拆成 5 个模块。

### 5.1 场景模块

回答：

```text
现网到底在解决什么问题
```

产物：

- `network_scenarios.csv`

### 5.2 语义模块

回答：

```text
这个场景在业务感知语义层到底由哪些语义对象组成
```

产物：

- `scenario_semantic_mapping.csv`

### 5.3 方案模块

回答：

```text
从语义到特性、命令、运行证据，怎么形成可落地方案
```

产物：

- `delivery_solutions.csv`
- `delivery_solution_capability_mapping.csv`
- `feature_capability_mapping.csv`
- `delivery_solution_task_mapping.csv`
- `engineering_task_config_mapping.csv`

### 5.4 验收诊断模块

回答：

```text
方案上线后怎么确认、出问题怎么回查
```

产物：

- `validation_plans.csv`
- `diagnosis_rules.csv`

### 5.5 覆盖面模块

回答：

```text
业务感知主线到底涉及哪些特性和命令
```

产物：

- `business_related_features.csv`
- `business_related_commands.csv`
- `business_related_object_chains.csv`

## 6. 哪些可以用代码，哪些不能

业务图谱比前两层更依赖 Agent，但仍然不是全人工。

### 6.1 可以代码化的部分

#### A. 文档候选索引

可以先批量索引与业务感知相关的原料：

- UDG 业务感知专题
- UDG 业务感知相关特性
- UNC 融合计费/热计费/离线计费/PCC
- 5G 基础知识中的业务感知章节

输出：

- `business_source_index.csv`

#### B. 特性和命令反查

基于前两层已有结果，可以代码产出：

- 某场景候选相关特性清单
- 某特性关联命令清单
- 某对象链闭包

#### C. 业务感知相关特性/命令候选筛选

利用：

- `command-graph/` 的 `command_source_index.csv`
- `command-graph/data/stage1/` 的对象、动作、候选关系表
- 后续特性层 `features.csv` / `feature_files.csv`

代码可以先筛出：

- 业务感知相关命令候选集
- 业务感知相关配置对象候选集
- 业务感知相关特性候选集

#### D. 审查包生成

业务图谱也可以代码生成：

- 小闭包图
- 场景对象表
- 方案映射表

### 6.2 必须 Agent 做的部分

#### A. 场景归纳

“差异化计费”“默认兜底计费”“URL过滤”这些不是目录显式字段，必须归纳。

#### B. 语义实例化

比如“这个场景的流量识别语义到底是什么”，必须 Agent 解释。

#### C. 方案归并

同一个场景可能有多条产品路径，Agent 要做方案候选归并。

#### D. 验收与诊断链

这本质上是一线经验式推理，哪怕当前只基于产品文档，也必须 Agent 来总结。

#### E. 业务感知相关特性/命令的最终归并

哪些特性和命令真正属于业务感知主线，哪些只是外围支撑，必须 Agent 结合上下文判断。

## 7. 建议的业务图谱 pipeline

当前不建议一上来做全量业务图谱。建议拆成 4 段。

### 7.1 Source Index Pipeline

输入：

- 业务专题
- 5G 基础知识
- 相关特性
- 命令图谱/特性图谱结果

输出：

- `business_source_index.csv`
- `business_related_features_candidates.csv`
- `business_related_commands_candidates.csv`

作用：

先固定业务图谱原料池和业务感知相关工作面。

### 7.2 Scenario Discovery Pipeline

以 Agent 为主，代码辅助。

输入：

- `business_source_index.csv`
- 特性图谱结果
- 命令图谱结果

输出：

- `network_scenarios.csv`

作用：

先把业务感知拆成稳定业务子场景。

### 7.3 Solution Closure Pipeline

以 Agent 为主。

输入：

- `network_scenarios.csv`
- 业务感知语义定义
- 特性图谱
- 命令图谱

输出：

- `delivery_solutions.csv`
- `delivery_solution_capability_mapping.csv`
- `feature_capability_mapping.csv`
- `delivery_solution_task_mapping.csv`
- `engineering_task_config_mapping.csv`

作用：

给每个场景形成“文档归纳方案候选”。

### 7.4 Validation & Diagnosis Pipeline

以 Agent 为主，代码生成审查面。

输出：

- `validation_plans.csv`
- `diagnosis_rules.csv`
- 小闭包 review 页面

## 8. 业务感知全景扩展路线

当前第一条最小闭包只是起点。

业务感知业务图谱最终要逐步扩展到更完整的覆盖面，建议按下面路线推进：

### Phase 1：计费主线

```text
差异化计费
默认兜底计费
免费/独立RG
融合计费相关对象链
```

### Phase 2：配额与动作主线

```text
配额耗尽重定向
配额耗尽阻断
继续转发
相关启用条件和验收链
```

### Phase 3：七层识别与访问控制主线

```text
URL/Host/Path识别
访问限制
七层重定向
规则优先级与兜底
```

### Phase 4：体验与增强主线

```text
带宽控制
头增强
安全增强/防欺诈
相关限制和环境依赖
```

### Phase 5：业务感知全景收口

```text
收口业务感知相关特性全集
收口业务感知相关命令/对象链全集
收口业务感知主要场景全集
形成完整业务感知业务图谱工作面
```

这里的“全景”并不代表现网一切都穷尽，而是：

```text
在当前产品文档边界内，
把业务感知主线涉及的主要场景、特性、命令和闭包尽可能收全。
```

## 9. 第一批建议怎么做

当前不要全量做业务感知业务图谱。

建议第一批只打一个最小业务闭包：

```text
差异化计费 + 默认兜底计费
```

原因：

1. 它能连接：
   - 流量识别
   - 规则语义
   - 计费语义
   - UDG 对象链
   - UNC 对象链
2. 它比“只做URL过滤”更能代表业务感知主线
3. 它还能自然延伸到：
   - 配额耗尽重定向
   - 免费 / 默认收费
   - 融合计费

这一步的意义不是“范围定死”，而是：

```text
用一条最容易打穿的主线建立第一批闭包和工作方法，
然后逐步扩到整个业务感知。
```

## 10. 当前最合理的推进顺序

当前建议顺序如下：

1. 固定业务图谱使用的原始语料目录和证据索引机制
2. 直接回查原始命令、特性、业务专题文档，筛出业务感知相关命令/对象候选集
3. 从业务感知专题、基础知识、相关特性中建 `business_source_index.csv`
4. 让 Agent 从原料池中归纳第一批 `NetworkScenario`
5. 每次只选一条主线做闭包
6. 审查闭包后，沿 Phase 1 -> Phase 5 路线逐步扩展

## 11. 当前结论

业务图谱当前不该理解成“抽文档章节”，而该理解成：

```text
一线工程师基于业务感知相关文档，
自己归纳出的：
  场景
  语义
  方案
  任务
  验收诊断
```

所以它的构建策略应该是：

```text
命令和特性先打地基
业务图谱按场景和闭包逐步归纳
先做最小闭包，但规划始终面向整个业务感知全景扩展
代码先做原料索引、候选筛选、审查包
Agent 负责场景、语义、方案、诊断和相关特性/命令归并
```
