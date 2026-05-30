# 业务图谱最终 Schema 定义

## 文件说明

本文件基于 `03-schema-design.md` 的分析和决策（D1-D8），定义业务层四个主链对象的最终 schema。

每个对象包含两部分：
1. **Schema 定义**：属性、边、约束
2. **业务感知域实例**：具体实例化内容 + 原始文档证据链

## 已确认的决策（D1-D8 汇总）

| 编号 | 决策 |
|------|------|
| D1 | NS 采用 4 个粗粒度（计费/带宽控制/访问限制/本地分流），CSV 中 6 个细粒度条目降级为 DS 子标签 |
| D2 | "行为分析"不恢复为独立 NS，其知识分布在其他 NS 的扩展子场景中 |
| D3 | DS-02 合并到 DS-01，作为 DS-01 的 DecisionPoint 分支。DS 从 5 个变为 4 个 |
| D4 | 交叉覆盖不用 primary/cross-cutting，改用 dependency_type（required/optional/none） |
| D5 | EngineeringTask 增加 phase 字段（plan/execute/verify） |
| D6 | 不构建 ProcedureStep；特性图谱保留 `Feature → ProcedureVariant → ConfigStep`，业务图谱中的 execute Task 在需要时映射到 ConfigStep |
| D7 | BD 不增加 Participant/DSO/Evidence 边；进一步精简：删除 core_mechanism/cp_up_split/product_structure（与 Participant/DS/DSO 重复），删除 app_scopes（与 NS 职责重叠） |
| D8 | ~~BD 保留 app_scopes 字段~~ → 已修订：app_scopes 删除，NS 的 positioning_source 字段同步删除（无溯源对象）；domain_id 不绑定产品缩写（域可能跨多产品） |

## 主链结构

```
BusinessDomain ──contains──> NetworkScenario ──instantiated_as──> DeliverySolution ──decomposes_to──> EngineeringTask
```

DS 数量：4 个（DS-01 含配额分支、DS-02 访问限制、DS-03 带宽控制、DS-04 本地分流）
NS 数量：4 个（计费、带宽控制、访问限制、本地分流）

---

## 1. BusinessDomain（业务域）

### 1.1 Schema 定义

**定位**：图谱的轻量根节点，只做一件事——限定讨论边界，指向它包含的现网场景。

**属性**：

| 字段 | 类型 | 必选 | 说明 |
|------|------|------|------|
| domain_id | string | 是 | 唯一标识，语义化命名，不绑定产品缩写（一个域可能跨多个产品） |
| domain_name | string | 是 | 域名称 |
| domain_summary | string | 是 | 一句话定义 |
| status | string | 是 | 数据状态 |

**边**：

```
BusinessDomain --contains--> NetworkScenario
```

> **精简依据**（修订 D7/D8）：
> - ~~core_mechanism~~：域的骨架信息从 `BD→NS→DS` 链路可推导，DSO/DS 承载了具体机制组合
> - ~~app_scopes~~：与 NS 职责重叠，NS 的 scenario_name/summary 已覆盖语义检索入口
> - ~~cp_up_split~~、~~product_structure~~：与 Participant 对象重复，参与方信息由 Participant 承载
> - domain_id 不绑定产品缩写，因为业务感知域同时涉及 UDG（用户面）和 UNC（控制面）

### 1.2 业务感知域实例

| 字段 | 值 |
|------|-----|
| domain_id | `service-awareness` |
| domain_name | 业务感知 |
| domain_summary | 在用户会话过程中，对用户的数据报文进行解析，从而区分出用户使用的不同业务，以实现策略控制和计费控制 |
| status | accepted |

### 1.3 证据链

| 字段 | 证据来源 | 关键引用 |
|------|---------|---------|
| domain_id | 语义构造 | 不绑定产品缩写，业务感知域跨 UDG + UNC 两个产品 |
| domain_name | 业务感知定义_92407879.md | "业务感知（Service Awareness，简称SA）" |
| domain_summary | 业务感知定义_92407879.md | "是指在用户会话过程中，对用户的数据报文进行解析，从而区分出用户使用的不同业务。" |

---

## 2. NetworkScenario（现网场景）

### 2.1 Schema 定义

**属性**：

| 字段 | 类型 | 必选 | 说明 |
|------|------|------|------|
| scenario_id | string | 是 | 唯一标识 |
| scenario_name | string | 是 | 场景名称 |
| scenario_summary | string | 是 | 一句话描述 |
| judgment_basis | string | 是 | 判断基础：什么情况下属于该场景 |
| typical_outcome | string | 是 | 典型结果 |
| source_evidence_ids | list[string] | 是 | 证据来源 |
| status | string | 是 | 数据状态 |

**边**：

```
BusinessDomain --contains--> NetworkScenario
NetworkScenario --instantiated_as--> DeliverySolution
  属性: dependency_type (required/optional/none)
NetworkScenario --uses_semantic_object--> DomainSemanticObject
```

> 决策依据：D1（4 个粗粒度）、D2（行为分析不恢复）、D4（dependency_type）

### 2.2 NS-01 计费场景

| 字段 | 值 |
|------|-----|
| scenario_id | NS-01 |
| scenario_name | 计费场景 |
| scenario_summary | 对不同业务流采用不同计费方式，结合默认计费、免费业务和配额动作完成计费闭环 |
| judgment_basis | 用户访问了可识别的业务流，或会话需要按规则进入默认计费、免费业务或配额处理 |
| typical_outcome | 专项业务单独计费、免费业务不计费、普通业务默认计费，必要时额度变化后切换到重定向或其他处理路径 |
| status | active |

| 字段 | 证据来源 | 关键引用 |
|------|---------|---------|
| judgment_basis | final_v2 Section 8.1 | "用户访问了可识别的业务流，或会话需要按规则进入默认计费、免费业务或配额处理" |

### 2.3 NS-02 带宽控制场景

| 字段 | 值 |
|------|-----|
| scenario_id | NS-02 |
| scenario_name | 带宽控制场景 |
| scenario_summary | 对不同业务、用户或范围域施加差异化带宽控制，落实到QoS策略和QoS Flow |
| judgment_basis | 识别出特定业务、用户属性、时段或TOS，或根据签约/位置等条件生成不同SM策略 |
| typical_outcome | 某类业务限速、保障优先级、整形、映射到不同QoS Flow，获得差异化体验 |
| status | active |

| 字段 | 证据来源 | 关键引用 |
|------|---------|---------|
| judgment_basis | 套餐2_94838085.md 操作场景 | "运营商需要布置带宽控制相关的业务套餐" |

### 2.4 NS-03 访问限制场景

| 字段 | 值 |
|------|-----|
| scenario_id | NS-03 |
| scenario_name | 访问限制场景 |
| scenario_summary | 对指定业务流实施阻塞、重定向、头增强或Portal处理 |
| judgment_basis | 三四层、协议、七层条件命中，或命中导向类规则 |
| typical_outcome | 业务被阻塞、被重定向到目标地址、被附加头增强，或进入Portal处理路径 |
| status | active |

| 字段 | 证据来源 | 关键引用 |
|------|---------|---------|
| judgment_basis | 套餐3_94838086.md 操作场景 | "运营商需要布置对用户访问进行管控的业务套餐" |

### 2.5 NS-04 本地分流场景

| 字段 | 值 |
|------|-----|
| scenario_id | NS-04 |
| scenario_name | 本地分流场景 |
| scenario_summary | 将访问本地业务的数据导向本地DN/边缘DN，必要时公网/专网独立计费 |
| judgment_basis | 满足DNN、位置、PRA、DNAI、selectedDnn、预定义规则或动态规则等分流触发条件 |
| typical_outcome | UL CL/辅锚点分流，导向本地DN/边缘DN，公网/专网分别计量 |
| status | active |

| 字段 | 证据来源 | 关键引用 |
|------|---------|---------|
| judgment_basis | How分流_58273329.md | 策略来源含 PCF下发/SMF下发/PCF经SMF下发/MPF下发四种，分流条件为 DNN/位置/PRA/DNAI |

---

## 3. DeliverySolution（交付方案）

### 3.1 Schema 定义

**属性**：

| 字段 | 类型 | 必选 | 说明 |
|------|------|------|------|
| solution_id | string | 是 | 唯一标识 |
| solution_name | string | 是 | 方案名称 |
| solution_summary | string | 是 | 一句话描述，概括方案闭包核心 |
| core_mechanism_combo | string | 是 | 核心机制组合——方案区别于场景名称的关键差异化信息 |
| source_evidence_ids | list[string] | 是 | 证据来源文档ID列表 |
| status | string | 是 | 数据状态 |

**边**：

