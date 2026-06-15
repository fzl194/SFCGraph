# 计费场景三层图谱 · 第3层：任务原子层

> **文件定位**：`three-layer-graph/03-task-layer.md`
> **Schema参考**：`三层图谱Schema-最终版-v0.1.md` §10 任务原子层
> **作用**：实例化27个ConfigTask + TaskRule + TaskCommandOrderEdge
> **数据来源**：`feature-knowledge/cross-feature-analysis.md`（附录D端到端配置流程）、`unified-knowledge/计费场景统一知识库.md`（K001-K261）

---

## 0. 任务层总览

### 0.1 ConfigTask 分类

| 类型 | 数量 | 编号范围 | 说明 |
|------|------|---------|------|
| generic（通用，跨特性复用） | 8 | T-001~T-008 | 计费三件套+基础识别+刷新 |
| feature_specific（特性专属） | 19 | T-101~T-311 | License/SA/在线/融合/CG/CC专属 |
| **合计** | **27** | — | — |

> **Task编号段说明**：
> - `T-001~T-008`：通用Task（generic），跨特性复用的基础配置步骤
> - `T-101~T-104`：离线计费/内容计费专属（规划、SA特征库、协议绑定、兜底URR组）
> - `T-201~T-204`：在线计费专属（规划、URR、URRGROUP、PCC策略组）
> - `T-301~T-311`：融合计费/UNC控制面专属（三联前置CHGMODE/CHARGECTRL/CHFINIT、CHF选择TNF链、CC属性、CCT模板、Trigger、异常处理、缓存、CG接口、热计费）
> - **跨场景注意**：带宽控制场景使用 T-101~T-603 编号段，合并时需加场景前缀（如 T-BW-101）避免冲突

### 0.2 任务原子化原则

1. **每Task一个明确goal**：可复用的配置步骤独立成Task
2. **generic优先**：跨3+特性复用的步骤提升为generic
3. **feature_specific保留特性语义**：License开启、协议配置等不可泛化的步骤保留特性绑定
4. **命令顺序通过TaskCommandOrderEdge表达**：Task间顺序通过`05-cross-layer-mapping.md`的FeatureTaskOrderEdge表达

---

## 1. 通用Task（generic，8个）

### T-001 规划业务分类与识别条件

| 字段 | 值 |
|------|---|
| `task_id` | `T-001` |
| `task_name` | `规划业务分类与识别条件` |
| `scope_type` | `generic` |
| `goal` | 建立业务分类体系，为计费业务识别提供SA分类基础 |
| `input` | 业务清单、识别规则规划 |
| `output` | CATEGORYPROP/FILTER/L7FILTER实例集 |
| `command_refs` | `ADD CATEGORYPROP`, `ADD FILTER`, `ADD FILTERIPV6`, `ADD L7FILTER` |
| `feature_ref` | GWFD-110101（SA-Basic） |
| `source_evidence_ids` | EV-FK-SA-Basic, EV-CFA |
| `reused_by` | CS-CH-01~07（全部方案） |

### T-002 配置流过滤器与绑定

| 字段 | 值 |
|------|---|
| `task_id` | `T-002` |
| `task_name` | `配置流过滤器与绑定` |
| `scope_type` | `generic` |
| `goal` | 建立可复用的流匹配条件，承接计费规则匹配 |
| `input` | FILTER/L7FILTER实例 |
| `output` | FLOWFILTER + 绑定关系 |
| `command_refs` | `ADD FLOWFILTER`, `ADD FLTBINDFLOWF` |
| `feature_ref` | GWFD-110101, GWFD-020351 |
| `source_evidence_ids` | EV-FK-SA-Basic, EV-FK-PCC-UDG, EV-CFA |
| `reused_by` | CS-CH-01~07 |

### T-003 配置PCC规则

