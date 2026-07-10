---
id: ConfigurationSolution@charging-online
type: ConfigurationSolution
name: 在线计费
domain: business-awareness
scenario: charging
status: draft
---

# 在线计费
> SMF 经 Gy/DCC 与 OCS 实时对接，OCS 配额管理（GSU）+ 信用控制（CCR-I/U/T 三阶段），UDG 单条 online URR 上报使用量，配额耗尽触发 Final-Unit-Action（BLOCK/REDIRECT/RESTRICT）。属于[计费](business/business-awareness/charging/NetworkScenario@charging.md)场景。编排 UDG 侧 feature task + UNC/SMF 侧 CTF 角色对接。

## 概览
在线计费（Online Charging）是预付费用户的实时信用控制方式：UDG（UPF）按业务统计时长/流量/事件，经 N4/PFCP Usage Report 上报 UNC（SMF）；UNC 作为 CTF（Charging Trigger Function）经 Gy 接口/Diameter Credit Control（DCC）协议与 OCS 实时交互——**CCR-I 申请初始配额**（CCA-I 携带 GSU 授权配额）→ 配额使用中按阈值触发 **CCR-U 申请新配额** → 业务终结发 **CCR-T**。配额耗尽触发 **Final-Unit-Action**（BLOCK/REDIRECT/RESTRICT）实现实时信用控制。与离线/融合的核心差异：**实时配额管理 + Final-Unit-Action 终结动作**，不与 CG/CHF 交互，仅 OCS。

本方案编排 3 个 UDG 特性 + UNC/SMF 侧 CTF 角色——UDG [在线计费 2-00004](task/UDG/20.15.2/2-00004.md)（核心）+ [内容计费 2-00003](task/UDG/20.15.2/2-00003.md)（业务粒度维度增强，可选）+ [事件计费 2-00009](task/UDG/20.15.2/2-00009.md)（计量维度增强，可选）：
- **UDG 用户面（UPF）**：每业务配单条 online URR（`USAGERPTMODE=ONLINE` + `ONLMETERINGTYPE`），不复用离线 URR。复用内容计费通用 backbone（计费三件套+过滤链+规则绑定+计费收尾）。
- **UNC 控制面（SMF，CTF 角色）**：配置 Gy/DCC 对接（Diameter 本端/对端 + 链路组/链路 + OCS 选择）+ DCC 会话（CCR-I/U/T + Final-Unit-Action）+ OCS 配额管理（GSU 授权 + 触发器）。**UDG 主导配置，UNC/SMF 按 UDG 编排配 Gy 接口对接 + DCC 会话**。

核心架构：UDG ↔(N4/PFCP)↔ UNC/SMF(CTF) ↔(Gy/DCC)↔ OCS。配额闭环：OCS 授权 GSU → SMF 创建 N4 URR 含配额 → UPF 累计 → Usage Report → SMF → CCR-U → OCS 续配额 → 耗尽触发 Final-Unit-Action。

## 配置与协同

本方案编排 **3 个 UDG 特性**：UDG [2-00004 在线计费](task/UDG/20.15.2/2-00004.md)（核心）+ [2-00003 内容计费](task/UDG/20.15.2/2-00003.md)（业务粒度维度增强）+ [2-00009 事件计费](task/UDG/20.15.2/2-00009.md)（计量维度增强，可选）。UNC/SMF 侧配 Gy/DCC 对接。

**特性关系矩阵**（★回答"哪些必配 / 可选 / 包含 / 正交"，追溯原始文档「与其他特性的交互」段 + feature task 依赖声明）：

| 特性 | 角色 | 必配? | 关系说明 |
|---|---|---|---|
| [在线计费 2-00004](task/UDG/20.15.2/2-00004.md) | 核心（方案主体） | 必配 | 本方案的计费模式（实时配额 + Gy/OCS）；费率三件套（URR/URRGROUP/PCCPOLICYGRP）结构由此特性承载 |
| [内容计费 2-00003](task/UDG/20.15.2/2-00003.md) | 业务粒度增强（维度） | 可选 | 按业务差异化费率时叠加；**费率三件套与在线计费配置重叠——配在线计费时三件套已含内容计费结构，不需额外配内容计费**；不按业务粒度则在线计费用默认费率 |
| [事件计费 2-00009](task/UDG/20.15.2/2-00009.md) | 计量维度增强（正交） | 可选 | 按事件计量时叠加；**与计费模式正交**（仅在线 SCUR，不支持 Default Quota）；本身依赖内容计费三件套结构 |

