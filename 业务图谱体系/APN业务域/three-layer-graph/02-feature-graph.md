# APN 业务域三层图谱 · 第 2 层：特性图谱

> **文件定位**：`three-layer-graph/02-feature-graph.md`
> **Schema 参考**：`三层图谱Schema-最终版-v0.1.md` §9 特性图谱层（★§9.3 Feature 字段含 `variant_dimensions`，§9.6 FeatureRule，§9.8 关系）
> **本体参考**：`三层图谱本体标准定义.md`、`三层图谱对象与关系设计.md`
> **作用**：实例化 APN 业务域 37 个 Feature + depends_on 边 + requires_license 边 + FeatureRule + FeatureTaskOrderEdge
> **数据来源**：`feature-knowledge/cross-feature-analysis.md`（1,139 行）、37 篇 feature-knowledge、`apn-feature-doc-list.md`（★ EV-FK 编号权威顺序）

---

## 0. 特性图谱总览

### 0.1 37 Feature 分组（6 大类）

> 分类原则来自 `cross-feature-analysis.md` §1.1 + `归纳-APN底座三维度.md`。每个 Feature 节点标注 `feature_group` 属性。

| feature_group | 特性数 | UDG 侧特性 | UNC 侧特性 | 核心能力 |
|---------------|--------|------------|------------|----------|
| **APN 基础**（会话管理底座） | **5** | GWFD-010101 会话管理(U) | WSFD-010501 会话管理(C)、WSFD-010503 多 PDN/PDU、WSFD-010400 用户数据管理、WSFD-106203 别名 APN | 宿主流程 + 签约数据源 + 并发治理 + APN 映射（纯描述性底座） |
| **地址分配** | **18** | GWFD-010104 总览、GWFD-010105 用户面分配、GWFD-020421 基于位置、GWFD-010107 静态路由冗余、GWFD-010108 地址自动检测、GWFD-020401 IPv6 承载、GWFD-020403 IPv4v6 双栈、GWFD-020406 IPv6 PD | WSFD-010502 地址分配方式、WSFD-010504 控制面地址分配、WSFD-104002 IPv4v6 双栈、WSFD-104001 IPv6 承载、WSFD-104004 IPv6 PD、WSFD-104005 DHCPv6、WSFD-104413 DHCP、WSFD-107010 UPF 选择、WSFD-107021 静态路由冗余(C) | 地址分配来源×类型正交矩阵；IPv6 承载 License 串联链 |
| **鉴权计费** | **5** | — | WSFD-010301 鉴权功能(AKA)、WSFD-011305 Radius 鉴权接入、WSFD-011306 Radius 功能、WSFD-011307 Radius 抄送、WSFD-108007 终端二次鉴权 | 两套并列鉴权体系 + Radius 三件套级联 |
| **接入方式**（4 隧道） | **5** | IPFD-015002 GRE(U+C)、IPFD-015004 IPSec(UDG)、GWFD-020411 MPLS VPN、GWFD-020412 L2TP VPN | IPFD-016000 IPSec(UNC)、WSFD-104411 MPLS VPN、WSFD-104410 L2TP VPN | 4 隧道对比；对称同构 3 + C 决策 U 执行 1 |
| **网元选择** | **2** | — | WSFD-107010 UPF 选择（5G）、WSFD-010202 对等网元选择（Pre-5G） | 代际互补；UPF 三轮筛选 + DNS 域名聚合 |
| **接入控制** | **2** | GWFD-010151 接入控制（U 面带宽流控） | WSFD-106003 用户接入控制功能（C 面接入权限） | ★ 非 C-U 对称（同名不同义） |
| **合计** | **37** | 16 | 21 | — |

> **注**：地址分配域 18 个含 WSFD-107010/WSFD-107021（与地址分配强耦合）。WSFD-107010 在 `apn-feature-doc-list.md` 中位于网元选择类，但首要归属仍为网元选择，次要归属地址分配（`cross_group`）。

### 0.2 License 总览

| 产品 | License 数 | 说明 |
|------|-----------|------|
| UDG | 7 | IPv6 三件套（承载/双栈/PD）+ 基于位置 + MPLS + L2TP + IPv6 承载底座 |
| UNC | 6 | IPv6 PD + MPLS + 二次鉴权 + ARD-B + UPF 选择（双）+ 别名 APN（双） |
| 共享/无 License | 24 | 纯描述性底座（5）+ 地址分配机制层（8）+ Radius 三件套（3）+ GRE/IPSec（3）+ 接入控制 U 侧（1）+ 对等网元选择（1）+ 其他（3） |
| **需 License 总计** | **13** | 见 §3 完整清单 |

### 0.3 全局字段声明（status）

> **适用范围**：本文件 §1（37 个 Feature）和 §3（13 个 License）所有对象。
> **声明**：本文件所有 Feature（GWFD/WSFD/IPFD-*）和 License（LKV*）的 `status` 字段值均为 `active`（Schema §9.3 Feature.status 必备、§9.5 License.status 必备）。
> **★字段补齐说明（P1 批次2）**：§1 所有 37 个 Feature 表已显式补 `status` 行（均 `active`，含纯描述性底座 GWFD-010101 / WSFD-010501）。License 表 §3 已含 `status` 列（无需补）。
> **依据**：APN 业务域所有特性和 License 均处于正式启用状态。
> **例外**：无。所有对象当前均为 `active`，无 `deprecated` 或 `planned` 状态。

### 0.4 EV-FK 编号约定（★ 严格按 apn-feature-doc-list.md 顺序）

> **重要**：`source_evidence_ids` 中的 `EV-FK-01` ~ `EV-FK-37` 编号严格按 `apn-feature-doc-list.md` 总览表的序号 1-37，**不按 cross-feature-analysis 附录 A 的分组顺序**。下表为完整映射：

| EV-FK | feature_id | EV-FK | feature_id | EV-FK | feature_id | EV-FK | feature_id |
|-------|-----------|-------|-----------|-------|-----------|-------|-----------|
| EV-FK-01 | GWFD-010101 | EV-FK-11 | GWFD-020412 | EV-FK-21 | WSFD-104004 | EV-FK-31 | IPFD-016000 |
| EV-FK-02 | WSFD-010501 | EV-FK-12 | WSFD-010502 | EV-FK-22 | WSFD-104413 | EV-FK-32 | GWFD-020411 |
| EV-FK-03 | WSFD-010503 | EV-FK-13 | WSFD-010504 | EV-FK-23 | WSFD-104005 | EV-FK-33 | WSFD-104411 |
| EV-FK-04 | WSFD-010400 | EV-FK-14 | WSFD-104410 | EV-FK-24 | WSFD-011305 | EV-FK-34 | WSFD-107010 |
| EV-FK-05 | WSFD-106203 | EV-FK-15 | WSFD-107021 | EV-FK-25 | WSFD-011306 | EV-FK-35 | WSFD-010202 |
| EV-FK-06 | GWFD-010105 | EV-FK-16 | GWFD-020403 | EV-FK-26 | WSFD-010301 | EV-FK-36 | WSFD-106003 |
| EV-FK-07 | GWFD-010104 | EV-FK-17 | WSFD-104002 | EV-FK-27 | WSFD-108007 | EV-FK-37 | GWFD-010151 |
| EV-FK-08 | GWFD-020421 | EV-FK-18 | GWFD-020401 | EV-FK-28 | WSFD-011307 | | |
| EV-FK-09 | GWFD-010108 | EV-FK-19 | WSFD-104001 | EV-FK-29 | IPFD-015002 | | |
| EV-FK-10 | GWFD-010107 | EV-FK-20 | GWFD-020406 | EV-FK-30 | IPFD-015004 | | |

---

## 1. Feature 实例化（37 个）

### 1.1 APN 基础（会话管理底座，5 个）

#### GWFD-010101 会话管理（U）

| 字段 | 值 |
|------|---|
| `feature_id` | `GWFD-010101` |
| `feature_name` | `会话管理(U)` |
| `feature_summary` | UDG 侧 PDU/PDN/PDP 会话宿主流程，被动接收 PFCP/GTP-C 信令建立/释放会话，分配 F-TEID，是 APN 域纯描述性根底座（无独立配置命令） |
| `feature_group` | `APN 基础` |
| `variant_dimensions` | `["代际(2G/3G/4G/5G)", "会话类型(PDP/PDN/PDU)"]` |
| `applicable_nf_map` | `{"UDG": ["SGW-U", "PGW-U", "UPF"]}` |
| `first_release` | `UDG 20.0.0`（2/3G 补全 20.3.0） |
| `requires_license` | 无 |
| `key_capabilities` | ① PDU/PDN/PDP 会话建立/释放宿主流程 ② 接收 UNC PFCP/GTP-C 信令装规则（PDR/FAR/URR/QER）③ 分配 F-TEID ④ 纯描述性底座，无独立 MML 配置命令（仅运维查询 DSP POOLUSAGE/DSP SESSIONINFO + 2/3G PDPAPN 维护） |
| `source_evidence_ids` | `EV-FK-01`, `EV-CA-01` |
| `status` | `active` |

> **FeatureRule 说明**：本特性为纯描述性底座，无 ConfigTask 直接关联，通过 `FR-APN-04`（会话管理底座被动触发）说明其描述性定位（见 §5）。

#### WSFD-010501 会话管理（C）

| 字段 | 值 |
|------|---|
| `feature_id` | `WSFD-010501` |
| `feature_name` | `会话管理(C)` |
| `feature_summary` | UNC 侧会话管理控制面，经 PFCP/GTP-C 下发 PDR/FAR/URR/QER 给 UDG，管理 PDU/PDN/PDP 会话生命周期，APN 域纯描述性根底座 |
| `feature_group` | `APN 基础` |
| `variant_dimensions` | `["代际(2G/3G/4G/5G)", "接口(Gx/N7/PFCP)"]` |
| `applicable_nf_map` | `{"UNC": ["SGSN", "MME", "SGW-C", "PGW-C", "SMF", "AMF"]}` |
| `first_release` | `UNC 20.0.0`（2/3G 补全 20.3.2） |
| `requires_license` | 无 |
| `key_capabilities` | ① PFCP Session Est/Mod/Del 下发 UDG ② GTP-C 会话管理（2/3/4G）③ N7/N11 服务化会话管理（5G）④ 2/3G PDP APN 维护（ADD/MOD/RMV PDPAPN）⑤ 纯描述性底座，无独立 License/配置对象 |
| `source_evidence_ids` | `EV-FK-02`, `EV-CA-01` |
| `status` | `active` |

> **FeatureRule 说明**：本特性为纯描述性底座，无 ConfigTask 直接关联，通过 `FR-APN-04` 说明其描述性定位（见 §5）。

#### WSFD-010503 多 PDN/PDU 功能

| 字段 | 值 |
|------|---|
| `feature_id` | `WSFD-010503` |
| `feature_name` | `多 PDN/PDU 功能` |
| `feature_summary` | 单用户多 PDN/PDU 并发会话治理，限制单 APN 并发数（PDNNUM/IPV4ADDRNUM/IPV6ADDRNUM），超限拒绝并下发 PDNCONNREJCAUSE |
| `feature_group` | `APN 基础` |
| `variant_dimensions` | `["并发维度(PDN数/IPv4地址数/IPv6地址数)", "拒绝原因值(PDNCONNREJCAUSE)"]` |
| `applicable_nf_map` | `{"UNC": ["MME", "SMF"]}` |
| `first_release` | `UNC 20.0.0` |
| `requires_license` | 无 |
| `key_capabilities` | ① 单 APN 并发限制（ADD APNACTNUM）② 三维度并发：PDNNUM/IPV4ADDRNUM/IPV6ADDRNUM ③ 超限拒绝原因 PDNCONNREJCAUSE ④ 继承会话管理（C）的并发治理层 |
| `source_evidence_ids` | `EV-FK-03`, `EV-CA-01` |
| `status` | `active` |

#### WSFD-010400 用户数据管理

| 字段 | 值 |
|------|---|
| `feature_id` | `WSFD-010400` |
| `feature_name` | `用户数据管理` |
| `feature_summary` | UNC 侧用户签约数据管理，与 UDM/UDR/HSS 交互，提供 APN 签约、地址分配签约数据源，SUBSTORAG 存储分拆 |
| `feature_group` | `APN 基础` |
| `variant_dimensions` | `["数据源(UDM/UDR/HSS)", "存储分拆(SUBSTORAG)"]` |
| `applicable_nf_map` | `{"UNC": ["SGSN", "MME", "SMF", "AMF"]}` |
| `first_release` | `UNC 20.0.0` |
| `requires_license` | 无 |
| `key_capabilities` | ① 签约数据库定时器管理（SET SDBTMR）② 系统配置（SET SYS）③ SUBSTORAG 存储分拆 ④ UDM/UDR/HSS 签约数据交互 ⑤ 地址分配签约数据源 |
| `source_evidence_ids` | `EV-FK-04`, `EV-CA-01` |
| `status` | `active` |

