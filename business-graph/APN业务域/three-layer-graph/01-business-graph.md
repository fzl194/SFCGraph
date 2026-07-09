# APN 业务域三层图谱 · 第1层：业务图谱（重建版 v2 · Phase 4）

> **★版本状态（2026-06-29）**：业务层重建版 v2 —— **9 个编造 ConfigurationSolution 收敛为 1 个 CS-APN-01（APN开通方案）**，业务结构以 `APN配置树.md`（EV-BS-02）为权威骨架。原 9 CS（智慧农业/工控/家庭CPE/VoLTE/企业AAA/DHCP迁移/L2TP-VPN/区域化运营/企业双栈）经审查确认**不在产品文档**（源自 SKILL 自撰意图澄清 EV-BS-01 + 自撰归纳 EV-TK-01/EV-CA-02，伪追溯），已删除。
> **文件定位**：`three-layer-graph/01-business-graph.md`
> **Schema 参考**：`三层图谱Schema-最终版-v0.1.md` §8 业务图谱（§8.3~§8.11 字段 + §8.12 关系）
> **本体参考**：`三层图谱本体标准定义.md`；**业务骨架**：`APN配置树.md`

---

## 0. 适用定义与来源（★权威重定位）

### 0.1 根定义
- `三层图谱本体标准定义.md` / `三层图谱Schema-最终版-v0.1.md`

### 0.2 APN 业务域知识来源（★权威重定位）
| 证据 | 角色 | 说明 |
|------|------|------|
| `APN配置树.md`（EV-BS-02） | **★业务结构权威** | APN 开通配置树（root/AND/OR/branch/leaf），CS/DP 骨架来源 |
| `feature-knowledge/*.md`（EV-FK-01~37）→ 产品文档 | **★内容权威** | 特性机制/参数/激活场景，源自 `output/UDG_*`、`output/UNC *` 产品文档 |
| `APN意图澄清知识库.md`（EV-BS-01） | reference（降级） | SKILL 意图澄清业务引导，**非事实源**，不作 CS 权威 |
| `topic-knowledge/Batch-14-业务场景方案.md`（EV-TK-01） | **deprecated（废弃）** | 9 编造场景归纳来源，**已不作 CS 权威** |
| `cross-topic-analysis.md`（EV-CA-02） | supporting（降级） | 自撰横向归纳，仅作 supporting，不作权威 |

> **★关键变更**：原业务层 9 CS 的 `source_evidence_ids: EV-TK-01, EV-CA-02` 为伪追溯（自撰归纳），本版 CS/DP/BR/SO 权威改为 **EV-BS-02（配置树）+ EV-FK-*（特性文档，源自产品文档）**。下文 §3~§5 行内仍保留 EV-CA-02 为 supporting 引用，但权威以 EV-BS-02/EV-FK-* 为准（证据层 Phase 5 全量重指产品文档）。

---

## 1. BusinessDomain + NetworkScenario

### 1.1 BusinessDomain

| 字段 | 值 |
|------|---|
| `domain_id` | `BD-APN-01` |
| `domain_name` | `接入与会话管理` |
| `domain_summary` | UE 从附着到 PDU/PDN 会话建立的完整接入链路：身份验证、接入权限判定、地址分配、网元选择、隧道接入、会话治理；APN/DNN 是业务接入的统一锚点 |
| `status` | `active` |
| `source_evidence_ids` | `EV-BS-02`, `EV-FK-01`, `EV-FK-02` |

> **★ 独立 BD**：APN（接入与会话管理）与"业务感知"（BD-CH-01/BD-BW-01）并列独立。两者通过 PDU 会话上下文（SO-APN-SESSION-CONTEXT）协同，根对象不重叠。

### 1.2 NetworkScenario

| 字段 | 值 |
|------|---|
| `scenario_id` | `NS-APN-01` |
| `scenario_name` | `APN 开通场景` |
| `scenario_summary` | UE 接入核心网并建立 PDU/PDN 会话的完整开通：按配置树 4 维度（地址分配 × 鉴权计费 × 接入方式 × 地址类型）决策组合，叠加 3 底座（会话管理 × 网元选择 × 接入控制）支撑 |
| `judgment_basis` | 需为 UE 分配 IP 地址并建立 PDU/PDN 会话；或需对接 Radius/DHCP/AAA；或需配置隧道（IPSec/GRE/MPLS/L2TP）接入企业 DN；或需按区域/双栈/并发维度治理 APN 接入 |
| `typical_outcome` | UE 获得 IPv4/IPv6/双栈地址，PDU 会话建立，按签约与策略接入目标网络 |
| `status` | `active` |
| `source_evidence_ids` | `EV-BS-02`, `EV-FK-01`, `EV-FK-02`, `EV-FK-06` |

#### 场景边界
**覆盖**：UDG（用户面）+ UNC（控制面）+ IPFD（隧道基础）；4 开通主线维度 + 3 底座支撑。
**不覆盖**：计费场景（BD-CH-01，差异化计费/配额）、带宽控制（BD-BW-01，限速/整形/FUP）、访问限制（URL 过滤/重定向）。

---

## 2. ConfigurationSolution（单一方案闭包，对标计费"机制闭包"）

