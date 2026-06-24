# APN 业务域 topic-knowledge：APN 底座三维度归纳（会话管理 / 网元选择 / 接入控制）

> **定位**：Stage 2 维度归纳层。补充《归纳-四维度决策与机制.md》未覆盖的 3 类**底座类特性**（会话管理 / 网元选择 / 接入控制），即不直接产生 DecisionPoint 决策、但为决策提供"宿主流程 / 签约数据 / 网元实例 / 接入权限"输入的基础特性。
> **数据源**：仅基于 feature-knowledge（不再回读产品文档）。
> **来源特性标注规范**：每条结论后括注 `[GWFD-xxxxx]` 或 `[WSFD-xxxxx]`；多特性共同支撑用 `+` 连接。
> **Evidence 占位**：本文件全部结论使用统一占位 `EV-TK-底座`（Stage 4 实例化时映射到具体 feature-knowledge 的 EV-FK-xx）。

---

## 0. 元数据

| 字段 | 取值 |
|------|------|
| topic_id | TK-APN-底座三维度 |
| topic_name | APN 底座三维度（会话管理 / 网元选择 / 接入控制） |
| topic_layer | 1（DecisionPoint / SemanticObject 输入来源 + FeatureRule 候选） |
| source_feature_count | 8 个底座特性（会话管理 5 + 网元选择 2 + 接入控制 2，部分跨域） |
| source_evidence_ids | EV-TK-底座 |
| downstream_consumers | Stage 3 cross-analysis；Stage 4 DecisionPoint/SemanticObject/FeatureRule 实例化 |
| 配套文件 | 《归纳-四维度决策与机制.md》（互补，共同覆盖 APN 业务域全部特性） |

### 三类底座定位速查

| 底座类别 | 特性数 | 核心角色 | 产出形态 |
|---------|-------|---------|---------|
| 会话管理底座 | 5 | 宿主流程 + 签约数据源 + 并发治理 + APN 映射 | SemanticObject（会话上下文/签约数据/APN映射表） |
| 网元选择底座 | 2 | 网元实例决策（UPF / 对等控制面网元） | DecisionPoint 输入（网元选择决策） |
| 接入控制底座 | 2 | 接入权限 + 用户面带宽流控 | DecisionPoint（允许/拒绝）+ FeatureRule（带宽约束） |

---

## 1. 维度一：会话管理底座（5 特性）

### 1.1 纯描述性根底座：GWFD-010101(U) + WSFD-010501(C)

**关键结论**：会话管理是 APN 域的**纯描述性根底座** —— 无 MML、无 License、无独立配置对象，PDU/PDN/PDP 会话由控制面 PFCP/GTP-C 信令被动触发。

| 维度 | GWFD-010101（UDG/U 面） | WSFD-010501（UNC/C 面） |
|------|------------------------|------------------------|
| 网元角色 | GGSN-U / SGW-U / PGW-U / UPF | SGSN / MME / SGW-C / PGW-C / GGSN-C / SMF / AMF |
| 决策/执行 | 执行方（无决策权） | 决策方（建/改/放 + 在哪里建） |
| License | 无 [GWFD-010101][WSFD-010501] | 无，且无需配置即可使用 [WSFD-010501] |
| MML 命令 | **无专属 MML**（16 个源文档均无 MML）[GWFD-010101] | 仅 2/3G 维护命令（ADD/MOD/RMV/LST PDPAPN、SET GBSM/IUSM、SET SMPDUCTRL）[WSFD-010501] |
| 配置对象 | **无独立配置对象**（分散在 N4 接口、APN、地址池、PCC、签约中）[GWFD-010101] | 无（底座特性）[WSFD-010501] |
| 触发方式 | 控制面 PFCP/GTP-C 被动触发 | UE NAS 信令触发（注册/附着/RAU/TAU） |

**C-U 协同分工**（强语义耦合但文档明示"不涉及交互"）[GWFD-010101][WSFD-010501]：
- UNC（C 面）决策"何时建/改/放 + 在哪里建"，通过 PFCP Session Establishment/Modification/Deletion 下发 PDR/FAR/URR/QER
- UDG（U 面）按 C 面指示安装规则、分配 F-TEID、执行报文检测/转发/QoS/上报
- 接口：N4（5G）/ Sxa/Sxb（4G CUPS）/ Gn/Gp（2-3G）

**代际覆盖差异**：
- 5G/4G 首发版本 20.0.0；**2/3G 首发版本 20.3.0/20.3.2**（后向补全）[GWFD-010101][WSFD-010501]
- 会话管理对象演进：PDP 上下文（2/3G）→ EPS 承载（4G）→ PDU 会话 + QoS Flow（5G）[WSFD-010501]
- 5G 新增 **SSC Mode**（SSC1 IP 连续 / SSC2 先断后连 / SSC3 先连后断）+ **已有 PDU 会话用户面连接的选择性激活/去激活**（节约无线资源）[WSFD-010501]

> EV-TK-底座: 纯描述性底座判定（无 MML、无 License、无独立配置对象、被动信令触发）

### 1.2 多 PDN/PDU 并发治理：WSFD-010503