#### WSFD-106203 别名 APN（★ 双视角语义反转特性）

| 字段 | 值 |
|------|---|
| `feature_id` | `WSFD-106203` |
| `feature_name` | `别名 APN` |
| `feature_summary` | 同特性 ID 在两套网元下映射方向相反、命令族命名不同、License 分离 —— SGSN/MME 侧（协商 APN→别名 APN，DNS 屏蔽）vs. GGSN/PGW-C/SMF 侧（别名 APN→真实 APN，资源归一） |
| `feature_group` | `APN 基础` |
| `variant_dimensions` | `["网元视角(SGSN-MME协商端 / GGSN-PGW-C-SMF归一端)", "匹配维度(IMSI号段 / 切片SST+SD)"]` |
| `applicable_nf_map` | `{"UNC": ["SGSN", "MME", "GGSN-C", "PGW-C", "SMF"]}` |
| `first_release` | `UNC 20.3.0` |
| `requires_license` | `LKV2ALIASAPN02`（SGSN/MME 侧）+ `LKV2AAPN01`（GGSN/PGW-C/SMF 侧） |
| `key_capabilities` | ① SGSN/MME 侧：ADD ALIASAPN（协商 APN→别名 APN，DNS 屏蔽，双条件 IMSI 号段 AND 协商 APN）② GGSN/PGW-C/SMF 侧：ADD APNALIAS（别名 APN→真实 APN，资源归一，5G 先按切片 SST+SD 查再按 ALL_USER）③ SET APNREPORTATTR 报告属性 ④ SET DEACTIVERATE 去活速率 |
| `source_evidence_ids` | `EV-FK-05`, `EV-CA-01` |
| `status` | `active` |

> **★ 双视角说明**（配置树修正核心）：variant_dimensions 第 1 维度"网元视角"区分两个语义反转的变体；双 License 并存；详见 `FR-APN-07`（见 §5）。

### 1.2 地址分配（18 个）

#### GWFD-010105 用户面地址分配

| 字段 | 值 |
|------|---|
| `feature_id` | `GWFD-010105` |
| `feature_name` | `用户面地址分配` |
| `feature_summary` | UDG 侧地址分配机制层，按 PFCP CHV4/CHV6 真值表执行分配（POOLTYPE=LOCAL），共享 SECTION→POOL→POOLGROUP→POOLGRPMAP 绑定链，是地址分配域辐射中心 |
| `feature_group` | `地址分配` |
| `variant_dimensions` | `["分配方式(用户面本地/SMF下发/Radius/DHCP)", "地址类型(IPv4/IPv6/双栈)", "POOLTYPE(LOCAL/EXTERNAL)"]` |
| `applicable_nf_map` | `{"UDG": ["SGW-U", "PGW-U", "UPF"]}` |
| `first_release` | `UDG 20.0.0` |
| `requires_license` | 无 |
| `key_capabilities` | ① CHV4/CHV6 真值表执行（1=用户面分配，0=外部分配）② POOLTYPE=LOCAL 地址池（★区别 UNC ADDRPOOL）③ SECTION→POOL→POOLGROUP→POOLBINDGROUP→POOLGRPMAP 标准绑定链 ④ SET IPALLOCRULE 全局三级规则（FIRSTRULE/SECONDRULE/THIRDRULE）⑤ SET APNIPALLOCRULE APN 级覆盖 ⑥ ADD CPNODEID（SMF NodeID）+ SET IPALLOCBYSMFSW 基于 SMF 分配 |
| `source_evidence_ids` | `EV-FK-06`, `EV-CA-01` |
| `status` | `active` |

#### GWFD-010104 地址分配方式（总览）

| 字段 | 值 |
|------|---|
| `feature_id` | `GWFD-010104` |
| `feature_name` | `地址分配方式(总览)` |
| `feature_summary` | UDG 侧地址分配方式总览特性（配置树补全），归纳 6×3 正交矩阵（分配来源×地址类型），本身无独立配置命令，为机制层提供分类视图 |
| `feature_group` | `地址分配` |
| `variant_dimensions` | `["分配来源(6类)", "地址类型(IPv4/IPv6/双栈)"]` |
| `applicable_nf_map` | `{"UDG": ["SGW-U", "PGW-U", "UPF"]}` |
| `first_release` | `UDG 20.0.0` |
| `requires_license` | 无 |
| `key_capabilities` | ① 6×3 正交矩阵（分配来源×地址类型）② 配置树补全总览 ③ 复用 010105 的 POOL/SECTION 绑定链 ④ OSPF/OSPFv3 路由发布（ADD OSPFIMPORTROUTE PROTOCOL=wlr） |
| `source_evidence_ids` | `EV-FK-07`, `EV-CA-01` |
| `status` | `active` |

#### GWFD-020421 基于位置的地址分配

| 字段 | 值 |
|------|---|
| `feature_id` | `GWFD-020421` |
| `feature_name` | `基于位置的地址分配` |
| `feature_summary` | UDG 侧基于 LAC/TAC 位置区的地址分配，按位置匹配不同地址池，支持 IPv4/IPv6 分别开关，需白名单（MSISDN）控制，License 82200BAK |
| `feature_group` | `地址分配` |
| `variant_dimensions` | `["位置维度(LAC/TAC/S1TAC/N2TAC)", "地址类型(IPv4/IPv6分别开关)", "白名单(MSISDN)"]` |
| `applicable_nf_map` | `{"UDG": ["PGW-U", "UPF"]}` |
| `first_release` | `UDG 20.5.0` |
| `requires_license` | `LKV3G5LBAA01` |
| `key_capabilities` | ① LACGROUP/LACID（2/3G 位置区）② TACGROUP/S1TACID/N2TACID（4/5G 位置区）③ SET IPALLOCBYLOCGLBSW 全局开关（IPv4/IPv6 分别）④ SET IPALLOCBYLOCSW 指定位置区覆盖 ⑤ ADD ADRLOCWHITELST 白名单（MSISDN）⑥ 复用 010105 POOL 绑定链 |
| `source_evidence_ids` | `EV-FK-08`, `EV-CA-01` |
| `status` | `active` |

#### GWFD-010108 用户面地址自动检测

| 字段 | 值 |
|------|---|
| `feature_id` | `GWFD-010108` |
| `feature_name` | `用户面地址自动检测` |
| `feature_summary` | UDG 侧地址探测可靠性检测（PING/DNS/Tracert），纯运维特性无 ADD 配置命令（仅 STR/STP/DSP PDNROUTETST 三条运维命令），与 L2TP 互斥 |
| `feature_group` | `地址分配` |
| `variant_dimensions` | `["检测方式(PING/DNS/Tracert)", "检测动作(STR启动/STP停止/DSP查询)"]` |
| `applicable_nf_map` | `{"UDG": ["PGW-U", "UPF"]}` |
| `first_release` | `UDG 20.3.0` |
| `requires_license` | 无 |
| `key_capabilities` | ① STR PDNROUTETST 启动检测 ② STP PDNROUTETST 停止检测 ③ DSP PDNTSTRESULT 查询结果 ④ PING/DNS/Tracert 三种检测方式 ⑤ 与 GWFD-020412 L2TP 互斥（FR-LOC-L2TP-EXCL、FR-L2TP-ADDRAUTO-EXCL） |
| `source_evidence_ids` | `EV-FK-09`, `EV-CA-01` |
| `status` | `active` |

#### GWFD-010107 静态地址用户路由冗余（U）

| 字段 | 值 |
|------|---|
| `feature_id` | `GWFD-010107` |
| `feature_name` | `静态地址用户路由冗余(U)` |
| `feature_summary` | UDG 侧静态地址用户主备冗余保护，主备 UDG 间经 GRE Tunnel 转发上行报文，ADDRPOOL/POOLGRPMAP 双使能 + SET REDUNDUSER 全局开关，与 WSFD-107021 对称同构 |
| `feature_group` | `地址分配` |
| `variant_dimensions` | `["角色(主UDG/备UDG)", "隧道类型(GRE)", "命令前缀(POOL，U侧)"]` |
| `applicable_nf_map` | `{"UDG": ["PGW-U", "UPF"]}` |
| `first_release` | `UDG 20.3.0` |
| `requires_license` | 无 |
| `key_capabilities` | ① ADD REDUNDRDTIP 虚拟 IP（重定向业务流到 GRE Tunnel）② SET REDUNDUSER 全局冗余开关（与 ADD POOL REDUNDFUNC 双使能）③ SET APNREDUNDUPSW 备用 UDG 上行隧道转发开关 ④ ADD OSPFINTERFACE 主备路由互通（COST/MED 优先级）⑤ ADD GRETUNNEL 主备 GRE Tunnel ⑥ 命令前缀 POOL（区别 UNC ADDRPOOL） |
| `source_evidence_ids` | `EV-FK-10`, `EV-CA-01` |
| `status` | `active` |

#### GWFD-020412 L2TP VPN（U，LAC 执行）

| 字段 | 值 |
|------|---|
| `feature_id` | `GWFD-020412` |
| `feature_name` | `L2TP VPN(U, LAC)` |
| `feature_summary` | UDG 侧 L2TP VPN，作 LAC 执行二层隧道封装+PPP 透传，SET APNL2TPATTR 是 U 面核心（10+ 参数），C 决策 U 执行模式的典型；License C-U 不对称（U 必须 82200BVC，C 无） |
| `feature_group` | `接入方式` |
| `variant_dimensions` | `["配置方式(本地L2TPGROUP / AAA下发L2TPRDSCLIENT)", "角色(LAC执行)", "C-U不对称(License仅U侧)"]` |
| `applicable_nf_map` | `{"UDG": ["PGW-U", "UPF"]}` |
| `first_release` | `UDG 20.3.0` |
| `requires_license` | `LKV3G5L2TP01` |
| `key_capabilities` | ① SET APNL2TPATTR（★U 面核心，10+ 参数，L2TPSWITCH/SUPPORTIPV6 等）② ADD L2TPGROUP+L2TPLNSINFO（本地配置 LNS 容器）③ ADD L2TPCLIENTIP/L2TPRDSCLIENT（源端 Giif 绑定，本地/AAA 两方式）④ SET GLOBALL2TP 缺省属性 ⑤ SET PPPCFG/APNPPPACCESS PPP 协商+鉴权 ⑥ SET L2TPN4KEY（U 侧 N4 加密）⑦ 不支持 PPP 用户/DHCP 延迟分配/IPv6 PD/NAT |
| `source_evidence_ids` | `EV-FK-11`, `EV-CA-01` |
| `status` | `active` |

> **★ 配置树修正说明**：① APNL2TPATTR（U，10+ 参数）≠ APNL2TPCTRL（C，2 参数），C 决策 U 执行典型不对称（见 `FR-APN-02`）；② C-U 不对称（License 仅 U 侧）；③ 与 GWFD-020421/010108 互斥（见 `FR-APN-05`、`FR-APN-06`）。

#### WSFD-010502 地址分配方式（C）

| 字段 | 值 |
|------|---|
| `feature_id` | `WSFD-010502` |
| `feature_name` | `地址分配方式(C)` |
| `feature_summary` | UNC 侧地址分配决策层，决策分配源（UDM/Radius/SMF/DHCP）经 PFCP 下发 UDG 执行，ADDRPOOL 体系（区别 UDG POOL），支持静态 IP 段绑定 UPF + 黑名单 |
| `feature_group` | `地址分配` |
| `variant_dimensions` | `["分配源(UDM静态/Radius/SMF/DHCP)", "命令前缀(ADDRPOOL，C侧)", "静态IP段绑定UPF"]` |
| `applicable_nf_map` | `{"UNC": ["GGSN-C", "PGW-C", "SMF"]}` |
| `first_release` | `UNC 20.0.0` |
| `requires_license` | 无 |
| `key_capabilities` | ① ADD ADDRPOOL（★UNC 侧，POOLTYPE 无 LOCAL，仅 UDM 静态）② ADD ADDRPOOLGRP/ADDRUPGROUP ③ ADD POOLBINDGRP/POOLBINDAPN（命名 GRP 非 GROUP）④ ADD POOLGRPMAP 池组映射 ⑤ ADD UPNODE（ADDRALLOCMODE=INHERIT）+ ADD UPFBINDGRP（PRIORITY）⑥ SET STATICADDRPARA 静态 IP 段绑定 UPF ⑦ ADD BLACKLIST 静态地址黑名单 ⑧ 共用 WSFD-107010 的 ADD UPNODE/PNFPROFILE（地址分配与网元选择耦合点） |
| `source_evidence_ids` | `EV-FK-12`, `EV-CA-01` |
| `status` | `active` |

