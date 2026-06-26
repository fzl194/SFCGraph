# APN 业务域 topic-knowledge：配置树修正与 Stage 3 待解决项汇总

> **定位**：Stage 2 收敛层（基于 37 篇 feature-knowledge §8 章节 + 四维度归纳 §6 预留问题）。是 Stage 3 cross-analysis 的**关键输入清单**，每条结论已标注来源特性，Stage 3 可直接据此执行。
> **数据源**：仅基于 feature-knowledge 的 §8（文档一致性说明 / 文档缺口标注）章节，不再回读产品文档。
> **来源特性标注规范**：每条结论后括注 `[GWFD-xxxxx]` 或 `[WSFD-xxxxx]`；多特性共同支撑用 `+` 连接。
> **Evidence 占位**：本文件全部结论使用统一占位 `EV-TK-修正`（Stage 4 实例化时映射到具体 feature-knowledge 的 EV-FK-xx）。

---

## 0. 元数据

| 字段 | 取值 |
|------|------|
| topic_id | TK-APN-修正清单 |
| topic_name | 配置树修正与 Stage 3 待解决项汇总 |
| topic_layer | 2（Stage 3 输入清单） |
| source_feature_count | 37 篇 feature-knowledge §8 章节（覆盖全部 APN 业务域特性） |
| source_evidence_ids | EV-TK-修正 |
| downstream_consumers | Stage 3 cross-analysis（横向验证 12 个待解决问题）→ Stage 4 DecisionPoint/SemanticObject/FeatureRule 实例化 |

---

## 1. ★ 配置树 / 意图澄清修正清单（11 处）

> 以下为配置树归类、父子关系、C-U 对称性、特性边界等**需要在图谱建模时修正或特别标注**的项。每条含：配置树/任务清单原描述 → 产品文档实际 → 依据特性 → 对图谱建模的影响。

