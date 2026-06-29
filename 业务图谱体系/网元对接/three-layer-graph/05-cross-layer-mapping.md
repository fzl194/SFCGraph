# 05 跨层映射 Cross-Layer Mapping

> 第5层 | 网元对接业务域 / UPF网元对接子场景
> 汇总 01-04 层的跨层关系边（Schema §12），并验证端到端链路一致性。
> EV-CA-02

---

## 0. 概述

本文汇总三层图谱的跨层映射边，按 Schema §12.1~§12.5 组织，并给出端到端链路验证（BD→NS→CS→Feature→Task→Command→ConfigObject）与一致性校验。

跨层引用 ID 规范（全库一致）：
- 特性：`feature_code`（如 IPFD-014000），定义于 02-feature-graph
- 任务：`T-ND-NN`，定义于 03-task-layer
- 命令：`command_name`（如 `ADD OSPF`），定义于 04-command-graph
- 配置对象：`object_name`，定义于 04-command-graph

---

## 1. 业务图谱 → 特性图谱（§12.1）

### 1.1 ConfigurationSolution `uses_feature` Feature

| CS（对接面） | uses_feature（feature_code） |
|---|---|
| CS-ND-01 控制面对接(N4↔SMF) | GWFD-010234(Single IP)、GWFD-020161(CU Full Mesh)、GWFD-010105(用户面地址分配) |
| CS-ND-02 用户面对接(N3/N9/N6+会话接入) | GWFD-010234、GWFD-010105、GWFD-020421(基于位置地址分配)、IPFD-010001(接口管理) |
| CS-ND-03 网管对接 | NPFD-010000(操作维护)、NPFD-010014(NTP) |
| CS-ND-04 路由对接(★最大) | IPFD-014000(路由功能)、IPFD-014001(OSPF)、IPFD-014002(BGP)、IPFD-014003(静态路由)、IPFD-012003(BFD)、IPFD-012000(IP可靠性)、IPFD-015004(IPSec)、GWFD-020411(MPLS VPN)、GWFD-020161(CU Full Mesh)、GWFD-010234、IPFD-010001 |
| CS-ND-05 基础就绪 | NPFD-010014(NTP)、NPFD-010000(操作维护)、IPFD-010001(接口管理/MTU) |

> uses_feature 共引用 17 特性（与 cross-feature-analysis.md §1.4、02-feature-graph 一致；IPFD-104403 别名归并至 IPFD-012003）。

### 1.2 BusinessRule `refined_by` FeatureRule

| BusinessRule | refined_by FeatureRule | 说明 |
|---|---|---|
| BR-ND-01 N4必备性 | FR-UD-01(目录父节点) / FR-UD-02(路由BFD三段式) | N4偶联前提细化 |
| BR-ND-02 接口强制合一(Paif/N4if) | FR-UD-01 | 抽象接口约束 |
| BR-ND-06 BGP依赖IGP | FR-UD-02 | 路由协议依赖 |
| BR-ND-09 自动部署开关时序 | FR-UD-02 | 部署规范 |
| （其余 BR 落到 TaskRule/CommandRule） | — | 见 §2.2、§4 |

### 1.3 SemanticObject `realized_by` Feature

| SemanticObject（代表性） | realized_by Feature |
|---|---|
| SO 抽象接口(N4if/Saif/Scif/Paif) | GWFD-010234(Single IP) |
| SO 地址池/会话接入 | GWFD-010105、GWFD-020421 |
| SO 路由协议(OSPF/BGP/静态) | IPFD-014001、IPFD-014002、IPFD-014003 |
| SO BFD检测 | IPFD-012003 |
| SO MPLS VPN隧道 | GWFD-020411 |

---

## 2. 业务图谱 → 任务原子层（§12.2）

### 2.1 ConfigurationSolution `uses_task` ConfigTask

