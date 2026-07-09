# UPF网元对接三层图谱 · 第2层：特性图谱

> **文件定位**：`three-layer-graph/02-feature-graph.md`
> **Schema参考**：`三层图谱Schema-最终版-v0.1.md` §9 特性图谱
> **作用**：实例化 8 个目录原生 Feature + depends_on 边 + FeatureRule + FeatureTaskOrderEdge
> **数据来源**：`UDG初始配置与调测` 原始目录 + `three-layer-graph/00-overview.md`

---

## 0. 特性图谱总览

### 0.1 8 Feature 分组

| 分组 | Feature | 小计 |
|------|---------|------|
| 目录基础 | ND-FEAT-01 架构认知与角色判定 | 1 |
| 开局基础 | ND-FEAT-02 License与基础数据就绪 | 1 |
| 运维接入 | ND-FEAT-03 网管纳管与安全授权 | 1 |
| 接口对接 | ND-FEAT-04 控制面对接 / ND-FEAT-05 用户面接口对接 | 2 |
| 会话接入 | ND-FEAT-06 会话接入数据 | 1 |
| 路由实施 | ND-FEAT-07 路由组网实施 | 1 |
| 验证验收 | ND-FEAT-08 实例与整网调测 | 1 |
| **合计** | **8** | **8** |

### 0.2 特性来源声明

| 类型 | 数量 | 说明 |
|------|------|------|
| 目录原生特性 | 8 | 全部特性直接从目录模块抽象，不回写产品原始 feature_code |
| 产品原生特性引用 | 0 | 本场景不以产品原始特性树为主体 |

### 0.3 全局字段声明（status）

> **适用范围**：本文件 §1（8个Feature）所有对象。
> **声明**：除非特别标注，本文件所有 Feature 的 `status` 字段值均为 `active`。

---

## 1. Feature 实例化（8个）

### 1.1 目录基础

#### ND-FEAT-01 架构认知与角色判定

| 字段 | 值 |
|------|---|
| `feature_id` | `ND-FEAT-01` |
| `feature_name` | `架构认知与角色判定` |
| `feature_summary` | 负责解释 UDG 的部署角色、参考点、逻辑接口抽象和基本组网认知，是目录其余章节的前置语义底座 |
| `feature_group` | `目录基础` |
| `applicable_nf_map` | `UDG: UPF/PGW-U/SGW-U` |
| `variant_dimensions` | `部署角色`, `接口抽象策略`, `参考点映射` |
| `key_capabilities` | ① 部署角色判定 ② 参考点语义映射 ③ 逻辑接口命名约束 ④ 后续实施分支前置判断 |
| `source_evidence_ids` | `EV-FEAT-01`, `EV-TK-01` |

### 1.2 开局基础

#### ND-FEAT-02 License与基础数据就绪

| 字段 | 值 |
|------|---|
| `feature_id` | `ND-FEAT-02` |
| `feature_name` | `License与基础数据就绪` |
| `feature_summary` | 负责把网元从“可识别”推进到“可配置”，涵盖 License、NTP、网元信息、公共参数、MTU 与高危命令授权前置 |
| `feature_group` | `开局基础` |
| `applicable_nf_map` | `UDG: UPF/PGW-U/SGW-U` |
| `variant_dimensions` | `License路径`, `时间源`, `网元标识`, `MTU层级` |
| `key_capabilities` | ① License激活 ② 双时间源同步 ③ 网元身份初始化 ④ 公共参数成组配置 ⑤ MTU层级配置 |
| `source_evidence_ids` | `EV-FEAT-02`, `EV-TK-01`, `EV-TK-02` |

### 1.3 运维接入

#### ND-FEAT-03 网管纳管与安全授权

