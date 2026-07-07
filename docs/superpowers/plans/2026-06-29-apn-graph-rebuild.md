# APN 业务域三层图谱 · 全量重建实施计划

> **For agentic workers:** 本计划是 Agent 驱动的内容抽取(读产品文档→重写图谱),非传统代码 TDD。步骤用 `- [ ]` 跟踪。每阶段产出后对照产品文档核对再提交。配套 spec: `docs/superpowers/specs/2026-06-29-apn-graph-rebuild-design.md`。

**Goal:** 全量重建 APN 三层图谱,从原始产品文档(特性指南 + MML 命令手册 + 配置树)重新溯源,修掉业务层编造与命令/特性/任务层信息丢失,达到"能准确生成配置脚本"的密度。

**Architecture:** bottom-up 逐层重建(命令→特性→任务→业务→跨层),每层由 Agent 读源文档重写、对照产品文档核对;业务层由 9 编造 CS 收敛为 1 CS + 决策点。最多 2 并行 Agent。

**Tech Stack:** Agent(LLM)抽取 + Markdown 图谱产物(`业务图谱体系/APN业务域/three-layer-graph/*.md`)。源:`output/UDG_*`、`output/UNC *`、`APN配置树.md`。

---

## 文件结构(将被重写)

| 文件 | 责任 | 本计划动作 |
|---|---|---|
| `three-layer-graph/04-command-graph.md` | 命令层:MMLCommand/CommandParameter/ConfigObject/CommandRule | **重写**(Phase 1) |
| `three-layer-graph/02-feature-graph.md` | 特性层:Feature/SubFeature/License/FeatureRule/FTOE | **重写**(Phase 2) |
| `three-layer-graph/03-task-layer.md` | 任务层:ConfigTask/TaskRule/TCOE | **重写**(Phase 3) |
| `three-layer-graph/01-business-graph.md` | 业务层:BD/NS/CS/DP/BR/SO | **重写**(Phase 4:9 CS→1 CS) |
| `three-layer-graph/05-cross-layer-mapping.md` | 跨层映射 | **重写**(Phase 5) |
| `three-layer-graph/06-evidence-index.md` | 证据索引 | **重写**(Phase 5:重指产品文档) |
| `three-layer-graph/00-overview.md` | 总览 | **重写**(Phase 5:计数/导航对齐) |
| `three-layer-graph/audit/` | 审查记录 | 新建重建审查(Phase 5) |

特性簇划分(沿用 apn-feature-doc-list.md 分类,便于 Agent 分批):
- **簇A APN基础**(5):GWFD-010101/WSFD-010501/WSFD-010503/WSFD-010400/WSFD-106203
- **簇B 地址分配-本地/签约/位置**(8):GWFD-010105/010104/020421/010108/010107、WSFD-010502/010504/107021
- **簇C 地址分配-L2TP/双栈/IPv6/DHCP**(10):GWFD-020412/020403/020401/020406、WSFD-104410/104002/104001/104004/104413/104005
- **簇D 鉴权计费**(5):WSFD-011305/011306/010301/108007/011307
- **簇E 接入方式-隧道**(5):IPFD-015002/015004/016000、GWFD-020411/WSFD-104411(MPLS)
- **簇F 网元选择+接入控制**(4):WSFD-107010/010202、WSFD-106003/GWFD-010151

---

## Phase 1:命令层重建(P0 止血)

> 每个特性簇一个 Agent 任务。Agent 读:该簇各特性的特性指南(命令清单)+ 对应 MML 命令手册 md(参数金标准)。产出 04-command-graph.md 对应小节。

### 抽取标准(所有命令层任务共用)
对每条命令,从 `OM参考/命令/<NF> MML命令/.../<动作>（COMMAND）_<docid>.md` 抽:
- MMLCommand:command_id / command_name / verb / object_keyword / command_summary / status / source_evidence_ids(→ EV-CMD-*)
- CommandParameter **全量**:parameter_id / command_ref / parameter_name / data_type / **required_mode**(required/optional/conditional_required + 条件,如"FIRSTRULESW=ENABLE 时必选")/ default_value / enum_values(含位域格式 `APN-X&LOCATION-X&SMF-X`)/ description
- CommandRule(从"注意事项"):rule_type(precondition_rule/runtime_check_rule/parameter_dependency 等)/ rule_logic / severity
- 使用实例:保留原文 MML 脚本片段
- ConfigObject:object_id / object_name / identifier_parameters / object_kind / 关系边(contains/refers_to/depends_on/conflicts_with/activates)

### Task 1.1:簇A APN基础 命令层
**Files:** 读 簇A 特性指南 + MML手册;写 `04-command-graph.md` §APN基础小节
- [ ] Agent 抽取簇A 5 特性涉及命令的完整 CommandParameter/CommandRule/ConfigObject
- [ ] 核对:每条命令在 MML 手册定位到原文,参数数 ≥ 原文表行数
- [ ] 提交小节草稿