> **★拆分依据**：`APN配置树.md`（EV-BS-02）—— APN 开通 root 下 `地址分配信息(OR) AND 鉴权计费信息(AND) AND 接入方式信息(OR)`，每维度由 DecisionPoint 选择。APN 开通是一套完整方案模板，4 维度是步骤决策（DP），不是并列方案。**对标计费场景**：计费 CS = 计费机制闭包（离线/在线/融合…），APN CS = 开通机制闭包（地址×鉴权×接入×类型），维度选择 = DP。

### 2.1 CS-APN-01 APN 开通方案

| 字段 | 值 |
|------|---|
| `solution_id` | `CS-APN-01` |
| `solution_name` | `APN 开通方案` |
| `solution_summary` | UE 接入核心网并建立 PDU/PDN 会话的完整开通：按配置树 4 维度决策组合实例化 —— 地址分配（本地池/UDM静态/RADIUS/DHCP/LNS）× 鉴权（透明/透明鉴权/不透明/本地）× 接入隧道（直连/GRE/IPSec/L2TP/MPLS）× 地址类型（IPv4/IPv6/双栈），叠加会话管理/网元选择/接入控制 3 底座 |
| `design_intent` | 解决"UE 如何获得地址、经何种鉴权与隧道接入目标 DN"的完整 APN 开通问题；任一具体开通 = 4 维度各取一值的实例 |
| `core_mechanism_combo` | 配置树：`APN开通 = 地址分配信息(OR) AND 鉴权计费信息(AND) AND 接入方式信息(OR)`，地址类型为每会话决策；每 OR/AND 分支由 DP 选择 → Feature → ConfigTask → MML（见第 2~4 层） |
| `status` | `active` |
| `source_evidence_ids` | `EV-BS-02`, `EV-FK-06`, `EV-FK-12`, `EV-FK-24`, `EV-FK-29`, `EV-FK-30` |

**scopes**: subscriber（单用户静态地址/鉴权）、subscription（会话级地址/流控）、access（APN/DNN 粒度）、location（位置区池组）

**participants**: UE、UNC/SMF/PGW-C（控制面）、UDG/UPF/PGW-U（用户面）、UDM/HSS/HLR（签约）、Radius/DN-AAA、外部 DHCP Server、IPSec/GRE/MPLS/LNS 网关、SGSN/MME/AMF（接入侧）

**uses_feature**（按配置树维度组织，★终点全为 Feature，§13 合规）：
- 地址分配（OR 分支）：`GWFD-010105`(UPF本地) / `GWFD-020421`(基于位置) / `WSFD-010502`(UDM静态/RADIUS/DHCP/SMF) / `WSFD-104410`(LNS) / `WSFD-104413`+`WSFD-104005`(DHCP)
- 鉴权计费（AND）：`WSFD-011305`(Radius鉴权接入) / `WSFD-011306`(Radius功能) / `WSFD-010301`(AKA鉴权) / `WSFD-108007`(DN二次鉴权) / `WSFD-011307`(Radius抄送)
- 接入方式（OR 分支）：`IPFD-015002`(GRE) / `IPFD-015004`(IPSec-UDG) / `IPFD-016000`(IPSec-UNC) / `GWFD-020412`+`WSFD-104410`(L2TP) / `GWFD-020411`+`WSFD-104411`(MPLS VPN)
- 地址类型/IPv6 承载：`GWFD-020403`+`WSFD-104002`(双栈) / `GWFD-020401`+`WSFD-104001`(IPv6承载) / `GWFD-020406`+`WSFD-104004`(PD)
- 底座：`GWFD-010101`+`WSFD-010501`(会话管理) / `WSFD-010503`(多PDN并发) / `WSFD-010400`(用户数据) / `WSFD-106203`(别名APN) / `WSFD-107010`(UPF选择) / `WSFD-010202`(对等网元) / `WSFD-106003`+`GWFD-010151`(接入控制) / `GWFD-010108`(地址检测) / `GWFD-010107`+`WSFD-107021`(静态路由冗余)

**uses_semantic_object**: `SO-APN-ADDRESS-POOL`, `SO-APN-AUTH-AAA`, `SO-APN-TUNNEL`, `SO-APN-SESSION-CONTEXT`, `SO-APN-SUBSCRIPTION`, `SO-APN-QUOTA-LIFECYCLE`
**constrained_by**: 全部 16 条 BR（见 §4）

> **★与原 9 编造 CS 的关系**：原 9 CS（智慧农业传感器上报/工厂工控访问内网/家庭CPE宽带/VoLTE/企业AAA二次鉴权/传统企业DHCP迁移/企业L2TP VPN/区域化运营/企业双栈加密）是 4 维度矩阵的一种人为业务用例切分，场景命名与业务需求叙述系 SKILL 意图澄清文档脑补，不在产品文档，已删除。其底层技术决策（地址/鉴权/隧道/类型组合）由本 CS 的 DP 选择承载。

---

## 3. DecisionPoint（12 个，★配置树步骤维度 + 特性文档背书，保留）

> **owner_ref 规范**：APN 开通的 12 个决策点均为场景级稳定选择点，归 `NS-APN-01`。前 5 个对应配置树 4 维度步骤（地址方式/粒度/鉴权/接入隧道/地址类型），后 7 个为特性文档背书的底座决策（UPF选择/对等网元/接入权限/并发/别名APN/二次鉴权/带宽流控）。