> 矩阵规则：①**核心**=方案主体（必配）；②**基础/依赖前提**=核心依赖的底层（必配，配置常与核心重叠）；③**维度增强**=正交维度可选叠加（按业务诉求）；④**跨网元对端**=另一网元对应特性（组合）；⑤**二选一**=互斥路径选其一。**配置重叠必须在「关系说明」注明**（防"额外配一遍"误解）。

各特性未变化的配置走其**标准配置方法**（见各 feature task），以下仅说明本方案的**特性级变种/排除项**与**跨网元协同**。

### UDG 用户面：在线计费特性（[2-00004](task/UDG/20.15.2/2-00004.md)）

走标准配置方法（见 feature task），但有以下**变种/排除**（在线独有）：

- **单 URR 变种**：计费三件套每业务只配 1 条 **online URR**（`USAGERPTMODE=ONLINE` + `ONLMETERINGTYPE`），不配 offline URR、不配双 URR（同组）。URRGROUP 仅绑 online URR（`UPURRNAME1`/`DOWNURRNAME1`=online URR，不配 2）。这是该特性对该方案的核心特化——单 URR 是与融合计费（双 URR）/离线计费（单 offline URR）的关键差异。
- **`ONLMETERINGTYPE` 选值**：按业务选 VOLUME（流量）/ DURATION（时长）/ EVENT（事件）/ 组合 / FREE（异常免费）；EVENT 取值仅支持在线 SCUR（见事件计费约束），ECUR 额外支持需 BIT1250（PGW-C/UPF 双开）。
- **必配** `SET UPDEFAULTQUOTA`（[0-00016](task/UDG/20.15.2/0-00016.md)）：在线计费专属——`UPDEFAULTQUOTASW=ENABLE` + `DFTQUOTAVOLUME`/`DFTQUOTATIME` 默认配额，OCS 申请配额期间用默认配额放通避免阻塞。**与 `SET UPGLBCHGPARA`（Credit Pooling，全局开关 [0-00017](task/UDG/20.15.2/0-00017.md)）互斥**——两者只能开一个（仅流量计费 + 仅 Gy 接口）。
- **可选** `SET URRFAILACTION`（[0-00018](task/UDG/20.15.2/0-00018.md)）：URR 上报失败/配额超时动作，配额超时阻塞放通（`RETRYFAILACT=CONTINUE`）。
- **排除** CCT 模板（融合计费专属，Nchf/N40 接口）：在线用 Gy/DCC + OCS，无 CCT。
- **刷新类型**：`SET REFRESHSRV:REFRESHTYPE=USERPROFILE`（原始在线文档取值，非融合/内容的 ALL）。

### UDG 用户面：内容计费特性（[2-00003](task/UDG/20.15.2/2-00003.md)）

走标准配置方法（见 feature task），**无特性级变种**。内容计费提供通用 backbone（计费三件套 + 过滤链 + 规则绑定 + 计费收尾），在线计费特性在其上做 URR 在线参数特化。

### UDG 用户面：事件计费特性（[2-00009](task/UDG/20.15.2/2-00009.md)）

走标准配置方法（见 feature task），但有以下**在线特有约束**：

- **PCCPOLICYGRP 必使能事件计费**：`EVENTCHARGEFLAG=ENABLE` + `EVENTCHGPOINT=REQUEST/RESPONSE/FINISH`（DP 选）。
- **仅限在线 SCUR**（critical 约束）：事件计费仅支持 SCUR（Session Charging with Unit Reservation）；ECUR 需 BIT1250；**不支持 Default Quota**（与 `SET UPDEFAULTQUOTA` 不兼容，方案级必配变冲突——事件计费业务需关闭 UPDEFAULTQUOTA 走 Credit Pooling 或单 GSU 配额）。
- **URR 统计类型 = EVENT**：`ONLMETERINGTYPE=EVENT`；CCR 上报 `serviceSpecificUnits`。
- **排除** `SET SPECTRAFURRGRP`（[0-00290](task/UDG/20.15.2/0-00290.md)）：事件计费场景全局缺省 URR 组对事件计量无效（仅支持时长和流量）。
- **性能约束**：七层解析+事件统计对吞吐量影响大；仅支持 HTTP1.x；不支持加密协议（SSL/FTPS）。

