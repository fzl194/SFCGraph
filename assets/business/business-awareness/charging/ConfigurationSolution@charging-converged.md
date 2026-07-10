---
id: ConfigurationSolution@charging-converged
type: ConfigurationSolution
name: 融合计费
domain: business-awareness
scenario: charging
status: draft
---

# 融合计费
> 5G SA 场景下 SMF 经 N40/Nchf 与 CHF 对接，同一 PDU 会话在线 RG 与离线 RG 共存，CHF 融合 CG 的 CGF 与 OCS 的 ABMF/RF。属于[计费](business/business-awareness/charging/NetworkScenario@charging.md)场景。编排 UDG+UNC 跨网元 feature/compound task。

## 概览
融合计费（Converged Charging）是 5G 引入的统一计费架构，解决"在线+离线统一"问题：同一用户的同一 PDU 会话中，部分业务按在线 RG 实时计费（CHF 配额管理），部分业务按离线 RG 后计费（仅参数记录），数据归一避免不一致。CHF 同时融合了离线 CG 的 CGF（话单生成）与在线 OCS 的 ABMF/RF（批价扣费）功能，SMF 通过 Nchf（N40）服务化接口与 CHF 完成实时计费和后计费。

本方案编排 2 个特性跨网元协同——UDG 侧[融合计费特性 2-00006](task/UDG/20.15.2/2-00006.md) + UNC 侧[融合计费特性 2-00003](task/UNC/20.15.2/2-00003.md)：
- **UDG 用户面（UPF）**：每个业务配双 URR——1 个 offline URR（`USAGERPTMODE=OFFLINE`）+ 1 个 online URR（`USAGERPTMODE=ONLINE`），组装到同一 URRGROUP。UPF 累计时长/流量/事件，经 N4/PFCP Usage Report 上报 SMF。复用计费三件套 + 过滤链 + 规则绑定 + 计费收尾。
- **UNC 控制面（SMF）**：三联前置（`CHGMODE=NchfMode` + `CHARGECTRL`/`USRPROFCHARGE` 使能 + `CHFINIT=SENDREQ`）→ CCT 模板（配额阈值/Trigger/终结方式）→ CHF 选择（TNF 族 + 按 IMSI/号段/CC 选）→ SMF-CHF 交互 Trigger → 费率标识链（双 URR 变种）→ N40/Nchf ChargingData Create/Update/Release 三阶段。

核心架构：UDG ↔(N4/PFCP)↔ SMF ↔(Nchf/N40)↔ CHF。PCF 通过 N7 下发 chargingInfo（含 CHF 地址），NRF 用于 CHF 发现。

## 配置与协同

本方案跨网元编排 **2 个融合计费特性**：UNC 控制面 [2-00003](task/UNC/20.15.2/2-00003.md) + UDG 用户面 [2-00006](task/UDG/20.15.2/2-00006.md)。融合计费依赖内容计费三件套基础 + SA-Basic 业务识别前提，但费率三件套结构**已在融合计费配置内含**（重叠，不需额外配内容计费）。

**特性关系矩阵**（★回答"哪些必配 / 可选 / 包含 / 正交"，追溯原始文档「与其他特性的交互」段 + feature task 依赖声明）：

| 特性 | 角色 | 必配? | 关系说明 |
|---|---|---|---|
| [UDG 融合计费 2-00006](task/UDG/20.15.2/2-00006.md) | 核心（方案主体） | 必配 | 本方案的计费模式（双 URR + Nchf/N40 + CHF），含费率三件套基础（内容计费结构重叠已含，不需额外配内容计费） |
| [UNC 融合计费 2-00003](task/UNC/20.15.2/2-00003.md) | 跨网元对端 | 必配 | UNC 侧 Nchf/CCT/CHF 对接链 + 费率标识链（双 URR 变种），与 UDG 对端组合 |
| UDG 内容计费（GWFD-020301） | 基础（费率三件套结构） | 可选（配置重叠已含） | 费率三件套（URR/URRGROUP/PCCPOLICYGRP）结构**已内含于融合计费配置**——配融合计费时三件套已配，不需额外配内容计费特性；License LKV3G5BCBC01 必开 |
| UDG SA-Basic（GWFD-110101） | 依赖前提（业务识别） | License 必开 | 业务识别前提；融合计费依赖其识别业务流。配置不重叠，License 必须开启 |

> 矩阵规则：①**核心**=方案主体（必配）；②**基础/依赖前提**=核心依赖的底层（必配，配置常与核心重叠）；③**维度增强**=正交维度可选叠加（按业务诉求）；④**跨网元对端**=另一网元对应特性（组合）；⑤**二选一**=互斥路径选其一。**配置重叠必须在「关系说明」注明**（防"额外配一遍"误解）。

