---
id: ConfigurationSolution@bandwidth-coderate-terminal
type: ConfigurationSolution
name: 终端系统码率差异化
domain: business-awareness
scenario: bandwidth-control
status: draft
---

# 终端系统码率差异化

> 按终端 OS 类型（Android/iOS/Windows）差异化码率监管方案。属于[带宽控制](business/business-awareness/bandwidth-control/NetworkScenario@bandwidth-control.md)场景。本方案是带宽族中**唯一直正共享 BWM 对象族的维度增强**——在 BWMRULE 上增加终端平台匹配维度。

## 概览

终端系统码率差异化解决"同一业务/用户组下不同 OS 终端需差异化码率"的诉求：对同一用户组下的 IOS/Android 等操作系统用户差异化执行 CAR 码率监管。核心机制：**BWMSERVICE 增加 OSTYPE 参数维度**（按 OS 识别业务流）→ BWMCONTROLLER（CAR，上下行各一）→ BWMUSERGROUP（组级 NONTOS）→ BWMRULE（GROUP_SPECIFIC）→ 绑定 APN → **APNOSLELBWMSW**（APN 级 OS 差异化开关，末步）。

本方案与 BWM 范本的关系：**共享 BWM 全套对象族**（BWMSERVICE/BWMCONTROLLER/BWMUSERGROUP/BWMRULE/APNBINDBWMUSRG），差异仅在 BWMSERVICE 增 OSTYPE 参数 + 末步加 APNOSLELBWMSW 开关——这是带宽族中与 BWM 正交共享最深的维度增强（其他变种如 Shaping 改 CTRLTYPE、QoS 触发走独立对象族）。

## 配置与协同

本方案编排 **3 个特性**：UDG 核心 [2-00025 终端码率](task/UDG/20.15.2/2-00025.md) + UDG 基础 [2-00001 BWM](task/UDG/20.15.2/2-00001.md)（依赖前提）+ UDG 基础 [2-00019 SA-Basic](task/UDG/20.15.2/2-00019.md)（业务识别前提）。

**特性关系矩阵**（★回答"哪些必配 / 可选 / 包含 / 正交"）：

| 特性 | 角色 | 必配? | 关系说明 |
|---|---|---|---|
| [110301 终端码率](task/UDG/20.15.2/2-00025.md) | 核心 | 必配 | BWMRULE 增加终端平台维度（Android/iOS/Windows）；**共享 BWM 对象族**（唯一直正共享的维度增强）；配置重叠（同一 BWMRULE 加终端维度，BWMSERVICE 增 OSTYPE） |
| [BWM 110311](task/UDG/20.15.2/2-00001.md) | 基础（依赖前提） | 必配 | 110301 是 BWMRULE 维度扩展——共享全套 BWM 对象族骨架；配置重叠（配核心时 BWM 基础结构已含） |
| [SA-Basic](task/UDG/20.15.2/2-00019.md) | 基础（依赖前提） | 必配 | 终端平台识别依赖 SA（PROTOCOLNAME 引用需 SA 特征库）；配置不重叠（SA 配识别链，BWM 配限速对象） |

> 矩阵规则：①**核心**=方案主体（必配）；②**基础/依赖前提**=核心依赖的底层（必配，配置常与核心重叠）；③**维度增强**=正交维度可选叠加（按业务诉求）；④**跨网元对端**=另一网元对应特性（组合）；⑤**二选一**=互斥路径选其一。**配置重叠必须在「关系说明」注明**（防"额外配一遍"误解）。

各特性未变化的配置走其**标准配置方法**（见各 feature task），以下仅说明本方案的**特性级变种/排除项**与**跨特性协同**。

### UDG 核心：终端系统码率差异化（[2-00025](task/UDG/20.15.2/2-00025.md)）

走标准配置方法（见 feature task）。**本方案核心变种**：

- **BWMSERVICE 增 OSTYPE 参数**：`BWMSERVICETYPE=NONTOS,NONTOSSRVTYPE=PROTOCOL,PROTOCOLNAME=http,OSTYPE=IOS`（OSTYPE 是本特性差异维度，BWM 范本无此参数）。同一 PROTOCOLNAME 按 OSTYPE 建多条 BWMSERVICE（按 OS 分流）。
- **BWMCONTROLLER 上下行各一**：CAR 模式，`BWMCNAME="bc-up"/"bc-down"`（上下行分别配置，activation 样例）。
- **BWMRULE 走组级 GROUP_SPECIFIC**：`USERGLEVSRVTYPE=NONTOS`（组级 NONTOS 路径，非用户级 SUBSCRIBER_SPECIFIC）——区别于 Shaping（用户级）。
- **末步 APNOSLELBWMSW 开关**：`SET APNOSLELBWMSW:APNNAME=引用,ISENABLE=ENABLE`（APN 级 OS 差异化总开关，本特性生效前提——不开则 APN 下用户不按 OS 差异化执行）。
- **License**：`LKV3G5RDSC01`（与 BWM 主特性 `LKV3G5TCSA01`、Shaping `LKV3G5SBTS01` 均不同——终端差异化是独立 License 控制项）。

**排除项**：不走用户级 SUBSCRIBER_SPECIFIC（本特性是组级码率差异化，同组内按 OS 分流）；不走 SHAPING（CAR 模式，组级不支持 SHAPING）。

### UDG 基础：BWM（[2-00001](task/UDG/20.15.2/2-00001.md)）