| # | 项 | 配置树/任务清单描述 | 产品文档实际 | 依据特性 | 对图谱建模的影响 |
|---|----|--------------------|-------------|----------|-----------------|
| **1.1** | **IPv4v6 双栈定位** | 配置树将 GWFD-020403 与 GWFD-010105 视为并列地址分配特性 | **双栈 = 能力使能层，非分配机制层**。GWFD-020403 是 License 使能层（LKV3G5VDSA01），使能 GWFD-010105 的 IPv4v6 地址类型落地；非父子、非包含，是"能力叠加"关系 | GWFD-020403 §8 + GWFD-010105 §8 | Feature 变体维度需建模 `能力层级=使能层/机制层`；License 约束建模为 FeatureRule `FR-DUALSTACK-NEED-LICENSE`，使能方向单向（020403→010105） |
| **1.2** | **WSFD-010504 与 WSFD-010502 关系** | 配置树推断 "010504 = 010502 父节点"（parent_feature_id） | **证伪**：010504 ⊂ 010502（010504 仅 SMF 本地池 1 种，010502 共 4 种 UDM/Radius/SMF/DHCP）；010504 发布更晚（20.8.0 vs 20.0.0）；两者为**并列子集**关系 | WSFD-010504 §8.1 #4 + §8.2 | 图谱 parent_feature_id 应置空或指向更高层节点；FeatureRelation 建模为 `subset_of`（010504 → 010502），非 `parent_of` |
| **1.3** | **APNL2TPATTR (U) vs APNL2TPCTRL (C) 不对称** | 配置树/任务要求假设 C-U 两侧配置对象对称 | **C-U 配置对象命名与参数量均不对称**：U 面 `APNL2TPATTR`（SET APNL2TPATTR，10+ 参数）；C 面 `APNL2TPCTRL`（SET APNL2TPCTRL，仅 2 参数 APN/L2TPSWITCH）。U 面承担实际隧道执行需配置细节，C 面仅使能开关 | GWFD-020412 §8.1 #1 + §8.3 #3 / WSFD-104410 §8.3 | SemanticObject `SO-TUNNEL` 需建模 `c_u_object_asym=true`；ConfigObject 节点两侧分离建模（L2TPATTR_U / L2TPCTRL_C），非同一对象 |
| **1.4** | **IPV4ALLOCTYPE / IPV6ALLOCTYPE 真实载体** | 任务要求重点关注 `IPV4ALLOCTYPE`/`IPV6ALLOCTYPE` 参数 | **两侧 WSFD-010502 / GWFD-010105 产品文档均未显式定义此参数名**；实际指示 IPv4/IPv6 分配类型的是 PFCP Session Est Req 中的 **CHV4/CHV6/V4/V6 BIT 位组合**（GWFD-010105 §3.4.2 真值表） | WSFD-010502 §8.2 #6 + GWFD-010105 §3.4 | SemanticObject `SO-ADDRESS-POOL` 的 `type` 属性来源应标 `PFCP BIT (CHV4/CHV6/V4/V6)`；不要建模为配置参数 |
| **1.5** | **WSFD-010202 网元角色** | 文档清单标 "UNC/SMF，网元选择类" | **实际适用 NF 为 SGSN、MME**（非 SMF）；SMF 是 5G 实体，本特性是 2G/3G/4G 特性，不涉及 SMF | WSFD-010202 §7.1 #3 | Feature 节点 `applicable_nf` 字段必须修正为 `SGSN/MME`；不要与 5G UPF 选择（WSFD-107010）混淆，两者代际互补不重叠 |
| **1.6** | **GWFD-010151 与 WSFD-106003 非对称** | 任务要求假设两者为 C-U 对称的"接入控制" | **机制完全不同，非 C-U 对称**：GWFD-010151（UDG 侧）= **带宽流控**（CAR/Shaping，协商带宽资源）；WSFD-106003（UNC 侧）= **接入权限**（签约 ARD/APN/卡类型控制）。两者是"接入控制"同名不同义 | GWFD-010151 §8 #8 + WSFD-106003 §8 | 图谱必须区分两类"接入控制"：建模为两个独立 Feature 变体（bandwidth_control vs access_permission），FeatureRelation 不建 `c_u_symmetric` 边 |
| **1.7** | **WSFD-106003 双特性合一** | 文档清单标题"用户接入控制(APN接入权限)"单一描述 | **同一特性 ID 下含两个实现独立的子特性**：子特性 A（AMF 侧 5GC，RAT+核心网限制，无 License）+ 子特性 B（SGSN/MME 侧 2/3/4G，签约 ARD+APN+卡类型，需 License LKV2ARD02）。定义、适用 NF、控制依据、License 均不同 | WSFD-106003 §8.1 #1 + §8.2 | 图谱 Feature 节点需建模 `variant_dimensions` 含 `子特性=A/B`；拆分为两个 Feature 变体节点或用 variant 区分，避免规则匹配混淆 |
| **1.8** | **WSFD-106203 别名 APN 双视角语义反转** | 文档清单标题"别名APN/虚拟APN(聚合与重定向)"单一语义 | **同一特性 ID 在两套网元下映射方向相反**：SGSN/MME = 协商APN→别名APN（DNS 屏蔽）；GGSN/PGW-C/SMF = 别名APN→真实APN（资源归一）。两侧 License（LKV2AAPN01 vs LKV2ALIASAPN02）、命令（ADD APNALIAS vs ADD ALIASAPN）、规格均不同 | WSFD-106203 §8.1 + §8.3 | 图谱建议拆分为两个 Feature 变体（按网元角色视角区分）；FeatureRule 需分网元建模映射方向 |
| **1.9** | **GWFD-010104 与 GWFD-010105 父子关系** | 配置树将 GWFD-010104 列为 GWFD-010105 父节点 | **父子关系成立**：010104 是"地址分配方式总览"（外部+用户面），010105 是其下"用户面地址分配"分支详细展开；010104 文档明确正向引用 010105。但 010104 无 License、无告警、无应用限制，与 010105 差异显著 | GWFD-010104 §8 #1,5,6,7 | 图谱 parent_feature_id（010105→010104）保留；但 Feature 变体需区分 `总览/分支`，License/告警/限制按 010105 独立建模 |
| **1.10** | **WSFD-104001 单向依赖声明矛盾** | 配置树未呈现依赖关系 | **WSFD-104001 三套代际均声明"不涉及与其他特性的交互"**，但 WSFD-104002（5G 明确）、WSFD-104004（显式声明）均强依赖 WSFD-104001 提供 IPv6 路由广播底座；2/3/4G 流程描述也实际引用其能力 | WSFD-104001 §8.2 + WSFD-104004 §8.2 | 图谱 FeatureRelation 必须建模 `strong_depends_on`（104002→104001, 104004→104001）；忽略"不涉及交互"声明，以流程语义为准 |
| **1.11** | **MPLS VPN 缺激活/调测文档** | 文档清单列 9 个文件（全 UDG 侧） | **9 篇全为概念/原理/组网说明文档，无激活/调测/参考信息操作文档**；核心配置对象（VPN 实例 VRF + RD + VPN Target + 两层标签 + MP-BGP）的具体 MML 命令文档未直接列出 | GWFD-020411 §9.1 #6 + §9.2 #1,8 | 图谱 ConfigObject 节点需从 UDG 命令字典补全；标注 `doc_gap=MML命令缺失`，Stage 3 需补全命令/脚本/调测/告警 |

