---
id: ConfigurationSolution@charging-quota-exhaust
type: ConfigurationSolution
name: 配额降速与体验切换
domain: business-awareness
scenario: charging
status: draft
---

# 配额降速与体验切换
> 在线/融合计费配额耗尽（QUOTA_EXHAUSTED/Final-Unit-Indication）后，OCS/CHF 通过 Final-Unit-Action 下发体验切换动作（BLOCK 阻断/REDIRECT 重定向/FORWARD 放行走默认费率），或融合路径下经 CHF Notify(REAUTHORIZATION) 重授权新配额。属于[计费](business/business-awareness/charging/NetworkScenario@charging.md)场景。编排 UDG+UNC 跨网元 feature task。

## 概览
配额降速与体验切换（Quota Exhaust & Experience Switch）是套餐超量后的用户体验切换机制：在线/融合计费用户当月套餐配额用完后，OCS（在线）或 CHF（融合）通过 Diameter/Nchf 下发 Final-Unit-Action 触发体验切换——典型路径 A 阻断（`QUOTAEXHAUSTACT=BLOCK` → DISCARD）、路径 B 重定向（`=REDIRECT` → 重定向到门户页）、路径 C 放行（无动作，走 `DFTURRGRPNAME` 兜底）、路径 D 融合重授权（CHF Notify REAUTHORIZATION → 新配额下发）。核心解决"套餐超量后用户如何被引导续订/降速/保通"的问题。

与计费方式（在线/融合）正交——本方案聚焦"配额耗尽触发动作"这一层。在线计费触发流程：UDG 累计使用量 → N4/PFCP Usage Report → SMF → Gy/DCC CCR-U → OCS 判定配额耗尽 → OCS 通过 Final-Unit-Indication 下发 Final-Unit-Action → SMF 转 N4 触发 UPF 执行（BLOCK/REDIRECT/RESTRICT）。融合路径多一步：CHF Notify(REAUTHORIZATION) 走 Nchf 重新申请新配额。

本方案编排 3 个特性跨网元协同——UDG [在线计费 2-00004](task/UDG/20.15.2/2-00004.md)（在线触发链）+ [融合计费 2-00006](task/UDG/20.15.2/2-00006.md)（融合触发链）；UNC [融合计费 2-00003](task/UNC/20.15.2/2-00003.md)（融合 CCT/CCT Trigger + Final-Unit-Action 下发）：
- **UDG 用户面（UPF）**：执行 Final-Unit-Action——QUOTAEXHAUSTACT BLOCK/REDIRECT/RESTRICT 三选一，UPF 丢弃/重定向/限速；或接受 CHF/OCS 新配额继续累计。
- **UNC 控制面（SMF）**：CCT 模板配 Trigger（VQT/TQT/UQT 阈值触发 CCR-U）+ 终结方式 FUATERMINATE；CCT 绑定按 4 层次（UserProfile/APN/CC/全局）；CCT 触发耗尽 → OCS/CHF Final-Unit-Action 下发 → SMF 转 UPF 执行。

核心架构：UDG ↔(N4/PFCP)↔ UNC/SMF ↔(Gy/DCC 或 Nchf/N40)↔ OCS/CHF。体验切换闭环：UDG 累计 → Usage Report → SMF → OCS/CHF 判定耗尽 → Final-Unit-Action/REAUTHORIZATION 下发 → SMF → UPF 执行（BLOCK/REDIRECT/RESTRICT/FORWARD）。

## 配置与协同

本方案跨网元编排 **3 个特性**：UDG [2-00004 在线计费](task/UDG/20.15.2/2-00004.md) + [2-00006 融合计费](task/UDG/20.15.2/2-00006.md)；UNC [2-00003 融合计费](task/UNC/20.15.2/2-00003.md)。各特性未变化的配置走其**标准配置方法**（见各 feature task），以下仅说明本方案的**特性级变种/排除项**与**跨网元协同**。

### UDG 用户面：在线计费特性（[2-00004](task/UDG/20.15.2/2-00004.md)）

走标准配置方法（见 feature task），本方案的核心强化点：

- **必配** `SET UPDEFAULTQUOTA`（[0-00016](task/UDG/20.15.2/0-00016.md)）：配额耗尽触发 Final-Unit-Action 期间，默认配额作放通缓冲——未配则可能立即阻塞。
- **`ONLMETERINGTYPE` 影响阈值触发**：CCT 模板的 VQT（流量阈值百分比）/TQT（时长阈值百分比）/UQT（事件阈值百分比）触发 CCR-U 续配额；事件计费场景 UQT 与服务事件数对应。
- **可选** `SET URRFAILACTION`（[0-00018](task/UDG/20.15.2/0-00018.md)）：Final-Unit-Action 执行期间业务异常时放通（`RETRYFAILACT=CONTINUE`）。
- **配额超时放通约束**：配额耗尽 CCR-U 超时（`T3RESPONSE×N3REQUEST+4s`，`SET UPPFCPPATH` 配）→ PGW-U 阻塞业务；应急放通用 `SET URRFAILACTION:RETRYFAILACT=CONTINUE`。