| 字段 | 值 |
|------|---|
| `task_id` | `T-003` |
| `task_name` | `配置PCC规则` |
| `scope_type` | `generic` |
| `goal` | 建立策略规则实例，POLICYTYPE=CHARGING（计费场景固定） |
| `input` | FLOWFILTER + PCCPOLICYGRP + 优先级规划 |
| `output` | RULE实例 |
| `command_refs` | `ADD RULE` |
| `feature_ref` | GWFD-020351, WSFD-109101 |
| `source_evidence_ids` | EV-FK-PCC-UDG, EV-FK-PCC-UNC, EV-CFA |
| `reused_by` | CS-CH-01~07 |

### T-004 配置用户模板与规则绑定

| 字段 | 值 |
|------|---|
| `task_id` | `T-004` |
| `task_name` | `配置用户模板与规则绑定` |
| `scope_type` | `generic` |
| `goal` | 将计费规则组织为用户模板，承载计费策略容器 |
| `input` | RULE实例集 |
| `output` | USERPROFILE + RULEBINDING |
| `command_refs` | `ADD USERPROFILE`, `ADD RULEBINDING` |
| `feature_ref` | GWFD-020351, WSFD-109002 |
| `source_evidence_ids` | EV-FK-PCC-UDG, EV-FK-Content-UNC, EV-CFA |
| `reused_by` | CS-CH-01~07 |

### T-005 配置用户模板组与APN绑定

| 字段 | 值 |
|------|---|
| `task_id` | `T-005` |
| `task_name` | `配置用户模板组与APN绑定` |
| `scope_type` | `generic` |
| `goal` | 完成APN/DNN级计费策略生效的标准绑定链（UNC侧） |
| `input` | USERPROFILE实例 |
| `output` | USRPROFGROUP + UPBINDUPG + APNUSRPROFG |
| `command_refs` | `ADD USRPROFGROUP`, `ADD UPBINDUPG`, `ADD APNUSRPROFG` |
| `feature_ref` | WSFD-109002 |
| `source_evidence_ids` | EV-FK-Content-UNC, EV-CFA |
| `reused_by` | CS-CH-01~07（UNC侧绑定链） |

### T-006 配置URR与URR组

| 字段 | 值 |
|------|---|
| `task_id` | `T-006` |
| `task_name` | `配置URR与URR组` |
| `scope_type` | `generic` |
| `goal` | 定义使用量上报规则（计量方式/费率组/阈值/上报模式），组织为URR组 |
| `input` | URR规划（URRID/RG/USAGERPTMODE/METERINGTYPE） |
| `output` | URR + URRGROUP实例 |
| `command_refs` | `ADD URR`, `ADD URRGROUP` |
| `feature_ref` | GWFD-020301, WSFD-109002 |
| `source_evidence_ids` | EV-FK-Content-UDG, EV-FK-Content-UNC, EV-CFA, EV-KB-001 |
| `reused_by` | CS-CH-01~07（计费三件套核心） |
| `note` | 计费场景核心Task，承载差异化计费能力 |

### T-007 配置PCC策略组

| 字段 | 值 |
|------|---|
| `task_id` | `T-007` |
| `task_name` | `配置PCC策略组` |
| `scope_type` | `generic` |
| `goal` | 将URRGROUP绑定到策略组，实现业务匹配到计费执行 |
| `input` | URRGROUP实例 |
| `output` | PCCPOLICYGRP实例 |
| `command_refs` | `ADD PCCPOLICYGRP` |
| `feature_ref` | GWFD-020301, WSFD-109002 |
| `source_evidence_ids` | EV-FK-Content-UDG, EV-FK-Content-UNC, EV-CFA |
| `reused_by` | CS-CH-01~07 |

### T-008 策略刷新生效

| 字段 | 值 |
|------|---|
| `task_id` | `T-008` |
| `task_name` | `策略刷新生效` |
| `scope_type` | `generic` |
| `goal` | UDG侧修改FILTER/FLOWFILTER后执行刷新，约60秒完全下发 |
| `input` | 所有配置完成 |
| `output` | 配置生效 |
| `command_refs` | `SET REFRESHSRV` |
| `feature_ref` | GWFD-020351, GWFD-020301 |
| `source_evidence_ids` | EV-FK-PCC-UDG, EV-FK-Content-UDG, EV-CFA |
| `reused_by` | CS-CH-01~07（UDG侧） |
| `must_be_last` | `true` |
| `note` | FR-01硬约束：必须最后执行，PROTBINDFLOWF需等待60秒 |