---

## 2. C-U 关系模式分类表

> APN 业务域 37 个特性按 C-U 协同模式可清晰归类为 **4 种模式**。Stage 3 需据此为每个 Feature 节点标注 `c_u_mode` 属性。

| 模式 | 适用特性对 | C-U 协同特征 | License 对称性 | 核心配置对象对称性 | 依据特性 |
|------|-----------|-------------|---------------|-------------------|----------|
| **A. 对称同构型** | GRE：IPFD-015002（U+C 双侧同特性）<br>IPSec：IPFD-015004（UDG）+ IPFD-016000（UNC）<br>MPLS VPN：GWFD-020411（UDG）+ WSFD-104411（UNC）<br>静态冗余：GWFD-010107（UDG）+ WSFD-107021（UNC） | UDG 与 UNC 两产品**均部署同名特性**，两侧配置对象与命令基本对称；IPSec 两侧特性概述/原理/术语 hash 完全相同（61317289）；MPLS 两侧 9 子文档一一对应 | **License 对称**（GRE/IPSec 两侧均无；MPLS 两侧均需；静态冗余两侧均无） | **基本对称**（命令族对称，个别参数差异） | IPFD-015002 §8.3 / IPFD-015004 §8.1 #4 / GWFD-020411 §9.1 #5 / GWFD-010107 §8.2 |
| **B. C 决策 U 执行型** | L2TP VPN：WSFD-104410（UNC 决策）+ GWFD-020412（UDG 作 LAC 执行） | UNC 决策 LNS 参数并经 N4 PFCP 下发；UDG 作 LAC 执行封装 + PPP 透传；C-U 协同通道为 N4 接口 L2TP 私有信元 | **License 不对称**（UDG 必须 82200BVC，UNC 无 License） | **对象不对称**（U: APNL2TPATTR 10+参数；C: APNL2TPCTRL 2参数） | GWFD-020412 §8.1 #1 + §8.3 |
| **C. 决策执行分离型** | 地址分配：WSFD-010502（C 决策 4 来源）+ GWFD-010105（U 执行 4 子方式）<br>控制面分配：WSFD-010504（C 决策+执行 SMF 本地池）vs GWFD-010105（U 执行）<br>IPv6 承载：WSFD-104001（C 决策+生成 RA）+ GWFD-020401（U 透传）<br>IPv6 PD：WSFD-104004（C 决策前缀）+ GWFD-020406（U 透传协商）<br>会话管理：WSFD-010501（C 决策）+ GWFD-010101（U 执行） | C 面拥有决策权（选方式/选类型/生成前缀），U 面无决策权按 C 面指示执行；通过 PFCP 消息解耦 | **License 对称或 U 侧独立**（010105/010502 两侧均无；020401/104001 各自独立 License） | **命令前缀差异**（U: ADD POOL/POOLGROUP；C: ADD ADDRPOOL/ADDRPOOLGRP；POOLTYPE 取值 LOCAL vs UDM） | WSFD-010502 §8.2 / WSFD-010504 §8.3 / WSFD-104001 §8.5 / WSFD-104004 §8.5 / WSFD-010501 §8.2 |
| **D. 非对称（同名不同义）型** | 接入控制：GWFD-010151（UDG 带宽流控）vs WSFD-106003（UNC 接入权限） | **机制完全不同，非 C-U 对称**：U 侧 CAR/Shaping 协商带宽；C 侧签约 ARD/APN/卡类型控制；任务要求假设对称但文档实际不对称 | **License 独立**（010151 无 License；106003 子特性 B 需 LKV2ARD02，子特性 A 无） | **对象完全不同**（U: APN+APNQOSATTR；C: ADD GBARD/IUARD/S1ARD 或 ADD NGMMSUBDATA） | GWFD-010151 §8 #8 + WSFD-106003 §8 |

> **Stage 3 关键结论**：模式 A（对称同构）与模式 B（C 决策 U 执行）是接入方式类 4 隧道的清晰二分；模式 C（决策执行分离）覆盖地址分配/IPv6/会话管理域；模式 D（非对称同名）需特别防范建模混淆。

---

## 3. 依赖声明矛盾清单

> 以下为特性文档"与其他特性的交互"章节声明"不涉及"或未声明，但**实际被他特性强依赖或存在隐性交互**的特性对。Stage 3 需以流程语义为准建模依赖关系。