```
NetworkScenario --instantiated_as--> DeliverySolution
  属性: dependency_type (required/optional/none)
DeliverySolution --uses_task--> EngineeringTask (M:N)
DeliverySolution --involves--> Participant
DeliverySolution --applies_to--> Scope
DeliverySolution --has_decision--> DecisionPoint
DeliverySolution --has_runtime_flow--> RuntimeFlow
DeliverySolution --validated_by--> ValidationPlan
DeliverySolution --diagnosed_by--> DiagnosisRule
DeliverySolution --constrained_by--> RiskConstraint
DeliverySolution --instantiates_semantic_object--> DomainSemanticObject
DeliverySolution --requires_capability--> Feature
DeliverySolution --supported_by--> Evidence
```

> 决策依据：D3（DS-02合并为DS-01的DecisionPoint分支）、D4（dependency_type替代primary/cross-cutting）、D6（不构建 ProcedureStep，Task 与特性图谱 ConfigStep 按需映射）

### 3.2 DS-01 差异化计费组合方案（含配额分支）

| 字段 | 值 |
|------|-----|
| solution_id | DS-01 |
| solution_name | 差异化计费组合方案（含配额分支） |
| solution_summary | 通过过滤条件识别业务流，按优先级裁决Rule，绑定PCC/URR计费链实现差异化计费、免费业务与默认计费，并在配额耗尽后通过DecisionPoint切换用户体验 |
| core_mechanism_combo | 过滤条件(IPLIST/FILTER/L7FILTER/FLOWFILTER) + Rule优先级裁决 + PCC/URR计费链(PCCPOLICYGRP-URRGROUP-URR) + 默认URR组兜底 + Trigger驱动计费会话更新 + 配额耗尽动作切换(BLOCK/REDIRECT/FORWARD) |
| source_evidence_ids | ["套餐1_93112148", "计费解决方案概述_90776649", "融合计费概述_42995681"] |
| status | active |

**证据链**：

| 字段 | 证据来源 | 关键引用 |
|------|---------|---------|
| core_mechanism_combo（过滤条件+Rule+PCC/URR链） | 套餐1_93112148.md 脚本段 | IPLIST→FILTER/L7FILTER→FLOWFILTER→RULE(POLICYTYPE=PCC,PRIORITY=100/200/300/400)→PCCPOLICYGRP(绑URRGROUP)→URR(OFFLINE/FREE)→USERPROFILE→RULEBINDING |
| core_mechanism_combo（默认URR组兜底） | 套餐1_93112148.md 脚本段 | "SET URRGRPBINDING: USERPROFILENAME='up_charging',DFTURRGRPNAME='urrgD',DFTSIGURRGNAME='urrgD'"——业务4作为兜底策略配置默认URR组 |
| core_mechanism_combo（Trigger+配额） | 融合计费概述_42995681.md 表1 | SMF："对在线计费业务进行配额监控"；CHF："提供重授权触发条件"；UPF："按规则上报采集的计费信息" |
| solution_summary（配额分支） | 计费解决方案概述_90776649.md | "在线计费：进行配额管理...在配额不足时，SMF可以停止业务使用"——配额耗尽后动作切换是计费闭环的有机组成部分 |

> **配额分支说明**：原 DS-02（配额耗尽后体验切换方案）按 D3 决策合并为本方案的 DecisionPoint 分支。配额耗尽后的 BLOCK/REDIRECT/FORWARD 选择不再是独立方案，而是差异化计费方案内部的决策分支。

### 3.3 DS-02 访问限制组合方案

| 字段 | 值 |
|------|-----|
| solution_id | DS-02 |
| solution_name | 访问限制组合方案 |
| solution_summary | 通过过滤条件识别目标业务流，按Rule裁决命中后执行阻塞、头增强、IP重定向或URL重定向等处理路径，实现多维访问管控 |
| core_mechanism_combo | 过滤条件(FILTER/L7FILTER/FLOWFILTER) + Rule裁决 + 多策略类型处理路径(PCC阻塞/HEADEN头增强/IPREDIR重定向/PCC重定向) + 优先级控制(高优先级Rule优先匹配) |
| source_evidence_ids | ["套餐3_94838086"] |
| status | active |

**证据链**：

| 字段 | 证据来源 | 关键引用 |
|------|---------|---------|
| core_mechanism_combo（多策略类型处理路径） | 套餐3_94838086.md 数据表 | 业务1(PCC阻塞)、业务2(HEADEN插入MSISDN+防欺诈)、业务3(IPREDIR重定向至10.100.111.222)、业务4(PCC重定向至www.huawei.com)——四种策略类型并存 |
| core_mechanism_combo（过滤条件+Rule裁决） | 套餐3_94838086.md 脚本段 | ADD FILTER→ADD L7FILTER→ADD FLOWFILTER→ADD RULE(POLICYTYPE=PCC/HEADEN/IPREDIR)→ADD USERPROFILE→ADD RULEBINDING |

### 3.4 DS-03 带宽控制与QoS编排方案

| 字段 | 值 |
|------|-----|
| solution_id | DS-03 |
| solution_name | 带宽控制与QoS编排方案 |
| solution_summary | 通过过滤条件识别业务流，绑定BWM带宽控制策略实现限速/保障/整形，必要时与QoS Flow映射结合实现端到端体验保障 |
| core_mechanism_combo | 过滤条件(FILTER/L7FILTER/FLOWFILTER) + BWM带宽控制策略(CATEGORYPROP→BWMSERVICE→BWMCONTROLLER) + Rule优先级 + 例外黑名单(BLACKLISTRULE) + QoS Flow映射（静态/动态规则） + 端到端QoS编排(PCF→SMF→UPF/RAN/UE) |
| source_evidence_ids | ["套餐2_94838085"] |
| status | active |

**证据链**：

| 字段 | 证据来源 | 关键引用 |
|------|---------|---------|
| core_mechanism_combo（BWM策略链） | 套餐2_94838085.md 脚本段 | ADD CATEGORYPROP→ADD BWMSERVICE(NONTOS, CATEGORY_PROP)→ADD BWMCONTROLLER(CIR=10240/PIR=8192/RATE=10240)→ADD BWMUSERGROUP→ADD BWMRULE→ADD RULE(POLICYTYPE=BWM) |
| core_mechanism_combo（例外黑名单） | 套餐2_94838085.md 脚本段 | "ADD BLACKLISTRULE:RULENAME='ruleC1',POLICYTYPE=BWM,FILTERINGMODE=FLOWFILTER,FLOWFILTERNAME='flowfilterC1'"——业务3的例外情况通过黑名单排除 |
| core_mechanism_combo（QoS Flow映射） | final_v2 Section 15 | "NS-02会在'执行通路建立'阶段展开成QoS Flow建立、PFS/QFI映射和PCF/SMF发起更新" |

### 3.5 DS-04 本地分流与独立计费方案

| 字段 | 值 |
|------|-----|
| solution_id | DS-04 |
| solution_name | 本地分流与独立计费方案 |
| solution_summary | 在满足分流触发条件时，通过UL CL/辅锚点UPF将业务流导向本地DN/边缘DN，主/辅锚点各自独立执行计费，实现公网/专网会话分离计量与计费 |
| core_mechanism_combo | 分流策略来源(PCF下发/SMF下发/PCF经SMF下发/MPF下发) + UL CL/辅锚点UPF选择与插入 + 会话修改(UE-基站-ULCL-主/辅锚点) + 本地DN导向 + 主/辅锚点独立计费(各UPF独享配额) |
| source_evidence_ids | ["How分流_58273329", "MEC计费流程_52284255", "GWFD-020531特性概述_57047936"] |
| status | active |

**证据链**：

| 字段 | 证据来源 | 关键引用 |
|------|---------|---------|
| core_mechanism_combo（分流策略来源） | How分流_58273329.md 分流策略来源段 | 四种策略来源："1. PCF下发策略...2. SMF下发策略...3. PCF经过SMF下发策略...4. MPF下发策略" |
| core_mechanism_combo（UL CL/辅锚点选择） | How分流_58273329.md UPF选择与插入表 | 主锚点(用户激活时/DNN+切片+位置)、UL CL(触发分流时/是否支持UL CL+切片+位置)、辅锚点(触发分流时/DNAI+DNN+切片+位置) |
| core_mechanism_combo（会话修改） | How分流_58273329.md 分流的流程Step4 | "将原有的UE-基站-主锚点UPF之间的常规PDU会话，更新为UE-基站-UL CL UPF-主锚点UPF/辅锚点UPF之间的分流PDU会话" |
| core_mechanism_combo（独立计费） | MEC计费流程_52284255.md 计费流程段 | "SMF按UPF向CHF申请配额（消息中Multiple Unit Usage字段携带UPF ID），哪个UPF申请就向哪个UPF下发配额"——每个UPF独享配额 |

> **交叉覆盖说明**：DS-04 同时覆盖 NS-04（本地分流）和 NS-01（计费），且两者均为 required。这反映了本地分流场景中独立计费是方案的有机组成部分，而非可选增强。按 D4 决策，使用 dependency_type 表达而非 primary/cross-cutting 标签。

