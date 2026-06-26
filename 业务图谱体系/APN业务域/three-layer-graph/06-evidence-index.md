# APN业务域三层图谱 · 第6层：证据层索引

> **文件定位**：`three-layer-graph/06-evidence-index.md`
> **Schema参考**：`三层图谱Schema-最终版-v0.1.md` §8.11 EvidenceSource（字段：evidence_id, evidence_type, title, path, source_system, status）
> **作用**：为本业务域三层图谱所有对象的 `source_evidence_ids` 字段提供可追溯的证据源注册表。每个图谱对象引用本表中的 `evidence_id`，即可通过本表回溯到原始知识文档。

---

## §1 EvidenceSource 总览

APN业务域三层图谱的证据源共分四类，合计 **45份知识资产**：

| 证据类型 | ID前缀 | 数量 | `evidence_type` | `status` | 路径根目录 |
|---------|--------|------|-----------------|----------|-----------|
| 特性知识文档 | `EV-FK-*` | 37 | markdown | active | `feature-knowledge/` |
| 主题知识归纳 | `EV-TK-*` | 4 | markdown | active | `topic-knowledge/` |
| 跨特性/跨主题分析 | `EV-CA-*` | 2 | markdown | active | `feature-knowledge/cross-feature-analysis.md`、`cross-topic-analysis.md` |
| 业务底座知识 | `EV-BS-*` | 2 | markdown | active | `APN意图澄清知识库.md`、`APN配置树.md` |
| **合计** | — | **45** | — | — | — |

> 所有证据路径相对本业务域目录（`业务图谱体系/APN业务域/`）。`source_system` 统一为 `APN业务域`。

---

## §2 特性知识证据（EV-FK-*，37份）

来源：37个特性的横向解读，每特性产出一份知识文档，覆盖特性概述、激活、原理、配置、调测、参考信息。

> **编号规则**：`EV-FK-01` ~ `EV-FK-37` 严格按 `apn-feature-doc-list.md` 总览表序号 1-37，与 `02-feature-graph.md` 的 `source_evidence_ids` 完全一致。

