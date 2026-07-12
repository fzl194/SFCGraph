# UNC APN 域 · 特性/步骤级 wiki 建设方案

> **范围**：UNC APN 业务域 21 个特性的 feature(2-) + compound(1-) 构建，与 0-00213~0-00280 atom 资产层对接。
> **SOP 准则**：`assets/task/特性步骤级构建SOP.md`（§3.5 防平铺、§3.7 能力型底座、§6 硬约束：调测剥离/防平铺、§8 族内构建顺序）。
> **前置资产**：280 atom（含本批新建 68 条 APN 域 atom）+ UDG APN 域范本（2-00033~46、1-00018~34）+ UNC 计费域既有 19 compound（**不直接复用**，命令集零重合；仅复用作对照）。

## 0. 关键决策摘要（用户已对齐）

| 决策项 | 选择 |
|---|---|
| 范围 | **仅 UNC APN 域 21 特性**（UDG 不归我） |
| compound 复用 | **全新建 UNC 域专属 compound**（**命令集与计费域零重合 + UDG 不能跨产品复用**） |
| UDG 角色 | **仅作设计参考**（结构骨架/场景差异维度/DP 表达 —— 不引用 UDG compound md）|
| 建设顺序 | **按 APN 域依赖链**（会话管理 → 地址分配 → 接入控制 → Radius → IPO/L2TP） |
| 与上方 7 任务的边界 | 上方新建的 68 atom 不再修改反向链接（保持"feature wiki 待建"占位）；本阶段建 feature 时**回填反向链接 + 完成双向闭环** |

> **UDG vs UNC 边界铁律**（CLAUDE.md §5.5 + 用户最终确认）：
> - UDG 与 UNC 是**两个独立产品**（UDG=用户面执行，UNC=控制面中转），compound **不能跨产品复用 md 文件**
> - UDG 的 `task/UDG/20.15.2/{compound-id}.md` 与 UNC 的 `task/UNC/20.15.2/{compound-id}.md` 是**同名不同物**（哪怕编号一样），互不引用
> - UDG 仅作**设计参考**（建 UNC 域 compound 时看 UDG 怎么分阶段、维度怎么拆、场景差异怎么组织），**不复用内容**
> - UDG 的"被引用于"段**不追加**UNC 域 feature 链接（避免反向交叉维护责任）
> - UNC 域每个 compound 全新写，**资产独立**、维护责任独立

## 1. UNC APN 域 21 特性清单（来自 `业务图谱体系/APN业务域/apn-feature-doc-list.md`，UNC 部分）

按依赖链排序，5 批 12 场景子域：

| # | feature_code | 名称 | 类别 | 复杂度 | 优先级 |
|---|---|---|---|---|---|
| 1 | **WSFD-010501** | 会话管理 | APN基础 | 能力型骨架 | ★核心 |
| 2 | WSFD-010503 | 多 PDN/PDU 功能 | APN基础 | 复用会话管理+激活档 | ★核心 |
| 3 | WSFD-010400 | 用户数据管理 | APN基础 | UDM签约+UDM静态分配联动 | ★核心 |
| 4 | WSFD-106203 | 别名 APN | APN基础 | 4 激活档（APN聚合/重定向） | ★核心 |
| 5 | **WSFD-010502** | 地址分配方式 | 地址分配 | **最复杂**（UDM/RADIUS/DHCP/SMF三子方式）| ★核心 |
| 6 | WSFD-010504 | 控制面地址分配方式 | 地址分配 | UDG 对称 GWFD-010104 | ★核心 |
| 7 | WSFD-104410 | L2TP VPN | 地址分配 | LNS分配+APNL2TPCTRL 联动 | ★核心 |
| 8 | WSFD-107021 | 静态地址用户路由冗余 | 地址分配 | UDG 对称 2-00038（重套 UDG 1-00031 不复用）| 辅助 |
| 9 | WSFD-104002 | IPv4v6 双栈接入 | 地址分配 | UDG 对称 2-00039 | ★核心 |
| 10 | WSFD-104001 | IPv6 承载上下文 | 地址分配 | UDG 对称 2-00040 | ★核心 |
| 11 | WSFD-104004 | IPv6 前缀代理 | 地址分配 | UDG 对称 2-00041 | ★核心 |
| 12 | WSFD-104413 | DHCP 功能 | 地址分配 | DHCPv4 仅 2 文件 | ★核心 |
| 13 | WSFD-104005 | DHCPv6 地址分配 | 地址分配 | DHCPv6 仅 2 文件 | ★核心 |
| 14 | **WSFD-011305** | Radius 鉴权接入 | 鉴权计费 | 4 鉴权方式（透明/透明鉴权/不透明/本地）| ★核心 |
| 15 | WSFD-011306 | Radius 功能 | 鉴权计费 | AA 服务器组+工作模式 | ★核心 |
| 16 | WSFD-010301 | 鉴权功能 | 鉴权计费 | 基础鉴权（2G/3G/4G/5G）| ★核心 |
| 17 | WSFD-108007 | 终端二次鉴权 | 鉴权计费 | 辅助 | 辅助 |
| 18 | WSFD-011307 | Radius 抄送功能 | 鉴权计费 | 辅助 | 辅助 |
| 19 | IPFD-015002 | GRE | 接入方式 | UDG 范本 2-00042 | ★核心 |
| 20 | IPFD-016000 | IPSec | 接入方式 | **最复杂**（VNRS+IPsec 双配 9 场景同 UDG 1-00033 思路但命令不同）| ★核心 |
| 21 | WSFD-104411 | MPLS VPN | 接入方式 | UDG 范本 2-00043 | ★核心 |
| - | WSFD-107010 | UPF 选择 | 网元选择 | 1 文件 | ★核心 |
| - | WSFD-010202 | 基于位置区域对等网元选择 | 网元选择 | 辅助 | 辅助 |
| - | **WSFD-106003** | 用户接入控制功能 | 接入控制 | UDG 对称 2-00045（极简） | ★核心 |