---

## 4. EngineeringTask（工程任务）

### 4.1 Schema 定义

**定位**：原子动作单元，可被多个 DS 或 Feature 复用。不再绑定单一 DS。Task 不是“配置步骤”的同义词，而是覆盖 `plan / execute / verify` 三类工程动作的更高层单元；其中只有 execute 类 Task 才会在需要时下沉到特性图谱中的 `ConfigStep`。

**属性**：

| 字段 | 类型 | 必选 | 说明 |
|------|------|------|------|
| task_id | string | 是 | 唯一标识 |
| task_name | string | 是 | 任务名称 |
| task_summary | string | 是 | 一句话描述 |
| phase | string | 是 | 阶段：plan / execute / verify |
| input_artifacts | list[string] | 是 | 需要的输入 |
| output_artifacts | list[string] | 是 | 产出的输出 |
| command | string | 否 | 命令示例（`ADD`/`SET`/`LST`/`DSP`，plan 阶段为 `-`） |
| config_object | string | 否 | 涉及的配置对象（plan 阶段为 `-`） |
| source_evidence_ids | list[string] | 是 | 证据来源文档 ID 列表 |
| status | string | 是 | 数据状态 |

**边**：

```
DeliverySolution --uses_task--> EngineeringTask (M:N)
Feature --contains--> EngineeringTask (M:N，后续Feature定义时启用)
EngineeringTask --creates_config--> ConfigObject (execute phase)
EngineeringTask --verifies_config--> ConfigObject (verify phase)
EngineeringTask --realized_by_config_step--> ConfigStep (0:N, execute phase，可选)
EngineeringTask --supported_by--> Evidence
```

> 决策依据：D5（phase 字段）、D6（Task 不等于配置步骤；特性图谱保留 `ProcedureVariant → ConfigStep`，业务 execute Task 在需要时映射到 `ConfigStep`）、M:N 共享模型（Task 是原子单元，可被 DS 和 Feature 复用）

### 4.2 方案到任务的映射表

#### 共享任务（多个 DS 共用）

| 原子 Task ID | Task 名称 | phase | 涉及 ConfigObject | DS-01 | DS-02 | DS-03 | DS-04 |
|-------------|-----------|-------|-------------------|-------|-------|-------|-------|
| T-PLAN-001 | 规划生效范围 | plan | - | ✓ | ✓ | ✓ | ✓ |
| T-PLAN-002 | 规划识别条件 | plan | - | ✓ | ✓ | ✓ | ✓ |
| T-PLAN-003 | 规划 Rule 与优先级 | plan | - | ✓ | ✓ | ✓ | ✓ |
| T-EXEC-001 | 配置 IP 地址列表 | execute | IPLIST | ✓ | - | - | - |
| T-EXEC-002 | 配置三四层过滤条件 | execute | FILTER | ✓ | ✓ | ✓ | - |
| T-EXEC-003 | 配置七层过滤条件 | execute | L7FILTER | ✓ | ✓ | ✓ | - |
| T-EXEC-004 | 配置流过滤器与绑定 | execute | FLOWFILTER, FLTBINDFLOWF, PROTBINDFLOWF | ✓ | ✓ | ✓ | - |
| T-EXEC-008 | 配置 Rule | execute | RULE | ✓ | ✓ | ✓ | - |
| T-EXEC-010 | 配置 UserProfile 与 Rule 绑定 | execute | USERPROFILE, RULEBINDING, REFRESHSRV | ✓ | ✓ | ✓ | - |

#### 方案特有任务

| 原子 Task ID | Task 名称 | phase | 涉及 ConfigObject | 所属 DS |
|-------------|-----------|-------|-------------------|---------|
| T-PLAN-004 | 规划计费对象与费率标识 | plan | - | DS-01 |
| T-PLAN-005 | 规划配额耗尽动作 | plan | - | DS-01 |
| T-PLAN-006 | 规划导向与增强动作 | plan | - | DS-02 |
| T-PLAN-007 | 规划 BWM 策略 | plan | - | DS-03 |
| T-PLAN-008 | 规划分流触发与锚点插入 | plan | - | DS-04 |
| T-PLAN-009 | 规划计费 Trigger 与多 UPF 配额 | plan | - | DS-04 |
| T-EXEC-005 | 配置计费动作链 | execute | URR, URRGROUP, PCCPOLICYGRP | DS-01 |
| T-EXEC-006 | 配置策略动作链 | execute | PCCACTIONPROP, HEADEN, REDIRECT, PCCPOLICYGRP | DS-02 |
| T-EXEC-007 | 配置 BWM 带宽控制链 | execute | CATEGORYPROP, BWMSERVICE, BWMCONTROLLER, BWMUSERGROUP, BWMRULE | DS-03 |
| T-EXEC-009 | 配置 BlacklistRule | execute | BLACKLISTRULE | DS-03 |
| T-VERIFY-001 | 验证 License 开关 | verify | LICENSESWITCH | DS-01 |
| T-VERIFY-002 | 验证配置链逐层回查 | verify | RULEBINDING→RULE→...→FILTER 全链路 | DS-01, DS-02 |
| T-VERIFY-003 | 验证 PFCP 会话上报与计费流量 | verify | PFCP Session Report | DS-01 |
| T-VERIFY-004 | 验证三四层阻塞生效 | verify | RULEBINDING→RULE→PCCPOLICYGRP→PCCACTIONPROP→FILTER | DS-02 |
| T-VERIFY-005 | 验证七层配置链 | verify | RULEBINDING→RULE→...→L7FILTER→FILTER 全链路 | DS-02 |
| T-VERIFY-006 | 验证带宽控制策略生效 | verify | BWM 全链路 | DS-03 |

#### 各方案任务编排顺序

**DS-01 差异化计费组合方案**：

```
T-PLAN-001 → T-PLAN-002 → T-PLAN-003 → T-PLAN-004 → T-PLAN-005
→ T-EXEC-001 → T-EXEC-002 → T-EXEC-003 → T-EXEC-004 → T-EXEC-005 → T-EXEC-008 → T-EXEC-010
→ T-VERIFY-001 → T-VERIFY-002 → T-VERIFY-003
```

**DS-02 访问限制组合方案**：

```
T-PLAN-001 → T-PLAN-002 → T-PLAN-003 → T-PLAN-006
→ T-EXEC-002 → T-EXEC-003 → T-EXEC-004 → T-EXEC-006 → T-EXEC-008 → T-EXEC-010
→ T-VERIFY-004 → T-VERIFY-005
```

**DS-03 带宽控制与 QoS 编排方案**：

```
T-PLAN-001 → T-PLAN-002 → T-PLAN-003 → T-PLAN-007
→ T-EXEC-002 → T-EXEC-003 → T-EXEC-004 → T-EXEC-007 → T-EXEC-009 → T-EXEC-008 → T-EXEC-010
→ T-VERIFY-006
```

**DS-04 本地分流与独立计费方案**（源文档无完整脚本实例，仅规划态）：

```
T-PLAN-001 → T-PLAN-008 → T-PLAN-009
```

### 4.3 原子 Task 详情

> 以下逐个 Task 列出完整字段。plan 态 Task 无 ConfigObject 和命令映射；execute/verify 态 Task 需列明 ConfigObject 和命令示例。内容来源于原始产品文档，逐个 Task 从源文档提取。

（待填充——逐个 Task 从产品文档提取 ConfigObject 和命令示例）

#### T-PLAN-001 规划生效范围

| 字段 | 值 |
|------|-----|
| task_id | T-PLAN-001 |
| task_name | 规划生效范围 |
| task_summary | 确定策略对谁生效：定义用户范围、业务边界、DNN/APN 和默认兜底策略，最终体现为 UserProfile 的名称、结构与规则绑定规划 |
| phase | plan |
| input_artifacts | ["用户范围定义", "业务边界", "DNN/APN 规划", "默认兜底策略要求"] |
| output_artifacts | ["UserProfile 名称与结构规划", "默认策略绑定规划（如 DFTURRGRPNAME）", "规则绑定分配方案"] |
| command | - |
| config_object | - |
| source_evidence_ids | ["套餐1_93112148", "套餐2_94838085", "套餐3_94838086"] |
| status | active |

> 证据：三个套餐各创建一个 UserProfile（up_charging / up_bwmcontrol / up_policy）作为范围边界。套餐1 数据段："业务4作为兜底策略...计费策略可以直接配置在User Profile中"。套餐1 步骤7："配置User Profile，并绑定普通策略"——`ADD USERPROFILE` + `SET URRGRPBINDING`（设置默认 URR 组）。UserProfile 是生效范围的载体，所有规则通过 RULEBINDING 绑定到同一个 UserProfile 下，形成最终业务套餐。

#### T-PLAN-002 规划识别条件