**关键结论**：WSFD-010503 是 WSFD-010501 的**多实例并发治理层**，不引入新会话机制，仅判"能否再开一个并发会话"。

| 维度 | WSFD-010501（单会话） | WSFD-010503（并发治理） |
|------|---------------------|----------------------|
| 定位 | 单 PDN/PDU 建立/修改/释放流程 | 单 UE 多 PDN/PDU 并发实例并存与上限治理 |
| 流程复用 | 定义基础会话流程 | 每个并发实例复用 010501 的建立流程 |
| 关键判定 | 单会话鉴权/资源不足拒绝 | 并发超限拒绝 |
| IP 地址 | 分配机制 | EPC 下每个 PDN 连接独立 IP（PGW-C 分配） |

**并发规格（文档依据）**[WSFD-010503]：
- **EPC 单用户全局 PDN 上限：11**（超 11 时 MME 拒绝）
- **5GC 单用户全局 PDU 上限：15**（超 15 时 SMF 拒绝）
- **单 APN 粒度可配**（仅 EPC）：`ADD APNACTNUM`（PDNNUM/IPV4ADDRNUM/IPV6ADDRNUM + PDNCONNREJCAUSE）
- 5GC 当前文档**未提供单 DNN 粒度配置**（代际不对称）

**拒绝原因值**：`MULTI_PDN_FOR_APN_NOT_ALW_55`（EPC 单 APN 超限）[WSFD-010503]

**软参**：`DWORD1021 BIT1` —— 多 PDN 场景 TEID=0 并存控制（是否删除已有 TEID=0 的 PDN 连接）[WSFD-010503]

> EV-TK-底座: 并发治理层定位 + 全局/单 APN 双层上限 + 代际不对称（5GC 无单 DNN 配置）

### 1.3 签约数据基础底座：WSFD-010400

**关键结论**：WSFD-010400 是 APN 域**签约数据唯一数据源** —— 所有 APN/DNN 签约、QoS、APN-AMBR、PDN Address（静态 IP）、ARD、APN-OI Replacement 均由本特性从 UDM/HSS/HLR 下发。

**两类数据 × 三代际演进**[WSFD-010400]：

| 代际 | 后端数据库 | 接口（协议） | UNC 侧控制面 NF |
|------|----------|-------------|----------------|
| 5G | UDM | Nudm（SBA / HTTP/2） | AMF、SMF |
| 4G | HSS | S6a（Diameter） | MME |
| 2/3G | HLR + HSS | Gr（MAP）+ S6d（Diameter） | SGSN |

**5G Nudm 服务族（SBA 双服务）**[WSFD-010400]：
- **Nudm_SDM**（Subscriber Data Management）：Get / Subscribe / Unsubscribe / Notification
- **Nudm_UECM**（UE Context Management）：Get / Registration / Deregistration / Update(仅 AMF) / DeregistrationNotification(仅 AMF)

**UDM 静态分配是地址分配方式的唯一数据源**（与 WSFD-010502 强纵向链路）[WSFD-010400]：
- 5G：SMF 调用 `Nudm_SDM_Get` 获取 UE 在 UDM 签约时确定的静态 IP/前缀 → 决策地址分配方式为 UDM 静态
- 4G：MME 从 HSS 获取 PDN Address（静态），通过 Create Session Request 的 PAA 信元下发
- 2/3G：SGSN 验证 UE 提供的 PDP 地址与 HLR 签约记录

**反向数据流（UNC → 后端）**：4G `Notification` 流程通知 HSS "动态分配给 APN 的 PDN 网关的分配/更改/移除"，用于 HSS 后续 PDN GW 选择（静态保持不变，动态可更新）[WSFD-010400]

**签约数据存储分拆**：`SET SYS SUBSTORAG` 控制 GPRS/EPS 签约数据分开存储（10 公有字段中 8 个可分开）；修改后**在用户发生移动性管理流程时生效**（非立即）[WSFD-010400]

**关键签约字段（APN 域相关）**[WSFD-010400]：
- APN/DNN 签约（Context ID、PDN Type、PDN Address 静态、QoS profile、APN-AMBR、VPLMN Address Allowed、PDN GW identity、PDN GW Allocation Type 静态/动态）
- APN-OI Replacement（用户级 + APN 级，APN 级优先级更高）
- APN-PDN 网关 ID 关系列表（含野卡 APN 的 PDN 签约上下文）
- 3GPP-Charging-Characteristics（计费属性）
- Access-Restriction-Data / Subscriber-Status / ODB（接入限制，供 WSFD-106003 读取）

> EV-TK-底座: 签约数据唯一源 + Nudm 双服务族 + 反向数据流（UNC→HSS）+ 存储分拆延迟生效

### 1.4 别名 APN：同特性 ID 的双视角语义反转（WSFD-106203）

**关键结论**：WSFD-106203 是 APN 域**最特殊的特性** —— 同一特性 ID 在两套网元下**映射方向相反**，必须在图谱中拆分为两个 Feature 变体节点避免规则匹配混淆。