---

## 2. 特性专属Task（feature_specific，19个）

### 2.1 License与SA基础

#### T-101 配置License前置门控

| 字段 | 值 |
|------|---|
| `task_id` | `T-101` |
| `task_name` | `配置License前置门控` |
| `scope_type` | `feature_specific` |
| `goal` | 开启计费特性License（SA-Basic/内容计费/在线计费等） |
| `command_refs` | `SET LICENSESWITCH` |
| `feature_ref` | 全部14特性（按需） |
| `source_evidence_ids` | EV-FK-SA-Basic, EV-CFA |
| `note` | BR-CH-12 License前置门控 |

#### T-102 加载SA特征库

| 字段 | 值 |
|------|---|
| `task_id` | `T-102` |
| `task_name` | `加载SA特征库` |
| `scope_type` | `feature_specific` |
| `goal` | 加载SA特征库和解析库，为业务识别提供数据基础 |
| `command_refs` | `LOD SIGNATUREDB`, `LOD PARSERDB` |
| `feature_ref` | GWFD-110101 |
| `source_evidence_ids` | EV-FK-SA-Basic, EV-CFA |

#### T-103 配置协议绑定

| 字段 | 值 |
|------|---|
| `task_id` | `T-103` |
| `task_name` | `配置协议绑定` |
| `scope_type` | `feature_specific` |
| `goal` | PROTBINDFLOWF将协议绑定到FlowFilter，修改后需等待60秒 |
| `command_refs` | `ADD PROTBINDFLOWF` |
| `feature_ref` | GWFD-110101 |
| `source_evidence_ids` | EV-FK-SA-Basic, EV-CFA |
| `note` | BR-CH-11协议匹配约束：必须与目标网站实际协议一致 |

#### T-104 配置URR组绑定与兜底

| 字段 | 值 |
|------|---|
| `task_id` | `T-104` |
| `task_name` | `配置URR组绑定与兜底` |
| `scope_type` | `feature_specific` |
| `goal` | SET URRGRPBINDING绑定默认URR组 + SET SPECTRAFURRGRP兜底特殊流量 |
| `command_refs` | `SET URRGRPBINDING`, `SET SPECTRAFURRGRP`, `ADD SPECURRGRPLIST` |
| `feature_ref` | GWFD-020301 |
| `source_evidence_ids` | EV-FK-Content-UDG, EV-CFA |
| `note` | CS-CH-07兜底方案核心Task |

### 2.2 在线计费专属（UDG）

#### T-201 配置DCC模板与OCS链路

| 字段 | 值 |
|------|---|
| `task_id` | `T-201` |
| `task_name` | `配置DCC模板与OCS链路` |
| `scope_type` | `feature_specific` |
| `goal` | 配置Diameter链路组、DCC模板、OCS选择 |
| `command_refs` | `ADD DIAMCONNGRP`, `ADD DCCTEMPLATE`, `SET OCSDOWNACTION` |
| `feature_ref` | GWFD-020300 |
| `source_evidence_ids` | EV-FK-Online, EV-CFA |

#### T-202 配置在线计费异常处理

| 字段 | 值 |
|------|---|
| `task_id` | `T-202` |
| `task_name` | `配置在线计费异常处理` |
| `scope_type` | `feature_specific` |
| `goal` | 配置Tx定时器、CCFH异常处理、异常返回码动作 |
| `command_refs` | `ADD CMDRCACT`, `ADD MSCCRCACT`, `SET FHBYPASS`, `SET TXTIMER` |
| `feature_ref` | GWFD-020300 |
| `source_evidence_ids` | EV-FK-Online, EV-CFA |
| `note` | FR-03超时阻塞公式：T3RESPONSE×N3REQUEST+4秒 |

#### T-203 配置Default Quota