| 字段 | 值 |
|------|-----|
| task_id | T-PLAN-002 |
| task_name | 规划识别条件 |
| task_summary | 将业务描述翻译成可匹配的过滤条件：L3/L4 过滤器（FILTER）、协议绑定（PROTBINDFLOWF）、L7 URL 过滤器（L7FILTER），并组合成流过滤器（FLOWFILTER/FLOWFILTERGRP） |
| phase | plan |
| input_artifacts | ["业务描述（协议、URL、地址、端口）", "过滤条件与识别逻辑"] |
| output_artifacts | ["过滤条件规划表：FILTER/L7FILTER/PROTBINDFLOWF 的对应关系与参数"] |
| command | - |
| config_object | - |
| source_evidence_ids | ["套餐1_93112148", "套餐2_94838085", "套餐3_94838086"] |
| status | active |

> 证据：套餐1 数据段将"用户访问 www.huawei.com 网站"翻译为 FILTER(filterA, ANY) + L7FILTER(l7filterA, URL=www.huawei.com/\*) + PROTOCOL=HTTPS → flowfilterA。套餐1 业务3 是两种条件的并集（IP 地址 OR RTSP 协议），需要 FLOWFILTERGRP 组合。套餐3 业务3 使用端口范围 MSSTARTPORT=1000, MSENDPORT=20000。套餐2 业务3 例外情况通过 BLACKLISTRULE 排除。核心翻译模式：特定 URL → L7FILTER；特定协议 → PROTBINDFLOWF；特定 IP → FILTER+IPLIST；"任意" → FILTER(ANY)。

#### T-PLAN-003 规划 Rule 与优先级

| 字段 | 值 |
|------|-----|
| task_id | T-PLAN-003 |
| task_name | 规划 Rule 与优先级 |
| task_summary | 决定多业务重叠时谁先生效，按业务语义分配 PRIORITY 数值（数值越小优先级越高），覆盖型规则优先于常规规则，兜底规则最低 |
| phase | plan |
| input_artifacts | ["多类业务目标和动作关系", "过滤条件是否有交集"] |
| output_artifacts | ["Rule 层次与优先级排序"] |
| command | - |
| config_object | - |
| source_evidence_ids | ["套餐1_93112148", "套餐2_94838085", "套餐3_94838086"] |
| status | active |

> 证据：套餐1 数据段——"当多个业务出现重合时，业务编号越小，优先级越高"，PRIORITY=100/200/300/400 简单递增。套餐2 业务5（累计流量超50GB时限速）需覆盖所有其他业务，PRIORITY=50 最高优先级，业务4 兜底 PRIORITY=200。套餐3 业务4（话费耗尽重定向）PRIORITY=400 覆盖业务1-3（500/550/700）。优先级按业务语义分配，非简单编号顺序。

#### T-PLAN-004 规划计费对象与费率标识

| 字段 | 值 |
|------|-----|
| task_id | T-PLAN-004 |
| task_name | 规划计费对象与费率标识 |
| task_summary | 根据资费模型（单价/免费/兜底）和在线/离线要求，规划 URR→URRGROUP→PCCPOLICYGRP 计费对象链，将每条业务的费率落到可执行的控制面对象 |
| phase | plan |
| input_artifacts | ["资费模型（如 1元/GB、免费、0.1元/GB）", "在线/离线计费方式要求", "业务粒度"] |
| output_artifacts | ["URR 及 URRID 规划表", "URRGROUP 规划", "PCCPOLICYGRP 规划", "默认 URR 组绑定方案"] |
| command | - |
| config_object | - |
| source_evidence_ids | ["套餐1_93112148"] |
| status | active |

> 证据：套餐1 数据段——"业务1、2、4都涉及到了计费，URRID 分别为 urrA=1000、urrB=2000、urrD=3000"。业务3 免费："设置 urrC=4000, OFFMETERINGTYPE=FREE"。业务4 兜底："SET URRGRPBINDING: DFTURRGRPNAME='urrgD'"。

#### T-PLAN-005 规划配额耗尽动作

| 字段 | 值 |
|------|-----|
| task_id | T-PLAN-005 |
| task_name | 规划配额耗尽动作 |
| task_summary | 规划在线计费配额耗尽后用户体验如何变化：阻断(BLOCK)、重定向(REDIRECT)还是放行(FORWARD)，并设计对应的动作策略 |
| phase | plan |
| input_artifacts | ["配额控制要求", "用户体验要求（耗尽后是否允许继续访问）"] |
| output_artifacts | ["配额耗尽动作策略（BLOCK/REDIRECT/FORWARD）"] |
| command | - |
| config_object | - |
| source_evidence_ids | ["计费解决方案概述_90776649", "融合计费概述_42995681", "套餐3_94838086"] |
| status | active |

> 证据：套餐3 业务4——"话费余额耗尽场景下，用户访问任何网站都会重定向到充值页面"。计费解决方案概述——"在线计费：进行配额管理...在配额不足时，SMF 可以停止业务使用"。

#### T-PLAN-006 规划导向与增强动作

| 字段 | 值 |
|------|-----|
| task_id | T-PLAN-006 |
| task_name | 规划导向与增强动作 |
| task_summary | 规划访问限制场景中除简单阻断外的多种动作：阻塞(DISCARD)、头增强(HEADEN+MSISDN+防欺诈)、IP重定向(IPREDIR)、URL重定向(REDIRECT)，确定参数和优先级 |
| phase | plan |
| input_artifacts | ["导向目标（阻塞/重定向 IP/URL）", "安全增强需求（ANTIFRAUD）", "Portal 约束"] |
| output_artifacts | ["PCCACTIONPROP/HEADEN/REDIRECT/IPREDIR 动作设计"] |
| command | - |
| config_object | - |
| source_evidence_ids | ["套餐3_94838086"] |
| status | active |

> 证据：套餐3——业务1"流动作是阻塞，通过配置 PCC 动作属性完成"（DISCARD 四方向门控）。业务2"插入 MSISDN 号和防欺诈"（HEADEN+ANTIFRAUD=ENABLE）。业务3"IP 重定向"（IPREDIRECTIP=10.100.111.222）。业务4"URL 重定向到充值页面"。

#### T-PLAN-007 规划 BWM 策略

| 字段 | 值 |
|------|-----|
| task_id | T-PLAN-007 |
| task_name | 规划 BWM 策略 |
| task_summary | 根据带宽控制目标（CIR 保障/PIR 限速/RATE 整形）为每条业务规划 BWMCONTROLLER 参数，处理例外黑名单和 FUP 限额后限速场景 |
| phase | plan |
| input_artifacts | ["每条业务的带宽目标（保障/限速/整形）", "速率参数（10M/8M/20M/2M）", "例外情况需求"] |
| output_artifacts | ["BWMCONTROLLER 参数表（CIR/PIR/RATE）", "CATEGORYPROP/BWMSERVICE 链规划", "黑名单规划"] |
| command | - |
| config_object | - |
| source_evidence_ids | ["套餐2_94838085"] |
| status | active |

> 证据：套餐2——"bwmcontrolerA:CIR=10240(最低保障)、bwmcontrolerB:PIR=8192(限速)、bwmcontrolerC:RATE=10240(整形)、bwmcontrolerD:PIR=20480(兜底限速)、bwmcontrolerE:PIR=2048(限额后限速)"。业务3 例外："需要配置黑名单规则"。

#### T-PLAN-008 规划分流触发与锚点插入

| 字段 | 值 |
|------|-----|
| task_id | T-PLAN-008 |
| task_name | 规划分流触发与锚点插入 |
| task_summary | 规划本地分流何时触发（DNN+位置/PRA/DNAI/动态规则），SMF 如何选择 UL CL UPF 和辅锚点 UPF，以及如何通过 PFCP 会话修改将常规 PDU 会话更新为分流 PDU 会话 |
| phase | plan |
| input_artifacts | ["DNN/位置/PRA/DNAI/触发方式", "UPF 能力和切片信息"] |
| output_artifacts | ["UL CL 触发条件", "主/辅锚点选择方案", "PFCP 会话建立方案"] |
| command | - |
| config_object | - |
| source_evidence_ids | ["How分流_58273329"] |
| status | active |

> 证据：How分流——"SMF 会实时检测用户的位置（TAI 区或小区），一旦 DNN+位置组合满足分流触发条件便触发分流"。UL CL UPF 决策条件："是否支持 UL CL 功能、用户切片信息、用户位置区信息"。辅锚点决策条件："DNAI 信息、DNN 与切片信息"。

#### T-PLAN-009 规划计费 Trigger 与多 UPF 配额

| 字段 | 值 |
|------|-----|
| task_id | T-PLAN-009 |
| task_name | 规划计费 Trigger 与多 UPF 配额 |
| task_summary | 规划本地分流场景下主/辅锚点各自的计费规则下发、Trigger 驱动的配额申请机制，以及 SMF 按 UPF 向 CHF 独立申请配额的多 UPF 配额管理策略 |
| phase | plan |
| input_artifacts | ["计费方式", "RG 粒度", "Trigger 类别", "锚点 UPF 数量"] |
| output_artifacts | ["Trigger 策略", "多 UPF 配额策略", "计费规则下发方案"] |
| command | - |
| config_object | - |
| source_evidence_ids | ["MEC计费流程_52284255", "融合计费概述_42995681"] |
| status | active |

