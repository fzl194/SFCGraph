# APN 业务域三层图谱 · 第1层：业务图谱

> **文件定位**：`three-layer-graph/01-business-graph.md`
> **Schema 参考**：`三层图谱Schema-最终版-v0.1.md` §8 业务图谱（§8.3 ~ §8.11 字段 + §8.12 关系）
> **本体参考**：`三层图谱本体标准定义.md`
> **作用**：实例化 APN 业务域业务层对象（BD / NS / CS / DP / BR / SO）及其关系边
> **★ 独立性说明**：APN 业务域是**独立 BusinessDomain**（接入与会话管理），非"业务感知"子场景。与计费场景（BD-CH-01）、带宽控制场景（BD-BW-01）共享通用 ConfigTask/ConfigObject，但不共享根对象。

---

## 0. 适用定义与来源

### 0.1 根定义
- `三层图谱本体标准定义.md`
- `三层图谱Schema-最终版-v0.1.md`

### 0.2 APN 业务域知识来源
- `cross-topic-analysis.md`（Stage 3 横向综合分析，53KB，4 topic + 37 feature 综合定稿 49 对象）
- `APN意图澄清知识库.md`（EV-BS-01 意图澄清证据）
- `APN配置树.md`（EV-BS-02 配置树证据）
- `topic-knowledge/`（4 文件：Batch-14 业务场景、归纳-四维度、归纳-APN底座三维度、归纳-配置树修正与Stage3待解决项）
- `feature-knowledge/`（37 特性横向抽取）

### 0.3 证据编号映射（Stage 5 审查追溯用）

> **★ 统一数字格式**：本图谱所有 `source_evidence_ids` 严格使用 `06-evidence-index.md` 注册的数字格式（`EV-FK-01~37` / `EV-TK-01~04` / `EV-CA-01~02` / `EV-BS-01~02`）。历史语义别名（`EV-FK-{特性ID}`、`EV-TK-14-{场景号}`）已于 Stage 5 批次1 全部替换为数字格式；下表"数字格式"列为权威引用，"语义别名（已弃用）"列仅作追溯参考。

| 数字格式（权威） | 含义 | 物理来源 | 语义别名（已弃用，仅追溯用） |
|---------|------|---------|---------|
| `EV-BS-01` | APN 意图澄清知识库 | `APN意图澄清知识库.md` | — |
| `EV-BS-02` | APN 配置树 | `APN配置树.md` | — |
| `EV-CA-02` | cross-topic 综合分析（第1层直接来源） | `cross-topic-analysis.md` | — |
| `EV-TK-01` | Batch-14 业务场景方案（CS-APN-01~09 共用） | `topic-knowledge/Batch-14-业务场景方案.md` | `EV-TK-14-01`~`EV-TK-14-09` |
| `EV-FK-06` | GWFD-010105 用户面地址分配特性知识 | `feature-knowledge/GWFD-010105*.md` | `EV-FK-010105` |
| `EV-FK-08` | GWFD-020421 基于位置地址分配特性知识 | `feature-knowledge/GWFD-020421*.md` | `EV-FK-020421` |
| `EV-FK-11` | GWFD-020412 L2TP VPN 特性知识 | `feature-knowledge/GWFD-020412*.md` | `EV-FK-020412` |
| `EV-FK-16` | GWFD-020403 IPv4v6 双栈接入特性知识 | `feature-knowledge/GWFD-020403*.md` | `EV-FK-020403` |
| `EV-FK-02`/`EV-FK-01` | 会话管理根底座（C/U 面） | `feature-knowledge/WSFD-010501*.md` / `GWFD-010101*.md` | `EV-FK-010501`/`EV-FK-010101` |
| `EV-FK-24`/`EV-FK-25`/`EV-FK-27`/`EV-FK-28` | Radius 鉴权链特性 | `feature-knowledge/WSFD-011305*.md` 等 | `EV-FK-011305`/`EV-FK-011306`/`EV-FK-108007`/`EV-FK-011307` |
| `EV-FK-26` | 底层 AKA 网络接入鉴权 | `feature-knowledge/WSFD-010301*.md` | `EV-FK-010301` |
| `EV-FK-12`/`EV-FK-13` | UNC 地址分配决策 | `feature-knowledge/WSFD-010502*.md` / `WSFD-010504*.md` | `EV-FK-010502`/`EV-FK-010504` |
| `EV-FK-34`/`EV-FK-35` | 网元选择 | `feature-knowledge/WSFD-107010*.md` / `WSFD-010202*.md` | `EV-FK-107010`/`EV-FK-010202` |
| `EV-FK-36`/`EV-FK-37` | 接入控制（C 面权限 / U 面带宽） | `feature-knowledge/WSFD-106003*.md` / `GWFD-010151*.md` | `EV-FK-106003`/`EV-FK-010151` |
| `EV-FK-04`/`EV-FK-03`/`EV-FK-05` | 签约/并发/别名 | `feature-knowledge/WSFD-010400*.md` 等 | `EV-FK-010400`/`EV-FK-010503`/`EV-FK-106203` |
| `EV-FK-29`/`EV-FK-30`/`EV-FK-31` | IPFD 隧道（GRE/IPSec） | `feature-knowledge/IPFD-015002*.md` 等 | `EV-FK-015002`/`EV-FK-015004`/`EV-FK-016000` |
| `EV-FK-32`/`EV-FK-33` | MPLS VPN | `feature-knowledge/GWFD-020411*.md` / `WSFD-104411*.md` | `EV-FK-020411`/`EV-FK-104411` |
| `EV-FK-22`/`EV-FK-23` | DHCP/DHCPv6 代理 | `feature-knowledge/WSFD-104413*.md` / `WSFD-104005*.md` | `EV-FK-104413`/`EV-FK-104005` |
| `EV-FK-18`/`EV-FK-20`/`EV-FK-19`/`EV-FK-17`/`EV-FK-21` | IPv6 承载链 | `feature-knowledge/GWFD-020401*.md` 等 | `EV-FK-020401`/`EV-FK-020406`/`EV-FK-104001`/`EV-FK-104002`/`EV-FK-104004` |

> **完整 EV-FK ↔ 特性 ID 映射**见 `02-feature-graph.md` §0.4（权威：按 `apn-feature-doc-list.md` 顺序 EV-FK-01~37）。

---

## 1. BusinessDomain + NetworkScenario

### 1.1 BusinessDomain

| 字段 | 值 |
|------|---|
| `domain_id` | `BD-APN-01` |
| `domain_name` | `接入与会话管理` |
| `domain_summary` | UE 从附着到 PDU/PDN 会话建立的完整接入链路：身份验证、接入权限判定、地址分配、网元选择、隧道接入、会话治理；APN/DNN 是业务接入的统一锚点 |
| `status` | `active` |
| `source_evidence_ids` | `EV-BS-01`, `EV-BS-02`, `EV-CA-02` |

> **★ 独立 BD 定位**：APN 与"业务感知"（BD-CH-01 / BD-BW-01）是**并列独立域**。业务感知域对会话内流量做策略/计费控制，APN 域解决"UE 如何进入网络、如何获得地址、如何接入目标 DN"——两者通过 PDU 会话上下文（SO-APN-SESSION-CONTEXT）协同，但根对象不重叠。

### 1.2 NetworkScenario

| 字段 | 值 |
|------|---|
| `scenario_id` | `NS-APN-01` |
| `scenario_name` | `APN 开通场景` |
| `scenario_summary` | 将不同业务诉求（工控内网、IoT 上报、宽带、VoLTE、企业 AAA、DHCP 迁移、远程办公、区域运营、双栈加密）映射到 APN 4 维度决策（地址分配 × 鉴权 × 接入方式 × 地址类型）与 3 类底座支撑（会话管理 × 网元选择 × 接入控制）的组合方案 |
| `judgment_basis` | 需为 UE 分配 IP 地址并建立 PDU/PDN 会话；或需对接 Radius/DHCP/AAA 外部系统；或需配置隧道（IPSec/GRE/MPLS/L2TP）接入企业 DN；或需按区域/位置/双栈/并发维度治理 APN 接入 |
| `typical_outcome` | UE 获得 IPv4/IPv6/双栈地址，PDU 会话建立，按签约与策略接入目标网络；可按 APN 粒度差异化鉴权、分配、限速、映射 |
| `status` | `active` |
| `source_evidence_ids` | `EV-BS-01`, `EV-BS-02`, `EV-CA-02`, `EV-TK-01`, `EV-FK-06`, `EV-FK-02` |

