# APN 业务域 — 跨主题综合分析（Stage 3）

> **定位**：Stage 3 横向综合分析层。基于 topic-knowledge 4 文件（Batch-14 业务场景方案、归纳-四维度决策与机制、归纳-APN 底座三维度、归纳-配置树修正与 Stage 3 待解决项）+ feature-knowledge 37 特性的横向抽取，整合定稿三层图谱**第 1 层**对象（ConfigurationSolution / DecisionPoint / SemanticObject / BusinessRule）。
> **数据源**：仅基于 topic-knowledge 与 feature-knowledge，不再回读产品文档。
> **来源标注规范**：每条结论后括注 `[GWFD-xxxxx]` / `[WSFD-xxxxx]` / `[IPFD-xxxxx]`；多特性共同支撑用 `+` 连接；跨归纳用 `[归纳-四维度 §N]` / `[归纳-底座 §N]` / `[修正 §N]` / `[Batch-14 §N]`。
> **Evidence 占位**：本文件统一使用占位 `EV-CA-02`（Stage 4 实例化时映射到 `EV-TK-*` / `EV-FK-*`）。

---

## 0. 元数据

| 字段 | 取值 |
|------|------|
| doc_id | CA-APN-02 |
| doc_name | APN 业务域跨主题综合分析 |
| stage | 3（横向综合分析） |
| source_topic_count | 4 个 topic-knowledge 文件 |
| source_feature_count | 37 个 feature-knowledge 特性（地址分配 18 + 鉴权 5 + 接入方式 5 + 会话/网元/接入控制/别名 9） |
| source_evidence_ids | EV-CA-02 |
| downstream_consumers | Stage 4 第 1 层对象实例化（CS / DP / SO / BR） |
| 第 1 层对象定稿 | ConfigurationSolution 9 个 / DecisionPoint 12 个 / SemanticObject 12 个 / BusinessRule 16 个 |

---

## 1. 概述

### 1.1 场景定位

APN（接入点名称 / Access Point Name）业务域是业务感知体系的**基础接入与会话管理场景**，覆盖 UE 从附着到 PDU 会话建立的完整链路：用户身份验证 → 接入权限判定 → 地址分配 → 网元选择 → 隧道接入 → 会话治理。

本场景核心目标：**将不同业务诉求（工控内网、IoT 上报、宽带、VoLTE、企业 AAA、DHCP 迁移、远程办公、区域运营、双栈加密）映射到 APN 4 维度决策（地址分配 × 鉴权 × 接入方式 × 地址类型）与 3 类底座支撑（会话管理 / 网元选择 / 接入控制）的组合方案**。

### 1.2 文档范围

| 维度 | 覆盖内容 |
|------|----------|
| 产品 | UDG（用户面 UPF/PGW-U）、UNC（控制面 SMF/PGW-C/AMF/SGSN/MME） |
| 特性 | 37 个特性（UDG 17 + UNC 18 + IPFD 2，含 C-U 对称对） |
| 决策维度 | 4 开通主线维度 + 3 底座支撑维度（共 7 维度） |
| 业务方案 | 9 个 ConfigurationSolution（工厂工控、IoT 上报、家庭宽带、VoLTE、企业 AAA、DHCP、L2TP、区域化、企业双栈） |
| topic-knowledge | 4 文件（Batch-14 业务场景 + 四维度归纳 + 底座三维度 + 配置树修正） |

### 1.3 分析方法论

本文档采用**横向综合 + 纵向收敛**双层方法：
- **横向**：将 4 个 topic-knowledge 的候选清单交叉验证（四维度归纳 §5 提出 6 DP + 4 SO + 11 FR 候选；底座三维度 §4 补充 6 DP + 8 SO + 16 FR 候选）
- **纵向**：Batch-14 的 9 场景方案验证 DecisionPoint 取值空间的完整性；修正清单的 11 处修正 + 12 个 Stage 3 待解决问题逐个验证

---

## 2. 主题分类与知识地图

### 2.1 APN 知识地图（7 维度全息视图）

APN 业务域所有特性可归为 **2 大集群 7 维度**：

| 集群 | 维度 | 核心职责 | 主特性 | 产出形态 |
|------|------|---------|--------|---------|
| **开通主线集群**（决策产生层） | 地址分配 | UE IP 由谁分配、以何种方式分配 | GWFD-010104/010105/020421 + WSFD-010502/010504 | DecisionPoint + SemanticObject |
| | 鉴权 | UE 接入鉴权方式与 AAA 对接 | WSFD-010301 + WSFD-011305/011306/011307/108007 | DecisionPoint + FeatureRule |
| | 接入方式 | UE 接入企业 DN/异地网络的隧道方案 | IPFD-015002/015004/016000 + GWFD-020411/020412 + WSFD-104410/104411 | DecisionPoint + SemanticObject |
| | 地址类型 | UE 获得 IPv4 / IPv6 / 双栈 | GWFD-020401/020403/020406 + WSFD-104001/104002/104004/104005 | DecisionPoint |
| **底座支撑集群**（基础支撑层） | 会话管理 | 宿主流程 + 签约数据 + 并发治理 + APN 映射 | GWFD-010101/WSFD-010501 + WSFD-010503/010400/106203 | SemanticObject + FeatureRule |
| | 网元选择 | 网元实例决策（UPF / 对等控制面网元） | WSFD-107010 + WSFD-010202 | DecisionPoint |
| | 接入控制 | 接入权限 + 用户面带宽流控 | WSFD-106003 + GWFD-010151 | DecisionPoint + FeatureRule |

### 2.2 维度间正交关系矩阵

4 开通主线维度之间存在明确的正交决策关系：

```
地址类型 (IPv4 / IPv6 / IPv4v6)
        │ 决定池配置（IPVERSION + V4STARTIP / V6PREFIXSTART）
        ▼
地址分配 (UDM / UPF-APN / UPF-LOCATION / UPF-SMF / SMF / RADIUS / DHCP / LNS)
        │ 决定 POOLTYPE（LOCAL / UDM / SMF / EXTERNAL）+ ALLOCPRECEDENCE
        ▼
鉴权 (TRANS_NON_AUTH / TRANS_AUTH / NON_TRANS / LOC_AUTH)
        │ 决定是否调用 AAA（仅 NON_TRANS / TRANS_AUTH 强依赖 Radius）
        ▼
接入方式 (直连 / NAT / IPSec / GRE / MPLS / L2TP / GRE-over-IPSec)
        │ 决定隧道封装（对称同构 vs C 决策 U 执行）
```

> **关键结论**：4 维度理论上完全正交，但实际受 License / 互斥 / 协议限制约束（详见 §5）。例如 L2TP 接入方式与基于位置的地址分配**双向互斥**；双栈地址类型必须叠加 License LKV3G5VDSA01。

### 2.3 UDG vs UNC 视角分工

| 对比维度 | UDG（UPF / PGW-U） | UNC（SMF / PGW-C / SGSN / MME / AMF） |
|----------|---------------------|----------------------------------------|
| 网元角色 | 用户面执行体 | 控制面决策体（决策"何时建/改/放 + 在哪里建"） |
| 地址分配 | 执行 4 子方式（基于 APN / 位置 / SMF / Radius 下发池名）[GWFD-010105] | 决策 4 来源（UDM / Radius / SMF 本地 / DHCP）[WSFD-010502] |
| 鉴权 | 不涉及 APN 业务鉴权（仅底层 AKA 网络接入层） | 决策 ACCESSMODE 4 方式；承载 Radius 功能 [WSFD-011305] |
| 接入方式 | 隧道执行（L2TP 作 LAC；GRE/IPSec/MPLS 同构部署） | L2TP 决策下发 LNS 参数；其他隧道 C 面对称部署 |
| 接入控制 | 带宽流控（CAR/Shaping，基于协商带宽）[GWFD-010151] | 接入权限控制（签约 ARD/APN/卡类型/RAT 限制）[WSFD-106003] |
| 网元选择 | UPF 选择是被选择对象 | SMF 决策 UPF 选择 [WSFD-107010]；SGSN/MME 决策对等网元 [WSFD-010202] |

---

## 3. 共性机制分析

### 3.1 四大 SemanticObject 跨维度共性

APN 业务域的 7 维度特性最终收敛到 **4 大核心语义对象**，每个语义对象跨多个维度共享基础设施：