> 证据：MEC 计费流程——"SMF 按 UPF 向 CHF 申请配额（消息中 Multiple Unit Usage 字段携带 UPF ID），哪个 UPF 申请就向哪个 UPF 下发配额"。"UL CL UPF 没有计费规则，不计费。通常 UL CL UPF 与辅锚点合设"。

#### T-EXEC-002 配置三四层过滤条件

| 字段 | 值 |
|------|-----|
| task_id | T-EXEC-002 |
| task_name | 配置三四层过滤条件 |
| task_summary | 创建三四层过滤器，定义协议类型、源/目的 IP 地址或 IP 列表等匹配条件 |
| phase | execute |
| input_artifacts | ["规划态输出的过滤条件规划表"] |
| output_artifacts | ["FILTER 配置"] |
| command | `ADD FILTER:FILTERNAME="filterA",L34PROTTYPE=STRING,L34PROTOCOL=ANY;`<br>`ADD FILTER:FILTERNAME="filterC",L34PROTTYPE=STRING,L34PROTOCOL=TCP,SVRIPMODE=IPLIST,SVRIPLISTNAME="iplistB";` |
| config_object | `FILTER` |
| source_evidence_ids | ["套餐1_93112148", "套餐2_94838085", "套餐3_94838086"] |
| status | active |

**各方案参数差异**：

| 方案 | 过滤器名 | 关键参数 | 来源 |
|------|---------|---------|------|
| DS-01 计费 | filterA(ANY), filterC(TCP+IPLIST) | L34PROTOCOL=ANY/TCP, SVRIPMODE=IPLIST | 套餐1 步骤2 |
| DS-02 访问限制 | filterA(ANY), filterC(端口范围) | MSSTARTPORT=1000, MSENDPORT=20000 | 套餐3 步骤1 |
| DS-03 带宽控制 | filterA(ANY), filterC1(指定IP) | SVRIP="10.11.12.13" | 套餐2 步骤1 |

#### T-EXEC-001 配置 IP 地址列表

| 字段 | 值 |
|------|-----|
| task_id | T-EXEC-001 |
| task_name | 配置 IP 地址列表 |
| task_summary | 创建 IP 地址列表（IPLIST），供三四层过滤器引用以匹配特定服务器 IP 地址范围 |
| phase | execute |
| input_artifacts | ["规划态输出的 IP 地址规划表"] |
| output_artifacts | ["IPLIST 配置"] |
| command | `ADD IPLIST:IPLISTNAME="iplistB",IPVERSION=IPV4,IPV4ADDR="10.123.234.10",MASKVALUE=32;`<br>`ADD IPLIST:IPLISTNAME="iplistB",IPVERSION=IPV4,IPV4ADDR="10.123.234.11",MASKVALUE=32;`<br>`ADD IPLIST:IPLISTNAME="iplistB",IPVERSION=IPV4,IPV4ADDR="10.123.234.12",MASKVALUE=32;`<br>`ADD IPLIST:IPLISTNAME="iplistB",IPVERSION=IPV4,IPV4ADDR="10.123.234.13",MASKVALUE=32;` |
| config_object | `IPLIST` |
| source_evidence_ids | ["套餐1_93112148"] |
| status | active |

**说明**：IPLIST 仅在计费场景（DS-01）中使用，用于业务3中 filterC 匹配 10.123.234.10~10.123.234.13 范围内的服务器 IP 地址。同名的多条 ADD IPLIST 命令向同一列表追加不同 IP 条目。

#### T-EXEC-003 配置七层过滤条件

| 字段 | 值 |
|------|-----|
| task_id | T-EXEC-003 |
| task_name | 配置七层过滤条件 |
| task_summary | 创建七层过滤器，定义应用层 URL 匹配条件或协议绑定关系，用于识别特定网站访问或应用协议流量 |
| phase | execute |
| input_artifacts | ["规划态输出的七层过滤条件规划表"] |
| output_artifacts | ["L7FILTER 配置"] |
| command | `ADD L7FILTER:L7FILTERNAME="l7filterA",SUBL7FLTNAME="sl7A",URLTYPE=URL,URL="www.huawei.com/*";` |
| config_object | `L7FILTER` |
| source_evidence_ids | ["套餐1_93112148", "套餐2_94838085", "套餐3_94838086"] |
| status | active |

**各方案参数差异**：

| 方案 | 过滤器名 | 关键参数 | 来源 |
|------|---------|---------|------|
| DS-01 计费 | l7filterA | URLTYPE=URL, URL="www.huawei.com/*" | 套餐1 步骤3 |
| DS-02 带宽控制 | l7filterA, l7filterB, l7filterC | l7filterA: URL="www.huawei.com"; l7filterB: 无 URL（仅协议绑定）；l7filterC: URL="www.example.com*/*" | 套餐2 步骤2 |
| DS-03 访问限制 | l7filterA, l7filterB | l7filterA: URL="www.huawei.com"; l7filterB: URL="www.vmall.com" | 套餐3 步骤2 |

#### T-EXEC-004 配置流过滤器与绑定

| 字段 | 值 |
|------|-----|
| task_id | T-EXEC-004 |
| task_name | 配置流过滤器与绑定 |
| task_summary | 配置流过滤器（组），并将三四层、七层过滤条件与流过滤器绑定——流过滤器是三四层过滤条件与七层过滤条件的组合 |
| phase | execute |
| input_artifacts | ["FILTER对象", "L7FILTER对象", "IPLIST对象(可选)", "协议识别规划"] |
| output_artifacts | ["FLOWFILTER对象", "FLOWFILTERGRP对象(可选)", "FLTBINDFLOWF绑定关系", "PROTBINDFLOWF绑定关系"] |
| command | `ADD FLOWFILTER:FLOWFILTERNAME="flowfilterA";`<br>`ADD FLTBINDFLOWF:FLOWFILTERNAME="flowfilterA",FILTERNAME="filterA";`<br>`ADD PROTBINDFLOWF:FLOWFILTERNAME="flowfilterA",PROTOCOLNAME="HTTPS",L7FILTERNAME="l7filterA";`<br>`ADD PROTBINDFLOWF:FLOWFILTERNAME="flowfilterB",PROTOCOLNAME="HTTP";`<br>`ADD FLOWFILTERGRP:FLWFLTRGRPNAME="flowfiltergroupC",FLOWFILTERNAME="flowfilterC1";`<br>`ADD FLOWFILTERGRP:FLWFLTRGRPNAME="flowfiltergroupC",FLOWFILTERNAME="flowfilterC2";` |
| config_object | `FLOWFILTER`, `FLOWFILTERGRP`, `FLTBINDFLOWF`, `PROTBINDFLOWF` |
| source_evidence_ids | ["套餐1_93112148", "套餐2_94838085", "套餐3_94838086"] |
| status | active |

**各方案参数差异**：

| 方案 | FLOWFILTER 数量 | 绑定模式 | FLOWFILTERGRP | 来源 |
|------|----------------|---------|---------------|------|
| DS-01 计费 | 4 个 (A/B/C1+C2/D) | FLTBINDFLOWF + PROTBINDFLOWF | 是 (groupC 含 C1+C2) | 套餐1 步骤4 |
| DS-02 带宽控制 | 5 个 (A/B/C/C1/D) | FLTBINDFLOWF + PROTBINDFLOWF | 否 | 套餐2 步骤3 |
| DS-03 访问限制 | 4 个 (A/B/C/D) | FLTBINDFLOWF + PROTBINDFLOWF | 否 | 套餐3 步骤3 |

**绑定模式说明**：
- **FLTBINDFLOWF**：将三四层 FILTER 绑定到 FLOWFILTER（每个 FLOWFILTER 必须绑定至少一个 FILTER）
- **PROTBINDFLOWF**：将协议 + 可选七层过滤器绑定到 FLOWFILTER；仅协议识别时可省略 L7FILTERNAME
- **FLOWFILTERGRP**：多条件组合（或关系）时使用，将多个 FLOWFILTER 编入同一组

#### T-EXEC-005 配置计费动作链