各特性未变化的配置走其**标准配置方法**（见各 feature task），以下仅说明本方案的**特性级变种/排除项**与**跨网元协同**。

### UNC 控制面：融合计费特性（[2-00003](task/UNC/20.15.2/2-00003.md)）

走标准配置方法（见 feature task），**无特性级变种**。CCT 绑定层次按 DP-3 选（通常 UserProfile 层）；CHF 选择方式按 DP-4；配额阈值按 DP-5。

### UDG 用户面：融合计费特性（[2-00006](task/UDG/20.15.2/2-00006.md)）

走标准配置方法（见 feature task），但有以下**变种/排除**（融合独有）：

- **双 URR 变种**：计费三件套每业务配 offline URR（`USAGERPTMODE=OFFLINE`）+ online URR（`USAGERPTMODE=ONLINE`）同组，`RGAPPLIED` 决定在线/离线归属（见 [1-00010](task/UDG/20.15.2/1-00010.md) 场景差异 + DP-2）；URRGROUP 按 RGAPPLIED 配 UP/DOWNURRNAME1/2。这是融合计费对该特性标准配置（单 URR）的核心特化。
- **排除** `SET UPDEFAULTQUOTA`：配额由 CHF 经 Nchf 统一下发，非 UDG 本地默认配额开关（标准配置里有，融合方案不用）。
- **可选** `SET URRFAILACTION`（[0-00018](task/UDG/20.15.2/0-00018.md)）：配额超时阻塞放通。

### 跨网元/跨特性协同

- **顺序**：UNC 侧 CHF 对接链 + CCT 模板先就绪 → UDG 侧双 URR 配置（参数与 UNC 费率标识链对齐）→ UDG `SET REFRESHSRV` 最后生效（`PROTBINDFLOWF` 后 60s）。
- **一致性**：UDG `ADD URR.RG` = UNC `ADD URR.RG`（RG 跨侧一致）；URRID 全局唯一；CP/UP 的 `USAGERPTMODE`/`METERINGTYPE`/`RULENAME`/`POLICYNAME`/`USERPROFILENAME` 一致（见约束段）。
- **协议链**：UDG ↔(N4/PFCP)↔ SMF ↔(Nchf/N40)↔ CHF；PCF 经 N7 下发 chargingInfo（含 CHF 地址），NRF 用于 CHF 发现。

> 方案优先复用已有 UNC 1-00005~1-00011 与 UDG 1-00009~1-00012，不新建 atom/compound（跨网元协同已由两侧 feature task 覆盖）。

## 决策点

### DP-1：计费方式选择（方案级，选 CS）
进入计费场景时的首要决策，决定走哪个 ConfigurationSolution。

| 选项/场景 | 影响（参数/命令/联动） |
|---|---|
| 融合计费 | 选本 CS。UDG 双 URR（offline+online）+ UNC Nchf/CCT/CHF 全链；`CHGMODE=NchfMode`；`CHFINIT=SENDREQ`；RGAPPLIED 配在线/离线归属 |
| 离线计费 | 选离线 CS。UDG 仅 offline URR + UNC Ga/CG 接口；无配额管理；`CHGMODE` 非 NchfMode |
| 在线计费 | 选在线 CS。UDG 仅 online URR + UNC Gy/DCC/OCS 接口；配额实时申请；`CHGMODE` 非 NchfMode |

### DP-2：双 URR 在线/离线分配（RGAPPLIED，★融合核心）
UNC 侧 `SET USRPROFCHARGE`/`SET APNCHARGECTRL`/`ADD CHARGEMETHOD` 的 RGAPPLIED 参数决定 URRGROUP 怎么配，UDG 侧必须匹配。

| 选项/场景 | 影响（参数/命令/联动） |
|---|---|
| 未设/融合正常模式 | URRGROUP 双 URR：UPURRNAME1/DOWNURRNAME1=离线 URR + UPURRNAME2/DOWNURRNAME2=在线 URR；在线+离线 RG 同接口并存（原始文档任务示例取此值） |
| ONLINERGONLY | URRGROUP 只配在线 URR（UPURRNAME1/DOWNURRNAME1=online URR，不配 2）；仅在线 RG，CHF 配额管理；行为同在线计费 |
| OFFLINERGONLY | URRGROUP 只配离线 URR（UPURRNAME1/DOWNURRNAME1=offline URR，不配 2）；仅离线 RG，无配额管理；行为同离线计费 |
| DEFAULT | URRGROUP 只能配一种模式（仅离线或仅在线 URR，二选一）；SMF 按用户签约决定在线或离线；**不能同时配离线+在线 URR**，否则计费冲突（critical 约束） |