#### WSFD-010504 控制面地址分配方式

| 字段 | 值 |
|------|---|
| `feature_id` | `WSFD-010504` |
| `feature_name` | `控制面地址分配方式` |
| `feature_summary` | UNC 侧控制面地址分配精细控制，补充 WSFD-010502，提供 SET IPALLOCRULE/ADDRESSATTR/SOFTPARA 全局规则与 SET IPALLOCBYLOCGLBSW 基于位置开关 |
| `feature_group` | `地址分配` |
| `variant_dimensions` | `["规则层级(全局/APN级)", "地址族(IPv4/IPv6)", "位置开关"]` |
| `applicable_nf_map` | `{"UNC": ["GGSN-C", "PGW-C", "SMF"]}` |
| `first_release` | `UNC 20.8.0` |
| `requires_license` | 无 |
| `key_capabilities` | ① SET IPALLOCRULE/SET APNIPALLOCRULE 地址分配规则（UNC 控制面侧）② SET ADDRESSATTR 地址属性 ③ SET SOFTPARA 软参 ④ SET IPALLOCBYLOCGLBSW 基于位置全局开关（UNC）⑤ SET APNADDRESSATTR APN 地址分配属性 ⑥ 复用 ADDRPOOL 绑定链 |
| `source_evidence_ids` | `EV-FK-13`, `EV-CA-01` |
| `status` | `active` |

#### WSFD-104410 L2TP VPN（C，决策）

| 字段 | 值 |
|------|---|
| `feature_id` | `WSFD-104410` |
| `feature_name` | `L2TP VPN(C, 决策)` |
| `feature_summary` | UNC 侧 L2TP VPN 决策面，SET APNL2TPCTRL 仅 2 参数（APN/L2TPSWITCH），决策 LNS 参数经 N4 下发 UDG 执行；C 决策 U 执行模式；无 License（C-U 不对称） |
| `feature_group` | `接入方式` |
| `variant_dimensions` | `["角色(决策端)", "参数量(仅2参数，vs U侧10+)", "C-U不对称(License仅U侧)"]` |
| `applicable_nf_map` | `{"UNC": ["GGSN-C", "PGW-C", "SMF"]}` |
| `first_release` | `UNC 20.3.0` |
| `requires_license` | 无（C-U 不对称，U 侧 GWFD-020412 需 License） |
| `key_capabilities` | ① SET APNL2TPCTRL（★C 面专用，仅 2 参数 APN/L2TPSWITCH）② SET L2TPKEY（C 侧 N4 加密，与 UDG L2TPN4KEY 相同）③ SET PFCPPVTEXT PFCP 私有扩展（下发 LNS 参数经 N4）④ ADD UPCMPT UP 控制面管理 ⑤ 无 License 要求 |
| `source_evidence_ids` | `EV-FK-14`, `EV-CA-01` |
| `status` | `active` |

#### WSFD-107021 静态地址用户路由冗余（C）

| 字段 | 值 |
|------|---|
| `feature_id` | `WSFD-107021` |
| `feature_name` | `静态地址用户路由冗余(C)` |
| `feature_summary` | UNC 侧静态地址用户冗余控制面，与 GWFD-010107 对称同构，两侧均配 ADDRPOOL/POOLGRPMAP + GRE Tunnel，命令前缀差异（U: POOL；C: ADDRPOOL） |
| `feature_group` | `地址分配` |
| `variant_dimensions` | `["角色(控制面决策)", "隧道类型(GRE)", "命令前缀(ADDRPOOL，C侧)"]` |
| `applicable_nf_map` | `{"UNC": ["PGW-C", "SMF"]}` |
| `first_release` | `UNC 20.3.0` |
| `requires_license` | 无 |
| `key_capabilities` | ① SET REDUNDUSER 全局冗余开关（UNC 侧）② ADD ADDRPOOL/POOLGRPMAP 地址池（UNC 命名）③ 与 GWFD-010107 对称同构 ④ 共用 ADD UPNODE/PNFPROFILE（地址分配与网元选择耦合） |
| `source_evidence_ids` | `EV-FK-15`, `EV-CA-01` |
| `status` | `active` |

#### GWFD-020403 IPv4v6 双栈接入（U，能力使能层）

| 字段 | 值 |
|------|---|
| `feature_id` | `GWFD-020403` |
| `feature_name` | `IPv4v6 双栈接入(U)` |
| `feature_summary` | UDG 侧双栈能力使能层（非父子、非包含），不替代 GWFD-010105 分配机制，而是使能其 IPv4v6 地址类型落地，是 010105 的"双栈特化版本"；IPv6 承载 License 串联链中间层 |
| `feature_group` | `地址分配` |
| `variant_dimensions` | `["能力层级(使能层，非机制层)", "地址类型(IPv4+IPv6并存)", "VPN双实例(IPv4+IPv6)"]` |
| `applicable_nf_map` | `{"UDG": ["PGW-U", "UPF"]}` |
| `first_release` | `UDG 20.1.0` |
| `requires_license` | `LKV3G5VDSA01` |
| `key_capabilities` | ① 双栈能力使能（License LKV3G5VDSA01）② ADD APN HASVPN+HASVPNIPV6 双 VPN 绑定 ③ 双池双段（IPv4 POOL + IPv6 POOL 并存）④ IPV4ALLOCPRIALG/IPV6ALLOCPRIALG 双优先级算法 ⑤ ADD VPNINSTAF AFTYPE=ipv6uni IPv6 地址族激活 ⑥ OSPF+OSPFv3 双进程路由发布 ⑦ RA 通告（UDG 主动下发，独有）⑧ V6PREFIXLENGTH=64 普通 IPv6 / <64 切换 PD 模式（020406） |
| `source_evidence_ids` | `EV-FK-16`, `EV-CA-01` |
| `status` | `active` |

> **★ 配置树修正说明**：① 双栈=能力使能层，非父子非包含，使能方向单向 020403→010105（见 `FR-APN-01`）；② IPv6 承载 License 串联链中间层（020401→020403→020406）。

#### WSFD-104002 IPv4v6 双栈接入（C）

| 字段 | 值 |
|------|---|
| `feature_id` | `WSFD-104002` |
| `feature_name` | `IPv4v6 双栈接入(C)` |
| `feature_summary` | UNC 侧双栈接入，与 GWFD-020403 对称，依赖 WSFD-104001 IPv6 承载（强依赖声明矛盾修正），ADDRPOOL 双池绑定 |
| `feature_group` | `地址分配` |
| `variant_dimensions` | `["能力层级(使能层)", "地址类型(IPv4+IPv6)", "接口(Gx/N7)"]` |
| `applicable_nf_map` | `{"UNC": ["GGSN-C", "PGW-C", "SMF"]}` |
| `first_release` | `UNC 20.5.0` |
| `requires_license` | 无（声明矛盾：强依赖 WSFD-104001） |
| `key_capabilities` | ① 双栈能力使能（UNC 侧）② ADD ADDRPOOL 双池（IPv4 + IPv6）③ ADD SMSUBDATA SM 子表（UNC IPv6 承载）④ SET SMFUNC/MOD GTPCCMPT SM 功能 ⑤ 强依赖 WSFD-104001（声明矛盾修正，忽略"不涉及"声明） |
| `source_evidence_ids` | `EV-FK-17`, `EV-CA-01` |
| `status` | `active` |

#### GWFD-020401 IPv6 承载上下文（U）

| 字段 | 值 |
|------|---|
| `feature_id` | `GWFD-020401` |
| `feature_name` | `IPv6 承载上下文(U)` |
| `feature_summary` | UDG 侧 IPv6 承载基础设施，提供 IPv6 路由广播透传（UNC 生成 RA），是 IPv6 承载 License 串联链起点（必装底座 LKV3G5V6PB01），被双栈和 PD 强依赖 |
| `feature_group` | `地址分配` |
| `variant_dimensions` | `["地址族(IPv6uni)", "路由协议(OSPFv3)", "RA通告来源(UNC生成，U透传)"]` |
| `applicable_nf_map` | `{"UDG": ["PGW-U", "UPF"]}` |
| `first_release` | `UDG 20.1.0` |
| `requires_license` | `LKV3G5V6PB01` |
| `key_capabilities` | ① IPv6 承载基础设施（License LKV3G5V6PB01，必装底座）② ADD VPNINSTAF AFTYPE=ipv6uni IPv6 地址族激活 ③ ADD OSPFV3/OSPFV3AREA/OSPFV3INTERFACE IPv6 OSPFv3 进程 ④ ADD OSPFV3IMPORTROUTE PROTOCOL=wlr 引入 WLR ⑤ ADD ROUTEPOLICY 路由策略 ⑥ 透传 UNC 生成的 RA（IPv6 路由广播） |
| `source_evidence_ids` | `EV-FK-18`, `EV-CA-01` |
| `status` | `active` |

#### WSFD-104001 IPv6 承载上下文（C）

| 字段 | 值 |
|------|---|
| `feature_id` | `WSFD-104001` |
| `feature_name` | `IPv6 承载上下文(C)` |
| `feature_summary` | UNC 侧 IPv6 承载决策+生成 RA，决策 IPv6 地址分配经 PFCP 下发 UDG 透传；强被依赖（WSFD-104002/104004 依赖），无独立 License |
| `feature_group` | `地址分配` |
| `variant_dimensions` | `["地址族(IPv6uni)", "RA生成(UNC生成，U透传)", "接口(Gx/N7)"]` |
| `applicable_nf_map` | `{"UNC": ["GGSN-C", "PGW-C", "SMF"]}` |
| `first_release` | `UNC 20.0.0` |
| `requires_license` | 无（强被依赖：WSFD-104002/104004 依赖） |
| `key_capabilities` | ① IPv6 承载决策（UNC 侧）② 生成 RA（Router Advertisement）③ ADD SMSUBDATA SM 子表 ④ SET SMFUNC SM 功能 ⑤ MOD GTPCCMPT GTP-C 控制 ⑥ 强被 WSFD-104002/104004 依赖（声明矛盾修正） |
| `source_evidence_ids` | `EV-FK-19`, `EV-CA-01` |
| `status` | `active` |

#### GWFD-020406 IPv6 Prefix Delegation（U）

| 字段 | 值 |
|------|---|
| `feature_id` | `GWFD-020406` |
| `feature_name` | `IPv6 Prefix Delegation(U)` |
| `feature_summary` | UDG 侧 IPv6 前缀代理，V6PREFIXLENGTH<64 触发 PD 模式（前缀代理给下级路由器），IPv6 承载 License 串联链终点，复用 010105 POOL 绑定链 |
| `feature_group` | `地址分配` |
| `variant_dimensions` | `["V6PREFIXLENGTH(<64=PD模式，64=普通IPv6)", "代理方向(下发给下级路由)", "触发条件(前缀长度)"]` |
| `applicable_nf_map` | `{"UDG": ["PGW-U", "UPF"]}` |
| `first_release` | `UDG 20.5.0` |
| `requires_license` | `LKV3G5P6PD01` |
| `key_capabilities` | ① IPv6 PD 前缀代理（License LKV3G5P6PD01）② V6PREFIXLENGTH<64 触发 PD 模式（★分水岭）③ ADD POOL/SECTION 复用 010105 绑定链 ④ ADD LACGROUP/LACID 位置区（与 020421 共用）⑤ ADD ADRLOCWHITELST 白名单 ⑥ ADD CPNODEID（SMF NodeID）+ SET IPALLOCBYSMFGLBSW 基于 SMF 分配 ⑦ ADD CONFLICTIP/CONFLICTIPV6 冲突地址标识 |
| `source_evidence_ids` | `EV-FK-20`, `EV-CA-01` |
| `status` | `active` |

#### WSFD-104004 IPv6 前缀代理（C）

| 字段 | 值 |
|------|---|
| `feature_id` | `WSFD-104004` |
| `feature_name` | `IPv6 前缀代理(C)` |
| `feature_summary` | UNC 侧 IPv6 前缀代理决策，决策前缀经 PFCP 下发 UDG 执行（PFCP 解耦），依赖 WSFD-104001（强依赖声明矛盾修正），License LKV3W9V6PD11 |
| `feature_group` | `地址分配` |
| `variant_dimensions` | `["前缀决策(UNC决策，U执行)", "PFCP解耦", "接口(Gx/N7)"]` |
| `applicable_nf_map` | `{"UNC": ["GGSN-C", "PGW-C", "SMF"]}` |
| `first_release` | `UNC 20.5.0` |
| `requires_license` | `LKV3W9V6PD11` |
| `key_capabilities` | ① IPv6 PD 前缀代理决策（License LKV3W9V6PD11）② PFCP 解耦下发 UDG 执行 ③ ADD SMSUBDATA SM 子表 ④ SET SMFUNC SM 功能 ⑤ 强依赖 WSFD-104001（声明矛盾修正）⑥ ADD ADDRPOOL/SECTION UNC 地址池 |
| `source_evidence_ids` | `EV-FK-21`, `EV-CA-01` |
| `status` | `active` |