| 字段 | 值 |
|------|-----|
| task_id | T-EXEC-005 |
| task_name | 配置计费动作链 |
| task_summary | 配置离线计费的流动作链：创建 URR 定义计费方式与上报模式，创建 URRGROUP 组合上下行 URR，创建 PCCPOLICYGRP 将 URRGROUP 绑定到 PCC 策略组 |
| phase | execute |
| input_artifacts | ["FILTER 配置", "FLOWFILTER 配置"] |
| output_artifacts | ["URR 配置", "URRGROUP 配置", "PCCPOLICYGRP 配置"] |
| command | `ADD URR:URRNAME="urrA",URRID=1000,USAGERPTMODE=OFFLINE;`<br>`ADD URRGROUP:URRGROUPNAME="urrgA",UPURRNAME1="urrA",DOWNURRNAME1="urrA";`<br>`ADD PCCPOLICYGRP:PCCPOLICYGRPNM="pccgA",URRGROUPNAME="urrgA";`<br>`ADD URR:URRNAME="urrC",URRID=4000,USAGERPTMODE=OFFLINE,OFFMETERINGTYPE=FREE;`<br>`ADD URRGROUP:URRGROUPNAME="urrgC",UPURRNAME1="urrC",DOWNURRNAME1="urrC";`<br>`ADD PCCPOLICYGRP:PCCPOLICYGRPNM="pccgC",URRGROUPNAME="urrgC";` |
| config_object | `URR`, `URRGROUP`, `PCCPOLICYGRP` |
| source_evidence_ids | ["套餐1_93112148"] |
| status | active |

**说明**：计费动作链为三层嵌套结构：URR（定义计费规则/URRID/上报模式）→ URRGROUP（组合上下行 URR）→ PCCPOLICYGRP（封装为 PCC 策略组，供 RULE 引用）。免费业务通过 `OFFMETERINGTYPE=FREE` 实现零计费。此任务仅用于 DS-01（计费场景）。

#### T-EXEC-006 配置策略动作链

| 字段 | 值 |
|------|-----|
| task_id | T-EXEC-006 |
| task_name | 配置策略动作链 |
| task_summary | 为访问限制场景配置策略动作链，包括 PCC 阻塞动作属性、HTTP 头增强（插入 MSISDN+防欺诈）、URL 重定向三种动作类型 |
| phase | execute |
| input_artifacts | ["FLOWFILTER 配置", "策略类型规划"] |
| output_artifacts | ["PCCACTIONPROP 配置", "HEADEN 配置", "REDIRECT 配置", "PCCPOLICYGRP 配置"] |
| command | `ADD PCCACTIONPROP:PCCACTPROPNAME="pccactA",UPINITUPGATE=DISCARD,UPINITDNGATE=DISCARD,DNINITUPGATE=DISCARD,DNINITDNGATE=DISCARD;`<br>`ADD PCCPOLICYGRP:PCCPOLICYGRPNM="pccgrpA",PCCACTPROPNAME="pccactA";`<br>`ADD HEADEN:HEADERENNAME="headenB",DATATYPE=MSISDN1,ANTIFRAUD=ENABLE;`<br>`ADD REDIRECT:REDIRECTNAME="redirectD",URL="www.huawei.com";`<br>`ADD PCCACTIONPROP:PCCACTPROPNAME="pccactD",UPINITREDIRNM="redirectD";`<br>`ADD PCCPOLICYGRP:PCCPOLICYGRPNM="pccgrpD",PCCACTPROPNAME="pccactD";` |
| config_object | `PCCACTIONPROP`, `HEADEN`, `REDIRECT`, `PCCPOLICYGRP` |
| source_evidence_ids | ["套餐3_94838086"] |
| status | active |

**说明**：访问限制场景包含三种策略动作类型：**PCC 阻塞**（PCCACTIONPROP 四向门控置 DISCARD）→ PCCPOLICYGRP 包装；**头增强**（HEADEN 插入 MSISDN+防欺诈）可直接被 RULE 引用；**URL 重定向**（REDIRECT 指定目标 URL → PCCACTIONPROP 引用 REDIRECT → PCCPOLICYGRP 包装）。此任务仅用于 DS-02（访问限制）。

#### T-EXEC-007 配置 BWM 带宽控制链

| 字段 | 值 |
|------|-----|
| task_id | T-EXEC-007 |
| task_name | 配置 BWM 带宽控制链 |
| task_summary | 创建带宽管理控制链：配置 CATEGORYPROP → BWMSERVICE → BWMCONTROLLER → BWMUSERGROUP → BWMRULE，支持最低速率保障（CAR+CIR）、最高速率限制（CAR+PIR）、流量整形（SHAPING+RATE）三种模式 |
| phase | execute |
| input_artifacts | ["FLOWFILTER 配置"] |
| output_artifacts | ["CATEGORYPROP 配置", "BWMSERVICE 配置", "BWMCONTROLLER 配置", "BWMUSERGROUP 配置", "BWMRULE 配置"] |
| command | `ADD CATEGORYPROP:CATEPROPNAME="catropA";`<br>`ADD BWMSERVICE:BWMSERVICENAME="bwmservA",BWMSERVICETYPE=NONTOS,NONTOSSRVTYPE=CATEGORY_PROP,CATEPROPNAME="catropA";`<br>`ADD BWMCONTROLLER:BWMCNAME="bwmcontrolA",CTRLTYPE=CAR,CIR=10240;`<br>`ADD BWMUSERGROUP:USERGROUPTYPE=SPECIFIC_GROUP,USERGROUPNAME="bwmgrpA",USERGROUPPRI=100,USERLEVSRVTYPE=NONTOS;`<br>`ADD BWMRULE:USERGROUPTYPE=SPECIFIC_GROUP,USERGROUPNAME="bwmgrpA",BWMRULETYPE=SUBSCRIBER_SPECIFIC,BWMRULENAME="bwmruleA",BWMSERVICENAME="bwmservA",UPBWMCTRLNAME1="bwmcontrolA",DNBWMCTRLNAME1="bwmcontrolA",BWMRULEPRI=100;`<br>`ADD CATEGORYPROP:CATEPROPNAME="catropB";`<br>`ADD BWMCONTROLLER:BWMCNAME="bwmcontrolB",CTRLTYPE=CAR,PIR=8192;`<br>`ADD BWMUSERGROUP:USERGROUPTYPE=SPECIFIC_GROUP,USERGROUPNAME="bwmgrpB",USERGROUPPRI=110,USERLEVSRVTYPE=NONTOS;`<br>`ADD BWMRULE:USERGROUPTYPE=SPECIFIC_GROUP,USERGROUPNAME="bwmgrpB",BWMRULETYPE=SUBSCRIBER_SPECIFIC,BWMRULENAME="bwmruleB",BWMSERVICENAME="bwmservB",UPBWMCTRLNAME1="bwmcontrolB",DNBWMCTRLNAME1="bwmcontrolB",BWMRULEPRI=110;`<br>`ADD CATEGORYPROP:CATEPROPNAME="catropC";`<br>`ADD BWMCONTROLLER:BWMCNAME="bwmcontrolC",CTRLTYPE=SHAPING,RATE=10240;`<br>`ADD BWMUSERGROUP:USERGROUPTYPE=SPECIFIC_GROUP,USERGROUPNAME="bwmgrpC",USERGROUPPRI=120,USERLEVSRVTYPE=NONTOS;`<br>`ADD BWMRULE:USERGROUPTYPE=SPECIFIC_GROUP,USERGROUPNAME="bwmgrpC",BWMRULETYPE=SUBSCRIBER_SPECIFIC,BWMRULENAME="bwmruleC",BWMSERVICENAME="bwmservC",UPBWMCTRLNAME1="bwmcontrolC",DNBWMCTRLNAME1="bwmcontrolC",BWMRULEPRI=120;` |
| config_object | `CATEGORYPROP`, `BWMSERVICE`, `BWMCONTROLLER`, `BWMUSERGROUP`, `BWMRULE` |
| source_evidence_ids | ["套餐2_94838085"] |
| status | active |

**说明**：BWM 控制链为五层结构：CATEGORYPROP（命名锚点）→ BWMSERVICE（绑定类别属性）→ BWMCONTROLLER（定义带宽参数，三种模式：CAR+CIR 保障/CA+PIR 限速/SHAPING+RATE 整形）→ BWMUSERGROUP（用户组+优先级）→ BWMRULE（绑定用户组+服务+控制器）。速率单位 Kbps。此任务仅用于 DS-03（带宽控制）。

#### T-EXEC-008 配置 Rule

