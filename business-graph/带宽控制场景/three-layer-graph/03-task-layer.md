# 带宽控制场景三层图谱 · 第3层：任务原子层

> **文件定位**：`three-layer-graph/03-task-layer.md`
> **Schema参考**：`三层图谱Schema-最终版-v0.1.md` §10 任务原子层
> **作用**：实例化32个ConfigTask + 6条TaskRule + TaskCommandOrderEdge
> **数据来源**：`cross-feature-analysis.md`（附录D端到端配置流程、附录B命令交叉参考、附录C配置对象复用矩阵）、`feature-knowledge/*.md`（24个特性知识文档）

---

## §0 任务层总览

### 0.1 ConfigTask 分类

| 类型 | 数量 | 编号范围 | 说明 |
|------|------|---------|------|
| generic（通用，跨特性复用） | 8 | T-001~T-008 | 分类/流过滤/PCC规则/用户模板/APN绑定/刷新/License/SA特征库 |
| feature_specific（特性专属） | 24 | T-101~T-603 | BWM/FUP/QoS/ADC/UNC控制面/无线优化专属 |
| **合计** | **32** | — | — |

> **Task编号段说明**：
> - `T-001~T-008`：通用Task（generic），跨特性复用的基础配置步骤
> - `T-101~T-107`：BWM专属（规划/服务/控制器/用户组/规则/APN绑定/服务等级策略）
> - `T-201~T-205`：FUP专属（规划/URR/URR组/PCC策略组/Gx FUP功能）
> - `T-301~T-303`：QoS/GBR专属（QoS属性/空闲定时器/去活策略）
> - `T-401~T-402`：ADC专属（ADC参数/三策略组）
> - `T-501~T-504`：UNC控制面专属（PCRF组/功能开关/故障定时器/N7属性）
> - `T-601~T-603`：无线优化专属（DSCP/FPI标记/终端OS差异化/小区负荷上报）

### 0.2 任务原子化原则

1. **每Task一个明确goal**：可复用的配置步骤独立成Task
2. **generic优先**：跨3+特性复用的步骤提升为generic
3. **feature_specific保留特性语义**：BWM三级控制体系、FUP三件套等不可泛化的步骤保留特性绑定
4. **命令顺序通过TaskCommandOrderEdge表达**：Task间顺序通过`05-cross-layer-mapping.md`的FeatureTaskOrderEdge表达

### 0.3 与计费场景编号段隔离

> 带宽控制场景使用 `T-101~T-603` 编号段（不含T-201在线计费/T-301融合计费），与计费场景的 `T-101~T-311` 编号段不重叠。合并时需加场景前缀（如 `T-BW-101`）避免冲突。通用Task `T-001~T-008` 两场景编号相同，合并时同样需加前缀。

---

## §1 通用Task（generic，8个）

### T-001 规划业务分类与识别条件

| 字段 | 值 |
|------|---|
| `task_id` | `T-001` |
| `task_name` | `规划业务分类与识别条件` |
| `task_summary` | 建立业务分类体系，为BWM/FUP/ADC/QoS提供SA分类基础 |
| `task_scope_type` | `generic` |
| `task_goal` | 定义SVC业务大类与APP具体应用的识别规则，输出CATEGORYPROP/FILTER/L7FILTER实例集 |
| `input_contract` | 业务需求清单、目标业务类型列表 |
| `output_contract` | 业务分类表、CATEGORYPROP/FILTER/L7FILTER实例集 |
| `command_refs` | `ADD CATEGORYPROP`, `ADD FILTER`, `ADD L7FILTER` |
| `status` | `active` |
| `source_evidence_ids` | `EV-FK-BW-SA-Basic`, `EV-FK-BW-BWM`, `EV-CA-01` |
| `reused_by` | SA-BWM, FUP业务级, ADC, QoS保证, Shaping, IM管控, 码率差异化, 视频解耦, FPI标记 |

### T-002 配置流过滤器与绑定

| 字段 | 值 |
|------|---|
| `task_id` | `T-002` |
| `task_name` | `配置流过滤器与绑定` |
| `task_summary` | 建立可复用的流匹配条件，承接BWM/FUP/ADC/QoS规则匹配 |
| `task_scope_type` | `generic` |
| `task_goal` | 配置FlowFilter/FILTER/L7FILTER及绑定关系，定义业务流匹配条件 |
| `input_contract` | T-001输出的业务分类表 |
| `output_contract` | FLOWFILTER + 绑定关系实例集 |
| `command_refs` | `ADD FLOWFILTER`, `ADD FLTBINDFLOWF` |
| `status` | `active` |
| `source_evidence_ids` | `EV-FK-BW-SA-Basic`, `EV-FK-BW-PCC-UDG`, `EV-CA-01` |
| `reused_by` | 所有需要业务流匹配的特性（BWM/FUP/ADC/QoS/Shaping） |

### T-003 配置PCC规则

| 字段 | 值 |
|------|---|
| `task_id` | `T-003` |
| `task_name` | `配置PCC规则` |
| `task_summary` | 通过ADD RULE定义PCC策略规则，POLICYTYPE由决策点决定（BWM/PCC/QOS/ADC） |
| `task_scope_type` | `generic` |
| `task_goal` | 建立策略规则实例，承接FlowFilter与策略动作，POLICYTYPE标识策略类型分支 |
| `input_contract` | T-002输出的FLOWFILTER + 策略类型决策(DP-BW-01) |
| `output_contract` | RULE实例（POLICYTYPE=BWM/PCC/QOS/ADC） |
| `command_refs` | `ADD RULE` |
| `status` | `active` |
| `source_evidence_ids` | `EV-FK-BW-PCC-UDG`, `EV-FK-BW-PCC-UNC`, `EV-CA-01` |
| `reused_by` | BWM, FUP, ADC, QoS保证（全部PCC特性） |
| `note` | POLICYTYPE是统一策略标识（发现一）：BWM=带宽管理、PCC=标准PCC含FUP、QOS=QoS属性、ADC=应用检测 |

### T-004 配置用户模板与规则绑定