**合计 24 特性**（核心 21 + 3 辅助）。本方案按依赖链**先建 17 个★核心（4 批）+ 6 个辅助（1 批=扫尾）**。

> 简化：UDG 域 14 特性在 2-00033~46 共 14 个编号；UNC 域 24 特性按 UNC 复续，已建 2-00001~13 是计费域（13 个），故 UNC APN 域新 feature 编号为 **2-00014~2-00037（共 24 个）**。

## 2. 复合物设计骨架（compound 候选清单 + UDG 参考映射）

> 按 SOP §3.5 防平铺：每个多命令（≥3 条）阶段必须先查复用库 → 再判是否抽 compound。
> **本次建设 UNC APN 域全部 compound 全新建**（用户最终确认：UDG 与 UNC 是两个独立产品，**不能跨产品复用 compound md**，UDG 仅作设计参考）。

### 2.1 UDG → UNC 参考映射（**仅结构参考，不复用 md**）

UNC 域每个候选 compound 在 UDG 域有结构同构的对应（仅供我建 UNC 时**参考阶段划分、维度拆解、场景差异组织**）：

| UDG 域参考 compound（仅参考） | UNC 域**全新建**（结构参考 UDG 但内容/责任独立） |
|---|---|
| UDG 1-00029 APN 接入基础设施 | **UNC 1-00029**（独立建，UNC 域 License 不同） |
| UDG 1-00024 下行 OSPF 路由 | **UNC 1-00030**（独立建，OSPF 命令名同但 atom 跨产品独立） |
| UDG 1-00032 GRE 隧道建立 | **UNC 1-00031**（独立建，UNC GRE 端与 UDG 用户面 GRE 端对称但资产独立） |
| UDG 1-00033 IPSec 隧道建立 | **UNC 1-00032**（独立建，IPSec 协议骨架 UNC/UDG 对称） |
| UDG 1-00030 MPLS VPN | **UNC 1-00033**（独立建，UNC 域无 RT 发布等 VRF 视图差异） |
| UDG 1-00021~28 地址分配族 | **UNC 1-00034**（UNC 用 ADDRPOOL 命名，独立设计） |
| UDG 1-00018~20 能力型骨架 | **UNC 1-00020~22**（独立建能力型骨架，UNC 是控制面触发 PFCP，骨架描述不同） |

### 2.2 UNC APN 域候选 compound 清单（**全部全新建，共 ~10 个**）