| 字段 | 值 |
|------|-----|
| task_id | T-EXEC-008 |
| task_name | 配置 Rule |
| task_summary | 创建规则对象，将流过滤器（匹配条件）与策略动作（执行动作）绑定，并设定优先级——Rule 是 SA 配置链路的核心汇聚点 |
| phase | execute |
| input_artifacts | ["FLOWFILTER 配置", "策略动作配置（PCCPOLICYGRP/HEADEN/CATEGORYPROP）"] |
| output_artifacts | ["RULE 配置"] |
| command | `ADD RULE:RULENAME="ruleA",POLICYTYPE=PCC,FILTERINGMODE=FLOWFILTER,FLOWFILTERNAME="flowfilterA",POLICYNAME="pccgA",PRIORITY=100;`<br>`ADD RULE:RULENAME="ruleC",POLICYTYPE=PCC,FILTERINGMODE=FLOWFILTERGRP,FLWFLTRGRPNAME="flowfiltergroupC",POLICYNAME="pccgC",PRIORITY=300;`<br>`ADD RULE:RULENAME="ruleB",POLICYTYPE=HEADEN,FILTERINGMODE=FLOWFILTER,FLOWFILTERNAME="flowfilterB",POLICYNAME="headenB",PRIORITY=550;`<br>`ADD RULE:RULENAME="ruleC",POLICYTYPE=IPREDIR,FILTERINGMODE=FLOWFILTER,FLOWFILTERNAME="flowfilterC",REDIRIPVERFLAG=IPV4,IPREDIRECTIP=10.100.111.222;`<br>`ADD RULE:RULENAME="ruleA",POLICYTYPE=BWM,FILTERINGMODE=FLOWFILTER,FLOWFILTERNAME="flowfilterA",POLICYNAME="catropA",PRIORITY=100;`<br>`ADD RULE:RULENAME="ruleE",POLICYTYPE=BWM,FILTERINGMODE=FLOWFILTER,FLOWFILTERNAME="flowfilterD",POLICYNAME="catropE",PRIORITY=50;` |
| config_object | `RULE`, `BLACKLISTRULE` |
| source_evidence_ids | ["套餐1_93112148", "套餐2_94838085", "套餐3_94838086"] |
| status | active |

**各方案参数差异**：

**各方案参数差异**：

| 方案 | POLICYTYPE | POLICYNAME 指向 | FILTERINGMODE | 来源 |
|------|-----------|----------------|---------------|------|
| DS-01 计费 | PCC | PCCPOLICYGRP (pccgX) | FLOWFILTER / FLOWFILTERGRP | 套餐1 步骤6 |
| DS-02 访问限制 | PCC / HEADEN / IPREDIR | PCCPOLICYGRP / HEADEN / 内联 IP | FLOWFILTER | 套餐3 步骤5 |
| DS-03 带宽控制 | BWM | CATEGORYPROP (catropX) | FLOWFILTER | 套餐2 步骤5 |

**核心语义**：Rule = flowfilter（匹配什么流量）+ POLICYTYPE + POLICYNAME（对流量做什么动作）+ PRIORITY（同类型规则间的匹配顺序）。IPREDIR 类型特殊：动作内联在 RULE 中（REDIRIPVERFLAG + IPREDIRECTIP），无需引用外部策略对象。

#### T-EXEC-009 配置 BlacklistRule

| 字段 | 值 |
|------|-----|
| task_id | T-EXEC-009 |
| task_name | 配置 BlacklistRule |
| task_summary | 为带宽控制场景中的例外流量创建黑名单规则，使特定流不受 BWM 策略限制——BlacklistRule 是 Rule 的例外豁免机制 |
| phase | execute |
| input_artifacts | ["FLOWFILTER 配置（例外流过滤器）"] |
| output_artifacts | ["BLACKLISTRULE 配置"] |
| command | `ADD BLACKLISTRULE:RULENAME="ruleC1",POLICYTYPE=BWM,FILTERINGMODE=FLOWFILTER,FLOWFILTERNAME="flowfilterC1";` |
| config_object | `BLACKLISTRULE` |
| source_evidence_ids | ["套餐2_94838085"] |
| status | active |

**说明**：BlacklistRule 无需指定 POLICYNAME 和 PRIORITY——其语义是"匹配到此流量的流量不做策略处理"，即豁免而非执行。需先为例外流量单独配置 FILTER + FLOWFILTER，再通过 BLACKLISTRULE 声明豁免。此任务仅用于 DS-03（带宽控制）。

#### T-EXEC-010 配置 UserProfile 与 Rule 绑定

| 字段 | 值 |
|------|-----|
| task_id | T-EXEC-010 |
| task_name | 配置 UserProfile 与 Rule 绑定 |
| task_summary | 创建 USERPROFILE 作为业务套餐容器，将 RULE 逐条绑定到其下，最后刷新服务使配置生效——UserProfile 是 SA 配置链路的最终汇聚与生效点 |
| phase | execute |
| input_artifacts | ["RULE 配置", "BLACKLISTRULE 配置（可选）", "URRGROUP 配置（DS-01）"] |
| output_artifacts | ["USERPROFILE 配置", "RULEBINDING 配置", "REFRESHSRV 生效"] |
| command | `ADD USERPROFILE:USERPROFILENAME="up_charging";`<br>`SET URRGRPBINDING:USERPROFILENAME="up_charging",DFTURRGRPNAME="urrgD",DFTSIGURRGNAME="urrgD";`<br>`ADD RULEBINDING:USERPROFILENAME="up_charging",RULENAME="ruleA",POLICYTYPE=PCC;`<br>`ADD RULEBINDING:USERPROFILENAME="up_charging",RULENAME="ruleB",POLICYTYPE=PCC;`<br>`ADD RULEBINDING:USERPROFILENAME="up_charging",RULENAME="ruleC",POLICYTYPE=PCC;`<br>`ADD RULEBINDING:USERPROFILENAME="up_charging",RULENAME="ruleD",POLICYTYPE=PCC;`<br>`SET REFRESHSRV:REFRESHTYPE=USERPROFILE;` |
| config_object | `USERPROFILE`, `RULEBINDING`, `REFRESHSRV`, `URRGRPBINDING` |
| source_evidence_ids | ["套餐1_93112148", "套餐2_94838085", "套餐3_94838086"] |
| status | active |

**各方案参数差异**：

| 方案 | UserProfile 名 | URRGRPBINDING | RULEBINDING 类型 | 绑定 Rule 数 | 来源 |
|------|---------------|---------------|-----------------|-------------|------|
| DS-01 计费 | up_charging | 有（默认 URRGROUP） | PCC | 4 条 | 套餐1 步骤7-8 |
| DS-02 访问限制 | up_policy | 无 | PCC / HEADEN / IPREDIR | 4 条 | 套餐3 步骤6 |
| DS-03 带宽控制 | up_bwmcontrol | 无 | BWM | 6 条（含 BlacklistRule） | 套餐2 步骤6 |

**核心语义**：ADD USERPROFILE（创建空容器）→ SET URRGRPBINDING（仅 DS-01，绑定默认计费组）→ 多条 ADD RULEBINDING（将 Rule 逐一绑定）→ SET REFRESHSRV（刷新生效）。RULEBINDING 的 POLICYTYPE 必须与对应 RULE 一致。

#### T-VERIFY-001 验证 License 开关

| 字段 | 值 |
|------|-----|
| task_id | T-VERIFY-001 |
| task_name | 验证 License 开关 |
| task_summary | 验证 SA 基础 License 开关已开启，确保业务感知功能可用；同时验证内容计费基本功能 License 已启用 |
| phase | verify |
| input_artifacts | ["所需 License 控制项列表"] |
| output_artifacts | ["License 开关状态查询结果"] |
| command | `LST LICENSESWITCH:LICITEM="LKV3G5SABS01";`<br>`LST LICENSESWITCH:LICITEM="LKV3G5BCBC01";` |
| config_object | `LICENSESWITCH` |
| source_evidence_ids | ["EVID-SA-BASIC-LICENSE", "EVID-CONTENT-BILLING-LICENSE"] |
| status | active |

**说明**：本任务在执行任何 SA 配置之前运行。SA-Basic（LKV3G5SABS01）是必须开启的基础 License；计费场景还需内容计费基本功能（LKV3G5BCBC01）。查询返回"开关=ENABLE"表示已开启。此任务仅用于 DS-01（计费场景）。

#### T-VERIFY-002 验证配置链逐层回查

| 字段 | 值 |
|------|-----|
| task_id | T-VERIFY-002 |
| task_name | 验证配置链逐层回查 |
| task_summary | 从 User Profile 出发，通过 LST 命令逐层回查 RULEBINDING→RULE→FLOWFILTER→FILTER 全链路配置，核实每一层的对象名称、绑定关系和过滤参数是否与规划值一致 |
| phase | verify |
| input_artifacts | ["UserProfile 名称", "规划参数表"] |
| output_artifacts | ["各层 LST 查询结果", "逐层一致性校验结论"] |
| command | `LST RULEBINDING:USERPROFILENAME="up_charging";`<br>`LST RULE:RULENAME="ruleA",POLICYTYPE=PCC;`<br>`LST PCCPOLICYGRP:PCCPOLICYGRPNM="pccgA";`<br>`LST FLOWFILTER:FLOWFILTERNAME="flowfilterA";`<br>`LST FLTBINDFLOWF:FLOWFILTERNAME="flowfilterA";`<br>`LST FILTER:FILTERNAME="filterA";` |
| config_object | `RULEBINDING`, `RULE`, `FLOWFILTER`, `FILTER`, `PCCPOLICYGRP`, `PCCACTIONPROP`, `PROTBINDFLOWF`, `L7FILTER` |
| source_evidence_ids | ["套餐1_93112148", "套餐3_94838086"] |
| status | active |