| 字段 | 值 |
|------|---|
| `task_id` | `T-004` |
| `task_name` | `配置用户模板与规则绑定` |
| `task_summary` | 配置USERPROFILE（UPTYPE=PCC）并通过RULEBINDING绑定RULE |
| `task_scope_type` | `generic` |
| `task_goal` | 将规则组织为用户模板，承载多类型规则组合 |
| `input_contract` | T-003输出的RULE实例集 |
| `output_contract` | USERPROFILE + RULEBINDING实例集 |
| `command_refs` | `ADD USERPROFILE`, `ADD RULEBINDING` |
| `status` | `active` |
| `source_evidence_ids` | `EV-FK-BW-PCC-UDG`, `EV-CA-01` |
| `reused_by` | 所有PCC特性（BWM/FUP/ADC/QoS/Shaping/码率差异化） |

### T-005 配置用户模板组与APN绑定

| 字段 | 值 |
|------|---|
| `task_id` | `T-005` |
| `task_name` | `配置用户模板组与APN绑定` |
| `task_summary` | 完成APN/DNN级策略生效的标准绑定链（USRPROFGROUP→UPBINDUPG→APNUSRPROFG） |
| `task_scope_type` | `generic` |
| `task_goal` | 使策略按APN/DNN生效，完成标准绑定链 |
| `input_contract` | T-004输出的USERPROFILE实例 |
| `output_contract` | USRPROFGROUP + UPBINDUPG + APNUSRPROFG实例集 |
| `command_refs` | `ADD USRPROFGROUP`, `ADD UPBINDUPG`, `ADD APNUSRPROFG` |
| `status` | `active` |
| `source_evidence_ids` | `EV-CA-01` |
| `reused_by` | BWM(UNC侧), FUP(UNC侧), QoS保证(UNC侧), ADC(UNC侧) |

### T-006 策略刷新生效

| 字段 | 值 |
|------|---|
| `task_id` | `T-006` |
| `task_name` | `策略刷新生效` |
| `task_summary` | 执行SET REFRESHSRV刷新策略，约60秒后完全下发（PROTBINDFLOWF定时器） |
| `task_scope_type` | `generic` |
| `task_goal` | 使UDG侧配置变更生效 |
| `input_contract` | 所有策略配置完成 |
| `output_contract` | 配置生效 |
| `command_refs` | `SET REFRESHSRV` |
| `status` | `active` |
| `source_evidence_ids` | `EV-FK-BW-PCC-UDG`, `EV-FK-BW-SA-Basic`, `EV-FK-BW-BWM`, `EV-CA-01` |
| `reused_by` | PCC, SA-Basic, BWM, Shaping |
| `must_be_last` | `true` |
| `note` | TR-BW-01硬约束：必须最后执行，PROTBINDFLOWF需等待60秒 |

### T-007 License开启

| 字段 | 值 |
|------|---|
| `task_id` | `T-007` |
| `task_name` | `License开启` |
| `task_summary` | 通过SET LICENSESWITCH开启对应特性的License，是全部特性的前置门控 |
| `task_scope_type` | `generic` |
| `task_goal` | 满足License前置门控，使特性功能可用 |
| `input_contract` | 特性清单、对应License项 |
| `output_contract` | License使能 |
| `command_refs` | `SET LICENSESWITCH` |
| `status` | `active` |
| `source_evidence_ids` | `EV-CA-01` |
| `reused_by` | 全部24个特性（16 UDG + 8 UNC独立License） |
| `note` | UDG与UNC的License编号体系完全独立（发现四），需分别获取 |

### T-008 SA特征库加载

| 字段 | 值 |
|------|---|
| `task_id` | `T-008` |
| `task_name` | `SA特征库加载` |
| `task_summary` | 加载SA特征库与解析库，为SA-Basic引擎提供业务识别数据基础 |
| `task_scope_type` | `generic` |
| `task_goal` | 使SA引擎具备L3/L4/L7业务识别能力 |
| `input_contract` | SA特征库文件（signature_db.dat）、解析库文件（parser_db.dat） |
| `output_contract` | SA引擎就绪 |
| `command_refs` | `LOD SIGNATUREDB`, `LOD PARSERDB` |
| `status` | `active` |
| `source_evidence_ids` | `EV-FK-BW-SA-Basic`, `EV-FK-BW-SA-Mgmt` |
| `reused_by` | SA-Basic(GWFD-110101), SA特征库管控(GWFD-111600) |
| `note` | SA-Basic辐射范围最大，12个特性直接依赖其业务识别能力（§4.2辐射分析） |

---

## §2 BWM专属Task（feature_specific，7个）

### T-101 规划BWM控制策略

| 字段 | 值 |
|------|---|
| `task_id` | `T-101` |
| `task_name` | `规划BWM控制策略` |
| `task_summary` | 规划控制层级(用户级/组级/全局级)、CTRLTYPE(CAR/SHAPING)、参数模式 |
| `task_scope_type` | `feature_specific` |
| `task_goal` | 输出BWM三级控制策略规划（BWMRULETYPE + CTRLTYPE + 参数映射） |
| `input_contract` | 业务需求、带宽控制目标 |
| `output_contract` | BWM策略规划表（层级/模式/参数） |
| `command_refs` | （规划task，无命令） |
| `status` | `active` |
| `source_evidence_ids` | `EV-FK-BW-BWM`, `EV-CA-01` |
| `feature_ref` | GWFD-110311, WSFD-211005 |

### T-102 配置BWM服务

| 字段 | 值 |
|------|---|
| `task_id` | `T-102` |
| `task_name` | `配置BWM服务` |
| `task_summary` | ADD BWMSERVICE定义BWM业务实例（业务名/协议/业务类型） |
| `task_scope_type` | `feature_specific` |
| `task_goal` | 建立BWM业务实例，将SA识别的SVC/APP映射为BWM控制对象 |
| `input_contract` | T-101策略规划表 |
| `output_contract` | BWMSERVICE实例 |
| `command_refs` | `ADD BWMSERVICE` |
| `status` | `active` |
| `source_evidence_ids` | `EV-FK-BW-BWM` |
| `feature_ref` | GWFD-110311 |

