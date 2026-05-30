# 当前结构分析

## 1. 分析对象

以 `myoutput/business-awareness-graph/19-*-final_v2.md` 为基准，分析当前 17 个对象类型的合理性和普适性。

## 2. 当前结构总览

```
业务层（5）:  BusinessDomain / NetworkScenario / ReferencePattern / DeliverySolution / EngineeringTask
支撑层（8）:  Participant / Scope / DecisionPoint / RuntimeFlow / ValidationPlan / DiagnosisRule / RiskConstraint / Evidence
桥接层（3）:  DomainSemanticObject / Feature / ConfigObject
```

关系主链：
```
BusinessDomain → NetworkScenario → ReferencePattern → DeliverySolution → EngineeringTask
```

## 3. 逐对象分析

### 3.1 BusinessDomain（业务域）

**合理性**: ✅ 无争议
- 一个业务域作为图谱的根对象，限定讨论边界

**普适性**: ✅ 通用
- 任何业务域都可以作为根：业务感知、故障管理、切片管理、安全防护……

**开放问题**: 无

---

### 3.2 NetworkScenario（现网场景）

**合理性**: ✅ 成立
- "一线遇到的需求类型或问题情境"——这个定义准确
- 4 个一级场景（计费/带宽控制/访问限制/本地分流）来自原始语料

**普适性**: ⚠️ 名称可能有歧义
- "现网场景"这个中文名在非运营商语境下可能不好理解
- 故障管理域下的"场景"可能是"告警风暴"、"业务中断"、"性能劣化"——这些确实是场景
- 切片管理域下的"场景"可能是"eMBB 切片部署"、"URLLC 切片保障"——也是场景

**开放问题**:
1. 场景的划分粒度是否需要约束？（当前 4 个是手动归纳的，没有规则）
2. 场景之间是否允许交叉？（DS-05 同时覆盖 NS-04 和 NS-01）

---

### 3.3 ReferencePattern（产品参考范式）

**合理性**: ⚠️ 有问题

问题 1：RP 和 DS 边界模糊
- RP-03"计费场景样板" vs DS-01"差异化计费组合方案"——内容高度重叠
- RP-07"融合计费会话闭环样板" vs DS-02"配额耗尽后体验切换方案"——覆盖内容交叉

问题 2：RP 的真正作用是"证据结构"
- 从 `03-global-graph-skeleton.md` 看，最初只有 2 个 RP
- 到 final_v2 扩展到 9 个，扩展方向是**每个场景配一个样板**
- 本质上 RP = "从哪组文档中学到了什么结构"

问题 3：换个业务域 RP 还成立吗？
- "故障管理"域的参考材料可能不是"产品文档样板"，而是"故障案例库"、"运维 SOP"
- "切片管理"域的参考材料可能不是"套餐样板"，而是"切片模板"、"SLA 规范"

**普适性**: ⚠️ 名称和定位都偏"产品文档"范式

**建议选项**:

| 选项 | 做法 | 优点 | 缺点 |
|------|------|------|------|
| A. 保留但重新定义 | 把 RP 重新定义为"可复用知识结构"，不限定来源 | 变化小 | 和 DS 的区分仍然模糊 |
| B. 降级为 Evidence 的属性 | 取消 RP 独立对象，把"样板知识"变成 Evidence 的分类 | 减少对象数 | 丢失了"可复用结构"这个概念 |
| C. 合并到 DeliverySolution | RP 变成 DS 的 `pattern_source` 字段 | 简化主链 | 失去独立表达力 |

---

### 3.4 DeliverySolution（交付方案）

**合理性**: ✅ 成立
- "针对某个场景形成的可落地方案闭包"——这个定义准确
- 5 个方案对象（DS-01~DS-05）确实是从原始语料归纳的

**普适性**: ⚠️ "交付"这个词有偏向性
- "交付方案"隐含"给客户交付"的场景
- 故障管理域下更像是"处置方案"或"恢复方案"
- 切片管理域下更像是"部署方案"或"调整方案"

**开放问题**:
1. 是否应该用更中性的名字，如"Solution"或"SolutionCandidate"？
2. 一个方案允许跨场景吗？（DS-05 跨 NS-04 和 NS-01）

---

### 3.5 EngineeringTask（工程任务）

**合理性**: ⚠️ 偏规划态

当前 11 个 TASK 全部是"规划xxx"：
- 规划生效范围、规划识别条件、规划 Rule、规划计费对象、规划配额耗尽动作……

但 `01-business-graph-build-strategy-v0.1.md` 原始设计里 TASK 包括三类：
1. 规划态：规划业务识别范围、选择识别路径
2. 执行态：配置对象链
3. 验证态：验收 N4/N40/话单/现象

当前缺了后两类。原因可能是 Participant / Scope / DecisionPoint 没有独立实体化，导致执行和验证的细节被嵌在规划描述里。