| 维度 | SGSN/MME 侧 | GGSN/PGW-C/SMF 侧 |
|------|-------------|-------------------|
| 映射方向 | 协商 APN → **别名 APN** | **别名 APN** → 真实 APN |
| "别名 APN" 含义 | 映射后的目标 APN（用于 DNS） | 用户传来的待映射 APN |
| "真实 APN" 含义 | 映射前的协商 APN | 映射后的目标 APN（业务资源） |
| 用途 | DNS 解析屏蔽（节约 DNS 资源） | 业务资源归一（多 APN 共用资源） |
| 匹配维度 | IMSI 最长匹配 + 协商 APN | 用户范围（ALL_USER / 切片 SST+SD）+ 别名 APN |
| 命令族 | `ADD ALIASAPN`（注意命名差异） | `ADD APNALIAS` |
| License | `82207546 LKV2ALIASAPN02` | `82200BNM LKV2AAPN01` |
| HLR 签约 | **无需签约**（协商之后转换） | 转换 APN 必须已 `ADD APN` |
| 规格 | 1024 条映射记录 | 1000 别名 + 500/APN |

**双条件约束（SGSN/MME 侧）**[WSFD-106203]：IMSI 号段匹配 **AND** 协商 APN 在映射表中，两条件**同时满足**才执行转换。

**顺序约束**：用户携带错误 APN 时，**先执行 APN 纠错（WSFD-106004），再执行别名 APN 纠正**[WSFD-106203]

**5G 切片查询顺序**：5G 用户**先按指定切片（SST+SD）查询，未中再按 ALL_USER 查询**[WSFD-106203]

**流程位置**：别名 APN 是 APN 协商（WSFD-010501 APN 选择子流程）之后、PDU 会话建立/DNS 解析之前的**映射预处理环节**[WSFD-106203]

**Stage 4 建议**：将本特性拆分为两个 Feature 变体节点（通过 `variant_dimensions` 的"网元角色视角"维度区分），避免规则匹配时语义混淆[WSFD-106203]

> EV-TK-底座: 同特性 ID 双视角语义反转 + 双 License + 命令族命名差异 + 5G 切片查询顺序

### 1.5 会话管理底座共性

| 共性 | 依据 |
|------|------|
| 全部无 License（除 WSFD-106203 双 License） | [GWFD-010101][WSFD-010501][WSFD-010503][WSFD-010400] |
| 全部"不涉及与其他特性的交互"（文档明示）但强语义耦合 | [GWFD-010101][WSFD-010501][WSFD-010503][WSFD-010400][WSFD-106203] |
| 2/3G 发布版本晚于 4G/5G（20.3.0/20.3.2 vs 20.0.0） | [GWFD-010101][WSFD-010501][WSFD-010400] |
| 告警/软参多数为"无"（底座特性，观测点在子特性或 U 面） | [WSFD-010501][WSFD-010503][WSFD-010400] |

---

## 2. 维度二：网元选择底座（2 特性）

### 2.1 WSFD-107010 UPF 选择（5G，三轮筛选机制）

**关键结论**：UPF 选择采用**三轮递进筛选**机制，文档仅 1 篇特性概述（**无完整 MML 脚本、无独立调测、无告警/软参/测量指标**），是 APN 域文档缺口最大的特性。

**三轮筛选机制**[WSFD-107010]：

```
第一轮：必选条件（所有条件同时满足，无优先级）
  ① DNN 匹配       (ADD PNFDNN)
  ② S-NSSAI 切片   (ADD PNFNS)
  ③ 位置区匹配     (ADD UPAREA / ADD UPAREABINDN2TAI)
  ④ DNAI 匹配      (ADD PNFDNAI, 由 DNN 映射)
  ⑤ 接口能力       (UPF 上报, 如需 N6 须支持 N6)
  ⑥ EPS 互通       (ADD PNFUPFINFO, 4/5G 互操作)
  ⑦ 分流能力       (ADD UPNODE)
  → 全部不满足 = UPF 选择失败；仅 1 个满足 = 选择完成
        ↓ 多个满足
第二轮：优选条件（按策略次序，可配优先级）
  SET UPSELECTPRI（第一优先级默认 COMBINED, 第二优先级默认 LOCS11PRIORITY）
  SET UPSELECTFLAG（PRIORITYFLAG / AMBRUPFFLAG / N3UPFAPNFLAG / ULISGWFLAG）
  SET APNUPSELPLY（COMBINEPRISTG 用户位置区/合一UPF/优先级顺序）
        ↓ 仍多个满足
第三轮：权重 + 负载最终选择
  ① 权重（ADD PNFPROFILE WEIGHT, 加权随机，权重=容量）
  ② 负载（SET UPLOADBALANCE, UPF 偶联消息上报，优先选低负载）
```

**License**：`82209917 LKV2USBL01 UPF选择` + `82200BES LKV2GWUS01 GW-U选择`（双 License）[WSFD-107010]

**硬约束**：**SMF 和 UPF 必须同时为 HUAWEI 设备**[WSFD-107010]

**UPF 角色体系**[WSFD-107010]：
- 主锚点 UPF（PSA，PGW-U 角色）：根据是否支持 4/5G 互操作判断 EPS 互通能力
- I-UPF（中间 UPF / 接入锚点，SGW-U 角色）：`N3UPFAPNFLAG` 控制选 I-UPF 时 DNN 是否为选择条件
- 合一 UPF（SGW-U/PGW-U 合一 / 主锚点与 I-UPF 合一 / 辅锚点与分流节点合一）：第二轮优选条件之一

