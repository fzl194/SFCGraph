# 带宽控制场景任务原子层（新 Schema，v0.1）

> 范围：仅描述带宽控制场景（业务感知套餐2）在新三层图谱 schema 下的任务原子层部分。
> 约束：对象、关系、属性命名严格服从 `三层图谱Schema-最终版-v0.1.md` §10 任务原子层 Schema。
> 来源：基于 `cross-feature-analysis.md`（附录B命令、附录C对象、附录D端到端流程）。
> 说明：`ConfigTask` 是最小可复用配置原子，不强制隶属于某个 Feature。task 差异通过 `DecisionPoint + 关系边 + TaskRule` 表达。

---

## 0. 适用定义与来源

### 0.1 根定义

- `三层图谱本体标准定义.md`
- `三层图谱Schema-最终版-v0.1.md`

### 0.2 直接来源

- `cross-feature-analysis.md`（附录B MML命令交叉参考、附录C配置对象复用矩阵、附录D典型端到端配置流程）
- `feature-knowledge/*.md`（24个特性详情，含配置步骤）
- `topic-knowledge/Batch-19.md`（套餐2带宽控制配置实例）

### 0.3 本文件保留对象

| 对象 | 中文名 | 实例数 |
| --- | --- | --- |
| `ConfigTask` | 配置任务原子 | ~30 |
| `TaskRule` | 任务规则 | 6 |
| `TaskCommandOrderEdge` | 任务到命令编排边 | 见 §4 |
| `DecisionPoint`（task层） | 决策点 | 引用 `01-business-graph.md` DP-BW-* |

---

## 1. ConfigTask 分组总览

按 `task_scope_type` 分为 3 类：

| scope_type | 说明 | 数量 |
| --- | --- | --- |
| `generic` | 跨特性复用的通用 task | 8 |
| `feature_specific` | 特定特性族专属 task | 22 |

---

## 2. 通用 Task（generic，跨特性复用）

### 2.1 T-001: 规划业务分类与识别条件

| 字段 | 值 |
| --- | --- |
| `task_id` | `T-001` |
| `task_name` | `规划业务分类与识别条件` |
| `task_summary` | 规划 SVC/APP 业务大类与具体应用，定义识别条件 |
| `task_scope_type` | `generic` |
| `task_goal` | 建立业务分类体系，为后续 BWM/FUP/ADC/QoS 提供识别基础 |
| `input_contract` | 业务需求清单、目标业务类型列表 |
| `output_contract` | 业务分类表、识别条件定义 |
| `command_refs` | `ADD CATEGORYPROP`, `ADD FILTER`, `ADD L7FILTER` |
| `status` | `active` |
| `source_evidence_ids` | `EV-TK-17`, `EV-TK-19`, `EV-FK-110101` |

### 2.2 T-002: 配置流过滤器与绑定

| 字段 | 值 |
| --- | --- |
| `task_id` | `T-002` |
| `task_name` | `配置流过滤器与绑定` |
| `task_summary` | 配置 FlowFilter/FILTER/L7FILTER 及绑定关系，定义业务流匹配条件 |
| `task_scope_type` | `generic` |
| `task_goal` | 建立可复用的流匹配条件 |
| `input_contract` | T-001 输出的业务分类表 |
| `output_contract` | FlowFilter 配置实例 |
| `command_refs` | `ADD FLOWFILTER`, `ADD FILTER`, `ADD L7FILTER`, `ADD FLTBINDFLOWF` |
| `status` | `active` |
| `source_evidence_ids` | `EV-CFA-§2.5`, `EV-FK-020351` |

### 2.3 T-003: 配置 PCC 规则

| 字段 | 值 |
| --- | --- |
| `task_id` | `T-003` |
| `task_name` | `配置 PCC 规则` |
| `task_summary` | 通过 ADD RULE 定义 PCC 规则，含 RULENAME/POLICYTYPE/PRIORITY/FLOWFILTER |
| `task_scope_type` | `generic` |
| `task_goal` | 建立策略规则实例，承接 FlowFilter 与策略动作 |
| `input_contract` | T-002 输出的 FlowFilter、策略类型决策(DP-BW-01) |
| `output_contract` | RULE 配置实例（POLICYTYPE=BWM/PCC/QOS/ADC） |
| `command_refs` | `ADD RULE` |
| `status` | `active` |
| `source_evidence_ids` | `EV-CFA-§2.1`, `EV-CFA-§5.1` |