#### WSFD-104413 DHCP 功能

| 字段 | 值 |
|------|---|
| `feature_id` | `WSFD-104413` |
| `feature_name` | `DHCP 功能` |
| `feature_summary` | UNC 侧 DHCPv4 地址分配（SMF 作 DHCP Client），经 DHCP 服务器获取地址，复用 ADDRPOOL 绑定链 |
| `feature_group` | `地址分配` |
| `variant_dimensions` | `["地址族(IPv4)", "角色(DHCP Client)", "分配源(DHCP服务器)"]` |
| `applicable_nf_map` | `{"UNC": ["GGSN-C", "PGW-C", "SMF"]}` |
| `first_release` | `UNC 20.5.0` |
| `requires_license` | 无 |
| `key_capabilities` | ① SMF 作 DHCP Client ② ADD DHCPSERVER/DHCPSERVERGRP DHCP 服务器+组 ③ ADD AGENTIP DHCP Agent IP ④ ADD DHCPBINDPOOLGRP DHCP 池组绑定 ⑤ SET DHCPPARAREQ DHCP 参数请求 ⑥ 复用 ADDRPOOL 绑定链 |
| `source_evidence_ids` | `EV-FK-22`, `EV-CA-01` |
| `status` | `active` |

#### WSFD-104005 DHCPv6 地址分配

| 字段 | 值 |
|------|---|
| `feature_id` | `WSFD-104005` |
| `feature_name` | `DHCPv6 地址分配` |
| `feature_summary` | UNC 侧 DHCPv6 地址分配，与 WSFD-104413 对称的 IPv6 版本，经 DHCPv6 服务器获取 IPv6 地址，复用 ADDRPOOL 绑定链 |
| `feature_group` | `地址分配` |
| `variant_dimensions` | `["地址族(IPv6)", "角色(DHCPv6 Client)", "分配源(DHCPv6服务器)"]` |
| `applicable_nf_map` | `{"UNC": ["GGSN-C", "PGW-C", "SMF"]}` |
| `first_release` | `UNC 20.5.0` |
| `requires_license` | 无 |
| `key_capabilities` | ① DHCPv6 Client ② ADD DHCPSERVER/DHCPSERVERGRP（IPv6）③ ADD AGENTIP DHCPv6 Agent IP ④ ADD DHCPBINDPOOLGRP DHCPv6 池组绑定 ⑤ SET DHCPPARAREQ DHCPv6 参数请求 ⑥ 复用 ADDRPOOL 绑定链 |
| `source_evidence_ids` | `EV-FK-23`, `EV-CA-01` |
| `status` | `active` |

#### WSFD-107010 UPF 选择（★ 双特性合一，跨组归属）

| 字段 | 值 |
|------|---|
| `feature_id` | `WSFD-107010` |
| `feature_name` | `UPF 选择` |
| `feature_summary` | UNC(SMF) 侧为 PDU 会话选择 UPF，三轮筛选（第一轮必选 7 条件→第二轮优选策略→第三轮权重负载）；双 License；与地址分配耦合（共用 ADD UPNODE）；静态 IP 段绑定 UPF 冲突时 SMF 选择优先 |
| `feature_group` | `网元选择` |
| `variant_dimensions` | `["代际(5G UPF / 4G SGW-U)", "筛选轮次(必选/优选/权重)", "切片支持(SST+SD，4G不用)"]` |
| `applicable_nf_map` | `{"UNC": ["SMF"]}` |
| `first_release` | `UNC 20.0.0` |
| `requires_license` | `LKV2USBL01` + `LKV2GWUS01`（双 License） |
| `key_capabilities` | ① 第一轮必选 7 条件（PNFDNN/PNFNS/PNFDNAI/PNFUPFINFO/UPNODE/UPAREA/UPBINDS11+GNGP）② 第二轮优选（SET UPSELECTPRI/UPSELECTFLAG/APNUPSELPLY）③ 第三轮权重负载（SET UPLOADBALANCE）④ 4G 接入 PNFNSINDEX=0（不用切片）⑤ SMF 和 UPF 必须同厂商（FR-APF-同厂商约束）⑥ 静态 IP 段绑定 UPF 冲突时 SMF 选择优先（FR-SMF主锚点优先） |
| `source_evidence_ids` | `EV-FK-34`, `EV-CA-01` |
| `status` | `active` |

> **★ 双特性合一说明**（配置树修正核心）：WSFD-107010 在特性 ID 层面合一，但 variant_dimensions 第 1 维度"代际"清晰区分 5G UPF 选择和 4G SGW-U 选择两个变体；次要归属地址分配（`cross_group`）；与 WSFD-010502 单向引用（`interacts_with`，冲突协调 FR-SMF主锚点优先）。

#### WSFD-010202 基于位置区域对等网元选择

| 字段 | 值 |
|------|---|
| `feature_id` | `WSFD-010202` |
| `feature_name` | `基于位置区域对等网元选择` |
| `feature_summary` | UNC 侧 Pre-5G 对等网元选择（SGSN/MME/MSC），基于 LAC/RAC/TAC 位置区域 + DNS 域名聚合，与 WSFD-107010 代际互补（2/3/4G） |
| `feature_group` | `网元选择` |
| `variant_dimensions` | `["代际(2/3/4G)", "位置维度(LAC/RAC/TAC)", "DNS聚合(ZONESW)"]` |
| `applicable_nf_map` | `{"UNC": ["SGSN", "MME", "MSC"]}` |
| `first_release` | `UNC 20.3.0` |
| `requires_license` | 无 |
| `key_capabilities` | ① ADD AREADNS 位置区域 DNS 域名定制（LAC/RAC/TAC + ZONESW）② ADD DNSN/IPV4DNSH/SGSNDNS DNS 配置 ③ SET MSCSELPLCY MSC 选择策略（SRVCC 基于 RAI/LAI FQDN）④ 与 WSFD-107010 代际互补（Pre-5G） |
| `source_evidence_ids` | `EV-FK-35`, `EV-CA-01` |
| `status` | `active` |

### 1.3 鉴权计费（5 个）

#### WSFD-011305 Radius 鉴权接入

| 字段 | 值 |
|------|---|
| `feature_id` | `WSFD-011305` |
| `feature_name` | `Radius 鉴权接入` |
| `feature_summary` | UNC 侧 Radius 鉴权接入，SET APNAUTHATTR ACCESSMODE 4 种取值（透明接入/透明鉴权/非透明接入/本地鉴权），仅 TRANS_AUTH/NON_TRANS 强依赖 Radius 功能 |
| `feature_group` | `鉴权计费` |
| `variant_dimensions` | `["ACCESSMODE(TRANS_NON_AUTH/TRANS_AUTH/NON_TRANS/LOC_AUTH)", "Radius依赖(仅TRANS_AUTH/NON_TRANS)"]` |
| `applicable_nf_map` | `{"UNC": ["GGSN-C", "PGW-C", "SMF"]}` |
| `first_release` | `UNC 20.3.2` |
| `requires_license` | 无（强依赖 WSFD-011306 Radius 功能） |
| `key_capabilities` | ① SET APNAUTHATTR APN 鉴权属性（ACCESSMODE 4 种取值）② 透明接入 TRANS_NON_AUTH（不调 Radius）③ 透明鉴权 TRANS_AUTH（共用账号，调 Radius）④ 非透明接入 NON_TRANS（调 Radius）⑤ 本地鉴权 LOC_AUTH（不调 Radius）⑥ 共用 WSFD-010301 的 APNAUTHATTR ⑦ 强依赖 WSFD-011306（仅 TRANS_AUTH/NON_TRANS） |
| `source_evidence_ids` | `EV-FK-24`, `EV-CA-01` |
| `status` | `active` |

#### WSFD-011306 Radius 功能

| 字段 | 值 |
|------|---|
| `feature_id` | `WSFD-011306` |
| `feature_name` | `Radius 功能` |
| `feature_summary` | UNC 侧 Radius 协议承载（PAP/CHAP、服务器组、Bypass），是鉴权级联链起点，被 011305/011307/108007 强依赖；共享 RDSSVRGRP 配置对象 |
| `feature_group` | `鉴权计费` |
| `variant_dimensions` | `["协议(PAP/CHAP)", "Bypass(故障一键放通)", "计费控制(SRVTRIGGER)"]` |
| `applicable_nf_map` | `{"UNC": ["GGSN-C", "PGW-C", "SMF"]}` |
| `first_release` | `UNC 20.0.0` |
| `requires_license` | 无 |
| `key_capabilities` | ① ADD RDSSVRGRP/RDSSVR Radius 服务器组+服务器（鉴权级联核心）② ADD APNRDSSVRGRP APN↔Radius 绑定 ③ ADD APNRDSCLIENTIP APN Radius Client IP ④ SET APNRDSACCTCTRL Radius 计费控制（SRVTRIGGER/SUPPORTACCTRSP）⑤ SET APNRADIUSATTR Radius 域名增加/剥离 ⑥ SET RDSRSPADDRCHK 响应端口检查 ⑦ ADD UPLIST4RDS PGW-U/UPF List ⑧ SET FHBYPASS 故障一键放通（优先级最高）⑨ SRV_TRIGGER 场景复用 PCC 规则体系 |
| `source_evidence_ids` | `EV-FK-25`, `EV-CA-01` |
| `status` | `active` |

#### WSFD-010301 鉴权功能（AKA）

| 字段 | 值 |
|------|---|
| `feature_id` | `WSFD-010301` |
| `feature_name` | `鉴权功能(AKA)` |
| `feature_summary` | UNC 侧基础 AKA 鉴权（2G/3G/4G/5G），鉴权加密参数管理，是卡类型控制（WSFD-106003 子特性 B）的前置依赖；两套鉴权并列（AKA vs Radius） |
| `feature_group` | `鉴权计费` |
| `variant_dimensions` | `["代际(2G GBAUTHCIPH / 3G IUAUTHCIPH / 4G S1USRSECPARA / 5G NGUSRSECPARA)", "鉴权体系(AKA，并列于Radius)"]` |
| `applicable_nf_map` | `{"UNC": ["SGSN", "MME", "AMF"]}` |
| `first_release` | `UNC 20.0.0` |
| `requires_license` | 无 |
| `key_capabilities` | ① ADD GBAUTHCIPH（2G 鉴权加密）② ADD IUAUTHCIPH（3G 鉴权加密）③ ADD S1USRSECPARA（4G 鉴权加密）④ ADD NGUSRSECPARA（5G 鉴权加密）⑤ MOD AMDATA AM 数据修改 ⑥ DSP COMMTX 通信上下文查询 ⑦ 通过鉴权三元组/五元组区分 SIM/USIM（卡类型控制前置） |
| `source_evidence_ids` | `EV-FK-26`, `EV-CA-01` |
| `status` | `active` |

#### WSFD-108007 终端二次鉴权

| 字段 | 值 |
|------|---|
| `feature_id` | `WSFD-108007` |
| `feature_name` | `终端二次鉴权` |
| `feature_summary` | UNC 侧企业 DN-AAA 场景二次鉴权，经 UPF N4 GTP-U 隧道转接 DN-AAA，License 82200DSF；强依赖 WSFD-011305/011306；不支持 EAP/Diameter，仅 PAP/CHAP via Radius |
| `feature_group` | `鉴权计费` |
| `variant_dimensions` | `["AAA位置(DN-AAA经UPF中转)", "协议(仅PAP/CHAP via Radius，不支持EAP/Diameter)", "场景(企业DN)"]` |
| `applicable_nf_map` | `{"UNC": ["SMF"]}` |
| `first_release` | `UNC 20.8.0` |
| `requires_license` | `LKV2SECAA01` |
| `key_capabilities` | ① License LKV2SECAA01（82200DSF）② ADD NETWORKINSTVPNMAP UPF VPN 前置（★必须先于 UPFRDSSVR/CLIENTIP）③ ADD CPGTPUADDR SMF 下发 GTP-U 地址（分装 GTPU 报文）④ ADD UPLIST4RDS UP List（按主锚点 UPF 发送 AAA）⑤ ADD RDSUPFCTRL Radius UPF 控制（PREFERENCE/LOCKED）⑥ ADD UPFRDSSVR UPF Radius 服务器（DN-AAA，★必须先于 CLIENTIP）⑦ ADD UPFRDSCLIENTIP UPF Radius 客户端 IP（★必须最后，执行后立即触发建链）⑧ 直连 AAA 与经 UPF 中转 AAA 的 Radius Server IP 不可相同 |
| `source_evidence_ids` | `EV-FK-27`, `EV-CA-01` |
| `status` | `active` |