| Evidence ID | 对应特性 | 产品 | 类别 | 文件路径 |
|------------|---------|------|------|---------|
| EV-FK-01 | GWFD-010101 会话管理 | UDG | APN基础 | `feature-knowledge/GWFD-010101-会话管理.md` |
| EV-FK-02 | WSFD-010501 会话管理 | UNC | APN基础 | `feature-knowledge/WSFD-010501-会话管理.md` |
| EV-FK-03 | WSFD-010503 多PDN-PDU功能 | UNC | APN基础 | `feature-knowledge/WSFD-010503-多PDN-PDU功能.md` |
| EV-FK-04 | WSFD-010400 用户数据管理 | UNC | APN基础 | `feature-knowledge/WSFD-010400-用户数据管理.md` |
| EV-FK-05 | WSFD-106203 别名APN | UNC | APN基础 | `feature-knowledge/WSFD-106203-别名APN.md` |
| EV-FK-06 | GWFD-010105 用户面地址分配 | UDG | 地址分配 | `feature-knowledge/GWFD-010105-用户面地址分配.md` |
| EV-FK-07 | GWFD-010104 地址分配方式 | UDG | 地址分配 | `feature-knowledge/GWFD-010104-地址分配方式.md` |
| EV-FK-08 | GWFD-020421 基于位置的地址分配 | UDG | 地址分配 | `feature-knowledge/GWFD-020421-基于位置的地址分配.md` |
| EV-FK-09 | GWFD-010108 用户面地址自动检测 | UDG | 地址分配 | `feature-knowledge/GWFD-010108-用户面地址自动检测.md` |
| EV-FK-10 | GWFD-010107 静态地址用户路由冗余 | UDG | 地址分配 | `feature-knowledge/GWFD-010107-静态地址用户路由冗余.md` |
| EV-FK-11 | GWFD-020412 L2TP VPN | UDG | 地址分配 | `feature-knowledge/GWFD-020412-L2TPVPN.md` |
| EV-FK-12 | WSFD-010502 地址分配方式 | UNC | 地址分配 | `feature-knowledge/WSFD-010502-地址分配方式.md` |
| EV-FK-13 | WSFD-010504 控制面地址分配方式 | UNC | 地址分配 | `feature-knowledge/WSFD-010504-控制面地址分配方式.md` |
| EV-FK-14 | WSFD-104410 L2TP VPN | UNC | 地址分配 | `feature-knowledge/WSFD-104410-L2TPVPN.md` |
| EV-FK-15 | WSFD-107021 静态地址用户路由冗余 | UNC | 地址分配 | `feature-knowledge/WSFD-107021-静态地址用户路由冗余.md` |
| EV-FK-16 | GWFD-020403 IPv4v6双栈接入 | UDG | 地址分配 | `feature-knowledge/GWFD-020403-IPv4v6双栈接入.md` |
| EV-FK-17 | WSFD-104002 IPv4v6双栈接入 | UNC | 地址分配 | `feature-knowledge/WSFD-104002-IPv4v6双栈接入.md` |
| EV-FK-18 | GWFD-020401 IPv6承载上下文 | UDG | 地址分配 | `feature-knowledge/GWFD-020401-IPv6承载上下文.md` |
| EV-FK-19 | WSFD-104001 IPv6承载上下文 | UNC | 地址分配 | `feature-knowledge/WSFD-104001-IPv6承载上下文.md` |
| EV-FK-20 | GWFD-020406 IPv6PrefixDelegation | UDG | 地址分配 | `feature-knowledge/GWFD-020406-IPv6PrefixDelegation.md` |
| EV-FK-21 | WSFD-104004 IPv6前缀代理 | UNC | 地址分配 | `feature-knowledge/WSFD-104004-IPv6前缀代理.md` |
| EV-FK-22 | WSFD-104413 DHCP功能 | UNC | 地址分配 | `feature-knowledge/WSFD-104413-DHCP功能.md` |
| EV-FK-23 | WSFD-104005 DHCPv6地址分配 | UNC | 地址分配 | `feature-knowledge/WSFD-104005-DHCPv6地址分配.md` |
| EV-FK-24 | WSFD-011305 Radius鉴权接入 | UNC | 鉴权计费 | `feature-knowledge/WSFD-011305-Radius鉴权接入.md` |
| EV-FK-25 | WSFD-011306 Radius功能 | UNC | 鉴权计费 | `feature-knowledge/WSFD-011306-Radius功能.md` |
| EV-FK-26 | WSFD-010301 鉴权功能 | UNC | 鉴权计费 | `feature-knowledge/WSFD-010301-鉴权功能.md` |
| EV-FK-27 | WSFD-108007 终端二次鉴权 | UNC | 鉴权计费 | `feature-knowledge/WSFD-108007-终端二次鉴权.md` |
| EV-FK-28 | WSFD-011307 Radius抄送功能 | UNC | 鉴权计费 | `feature-knowledge/WSFD-011307-Radius抄送功能.md` |
| EV-FK-29 | IPFD-015002 GRE | UDG+UNC | 接入方式 | `feature-knowledge/IPFD-015002-GRE.md` |
| EV-FK-30 | IPFD-015004 IPSec功能 | UDG | 接入方式 | `feature-knowledge/IPFD-015004-IPSec功能.md` |
| EV-FK-31 | IPFD-016000 IPSec功能 | UNC | 接入方式 | `feature-knowledge/IPFD-016000-IPSec功能.md` |
| EV-FK-32 | GWFD-020411 MPLS VPN | UDG | 接入方式 | `feature-knowledge/GWFD-020411-MPLSVPN.md` |
| EV-FK-33 | WSFD-104411 MPLS VPN | UNC | 接入方式 | `feature-knowledge/WSFD-104411-MPLSVPN.md` |
| EV-FK-34 | WSFD-107010 UPF选择 | UNC | 网元选择 | `feature-knowledge/WSFD-107010-UPF选择.md` |
| EV-FK-35 | WSFD-010202 基于位置区域对等网元选择 | UNC | 网元选择 | `feature-knowledge/WSFD-010202-基于位置区域对等网元选择.md` |
| EV-FK-36 | WSFD-106003 用户接入控制功能 | UNC | 接入控制 | `feature-knowledge/WSFD-106003-用户接入控制功能.md` |
| EV-FK-37 | GWFD-010151 接入控制 | UDG | 接入控制 | `feature-knowledge/GWFD-010151-接入控制.md` |