| 字段 | 值 |
|------|---|
| `task_id` | `T-203` |
| `task_name` | `配置Default Quota` |
| `scope_type` | `feature_specific` |
| `goal` | 配置OCS不可达时的默认配额容灾 |
| `command_refs` | `SET UPDEFAULTQUOTA` |
| `feature_ref` | GWFD-020300 |
| `source_evidence_ids` | EV-FK-Online, EV-CFA |

#### T-204 配置配额耗尽动作

| 字段 | 值 |
|------|---|
| `task_id` | `T-204` |
| `task_name` | `配置配额耗尽动作` |
| `scope_type` | `feature_specific` |
| `goal` | 配置在线RG配额耗尽后动作（阻塞/重定向/转发） |
| `command_refs` | `ADD QUOTAEXHAUSTACT` |
| `feature_ref` | GWFD-020300, WSFD-011206 |
| `source_evidence_ids` | EV-FK-Online, EV-FK-Converged-UNC, EV-CFA |
| `note` | CS-CH-06配额降速核心Task，DP-CH-04决策点 |

### 2.3 融合计费专属（UNC）

#### T-301 配置计费接口模式

| 字段 | 值 |
|------|---|
| `task_id` | `T-301` |
| `task_name` | `配置计费接口模式` |
| `scope_type` | `feature_specific` |
| `goal` | SET CHGMODE全局 + ADD APNCHGMODE按APN + ADD ROAMCHGMODE按漫游 |
| `command_refs` | `SET CHGMODE`, `ADD APNCHGMODE`, `ADD ROAMCHGMODE` |
| `feature_ref` | WSFD-011201, WSFD-011206 |
| `source_evidence_ids` | EV-FK-Offline-UNC, EV-FK-Converged-UNC, EV-CFA |
| `note` | BR-CH-10三联前置约束之一：CHGMODE=NchfMode |

#### T-302 配置融合计费使能

| 字段 | 值 |
|------|---|
| `task_id` | `T-302` |
| `task_name` | `配置融合计费使能` |
| `scope_type` | `feature_specific` |
| `goal` | SET CHARGECTRL全局 / SET USRPROFCHARGE按UP / SET APNCHARGECTRL按DNN |
| `command_refs` | `SET CHARGECTRL`, `SET USRPROFCHARGE`, `SET APNCHARGECTRL` |
| `feature_ref` | WSFD-011206 |
| `source_evidence_ids` | EV-FK-Converged-UNC, EV-CFA |
| `note` | BR-CH-10三联前置约束之二：CHARGECTRL使能 |

#### T-303 配置CHF交互使能与选择

| 字段 | 值 |
|------|---|
| `task_id` | `T-303` |
| `task_name` | `配置CHF交互使能与选择` |
| `scope_type` | `feature_specific` |
| `goal` | SET CHFINIT + CHF选择链（7级优先级） |
| `command_refs` | `SET CHFINIT`, `ADD TNFINS`, `ADD TNFINSIP`, `ADD TNFGRP`, `ADD TNFBINDGRP`, `ADD SELECTCHFGBYCC`, `SET GLBDFTCHFGROUP` |
| `feature_ref` | WSFD-011206 |
| `source_evidence_ids` | EV-FK-Converged-UNC, EV-CFA |
| `note` | BR-CH-10三联前置约束之三：CHFINIT=SENDREQ |

#### T-304 配置CCT融合计费模板

| 字段 | 值 |
|------|---|
| `task_id` | `T-304` |
| `task_name` | `配置CCT融合计费模板` |
| `scope_type` | `feature_specific` |
| `goal` | ADD CCT定义QHT/VQT/TQT/VT/PDU阈值 + 绑定到CC/DNN/UP |
| `command_refs` | `ADD CCT`, `ADD SELECTCCTBYCC` |
| `feature_ref` | WSFD-011206 |
| `source_evidence_ids` | EV-FK-Converged-UNC, EV-CFA |

#### T-305 配置Trigger交互条件

