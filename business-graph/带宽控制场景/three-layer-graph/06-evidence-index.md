# 带宽控制场景三层图谱 · 第6层：证据层索引

> **文件定位**：`three-layer-graph/06-evidence-index.md`
> **Schema参考**：`三层图谱Schema-最终版-v0.1.md` §8.11 EvidenceSource（字段：evidence_id, evidence_type, title, path, source_system, status）
> **作用**：为本场景三层图谱所有对象的 `source_evidence_ids` 字段提供可追溯的证据源注册表。每个图谱对象引用本表中的 `evidence_id`，即可通过本表回溯到原始知识文档。

---

## §1 EvidenceSource 总览

带宽控制场景三层图谱的证据源共分四类，合计 **59份知识资产**：

| 证据类型 | ID前缀 | 数量 | `evidence_type` | `status` | 路径根目录 |
|---------|--------|------|-----------------|----------|-----------|
| 特性知识文档 | `EV-FK-*` | 24 | markdown | active | `feature-knowledge/` |
| 主题知识批次 | `EV-TK-*` | 32 | markdown | active | `topic-knowledge/` |
| 跨特性/跨主题分析 | `EV-CA-*` | 2 | markdown | active | `cross-feature-analysis.md`、`cross-topic-analysis.md` |
| 业务图谱 | `EV-BS-*` | 1 | markdown | active | `three-layer-graph/01-business-graph.md` |
| **合计** | — | **59** | — | — | — |

> 所有证据路径相对 `business-graph/带宽控制场景/`。

---

## §2 特性知识证据（EV-FK-*，24份）

来源：24个特性的横向解读，每特性产出一份知识文档，覆盖特性概述、激活、原理、配置、调测、参考信息。

| Evidence ID | 对应特性 | 文件路径 |
|------------|---------|---------|
| EV-FK-01 | GWFD-110101 SA-Basic | `feature-knowledge/GWFD-110101-SA-Basic.md` |
| EV-FK-02 | GWFD-111600 SA特征库更新管控 | `feature-knowledge/GWFD-111600-SA特征库更新管控.md` |
| EV-FK-03 | GWFD-020351 PCC基本功能（UDG） | `feature-knowledge/GWFD-020351-PCC基本功能.md` |
| EV-FK-04 | GWFD-110311 基于业务感知的带宽控制 | `feature-knowledge/GWFD-110311-基于业务感知的带宽控制.md` |
| EV-FK-05 | GWFD-020354 基于业务的Shaping | `feature-knowledge/GWFD-020354-基于业务的Shaping.md` |
| EV-FK-06 | GWFD-110313 基于智能Shaping的组级带宽控制 | `feature-knowledge/GWFD-110313-基于智能Shaping的组级带宽控制.md` |
| EV-FK-07 | GWFD-020353 基于累计流量的策略控制（会话级FUP） | `feature-knowledge/GWFD-020353-基于累计流量的策略控制.md` |
| EV-FK-08 | GWFD-110312 基于业务累计流量的策略控制（业务级FUP） | `feature-knowledge/GWFD-110312-基于业务累计流量的策略控制.md` |
| EV-FK-09 | GWFD-020357 增强的ADC基本功能（UDG） | `feature-knowledge/GWFD-020357-增强的ADC基本功能.md` |
| EV-FK-10 | GWFD-020358 业务触发的QoS保证（UDG） | `feature-knowledge/GWFD-020358-业务触发的QoS保证.md` |
| EV-FK-11 | GWFD-110301 基于终端系统的码率差异化控制 | `feature-knowledge/GWFD-110301-基于终端系统的码率差异化控制.md` |
| EV-FK-12 | GWFD-110302 基于上下行解耦的视频承载信令控制 | `feature-knowledge/GWFD-110302-基于上下行解耦的视频承载信令控制.md` |
| EV-FK-13 | GWFD-020359 IM类业务无线资源管控 | `feature-knowledge/GWFD-020359-IM类业务无线资源管控.md` |
| EV-FK-14 | GWFD-110331 基于业务流标识的无线资源优化 | `feature-knowledge/GWFD-110331-基于业务流标识的无线资源优化.md` |
| EV-FK-15 | GWFD-110332 基于小区负荷上报的无线资源优化（UDG） | `feature-knowledge/GWFD-110332-基于小区负荷上报的无线资源优化.md` |
| EV-FK-16 | GWFD-020305 终端异常下行流量检测 | `feature-knowledge/GWFD-020305-终端异常下行流量检测.md` |
| EV-FK-17 | WSFD-109101 PCC基本功能（UNC） | `feature-knowledge/WSFD-109101-PCC基本功能.md` |
| EV-FK-18 | WSFD-109104 基于累计流量的策略控制（UNC会话FUP） | `feature-knowledge/WSFD-109104-基于累计流量的策略控制.md` |
| EV-FK-19 | WSFD-211005 基于业务感知的带宽控制（UNC BWM） | `feature-knowledge/WSFD-211005-基于业务感知的带宽控制.md` |
| EV-FK-20 | WSFD-211009 基于业务累计流量的策略控制（UNC业务FUP） | `feature-knowledge/WSFD-211009-基于业务累计流量的策略控制.md` |
| EV-FK-21 | WSFD-109102 ADC基本功能（UNC） | `feature-knowledge/WSFD-109102-ADC基本功能.md` |
| EV-FK-22 | WSFD-109107 业务触发的QoS保证（UNC） | `feature-knowledge/WSFD-109107-业务触发的QoS保证.md` |
| EV-FK-23 | WSFD-109108 基于接入点策略控制（位置区域） | `feature-knowledge/WSFD-109108-基于接入点策略控制.md` |
| EV-FK-24 | WSFD-211101 基于小区负荷上报的无线资源优化（UNC） | `feature-knowledge/WSFD-211101-基于小区负荷上报的无线资源优化.md` |

