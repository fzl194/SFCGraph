# 计费场景三层图谱 · 第6层：证据层索引

> **文件定位**：`three-layer-graph/06-evidence-index.md`
> **Schema参考**：`三层图谱Schema-最终版-v0.1.md` §10 EvidenceSource
> **作用**：为本场景三层图谱所有对象的 `source_evidence_ids` 字段提供可追溯的证据源注册表。每个图谱对象引用本表中的 `evidence_id`，即可通过本表回溯到原始知识文档。

---

## 1. EvidenceSource 总览

计费场景三层图谱的证据源共分五类，合计 **32份知识资产**：

| 证据类型 | ID前缀 | 数量 | `evidence_type` | `status` | 路径根目录 |
|---------|--------|------|-----------------|----------|-----------|
| 特性知识文档 | `EV-FK-*` | 15 | markdown | active | `feature-knowledge/` |
| 统一知识库 | `EV-KB-*` | 4 | markdown | active | `unified-knowledge/计费场景统一知识库.md`、`unified-knowledge/knowledge-fused-part*.md` |
| 业务图谱 | `EV-BS-*` | 2 | markdown | active | `01计费场景业务图谱.md`、`SKILL/knowledge/计费场景业务图谱.md` |
| 协议知识 | `EV-PK-*` | 2 | markdown | active | `SKILL/knowledge/协议知识-*.md` |
| SKILL知识 | `EV-SK-*` | 5 | markdown | active | `SKILL/knowledge/*.md` |
| 跨特性分析 | `EV-CFA` | 1 | markdown | active | `feature-knowledge/cross-feature-analysis.md` |
| 特性文档清单 | `EV-FDL` | 1 | markdown | active | `charging-feature-doc-list.md` |
| 设计文档 | `EV-DES` | 1 | markdown | active | `design-mvp-closure.md` |
| 业务感知全景 | `EV-BSA-全景` | 1 | markdown | active | `SKILL/knowledge/业务感知业务图谱.md` |
| **合计** | — | **32** | — | — | — |

> 所有证据路径相对本场景目录（`业务图谱体系/计费场景/`）。

---

## 2. 特性知识证据（EV-FK-*，15份）

来源：14个特性的横向解读 + 1份跨特性分析。每特性产出一份知识文档，覆盖特性概述、激活、原理、配置、调测、参考信息。

| Evidence ID | 对应特性 | 文件路径 |
|------------|---------|---------|
| `EV-FK-SA-Basic` | GWFD-110101 SA-Basic | `feature-knowledge/GWFD-110101-SA-Basic.md` |
| `EV-FK-PCC-UDG` | GWFD-020351 PCC基本功能（UDG） | `feature-knowledge/GWFD-020351-PCC基本功能.md` |
| `EV-FK-Offline-UDG` | GWFD-010171 离线计费（UDG） | `feature-knowledge/GWFD-010171-离线计费.md` |
| `EV-FK-Online` | GWFD-020300 在线计费（UDG） | `feature-knowledge/GWFD-020300-在线计费.md` |
| `EV-FK-Converged-UDG` | GWFD-010173 融合计费（UDG） | `feature-knowledge/GWFD-010173-融合计费.md` |
| `EV-FK-Content-UDG` | GWFD-020301 内容计费基本功能（UDG） | `feature-knowledge/GWFD-020301-内容计费.md` |
| `EV-FK-Duration` | GWFD-020302 基于业务时长的计费 | `feature-knowledge/GWFD-020302-时长计费.md` |
| `EV-FK-Volume` | GWFD-020303 基于业务流量的计费 | `feature-knowledge/GWFD-020303-流量计费.md` |
| `EV-FK-Event` | GWFD-020306 支持事件计费 | `feature-knowledge/GWFD-020306-事件计费.md` |
| `EV-FK-PCC-UNC` | WSFD-109101 PCC基本功能（UNC） | `feature-knowledge/WSFD-109101-PCC基本功能.md` |
| `EV-FK-Offline-UNC` | WSFD-011201 支持离线计费（UNC） | `feature-knowledge/WSFD-011201-离线计费.md` |
| `EV-FK-Converged-UNC` | WSFD-011206 支持融合计费（UNC） | `feature-knowledge/WSFD-011206-融合计费.md` |
| `EV-FK-Content-UNC` | WSFD-109002 内容计费基本功能（UNC） | `feature-knowledge/WSFD-109002-内容计费.md` |
| `EV-FK-HotBilling` | WSFD-011202 支持热计费（UNC） | `feature-knowledge/WSFD-011202-热计费.md` |
| `EV-CFA` | 跨特性分析（14特性横向归纳） | `feature-knowledge/cross-feature-analysis.md` |