### UDG 用户面：融合计费特性（[2-00006](task/UDG/20.15.2/2-00006.md)）

走标准配置方法（见 feature task），但有以下**配额降速变种**（融合独有）：

- **URR 双配置 + RGAPPLIED 约束**：URRGROUP 同时绑在线+离线 URR（`UPURRNAME1/DOWNURRNAME1`=离线 + `UPURRNAME2/DOWNURRNAME2`=在线）；RGAPPLIED=DEFAULT 时 URRGROUP 只能配一种模式（仅离线或仅在线，二选一）— 否则计费冲突。
- **排除** `SET UPDEFAULTQUOTA`：配额由 CHF 经 Nchf 统一下发，非 UDG 本地默认配额开关（在线专属；融合不用）。
- **可选** `SET SPECTRAFURRGRP`（[0-00290](task/UDG/20.15.2/0-00290.md)）：整机级全局缺省 URR 组；配额耗尽动作 FORWARD 场景下，未命中 RULE 的流量走本兜底组。

### UNC 控制面：融合计费特性（[2-00003](task/UNC/20.15.2/2-00003.md)）

走标准配置方法（见 feature task），但有以下**配额降速变种**（融合独有）：

- **CCT 模板必配 Trigger**（[1-00005](task/UNC/20.15.2/1-00005.md)）：`VQT/TQT/UQT` 阈值百分比（如 20=20%）→ 触发 CCR-U 申请新配额；`VT`（在线配额有效时长分钟）超时触发重授权；`FUATERMINATE`（终结方式 = TERM_SERVICE 终结整个 PDU 会话 / 其他）。
- **CCT 模板必配终结方式**：`ADD QUOTAEXHAUSTACT`（[0-00066](task/UNC/20.15.2/0-00066.md)）配 BLOCK/REDIRECT/RESTRICT 终结动作——由 Final-Unit-Action 驱动。
- **CCT 绑定层次按 DP 选**（4 层次降级链）：UserProfile（`SET USRPROFCHARGE` 带 CCTEMPLATE+CONVERGEDSW+RGAPPLIED，[1-00002](task/UNC/20.15.2/1-00002.md)）/ APN（`SET APNCHARGECTRL`，[1-00003](task/UNC/20.15.2/1-00003.md)）/ CC（`ADD SELECTCCTBYCC`，[1-00006](task/UNC/20.15.2/1-00006.md)）/ 全局（`MOD CCT CCTMPLTNAME=global`，[0-00114](task/UNC/20.15.2/0-00114.md)）。
- **三联前置**（critical）：`SET CHARGECTRL` 总开关使能 + `SET CHGMODE FORCED=NchfMode` + `SET CHFINIT=SENDREQ`（[1-00008](task/UNC/20.15.2/1-00008.md)）— 否则不发送 Initial 或 Initial 不携带预期 RG。
- **路径 D REAUTHORIZATION**（融合独有）：`ADD RGTRIGGER` + `SET RGRESCTRL`（[1-00008](task/UNC/20.15.2/1-00008.md)）—— CHF Notify REAUTHORIZATION 触发 SMF 查询 UPF 用量并向 CHF 申请新配额。
- **可选**：异常处理（`SET FAILHANDLING` + `ADD PDUSCACT` + `ADD RGRCACT` + `SET CNVRGDCHGPARA`，[1-00010](task/UNC/20.15.2/1-00010.md)）+ 计费消息缓存（`SET N40MSGSTG` + `SET STGTRIGGER` + `SET GLBDFTCHFGROUP`，[1-00011](task/UNC/20.15.2/1-00011.md)）。

### 跨网元/跨特性协同