**4G 接入特殊处理**：4G 用户接入 EPC 时 SGW-C/PGW-C 选 SGW-U/PGW-U **不使用切片信息**，`ADD PNFDNN` 的 `PNFNSINDEX` 建议保持默认值 0[WSFD-107010]

**子特性包含关系**：WSFD-107005 GW-U 选择 + WSFD-107006 支持基于位置的 GW-U 选择 + WSFD-107008 支持基于权重的 GW-U 选择[WSFD-107010]

### 2.2 WSFD-010202 对等网元选择（Pre-5G，DNS 域名聚合）

**关键结论**：WSFD-010202 是 **Pre-5G（2G/3G/4G）控制面对等网元（SGSN/MME/MSC）选择**特性，与 WSFD-107010（5G U 面选择）**代际互补、机制完全不同**。

**核心机制：DNS 域名聚合**[WSFD-010202]：

| 映射方式 | 实现 | 效果 |
|---------|------|------|
| 映射到起始 LAI/RAI/TAI | `ADD AREADNS`（LAC+LACRANGE / RAC+RACRANGE / TAC+TACRANGE, ZONESW=NO） | 保留位置语义，聚合区域集合到起始码 |
| 映射到 ZONE 名称 | `ADD AREADNS`（ZONESW=YES + ZONENAME） | 脱离具体位置，纯运维命名 |

**价值**：将一定范围的 LAI/RAI/TAI 聚合为单一 DNS 域名，**大幅减少 DNS 配置记录数量**（定制前每区域码一条记录，定制后整集合一条）[WSFD-010202]

**触发流程与查询目标**[WSFD-010202]：
- Attach / RAU / TAU → 查询源侧 SGSN（LAI/RAI）
- Handover / Relocation → 查询目标侧 SGSN/MME（LAI/RAI/TAI）
- SRVCC → 查询目标 MSC（LAI/RAI，通过 `SET MSCSELPLCY` 选择基于 RAI FQDN 或 LAI FQDN）

**测量指标**：启用后 `117470813 DNS 服务器查询总次数` **降低**（聚合后查询次数减少）[WSFD-010202]

**License**：**无需 License**（与 WSFD-107010 双 License、GWFD-020421 License 82200BAK 显著不同）[WSFD-010202]

### 2.3 与地址分配的关系（UPF 选择决定地址分配侧）

**关键结论**：UPF 选择决策**直接决定地址分配的执行侧** —— SMF 选定 UPF 后通过 N4 PFCP 建立会话，UPF 侧（GWFD-010101 + GWFD-010105）执行用户面会话与地址分配。

**UPF 选择 vs 地址分配 冲突协调**（WSFD-010502 §3.2.4 明确引用 WSFD-107010）[WSFD-107010]：
- 冲突场景：静态 IP 段绑定 UPF（由 `SET STATICADDRPARA` 配置）与 SMF 主锚点 UPF 选择结果冲突
- 协调规则：**SMF 选择的主锚点 UPF 优先级更高**
- 文档引用方向：**单向引用** —— 地址分配侧感知冲突，UPF 选择侧声明"不涉及与其他特性的交互"

**共用配置对象**：`ADD UPNODE` —— 地址分配侧用 `ADDRALLOCMODE=INHERIT` 参数，UPF 选择侧用位置特征与分流能力参数（同一命令，不同参数维度）[WSFD-107010]

### 2.4 网元选择底座共性

| 共性 | WSFD-107010 | WSFD-010202 |
|------|------------|------------|
| 代际 | 5G（含 4/5G 互操作） | Pre-5G（2G/3G/4G） |
| 选择目标 | U 面网元（UPF） | C 面对等网元（SGSN/MME/MSC） |
| 核心机制 | 三轮多维属性筛选 + 权重/负载 | DNS 域名聚合 |
| License | 双 License | 无 |
| 文档完整度 | **缺口大**（1 篇概述，无 MML 脚本/调测/告警/软参/指标） | **完整**（5 文件齐全，3 个任务示例脚本） |
| 同厂商约束 | SMF 与 UPF 必须同为 HUAWEI | 无（DNS 是开放协议） |

---

## 3. 维度三：接入控制底座（2 特性）

### 3.1 WSFD-106003 双特性合一（AMF 移动性限制 + SGSN/MME ARD 权限）

**关键结论**：WSFD-106003 是**同一特性 ID 下两个实现独立的子特性** —— AMF 侧（5GC 移动性限制）与 SGSN/MME 侧（2/3/4G 签约 ARD/APN/卡类型），**控制依据、License、标准、适用 NF 全部不同**。

| 子特性 | AMF 侧 | SGSN/MME 侧 |
|--------|--------|-------------|
| 适用 NF | AMF（5GC） | SGSN、MME（2/3/4G） |
| 控制依据 | RAT 限制 + 核心网类型限制 | 签约 ARD + 签约 APN + 卡类型（SIM/USIM） |
| 数据来源 | UDM 签约 + AMF 本地配置 | HLR/HSS 签约（需 R6+ ARD）+ UNC 本地配置 |
| License | **无需** | **需 `82206571 LKV2ARD02`** |
| 遵循标准 | 3GPP 23.501/23.502/29.503/29.518 | 3GPP 29.002/29.272 |
| 首发版本 | 20.3.2（v02 20.11.0 加 RedCap） | 20.0.0 |
| 决策时机 | 注册/移动性注册更新/切换 | 附着/路由区更新 |

