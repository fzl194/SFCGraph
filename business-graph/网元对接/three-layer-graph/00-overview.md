# 00 总览 Overview — 网元对接业务域 / UPF网元对接子场景（目录原生重构版）

> 三层图谱入口 | 业务域 `BD-ND` 网元对接 | 子场景 `NS-ND-UPF` UPF网元对接
> 版本 2026-07-09 | Schema v0.1
> **重构口径**：本版不再以产品文档既有 `GWFD/IPFD/NPFD` 特性树为主体，而是**完全基于原始目录**
> `output/UDG_Product_Documentation_CH_20.15.2/网络部署/初始配置/UDG初始配置与调测/`
> 对目录章节、实施闭环、组网分支和调测路径进行重新建模。

---

## 1. 场景定位

| 对象 | 标识 | 说明 |
|---|---|---|
| BusinessDomain | `BD-ND` 网元对接 | 云核心网开局对接域，关注 UDG 如何作为 UPF/PGW-U/SGW-U 接入现网 |
| NetworkScenario | `NS-ND-UPF` UPF网元对接 | 以 UDG 初始配置与调测目录为唯一权威源，完成开局配置、业务接口对接、路由组网与 FirstCall 验证 |
| 典型结果 | FirstCall 打通 | 完成基础就绪、网管纳管、N4/用户面接口、会话接入、路由组网及端到端调测 |

---

## 2. 本版重构原则

| 维度 | 旧版口径 | 本版口径 |
|---|---|---|
| 特性来源 | 先反查产品原始特性，再映射目录 | **直接从目录章节抽象场景特性** |
| 业务主体 | 对接面 CS + 产品特性支撑 | **目录模块闭环 + 目录分支决策** |
| 证据组织 | 产品特性和主题分拆取证 | **目录章节、目录分支、目录实例、目录调测为主证据** |
| 三层关系 | 特性驱动较强 | **目录驱动，特性/任务/命令都服从目录结构** |

---

## 3. 三层对象计数

| 层 | 文件 | 对象类型 | 数量 |
|---|---|---|---|
| 第1层 业务图谱 | 01-business-graph | BusinessDomain / NetworkScenario | 1 / 1 |
|  |  | ConfigurationSolution | 5 |
|  |  | DecisionPoint | 16 |
|  |  | BusinessRule | 10 |
|  |  | SemanticObject | 25 |
| 第2层 特性图谱 | 02-feature-graph | Feature | 8 |
|  |  | FeatureRule | 8 |
|  |  | depends_on / decomposes_to | 7 / 14 |
| 第3层 任务原子层 | 03-task-layer | ConfigTask | 14 |
|  |  | TaskRule | 12 |
|  |  | TaskCommandOrderEdge / FeatureTaskOrderEdge | 26 / 12 |
| 第4层 命令图谱 | 04-command-graph | MMLCommand | 62 |
|  |  | ConfigObject | 34 |
|  |  | CommandRule | 14 |
| 第5层 跨层映射 | 05-cross-layer-mapping | 跨层边汇总 + 端到端链路 | 3 条完整链路 |
| 第6层 证据层 | 06-evidence-index | EvidenceSource | 17 |

---

## 4. 本版三层主链

```text
业务图谱(01)
  BD-ND 网元对接
    → NS-ND-UPF UPF网元对接
    → CS-ND-01 架构与基础就绪
    → CS-ND-02 网管与安全接入
    → CS-ND-03 控制面与用户面对接
    → CS-ND-04 路由组网实施
    → CS-ND-05 实例验证与整网调测

特性图谱(02)
  ND-FEAT-01 架构认知与角色判定
  ND-FEAT-02 License与基础数据就绪
  ND-FEAT-03 网管纳管与安全授权
  ND-FEAT-04 控制面对接
  ND-FEAT-05 用户面接口对接
  ND-FEAT-06 会话接入数据
  ND-FEAT-07 路由组网实施
  ND-FEAT-08 实例与整网调测

任务原子层(03)
  14 个目录原生 ConfigTask

命令图谱(04)
  62 条目录高频 MMLCommand

证据层(06)
  17 个目录驱动 EvidenceSource
```