| `decision_id` | `owner_layer` | `owner_ref_type` | `owner_ref` | `decision_name` | `decision_question` | `option_set` | `trigger_condition` | `impact_summary` | `status` | `source_evidence_ids` |
|---------------|---------------|-------------------|-------------|-----------------|---------------------|--------------|---------------------|------------------|----------|----------------------|
| `DP-APN-ADDR-MODE` | `business` | `NetworkScenario` | `NS-APN-01` | 地址分配方式决策（配置树·地址分配OR） | UE IP 地址由谁分配、以何种方式分配 | `["UDM静态签约","UPF-APN/DNN动态","UPF-LOCATION动态","UPF-SMF动态","SMF本地","RADIUS下发","DHCP代理","LNS(L2TP)"]` | PDU 会话建立、需为 UE 分配 IP 时 | 决定 POOLTYPE（LOCAL/UDM/SMF/EXTERNAL）、ALLOCPRECEDENCE、地址池语义对象实例化路径；决定 C-U 决策执行分离模式 | `active` | `EV-BS-02`, `EV-FK-12`, `EV-FK-06` |
| `DP-APN-ADDR-GRANULARITY` | `business` | `NetworkScenario` | `NS-APN-01` | 地址分配粒度决策（配置树·UPF分配OR子叶） | 地址池按什么粒度匹配 | `["APN-1&LOC-0&SMF-0","APN-0&LOC-1&SMF-0","APN-0&LOC-0&SMF-1","APN-1&LOC-1&SMF-0","APN-1&LOC-0&SMF-1","APN-0&LOC-1&SMF-1","APN-1&LOC-1&SMF-1"]` | 选择 UPF 本地分配方式后 | 决定三级优先级规则字符串（SET IPALLOCRULE / SET APNIPALLOCRULE）与 POOLGRPMAP 映射条件 | `active` | `EV-BS-02`, `EV-FK-06`, `EV-FK-08` |
| `DP-APN-ADDR-TYPE` | `business` | `NetworkScenario` | `NS-APN-01` | 地址类型决策 | UE 获得 IPv4 / IPv6 / 双栈 | `["IPv4","IPv6","IPv4v6双栈"]` | 每会话独立决策 | 决定 SECTION 配置（V4STARTIP/V6PREFIXSTART）、License 触发（IPv6→LKV3G5V6PB01；双栈→LKV3G5VDSA01；PD→LKV3G5P6PD01）；实际由 PFCP CHV4/CHV6/V4/V6 BIT 位组合指示 | `active` | `EV-BS-02`, `EV-FK-16`, `EV-FK-17` |
| `DP-APN-AUTH-MODE` | `business` | `NetworkScenario` | `NS-APN-01` | 鉴权方式决策（配置树·鉴权计费AND） | UE 接入鉴权采用哪种方式 | `["TRANS_NON_AUTH","TRANS_AUTH","NON_TRANS","LOC_AUTH"]` | PDU 会话/承载/PDP 上下文创建时 | 决定是否调用 AAA（仅 TRANS_AUTH/NON_TRANS 强依赖 Radius）；决定账密来源；LOC_AUTH 不支持 PPP 用户 | `active` | `EV-BS-02`, `EV-FK-24` |
| `DP-APN-ACCESS-MODE` | `business` | `NetworkScenario` | `NS-APN-01` | 接入隧道方式决策（配置树·接入方式OR） | UE 接入企业/异地 DN 采用哪种隧道 | `["直连","NAT","IPSec","GRE","MPLS-VPN","L2TP","GRE-over-IPSec"]` | 需穿越异种/不可信网络访问目标 DN 时 | 决定隧道封装类型、C-U 协同模式（对称同构 vs C 决策 U 执行）、License 触发（L2TP→LKV3G5L2TP01）；与地址分配存在互斥（L2TP↔位置） | `active` | `EV-BS-02`, `EV-FK-29`, `EV-FK-30`, `EV-FK-32`, `EV-FK-11` |
| `DP-APN-UPF-SELECT` | `business` | `NetworkScenario` | `NS-APN-01` | UPF 选择三轮决策 | 会话应锚定到哪个 UPF 实例 | `["按DNN","按S-NSSAI","按DNAI","按位置","按接口能力","按权重","按负载"]` | SMF 建立会话前 | 决定 UPF NF Profile 匹配维度（三轮递进：必选→优选→权重/负载）；选定结果直接决定地址分配执行侧 | `active` | `EV-FK-34` |
| `DP-APN-PEER-NF-SELECT` | `business` | `NetworkScenario` | `NS-APN-01` | 对等网元 DNS 域名聚合决策 | SGSN/MME 如何按区域聚合对等网元 DNS 域名 | `["按LAI","按RAI","按TAI","按ZONE名称"]` | 2G/3G/4G 附着/RAU/TAU 流程（非 5G） | 决定 AREDNS 配置（DNTYPE + LAC/RAC/TAC RANGE + ZONENAME）；适用 NF 为 SGSN/MME，非 SMF | `active` | `EV-FK-35` |
| `DP-APN-ACCESS-PERMISSION` | `business` | `NetworkScenario` | `NS-APN-01` | 用户接入权限判定（C 面） | 是否允许 UE 接入网络 | `["允许接入","拒绝(原因值)"]` | UE 附着/PDU 建立、需校验签约 ARD/APN/卡类型/RAT 限制时 | 决定 ARD 记录查询路径（AMF 本地 NGMMSUBDATA vs SGSN/MME GBARD/IUARD/S1ARD）；AMF 本地优先于签约兜底 | `active` | `EV-FK-36` |
| `DP-APN-BANDWIDTH-CTRL` | `business` | `NetworkScenario` | `NS-APN-01` | U 面带宽流控方式判定 | 用户面上下行带宽采用何种流控 | `["转发","丢弃(CAR)","缓存整形(Shaping)"] × ["上行","下行"]` | 基于协商带宽需在 U 面执行流控时 | 决定 APNQOSATTR 配置（CARSHAPESWUL/DL 开关 + 方式）；与 C 面接入权限机制完全不同，非 C-U 对称 | `active` | `EV-FK-37` |
| `DP-APN-CONCURRENCY` | `business` | `NetworkScenario` | `NS-APN-01` | 多 PDN/PDU 并发允许判定 | 是否允许该用户建立新的并发会话 | `["允许建立","拒绝(原因值55)"]` | UE 请求新建 PDN/PDU 且已达配额时 | 决定 APNACTNUM 查询（EPC 单 APN ≤11；5GC 单用户 PDU ≤15）；超限 MME/SMF 拒绝 | `active` | `EV-FK-03` |
| `DP-APN-ALIAS-APN` | `business` | `NetworkScenario` | `NS-APN-01` | 别名 APN 映射决策 | 协商到的 APN 是否需要映射为别名/真实 APN | `["映射后APN(别名/真实)","原APN"]` | SGSN/MME 协商 APN 或 GGSN/PGW-C/SMF 收到别名 APN 时 | 决定 ALIASAPNMAP 双向映射查询；两套网元映射方向相反（SGSN/MME: 协商→别名；GGSN/PGW-C/SMF: 别名→真实） | `active` | `EV-FK-05` |
| `DP-APN-SECOND-AUTH` | `business` | `NetworkScenario` | `NS-APN-01` | DN 二次鉴权决策 | 是否允许 UE 访问特定企业/园区 DN | `["允许访问DN","拒绝"]` | UE 会话建立后访问特定 DN、DN-AAA 触发时 | 决定经 UPF N4 GTP-U 隧道转接 DN-AAA 的路径；仅 PAP/CHAP via Radius，不支持 EAP/Diameter | `active` | `EV-FK-27` |