#### WSFD-011307 Radius 抄送功能

| 字段 | 值 |
|------|---|
| `feature_id` | `WSFD-011307` |
| `feature_name` | `Radius 抄送功能` |
| `feature_summary` | UNC 侧 Radius 鉴权/计费消息并行抄送给第三方，与 011305/011306 共享配置对象（RDSSVRGRP），PRIFLAG=CARBON_COPY 标识抄送服务器组；声明独立但功能强关联 |
| `feature_group` | `鉴权计费` |
| `variant_dimensions` | `["抄送类型(鉴权/计费)", "标识(PRIFLAG=CARBON_COPY)", "关系(parallel_extends，共享配置对象)"]` |
| `applicable_nf_map` | `{"UNC": ["GGSN-C", "PGW-C", "SMF"]}` |
| `first_release` | `UNC 20.3.2` |
| `requires_license` | 无 |
| `key_capabilities` | ① 共享 RDSSVRGRP（复用 011306 R2）② ADD APNRDSSVRGRP PRIFLAG=CARBON_COPY 抄送服务器组 ③ 共享 ADD UPLIST4RDS ④ 与 011305/011306 声明独立但配置对象共享（parallel_extends） |
| `source_evidence_ids` | `EV-FK-28`, `EV-CA-01` |
| `status` | `active` |

### 1.4 接入方式（4 隧道，5 个）

#### IPFD-015002 GRE（★ U+C 对称同构共享特性）

| 字段 | 值 |
|------|---|
| `feature_id` | `IPFD-015002` |
| `feature_name` | `GRE(U+C)` |
| `feature_summary` | GRE 隧道共享特性（UDG+UNC 两产品均部署同名特性），三层轻量封装（IP 协议号 47）不加密，对称同构；与 IPSec 源地址互斥；可 GRE over IPSec 弥补 IPSec 不支持组播 |
| `feature_group` | `接入方式` |
| `variant_dimensions` | `["产品部署(UDG+UNC同构对称)", "封装层次(三层)", "加密(否)", "嵌套(GRE over IPSec)"]` |
| `applicable_nf_map` | `{"UDG": ["SGW-U", "PGW-U", "UPF"], "UNC": ["SGSN", "MME", "SGW-C"]}` |
| `first_release` | `UDG+UNC 20.0.0` |
| `requires_license` | 无 |
| `key_capabilities` | ① ADD GRETUNNEL（TNLTYPE=gre，★核心）② ADD INTERFACE Tunnel 接口 + ADD IFIPV4ADDRESS ③ ADD SRROUTE/SRROUTE6 静态路由（引导流量进 Tunnel）④ LoopBack 接口（推荐隧道源）⑤ MOD GRETUNNEL 可选：Checksum/Key/Keepalive ⑥ GRE over IPSec 场景（弥补 IPSec 不支持组播）⑦ ★硬约束：GRE 隧道源地址不能与 IPSec 隧道源地址相同（FR-GRE-IPSEC-SRC-EXCL） |
| `source_evidence_ids` | `EV-FK-29`, `EV-CA-01` |
| `status` | `active` |

#### IPFD-015004 IPSec 功能（UDG）

| 字段 | 值 |
|------|---|
| `feature_id` | `IPFD-015004` |
| `feature_name` | `IPSec 功能(UDG)` |
| `feature_summary` | UDG 侧 IPSec 隧道（加密+认证），三层 AH(51)/ESP(50)+IKE，VNRS 微服务+IPsec 微服务双配镜像，对称同构（与 IPFD-016000） |
| `feature_group` | `接入方式` |
| `variant_dimensions` | `["产品(UDG)", "封装层次(三层)", "加密(ESP)", "微服务(VNRS+IPsec双配镜像)"]` |
| `applicable_nf_map` | `{"UDG": ["SGW-U", "PGW-U", "UPF"]}` |
| `first_release` | `UDG 20.0.0` |
| `requires_license` | 无 |
| `key_capabilities` | ① ADD IPSECPROPOSALIPSEC 安全提议（ENCAPSULATIONMODE/SECURITYPROTOCOL=ESP）② ADD IKEPROPOSAL/IKEPEER IKE 提议+对等体（★DH 组不能为 None）③ ADD IPSECPOLICY 安全策略（聚合 ACL+Proposal+IKE Peer）④ ADD ACLGROUPIPSEC/ACLRULEADV4IPSEC ACL 规则（仅源/目的 IP）⑤ IPsec 微服务镜像配置（L3VPNINSTIPSEC/INTERFACEIPSEC 等）⑥ ADD IPSECINTFCFGIPSEC 应用策略到 Tunnel ⑦ SET IKEGLOBALCONFIG DPD+NAT 保活 ⑧ 默认 IKEv2（IKEv1 需 MOD IKEPEER VERSION1=FALSE）⑨ 与 IPFD-015002 源地址互斥（FR-GRE-IPSEC-SRC-EXCL） |
| `source_evidence_ids` | `EV-FK-30`, `EV-CA-01` |
| `status` | `active` |

#### IPFD-016000 IPSec 功能（UNC）

| 字段 | 值 |
|------|---|
| `feature_id` | `IPFD-016000` |
| `feature_name` | `IPSec 功能(UNC)` |
| `feature_summary` | UNC 侧 IPSec 隧道，与 IPFD-015004 对称同构（同命令族同参数），UDG+UNC 对称部署 |
| `feature_group` | `接入方式` |
| `variant_dimensions` | `["产品(UNC)", "封装层次(三层)", "加密(ESP)", "微服务(VNRS+IPsec双配镜像)"]` |
| `applicable_nf_map` | `{"UNC": ["SGSN", "MME", "SGW-C"]}` |
| `first_release` | `UNC 20.0.0` |
| `requires_license` | 无 |
| `key_capabilities` | ① 与 IPFD-015004 命令族完全对称（IPSECPROPOSALIPSEC/IKEPROPOSAL/IKEPEER/IPSECPOLICY/ACL 等）② VNRS 微服务+IPsec 微服务双配镜像 ③ 对称同构部署 ④ ★DH 组不能为 None ⑤ NAT 穿越仅 ESP 隧道模式 ⑥ ACL 仅支持源/目的 IP 不支持端口 |
| `source_evidence_ids` | `EV-FK-31`, `EV-CA-01` |
| `status` | `active` |

#### GWFD-020411 MPLS VPN（U）

| 字段 | 值 |
|------|---|
| `feature_id` | `GWFD-020411` |
| `feature_name` | `MPLS VPN(U)` |
| `feature_summary` | UDG 侧 MPLS L3VPN 隧道，MPLS 标签（I-L+O-L）不加密，对称同构（与 WSFD-104411）；文档缺口：9 篇无 MML 脚本，需命令字典补全 VPNINSTANCE/BGPVPNV4 系列 |
| `feature_group` | `接入方式` |
| `variant_dimensions` | `["产品(UDG)", "封装层次(三层 L3VPN)", "加密(否)", "核心(VPN实例+RD+VPN Target+MP-BGP)"]` |
| `applicable_nf_map` | `{"UDG": ["PE"]}` |
| `first_release` | `UDG 20.2.0` |
| `requires_license` | 必须（编号待补） |
| `key_capabilities` | ① MPLS L3VPN 隧道（三层）② MPLS 标签（I-L+O-L）不加密 ③ ADD VPNINSTANCE VPN 实例（VRF）+ RD + VPN Target（★推导，文档缺口）④ ADD BGPVPNV4ROUTETARGET/BGPVPNV4PEER MP-BGP（★推导，需命令字典补全）⑤ 隐性依赖 IGP/MPLS/BGP 基础（explicit 无交互，implicit_depends_on）⑥ 9 篇文档无 MML 脚本（待补全） |
| `source_evidence_ids` | `EV-FK-32`, `EV-CA-01` |
| `status` | `active` |

#### WSFD-104411 MPLS VPN（C）

| 字段 | 值 |
|------|---|
| `feature_id` | `WSFD-104411` |
| `feature_name` | `MPLS VPN(C)` |
| `feature_summary` | UNC 侧 MPLS L3VPN 隧道，与 GWFD-020411 对称同构，License 81203325 LKV2MPVPN01 |
| `feature_group` | `接入方式` |
| `variant_dimensions` | `["产品(UNC)", "封装层次(三层 L3VPN)", "加密(否)", "核心(VPN实例+RD+VPN Target+MP-BGP)"]` |
| `applicable_nf_map` | `{"UNC": ["PE"]}` |
| `first_release` | `UNC 20.2.0` |
| `requires_license` | `LKV2MPVPN01` |
| `key_capabilities` | ① 与 GWFD-020411 对称同构 ② MPLS L3VPN 隧道（三层）③ License LKV2MPVPN01（81203325）④ VPN 实例+RD+VPN Target+MP-BGP（★推导，文档缺口） |
| `source_evidence_ids` | `EV-FK-33`, `EV-CA-01` |
| `status` | `active` |

### 1.5 接入控制（2 个，★ 非 C-U 对称）

#### GWFD-010151 接入控制（U 面带宽流控）

| 字段 | 值 |
|------|---|
| `feature_id` | `GWFD-010151` |
| `feature_name` | `接入控制(U)` |
| `feature_summary` | UDG 侧 APN 级带宽流控（CAR 直接丢弃 / SHAPE 缓存整形），上下行独立配置，仅 APN 粒度（无法针对单用户）；与 WSFD-106003 非 C-U 对称（同名不同义） |
| `feature_group` | `接入控制` |
| `variant_dimensions` | `["流控动作(CAR直接丢弃 / SHAPE缓存整形)", "方向(上行/下行独立)", "粒度(仅APN级，无法单用户)"]` |
| `applicable_nf_map` | `{"UDG": ["SGW-U", "PGW-U", "UPF"]}` |
| `first_release` | `UDG 20.0.0` |
| `requires_license` | 无 |
| `key_capabilities` | ① SET APNQOSATTR（★接入控制核心，CARSHAPESWUL/DL + CARSHAPEUL/DL）② 上下行独立配置 ③ CAR 直接丢弃 / SHAPE 缓存整形可选 ④ 仅 APN 粒度（无法针对单用户）⑤ ADD/MOD/LST APN APN 管理 |
| `source_evidence_ids` | `EV-FK-37`, `EV-CA-01` |
| `status` | `active` |

> **★ 非 C-U 对称说明**（配置树修正核心）：GWFD-010151（U 侧带宽流控）与 WSFD-106003（C 侧接入权限）机制完全不同，非同一控制目标的 C-U 分工。variant_dimensions 第 1 维度"流控动作"与 WSFD-106003 第 1 维度"控制目标"清晰区分；不建 `c_u_symmetric` 边（见 `FR-APN-03`）。

#### WSFD-106003 用户接入控制功能（C，★ 双特性合一）

| 字段 | 值 |
|------|---|
| `feature_id` | `WSFD-106003` |
| `feature_name` | `用户接入控制功能(C)` |
| `feature_summary` | UNC 侧用户接入权限控制（非带宽流控），双特性合一：子特性 A（5GC AMF 移动性限制 NGMMSUBDATA）+ 子特性 B（2/3/4G ARD 签约 APN/卡类型权限）；与 GWFD-010151 非 C-U 对称 |
| `feature_group` | `接入控制` |
| `variant_dimensions` | `["控制目标(接入权限，非带宽)", "子特性(A:5GC移动性限制 / B:2-3-4G ARD权限)", "代际(2G GBARD/3G IUARD/4G S1ARD/5G NGMMSUBDATA)"]` |
| `applicable_nf_map` | `{"UNC": ["SGSN", "MME", "AMF"]}` |
| `first_release` | `UNC 20.0.0`（子特性 B v02 RedCap 20.11.0） |
| `requires_license` | 子特性 B：`LKV2ARD02`（子特性 A 无） |
| `key_capabilities` | ① 子特性 A：ADD NGMMSUBDATA 5GC 接入限制（AMF 侧移动性限制，RATRESTRICT/CORERESTRICT）+ SET NGMMPROCTRL ② 子特性 B：ADD GBARD/IUARD/S1ARD 2/3/4G ARD 接入限制（签约 APN/卡类型，License LKV2ARD02）③ 本地配置优先于签约 ④ 紧急注册跳过 ⑤ 卡类型控制强依赖 WSFD-010301 鉴权（通过鉴权三元组/五元组区分 SIM/USIM） |
| `source_evidence_ids` | `EV-FK-36`, `EV-CA-01` |
| `status` | `active` |

> **★ 双特性合一说明**（配置树修正核心）：WSFD-106003 在特性 ID 层面合一，但 variant_dimensions 第 2 维度"子特性"清晰区分 A（5GC 移动性限制）和 B（2/3/4G ARD 权限）两个独立变体；License 仅子特性 B 需要；与 GWFD-010151 非 C-U 对称（见 `FR-APN-03`）。