### Task 1.2:簇B 地址分配-本地/签约/位置 命令层 ★(信息丢失重灾区)
**Files:** GWFD-010105 等;写 04 §地址分配小节
- [ ] 抽 GWFD-010105 全部命令(ADD POOL/SECTION/POOLGROUP/POOLBINDGROUP/POOLGRPMAP/CONFLICTIP、SET APNADDRESSATTR/IPALLOCRULE/APNIPALLOCRULE/ADDRESSATTR/IPALLOCBYSMFGLBSW/IPALLOCBYLOCSW、ADD CPNODEID/APN/L3VPNINST/VPNINSTAF/VPNINST、OSPF 族、DSP/LST 族)
- [ ] **重点核对**:`SET IPALLOCRULE` 必含 IPv6 规则集(IPV6FIRSTRULESW 等 7 参数)+ 规则字符串格式
- [ ] 核对 ADD POOL/SECTION 参数全量
- [ ] 提交

### Task 1.3:簇C 地址分配-L2TP/双栈/IPv6/DHCP 命令层
- [ ] 抽 L2TP(SET APNL2TPATTR 10+参数 / SET APNL2TPCTRL / L2TPN4KEY/L2TPKEY / L2TPGROUP / GLOBALL2TP 等)、双栈、IPv6承载/PD、DHCP 命令
- [ ] 核对 APNL2TPATTR 参数数 ≥ 产品文档(原图谱只列 3 个)
- [ ] DHCP 命令标注:产品文档仅参考信息,激活参数不全 → 相关 Task 后续标 draft
- [ ] 提交

### Task 1.4:簇D 鉴权计费 命令层 ★(Radius VSA 丢失)
- [ ] 抽 WSFD-011306 Radius 全命令,**补回** SET RDSACCTREQVSA/SET RDSACCTREQATTR/SET RDSAUTHREQVSA/ADD SPECIFICAPNVAL/MOD RDSSVRGRP
- [ ] 抽 011305(AUTHMODE 4 值)/010301(AKA)/108007(二次鉴权)/011307(抄送)
- [ ] 核对 Radius 命令族完整
- [ ] 提交

### Task 1.5:簇E 接入方式-隧道 命令层 ★(IPSec 场景 + MPLS 错命令)
- [ ] IPSec:抽 8 激活场景涉及命令族(IKE Peer/Proposal/Policy/ACL/证书/国密),标注每场景参数差异(WORKMODE/SEQUENCENUMBER/SRCINTERFACE/国密算法)
- [ ] GRE:GRETUNNEL 族 + 两层嵌套约束
- [ ] **MPLS 修复**:回溯 `output/UDG.../网络部署/初始配置/UDG初始配置与调测/组网路由配置/配置BGP_MPLS VPN_*.md`,取真实命令 `ADD L3VPNINST`/`ADD VPNINSTAF`/`ADD VPNTARGET`/`ADD BGPPEER`/`ADD BGPPEERAF`;**删除**错误的 ADD VPNINSTANCE/BGPVPNV4*
- [ ] 提交

### Task 1.6:簇F 网元选择+接入控制 命令层
- [ ] 抽 UPF选择(WSFD-107010,标注文档缺口)/对等网元选择(AREDNS 族)/接入控制(ARD/NGMMSUBDATA/APNQOSATTR 等)
- [ ] 提交

### Task 1.7:命令层合并 + 去重 + operates_on/governed_by 边
- [ ] 合并 6 簇产物,跨簇命令去重(如 ADD APN/OSPF 多簇共用)
- [ ] 补 MMLCommand→ConfigObject(operates_on)、CommandRule→(governs)边
- [ ] 计数核对:命令数 vs 编号槽一致
- [ ] Commit: `feat(apn): 命令层全量重建(产品文档溯源,修MPLS错命令/补IPv6规则集/Radius VSA)`

---

## Phase 2:特性层重建

> Agent 读特性指南(概述/激活/原理/参考),重写 02-feature-graph.md。

### Task 2.1~2.6:按簇抽取 Feature
每簇:variant_dimensions(从激活场景/参数枚举,真实)/ applicable_nf_map / depends_on / requires_license / first_release / feature_group / FeatureRule。
- [ ] 簇A~F 各抽 Feature + License + FeatureRule
- [ ] 核对 depends_on 与产品文档"与其他特性交互"一致(修原 8 对声明矛盾)
- [ ] requires_license 与产品文档 License 章节一致(修 GWFD-010105 无 License 等)

### Task 2.7:FeatureTaskOrderEdge
- [ ] 6 核心特性(010105/020412/020403/011306/015004/106003)的 FTOE
- [ ] Commit: `feat(apn): 特性层全量重建`