| 字段 | 值 |
|------|---|
| `task_id` | `T-305` |
| `task_name` | `配置Trigger交互条件` |
| `scope_type` | `feature_specific` |
| `goal` | ADD PDUTRIGGER(Session级) + ADD RGTRIGGER(RG级) |
| `command_refs` | `ADD PDUTRIGGER`, `ADD RGTRIGGER` |
| `feature_ref` | WSFD-011206 |
| `source_evidence_ids` | EV-FK-Converged-UNC, EV-CFA |

#### T-306 配置N40 API版本

| 字段 | 值 |
|------|---|
| `task_id` | `T-306` |
| `task_name` | `配置N40 API版本` |
| `scope_type` | `feature_specific` |
| `goal` | SET N40APIVER版本号与CHF一致 |
| `command_refs` | `SET N40APIVER` |
| `feature_ref` | WSFD-011206 |
| `source_evidence_ids` | EV-FK-Converged-UNC, EV-CFA |

#### T-307 配置异常返回码处理

| 字段 | 值 |
|------|---|
| `task_id` | `T-307` |
| `task_name` | `配置异常返回码处理` |
| `scope_type` | `feature_specific` |
| `goal` | SET FAILHANDLING + ADD PDUSCACT + ADD RGRCACT + SET CNVRGDCHGPARA |
| `command_refs` | `SET FAILHANDLING`, `ADD PDUSCACT`, `ADD RGRCACT`, `SET CNVRGDCHGPARA` |
| `feature_ref` | WSFD-011206 |
| `source_evidence_ids` | EV-FK-Converged-UNC, EV-CFA |

#### T-308 配置计费消息缓存

| 字段 | 值 |
|------|---|
| `task_id` | `T-308` |
| `task_name` | `配置计费消息缓存` |
| `scope_type` | `feature_specific` |
| `goal` | 主备CHF均故障时SMF缓存计费消息 |
| `command_refs` | `SET N40MSGSTG`, `SET STGTRIGGER`, `SET CDRSTORAGECTRL`, `SET N4CHGMSGCONTROL` |
| `feature_ref` | WSFD-011206 |
| `source_evidence_ids` | EV-FK-Converged-UNC, EV-CFA |

#### T-309 配置CC计费属性

| 字段 | 值 |
|------|---|
| `task_id` | `T-309` |
| `task_name` | `配置CC计费属性` |
| `scope_type` | `feature_specific` |
| `goal` | ADD CHARGECHAR(CC实例) + SET GLBCHARGECHAR(全局) |
| `command_refs` | `ADD CHARGECHAR`, `SET GLBCHARGECHAR` |
| `feature_ref` | WSFD-011201, WSFD-011202 |
| `source_evidence_ids` | EV-FK-Offline-UNC, EV-FK-HotBilling, EV-CFA |

#### T-310 配置费率切换

| 字段 | 值 |
|------|---|
| `task_id` | `T-310` |
| `task_name` | `配置费率切换` |
| `scope_type` | `feature_specific` |
| `goal` | ADD FESTIVAL + ADD WEEKDAY + ADD TARIFFGROUP（节假日/工作日/时段费率切换） |
| `command_refs` | `ADD FESTIVAL`, `ADD WEEKDAY`, `ADD TARIFFGROUP` |
| `feature_ref` | WSFD-011206 |
| `source_evidence_ids` | EV-FK-Converged-UNC, EV-CFA |

#### T-311 配置CG接口（离线）

| 字段 | 值 |
|------|---|
| `task_id` | `T-311` |
| `task_name` | `配置CG接口（离线）` |
| `scope_type` | `feature_specific` |
| `goal` | ADD CG(CG实例+WAL) + SET CDRTRANSFER(负荷分担算法) + SET OFCTHRESHOLD(话单阈值) |
| `command_refs` | `ADD CG`, `SET CDRTRANSFER`, `SET OFCTHRESHOLD`, `SET CONTAINERTRIGGER` |
| `feature_ref` | WSFD-011201, GWFD-010171 |
| `source_evidence_ids` | EV-FK-Offline-UNC, EV-FK-Offline-UDG, EV-CFA |
| `note` | CS-CH-01离线计费CG侧核心Task |