| 编号（UNC 独立） | 名称 | 命令集 | 主归属 feature | 设计参考 |
|---|---|---|---|---|
| UNC 1-00020~22 | 能力型骨架 3 个（被依赖维度：地址分配/PCC/N4）| (无) | WSFD-010501 会话管理（§3.7）| UDG 1-00018~20 结构 |
| **UNC 1-00023** | UNC SMF 地址池体系（ADDRPOOL 系）| `ADDRPOOL, ADDRPOOLGRP, ADDRUPGROUP, SECTION, POOLBINDAPN, POOLGRPMAP` | WSFD-010502/104002/104001 | UDG 1-00022 结构（但命名异义 POOL vs ADDRPOOL）|
| **UNC 1-00024** | UNC APN 接入基础设施（L3VPN+VPN+APN+APNADDRESSATTR）| `L3VPNINST, VPNINSTAF, VPNINST, APN, APNADDRESSATTR` | WSFD-010502+ 等 6 域通用 | UDG 1-00029 结构（UNC License 不同）|
| **UNC 1-00025** | UNC Radius 对接链 | `RDSSVR, RDSSVRGRP, APNRDSSVRGRP, APNRDSCLIENTIP, UPFRDSSVR, UPFRDSCLIENTIP, RDSUPFCTRL, UPLIST4RDS` | WSFD-011306 Radius 功能 | 控制面独有（UDG 无 Radius） |
| **UNC 1-00026** | UNC Radius 私有扩展 | `SET RDSACCTREQVSA, SET APNRDSACCTCTRL, SET APNRADIUSATTR` | WSFD-011306 | 控制面独有 |
| **UNC 1-00027** | UNC L2TP APN 控制 | `SET APNL2TPCTRL` (+ 跨产品协同) | WSFD-104410 L2TP | 仅 SET APNL2TPCTRL（UNC 域独有）|
| **UNC 1-00028** | UNC UPF 选择 | `ADD UPNODE, ADD UPFBINDGRP, ADD CPGTPUADDR` | WSFD-107010 | UNC 独有（UDG 无此步骤）|
| **UNC 1-00029** | OSPF 路由发布（接入域路由） | `ADD OSPF, ADD OSPFAREA, ADD OSPFNETWORK, ADD OSPFIMPORTROUTE` | WSFD-010502/104002/104001/104004 | UDG 1-00024 结构（命令同名同义，但 UNC 用其接入侧路由）|
| **UNC 1-00030** | GRE 隧道族 | `ADD GRETUNNEL, MOD GRETUNNEL, RMV GRETUNNEL, ADD INTERFACE, ADD IFIPV4ADDRESS, ADD IPBINDVPN, ADD SRROUTE` | WSFD-010502/IPFD-015002 | UDG 1-00032 结构（命令同名但 UNC-UDG 端独立）|
| **UNC 1-00031** | IPSec 五件套（隧道族）| `ADD L3VPNINSTIPSEC, ADD VPNINSTAFIPSEC, ADD INTERFACEIPSEC, ADD IPBINDVPNIPSEC, ADD IFIPV*ADDRESSIPSEC, ADD ACLGROUP*IPSEC, ADD ACLRULEADV*IPSEC, ADD IPSECPROPOSALIPSEC, ADD IPSECPOLICY, ADD IKEPROPOSAL, ADD IKEPEER, ADD ATTACHIKEPEER, ADD IPSECINTFCFG, ADD IPSECINTFCFGIPSEC, ADD PROPATTACHIPSECPROPOSAL, ADD CERTSCENE, SET IKEGLOBALCONFIG, SET IFIPV6ENABLEIPSEC, ADD IPBINDVPN, ADD IFIPV4ADDRESS, ADD L3VPNINST` | IPFD-016000 IPSec | UDG 1-00033 结构（命令集近同义，但 UNC 域独立建）|
| **UNC 1-00032** | MPLS VPN 基础设施 | `ADD VPNINST, ADD VPNINSTAF, MOD VPNINSTAF, ADD IPBINDVPN, ADD LOGICIP/INF` | WSFD-104411 | UDG 1-00030 结构（UNC 域 VRF/RT 视图可参考但独立）|
| **UNC 1-00033** | L2TP APN 决策 + PFCP 私有信元 | `SET APNL2TPCTRL, SET L2TPKEY, ADD UPCMPT, SET PFCPPVTEXT` | WSFD-104410 | 跨产品协同骨架 |

> **复核**：以上是 UNC APN 域 compound 候选清单，**全部独立建**（即便设计参考 UDG）。

### 2.3 与 UDG 范本的差异（C-U 对称差异，提前在 SOP 附录或新特性中注明）