### §2.1 特性知识证据分组（便于图谱对象快速引用）

| 特性分组 | Evidence IDs | 数量 |
|---------|-------------|------|
| 基础感知 | EV-FK-01, EV-FK-02 | 2 |
| PCC框架 | EV-FK-03, EV-FK-17 | 2 |
| 核心带宽控制（BWM） | EV-FK-04, EV-FK-19 | 2 |
| Shaping整形 | EV-FK-05, EV-FK-06 | 2 |
| FUP累计流量 | EV-FK-07, EV-FK-08, EV-FK-18, EV-FK-20 | 4 |
| QoS保证 | EV-FK-10, EV-FK-22, EV-FK-12 | 3 |
| ADC检测 | EV-FK-09, EV-FK-21 | 2 |
| 无线优化 | EV-FK-13, EV-FK-14, EV-FK-15, EV-FK-24 | 4 |
| 位置感知 | EV-FK-23 | 1 |
| 异常检测 | EV-FK-16 | 1 |
| 视频码率 | EV-FK-11, EV-FK-12 | 2（EV-FK-12与QoS保证共享） |

---

## §3 主题知识证据（EV-TK-*，32份）

来源：317份源文档按 `(产品, 主题)` 切分为32批次后产出的综合知识。

### 3.1 UDG侧主题批次（Batch-01 ~ Batch-21，共21批，200份源文档）