| # | 被依赖特性 | 声明内容 | 实际依赖方 | 矛盾类型 | 依据特性 | 图谱建模建议 |
|---|-----------|---------|-----------|---------|----------|-------------|
| **3.1** | WSFD-104001（IPv6 承载上下文） | 三套代际均声明"不涉及与其他特性的交互" | WSFD-104002（5G 明确强依赖）、WSFD-104004（显式声明强依赖）；2/3/4G 流程也描述 GGSN/PGW-C 生成 IPv6 路由广播实际由本特性提供 | **单向依赖声明矛盾**（被依赖方声明无，依赖方声明强依赖） | WSFD-104001 §8.2 + WSFD-104004 §8.2 | 建模 `strong_depends_on`（104002→104001, 104004→104001），忽略"不涉及"声明 |
| **3.2** | WSFD-107010（UPF 选择） | 文档"与其他特性的交互"声明"不涉及" | WSFD-010502 单向引用 WSFD-107010（静态 IP 段绑定 UPF 与 SMF 主锚点 UPF 冲突时，SMF 选择优先）；"定义"章节明示"在 PDU 会话建立流程中" | **单向引用**（地址分配侧感知冲突，UPF 选择侧声明独立） | WSFD-107010 §7.2 + §7.3 | 建模 `interacts_with`（010502↔107010）；FeatureRule `FR-UPF-CONFLICT` 建模冲突协调 |
| **3.3** | IPFD-015004（IPSec UDG） | 特性概述声明"不涉及与其他特性的交互" | IPFD-015002 GRE 文档"应用限制"明确"GRE 隧道源地址不能与 IPSec 源地址相同"；IPSec 激活文档存在独立"GRE over IPSec"场景脚本；OSPF over IPSec 场景 | **源地址互斥来自 GRE 文档，IPSec 未声明但实际生效** | IPFD-015004 §8.1 #7 + §8.2 #4 | 建模 `mutually_exclusive`（015002↔015004 源地址维度）；FeatureRule `FR-GRE-IPSEC-SRC-EXCL` 以 GRE 文档为准 |
| **3.4** | GWFD-010101（会话管理 UDG） | 三份特性概述均声明"不涉及与其他特性的交互" | PDU 会话建立流程文档步骤 16 明确引用 GWFD-010105 的"UPF 分配 IP 地址流程" | **概述层声明无交互，实现原理层强耦合** | GWFD-010101 §8 #3 | 建模 `flow_depends_on`（010101→010105，流程级依赖）；区分配置依赖与流程依赖 |
| **3.5** | WSFD-010301（鉴权功能） | 三代概述均声明"不涉及与其他特性的交互" | WSFD-106003 子特性 B（SGSN/MME 卡类型控制）**依赖 WSFD-010301**（UNC 需通过鉴权参数判断 SIM/USIM 卡类型）；WSFD-011305 也仅声明依赖 011306 未提及 010301 | **两套鉴权体系并列，文档互不引用** | WSFD-010301 §8.1 #5 + WSFD-106003 §8.1 #6 | 建模 `strong_depends_on`（106003_B→010301）；底层 AKA 与 APN 业务鉴权并列建模，隐式协同无直接信令耦合 |
| **3.6** | WSFD-011307（Radius 抄送） | 特性概述明确声明"本特性不涉及与其他特性的交互" | 功能语义上与 WSFD-011305（鉴权）、WSFD-011306（Radius 功能承载）强关联；是 011306 的并行扩展能力（共享配置对象 + 参数级扩展 PRIFLAG=CARBON_COPY） | **声明独立但功能强关联** | WSFD-011307 §8.2 + §8.3 | 建模 `parallel_extends`（011307→011306，配置对象共享）；FeatureRelation 非 parent_of 而是 `config_object_shared` |
| **3.7** | GWFD-020411（MPLS VPN） | 特性概述声明"不涉及与其他特性的交互" | 隐性依赖 IGP/MPLS/BGP 基础特性；与 GRE/IPSec/L2TP 存在同域并列可选关系（横向对比） | **显式无交互，隐性依赖基础协议** | GWFD-020411 §9.2 #5 | 不建显式 FeatureRelation；标注 `implicit_depends_on=IGP/MPLS/BGP` 元数据 |
| **3.8** | GWFD-020412（L2TP VPN）与 GWFD-020421（基于位置） | L2TP 特性概述仅列 010108/020482 互斥，**未声明与 020421 互斥** | GWFD-020421 文档明确声明"不支持与 L2TP VPN 同时应用"（控制项 82200BVC）；地址分配主体不同（LNS 远程 vs UDG 位置本地池）逻辑互斥 | **互斥声明单向**（020421 声明，020412 未声明） | GWFD-020412 §8.1 #6 + GWFD-020421 §8 #5 | 建模 `mutually_exclusive`（020412↔020421）双向；FeatureRule `FR-LOC-L2TP-EXCL` 以 020421 文档为准 |