---

## 3. TaskRule（任务级规则）

| `rule_id` | `rule_name` | `rule_type` | `applies_to` | `rule_logic` | `severity` |
|-----------|-------------|-------------|--------------|--------------|------------|
| `TR-CH-01` | 计费三件套必须完整链路 | `validation_rule` | T-006, T-007, T-003 | Rule → PCCPOLICYGRP → URRGROUP → URR 链路必须完整无断裂，任何一环缺失导致计费不生效 | critical |
| `TR-CH-02` | URR ID空间分段分配 | `naming_rule` | T-006 | 同一PDU会话内URR ID不能重复（不同业务需分段分配ID空间，如1-99/100+） | critical |
| `TR-CH-03` | REFRESHSRV必须最后执行 | `dependency_rule` | T-008 | SET REFRESHSRV必须在所有ADD/SET完成后执行；PROTBINDFLOWF需等待60秒 | critical |
| `TR-CH-04` | 融合计费三联前置约束 | `dependency_rule` | T-301, T-302, T-303 | 融合计费场景下CHGMODE=NchfMode + CHARGECTRL使能 + CHFINIT=SENDREQ 三项必须全部满足 | critical |
| `TR-CH-05` | CHF选择链完整性 | `dependency_rule` | T-303 | TNFINS → TNFINSIP → TNFGRP → TNFBINDGRP → SELECTCHFGBYCC → GLBDFTCHFGROUP 必须顺序完成 | warning |
| `TR-CH-06` | License前置门控 | `validation_rule` | T-101 | 计费特性配置前必须先SET LICENSESWITCH开启对应License；内容计费需UNC+UDG双License同时开启 | critical |

---

## 4. TaskCommandOrderEdge（Task内部命令顺序）

### 4.1 T-006 配置URR与URR组

| edge_id | task_ref | from_command | to_command | relation_type | requiredness | propagated_context | source_evidence_ids |
|---------|----------|--------------|------------|---------------|--------------|-------------------|---------------------|
| TE-006-1 | T-006 | `ADD URR` | `ADD URRGROUP` | `precedes` | required | URRID → URRGROUP.UPURRNAME1 | EV-FK-Content-UDG, EV-CFA |
| TE-006-2 | T-006 | `ADD URRGROUP` | `SET URRGRPBINDING` | `precedes` | required | URRGROUPNAME → URRGRPBINDING | EV-FK-Content-UDG, EV-CFA |
| TE-006-3 | T-006 | `SET URRGRPBINDING` | `SET SPECTRAFURRGRP` | `precedes` | optional | URRGROUPNAME | EV-FK-Content-UDG, EV-CFA |

### 4.2 T-007 配置PCC策略组

| edge_id | task_ref | from_command | to_command | relation_type | requiredness | propagated_context | source_evidence_ids |
|---------|----------|--------------|------------|---------------|--------------|-------------------|---------------------|
| TE-007-1 | T-007 | `ADD URRGROUP` | `ADD PCCPOLICYGRP` | `precedes` | required | URRGROUPNAME → PCCPOLICYGRP | EV-FK-Content-UDG, EV-CFA |
| TE-007-2 | T-007 | `ADD PCCPOLICYGRP` | `ADD RULE` | `precedes` | required | PCCPOLICYGRPNAME → RULE.POLICYNAME | EV-FK-Content-UDG, EV-CFA |

### 4.3 T-003 配置PCC规则（内部链）

| edge_id | task_ref | from_command | to_command | relation_type | requiredness | propagated_context | source_evidence_ids |
|---------|----------|--------------|------------|---------------|--------------|-------------------|---------------------|
| TE-003-1 | T-003 | `ADD FLOWFILTER` | `ADD RULE` | `precedes` | required | FLOWFILTERNAME → RULE | EV-FK-Content-UDG, EV-CFA |
| TE-003-2 | T-003 | `ADD PCCPOLICYGRP` | `ADD RULE` | `precedes` | required | PCCPOLICYGRPNAME → RULE.POLICYNAME | EV-FK-Content-UDG, EV-CFA |