**普适性**: ⚠️ 如果全是"规划xxx"，换一个域可能更好——故障管理的 TASK 应该是"隔离故障→执行恢复→验证业务"

**建议选项**:

| 选项 | 做法 | 优点 | 缺点 |
|------|------|------|------|
| A. 保持扁平 | TASK 不分类，允许混合规划/执行/验证 | 简单 | 无法区分任务性质 |
| B. 分阶段标记 | TASK 加 `phase` 字段：plan / execute / verify | 保持一个对象类型但可区分 | 需要额外约定 |
| C. 拆成三种对象 | PlanTask / ExecuteTask / VerifyTask | 类型明确 | 增加对象数 |

---

### 3.6 Participant（参与方）

**合理性**: ✅ 成立
- 12 个参与方（用户/PCF/SMF/UPF/CHF/AMF/UDM/RAN/AF-NEF/CTF-NCG/本地DN/业务服务器）

**普适性**: ✅ 通用
- 任何跨网元协同的业务域都有参与方

**注意点**: 在 `12-schema-alignment-audit` 中状态为"未对齐"——没有 CSV 表，只存在于 md 中

**开放问题**: 是否需要区分"必须参与"和"可选参与"？

---

### 3.7 Scope（生效范围）

**合理性**: ✅ 成立
- 7 种范围粒度（用户级/用户组级/整机级/APN-DNN/UserProfile/PRA-位置/切片）

**普适性**: ⚠️ 域特定
- "APN/DNN"、"UserProfile"、"PRA"这些范围类型是 SA 域特有的
- 故障管理域的范围可能是"网元级"/"单板级"/"链路级"
- 切片管理域的范围可能是"切片级"/"子网级"/"租户级"

**建议**: Scope 应该保留为通用对象类型，但允许每个域定义自己的范围粒度枚举

---

### 3.8 DecisionPoint（决策点）

**合理性**: ⚠️ 挂载位置有问题

当前挂在 DeliverySolution 下，但实际跨方案：
- "规则供给方式选择"（预定义/动态/本地）影响所有方案
- "计费粒度选择"影响 NS-01 和 DS-05
- "计费方式选择"影响 NS-01 和 DS-02/DS-05

**普适性**: ✅ 通用
- 任何业务域都有决策分支

**建议**: DecisionPoint 应该允许挂在 Scenario、Solution 或 Domain 级别

---

### 3.9 RuntimeFlow（运行流程）

**合理性**: ⚠️ 一条中性主链不够

final_v2 用一条 9 阶段中性链表达所有场景的运行流程：
```
策略生成 → 执行通路建立 → 报文到达 → 解析识别 → 规则匹配 → 策略执行 → 数据转发 → Usage上报
```

但实际每个场景的后段完全不同：
- 计费：Trigger→配额→重授权闭环
- 分流：DNN/位置→UL CL 插入→会话改写
- 访问限制：Filter 命中→PCCActionProp→阻断/重定向
- 带宽控制：QoS Flow 建立→PFS/QFI 映射→RAN 调度

用一条链 + 注释的方式，关键差异被压在注释里了。

**普适性**: ⚠️ 不同域的 RuntimeFlow 结构可能完全不同
- 故障管理：告警关联→根因定位→隔离→恢复→验证
- 切片管理：需求解析→资源分配→切片创建→监控→弹性调整

**建议选项**:

| 选项 | 做法 | 优点 | 缺点 |
|------|------|------|------|
| A. 保持中性主链 + 场景分支 | 当前方案 | 有统一框架 | 关键差异被压制 |
| B. 每个方案独立 RuntimeFlow | 允许每个 DS 有自己的运行链 | 表达力强 | 可能碎片化 |
| C. 两级结构：主链骨架 + 场景变体 | 定义通用的阶段名称（如"准备→执行→反馈"），每个场景定义自己的步骤 | 兼顾统一和差异 | 设计复杂度增加 |

---

### 3.10 ValidationPlan / DiagnosisRule / RiskConstraint

**合理性**: ✅ 对业务感知域非常重要
- 17 个 ValidationPlan、17 个 DiagnosisRule、18 个 RiskConstraint
- 来源包括调测文档、故障案例、已知约束

**普适性**: ⚠️ 重要性因域而异
- 故障管理域：DiagnosisRule 极其重要，ValidationPlan 次之
- 切片管理域：RiskConstraint（资源限制）重要，DiagnosisRule 可能没那么厚
- 安全防护域：RiskConstraint（合规要求）重要

**建议**: 这三个对象保留为通用类型，但不要求所有域等厚填充

---

### 3.11 Evidence（证据来源）

**合理性**: ✅ 成立且必要
- 12 类证据，覆盖定义、场景、特性、控制面、映射、调测等