- **顺序**：UNC 侧 CCT 模板（含 Trigger + FUATERMINATE + QUOTAEXHAUSTACT）+ 三联前置（CHGMODE/CHARGECTRL/CHFINIT）+ CHF 选择先就绪 → UDG 侧 online/offline URR 配置（按 RGAPPLIED 匹配）→ UDG `SET REFRESHSRV`（`REFRESHTYPE=ALL`）最后生效。
- **路径分支**：
  - **路径 A BLOCK**（典型硬切换）：OCS/CHF Final-Unit-Action=BLOCK → UNC.SMF 转 N4 → UPF `QUOTAEXHAUSTACT=BLOCK` → DISCARD 丢弃；用户被强制下线。
  - **路径 B REDIRECT**（典型引导切换）：Final-Unit-Action=REDIRECT → UPF 重定向到门户页（充值/续订）；用户可继续访问但被引导续订。
  - **路径 C FORWARD**（保通不计费）：无 Final-Unit-Action → 走 `DFTURRGRPNAME` 缺省费率组；不阻断但不扣配额。
  - **路径 D REAUTHORIZATION**（融合独有）：CHF Notify(REAUTHORIZATION) → SMF 经 Nchf 申请新配额 → UPF 继续累计；适合动态调整套餐。
- **优先级覆盖**：降速规则（Final-Unit-Action 触发后的限速 RULE）须**最高优先级**（数字最小）覆盖原保障规则的匹配范围——避免部分流量降速不彻底（BR-CH-09 critical 约束）。
- **降速规则匹配覆盖范围**：降速 RULE 的 FLOWFILTER 必须包含原保障 RULE 的匹配范围——否则部分原匹配流量漏降速。
- **数据流闭环**：UDG 累计使用量 → N4/PFCP Usage Report → SMF → Gy/DCC CCR-U（或 Nchf ChargingData Update）→ OCS/CHF 判定耗尽 → Final-Unit-Action/REAUTHORIZATION 下发 → SMF 转 UPF → UPF 执行（BLOCK/REDIRECT/RESTRICT/FORWARD）。
- **一致性**：UDG `ADD URR.RG` = UNC 配置的 RG；URRID 全局唯一；CP/UP 的 `URRID`/`USAGERPTMODE`/`METERINGTYPE`/`RULENAME`/`POLICYNAME`/`USERPROFILENAME` 必须一致。

> UDG 侧优先复用 [1-00010](task/UDG/20.15.2/1-00010.md) 计费三件套 + [1-00009](task/UDG/20.15.2/1-00009.md) 过滤链 + [1-00011](task/UDG/20.15.2/1-00011.md) 规则绑定 + [1-00012](task/UDG/20.15.2/1-00012.md) 计费收尾；UNC 侧融合计费 chain [1-00005](task/UNC/20.15.2/1-00005.md) CCT模板 + [1-00006](task/UNC/20.15.2/1-00006.md) CCT绑CC + [1-00007](task/UNC/20.15.2/1-00007.md) CHF选择 + [1-00008](task/UNC/20.15.2/1-00008.md) SMF-CHF交互 + [1-00010](task/UNC/20.15.2/1-00010.md) 异常处理 + [1-00011](task/UNC/20.15.2/1-00011.md) 消息缓存。

## 决策点

### DP-1：计费方式选择（方案级，选 CS）
进入计费场景时的首要决策，决定走哪个 ConfigurationSolution。

| 选项/场景 | 影响（参数/命令/联动） |
|---|---|
| 离线计费 | 选离线 CS。无配额管理，无 Final-Unit-Action；`CHGMODE` 非 NchfMode |
| 在线计费 | 选在线 CS。UDG 仅 online URR + UNC Gy/DCC/OCS；配额耗尽 OCS Final-Unit-Action |
| 融合计费 | 选融合 CS。UDG 双 URR + UNC Nchf/CCT/CHF；路径 D REAUTHORIZATION 可用 |
| 配额降速与体验切换 | 选本 CS。叠加在在线或融合 CS 之上——配置 `QUOTAEXHAUSTACT` + CCT Trigger + 降速规则 |

### DP-2：Final-Unit-Action 终结方式（★方案核心 DP）
配额耗尽后用户体验切换路径，DP-CH-04 业务级映射。

| 选项/场景 | 影响（参数/命令/联动） |
|---|---|
| BLOCK（阻断） | `ADD QUOTAEXHAUSTACT:BIT=BLOCK`；UPF 执行 DISCARD 丢弃；用户被强制下线（典型硬切断） |
| REDIRECT（重定向） | `ADD QUOTAEXHAUSTACT:BIT=REDIRECT`；UPF 重定向到门户页（充值/续订）；典型体验切换 |
| RESTRICT（限制） | `ADD QUOTAEXHAUSTACT:BIT=RESTRICT`；UPF 限速；保留连接但降速（套餐外限速） |
| FORWARD（放行走默认费率） | 无 Final-Unit-Action；走 `DFTURRGRPNAME` 缺省费率；不计费但保通（路径 C 兜底） |
| REAUTHORIZATION（重授权，融合独有） | CHF Notify(REAUTHORIZATION) → SMF 查询 UPF 用量 → 新配额下发（路径 D） |