---

## 2. Feature depends_on 关系边（35 条）

> **Schema 参考**：§9.8 `Feature depends_on Feature`。依赖类型遵循 cross-feature-analysis §4.1-§4.3（含 8 对依赖声明矛盾的修正建模）。

### 2.1 会话管理底座 + 地址分配机制层（10 条）

| 源 Feature | 关系 | 目标 Feature | 依赖类型 | 依赖理由 |
|-----------|------|-------------|----------|----------|
| GWFD-010105 (用户面地址分配) | `depends_on` | GWFD-010101 (会话管理 U) | flow_depends_on | PDU/PDN 会话宿主流程承载地址分配 |
| GWFD-010104 (地址分配总览) | `depends_on` | GWFD-010105 (用户面地址分配) | capability_enables | 总览归纳机制层的分类视图 |
| GWFD-020421 (基于位置) | `depends_on` | GWFD-010105 (用户面地址分配) | capability_enables | 复用 POOL 绑定链 + 位置维度扩展 |
| GWFD-020421 (基于位置) | `depends_on` | GWFD-010107 (静态冗余) | interacts_with | 共用 ADDRPOOL/POOLGRPMAP |
| GWFD-010108 (地址自动检测) | `depends_on` | GWFD-010105 (用户面地址分配) | optional | 检测对象是 010105 分配的地址 |
| GWFD-010107 (静态冗余 U) | `depends_on` | GWFD-010105 (用户面地址分配) | capability_enables | 静态地址用户复用 POOL 绑定链 |
| WSFD-010502 (地址分配 C) | `depends_on` | WSFD-010501 (会话管理 C) | flow_depends_on | PDU/PDN 会话宿主流程承载地址分配 |
| WSFD-010504 (控制面地址分配) | `depends_on` | WSFD-010502 (地址分配 C) | capability_enables | 精细控制补充 010502 |
| WSFD-010504 (控制面地址分配) | `depends_on` | WSFD-010400 (用户数据管理) | flow_depends_on | 签约数据源 |
| WSFD-010503 (多 PDN/PDU) | `depends_on` | WSFD-010501 (会话管理 C) | inherits + extends | 并发治理层继承会话管理 |

### 2.2 IPv6 承载 License 串联链（8 条）

| 源 Feature | 关系 | 目标 Feature | 依赖类型 | 依赖理由 |
|-----------|------|-------------|----------|----------|
| GWFD-020403 (双栈 U) | `depends_on` | GWFD-020401 (IPv6 承载 U) | strong_depends_on | 双栈能力使能层依赖承载底座（License 串联链） |
| GWFD-020403 (双栈 U) | `depends_on` | GWFD-010105 (用户面地址分配) | capability_enables | 使能 010105 的 IPv4v6 地址类型落地（单向，非父子） |
| GWFD-020406 (IPv6 PD U) | `depends_on` | GWFD-020401 (IPv6 承载 U) | strong_depends_on | PD 依赖承载底座（License 串联链终点） |
| GWFD-020406 (IPv6 PD U) | `depends_on` | GWFD-020403 (双栈 U) | strong_depends_on | PD 依赖双栈能力（License 串联链） |
| GWFD-020406 (IPv6 PD U) | `depends_on` | GWFD-010105 (用户面地址分配) | capability_enables | 复用 POOL 绑定链 |
| WSFD-104002 (双栈 C) | `depends_on` | WSFD-104001 (IPv6 承载 C) | strong_depends_on | 声明矛盾修正：忽略"不涉及"，强依赖承载 |
| WSFD-104004 (IPv6 PD C) | `depends_on` | WSFD-104001 (IPv6 承载 C) | strong_depends_on | 声明矛盾修正：忽略"不涉及"，强依赖承载 |
| WSFD-104004 (IPv6 PD C) | `depends_on` | WSFD-104002 (双栈 C) | strong_depends_on | PD 依赖双栈（UNC 对称链） |

### 2.3 鉴权级联链（5 条）

| 源 Feature | 关系 | 目标 Feature | 依赖类型 | 依赖理由 |
|-----------|------|-------------|----------|----------|
| WSFD-011305 (Radius 鉴权接入) | `depends_on` | WSFD-011306 (Radius 功能) | strong_depends_on | 仅 TRANS_AUTH/NON_TRANS 强依赖 Radius 功能（共享 RDSSVRGRP） |
| WSFD-108007 (终端二次鉴权) | `depends_on` | WSFD-011306 (Radius 功能) | strong_depends_on | DN-AAA 经 UPF 转接，依赖 Radius 承载（共享 UPLIST4RDS） |
| WSFD-108007 (终端二次鉴权) | `depends_on` | WSFD-011305 (Radius 鉴权接入) | strong_depends_on | 二次鉴权是鉴权接入的扩展 |
| WSFD-011307 (Radius 抄送) | `depends_on` | WSFD-011306 (Radius 功能) | parallel_extends | 声明独立但共享配置对象 RDSSVRGRP |
| WSFD-011307 (Radius 抄送) | `depends_on` | WSFD-011305 (Radius 鉴权接入) | parallel_extends | 抄送鉴权消息（共享配置对象） |

### 2.4 接入控制 + AKA 鉴权（3 条）

| 源 Feature | 关系 | 目标 Feature | 依赖类型 | 依赖理由 |
|-----------|------|-------------|----------|----------|
| GWFD-010151 (接入控制 U) | `depends_on` | WSFD-106003 (接入控制 C) | interacts_with | 非 C-U 对称但同名协同（同名不同义，FR-APN-03 说明） |
| WSFD-106003 (接入控制 C, 子特性 B) | `depends_on` | WSFD-010301 (鉴权功能 AKA) | strong_depends_on | 卡类型控制前置：通过鉴权三元组/五元组区分 SIM/USIM（声明矛盾修正） |
| WSFD-011305 (Radius 鉴权接入) | `depends_on` | WSFD-010301 (鉴权功能 AKA) | interacts_with | 两套鉴权并列（AKA vs Radius），共用 APNAUTHATTR |

### 2.5 网元选择 + 地址分配耦合（2 条）

| 源 Feature | 关系 | 目标 Feature | 依赖类型 | 依赖理由 |
|-----------|------|-------------|----------|----------|
| WSFD-010502 (地址分配 C) | `depends_on` | WSFD-107010 (UPF 选择) | interacts_with | 单向引用；共用 ADD UPNODE；静态 IP 段绑定 UPF 冲突时 SMF 选择优先（FR-SMF主锚点优先） |
| WSFD-107021 (静态冗余 C) | `depends_on` | WSFD-010502 (地址分配 C) | capability_enables | 复用 ADDRPOOL 绑定链 |

### 2.6 隧道 + L2TP C 决策 U 执行（3 条）

| 源 Feature | 关系 | 目标 Feature | 依赖类型 | 依赖理由 |
|-----------|------|-------------|----------|----------|
| GWFD-020412 (L2TP U, LAC) | `depends_on` | WSFD-104410 (L2TP C, 决策) | strong_depends_on | C 决策 U 执行：UNC 决策 LNS 参数经 N4 下发，UDG 作 LAC 执行 |
| GWFD-020411 (MPLS U) | `depends_on` | WSFD-104411 (MPLS C) | interacts_with | 对称同构部署协同 |
| IPFD-015004 (IPSec UDG) | `depends_on` | IPFD-016000 (IPSec UNC) | interacts_with | 对称同构部署协同 |

### 2.7 C-U 协同对称同构（4 条）

| 源 Feature | 关系 | 目标 Feature | 依赖类型 | 依赖理由 |
|-----------|------|-------------|----------|----------|
| GWFD-010107 (静态冗余 U) | `depends_on` | WSFD-107021 (静态冗余 C) | c_u_symmetric | 对称同构（命令前缀差异 POOL vs ADDRPOOL） |
| GWFD-020401 (IPv6 承载 U) | `depends_on` | WSFD-104001 (IPv6 承载 C) | c_u_symmetric | 决策执行分离：UNC 决策+生成 RA，UDG 透传 |
| GWFD-020406 (IPv6 PD U) | `depends_on` | WSFD-104004 (IPv6 PD C) | c_u_symmetric | 决策执行分离：UNC 决策前缀，UDG 透传协商（PFCP 解耦） |
| GWFD-010105 (用户面地址分配) | `depends_on` | WSFD-010502 (地址分配 C) | c_u_symmetric | 决策执行分离：UNC 决策分配源，UDG 按 CHV4/CHV6 真值表执行 |

---

## 3. License 实例化（13 个：UDG 7 + UNC 6）

> **Schema 参考**：§9.5 License。`status` 均为 `active`。License 使能统一通过 `SET LICENSESWITCH:LICITEM="LKV...",SWITCH=ENABLE` 命令。

### 3.1 UDG 侧 License（7 个）

| `license_id` | `license_name` | License 编号 | 对应 Feature | `status` | 说明 |
|---------------|----------------|-------------|-------------|----------|------|
| `LKV3G5V6PB01` | IPv6 承载上下文 | 82209828 | GWFD-020401 | `active` | IPv6 承载基础设施底座（License 串联链起点，必装） |
| `LKV3G5VDSA01` | IPv4v6 双栈接入 | 82209829 | GWFD-020403 | `active` | 双栈能力使能层（串联链中间层） |
| `LKV3G5P6PD01` | IPv6 Prefix Delegation | 82200CKF | GWFD-020406 | `active` | IPv6 前缀代理（V6PREFIXLENGTH<64 触发，串联链终点） |
| `LKV3G5LBAA01` | 基于位置的地址分配 | 82200BAK | GWFD-020421 | `active` | 位置区地址分配（LAC/TAC） |
| `LKV3G5L2TP01` | L2TP VPN | 82200BVC | GWFD-020412 | `active` | L2TP LAC 执行（★ C-U 不对称：仅 U 侧需 License） |
| `LKV-MPLS-UDG` | MPLS VPN(UDG) | 编号待补 | GWFD-020411 | `active` | MPLS L3VPN（文档缺口，编号待补） |
| （IPv6 承载底座已含 LKV3G5V6PB01） | — | — | — | — | — |

### 3.2 UNC 侧 License（6 个）

| `license_id` | `license_name` | License 编号 | 对应 Feature | `status` | 说明 |
|---------------|----------------|-------------|-------------|----------|------|
| `LKV3W9V6PD11` | IPv6 前缀代理(UNC) | 82208006 | WSFD-104004 | `active` | UNC IPv6 PD 决策 |
| `LKV2MPVPN01` | MPLS VPN(UNC) | 81203325 | WSFD-104411 | `active` | UNC MPLS L3VPN |
| `LKV2SECAA01` | 终端二次鉴权 | 82200DSF | WSFD-108007 | `active` | DN-AAA 企业二次鉴权 |
| `LKV2ARD02` | 用户接入控制(子特性 B) | 82206571 | WSFD-106003（子特性 B） | `active` | 2/3/4G ARD 接入权限（子特性 A 无 License） |
| `LKV2USBL01` + `LKV2GWUS01` | UPF 选择（双 License） | 82209917 + 82200BES | WSFD-107010 | `active` | UPF 选择（双 License 必须同时开启） |
| `LKV2ALIASAPN02` + `LKV2AAPN01` | 别名 APN（双 License） | 82207546 + 82200BNM | WSFD-106203 | `active` | 双视角：SGSN/MME 侧 + GGSN/PGW-C/SMF 侧 |

### 3.3 License 依赖链（IPv6 承载串联链）

```
IPv6 承载 License 串联链（UDG 侧，地址分配域最长依赖路径）
├── LKV3G5V6PB01 (82209828, IPv6 承载底座，必装) → GWFD-020401
        │
        ▼
├── LKV3G5VDSA01 (82209829, 双栈能力使能层) → GWFD-020403
        │
        ▼
└── LKV3G5P6PD01 (82200CKF, IPv6 PD) → GWFD-020406
        │
        ▼ （UNC 侧对称）
└── LKV3W9V6PD11 (82208006, UNC PD) → WSFD-104004
```

> **来源**：GWFD-020403 §7.2、GWFD-020406 §1.4、《归纳-四维度决策与机制》§1.4

### 3.4 无需 License 的特性（24 个）

> 纯描述性底座（5）：GWFD-010101、WSFD-010501、WSFD-010503、WSFD-010400、WSFD-010301（AKA 基础鉴权）
> 地址分配机制层（8）：GWFD-010104、GWFD-010105、GWFD-010107、GWFD-010108、WSFD-010502、WSFD-010504、WSFD-107021、WSFD-104002
> Radius 三件套（3）：WSFD-011305、WSFD-011306、WSFD-011307
> GRE/IPSec（3）：IPFD-015002、IPFD-015004、IPFD-016000
> 接入控制 U 侧（1）：GWFD-010151
> 对等网元选择（1）：WSFD-010202
> DHCP（2）：WSFD-104413、WSFD-104005
> UNC IPv6 承载（1）：WSFD-104001（强被依赖，无独立 License）

