# APN 业务域三层图谱 · 全量重建设计 (spec)

> 状态: 设计稿,待用户评审 → 转 writing-plans
> 日期: 2026-06-29
> 作者: 审查发现 APN 图谱存在系统性"业务层编造 + 命令/特性/任务层信息丢失"后,与用户对齐的重建方案

---

## 1. 背景:为什么要重建

审查(对照原始产品文档 `output/`)发现两类严重问题:

### 1.1 业务层 9 个 ConfigurationSolution 编造
- 原 9 个 CS(智慧农业传感器上报 / 工厂工控访问内网 / 家庭CPE宽带 / VoLTE / 企业AAA / DHCP迁移 / L2TP VPN / 区域化运营 / 企业双栈)**全部不在产品文档**。
- 全 `output/` 精确搜 `智慧农业|工控|传感器上报|家庭CPE|工厂工控` = 0 命中(仅 1 次泛词)。
- 来源链(图谱自述):`CS ──supported_by──► EV-TK-01(topic-knowledge/Batch-14,自撰)+ EV-CA-02(cross-topic-analysis,自撰)+ EV-BS-01(APN意图澄清知识库,SKILL自撰)`。**无一条指向产品文档** —— 是"追溯幻觉"。
- 底层技术决策(UDM静态/NON_TRANS/IPSec)有产品依据,但**场景命名与业务需求叙述是脑补**。

### 1.2 命令/特性/任务层信息丢失(致命,直接破坏"生成配置脚本"目标)
- **命令名错误**:MPLS 3 条命令 `ADD VPNINSTANCE/BGPVPNV4ROUTETARGET/BGPVPNV4PEER` 在产品文档中根本不存在(真实:`ADD L3VPNINST/VPNINSTAF/VPNTARGET/BGPPEER/BGPPEERAF`,且 MML 脚本在 `网络部署/初始配置/调测` 分支,特性指南分支无)。
- **参数深度丢失**:全图谱仅 9 命令有 `required_mode`;`SET IPALLOCRULE` 丢了**整个 IPv6 规则集**(IPV6FIRSTRULESW 等 7 参数)+ 规则字符串语法 `APN-X&LOCATION-X&SMF-X`;默认值/枚举大量缺失。
- **激活场景坍缩**:IPSec 8 激活场景(主备/多Sequence/GRE-over/OSPF-over/指定接口/国密/普通v4/v6)→ 合并为 1;Radius 4 组网 → 1。
- **配置脚本本体丢失**:Task 仅存命令名清单,零参数值/零脚本片段。
- **配置命令丢失**:Radius 信令控制类(VSA/ATTR/SPECIFICAPNVAL)全丢。
- **先天缺口**:UPF选择(1文档)/DHCP/DHCPv6/控制面地址分配(各2文档,无激活)/MPLS特性指南(9篇纯概念)→ 图谱内容必然推导,却多标 status=active。

### 1.3 根因
图谱是"人写中间态 md(feature-knowledge)→ 人写图谱"两级手工压缩,**图谱层未回溯产品文档核对**,只跑 schema 合规(查字段+引用完整性)。故 Stage 5 自报"P1+P2 合规率 100%"是**合规幻觉** —— 合规≠内容准确。

---

## 2. 目标
全量重建 APN 三层图谱,**全部从原始产品文档溯源**,达到"能准确生成配置脚本"的信息密度;业务层去编造化。

---

## 3. 约束(已与用户确认)
| 约束 | 取定 |
|---|---|
| Schema | `业务图谱体系/三层图谱Schema-最终版-v0.1.md`(不变) |
| 基础结构 | 必含 `APN配置树.md`(人工,业务骨架) |
| 抽取机制 | **纯 Agent 逐层重建**(读源文档重写,不建代码流水线) |
| 业务层 | **1 个大方案(CS-APN-01 APN开通)+ 决策点**,对标计费"从产品文档总结机制",删编造场景 |
| 并发 | 最多 2 个并行 Agent(用户既定规则) |
| Git | 直提 master,不开分支 |

---

## 4. 权威源(产品文档)
| 源 | 路径 | 喂哪层 |
|---|---|---|
| APN配置树(人工) | `业务图谱体系/APN业务域/APN配置树.md` | 业务层骨架 |
| UDG 特性指南 | `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/` | 特性+任务 |
| UNC 特性文档 | `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/` | 特性+任务 |
| UDG MML命令手册 | `output/UDG_Product_Documentation_CH_20.15.2/OM参考/命令/UDG MML命令/`(每命令1md) | 命令(参数金标准) |
| UNC MML命令手册 | `output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/` | 命令 |
| UDG 初始配置调测 | `output/UDG.../网络部署/初始配置/UDG初始配置与调测/` | 补 MPLS 等缺失命令 |

