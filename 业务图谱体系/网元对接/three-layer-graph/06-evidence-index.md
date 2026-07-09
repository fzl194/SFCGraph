# UPF网元对接三层图谱 · 第6层：证据层索引

> **文件定位**：`three-layer-graph/06-evidence-index.md`
> **Schema参考**：`三层图谱Schema-最终版-v0.1.md` §10 EvidenceSource
> **作用**：为本场景三层图谱所有对象的 `source_evidence_ids` 字段提供可追溯的证据源注册表

---

## 1. EvidenceSource 总览

UPF网元对接场景三层图谱的证据源共分三类，合计 **17份知识资产**：

| 证据类型 | ID前缀 | 数量 | `evidence_type` | `status` | 路径根目录 |
|---------|--------|------|-----------------|----------|-----------|
| 原始目录基线 | `EV-BS-*` | 1 | markdown | active | `output/UDG_Product_Documentation_CH_20.15.2/.../UDG初始配置与调测/` |
| 目录章节/分支证据 | `EV-TK-*` | 8 | markdown | active | 原始目录各章节/分支 |
| 图谱特性登记 | `EV-FEAT-*` | 8 | markdown | active | `three-layer-graph/02-feature-graph.md` |
| **合计** | — | **17** | — | — | — |

> 所有证据路径相对本场景目录 `业务图谱体系/网元对接/` 或其权威原始目录。

---

## 2. 原始目录基线证据（EV-BS-*，1份）

| Evidence ID | 标题 | 文件路径 |
|------------|------|---------|
| `EV-BS-01` | UPF网元对接目录与三层图谱重构基线 | `output/UDG_Product_Documentation_CH_20.15.2/网络部署/初始配置/UDG初始配置与调测/` |

---

## 3. 目录章节证据（EV-TK-*，8份）

| Evidence ID | 标题 | 文件路径 | 支撑范围 |
|------------|------|---------|---------|
| `EV-TK-01` | 架构认知章节证据 | `.../UDG初始配置与调测/了解组网架构*.md` | BusinessDomain、NetworkScenario、ND-FEAT-01 |
| `EV-TK-02` | 基础就绪与网管纳管证据 | `.../License申请与加载/` + `.../基础数据配置/` + `.../修改MTU值_75096774.md` + `.../配置网元和网管对接_34981624.md` | ND-FEAT-02/03、T-ND-02~05、基础命令 |
| `EV-TK-03` | 控制面、用户面与会话接入证据 | `.../组网对接配置/` | ND-FEAT-04/05/06、T-ND-06~09、接口命令 |
| `EV-TK-04` | 路由实施总览与无NP卡分支证据 | `.../组网路由配置/配置VNF侧IP路由数据（无NP卡_非SDN）*/` | ND-FEAT-07、路由主链 |
| `EV-TK-05` | NP卡直连PE分支证据 | `.../组网路由配置/配置VNF侧IP路由数据（NP卡直连PE）*/` | 路由分支、自动部署/级联 |
| `EV-TK-06` | 网络加速卡与SDN分支证据 | `.../组网路由配置/配置VNF侧IP路由数据（网络加速卡直连DC-GW）*/` + `.../组网路由配置/配置VNF侧IP路由（SDN）*/` | 路由分支、SDN/BFD/MPLS |
| `EV-TK-07` | 典型配置实例与整网调测证据 | `.../典型配置实例/` + `.../整网调测_31373646.md` | ND-FEAT-08、T-ND-14、验收命令 |
| `EV-TK-08` | 路由目录结构补充证据 | `.../组网路由配置/` | 路由目录边界补充 |

---

## 4. 图谱特性登记证据（EV-FEAT-*，8份）

| Evidence ID | 对应特性 | 文件路径 |
|------------|---------|---------|
| `EV-FEAT-01` | ND-FEAT-01 架构认知与角色判定 | `three-layer-graph/02-feature-graph.md#nd-feat-01-架构认知与角色判定` |
| `EV-FEAT-02` | ND-FEAT-02 License与基础数据就绪 | `three-layer-graph/02-feature-graph.md#nd-feat-02-license与基础数据就绪` |
| `EV-FEAT-03` | ND-FEAT-03 网管纳管与安全授权 | `three-layer-graph/02-feature-graph.md#nd-feat-03-网管纳管与安全授权` |
| `EV-FEAT-04` | ND-FEAT-04 控制面对接 | `three-layer-graph/02-feature-graph.md#nd-feat-04-控制面对接` |
| `EV-FEAT-05` | ND-FEAT-05 用户面接口对接 | `three-layer-graph/02-feature-graph.md#nd-feat-05-用户面接口对接` |
| `EV-FEAT-06` | ND-FEAT-06 会话接入数据 | `three-layer-graph/02-feature-graph.md#nd-feat-06-会话接入数据` |
| `EV-FEAT-07` | ND-FEAT-07 路由组网实施 | `three-layer-graph/02-feature-graph.md#nd-feat-07-路由组网实施` |
| `EV-FEAT-08` | ND-FEAT-08 实例与整网调测 | `three-layer-graph/02-feature-graph.md#nd-feat-08-实例与整网调测` |

---

## 5. 证据使用规范

### 5.1 图谱对象引用方式

每个图谱对象的 `source_evidence_ids` 字段填写本表中的 `evidence_id`，遵循以下规范：

```yaml
- id: CS-ND-03
  type: ConfigurationSolution
  source_evidence_ids:
    - EV-BS-01
    - EV-TK-03

- id: ND-FEAT-07
  type: Feature
  source_evidence_ids:
    - EV-FEAT-07
    - EV-TK-04
    - EV-TK-05
    - EV-TK-06

- id: CMD-ND-046
  type: MMLCommand
  source_evidence_ids:
    - EV-TK-04
    - EV-TK-05
```

### 5.2 证据强度等级

| 等级 | 判定 | 典型证据 |
|------|------|---------|
| `direct` | 结论与原文明确对应 | 目录中的命令、步骤、分支选择 |
| `supporting` | 原文支持但需抽象组织 | 方案闭包、Feature分组 |
| `inferred` | 由多条目录证据综合归纳 | 端到端方案链、对象归类 |

> 本图谱正式对象的 `source_evidence_ids` 至少达到 `supporting` 强度；命令层对象默认 `direct`。

### 5.3 证据可追溯链路

图谱任意对象 → `source_evidence_ids` → 本索引 → 原始目录章节或图谱登记页。

完整链路示例：

```text
CS-ND-03（控制面与用户面对接）
  → source_evidence_ids: [EV-BS-01, EV-TK-03]
    → UDG初始配置与调测目录基线
    → 组网对接配置原始章节
      → N4/用户面/会话接入原始md
```

---

## 6. 证据完整性检查清单

- [x] 1份目录基线证据已登记
- [x] 8份目录章节/分支证据已登记
- [x] 8份图谱特性登记证据已登记
- [x] 业务层、特性层、任务层、命令层均可回溯到本索引

---

> 本文件服务三层图谱全部对象的证据追溯，不服务旧版产品特性引用体系。
