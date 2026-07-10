---
id: ConfigurationSolution@charging-offline
type: ConfigurationSolution
name: 离线计费
domain: business-awareness
scenario: charging
status: draft
---

# 离线计费
> 通过 RG 标识业务，UDG 侧 URR 累计流量/时长/事件，UNC 侧格式化为话单经 Ga 接口发送到 CG，CG 标准化后送 BD 出账单。非实时后付费。属于[计费](business/business-awareness/charging/NetworkScenario@charging.md)场景。编排 UDG+UNC 跨网元 feature task。

## 概览
离线计费（Offline Charging）是后付费方式：UDG（SGW-U/PGW-U/UPF）按业务统计时长/流量/事件，经 N4/PFCP Usage Report 上报 UNC（SMF/PGW-C），UNC 格式化为 CDR 话单通过 **Ga 接口**（GTP'）发送到 CG（话单网关），CG 标准化后经 Bx 上传 BD 营账系统出账单。与在线/融合计费的核心差异：**无实时配额管理**，不与 OCS/CHF 交互，仅事后统计出账。

本方案编排 3 个特性跨网元协同——UDG 侧[离线计费特性 2-00005](task/UDG/20.15.2/2-00005.md) + [内容计费特性 2-00003](task/UDG/20.15.2/2-00003.md)；UNC 侧[离线计费特性 2-00001](task/UNC/20.15.2/2-00001.md)：
- **UDG 用户面（UPF）**：每业务配单条 URR（`USAGERPTMODE=OFFLINE` + `OFFMETERINGTYPE` 选 VOLUME/TIME/EVENT），复用内容计费通用 backbone（计费三件套 + 过滤链 + 规则绑定 + 计费收尾）。累计使用量经 N4/PFCP Usage Report 上报 SMF。
- **UNC 控制面（SMF）**：配置 **OFCTemplate**（离线计费模板：话单版本+计费方式+阈值+话单触发），按 4 层次降级链（UserProfile > APN > CC > 全局）之一绑定。话单经 Ga 接口送 CG。