> 现有 `feature-knowledge/`(37 特性 md)作为**中间态参考**,非权威 —— 一切以产品文档原文为准核对。

---

## 5. 业务层设计(核心变更:9 CS → 1 CS)

### 5.1 结构
```
BD-APN-01 接入与会话管理(保留)
└─ NS-APN-01 APN开通场景(保留)
   └─ CS-APN-01 APN开通方案(单一,替代原 9 个编造 CS)
      ├─ core_mechanism_combo = 配置树 4 维度: 地址分配 × 鉴权 × 接入隧道 × 地址类型
      ├─ has_decision → DP*(步骤决策)
      ├─ constrained_by → BR*
      └─ uses_semantic_object → SO*
```
- **删除**:智慧农业/工控/家庭CPE/VoLTE/区域化运营/企业双栈 等 9 个编造 CS 及其业务需求叙述。
- CS-APN-01 = 配置树的 `APN开通` root 节点本身,是"一套 APN 开通的完整方案模板"。

### 5.2 DecisionPoint(挂在 NS/CS 下,产品文档+配置树背书)
配置树步骤维度的 DP(新增/明确):
| DP | 选项(配置树 OR 分支) |
|---|---|
| DP-地址分配方式 | 本地地址池(UPF/SMF) / UDM签约静态 / RADIUS下发 / DHCP代理 / LNS(L2TP) |
| DP-地址分配粒度 | 基于APN/DNN / 基于SMF / 基于位置区(仅"本地地址池"时) |
| DP-鉴权方式 | TRANS_NON_AUTH / TRANS_AUTH / NON_TRANS / LOC_AUTH |
| DP-接入隧道类型 | 直连(Native) / GRE / IPSec / L2TP |
| DP-地址类型 | IPv4 / IPv6 / IPv4v6双栈 |

特性文档背书的 DP(原图谱 12 个 DP 中产品文档有据的,保留并复核):
- DP-UPF选择 / DP-别名APN映射 / DP-用户接入权限判定 / DP-多PDN并发 / DP-DN二次鉴权 / DP-对等网元DNS聚合 / DP-带宽流控方式

> 复核标准:每个 DP 的 option_set 与 impact_summary 必须能在特性文档中找到依据,否则降级或删除。

### 5.3 BusinessRule(保留并复核,产品文档背书)
- 互斥:L2TP↔基于位置;GRE↔IPSec 源地址;L2TP↔地址自动检测
- License 触发:双栈(LKV3G5VDSA01)/基于位置(LKV3G5LBAA01)/L2TP(LKV3G5L2TP01,C-U不对称)
- 强依赖链:Radius级联(011306→011305→108007);IPv6承载链(020401→020403→020406)
- 其他:并发上限(EPC≤11/5GC≤15)、AMF本地优先、卡类型依赖鉴权、SMF-UPF同厂商

### 5.4 SemanticObject(保留并复核)
地址分配/鉴权AAA/隧道/会话上下文/签约/配额生命周期/别名APN映射/UPF NF属性/区域DNS/ARD记录/APN QoS属性 等。

---

## 6. 命令层重建(从 MML 命令手册,P0 止血)

对每个 APN 相关命令,读 `OM参考/命令/<NF> MML命令/` 下对应 md(命名 `{动作}（COMMAND）_{docid}.md`),抽取:
- **CommandParameter 全量**:参数标识 / 参数名称 / required_mode(含"条件必选"及前提条件,如 `FIRSTRULE` 在 `FIRSTRULESW=ENABLE` 时必选)/ 数据类型 / 取值范围(枚举值 + 位域格式如 `APN-X&LOCATION-X&SMF-X`)/ 默认值 / 配置原则
- **CommandRule**(从"注意事项"编码):时序(REFRESHSRV last)、前置(基于SMF需先 SET IPALLOCBYSMFSW)、互斥、上限(最大记录数)
- **使用实例脚本**:保留原文 MML