**AMF 侧决策优先级**（核心机制）[WSFD-106003]：
1. **本地配置匹配优先**：用户匹配 AMF 本地配置的接入限制记录 → 按本地配置执行
2. **签约数据兜底**：AMF 本地未配置或无匹配 → 按签约数据检查
3. **本地配置 Null = 允许**：本地配置 RAT/核心网限制均为 Null → 不论签约如何，**允许接入**
4. **本地配置用户范围优先级**：IMSI 前缀 > 外网用户 > 本网用户 > 所有用户

**AMF 侧 12 种决策组合**（文档表1，RAT 限制 × 核心网限制 × 本地/签约）[WSFD-106003]：核心结论是"本地匹配优先于签约、本地 Null 强制允许"

**SGSN/MME 侧三类控制方式**[WSFD-106003]：
- **方式1：签约 ARD 控制**（HLR/HSS R6+ ARD，AccessRestrictionData 信元 bit0=UTRAN/bit1=GERAN/bit4=E-UTRAN/bit6=NB-IoT，**1=拒绝**）
- **方式2：签约特殊 APN 控制**（HLR/HSS 签约特殊 APNNI 如 GERAN_USER/UTRAN_USER/E_UTRAN_USER，UNC 比对签约列表）—— **注意：不是 APN 黑白名单，是基于特殊 APNNI 签约的接入允许/拒绝**
- **方式3：卡类型控制**（仅 GERAN/UTRAN，通过鉴权三元组/五元组区分 SIM/USIM，**依赖 WSFD-010301 鉴权功能**）

**SGSN/MME 侧决策规则**[WSFD-106003]：
- 步骤1：IMSI 号段分类（匹配号段 → 步骤2；不匹配 → 允许）
- 步骤2-3：用户属性匹配（签约 ARD/APN/卡类型至少一个匹配 → 采取与配置相同策略；无匹配 → 采取相反策略）
- 步骤4-6：CTRLTYPE=ALLOW 允许 / REJECT 拒绝（携带 CAUSE）

**互操作 ARD 转换**（基于 N26 接口 EPS→5GS）[WSFD-106003]：
- 目标 AMF 将 4G 上下文 ARD 的 **ENA（WB-E-UTRAN Not Allowed）** 转换为 5G RAT 限制的 **EUTRA**
- 将 **NR in 5GS Not Allowed** 转换为 5G RAT 限制的 **NR**
- 基于 N26 的 EPS→5GS 切换，AMF 给 NG-RAN 下发的 MRL **只能携带 RAT Restriction**

**应用限制（AMF 侧）**[WSFD-106003]：
- **紧急注册跳过**接入控制检查
- **本地配置优先**于签约数据
- **存量用户不生效**：本地配置变更仅对新注册用户生效，已注册用户下一次移动性注册流程才生效

**与其他特性的顺序/依赖**[WSFD-106003]：
- AMF 侧：用户接入控制检查通过后，AMF 才进一步检查 WSFD-105003 区域漫游限制
- SGSN/MME 侧：卡类型控制**必须先启用 WSFD-010301 鉴权功能**（强依赖）

### 3.2 GWFD-010151 接入控制（U 面带宽流控）

**关键结论**：GWFD-010151 是 **U 面带宽维度的接入流控**，与 WSFD-106003（C 面接入权限）**机制完全不同，非 C-U 对称**。

**两种控制方式**[GWFD-010151]：
- **CAR（Committed Access Rate）带宽控制**：超出协商带宽的报文**直接丢弃**，未超出则转发（实现简单、无延迟、无抖动）
- **Shaping 流量整形**：使用 **GTS 队列 + 令牌桶**，超带宽报文**缓存而非立即丢弃**，缓满才丢（平滑流量、减少突发丢包，引入缓存延迟）

**令牌桶机制**[GWFD-010151]：
- 按"用户已协商的带宽速率"向桶中放置令牌
- 报文发送消耗令牌；令牌充足直接发送；令牌不足产生 GTS 队列，报文缓存
- GTS 周期性取报文与令牌比较，直至令牌不足或队列发送完毕；队列已满则丢弃

**配置对象极其精简**[GWFD-010151]：
```
APN 实例（ADD APN）
  └── APNQOSATTR 属性（SET APNQOSATTR）
        ├── CARSHAPESWUL（上行开关）+ CARSHAPEUL（上行方式 CAR/SHAPE）
        └── CARSHAPESWDL（下行开关）+ CARSHAPEDL（下行方式 CAR/SHAPE）
```
- 配置粒度：**仅 APN 级**，无法针对单用户单独配置
- 上下行独立：可分别选择 CAR 或 SHAPE，可上下行不同方式

**协商带宽来源（C 面下发）**[GWFD-010151]：SGW-C/PGW-C/SMF 与周边网元协商用户带宽资源 → 通过 N4/Sxa/Sxb 接口下发至 U 面 —— **具体 PFCP 信元文档未明示**（缺口，需对照 GWFD-010224 N4 接口特性验证）