| SemanticObject | 跨维度共享 | 主承载特性 | 关键属性 |
|----------------|-----------|-----------|---------|
| **SO-ADDRESS-POOL**（地址池语义） | 地址分配 + 地址类型 | GWFD-010105 + GWFD-010104（UDG） / WSFD-010502 + WSFD-010504（UNC） | source(6来源), type(IPv4/IPv6/双栈), pool_group, section_range, lifetime, conflict_state |
| **SO-AUTH-AAA**（鉴权 AAA 语义） | 鉴权 + 接入控制（C 面权限） | WSFD-010301（底层）+ WSFD-011305（业务）+ WSFD-108007（二次） | layer(接入/业务/DN), protocol(AKA/PAP/CHAP), vector(三元/四元/五元组), aaa_target(HLR/HSS/UDM/AAA/DN-AAA) |
| **SO-TUNNEL**（隧道语义） | 接入方式 | IPFD-015002/015004/016000 + GWFD-020411/020412 | type(GRE/IPSec/MPLS/L2TP), encryption(bool), multicast_support(bool), c_u_mode(对称/C决策U执行) |
| **SO-SESSION-CONTEXT**（会话上下文语义） | 会话管理 + 网元选择 + 地址分配 | GWFD-010101 + WSFD-010501 + WSFD-010400 + WSFD-010503 + WSFD-106203 | session_id, dnn/apn, qos_flow/bearer, ue_ip, f_teid, ssc_mode, subscription_data |

### 3.2 地址池基础设施（跨 6 来源统一）

**核心结论**[归纳-四维度 §1.2]：UDG 本地地址分配 4 种子方式（基于 APN / 位置 / SMF / Radius 下发池名）共享同一套基础设施，UNC 侧 4 种决策源（UDM / Radius / SMF 本地 / DHCP）通过 PFCP 信元解耦。

```
SECTION → POOL(LOCAL/UDM/SMF/EXTERNAL) → POOLGROUP → POOLGRPMAP(映射条件) → 规则匹配 → 分配
                                              ↑
                 全局规则 SET IPALLOCRULE / APN 级规则 SET APNIPALLOCRULE
                 三级优先级规则字符串：APN-{0|1}&LOCATION-{0|1}&SMF-{0|1}
```

**5 项跨子方式共性增值机制**[GWFD-010105]：
1. 地址池优先级（仅同类池间比较，段无优先级）
2. 地址延迟释放（避免敏感网元异常）
3. 地址租期续约（用户重接入复用原 IP）
4. 地址强制回收（需先锁定，强收回收会让在线用户下线）
5. 防止地址冲突（CONFLICTIP 标识）

**地址类型指示真值表**（跨产品跨特性收敛）[GWFD-010104][GWFD-010105]：
- CHV4/CHV6=1 & V4/V6=0 → **用户面分配**（UDG 本地）
- V4/V6=1 & CHV4/CHV6=0 → **外部分配**（SMF / Radius / UDM 下发）
- 软参 BIT391=0 标准 / BIT391=1 华为私有（Spare 扩展）

> **EV-CA-02**：地址类型不是配置参数（修正清单 1.4），实际由 PFCP `UE IP Address` 信元的 CHV4/CHV6/V4/V6 BIT 位组合决定；SemanticObject `SO-ADDRESS-POOL.type` 属性来源必须标 `PFCP BIT (CHV4/CHV6/V4/V6)`。

### 3.3 鉴权 AAA 三态体系（底层 + 业务 + 二次）

APN 业务域鉴权维度是**三态嵌套体系**，远比单层"是否鉴权"复杂[归纳-四维度 §2.2][归纳-底座 §3]：

| 鉴权层 | 鉴权对象 | 鉴权协议 | 鉴权网元 | 鉴权时机 | 触发特性 |
|--------|---------|---------|---------|---------|---------|
| **底层 AKA**（网络接入层） | SIM/USIM 卡身份（IMSI/SUPI/SUCI） | AKA 系列（GSM/UMTS/EPS/5G AKA、EAP-AKA'） | UE ↔ SGSN/MME/AMF ↔ HLR/HSS/UDM(ARPF)/AUSF | 移动性管理流程（注册/附着/RAU/TAU） | WSFD-010301 |
| **APN 业务鉴权**（应用层） | 用户名密码 | PAP/CHAP via Radius 或本地匹配 | UE/UNC ↔ AAA Server 或 UNC 本地 | PDU 会话/承载/PDP 上下文创建时 | WSFD-011305（+ WSFD-011306 承载） |
| **DN 二次鉴权**（企业 DN 层） | UE 访问企业/园区 DN 的授权 | PAP/CHAP via Radius（不支持 EAP/Diameter） | SMF ↔ UPF ↔ DN-AAA（必须经 UPF 转接） | 会话建立后访问特定企业 DN 时 | WSFD-108007 |

**执行时序**：底层 AKA 先发生（UE 通过接入鉴权进入网络），APN 业务鉴权后发生（创建 PDU 会话时按 ACCESSMODE 触发），DN 二次鉴权最后发生（访问特定企业 DN 时）。三层隐式协同，无直接信令耦合。

**5 特性级联强依赖链**[WSFD-108007 §2.2]：
```
[WSFD-011306 Radius 功能]（协议承载：PAP/CHAP、服务器组、Bypass）
        │ 必须先激活
        ▼
[WSFD-011305 Radius 鉴权接入]（AUTHMODE 决策：TRANS_AUTH/NON_TRANS/LOC_AUTH 触发）
        │ 必须先激活
        ▼
[WSFD-108007 终端二次鉴权]（DN-AAA 经 UPF N4 GTP-U 隧道转接，License 82200DSF LKV2SECAA01）
        │ 二次鉴权对象：UE 访问企业/园区 DN 的授权
        ▼
[WSFD-011307 Radius 抄送]（鉴权/计费消息并行抄送给 WAP GW 等第三方）
```

### 3.4 隧道四模式共性 + 二分

接入方式类 4 隧道（GRE / IPSec / MPLS / L2TP）按 C-U 协同模式清晰二分[归纳-四维度 §3.2][修正 §2]：

**模式 A：对称同构型**（GRE / IPSec / MPLS VPN）
- UDG 与 UNC 两产品**均部署同名特性**，两侧配置对象与命令基本对称
- License 对称（GRE/IPSec 两侧均无；MPLS 两侧均需）
- 适用场景：两侧各建隧道，用于 U 面或 C 面穿越异种/不可信网络

**模式 B：C 决策 U 执行型**（L2TP VPN）
- UNC 侧 WSFD-104410 **决策** LNS 参数并经 N4 PFCP 下发；UDG 侧 GWFD-020412 作 LAC **执行**封装与 PPP 透传
- License **C-U 不对称**（UDG 必须 License 82200BVC LKV3G5L2TP01；UNC 无 License）
- 配置对象不对称（U: `APNL2TPATTR` 10+ 参数；C: `APNL2TPCTRL` 仅 2 参数）

**四隧道对比速查**：

| 维度 | GRE [IPFD-015002] | IPSec [IPFD-015004/016000] | MPLS VPN [GWFD-020411/WSFD-104411] | L2TP VPN [GWFD-020412/WSFD-104410] |
|------|------|------|------|------|
| 隧道层次 | 三层 | 三层 | 三层（L3VPN） | **二层**（PPP） |
| 加密能力 | ❌ | ✅ | ❌ | ❌ |
| 组播/广播 | ✅ | ❌ | ✅ | ✅ |
| License | 无 | 无 | 必须 | C-U 不对称 |
| C-U 模式 | 对称同构 | 对称同构 | 对称同构 | C 决策 U 执行 |
| 关键约束 | 源地址与 IPSec 互斥 | DH 组不能 None | 标签规格 299008 | 与 010108/020482/020421 互斥 |

### 3.5 会话上下文纯描述性根底座

**关键发现**[归纳-底座 §1.1]：GWFD-010101 + WSFD-010501 是 APN 域的**纯描述性根底座** —— 无 MML、无 License、无独立配置对象，PDU/PDN/PDP 会话由控制面 PFCP/GTP-C 信令被动触发。所有上层特性的宿主流程都基于此底座。

**C-U 协同分工**（强语义耦合但文档明示"不涉及交互"）[GWFD-010101][WSFD-010501]：
- UNC（C 面）决策"何时建/改/放 + 在哪里建"，通过 PFCP Session Establishment/Modification/Deletion 下发 PDR/FAR/URR/QER
- UDG（U 面）按 C 面指示安装规则、分配 F-TEID、执行报文检测/转发/QoS/上报
- 接口：N4（5G）/ Sxa/Sxb（4G CUPS）/ Gn/Gp（2-3G）

---

## 4. 配置差异对比

### 4.1 地址分配 6 来源 × 3 类型 正交矩阵

**核心结论**[归纳-四维度 §1.1]：6 种来源 × 3 种类型理论上 18 格全可填，但实际组合受特性 License 与互斥约束限制。