### 2.4 T-004: 配置用户模板与规则绑定

| 字段 | 值 |
| --- | --- |
| `task_id` | `T-004` |
| `task_name` | `配置用户模板与规则绑定` |
| `task_summary` | 配置 USERPROFILE（UPTYPE=PCC）并通过 RULEBINDING 绑定 RULE |
| `task_scope_type` | `generic` |
| `task_goal` | 将规则组织为用户模板，承载多类型规则组合 |
| `input_contract` | T-003 输出的 RULE 实例 |
| `output_contract` | USERPROFILE + RULEBINDING 配置实例 |
| `command_refs` | `ADD USERPROFILE`, `ADD RULEBINDING` |
| `status` | `active` |
| `source_evidence_ids` | `EV-CFA-§2.5` |

### 2.5 T-005: 配置用户模板组与 APN 绑定

| 字段 | 值 |
| --- | --- |
| `task_id` | `T-005` |
| `task_name` | `配置用户模板组与 APN 绑定` |
| `task_summary` | 配置 USRPROFGROUP/UPBINDUPG/APNUSRPROFG 标准绑定链，使策略按 APN/DNN 生效 |
| `task_scope_type` | `generic` |
| `task_goal` | 完成 APN 级策略生效的标准绑定链 |
| `input_contract` | T-004 输出的 USERPROFILE |
| `output_contract` | USRPROFGROUP + UPBINDUPG + APNUSRPROFG 配置实例 |
| `command_refs` | `ADD USRPROFGROUP`, `ADD UPBINDUPG`, `ADD APNUSRPROFG` |
| `status` | `active` |
| `source_evidence_ids` | `EV-CFA-§2.5` |

### 2.6 T-006: 策略刷新生效

| 字段 | 值 |
| --- | --- |
| `task_id` | `T-006` |
| `task_name` | `策略刷新生效` |
| `task_summary` | 执行 SET REFRESHSRV 刷新策略，约60秒后完全下发（PROTBINDFLOWF定时器） |
| `task_scope_type` | `generic` |
| `task_goal` | 使配置变更生效 |
| `input_contract` | 所有策略配置完成 |
| `output_contract` | 策略生效 |
| `command_refs` | `SET REFRESHSRV` |
| `status` | `active` |
| `source_evidence_ids` | `EV-CFA-§5.5`, `EV-TK-20` |

> **硬约束**: 该 task 必须为 FeatureTaskOrderEdge 链的 `must_be_last`。

### 2.7 T-007: License 开启

| 字段 | 值 |
| --- | --- |
| `task_id` | `T-007` |
| `task_name` | `License 开启` |
| `task_summary` | 通过 SET LICENSESWITCH 开启对应特性的 License，是全部特性的前置门控 |
| `task_scope_type` | `generic` |
| `task_goal` | 满足 License 前置门控(BR-BW-06) |
| `input_contract` | 特性清单、对应 License 项 |
| `output_contract` | License 使能 |
| `command_refs` | `SET LICENSESWITCH` |
| `status` | `active` |
| `source_evidence_ids` | `EV-CFA-§2.3` |

### 2.8 T-008: SA 特征库加载

| 字段 | 值 |
| --- | --- |
| `task_id` | `T-008` |
| `task_name` | `SA 特征库加载` |
| `task_summary` | 加载 SA 特征库与解析库，为业务识别提供数据基础 |
| `task_scope_type` | `generic` |
| `task_goal` | 使 SA 引擎具备业务识别能力 |
| `input_contract` | SA 特征库文件、解析库文件 |
| `output_contract` | SA 引擎就绪 |
| `command_refs` | `LOD SIGNATUREDB`, `LOD PARSERDB` |
| `status` | `active` |
| `source_evidence_ids` | `EV-FK-110101`, `EV-FK-111600` |

---

## 3. 特性专属 Task（feature_specific）

### 3.1 BWM 专属 Task