---

## 4. BusinessRule（16 条，产品文档背书，保留）

> **rule_type 枚举服从 Schema §8.9**。权威来源：EV-BS-02（配置树）+ EV-FK-*（特性文档）。

| `rule_id` | `rule_name` | `rule_type` | `rule_expression_mode` | `rule_source_kind` | `rule_logic` | `violation_effect` | `status` | `source_evidence_ids` |
|-----------|-------------|-------------|------------------------|--------------------|--------------|---------------------|----------|----------------------|
| `BR-APN-LOC-L2TP-EXCL` | 基于位置与 L2TP 互斥 | `scope_rule` | `explicit` | `restriction` | 基于位置的地址分配（GWFD-020421）与 L2TP VPN（GWFD-020412）不可同时应用；020421 声明互斥，020412 未声明需双向补全 | 两者同时配置会导致地址分配冲突，L2TP 会话建立失败 | `active` | `EV-FK-08`, `EV-FK-11` |
| `BR-APN-GRE-IPSEC-SRC-EXCL` | GRE 与 IPSec 源地址互斥 | `scope_rule` | `explicit` | `restriction` | GRE 隧道（IPFD-015002）源地址不能与 IPSec 隧道（IPFD-015004）源地址相同 | 隧道封装冲突，报文无法正确转发 | `active` | `EV-FK-29`, `EV-FK-30` |
| `BR-APN-L2TP-ADDRAUTO-EXCL` | L2TP 与地址自动检测互斥 | `scope_rule` | `explicit` | `restriction` | L2TP VPN（GWFD-020412）与用户面地址自动检测（GWFD-010108）不可同时应用 | 地址检测抢占 L2TP 会话地址，L2TP 隧道异常 | `active` | `EV-FK-11` |
| `BR-APN-RADIUS-CASCADE` | Radius 级联强依赖链 | `design_rule` | `explicit` | `design` | Radius 功能（WSFD-011306）→ Radius 鉴权接入（WSFD-011305）→ 终端二次鉴权（WSFD-108007，+ 可选 Radius 抄送 WSFD-011307）；前级必须先激活，后级才能生效 | 跳级激活会导致鉴权链断裂，二次鉴权无 Radius 配置承载 | `active` | `EV-FK-25`, `EV-FK-24`, `EV-FK-27` |
| `BR-APN-LOC-AUTH-NO-PPP` | 本地鉴权不支持 PPP 用户 | `scope_rule` | `explicit` | `restriction` | 本地鉴权接入（ACCESSMODE=LOC_AUTH）不支持 PPP 用户接入 | PPP 用户强制走本地鉴权会鉴权失败 | `active` | `EV-FK-24` |
| `BR-APN-IPV6-CASCADE` | IPv6 承载强依赖链 | `design_rule` | `explicit` | `design` | IPv6 承载上下文（GWFD-020401，LKV3G5V6PB01）→ IPv4v6 双栈（GWFD-020403，LKV3G5VDSA01）→ IPv6 Prefix Delegation（GWFD-020406，LKV3G5P6PD01，V6PREFIXLENGTH<64 触发）；前缀长度 64 是 PD 分水岭 | IPv6 承载缺失会导致双栈/PD 无法生效；License 串联断裂 | `active` | `EV-FK-18`, `EV-FK-16`, `EV-FK-20` |
| `BR-APN-DUALSTACK-NEED-LICENSE` | 双栈必须 License | `selection_rule` | `explicit` | `config` | IPv4v6 双栈落地必须 License LKV3G5VDSA01；GWFD-020403 是"能力使能层"，使能 GWFD-010105 的 IPv4v6 取值（能力叠加关系，使能方向单向 020403→010105） | 缺 License 时双栈配置命令成功但功能不生效 | `active` | `EV-FK-16`, `EV-FK-06` |
| `BR-APN-LOC-NEED-LICENSE` | 基于位置必须 License | `selection_rule` | `explicit` | `config` | 基于位置的地址分配（GWFD-020421）必须 License LKV3G5LBAA01；母特性 GWFD-010105 无 License | 缺 License 时基于位置的池组匹配不生效 | `active` | `EV-FK-08` |
| `BR-APN-L2TP-CU-ASYM` | L2TP License C-U 不对称 | `scope_rule` | `explicit` | `design` | L2TP VPN License 仅 UDG 侧必须（LKV3G5L2TP01）；UNC 侧 WSFD-104410 无 License；C 决策 U 执行模式导致 License 不对称 | 误以为 UNC 侧也需 License 会造成 License 获取错误 | `active` | `EV-FK-11`, `EV-FK-14` |
| `BR-APN-DNAAA-IP-UNIQUE` | DN-AAA IP 唯一性 | `scope_rule` | `explicit` | `config` | 直连 AAA 与经 UPF 中转 AAA 场景的 Radius Server IP 不可相同 | 两套场景指向同一 AAA IP 会导致鉴权路由混乱 | `active` | `EV-FK-27` |
| `BR-APN-SECOND-AUTH-PROTO` | 二次鉴权协议限制 | `scope_rule` | `explicit` | `restriction` | 终端二次鉴权（WSFD-108007）仅支持 PAP/CHAP via Radius，不支持 EAP、不支持 Diameter | 误配 EAP/Diameter 会导致二次鉴权无法建立 | `active` | `EV-FK-27` |
| `BR-APN-CONCURRENCY-11-15` | 并发会话硬上限 | `scope_rule` | `explicit` | `restriction` | EPC 单用户 PDN 连接 ≤ 11；5GC 单用户 PDU 会话 ≤ 15；超限 MME/SMF 拒绝（原因值 55） | 超过硬上限的新会话被拒绝，业务中断 | `active` | `EV-FK-03` |
| `BR-APN-ALIAS-DOUBLE-COND` | 别名 APN 转换双条件 | `design_rule` | `explicit` | `design` | SGSN/MME 侧别名 APN 转换需双条件同时满足：IMSI 号段匹配 AND 协商 APN 在映射表；缺一不可 | 单条件匹配会误转换，导致 DNS 屏蔽失效 | `active` | `EV-FK-05` |
| `BR-APN-UPF-VENDOR-LOCK` | SMF 与 UPF 同厂商 | `scope_rule` | `explicit` | `restriction` | SMF 和 UPF 设备必须同时为 HUAWEI（WSFD-107010 硬约束） | 异厂商组网会导致 N4 PFCP 互通异常 | `active` | `EV-FK-34` |
| `BR-APN-AMF-LOCAL-FIRST` | AMF 本地配置优先于签约 | `selection_rule` | `explicit` | `config` | AMF 本地匹配 > 签约兜底；本地 Null 强制允许；紧急注册跳过接入控制 | 误用签约优先会导致 AMF 本地策略失效 | `active` | `EV-FK-36` |
| `BR-APN-CARDTYPE-NEED-AUTH` | 卡类型控制依赖鉴权 | `design_rule` | `explicit` | `design` | SGSN/MME 卡类型控制（WSFD-106003 子特性 B）必须先启用 WSFD-010301 鉴权功能；前置依赖 | 未启用鉴权直接配卡类型控制不生效 | `active` | `EV-FK-36`, `EV-FK-26` |