#### 场景边界

**覆盖范围**：
- 产品：UDG（用户面 UPF/PGW-U，17 特性）+ UNC（控制面 SMF/PGW-C/SGSN/MME/AMF，18 特性）+ IPFD（隧道基础，2 特性）
- 网元：UPF/PGW-U（UDG）、SMF/PGW-C/AMF/SGSN/MME（UNC）
- 接口：N4（PFCP，5G）、Sxa/Sxb（4G CUPS）、Gn/Gp（2-3G）、Gx/N7（策略）、Radius/DHCP（外部地址/鉴权）
- 决策维度：4 开通主线（地址分配 × 鉴权 × 接入方式 × 地址类型）+ 3 底座支撑（会话管理 × 网元选择 × 接入控制）

**不覆盖范围**（相邻场景）：
- 计费场景（BD-CH-01）：差异化计费、配额计费动作、Ga/Gy/N40 上报
- 带宽控制场景（BD-BW-01）：BWM 限速、FUP 降速、GBR 保证、ADC 应用感知
- 访问限制场景：URL 过滤、重定向阻断（非 APN 接入权限范畴）

---

## 2. ConfigurationSolution（9 个方案闭包）

> **拆分依据**：`cross-topic-analysis.md` §6.1（9 场景定稿）+ §8.1（9 场景归并表）。
> 9 方案按业务场景划分，每方案是 4 开通主线维度的稳定组合 + 主特性集合。
> **★ uses_feature 严格指向 Feature**（Schema §13 禁止 CS→ConfigObject / CS→MMLCommand 直接绑定）。

### 2.1 CS-APN-01 工厂工控访问内网方案

| 字段 | 值 |
|------|---|
| `solution_id` | `CS-APN-01` |
| `solution_name` | `工厂工控访问内网方案` |
| `solution_summary` | 工厂 UE 通过 IPSec 隧道接入，UDM 静态签约固定 IP，NON_TRANS 鉴权对接企业 Radius，IPv4 单栈访问工控内网 |
| `design_intent` | 解决"固定终端、固定地址、加密隧道接入内网"的工控场景：设备地址不变、链路加密、企业自管鉴权 |
| `core_mechanism_combo` | `UDM 静态签约(Framed-IP) → NON_TRANS 鉴权(UE 透传账密→UNC→Radius) → IPSec 隧道封装 → IPv4 单栈` |
| `status` | `active` |
| `source_evidence_ids` | `EV-TK-01`, `EV-CA-02`, `EV-FK-12`, `EV-FK-24`, `EV-FK-30` |

**scopes**: subscriber（单用户静态 IP）、access（IPSec 接入内网）

**participants**:
- UE（工控终端，endpoint，terminal_side）
- UNC/SMF（静态签约读取 + NON_TRANS 鉴权 + IPSec 对称部署，control_plane）
- UDG/UPF（用户面 IPSec 隧道终结，user_plane）
- UDM（静态签约数据源，external_system）
- 企业 Radius Server（AAA 鉴权，external_system）

**uses_feature**: `WSFD-010502`, `WSFD-011305`, `WSFD-011306`, `IPFD-015004`, `IPFD-016000`, `WSFD-010301`
**uses_semantic_object**: `SO-APN-ADDRESS-POOL`, `SO-APN-AUTH-AAA`, `SO-APN-TUNNEL`, `SO-APN-SUBSCRIPTION`
**constrained_by**: `BR-APN-RADIUS-CASCADE`, `BR-APN-GRE-IPSEC-SRC-EXCL`, `BR-APN-SECOND-AUTH-PROTO`

### 2.2 CS-APN-02 智慧农业传感器上报方案

| 字段 | 值 |
|------|---|
| `solution_id` | `CS-APN-02` |
| `solution_name` | `智慧农业传感器上报方案` |
| `solution_summary` | 大量 IoT 传感器通过 APN/DNN 粒度动态分配 IPv4 地址，透明接入免鉴权，NAT 直连上报告警数据 |
| `design_intent` | 解决"海量低成本终端、免鉴权、动态地址"的 IoT 场景：终端无键盘无法输入账密、地址池复用 |
| `core_mechanism_combo` | `UPF 本地池基于 APN 分配(POOLTYPE=LOCAL) → TRANS_NON_AUTH 透明接入(免鉴权) → NAT 直连上报 → IPv4 单栈` |
| `status` | `active` |
| `source_evidence_ids` | `EV-TK-01`, `EV-CA-02`, `EV-FK-06` |

**scopes**: access（APN/DNN 粒度地址池）、subscription（会话级上报）

**participants**:
- IoT 传感器（endpoint，terminal_side）
- UDG/UPF（本地地址池分配 + NAT，user_plane）
- UNC/SMF（PDU 会话建立控制，control_plane）

**uses_feature**: `GWFD-010105`, `GWFD-010101`, `WSFD-010501`
**uses_semantic_object**: `SO-APN-ADDRESS-POOL`, `SO-APN-SESSION-CONTEXT`
**constrained_by**: `BR-APN-DUALSTACK-NEED-LICENSE`（若升级双栈需 License）

### 2.3 CS-APN-03 家庭 CPE 宽带方案

| 字段 | 值 |
|------|---|
| `solution_id` | `CS-APN-03` |
| `solution_name` | `家庭 CPE 宽带方案` |
| `solution_summary` | 家庭 CPE 通过 SMF 粒度动态分配双栈地址，透明接入，NAT 直连，IPv4v6 双栈访问家庭宽带业务 |
| `design_intent` | 解决"家庭宽带双栈过渡、按 SMF 粒度负载分担"的宽带场景：同时支持 IPv4 老业务与 IPv6 新业务 |
| `core_mechanism_combo` | `UPF 本地池基于 SMF 分配 → TRANS_NON_AUTH 透明接入 → 双栈(License LKV3G5VDSA01 使能 010105 IPv4v6 取值) → NAT 直连` |
| `status` | `active` |
| `source_evidence_ids` | `EV-TK-01`, `EV-CA-02`, `EV-FK-06`, `EV-FK-16` |

**scopes**: subscription（会话级双栈）、access（SMF 粒度池）

**participants**:
- 家庭 CPE（endpoint，terminal_side）
- UDG/UPF（双栈地址池 + 双池双段 SECTION，user_plane）
- UNC/SMF（PDU 会话控制 + ALLOCPRECEDENCE 决策，control_plane）

**uses_feature**: `GWFD-010105`, `GWFD-020403`, `WSFD-010504`, `WSFD-010501`
**uses_semantic_object**: `SO-APN-ADDRESS-POOL`, `SO-APN-SESSION-CONTEXT`
**constrained_by**: `BR-APN-DUALSTACK-NEED-LICENSE`, `BR-APN-IPV6-CASCADE`

### 2.4 CS-APN-04 VoLTE 语音业务方案

| 字段 | 值 |
|------|---|
| `solution_id` | `CS-APN-04` |
| `solution_name` | `VoLTE 语音业务方案` |
| `solution_summary` | VoLTE UE 通过 SMF 本地动态分配双栈地址，透明接入直连 IMS，双栈支持 VoLTE 语音与视频通话，IMS 精确寻址 |
| `design_intent` | 解决"语音业务低时延、IMS 精确寻址、双栈兼容"的语音场景：IPv4 承载信令、IPv6 承载媒体 |
| `core_mechanism_combo` | `SMF 本地池动态分配 → TRANS_NON_AUTH 透明接入 → 双栈(IMS APN 精确寻址) → 直连` |
| `status` | `active` |
| `source_evidence_ids` | `EV-TK-01`, `EV-CA-02`, `EV-FK-12`, `EV-FK-13` |

**scopes**: subscription（会话级双栈）、access（IMS APN 精确寻址）