---

## 4. 文档缺口清单

> 以下为各 feature-knowledge §8 章节识别的**文档覆盖度不足项**。Stage 3 需从 OM 命令手册、业务专题、命令字典等补充。

| # | 缺口类型 | 涉及特性 | 缺口描述 | 影响 | Stage 3 补充来源建议 |
|---|---------|----------|---------|------|---------------------|
| **4.1** | 无 MML 激活脚本 | GWFD-020411 / WSFD-104411（MPLS VPN）<br>WSFD-107010（UPF 选择）<br>WSFD-010504（控制面地址分配）<br>WSFD-104413 / WSFD-104005（DHCP） | MPLS 9 篇全为概念/原理，无激活/调测/参考信息；UPF 选择仅 1 篇概述无完整脚本；010504 无独立脚本仅 14 条命令清单；DHCP 仅 2 篇无端到端脚本 | 配置实操无端到端参考；ConfigObject 节点无法从文档直接补全 | OM 命令手册各命令独立说明 + UDG/UNC 初始配置与调测 + 业务专题文档 |
| **4.2** | 仅 1 篇概述 | WSFD-107010（UPF 选择） | 仅 1 篇特性概述，无独立参考信息/激活/调测文档；无告警/软参/测量指标 | 作为网元选择类核心特性，文档精简至仅原理与原则表 | 业务专题 `UNC UPF选择专题/特性映射与交互_72976829.md` + OM 命令手册 |
| **4.3** | 4G/5G 指向外部手册 | GWFD-010101（会话管理 UDG）<br>WSFD-010501（会话管理 UNC） | 4G/5G 实现原理均指向外部手册；2/3G 实现原理为纯流程示意图（.png）无文字描述；5G 遵循标准仅引用 23.502（23.501 由 010105 引用） | 4G/5G 流程细节需查外部手册 | UDG/UNC 会话管理产品手册 |
| **4.4** | 子特性未完整描述 | WSFD-106003（双特性合一） | 配置树"APN接入权限"描述仅覆盖子特性 B 的部分能力（根据签约 ARD 控制），遗漏子特性 A（5GC 移动性接入限制）和子特性 B 的卡类型控制 | 图谱建模可能遗漏子特性维度 | 两个子特性独立文档（AMF + SGSN/MME） |
| **4.5** | 命令清单不完整 | GWFD-010104（地址分配总览）<br>GWFD-010105（用户面分配）<br>GWFD-020421（基于位置）<br>WSFD-010202（对等网元选择） | 010104 仅外部地址分配方式有脚本；010105 子方式分类文档清单概括不全（实际 4 种）；020421 全局开关 SET IPALLOCBYLOCSW 在操作步骤提及但参考信息未列出；010202 的 ADD SGSNDNS/SET MSCSELPLCY 未进入参考信息正式清单 | 命令体系不完整，ConfigObject 可能遗漏 | OM 命令手册对应命令独立说明 |
| **4.6** | C-U 协同细节缺失 | GWFD-010151（接入控制 UDG）<br>WSFD-104413（DHCP） | 010151 仅描述 C 面"与周边网元协商带宽资源"未列出具体 PFCP 信元名（MBR/GBR/Session AMBR）；104413 未明确与 UDG 侧 C-U 协同约束 | C-U 接口细节缺失 | 对照 GWFD-010224 N4 接口特性 + GWFD-010104/GWFD-010105 确认池网段一致性 |
| **4.7** | License 信息偏差 | GWFD-010104 / GWFD-010105 / WSFD-010502 / WSFD-010504 / WSFD-010301 / WSFD-010400 / WSFD-010501 / WSFD-011305 / WSFD-011306 等多个★核心特性 | 文档清单标注"[★核心]"（通常暗示需 License），但产品文档实际声明"无需 License" | License 约束建模可能错误 | 以各特性产品文档"可获得性"章节为准 |
| **4.8** | 文档内部不一致 | GWFD-010105（示例笔误 testpoo11）<br>GWFD-020421（V6PREFIXSTART 字段名笔误 / IPv6 PDP address 显示 IPv4）<br>GWFD-010151（CARSHAPESWUL/DL 步骤未列但脚本使用）<br>GWFD-020406（变体 5 License 用 LKV3G5LBAA01 而非 LKV3G5P6PD01） | 文档示例字段名/参数名/版本笔误；变体 5 可能实际属于 GWFD-020421 的 IPv6 扩展 | 图谱建模可能沿用错误参数 | 以激活脚本原样保留并标注；变体 5 需 Stage 3 澄清归属 |
| **4.9** | 测量指标/告警缺失 | GWFD-010151（接入控制）<br>WSFD-011307（Radius 抄送）<br>WSFD-010502（地址分配 UNC） | 010151 参考信息"无相关测量指标"但涉及带宽/丢包核心可观测量；011307 三项（告警/软参/指标）均无；010502 全部为"无" | 运维观测能力缺失，需依赖通用统计 | 可能在 UDG 侧或独立参考信息文档 |
| **4.10** | Radius 分配方式无脚本 | WSFD-010502（地址分配 UNC） | 仅 2 个子场景（静态 IP 段→UPF 绑定、静态地址黑名单）有完整 MML 脚本；Radius/SMF 本地池/DHCP 三种方式仅原理无脚本 | 另三种方式激活脚本需参考关联特性 | WSFD-011306 / WSFD-104413 等关联特性 |