| 字段 | 值 |
|------|---|
| `feature_id` | `ND-FEAT-03` |
| `feature_name` | `网管纳管与安全授权` |
| `feature_summary` | 负责将网元纳入网管体系并打通安全维护入口，涵盖北向用户、SNMPv3、适配层、证书与授权 |
| `feature_group` | `运维接入` |
| `applicable_nf_map` | `UDG: UPF/PGW-U/SGW-U; Manager: MAE/U2020` |
| `variant_dimensions` | `管理平台`, `认证方式`, `证书开关` |
| `key_capabilities` | ① 北向账号配置 ② SNMPv3 安全接入 ③ 网管适配层接入 ④ 证书与授权前置 |
| `source_evidence_ids` | `EV-FEAT-03`, `EV-TK-02` |

### 1.4 接口对接

#### ND-FEAT-04 控制面对接

| 字段 | 值 |
|------|---|
| `feature_id` | `ND-FEAT-04` |
| `feature_name` | `控制面对接` |
| `feature_summary` | 负责建立 N4 控制面入口，形成与 SMF/PGW-C/SGW-C 的会话控制基础 |
| `feature_group` | `接口对接` |
| `applicable_nf_map` | `UDG: UPF/PGW-U/SGW-U; Peer: SMF/PGW-C/SGW-C` |
| `variant_dimensions` | `IP版本`, `N4if地址规划`, `多SMF场景` |
| `key_capabilities` | ① N4入口建立 ② 信令VPN承载 ③ UPF标识配置 |
| `source_evidence_ids` | `EV-FEAT-04`, `EV-TK-03` |

#### ND-FEAT-05 用户面接口对接

| 字段 | 值 |
|------|---|
| `feature_id` | `ND-FEAT-05` |
| `feature_name` | `用户面接口对接` |
| `feature_summary` | 负责建立 Sa、Sc、Pa、S11-U、SGi/N6、Nupf 等用户面或服务化接口 |
| `feature_group` | `接口对接` |
| `applicable_nf_map` | `UDG: UPF/PGW-U/SGW-U` |
| `variant_dimensions` | `接口组合`, `切片绑定`, `接口抽象合一`, `是否启用Nupf` |
| `key_capabilities` | ① 用户面逻辑接口配置 ② Nupf服务化接口 ③ 切片绑定分支 |
| `source_evidence_ids` | `EV-FEAT-05`, `EV-TK-03` |

### 1.5 会话接入

#### ND-FEAT-06 会话接入数据

| 字段 | 值 |
|------|---|
| `feature_id` | `ND-FEAT-06` |
| `feature_name` | `会话接入数据` |
| `feature_summary` | 负责完成 APN/DNN、地址池、地址段、地址分配规则等会话接入数据闭环 |
| `feature_group` | `会话接入` |
| `applicable_nf_map` | `UDG: UPF/PGW-U/SGW-U` |
| `variant_dimensions` | `LOCAL/EXTERNAL`, `IPv4/IPv6/双栈`, `地址分配模式` |
| `key_capabilities` | ① APN/DNN定义 ② 地址池与地址段组织 ③ 地址分配规则控制 |
| `source_evidence_ids` | `EV-FEAT-06`, `EV-TK-03` |

### 1.6 路由实施

#### ND-FEAT-07 路由组网实施

| 字段 | 值 |
|------|---|
| `feature_id` | `ND-FEAT-07` |
| `feature_name` | `路由组网实施` |
| `feature_summary` | 负责按目录中的各类组网分支实施 VPN、外联口、OSPF/BGP/静态、BFD、IPsec、GRE、MPLS VPN 和自动部署模板 |
| `feature_group` | `路由实施` |
| `applicable_nf_map` | `UDG: UPF/PGW-U/SGW-U` |
| `variant_dimensions` | `硬件形态`, `SDN/非SDN`, `自动/手动`, `IPv4/IPv6/双栈`, `OSPF/BGP/静态`, `IPsec/GRE/MPLS VPN` |
| `key_capabilities` | ① VPN与外联口基础 ② 多协议路由链 ③ BFD与隧道增强 ④ 自动部署/级联口分支 |
| `source_evidence_ids` | `EV-FEAT-07`, `EV-TK-04`, `EV-TK-05`, `EV-TK-06` |