| 项 | UDG（用户面执行） | UNC（控制面中转）|
|---|---|---|
| 地址池 | `POOL/POOLGROUP/SECTION` | `ADDRPOOL/ADDRPOOLGRP/SECTION/ADDRUPGROUP`（**命名空间独立**） |
| APN 属性 | `SET APNADDRESSATTR`(本端)+`SET ADDRESSATTR`(全局) | `SET APNADDRESSATTR`(本端) |
| 路由发布 | `OSPF/IMPORTROUTE`(下行路由)| `OSPF/IMPORTROUTE`(UPF 接入侧，UNC 用同样命令但角色不同）|
| UPF 选择 | N/A | `ADD UPNODE`+`ADD CPGTPUADDR`（**UNC 独有**，UDG 无对应步骤）|
| 会话建立 | UDG 被动接收 PFCP | UNC 主动触发 N4 PFCP Session Establishment |
| IPSec 微服务 | UDG VNRS+IPsec 双配 | UNC IPsec 微服务（**配对独立**）|
| L2TP LNS | UDG 本地配 L2TPGROUP+L2TPCLIENTIP（用户面） | UNC 仅 SET APNL2TPCTRL（控制面下发到 UPF） |

### 2.4 UNC APN 域不复用现有 19 个计费/PCC compound 的判定

UNC 现有 19 个 compound（1-00001~19）多为计费/PCC/BWM/ADC 域，命令集与 APN 域命令集**几乎零重合**（仅 1-00003/0-00008 与 APNUSRPROFG 有轻交集但相位异义）。**不直接复用**，仅当 APN 域特性需计费联动时（如 Radius COPY 到 CDR 关联）才 reference。

> **结论（最终版）**：UNC APN 域 compound **全新建共 ~10 个**（3 骨架 + 7 域内族通用骨架 + 1 跨产品协同骨架），UDG 仅作**结构参考**。

### 2.2 与 UDG 范本的差异（C-U 对称差异，提前在 SOP 附录或新特性中注明）

| 项 | UDG（用户面执行） | UNC（控制面中转）|
|---|---|---|
| 地址池 | `POOL/POOLGROUP/SECTION` | `ADDRPOOL/ADDRPOOLGRP/SECTION/ADDRUPGROUP` |
| APN 属性 | `SET APNADDRESSATTR`(本端)+`SET ADDRESSATTR`(全局) | `SET APNADDRESSATTR`(本端) |
| 路由发布 | `OSPF/IMPORTROUTE`(下行路由)| `OSPF/IMPORTROUTE`(UPF 接入侧) |
| UPF 选择 | N/A | `ADD UPNODE`+`ADD CPGTPUADDR`（UNC 独有）|
| 会话建立 | 被动接收 PFCP | 主动触发 N4 PFCP Session Establishment |

UDG 1-00029 「APN 接入域基础设施」与 UNC 同名 compound **部分命令重合但场景不同**，不复用。

## 3. 批次计划（5 批，按依赖链）

| 批 | 主题 | 特性编号 | 数量 | compound 编号 | 工时估 |
|---|---|---|---|---|---|
| **批1** | **会话管理骨架** | 2-00014（WSFD-010501 能力型） | 1 feature + 3 骨架 | `UNC 1-00020~22`（**全新建**，参考 UDG 1-00018~20 结构）| 半天 |
| **批2** | **APN基础+地址分配**（最复杂族） | 2-00015~22（WSFD-010502/010504/104410/107021/104002/104001/104004/104413/104005）| 9 feature | `UNC 1-00023（ADDRPOOL 地址池体系）+ UNC 1-00024（APN 接入基础设施）+ UNC 1-00029（OSPF 路由）+ **先建 010502 把 UNC 1-00023 场景差异填全**` | 2 天 |
| **批3** | **鉴权计费** | 2-00023~28（WSFD-011305/011306/010301/108007/011307）| 5 feature | `UNC 1-00025（Radius 对接链）+ UNC 1-00026（Radius 私有扩展）` | 1 天 |
| **批4** | **接入方式（IPSec/GRE/MPLS）** | 2-00029~31（IPFD-015002/016000/WSFD-104411）| 3 feature | `UNC 1-00030（GRE 隧道族）+ UNC 1-00031（IPSec 五件套）+ UNC 1-00032（MPLS VPN 基础设施）+ UNC 1-00033（L2TP APN 控制）` | 2 天 |
| **批5** | **网元选择+接入控制+扫尾** | 2-00032~37（WSFD-107010/010202/106003 + 3 辅助）| 6 feature | `UNC 1-00028（UPF 选择）+ 单 atom` | 半天 |

> **compound 总数（最终版）**：
> - 全新建 UNC 域 compound：**~10 个**（3 骨架 + 1 ADDRPOOL + 1 APN 接入基础设施 + 1 OSPF + 1 GRE + 1 IPSec + 1 MPLS + 1 Radius 对接 + 1 Radius 私有 + 1 L2TP + 1 UPF）
> - **不跨产品复用 UDG compound**（用户最终确认：UDG/UNC 是独立产品，compound 不跨产品共享）

> **族内顺序**（SOP §8）：批2 先建 `WSFD-010502` 地址分配方式（含 UDM/Radius/DHCP 三子方式 + SMF 三子方式），把通用 compound 的「场景差异」一次性补到位；再建 `WSFD-104002/104001` 等参数变种特性。

## 4. 每特性构建流程（沿用 SOP §2 单特性 pass）

1. 收集资产：原始 md 清单（CSV 按 feature_code 过滤）+ 已有特性知识 md（业务图谱体系/APN业务域/feature-knowledge/）+ 已有 atom（查 _numbering.json 拿命令→编号）
2. 理解特性：核心对象模型 + 通用配置流程 + 多场景差异维度
3. **补缺失 atom**：本批新命令都已在 0-00213~0-00280 覆盖（68 条新建），但需复核每特性用到的命令是否齐
4. 设计 compound 拆分：按 §3 复用优先 + §3.5 存在前提 + §3.7 能力型底座
5. 建 compound wiki（模板 §4）
6. 建 feature wiki：编排 compound + 特性级 DP 场景影响表
7. **拷证据**：激活方法 md → `assets/evidence/UNC/20.15.2/`（自包含）
8. **双向链接回填**：atom 的"被引用于"段，**本批 68 条 atom 的反向链接全部回填本特性 feature wiki**
9. 更新 index.md（compound 复用库 + feature/atom 段）+ _numbering.json

## 5. 质检点（每批后）

| R1 审视维度 | 关键检查 |
|---|---|
| **R1.1 覆盖度** | 特性配置流程覆盖所有操作步骤（含子分支）|
| **R1.2 复用合理性** | 防平铺（≥3 atom 连续无 compound 强制抽）+ 防假通用（场景差异逐 feature 列）|
| **R1.5 证据链** | 配置流程每命令/参数可追溯到 evidence（无证据 → 移除或加 "本特性不配/由 X 决定"）|
| **R2.4 调测剥离** | 配置流程 0 DSP/LST/EXP/STP/STR；调测作为 evidence 链接不展开 |
| **R2.5 平铺检查** | feature 配置流程连续 ≥3 atom 无 compound 视为平铺失败 |
| **能力型骨架** | WSFD-010501: status:foundation，3 个骨架 compound |
| **C-U 对称差** | UNC 不复用 UDG compound，但 DP 表/场景差异表对齐 UDG 范本的可对比维度 |

## 6. 风险点

| 风险 | 缓解 |
|---|---|
| atom 反向链接回填 68 条工作量 | 用脚本/批量编辑一次完成（不重写 atom 内容，只追加 "被引用于" 行的 feature wiki 链接）|
| compound 场景差异欠债 | 严格按 SOP §8 「先建最复杂 → 后建简单」一次性补全 |
| 证据拷贝量大（每特性 5~10 个激活 md） | 用脚本 cp 批量；evidence 目录结构 `{feature_id}/{filename}.md` |
| 子 Agent 失败重演（429 quota/电脑重启） | **本批不派子 Agent**，主 Agent 一条条建质量优先；如有 Agent 协助，只用于机械性 md 拷贝 |
| UNC 与 UDG C-U 误复用 | 复核 §2.2 差异表后再引用 compound |

## 7. 编号与文件规划

- **feature** 编号：2-00014~2-00037（共 24 个）
- **compound** 编号：UNC 全新建 ~10 个（`UNC 1-00020~1-00033`，**不跨产品复用 UDG**）
- **atom**：现有 0-00213~0-00280（68 条）+ 0-00004/8/40/43/44/47/71/73/81/89/94/96/98/99 等复用
- **evidence** 目录：`assets/evidence/UNC/20.15.2/{feature_id}/`
- **index 段**：追加 24 feature 行 + ~10 个 UNC 全新 compound 行（已建的 24 个 UNC 计费域 compound 不动，UDG 域 index 不动）

## 8. 下一步确认

开工前请用户对齐：
1. **特性编号 2-00014~37**（接续现有 2-00001~13 计费域）—— OK？
2. **compound：UNC 全新建 ~10 个**（UNC 1-00020~33，**UDG 仅参考不复用**）—— OK？
3. **5 批建设顺序**（会话骨架→地址分配族→鉴权族→接入方式→扫尾）—— OK？
4. **不派子 Agent，主 Agent 一条条建**（质量优先）—— OK？
5. **atom 反向链接回填**：每批建完回填本批相关 atom 的"被引用于"段
6. **跨产品边界**：UNC feature 涉及 UDG 域命令时（OSPF/GRE/IPSec/MPLS），UNC 独立写 compound，**不 link UDG compound**；仅在 UNC 配置流程脚注说"对应 UDG 同名命令原理见 UDG 域 wiki"

确认后开干批 1（会话管理骨架，最简单，先打通流程）。