### 6.1 必修项
| 问题 | 修复 |
|---|---|
| MPLS 命令名错误 | 回溯 `网络部署/初始配置/UDG初始配置与调测/组网路由配置/配置BGP_MPLS VPN_*.md`,取真实命令 `ADD L3VPNINST`/`ADD VPNINSTAF`/`ADD VPNTARGET`/`ADD BGPPEER`/`ADD BGPPEERAF` |
| Radius 配置命令丢失 | 补 `SET RDSACCTREQVSA`/`SET RDSACCTREQATTR`/`SET RDSAUTHREQVSA`/`ADD SPECIFICAPNVAL`/`MOD RDSSVRGRP` 等 |
| IPv6 规则集丢失 | `SET IPALLOCRULE` 补 IPV6FIRSTRULESW 等 7 参数 |
| 参数深度 | 所有关键命令补全 required_mode/枚举/默认 |

### 6.2 命令清单来源
37 特性的特性指南命令列表 + 各激活文档脚本中出现命令(去重)→ 逐一在 MML 命令手册定位参数金标准。

---

## 7. 特性层重建(从特性指南)
每特性读 特性指南(概述/激活/原理/参考信息),抽取:
- Feature:`variant_dimensions`(从激活场景/参数枚举来,真实不编造)/ `applicable_nf_map` / `depends_on` / `requires_license` / `first_release` / `feature_group`
- SubFeature:仅在确有稳定细分(如别名APN双视角/接入控制双特性)时建
- FeatureRule:特性级约束

---

## 8. 任务层重建(从特性指南激活文档)
- **每个激活场景 = 一个 ConfigTask**(或 Task 变体),不合并:
  - IPSec 8 激活场景 → 8 Task(普通v4/v6/主备/多Sequence/GRE-over/OSPF-over/指定接口/国密)
  - Radius 4 组网 → 4 Task(单平面+静态路由+BFD / 双平面+OSPF+BFD / 带内GRE VPN / 带外GRE VPN)
- **TaskCommandOrderEdge**:命令时序 + `propagated_context`(POOLGROUPNAME/RULENAME 等传播参数)+ `value_pattern_summary`
- **保留每场景完整 MML 脚本**:作为 Task 的证据附着(或 command_refs 带条件取值)
- 产品文档无激活脚本的特性(UPF选择/DHCP/MPLS特性指南分支):Task 标 status=draft,注明文档缺口,不伪装完整

---

## 9. 证据层重建
- 全部 `source_evidence_ids` 重指产品文档原文:
  - `EV-FK-*` → 特性指南真实路径(核对 apn-feature-doc-list.md 已有路径)
  - 新增 `EV-CMD-*` → MML 命令手册路径(命令层金标准)
- **删除伪追溯权威**:`EV-TK-01`(Batch-14 自撰)/`EV-CA-02`(cross-topic 自撰)不再作为 CS 权威来源;`EV-BS-01`(意图澄清知识库)降级 status=reference(仅业务引导参考,不作事实源)

---

## 10. 产物格式
- 保持 `three-layer-graph/` 7 文件 md 结构(00-overview ~ 06-evidence-index,platform-next 读取此格式)
- `audit/` 重建审查记录
- 计数口径与各层一致(修复原 173 编号槽 vs 140 等计数矛盾)

---

## 11. 分期(Agent 逐层,bottom-up,让上层引用已验证下层)
1. **命令层**(P0 止血:错命令名 + 参数深度)—— 读 MML 命令手册
2. **特性层** —— 读特性指南
3. **任务层** —— 读特性指南激活文档
4. **业务层** —— 1 CS + DP(配置树 + 特性机制)
5. **跨层映射 + 证据 + 审计**

每期流程:Agent 读源文档 → 产出该层 → 对照产品文档核对 → 提交。最多 2 并行 Agent。

---

## 12. 非目标(本次不做)
- 不建代码抽取流水线(用户选纯 Agent)
- 不改 Schema v0.1
- 不改 platform-next 接入方式(保持 md 格式)
- 不动计费/带宽/访问限制其他场景
- 不保留 9 个编造业务场景(删除,非降级)

---

## 13. 验收标准
- 业务层:CS 仅 1 个,9 编造场景清除;DP/BR/SO 全部产品文档可追溯
- 命令层:MPLS 命令名正确;关键命令参数全量(含 IPv6 规则集、条件必选);Radius VSA 命令补齐
- 任务层:IPSec/Radius 场景不合并;每场景保留脚本;无激活文档的 Task 标 draft
- 证据:source_evidence_ids 指向产品文档;EV-TK-01/EV-CA-02 不背书 CS
- 抽样验证:任选 GWFD-010105,据图谱能复原产品文档场景一的可执行脚本
