# 06 证据层 Evidence Index（目录原生重构版）

> 本版 EvidenceSource 直接围绕目录章节、目录分支、目录实例和图谱产物注册。

---

## 1. EvidenceSource 主注册表（17条）

| `evidence_id` | `evidence_type` | `title` | `path` | `source_system` | `status` |
|---|---|---|---|---|---|
| `EV-BS-01` | `markdown` | UPF网元对接目录与三层图谱重构基线 | `output/UDG_Product_Documentation_CH_20.15.2/网络部署/初始配置/UDG初始配置与调测/` | `原始目录` | `active` |
| `EV-TK-01` | `markdown` | 架构认知章节证据 | `.../UDG初始配置与调测/了解组网架构*.md` | `原始目录` | `active` |
| `EV-TK-02` | `markdown` | 基础就绪与网管纳管证据 | `.../License申请与加载/` + `.../基础数据配置/` + `.../修改MTU值_75096774.md` + `.../配置网元和网管对接_34981624.md` | `原始目录` | `active` |
| `EV-TK-03` | `markdown` | 控制面、用户面与会话接入证据 | `.../组网对接配置/` | `原始目录` | `active` |
| `EV-TK-04` | `markdown` | 路由实施总览与无NP卡分支证据 | `.../组网路由配置/配置VNF侧IP路由数据（无NP卡_非SDN）*/` | `原始目录` | `active` |
| `EV-TK-05` | `markdown` | NP卡直连PE分支证据 | `.../组网路由配置/配置VNF侧IP路由数据（NP卡直连PE）*/` | `原始目录` | `active` |
| `EV-TK-06` | `markdown` | 网络加速卡与SDN分支证据 | `.../组网路由配置/配置VNF侧IP路由数据（网络加速卡直连DC-GW）*/` + `.../组网路由配置/配置VNF侧IP路由（SDN）*/` | `原始目录` | `active` |
| `EV-TK-07` | `markdown` | 典型配置实例与整网调测证据 | `.../典型配置实例/` + `.../整网调测_31373646.md` | `原始目录` | `active` |
| `EV-TK-08` | `markdown` | 路由目录结构补充证据 | `.../组网路由配置/` | `原始目录` | `active` |
| `EV-FEAT-01` | `markdown` | 目录原生特性：架构认知与角色判定 | `three-layer-graph/02-feature-graph.md#nd-feat-01-架构认知与角色判定` | `图谱产物` | `active` |
| `EV-FEAT-02` | `markdown` | 目录原生特性：License与基础数据就绪 | `three-layer-graph/02-feature-graph.md#nd-feat-02-license与基础数据就绪` | `图谱产物` | `active` |
| `EV-FEAT-03` | `markdown` | 目录原生特性：网管纳管与安全授权 | `three-layer-graph/02-feature-graph.md#nd-feat-03-网管纳管与安全授权` | `图谱产物` | `active` |
| `EV-FEAT-04` | `markdown` | 目录原生特性：控制面对接 | `three-layer-graph/02-feature-graph.md#nd-feat-04-控制面对接` | `图谱产物` | `active` |
| `EV-FEAT-05` | `markdown` | 目录原生特性：用户面接口对接 | `three-layer-graph/02-feature-graph.md#nd-feat-05-用户面接口对接` | `图谱产物` | `active` |
| `EV-FEAT-06` | `markdown` | 目录原生特性：会话接入数据 | `three-layer-graph/02-feature-graph.md#nd-feat-06-会话接入数据` | `图谱产物` | `active` |
| `EV-FEAT-07` | `markdown` | 目录原生特性：路由组网实施 | `three-layer-graph/02-feature-graph.md#nd-feat-07-路由组网实施` | `图谱产物` | `active` |
| `EV-FEAT-08` | `markdown` | 目录原生特性：实例与整网调测 | `three-layer-graph/02-feature-graph.md#nd-feat-08-实例与整网调测` | `图谱产物` | `active` |

---

## 2. 证据流转

| 证据 | 主要消费层 | 用途 |
|---|---|---|
| `EV-BS-01` | 第1层 | 场景和目录边界基线 |
| `EV-TK-01` | 第1层/第2层/第3层 | 架构与角色判定 |
| `EV-TK-02` | 第1层/第2层/第3层/第4层 | License、基础数据、授权、纳管 |
| `EV-TK-03` | 第1层/第2层/第3层/第4层 | N4、用户面接口、会话接入 |
| `EV-TK-04~06` | 第1层/第2层/第3层/第4层 | 路由组网各实施分支 |
| `EV-TK-07` | 第1层/第3层/第4层 | 典型实例与整网调测 |
| `EV-TK-08` | 第1层 | 路由目录结构补充 |
| `EV-FEAT-01~08` | 第2层 | 目录原生特性自身登记 |

---

## 3. 原始目录索引口径

本版不再把原始目录拆成“产品特性证据 + 主题证据”两套中心。
统一原则是：

1. 目录章节作为第一层证据源
2. 目录分支作为路由实施证据源
3. 目录实例与调测作为验收证据源
4. 图谱中抽象出的目录原生特性单独登记为 `EV-FEAT-*`

---

## 4. 合规声明

- 全部 `EvidenceSource` 符合 Schema §8.11
- `path` 统一可回溯到原始目录或图谱产物
- 本版证据层服务“目录原生重构”，不再服务旧版产品特性引用体系