---

## 5. 5 个目录原生 ConfigurationSolution

| CS | 名称 | 对应目录 | 作用 |
|---|---|---|---|
| `CS-ND-01` | 架构与基础就绪 | `了解组网架构/` `License申请与加载/` `基础数据配置/` `修改MTU值_*.md` | 形成开局前置条件 |
| `CS-ND-02` | 网管与安全接入 | `配置网元和网管对接_*.md` + 二次授权/证书相关章节 | 形成可纳管、可维护的运维入口 |
| `CS-ND-03` | 控制面与用户面对接 | `组网对接配置/` | 建立 N4、业务接口、会话接入闭环 |
| `CS-ND-04` | 路由组网实施 | `组网路由配置/` | 按硬件/SDN/协议/IP版本完成路由实施 |
| `CS-ND-05` | 实例验证与整网调测 | `典型配置实例/` `整网调测_*.md` | 验证端到端效果并沉淀实例模板 |

---

## 6. 目录原生 Feature 集

| Feature | 名称 | 来源章节 |
|---|---|---|
| `ND-FEAT-01` | 架构认知与角色判定 | `了解组网架构/` |
| `ND-FEAT-02` | License与基础数据就绪 | `License申请与加载/` `基础数据配置/` `修改MTU值_*.md` |
| `ND-FEAT-03` | 网管纳管与安全授权 | `配置网元和网管对接_*.md` + 二次授权 |
| `ND-FEAT-04` | 控制面对接 | `配置N4(N4_Sxa_Sxb)接口数据_*.md` |
| `ND-FEAT-05` | 用户面接口对接 | `配置Sa/Sc/Pa/S11-U/SGi_N6/Nupf接口数据_*.md` |
| `ND-FEAT-06` | 会话接入数据 | `配置会话接入数据_*.md` |
| `ND-FEAT-07` | 路由组网实施 | `组网路由配置/` 全量分支 |
| `ND-FEAT-08` | 实例与整网调测 | `典型配置实例/` `整网调测_*.md` |

---

## 7. 核心决策树

| 决策组 | 关键问题 |
|---|---|
| 架构决策 | UDG 部署角色是什么，接口抽象策略是什么 |
| 接口决策 | 需要哪些业务接口，是否切片绑定，地址池由谁分配 |
| 路由决策 | 硬件类型 / SDN与否 / 自动或手动 / 协议类型 / IPv4或IPv6或双栈 / 是否叠加 IPsec/GRE/MPLS VPN |
| 调测决策 | 按哪个实例模板落地，异常落在哪个排查分支 |

---

## 8. 端到端闭环

```text
架构认知
  → License与基础数据
  → 网管与安全接入
  → N4控制面对接
  → 用户面接口对接
  → 会话接入
  → 路由组网实施
  → 典型实例比对
  → 整网调测与 FirstCall
```

---

## 9. 文件导航

| 文件 | 内容 |
|---|---|
| 00-overview.md | 本文件，总览与重构口径 |
| 01-business-graph.md | 目录原生业务图谱 |
| 02-feature-graph.md | 8 个目录原生特性 |
| 03-task-layer.md | 14 个目录原生任务 |
| 04-command-graph.md | 62 条目录高频命令 |
| 05-cross-layer-mapping.md | 跨层边汇总与 3 条端到端链路 |
| 06-evidence-index.md | 17 个 EvidenceSource |

---

## 10. 合规声明

- 遵循 `业务图谱体系/三层图谱Schema-最终版-v0.1.md` §8-§13
- 业务层不直接绑定 `ConfigObject` / `MMLCommand`
- 特性层不再以产品原始特性编号作为主体
- 全部对象以给定目录中的 `md` 为权威源