### 2.1 特性知识证据分组（便于图谱对象快速引用）

| 特性分组 | Evidence IDs | 数量 |
|---------|-------------|------|
| 基础感知 | EV-FK-SA-Basic | 1 |
| PCC框架 | EV-FK-PCC-UDG, EV-FK-PCC-UNC | 2 |
| 离线计费 | EV-FK-Offline-UDG, EV-FK-Offline-UNC | 2 |
| 在线计费 | EV-FK-Online | 1 |
| 融合计费 | EV-FK-Converged-UDG, EV-FK-Converged-UNC | 2 |
| 内容计费 | EV-FK-Content-UDG, EV-FK-Content-UNC | 2 |
| 计量方式增强 | EV-FK-Duration, EV-FK-Volume, EV-FK-Event | 3 |
| 热计费 | EV-FK-HotBilling | 1 |
| 跨特性分析 | EV-CFA | 1 |

---

## 3. 统一知识库证据（EV-KB-*，4份）

| Evidence ID | 标题 | 文件路径 | 规模 |
|------------|------|---------|------|
| `EV-KB-001` | 计费场景统一知识库 | `unified-knowledge/计费场景统一知识库.md` | 3232行，K001-K261 |
| `EV-KB-002` | 知识融合A（业务方案+配置全景） | `unified-knowledge/knowledge-fused-partA.md` | 融合知识上半 |
| `EV-KB-003` | 知识融合B（命令+协议） | `unified-knowledge/knowledge-fused-partB.md` | 融合知识下半 |
| `EV-KB-004` | 知识融合C（故障诊断+运维） | `unified-knowledge/knowledge-fused-partC.md` | 融合知识运维篇，937行 |

### 3.1 统一知识库关键章节映射

| 统一知识库章节 | Knowledge IDs | 支撑图谱层 |
|--------------|---------------|----------|
| 计费系统概述 | K001-K004 | 第1层 CS-CH-01~03（计费方式分类） |
| 计费粒度与计量 | K013-K027 | 第1层 DP-CH-05/06、CS-CH-04/05 |
| 在线计费与配额 | K028-K048 | 第1层 CS-CH-02、CS-CH-06；SO-CH-09 |
| 融合计费架构 | K101-K121, K201-K213 | 第1层 CS-CH-03；SO-CH-11；BR-CH-10 |
| 配置链与命令 | K126-K167 | 第3层 ConfigTask；第4层 MMLCommand |
| 兜底与诊断 | K214-K261 | 第1层 CS-CH-07；BR-CH-06/08；SO-CH-12 |

---

## 4. 业务图谱证据（EV-BS-*，2份）

| Evidence ID | 标题 | 文件路径 | 规模 |
|------------|------|---------|------|
| `EV-BS-001` | 计费场景业务图谱（原始版） | `01计费场景业务图谱.md` | 757行 |
| `EV-BS-002` | 计费场景业务图谱（SKILL版） | `SKILL/knowledge/计费场景业务图谱.md` | 624行 |

> **别名注册（U-H-01已修复）**：历史版本中 01-business-graph.md 曾使用别名 `EV-01-业务图谱` 引用本表 `EV-BS-001`。经审查修复（批次1），01-business-graph.md 中全部6处引用已统一替换为正式ID `EV-BS-001`。别名 `EV-01-业务图谱` 已废止，不再使用。

---

## 5. 协议知识证据（EV-PK-*，2份）★

> 计费场景独有：1,422行协议知识，映射到 SO-CH-10 和 SO-CH-11。

| Evidence ID | 标题 | 文件路径 | 规模 | 映射SemanticObject |
|------------|------|---------|------|-------------------|
| `EV-PK-Ga-Gy-DCC` | 协议知识-Ga/Gy/DCC | `SKILL/knowledge/协议知识-Ga-Gy-DCC.md` | 680行 | **SO-CH-10** |
| `EV-PK-N40-PFCP-Gx` | 协议知识-N40/PFCP/Gx | `SKILL/knowledge/协议知识-N40-PFCP-Gx.md` | 742行 | **SO-CH-11** |