### UNC 控制面（SMF，CTF 角色）：Gy/DCC 对接 + DCC 会话

UNC/SMF 侧无独立特性 task（在线计费特性本身归属 UDG），按 UDG 编排配以下对接：

- **Gy/DCC 对接链**（Diameter 本端 + 对端 OCS + 链路组/链路）：`ADD DIAMLOCINFO` + `ADD OCS` + `ADD DIAMCONNGRP` + `ADD DIAMCONNECTION`（参考 [2-00005 PCC基本功能](task/UNC/20.15.2/2-00005.md) PCRF 对接链结构 [1-00012](task/UNC/20.15.2/1-00012.md)，OCS 替换 PCRF）
- **DCC 会话**（CCR-I/U/T 三阶段）：`ADD DCC TEMPLATE`（Diameter 模板，触发器 + GSU 授权）+ `ADD QUOTAEXHAUSTACT`（[0-00066](task/UNC/20.15.2/0-00066.md)，在线 RG 配额耗尽动作 BLOCK/REDIRECT/FORWARD）
- **OCS 选择**：按 IMSI/号段/全局默认（参考融合计费 CHF 选择 [1-00007](task/UNC/20.15.2/1-00007.md) 结构）

### 跨网元/跨特性协同

- **顺序**：UNC/SMF 侧 Gy/DCC 对接链 + OCS 选择 + DCC 模板先就绪 → UDG 侧 online URR 配置（URRID/RG 与 UNC 一致）→ UDG `SET REFRESHSRV`（`REFRESHTYPE=USERPROFILE`）最后生效。
- **数据流**：UDG 累计使用量 → N4/PFCP Usage Report → SMF(CTF) → Gy/DCC → OCS（CCR-I/U/T）→ GSU 授权/续配额 → 耗尽 Final-Unit-Action → SMF → N4 → UPF 执行。
- **一致性**：UDG `ADD URR.RG` = UNC 配置的 RG（跨侧一致）；URRID 全局唯一；CP/UP 的 `URRID`/`USAGERPTMODE=ONLINE`/`ONLMETERINGTYPE`/`RULENAME`/`POLICYNAME`/`USERPROFILENAME` 必须一致（见约束段）。
- **CCR-I/U/T 三阶段**：CCR-I 初始申请 → CCA-I 含 GSU 授权配额；CCR-U 阈值触发续配额 → CCA-U 新配额；CCR-T 会话终结。无 CCR-I 则无配额启动。

> UDG 侧优先复用 [1-00010](task/UDG/20.15.2/1-00010.md) 计费三件套 + [1-00009](task/UDG/20.15.2/1-00009.md) 过滤链 + [1-00011](task/UDG/20.15.2/1-00011.md) 规则绑定 + [1-00012](task/UDG/20.15.2/1-00012.md) 计费收尾；UNC 侧 Gy/DCC 对接复用 [2-00005 PCC基本功能](task/UNC/20.15.2/2-00005.md) Diameter 链结构（本方案不新建 UNC 特性 task）。

## 决策点

### DP-1：计费方式选择（方案级，选 CS）
进入计费场景时的首要决策，决定走哪个 ConfigurationSolution。

| 选项/场景 | 影响（参数/命令/联动） |
|---|---|
| 离线计费 | 选离线 CS。UDG 仅 offline URR + UNC Ga/CG 接口；无配额管理；`CHGMODE` 非 NchfMode；OFCTemplate 模板 |
| 在线计费 | 选本 CS。UDG 仅 online URR + UNC Gy/DCC/OCS 接口；配额实时申请；`SET UPDEFAULTQUOTA` 必配；DCC 模板 |
| 融合计费 | 选融合 CS。UDG 双 URR（offline+online）+ UNC Nchf/CCT/CHF 全链；`CHGMODE=NchfMode` |