| 地址类型 ↓ / 分配来源 → | UPF/PGW-U 本地池 | SMF/PGW-C 本地池 | UDM 静态签约 | Radius 下发 | DHCP / DHCPv6 代理 | LNS（PPP） |
|---|---|---|---|---|---|---|
| **IPv4** | ✅ POOLTYPE=LOCAL [GWFD-010105] | ✅ [WSFD-010502][WSFD-010504] | ✅ Framed-IP [WSFD-010502] | ✅ Framed-Pool [GWFD-010105 子方式4][WSFD-011306] | ✅ DHCP 代理 [WSFD-104413] | ✅ IPCP [GWFD-020412] |
| **IPv6** | ✅ IPv6 SECTION [GWFD-010105][GWFD-020401] | ✅ [WSFD-010502] | ✅ Framed-IPv6-Pool | ✅ [WSFD-011306] | ✅ DHCPv6 代理 [WSFD-104005] | ✅ RA+IPv6CP [GWFD-020412] |
| **IPv4v6 双栈** | ✅ 双池双段 + License LKV3G5VDSA01 [GWFD-020403] | ✅ [WSFD-104002] | ✅ UDM 纠正 PDP Type=IPv4→IPv4v6 [WSFD-104002] | ✅ | ✅ DHCP+DHCPv6 双代理 | ✅ L2TP v02+ [GWFD-020412] |

### 4.2 鉴权 4 方式 × Radius 依赖矩阵

**核心结论**[归纳-四维度 §2.1]：4 种 ACCESSMODE 中，仅 TRANS_AUTH / NON_TRANS 强依赖 Radius 功能。

| ACCESSMODE | 中文 | 是否鉴权 | Radius 功能依赖 | AAA Server | 账密来源 | PPP 用户 |
|---|---|---|---|---|---|---|
| **TRANS_NON_AUTH** | 透明接入 | 否 | **否** | 否 | 不适用 | ✅ |
| **TRANS_AUTH** | 透明鉴权（匿名） | 是（UNC 代发） | **必须** | **必须** | UNC 公用配置 | ✅ |
| **NON_TRANS** | 非透明接入 | 是（UE 透传） | **必须** | **必须** | UE PCO 携带 | ✅ |
| **LOC_AUTH** | 本地鉴权 | 是（本地匹配） | **否** | 否 | UE PCO + UNC 本地 | **❌ 不支持** |

### 4.3 地址类型 3 子方式差异

**核心结论**[归纳-四维度 §4.1]：IPv4 / IPv6 / 双栈的池配置参数完全不同，且双栈是"能力使能层"叠加在"分配机制层"之上。

| 维度 | IPv4 单栈 | IPv6 单栈 | IPv4v6 双栈 |
|------|----------|----------|-------------|
| 池配置 | `IPVERSION=IPV4` + `V4STARTIP/V4ENDIP` | `IPVERSION=IPV6` + `V6PREFIXSTART/V6PREFIXEND` + `V6PREFIXLENGTH` | 双池双段（IPv4+IPv6 两种 SECTION 并存） |
| License | 无 | **必须** LKV3G5V6PB01 [GWFD-020401] | **必须** LKV3G5VDSA01 [GWFD-020403]（使能 010105 IPv4v6 取值） |
| 前缀长度阈值 | 不适用 | =64（普通 IPv6 池） | <64（49~63）切换为 IPv6 Prefix Delegation 模式 [GWFD-020406] |
| PD 模式 | 不适用 | 不适用 | **必须** LKV3G5P6PD01（V6PREFIXLENGTH<64 触发） |
| RA 通告 | 无 | UDG 主动下发 | **GWFD-020403 独有主动下发**（010105 未涉及） |

**双栈分层关系**[GWFD-020403 §7.2]：

| 层 | 特性 | 职责 | License |
|---|---|---|---|
| **Layer A：能力使能层** | GWFD-020403 IPv4v6双栈接入 | 控制是否允许创建 IPv4v6 上下文；RA 通告机制；双栈对称配置形态 | **必须** LKV3G5VDSA01 |
| **Layer B：分配机制层** | GWFD-010105 用户面地址分配 | 4 种子方式、三级优先级规则、PFCP 类型协商（CHV4=1&CHV6=1）、本地池体系 | **无** |

> **EV-CA-02**：GWFD-020403 是 GWFD-010105 的"双栈特化版本"，**非父子关系、非包含关系**，是"能力叠加"关系（修正清单 1.1）。图谱 Feature 变体维度需建模 `能力层级=使能层/机制层`。

### 4.4 C-U 关系模式 4 分类

**核心结论**[修正 §2]：APN 业务域 37 个特性按 C-U 协同模式可清晰归类为 **4 种模式**。

| 模式 | 适用特性对 | C-U 协同特征 | License 对称性 |
|------|-----------|-------------|---------------|
| **A. 对称同构型** | GRE / IPSec / MPLS VPN / 静态冗余（GWFD-010107 + WSFD-107021） | 两侧部署同名特性，配置对象与命令基本对称 | 对称 |
| **B. C 决策 U 执行型** | L2TP VPN（WSFD-104410 决策 + GWFD-020412 执行） | UNC 决策 LNS 参数经 N4 PFCP 下发；UDG 作 LAC 执行封装 | **不对称**（UDG 必须，UNC 无） |
| **C. 决策执行分离型** | 地址分配 / 控制面分配 / IPv6 承载 / IPv6 PD / 会话管理 | C 面拥有决策权，U 面无决策权按 C 面指示执行；PFCP 消息解耦 | 对称或 U 侧独立 |
| **D. 非对称（同名不同义）型** | 接入控制（GWFD-010151 带宽流控 vs WSFD-106003 接入权限） | **机制完全不同，非 C-U 对称**；任务要求假设对称但文档实际不对称 | **独立**（010151 无 License；106003 子特性 B 需 LKV2ARD02） |

---

## 5. 依赖关系与协同

### 5.1 APN 技术栈分层依赖

```
┌─────────────────────────────────────────────────────┐
│  接入控制层（C 面权限 + U 面带宽流控）                │
│  WSFD-106003（接入权限）+ GWFD-010151（带宽流控）     │
│  归纳-底座 §3                                         │
├─────────────────────────────────────────────────────┤
│  隧道接入层（接入方式 4 隧道）                        │
│  GRE / IPSec / MPLS / L2TP                            │
│  归纳-四维度 §3                                       │
├─────────────────────────────────────────────────────┤
│  鉴权决策层（三态嵌套）                               │
│  WSFD-010301（底层 AKA）+ WSFD-011305/011306/011307  │
│  + WSFD-108007（DN 二次）                             │
│  归纳-四维度 §2                                       │
├─────────────────────────────────────────────────────┤
│  地址分配层（4 子方式 × 3 类型）                      │
│  GWFD-010105 + GWFD-010104 + WSFD-010502/010504      │
│  + GWFD-020421（基于位置）+ IPv6 三特性              │
│  归纳-四维度 §1 + §4                                  │
├─────────────────────────────────────────────────────┤
│  会话管理底座（纯描述性根底座）                       │
│  GWFD-010101 + WSFD-010501 + WSFD-010400 + WSFD-010503│
│  + WSFD-106203（别名 APN）                            │
│  归纳-底座 §1                                         │
├─────────────────────────────────────────────────────┤
│  网元选择底座（UPF 选择 + 对等网元选择）              │
│  WSFD-107010 + WSFD-010202                            │
│  归纳-底座 §2                                         │
└─────────────────────────────────────────────────────┘
```

### 5.2 C-U 决策执行分离（地址分配核心模式）

**核心 C-U 分层模式**[归纳-四维度 §1.3]：地址分配在 C 面决策、U 面执行，通过 PFCP 消息解耦。

| 决策/执行 | UNC（C 面：SMF/PGW-C/GGSN） | UDG（U 面：UPF/PGW-U） |
|---|---|---|
| **地址分配方式决策** | [WSFD-010502] 4 种决策源（UDM/Radius/SMF本地/DHCP）；[WSFD-010504] ALLOCPRECEDENCE 选 SMF 或 UPF 本地 | [GWFD-010105] 执行 C 面指示的分配方式与类型 |
| **能力协商** | 发起 PFCP Association Setup | 响应携带 **UP Function Flag ADUP=1**（恒定） |
| **地址类型指示** | PFCP Session Est Req 携带 CHV4/CHV6/V4/V6 | 按真值表执行分配或接收外部地址 |
| **地址池名下发** | Radius→SMF→UPF（Framed-Pool） | 解析池名按指定池分配 [GWFD-010105 子方式4] |
| **位置信息透传** | PFCP 携带 LAC/Tac | 基于位置匹配池组 [GWFD-020421] |