**participants**:
- VoLTE UE（endpoint，terminal_side）
- UNC/SMF（SMF 本地池分配 + IMS 寻址，control_plane）
- UDG/UPF（双栈会话执行，user_plane）

**uses_feature**: `WSFD-010502`, `WSFD-010504`, `WSFD-104002`, `GWFD-020403`
**uses_semantic_object**: `SO-APN-ADDRESS-POOL`, `SO-APN-SESSION-CONTEXT`
**constrained_by**: `BR-APN-DUALSTACK-NEED-LICENSE`, `BR-APN-IPV6-CASCADE`

### 2.5 CS-APN-05 企业 AAA 二次鉴权方案

| 字段 | 值 |
|------|---|
| `solution_id` | `CS-APN-05` |
| `solution_name` | `企业 AAA 二次鉴权方案` |
| `solution_summary` | 企业 UE 通过 Radius 分配地址，NON_TRANS 鉴权对接企业 AAA，可选 GRE 隧道接入，IPv4 单栈，支持 DN 二次鉴权访问企业内网 |
| `design_intent` | 解决"企业自管 AAA、Radius 下发地址、二次鉴权访问敏感 DN"的企业专网场景：一次鉴权管接入、二次鉴权管 DN 访问 |
| `core_mechanism_combo` | `Radius 下发地址(Framed-Pool, IGNOREV4/V6POOLID=DISABLE) → NON_TRANS 鉴权 → Radius 级联链(011306→011305→108007) → GRE 隧道(可选) → DN 二次鉴权` |
| `status` | `active` |
| `source_evidence_ids` | `EV-TK-01`, `EV-CA-02`, `EV-FK-24`, `EV-FK-25`, `EV-FK-29`, `EV-FK-27` |

**scopes**: subscriber（企业用户级）、access（GRE/直连接入企业 DN）

**participants**:
- 企业 UE（endpoint，terminal_side）
- UNC/SMF（Radius 鉴权中继 + 地址池名解析，control_plane）
- UDG/UPF（Radius 下发地址执行 + DN-AAA 转接，user_plane）
- 企业 Radius / DN-AAA（external_system）
- IPSec/GRE 网关（access_side，可选）

**uses_feature**: `WSFD-011305`, `WSFD-011306`, `WSFD-108007`, `WSFD-011307`, `IPFD-015002`, `GWFD-010105`
**uses_semantic_object**: `SO-APN-AUTH-AAA`, `SO-APN-ADDRESS-POOL`, `SO-APN-TUNNEL`
**constrained_by**: `BR-APN-RADIUS-CASCADE`, `BR-APN-SECOND-AUTH-PROTO`, `BR-APN-DNAAA-IP-UNIQUE`, `BR-APN-GRE-IPSEC-SRC-EXCL`

### 2.6 CS-APN-06 传统企业 DHCP 迁移方案

| 字段 | 值 |
|------|---|
| `solution_id` | `CS-APN-06` |
| `solution_name` | `传统企业 DHCP 迁移方案` |
| `solution_summary` | 传统企业 UE 通过 DHCP 代理分配 IPv4 地址，透明接入直连，平滑迁移已有 DHCP 地址管理体系 |
| `design_intent` | 解决"沿用企业既有 DHCP 地址管理、不改造终端"的迁移场景：运营商网络透明转发 DHCP 请求 |
| `core_mechanism_combo` | `DHCP 代理(UNC 转发→外部 DHCP Server) → TRANS_NON_AUTH 透明接入 → 直连 → IPv4 单栈` |
| `status` | `active` |
| `source_evidence_ids` | `EV-TK-01`, `EV-CA-02`, `EV-FK-22` |

**scopes**: subscription（会话级 DHCP 租约）、access（直连）

**participants**:
- 企业 UE（endpoint，terminal_side）
- UNC/SMF（DHCP 代理转发，control_plane）
- 外部 DHCP Server（external_system）

> 注：DHCP 完整激活脚本文档缺口（cross-topic §8.4），Stage 3 已标注，Stage 5 审查时不作阻断。

**uses_feature**: `WSFD-104413`, `WSFD-010501`, `GWFD-010101`
**uses_semantic_object**: `SO-APN-ADDRESS-POOL`, `SO-APN-SESSION-CONTEXT`
**constrained_by**: （本方案无强 License/互斥约束，仅受通用会话底座规则约束）

### 2.7 CS-APN-07 企业 L2TP VPN 方案

| 字段 | 值 |
|------|---|
| `solution_id` | `CS-APN-07` |
| `solution_name` | `企业 L2TP VPN 方案` |
| `solution_summary` | 远程办公 UE 通过 L2TP 隧道接入企业总部，LNS 分配双栈地址，NON_TRANS 鉴权对接企业 Radius，UNC 决策 LNS 参数 + UDG 作 LAC 执行封装 |
| `design_intent` | 解决"出差员工远程接入企业内网、二层 PPP 透传企业 AAA"的 L2TP 场景：C 决策 U 执行的典型不对称协同 |
| `core_mechanism_combo` | `UNC 决策 LNS 参数(N4 PFCP 下发) → UDG 作 LAC 执行 PPP/L2TP 封装 → LNS 分配双栈(IPCP/RA+IPv6CP) → NON_TRANS 鉴权 → C-U 不对称 License` |
| `status` | `active` |
| `source_evidence_ids` | `EV-TK-01`, `EV-CA-02`, `EV-FK-11`, `EV-FK-14`, `EV-FK-16` |

**scopes**: subscriber（远程用户级）、access（L2TP 隧道接入企业）

**participants**:
- 远程办公 UE（endpoint，terminal_side）
- UNC/SMF（L2TP 决策 + LNS 参数下发，control_plane）
- UDG/UPF（LAC 执行封装 + PPP 透传，user_plane）
- 企业 LNS（external_system，地址分配 + AAA）

**uses_feature**: `GWFD-020412`, `WSFD-104410`, `WSFD-011305`, `WSFD-011306`, `GWFD-020403`
**uses_semantic_object**: `SO-APN-TUNNEL`, `SO-APN-ADDRESS-POOL`, `SO-APN-AUTH-AAA`
**constrained_by**: `BR-APN-L2TP-CU-ASYM`, `BR-APN-LOC-L2TP-EXCL`, `BR-APN-L2TP-ADDRAUTO-EXCL`, `BR-APN-DUALSTACK-NEED-LICENSE`

### 2.8 CS-APN-08 区域化运营管理方案

| 字段 | 值 |
|------|---|
| `solution_id` | `CS-APN-08` |
| `solution_name` | `区域化运营管理方案` |
| `solution_summary` | 跨区域运营场景下，UE 移动时按位置区匹配地址池组，透明接入直连，IPv4 单栈实现区域差异化运营 |
| `design_intent` | 解决"跨区域用户移动、按位置差异化分配地址与策略"的区域运营场景：基于 LAC/Tac 匹配池组 |
| `core_mechanism_combo` | `UPF 本地池基于位置匹配池组(LAC/Tac→POOLGRPMAP) → TRANS_NON_AUTH 透明接入 → 直连 → IPv4 单栈(License LKV3G5LBAA01)` |
| `status` | `active` |
| `source_evidence_ids` | `EV-TK-01`, `EV-CA-02`, `EV-FK-08` |

**scopes**: location（位置区池组匹配）、subscription（会话级）

**participants**:
- 跨区域 UE（endpoint，terminal_side）
- UDG/UPF（位置感知 + 池组匹配，user_plane）
- UNC/SMF（PFCP 携带 LAC/Tac 透传，control_plane）

**uses_feature**: `GWFD-020421`, `GWFD-010105`, `WSFD-010501`
**uses_semantic_object**: `SO-APN-ADDRESS-POOL`, `SO-APN-SESSION-CONTEXT`
**constrained_by**: `BR-APN-LOC-NEED-LICENSE`, `BR-APN-LOC-L2TP-EXCL`

### 2.9 CS-APN-09 企业双栈加密接入方案