### T-103 配置BWM控制器

| 字段 | 值 |
|------|---|
| `task_id` | `T-103` |
| `task_name` | `配置BWM控制器` |
| `task_summary` | ADD BWMCONTROLLER配置限速/整形参数（CIR/PIR/CBS/PBS或RATE/QUEDEPTH） |
| `task_scope_type` | `feature_specific` |
| `task_goal` | 定义令牌桶参数和三色标记处理策略（GREEN/YELLOW/RED动作） |
| `input_contract` | T-101策略规划中的CTRLTYPE决策(DP-BW-05) |
| `output_contract` | BWMCONTROLLER实例 |
| `command_refs` | `ADD BWMCONTROLLER` |
| `status` | `active` |
| `source_evidence_ids` | `EV-FK-BW-BWM`, `EV-CA-01` |
| `feature_ref` | GWFD-110311 |
| `note` | TR-BW-03: CTRLTYPE决定参数集 — CAR用CIR/PIR/CBS/PBS，SHAPING用RATE/QUEDEPTH |

### T-104 配置BWM用户组

| 字段 | 值 |
|------|---|
| `task_id` | `T-104` |
| `task_name` | `配置BWM用户组` |
| `task_summary` | ADD BWMUSERGROUP定义用户组（SPECIFIC_GROUP/GLOBAL） |
| `task_scope_type` | `feature_specific` |
| `task_goal` | 建立BWM控制对象分组，支持用户级和组级控制 |
| `input_contract` | T-101策略规划中的层级决策 |
| `output_contract` | BWMUSERGROUP实例 |
| `command_refs` | `ADD BWMUSERGROUP` |
| `status` | `active` |
| `source_evidence_ids` | `EV-FK-BW-BWM` |
| `feature_ref` | GWFD-110311, GWFD-110313 |

### T-105 配置BWM规则

| 字段 | 值 |
|------|---|
| `task_id` | `T-105` |
| `task_name` | `配置BWM规则` |
| `task_summary` | ADD BWMRULE/ADD BWMRULEGLOBAL定义规则（BWMRULETYPE + BWMSERVICE + BWMCONTROLLER引用） |
| `task_scope_type` | `feature_specific` |
| `task_goal` | 建立BWM规则，关联BWMSERVICE（匹配业务）与BWMCONTROLLER（执行控制） |
| `input_contract` | T-102 BWMSERVICE实例 + T-103 BWMCONTROLLER实例 + T-104 BWMUSERGROUP实例 |
| `output_contract` | BWMRULE/BWMRULEGLOBAL实例 |
| `command_refs` | `ADD BWMRULE`, `ADD BWMRULEGLOBAL` |
| `status` | `active` |
| `source_evidence_ids` | `EV-FK-BW-BWM` |
| `feature_ref` | GWFD-110311 |

### T-106 配置BWM APN绑定

| 字段 | 值 |
|------|---|
| `task_id` | `T-106` |
| `task_name` | `配置BWM APN绑定` |
| `task_summary` | ADD APNBINDBWMUSRG将BWM用户组绑定到APN/DNN |
| `task_scope_type` | `feature_specific` |
| `task_goal` | 使BWM控制按APN/DNN生效 |
| `input_contract` | T-104 BWMUSERGROUP实例 |
| `output_contract` | APNBINDBWMUSRG实例 |
| `command_refs` | `ADD APNBINDBWMUSRG` |
| `status` | `active` |
| `source_evidence_ids` | `EV-FK-BW-BWM` |
| `feature_ref` | GWFD-110311 |

### T-107 配置业务服务等级策略

| 字段 | 值 |
|------|---|
| `task_id` | `T-107` |
| `task_name` | `配置业务服务等级策略` |
| `task_summary` | ADD BCSRVLEVELPLY为智能Shaping定义各ServiceLevel的SHAPRATE比例 |
| `task_scope_type` | `feature_specific` |
| `task_goal` | 为组级智能Shaping定义多优先级带宽分配策略 |
| `input_contract` | T-103 BWMCONTROLLER实例（WORKMODE=AUTO/MANUAL） |
| `output_contract` | BCSRVLEVELPLY实例集 |
| `command_refs` | `ADD BCSRVLEVELPLY` |
| `status` | `active` |
| `source_evidence_ids` | `EV-FK-BW-SmartShaping` |
| `feature_ref` | GWFD-110313 |

---

## §3 FUP专属Task（feature_specific，5个）

### T-201 规划FUP配额策略

| 字段 | 值 |
|------|---|
| `task_id` | `T-201` |
| `task_name` | `规划FUP配额策略` |
| `task_summary` | 规划累计粒度(会话级/业务级)、Monitoring-Key分配、阈值策略 |
| `task_scope_type` | `feature_specific` |
| `task_goal` | 输出FUP配额策略规划（粒度/Key/阈值/降速方案） |
| `input_contract` | 业务需求、流量配额目标 |
| `output_contract` | FUP策略规划表 |
| `command_refs` | （规划task，无命令） |
| `status` | `active` |
| `source_evidence_ids` | `EV-FK-BW-SessionFUP`, `EV-FK-BW-ServiceFUP`, `EV-CA-01` |
| `feature_ref` | GWFD-020353, GWFD-110312, WSFD-109104, WSFD-211009 |

### T-202 配置URR

| 字段 | 值 |
|------|---|
| `task_id` | `T-202` |
| `task_name` | `配置URR` |
| `task_summary` | ADD URR定义使用量上报规则（URRID/USAGERPTMODE/MEASUREMENTMETHOD/REPORTINGTHRESHOLD） |
| `task_scope_type` | `feature_specific` |
| `task_goal` | 定义流量监控规则，USAGERPTMODE决定URR用途模式 |
| `input_contract` | T-201策略规划 |
| `output_contract` | URR实例 |
| `command_refs` | `ADD URR` |
| `status` | `active` |
| `source_evidence_ids` | `EV-FK-BW-SessionFUP`, `EV-FK-BW-ServiceFUP`, `EV-CA-01` |
| `feature_ref` | GWFD-020353, GWFD-110312, WSFD-109104, WSFD-211009 |
| `note` | TR-BW-04: USAGERPTMODE决定URR用途 — 会话FUP=ONLINE/MONITORINGKEY，业务FUP=MONITORINGKEY，QoS保证=QOS（发现二） |