### 1.7 验证验收

#### ND-FEAT-08 实例与整网调测

| 字段 | 值 |
|------|---|
| `feature_id` | `ND-FEAT-08` |
| `feature_name` | `实例与整网调测` |
| `feature_summary` | 负责把目录中的典型实例当作实施模板，并通过整网调测验证 FirstCall 与路由效果 |
| `feature_group` | `验证验收` |
| `applicable_nf_map` | `UDG: UPF/PGW-U/SGW-U` |
| `variant_dimensions` | `实例模板`, `调测阶段`, `异常分支` |
| `key_capabilities` | ① 典型模板比对 ② 路由和会话核查 ③ FirstCall验收 |
| `source_evidence_ids` | `EV-FEAT-08`, `EV-TK-07` |

---

## 2. depends_on 关系（7条）

| 起点 | 关系 | 终点 | 说明 |
|------|------|------|------|
| `ND-FEAT-02` | `depends_on` | `ND-FEAT-01` | 基础数据和 License 必须建立在角色与架构认知上 |
| `ND-FEAT-03` | `depends_on` | `ND-FEAT-02` | 网管接入依赖网元身份、时间和授权前置 |
| `ND-FEAT-04` | `depends_on` | `ND-FEAT-02` | N4 接口依赖基础就绪 |
| `ND-FEAT-05` | `depends_on` | `ND-FEAT-04` | 用户面实施以控制面入口稳定为前提 |
| `ND-FEAT-06` | `depends_on` | `ND-FEAT-05` | 会话接入依赖业务接口完成 |
| `ND-FEAT-07` | `depends_on` | `ND-FEAT-05` | 路由实施依赖外联和用户面接口边界清晰 |
| `ND-FEAT-08` | `depends_on` | `ND-FEAT-06` / `ND-FEAT-07` | 实例和调测必须建立在会话与路由闭环之后 |

---

## 3. FeatureRule（8条）

| `rule_id` | `owner_ref` | `rule_name` | `rule_type` | `rule_logic` | `source_evidence_ids` |
|-----------|-------------|-------------|-------------|--------------|----------------------|
| `FR-ND-01` | `ND-FEAT-01` | 架构先于实现 | `dependency_rule` | 理解架构章节不是背景资料，而是实施分支的前置决策源 | `EV-TK-01` |
| `FR-ND-02` | `ND-FEAT-02` | 基础数据必须成组生效 | `consistency_rule` | License、时间、网元信息、公共参数、MTU 应视为同一基础闭环 | `EV-TK-01`, `EV-TK-02` |
| `FR-ND-03` | `ND-FEAT-03` | 网管接入依赖安全前置 | `restriction_rule` | 纳管前必须满足密码重置、SNMPv3 密钥和证书前置要求 | `EV-TK-02` |
| `FR-ND-04` | `ND-FEAT-04` | N4为控制面入口 | `dependency_rule` | 控制面对接以 N4 为唯一主入口 | `EV-TK-03` |
| `FR-ND-05` | `ND-FEAT-05` | 用户面接口按角色裁剪 | `selection_rule` | Sa/Sc/Pa/S11-U/SGi/N6/Nupf 不是全配集合，应由角色和场景裁剪 | `EV-TK-03` |
| `FR-ND-06` | `ND-FEAT-06` | 地址池配置服从分配主体 | `scope_rule` | LOCAL 与 EXTERNAL 两种模式对应不同的会话接入配置边界 | `EV-TK-03` |
| `FR-ND-07` | `ND-FEAT-07` | 路由实施服从目录分支 | `selection_rule` | 硬件、SDN、协议、部署方式和 IP 版本是路由分支的稳定组织轴 | `EV-TK-04`, `EV-TK-05`, `EV-TK-06` |
| `FR-ND-08` | `ND-FEAT-08` | 实例优先于自由组合 | `validation_rule` | 典型实例应优先作为模板，调测以实例链路作为验收路径 | `EV-TK-07` |