走标准配置方法（见 feature task，BWM 范本）。终端码率复用 BWM 全套对象族骨架——配置高度重叠，不需额外配一遍 BWM。差异（OSTYPE 维度 + 末步开关）在 110301 特性内处理。

### UDG 基础：SA-Basic（[2-00019](task/UDG/20.15.2/2-00019.md)）

走标准配置方法（见 feature task）。PROTOCOLNAME 引用需 SA 特征库（`LOD SIGNATUREDB`+`LOD PARSERDB`+`ADD WELLKNOWNPORT`）——否则 http 等协议识别无效。

### 跨网元/跨特性协同

- **顺序**：SA-Basic 协议识别链就绪 → BWM 对象族骨架就绪（BWMSERVICE 含 OSTYPE/BWMCONTROLLER 上下行各一/BWMUSERGROUP/BWMRULE GROUP_SPECIFIC/APNBINDBWMUSRG）→ `SET BANDWIDTHMNG RANGE=SYSTEM`（组级必配）→ 末步 `SET APNOSLELBWMSW ISENABLE=ENABLE`（APN 级 OS 差异化开关）→ `SET REFRESHSRV`。
- **一致性**：同一 PROTOCOLNAME 下不同 OSTYPE 各建 BWMSERVICE（BWMSERVICENAME 全网唯一）；上下行控制器分别引用（UPBWMCTRLNAME1/DNBWMCTRLNAME1）。
- **APNOSLELBWMSW 与全局开关两级**：APN 级开关承继全局 GLBOSLELBWMSW——全局关则 APN 级开亦无效。

## 决策点

### DP-1：操作系统类型（OSTYPE）

| 选项/场景 | 影响（参数/命令/联动） |
|---|---|
| IOS 终端（activation 演示） | BWMSERVICE OSTYPE=IOS；按 OS 建一条 BWMSERVICE |
| Android 终端（同族扩展） | BWMSERVICE OSTYPE=Android；另建一条 BWMSERVICE（同 PROTOCOLNAME，不同 OSTYPE） |
| 其他 OS（Windows 等） | BWMSERVICE OSTYPE=对应值；同理按 OS 分流 |

> 同一 PROTOCOLNAME 下不同 OSTYPE 各建 BWMSERVICE，实现 OS 间差异化码率。

## 约束

- **License 前置**（critical）：`LKV3G5RDSC01`（110301）+ `LKV3G5TCSA01`（BWM 110311）+ `LKV3G5SABS01`（SA-Basic）—— 全部开启后终端码率差异化才生效。
- **APNOSLELBWMSW 必开**（critical，★ 本特性生效前提）：末步 `SET APNOSLELBWMSW ISENABLE=ENABLE`——不开则 APN 下用户不按 OS 差异化执行，本特性失效（仅有 BWM 规则不生效 OS 差异）。
- **OSTYPE 唯一性**（warning）：同一 PROTOCOLNAME 下不同 OSTYPE 须各建 BWMSERVICE，BWMSERVICENAME 全网唯一。
- **SET BANDWIDTHMNG 必配**（warning）：组级场景 `RANGE=SYSTEM` 必配——否则组级控制范围不明。
- **组级（GROUP_SPECIFIC）非用户级**（info）：本特性是组级码率差异化（同组内按 OS 分流），非 Shaping 的用户级——故 USERGLEVSRVTYPE（组级）非 USERLEVSRVTYPE。
- **CAR 参数推荐**（warning）：CIR=0.5×PIR；CBS≥CIR×1.5×1000/8；PBS≥PIR×1.5×1000/8。
- **新增用户组对在线用户不生效**（warning）：需重激活。
- **REFRESHSRV 时序**（critical）：`SET REFRESHSRV` 必须最后执行。

## 关联

- 上游场景：[带宽控制](business/business-awareness/bandwidth-control/NetworkScenario@bandwidth-control.md)
- 范本派生：[BWM 基础限速](business/business-awareness/bandwidth-control/ConfigurationSolution@bandwidth-bwm.md)（本方案在其上派生，共享 BWM 对象族）
- 编排特性（feature task，优先）：[2-00025 UDG 终端码率](task/UDG/20.15.2/2-00025.md)（核心）· [2-00001 UDG BWM](task/UDG/20.15.2/2-00001.md)（基础依赖）· [2-00019 UDG SA-Basic](task/UDG/20.15.2/2-00019.md)（业务识别前提）
- 复用步骤/命令（compound/atom，按需）：UDG [1-00002](task/UDG/20.15.2/1-00002.md) 业务与控制器（OSTYPE 变种+上下行双控制器）· [1-00003](task/UDG/20.15.2/1-00003.md) 用户组规则绑定（组级 NONTOS）· [1-00001](task/UDG/20.15.2/1-00001.md) License+APN 前置 · [0-00107](task/UDG/20.15.2/0-00107.md) SET APNOSLELBWMSW（特性末步开关）· [0-00019](task/UDG/20.15.2/0-00019.md) License · [0-00015](task/UDG/20.15.2/0-00015.md) REFRESHSRV
- 证据：[UDG 110301 终端码率 特性概述](evidence/business/bandwidth-control/UDG_110301_GWFD-110301 基于终端系统的码率差异化控制特性概述_69712148.md) · [SA-Basic](evidence/business/bandwidth-control/UDG_SA-Basic特性概述.md) · [BWM 主干](evidence/business/bandwidth-control/GWFD-110311 基于业务感知的带宽控制特性概述_77219469.md)