### T-203 配置URR组

| 字段 | 值 |
|------|---|
| `task_id` | `T-203` |
| `task_name` | `配置URR组` |
| `task_summary` | ADD URRGROUP组合多个URR（UPURRNAME1/2/3仅为编号，无优先级语义） |
| `task_scope_type` | `feature_specific` |
| `task_goal` | 组织URR为逻辑组，供PCCPOLICYGRP引用 |
| `input_contract` | T-202 URR实例 |
| `output_contract` | URRGROUP实例 |
| `command_refs` | `ADD URRGROUP` |
| `status` | `active` |
| `source_evidence_ids` | `EV-FK-BW-SessionFUP`, `EV-FK-BW-ServiceFUP` |
| `feature_ref` | GWFD-020353, GWFD-110312, WSFD-211009 |

### T-204 配置FUP PCC策略组

| 字段 | 值 |
|------|---|
| `task_id` | `T-204` |
| `task_name` | `配置FUP PCC策略组` |
| `task_summary` | ADD PCCPOLICYGRP将URRGROUP纳入策略组，含Monitoring-Key（业务级FUP） |
| `task_scope_type` | `feature_specific` |
| `task_goal` | 完成FUP三件套（URR→URRGROUP→PCCPOLICYGRP）的最终绑定 |
| `input_contract` | T-203 URRGROUP实例 |
| `output_contract` | PCCPOLICYGRP实例 |
| `command_refs` | `ADD PCCPOLICYGRP` |
| `status` | `active` |
| `source_evidence_ids` | `EV-FK-BW-SessionFUP`, `EV-FK-BW-ServiceFUP`, `EV-CA-01` |
| `feature_ref` | GWFD-020353, GWFD-110312, WSFD-109104, WSFD-211009 |
| `note` | TR-BW-05: FUP三件套必须按序配置（URR→URRGROUP→PCCPOLICYGRP），断裂则FUP不生效 |

### T-205 配置Gx FUP功能（UNC）

| 字段 | 值 |
|------|---|
| `task_id` | `T-205` |
| `task_name` | `配置Gx FUP功能（UNC）` |
| `task_summary` | SET PCCFUNC + MOD PCRF(UMCH) + MOD PCCPOLICYGRP(FUPSESSIONEXC)，仅Gx(2/3/4G)场景需要 |
| `task_scope_type` | `feature_specific` |
| `task_goal` | 使能UNC侧Gx接口的FUP功能，含UMCH拥塞处理和会话级FUP排除 |
| `input_contract` | DP-BW-04接口类型决策（Gx=4G场景时需要） |
| `output_contract` | Gx FUP功能使能 |
| `command_refs` | `SET PCCFUNC`, `MOD PCRF`, `MOD PCCPOLICYGRP` |
| `status` | `active` |
| `source_evidence_ids` | `EV-FK-BW-PCC-UNC`, `EV-CA-01` |
| `feature_ref` | WSFD-109104, WSFD-211009 |
| `note` | 仅Gx接口场景需要；N7(5G)场景仅需License，阈值由PCF侧umDecs配置（附录D.2） |

---

## §4 QoS专属Task（feature_specific，3个）

### T-301 配置QoS属性

| 字段 | 值 |
|------|---|
| `task_id` | `T-301` |
| `task_name` | `配置QoS属性` |
| `task_summary` | ADD QOSPROP定义QoS参数（5QI/QCI/MBR/GBR/ARP），QOSTYPE区分5G/4G |
| `task_scope_type` | `feature_specific` |
| `task_goal` | 为专有承载/QoS Flow定义QoS参数，支持GBR带宽下限保证 |
| `input_contract` | QoS需求（GBR/MBR/5QI/QCI/ARP） |
| `output_contract` | QOSPROP实例 |
| `command_refs` | `ADD QOSPROP` |
| `status` | `active` |
| `source_evidence_ids` | `EV-FK-BW-QoS-UDG`, `EV-FK-BW-QoS-UNC`, `EV-CA-01` |
| `feature_ref` | GWFD-020358, WSFD-109107 |
| `note` | TR-BW-07: QOSTYPE区分5G/4G — 5G=QOS_FLOW_PARA(用FQI)，2/3/4G=QOS_BEARER_PARA(用QCIVALUE) |

### T-302 配置专有QoS Flow空闲定时器

| 字段 | 值 |
|------|---|
| `task_id` | `T-302` |
| `task_name` | `配置专有QoS Flow空闲定时器` |
| `task_summary` | SET APNIDLETIME定义专有QoS Flow空闲释放时间（DEDQFIDLETIMER） |
| `task_scope_type` | `feature_specific` |
| `task_goal` | 避免专有QoS Flow长期空闲占用资源 |
| `input_contract` | APN名称、空闲超时时间 |
| `output_contract` | APNIDLETIME配置 |
| `command_refs` | `SET APNIDLETIME` |
| `status` | `active` |
| `source_evidence_ids` | `EV-FK-BW-QoS-UNC` |
| `feature_ref` | WSFD-109107 |

### T-303 配置去活QoS Flow策略

| 字段 | 值 |
|------|---|
| `task_id` | `T-303` |
| `task_name` | `配置去活QoS Flow策略` |
| `task_summary` | ADD APNDEACTQFPLCY定义QoS Flow去活策略（DELAY_RELEASE延迟释放） |
| `task_scope_type` | `feature_specific` |
| `task_goal` | 定义专有QoS Flow的去活行为策略 |
| `input_contract` | APN名称、去活策略类型 |
| `output_contract` | APNDEACTQFPLCY实例 |
| `command_refs` | `ADD APNDEACTQFPLCY` |
| `status` | `active` |
| `source_evidence_ids` | `EV-FK-BW-QoS-UNC` |
| `feature_ref` | WSFD-109107 |