### DP-2：在线统计类型 ONLMETERINGTYPE
UDG 侧 URR 的统计维度，影响 CCR 上报单位。

| 选项/场景 | 影响（参数/命令/联动） |
|---|---|
| VOLUME（流量） | `ONLMETERINGTYPE=VOLUME`；CCR 上报 `CC-Input-Octets`/`CC-Output-Octets`；与 Credit Pooling 兼容 |
| DURATION（时长） | `ONLMETERINGTYPE=DURATION`；CCR 上报 `CC-Time`；CTP/QCT 由 OCS/CHF 决定 |
| EVENT（事件） | `ONLMETERINGTYPE=EVENT`；CCR 上报 `serviceSpecificUnits`；**仅 SCUR**；PCCPOLICYGRP 须 `EVENTCHARGEFLAG=ENABLE`；与 `UPDEFAULTQUOTA` 互斥 |
| 综合 | `ONLMETERINGTYPE=EVENT_VOLUME_TIME`；综合统计；按业务组合 |
| FREE（异常免费） | `ONLMETERINGTYPE=FREE`；该 URR 免费；异常/信令场景兜底 |

### DP-3：默认配额 vs Credit Pooling（★互斥必选一）
在线计费 OCS 申请配额期间，配额到前业务如何放通——必选一：

| 选项/场景 | 影响（参数/命令/联动） |
|---|---|
| **默认配额（UPDEFAULTQUOTA）** | `SET UPDEFAULTQUOTASW=ENABLE` + `DFTQUOTAVOLUME`/`DFTQUOTATIME`；申请期间用本地默认配额放通；**与 Credit Pooling 互斥** |
| **Credit Pooling（UPGLBCHGPARA）** | `SET UPGLBCHGPARA` 全局开关；多 URR 共享配额池；**仅流量计费** + **仅 Gy 接口**；不支持权重 |
| 不配（应急） | 配额到前业务可能阻塞；通常不推荐 |

### DP-4：Final-Unit-Action（配额耗尽动作）
在线计费配额耗尽后由 OCS 通过 Final-Unit-Indication 下发的动作决定用户体验切换。

| 选项/场景 | 影响（参数/命令/联动） |
|---|---|
| BLOCK（阻断） | `ADD QUOTAEXHAUSTACT:BIT=BLOCK`；UPF 执行 DISCARD 丢弃报文；用户被强制下线 |
| REDIRECT（重定向） | `ADD QUOTAEXHAUSTACT:BIT=REDIRECT`；UPF 重定向到门户页（如充值/续订页）；典型体验切换 |
| RESTRICT（限制） | `ADD QUOTAEXHAUSTACT:BIT=RESTRICT`；UPF 限速；保留连接但降速 |
| FORWARD（放行） | 无 Final-Unit-Action；继续走 `DFTURRGRPNAME` 缺省费率；不计费但保通 |

## 约束