**License**：无需 License[GWFD-010151]

### 3.3 ★两者非 C-U 对称（配置树归类需 Stage 3 重审）

**关键发现**：GWFD-010151 与 WSFD-106003 **不是同一控制目标在 C/U 面的分工**，而是**两类独立机制**，必须在图谱中明确区分。

| 对比维度 | GWFD-010151（U 面） | WSFD-106003（C 面） |
|---------|--------------------|---------------------|
| 网元角色 | SGW-U/PGW-U/UPF | **SGSN/MME/AMF**（注：文档实际为 SGSN/MME/AMF，**非 SMF**） |
| 控制维度 | **带宽维度**（基于协商带宽流控） | **接入权限维度**（基于用户属性允许/拒绝） |
| 控制依据 | 用户已用带宽 vs 协商带宽 | 签约 ARD/APN/卡类型/RAT 限制/核心网限制 |
| 控制方式 | CAR 丢弃 / Shaping 缓存整形 | 直接拒绝接入（返回原因值）或允许 |
| 控制时机 | 用户在线使用业务期间，持续流控 | 用户附着/接入网络时，一次性判定 |
| 控制对象 | 用户流量（报文级） | 用户接入请求（会话级） |
| License | 无 | SGSN/MME 侧 LKV2ARD02；AMF 侧无 |
| 配置对象 | APN + APNQOSATTR（CAR/Shaping 开关） | GBARD/IUARD/S1ARD 或 NGMMSUBDATA |
| 遵循标准 | 3GPP 23.214/29.244/33.210 | 3GPP 29.002/29.272（SGSN/MME）；23.501/29.503/29.518（AMF） |

**Stage 3 重审建议**[GWFD-010151]：
1. **任务描述纠偏**：原任务描述称 WSFD-106003 为"SMF 侧"，但文档实际适用 NF 为 **SGSN/MME/AMF**（控制面接入权限），**非 SMF**
2. **配置树归类重审**：两者不应归为"C-U 对称接入控制对"，应分别归入"U 面带宽流控"与"C 面接入权限控制"两个独立子类
3. **C 面带宽协商对称项待补**：GWFD-010151 真正的 C 面对称项应为"带宽协商特性"（SMF/PGW-C 侧），文档未指明对应 UNC 特性 ID，Stage 3 需在 UNC 侧查找"带宽协商/会话 AMBR 协商/QoS 协商"类特性补全

---

## 4. ★DP / SO / FeatureRule 候选补充（底座相关）

> 以下候选基于 8 个底座特性归纳，补充《归纳-四维度决策与机制.md》未覆盖的底座类图谱对象。

### 4.1 DecisionPoint（DP）候选

| DP ID 候选 | DP 名称 | 触发特性 | 决策维度 | 输入 | 输出 | 来源 |
|-----------|---------|---------|---------|------|------|------|
| DP-APN-并发判定 | 多 PDN/PDU 并发允许判定 | WSFD-010503 | 并发数 | 当前 UE PDN/PDU 总数 + 当前 APN 在用数 + APNACTNUM 配置 | 允许建立 / 拒绝（原因值 55） | [WSFD-010503] |
| DP-APN-别名APN映射 | 别名 APN 映射决策 | WSFD-106203 | 网元角色 + 用户范围 + APN | IMSI/切片 + 协商/别名 APN + 映射表 | 映射后 APN（别名/真实） / 原APN | [WSFD-106203] |
| DP-APN-UPF选择 | UPF 选择三轮决策 | WSFD-107010 | DNN/切片/位置/DNAI/接口/EPS互通/权重/负载 | UE 请求属性 + UPF 属性配置 + 策略次序 | 选定 UPF / 失败 | [WSFD-107010] |
| DP-APN-对等网元选择 | 对等网元 DNS 域名聚合决策 | WSFD-010202 | 位置区域（LAI/RAI/TAI）+ 目标网元类型 | 用户位置 + AREADNS 配置 + 映射方式 | 聚合 DNS 域名 → 解析对等网元 | [WSFD-010202] |
| DP-APN-接入权限 | 用户接入权限判定（C 面） | WSFD-106003 | RAT/核心网限制 OR ARD/APN/卡类型 | 用户签约 + 本地配置 + UE RAT/卡类型 | 允许接入 / 拒绝（原因值） | [WSFD-106003] |
| DP-APN-带宽流控 | U 面带宽流控方式判定 | GWFD-010151 | 上行/下行 × CAR/Shaping | 报文方向 + APNQOSATTR 配置 + 协商带宽 | 转发 / 丢弃 / 缓存整形 | [GWFD-010151] |

### 4.2 SemanticObject（SO）候选