### DP-3：CCT 模板配置层次选择
UNC 侧 CCT 模板共享同一套参数骨架，差异仅在绑到哪个对象，4 层次是降级链。

| 选项/场景 | 影响（参数/命令/联动） |
|---|---|
| UserProfile 层 | `SET USRPROFCHARGE` 带 CCTEMPLATE+CONVERGEDSW+RGAPPLIED；优先级最高；走 [1-00002](task/UNC/20.15.2/1-00002.md) |
| APN 层 | `SET APNCHARGECTRL` 带 CCTEMPLATE+CONVERGEDSW+RGAPPLIED；优先级次高；走 [1-00003](task/UNC/20.15.2/1-00003.md) |
| 计费属性 CC 层 | 分两步：① `ADD CHARGEMETHOD` 配 CONVERGED/RGAPPLIED（使能开关）② `ADD SELECTCCTBYCC` 绑 CCVALUE→CCTMPLTNAME（模板绑定）；走 [1-00006](task/UNC/20.15.2/1-00006.md) |
| 全局层 | `MOD CCT`（CCTMPLTNAME=global）；优先级最低；兜底，所有未配层次的最终取值；走 [0-00114](task/UNC/20.15.2/0-00114.md) |

### DP-4：配额阈值与触发（Trigger）
CCT 模板内的配额控制参数，影响续配额时机和耗尽动作触发。

| 选项/场景 | 影响（参数/命令/联动） |
|---|---|
| 阈值百分比触发 | VQT/TQT/UQT（流量/时长/事件阈值百分比，如 20=20%）；到达阈值触发 CCR-U / ChargingData Update 申请新配额 |
| 配额有效时长 | VT（在线配额有效时长，分钟）；超时触发重授权 |
| 终结方式 | FUATERMINATE=TERM_SERVICE（终结整个 PDU 会话）/ 其他；影响配额耗尽后业务处理 |
| RG Trigger | `ADD RGTRIGGER` 配 RG 老化触发条件；与 `SET RGRESCTRL` 配合控制 RG 老化（路径 D REAUTHORIZATION 前提） |

## 约束

- **SA+内容计费+融合 License 前置**（critical）：UDG 侧 SA-Basic（GWFD-110101，`LKV3G5SABS01`）+ 内容计费（GWFD-020301，`LKV3G5BCBC01`）+ UNC 侧内容计费（WSFD-109002，`LKV3W9BCC12`）+ 融合计费（WSFD-011206）License 必须全部开启 — 否则配置命令成功但功能不生效。
- **降速规则最高优先级**（critical，BR-CH-09）：在线/融合配额耗尽后的降速规则必须使用最高优先级（数字最小），且覆盖原保障规则的匹配范围 — 否则部分流量降速不彻底。
- **RGAPPLIED 强约束**（critical，融合场景）：URRGROUP 配置必须匹配 UNC 侧 RGAPPLIED；RGAPPLIED=DEFAULT 时 URRGROUP 只能配一种模式（仅离线或仅在线，二选一），其余模式须双配或单配匹配 — 配错则计费冲突。
- **CP/UP URRID/RG/USAGERPTMODE 跨侧一致**（critical）：UDG `ADD URR.RG` = UNC `ADD URR.RG`（RG 跨侧一致）；URRID 全局唯一；CP/UP 的 `URRID`/`USAGERPTMODE`/`METERINGTYPE`/`RULENAME`/`POLICYTYPE`/`POLICYNAME`/`USERPROFILENAME` 必须一致 — 不一致则计费异常/策略不生效（ALM-81026/81054）。
- **三联前置**（critical，融合场景）：融合计费需同时满足 `CHGMODE=NchfMode` + `CHARGECTRL`（或 USRPROFCHARGE/APNCHARGECTRL）使能 + `CHFINIT=SENDREQ` 三条件 — 否则不发送 Initial 或 Initial 不携带预期 RG。
- **REFRESHSRV 时序**（critical，UDG 侧）：`SET REFRESHSRV:REFRESHTYPE=ALL` 必须在所有 ADD/SET 完成后最后执行；`PROTBINDFLOWF` 配置后需等待 60 秒再执行 REFRESHSRV — 不执行或时序错则 FILTER 配置变更不生效。
- **CCTMPLTNAME 引用键**（critical，UNC 侧）：CCTMPLTNAME 须先建（[1-00005](task/UNC/20.15.2/1-00005.md)）再绑定 — 否则绑定命令找不到模板。
- **同一 RG 在线/离线属性唯一**（critical）：同一计费会话内，同一 RG 要么在线要么离线，不能同时 — 否则计费出错。
- **缓存前提**（critical，UNC 侧）：开启消息缓存（[1-00011](task/UNC/20.15.2/1-00011.md)）必须 FHACTION=CONTINUE + SCACT=FAILOVER/CONTINUE + STGSWITCH=ENABLE + CHGDATAREFGEN=SMF + 配全局默认 CHF 组。
- **每个 USERPROFILE 必绑缺省费率**（critical）：`SET URRGRPBINDING` 的 `DFTURRGRPNAME`（缺省业务费率）+ `DFTSIGURRGNAME`（缺省信令费率） — 否则未匹配费率的报文无法计费（路径 C FORWARD 场景下尤为重要）。
- **路径 D REAUTHORIZATION 前提**（warning，融合场景）：CHF Notify REAUTHORIZATION 触发需 `ADD RGTRIGGER` + `SET RGRESCTRL` 配置；无 RG Trigger 则重授权链不启动。
- **降速 RULE 匹配覆盖**（warning）：降速 RULE 的 FLOWFILTER 必须包含原保障 RULE 的匹配范围 — 否则部分原匹配流量漏降速（与"最高优先级"约束配套）。
- **多 UPF 独立配额**（warning）：MEC 场景下多 UPF 独立配额要求各 UPF 的 URR ID 全局唯一且配额不互相干扰；需要独立的 CHF 会话和 Usage Report 上报通道。
- **N40APIVER 与 CHF 一致**（warning）：APIVER 须与 CHF 使用相同协议版本 — 否则接口信元不一致（ALM-81026）。
- **不支持多 UPF 共享在线 RG 配额**（warning）：多 UPF 场景在线计费 RG 配额不共享，各 UPF 的 URR ID 须全局唯一且配额不互相干扰。
- **不支持 enhanced-ECUR/IEC**（warning）：20.15.2 不支持增强 ECUR/IEC 事件计费、紧耦合。