| `task_id` | `task_name` | `task_summary` | `command_refs` | `status` | `source_evidence_ids` |
| --- | --- | --- | --- | --- | --- |
| `T-101` | 规划 BWM 控制策略 | 规划控制层级(用户/组/全局)、CTRLTYPE(CAR/SHAPING)、参数模式 | （规划task，无命令） | `active` | `EV-FK-110311`, `EV-TK-19` |
| `T-102` | 配置 BWM 服务 | ADD BWMSERVICE 定义 BWM 业务实例（业务名/协议） | `ADD BWMSERVICE` | `active` | `EV-FK-110311` |
| `T-103` | 配置 BWM 控制器 | ADD BWMCONTROLLER 配置限速/整形参数（CIR/PIR/CBS/PBS 或 RATE/QUEDEPTH） | `ADD BWMCONTROLLER` | `active` | `EV-FK-110311`, `EV-CFA-附录F` |
| `T-104` | 配置 BWM 用户组 | ADD BWMUSERGROUP 定义用户组（SPECIFIC_GROUP/GLOBAL） | `ADD BWMUSERGROUP` | `active` | `EV-FK-110311` |
| `T-105` | 配置 BWM 规则 | ADD BWMRULE / ADD BWMRULEGLOBAL 定义规则（BWMRULETYPE + 控制器引用） | `ADD BWMRULE`, `ADD BWMRULEGLOBAL` | `active` | `EV-FK-110311` |
| `T-106` | 配置 BWM APN 绑定 | ADD APNBINDBWMUSRG 将 BWM 用户组绑定到 APN | `ADD APNBINDBWMUSRG` | `active` | `EV-FK-110311` |
| `T-107` | 配置业务服务等级策略 | ADD BCSRVLEVELPLY 为智能Shaping定义各 ServiceLevel 的 SHAPRATE | `ADD BCSRVLEVELPLY` | `active` | `EV-FK-110313` |

### 3.2 FUP 专属 Task

| `task_id` | `task_name` | `task_summary` | `command_refs` | `status` | `source_evidence_ids` |
| --- | --- | --- | --- | --- | --- |
| `T-201` | 规划 FUP 配额策略 | 规划累计粒度(会话/业务)、Monitoring-Key、阈值 | （规划task） | `active` | `EV-FK-020353`, `EV-TK-01` |
| `T-202` | 配置 URR | ADD URR 定义使用量上报规则（URRID/USAGERPTMODE/REPORTINGTHRESHOLD） | `ADD URR` | `active` | `EV-FK-020353`, `EV-CFA-§5.2` |
| `T-203` | 配置 URR 组 | ADD URRGROUP 组合多个 URR（UPURRNAME1/2/3） | `ADD URRGROUP` | `active` | `EV-FK-020353` |
| `T-204` | 配置 FUP PCC 策略组 | ADD PCCPOLICYGRP 将 URRGROUP 纳入策略组 | `ADD PCCPOLICYGRP` | `active` | `EV-FK-020353` |
| `T-205` | 配置 Gx FUP 功能(UNC) | SET PCCFUNC + MOD PCRF(UMCH) + MOD PCCPOLICYGRP(FUPSESSIONEXC)，仅Gx场景 | `SET PCCFUNC`, `MOD PCRF`, `MOD PCCPOLICYGRP` | `active` | `EV-FK-109104`, `EV-CFA-§3.3` |

### 3.3 QoS/GBR Task

| `task_id` | `task_name` | `task_summary` | `command_refs` | `status` | `source_evidence_ids` |
| --- | --- | --- | --- | --- | --- |
| `T-301` | 配置 QoS 属性 | ADD QOSPROP 定义 QoS 参数（5QI/QCI/MBR/GBR/ARP，QOSTYPE区分5G/4G） | `ADD QOSPROP` | `active` | `EV-FK-020358`, `EV-TK-24` |
| `T-302` | 配置专有 QoS Flow 空闲定时器 | SET APNIDLETIME 定义专有 QoS Flow 空闲释放时间 | `SET APNIDLETIME` | `active` | `EV-FK-109107` |
| `T-303` | 配置去活 QoS Flow 策略 | ADD APNDEACTQFPLCY 定义延迟释放策略 | `ADD APNDEACTQFPLCY` | `active` | `EV-FK-109107` |