| 字段 | 值 |
|------|---|
| `solution_id` | `CS-APN-09` |
| `solution_name` | `企业双栈加密接入方案` |
| `solution_summary` | 企业 UE 通过 IPSec 隧道加密接入，APN/DNN 粒度动态分配双栈地址，透明接入，IPv4v6 双栈（IPSec IPv6 支持 v02 20.8.0+） |
| `design_intent` | 解决"企业高安全双栈接入、加密隧道同时承载 IPv4/IPv6 业务"的综合场景：双栈叠加 IPSec 加密 |
| `core_mechanism_combo` | `UPF 本地池基于 APN 分配 → TRANS_NON_AUTH 透明接入 → 双栈(License LKV3G5VDSA01) → IPSec 隧道加密(IPSec IPv6 v02 20.8.0+)` |
| `status` | `active` |
| `source_evidence_ids` | `EV-TK-01`, `EV-CA-02`, `EV-FK-06`, `EV-FK-16`, `EV-FK-30` |

**scopes**: access（APN 粒度 + IPSec 接入）、subscription（会话级双栈）

**participants**:
- 企业 UE（endpoint，terminal_side）
- UDG/UPF（双栈地址池 + IPSec 隧道，user_plane）
- UNC/SMF（PDU 会话控制 + IPSec 对称部署，control_plane）
- IPSec 对端网关（access_side）

**uses_feature**: `GWFD-010105`, `GWFD-020403`, `IPFD-015004`, `IPFD-016000`, `WSFD-104002`
**uses_semantic_object**: `SO-APN-ADDRESS-POOL`, `SO-APN-TUNNEL`, `SO-APN-SESSION-CONTEXT`
**constrained_by**: `BR-APN-DUALSTACK-NEED-LICENSE`, `BR-APN-IPV6-CASCADE`, `BR-APN-GRE-IPSEC-SRC-EXCL`

---

## 3. DecisionPoint（12 个）

> **owner_ref 规范**：通用决策点归 `NS-APN-01`；方案特化决策点归对应 `CS-APN-xx`。

| `decision_id` | `owner_layer` | `owner_ref_type` | `owner_ref` | `decision_name` | `decision_question` | `option_set` | `trigger_condition` | `impact_summary` | `status` | `source_evidence_ids` |
|---------------|---------------|-------------------|-------------|-----------------|---------------------|--------------|---------------------|------------------|----------|----------------------|
| `DP-APN-ADDR-MODE` | `business` | `NetworkScenario` | `NS-APN-01` | 地址分配方式决策 | UE IP 地址由谁分配、以何种方式分配 | `["UDM静态签约","UPF-APN/DNN动态","UPF-LOCATION动态","UPF-SMF动态","SMF本地","RADIUS下发","DHCP代理","LNS(L2TP)"]` | PDU 会话建立、需为 UE 分配 IP 时 | 决定 POOLTYPE（LOCAL/UDM/SMF/EXTERNAL）、ALLOCPRECEDENCE、地址池语义对象实例化路径；决定 C-U 决策执行分离模式 | `active` | `EV-CA-02`, `EV-FK-12`, `EV-FK-06` |
| `DP-APN-ADDR-GRANULARITY` | `business` | `NetworkScenario` | `NS-APN-01` | 地址分配粒度决策 | 地址池按什么粒度匹配 | `["APN-1&LOC-0&SMF-0","APN-0&LOC-1&SMF-0","APN-0&LOC-0&SMF-1","APN-1&LOC-1&SMF-0","APN-1&LOC-0&SMF-1","APN-0&LOC-1&SMF-1","APN-1&LOC-1&SMF-1"]` | 选择 UPF 本地分配方式后 | 决定三级优先级规则字符串（SET IPALLOCRULE / SET APNIPALLOCRULE）与 POOLGRPMAP 映射条件 | `active` | `EV-CA-02`, `EV-FK-06`, `EV-FK-08` |
| `DP-APN-ADDR-TYPE` | `business` | `NetworkScenario` | `NS-APN-01` | 地址类型决策 | UE 获得 IPv4 / IPv6 / 双栈 | `["IPv4","IPv6","IPv4v6双栈"]` | 每会话独立决策（per_session=true） | 决定 SECTION 配置（V4STARTIP/V6PREFIXSTART）、License 触发（IPv6→LKV3G5V6PB01；双栈→LKV3G5VDSA01；PD→LKV3G5P6PD01）；实际由 PFCP CHV4/CHV6/V4/V6 BIT 位组合指示 | `active` | `EV-CA-02`, `EV-FK-16`, `EV-FK-17` |
| `DP-APN-AUTH-MODE` | `business` | `NetworkScenario` | `NS-APN-01` | 鉴权方式决策 | UE 接入鉴权采用哪种方式 | `["TRANS_NON_AUTH","TRANS_AUTH","NON_TRANS","LOC_AUTH"]` | PDU 会话/承载/PDP 上下文创建时 | 决定是否调用 AAA（仅 TRANS_AUTH/NON_TRANS 强依赖 Radius）；决定账密来源（UNC 公用配置 vs UE PCO 携带 vs 本地匹配）；LOC_AUTH 不支持 PPP 用户 | `active` | `EV-CA-02`, `EV-FK-24` |
| `DP-APN-ACCESS-MODE` | `business` | `NetworkScenario` | `NS-APN-01` | 接入方式决策 | UE 接入企业/异地 DN 采用哪种隧道 | `["直连","NAT","IPSec","GRE","MPLS-VPN","L2TP","GRE-over-IPSec"]` | 需穿越异种/不可信网络访问目标 DN 时 | 决定隧道封装类型、C-U 协同模式（对称同构 vs C 决策 U 执行）、License 触发（L2TP→LKV3G5L2TP01）；与地址分配方式存在互斥（L2TP↔位置） | `active` | `EV-CA-02`, `EV-FK-29`, `EV-FK-30`, `EV-FK-32`, `EV-FK-11` |
| `DP-APN-UPF-SELECT` | `business` | `NetworkScenario` | `NS-APN-01` | UPF 选择三轮决策 | 会话应锚定到哪个 UPF 实例 | `["按DNN","按S-NSSAI","按DNAI","按位置","按接口能力","按权重","按负载"]` | SMF 建立会话前 | 决定 UPF NF Profile 匹配维度（三轮递进：必选→优选→权重/负载）；选定结果直接决定地址分配执行侧 | `active` | `EV-CA-02`, `EV-FK-34` |
| `DP-APN-PEER-NF-SELECT` | `business` | `NetworkScenario` | `NS-APN-01` | 对等网元 DNS 域名聚合决策 | SGSN/MME 如何按区域聚合对等网元 DNS 域名 | `["按LAI","按RAI","按TAI","按ZONE名称"]` | 2G/3G/4G 附着/RAU/TAU 流程（非 5G） | 决定 AREDNS 配置（DNTYPE + LAC/RAC/TAC RANGE + ZONENAME）；本特性适用 NF 为 SGSN/MME，非 SMF | `active` | `EV-CA-02`, `EV-FK-35` |
| `DP-APN-ACCESS-PERMISSION` | `business` | `NetworkScenario` | `NS-APN-01` | 用户接入权限判定（C 面） | 是否允许 UE 接入网络 | `["允许接入","拒绝(原因值)"]` | UE 附着/PDU 建立、需校验签约 ARD/APN/卡类型/RAT 限制时 | 决定 ARD 记录查询路径（AMF 本地 NGMMSUBDATA vs SGSN/MME GBARD/IUARD/S1ARD）；AMF 本地优先于签约兜底 | `active` | `EV-CA-02`, `EV-FK-36` |
| `DP-APN-BANDWIDTH-CTRL` | `business` | `NetworkScenario` | `NS-APN-01` | U 面带宽流控方式判定 | 用户面上下行带宽采用何种流控 | `["转发","丢弃(CAR)","缓存整形(Shaping)"] × ["上行","下行"]` | 基于协商带宽需在 U 面执行流控时 | 决定 APNQOSATTR 配置（CARSHAPESWUL/DL 开关 + 方式）；与 C 面接入权限机制完全不同，非 C-U 对称 | `active` | `EV-CA-02`, `EV-FK-37` |
| `DP-APN-CONCURRENCY` | `business` | `NetworkScenario` | `NS-APN-01` | 多 PDN/PDU 并发允许判定 | 是否允许该用户建立新的并发会话 | `["允许建立","拒绝(原因值55)"]` | UE 请求新建 PDN/PDU 且已达配额时 | 决定 APNACTNUM 查询（EPC 单 APN ≤11；5GC 单用户 PDU ≤15）；超限 MME/SMF 拒绝 | `active` | `EV-CA-02`, `EV-FK-03` |
| `DP-APN-ALIAS-APN` | `business` | `NetworkScenario` | `NS-APN-01` | 别名 APN 映射决策 | 协商到的 APN 是否需要映射为别名/真实 APN | `["映射后APN(别名/真实)","原APN"]` | SGSN/MME 协商 APN 或 GGSN/PGW-C/SMF 收到别名 APN 时 | 决定 ALIASAPNMAP 双向映射查询；两套网元映射方向相反（SGSN/MME: 协商→别名；GGSN/PGW-C/SMF: 别名→真实） | `active` | `EV-CA-02`, `EV-FK-05` |
| `DP-APN-SECOND-AUTH` | `business` | `NetworkScenario` | `NS-APN-01` | DN 二次鉴权决策 | 是否允许 UE 访问特定企业/园区 DN | `["允许访问DN","拒绝"]` | UE 会话建立后访问特定 DN、DN-AAA 触发时 | 决定经 UPF N4 GTP-U 隧道转接 DN-AAA 的路径；仅 PAP/CHAP via Radius，不支持 EAP/Diameter | `active` | `EV-CA-02`, `EV-FK-27` |