### 5.3 级联鉴权链（企业 DN 场景）

企业 DN 场景下形成 **5 特性级联强依赖链**（详见 §3.3）。

**关键规律**：
- **一次鉴权 vs 二次鉴权**[WSFD-108007 §8.2]：一次鉴权（WSFD-011305）对接入侧 AAA，决定能否接入网络；二次鉴权（WSFD-108007）对 DN-AAA，决定能否访问该 DN
- **物理路径差异**：一次鉴权 SMF↔AAA 可直连；二次鉴权 SMF↔UPF↔DN-AAA **必须经 UPF 转接**（N4 GTP-U 隧道），根因是 UPF 下沉 + DN-AAA 部署企业内网导致 SMF 与 DN-AAA 不可直达
- **协议限制**：二次鉴权 **不支持 EAP、不支持 Diameter**，仅 PAP/CHAP via Radius

### 5.4 IPv6 承载依赖链（License 串联）

IPv6 完整承载需**线性 License 依赖链**，是地址分配维度最长的依赖路径[归纳-四维度 §1.4]：

```
[GWFD-020401 IPv6承载上下文] LKV3G5V6PB01
        │ （承载基础设施，必装）
        ▼
[GWFD-020403 IPv4v6双栈接入] LKV3G5VDSA01
        │ （双栈能力使能层：使能 GWFD-010105 的 IPv4v6 取值）
        ▼
[GWFD-020406 IPv6 Prefix Delegation] LKV3G5P6PD01（V6PREFIXLENGTH<64 时触发）
        │
        ▼ （UNC 侧对称）
[WSFD-104002][WSFD-104004][WSFD-104005] IPv6/双栈/PD/DHCPv6
```

**前缀长度 64 是 PD 分水岭**[GWFD-020403 §3.1.3][GWFD-020406]：
- =64 → 普通 IPv6 地址池分配（NDP/RA 通告接口 ID）
- <64（49~63）→ IPv6 Prefix Delegation（向 UE/企业代理整个 /60、/56 等网段）

### 5.5 UPF 选择决定地址分配侧

**关键结论**[归纳-底座 §2.3]：UPF 选择决策**直接决定地址分配的执行侧** —— SMF 选定 UPF 后通过 N4 PFCP 建立会话，UPF 侧（GWFD-010101 + GWFD-010105）执行用户面会话与地址分配。

**UPF 选择 vs 地址分配冲突协调**[WSFD-010502 §3.2.4]：
- 冲突场景：静态 IP 段绑定 UPF（由 `SET STATICADDRPARA` 配置）与 SMF 主锚点 UPF 选择结果冲突
- 协调规则：**SMF 选择的主锚点 UPF 优先级更高**
- 文档引用方向：**单向引用** —— 地址分配侧感知冲突，UPF 选择侧声明"不涉及与其他特性的交互"

---

## 6. ★ 与 APN 核心关联（第 1 层直接来源）

### 6.1 ConfigurationSolution 定稿（9 个，Batch-14 直接来源）

> 来源：Batch-14 §0 9 场景 → ConfigurationSolution 映射摘要表 [EV-CA-02]。
> 每方案：地址分配 × 鉴权 × 接入方式 × 地址类型组合 + 主特性。

| CS ID | 业务场景 | 地址分配 | 鉴权 | 接入方式 | 地址类型 | 主特性 | source_evidence_ids |
|-------|---------|---------|------|---------|---------|--------|---------------------|
| **CS-APN-01** | 工厂工控访问内网 | UDM 静态 | NON_TRANS（不透明） | IPSec 隧道 | IPv4 | WSFD-010502 / IPFD-015004 / WSFD-011305 | EV-CA-02（EV-TK-14-01） |
| **CS-APN-02** | 智慧农业传感器上报 | UPF 动态（基于 APN/DNN） | TRANS_NON_AUTH（透明） | VPN 直连（NAT） | IPv4 | GWFD-010105 | EV-CA-02（EV-TK-14-02） |
| **CS-APN-03** | 家庭 CPE 宽带 | UPF 动态（基于 SMF） | TRANS_NON_AUTH | VPN 直连（NAT） | IPv4v6 双栈 | GWFD-010105 / GWFD-020403 | EV-CA-02（EV-TK-14-03） |
| **CS-APN-04** | VoLTE 语音业务 | SMF 动态 | TRANS_NON_AUTH | VPN 直连 | IPv4v6 双栈 | WSFD-010502 / WSFD-010504 | EV-CA-02（EV-TK-14-04） |
| **CS-APN-05** | 企业 AAA 二次鉴权 | RADIUS 分配 | NON_TRANS | VPN 或 GRE | IPv4 | WSFD-011305 / WSFD-011306 / IPFD-015002 | EV-CA-02（EV-TK-14-05） |
| **CS-APN-06** | 传统企业 DHCP 迁移 | DHCP 分配 | TRANS_NON_AUTH | VPN 直连 | IPv4 | WSFD-104413 | EV-CA-02（EV-TK-14-06） |
| **CS-APN-07** | 企业 L2TP VPN | LNS 分配 | NON_TRANS | L2TP 隧道 | IPv4v6 双栈 | GWFD-020412 / WSFD-104410 | EV-CA-02（EV-TK-14-07） |
| **CS-APN-08** | 区域化运营管理 | UPF 动态（基于位置区） | TRANS_NON_AUTH | VPN 直连 | IPv4 | GWFD-020421 | EV-CA-02（EV-TK-14-08） |
| **CS-APN-09** | 企业双栈 | UPF 动态（基于 APN/DNN） | TRANS_NON_AUTH | IPSec 隧道 | IPv4v6 双栈 | GWFD-010105 / GWFD-020403 / IPFD-015004 | EV-CA-02（EV-TK-14-09） |

**9 方案闭包特性**：
- C-U 协同普遍性：9 方案中 8 个涉及 UDG + UNC 双侧配置（仅 CS-APN-04 SMF 分配主在 UNC）[Batch-14 §10.4]
- License 触发点：CS-APN-07（L2TP, LKV3G5L2TP01）、CS-APN-08（基于位置, LKV3G5LBAA01）、CS-APN-09（双栈, LKV3G5VDSA01）三个方案需 License；其余 6 方案无 License 门槛
- 互斥约束：CS-APN-07（L2TP）与 CS-APN-08（基于位置）双向互斥；CS-APN-01/09（IPSec）与 GRE 隧道源地址不可相同
- 鉴权-地址联动：NON_TRANS 方式（CS-APN-01/05/07）必须开启 Radius 功能；RADIUS 地址分配（CS-APN-05）必须 `IGNOREV4/V6POOLID=DISABLE`
- 双栈配置要点：CS-APN-03/04/07/09 四方案均需为本地地址池配置 IPv4+IPv6 两种 SECTION；IPSec IPv6 支持 v02 20.8.0+

### 6.2 DecisionPoint 定稿（12 个）

> 来源：四维度归纳 §5.1（6 候选）+ 底座三维度 §4.1（6 候选），整合去重后定稿。