## 关联
- 上游场景：[计费](business/business-awareness/charging/NetworkScenario@charging.md)
- 编排特性（feature task，优先）：[2-00004 UDG 在线计费](task/UDG/20.15.2/2-00004.md) · [2-00006 UDG 融合计费](task/UDG/20.15.2/2-00006.md) · [2-00003 UNC 融合计费](task/UNC/20.15.2/2-00003.md)
- 复用步骤/命令（compound/atom，按需）：UDG [1-00010](task/UDG/20.15.2/1-00010.md) 计费三件套 · [1-00009](task/UDG/20.15.2/1-00009.md) 过滤链 · [1-00011](task/UDG/20.15.2/1-00011.md) 规则绑定 · [1-00012](task/UDG/20.15.2/1-00012.md) 计费收尾 · [0-00019](task/UDG/20.15.2/0-00019.md) License · [0-00016](task/UDG/20.15.2/0-00016.md) UPDEFAULTQUOTA · [0-00018](task/UDG/20.15.2/0-00018.md) URRFAILACTION · [0-00290](task/UDG/20.15.2/0-00290.md) 全局缺省URR组（FORWARD 路径）；UNC [1-00005](task/UNC/20.15.2/1-00005.md) CCT模板 · [1-00006](task/UNC/20.15.2/1-00006.md) CCT绑CC · [1-00007](task/UNC/20.15.2/1-00007.md) CHF选择 · [1-00008](task/UNC/20.15.2/1-00008.md) SMF-CHF交互 · [1-00010](task/UNC/20.15.2/1-00010.md) 异常处理 · [1-00011](task/UNC/20.15.2/1-00011.md) 消息缓存 · [1-00002](task/UNC/20.15.2/1-00002.md) 绑UserProfile · [1-00003](task/UNC/20.15.2/1-00003.md) 绑APN · [0-00114](task/UNC/20.15.2/0-00114.md) 全局CCT · [0-00066](task/UNC/20.15.2/0-00066.md) QUOTAEXHAUSTACT · [0-00157](task/UNC/20.15.2/0-00157.md) SET CHARGECTRL · [0-00162](task/UNC/20.15.2/0-00162.md) SET CHGMODE · [0-00183](task/UNC/20.15.2/0-00183.md) SET N40APIVER · [0-00177](task/UNC/20.15.2/0-00177.md) SET GLBTARIFFGROUP（费率切换，可选）
- 证据：[计费场景业务图谱_旧版参考](evidence/business/charging/计费场景业务图谱_旧版参考.md)（§2.6 CS-CH-06 配额降速 + §10.6 配额降速端到端流程）