---

## 4. BusinessRule（16 条）

> **rule_type 枚举严格服从 Schema §8.9**：`selection_rule / scope_rule / design_rule / acceptance_rule / diagnosis_rule`。
> **rule_source_kind 枚举**：`principle / config / design / ops / case / restriction`。

| `rule_id` | `rule_name` | `rule_type` | `rule_expression_mode` | `rule_source_kind` | `rule_logic` | `violation_effect` | `status` | `source_evidence_ids` |
|-----------|-------------|-------------|------------------------|--------------------|--------------|---------------------|----------|----------------------|
| `BR-APN-LOC-L2TP-EXCL` | 基于位置与 L2TP 互斥 | `scope_rule` | `explicit` | `restriction` | 基于位置的地址分配（GWFD-020421）与 L2TP VPN（GWFD-020412）不可同时应用；020421 声明互斥，020412 未声明需双向补全 | 两者同时配置会导致地址分配冲突，L2TP 会话建立失败 | `active` | `EV-CA-02`, `EV-FK-08`, `EV-FK-11` |
| `BR-APN-GRE-IPSEC-SRC-EXCL` | GRE 与 IPSec 源地址互斥 | `scope_rule` | `explicit` | `restriction` | GRE 隧道（IPFD-015002）源地址不能与 IPSec 隧道（IPFD-015004）源地址相同 | 隧道封装冲突，报文无法正确转发 | `active` | `EV-CA-02`, `EV-FK-29`, `EV-FK-30` |
| `BR-APN-L2TP-ADDRAUTO-EXCL` | L2TP 与地址自动检测互斥 | `scope_rule` | `explicit` | `restriction` | L2TP VPN（GWFD-020412）与用户面地址自动检测（GWFD-010108）不可同时应用 | 地址检测抢占 L2TP 会话地址，L2TP 隧道异常 | `active` | `EV-CA-02`, `EV-FK-11` |
| `BR-APN-RADIUS-CASCADE` | Radius 级联强依赖链 | `design_rule` | `explicit` | `design` | Radius 功能（WSFD-011306）→ Radius 鉴权接入（WSFD-011305）→ 终端二次鉴权（WSFD-108007，+ 可选 Radius 抄送 WSFD-011307）；前级必须先激活，后级才能生效 | 跳级激活会导致鉴权链断裂，二次鉴权无 Radius 配置承载 | `active` | `EV-CA-02`, `EV-FK-25`, `EV-FK-24`, `EV-FK-27` |
| `BR-APN-LOC-AUTH-NO-PPP` | 本地鉴权不支持 PPP 用户 | `scope_rule` | `explicit` | `restriction` | 本地鉴权接入（ACCESSMODE=LOC_AUTH）不支持 PPP 用户接入 | PPP 用户强制走本地鉴权会鉴权失败 | `active` | `EV-CA-02`, `EV-FK-24` |
| `BR-APN-IPV6-CASCADE` | IPv6 承载强依赖链 | `design_rule` | `explicit` | `design` | IPv6 承载上下文（GWFD-020401，LKV3G5V6PB01）→ IPv4v6 双栈（GWFD-020403，LKV3G5VDSA01）→ IPv6 Prefix Delegation（GWFD-020406，LKV3G5P6PD01，V6PREFIXLENGTH<64 触发）；前缀长度 64 是 PD 分水岭 | IPv6 承载缺失会导致双栈/PD 无法生效；License 串联断裂 | `active` | `EV-CA-02`, `EV-FK-18`, `EV-FK-16`, `EV-FK-20` |
| `BR-APN-DUALSTACK-NEED-LICENSE` | 双栈必须 License | `selection_rule` | `explicit` | `config` | IPv4v6 双栈落地必须 License LKV3G5VDSA01；GWFD-020403 是"能力使能层"，使能 GWFD-010105 的 IPv4v6 取值（能力叠加关系，非父子非包含，使能方向单向 020403→010105） | 缺 License 时双栈配置命令成功但功能不生效，难以排查 | `active` | `EV-CA-02`, `EV-FK-16`, `EV-FK-06` |
| `BR-APN-LOC-NEED-LICENSE` | 基于位置必须 License | `selection_rule` | `explicit` | `config` | 基于位置的地址分配（GWFD-020421）必须 License LKV3G5LBAA01；母特性 GWFD-010105 无 License | 缺 License 时基于位置的池组匹配不生效 | `active` | `EV-CA-02`, `EV-FK-08` |
| `BR-APN-L2TP-CU-ASYM` | L2TP License C-U 不对称 | `scope_rule` | `explicit` | `design` | L2TP VPN License 仅 UDG 侧必须（82200BVC LKV3G5L2TP01）；UNC 侧 WSFD-104410 无 License；C 决策 U 执行模式导致 License 不对称 | 误以为 UNC 侧也需 License 会造成 License 获取错误 | `active` | `EV-CA-02`, `EV-FK-11`, `EV-FK-14` |
| `BR-APN-DNAAA-IP-UNIQUE` | DN-AAA IP 唯一性 | `scope_rule` | `explicit` | `config` | 直连 AAA 与经 UPF 中转 AAA 场景的 Radius Server IP 不可相同 | 两套场景指向同一 AAA IP 会导致鉴权路由混乱 | `active` | `EV-CA-02`, `EV-FK-27` |
| `BR-APN-SECOND-AUTH-PROTO` | 二次鉴权协议限制 | `scope_rule` | `explicit` | `restriction` | 终端二次鉴权（WSFD-108007）仅支持 PAP/CHAP via Radius，不支持 EAP、不支持 Diameter | 误配 EAP/Diameter 会导致二次鉴权无法建立 | `active` | `EV-CA-02`, `EV-FK-27` |
| `BR-APN-CONCURRENCY-11-15` | 并发会话硬上限 | `scope_rule` | `explicit` | `restriction` | EPC 单用户 PDN 连接 ≤ 11；5GC 单用户 PDU 会话 ≤ 15；超限 MME/SMF 拒绝（原因值 55） | 超过硬上限的新会话被拒绝，业务中断 | `active` | `EV-CA-02`, `EV-FK-03` |
| `BR-APN-ALIAS-DOUBLE-COND` | 别名 APN 转换双条件 | `design_rule` | `explicit` | `design` | SGSN/MME 侧别名 APN 转换需双条件同时满足：IMSI 号段匹配 AND 协商 APN 在映射表；缺一不可 | 单条件匹配会误转换，导致 DNS 屏蔽失效 | `active` | `EV-CA-02`, `EV-FK-05` |
| `BR-APN-UPF-VENDOR-LOCK` | SMF 与 UPF 同厂商 | `scope_rule` | `explicit` | `restriction` | SMF 和 UPF 设备必须同时为 HUAWEI（WSFD-107010 硬约束） | 异厂商组网会导致 N4 PFCP 互通异常 | `active` | `EV-CA-02`, `EV-FK-34` |
| `BR-APN-AMF-LOCAL-FIRST` | AMF 本地配置优先于签约 | `selection_rule` | `explicit` | `config` | AMF 本地匹配 > 签约兜底；本地 Null 强制允许；紧急注册跳过接入控制 | 误用签约优先会导致 AMF 本地策略失效 | `active` | `EV-CA-02`, `EV-FK-36` |
| `BR-APN-CARDTYPE-NEED-AUTH` | 卡类型控制依赖鉴权 | `design_rule` | `explicit` | `design` | SGSN/MME 卡类型控制（WSFD-106003 子特性 B）必须先启用 WSFD-010301 鉴权功能；前置依赖 | 未启用鉴权直接配卡类型控制不生效 | `active` | `EV-CA-02`, `EV-FK-36`, `EV-FK-26` |