| DP ID | DP 名称 | 决策维度 | 取值空间 | 主决策特性 | 来源 |
|-------|---------|---------|---------|-----------|------|
| **DP-APN-ADDR-MODE** | 地址分配方式决策 | 地址分配方式 | {UDM静态, UPF-APN/DNN, UPF-LOCATION, UPF-SMF, SMF本地, RADIUS, DHCP, LNS(L2TP)} | WSFD-010502 + GWFD-010105 | [归纳-四维度 §5.1] + [Batch-14 §0] |
| **DP-APN-ADDR-GRANULARITY** | 地址分配粒度决策 | 地址分配粒度 | {APN-1&LOC-0&SMF-0, APN-0&LOC-1&SMF-0, APN-0&LOC-0&SMF-1, APN-1&LOC-1&SMF-0, APN-1&LOC-0&SMF-1, APN-0&LOC-1&SMF-1, APN-1&LOC-1&SMF-1} | GWFD-010105 + GWFD-020421 | [归纳-四维度 §5.1] |
| **DP-APN-ADDR-TYPE** | 地址类型决策 | 地址类型 | {IPv4, IPv6, IPv4v6} | WSFD-104002 + GWFD-020403（双栈需 License） | [归纳-四维度 §5.1] |
| **DP-APN-AUTH-MODE** | 鉴权方式决策 | 鉴权 | {TRANS_NON_AUTH, TRANS_AUTH, NON_TRANS, LOC_AUTH} | WSFD-011305 | [归纳-四维度 §5.1] |
| **DP-APN-ACCESS-MODE** | 接入方式决策 | 接入方式 | {直连, NAT, IPSec, GRE, MPLS-VPN, L2TP, GRE-over-IPSec} | IPFD-015002/015004/016000 + GWFD-020411/020412 | [归纳-四维度 §5.1] |
| **DP-APN-UPF-SELECT** | UPF 选择三轮决策 | 网元选择 | {按 DNN, 按 S-NSSAI, 按 DNAI, 按位置, 按接口能力, 按权重, 按负载} | WSFD-107010 | [归纳-底座 §4.1] |
| **DP-APN-PEER-NF-SELECT** | 对等网元 DNS 域名聚合决策 | 网元选择 | {按 LAI, 按 RAI, 按 TAI, 按 ZONE 名称} | WSFD-010202 | [归纳-底座 §4.1] |
| **DP-APN-ACCESS-PERMISSION** | 用户接入权限判定（C 面） | 接入控制（权限） | {允许接入, 拒绝（原因值）} | WSFD-106003 | [归纳-底座 §4.1] |
| **DP-APN-BANDWIDTH-CTRL** | U 面带宽流控方式判定 | 接入控制（带宽） | {转发, 丢弃(CAR), 缓存整形(Shaping)} × {上行, 下行} | GWFD-010151 | [归纳-底座 §4.1] |
| **DP-APN-CONCURRENCY** | 多 PDN/PDU 并发允许判定 | 会话管理 | {允许建立, 拒绝（原因值 55）} | WSFD-010503 | [归纳-底座 §4.1] |
| **DP-APN-ALIAS-APN** | 别名 APN 映射决策 | 会话管理 | {映射后 APN（别名/真实）, 原 APN} | WSFD-106203 | [归纳-底座 §4.1] |
| **DP-APN-SECOND-AUTH** | DN 二次鉴权决策 | 鉴权（DN 层） | {允许访问 DN, 拒绝} | WSFD-108007 | [归纳-四维度 §2.3 扩展] |

**12 DP 闭包特性**：
- 决策执行分离：DP-ADDR-MODE / DP-ADDR-GRANULARITY / DP-ADDR-TYPE 在 C 面决策、U 面执行（模式 C）
- 三轮筛选：DP-UPF-SELECT 采用三轮递进筛选（必选条件 → 优选条件 → 权重/负载）[归纳-底座 §2.1]
- 别名 APN 双视角：DP-ALIAS-APN 在 SGSN/MME 侧（协商 APN→别名 APN）与 GGSN/PGW-C/SMF 侧（别名 APN→真实 APN）**映射方向相反**，需在图谱中拆分为两个 Feature 变体节点[归纳-底座 §1.4]
- 接入控制非对称：DP-ACCESS-PERMISSION（C 面权限）vs DP-BANDWIDTH-CTRL（U 面带宽），机制完全不同，**非 C-U 对称**[修正 §1.6]

### 6.3 SemanticObject 定稿（12 个）

> 来源：四维度归纳 §5.2（4 候选）+ 底座三维度 §4.2（8 候选），整合后定稿。

| SO ID | SO 名称 | 语义内容 | 主承载特性 | 关键属性 | source_evidence_ids |
|-------|---------|---------|-----------|---------|---------------------|
| **SO-APN-ADDRESS-POOL** | 地址分配语义 | UE IP 地址的分配契约（来源、类型、池组、生命周期） | GWFD-010105 + GWFD-010104（UDG） / WSFD-010502（UNC） | source(6来源), type(IPv4/IPv6/双栈), pool_group, section_range, lifetime, conflict_state | EV-CA-02（EV-TK-归纳） |
| **SO-APN-AUTH-AAA** | 鉴权语义 | 用户身份验证契约（底层 AKA + APN 业务鉴权 + 二次鉴权三态） | WSFD-010301 + WSFD-011305 + WSFD-108007 | layer(接入/业务/DN), protocol(AKA/PAP/CHAP), vector(三元/四元/五元组), aaa_target(HLR/HSS/UDM/AAA/DN-AAA) | EV-CA-02（EV-TK-归纳） |
| **SO-APN-TUNNEL** | 隧道语义 | 报文穿越异种/不可信网络的封装契约 | IPFD-015002/015004/016000 + GWFD-020411/020412 | type(GRE/IPSec/MPLS/L2TP), encryption(bool), multicast_support(bool), c_u_mode(对称/C决策U执行), c_u_object_asym(bool) | EV-CA-02（EV-TK-归纳+修正） |
| **SO-APN-QUOTA-LIFECYCLE** | 配额/地址生命周期语义 | 地址池占用、释放、延迟释放、租期续约、强制回收的完整生命周期 | GWFD-010105（5 大增值功能） | alloc_state, hold_state, release_time, renew_state, force_reclaim_state | EV-CA-02（EV-TK-归纳） |
| **SO-APN-SESSION-CONTEXT** | PDU/PDN/PDP 会话上下文 | 会话级状态（会话 ID、DNN/APN、QoS Flow/承载、UE IP、F-TEID、SSC Mode） | GWFD-010101 + WSFD-010501 | session_id, dnn/apn, qos_flow/bearer, ue_ip, f_teid, ssc_mode | EV-CA-02（EV-TK-底座） |
| **SO-APN-SUBSCRIPTION** | UNC 签约数据本地缓存 | UDM/HSS/HLR 下发的 APN/DNN 签约、QoS、APN-AMBR、PDN Address、ARD、APN-OI Replacement | WSFD-010400 | apn_subscription, pdn_address(static), qos_profile, apn_ambr, ard, apn_oi_replacement, charging_characteristics | EV-CA-02（EV-TK-底座） |
| **SO-APN-APNACTNUM** | 单 APN 并发限制配置 | EPC 单 APN 粒度并发上限配置 | WSFD-010503 | APNNI, PDNNUM, IPV4ADDRNUM, IPV6ADDRNUM, PDNCONNREJCAUSE | EV-CA-02（EV-TK-底座） |
| **SO-APN-ALIAS-APN-MAP** | 别名 APN 映射记录 | 别名 APN ↔ 真实 APN 双向映射表 | WSFD-106203 | （SGSN/MME 侧）IMSI 前缀 + OLDAPN + NEWAPN；（GGSN/PGW-C/SMF 侧）SUBRANGE + ALIASAPN + CONVERTAPN + SST/SD | EV-CA-02（EV-TK-底座） |
| **SO-APN-PNFPROFILE** | UPF NF 实例属性 | UPF NF 实例的多维属性（用于三轮筛选） | WSFD-107010 | NFINSTANCENAME, NF TYPE, WEIGHT, PRIORITY, DNN/切片/DNAI/位置/EPS互通能力 | EV-CA-02（EV-TK-底座） |
| **SO-APN-AREDNS** | 位置区域 DNS 域名定制 | LAI/RAI/TAI 聚合到单一 DNS 域名 | WSFD-010202 | DNTYPE, LAC/RAC/TAC + RANGE, ZONESW, ZONENAME | EV-CA-02（EV-TK-底座） |
| **SO-APN-ARD-RECORD** | 接入限制参数记录（C 面） | C 面接入权限判定的配置记录 | WSFD-106003 | （AMF）NGMMSUBDATA（IMSIPRE/RATRESTRICT/CORERESTRICT）；（SGSN/MME）GBARD/IUARD/S1ARD（IMSI/APNNI/CARDTYPE/ARD/CTRLTYPE/CAUSE） | EV-CA-02（EV-TK-底座） |
| **SO-APN-APNQOSATTR** | APN QoS 属性（U 面带宽流控） | U 面带宽流控的上下行 CAR/Shaping 开关与方式 | GWFD-010151 | CARSHAPESWUL/CARSHAPEUL/CARSHAPESWDL/CARSHAPEDL | EV-CA-02（EV-TK-底座） |

### 6.4 BusinessRule 定稿（16 个）

> 来源：四维度归纳 §5.3（11 候选）+ 底座三维度 §4.3（16 候选），整合去重后定稿。
> 严重级别：CRITICAL（互斥/License 阻断）/ HIGH（强依赖链）/ MEDIUM（顺序约束/优先级）/ LOW（配置约束）。