### 3.4 ADC Task

| `task_id` | `task_name` | `task_summary` | `command_refs` | `status` | `source_evidence_ids` |
| --- | --- | --- | --- | --- | --- |
| `T-401` | 配置 ADC 参数 | ADD ADCPARA 定义 ADC 检测参数 | `ADD ADCPARA` | `active` | `EV-FK-020357`, `EV-TK-27` |
| `T-402` | 配置 ADC 三策略组 | ADD RULE 定义 Normal/Start/Stop 三个策略组 | `ADD RULE` | `active` | `EV-FK-020357`, `EV-CTA-§7.5` |

### 3.5 UNC 控制面 Task

| `task_id` | `task_name` | `task_summary` | `command_refs` | `status` | `source_evidence_ids` |
| --- | --- | --- | --- | --- | --- |
| `T-501` | 配置 PCRF 组与绑定 | ADD PCRF/PCRFGROUP/PCRFBINDGRP/SET DFTGLBPCRFGRP | `ADD PCRF`, `ADD PCRFGROUP`, `ADD PCRFBINDGRP`, `SET DFTGLBPCRFGRP` | `active` | `EV-FK-109101` |
| `T-502` | 配置 PCC 功能开关 | SET PCCFUNC / SET APNPCCFUNC | `SET PCCFUNC`, `SET APNPCCFUNC` | `active` | `EV-FK-109101` |
| `T-503` | 配置 PCC 故障与定时器 | SET PCCFAILACTION / SET PCCTIMER | `SET PCCFAILACTION`, `SET PCCTIMER` | `active` | `EV-FK-109101` |
| `T-504` | 配置 N7 属性控制 | SET N7RCVATTRCTRL / SET N7SNDATTRCTRL（仅5G） | `SET N7RCVATTRCTRL`, `SET N7SNDATTRCTRL` | `active` | `EV-FK-109101` |

### 3.6 无线优化 Task

| `task_id` | `task_name` | `task_summary` | `command_refs` | `status` | `source_evidence_ids` |
| --- | --- | --- | --- | --- | --- |
| `T-601` | 配置 DSCP/FPI 标记 | 按业务类型映射 DSCP 或 FPI 值，影响无线调度 | （依特性定，GWFD-020359/110331） | `active` | `EV-FK-020359`, `EV-FK-110331` |
| `T-602` | 配置终端 OS 差异化 | SET APNOSLELBWMSW 开启终端OS BWM差异化 | `SET APNOSLELBWMSW` | `active` | `EV-FK-110301` |
| `T-603` | 配置小区负荷上报 | SET APNREPORTATTR 配置APN拥塞上报属性 | `SET APNREPORTATTR` | `active` | `EV-FK-110332`, `EV-FK-211101` |

---

## 4. TaskCommandOrderEdge（task 内部命令顺序）

来源：`cross-feature-analysis.md` 附录D。

### 4.1 T-005 内部命令顺序（标准绑定链）

| `edge_id` | `task_ref` | `from_command_ref` | `to_command_ref` | `relation_type` | `requiredness` | `propagated_context` | `source_evidence_ids` |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `TE-005-1` | `T-005` | `ADD USERPROFILE` | `ADD RULEBINDING` | `precedes` | `required` | `UPNAME` | `EV-CFA-§2.5` |
| `TE-005-2` | `T-005` | `ADD RULEBINDING` | `ADD USRPROFGROUP` | `precedes` | `required` | `UPNAME→UPGNAME` | `EV-CFA-§2.5` |
| `TE-005-3` | `T-005` | `ADD USRPROFGROUP` | `ADD UPBINDUPG` | `precedes` | `required` | `UPGNAME` | `EV-CFA-§2.5` |
| `TE-005-4` | `T-005` | `ADD UPBINDUPG` | `ADD APNUSRPROFG` | `precedes` | `required` | `UPGNAME→APNNAME` | `EV-CFA-§2.5` |

### 4.2 T-204 内部命令顺序（FUP计费链）