| Evidence ID | 批次 | 主题 | 文件路径 |
|------------|------|------|---------|
| EV-TK-01 | Batch-01 | FUP解决方案-业务级与会话级原理 | `topic-knowledge/Batch-01-FUP解决方案-业务级与会话级原理.md` |
| EV-TK-02 | Batch-02 | FUP会话级配置与体验感知初始配置 | `topic-knowledge/Batch-02-FUP会话级配置与体验感知初始配置.md` |
| EV-TK-03 | Batch-03 | 体验感知-重点用户UPCF与接口对接 | `topic-knowledge/Batch-03-体验感知-重点用户UPCF与接口对接.md` |
| EV-TK-04 | Batch-04 | 体验感知-接口对接与部署总览 | `topic-knowledge/Batch-04-体验感知-接口对接与部署总览.md` |
| EV-TK-05 | Batch-05 | 体验感知-信令流程与方案约束 | `topic-knowledge/Batch-05-体验感知-信令流程与方案约束.md` |
| EV-TK-06 | Batch-06 | 体验感知异厂商与重点业务保障初始配置 | `topic-knowledge/Batch-06-体验感知异厂商与重点业务保障初始配置.md` |
| EV-TK-07 | Batch-07 | 重点业务保障-UNC-UPCF配置与数据规划 | `topic-knowledge/Batch-07-重点业务保障-UNC-UPCF配置与数据规划.md` |
| EV-TK-08 | Batch-08 | 重点业务保障-CloudUDN-NWDAF对接与跨区移动 | `topic-knowledge/Batch-08-重点业务保障-CloudUDN-NWDAF对接与跨区移动.md` |
| EV-TK-09 | Batch-09 | 重点业务保障-接口对接总览与新增保障业务 | `topic-knowledge/Batch-09-重点业务保障-接口对接总览与新增保障业务.md` |
| EV-TK-10 | Batch-10 | 重点业务保障-新增保障业务-部署总览与订阅流程 | `topic-knowledge/Batch-10-重点业务保障-新增保障业务-部署总览与订阅流程.md` |
| EV-TK-11 | Batch-11 | 重点业务保障-异厂商订阅-保障建议与数据采集 | `topic-knowledge/Batch-11-重点业务保障-异厂商订阅-保障建议与数据采集.md` |
| EV-TK-12 | Batch-12 | 重点业务保障-漫游移动-网元选择与全流程 | `topic-knowledge/Batch-12-重点业务保障-漫游移动-网元选择与全流程.md` |
| EV-TK-13 | Batch-13 | 重点业务保障-场景约束与实现原理 | `topic-knowledge/Batch-13-重点业务保障-场景约束与实现原理.md` |
| EV-TK-14 | Batch-14 | 重点业务保障-方案概述-组网与计费原理 | `topic-knowledge/Batch-14-重点业务保障-方案概述-组网与计费原理.md` |
| EV-TK-15 | Batch-15 | 5G基础知识-PCC静态规则与SM策略QoS管理 | `topic-knowledge/Batch-15-5G基础知识-PCC静态规则与SM策略QoS管理.md` |
| EV-TK-16 | Batch-16 | 5G基础知识-业务感知SA解读与QoS基础 | `topic-knowledge/Batch-16-5G基础知识-业务感知SA解读与QoS基础.md` |
| EV-TK-17 | Batch-17 | UDG业务感知专题-背景定义与核心概念 | `topic-knowledge/Batch-17-UDG业务感知专题-背景定义与核心概念.md` |
| EV-TK-18 | Batch-18 | UDG业务感知专题-规则匹配流程与套餐配置 | `topic-knowledge/Batch-18-UDG业务感知专题-规则匹配流程与套餐配置.md` |
| EV-TK-19 | Batch-19 | UDG业务感知-套餐2带宽控制配置与规则全景 ★ | `topic-knowledge/Batch-19-UDG业务感知-套餐2带宽控制配置与规则全景.md` |
| EV-TK-20 | Batch-20 | UDG业务感知-规则实例-License与调测 | `topic-knowledge/Batch-20-UDG业务感知-规则实例-License与调测.md` |
| EV-TK-21 | Batch-21 | UDG业务感知-调测总览 | `topic-knowledge/Batch-21-UDG业务感知-调测总览.md` |

### 3.2 UNC侧主题批次（Batch-22 ~ Batch-32，共11批，117份源文档）

| Evidence ID | 批次 | 主题 | 文件路径 |
|------------|------|------|---------|
| EV-TK-22 | Batch-22 | UNC-FUP解决方案-业务级与会话级原理 | `topic-knowledge/Batch-22-UNC-FUP解决方案-业务级与会话级原理.md` |
| EV-TK-23 | Batch-23 | UNC-FUP会话级配置与SM策略E2E原理 | `topic-knowledge/Batch-23-UNC-FUP会话级配置与SM策略E2E原理.md` |
| EV-TK-24 | Batch-24 | UNC-SM策略-QoS架构与关键内容调测 | `topic-knowledge/Batch-24-UNC-SM策略-QoS架构与关键内容调测.md` |
| EV-TK-25 | Batch-25 | UNC-SM策略-调测方法与业务拆解配置 | `topic-knowledge/Batch-25-UNC-SM策略-调测方法与业务拆解配置.md` |
| EV-TK-26 | Batch-26 | UNC-SM策略-三类规则配置示例与典型场景 | `topic-knowledge/Batch-26-UNC-SM策略-三类规则配置示例与典型场景.md` |
| EV-TK-27 | Batch-27 | UNC-E2E方案-业务重定向与ADC带宽差异化 ★ | `topic-knowledge/Batch-27-UNC-E2E方案-业务重定向与ADC带宽差异化.md` |
| EV-TK-28 | Batch-28 | UNC-E2E方案-ADC带宽差异化与位置区域带宽 ★ | `topic-knowledge/Batch-28-UNC-E2E方案-ADC带宽差异化与位置区域带宽.md` |
| EV-TK-29 | Batch-29 | UNC-E2E方案-位置区域带宽与多业务策略控制 | `topic-knowledge/Batch-29-UNC-E2E方案-位置区域带宽与多业务策略控制.md` |
| EV-TK-30 | Batch-30 | UNC-E2E方案-用户等级资费差异化与SM策略总览 | `topic-knowledge/Batch-30-UNC-E2E方案-用户等级资费差异化与SM策略总览.md` |
| EV-TK-31 | Batch-31 | UNC-5G基础知识-PCC策略QoS管理与静态规则 | `topic-knowledge/Batch-31-UNC-5G基础知识-PCC策略QoS管理与静态规则.md` |
| EV-TK-32 | Batch-32 | UNC-5G基础知识-业务感知SA与QoS基础 | `topic-knowledge/Batch-32-UNC-5G基础知识-业务感知SA与QoS基础.md` |