---

## §5 ADC专属Task（feature_specific，2个）

### T-401 配置ADC参数

| 字段 | 值 |
|------|---|
| `task_id` | `T-401` |
| `task_name` | `配置ADC参数` |
| `task_summary` | ADD ADCPARA定义ADC检测参数（应用检测规则配置） |
| `task_scope_type` | `feature_specific` |
| `task_goal` | 配置ADC应用检测参数，供PCRF/PCF动态策略触发 |
| `input_contract` | 检测目标应用列表 |
| `output_contract` | ADCPARA实例 |
| `command_refs` | `ADD ADCPARA` |
| `status` | `active` |
| `source_evidence_ids` | `EV-FK-BW-ADC-UDG`, `EV-FK-BW-ADC-UNC`, `EV-CA-01` |
| `feature_ref` | GWFD-020357, WSFD-109102 |

### T-402 配置ADC三策略组

| 字段 | 值 |
|------|---|
| `task_id` | `T-402` |
| `task_name` | `配置ADC三策略组` |
| `task_summary` | ADD RULE定义Normal/Start/Stop三个策略组，触发APPLICATION_START/STOP事件 |
| `task_scope_type` | `feature_specific` |
| `task_goal` | 建立ADC完整的事件触发策略链（Normal=持续检测、Start=应用开始、Stop=应用结束） |
| `input_contract` | ADC检测目标、PCRF策略要求 |
| `output_contract` | 3个RULE实例（Normal/Start/Stop） |
| `command_refs` | `ADD RULE` |
| `status` | `active` |
| `source_evidence_ids` | `EV-FK-BW-ADC-UDG`, `EV-FK-BW-ADC-UNC`, `EV-CA-01` |
| `feature_ref` | GWFD-020357, WSFD-109102 |
| `note` | TR-BW-06: ADC必须配置Normal/Start/Stop三个策略组，缺失则ADC事件上报不完整 |

---

## §6 UNC控制面Task（feature_specific，4个）

### T-501 配置PCRF组与绑定

| 字段 | 值 |
|------|---|
| `task_id` | `T-501` |
| `task_name` | `配置PCRF组与绑定` |
| `task_summary` | ADD PCRF/PCRFGROUP/PCRFBINDGRP/SET DFTGLBPCRFGRP，建立PCRF冗余体系 |
| `task_scope_type` | `feature_specific` |
| `task_goal` | 建立UNC与PCRF/PCF的连接，支持主备/轮询/百分比冗余模式 |
| `input_contract` | PCRF/PCF地址、冗余模式 |
| `output_contract` | PCRF组与绑定配置 |
| `command_refs` | `ADD PCRF`, `ADD PCRFGROUP`, `ADD PCRFBINDGRP`, `SET DFTGLBPCRFGRP` |
| `status` | `active` |
| `source_evidence_ids` | `EV-FK-BW-PCC-UNC` |
| `feature_ref` | WSFD-109101 |

### T-502 配置PCC功能开关

| 字段 | 值 |
|------|---|
| `task_id` | `T-502` |
| `task_name` | `配置PCC功能开关` |
| `task_summary` | SET PCCFUNC全局开关 / SET APNPCCFUNC按APN开关 |
| `task_scope_type` | `feature_specific` |
| `task_goal` | 使能UNC侧PCC功能，含Gx/N7接口模式选择 |
| `input_contract` | 接口类型决策(DP-BW-04)、功能列表 |
| `output_contract` | PCC功能使能 |
| `command_refs` | `SET PCCFUNC`, `SET APNPCCFUNC` |
| `status` | `active` |
| `source_evidence_ids` | `EV-FK-BW-PCC-UNC` |
| `feature_ref` | WSFD-109101 |

### T-503 配置PCC故障与定时器

| 字段 | 值 |
|------|---|
| `task_id` | `T-503` |
| `task_name` | `配置PCC故障与定时器` |
| `task_summary` | SET PCCFAILACTION定义故障处理策略 / SET PCCTIMER定义定时器 |
| `task_scope_type` | `feature_specific` |
| `task_goal` | 配置PCC连接故障时的容灾策略和超时参数 |
| `input_contract` | 容灾需求、超时阈值 |
| `output_contract` | PCC故障处理与定时器配置 |
| `command_refs` | `SET PCCFAILACTION`, `SET PCCTIMER` |
| `status` | `active` |
| `source_evidence_ids` | `EV-FK-BW-PCC-UNC` |
| `feature_ref` | WSFD-109101 |

### T-504 配置N7属性控制

| 字段 | 值 |
|------|---|
| `task_id` | `T-504` |
| `task_name` | `配置N7属性控制` |
| `task_summary` | SET N7RCVATTRCTRL / SET N7SNDATTRCTRL，仅5G N7接口场景 |
| `task_scope_type` | `feature_specific` |
| `task_goal` | 控制N7接口接收/发送的属性映射，适配PCF的QoS参数格式 |
| `input_contract` | DP-BW-04=5G场景 |
| `output_contract` | N7属性控制配置 |
| `command_refs` | `SET N7RCVATTRCTRL`, `SET N7SNDATTRCTRL` |
| `status` | `active` |
| `source_evidence_ids` | `EV-FK-BW-PCC-UNC` |
| `feature_ref` | WSFD-109101 |
| `note` | 仅N7(5G)场景需要；Gx(2/3/4G)场景不使用 |

---

## §7 无线优化Task（feature_specific，3个）

### T-601 配置DSCP/FPI标记

| 字段 | 值 |
|------|---|
| `task_id` | `T-601` |
| `task_name` | `配置DSCP/FPI标记` |
| `task_summary` | 按业务类型映射DSCP或FPI值，通过GTP-U扩展头影响无线调度 |
| `task_scope_type` | `feature_specific` |
| `task_goal` | 标记报文优先级，引导基站进行差异化无线资源调度 |
| `input_contract` | 业务类型→标记值映射表 |
| `output_contract` | DSCP/FPI标记配置 |
| `command_refs` | （依特性定，GWFD-020359用ADD RULE配置DSCP，GWFD-110331用FPI规则） |
| `status` | `active` |
| `source_evidence_ids` | `EV-FK-BW-IM-Ctrl`, `EV-FK-BW-FPI`, `EV-CA-01` |
| `feature_ref` | GWFD-020359, GWFD-110331 |