---

## 5. Stage 3 cross-analysis 待解决问题清单（12 个）

> 以下为各 feature-knowledge §8 章节及四维度归纳 §6 收集的待解决问题。Stage 3 需横向分析时逐个验证，每个问题已标注来源特性与验证方向。

### 5.1 地址分配域（5 个）

| # | 问题 | 来源特性 | 验证方向 | 图谱建模影响 |
|---|------|---------|---------|-------------|
| **Q1** | **WSFD-010504 的 ALLOCPRECEDENCE 决策边界**：在何种场景下选择"SMF 本地分配"而非"UPF 本地分配"？两者并存时地址冲突如何避免？ | WSFD-010504 §8.3 + 四维度 §6.1 | 横向核对 GWFD-010105 ALLOCPRECEDENCE=UPF_FIRST vs WSFD-010504 ALLOCPRECEDENCE=SMF_ALLOC 的互斥场景 | DecisionPoint `DP-ADDR-MODE` 取值空间需含 `SMF_ALLOC` 独立分支；FeatureRule `FR-CU-ALLOC-EXCL` 建模 C/U 二选一 |
| **Q2** | **Radius 地址分配的端到端链路信元映射**：GWFD-010105 子方式 4（UDG 侧基于 Radius 下发池名）↔ WSFD-011306（UNC 侧 Radius 功能）↔ WSFD-010502（UNC 侧 Radius 分配决策），三者完整链路的 PFCP/Radius 信元映射 | GWFD-010105 §8 + 四维度 §6.2 | Stage 3 绘制时序图：Radius Access-Accept → SMF → PFCP Framed-Pool → UPF 解析池名 | SemanticObject `SO-ADDRESS-POOL` 需建模 `radius_pool_chain=true`；FeatureRule 建模三特性级联 |
| **Q3** | **WSFD-104004（IPv6 PD UNC）的 3 个强依赖具体内容**：文档声明 3 条强依赖（WSFD-104001/WSFD-011306/WSFD-104002），具体依赖条件与场景组合 | WSFD-104004 §8.2 + §8.3 + 四维度 §6.3 | 读取 WSFD-104004 完整交互章节确认：104001（承载底座强依赖）、011306（Radius 获取 PD 网段强制）、104002（双栈+PD 叠加条件依赖） | FeatureRule `FR-IPV6-PD-CASCADE` 建模 3 条依赖链 |
| **Q4** | **SET APNADDRESSATTR 在 010104 与 010105 中的参数用法差异**：010104 用 HOSTROUTEIP，010105 用 SUPPORTIPV4/V6/IGNOREV4/V6POOLID，是否为同一命令的不同参数用法 | GWFD-010104 §9 #1 | Stage 3 跨特性核对 SET APNADDRESSATTR 命令参数集 | ConfigObject `APNADDRESSATTR` 需建模 `shared_by=[010104,010105]`；参数维度按特性分离 |
| **Q5** | **GWFD-020406 变体 5（基于位置）的 License 归属**：变体 5 激活脚本使用 LKV3G5LBAA01（基于位置）而非 LKV3G5P6PD01（PD License），是否实际属于 GWFD-020421 的 IPv6 扩展而非 GWFD-020406 | GWFD-020406 §8 #11 | Stage 3 澄清变体 5 特性归属；核对前提条件指向 020421 而非 020406 根文档 | Feature 变体维度需区分；可能需将变体 5 从 020406 迁移至 020421 建模 |

### 5.2 接入方式域（3 个）

