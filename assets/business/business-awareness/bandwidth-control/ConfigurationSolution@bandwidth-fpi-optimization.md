---
id: ConfigurationSolution@bandwidth-fpi-optimization
type: ConfigurationSolution
name: FPI 业务流标识无线优化
domain: business-awareness
scenario: bandwidth-control
status: draft
---

# FPI 业务流标识无线优化

> 基于 FPI（Flow Packet Identifier）业务流标识触发无线侧差异化调度的资源优化方案。属于[带宽控制](business/business-awareness/bandwidth-control/NetworkScenario@bandwidth-control.md)场景。不共享 BWM 对象族，仅共享 SA 基础——FPI 经 DSCP/GTP-U 扩展头传递 RAN 调度。

## 概览

FPI 业务流标识无线优化解决"高价值业务/用户需无线侧资源倾斜"的诉求：UDG 开启 FPI 差异化控制后，将业务流标识（FPI）映射到业务数据报文的 DSCP 字段或 GTP-U 扩展头传递到无线侧（RAN），无线侧按 FPI 值进行 QoS 差异化调度。核心机制：`SET FPIFUNC` 全局使能 → 三四层过滤链 → PCC 动作属性（下行透传）→ PCC 策略组 → **双 RULE**（POLICYTYPE=PCC 触发 PCC 策略 + POLICYTYPE=REMARK_FPI 标 FPI 值）。

**双 RULE 语义**：RULE1（PCC + POLICYNAME=PCCPOLICYGRPNM）将匹配流绑定到 PCC 策略组；RULE2（REMARK_FPI + REMARKFPISEL=FPI + FPIVALUE=63）给匹配流打 FPI 标记触发无线侧调度。两条 RULE 共用同一 FLOWFILTER（同业务流），PRIORITY 区分。本方案与 BWM 正交（不共享 BWM 对象族），与 QoS 触发（专有承载）也不同——FPI 不建专有承载，而是标记报文传 RAN 调度。

## 配置与协同

本方案编排 **2 个特性**：UDG 核心 [2-00031 FPI业务流标识](task/UDG/20.15.2/2-00031.md) + UDG 基础 [2-00019 SA-Basic](task/UDG/20.15.2/2-00019.md)（业务识别前提）。

**特性关系矩阵**（★回答"哪些必配 / 可选 / 包含 / 正交"）：

| 特性 | 角色 | 必配? | 关系说明 |
|---|---|---|---|
| [110331 FPI业务流标识](task/UDG/20.15.2/2-00031.md) | 核心 | 必配 | FPI + GTP-U 扩展头/DSCP 映射传递 RAN 调度；**不共享 BWM 对象族**（无 BWMSERVICE/BWMCONTROLLER/BWMRULE），仅共享 SA 基础；用 PCCACTIONPROP + 双 RULE（PCC+REMARK_FPI）专属组装 |
| [SA-Basic](task/UDG/20.15.2/2-00019.md) | 基础（依赖前提） | 必配 | 基于 SA 业务识别——过滤链匹配业务流需 SA 基础；配置不重叠（SA 配识别链，FPI 配 SET FPIFUNC/双 RULE） |

> 矩阵规则：①**核心**=方案主体（必配）；②**基础/依赖前提**=核心依赖的底层（必配，配置常与核心重叠）；③**维度增强**=正交维度可选叠加（按业务诉求）；④**跨网元对端**=另一网元对应特性（组合）；⑤**二选一**=互斥路径选其一。**配置重叠必须在「关系说明」注明**（防"额外配一遍"误解）。

> **PCC 基本功能**（[2-00018](task/UDG/20.15.2/2-00018.md)）未单列矩阵行——activation 演示的 POLICYTYPE=PCC RULE1 隐含 PCC 基本功能依赖（PCC 规则体系为 FPI 规则链载体），但特性 wiki「与其他特性的交互」仅显式列 SA-Basic，PCC 依赖级别为 warning（非 critical）。若 PCC backbone 未配，RULE1 无 PCCPOLICYGRP 可绑——实际部署时按需配 PCC 基本功能。

各特性未变化的配置走其**标准配置方法**（见各 feature task），以下仅说明本方案的**特性级变种/排除项**与**跨特性协同**。

### UDG 核心：FPI 业务流标识无线优化（[2-00031](task/UDG/20.15.2/2-00031.md)）

走标准配置方法（见 feature task）。**本方案核心变种**：

- **SET FPIFUNC 全局使能**（特性专属首步）：`FPISWITCH=ENABLE, FPITRANSMETHOD=DSCP`（或 GTPU，按 RAN 能力选）——FPI 信息携带在下行数据报文中。
- **PCCACTIONPROP 下行透传**：`ADD PCCACTIONPROP:UPINITDNGATE=PASS`（FPI 经 DSCP/GTP-U 扩展头传无线侧，下行需直接通过）。
- **双 RULE 专属组装**：RULE1（POLICYTYPE=PCC + POLICYNAME=PCCPOLICYGRPNM）+ RULE2（POLICYTYPE=REMARK_FPI + REMARKFPISEL=FPI + FPIVALUE=63）——两条 RULE 共用同一 FLOWFILTER，PRIORITY 区分（activation 样例 1/2）。
- **License**：`LKV3G5WOFR01`（控制项 82200DHE）。

**排除项**：不走 BWM 对象族（与 BWM 正交，无 BWMSERVICE/BWMCONTROLLER）；不建专有承载（与 QoS 触发正交，无 SADEDICBEARER/QOSPROP）；过滤链仅三四层（无 L7FILTER，activation 演示 TCP）。

### UDG 基础：SA-Basic（[2-00019](task/UDG/20.15.2/2-00019.md)）