### 4.4 T-311 配置CG接口（离线CG侧链）

| edge_id | task_ref | from_command | to_command | relation_type | requiredness | propagated_context | source_evidence_ids |
|---------|----------|--------------|------------|---------------|--------------|-------------------|---------------------|
| TE-311-1 | T-311 | `ADD CG` | `SET CDRTRANSFER` | `precedes` | required | CGNAME | EV-FK-Offline-UDG, EV-CFA |
| TE-311-2 | T-311 | `SET CDRTRANSFER` | `SET OFCTHRESHOLD` | `precedes` | required | — | EV-FK-Offline-UDG, EV-CFA |
| TE-311-3 | T-311 | `SET OFCTHRESHOLD` | `SET CONTAINERTRIGGER` | `precedes` | optional | — | EV-FK-Offline-UDG, EV-CFA |

### 4.5 T-303 配置CHF交互使能与选择链

| edge_id | task_ref | from_command | to_command | relation_type | requiredness | propagated_context | source_evidence_ids |
|---------|----------|--------------|------------|---------------|--------------|-------------------|---------------------|
| TE-303-1 | T-303 | `SET CHFINIT` | `ADD TNFINS` | `precedes` | required | CHFINIT=SENDREQ | EV-FK-Converged-UNC, EV-CFA |
| TE-303-2 | T-303 | `ADD TNFINS` | `ADD TNFINSIP` | `precedes` | required | TNFNAME | EV-FK-Converged-UNC, EV-CFA |
| TE-303-3 | T-303 | `ADD TNFINSIP` | `ADD TNFGRP` | `precedes` | required | TNFNAME → TNFGRP | EV-FK-Converged-UNC, EV-CFA |
| TE-303-4 | T-303 | `ADD TNFGRP` | `ADD TNFBINDGRP` | `precedes` | required | TNFGRPNAME, TNFNAME | EV-FK-Converged-UNC, EV-CFA |
| TE-303-5 | T-303 | `ADD TNFBINDGRP` | `ADD SELECTCHFGBYCC` | `precedes` | required | TNFGRPNAME → SELECTCHFGBYCC | EV-FK-Converged-UNC, EV-CFA |
| TE-303-6 | T-303 | `ADD SELECTCHFGBYCC` | `SET GLBDFTCHFGROUP` | `precedes` | optional | TNFGRPNAME | EV-FK-Converged-UNC, EV-CFA |

### 4.6 T-302 融合计费配置链（三联前置约束）

| edge_id | task_ref | from_command | to_command | relation_type | requiredness | propagated_context | source_evidence_ids |
|---------|----------|--------------|------------|---------------|--------------|-------------------|---------------------|
| TE-302-1 | T-302 | `SET CHGMODE` | `SET CHARGECTRL` | `precedes` | required | FORCED=NchfMode | EV-FK-Converged-UNC, EV-CFA |
| TE-302-2 | T-302 | `SET CHARGECTRL` | `SET CHFINIT` | `precedes` | required | RGAPPLIED | EV-FK-Converged-UNC, EV-CFA |

---

## 5. ConfigTask 适用矩阵（Task × Feature）