---

## 5. SemanticObject（12 个，保留）

| `semantic_object_id` | `semantic_object_name` | `semantic_summary` | `semantic_layer_hint` | `status` | `source_evidence_ids` |
|----------------------|------------------------|--------------------|------------------------|----------|-----------------------|
| `SO-APN-ADDRESS-POOL` | 地址分配语义 | UE IP 地址的分配契约：来源（6 来源）、类型（IPv4/IPv6/双栈）、池组、段范围、生命周期、冲突态；地址类型实际由 PFCP CHV4/CHV6/V4/V6 BIT 位组合指示 | `cross_layer` | `active` | `EV-BS-02`, `EV-FK-06`, `EV-FK-12` |
| `SO-APN-AUTH-AAA` | 鉴权 AAA 语义 | 用户身份验证契约：三态嵌套（底层 AKA + APN 业务鉴权 + DN 二次鉴权）、协议（AKA/PAP/CHAP）、向量（三元/四元/五元组）、AAA 目标 | `cross_layer` | `active` | `EV-FK-26`, `EV-FK-24`, `EV-FK-27` |
| `SO-APN-TUNNEL` | 隧道语义 | 报文穿越异种/不可信网络的封装契约：类型（GRE/IPSec/MPLS/L2TP）、加密、组播支持、C-U 模式（对称同构 vs C 决策 U 执行）、C-U 对象不对称 | `cross_layer` | `active` | `EV-FK-29`, `EV-FK-30`, `EV-FK-32`, `EV-FK-11` |
| `SO-APN-QUOTA-LIFECYCLE` | 配额/地址生命周期语义 | 地址池占用、释放、延迟释放、租期续约、强制回收的完整生命周期（5 大增值功能） | `cross_layer` | `active` | `EV-FK-06` |
| `SO-APN-SESSION-CONTEXT` | PDU/PDN/PDP 会话上下文 | 会话级状态：会话 ID、DNN/APN、QoS Flow/承载、UE IP、F-TEID、SSC Mode；纯描述性根底座，由控制面 PFCP/GTP-C 被动触发 | `cross_layer` | `active` | `EV-FK-01`, `EV-FK-02` |
| `SO-APN-SUBSCRIPTION` | UNC 签约数据本地缓存 | UDM/HSS/HLR 下发的 APN/DNN 签约、QoS、APN-AMBR、PDN Address（静态）、ARD、APN-OI Replacement | `cross_layer` | `active` | `EV-FK-04` |
| `SO-APN-APNACTNUM` | 单 APN 并发限制配置 | EPC 单 APN 粒度并发上限配置：APNNI、PDNNUM、IPV4ADDRNUM、IPV6ADDRNUM、PDNCONNREJCAUSE | `cross_layer` | `active` | `EV-FK-03` |
| `SO-APN-ALIAS-APN-MAP` | 别名 APN 映射记录 | 别名 APN ↔ 真实 APN 双向映射表；SGSN/MME 侧与 GGSN/PGW-C/SMF 侧映射方向相反 | `cross_layer` | `active` | `EV-FK-05` |
| `SO-APN-PNFPROFILE` | UPF NF 实例属性 | UPF NF 实例的多维属性，用于三轮筛选：NFINSTANCENAME、NF TYPE、WEIGHT、PRIORITY、DNN/切片/DNAI/位置/EPS 互通能力 | `cross_layer` | `active` | `EV-FK-34` |
| `SO-APN-AREDNS` | 位置区域 DNS 域名定制 | LAI/RAI/TAI 聚合到单一 DNS 域名：DNTYPE、LAC/RAC/TAC + RANGE、ZONESW、ZONENAME；适用 NF 为 SGSN/MME | `cross_layer` | `active` | `EV-FK-35` |
| `SO-APN-ARD-RECORD` | 接入限制参数记录（C 面） | C 面接入权限判定的配置记录：AMF 侧 NGMMSUBDATA；SGSN/MME 侧 GBARD/IUARD/S1ARD | `cross_layer` | `active` | `EV-FK-36` |
| `SO-APN-APNQOSATTR` | APN QoS 属性（U 面带宽流控） | U 面带宽流控的上下行 CAR/Shaping 开关与方式：CARSHAPESWUL/CARSHAPEUL/CARSHAPESWDL/CARSHAPEDL；与 C 面接入权限机制不同，非 C-U 对称 | `cross_layer` | `active` | `EV-FK-37` |