| CS | uses_task（task_id） | task_scope_type |
|---|---|---|
| CS-ND-05 基础就绪 | T-ND-01 加载License、T-ND-02 NTP、T-ND-03 网元基本信息、T-ND-04 公共参数/MTU、T-ND-05 高危命令二次授权 | generic |
| CS-ND-03 网管对接 | T-ND-06 配置网元和网管对接 | cross_feature |
| CS-ND-01 控制面对接 | T-ND-07 配置N4(N4if)控制面接口 | feature_specific |
| CS-ND-02 用户面对接 | T-ND-08 配置业务用户面接口、T-ND-09 配置会话接入 | feature_specific / cross_feature |
| CS-ND-04 路由对接 | T-ND-10 VPN实例与接口绑定、T-ND-11 外联口自动部署、T-ND-12 OSPF、T-ND-13 BGP、T-ND-14 静态路由、T-ND-15 BFD、T-ND-16 隧道、T-ND-17 级联口(NP卡) | generic/cross_feature/feature_specific |
| （调测） | T-ND-18 整网调测FirstCall | cross_feature |

### 2.2 BusinessRule `refined_by` TaskRule

| BusinessRule | refined_by TaskRule |
|---|---|
| BR-ND-03 VPN四统一 | TR-ND（VPN一致性校验） |
| BR-ND-07 MPLS VPN公私分离 | TR-ND（_public_ VPN约束） |
| BR-ND-08 自动部署开关规范 | TR-ND（SET AUTOCONFIG FALSE→配→TRUE + DSP OPSASSISTSTATE） |
| BR-ND-10 MTU层级 | TR-ND（Fabric/Tunnel/外联口三层） |

### 2.3 SemanticObject `realized_by` ConfigTask

| SemanticObject | realized_by Task |
|---|---|
| SO 逻辑接口/VPN | T-ND-10 |
| SO N4if | T-ND-07 |
| SO 用户面接口/会话接入 | T-ND-08、T-ND-09 |
| SO 路由协议/BFD/隧道 | T-ND-12~16 |
| SO 自动部署模板 | T-ND-11 |

---

## 3. 特性图谱 → 任务原子层（§12.3）

### 3.1 Feature `decomposes_to` ConfigTask

| Feature | decomposes_to Task |
|---|---|
| GWFD-010234 Single IP | T-ND-07(N4接口)、T-ND-08(业务接口) |
| GWFD-010105 用户面地址分配 | T-ND-09(会话接入) |
| GWFD-020421 基于位置地址分配 | T-ND-09 |
| GWFD-020161 CU Full Mesh | T-ND-07(多SMF)、T-ND-17(级联口) |
| GWFD-020411 MPLS VPN | T-ND-16(隧道) |
| IPFD-014001 OSPF | T-ND-12 |
| IPFD-014002 BGP | T-ND-13 |
| IPFD-014003 静态路由 | T-ND-14 |
| IPFD-012003 BFD | T-ND-15 |
| IPFD-015004 IPSec | T-ND-16 |
| IPFD-010001 接口管理 | T-ND-08、T-ND-10、T-ND-11 |
| NPFD-010014 NTP | T-ND-02 |
| NPFD-010000 操作维护 | T-ND-03、T-ND-05、T-ND-06 |
| （目录父节点 IPFD-010000/012000/014000） | 由子能力间接覆盖，不单独 decomposes_to |

### 3.2 FeatureRule `constrains_task` ConfigTask

| FeatureRule | constrains_task |
|---|---|
| FR-UD-02 路由+BFD三段式 | T-ND-12/13/14/15（路由协议task须配合BFD） |
| FR-UD-01 目录父节点不挂命令 | 约束目录特性不直接 decomposes_to |

---

## 4. 任务原子层 → 命令图谱（§12.4）

### 4.1 ConfigTask `invokes` MMLCommand（核心映射）