**普适性**: ✅ 通用
- 任何知识图谱都需要可追溯性

**开放问题**: 当前 Evidence 粒度偏粗（一组文档一个证据），是否需要更细的页级/段落级粒度？

---

### 3.12 DomainSemanticObject（领域语义对象）

**合理性**: ✅ 这是最关键的创新
- 16 个语义对象把"业务问题"翻译成"可桥接的语义单元"
- 避免了"场景名 → 特性名 → 命令名"的三堆名词直连

**普适性**: ✅ 通用，但每个域的语义对象完全不同
- 故障管理域：告警关联、根因分析、影响范围、恢复动作……
- 切片管理域：切片模板、SLA、资源配额、隔离等级……

**开放问题**: 16 个是否太多？BA.Runtime 和 BA.ValidationDiagnosis 看起来更像横切关注点而非领域语义对象

---

### 3.13 Feature / ConfigObject（特性 / 配置对象）

**合理性**: ✅ 成立
- Feature = 正式能力载体
- ConfigObject = 最终落地对象链

**普适性**: ✅ 通用
- 任何产品化的业务域都有特性和配置对象

---

## 4. 汇总判断

| 对象 | 合理性 | 普适性 | 需要讨论 |
|------|--------|--------|----------|
| BusinessDomain | ✅ | ✅ | 无 |
| NetworkScenario | ✅ | ⚠️ 名称 | 场景粒度约束 |
| ReferencePattern | ⚠️ | ⚠️ | 是否保留为独立对象 |
| DeliverySolution | ✅ | ⚠️ 名称 | 是否改中性名 |
| EngineeringTask | ⚠️ 偏规划 | ⚠️ | 是否分阶段 |
| Participant | ✅ | ✅ | 无 |
| Scope | ✅ | ⚠️ 域特定枚举 | 允许域自定义 |
| DecisionPoint | ⚠️ 挂载位置 | ✅ | 允许多级挂载 |
| RuntimeFlow | ⚠️ 一条链 | ⚠️ | 是否允许场景独立链 |
| ValidationPlan | ✅ | ✅ | 不要求等厚 |
| DiagnosisRule | ✅ | ✅ | 不要求等厚 |
| RiskConstraint | ✅ | ✅ | 不要求等厚 |
| Evidence | ✅ | ✅ | 粒度 |
| DomainSemanticObject | ✅ | ✅ | 对象数量和分类 |
| Feature | ✅ | ✅ | 无 |
| ConfigObject | ✅ | ✅ | 无 |

## 5. 已决策

### Q1: ReferencePattern → **删除** ✓

**决策**：ReferencePattern 不保留为独立 schema 对象。

**依据**：
1. 源文档内容审视（`00-design-charter.md` 3.2 中的原始语料）表明，产品文档给出的是**配置案例**（如套餐1/2/3）和**机制描述**（如融合计费概述、How分流），不是"参考范式"
2. RP 只有两条边：`NS --has_pattern--> RP` 和 `RP --supported_by--> Evidence`。这两条边可以被 `各节点 --supported_by--> Evidence` 替代
3. RP 的"学到的业务结构"本质上是其他节点的边已经表达的知识（DS 连接的 DomainSemanticObject/Feature/ConfigObject）
4. RP 与 DS 内容高度重叠（RP-03 对应 DS-01，RP-04 对应 DS-03，RP-06 对应 DS-05）

**知识去向**：
- RP 中有价值的知识纳入 DS（如机制来源描述、核心知识归纳）
- 证明链功能由 `各节点 --supported_by--> Evidence` 承担
- Evidence 可增加 `evidence_type` 属性区分知识来源类型（配置案例/机制描述/域定义/调测验证）

**影响**：对象从 17 个减少到 16 个，主链简化为：
```
BusinessDomain → NetworkScenario → DeliverySolution → EngineeringTask
```

## 6. 待讨论的核心问题

### Q2: EngineeringTask 是否分阶段？
- 选项 A: 保持扁平
- 选项 B: 加 phase 字段
- 选项 C: 拆成三种对象

### Q3: RuntimeFlow 是否允许场景独立链？
- 选项 A: 保持中性主链 + 注释
- 选项 B: 每个方案独立 RuntimeFlow
- 选项 C: 两级结构（通用骨架 + 场景变体）

### Q4: 哪些是"通用核心"、哪些是"域可扩展"？
- 通用核心（所有域必须有）：Domain / Scenario / Solution / Task / SemanticObject / Feature / ConfigObject / Evidence
- 域可扩展（按需填充）：Participant / Scope / DecisionPoint / RuntimeFlow / ValidationPlan / DiagnosisRule / RiskConstraint

### Q5: 每个对象的边和内部属性是什么？
- 这是 Q1-Q4 解决后的下一步工作
- 需要结合原始语料和实际使用场景逐对象定义