---

## 6. Scope（子对象）

| `scope_name` | `scope_type` | `scope_summary` | 关联方案 |
|--------------|--------------|-----------------|----------|
| 用户级范围 | `subscriber` | 单用户特定业务/静态地址/鉴权策略 | CS-APN-01 |
| 会话承载范围 | `subscription` | PDU/PDN 会话级地址分配与流控 | CS-APN-01 |
| APN/DNN 接入范围 | `access` | 按 APN/DNN 粒度匹配地址池或鉴权 | CS-APN-01 |
| 位置区域范围 | `location` | 按 LAC/Tac 池组匹配差异化地址分配 | CS-APN-01 |

---

## 7. Participant（子对象）

| `participant_name` | `participant_type` | `plane_or_side` | `responsibility_summary` | 关联方案 |
|--------------------|--------------------|-----------------|--------------------------|----------|
| UE / 终端 | `endpoint` | `terminal_side` | 发起附着/PDU 建立、携带 PCO 账密、发起业务访问 | CS-APN-01 |
| UNC / SMF / PGW-C | `network_function` | `control_plane` | PDU 会话控制、鉴权决策、地址分配决策、UPF 选择、L2TP 决策、别名 APN 映射 | CS-APN-01 |
| UDG / UPF / PGW-U | `network_function` | `user_plane` | 地址池执行、双栈会话执行、隧道终结（IPSec/GRE/L2TP LAC）、DN-AAA 转接、带宽流控 | CS-APN-01 |
| UDM / HSS / HLR | `external_system` | `external` | 静态签约数据、APN-AMBR、QoS profile、ARD 下发 | CS-APN-01 |
| Radius / DN-AAA Server | `external_system` | `external` | 业务鉴权、DN 二次鉴权、Radius 下发地址（Framed-Pool） | CS-APN-01 |
| 外部 DHCP Server | `external_system` | `external` | DHCP/DHCPv6 地址下发 | CS-APN-01 |
| IPSec / GRE / MPLS / LNS 网关 | `access_side` | `access_side` | 隧道对端、LNS 地址分配 + AAA | CS-APN-01 |
| SGSN / MME / AMF | `access_side` | `access_side` | 底层 AKA 鉴权、对等网元选择、别名 APN 映射（协商侧）、接入权限本地判定 | CS-APN-01 |