### DP-3：CCT 模板配置层次选择
CCT 模板共享同一套参数骨架，差异仅在绑到哪个对象，4 层次是降级链。

| 选项/场景 | 影响（参数/命令/联动） |
|---|---|
| UserProfile 层 | `SET USRPROFCHARGE` 带 CCTEMPLATE+CONVERGEDSW+RGAPPLIED；优先级最高；走 [1-00002](task/UNC/20.15.2/1-00002.md) |
| APN 层 | `SET APNCHARGECTRL` 带 CCTEMPLATE+CONVERGEDSW+RGAPPLIED；优先级次高；走 [1-00003](task/UNC/20.15.2/1-00003.md) |
| 计费属性 CC 层 | 分两步：① `ADD CHARGEMETHOD` 配 CONVERGED/RGAPPLIED（使能开关）② `ADD SELECTCCTBYCC` 绑 CCVALUE→CCTMPLTNAME（模板绑定）；走 [1-00006](task/UNC/20.15.2/1-00006.md) |
| 全局层 | `MOD CCT`（CCTMPLTNAME=global）；优先级最低；兜底，所有未配层次的最终取值；走 [0-00114](task/UNC/20.15.2/0-00114.md) |

### DP-4：CHF 选择方式
决定 SMF 如何选择 CHF 实例/组，影响 CHF 对接与故障处理。

| 选项/场景 | 影响（参数/命令/联动） |
|---|---|
| 基于 IMSI | `ADD SELCHFGBYIMSI`；优先级最高；适用拨测 |
| 基于 IMSI 号段 | `ADD SELCHFGBIMSISEG`；优先级次高；多 CHF 负载均衡 |
| PCF 下发 FQDN | `ADD TNFINS` 带 FQDN；PCF 携带 chargingInfo 场景 |
| 本地 CC 选 CHF | `ADD SELECTCHFGBYCC`；本地 CC 绑 CHF 组 |
| 全局默认 CHF 组 | `SET GLBDFTCHFGROUP`；优先级最低；兜底，缓存回放前提 |

### DP-5：配额阈值与终结方式
CCT 模板内的配额控制参数，影响在线 RG 的配额闭环行为。

| 选项/场景 | 影响（参数/命令/联动） |
|---|---|
| 阈值百分比触发 | VQT/TQT/UQT（流量/时长/事件阈值百分比，如 20=20%）；到达阈值触发 ChargingData Update 申请新配额 |
| 配额有效时长 | VT（在线配额有效时长，分钟）；超时触发重授权 |
| 终结方式 | FUATERMINATE=TERM_SERVICE（终结整个 PDU 会话）/ 其他；影响配额耗尽后业务处理 |
| 配额耗尽动作 | `ADD QUOTAEXHAUSTACT`：BLOCK（阻塞）/REDIRECT（重定向）/FORWARD（放行走默认费率）；由 Final-Unit-Action 驱动 |

## 约束