| `edge_id` | `task_ref` | `from_command_ref` | `to_command_ref` | `relation_type` | `requiredness` | `propagated_context` | `source_evidence_ids` |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `TE-204-1` | `T-204` | `ADD URR` | `ADD URRGROUP` | `precedes` | `required` | `URRID → URRGROUP.UPURRNAME1` | `EV-FK-020353` |
| `TE-204-2` | `T-204` | `ADD URRGROUP` | `ADD PCCPOLICYGRP` | `precedes` | `required` | `URRGROUPNAME → PCCPOLICYGRP` | `EV-FK-020353` |

### 4.3 T-103 内部（BWM控制器独立配置）

T-103（配置BWM控制器）为单命令 task，无内部命令顺序依赖。BWMCONTROLLER 配置独立，参数由 DP-BW-05 决定模式。

### 4.4 T-107 内部（智能Shaping ServiceLevel）

| `edge_id` | `task_ref` | `from_command_ref` | `to_command_ref` | `relation_type` | `requiredness` | `propagated_context` | `source_evidence_ids` |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `TE-107-1` | `T-107` | `ADD BWMCONTROLLER` | `ADD BCSRVLEVELPLY` | `depends_on` | `required` | `BWMCNAME→SERVICELEVEL` | `EV-FK-110313` |

---

## 5. TaskRule

6 条 task 级规则。

| `rule_id` | `task_ref` | `rule_name` | `rule_type` | `rule_expression_mode` | `rule_logic` | `status` | `source_evidence_ids` |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `TR-BW-01` | `T-006` | REFRESHSRV 必须最后执行 | `dependency_rule` | `explicit` | T-006 必须在所有策略配置 task 之后执行，且执行后约60秒生效 | `active` | `EV-CFA-§5.5` |
| `TR-BW-02` | `T-003` | POLICYTYPE 决定策略类型分支 | `selection_rule` | `explicit` | T-003 的 POLICYTYPE 取值由 DP-BW-01 决定，不同取值导向不同下游 task（BWM→T-102，ADC→T-401） | `active` | `EV-CFA-§5.1`, `EV-CFA-§5.6` |
| `TR-BW-03` | `T-103` | CTRLTYPE 决定参数集 | `selection_rule` | `explicit` | T-103 的 CTRLTYPE 由 DP-BW-05 决定：CAR 用 CIR/PIR/CBS/PBS，SHAPING 用 RATE/QUEDEPTH | `active` | `EV-FK-110311`, `EV-CFA-附录F` |
| `TR-BW-04` | `T-202` | USAGERPTMODE 决定 URR 用途 | `selection_rule` | `explicit` | T-202 的 USAGERPTMODE：会话FUP=ONLINE/MONITORINGKEY，业务FUP=MONITORINGKEY，QoS保证=QOS | `active` | `EV-CFA-§5.2` |
| `TR-BW-05` | `T-205` | Gx FUP 额外配置 | `scope_rule` | `explicit` | T-205 仅在 Gx 接口(DP-BW-04=4G)场景需要；N7(5G)场景仅需 License，阈值由PCF侧配置 | `active` | `EV-FK-109104`, `EV-CFA-§3.3` |
| `TR-BW-06` | `T-301` | QOSTYPE 区分 5G/4G | `validation_rule` | `explicit` | T-301 的 QOSTYPE：5G=QOS_FLOW_PARA(用FQI)，2/3/4G=QOS_BEARER_PARA(用QCIVALUE) | `active` | `EV-FK-020358`, `EV-FK-109107` |

---

## 6. 任务原子层关系边汇总

| 起点 | 关系 | 终点 | 数量 |
| --- | --- | --- | --- |
| `ConfigTask` | `constrained_by` | `TaskRule` | 6条（见§5） |
| `ConfigTask` | `has_decision` | `DecisionPoint` | 见`01-business-graph.md` |
| `ConfigTask` | `invokes` | `MMLCommand` | 见`05-cross-layer-mapping.md` |
| `ConfigTask` | `targets` | `SemanticObject/ConfigObject` | 见`05-cross-layer-mapping.md` |
| `ConfigTask` | `orchestrates` | `TaskCommandOrderEdge` | 见§4 |
| `ConfigTask` | `may_require_feature` | `Feature` | feature_specific task 关联 |
| `ConfigTask` | `supported_by` | `EvidenceSource` | 见各 task `source_evidence_ids` |