### T-602 配置终端OS差异化

| 字段 | 值 |
|------|---|
| `task_id` | `T-602` |
| `task_name` | `配置终端OS差异化` |
| `task_summary` | SET APNOSLELBWMSW开启终端OS BWM差异化，按Android/iOS/Windows匹配不同BWM策略 |
| `task_scope_type` | `feature_specific` |
| `task_goal` | 按终端OS类型差异化带宽策略，适配不同编码格式 |
| `input_contract` | APN名称、目标终端OS类型 |
| `output_contract` | 终端OS差异化配置 |
| `command_refs` | `SET APNOSLELBWMSW` |
| `status` | `active` |
| `source_evidence_ids` | `EV-FK-BW-RateDiff` |
| `feature_ref` | GWFD-110301 |

### T-603 配置小区负荷上报

| 字段 | 值 |
|------|---|
| `task_id` | `T-603` |
| `task_name` | `配置小区负荷上报` |
| `task_summary` | SET APNREPORTATTR配置APN拥塞上报属性，小区负荷等级变化时触发PCRF策略调整 |
| `task_scope_type` | `feature_specific` |
| `task_goal` | 使能小区负荷感知上报，触发PCRF/PCF动态带宽策略 |
| `input_contract` | APN名称、上报属性配置 |
| `output_contract` | APNREPORTATTR配置 |
| `command_refs` | `SET APNREPORTATTR` |
| `status` | `active` |
| `source_evidence_ids` | `EV-FK-BW-CellLoad-UDG`, `EV-FK-BW-CellLoad-UNC`, `EV-CA-01` |
| `feature_ref` | GWFD-110332, WSFD-211101 |

---

## §8 TaskRule（任务级规则，6条）

| `rule_id` | `rule_name` | `rule_type` | `applies_to` | `rule_logic` | `severity` |
|-----------|-------------|-------------|--------------|--------------|------------|
| `TR-BW-01` | REFRESHSRV时序约束 | `dependency_rule` | T-006 | SET REFRESHSRV必须在所有BWM/FILTER/策略配置之后执行；执行后约60秒生效（PROTBINDFLOWF定时器） | critical |
| `TR-BW-02` | BWMSERVICE→BWMCONTROLLER前置 | `dependency_rule` | T-102, T-103 | 必须先ADD BWMSERVICE再ADD BWMCONTROLLER，BWMRULE引用两者 | critical |
| `TR-BW-03` | URR→URRGROUP→PCCPOLICYGRP三件套链 | `dependency_rule` | T-202, T-203, T-204 | FUP三件套必须按序配置：ADD URR→ADD URRGROUP→ADD PCCPOLICYGRP，断裂则FUP不生效 | critical |
| `TR-BW-04` | QoS URR模式校验 | `validation_rule` | T-202 | QoS保证场景URR.USAGERPTMODE必须为QOS；FUP场景为ONLINE/MONITORINGKEY；不可混用 | critical |
| `TR-BW-05` | ADC三策略组完整性 | `validation_rule` | T-402 | ADC必须配置Normal/Start/Stop三个策略组（EVENT-TRIGGER=APPLICATION_START/STOP），缺失则ADC事件上报不完整 | warning |
| `TR-BW-06` | 预定义规则全网一致性前置 | `consistency_rule` | T-003 | 预定义规则RULENAME在PCF/SMF/UPF三侧必须同名同参（BWM/ADC/QoS/业务FUP均要求）；PCC类型RULENAME不能与QOS类型RULENAME同名 | critical |

> **规则溯源**：
> - TR-BW-01 ← 发现五（SET REFRESHSRV是隐藏的关键配置点）
> - TR-BW-02 ← 附录D.1 BWM端到端配置链路第2步
> - TR-BW-03 ← 附录D.2 FUP端到端配置链路
> - TR-BW-04 ← 发现二（URR的多种用途模式），附录C
> - TR-BW-05 ← 附录B ADC命令交叉参考
> - TR-BW-06 ← 发现七（预定义规则名全网一致性要求），发现一（POLICYTYPE约束）

---

## §9 TaskCommandOrderEdge（Task内部命令顺序）

来源：`cross-feature-analysis.md` 附录D端到端配置流程。

### 9.1 T-005 标准绑定链（用户模板组与APN绑定）

| `edge_id` | `task_ref` | `from_command_ref` | `to_command_ref` | `relation_type` | `requiredness` | `propagated_context` | `source_evidence_ids` |
|-----------|------------|--------------------|--------------------|-----------------|----------------|---------------------|----------------------|
| `TE-005-1` | T-005 | `ADD USERPROFILE` | `ADD RULEBINDING` | `precedes` | `required` | `UPNAME` | `EV-CA-01` |
| `TE-005-2` | T-005 | `ADD RULEBINDING` | `ADD USRPROFGROUP` | `precedes` | `required` | `UPNAME→UPGNAME` | `EV-CA-01` |
| `TE-005-3` | T-005 | `ADD USRPROFGROUP` | `ADD UPBINDUPG` | `precedes` | `required` | `UPGNAME` | `EV-CA-01` |
| `TE-005-4` | T-005 | `ADD UPBINDUPG` | `ADD APNUSRPROFG` | `precedes` | `required` | `UPGNAME→APNNAME` | `EV-CA-01` |

### 9.2 T-204 FUP三件套链（PCC策略组）

| `edge_id` | `task_ref` | `from_command_ref` | `to_command_ref` | `relation_type` | `requiredness` | `propagated_context` | `source_evidence_ids` |
|-----------|------------|--------------------|--------------------|-----------------|----------------|---------------------|----------------------|
| `TE-204-1` | T-204 | `ADD URR` | `ADD URRGROUP` | `precedes` | `required` | `URRID → URRGROUP.UPURRNAME1` | `EV-FK-BW-SessionFUP`, `EV-CA-01` |
| `TE-204-2` | T-204 | `ADD URRGROUP` | `ADD PCCPOLICYGRP` | `precedes` | `required` | `URRGROUPNAME → PCCPOLICYGRP` | `EV-FK-BW-SessionFUP`, `EV-CA-01` |