---

## 4. License → Feature 映射（requires_license 边，13 条）

> **Schema 参考**：§9.8 `Feature requires_license License`。部分 Feature 双 License（WSFD-107010、WSFD-106203），按 License 计数 15 条边（13 Feature）。

| Feature | `requires_license` | 产品 | 说明 |
|---------|-------------------|------|------|
| GWFD-020401 | `LKV3G5V6PB01` | UDG | IPv6 承载底座 |
| GWFD-020403 | `LKV3G5VDSA01` | UDG | 双栈能力使能 |
| GWFD-020406 | `LKV3G5P6PD01` | UDG | IPv6 PD |
| GWFD-020421 | `LKV3G5LBAA01` | UDG | 基于位置 |
| GWFD-020412 | `LKV3G5L2TP01` | UDG | L2TP LAC（C-U 不对称） |
| GWFD-020411 | `LKV-MPLS-UDG` | UDG | MPLS VPN（编号待补） |
| WSFD-104004 | `LKV3W9V6PD11` | UNC | IPv6 PD |
| WSFD-104411 | `LKV2MPVPN01` | UNC | MPLS VPN |
| WSFD-108007 | `LKV2SECAA01` | UNC | 二次鉴权 |
| WSFD-106003（子特性 B） | `LKV2ARD02` | UNC | ARD 接入权限 |
| WSFD-107010 | `LKV2USBL01` + `LKV2GWUS01` | UNC | UPF 选择（双 License） |
| WSFD-106203（SGSN/MME 侧） | `LKV2ALIASAPN02` | UNC | 别名 APN 协商端 |
| WSFD-106203（GGSN/PGW-C/SMF 侧） | `LKV2AAPN01` | UNC | 别名 APN 归一端 |

---

## 5. FeatureRule（9 条，含 3 互斥 + 配置树修正）

> **Schema 参考**：§9.6 FeatureRule。`owner_ref_type` 均为 `feature`（本域所有 FeatureRule 均挂在 Feature 层级，无 SubFeature）。`rule_expression_mode`/`rule_source_kind`/`status`/`source_evidence_ids` 按 Schema §9.6 枚举与本域 EV-FK 编号约定（§0.4）补齐。
> **字段列说明**：下表已补齐 Schema §9.6 全部 5 个必选字段列 —— `owner_ref_type` / `rule_expression_mode` / `rule_source_kind` / `status` / `source_evidence_ids`。

| `rule_id` | `owner_ref_type` | 所属 Feature（owner_ref） | `rule_name` | `rule_type` | `rule_expression_mode` | `rule_source_kind` | `status` | `rule_logic` | `violation_effect` | `severity` | `source_evidence_ids` |
|-----------|------------------|---------------------------|-------------|-------------|------------------------|--------------------|----------|--------------|-------------------|------------|----------------------|
| `FR-APN-01` | `feature` | GWFD-020403 | 双栈能力使能层单向依赖 | `dependency_rule` | `explicit` | `design` | `active` | 双栈（020403）是能力使能层，非父子非包含，使能方向单向 020403→010105；不替代 010105 分配机制，而是使能其 IPv4v6 地址类型落地 | 若误建为父子包含关系，会导致 License 约束和 Feature 变体建模错误 | critical | `EV-FK-16` |
| `FR-APN-02` | `feature` | GWFD-020412 / WSFD-104410 | L2TP C 决策 U 执行不对称 | `naming_rule` | `explicit` | `config` | `active` | APNL2TPATTR（U 面，10+ 参数）≠ APNL2TPCTRL（C 面，仅 2 参数 APN/L2TPSWITCH）；UNC 决策 LNS 参数经 N4 下发，UDG 作 LAC 执行封装+PPP 透传；License C-U 不对称（U 必须 LKV3G5L2TP01，C 无） | 侧别配置错误或 License 遗漏将导致 L2TP 隧道无法建立 | critical | `EV-FK-11`, `EV-FK-14` |
| `FR-APN-03` | `feature` | GWFD-010151 / WSFD-106003 | 接入控制非 C-U 对称（同名不同义） | `restriction_rule` | `explicit` | `design` | `active` | GWFD-010151（U 面带宽流控 CAR/Shaping）与 WSFD-106003（C 面接入权限 ARD/APN/卡类型）机制完全不同，非同一控制目标的 C-U 分工；必须分别建模为两个独立 Feature 变体，不建 `c_u_symmetric` 边 | 若误建 C-U 对称，会导致配置对象混淆（APNQOSATTR vs GBARD/NGMMSUBDATA） | critical | `EV-FK-37`, `EV-FK-36` |
| `FR-APN-04` | `feature` | GWFD-010101 / WSFD-010501 | 会话管理纯描述性底座定位 | `scope_rule` | `explicit` | `principle` | `active` | 会话管理根底座（U+C）是纯描述性特性 —— 无独立 MML 配置命令（仅运维查询 DSP POOLUSAGE/DSP SESSIONINFO + 2/3G PDPAPN 维护）、无 License、无独立配置对象；PDU/PDN/PDP 会话由控制面 PFCP/GTP-C 信令被动触发；无 ConfigTask 直接关联 | 若误建为有独立配置命令的特性，会导致 ConfigTask 归属错误 | warning | `EV-FK-01`, `EV-FK-02` |
| `FR-APN-05` | `feature` | GWFD-020421 / GWFD-020412 | 位置↔L2TP 互斥 | `restriction_rule` | `explicit` | `restriction` | `active` | 基于位置的地址分配（020421）与 L2TP VPN（020412）不可同时应用 —— 地址分配主体不同（LNS 远程 vs 位置本地池）；互斥双向（FR-LOC-L2TP-EXCL） | 同时配置将导致地址分配冲突 | critical | `EV-FK-08`, `EV-FK-11` |
| `FR-APN-06` | `feature` | GWFD-020412 / GWFD-010108 | L2TP↔地址检测互斥 | `restriction_rule` | `explicit` | `restriction` | `active` | L2TP VPN（020412）与用户面地址自动检测（010108）不可同时应用（FR-L2TP-ADDRAUTO-EXCL） | 同时配置将导致检测干扰 L2TP 协商 | critical | `EV-FK-11`, `EV-FK-09` |
| `FR-APN-07` | `feature` | IPFD-015002 / IPFD-015004 | GRE↔IPSec 源地址互斥 | `validation_rule` | `explicit` | `restriction` | `active` | GRE 隧道源地址不能与 IPSec 隧道源地址相同（FR-GRE-IPSEC-SRC-EXCL）；GRE over IPSec 场景下两隧道源地址必须不同 | 源地址相同将导致隧道冲突，流量无法转发 | critical | `EV-FK-29`, `EV-FK-30` |
| `FR-APN-08` | `feature` | WSFD-106203 | 别名 APN 双视角语义反转 | `naming_rule` | `explicit` | `design` | `active` | WSFD-106203 同特性 ID 在两套网元下映射方向相反、命令族命名不同、License 分离 —— SGSN/MME 侧（协商 APN→别名 APN，ADD ALIASAPN，LKV2ALIASAPN02）vs. GGSN/PGW-C/SMF 侧（别名 APN→真实 APN，ADD APNALIAS，LKV2AAPN01）；建议拆分为两个 Feature 变体 | 若不区分视角，会导致映射方向错误，DNS 屏蔽或资源归一失效 | critical | `EV-FK-05` |
| `FR-APN-09` | `feature` | WSFD-107010 / WSFD-010502 | SMF 主锚点 UPF 选择优先 | `task_selection_rule` | `explicit` | `ops` | `active` | 静态 IP 段绑定 UPF（WSFD-010502 STATICADDRPARA）与 SMF 主锚点 UPF 选择（WSFD-107010）冲突时，SMF 选择优先（FR-SMF主锚点优先） | 冲突时静态绑定失效，按 SMF 选择执行 | warning | `EV-FK-34`, `EV-FK-12` |

---

## 6. FeatureTaskOrderEdge（核心 Feature 的 Task 展开顺序）

> **Schema 参考**：§9.7 FeatureTaskOrderEdge + §11.4。详细 Task 定义见 `03-task-graph.md`。
> **关系类型**：本场景所有 FTOE 均为 `precedes`（顺序执行），因 APN 配置链存在严格前后依赖。
> **说明**：SET LICENSESWITCH / SET REFRESHSRV 等内联命令步骤归入其所属 Task，不单独建边。
> **ID 前缀**：FTOE-APN-，顺序编号。
> **Task ID 占位**：T-xxx（纯数字，对齐访问限制 graph_parser；具体定义在 03-task-layer.md）。

### 6.1 GWFD-010105 用户面地址分配（UDG 侧配置链，6 条边）

| `edge_id` | `owner_ref_type` | `owner_ref` | `from_task_ref` | `to_task_ref` | `relation_type` | `source_evidence_ids` |
|-----------|-----------------|-------------|-----------------|---------------|-----------------|----------------------|
| `FTOE-APN-001` | `Feature` | `GWFD-010105` | `T-001` | `T-002` | `precedes` | `EV-FK-06, EV-CA-01` |
| `FTOE-APN-002` | `Feature` | `GWFD-010105` | `T-002` | `T-003` | `precedes` | `EV-FK-06, EV-CA-01` |
| `FTOE-APN-003` | `Feature` | `GWFD-010105` | `T-003` | `T-004` | `precedes` | `EV-FK-06, EV-CA-01` |
| `FTOE-APN-004` | `Feature` | `GWFD-010105` | `T-004` | `T-005` | `precedes` | `EV-FK-06, EV-CA-01` |
| `FTOE-APN-005` | `Feature` | `GWFD-010105` | `T-005` | `T-006` | `precedes` | `EV-FK-06, EV-CA-01` |
| `FTOE-APN-006` | `Feature` | `GWFD-010105` | `T-006` | `T-007` | `precedes` | `EV-FK-06, EV-CA-01` |

> **Task 说明**：T-001=VPN 实例准备, T-002=APN 配置, T-003=地址池配置（POOLTYPE=LOCAL）, T-004=池组映射, T-005=地址分配规则, T-006=下行路由发布（OSPF）, T-007=SET REFRESHSRV

### 6.2 GWFD-020403 IPv4v6 双栈（UDG 侧配置链，9 条边）

| `edge_id` | `owner_ref_type` | `owner_ref` | `from_task_ref` | `to_task_ref` | `relation_type` | `source_evidence_ids` |
|-----------|-----------------|-------------|-----------------|---------------|-----------------|----------------------|
| `FTOE-APN-007` | `Feature` | `GWFD-020403` | `T-101` | `T-102` | `precedes` | `EV-FK-16, EV-CA-01` |
| `FTOE-APN-008` | `Feature` | `GWFD-020403` | `T-102` | `T-103` | `precedes` | `EV-FK-16, EV-CA-01` |
| `FTOE-APN-009` | `Feature` | `GWFD-020403` | `T-103` | `T-104` | `precedes` | `EV-FK-16, EV-CA-01` |
| `FTOE-APN-010` | `Feature` | `GWFD-020403` | `T-104` | `T-105` | `precedes` | `EV-FK-16, EV-CA-01` |
| `FTOE-APN-011` | `Feature` | `GWFD-020403` | `T-105` | `T-106` | `precedes` | `EV-FK-16, EV-CA-01` |
| `FTOE-APN-012` | `Feature` | `GWFD-020403` | `T-106` | `T-107` | `precedes` | `EV-FK-16, EV-CA-01` |
| `FTOE-APN-013` | `Feature` | `GWFD-020403` | `T-107` | `T-108` | `precedes` | `EV-FK-16, EV-CA-01` |
| `FTOE-APN-014` | `Feature` | `GWFD-020403` | `T-108` | `T-109` | `precedes` | `EV-FK-16, EV-CA-01` |
| `FTOE-APN-015` | `Feature` | `GWFD-020403` | `T-109` | `T-007` | `precedes` | `EV-FK-16, EV-CA-01` |

> **Task 说明**：T-101=双 License 使能（V6PB01+VDSA01）, T-102=VPN 双实例（IPv4+IPv6, VPNINSTAF AFTYPE=ipv6uni）, T-103=双栈 APN（HASVPN+HASVPNIPV6）, T-104=双池双段（IPv4 POOL+IPv6 POOL）, T-105=双池绑定同组（双优先级算法）, T-106=APN 级双栈属性, T-107=池组映射, T-108=下行路由发布（OSPF+OSPFv3 双进程）, T-109=RA 通告（020403 独有）