| BR ID | BR 名称 | 约束类型 | 约束内容 | 涉及特性 | 严重级别 | 来源 |
|-------|---------|---------|---------|---------|---------|------|
| **BR-APN-LOC-L2TP-EXCL** | 基于位置与 L2TP 互斥 | 互斥（双向） | 基于位置的地址分配与 L2TP VPN 不可同时应用；020421 声明互斥，020412 未声明需双向补全 | GWFD-020421 ↔ GWFD-020412 | CRITICAL | [归纳-四维度 §5.3][修正 §3.8] |
| **BR-APN-GRE-IPSEC-SRC-EXCL** | GRE 与 IPSec 源地址互斥 | 互斥 | GRE 隧道源地址不能与 IPSec 隧道源地址相同 | IPFD-015002 ↔ IPFD-015004 | CRITICAL | [归纳-四维度 §5.3][修正 §3.3] |
| **BR-APN-L2TP-ADDRAUTO-EXCL** | L2TP 与地址自动检测互斥 | 互斥 | L2TP VPN 与用户面地址自动检测不可同时应用 | GWFD-020412 ↔ GWFD-010108 | CRITICAL | [归纳-四维度 §5.3] |
| **BR-APN-RADIUS-CASCADE** | Radius 级联强依赖链 | 强依赖链 | Radius 功能 → Radius 鉴权接入 → 终端二次鉴权（+ Radius 抄送） | WSFD-011306 → WSFD-011305 → WSFD-108007（→ WSFD-011307） | HIGH | [归纳-四维度 §5.3][归纳-四维度 §2.3] |
| **BR-APN-LOC-AUTH-NO-PPP** | 本地鉴权不支持 PPP 用户 | 限制 | 本地鉴权接入（LOC_AUTH）不支持 PPP 用户 | WSFD-011305（LOC_AUTH） | HIGH | [归纳-四维度 §5.3] |
| **BR-APN-IPV6-CASCADE** | IPv6 承载强依赖链 | 强依赖链 | IPv6 承载 → 双栈 → PD（V6PREFIXLENGTH<64 触发） | GWFD-020401 → GWFD-020403 → GWFD-020406 | HIGH | [归纳-四维度 §5.3][归纳-四维度 §1.4] |
| **BR-APN-DUALSTACK-NEED-LICENSE** | 双栈必须 License | License 约束 | IPv4v6 双栈落地必须 License LKV3G5VDSA01（GWFD-020403 使能 GWFD-010105 的 IPv4v6 取值） | GWFD-020403 使能 GWFD-010105 | CRITICAL | [归纳-四维度 §5.3][修正 §1.1] |
| **BR-APN-LOC-NEED-LICENSE** | 基于位置必须 License | License 约束 | 基于位置的地址分配必须 License LKV3G5LBAA01（母特性 010105 无 License） | GWFD-020421 | CRITICAL | [归纳-四维度 §5.3] |
| **BR-APN-L2TP-CU-ASYM** | L2TP License C-U 不对称 | C-U 不对称 | L2TP VPN License 仅 UDG 侧必须（82200BVC），UNC 侧无 | GWFD-020412 ↔ WSFD-104410 | HIGH | [归纳-四维度 §5.3][修正 §1.3] |
| **BR-APN-DNAAA-IP-UNIQUE** | DN-AAA IP 唯一性 | 唯一性约束 | 直连 AAA 与经 UPF 中转 AAA 场景的 Radius Server IP 不可相同 | WSFD-108007 | MEDIUM | [归纳-四维度 §5.3] |
| **BR-APN-SECOND-AUTH-PROTO** | 二次鉴权协议限制 | 协议限制 | 终端二次鉴权仅支持 PAP/CHAP via Radius，不支持 EAP/Diameter | WSFD-108007 | HIGH | [归纳-四维度 §5.3][归纳-四维度 §2.3] |
| **BR-APN-CONCURRENCY-11-15** | 并发会话硬上限 | 硬上限 | EPC 单用户 PDN 连接 ≤ 11；5GC 单用户 PDU 会话 ≤ 15；超限 MME/SMF 拒绝 | WSFD-010503 | HIGH | [归纳-底座 §4.3] |
| **BR-APN-ALIAS-DOUBLE-COND** | 别名 APN 转换双条件 | 逻辑与 | SGSN/MME 侧：IMSI 号段匹配 AND 协商 APN 在映射表，两条件同时满足才转换 | WSFD-106203 | MEDIUM | [归纳-底座 §4.3] |
| **BR-APN-UPF-VENDOR-LOCK** | SMF 与 UPF 同厂商 | 硬约束 | SMF 和 UPF 设备必须同时为 HUAWEI | WSFD-107010 | CRITICAL | [归纳-底座 §4.3] |
| **BR-APN-AMF-LOCAL-FIRST** | AMF 本地配置优先于签约 | 优先级 | AMF 本地匹配 > 签约兜底；本地 Null 强制允许；紧急注册跳过接入控制 | WSFD-106003 | MEDIUM | [归纳-底座 §4.3] |
| **BR-APN-CARDTYPE-NEED-AUTH** | 卡类型控制依赖鉴权 | 前置依赖 | SGSN/MME 卡类型控制（WSFD-106003 子特性 B）必须先启用 WSFD-010301 鉴权功能 | WSFD-106003_B → WSFD-010301 | HIGH | [归纳-底座 §4.3][修正 §3.5] |

---

## 7. 关键发现（11 修正 + 归类重审）

### 7.1 配置树 11 处修正清单（Stage 3 验证定稿）

> 来源：修正清单 §1。每条经 Stage 3 横向验证后定稿为图谱建模指导。

| # | 修正项 | 修正结论 | 图谱建模影响 | 来源 |
|---|--------|---------|-------------|------|
| **7.1.1** | IPv4v6 双栈定位 | 双栈 = 能力使能层（GWFD-020403），使能 GWFD-010105 的 IPv4v6 取值；非父子、非包含，是"能力叠加"关系 | Feature 变体维度建模 `能力层级=使能层/机制层`；BR-APN-DUALSTACK-NEED-LICENSE 使能方向单向（020403→010105） | [修正 §1.1] |
| **7.1.2** | WSFD-010504 与 WSFD-010502 关系 | 010504 ⊂ 010502（010504 仅 SMF 本地池 1 种，010502 共 4 种）；并列子集，非父子 | parent_feature_id 置空或指向更高层；FeatureRelation 建模 `subset_of` | [修正 §1.2] |
| **7.1.3** | APNL2TPATTR vs APNL2TPCTRL 不对称 | C-U 配置对象命名与参数量均不对称（U: 10+参数；C: 2参数） | SO-APN-TUNNEL 建模 `c_u_object_asym=true`；ConfigObject 两侧分离建模 | [修正 §1.3] |
| **7.1.4** | IPV4ALLOCTYPE / IPV6ALLOCTYPE 真实载体 | 两侧产品文档均未显式定义此参数名；实际指示是 PFCP CHV4/CHV6/V4/V6 BIT 位组合 | SO-APN-ADDRESS-POOL.type 来源标 `PFCP BIT`；不建模为配置参数 | [修正 §1.4] |
| **7.1.5** | WSFD-010202 网元角色 | 实际适用 NF 为 SGSN、MME（非 SMF）；本特性是 2G/3G/4G 特性 | Feature 节点 `applicable_nf` 修正为 `SGSN/MME`；不与 5G UPF 选择（WSFD-107010）混淆 | [修正 §1.5] |
| **7.1.6** | GWFD-010151 与 WSFD-106003 非对称 | 机制完全不同，非 C-U 对称：UDG = 带宽流控（CAR/Shaping）；UNC = 接入权限（签约 ARD/APN/卡类型） | 拆分为两个 Feature 变体（bandwidth_control vs access_permission）；不建 `c_u_symmetric` 边 | [修正 §1.6] |
| **7.1.7** | WSFD-106003 双特性合一 | 同一特性 ID 下含两个实现独立的子特性：AMF 侧（5GC，RAT+核心网限制，无 License）+ SGSN/MME 侧（2/3/4G，签约 ARD+APN+卡类型，需 LKV2ARD02） | Feature 变体建模 `子特性=A/B`；拆分为两个 Feature 变体节点 | [修正 §1.7] |
| **7.1.8** | WSFD-106203 别名 APN 双视角语义反转 | 同一特性 ID 在两套网元下映射方向相反：SGSN/MME = 协商→别名（DNS 屏蔽）；GGSN/PGW-C/SMF = 别名→真实（资源归一） | 拆分为两个 Feature 变体（按网元角色视角区分）；BR 分网元建模映射方向 | [修正 §1.8] |
| **7.1.9** | GWFD-010104 与 GWFD-010105 父子关系 | 父子关系成立：010104 是"地址分配方式总览"，010105 是其下"用户面地址分配"分支；但 010104 无 License/告警/限制 | parent_feature_id 保留（010105→010104）；Feature 变体区分 `总览/分支` | [修正 §1.9] |
| **7.1.10** | WSFD-104001 单向依赖声明矛盾 | 三套代际均声明"不涉及与其他特性的交互"，但 WSFD-104002（5G 明确）、WSFD-104004（显式声明）均强依赖 | FeatureRelation 建模 `strong_depends_on`（104002→104001, 104004→104001）；忽略"不涉及"声明，以流程语义为准 | [修正 §1.10] |
| **7.1.11** | MPLS VPN 缺激活/调测文档 | 9 篇全为概念/原理/组网说明文档，无激活/调测/参考信息操作文档 | ConfigObject 节点从 UDG 命令字典补全；标注 `doc_gap=MML命令缺失` | [修正 §1.11] |