| SO ID 候选 | SO 名称 | 归属特性 | 关键属性 | 来源 |
|-----------|---------|---------|---------|------|
| SO-APN-会话上下文 | PDU/PDN/PDP 会话上下文 | GWFD-010101 + WSFD-010501 | 会话 ID、DNN/APN、QoS Flow/承载、UE IP、F-TEID、SSC Mode | [GWFD-010101][WSFD-010501] |
| SO-APN-签约数据缓存 | UNC 签约数据本地缓存 | WSFD-010400 | APN 签约、PDN Address、QoS、APN-AMBR、ARD、APN-OI Replacement、Charging Characteristics | [WSFD-010400] |
| SO-APN-APNACTNUM | 单 APN 并发限制配置 | WSFD-010503 | APNNI、PDNNUM、IPV4ADDRNUM、IPV6ADDRNUM、PDNCONNREJCAUSE | [WSFD-010503] |
| SO-APN-别名APN映射表 | 别名 APN 映射记录 | WSFD-106203 | （SGSN/MME 侧）IMSI 前缀 + OLDAPN + NEWAPN；（GGSN/PGW-C/SMF 侧）SUBRANGE + ALIASAPN + CONVERTAPN + SST/SD | [WSFD-106203] |
| SO-APN-PNFPROFILE | UPF NF 实例属性 | WSFD-107010 | NFINSTANCENAME、NF TYPE、WEIGHT、PRIORITY、DNN/切片/DNAI/位置/EPS互通能力 | [WSFD-107010] |
| SO-APN-AREDNS | 位置区域 DNS 域名定制 | WSFD-010202 | DNTYPE、LAC/RAC/TAC + RANGE、ZONESW、ZONENAME | [WSFD-010202] |
| SO-APN-ARD记录 | 接入限制参数记录（C 面） | WSFD-106003 | （AMF）NGMMSUBDATA（IMSIPRE/RATRESTRICT/CORERESTRICT）；（SGSN/MME）GBARD/IUARD/S1ARD（IMSI/APNNI/CARDTYPE/ARD/CTRLTYPE/CAUSE） | [WSFD-106003] |
| SO-APN-APNQOSATTR | APN QoS 属性（U 面带宽流控） | GWFD-010151 | CARSHAPESWUL/CARSHAPEUL/CARSHAPESWDL/CARSHAPEDL | [GWFD-010151] |

### 4.3 FeatureRule 候选

| FR ID 候选 | FR 名称 | 约束类型 | 约束内容 | 来源 |
|-----------|---------|---------|---------|------|
| FR-APN-并发上限-11 | EPC 单用户 PDN 连接上限 11 | 硬上限 | 单用户 PDN 连接总数 ≤ 11，超限 MME 拒绝 | [WSFD-010503] |
| FR-APN-并发上限-15 | 5GC 单用户 PDU 会话上限 15 | 硬上限 | 单用户 PDU 会话总数 ≤ 15，超限 SMF 拒绝 | [WSFD-010503] |
| FR-APN-单APN并发 | 单 APN 并发可配（仅 EPC） | 配置阈值 | ADD APNACTNUM 的 PDNNUM/IPV4ADDRNUM/IPV6ADDRNUM；5GC 当前无单 DNN 粒度配置 | [WSFD-010503] |
| FR-APN-别名双条件 | SGSN/MME 别名 APN 转换双条件 | 逻辑与 | IMSI 号段匹配 **AND** 协商 APN 在映射表，两条件同时满足才转换 | [WSFD-106203] |
| FR-APN-纠错顺序 | APN 纠错先于别名 APN | 顺序约束 | 用户携带错误 APN 时，先 WSFD-106004 纠错，再 WSFD-106203 别名转换 | [WSFD-106203] |
| FR-APN-5G切片查询顺序 | 5G 切片查询顺序 | 优先级 | 5G 用户先按指定切片（SST+SD）查别名 APN，未中再按 ALL_USER 查 | [WSFD-106203] |
| FR-APN-UPF必选全满足 | UPF 选择第一轮必选条件全满足 | 逻辑与 | DNN+切片+位置+DNAI+接口+EPS互通+分流 7 个必选条件同时满足，无优先级 | [WSFD-107010] |
| FR-APN-SMF主锚点优先 | SMF 主锚点 UPF 优先于静态 IP 段绑定 | 优先级 | 静态 IP 段绑定 UPF 与 SMF 主锚点 UPF 冲突时，SMF 选择优先 | [WSFD-107010] |
| FR-APF-同厂商约束 | SMF 与 UPF 同厂商 | 硬约束 | SMF 和 UPF 设备必须同时为 HUAWEI | [WSFD-107010] |
| FR-APN-4G切片不参与 | 4G 接入选 SGW-U/PGW-U 不用切片 | 代际特殊 | 4G 用户接入 EPC 时 ADD PNFDNN 的 PNFNSINDEX 保持默认 0 | [WSFD-107010] |
| FR-APN-签约存储延迟生效 | 签约数据存储方式变更延迟生效 | 生效时机 | SET SYS SUBSTORAG 修改后在用户发生移动性管理流程时生效 | [WSFD-010400] |
| FR-APN-AMF本地配置优先 | AMF 本地配置优先于签约 | 优先级 | 本地匹配 > 签约兜底；本地 Null 强制允许 | [WSFD-106003] |
| FR-APN-紧急注册跳过 | 紧急注册跳过接入控制 | 豁免 | 紧急注册时跳过 WSFD-106003 接入控制检查 | [WSFD-106003] |
| FR-APN-卡类型依赖鉴权 | 卡类型控制依赖鉴权功能 | 前置依赖 | SGSN/MME 卡类型控制必须先启用 WSFD-010301 鉴权功能 | [WSFD-106003] |
| FR-APN-带宽上下行独立 | U 面带宽流控上下行独立 | 配置独立 | CARSHAPESWUL/DL 与 CARSHAPEUL/DL 上下行独立配置，可不同方式 | [GWFD-010151] |
| FR-APN-带宽粒度APN | U 面带宽流控仅 APN 粒度 | 粒度限制 | 接入控制策略绑定 APN，无法针对单用户配置 | [GWFD-010151] |