> **rule_type 说明**：严格服从 Schema §8.9 标准枚举。`selection_rule`=选择规则、`scope_rule`=范围/互斥约束、`design_rule`=设计/强依赖链规则、`acceptance_rule`=验收规则、`diagnosis_rule`=诊断规则。本场景无 `acceptance_rule` / `diagnosis_rule`（验收与诊断规则由 Stage 4 后续层补充）。

---

## 5. SemanticObject（12 个）

| `semantic_object_id` | `semantic_object_name` | `semantic_summary` | `semantic_layer_hint` | `status` | `source_evidence_ids` |
|----------------------|------------------------|--------------------|------------------------|----------|-----------------------|
| `SO-APN-ADDRESS-POOL` | 地址分配语义 | UE IP 地址的分配契约：来源（6 来源）、类型（IPv4/IPv6/双栈）、池组、段范围、生命周期、冲突态；地址类型实际由 PFCP CHV4/CHV6/V4/V6 BIT 位组合指示（非配置参数） | `cross_layer` | `active` | `EV-CA-02`, `EV-FK-06`, `EV-FK-12`, `EV-BS-02` |
| `SO-APN-AUTH-AAA` | 鉴权 AAA 语义 | 用户身份验证契约：三态嵌套（底层 AKA + APN 业务鉴权 + DN 二次鉴权）、协议（AKA/PAP/CHAP）、向量（三元/四元/五元组）、AAA 目标（HLR/HSS/UDM/AAA/DN-AAA） | `cross_layer` | `active` | `EV-CA-02`, `EV-FK-26`, `EV-FK-24`, `EV-FK-27` |
| `SO-APN-TUNNEL` | 隧道语义 | 报文穿越异种/不可信网络的封装契约：类型（GRE/IPSec/MPLS/L2TP）、加密、组播支持、C-U 模式（对称同构 vs C 决策 U 执行）、C-U 对象不对称 | `cross_layer` | `active` | `EV-CA-02`, `EV-FK-29`, `EV-FK-30`, `EV-FK-32`, `EV-FK-11` |
| `SO-APN-QUOTA-LIFECYCLE` | 配额/地址生命周期语义 | 地址池占用、释放、延迟释放、租期续约、强制回收的完整生命周期（5 大增值功能） | `cross_layer` | `active` | `EV-CA-02`, `EV-FK-06` |
| `SO-APN-SESSION-CONTEXT` | PDU/PDN/PDP 会话上下文 | 会话级状态：会话 ID、DNN/APN、QoS Flow/承载、UE IP、F-TEID、SSC Mode；纯描述性根底座，无 MML/License/独立配置对象，由控制面 PFCP/GTP-C 被动触发 | `cross_layer` | `active` | `EV-CA-02`, `EV-FK-01`, `EV-FK-02` |
| `SO-APN-SUBSCRIPTION` | UNC 签约数据本地缓存 | UDM/HSS/HLR 下发的 APN/DNN 签约、QoS、APN-AMBR、PDN Address（静态）、ARD、APN-OI Replacement、Charging Characteristics | `cross_layer` | `active` | `EV-CA-02`, `EV-FK-04` |
| `SO-APN-APNACTNUM` | 单 APN 并发限制配置 | EPC 单 APN 粒度并发上限配置：APNNI、PDNNUM、IPV4ADDRNUM、IPV6ADDRNUM、PDNCONNREJCAUSE | `cross_layer` | `active` | `EV-CA-02`, `EV-FK-03` |
| `SO-APN-ALIAS-APN-MAP` | 别名 APN 映射记录 | 别名 APN ↔ 真实 APN 双向映射表；SGSN/MME 侧（IMSI 前缀 + OLDAPN + NEWAPN）与 GGSN/PGW-C/SMF 侧（SUBRANGE + ALIASAPN + CONVERTAPN + SST/SD）映射方向相反 | `cross_layer` | `active` | `EV-CA-02`, `EV-FK-05` |
| `SO-APN-PNFPROFILE` | UPF NF 实例属性 | UPF NF 实例的多维属性，用于三轮筛选：NFINSTANCENAME、NF TYPE、WEIGHT、PRIORITY、DNN/切片/DNAI/位置/EPS 互通能力 | `cross_layer` | `active` | `EV-CA-02`, `EV-FK-34` |
| `SO-APN-AREDNS` | 位置区域 DNS 域名定制 | LAI/RAI/TAI 聚合到单一 DNS 域名：DNTYPE、LAC/RAC/TAC + RANGE、ZONESW、ZONENAME；适用 NF 为 SGSN/MME（非 SMF） | `cross_layer` | `active` | `EV-CA-02`, `EV-FK-35` |
| `SO-APN-ARD-RECORD` | 接入限制参数记录（C 面） | C 面接入权限判定的配置记录：AMF 侧 NGMMSUBDATA（IMSIPRE/RATRESTRICT/CORERESTRICT）；SGSN/MME 侧 GBARD/IUARD/S1ARD（IMSI/APNNI/CARDTYPE/ARD/CTRLTYPE/CAUSE） | `cross_layer` | `active` | `EV-CA-02`, `EV-FK-36` |
| `SO-APN-APNQOSATTR` | APN QoS 属性（U 面带宽流控） | U 面带宽流控的上下行 CAR/Shaping 开关与方式：CARSHAPESWUL/CARSHAPEUL/CARSHAPESWDL/CARSHAPEDL；与 C 面接入权限机制完全不同，非 C-U 对称 | `cross_layer` | `active` | `EV-CA-02`, `EV-FK-37` |

---

## 6. Scope（子对象，跨方案汇总）

| `scope_name` | `scope_type` | `scope_summary` | 关联方案 |
|--------------|--------------|-----------------|----------|
| 用户级范围 | `subscriber` | 单用户特定业务/静态地址/鉴权策略 | CS-APN-01, CS-APN-05, CS-APN-07 |
| 会话承载范围 | `subscription` | PDU/PDN 会话级地址分配与流控 | CS-APN-02, CS-APN-03, CS-APN-04, CS-APN-06, CS-APN-08, CS-APN-09 |
| APN/DNN 接入范围 | `access` | 按 APN/DNN 粒度匹配地址池或鉴权 | CS-APN-01, CS-APN-02, CS-APN-06, CS-APN-07, CS-APN-09 |
| 位置区域范围 | `location` | 按 LAC/Tac 池组匹配差异化地址分配 | CS-APN-08 |

---

## 7. Participant（子对象，跨方案汇总）