### 9.3 T-103 BWM控制器（独立配置）

T-103（配置BWM控制器）为单命令task，无内部命令顺序依赖。BWMCONTROLLER配置独立，参数由DP-BW-05决定CTRLTYPE（CAR/SHAPING）后映射不同参数集。

### 9.4 T-107 智能Shaping ServiceLevel链

| `edge_id` | `task_ref` | `from_command_ref` | `to_command_ref` | `relation_type` | `requiredness` | `propagated_context` | `source_evidence_ids` |
|-----------|------------|--------------------|--------------------|-----------------|----------------|---------------------|----------------------|
| `TE-107-1` | T-107 | `ADD BWMCONTROLLER` | `ADD BCSRVLEVELPLY` | `depends_on` | `required` | `BWMCNAME → SERVICELEVEL` | `EV-FK-BW-SmartShaping` |

> 智能Shaping需先配置BWMCONTROLLER（WORKMODE=AUTO/MANUAL），再为每个ServiceLevel配置BCSRVLEVELPLY的SHAPRATE比例。参见附录D.4组级智能Shaping配置链路。

### 9.5 T-501 PCRF组与绑定链

| `edge_id` | `task_ref` | `from_command_ref` | `to_command_ref` | `relation_type` | `requiredness` | `propagated_context` | `source_evidence_ids` |
|-----------|------------|--------------------|--------------------|-----------------|----------------|---------------------|----------------------|
| `TE-501-1` | T-501 | `ADD PCRF` | `ADD PCRFGROUP` | `precedes` | `required` | `PCRFID → PCRFGROUP` | `EV-FK-BW-PCC-UNC` |
| `TE-501-2` | T-501 | `ADD PCRFGROUP` | `ADD PCRFBINDGRP` | `precedes` | `required` | `PCRFGROUPNAME → PCRFBINDGRP` | `EV-FK-BW-PCC-UNC` |
| `TE-501-3` | T-501 | `ADD PCRFBINDGRP` | `SET DFTGLBPCRFGRP` | `precedes` | `optional` | `PCRFGROUPNAME` | `EV-FK-BW-PCC-UNC` |

### 9.6 T-003 PCC规则（内部链）

| `edge_id` | `task_ref` | `from_command_ref` | `to_command_ref` | `relation_type` | `requiredness` | `propagated_context` | `source_evidence_ids` |
|-----------|------------|--------------------|--------------------|-----------------|----------------|---------------------|----------------------|
| `TE-003-1` | T-003 | `ADD FLOWFILTER` | `ADD RULE` | `precedes` | `required` | `FLOWFILTERNAME → RULE` | `EV-CA-01` |
| `TE-003-2` | T-003 | `ADD PCCPOLICYGRP` | `ADD RULE` | `precedes` | `required` | `PCCPOLICYGRPNAME → RULE.POLICYNAME` | `EV-CA-01` |

### 9.7 T-102~T-106 BWM三级控制链（跨Task，附录D.1）

> 以下边表示BWM三级控制体系内部的命令依赖顺序，跨多个Task但在同一BWM配置流程中：

| `edge_id` | `task_ref` | `from_command_ref` | `to_command_ref` | `relation_type` | `requiredness` | `propagated_context` | `source_evidence_ids` |
|-----------|------------|--------------------|--------------------|-----------------|----------------|---------------------|----------------------|
| `TE-BWM-1` | T-102→T-103 | `ADD BWMSERVICE` | `ADD BWMCONTROLLER` | `precedes` | `required` | `BWMSERVICENAME` | `EV-FK-BW-BWM`, `EV-CA-01` |
| `TE-BWM-2` | T-103→T-105 | `ADD BWMCONTROLLER` | `ADD BWMRULE` | `precedes` | `required` | `BWMCNAME → BWMRULE.UPBWMCTRLNAME1` | `EV-FK-BW-BWM`, `EV-CA-01` |
| `TE-BWM-3` | T-104→T-105 | `ADD BWMUSERGROUP` | `ADD BWMRULE` | `precedes` | `required` | `USERGROUPNAME` | `EV-FK-BW-BWM` |
| `TE-BWM-4` | T-104→T-106 | `ADD BWMUSERGROUP` | `ADD APNBINDBWMUSRG` | `precedes` | `required` | `USERGROUPNAME → APNNAME` | `EV-FK-BW-BWM` |

---

## §10 ConfigTask适用矩阵（Task × Feature）

> ★ = primary（主属特性，Task在此特性下定义）
> ☆ = optional（可选复用，特性可选用此Task）
> — = 不适用