---

## 5. 关键发现与 Stage 3 建议

### 5.1 三大关键发现

1. **纯描述性根底座**：GWFD-010101 + WSFD-010501 是 APN 域的纯描述性根底座（无 MML、无 License、无独立配置对象、被动信令触发），是所有上层特性的宿主流程[GWFD-010101][WSFD-010501]
2. **同特性 ID 双视角语义反转**：WSFD-106203 在 SGSN/MME 侧（协商 APN→别名 APN，DNS 屏蔽）与 GGSN/PGW-C/SMF 侧（别名 APN→真实 APN，资源归一）**映射方向相反、命令族命名不同、License 分离**，建议 Stage 4 拆分为两个 Feature 变体节点[WSFD-106203]
3. **接入控制非 C-U 对称**：GWFD-010151（U 面带宽流控）与 WSFD-106003（C 面接入权限）**机制完全不同**，非同一控制目标的 C-U 分工，配置树归类需 Stage 3 重审；且 WSFD-106003 文档实际适用 NF 为 SGSN/MME/AMF（**非 SMF**），原任务描述需纠偏[GWFD-010151][WSFD-106003]

### 5.2 Stage 3 横向分析建议

| 建议项 | 内容 | 涉及特性 |
|--------|------|---------|
| 文档缺口补全 | WSFD-107010 UPF 选择文档缺口最大（1 篇概述，无 MML 脚本/调测/告警/软参/指标），需查 OM 命令手册 + UDG 初始配置 + 业务专题 `UNC UPF选择专题/特性映射与交互_72976829.md` | [WSFD-107010] |
| C 面带宽协商对称项补全 | GWFD-010151 的 C 面对称项应为"带宽协商/QoS 协商"特性（SMF/PGW-C 侧），文档未指明 UNC 特性 ID，需在 UNC 侧查找 | [GWFD-010151] |
| N4 协商带宽信元补全 | GWFD-010151 未明示 C 面下发协商带宽的具体 PFCP 信元（MBR/GBR/Session AMBR），需对照 GWFD-010224 N4 接口特性验证 | [GWFD-010151] |
| 5G 单 DNN 并发配置不对称 | WSFD-010503 当前 5GC 场景无单 DNN 粒度并发配置（仅 EPC 有 ADD APNACTNUM），代际不对称需记录 | [WSFD-010503] |
| 代际发布时序 | 2/3G 发布版本（20.3.0/20.3.2）晚于 4G/5G（20.0.0），反映 2/3G 是后向补全 | [GWFD-010101][WSFD-010501][WSFD-010400] |
| 配置树归类重审 | 接入控制类不应将 GWFD-010151 与 WSFD-106003 归为 C-U 对称对，应分"U 面带宽流控"与"C 面接入权限控制"两个独立子类 | [GWFD-010151][WSFD-106003] |

### 5.3 与《归纳-四维度决策与机制.md》的关系

本文件**补充而非替代**四维度归纳：
- 四维度归纳覆盖：地址分配、鉴权、接入方式、地址类型（决策产生层）
- 本文件覆盖：会话管理、网元选择、接入控制（底座支撑层）
- 两者共同覆盖 APN 业务域全部特性，是 Stage 3 cross-analysis 的完整输入

---

## 附录：来源特性速查

| 特性 ID | 特性名 | 类别 | 文件 |
|---------|--------|------|------|
| GWFD-010101 | 会话管理（U 面） | 会话管理底座 | feature-knowledge/GWFD-010101-会话管理.md |
| WSFD-010501 | 会话管理（C 面） | 会话管理底座 | feature-knowledge/WSFD-010501-会话管理.md |
| WSFD-010503 | 多 PDN/PDU 功能 | 会话管理底座 | feature-knowledge/WSFD-010503-多PDN-PDU功能.md |
| WSFD-010400 | 用户数据管理 | 会话管理底座 | feature-knowledge/WSFD-010400-用户数据管理.md |
| WSFD-106203 | 别名 APN | 会话管理底座 | feature-knowledge/WSFD-106203-别名APN.md |
| WSFD-107010 | UPF 选择 | 网元选择底座 | feature-knowledge/WSFD-107010-UPF选择.md |
| WSFD-010202 | 基于位置区域的对等网元选择 | 网元选择底座 | feature-knowledge/WSFD-010202-基于位置区域对等网元选择.md |
| WSFD-106003 | 用户接入控制功能 | 接入控制底座 | feature-knowledge/WSFD-106003-用户接入控制功能.md |
| GWFD-010151 | 接入控制（U 面） | 接入控制底座 | feature-knowledge/GWFD-010151-接入控制.md |