**各方案参数差异**：

| 对比维度 | DS-01 计费 | DS-02 访问限制 |
|----------|-----------|---------------|
| POLICYTYPE | 全部 PCC | 混合 PCC / HEADEN / IPREDIR |
| 策略层回查 | PCCPOLICYGRP→URRGROUP→URR | PCCPOLICYGRP→PCCACTIONPROP / HEADEN |
| 七层回查 | PROTBINDFLOWF→L7FILTER | 同左 |
| 来源 | 套餐1 步骤9 | 套餐3 步骤7 |

#### T-VERIFY-003 验证 PFCP 会话上报与计费流量

| 字段 | 值 |
|------|-----|
| task_id | T-VERIFY-003 |
| task_name | 验证 PFCP 会话上报与计费流量 |
| task_summary | 验证 UPF 向 SMF 发送的 PFCP Session Report 中 Usage Report 的 URR ID 与业务规则绑定一致，确认计费流量被正确识别和上报 |
| phase | verify |
| input_artifacts | ["T-VERIFY-002 配置链回查通过", "OM Portal N4 接口跟踪任务"] |
| output_artifacts | ["PFCP Session Report 验证结果", "URR ID 匹配确认"] |
| command | `LST RULEBINDING:USERPROFILENAME="up_charging";`<br>`LST RULE:RULENAME="ruleA";`<br>`LST PCCPOLICYGRP:PCCPOLICYGRPNM="pccgA";`<br>`LST URRGROUP:URRGROUPNAME="urrgA";`<br>`LST URR:URRNAME="urrA";`<br>`LST PROTBINDFLOWF:FLOWFILTERNAME="flowfilterA";`<br>`LST L7FILTER:L7FILTERNAME="l7filterA";` |
| config_object | `RULEBINDING`, `RULE`, `PCCPOLICYGRP`, `URRGROUP`, `URR`, `PROTBINDFLOWF`, `FLOWFILTER`, `L7FILTER` |
| source_evidence_ids | ["调测内容计费_08957400"] |
| status | active |

**操作步骤**：

1. 在 OM Portal 创建 N4 接口跟踪任务
2. 测试终端使用已配置 DNN 接入网络
3. 终端访问目标业务（如 www.huawei.com），浏览至满足上报条件
4. 查看 UPF 向 SMF 发送的 PFCP Session Report Request，检查 Usage Report 中 URR ID

**说明**：本任务是 DS-01（计费场景）的最终验收步骤。通过 OM Portal 的 N4 接口跟踪功能抓取 PFCP Session Report，核心判断标准：URR ID 是否与 ADD URR 配置一致。此任务仅用于 DS-01。

#### T-VERIFY-004 验证三四层阻塞生效

| 字段 | 值 |
|------|-----|
| task_id | T-VERIFY-004 |
| task_name | 验证三四层阻塞生效 |
| task_summary | 逐层回查 RULEBINDING→RULE→PCCPOLICYGRP→PCCACTIONPROP→FLTBINDFLOWF→FILTER 全链路，验证阻塞规则已正确绑定且门控动作为 DISCARD |
| phase | verify |
| input_artifacts | ["UserProfile 名称", "规划参数表"] |
| output_artifacts | ["各层 LST 查询结果", "阻塞验证结论"] |
| command | `LST RULEBINDING:USERPROFILENAME="up_policy";`<br>`LST RULE:RULENAME="ruleA";`<br>`LST PCCPOLICYGRP:PCCPOLICYGRPNM="pccgrpA";`<br>`LST PCCACTIONPROP:PCCACTPROPNAME="pccactA";`<br>`LST FLTBINDFLOWF:FLOWFILTERNAME="flowfilterA";`<br>`LST FILTER:FILTERNAME="filterA";` |
| config_object | `RULEBINDING`, `RULE`, `PCCPOLICYGRP`, `PCCACTIONPROP`, `FLTBINDFLOWF`, `FILTER` |
| source_evidence_ids | ["套餐3_94838086"] |
| status | active |

**验证要点**：PCCACTIONPROP 的四个门控字段（UPINITUPGATE/UPINITDNGATE/DNINITUPGATE/DNINITDNGATE）必须全部为 DISCARD。

**说明**：此任务仅用于 DS-02（访问限制）。

#### T-VERIFY-005 验证七层配置链

| 字段 | 值 |
|------|-----|
| task_id | T-VERIFY-005 |
| task_name | 验证七层配置链 |
| task_summary | 逐层回查 DS-02 中涉及七层过滤的完整配置链，验证 RULEBINDING→RULE→PCCPOLICYGRP→PCCACTIONPROP→FLOWFILTER→PROTBINDFLOWF→L7FILTER→FLTBINDFLOWF→FILTER 全链路 |
| phase | verify |
| input_artifacts | ["UserProfile 名称", "七层过滤条件规划值"] |
| output_artifacts | ["七层配置链全链路查询结果"] |
| command | `LST RULEBINDING:USERPROFILENAME="up_policy";`<br>`LST RULE:RULENAME="ruleA",POLICYTYPE=PCC;`<br>`LST PCCPOLICYGRP:PCCPOLICYGRPNM="pccgrpA";`<br>`LST PCCACTIONPROP:PCCACTPROPNAME="pccactA";`<br>`LST FLOWFILTER:FLOWFILTERNAME="flowfilterA";`<br>`LST PROTBINDFLOWF:FLOWFILTERNAME="flowfilterA";`<br>`LST L7FILTER:L7FILTERNAME="l7filterA";`<br>`LST FLTBINDFLOWF:FLOWFILTERNAME="flowfilterA";`<br>`LST FILTER:FILTERNAME="filterA";`<br>`DSP SIGNATUREDB;` |
| config_object | `RULEBINDING`, `RULE`, `PCCPOLICYGRP`, `PCCACTIONPROP`, `FLOWFILTER`, `PROTBINDFLOWF`, `L7FILTER`, `FLTBINDFLOWF`, `FILTER`, `SIGNATUREDB` |
| source_evidence_ids | ["套餐3_94838086"] |
| status | active |

**说明**：与 T-VERIFY-004 相比增加了两个关键环节：(1) 通过 LST PROTBINDFLOWF 确认七层过滤条件（URL）已正确挂载；(2) 通过 DSP SIGNATUREDB 确认协议特征库已加载完成。此任务仅用于 DS-02（访问限制），在 T-VERIFY-004 之后执行。

#### T-VERIFY-006 验证带宽控制策略生效

| 字段 | 值 |
|------|-----|
| task_id | T-VERIFY-006 |
| task_name | 验证带宽控制策略生效 |
| task_summary | 通过 LST 查询 BWM 全链路配置，从 RULEBINDING→RULE→CATEGORYPROP→BWMSERVICE→BWMCONTROLLER→BWMUSERGROUP→BWMRULE 逐层回查，验证带宽控制策略完整且绑定关系正确 |
| phase | verify |
| input_artifacts | ["UserProfile 名称", "BWM 对象名称列表"] |
| output_artifacts | ["BWM 全链路回查结果"] |
| command | `LST RULEBINDING:USERPROFILENAME="up_bwmcontrol",POLICYTYPE=BWM;`<br>`LST RULE:RULENAME="ruleA";`<br>`LST CATEGORYPROP:CATEPROPNAME="catropA";`<br>`LST BWMSERVICE:BWMSERVICENAME="bwmservA";`<br>`LST BWMCONTROLLER:BWMCNAME="bwmcontrolA";`<br>`LST BWMUSERGROUP:QRYUSRGRPTYPE=SPECIFIC_GROUP,USERGROUPNAME="bwmgrpA";`<br>`LST BWMRULE:USERGROUPTYPE=SPECIFIC_GROUP,USERGROUPNAME="bwmgrpA",BWMRULETYPE=SUBSCRIBER_SPECIFIC,BWMRULENAME="bwmruleA";` |
| config_object | `USERPROFILE`, `RULEBINDING`, `RULE`, `CATEGORYPROP`, `BWMSERVICE`, `BWMCONTROLLER`, `BWMUSERGROUP`, `BWMRULE` |
| source_evidence_ids | ["套餐2_94838085"] |
| status | active |

**说明**：回查路径共八层对象。验证要点：(1) RULEBINDING 中 POLICYTYPE=BWM 的规则均已绑定；(2) RULE 的 POLICYNAME 指向的 CATEGORYPROP 存在；(3) BWMSERVICE 的 CATEPROPNAME 与 RULE 引用一致；(4) BWMCONTROLLER 的 CTRLTYPE 与速率参数符合规划；(5) BWMUSERGROUP 优先级正确；(6) BWMRULE 将 USERGROUP+SERVICE+CONTROLLER 正确关联。此任务仅用于 DS-03（带宽控制）。