> ★ 标识核心证据：套餐2带宽控制配置实例（EV-TK-19）和ADC/位置区域端到端方案（EV-TK-27/28）是构建业务层 ConfigurationSolution 的关键来源。

---

## §4 跨特性/跨主题分析证据（EV-CA-*，2份）

| Evidence ID | 标题 | 文件路径 | 关键章节 |
|------------|------|---------|---------|
| EV-CA-01 | 跨特性分析 | `cross-feature-analysis.md` | §1.1功能层次；§2.3 License链；§4.1-4.2依赖图；附录B MML命令；附录C配置对象；附录D端到端流程；附录G无线优化 |
| EV-CA-02 | 跨主题分析 | `cross-topic-analysis.md` | §1.1场景定位；§4.4三条核心链路；§6.2五维度；§7.5 ADC策略；§8.4九场景归并；§H.4冲突矩阵 |

### 4.1 跨层分析与图谱层的映射

| 图谱层 | 主要引用证据 |
|-------|------------|
| 第1层 业务图谱（CS/DP/BR） | EV-CA-02（§6.2/§8.4）+ EV-TK-19/27/28 |
| 第2层 特性图谱（Feature依赖/License） | EV-CA-01（§2.3/§4.1-4.2）+ EV-FK-* |
| 第3层 任务原子层（Task/OrderEdge） | EV-CA-01（附录D）+ EV-TK-19/25/26 |
| 第4层 命令图谱（Command/Object/Rule） | EV-CA-01（附录B/C/H）+ EV-FK-*（特性命令详表）|
| 第5层 跨层映射 | EV-CA-01 + EV-CA-02（综合引用） |

---

## §5 业务图谱证据（EV-BS-*，1份）

| Evidence ID | 标题 | 文件路径 | 规模 |
|------------|------|---------|------|
| `EV-BS-01` | 带宽控制场景业务图谱 | `three-layer-graph/01-business-graph.md` | 三层图谱第1层 |

> 带宽控制场景业务图谱直接以三层图谱形式产出（与计费场景独立md不同），EV-BS-01 是第1层（业务层）图谱的权威来源。

---

## §6 证据使用规范

### 6.1 图谱对象引用证据的方式

每个图谱对象的 `source_evidence_ids` 字段填写本表中的 `evidence_id`，遵循以下规范：

```yaml
# 业务层对象示例
- id: CS-BW-01
  type: ConfigurationSolution
  source_evidence_ids:
    - EV-CA-02          # 跨主题分析§4.4链路1
    - EV-TK-19          # 套餐2带宽控制配置实例
    - EV-FK-04          # GWFD-110311 BWM特性
    - EV-BS-01          # 业务图谱第1层

# 特性层对象示例
- id: GWFD-110311
  type: Feature
  source_evidence_ids:
    - EV-FK-04          # 特性专属证据（必填）
    - EV-CA-01          # 跨特性分析§4.1依赖图

# 命令层对象示例
- id: ADD-BWMCONTROLLER
  type: MMLCommand
  source_evidence_ids:
    - EV-FK-04          # 主属特性
    - EV-CA-01          # 跨特性分析附录B
    - EV-TK-19          # 配置实例
```

### 6.2 证据强度等级（参考Schema §8.11）

| 等级 | 判定 | 典型证据 |
|------|------|---------|
| `direct` | 结论与原文明确对应 | 特性文档中的命令定义、参数取值 |
| `supporting` | 原文支持但非直接陈述 | 跨特性分析归纳的依赖关系 |
| `inferred` | 由多条证据推理得出 | 跨主题分析归纳的方案闭包 |
| `weak` | 单一弱证据，需进一步验证 | 配置实例中的隐含规则 |

> 本图谱所有正式对象的 `source_evidence_ids` 至少达到 `supporting` 强度；特性/命令层对象的证据默认 `direct`。