---

## 8. 业务图谱关系边（严格 §8.12）

### 8.1 层级包含

| 起点 | 关系 | 终点 |
|------|------|------|
| `BD-APN-01` | `contains` | `NS-APN-01` |
| `NS-APN-01` | `instantiated_as` | `CS-APN-01` |

### 8.2 方案使用特性（uses_feature，单一 CS · 配置树维度组织）

| 起点 | 关系 | 终点（见 §2.1 uses_feature 完整清单） |
|------|------|------|
| `CS-APN-01` | `uses_feature` | 地址分配: `GWFD-010105`,`GWFD-020421`,`WSFD-010502`,`WSFD-104410`,`WSFD-104413`,`WSFD-104005` ／ 鉴权: `WSFD-011305`,`WSFD-011306`,`WSFD-010301`,`WSFD-108007`,`WSFD-011307` ／ 接入隧道: `IPFD-015002`,`IPFD-015004`,`IPFD-016000`,`GWFD-020412`,`GWFD-020411`,`WSFD-104411` ／ IPv6/双栈: `GWFD-020403`,`WSFD-104002`,`GWFD-020401`,`WSFD-104001`,`GWFD-020406`,`WSFD-104004` ／ 底座: `GWFD-010101`,`WSFD-010501`,`WSFD-010503`,`WSFD-010400`,`WSFD-106203`,`WSFD-107010`,`WSFD-010202`,`WSFD-106003`,`GWFD-010151`,`GWFD-010108`,`GWFD-010107`,`WSFD-107021` |

> **★ Schema §13 合规**：uses_feature 终点全部为 Feature（WSFD-/GWFD-/IPFD- 前缀），无 ConfigObject/MMLCommand 直接绑定。

### 8.3 决策点归属（has_decision）

| 起点 | 关系 | 终点 | 说明 |
|------|------|------|------|
| `NS-APN-01` | `has_decision` | `DP-APN-ADDR-MODE`, `DP-APN-ADDR-GRANULARITY`, `DP-APN-ADDR-TYPE`, `DP-APN-AUTH-MODE`, `DP-APN-ACCESS-MODE`, `DP-APN-UPF-SELECT`, `DP-APN-PEER-NF-SELECT`, `DP-APN-ACCESS-PERMISSION`, `DP-APN-BANDWIDTH-CTRL`, `DP-APN-CONCURRENCY`, `DP-APN-ALIAS-APN`, `DP-APN-SECOND-AUTH` | 12 决策点归 NS（APN 开通场景级）；前 5 = 配置树 4 维度步骤，后 7 = 底座决策 |

### 8.4 业务规则约束（constrained_by）

| 起点 | 关系 | 终点 |
|------|------|------|
| `CS-APN-01` | `constrained_by` | 全部 16 条 `BR-APN-*`（互斥/License/强依赖，见 §4） |

### 8.5 语义对象使用（uses_semantic_object）

| 起点 | 关系 | 终点 |
|------|------|------|
| `CS-APN-01` | `uses_semantic_object` | `SO-APN-ADDRESS-POOL`, `SO-APN-AUTH-AAA`, `SO-APN-TUNNEL`, `SO-APN-SESSION-CONTEXT`, `SO-APN-SUBSCRIPTION`, `SO-APN-QUOTA-LIFECYCLE` |

### 8.6 证据支撑（supported_by，★去伪追溯）

| 起点 | 关系 | 终点 |
|------|------|------|
| `BD-APN-01` | `supported_by` | `EV-BS-02`(配置树), `EV-FK-01`, `EV-FK-02` |
| `NS-APN-01` | `supported_by` | `EV-BS-02`(配置树), `EV-FK-01`, `EV-FK-02`, `EV-FK-06` |
| `CS-APN-01` | `supported_by` | `EV-BS-02`(配置树·权威骨架) + 配置树各维度主属特性 `EV-FK-06/12/24/29/30` |

> **★去伪追溯**：原 `CS-APN-01~09 supported_by EV-TK-01/EV-CA-02`（自撰归纳）已移除。EV-TK-01 标 `deprecated`，EV-CA-02 降级 `supporting`，EV-BS-01 降级 `reference`。CS/DP/BR/SO 权威 = EV-BS-02（配置树）+ EV-FK-*（特性文档，源自产品文档）。

---

## 9. 端到端方案链路（真实机制，非编造场景）

> 以下为 APN 开通的真实机制路径（4 维度组合的典型实例），跨层映射依据。每条 = DP 各取一值的实例化，非编造业务垂直场景。

### 9.1 实例A：UPF本地地址池 + 透明接入 + 直连 + IPv4（基础 Internet 接入）
```
UE 附着 → 底层 AKA 鉴权(WSFD-010301)
→ PDU 建立 → UPF 本地池基于 APN 分配(GWFD-010105: ADD POOL/SECTION/POOLGRPMAP, SET IPALLOCRULE=APN-1&LOCATION-0&SMF-0)
→ TRANS_NON_AUTH 透明接入(WSFD-011305, 无需 Radius 功能)
→ 直连(NAT) → IPv4 单栈 → OSPF 下行路由发布(GWFD-010104)
```