### 5.1 协议知识覆盖范围

| 协议 | 接口 | 角色 | 证据 |
|------|------|------|------|
| Ga | CG↔BD（离线） | GTP'话单传输 | EV-PK-Ga-Gy-DCC §Ga |
| Gy | SMF↔OCS（在线） | Diameter/DCC信用控制 | EV-PK-Ga-Gy-DCC §Gy/DCC |
| DCC | Gy会话协议 | CCR-I/U/T三阶段、MSCC | EV-PK-Ga-Gy-DCC §DCC会话 |
| N40 | SMF↔CHF（融合） | Nchf/HTTP2服务化 | EV-PK-N40-PFCP-Gx §N40/Nchf |
| PFCP | SMF↔UPF（N4） | Usage Report上报 | EV-PK-N40-PFCP-Gx §PFCP |
| Gx | PCRF↔SMF（4G） | Diameter策略下发 | EV-PK-N40-PFCP-Gx §Gx |

---

## 6. SKILL知识证据（EV-SK-*，5份）

| Evidence ID | 标题 | 文件路径 | 用途 |
|------------|------|---------|------|
| `EV-SK-Schema` | 业务图谱Schema | `SKILL/knowledge/business-graph-schema.md` | Schema参考 |
| `EV-SK-Config` | 方案设计-配置全景 | `SKILL/knowledge/方案设计-配置全景.md` | 配置链端到端 |
| `EV-SK-Fault` | 故障案例与运维 | `SKILL/knowledge/故障案例与运维.md` | 故障诊断（SO-CH-12） |
| `EV-SK-Arch` | 原理-架构与术语 | `SKILL/knowledge/原理-架构与术语.md` | 架构基础 |
| `EV-SK-KB` | 计费知识库（精简版） | `SKILL/knowledge/计费知识库.md` | 1297行精简知识 |

---

## 7. 业务感知全景证据

| Evidence ID | 标题 | 文件路径 | 规模 |
|------------|------|---------|------|
| `EV-BSA-全景` | 业务感知业务图谱（全景） | `SKILL/knowledge/业务感知业务图谱.md` | 1628行 |

> 计费、带宽控制、访问限制三场景共享此全景知识。BD-CH-01（业务感知）根对象主要引用此证据。

---

## 8. 跨层分析与清单证据

| Evidence ID | 标题 | 文件路径 | 规模 |
|------------|------|---------|------|
| `EV-CFA` | 跨特性分析（14特性） | `feature-knowledge/cross-feature-analysis.md` | 580行 |
| `EV-FDL` | 特性文档清单（154文件登记） | `charging-feature-doc-list.md` | 文档登记 |
| `EV-DES` | MVP闭包设计 | `design-mvp-closure.md` | 设计文档 |

---

## 9. 证据使用规范

### 9.1 图谱对象引用证据的方式

每个图谱对象的 `source_evidence_ids` 字段填写本表中的 `evidence_id`，遵循以下规范：

```yaml
# 业务层对象示例
- id: CS-CH-01
  type: ConfigurationSolution
  source_evidence_ids:
    - EV-KB-001        # 统一知识库K001-K004计费系统概述
    - EV-BS-001        # 业务图谱原始版
    - EV-FK-Offline-UDG # GWFD-010171特性知识

# 特性层对象示例
- id: GWFD-020301
  type: Feature
  source_evidence_ids:
    - EV-FK-Content-UDG # 特性专属证据（必填）
    - EV-CFA            # 跨特性分析

# 命令层对象示例
- id: CMD-UDG-016
  type: MMLCommand
  source_evidence_ids:
    - EV-FK-Content-UDG # 主属特性
    - EV-CFA            # 跨特性分析附录B
    - EV-KB-001         # 统一知识库配置实例
```

### 9.2 证据强度等级（参考CLAUDE.md §8 审查模式）

| 等级 | 判定 | 典型证据 |
|------|------|---------|
| `direct` | 结论与原文明确对应 | 特性文档中的命令定义、参数取值 |
| `supporting` | 原文支持但非直接陈述 | 跨特性分析归纳的依赖关系 |
| `inferred` | 由多条证据推理得出 | 统一知识库归纳的方案闭包 |
| `weak` | 单一弱证据，需进一步验证 | 配置实例中的隐含规则 |