走标准配置方法（见 feature task）。FPI 基于 SA 业务识别——过滤链匹配的业务流需 SA 基础（三四层 TCP/UDP 等）。License `LKV3G5SABS01`（控制项 82209749）须同时开启。

### 跨网元/跨特性协同

- **顺序**：SA-Basic 业务识别基础就绪 → `SET FPIFUNC` 全局使能（选 FPI 传递方式）→ 三四层过滤链就绪（FILTER+FLOWFILTER+FLTBINDFLOWF）→ `SET REFRESHSRV` → PCCACTIONPROP（下行透传）→ PCCPOLICYGRP（绑动作属性 + 可选 URRGROUP）→ 双 RULE（PCC + REMARK_FPI）+ USERPROFILE + RULEBINDING。
- **一致性**：双 RULE 共用同一 FLOWFILTERNAME；PRIORITY 不重复（activation：RULE1=1, RULE2=2）；FPIVALUE 全网规划（0~255，与 RAN 侧调度权重对应）。
- **无线侧必须支持**：本特性要求无线侧网元同时支持基于业务流标识的无线资源优化功能——否则 FPI 信息到无线侧不触发调度。

## 决策点

### DP-1：FPI 传递方式（FPITRANSMETHOD）

| 选项/场景 | 影响（参数/命令/联动） |
|---|---|
| DSCP 方式（activation 演示） | `FPITRANSMETHOD=DSCP`；FPI 映射到 DSCP 字段传无线侧；对性能影响可忽略 |
| GTP-U 方式（FPI 取本地规则） | `FPITRANSMETHOD=GTPU` + `FPIPOLICYORIGIN=INTERNAL`；GTP-U 扩展头（最长 12 字节）传 FPI；影响网络 MTU 规划（需整网规划） |
| GTP-U 方式（FPI 取用户报文 DSCP） | `FPITRANSMETHOD=GTPU` + `FPIPOLICYORIGIN=EXTERNAL`；用户下行报文 DSCP 映射 GTP-U 扩展头 |

### DP-2：三四层协议 + FPI 值

| 选项/场景 | 影响（参数/命令/联动） |
|---|---|
| TCP 业务（activation 演示，FPI=63） | FILTER L34PROTOCOL=TCP；RULE2 FPIVALUE=63（全网规划） |
| 其他三四层（UDP/ANY） | FILTER 按目标业务规划；FPIVALUE 全网规划（0~255，与 RAN 调度权重对应表见特性 wiki） |

## 约束

- **License 前置**（critical）：`LKV3G5WOFR01`（110331，控制项 82200DHE）+ `LKV3G5SABS01`（SA-Basic，控制项 82209749）—— 须同时开启。
- **强依赖 SA-Basic**（critical）：UDG 基于 SA 执行业务识别，本特性开通必须同时开启 SA 功能（特性 wiki 明示）。
- **依赖 PCC 基本功能**（warning）：activation 演示 POLICYTYPE=PCC 的 RULE1（POLICYNAME=PCCPOLICYGRPNM），PCC 规则体系为 FPI 规则链载体——PCC backbone 未配则 RULE1 无 PCCPOLICYGRP 可绑。
- **无线侧必须支持**（critical，★ 本特性核心）：要求无线侧网元同时支持基于业务流标识的无线资源优化功能——否则 FPI 信息到无线侧不触发调度。
- **GTP-U 方案影响 MTU 规划**（warning）：GTP-U 扩展头（最长 12 字节）影响网络 MTU 规划，需整网规划 MTU 值；DSCP 方案对性能影响可忽略。
- **双 RULE 共用 FLOWFILTER**（warning）：rule_test1（PCC）与 rule_test2（REMARK_FPI）绑定同一 FLOWFILTERNAME + PRIORITY 区分——PRIORITY 不能重复。
- **与 BWM 正交**（info）：不共享 BWM 对象族，可与 BWM 共存——不会互相干扰。

## 关联

- 上游场景：[带宽控制](business/business-awareness/bandwidth-control/NetworkScenario@bandwidth-control.md)
- 编排特性（feature task，优先）：[2-00031 UDG FPI业务流标识](task/UDG/20.15.2/2-00031.md)（核心）· [2-00019 UDG SA-Basic](task/UDG/20.15.2/2-00019.md)（业务识别前提）· [2-00018 UDG PCC基本功能](task/UDG/20.15.2/2-00018.md)（PCC 规则链载体，warning 级依赖）
- 复用步骤/命令（compound/atom，按需）：UDG [1-00009](task/UDG/20.15.2/1-00009.md) 过滤链（三四层 TCP）· [1-00011](task/UDG/20.15.2/1-00011.md) 规则绑定（双 RULE：PCC + REMARK_FPI 变体）· [0-00109](task/UDG/20.15.2/0-00109.md) SET FPIFUNC（特性专属首步）· [0-00028](task/UDG/20.15.2/0-00028.md) ADD PCCACTIONPROP（下行透传）· [0-00003](task/UDG/20.15.2/0-00003.md) ADD PCCPOLICYGRP（绑动作属性 + 可选 URR 组）· [0-00019](task/UDG/20.15.2/0-00019.md) License · [0-00015](task/UDG/20.15.2/0-00015.md) REFRESHSRV
- 证据：[UDG 110331 FPI 特性概述](evidence/business/bandwidth-control/UDG_110331_GWFD-110331 基于业务流标识的无线资源优化特性概述_05031130.md) · [SA-Basic](evidence/business/bandwidth-control/UDG_SA-Basic特性概述.md) · [UDG PCC基本功能](evidence/business/bandwidth-control/UDG_PCC基本功能特性概述.md)