### 9.2 实例B：LNS(L2TP) + 不透明接入 + L2TP 隧道 + 双栈（C 决策 U 执行典型）
```
UE 附着 → PDU 建立 → NON_TRANS 鉴权(WSFD-011305)
→ UNC/SMF 决策 LNS 参数(WSFD-104410: SET APNL2TPCTRL 2参数, 经 N4 PFCP 下发)
→ UDG 作 LAC 执行封装(GWFD-020412: SET APNL2TPATTR 14参数 + L2TPGROUP + PPP/LCP/IPCP)
→ LNS 分配双栈(IPCP IPv4 + RA+IPv6CP IPv6, 需 License LKV3G5L2TP01 仅 UDG)
→ C-U 不对称：L2TPN4KEY(U) 与 L2TPKEY(C) 必须相同
```

### 9.3 实例C：UDM静态签约 + 不透明接入 + IPSec 隧道 + IPv4（企业加密接入）
```
UE 附着 → PDU 建立 → UDM 静态签约读取(WSFD-010502: ADD ADDRPOOL POOLTYPE=UDM + 白名单 CHECKIPVALID)
→ NON_TRANS 鉴权(WSFD-011305, UE 透传账密→UNC→企业 Radius, 需 011306 Radius 功能)
→ IPSec 隧道加密(IPFD-015004: IKE Peer+Proposal+Policy, 8 场景之一)
→ IPv4 单栈访问企业内网
```

---

## 10. 与计费/带宽场景业务图谱的对比

| 维度 | 计费场景 | 带宽控制场景 | APN 业务域（本文件 v2） |
|------|---------|------------|---------------------|
| BusinessDomain | `业务感知`（BD-CH-01） | `业务感知`（BD-BW-01） | `接入与会话管理`（**BD-APN-01，独立**） |
| NetworkScenario | NS-CH-01 计费场景 | NS-BW-01 带宽控制场景 | NS-APN-01 APN 开通场景 |
| ConfigurationSolution | 7（按计费机制闭包：离线/在线/融合…） | 7（按控制机制） | **1（APN 开通方案，配置树 4 维度组合；原 9 编造 CS 已删）** |
| 核心机制 | SA→Rule→PCC/URR→上报→配额 | SA→BWM→CAR/Shaping/FUP/GBR | 4 维度决策（地址×鉴权×接入×类型）+ 3 底座 |
| DecisionPoint | 8 | 8 | **12**（5 配置树步骤 + 7 底座） |
| BusinessRule | 16 | 6 | **16** |
| SemanticObject | 12（含协议栈 2） | 8 | **12**（含底座签约/网元类） |
| 独立性 | 共享"业务感知"根 | 共享"业务感知"根 | **独立根，与业务感知并列** |

---

## 11. 对象计数汇总

| 对象类型 | 数量 | 编号范围 |
|---------|------|---------|
| BusinessDomain | 1 | BD-APN-01 |
| NetworkScenario | 1 | NS-APN-01 |
| ConfigurationSolution | **1**（原 9 编造 CS 已删） | CS-APN-01 |
| DecisionPoint | 12 | DP-APN-ADDR-MODE / ADDR-GRANULARITY / ADDR-TYPE / AUTH-MODE / ACCESS-MODE / UPF-SELECT / PEER-NF-SELECT / ACCESS-PERMISSION / BANDWIDTH-CTRL / CONCURRENCY / ALIAS-APN / SECOND-AUTH |
| BusinessRule | 16 | BR-APN-LOC-L2TP-EXCL / GRE-IPSEC-SRC-EXCL / L2TP-ADDRAUTO-EXCL / RADIUS-CASCADE / LOC-AUTH-NO-PPP / IPV6-CASCADE / DUALSTACK-NEED-LICENSE / LOC-NEED-LICENSE / L2TP-CU-ASYM / DNAAA-IP-UNIQUE / SECOND-AUTH-PROTO / CONCURRENCY-11-15 / ALIAS-DOUBLE-COND / UPF-VENDOR-LOCK / AMF-LOCAL-FIRST / CARDTYPE-NEED-AUTH |
| SemanticObject | 12 | SO-APN-ADDRESS-POOL / AUTH-AAA / TUNNEL / QUOTA-LIFECYCLE / SESSION-CONTEXT / SUBSCRIPTION / APNACTNUM / ALIAS-APN-MAP / PNFPROFILE / AREDNS / ARD-RECORD / APNQOSATTR |
| Scope（子对象） | 4 | subscriber / subscription / access / location |
| Participant（子对象） | 8 | UE / UNC-SMF / UDG-UPF / UDM-HSS / Radius-DNAAA / DHCP / 隧道网关 / SGSN-MME-AMF |
| **业务层对象总计** | **42** | BD 1 + NS 1 + CS 1 + DP 12 + BR 16 + SO 12（-1 vs 原版，因 9 CS → 1 CS） |

---

> 本文件为 APN 业务域三层图谱第 1 层（Phase 4 重建版）。命令层（04）已完成 Phase 1 全量重建（37/37 特性）；特性层（02）/任务层（03）/跨层映射（05）/证据（06）见同目录其他文件（待 Phase 2/3/5 重建）。