### §2.1 特性知识证据分组（便于图谱对象快速引用）

| 特性分组 | Evidence IDs | 数量 |
|---------|-------------|------|
| APN基础（会话/用户数据/别名APN） | EV-FK-01, EV-FK-02, EV-FK-03, EV-FK-04, EV-FK-05 | 5 |
| 地址分配-基础（UPF/SMF分配） | EV-FK-06, EV-FK-07, EV-FK-08, EV-FK-09, EV-FK-10, EV-FK-12, EV-FK-13, EV-FK-15 | 8 |
| 地址分配-L2TP VPN | EV-FK-11, EV-FK-14 | 2 |
| 地址分配-IPv6/双栈 | EV-FK-16, EV-FK-17, EV-FK-18, EV-FK-19, EV-FK-20, EV-FK-21, EV-FK-22, EV-FK-23 | 8 |
| 鉴权计费（Radius/鉴权） | EV-FK-24, EV-FK-25, EV-FK-26, EV-FK-27, EV-FK-28 | 5 |
| 接入方式（VPN隧道） | EV-FK-29, EV-FK-30, EV-FK-31, EV-FK-32, EV-FK-33 | 5 |
| 网元选择（UPF/对等） | EV-FK-34, EV-FK-35 | 2 |
| 接入控制 | EV-FK-36, EV-FK-37 | 2 |

---

## §3 主题知识归纳证据（EV-TK-*，4份）

来源：跨特性分析阶段产出的4份归纳文档，分别从业务场景、四维度决策、APN底座、配置树修正四个方向综合归纳。

| Evidence ID | 归纳主题 | 文件路径 | 关键内容 |
|------------|---------|---------|---------|
| EV-TK-01 | 业务场景方案（Batch-14） | `topic-knowledge/Batch-14-业务场景方案.md` | APN业务场景端到端方案归纳 |
| EV-TK-02 | 四维度决策与机制 | `topic-knowledge/归纳-四维度决策与机制.md` | 地址分配/接入控制/鉴权/接入方式四维度决策机制 |
| EV-TK-03 | APN底座三维度 | `topic-knowledge/归纳-APN底座三维度.md` | APN底座（会话管理/用户数据/别名APN）三维度归纳 |
| EV-TK-04 | 配置树修正与Stage3待解决项 | `topic-knowledge/归纳-配置树修正与Stage3待解决项.md` | 配置树修正及Stage3遗留问题闭环 |

---

## §4 跨特性/跨主题分析证据（EV-CA-*，2份）

| Evidence ID | 标题 | 文件路径 | 关键内容 |
|------------|------|---------|---------|
| EV-CA-01 | 跨特性分析 | `feature-knowledge/cross-feature-analysis.md` | 37特性横向归纳：依赖图、License链、配置对象映射、命令清单、端到端流程 |
| EV-CA-02 | 跨主题分析 | `cross-topic-analysis.md` | 4份主题归纳综合归纳：场景定位、核心链路、维度归并、冲突矩阵 |

### 4.1 跨层分析与图谱层的映射

| 图谱层 | 主要引用证据 |
|-------|------------|
| 第1层 业务图谱（CS/DP/BR） | EV-CA-02 + EV-TK-01~04 + EV-BS-01/02 |
| 第2层 特性图谱（Feature依赖/License） | EV-CA-01 + EV-FK-01~37 |
| 第3层 任务原子层（Task/OrderEdge） | EV-CA-01 + EV-FK-06/11/16/24/25/29/34/36 等 |
| 第4层 命令图谱（Command/Object/Rule） | EV-CA-01 + EV-FK-*（特性命令详表）|
| 第5层 跨层映射 | EV-CA-01 + EV-CA-02（综合引用） |

---

## §5 业务底座知识证据（EV-BS-*，2份）