### 7.2 归类重审（Stage 3 横向验证后定稿）

| # | 重审项 | 重审结论 | 来源 |
|---|--------|---------|------|
| **7.2.1** | GWFD-010151 与 WSFD-106003 非 C-U 对称，需拆分 | **定稿拆分**：UDG 侧归"U 面带宽流控"子类；UNC 侧归"C 面接入权限控制"子类；图谱不建 `c_u_symmetric` 边 | [归纳-底座 §3.3][修正 §1.6] |
| **7.2.2** | WSFD-106003 双特性合一需拆分 | **定稿拆分**：子特性 A（AMF 侧，5GC 移动性限制，无 License）+ 子特性 B（SGSN/MME 侧，2/3/4G 签约 ARD/APN/卡类型，需 LKV2ARD02）；适用 NF / 控制依据 / License / 标准 / 决策时机全部不同 | [归纳-底座 §3.1][修正 §1.7] |
| **7.2.3** | WSFD-106203 同特性 ID 双视角语义反转需拆分 | **定稿拆分**：SGSN/MME 侧（协商 APN→别名 APN，DNS 屏蔽，License LKV2ALIASAPN02，命令 ADD ALIASAPN）vs GGSN/PGW-C/SMF 侧（别名 APN→真实 APN，资源归一，License LKV2AAPN01，命令 ADD APNALIAS）；映射方向 / License / 命令族 / 规格全不同 | [归纳-底座 §1.4][修正 §1.8] |
| **7.2.4** | WSFD-010202 网元角色纠偏 | **定稿纠偏**：适用 NF 从文档清单标注的 "UNC/SMF" 修正为 "SGSN、MME"；本特性是 Pre-5G（2G/3G/4G）特性，与 5G UPF 选择（WSFD-107010）代际互补不重叠 | [归纳-底座 §2.2][修正 §1.5] |
| **7.2.5** | GWFD-020403 与 GWFD-010105 关系定稿 | **定稿**：能力叠加关系（非父子、非包含）；GWFD-020403 是 GWFD-010105 的"双栈特化版本"；License 使能方向单向（020403→010105） | [归纳-四维度 §4.2][修正 §1.1] |

### 7.3 Stage 3 横向验证 — 12 个待解决问题处置

> 来源：修正清单 §5。Stage 3 对每个问题给出处置结论（已验证 / 待 Stage 4 处理 / 标注缺口）。

| Q# | 问题 | Stage 3 处置结论 | 来源 |
|----|------|-----------------|------|
| **Q1** | WSFD-010504 的 ALLOCPRECEDENCE 决策边界 | **定稿建模**：DP-APN-ADDR-MODE 取值空间含 `SMF_ALLOC` 独立分支；BR 建模 C/U 二选一（待 Stage 4 实例化时从 OM 手册补充具体互斥场景） | [修正 §5.1 Q1] |
| **Q2** | Radius 地址分配端到端链路信元映射 | **定稿建模**：SO-APN-ADDRESS-POOL 建模 `radius_pool_chain=true`；BR-APN-RADIUS-CASCADE 建模三特性级联；时序图 Stage 4 实例化时绘制 | [修正 §5.1 Q2] |
| **Q3** | WSFD-104004 的 3 个强依赖具体内容 | **定稿建模**：104001（承载底座强依赖）、011306（Radius 获取 PD 网段强制）、104002（双栈+PD 叠加条件依赖）；BR-APN-IPV6-CASCADE 已含 | [修正 §5.1 Q3] |
| **Q4** | SET APNADDRESSATTR 在 010104 与 010105 中参数差异 | **定稿建模**：ConfigObject `APNADDRESSATTR` 建模 `shared_by=[010104,010105]`；参数维度按特性分离 | [修正 §5.1 Q4] |
| **Q5** | GWFD-020406 变体 5 License 归属 | **标注缺口**：变体 5 使用 LKV3G5LBAA01（基于位置）而非 LKV3G5P6PD01（PD License），可能实际属于 GWFD-020421 的 IPv6 扩展；Stage 4 实例化时需澄清归属 | [修正 §5.1 Q5] |
| **Q6** | WSFD-108007 与 IPSec/GRE 场景关联 | **标注协同**：企业专网典型组网中二次鉴权与 IPSec/GRE 隧道协同配置；建模为 `co_deployed` 软关联（非强依赖） | [修正 §5.2 Q6] |
| **Q7** | GWFD-020412 与 GWFD-020421 互斥双向声明 | **定稿双向建模**：BR-APN-LOC-L2TP-EXCL 已双向建模；以 020421 文档为准 | [修正 §5.2 Q7] |
| **Q8** | MPLS VPN MML 命令补全 | **标注缺口**：ConfigObject 节点标注 `source=命令字典补全`；Stage 4 从 UDG 命令字典补全 ADD/MOD VPNINSTANCE 等 | [修正 §5.2 Q8] |
| **Q9** | 底层 AKA 与 APN 业务鉴权隐式协同 | **定稿建模**：FeatureRelation 建模 `implicit_sequence`（010301 → 011305 时序）；非强依赖，隐式协同无直接信令耦合 | [修正 §5.3 Q9] |
| **Q10** | AUTHMODE 与地址空间归属联动 | **定稿建模**：BR-APN-AUTH-ADDRSPACE 建模鉴权方式与地址空间归属联动（TRANS_NON_AUTH=运营商；NON_TRANS/TRANS_AUTH=ISP/企业网） | [修正 §5.3 Q10] |
| **Q11** | RA（Router Advertisement）License 归属 | **标注缺口**：RA 在 GWFD-020401/020403/020406 共享描述；Stage 4 实例化时需区分 RA 生成归属（多 License 可能） | [修正 §5.4 Q11] |
| **Q12** | 多 PDN/PDU 场景每会话地址类型独立决策 | **定稿建模**：DP-APN-ADDR-TYPE 标注 `per_session=true`；无跨会话约束 | [修正 §5.4 Q12] |

---

## 8. 附录

### 8.1 9 场景归并表（地址分配 × 鉴权 × 接入 × 类型）

| CS ID | 地址分配 | 鉴权 | 接入方式 | 地址类型 | 是否需 License | 关键约束 |
|-------|---------|------|---------|---------|---------------|---------|
| CS-APN-01 | UDM 静态 | NON_TRANS | IPSec | IPv4 | 否 | IPSec 源地址不与 GRE 冲突 |
| CS-APN-02 | UPF-APN/DNN | TRANS_NON_AUTH | NAT | IPv4 | 否 | 无 |
| CS-APN-03 | UPF-SMF | TRANS_NON_AUTH | NAT | IPv4v6 | **是**（LKV3G5VDSA01 双栈） | 双栈需 IPv4+IPv6 两种 SECTION |
| CS-APN-04 | SMF 本地 | TRANS_NON_AUTH | 直连 | IPv4v6 | **是**（LKV3G5VDSA01 双栈） | IMS 精确寻址 |
| CS-APN-05 | RADIUS | NON_TRANS | GRE（可选） | IPv4 | 否 | NON_TRANS 必须开启 Radius；IGNOREV4/V6POOLID=DISABLE |
| CS-APN-06 | DHCP | TRANS_NON_AUTH | 直连 | IPv4 | 否 | DHCP 文档缺口（无完整脚本） |
| CS-APN-07 | LNS（L2TP） | NON_TRANS | L2TP | IPv4v6 | **是**（LKV3G5L2TP01） | 与基于位置互斥；PPP 鉴权 |
| CS-APN-08 | UPF-LOCATION | TRANS_NON_AUTH | 直连 | IPv4 | **是**（LKV3G5LBAA01） | 与 L2TP 互斥；用户移动需重新分配 |
| CS-APN-09 | UPF-APN/DNN | TRANS_NON_AUTH | IPSec | IPv4v6 | **是**（LKV3G5VDSA01 双栈） | IPSec IPv6 支持 v02 20.8.0+ |

### 8.2 特性互斥/依赖矩阵