核心架构：UDG ↔(N4/PFCP)↔ UNC ↔(Ga/GTP')↔ CG ↔(Bx/FTP)↔ BD。

## 配置与协同

本方案跨网元编排 **3 个特性**：UDG 侧 [2-00005 离线计费](task/UDG/20.15.2/2-00005.md) + [2-00003 内容计费](task/UDG/20.15.2/2-00003.md)；UNC 侧 [2-00001 离线计费](task/UNC/20.15.2/2-00001.md)。

**特性关系矩阵**（★回答"哪些必配 / 可选 / 包含 / 正交"，追溯原始文档「与其他特性的交互」段 + feature task 依赖声明）：

| 特性 | 角色 | 必配? | 关系说明 |
|---|---|---|---|
| [UDG 离线计费 2-00005](task/UDG/20.15.2/2-00005.md) | 核心（方案主体） | 必配 | 本方案的计费模式（offline URR + Ga/CG 话单），含费率三件套基础 |
| [UDG 内容计费 2-00003](task/UDG/20.15.2/2-00003.md) | 业务粒度增强（维度） | 可选 | 按业务差异化费率时叠加；**费率三件套与离线计费配置重叠——配离线计费时三件套已含内容计费结构，不需额外配内容计费**；不按业务粒度则离线计费用默认费率 |
| [UNC 离线计费 2-00001](task/UNC/20.15.2/2-00001.md) | 跨网元对端 | 必配 | UNC 侧 OFCTemplate + Ga 发送，与 UDG 对端组合 |

> 矩阵规则：①**核心**=方案主体（必配）；②**基础/依赖前提**=核心依赖的底层（必配，配置常与核心重叠）；③**维度增强**=正交维度可选叠加（按业务诉求）；④**跨网元对端**=另一网元对应特性（组合）；⑤**二选一**=互斥路径选其一。**配置重叠必须在「关系说明」注明**（防"额外配一遍"误解）。

各特性未变化的配置走其**标准配置方法**（见各 feature task），以下仅说明本方案的**特性级变种/排除项**与**跨网元协同**。

### UDG 用户面：离线计费特性（[2-00005](task/UDG/20.15.2/2-00005.md)）

走标准配置方法（见 feature task），但有以下**变种/排除**（离线独有）：

- **单 URR 变种**：计费三件套每业务只配 1 条 **offline URR**（`USAGERPTMODE=OFFLINE` + `OFFMETERINGTYPE`），不配 online URR。与融合计费的双 URR（offline+online 同组）不同，离线方案 URRGROUP 仅绑离线 URR（`UPURRNAME1`/`DOWNURRNAME1`=offline URR，不配 2）。这是离线计费对该特性标准配置的核心特化。
- **OFFMETERINGTYPE 选值**：按业务选 VOLUME（流量，默认）/ TIME（时长）/ EVENT（事件）/ 组合 / FREE（免费防欺诈）；含 EVENT 的取值有性能影响（见 [2-00005](task/UDG/20.15.2/2-00005.md) DP）。
- **排除** `SET UPDEFAULTQUOTA`：离线计费无 OCS 实时配额，不申请配额，不配默认配额开关（在线/融合专属）。
- **排除** CCT 模板：CCT 是融合计费专属（Nchf/N40 接口），离线方案用 OFCTemplate（UNC 侧），UDG 侧无 CCT 相关配置。
- **刷新类型**：`SET REFRESHSRV:REFRESHTYPE=USERPROFILE`（非融合/内容的 ALL，以原始文档操作步骤为准）。
- **可选** `SET URRFAILACTION`（[0-00018](task/UDG/20.15.2/0-00018.md)）：URR 上报失败时放通业务不计费（`RETRYFAILACT=CONTINUE`）。

### UDG 用户面：内容计费特性（[2-00003](task/UDG/20.15.2/2-00003.md)）

走标准配置方法（见 feature task），**无特性级变种**。内容计费提供通用 backbone（计费三件套 + 过滤链 + 规则绑定 + 计费收尾），离线计费特性在其上做 URR 离线参数特化。

### UNC 控制面：离线计费特性（[2-00001](task/UNC/20.15.2/2-00001.md)）

走标准配置方法（见 feature task），核心是 **OFCTemplate**（非融合的 CCT）：

- **OFCTemplate 模板**（[1-00001](task/UNC/20.15.2/1-00001.md)）：配置话单版本（GUL 切换须 R8+）+ 计费方式（`TQM=QCT`）+ 阈值（`TIMETHRESHOLD`/`VOLUMETHRESHOLD`）+ 话单触发条件（`SET CDRTRIGGER`/`SET CONTAINERTRIGGER`）。这是离线计费的话单容器。
- **绑定层次**（DP-2 选）：4 层次降级链 UserProfile > APN > CC > 全局，高一级未配取下一级。通常走 UserProfile 层（[1-00002](task/UNC/20.15.2/1-00002.md)）或 APN 层（[1-00003](task/UNC/20.15.2/1-00003.md)）。
- **CG 对接前置**：须先完成"配置到 CG 的数据"（Ga 接口对接，见特性 wiki），CG 接收话单后标准化送 BD。

### 跨网元/跨特性协同

- **顺序**：UNC 侧 OFCTemplate + CG 对接先就绪 → UDG 侧 offline URR 配置（URRID/RG 与 UNC 一致）→ UDG `SET REFRESHSRV`（`REFRESHTYPE=USERPROFILE`）最后生效。
- **数据流**：UDG 累计使用量 → N4/PFCP Usage Report → UNC 格式化 CDR → Ga/GTP' → CG 标准化 → Bx → BD 营账。
- **一致性**：UDG `ADD URR.RG` = UNC 配置的 RG（跨侧一致）；URRID 全局唯一；CP/UP 的 `URRID`/`USAGERPTMODE=OFFLINE`/`OFFMETERINGTYPE`/`RULENAME`/`POLICYNAME`/`USERPROFILENAME` 必须一致（见约束段）。

> 方案优先复用已有 UDG 1-00009~1-00012 与 UNC 1-00001~1-00004，不新建 atom/compound（跨网元协同已由两侧 feature task 覆盖）。

## 决策点

### DP-1：计费方式选择（方案级，选 CS）
进入计费场景时的首要决策，决定走哪个 ConfigurationSolution。

| 选项/场景 | 影响（参数/命令/联动） |
|---|---|
| 离线计费 | 选本 CS。UDG 仅 offline URR + UNC Ga/CG 接口；无配额管理；`CHGMODE` 非 NchfMode；OFCTemplate 模板 |
| 在线计费 | 选在线 CS。UDG 仅 online URR + UNC Gy/DCC/OCS 接口；配额实时申请 |
| 融合计费 | 选融合 CS。UDG 双 URR（offline+online）+ UNC Nchf/CCT/CHF 全链 |

### DP-2：OFCTemplate 绑定层次选择
UNC 侧 OFCTemplate 共享同一套参数骨架，差异仅在绑到哪个对象，4 层次是降级链。

| 选项/场景 | 影响（参数/命令/联动） |
|---|---|
| UserProfile 层 | `SET USRPROFCHARGE` 绑 OFCTEMPLATE；优先级最高；走 [1-00002](task/UNC/20.15.2/1-00002.md) |
| APN 层 | `SET APNCHARGECTRL` 绑 OFCTEMPLATE；优先级次高；走 [1-00003](task/UNC/20.15.2/1-00003.md) |
| 计费属性 CC 层 | `ADD CHARGECHAR` + `ADD GLBOFCTEMPLATE` 绑 CC→模板；优先级次低；走 [1-00004](task/UNC/20.15.2/1-00004.md) |
| 全局层 | `ADD GLBOFCTEMPLATE`；优先级最低；兜底，所有未配层次的最终取值；走 [0-00033](task/UNC/20.15.2/0-00033.md) |

### DP-3：离线统计类型 OFFMETERINGTYPE
UDG 侧 URR 的统计维度，影响话单上报内容。

| 选项/场景 | 影响（参数/命令/联动） |
|---|---|
| 按流量计费（默认） | `OFFMETERINGTYPE=VOLUME`；统计流量字节数 |
| 按时长计费 | `OFFMETERINGTYPE=TIME`；统计时长 |
| 按事件计费 | `OFFMETERINGTYPE=EVENT`；统计事件次数；**性能有影响**，评估后使用 |
| 流量+时长 | `OFFMETERINGTYPE=VOLUME_TIME`；统计流量和时长 |
| 免费（防欺诈） | `OFFMETERINGTYPE=FREE`；该 URR 有欺诈风险，需配合 UNC 做防欺诈判断 |

## 约束

- **SA+内容计费 License 二前置**（critical）：UDG 侧 SA-Basic（GWFD-110101）+ 内容计费基本功能（GWFD-020301，`LKV3G5BCBC01`）License 必须开启 — 否则配置命令成功但功能不生效。
- **URR 离线一致性**（critical）：`URRID`/`USAGERPTMODE=OFFLINE`/`OFFMETERINGTYPE` 在 SGW-C/PGW-C 与 SGW-U/PGW-U 必须一致 — 不一致则计费行为异常。
- **USERPROFILE/RULE 跨侧一致**（critical）：`USERPROFILENAME`/`RULENAME`/`POLICYTYPE`/`POLICYNAME` 在 PCRF/SGW-C/PGW-C/SGW-U/PGW-U 间必须一致 — 不一致则策略无法按预期生效。
- **RG 跨侧一致**（critical）：UDG `ADD URR.RG` = UNC 配置的 RG — 不一致则报表与实际计费不一致。
- **URRID 全网唯一**（critical）：建议从 1000 开始分配 — 重复则 PFCP Session Report 无法关联。
- **REFRESHSRV 时序**（critical，UDG 侧）：`SET REFRESHSRV:REFRESHTYPE=USERPROFILE` 必须在所有 ADD/SET 完成后最后执行 — 不执行或时序错则 FILTER 配置变更不生效。
- **每个 USERPROFILE 必绑缺省费率**（critical）：`SET URRGRPBINDING` 的 `DFTURRGRPNAME`（缺省业务费率）+ `DFTSIGURRGNAME`（缺省信令费率） — 否则未匹配费率的报文无法计费。
- **模板名是引用键**（critical，UNC 侧）：OFCTEMPLATENAME 须先建（[1-00001](task/UNC/20.15.2/1-00001.md)）再绑定 — 否则绑定命令找不到模板。
- **CG 对接前置**（warning，UNC 侧）：须先完成 Ga 接口到 CG 的数据配置 — 否则话单无法上报。
- **话单版本跨网元一致**（warning）：GCDRVERSION/PGWCDRVERSION/SGWCDRVERSION 全网规划；GUL 切换网络须 R8+ — 否则话单不兼容。
- **4 层次降级链**（warning，UNC 侧）：UserProfile > APN > CC > 全局，高一级未配取下一级 — 规划时注意最终生效层次。
- **含 EVENT 的 OFFMETERINGTYPE 性能影响**（warning）：EVENT/EVENT_VOLUME/EVENT_TIME/EVENT_VOLUME_TIME 对性能有影响 — 执行前评估。

## 关联
- 上游场景：[计费](business/business-awareness/charging/NetworkScenario@charging.md)
- 编排特性（feature task，优先）：[2-00005 UDG 离线计费](task/UDG/20.15.2/2-00005.md) · [2-00003 UDG 内容计费](task/UDG/20.15.2/2-00003.md) · [2-00001 UNC 离线计费](task/UNC/20.15.2/2-00001.md)
- 复用步骤/命令（compound/atom，按需）：UDG [1-00010](task/UDG/20.15.2/1-00010.md) 计费三件套 · [1-00009](task/UDG/20.15.2/1-00009.md) 过滤链 · [1-00011](task/UDG/20.15.2/1-00011.md) 规则绑定 · [1-00012](task/UDG/20.15.2/1-00012.md) 计费收尾 · [0-00019](task/UDG/20.15.2/0-00019.md) License · [0-00018](task/UDG/20.15.2/0-00018.md) URRFAILACTION；UNC [1-00001](task/UNC/20.15.2/1-00001.md) OFCTemplate模板 · [1-00002](task/UNC/20.15.2/1-00002.md) 绑UserProfile · [1-00003](task/UNC/20.15.2/1-00003.md) 绑APN · [1-00004](task/UNC/20.15.2/1-00004.md) 绑CC · [0-00033](task/UNC/20.15.2/0-00033.md) 全局OFCT
- 证据：[计费场景业务图谱_旧版参考](evidence/business/charging/计费场景业务图谱_旧版参考.md)（§2.1 CS-CH-01 离线 + §10.1 离线端到端流程）