- **SA+PCC+融合 License 三前置**（critical）：UDG 侧 SA-Basic（GWFD-110101）+ 内容计费基本功能（GWFD-020301，LKV3G5BC01）+ UNC 侧内容计费（WSFD-109002，LKV3W9BCC12）+ 融合计费（WSFD-011206）License 必须全部开启 — 否则配置命令成功但功能不生效，难以排查。
- **RGAPPLIED 强约束**（critical）：融合计费 RG 必须配 RGAPPLIED 标识在线/离线归属；RGAPPLIED=DEFAULT 时 URRGROUP 不能同时配离线+在线 URR（只能二选一），其余模式须双配或单配匹配 — 配错则计费冲突，这是融合计费最易配错的点。
- **CP/UP URRID/RG/USAGERPTMODE 跨侧一致**（critical）：UDG.ADD URR.RG = UNC.ADD URR.RG（RG 跨侧一致）；URRID 全局唯一；CP/UP 的 URRID/USAGERPTMODE/METERINGTYPE/RULENAME/POLICYTYPE/POLICYNAME/USERPROFILENAME 必须一致 — 不一致则计费异常/策略不生效（告警 ALM-81026/ALM-81054）。
- **三联前置 CHGMODE/CHARGECTRL/CHFINIT**（critical）：融合计费需同时满足 `CHGMODE=NchfMode` + `CHARGECTRL`（或 USRPROFCHARGE/APNCHARGECTRL）使能 + `CHFINIT=SENDREQ` 三条件 — 否则不发送 Initial 或 Initial 不携带预期 RG。
- **REFRESHSRV 时序**（critical，UDG 侧）：`SET REFRESHSRV:REFRESHTYPE=ALL` 必须在所有 ADD/SET 完成后最后执行；`PROTBINDFLOWF` 配置后需等待 60 秒再执行 REFRESHSRV — 不执行或时序错则 FILTER 配置变更不生效。
- **模板名是引用键**（critical，UNC 侧）：CCTMPLTNAME 须先建（[1-00005](task/UNC/20.15.2/1-00005.md)）再绑定 — 否则绑定命令找不到模板。
- **同一 RG 在线/离线属性唯一**（critical）：同一计费会话内，同一 RG 要么在线要么离线，不能同时 — 否则计费出错。
- **缓存前提**（critical，UNC 侧）：开启消息缓存（[1-00011](task/UNC/20.15.2/1-00011.md)）必须 FHACTION=CONTINUE + SCACT=FAILOVER/CONTINUE + STGSWITCH=ENABLE + CHGDATAREFGEN=SMF + 配全局默认 CHF 组。
- **每个 USERPROFILE 必绑缺省费率**（critical）：`SET URRGRPBINDING` 的 DFTURRGRPNAME（缺省业务费率）+ DFTSIGURRGNAME（缺省信令费率） — 否则未匹配费率的报文无法计费。
- **互操作计费连续性**（warning）：5GS↔EPS 互操作切换时，目标系统必须继承源系统的计费上下文（RG/URR ID/配额余额）；切换前后 Usage Report 必须连续不中断 — 否则切换期间计费中断或话单丢失。
- **不支持多 UPF 共享在线 RG 配额**（warning）：多 UPF 场景在线计费 RG 配额不共享，各 UPF 的 URR ID 须全局唯一且配额不互相干扰。
- **N40APIVER 与 CHF 一致**（warning）：APIVER 须与 CHF 使用相同协议版本 — 否则接口信元不一致（ALM-81026）。

## 关联
- 上游场景：[计费](business/business-awareness/charging/NetworkScenario@charging.md)
- 编排特性（feature task，优先）：[2-00003 UNC 融合计费](task/UNC/20.15.2/2-00003.md) · [2-00006 UDG 融合计费](task/UDG/20.15.2/2-00006.md)
- 复用步骤/命令（compound/atom，按需）：UNC [1-00005](task/UNC/20.15.2/1-00005.md) CCT模板 · [1-00006](task/UNC/20.15.2/1-00006.md) CCT绑CC · [1-00007](task/UNC/20.15.2/1-00007.md) CHF选择 · [1-00008](task/UNC/20.15.2/1-00008.md) SMF-CHF交互 · [1-00009](task/UNC/20.15.2/1-00009.md) 费率标识链 · [1-00010](task/UNC/20.15.2/1-00010.md) 异常处理 · [1-00011](task/UNC/20.15.2/1-00011.md) 消息缓存 · [1-00002](task/UNC/20.15.2/1-00002.md) 绑UserProfile · [1-00003](task/UNC/20.15.2/1-00003.md) 绑APN · [0-00114](task/UNC/20.15.2/0-00114.md) 全局CCT；UDG [1-00010](task/UDG/20.15.2/1-00010.md) 计费三件套 · [1-00009](task/UDG/20.15.2/1-00009.md) 过滤链 · [1-00011](task/UDG/20.15.2/1-00011.md) 规则绑定 · [1-00012](task/UDG/20.15.2/1-00012.md) 计费收尾 · [0-00019](task/UDG/20.15.2/0-00019.md) License · [0-00018](task/UDG/20.15.2/0-00018.md) URRFAILACTION
- 证据：[计费场景业务图谱_旧版参考](evidence/business/charging/计费场景业务图谱_旧版参考.md)（§2.3 CS-CH-03 + §10.3 融合端到端流程）· [部署融合计费功能](evidence/business/charging/部署融合计费功能_55040304.md) · [配置融合计费费率标识](evidence/business/charging/配置融合计费费率标识_55040292.md) · [配置NCG_CHF(OCS)选择方式](evidence/business/charging/配置NCG_CHF(OCS)选择方式_55040296.md) · [配置融合计费模板](evidence/business/charging/配置融合计费模板_90839473.md) · [配置SMF与NCG_CHF交互](evidence/business/charging/配置SMF与NCG_CHF交互_55040288.md)