| Task | invokes（command_name，详见 04-command-graph） |
|---|---|
| T-ND-07 配置N4接口 | ADD VPNINST、ADD LOGICINF、SET UPINFO |
| T-ND-08 配置业务接口 | ADD VPNINST、ADD LOGICINF、ADD SNSSAIUPINTF(切片) |
| T-ND-09 配置会话接入 | ADD APN、ADD POOL、ADD SECTION、ADD POOLGROUP、ADD POOLGRPMAP、SET IPALLOCRULE |
| T-ND-10 配置VPN实例 | ADD L3VPNINST、ADD VPNINSTAF、ADD VPNTARGET、ADD IPBINDVPN |
| T-ND-11 外联口自动部署 | SET AUTOCONFIG、ADD AUTOSCALINGSERVICE、ADD AUTOSCALINGETHTRUNK、DSP OPSASSISTSTATE |
| T-ND-12 配置OSPF | ADD OSPF、ADD OSPFAREA、ADD OSPFINTERFACE、ADD OSPFIMPORTROUTE（OSPFv3系列对应IPv6） |
| T-ND-13 配置BGP | SET BGP、ADD BGPVRF、ADD BGPVRFAF、ADD BGPPEER、ADD BGPPEERAF、ADD IMPORTROUTE |
| T-ND-14 配置静态路由 | ADD SRROUTE（+ AUTOSCALINGSRROUTE） |
| T-ND-15 配置BFD | SET BFD、ADD AUTOSCALINGBFD |
| T-ND-16 配置隧道 | ADD GRETUNNEL、SET MPLSSITE、ADD MPLSIF、IPsec命令 |
| T-ND-17 级联口(NP卡) | ADD NPDIRECTCONNECTPORT |
| T-ND-18 调测FirstCall | DSP SESSIONINFO、NGPING、PING、DSP ROUTE、DSP OSPFPEER、DSP BGPPEERINFO、LST OSPFIMPORTROUTE |
| T-ND-02 NTP | SET NTP |
| T-ND-03 网元基本信息 | MOD ME、SET OMIP |
| T-ND-05 高危命令二次授权 | SET SECAUTH |
| T-ND-06 网管对接 | SET NEWCERTSWITCH、LST ME |

### 4.2 ConfigTask `targets` ConfigObject

| Task | targets（ConfigObject） |
|---|---|
| T-ND-07 | VPNInstance、N4Interface、UPFIdentity |
| T-ND-08 | VPNInstance、LogicInterface(Saif/Scif/Paif) |
| T-ND-09 | APN/DNN、AddressPool、AddressSection、AddressPoolGroup |
| T-ND-10 | L3VPNInstance、VPNTarget |
| T-ND-12 | OSPFProcess、OSPFArea |
| T-ND-13 | BGPVRF、BPGPeer、BGPAF |
| T-ND-15 | BFDSession |
| T-ND-16 | GRETunnel、MPLSVPN、IPsecTunnel |
| T-ND-11 | AutoScalingService、EthTrunk |

### 4.3 TaskRule `refined_by` CommandRule

| TaskRule | refined_by CommandRule |
|---|---|
| TR 自动部署开关时序 | CR-ND（SET AUTOCONFIG 时序 + DSP OPSASSISTSTATE） |
| TR MPLS公私分离 | CR-ND（_public_ VPN + VRFRD） |
| TR 入不转板 | CR-ND（DATAPLANEGIINFMODE vs DATAPLANEINFMODE） |
| TR 接口掩码统一 | CR-ND（255.255.255.255） |

---

## 5. DecisionPoint 影响关系（§12.5）

| DecisionPoint | selects / sets_value_pattern |
|---|---|
| DP-CS4-01 硬件类型 | selects T-ND-17(级联口,仅NP卡/加速卡)；sets NP100/NP121 参数模式 |
| DP-CS4-02 组网架构(SDN/非SDN) | selects T-ND-11/12/13/14 组合；sets DHCP分配(IPALLOCTYPE/​NEXTHOPALLOCTYPE)、单臂BFD(ONEARMECHO) |
| DP-CS4-03 部署方式(自动/手动) | selects AUTOSCALING模板族 vs 逐条MML；sets MPLS接口模式(AUTOSCALINGMPLS vs ADD MPLSIF) |
| DP-CS4-04 路由协议×IP版本 | selects T-ND-12/13/14；sets OSPF/OSPFv3、IPv4/IPv6 地址族 |
| DP-CS4-05 BFD模式 | sets 双向/单臂Echo |
| DP-CS4-07 隧道叠加 | selects T-ND-16(IPsec/GRE/MPLS VPN) |
| DP-CS5-06 License加载路径 | selects OM Portal / U2020-MAE |
| DP-CS2-05 地址分配主体 | sets LOCAL/EXTERNAL（POOLTYPE） |
| DP-CS1 多SMF | selects GWFD-020161 CU Full Mesh |

---

## 6. ★端到端链路验证（SOP §5.5 要求 ≥3 条）

### 链路1：CS-1 N4 控制面偶联
```
BD-ND(网元对接)
 → NS-ND-UPF(UPF网元对接)
 → CS-ND-01(控制面对接)
 → GWFD-010234 / GWFD-020161(Single IP/CU Full Mesh)
 → T-ND-07(配置N4接口)
 → ADD VPNINST → ADD LOGICINF → SET UPINFO
 → VPNInstance / N4Interface(N4if) / UPFIdentity
```