### 6.3 证据可追溯链路验证

图谱任意对象 → `source_evidence_ids` → 本索引 → 知识文档 → 原始产品文档（通过知识文档中的 SourcePath/OriginalPath 字段回溯到 `output/UDG_*` 或 `output/UNC_*` 原始md）。

完整链路示例：
```
CS-BW-01 (SA-BWM方案)
  → source_evidence_ids: [EV-CA-02, EV-TK-19, EV-FK-04, EV-BS-01]
    → cross-topic-analysis.md §4.4 链路1
    → Batch-19 UDG业务感知-套餐2带宽控制配置与规则全景.md
    → GWFD-110311-基于业务感知的带宽控制.md
    → three-layer-graph/01-business-graph.md §CS-BW-01
      → SourcePath: output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/.../GWFD-110311*
      → 原始产品文档（权威事实源）
```

---

## §7 证据完整性检查清单

- [x] 24份特性知识全部登记并分配 Evidence ID（EV-FK-01 ~ EV-FK-24）
- [x] 32份主题知识全部登记并分配 Evidence ID（EV-TK-01 ~ EV-TK-32）
- [x] 2份跨特性/跨主题分析全部登记并分配 Evidence ID（EV-CA-01, EV-CA-02）
- [x] 1份业务图谱登记并分配 Evidence ID（EV-BS-01）
- [x] 所有路径相对 `business-graph/带宽控制场景/` 准确
- [x] 核心方案 CS-BW-01~07 至少引用 1份 direct 证据 + 1份 supporting 证据
- [x] 所有 Feature 对象引用对应 EV-FK-*
- [x] 所有核心 Command 对象引用对应 EV-FK-* + EV-CA-01
- [x] 证据可追溯链路验证（图谱对象 → 本索引 → 知识文档 → 原始md）
- [x] 所有证据 status = active，evidence_type = markdown
- [x] UDG/UNC 对应特性对证据交叉引用完整（8对 UDG-UNC 对应关系）

---

## §8 与计费场景证据层的对比

| 维度 | 计费场景 | 带宽控制场景 |
|------|---------|------------|
| 证据总数 | 32 | 59 |
| 特性知识 | 14 EV-FK（15含跨特性分析） | **24 EV-FK**（11核心 + 13辅助，16 UDG + 8 UNC） |
| 主题知识 | — | **32 EV-TK**（UDG 21批 + UNC 11批，317份源文档） |
| 跨特性分析 | 1 EV-CFA（580行） | 1 EV-CA-01（1119行，24特性横向归纳） |
| 跨主题分析 | — | 1 EV-CA-02（862行，32批次综合归纳） |
| 统一知识库 | 4 EV-KB（3232行+3份融合） | — |
| 业务图谱 | 2 EV-BS（原始版+SKILL版） | 1 EV-BS（三层图谱形式） |
| **协议知识** | **2 EV-PK（★独有，1422行）** | — |
| SKILL知识 | 5 EV-SK | — |
| 文档清单 | 1 EV-FDL（154文件） | — |
| 设计文档 | 1 EV-DES | — |
| 业务感知全景 | 1 EV-BSA-全景 | — |

### 关键差异说明

1. **带宽控制场景知识规模更大**：24特性 + 32主题批次 = 56份知识文档（不含分析），远超计费场景的14特性。原因是带宽控制涉及BWM、FUP、Shaping、QoS、ADC、无线优化等多个技术方向，且UDG/UNC双产品线特性数量不对称（16+8）。

2. **主题知识是带宽控制独有资产**：计费场景无主题批次证据，带宽控制因源文档数量大（317份）而引入按 `(产品, 主题)` 分批处理模式，产出32份综合主题知识。

3. **计费场景独有协议知识**：Ga/Gy/DCC/N40/PFCP/Gx 共1422行协议知识，支撑 SO-CH-10/11 两个协议栈 SemanticObject，是计费场景区别于带宽场景的核心知识资产。带宽控制的协议交互（PFCP/N7/Gx）嵌入在特性知识和主题批次中，未单独提取。

4. **跨特性分析深度不同**：带宽控制的跨特性分析（1119行）覆盖24特性的依赖图、License链、配置对象映射和端到端流程，规模为计费场景（580行）的近2倍。

---

> 本索引为带宽控制场景三层图谱的"证据层"，确保图谱任何结论都能反查到权威事实源，满足 Schema §8.11 EvidenceSource 字段规范和质量门禁的"可信度门禁"要求。