| `participant_name` | `participant_type` | `plane_or_side` | `responsibility_summary` | 关联方案 |
|--------------------|--------------------|-----------------|--------------------------|----------|
| UE / 终端 | `endpoint` | `terminal_side` | 发起附着/PDU 建立、携带 PCO 账密、发起业务访问 | CS-APN-01~09 |
| UNC / SMF / PGW-C | `network_function` | `control_plane` | PDU 会话控制、鉴权决策、地址分配决策、UPF 选择、L2TP 决策、别名 APN 映射 | CS-APN-01~09 |
| UDG / UPF / PGW-U | `network_function` | `user_plane` | 地址池执行、双栈会话执行、隧道终结（IPSec/GRE/L2TP LAC）、DN-AAA 转接、带宽流控 | CS-APN-01~05, CS-APN-07~09 |
| UDM / HSS / HLR | `external_system` | `external` | 静态签约数据、APN-AMBR、QoS profile、ARD 下发 | CS-APN-01, CS-APN-04 |
| Radius / DN-AAA Server | `external_system` | `external` | 业务鉴权、DN 二次鉴权、Radius 下发地址（Framed-Pool） | CS-APN-01, CS-APN-05, CS-APN-07 |
| 外部 DHCP Server | `external_system` | `external` | DHCP/DHCPv6 地址下发 | CS-APN-06 |
| IPSec / GRE / MPLS / LNS 网关 | `access_side` | `access_side` | 隧道对端、LNS 地址分配 + AAA | CS-APN-01, CS-APN-05, CS-APN-07, CS-APN-09 |
| SGSN / MME / AMF | `access_side` | `access_side` | 底层 AKA 鉴权、对等网元选择、别名 APN 映射（协商侧）、接入权限本地判定 | CS-APN-01, CS-APN-04（隐含签约链路） |

---

## 8. 业务图谱关系边（严格 §8.12）

### 8.1 层级包含

| 起点 | 关系 | 终点 |
|------|------|------|
| `BD-APN-01` | `contains` | `NS-APN-01` |
| `NS-APN-01` | `instantiated_as` | `CS-APN-01` ~ `CS-APN-09` |

### 8.2 方案使用特性（uses_feature，共 9 方案 × 主特性集合）

| 起点 | 关系 | 终点 |
|------|------|------|
| `CS-APN-01` | `uses_feature` | `WSFD-010502`, `WSFD-011305`, `WSFD-011306`, `IPFD-015004`, `IPFD-016000`, `WSFD-010301` |
| `CS-APN-02` | `uses_feature` | `GWFD-010105`, `GWFD-010101`, `WSFD-010501` |
| `CS-APN-03` | `uses_feature` | `GWFD-010105`, `GWFD-020403`, `WSFD-010504`, `WSFD-010501` |
| `CS-APN-04` | `uses_feature` | `WSFD-010502`, `WSFD-010504`, `WSFD-104002`, `GWFD-020403` |
| `CS-APN-05` | `uses_feature` | `WSFD-011305`, `WSFD-011306`, `WSFD-108007`, `WSFD-011307`, `IPFD-015002`, `GWFD-010105` |
| `CS-APN-06` | `uses_feature` | `WSFD-104413`, `WSFD-010501`, `GWFD-010101` |
| `CS-APN-07` | `uses_feature` | `GWFD-020412`, `WSFD-104410`, `WSFD-011305`, `WSFD-011306`, `GWFD-020403` |
| `CS-APN-08` | `uses_feature` | `GWFD-020421`, `GWFD-010105`, `WSFD-010501` |
| `CS-APN-09` | `uses_feature` | `GWFD-010105`, `GWFD-020403`, `IPFD-015004`, `IPFD-016000`, `WSFD-104002` |

> **★ Schema §13 合规**：uses_feature 终点全部为 Feature（WSFD-/GWFD-/IPFD- 前缀），无任何 ConfigObject 或 MMLCommand 直接绑定。Feature → ConfigObject/Task 的映射由第 2/3 层承载。

### 8.3 决策点归属（has_decision）

| 起点 | 关系 | 终点 | 说明 |
|------|------|------|------|
| `NS-APN-01` | `has_decision` | `DP-APN-ADDR-MODE`, `DP-APN-ADDR-GRANULARITY`, `DP-APN-ADDR-TYPE`, `DP-APN-AUTH-MODE`, `DP-APN-ACCESS-MODE`, `DP-APN-UPF-SELECT`, `DP-APN-PEER-NF-SELECT`, `DP-APN-ACCESS-PERMISSION`, `DP-APN-BANDWIDTH-CTRL`, `DP-APN-CONCURRENCY`, `DP-APN-ALIAS-APN`, `DP-APN-SECOND-AUTH` | 12 个决策点均为场景级通用决策，归 NS |

> 注：APN 业务域的 12 个决策点均为 4 开通主线维度 + 3 底座支撑维度的场景级稳定选择点，归 NS-APN-01。方案特化在 §8.2 uses_feature 与 §8.4 constrained_by 中体现，不再在 CS 重复挂决策点（避免冗余）。

### 8.4 业务规则约束（constrained_by）

| 起点 | 关系 | 终点 |
|------|------|------|
| `NS-APN-01` | `constrained_by` | `BR-APN-CONCURRENCY-11-15`, `BR-APN-AMF-LOCAL-FIRST`, `BR-APN-ALIAS-DOUBLE-COND`, `BR-APN-UPF-VENDOR-LOCK`（场景级通用约束） |
| `CS-APN-01` | `constrained_by` | `BR-APN-RADIUS-CASCADE`, `BR-APN-GRE-IPSEC-SRC-EXCL`, `BR-APN-SECOND-AUTH-PROTO` |
| `CS-APN-03` | `constrained_by` | `BR-APN-DUALSTACK-NEED-LICENSE`, `BR-APN-IPV6-CASCADE` |
| `CS-APN-04` | `constrained_by` | `BR-APN-DUALSTACK-NEED-LICENSE`, `BR-APN-IPV6-CASCADE` |
| `CS-APN-05` | `constrained_by` | `BR-APN-RADIUS-CASCADE`, `BR-APN-SECOND-AUTH-PROTO`, `BR-APN-DNAAA-IP-UNIQUE`, `BR-APN-GRE-IPSEC-SRC-EXCL` |
| `CS-APN-07` | `constrained_by` | `BR-APN-L2TP-CU-ASYM`, `BR-APN-LOC-L2TP-EXCL`, `BR-APN-L2TP-ADDRAUTO-EXCL`, `BR-APN-DUALSTACK-NEED-LICENSE`, `BR-APN-LOC-AUTH-NO-PPP` |
| `CS-APN-08` | `constrained_by` | `BR-APN-LOC-NEED-LICENSE`, `BR-APN-LOC-L2TP-EXCL` |
| `CS-APN-09` | `constrained_by` | `BR-APN-DUALSTACK-NEED-LICENSE`, `BR-APN-IPV6-CASCADE`, `BR-APN-GRE-IPSEC-SRC-EXCL` |
| `CS-APN-02`, `CS-APN-06` | `constrained_by` | `BR-APN-DUALSTACK-NEED-LICENSE`（若升级双栈时触发） |

### 8.5 语义对象使用（uses_semantic_object）

| 起点 | 关系 | 终点 |
|------|------|------|
| `NS-APN-01` | `uses_semantic_object` | `SO-APN-SESSION-CONTEXT`, `SO-APN-SUBSCRIPTION`, `SO-APN-APNACTNUM`, `SO-APN-ALIAS-APN-MAP`, `SO-APN-PNFPROFILE`, `SO-APN-AREDNS`, `SO-APN-ARD-RECORD`, `SO-APN-APNQOSATTR`（底座支撑语义对象归 NS） |
| `CS-APN-01` | `uses_semantic_object` | `SO-APN-ADDRESS-POOL`, `SO-APN-AUTH-AAA`, `SO-APN-TUNNEL`, `SO-APN-SUBSCRIPTION` |
| `CS-APN-02` | `uses_semantic_object` | `SO-APN-ADDRESS-POOL`, `SO-APN-SESSION-CONTEXT` |
| `CS-APN-03` | `uses_semantic_object` | `SO-APN-ADDRESS-POOL`, `SO-APN-SESSION-CONTEXT` |
| `CS-APN-04` | `uses_semantic_object` | `SO-APN-ADDRESS-POOL`, `SO-APN-SESSION-CONTEXT` |
| `CS-APN-05` | `uses_semantic_object` | `SO-APN-AUTH-AAA`, `SO-APN-ADDRESS-POOL`, `SO-APN-TUNNEL` |
| `CS-APN-06` | `uses_semantic_object` | `SO-APN-ADDRESS-POOL`, `SO-APN-SESSION-CONTEXT` |
| `CS-APN-07` | `uses_semantic_object` | `SO-APN-TUNNEL`, `SO-APN-ADDRESS-POOL`, `SO-APN-AUTH-AAA` |
| `CS-APN-08` | `uses_semantic_object` | `SO-APN-ADDRESS-POOL`, `SO-APN-SESSION-CONTEXT` |
| `CS-APN-09` | `uses_semantic_object` | `SO-APN-ADDRESS-POOL`, `SO-APN-TUNNEL`, `SO-APN-SESSION-CONTEXT` |
| `CS-APN-01` ~ `CS-APN-09`（涉及地址分配） | `uses_semantic_object` | `SO-APN-QUOTA-LIFECYCLE`（地址生命周期语义跨所有地址分配方案） |