- **SA+在线+内容计费 License 三前置**（critical）：UDG 侧 SA-Basic（GWFD-110101，`LKV3G5SABS01`）+ 内容计费（GWFD-020301，`LKV3G5BCBC01`）+ 在线计费（GWFD-020300，`LKV3G5OLCH01`）License 必须开启 — 否则配置命令成功但功能不生效。
- **URR 在线一致性**（critical）：`URRID`/`USAGERPTMODE=ONLINE`/`ONLMETERINGTYPE` 在 SGW-C/PGW-C 与 SGW-U/PGW-U 必须一致 — 不一致则计费异常（ALM-81026/81054）。
- **USERPROFILE/RULE 跨侧一致**（critical）：`USERPROFILENAME`/`RULENAME`/`POLICYTYPE`/`POLICYNAME` 在 PCRF/SGW-C/PGW-C/SGW-U/PGW-U 间必须一致 — 不一致则策略无法按预期生效。
- **RG 跨侧一致**（critical）：UDG `ADD URR.RG` = UNC 配置的 RG — 不一致则报表与实际计费不一致。
- **URRID 全网唯一**（critical）：建议从 1000 开始分配 — 重复则 PFCP Session Report 无法关联。
- **REFRESHSRV 时序**（critical，UDG 侧）：`SET REFRESHSRV:REFRESHTYPE=USERPROFILE` 必须在所有 ADD/SET 完成后最后执行 — 不执行或时序错则 FILTER 配置变更不生效。
- **每个 USERPROFILE 必绑缺省费率**（critical）：`SET URRGRPBINDING` 的 `DFTURRGRPNAME`（缺省业务费率）+ `DFTSIGURRGNAME`（缺省信令费率） — 否则未匹配费率的报文无法计费。
- **UPDEFAULTQUOTA 与 UPGLBCHGPARA 互斥**（critical）：`SET UPDEFAULTQUOTA` 与 `SET UPGLBCHGPARA`（Credit Pooling）只能开一个 — 同时开则配置冲突。
- **事件计费仅限在线 SCUR**（critical）：事件计费（[2-00009](task/UDG/20.15.2/2-00009.md)）不支持 Default Quota（与 `SET UPDEFAULTQUOTA` 不兼容）；ECUR 仅在线计费额外支持（需 BIT1250）— 违反则事件计费不生效或配额异常。
- **CCR-I 必发**（critical）：`SET CHFINIT=SENDREQ`（参考融合计费同义命令）— 不发则无配额启动，CCR-U 无基础；SESSION 不建立。
- **Gy 接口 Diameter 协议栈一致性**（warning）：Gy 接口走 Diameter 协议（TCP/SCTP）；链路组/链路状态须 UP — 否则 DCC 会话无法建立（ALM-81026）。
- **不支持多 UPF 共享在线配额**（warning）：多 UPF 场景在线 RG 配额不共享，各 UPF 的 URR ID 须全局唯一且配额不互相干扰。
- **配额超时阻塞**（warning）：配额耗尽申请超时（`T3RESPONSE×N3REQUEST+4s`，`SET UPPFCPPATH` 配）→ PGW-U 阻塞业务；应急放通用 `SET URRFAILACTION:RETRYFAILACT=CONTINUE`。
- **依赖链**（warning）：SA-Basic → 内容计费 → 在线计费，依赖链上每环 License 须先开。
- **不支持 enhanced-ECUR/IEC**（warning）：20.15.2 不支持增强 ECUR/IEC 事件计费、紧耦合。

## 关联
- 上游场景：[计费](business/business-awareness/charging/NetworkScenario@charging.md)
- 编排特性（feature task，优先）：[2-00004 UDG 在线计费](task/UDG/20.15.2/2-00004.md) · [2-00003 UDG 内容计费](task/UDG/20.15.2/2-00003.md) · [2-00009 UDG 事件计费](task/UDG/20.15.2/2-00009.md)（可选）
- 复用步骤/命令（compound/atom，按需）：UDG [1-00010](task/UDG/20.15.2/1-00010.md) 计费三件套 · [1-00009](task/UDG/20.15.2/1-00009.md) 过滤链 · [1-00011](task/UDG/20.15.2/1-00011.md) 规则绑定 · [1-00012](task/UDG/20.15.2/1-00012.md) 计费收尾 · [0-00019](task/UDG/20.15.2/0-00019.md) License · [0-00016](task/UDG/20.15.2/0-00016.md) UPDEFAULTQUOTA · [0-00017](task/UDG/20.15.2/0-00017.md) UPGLBCHGPARA / Credit Pooling（与 UPDEFAULTQUOTA 互斥）· [0-00018](task/UDG/20.15.2/0-00018.md) URRFAILACTION · [0-00290](task/UDG/20.15.2/0-00290.md) 全局缺省URR组（事件计费除外）；UNC 侧参考 [2-00005 UNC PCC基本功能](task/UNC/20.15.2/2-00005.md) Diameter 对接链结构 + [2-00004 UNC 内容计费](task/UNC/20.15.2/2-00004.md) 费率标识链 + [0-00066](task/UNC/20.15.2/0-00066.md) QUOTAEXHAUSTACT
- 证据：[计费场景业务图谱_旧版参考](evidence/business/charging/计费场景业务图谱_旧版参考.md)（§2.2 CS-CH-02 在线 + §10.2 在线端到端流程）