| 特性对 | 关系类型 | 关系内容 | BR ID |
|--------|---------|---------|-------|
| GWFD-020421 ↔ GWFD-020412 | 互斥（双向） | 基于位置与 L2TP 不可同时应用 | BR-APN-LOC-L2TP-EXCL |
| IPFD-015002 ↔ IPFD-015004 | 互斥（源地址） | GRE 与 IPSec 源地址不可相同 | BR-APN-GRE-IPSEC-SRC-EXCL |
| GWFD-020412 ↔ GWFD-010108 | 互斥 | L2TP 与地址自动检测不可同时应用 | BR-APN-L2TP-ADDRAUTO-EXCL |
| WSFD-011306 → WSFD-011305 → WSFD-108007（→ WSFD-011307） | 强依赖链 | Radius 级联（功能→鉴权→二次→抄送） | BR-APN-RADIUS-CASCADE |
| GWFD-020401 → GWFD-020403 → GWFD-020406 | 强依赖链 | IPv6 承载→双栈→PD（License 串联） | BR-APN-IPV6-CASCADE |
| GWFD-020403 → GWFD-010105 | 能力使能（单向） | 双栈使能 IPv4v6 取值 | BR-APN-DUALSTACK-NEED-LICENSE |
| WSFD-106003_B → WSFD-010301 | 前置依赖 | 卡类型控制依赖鉴权功能 | BR-APN-CARDTYPE-NEED-AUTH |
| WSFD-104002 → WSFD-104001 | 强依赖（流程级） | IPv4v6 双栈依赖 IPv6 承载底座（忽略"不涉及"声明） | （隐含，Stage 4 建模） |
| WSFD-104004 → WSFD-104001 | 强依赖（流程级） | IPv6 PD 依赖 IPv6 承载底座（忽略"不涉及"声明） | （隐含，Stage 4 建模） |
| WSFD-010502 ↔ WSFD-107010 | 单向引用 | 地址分配侧感知 UPF 选择冲突；SMF 主锚点优先 | （隐含，Stage 4 建模） |
| WSFD-010301 → WSFD-011305 | 隐式时序（非强依赖） | 底层 AKA 先发生，业务鉴权后发生 | （隐含，Stage 4 建模） |
| WSFD-011307 → WSFD-011306 | parallel_extends（配置共享） | Radius 抄送共享 Radius 功能配置对象 | （隐含，Stage 4 建模） |

### 8.3 C-U 关系模式归类速查

| 模式 | 适用特性 | 数量 |
|------|---------|------|
| **A. 对称同构** | GRE（IPFD-015002 双侧）、IPSec（IPFD-015004 + IPFD-016000）、MPLS VPN（GWFD-020411 + WSFD-104411）、静态冗余（GWFD-010107 + WSFD-107021） | 4 对 |
| **B. C 决策 U 执行** | L2TP VPN（WSFD-104410 + GWFD-020412） | 1 对 |
| **C. 决策执行分离** | 地址分配（WSFD-010502 + GWFD-010105）、控制面分配（WSFD-010504 + GWFD-010105）、IPv6 承载（WSFD-104001 + GWFD-020401）、IPv6 PD（WSFD-104004 + GWFD-020406）、会话管理（WSFD-010501 + GWFD-010101） | 5 对 |
| **D. 非对称（同名不同义）** | 接入控制（GWFD-010151 带宽流控 vs WSFD-106003 接入权限） | 1 对 |

### 8.4 文档缺口清单（Stage 4 补全方向）

| 缺口 | 涉及特性 | Stage 4 补全来源 |
|------|---------|-----------------|
| 无 MML 激活脚本 | GWFD-020411 / WSFD-104411 / WSFD-107010 / WSFD-010504 / WSFD-104413 / WSFD-104005 | OM 命令手册 + UDG/UNC 初始配置与调测 + 业务专题 |
| 仅 1 篇概述 | WSFD-107010 | 业务专题 `UNC UPF选择专题/特性映射与交互_72976829.md` |
| 4G/5G 指向外部手册 | GWFD-010101 / WSFD-010501 | UDG/UNC 会话管理产品手册 |
| 子特性未完整描述 | WSFD-106003（双特性合一） | 两个子特性独立文档（AMF + SGSN/MME） |
| C-U 协同细节缺失 | GWFD-010151 / WSFD-104413 | 对照 GWFD-010224 N4 接口特性 |
| 文档内部不一致 | GWFD-010105 / GWFD-020421 / GWFD-010151 / GWFD-020406 | 以激活脚本原样保留并标注 |
| 测量指标/告警缺失 | GWFD-010151 / WSFD-011307 / WSFD-010502 | 可能在 UDG 侧或独立参考信息文档 |

### 8.5 Evidence 占位映射规范

本文件统一使用占位 `EV-CA-02`。Stage 4 实例化时按以下规则展开：

| 结论标注 | 展开规则 |
|---------|---------|
| `[归纳-四维度 §N]` | 展开为 `归纳-四维度决策与机制.md` 的 `EV-TK-归纳` 占位 |
| `[归纳-底座 §N]` | 展开为 `归纳-APN底座三维度.md` 的 `EV-TK-底座` 占位 |
| `[修正 §N]` | 展开为 `归纳-配置树修正与Stage3待解决项.md` 的 `EV-TK-修正` 占位 |
| `[Batch-14 §N]` | 展开为 `Batch-14-业务场景方案.md` 的 `EV-TK-14` 占位（细分 EV-TK-14-01~09） |
| `[GWFD-xxxxx §N]` / `[WSFD-xxxxx §N]` / `[IPFD-xxxxx §N]` | 展开为该特性 feature-knowledge 文件的 `EV-FK-xx` 占位 |

---

## 9. Stage 3 总结与 Stage 4 衔接

### 9.1 第 1 层对象定稿统计

| 对象类型 | 定稿数量 | 来源分布 |
|---------|---------|---------|
| **ConfigurationSolution（CS）** | **9 个** | Batch-14 §0 直接来源（CS-APN-01 ~ CS-APN-09） |
| **DecisionPoint（DP）** | **12 个** | 四维度归纳 6 个 + 底座三维度 6 个 |
| **SemanticObject（SO）** | **12 个** | 四维度归纳 4 个 + 底座三维度 8 个 |
| **BusinessRule（BR）** | **16 个** | 四维度归纳 11 个 + 底座三维度 16 个，去重后定稿 |
| **合计** | **49 个第 1 层对象** | |

### 9.2 关键修正定稿（11 处 + 5 处归类重审）

- **11 处配置树/意图澄清修正**：全部经 Stage 3 横向验证后定稿，作为 Stage 4 Feature 节点建模指导
- **5 处归类重审**：双栈能力使能层（GWFD-020403↔010105）、WSFD-010504 并列子集、APNL2TPATTR/CTRL 不对称、010202 网元角色纠偏、接入控制非对称拆分（GWFD-010151 vs WSFD-106003）、106003 双特性合一拆分、106203 双视角反转拆分

### 9.3 12 个 Stage 3 待解决问题处置

- **9 个定稿建模**：Q1/Q2/Q3/Q4/Q7/Q9/Q10/Q12 已定稿为 DP/SO/BR 建模指导
- **3 个标注缺口**：Q5（020406 变体 5 License 归属）、Q8（MPLS MML 命令补全）、Q11（RA License 归属）需 Stage 4 实例化时补全

### 9.4 Stage 4 衔接

本文档产出的 49 个第 1 层对象（9 CS + 12 DP + 12 SO + 16 BR）作为 Stage 4 三层图谱实例化的**第 1 层直接数据源**：

| Stage 4 任务 | 数据源 |
|-------------|--------|
| 第 1 层 ConfigurationSolution 实例化 | §6.1（9 CS 定稿） |
| 第 1 层 DecisionPoint 实例化 | §6.2（12 DP 定稿） |
| 第 1 层 SemanticObject 实例化 | §6.3（12 SO 定稿） |
| 第 1 层 BusinessRule 实例化 | §6.4（16 BR 定稿） |
| 第 2 层 Feature 节点建模（含拆分/变体） | §7.1（11 修正）+ §7.2（5 归类重审） |
| 第 2 层 FeatureRelation 建模 | §8.2（特性互斥/依赖矩阵） |
| 第 3 层 ConfigObject 补全 | §8.4（文档缺口清单） |

---

**文档版本**：v1.0（Stage 3 横向综合分析）
**完成时间**：2026-06-22
**上游来源**：topic-knowledge 4 文件 + feature-knowledge 37 特性
**下游消费者**：Stage 4 三层图谱实例化（第 1 层 CS/DP/SO/BR + 第 2 层 Feature/FeatureRelation + 第 3 层 ConfigObject）