---

## Phase 3:任务层重建

> Agent 读特性指南**激活文档**,每激活场景一个 Task,不合并。

### Task 3.1:IPSec 8 场景拆 Task
- [ ] 普通 IPv4 IPsec / 普通 IPv6 / IPv4主备 / IPv6主备 / 多Sequence / GRE over IPsec / OSPF over IPsec / 指定接口 / 国密 → 各一 Task
- [ ] 每个 Task 保留完整 MML 脚本(command_refs 带条件取值 或 附脚本)

### Task 3.2:Radius 4 组网拆 Task
- [ ] 单平面+静态路由+BFD / 双平面+OSPF+BFD / 带内GRE VPN / 带外GRE VPN → 各一 Task

### Task 3.3:其余特性 Task
- [ ] 地址分配(4 子方式)/L2TP/双栈/IPv6/PD/DHCP/鉴权/接入控制 等,每激活场景一 Task
- [ ] 文档缺口特性(UPF选择/DHCP/MPLS特性指南分支):Task status=draft + 注明缺口

### Task 3.4:TaskCommandOrderEdge + TaskRule
- [ ] 命令时序(precedes/depends_on/must_be_last)+ propagated_context(POOLGROUPNAME 等)
- [ ] TaskRule
- [ ] Commit: `feat(apn): 任务层全量重建(激活场景不合并,保留脚本)`

---

## Phase 4:业务层重建(9 CS → 1 CS)

### Task 4.1:重写业务层骨架
- [ ] BD-APN-01 / NS-APN-01 保留
- [ ] **CS 收敛为 CS-APN-01 APN开通**(单一),core_mechanism_combo = 配置树 4 维度
- [ ] **删除** 智慧农业/工控/家庭CPE/VoLTE/区域化/企业双栈/企业AAA/DHCP迁移/L2TP-VPN 9 个编造 CS 及叙述

### Task 4.2:DecisionPoint(配置树步骤 + 复核有据 DP)
- [ ] 配置树步骤 DP:地址分配方式 / 地址分配粒度 / 鉴权方式 / 接入隧道类型 / 地址类型
- [ ] 复核原 12 DP:UPF选择/别名APN/接入权限/并发/二次鉴权/对等网元/带宽流控 —— 逐个核对产品文档依据,无据的删
- [ ] DP option_set 与 impact_summary 对齐特性文档

### Task 4.3:BusinessRule + SemanticObject
- [ ] BR(互斥/License/强依赖)逐条核对特性文档
- [ ] SO(地址池/鉴权AAA/隧道/会话上下文等)核对
- [ ] Commit: `feat(apn): 业务层重建(9编造CS→1CS+决策点,去伪追溯)`

---

## Phase 5:跨层映射 + 证据 + 审计 + 总览

### Task 5.1:跨层映射 05
- [ ] uses_feature / decomposes_to / invokes / targets / refined_by 边,全部指向已重建的真实对象
- [ ] 端到端链路(≥3 条)重写,基于真实机制

### Task 5.2:证据层 06
- [ ] source_evidence_ids 全部重指产品文档(EV-FK-* 核对路径 + 新增 EV-CMD-* 命令手册)
- [ ] **删除** EV-TK-01/EV-CA-02 对 CS 的权威背书;EV-BS-01 降 status=reference
- [ ] EV 编号统一数字格式

### Task 5.3:总览 00 + 审计
- [ ] 00-overview 计数/导航/合规清单对齐新结构
- [ ] 新建 audit/重建审查报告:逐项核对 spec §13 验收标准
- [ ] Commit: `feat(apn): 跨层映射+证据+总览重建,重建审查`

---

## 验收门(对应 spec §13)
- [ ] 业务层:CS 仅 1 个,9 编造场景清除;DP/BR/SO 产品文档可追溯
- [ ] 命令层:MPLS 命令名正确;关键命令参数全量(含 IPv6 规则集、条件必选);Radius VSA 补齐
- [ ] 任务层:IPSec/Radius 场景不合并;每场景保留脚本;无激活文档 Task 标 draft
- [ ] 证据:source_evidence_ids 指向产品文档;EV-TK-01/EV-CA-02 不背书 CS
- [ ] **抽样脚本复原**:据 GWFD-010105 图谱内容能复原产品文档"基于APN/DNN分配地址"场景一的可执行脚本(含 SET IPALLOCRULE 规则字符串)

---

## 执行说明
- 顺序严格 bottom-up(Phase 1→5),上层引用已验证下层
- 每 Task:Agent 抽取 → 对照产品文档核对(必填:`核对:` 行写明比对的产品文档路径)→ 提交
- 簇级 Task 可 2 并行(簇间独立);Phase 间串行
- 频繁提交(每 Task/Phase 一个 commit,直提 master)