| # | 问题 | 来源特性 | 验证方向 | 图谱建模影响 |
|---|------|---------|---------|-------------|
| **Q6** | **WSFD-108007（终端二次鉴权）与接入方式（IPSec/GRE）的场景关联**：108007 文档未直接引用 IPFD-016000/015002，但归类 MEC 解决方案 + UPF 下沉场景天然关联 | 四维度 §6.4 | Stage 3 验证企业专网典型组网中二次鉴权与 IPSec/GRE 隧道的协同配置 | FeatureRule 可能需建模 `co_deployed`（108007 + IPSec/GRE 在企业 DN 场景） |
| **Q7** | **GWFD-020412（L2TP）与 GWFD-020421（基于位置）的互斥双向声明**：020421 声明互斥，020412 未声明，是否需在 020412 补充反向声明 | GWFD-020412 §8.1 #6 + GWFD-020421 §8 #5 | Stage 3 结合 020421 文档验证是否双向声明；语义级互斥（地址分配主体不同）是否成立 | FeatureRule `FR-LOC-L2TP-EXCL` 需双向建模 |
| **Q8** | **MPLS VPN 的 MML 命令补全**：9 篇文档无激活/调测/参考信息，核心配置对象（VRF + RD + VPN Target + MP-BGP）的命令需从何处补全 | GWFD-020411 §9.1 #6 + §9.2 #8 | Stage 3 从 UDG 命令字典补全 ADD/MOD VPNINSTANCE、配置 BGP VPNv4 对等体等命令 | ConfigObject 节点补全；标注 `source=命令字典补全` |

### 5.3 鉴权域（2 个）

| # | 问题 | 来源特性 | 验证方向 | 图谱建模影响 |
|---|------|---------|---------|-------------|
| **Q9** | **底层 AKA（WSFD-010301）与 APN 业务鉴权（WSFD-011305）的隐式协同建模**：两套鉴权体系文档互不引用，但执行时序上 AKA 先发生、业务鉴权后发生 | 四维度 §6（鉴权 §2.2） | Stage 3 验证隐式协同是否建模为 FeatureRule 或保持独立并列 | 建议 FeatureRelation 建模 `implicit_sequence`（010301 → 011305 时序）；非强依赖 |
| **Q10** | **AUTHMODE 与地址空间归属联动是否建模**：TRANS_NON_AUTH 属运营商地址空间，NON_TRANS/TRANS_AUTH 属 ISP/企业网地址空间 | 四维度 §6.6 | Stage 3 验证此联动是否在图谱中建模为 FeatureRule | FeatureRule `FR-AUTH-ADDRSPACE` 建模鉴权方式与地址空间归属的联动约束 |

### 5.4 地址类型/IPv6 域（2 个）

| # | 问题 | 来源特性 | 验证方向 | 图谱建模影响 |
|---|------|---------|---------|-------------|
| **Q11** | **RA（Router Advertisement）机制的 License 归属**：RA 在 GWFD-020401（IPv6 承载）、GWFD-020403（双栈独有主动下发）、GWFD-020406（PD 步骤 12）中共享描述，RA 实际归属哪个 License 控制（V6PB01/VDSA01/P6PD01） | GWFD-020406 §8 #12 + GWFD-020403 §8 | Stage 3 横向核对三特性 RA 机制的 License 控制归属 | SemanticObject 需区分 RA 生成归属；FeatureRule 可能需建模 `RA_belongs_to` 多 License |
| **Q12** | **多 PDN/PDU 场景下每会话地址类型独立决策**：WSFD-010503 支持单用户 11 PDN（EPC）/ 15 PDU（5GC），多会话场景下每个会话的地址类型可独立决策（IPv4/IPv6/双栈混发）？ | 四维度 §6.5 | Stage 3 验证多会话地址类型的独立性 | DecisionPoint `DP-ADDR-TYPE` 需标注 `per_session=true`；FeatureRule 无跨会话约束 |

---

## 6. 计数统计（供 Stage 3 直接引用）