### 6.3 GWFD-020412 L2TP VPN（UDG 侧 LAC 执行配置链，7 条边）

| `edge_id` | `owner_ref_type` | `owner_ref` | `from_task_ref` | `to_task_ref` | `relation_type` | `source_evidence_ids` |
|-----------|-----------------|-------------|-----------------|---------------|-----------------|----------------------|
| `FTOE-APN-016` | `Feature` | `GWFD-020412` | `T-201` | `T-202` | `precedes` | `EV-FK-11, EV-CA-01` |
| `FTOE-APN-017` | `Feature` | `GWFD-020412` | `T-202` | `T-203` | `precedes` | `EV-FK-11, EV-CA-01` |
| `FTOE-APN-018` | `Feature` | `GWFD-020412` | `T-203` | `T-204` | `precedes` | `EV-FK-11, EV-CA-01` |
| `FTOE-APN-019` | `Feature` | `GWFD-020412` | `T-204` | `T-205` | `precedes` | `EV-FK-11, EV-CA-01` |
| `FTOE-APN-020` | `Feature` | `GWFD-020412` | `T-205` | `T-206` | `precedes` | `EV-FK-11, EV-CA-01` |
| `FTOE-APN-021` | `Feature` | `GWFD-020412` | `T-206` | `T-207` | `precedes` | `EV-FK-11, EV-CA-01` |
| `FTOE-APN-022` | `Feature` | `GWFD-020412` | `T-207` | `T-208` | `precedes` | `EV-FK-11, EV-CA-01` |

> **Task 说明**：T-201=License 使能（LKV3G5L2TP01）, T-202=VPN+Giif 接口, T-203=SET APNL2TPATTR（★U 面核心 10+ 参数）, T-204=L2TP 组（本地配置方式 L2TPGROUP+L2TPLNSINFO）或 AAA 下发（L2TPRDSCLIENT）, T-205=L2TP 缺省属性+PPP 协商（GLOBALL2TP+PPPCFG）, T-206=N4 加密（SET L2TPN4KEY）, T-207=静态路由（ADD SRROUTE）, T-208=SET REFRESHSRV

### 6.4 WSFD-011305/011306 Radius 鉴权级联（UNC 侧配置链，6 条边）

| `edge_id` | `owner_ref_type` | `owner_ref` | `from_task_ref` | `to_task_ref` | `relation_type` | `source_evidence_ids` |
|-----------|-----------------|-------------|-----------------|---------------|-----------------|----------------------|
| `FTOE-APN-023` | `Feature` | `WSFD-011306` | `T-301` | `T-302` | `precedes` | `EV-FK-25, EV-CA-01` |
| `FTOE-APN-024` | `Feature` | `WSFD-011306` | `T-302` | `T-303` | `precedes` | `EV-FK-25, EV-CA-01` |
| `FTOE-APN-025` | `Feature` | `WSFD-011306` | `T-303` | `T-304` | `precedes` | `EV-FK-25, EV-CA-01` |
| `FTOE-APN-026` | `Feature` | `WSFD-011305` | `T-304` | `T-305` | `precedes` | `EV-FK-24, EV-CA-01` |
| `FTOE-APN-027` | `Feature` | `WSFD-011305` | `T-305` | `T-306` | `precedes` | `EV-FK-24, EV-CA-01` |
| `FTOE-APN-028` | `Feature` | `WSFD-011305` | `T-306` | `T-307` | `precedes` | `EV-FK-24, EV-CA-01` |

> **Task 说明**：T-301=VPN+Gi 接口（AAA VPN）, T-302=Radius 服务器组+服务器（RDSSVRGRP+RDSSVR）, T-303=APN 级 Radius 绑定（APNRDSSVRGRP+APNRDSCLIENTIP）, T-304=Radius 计费控制+域名（APNRDSACCTCTRL+APNRADIUSATTR）, T-305=APN 鉴权属性（SET APNAUTHATTR ACCESSMODE 4 种）, T-306=验证（LST APNAUTHATTR）, T-307=SET REFRESHSRV

### 6.5 WSFD-107010 UPF 选择（UNC 侧三轮筛选配置链，5 条边）

| `edge_id` | `owner_ref_type` | `owner_ref` | `from_task_ref` | `to_task_ref` | `relation_type` | `source_evidence_ids` |
|-----------|-----------------|-------------|-----------------|---------------|-----------------|----------------------|
| `FTOE-APN-029` | `Feature` | `WSFD-107010` | `T-401` | `T-402` | `precedes` | `EV-FK-34, EV-CA-01` |
| `FTOE-APN-030` | `Feature` | `WSFD-107010` | `T-402` | `T-403` | `precedes` | `EV-FK-34, EV-CA-01` |
| `FTOE-APN-031` | `Feature` | `WSFD-107010` | `T-403` | `T-404` | `precedes` | `EV-FK-34, EV-CA-01` |
| `FTOE-APN-032` | `Feature` | `WSFD-107010` | `T-404` | `T-405` | `precedes` | `EV-FK-34, EV-CA-01` |
| `FTOE-APN-033` | `Feature` | `WSFD-107010` | `T-405` | `T-406` | `precedes` | `EV-FK-34, EV-CA-01` |

> **Task 说明**：T-401=双 License 使能（LKV2USBL01+LKV2GWUS01）, T-402=第一轮必选 7 条件（PNFDNN/PNFNS/PNFDNAI/PNFUPFINFO/UPNODE/UPAREA/UPBINDS11+GNGP）, T-403=接口绑定（4G 互操作）, T-404=第二轮优选策略（UPSELECTPRI/UPSELECTFLAG/APNUPSELPLY）, T-405=第三轮权重负载（UPLOADBALANCE）, T-406=SET REFRESHSRV

### 6.6 WSFD-106003 接入控制（UNC 侧子特性 B ARD 配置链，3 条边）

| `edge_id` | `owner_ref_type` | `owner_ref` | `from_task_ref` | `to_task_ref` | `relation_type` | `source_evidence_ids` |
|-----------|-----------------|-------------|-----------------|---------------|-----------------|----------------------|
| `FTOE-APN-034` | `Feature` | `WSFD-106003` | `T-501` | `T-502` | `precedes` | `EV-FK-36, EV-CA-01` |
| `FTOE-APN-035` | `Feature` | `WSFD-106003` | `T-502` | `T-503` | `precedes` | `EV-FK-36, EV-CA-01` |
| `FTOE-APN-036` | `Feature` | `WSFD-106003` | `T-503` | `T-504` | `precedes` | `EV-FK-36, EV-CA-01` |

> **Task 说明**：T-501=License 使能（LKV2ARD02，子特性 B）+ 前置 WSFD-010301 鉴权, T-502=ARD 接入限制（GBARD 2G/IUARD 3G/S1ARD 4G）, T-503=5GC 移动性限制（NGMMSUBDATA，子特性 A，无 License）, T-504=SET REFRESHSRV

> **FTOE 统计**：6 个核心 Feature x 36 条顺序边。License 使能或 VPN 准备为起点，SET REFRESHSRV 为终点。

---

## 7. 关系边汇总

> **Schema 参考**：§9.8 特性图谱关系全集。

| 关系类型 | 数量 | 说明 |
|---------|------|------|
| `depends_on` | 35 | §2（会话管理底座 10 + IPv6 串联链 8 + 鉴权级联 5 + 接入控制 3 + 网元选择 2 + 隧道 3 + C-U 协同 4） |
| `requires_license` | 15 | §4（13 Feature，WSFD-107010/106203 双 License 各计 2 条边） |
| `constrained_by`（FeatureRule） | 9 | §5（FR-APN-01~FR-APN-09，含 3 互斥 + 4 配置树修正 + 2 命名/选择） |
| `task_order`（FeatureTaskOrderEdge） | 36 | §6（FTOE-APN-001~036，6 个核心 Feature） |
| `decomposes_to`（Feature→ConfigTask） | 37 | 见 `05-cross-layer-mapping.md`（每个 Feature 至少 1 个 ConfigTask，纯描述性底座除外） |
| `supported_by`（Feature→EvidenceSource） | 37 | 每个 Feature 由 EV-FK-01~37 + EV-CA-01 支撑 |
| `has_subfeature` | 0 | 本版未建 SubFeature（差异通过 variant_dimensions 表达，Schema §9.1 指引） |
| **特性层对象总计** | **37 Feature + 13 License + 9 FeatureRule + 36 FTOE** | — |

---

## 8. 与带宽控制场景特性图谱的对比

| 维度 | 带宽控制场景 | APN 业务域 |
|------|------------|-----------|
| Feature 数量 | 24（UDG 16 + UNC 8） | 37（UDG 16 + UNC 21） |
| 核心特性族 | BWM 三级控制体系（BWMSERVICE/BWMCONTROLLER/BWMUSERGROUP/BWMRULE） | 地址分配 6×3 正交矩阵 + 4 隧道 + IPv6 承载 License 串联链 |
| 独有 Feature | GWFD-110311/110312/110313/020354/020357/020358/020359/110301/110302/110331/110332/020305, WSFD-211005/109104/211009/109107/109102/109108/211101 | GWFD-010101/010104/010105/010107/010108/010151/020401/020403/020406/020411/020412/020421, IPFD-015002/015004/016000, WSFD-010202/010301/010400/010501/010502/010503/010504/011305/011306/011307/104001/104002/104004/104005/104410/104411/104413/106003/106203/107010/107021/108007 |
| 共享 Feature | GWFD-110101(SA-Basic), GWFD-020351/WSFD-109101(PCC) | 无（APN 域不依赖 SA-Basic/PCC，独立底座为会话管理） |
| License 数量 | 24（全部需 License） | 13（24 个无需 License） |
| 依赖链核心 | SA-Basic→PCC→BWM→[Shaping/FUP/QoS/ADC/无线优化] | 会话管理底座→地址分配机制层→[IPv6 串联链/Radius 级联/4 隧道] |
| 特性辐射中心 | SA-Basic（12 个依赖）+ PCC（22/24 依赖） | 会话管理底座（U+C，10 个依赖）+ IPv6 承载（8 个串联依赖）+ Radius 功能（5 个级联依赖） |
| 独有 FeatureRule | 5 条（BWM 层级+智能 Shaping 依赖+POLICYTYPE 侧别+FUP SA 依赖+URR 模式） | 9 条（双栈使能层单向+C 决策 U 执行+非 C-U 对称+底座描述性+3 互斥+别名双视角+SMF 优先） |
| C-U 配对 | 8 对 | 8 对（决策执行分离 5 + 对称同构 4 + 非对称 2） |
| Task 链复杂度 | 25 条 FTOE（5 个核心 Feature） | 36 条 FTOE（6 个核心 Feature） |

> 两场景特性图谱结构相似但领域不同：带宽控制是"控制机制"维度扩展（限速/整形/GBR/FUP/DSCP），APN 是"接入与会话管理"维度扩展（地址分配/鉴权/隧道/网元选择）。APN 域的纯描述性底座（会话管理）和配置树修正项（双栈使能层、C 决策 U 执行、非 C-U 对称、双特性合一、双视角反转）是 Stage 5 审查重点。

---

## 9. 对象计数汇总

| 对象类型 | 数量 | 编号范围 |
|---------|------|---------|
| Feature | 37 | UDG 16: GWFD-010101/010104/010105/010107/010108/010151/020401/020403/020406/020411/020412/020421 + IPFD-015002/015004；UNC 21: WSFD-010202/010301/010400/010501/010502/010503/010504/011305/011306/011307/104001/104002/104004/104005/104410/104411/104413/106003/106203/107010/107021/108007 + IPFD-016000 |
| License | 13 | UDG 7: LKV3G5V6PB01/VDSA01/P6PD01/LBAA01/L2TP01 + LKV-MPLS-UDG；UNC 6: LKV3W9V6PD11/LKV2MPVPN01/LKV2SECAA01/LKV2ARD02 + LKV2USBL01+LKV2GWUS01(双) + LKV2ALIASAPN02+LKV2AAPN01(双) |
| FeatureRule | 9 | FR-APN-01~FR-APN-09 |
| depends_on 边 | 35 | §2（会话底座 10 + IPv6 串联 8 + 鉴权级联 5 + 接入控制 3 + 网元选择 2 + 隧道 3 + C-U 协同 4） |
| requires_license 边 | 15 | §4（13 Feature，双 License 计 2 条边） |
| FTOE 边 | 36 | FTOE-APN-001~FTOE-APN-036（6 个核心 Feature） |
| **特性层对象总计** | **37 Feature + 13 License + 9 FeatureRule + 36 FTOE** | — |

---

> 本文件为 APN 业务域三层图谱第 2 层。第 1 层业务图谱见 `01-business-graph.md`，第 3 层任务原子层、第 4 层命令图谱、第 5 层跨层映射、第 6 层证据索引见同目录其他文件。