| Task | GWFD-110101 | GWFD-020351 | WSFD-109101 | GWFD-010171 | WSFD-011201 | GWFD-020300 | GWFD-010173 | WSFD-011206 | GWFD-020301 | WSFD-109002 | GWFD-020302 | GWFD-020303 | GWFD-020306 | WSFD-011202 |
|------|:-----------:|:-----------:|:-----------:|:-----------:|:-----------:|:-----------:|:-----------:|:-----------:|:-----------:|:-----------:|:-----------:|:-----------:|:-----------:|:-----------:|
| T-001 | ★ | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ | ★ | ☆ | ☆ | ☆ | ☆ | ☆ |
| T-002 | ★ | ★ | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ | ★ | ☆ | ☆ | ☆ | ☆ | ☆ |
| T-003 | ☆ | ★ | ★ | ☆ | ☆ | ☆ | ☆ | ☆ | ★ | ★ | ☆ | ☆ | ☆ | ☆ |
| T-004 | ☆ | ★ | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ | ★ | ★ | ☆ | ☆ | ☆ | ☆ |
| T-005 | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ | ★ | ☆ | ☆ | ☆ | ☆ |
| T-006 | ☆ | ☆ | ☆ | ★ | ☆ | ★ | ★ | ☆ | ★ | ★ | ★ | ★ | ★ | ☆ |
| T-007 | ☆ | ☆ | ☆ | ★ | ☆ | ★ | ★ | ☆ | ★ | ★ | ★ | ★ | ★ | ☆ |
| T-008 | ☆ | ★ | ☆ | ★ | ☆ | ★ | ★ | ☆ | ★ | ☆ | ★ | ★ | ★ | ☆ |
| T-101 | ★ | ★ | ★ | ☆ | ☆ | ★ | ☆ | ★ | ★ | ★ | ★ | ★ | ★ | ★ |
| T-102 | ★ | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ |
| T-103 | ★ | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ |
| T-104 | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ | ★ | ☆ | ☆ | ☆ | ☆ | ☆ |
| T-201 | ☆ | ☆ | ☆ | ☆ | ☆ | ★ | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ |
| T-202 | ☆ | ☆ | ☆ | ☆ | ☆ | ★ | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ |
| T-203 | ☆ | ☆ | ☆ | ☆ | ☆ | ★ | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ |
| T-204 | ☆ | ☆ | ☆ | ☆ | ☆ | ★ | ☆ | ★ | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ |
| T-301 | ☆ | ☆ | ☆ | ☆ | ★ | ☆ | ☆ | ★ | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ |
| T-302 | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ | ★ | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ |
| T-303 | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ | ★ | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ |
| T-304 | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ | ★ | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ |
| T-305 | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ | ★ | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ |
| T-306 | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ | ★ | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ |
| T-307 | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ | ★ | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ |
| T-308 | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ | ★ | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ |
| T-309 | ☆ | ☆ | ☆ | ☆ | ★ | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ | ★ |
| T-310 | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ | ★ | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ |
| T-311 | ☆ | ☆ | ☆ | ★ | ★ | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ |

> ★ = primary（主属特性，Task在此特性下定义）  ☆ = optional（可选复用，特性可选用此Task）

---

## 6. 与带宽场景任务层的对比

| 维度 | 计费场景 | 带宽控制场景 |
|------|---------|------------|
| 通用Task数 | 8（T-001~T-008） | 8（T-001~T-008） |
| 特性专属Task数 | 20（T-101~T-311） | ~22（T-101~T-603） |
| 共享通用Task | T-002(流过滤), T-003(PCC规则), T-004(用户模板), T-005(APN绑定), T-007(PCC策略组), T-008(刷新) | 同左 |
| 独有Task族 | 计费三件套(T-006 URR/URRGROUP), 在线计费(T-201~T-204), 融合计费(T-301~T-310), CG接口(T-311) | BWM(T-101~T-107), FUP(T-201~T-205), QoS(T-301~T-303), ADC(T-401~T-402), UNC控制面(T-501~T-504), 无线优化(T-601~T-603) |

> 两场景共享6个通用Task（流过滤/PCC规则/用户模板/APN绑定/PCC策略组/刷新）。计费场景独有URR计费三件套相关Task和协议配置Task；带宽场景独有限速/整形/FUP控制Task。

---

## 7. 对象计数汇总

| 对象类型 | 数量 | 编号范围 |
|---------|------|---------|
| ConfigTask | 27 | T-001~T-008（generic 8）+ T-101~T-311（feature_specific 19） |
| TaskRule | 6 | TR-CH-01~TR-CH-06 |
| TaskCommandOrderEdge | 20 | TE-006/007/003/311/303/302 系列 |
| **任务层对象总计** | **54** | — |

---

> 本文件为计费场景三层图谱第3层。第4层命令图谱、第5层跨层映射、第6层证据索引见同目录其他文件。