| 类别 | 计数 | 明细 |
|------|------|------|
| **1. 配置树/意图澄清修正** | **11 处** | 双栈能力使能层(1.1)、010504并列子集(1.2)、APNL2TPATTR/CTRL不对称(1.3)、IPV4ALLOCTYPE实为PFCP BIT(1.4)、010202网元为SGSN/MME(1.5)、010151/106003非对称(1.6)、106003双特性合一(1.7)、106203双视角反转(1.8)、010104/010105父子(1.9)、104001单向依赖矛盾(1.10)、MPLS文档缺口(1.11) |
| **2. C-U 关系模式分类** | **4 种模式** | A.对称同构(GRE/IPSec/MPLS/静态冗余) + B.C决策U执行(L2TP) + C.决策执行分离(地址分配/IPv6/会话管理) + D.非对称同名(接入控制010151/106003) |
| **3. 依赖声明矛盾** | **8 对** | 104001被104002/104004强依赖(3.1)、107010被010502单向引用(3.2)、015004源地址互斥(3.3)、010101流程耦合010105(3.4)、010301被106003_B依赖(3.5)、011307与011306配置共享(3.6)、020411隐性依赖IGP/BGP(3.7)、020412↔020421互斥单向(3.8) |
| **4. 文档缺口** | **10 类** | 无MML脚本(4.1)、仅1篇概述(4.2)、4G/5G指向外部手册(4.3)、子特性未完整(4.4)、命令清单不完整(4.5)、C-U协同细节缺失(4.6)、License信息偏差(4.7)、文档内部不一致(4.8)、测量指标缺失(4.9)、Radius分配无脚本(4.10) |
| **5. Stage 3 待解决问题** | **12 个** | 地址分配域5个(Q1-Q5) + 接入方式域3个(Q6-Q8) + 鉴权域2个(Q9-Q10) + 地址类型/IPv6域2个(Q11-Q12) |

---

## 附录 A：本修正清单涉及的全部特性（37 个）

### 地址分配域（18 个）
- **UDG 侧**：GWFD-010104（总览）、GWFD-010105（用户面分配）、GWFD-020421（基于位置）、GWFD-010107（静态路由冗余）、GWFD-010108（地址自动检测，互斥对象）
- **UDG IPv6**：GWFD-020401（IPv6 承载）、GWFD-020403（IPv4v6 双栈）、GWFD-020406（IPv6 PD）
- **UNC 侧**：WSFD-010502（地址分配方式）、WSFD-010504（控制面地址分配方式）、WSFD-104002（IPv4v6 双栈）、WSFD-104001（IPv6 承载）、WSFD-104004（IPv6 PD）、WSFD-104005（DHCPv6）、WSFD-104413（DHCP）、WSFD-010503（多 PDN/PDU）、WSFD-107010（UPF 选择）、WSFD-107021（静态地址路由冗余 C 侧）

### 鉴权计费域（5 个）
- **底层鉴权**：WSFD-010301（2G&3G/4G/5G AKA 系列）
- **APN 业务鉴权**：WSFD-011305（Radius 鉴权接入）、WSFD-011306（Radius 功能）、WSFD-011307（Radius 抄送）、WSFD-108007（终端二次鉴权）

### 接入方式域（5 个，含 C-U 对称对）
- **GRE**：IPFD-015002（UDG+UNC 双侧同构）
- **IPSec**：IPFD-015004（UDG）+ IPFD-016000（UNC）对称
- **MPLS VPN**：GWFD-020411（UDG）+ WSFD-104411（UNC）对称
- **L2TP VPN**：GWFD-020412（UDG，C-U 非对称）+ WSFD-104410（UNC）

### 会话/用户数据/接入控制/别名域（9 个）
- **会话管理**：GWFD-010101（UDG）+ WSFD-010501（UNC）
- **用户数据**：WSFD-010400
- **对等网元选择**：WSFD-010202（SGSN/MME，Pre-5G）
- **接入控制**：GWFD-010151（UDG 带宽流控）+ WSFD-106003（UNC 接入权限，双特性合一）
- **别名 APN**：WSFD-106203（双视角语义反转）

---

## 附录 B：Evidence 占位映射规范

本文件全部结论使用统一占位 `EV-TK-修正`。Stage 4 实例化时按以下规则展开：

| 结论标注 | 展开规则 |
|---|---|
| `[GWFD-xxxxx §8]` 或 `[WSFD-xxxxx §8]` | 展开为该特性 feature-knowledge 文件 §8 章节的 `EV-FK-xx` 占位 |
| `[GWFD-xxxxx §8 + WSFD-yyy §8]` | 展开为两侧特性 §8 章节 EV-FK-xx 的组合 |
| 四维度归纳 §6 来源 | 展开为 `归纳-四维度决策与机制.md` 的 `EV-TK-归纳` 占位 |

---

**文档版本**：v1.0（Stage 2 修正清单汇总）
**完成时间**：2026-06-22
**上游来源**：37 篇 feature-knowledge §8 章节 + 四维度归纳 §6 预留问题
**下游消费者**：Stage 3 cross-analysis（横向验证 12 个待解决问题）→ Stage 4 DecisionPoint/SemanticObject/FeatureRule 实例化