> 本图谱所有正式对象的 `source_evidence_ids` 至少达到 `supporting` 强度；特性/命令层对象的证据默认 `direct`。

### 9.3 证据可追溯链路验证

图谱任意对象 → `source_evidence_ids` → 本索引 → 知识文档 → 原始产品文档（通过知识文档中的 SourcePath/OriginalPath 字段回溯到 `output/UDG_*` 或 `output/UNC_*` 原始md）。

完整链路示例：
```
CS-CH-01 (离线计费方案)
  → source_evidence_ids: [EV-KB-001, EV-BS-001, EV-FK-Offline-UDG]
    → unified-knowledge/计费场景统一知识库.md §K001-K004 计费系统概述
    → 01计费场景业务图谱.md §离线计费方案
    → GWFD-010171-离线计费.md
      → SourcePath: output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/.../GWFD-010171*
      → 原始产品文档（权威事实源）
```

---

## 10. 证据完整性检查清单

- [x] 14份特性知识全部登记并分配 Evidence ID
- [x] 1份跨特性分析登记
- [x] 4份统一知识库/融合知识登记
- [x] 2份业务图谱登记
- [x] 2份协议知识登记（Ga/Gy/DCC + N40/PFCP/Gx）
- [x] 5份SKILL知识登记
- [x] 1份特性文档清单登记
- [x] 1份设计文档登记
- [x] 1份业务感知全景登记
- [x] 所有路径相对本场景目录（`业务图谱体系/计费场景/`）准确
- [x] 核心方案 CS-CH-01~07 至少引用1份direct证据 + 1份supporting证据
- [x] 所有Feature对象引用对应 EV-FK-*
- [x] 所有核心Command对象引用对应 EV-FK-* + EV-CFA
- [x] 协议知识（SO-CH-10/11）完整引用 EV-PK-*
- [x] 证据可追溯链路验证（图谱对象 → 本索引 → 知识文档 → 原始md）

---

## 11. 证据扩展与维护

### 11.1 新增证据流程

1. 知识库扩展（新增特性/主题/协议）→ 产出新知识文档
2. 在本索引对应分类下追加 `EV-FK-*` / `EV-KB-*` / `EV-PK-*` 条目
3. 在引用该证据的图谱对象 `source_evidence_ids` 中追加新ID
4. 更新本索引 §1 总览统计

### 11.2 证据冲突处理

如发现证据冲突（如不同文档对同一参数描述不一致），按以下顺序处理：

1. 优先采信原始产品文档（output/UDG_*、output/UNC_*）
2. 次采信特性知识文档（feature-knowledge/，已审查）
3. 最后采信统一知识库（unified-knowledge/计费场景统一知识库.md，综合归纳）
4. 冲突记录到 `conflicts/` 目录，并在图谱对象标注冲突引用

---

## 12. 与带宽场景证据层的对比

| 维度 | 计费场景 | 带宽控制场景 |
|------|---------|------------|
| 证据总数 | 32 | 58 |
| 特性知识 | 14 EV-FK | 24 EV-FK |
| 跨特性分析 | 1 EV-CFA（580行） | 1 EV-CA-01（1119行） |
| 主题知识 | — | 32 EV-TK |
| 统一知识库 | 4 EV-KB | — |
| 业务图谱 | 2 EV-BS | — |
| **协议知识** | **2 EV-PK（★独有，1422行）** | — |
| 跨主题分析 | — | 1 EV-CA-02（862行） |
| SKILL知识 | 5 EV-SK | — |
| 文档清单 | 1 EV-FDL（154文件） | — |
| 设计文档 | 1 EV-DES | — |
| 业务感知全景 | 1 EV-BSA-全景 | — |

> 计费场景独有协议知识证据（Ga/Gy/DCC/N40/PFCP/Gx），支撑 SO-CH-10/11 两个协议栈SemanticObject，是计费场景区别于带宽场景的核心知识资产。

---

> 本索引为计费场景三层图谱的"证据层"，确保图谱任何结论都能反查到权威事实源，满足 CLAUDE.md §16 质量门禁的"可信度门禁"要求。