| Task | SA-Basic 110101 | PCC-UDG 020351 | BWM 110311 | SmartShaping 110313 | SessionFUP 020353 | ServiceFUP 110312 | Shaping 020354 | QoS-UDG 020358 | ADC-UDG 020357 | Anomaly 020305 | IM-Ctrl 020359 | RateDiff 110301 | Video 110302 | FPI 110331 | CellLoad-UDG 110332 | SA-Mgmt 111600 | PCC-UNC 109101 | BWM-UNC 211005 | SessionFUP-UNC 109104 | ServiceFUP-UNC 211009 | QoS-UNC 109107 | ADC-UNC 109102 | APN-Policy 109108 | CellLoad-UNC 211101 |
|------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| T-001 | ★ | ☆ | ★ | ☆ | — | ★ | ☆ | ☆ | ☆ | — | ☆ | ☆ | ☆ | ☆ | — | ☆ | — | ☆ | — | ☆ | ☆ | ☆ | — | — |
| T-002 | ★ | ★ | ☆ | ☆ | — | — | ☆ | ☆ | ☆ | — | — | — | — | — | — | — | — | — | — | — | ☆ | ★ | — | — |
| T-003 | ☆ | ★ | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ | — | ★ | ★ | ★ | ★ | ★ | ★ | ☆ | ☆ |
| T-004 | ☆ | ★ | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ | ☆ | — | ★ | ★ | ★ | ★ | ★ | ★ | — | — |
| T-005 | — | ☆ | — | — | — | — | — | ☆ | — | — | — | ☆ | — | — | — | — | — | ★ | — | ★ | ★ | ★ | — | — |
| T-006 | — | ★ | ★ | ★ | — | — | ★ | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| T-007 | ★ | ★ | ★ | ★ | ★ | ★ | ★ | ★ | ★ | ★ | ★ | ★ | ★ | ★ | ★ | ★ | ★ | ★ | ★ | ★ | ★ | ★ | ★ | ★ |
| T-008 | ★ | — | — | — | — | — | — | — | — | — | — | — | — | — | — | ★ | — | — | — | — | — | — | — | — |
| T-101 | — | — | ★ | ☆ | — | — | — | — | — | — | — | — | — | — | — | — | — | ☆ | — | — | — | — | — | — |
| T-102 | — | — | ★ | ☆ | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| T-103 | — | — | ★ | ★ | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| T-104 | — | — | ★ | ★ | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| T-105 | — | — | ★ | ★ | — | — | ★ | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| T-106 | — | — | ★ | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| T-107 | — | — | — | ★ | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| T-201 | — | — | — | — | ★ | ★ | — | — | — | — | — | — | — | — | — | — | — | — | ★ | ★ | — | — | — | — |
| T-202 | — | — | — | — | ★ | ★ | — | ☆ | — | — | — | — | — | — | — | — | — | — | ★ | ★ | ★ | — | — | — |
| T-203 | — | — | — | — | ★ | ★ | — | — | — | — | — | — | — | — | — | — | — | — | — | ★ | — | — | — | — |
| T-204 | — | — | — | — | ★ | ★ | — | — | — | — | — | — | — | — | — | — | — | — | ★ | ★ | ★ | — | — | — |
| T-205 | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | ★ | ★ | — | — | — | — |
| T-301 | — | — | — | — | — | — | — | ★ | — | — | — | — | ★ | — | — | — | — | — | — | — | ★ | — | — | — |
| T-302 | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | ★ | — | — | — |
| T-303 | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | ★ | — | — | — |
| T-401 | — | — | — | — | — | — | — | — | ★ | — | — | — | — | — | — | — | — | — | — | — | — | ★ | — | — |
| T-402 | — | — | — | — | — | — | — | — | ★ | — | — | — | — | — | — | — | — | — | — | — | — | ★ | — | — |
| T-501 | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | ★ | ★ | ★ | ★ | ★ | ★ | ★ | ★ |
| T-502 | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | ★ | — | ★ | ★ | — | — | — | — |
| T-503 | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | ★ | — | — | — | — | — | — | — |
| T-504 | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | ★ | — | — | — | — | — | — | — |
| T-601 | — | — | — | — | — | — | — | — | — | — | ★ | — | — | ★ | — | — | — | — | — | — | — | — | — | — |
| T-602 | — | — | — | — | — | — | — | — | — | — | — | ★ | — | — | — | — | — | — | — | — | — | — | — | — |
| T-603 | — | — | — | — | — | — | — | — | — | — | — | — | — | — | ★ | — | — | — | — | — | — | — | — | ★ |

---

## §11 与计费场景任务层的对比

| 维度 | 计费场景 | 带宽控制场景 |
|------|---------|------------|
| 通用Task数 | 8（T-001~T-008） | 8（T-001~T-008） |
| 特性专属Task数 | 19（T-101~T-311） | 24（T-101~T-603） |
| TaskRule数 | 6（TR-CH-01~TR-CH-06） | 6（TR-BW-01~TR-BW-06） |
| **共享通用Task** | T-001(分类), T-002(流过滤), T-003(PCC规则), T-004(用户模板), T-005(APN绑定), T-006(刷新), T-007(License) | 同左，但T-008不同（计费=协议绑定，带宽=SA特征库加载） |
| **独有Task族** | 计费三件套(T-006 URR/URRGROUP), 在线计费(T-201~T-204), 融合计费(T-301~T-311), CG接口(T-311) | BWM三级控制(T-101~T-107), FUP三件套(T-201~T-205), QoS/GBR(T-301~T-303), ADC(T-401~T-402), UNC控制面(T-501~T-504), 无线优化(T-601~T-603) |
| **核心差异** | URR用于差异化计费（费率组/计量方式） | URR用于流量阈值监控（FUP降速/QoS事件上报），BWM用于限速整形 |
| **POLICYTYPE** | CHARGING（计费场景固定） | BWM/PCC/QOS/ADC（按策略类型分支） |
| **跨场景复用点** | — | T-003(PCC规则)通过POLICYTYPE区分场景；T-202(URR)跨FUP/QoS复用；T-005(APN绑定)跨全部UNC特性 |

---

## §12 对象计数汇总

| 对象类型 | 数量 | 编号范围 |
|---------|------|---------|
| ConfigTask（generic） | 8 | T-001~T-008 |
| ConfigTask（BWM专属） | 7 | T-101~T-107 |
| ConfigTask（FUP专属） | 5 | T-201~T-205 |
| ConfigTask（QoS专属） | 3 | T-301~T-303 |
| ConfigTask（ADC专属） | 2 | T-401~T-402 |
| ConfigTask（UNC控制面） | 4 | T-501~T-504 |
| ConfigTask（无线优化） | 3 | T-601~T-603 |
| **ConfigTask合计** | **32** | — |
| TaskRule | 6 | TR-BW-01~TR-BW-06 |
| TaskCommandOrderEdge | 16 | TE-005(4) + TE-204(2) + TE-107(1) + TE-501(3) + TE-003(2) + TE-BWM(4) |
| **任务层对象总计** | **54** | — |

---

> 本文件为带宽控制场景三层图谱第3层。第4层命令图谱、第5层跨层映射、第6层证据索引见同目录其他文件。