### 8.6 证据支撑（supported_by）

| 起点 | 关系 | 终点 |
|------|------|------|
| `BD-APN-01` | `supported_by` | `EV-BS-01`, `EV-BS-02`, `EV-CA-02` |
| `NS-APN-01` | `supported_by` | `EV-BS-01`, `EV-BS-02`, `EV-CA-02`, `EV-TK-01`（Batch-14 业务场景方案，覆盖 9 场景） |
| `CS-APN-01` ~ `CS-APN-09` | `supported_by` | `EV-TK-01`（9 场景共用 Batch-14 方案归纳）+ 方案特性级 `EV-FK-*` |

---

## 9. 端到端方案链路（跨层映射依据）

### 9.1 CS-APN-01 工厂工控端到端
```
UE 附着 → 底层 AKA 鉴权(WSFD-010301, SGSN/MME/AMF ↔ HLR/HSS/UDM)
→ PDU 建立 → UDM 静态签约读取(WSFD-010502, Framed-IP)
→ NON_TRANS 鉴权(WSFD-011305, UE 透传账密 → UNC → 企业 Radius)
→ IPSec 隧道封装(IPFD-015004, UDG 对称部署)
→ IPv4 单栈访问工控内网
```

### 9.2 CS-APN-05 企业 AAA 二次鉴权端到端
```
UE 附着 → PDU 建立 → NON_TRANS 鉴权(一次, WSFD-011305, 接入侧 AAA)
→ Radius 下发地址(WSFD-011306, Framed-Pool, IGNOREV4POOLID=DISABLE)
→ 会话建立 → 访问企业 DN
→ DN 二次鉴权(WSFD-108007, SMF ↔ UPF ↔ DN-AAA 经 N4 GTP-U 隧道转接)
→ 允许访问 DN（或拒绝）
（可选 Radius 抄送 WSFD-011307 并行给 WAP GW 等第三方）
```

### 9.3 CS-APN-07 企业 L2TP VPN 端到端（C 决策 U 执行典型）
```
远程 UE 附着 → PDU 建立 → NON_TRANS 鉴权(WSFD-011305)
→ UNC/SMF 决策 LNS 参数(WSFD-104410, 经 N4 PFCP 下发 APNL2TPCTRL 2 参数)
→ UDG 作 LAC 执行封装(GWFD-020412, APNL2TPATTR 10+ 参数, PPP/L2TP)
→ LNS 分配双栈地址(IPCP IPv4 + RA+IPv6CP IPv6, 双栈需 License LKV3G5L2TP01)
→ UE 经 L2TP 隧道接入企业总部
```

### 9.4 CS-APN-09 企业双栈加密端到端
```
UE 附着 → PDU 建立 → UPF 基于 APN 分配双栈地址(GWFD-010105 + GWFD-020403 使能)
→ IPv4 段 + IPv6 段双 SECTION → 双栈地址下发
→ TRANS_NON_AUTH 透明接入
→ IPSec 隧道加密(IPFD-015004, IPv6 支持 v02 20.8.0+)
→ UE 双栈加密接入企业
```

---

## 10. 与计费/带宽控制场景业务图谱的对比

| 维度 | 计费场景 | 带宽控制场景 | APN 业务域（本文件） |
|------|---------|------------|---------------------|
| BusinessDomain | `业务感知`（BD-CH-01） | `业务感知`（BD-BW-01） | `接入与会话管理`（**BD-APN-01，独立**） |
| NetworkScenario | `NS-CH-01 计费场景` | `NS-BW-01 带宽控制场景` | `NS-APN-01 APN 开通场景` |
| ConfigurationSolution | 7（按计费方式/计量/兜底） | 7（按控制机制） | **9（按业务场景 4 维度组合）** |
| 核心机制 | SA→Rule→PCC/URR→上报→配额 | SA→BWM→CAR/Shaping/FUP/GBR | 4 维度决策（地址×鉴权×接入×类型）+ 3 底座（会话×网元×权限） |
| 独有对象族 | 计费三件套 + SMF 融合计费 | BWM 四级体系 | 地址池/鉴权 AAA/隧道/会话上下文/签约/别名 APN/ARD |
| DecisionPoint | 8 | 8 | **12** |
| BusinessRule | 16 | 6 | **16** |
| SemanticObject | 12（含协议栈 2） | 8（无协议栈） | **12（无协议栈，含底座签约/网元类）** |
| 独立性 | 共享"业务感知"根 | 共享"业务感知"根 | **独立根，与业务感知并列** |

> APN 与业务感知两域通过 PDU 会话上下文（SO-APN-SESSION-CONTEXT）协同：APN 域负责"建会话、分地址、管接入"，业务感知域负责"会话内流量做策略/计费"。两者根对象不重叠。

---

## 11. 对象计数汇总

| 对象类型 | 数量 | 编号范围 |
|---------|------|---------|
| BusinessDomain | 1 | BD-APN-01 |
| NetworkScenario | 1 | NS-APN-01 |
| ConfigurationSolution | 9 | CS-APN-01 ~ CS-APN-09 |
| DecisionPoint | 12 | DP-APN-ADDR-MODE / ADDR-GRANULARITY / ADDR-TYPE / AUTH-MODE / ACCESS-MODE / UPF-SELECT / PEER-NF-SELECT / ACCESS-PERMISSION / BANDWIDTH-CTRL / CONCURRENCY / ALIAS-APN / SECOND-AUTH |
| BusinessRule | 16 | BR-APN-LOC-L2TP-EXCL / GRE-IPSEC-SRC-EXCL / L2TP-ADDRAUTO-EXCL / RADIUS-CASCADE / LOC-AUTH-NO-PPP / IPV6-CASCADE / DUALSTACK-NEED-LICENSE / LOC-NEED-LICENSE / L2TP-CU-ASYM / DNAAA-IP-UNIQUE / SECOND-AUTH-PROTO / CONCURRENCY-11-15 / ALIAS-DOUBLE-COND / UPF-VENDOR-LOCK / AMF-LOCAL-FIRST / CARDTYPE-NEED-AUTH |
| SemanticObject | 12 | SO-APN-ADDRESS-POOL / AUTH-AAA / TUNNEL / QUOTA-LIFECYCLE / SESSION-CONTEXT / SUBSCRIPTION / APNACTNUM / ALIAS-APN-MAP / PNFPROFILE / AREDNS / ARD-RECORD / APNQOSATTR |
| Scope（子对象） | 4 | subscriber / subscription / access / location |
| Participant（子对象） | 7 | UE / UNC-SMF / UDG-UPF / UDM-HSS / Radius-DNAAA / DHCP / 隧道网关 / SGSN-MME-AMF（合并表述） |
| **业务层对象总计** | **51** | BD 1 + NS 1 + CS 9 + DP 12 + BR 16 + SO 12 |

---

> 本文件为 APN 业务域三层图谱第 1 层。第 2 层特性图谱、第 3 层任务原子层、第 4 层命令图谱、第 5 层跨层映射、第 6 层证据索引见同目录其他文件。
>
> **Stage 5 审查重点预告**：
> 1. 每对象 source_evidence_ids 是否指向真实证据（§0.3 映射表）
> 2. uses_feature 终点是否全部为 Feature（§13 合规，已在 §8.2 验证）
> 3. DP 字段完整性（decision_id / owner_layer / owner_ref_type / owner_ref / decision_question / option_set / impact_summary / source_evidence_ids）
> 4. BR 字段完整性（rule_id / rule_type / rule_expression_mode / rule_source_kind / rule_logic / source_evidence_ids）
> 5. status 是否全部为 active
> 6. APN 独立 BD 定位是否清晰（§1.1 + §10 对比表）