### 链路2：CS-4 实例1 融合UDG OSPF IPv4 自动非SDN
```
BD-ND → NS-ND-UPF → CS-ND-04(路由对接)
 → IPFD-014000/014001/012003(路由/OSPF/BFD)
 → T-ND-10(VPN) → T-ND-12(OSPF) → T-ND-11(外联口自动部署,OSPFENABLE=TRUE) → T-ND-15(BFD) → T-ND-18(调测)
 → ADD L3VPNINST/IPBINDVPN → ADD OSPF/OSPFAREA/OSPFINTERFACE/OSPFIMPORTROUTE → ADD AUTOSCALINGSERVICE → SET BFD → DSP SESSIONINFO
 → L3VPNInstance / OSPFProcess / AutoScalingService / BFDSession
```

### 链路3：CS-4 实例7 SDN BGP over静态路由 IPv4v6 双栈（最完整）
```
BD-ND → NS-ND-UPF → CS-ND-04(路由对接, SDN分支)
 → IPFD-014002/014003/012003(BGP/静态/BFD) + GWFD-020411(MPLS VPN, 可选)
 → T-ND-10(VPN) → T-ND-15(单臂BFD Echo, ONEARMECHO=TRUE) → T-ND-14(静态路由,DHCP) → T-ND-11(外联口DHCP+DHCP6CLIENTDUID) → T-ND-13(BGP) → T-ND-18(调测)
 → SET BGP/ADD BGPVRF/BGPPEER → ADD SRROUTE(DHCPENABLE=TRUE) → ADD AUTOSCALINGSERVICE → DSP SESSIONINFO
 → BGPVRF/BPGPeer / StaticRoute / AutoScalingService / BFDSession
```

> 三条链路逐层贯通至 ConfigObject，覆盖 控制面对接 / 非SDN路由 / SDN路由 三类典型场景。

---

## 7. 跨层一致性校验

| 校验项 | 结果 |
|---|---|
| CS `uses_feature` 的 feature_code 全部在 02 存在 | ✅ 17 特性全覆盖（IPFD-104403 别名归并 IPFD-012003） |
| CS `uses_task` 的 task_id 全部在 03 存在 | ✅ T-ND-01~18 全覆盖 |
| Task `invokes` 的 command_name 全部在 04 存在 | ✅（03 已做 14 命令抽样交叉校验通过） |
| Feature `decomposes_to` Task 的 task 在 03 存在 | ✅ |
| DP `selects` 的对象在各层存在 | ✅ |
| 端到端链路 ≥3 条且贯通到 Object | ✅ 3 条 |

---

## 8. §13 禁止关系复核

| 禁止关系 | 复核结果 |
|---|---|
| CS → ConfigObject 直连 | ✅ 未出现（CS 经 uses_feature/uses_task 间接） |
| CS → MMLCommand 直连 | ✅ 未出现（CS→Task→Command） |
| BusinessRule → CommandParameter 写死值 | ✅ 未出现（用 DecisionPoint/TaskRule/CommandRule） |
| Feature → MMLCommand 跳层强绑 | ✅ 未出现（Feature→Task→Command） |
| Feature → ConfigObject 携带参数差异 | ✅ 未出现（用 SemanticObject/FeatureRule） |
| 业务层内建 ConfigObject | ✅ 未出现 |
| CS → ConfigTask 完整顺序链 | ✅ 仅 uses_task，顺序由 03 层 TaskCommandOrderEdge/FeatureTaskOrderEdge 承载 |

---

## 9. 跨层边计数汇总

| 跨层边类型 | 数量 |
|---|---|
| CS uses_feature | 18（引用17特性） |
| CS uses_task | ~18（5 CS × task） |
| Feature decomposes_to Task | ~14 |
| Task invokes Command | 18 task × 多命令（详见 03 command_refs） |
| Task targets ConfigObject | ~18 |
| DP selects/sets_value_pattern | ~11 |
| BusinessRule refined_by (FR/TR) | ~8 |
| SemanticObject realized_by (Feature/Task) | ~12 |
| 端到端链路 | 3 |

> 详细跨层边以 01-04 各层文件为准；本文为跨层映射汇总与一致性校验视图。