---

## 4. Feature → ConfigTask（decomposes_to，8组）

| Feature | decomposes_to | Task集 | 说明 |
|---------|---------------|--------|------|
| `ND-FEAT-01` | `T-ND-01` | `T-ND-01` | 架构认知前置 |
| `ND-FEAT-02` | `T-ND-02`, `T-ND-03` | `T-ND-02~03` | License与基础数据闭环 |
| `ND-FEAT-03` | `T-ND-04`, `T-ND-05` | `T-ND-04~05` | 安全与纳管闭环 |
| `ND-FEAT-04` | `T-ND-06` | `T-ND-06` | N4入口 |
| `ND-FEAT-05` | `T-ND-07`, `T-ND-08` | `T-ND-07~08` | 用户面接口与Nupf分支 |
| `ND-FEAT-06` | `T-ND-09` | `T-ND-09` | 会话接入数据 |
| `ND-FEAT-07` | `T-ND-10`, `T-ND-11`, `T-ND-12`, `T-ND-13` | `T-ND-10~13` | 路由实施主链 |
| `ND-FEAT-08` | `T-ND-14` | `T-ND-14` | 实例与验收 |

---

## 5. FeatureTaskOrderEdge（12条）

| `edge_id` | `owner_ref` | `from_task_ref` | `to_task_ref` | `relation_type` | `requiredness` | `source_evidence_ids` |
|-----------|-------------|-----------------|---------------|-----------------|----------------|----------------------|
| `FE-ND-01` | `ND-FEAT-01` | `T-ND-01` | `T-ND-02` | `precedes` | `required` | `EV-TK-01` |
| `FE-ND-02` | `ND-FEAT-02` | `T-ND-02` | `T-ND-03` | `precedes` | `required` | `EV-TK-01`, `EV-TK-02` |
| `FE-ND-03` | `ND-FEAT-03` | `T-ND-04` | `T-ND-05` | `precedes` | `required` | `EV-TK-02` |
| `FE-ND-04` | `ND-FEAT-04` | `T-ND-05` | `T-ND-06` | `depends_on` | `required` | `EV-TK-02`, `EV-TK-03` |
| `FE-ND-05` | `ND-FEAT-05` | `T-ND-06` | `T-ND-07` | `precedes` | `required` | `EV-TK-03` |
| `FE-ND-06` | `ND-FEAT-05` | `T-ND-07` | `T-ND-08` | `fallback_to` | `optional` | `EV-TK-03` |
| `FE-ND-07` | `ND-FEAT-06` | `T-ND-07` | `T-ND-09` | `depends_on` | `required` | `EV-TK-03` |
| `FE-ND-08` | `ND-FEAT-07` | `T-ND-10` | `T-ND-11` | `precedes` | `required` | `EV-TK-04`, `EV-TK-05`, `EV-TK-06` |
| `FE-ND-09` | `ND-FEAT-07` | `T-ND-11` | `T-ND-12` | `precedes` | `optional` | `EV-TK-04`, `EV-TK-05`, `EV-TK-06` |
| `FE-ND-10` | `ND-FEAT-07` | `T-ND-10` | `T-ND-13` | `fallback_to` | `optional` | `EV-TK-04`, `EV-TK-05`, `EV-TK-06` |
| `FE-ND-11` | `ND-FEAT-08` | `T-ND-11` | `T-ND-14` | `depends_on` | `required` | `EV-TK-07` |
| `FE-ND-12` | `ND-FEAT-08` | `T-ND-12` | `T-ND-14` | `depends_on` | `optional` | `EV-TK-07` |

---

## 6. 合规声明

- 本文件中的 Feature 为目录原生特性
- Feature 通过 `decomposes_to` 落到任务层，不直接绑定命令层
- 本场景特性图谱服务前端链路 `方案 → 特性 → 任务`