| Evidence ID | 标题 | 文件路径 | 内容定位 |
|------------|------|---------|---------|
| EV-BS-01 | APN意图澄清知识库 | `APN意图澄清知识库.md` | 业务意图澄清、APN核心定义、专家梳理的业务语义 |
| EV-BS-02 | APN配置树 | `APN配置树.md` | 专家梳理的配置树叶子节点（11节点+26特性补全的权威结构来源） |

> EV-BS-01/02 是APN业务域的"权威底座"，配置树（EV-BS-02）是特性筛选（37特性）和图谱对象结构的源头；意图澄清知识库（EV-BS-01）是业务语义和场景定义的源头。

---

## §6 证据使用规范

### 6.1 图谱对象引用证据的方式

每个图谱对象的 `source_evidence_ids` 字段填写本表中的 `evidence_id`，遵循以下规范：

```yaml
# 特性层对象示例（与02-feature-graph.md一致）
- id: GWFD-010101
  type: Feature
  source_evidence_ids:
    - EV-FK-01          # 特性专属证据（必填）
    - EV-CA-01          # 跨特性分析

# 业务层对象示例
- id: CS-APN-XX
  type: ConfigurationSolution
  source_evidence_ids:
    - EV-CA-02          # 跨主题分析
    - EV-TK-01          # 业务场景方案
    - EV-FK-06          # 主属特性
    - EV-BS-02          # 配置树

# 命令层对象示例
- id: ADD-XXX
  type: MMLCommand
  source_evidence_ids:
    - EV-FK-06          # 主属特性
    - EV-CA-01          # 跨特性分析
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
GWFD-010101 (Feature 会话管理)
  → source_evidence_ids: [EV-FK-01, EV-CA-01]
    → feature-knowledge/GWFD-010101-会话管理.md
    → feature-knowledge/cross-feature-analysis.md
      → SourcePath: output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/基本接入功能/GWFD-010101 会话管理/...
      → 原始产品文档（权威事实源）
```

---

## §7 证据完整性检查清单

- [x] 37份特性知识全部登记并分配 Evidence ID（EV-FK-01 ~ EV-FK-37），顺序严格对齐 `apn-feature-doc-list.md` 总览表
- [x] 4份主题知识归纳全部登记并分配 Evidence ID（EV-TK-01 ~ EV-TK-04）
- [x] 2份跨特性/跨主题分析全部登记并分配 Evidence ID（EV-CA-01, EV-CA-02）
- [x] 2份业务底座知识登记并分配 Evidence ID（EV-BS-01, EV-BS-02）
- [x] 所有路径相对本业务域目录（`业务图谱体系/APN业务域/`）准确
- [x] 所有 Feature 对象引用对应 EV-FK-*（与02-feature-graph.md一致）
- [x] 所有 FTOE OrderEdge 引用对应 EV-FK-* + EV-CA-01
- [x] evidence_type 全部为 markdown（符合 Schema §8.11 枚举）
- [x] status 全部为 active（符合 Schema §8.11 枚举）
- [x] source_system 统一为 APN业务域
- [x] UDG/UNC 对应特性对证据交叉引用完整（如 GWFD-010101 ↔ WSFD-010501、GWFD-020412 ↔ WSFD-104410 等）

---

## §8 EvidenceSource 字段规范摘要（Schema §8.11）

| 字段 | 类型 | 取值约束 | 本索引应用 |
|------|------|---------|-----------|
| `evidence_id` | string | 全局唯一，格式 `EV-{TYPE}-{NN}` | EV-FK-01~37 / EV-TK-01~04 / EV-CA-01~02 / EV-BS-01~02 |
| `evidence_type` | enum | `markdown` \| `excel` \| `pdf` \| `txt` \| `other` | 全部 `markdown` |
| `title` | string | 证据标题（人类可读） | 特性名/归纳主题/分析类型/底座名称 |
| `path` | string | 相对业务域目录的文件路径 | 见各表"文件路径"列 |
| `source_system` | string | 证据来源系统 | 统一 `APN业务域` |
| `status` | enum | `draft` \| `active` \| `deprecated` | 全部 `active` |

---

> 本索引为APN业务域三层图谱的"证据层"，确保图谱任何结论都能反查到权威事实源，满足 Schema §8.11 EvidenceSource 字段规范和质量门禁的"可信度门禁"要求。
