# 在线计费 MVP 业务图谱实例

## 文档说明

本文档是业务图谱 Schema 的**完整 MVP 实例化**——用一个具体的在线计费案例，将12种Schema对象全部实例化，并严格填充所有关系边（含07a扩展的5条新边）。

**目标读者**：需要理解"业务图谱到底能干什么"的产品/技术决策者。

**案例场景**：

> 某运营商需要为5G用户配置在线计费策略：
> - **视频业务**：访问华为视频网站(video.huawei.com)，按**流量**(VOLUME)在线计费，RG=100
> - **IM消息**：所有IM类协议流量，按**时长**(DURATION)在线计费，RG=200
> - **默认流量**：未命中上述规则的流量，在线计费，RG=300
> - **配额耗尽动作**：阻断(BLOCK)
>
> 匹配方式：视频走L7层URL匹配，IM走L34层协议匹配，默认走any匹配。

**来源**：
- Schema 标准：`business-graph-schema.md`
- 扩展标准：`07a-schema-extension-decision-driven.md`
- 已有实例：`SKILL/knowledge/计费场景业务图谱.md`、`07b-charging-instance-decision-driven.md`
- 原始文档：`SKILL/feature/UDG/UPF/GWFD-020300/`、`SKILL/knowledge/计费知识库.md`

---

## 1. 案例全景图

本MVP实例包含以下Schema对象实例：

| 层 | Schema | 实例数 | 本案例实例 |
|----|--------|--------|-----------|
| 业务层 | BusinessDomain | 1 | 业务感知 |
| 业务层 | NetworkScenario | 1 | NS-01 计费场景 |
| 业务层 | DeliverySolution | 1 | DS-01 差异化计费组合方案 |
| 业务层 | EngineeringTask | 13 | 5 plan + 5 execute + 3 verify |
| 支撑层 | Participant | 4 | SMF, UPF, CHF/OCS, UE（在线计费子集） |
| 支撑层 | Scope | 3 | 用户级/APN/UserProfile |
| 支撑层 | DecisionPoint | 3 | DP-01(计费方式), DP-02(配额动作), DP-03(匹配层次) |
| 支撑层 | ValidationPlan | 1 | VP-01 差异化计费验收 |
| 支撑层 | BusinessRule | 6 | 在线计费相关规则子集 |
| 桥接层 | DomainSemanticObject | 6 | 过滤/规则/计费/配额/优先级/验证 |
| 桥接层 | Feature | 6 | 在线计费特性栈 |
| 桥接层 | ConfigObject | 15 | 从IPLIST到REFRESHSRV的完整配置对象链 |

**关系边统计**（本案例实际使用的关系）：

| 关系类型 | 标准边数 | 扩展边数 | 本案例使用 |
|---------|---------|---------|-----------|
| 业务主链 | 3 | 0 | 3 |
| 方案到支撑 | 7 | 0 | 7 |
| 验收内部 | 2 | 0 | 2 |
| 向下桥接 | 4 | 0 | 4 |
| Task相关 | 3 | 0 | 3 |
| 决策驱动(07a) | 0 | 5 | 5 |
| **合计** | **19** | **5** | **24** |

---

## 2. 决策点选择（MVP前提）

在实例化之前，先确定本案例在每个DecisionPoint上的选择，因为后续所有参数和任务编排都由此决定。

### 2.1 DP-01：计费方式选择 → **在线计费**

| 决策项 | 选择 | 影响 |
|-------|------|------|
| 计费方式 | **在线计费** | URR.USAGERPTMODE=ONLINE, ONLMETERINGTYPE 生效 |
| 配额控制 | 需要CCT模板 | SMF侧需配置 CCT/CHFINIT |
| CDR上报 | 通过N4→SMF→OCS | 不经过CG |

**由此决策驱动的参数绑定（parameter_binding）**：

| 目标ConfigObject | 参数 | 值 | 来源 |
|-----------------|------|-----|------|
| URR(视频) | USAGERPTMODE | ONLINE | DP-01=在线 |
| URR(视频) | ONLMETERINGTYPE | VOLUME | DP-01=在线 + Feature=流量计费 |
| URR(IM) | USAGERPTMODE | ONLINE | DP-01=在线 |
| URR(IM) | ONLMETERINGTYPE | DURATION | DP-01=在线 + Feature=时长计费 |
| URR(默认) | USAGERPTMODE | ONLINE | DP-01=在线 |
| URR(默认) | ONLMETERINGTYPE | VOLUME | DP-01=在线（默认按流量） |

**由此决策驱动的任务门控（gates）**：

| Task | 门控状态 | 原因 |
|------|---------|------|
| T-PLAN-005(规划配额耗尽动作) | **active** | 在线计费需要规划配额耗尽后的动作 |
| T-EXEC-005(配置计费动作链) | **active** | 在线计费需创建URR/URRGROUP/PCCPOLICYGRP |

### 2.2 DP-02：配额耗尽后动作 → **BLOCK**

| 决策项 | 选择 | 影响 |
|-------|------|------|
| 耗尽动作 | **BLOCK** | 需要PCCACTIONPROP(门控策略) |

本案例选择BLOCK，意味着：
- PCCPOLICYGRP(默认) 需要额外绑定 PCCACTIONPROP
- 在线计费配额耗尽后，流量将被阻断

### 2.3 DP-03：匹配层次选择 → **混合匹配**

本案例中3条业务的匹配层次不同：

| 业务 | 匹配层次 | 影响 |
|------|---------|------|
| 视频业务 | **L7层URL匹配** | 需要L7FILTER + PROTBINDFLOWF |
| IM消息 | **L34层协议匹配** | 仅需FILTER，PROTBINDFLOWF绑定协议名 |
| 默认流量 | **L34层匹配(ANY)** | 仅需FILTER(L34PROTOCOL=ANY) |

**由此决策驱动的任务门控**：

| Task | 业务 | 门控状态 | 原因 |
|------|------|---------|------|
| T-EXEC-003(配置七层过滤条件) | 视频 | **active** | 需要L7FILTER |
| T-EXEC-003(配置七层过滤条件) | IM | **skip** | 不需要L7FILTER |
| T-EXEC-003(配置七层过滤条件) | 默认 | **skip** | 不需要L7FILTER |
| T-EXEC-001(配置IP地址列表) | 全部 | **skip** | 不需要特定IP匹配 |

---

## 3. 业务层主链

### 3.1 BusinessDomain：业务感知

| 字段 | 值 |
|------|-----|
| domain_id | `service-awareness` |
| domain_name | 业务感知 |
| domain_summary | 在用户会话过程中，对用户的数据报文进行解析，从而区分出用户使用的不同业务，以实现策略控制和计费控制 |
| status | accepted |

### 3.2 NetworkScenario：NS-01 计费场景

| 字段 | 值 |
|------|-----|
| scenario_id | `NS-01` |
| scenario_name | 计费场景 |
| scenario_summary | 对不同业务流采用不同计费方式，结合默认计费、免费业务和配额动作完成计费闭环 |
| judgment_basis | 用户需要按业务粒度差异化计费（离线/在线/融合），或需要按流量/时长/事件统计特定业务的使用量 |
| typical_outcome | 专项业务单独计费、免费业务不计费、普通业务默认计费，配额耗尽后切换到阻断或重定向 |
| source_evidence_ids | `["套餐1_93112148","计费解决方案概述_90776649"]` |
| status | active |

### 3.3 DeliverySolution：DS-01 差异化计费组合方案

| 字段 | 值 |
|------|-----|
| solution_id | `DS-01` |
| solution_name | 差异化计费组合方案（含配额分支） |
| solution_summary | 通过过滤条件识别业务流，按优先级裁决Rule，绑定PCC/URR计费链实现差异化计费，配额耗尽后通过BLOCK动作阻断 |
| core_mechanism_combo | `L7FILTER(视频URL) + FILTER(IM协议/ANY) + Rule优先级裁决 + PCC/URR在线计费链(PCCPOLICYGRP-URRGROUP-URR, USAGERPTMODE=ONLINE) + 默认URR组兜底 + BLOCK配额耗尽动作` |
| source_evidence_ids | `["套餐1_93112148","GWFD-020300_66347600","配置Gy接口在线计费_83167737"]` |
| status | active |

### 3.4 EngineeringTask（13个）

> 以下Task直接复用 `计费场景业务图谱.md` 中的定义，这里只标注本案例中的**具体行为**。

#### 3.4.1 Plan 阶段（5个）

**T-PLAN-001 规划生效范围**

本案例具体行为：
- 确定UserProfile名称：`up_online_charging`
- 确定DNN：`internet`
- 确定默认URR组：`urrg_default`

| 字段 | 值 |
|------|-----|
| task_id | T-PLAN-001 |
| task_name | 规划生效范围 |
| phase | plan |
| input_artifacts | ["用户范围：5G普通用户","DNN：internet","默认策略：在线计费兜底"] |
| output_artifacts | ["UserProfile=up_online_charging","DFTURRGRPNAME=urrg_default","DFTSIGURRGNAME=urrg_default"] |
| command | - |
| config_object | - |

**T-PLAN-002 规划识别条件**

本案例具体行为：
- 视频业务：L7 URL匹配 `video.huawei.com/*` → L7FILTER
- IM消息：L34协议匹配 IM协议组 → PROTBINDFLOWF
- 默认流量：L34 ANY匹配 → FILTER

| 字段 | 值 |
|------|-----|
| task_id | T-PLAN-002 |
| task_name | 规划识别条件 |
| phase | plan |
| input_artifacts | ["视频：访问video.huawei.com","IM：IM类协议流量","默认：所有流量"] |
| output_artifacts | ["L7FILTER(l7_video) for 视频","FILTER+PROTBINDFLOWF(IM协议) for IM","FILTER(any) for 默认"] |
| command | - |
| config_object | - |

**T-PLAN-003 规划Rule与优先级**

本案例具体行为：

| Rule | FLOWFILTER | PCCPOLICYGRP | PRIORITY | 说明 |
|------|-----------|-------------|----------|------|
| Rule_video | ff_video | PPG_video | 100 | L7匹配，优先级最高 |
| Rule_im | ff_im | PPG_im | 200 | 协议匹配 |
| Rule_default | ff_any | PPG_default | 65000 | 兜底，优先级最低 |

| 字段 | 值 |
|------|-----|
| task_id | T-PLAN-003 |
| task_name | 规划Rule与优先级 |
| phase | plan |
| input_artifacts | ["3条业务目标","无交集（各自独立）"] |
| output_artifacts | ["Rule层次：视频(100) > IM(200) > 兜底(65000)","无OR条件"] |
| command | - |
| config_object | - |

**T-PLAN-004 规划计费对象与费率标识**

本案例具体行为——规划3套独立三件套：

| 业务 | URR名称 | URRID | USAGERPTMODE | ONLMETERINGTYPE | RG | URRGROUP | PCCPOLICYGRP |
|------|---------|-------|-------------|----------------|-----|----------|-------------|
| 视频 | urr_video | 1001 | ONLINE | VOLUME | 100 | urrg_video | PPG_video |
| IM | urr_im | 1002 | ONLINE | DURATION | 200 | urrg_im | PPG_im |
| 默认 | urr_default | 1003 | ONLINE | VOLUME | 300 | urrg_default | PPG_default |

> URRID从1001开始，RG值需与SMF侧一致。

| 字段 | 值 |
|------|-----|
| task_id | T-PLAN-004 |
| task_name | 规划计费对象与费率标识 |
| phase | plan |
| input_artifacts | ["视频：按流量,RG=100","IM：按时长,RG=200","默认：按流量,RG=300","全部在线计费"] |
| output_artifacts | ["3套URR→URRGROUP→PCCPOLICYGRP三件套规划","URRID分配表","RG与SMF对齐方案"] |
| command | - |
| config_object | - |
| output_cardinality | - |

**T-PLAN-005 规划配额耗尽动作**

本案例具体行为：
- DP-02=BLOCK → 需创建 PCCACTIONPROP(门控策略)
- 配额耗尽后，PCCPOLICYGRP(默认) 绑定的 PCCACTIONPROP 生效，阻断流量

| 字段 | 值 |
|------|-----|
| task_id | T-PLAN-005 |
| task_name | 规划配额耗尽动作 |
| phase | plan |
| input_artifacts | ["配额控制要求：需要","DP-02选择：BLOCK"] |
| output_artifacts | ["PCCACTIONPROP=pccact_block(门控策略)","绑定到PPG_default"] |
| command | - |
| config_object | - |
| gates状态 | **active**（在线计费需要配额规划） |

#### 3.4.2 Execute 阶段（5个活跃 + 2个skip）

**T-EXEC-001 配置IP地址列表 → SKIP**

| gates状态 | **skip** |
|-----------|----------|
| 原因 | 本案例无特定IP匹配需求，全部业务使用协议/URL匹配 |

**T-EXEC-002 配置三四层过滤条件**

本案例创建2个FILTER：

```
// 默认流量 - ANY匹配
ADD FILTER:FILTERNAME="filter_any",L34PROTTYPE=STRING,L34PROTOCOL=ANY;

// IM消息 - 协议匹配（由PROTBINDFLOWF指定具体协议）
ADD FILTER:FILTERNAME="filter_im",L34PROTTYPE=STRING,L34PROTOCOL=ANY;
```

| 字段 | 值 |
|------|-----|
| task_id | T-EXEC-002 |
| task_name | 配置三四层过滤条件 |
| phase | execute |
| input_artifacts | ["过滤条件规划表"] |
| output_artifacts | ["filter_any(FILTER)","filter_im(FILTER)"] |
| command | `ADD FILTER:...` |
| config_object | FILTER |
| output_cardinality | M=2(FILTER数量) |

**T-EXEC-003 配置七层过滤条件**

本案例创建1个L7FILTER（视频URL）：

```
ADD L7FILTER:L7FILTERNAME="l7_video",URLTYPE=URL,URL="video.huawei.com/*";
```

| 字段 | 值 |
|------|-----|
| task_id | T-EXEC-003 |
| task_name | 配置七层过滤条件 |
| phase | execute |
| input_artifacts | ["L7过滤条件规划表"] |
| output_artifacts | ["l7_video(L7FILTER)"] |
| command | `ADD L7FILTER:...` |
| config_object | L7FILTER |
| output_cardinality | K=1(仅视频需要L7) |
| gates状态 | **active**（视频业务需要L7FILTER） |

**T-EXEC-004 配置流过滤器与绑定**

本案例创建3个FLOWFILTER及绑定：

```
// 视频业务：L34 ANY + L7 URL
ADD FLOWFILTER:FLOWFILTERNAME="ff_video";
ADD FLTBINDFLOWF:FLOWFILTERNAME="ff_video",FILTERNAME="filter_any";
ADD PROTBINDFLOWF:FLOWFILTERNAME="ff_video",PROTOCOLNAME="http",L7FILTERNAME="l7_video";

// IM消息：L34 ANY + 协议绑定(无L7FILTER)
ADD FLOWFILTER:FLOWFILTERNAME="ff_im";
ADD FLTBINDFLOWF:FLOWFILTERNAME="ff_im",FILTERNAME="filter_im";
ADD PROTBINDFLOWF:FLOWFILTERNAME="ff_im",PROTOCOLNAME="im";

// 默认流量：L34 ANY only
ADD FLOWFILTER:FLOWFILTERNAME="ff_any";
ADD FLTBINDFLOWF:FLOWFILTERNAME="ff_any",FILTERNAME="filter_any";
```

| 字段 | 值 |
|------|-----|
| task_id | T-EXEC-004 |
| task_name | 配置流过滤器与绑定 |
| phase | execute |
| input_artifacts | ["FILTER对象","L7FILTER对象(视频)","协议规划(IM)"] |
| output_artifacts | ["ff_video(FLOWFILTER+FLTBINDFLOWF+PROTBINDFLOWF)","ff_im(FLOWFILTER+FLTBINDFLOWF+PROTBINDFLOWF)","ff_any(FLOWFILTER+FLTBINDFLOWF)"] |
| command | `ADD FLOWFILTER:...; ADD FLTBINDFLOWF:...; ADD PROTBINDFLOWF:...;` |
| config_object | FLOWFILTER, FLTBINDFLOWF, PROTBINDFLOWF |
| output_cardinality | S=3(FLOWFILTER), 3(FLTBINDFLOWF), 2(PROTBINDFLOWF, 仅视频和IM) |

**T-EXEC-005 配置计费动作链**

本案例创建3套三件套 + 1个PCCACTIONPROP：

```
// === 视频业务：按流量在线计费 ===
ADD URR:URRNAME="urr_video",URRID=1001,USAGERPTMODE=ONLINE,ONLMETERINGTYPE=VOLUME,RG=100;
ADD URRGROUP:URRGROUPNAME="urrg_video",UPURRNAME1="urr_video",DOWNURRNAME1="urr_video";
ADD PCCPOLICYGRP:PCCPOLICYGRPNM="PPG_video",URRGROUPNAME="urrg_video";

// === IM消息：按时长在线计费 ===
ADD URR:URRNAME="urr_im",URRID=1002,USAGERPTMODE=ONLINE,ONLMETERINGTYPE=DURATION,RG=200;
ADD URRGROUP:URRGROUPNAME="urrg_im",UPURRNAME1="urr_im",DOWNURRNAME1="urr_im";
ADD PCCPOLICYGRP:PCCPOLICYGRPNM="PPG_im",URRGROUPNAME="urrg_im";

// === 默认计费：按流量在线 + 配额耗尽BLOCK ===
ADD URR:URRNAME="urr_default",URRID=1003,USAGERPTMODE=ONLINE,ONLMETERINGTYPE=VOLUME,RG=300;
ADD URRGROUP:URRGROUPNAME="urrg_default",UPURRNAME1="urr_default",DOWNURRNAME1="urr_default";
ADD PCCACTIONPROP:PCCACTPROPNM="pccact_block",GATINGSTATUS=CLS;
ADD PCCPOLICYGRP:PCCPOLICYGRPNM="PPG_default",URRGROUPNAME="urrg_default",PCCACTPROPNAME="pccact_block";
```

| 字段 | 值 |
|------|-----|
| task_id | T-EXEC-005 |
| task_name | 配置计费动作链 |
| phase | execute |
| input_artifacts | ["三件套规划表","PCCACTIONPROP规划"] |
| output_artifacts | ["3个URR + 3个URRGROUP + 3个PCCPOLICYGRP + 1个PCCACTIONPROP"] |
| command | `ADD URR:...; ADD URRGROUP:...; ADD PCCPOLICYGRP:...;` |
| config_object | URR, URRGROUP, PCCPOLICYGRP, PCCACTIONPROP |
| output_cardinality | URR: N+2=3+2=5(实际本案例3+0=3,无融合); URRGROUP: N+2=3(但实际只需3); PCCPOLICYGRP: N+1=3 |

> output_cardinality 公式说明：N=特定业务数。本案例N=2(视频+IM)，+1兜底=3套。
> 融合模式时URR数量为2N+2（每业务2个），单一在线模式为N+2（每业务1个+兜底+异常）。
> 本案例在线单一模式，3个URR(每业务1个)。

**T-EXEC-008 配置Rule**

本案例创建3个RULE：

```
ADD RULE:RULENAME="Rule_video",POLICYTYPE=PCC,FILTERINGMODE=FLOWFILTER,FLOWFILTERNAME="ff_video",PRIORITY=100,POLICYNAME="PPG_video";
ADD RULE:RULENAME="Rule_im",POLICYTYPE=PCC,FILTERINGMODE=FLOWFILTER,FLOWFILTERNAME="ff_im",PRIORITY=200,POLICYNAME="PPG_im";
ADD RULE:RULENAME="Rule_default",POLICYTYPE=PCC,FILTERINGMODE=FLOWFILTER,FLOWFILTERNAME="ff_any",PRIORITY=65000,POLICYNAME="PPG_default";
```

| 字段 | 值 |
|------|-----|
| task_id | T-EXEC-008 |
| task_name | 配置Rule |
| phase | execute |
| input_artifacts | ["FLOWFILTER配置","PCCPOLICYGRP配置","优先级规划"] |
| output_artifacts | ["Rule_video(P100)","Rule_im(P200)","Rule_default(P65000)"] |
| command | `ADD RULE:...` |
| config_object | RULE |
| output_cardinality | S=3 |

**T-EXEC-010 配置UserProfile与Rule绑定**

```
ADD USERPROFILE:USERPROFILENAME="up_online_charging";
SET URRGRPBINDING:USERPROFILENAME="up_online_charging",DFTURRGRPNAME="urrg_default",DFTSIGURRGNAME="urrg_default";
ADD RULEBINDING:USERPROFILENAME="up_online_charging",POLICYTYPE=PCC,RULENAME="Rule_video";
ADD RULEBINDING:USERPROFILENAME="up_online_charging",POLICYTYPE=PCC,RULENAME="Rule_im";
ADD RULEBINDING:USERPROFILENAME="up_online_charging",POLICYTYPE=PCC,RULENAME="Rule_default";
SET REFRESHSRV:REFRESHTYPE=ALL;
```

| 字段 | 值 |
|------|-----|
| task_id | T-EXEC-010 |
| task_name | 配置UserProfile与Rule绑定 |
| phase | execute |
| input_artifacts | ["RULE配置","URRGROUP配置","UserProfile规划"] |
| output_artifacts | ["up_online_charging(USERPROFILE)","3个RULEBINDING","URRGRPBINDING","REFRESHSRV"] |
| command | `ADD USERPROFILE:...; SET URRGRPBINDING:...; ADD RULEBINDING:...; SET REFRESHSRV:...;` |
| config_object | USERPROFILE, URRGRPBINDING, RULEBINDING, REFRESHSRV |

#### 3.4.3 Verify 阶段（3个）

**T-VERIFY-001 验证License开关**

```
LST LICENSESWITCH:LICITEM="LKV3G5SABS01";
LST LICENSESWITCH:LICITEM="LKV3G5BCBC01";
LST LICENSESWITCH:LICITEM="LKV3G5PCCB01";
LST LICENSESWITCH:LICITEM="LKV3G5OLCH01";
```

> 在线计费额外需要 LKV3G5OLCH01（来源：GWFD-020300特性概述）

**T-VERIFY-002 验证配置链逐层回查**

从 `up_online_charging` 出发，逐层回查：
```
LST RULEBINDING:USERPROFILENAME="up_online_charging";
// 应返回3条RULEBINDING: Rule_video, Rule_im, Rule_default
LST RULE:RULENAME="Rule_video",POLICYTYPE=PCC;
// POLICYNAME=PPG_video, FLOWFILTERNAME=ff_video, PRIORITY=100
LST PCCPOLICYGRP:PCCPOLICYGRPNM="PPG_video";
// URRGROUPNAME=urrg_video
LST URRGROUP:URRGROUPNAME="urrg_video";
// UPURRNAME1=urr_video, DOWNURRNAME1=urr_video
LST URR:URRNAME="urr_video";
// URRID=1001, USAGERPTMODE=ONLINE, ONLMETERINGTYPE=VOLUME, RG=100
// （对Rule_im和Rule_default重复上述回查）
```

**T-VERIFY-003 验证PFCP会话上报与计费流量**

通过OM Portal抓取PFCP Session Report，验证Usage Report中URRID=1001/1002/1003与配置一致。

#### 3.4.4 任务编排顺序

```
T-PLAN-001 → T-PLAN-002 → T-PLAN-003 → T-PLAN-004 → T-PLAN-005
→ [SKIP T-EXEC-001]
→ T-EXEC-002 → T-EXEC-003 → T-EXEC-004 → T-EXEC-005 → T-EXEC-008 → T-EXEC-010
→ T-VERIFY-001 → T-VERIFY-002 → T-VERIFY-003
```

> 注意：T-EXEC-001(IPLIST)被DP-03的门控跳过，T-EXEC-003(L7FILTER)仅创建1个。

---

## 4. 支撑层

### 4.1 Participant（在线计费参与方，4个）

> 从06文件的10个参与方中，选取在线计费场景涉及的4个。

| participant_id | participant_name | participant_type | plane_or_side | responsibility_summary | 在线计费中的角色 |
|------|------|------|------|------|------|
| P-02 | SMF | network_function | control_plane | 编排计费策略、与OCS交互、下发计费规则到UPF、配额管理 | 在线计费核心：管理配额、与OCS/Gy接口交互、通过N4下发URR到UPF |
| P-03 | UPF | network_function | user_plane | 业务识别、流量统计、执行计费规则、上报使用量 | 执行计费策略：按URR统计流量/时长、通过N4上报Usage Report |
| P-04 | CHF/OCS | external_system | external | 处理计费请求、配额分配、重授权触发 | 在线计费专用：通过Gy接口提供配额、处理实时扣费、配额耗尽触发重授权 |
| P-05 | UE/用户 | endpoint | terminal_side | 发起会话与业务访问，产生待计费业务流 | 产生视频/IM/默认三类待计费流量 |

> 与离线计费的区别：不需要 P-10(CG)，因为在线计费不走CDR离线通道。P-01(PCF)在静态规则场景下不参与。

### 4.2 Scope（生效范围，3个）

| scope_id | scope_name | scope_type | scope_expression | scope_summary | 本案例实例化 |
|------|------|------|------|------|------|
| S-01 | 用户级范围 | subscriber | 普通5G用户 | 计费策略按用户粒度生效 | 所有开通数据业务的5G用户 |
| S-02 | APN/DNN范围 | access | internet | 计费策略按接入点或数据网名称生效 | DNN=internet的会话 |
| S-06 | UserProfile承载范围 | subscription | up_online_charging | 承载规则绑定和默认计费组 | UserProfile=up_online_charging |

### 4.3 DecisionPoint（3个，已在§2详细展开）

| decision_id | decision_name | 挂载层级 | 本案例选择 | 影响摘要 |
|------|------|------|---------|---------|
| DP-01 | 计费方式选择 | NS-01 | **在线计费** | URR.USAGERPTMODE=ONLINE, 需CCT模板, 需配额管理 |
| DP-02 | 配额耗尽后动作选择 | DS-01 | **BLOCK** | 需PCCACTIONPROP(门控), PPG_default绑定pccact_block |
| DP-03 | 匹配层次选择 | DS-01 | **混合匹配** | 视频=L7URL, IM=L34协议, 默认=L34ANY |

**DP-03 的具体选项-影响映射**：

| DP-03选项 | 影响的ConfigObject | 本案例是否使用 |
|-----------|-------------------|-------------|
| L34层匹配(ANY) | FILTER+FLTBINDFLOWF，无PROTBINDFLOWF | 默认流量使用 |
| L34层协议匹配 | FILTER+PROTBINDFLOWF(PROTOCOLNAME)，无L7FILTERNAME | IM消息使用 |
| L7层URL匹配 | FILTER+PROTBINDFLOWF+L7FILTERNAME | 视频业务使用 |
| L34+L7混合 | 两种绑定都用 | 视频业务本质上也是混合 |

### 4.4 ValidationPlan（1个）

| 字段 | 值 |
|------|-----|
| validation_id | VP-01 |
| validation_name | 在线计费差异化验收 |
| validation_goal | 确认在线计费链完整、URR参数正确、配额动作生效、PFCP上报一致 |
| target_objects | `["LICENSESWITCH(LKV3G5SABS01+LKV3G5BCBC01+LKV3G5PCCB01+LKV3G5OLCH01)","RULEBINDING(3条)","RULE(3条)","URR(3个,USAGERPTMODE=ONLINE)","PCCPOLICYGRP(3个)","PCCACTIONPROP(pccact_block)","PFCP Session Report"]` |
| pass_condition | License全部ENABLE + 3套三件套完整 + RG值与规划一致 + PCCACTIONPROP绑定正确 + URRID与PFCP上报一致 |
| expected_result | 视频流量走VOLUME(RG=100)、IM流量走DURATION(RG=200)、默认走VOLUME(RG=300)，配额耗尽后流量被BLOCK |
| source_evidence_ids | `["GWFD-020300_66347600","配置Gy接口在线计费_83167737"]` |
| status | active |

### 4.5 BusinessRule（6个，在线计费相关子集）

| rule_id | rule_name | rule_type | check_target | check_logic | 本案例验证点 |
|---------|-----------|-----------|-------------|-------------|------------|
| BR-01 | SA基础+在线计费License开启断言 | constraint_rule | LICENSESWITCH | LKV3G5SABS01 + LKV3G5BCBC01 + LKV3G5PCCB01 + LKV3G5OLCH01 必须ENABLE | 4个License必须开启 |
| BR-02 | 配置链逐层一致性校验 | validation_rule | RULEBINDING→RULE→PCCPOLICYGRP→URRGROUP→URR→FLOWFILTER→FILTER | 各层名称与规划一致 | 3条链回查 |
| BR-03 | PFCP Usage Report一致性校验 | validation_rule | PFCP Session Report / URR ID | URRID(1001/1002/1003)与配置一致 | 3个URRID匹配 |
| BR-04 | CP/UP URR一致性诊断 | diagnosis_rule | SMF侧URR vs UPF侧URR | URR名称、RG值、URRID在SMF和UPF侧一致 | RG=100/200/300跨侧一致 |
| BR-05 | URRID全局唯一约束 | constraint_rule | 所有URR | URRID(1001/1002/1003)不重复 | 3个ID互不相同 |
| BR-06 | 默认URR组必须配置 | constraint_rule | URRGRPBINDING | DFTURRGRPNAME和DFTSIGURRGNAME必须同时配置 | 均为urrg_default |

> 相比完整计费场景的9条规则，在线计费MVP中省略了 BR-07(RG跨侧约束)和BR-09(PROTBINDFLOWF协议约束)——这些在更复杂场景下才需要。BR-08(REFRESHSRV时序)保留为隐含约束。

---

## 5. 桥接层

### 5.1 DomainSemanticObject（6个，在线计费子集）

| 语义对象 | 定义 | 在本案例中的含义 | 落地ConfigObject |
|---------|------|----------------|-----------------|
| BA.FilterCondition | 如何组织成可匹配条件 | 视频用L7 URL，IM用协议，默认用ANY | FILTER, L7FILTER, FLOWFILTER |
| BA.Rule | 最小组织单元 | 3条Rule：视频/IM/默认，优先级裁决 | RULE(POLICYTYPE=PCC) |
| BA.Charging | 如何按业务收费 | 在线计费：3套URR/URRGROUP/PCCPOLICYGRP，USAGERPTMODE=ONLINE | URR, URRGROUP, PCCPOLICYGRP |
| BA.Quota | 如何处理配额 | 在线计费配额管理，耗尽后BLOCK | PCCACTIONPROP, DFTQUOTAVOLUME |
| BA.Priority | 多规则裁决 | 视频(100) > IM(200) > 默认(65000) | RULE.PRIORITY |
| BA.ValidationDiagnosis | 如何验证 | License→链回查→PFCP上报三级验证 | LST全链路, PFCP Session Report |

### 5.2 Feature（6个，在线计费特性栈）

> 严格按特性依赖关系列出。

| feature_id | feature_name | 正式能力定位 | 依赖关系 | License | 本案例角色 |
|------------|-------------|-------------|---------|---------|-----------|
| GWFD-110101 | SA-Basic | 识别底座 | 无（根特性） | LKV3G5SABS01 | 前提：提供报文解析和协议识别能力 |
| GWFD-020351 | PCC基本功能 | 用户面策略执行骨架 | 独立于内容计费 | LKV3G5PCCB01 | 前提：提供RULE/PCCPOLICYGRP框架 |
| GWFD-020301 | 内容计费基本功能 | 内容计费能力底座 | → GWFD-110101 | LKV3G5BCBC01 | 前提：提供按业务粒度差异化计费能力 |
| GWFD-020300 | 在线计费 | 在线配额控制 | → GWFD-020301 | LKV3G5OLCH01 | **核心**：在线计费主特性，提供ONLINE模式和配额管理 |
| GWFD-020303 | 基于业务流量的计费 | 按流量统计 | → GWFD-020301 | LKV3G5VBCS01 | 视频+默认：ONLMETERINGTYPE=VOLUME |
| GWFD-020302 | 基于业务时长的计费 | 按时长统计 | → GWFD-020301 | LKV3G5TBCS01 | IM：ONLMETERINGTYPE=DURATION |

特性依赖树：
```
GWFD-110101 (SA-Basic)
  └→ GWFD-020301 (内容计费)
       ├→ GWFD-020300 (在线计费) ← 本案例核心
       ├→ GWFD-020303 (流量计费) ← 视频+默认
       └→ GWFD-020302 (时长计费) ← IM

GWFD-020351 (PCC) — 独立
```

### 5.3 ConfigObject（15个，完整配置对象链）

| 对象链位置 | 关键对象 | 所属侧别 | 业务作用 | 本案例实例 |
|-----------|---------|---------|---------|-----------|
| 识别层 | FILTER | UDG/UPF | 三四层过滤条件 | filter_any, filter_im (2个) |
| 识别层 | L7FILTER | UDG/UPF | 七层URL匹配 | l7_video (1个) |
| 识别组合层 | FLOWFILTER | UDG/UPF | 流过滤器 | ff_video, ff_im, ff_any (3个) |
| 识别绑定层 | FLTBINDFLOWF | UDG/UPF | FILTER→FLOWFILTER绑定 | 3个(跟随FLOWFILTER) |
| 识别绑定层 | PROTBINDFLOWF | UDG/UPF | 协议+L7→FLOWFILTER绑定 | 2个(视频+IM，默认无) |
| 计费对象层 | URR | UDG/UPF + UNC/SMF | 使用量统计与计费标识 | urr_video, urr_im, urr_default (3个) |
| 计费组合层 | URRGROUP | UDG/UPF + UNC/SMF | 组合上下行URR | urrg_video, urrg_im, urrg_default (3个) |
| 策略组层 | PCCPOLICYGRP | UDG/UPF + UNC/SMF | 封装URRGROUP为策略组 | PPG_video, PPG_im, PPG_default (3个) |
| 动作属性层 | PCCACTIONPROP | UDG/UPF | 门控/阻断动作 | pccact_block (1个，配额耗尽BLOCK) |
| 规则层 | RULE | UDG/UPF + UNC/SMF | 匹配条件+策略动作+优先级 | Rule_video, Rule_im, Rule_default (3个) |
| 策略容器层 | USERPROFILE | UDG/UPF + UNC/SMF | 承载规则和默认策略 | up_online_charging (1个) |
| 绑定层 | RULEBINDING | UDG/UPF + UNC/SMF | RULE绑定到USERPROFILE | 3个(跟随RULE) |
| 默认计费层 | URRGRPBINDING | UDG/UPF + UNC/SMF | 默认计费组绑定 | 1个(DFTURRGRPNAME=urrg_default) |
| 刷新层 | REFRESHSRV | UDG/UPF | 刷新使配置生效 | 1个(最后执行) |

**依赖顺序（本案例实际执行的创建顺序）**：

```
FILTER(filter_any, filter_im)
  → L7FILTER(l7_video)
    → FLOWFILTER(ff_video, ff_im, ff_any)
      → FLTBINDFLOWF(3个)
        → PROTBINDFLOWF(2个: 视频+IM)
          → URR(urr_video, urr_im, urr_default)
            → URRGROUP(urrg_video, urrg_im, urrg_default)
              → PCCACTIONPROP(pccact_block)
                → PCCPOLICYGRP(PPG_video, PPG_im, PPG_default)
                  → RULE(Rule_video, Rule_im, Rule_default)
                    → USERPROFILE(up_online_charging)
                      → URRGRPBINDING
                        → RULEBINDING(3个)
                          → REFRESHSRV
```

---

## 6. 决策驱动关系（07a 扩展，核心创新点）

> 这是业务图谱区别于普通知识库的关键——决策点不再只是文字描述，而是**结构化地驱动参数赋值、任务门控和对象组合**。

### 6.1 E1: DecisionPoint --parameter_binding--> ConfigObject

#### 6.1.1 DP-01(在线计费) → URR 参数绑定

| DP选项 | 目标ConfigObject | 参数 | 值 | 附带影响 |
|--------|-----------------|------|-----|---------|
| 在线计费 | URR(urr_video) | USAGERPTMODE | ONLINE | ONLMETERINGTYPE生效 |
| 在线计费 | URR(urr_video) | ONLMETERINGTYPE | VOLUME | 按流量统计 |
| 在线计费 | URR(urr_im) | USAGERPTMODE | ONLINE | ONLMETERINGTYPE生效 |
| 在线计费 | URR(urr_im) | ONLMETERINGTYPE | DURATION | 按时长统计 |
| 在线计费 | URR(urr_default) | USAGERPTMODE | ONLINE | ONLMETERINGTYPE生效 |
| 在线计费 | URR(urr_default) | ONLMETERINGTYPE | VOLUME | 默认按流量 |
| 在线计费 | URRGROUP(urrg_video) | UPURRNAME2/DOWNURRNAME2 | urr_video | 在线模式用NAME2槽位 |
| 在线计费 | URRGROUP(urrg_im) | UPURRNAME2/DOWNURRNAME2 | urr_im | 在线模式用NAME2槽位 |
| 在线计费 | URRGROUP(urrg_default) | UPURRNAME2/DOWNURRNAME2 | urr_default | 在线模式用NAME2槽位 |

> **注意**：实际配置中UPURRNAME1和UPURRNAME2只是编号，不区分优先级。在线单一模式时通常用NAME1。此处标注NAME2是为了与07b中"在线=NAME2, 离线=NAME1"的约定保持一致。

#### 6.1.2 DP-02(BLOCK) → PCCPOLICYGRP 参数绑定

| DP选项 | 目标ConfigObject | 影响 |
|--------|-----------------|------|
| BLOCK | PCCPOLICYGRP(PPG_default) | 需绑定PCCACTIONPROPNAME="pccact_block"，GATINGSTATUS=CLS |
| REDIRECT | PCCPOLICYGRP(PPG_default) | 需绑定REDIRECT对象（本案例未选） |
| FORWARD | PCCPOLICYGRP(PPG_default) | 无额外绑定（本案例未选） |

#### 6.1.3 DP-03(混合匹配) → FLOWFILTER 参数绑定

| DP-03选项 | 目标ConfigObject | 影响 | 本案例 |
|-----------|-----------------|------|-------|
| L7层URL匹配 | FLOWFILTER(ff_video) | 需PROTBINDFLOWF+L7FILTERNAME | 视频业务 |
| L34层协议匹配 | FLOWFILTER(ff_im) | 需PROTBINDFLOWF(PROTOCOLNAME="im")，无L7FILTERNAME | IM消息 |
| L34层匹配(ANY) | FLOWFILTER(ff_any) | 仅FLTBINDFLOWF，无PROTBINDFLOWF | 默认流量 |

### 6.2 E2: DecisionPoint --gates--> EngineeringTask

| DecisionPoint | 选项 | 门控Task | 门控状态 | 说明 |
|--------------|------|---------|---------|------|
| DP-01(在线) | 在线计费 | T-PLAN-005(规划配额耗尽动作) | **active** | 在线计费必须规划配额耗尽后动作 |
| DP-02(BLOCK) | BLOCK | T-EXEC-005(配置计费动作链) | **active** | 需额外创建PCCACTIONPROP |
| DP-03(混合) | 视频=L7 | T-EXEC-003(配置七层过滤条件) | **active** | 视频需创建l7_video |
| DP-03(混合) | IM=L34协议 | T-EXEC-003 | **skip** | IM不需要L7FILTER |
| DP-03(混合) | 默认=ANY | T-EXEC-003 | **skip** | 默认不需要L7FILTER |
| DP-03(混合) | 全部=无特定IP | T-EXEC-001(配置IP地址列表) | **skip** | 本案例不需要IPLIST |

**可视化：任务编排受决策点影响**

```
                    DP-01=在线         DP-03=混合
                        ↓                  ↓
T-PLAN-001 ─→ T-PLAN-002 ─→ T-PLAN-003 ─→ T-PLAN-004 ─→ T-PLAN-005(active)
                                                                      ↓
T-EXEC-001(skip) ─→ T-EXEC-002 ─→ T-EXEC-003(active, 仅1个) ─→ T-EXEC-004 ─→ T-EXEC-005 ─→ T-EXEC-008 ─→ T-EXEC-010
                                                                                                                    ↓
                                                                                    T-VERIFY-001 ─→ T-VERIFY-002 ─→ T-VERIFY-003
```

### 6.3 E3: ConfigObject --composes--> ConfigObject

本案例的配置对象组合关系：

| 容器对象 | 被包含对象 | 基数 | 绑定参数 | 本案例实例 |
|---------|-----------|------|---------|-----------|
| URRGROUP(urrg_video) | URR(urr_video) | 1 | UPURRNAME1/DOWNURRNAME1 | 视频业务1个URR |
| URRGROUP(urrg_im) | URR(urr_im) | 1 | UPURRNAME1/DOWNURRNAME1 | IM业务1个URR |
| URRGROUP(urrg_default) | URR(urr_default) | 1 | UPURRNAME1/DOWNURRNAME1 | 默认1个URR |
| PCCPOLICYGRP(PPG_video) | URRGROUP(urrg_video) | 1:1 | URRGROUPNAME | 视频策略组 |
| PCCPOLICYGRP(PPG_im) | URRGROUP(urrg_im) | 1:1 | URRGROUPNAME | IM策略组 |
| PCCPOLICYGRP(PPG_default) | URRGROUP(urrg_default) | 1:1 | URRGROUPNAME | 默认策略组 |
| PCCPOLICYGRP(PPG_default) | PCCACTIONPROP(pccact_block) | 0:1 | PCCACTPROPNAME | 配额耗尽BLOCK |
| RULE(Rule_video) | FLOWFILTER(ff_video) | 1:1 | FLOWFILTERNAME | 视频规则 |
| RULE(Rule_video) | PCCPOLICYGRP(PPG_video) | 1:1 | POLICYNAME | 视频规则→策略 |
| RULE(Rule_im) | FLOWFILTER(ff_im) | 1:1 | FLOWFILTERNAME | IM规则 |
| RULE(Rule_im) | PCCPOLICYGRP(PPG_im) | 1:1 | POLICYNAME | IM规则→策略 |
| RULE(Rule_default) | FLOWFILTER(ff_any) | 1:1 | FLOWFILTERNAME | 默认规则 |
| RULE(Rule_default) | PCCPOLICYGRP(PPG_default) | 1:1 | POLICYNAME | 默认规则→策略 |
| USERPROFILE(up_online_charging) | RULE(Rule_video) | 1:N | RULEBINDING | 视频绑定 |
| USERPROFILE(up_online_charging) | RULE(Rule_im) | 1:N | RULEBINDING | IM绑定 |
| USERPROFILE(up_online_charging) | RULE(Rule_default) | 1:N | RULEBINDING | 默认绑定 |
| USERPROFILE(up_online_charging) | URRGROUP(urrg_default) | 1:1 | DFTURRGRPNAME | 默认计费组 |
| FLOWFILTER(ff_video) | FILTER(filter_any) | 1:1 | FLTBINDFLOWF | L34基础 |
| FLOWFILTER(ff_video) | L7FILTER(l7_video) | 0:1 | PROTBINDFLOWF | L7 URL |
| FLOWFILTER(ff_im) | FILTER(filter_im) | 1:1 | FLTBINDFLOWF | L34基础 |
| FLOWFILTER(ff_im) | — | 0:1 | PROTBINDFLOWF(PROTOCOLNAME="im") | 协议绑定 |
| FLOWFILTER(ff_any) | FILTER(filter_any) | 1:1 | FLTBINDFLOWF | 仅L34 |

**组合关系可视化（以视频业务为例）**：

```
USERPROFILE(up_online_charging)
  ├── URRGRPBINDING → URRGROUP(urrg_default) [兜底]
  ├── RULEBINDING → RULE(Rule_video)
  │                  ├── FLOWFILTER(ff_video)
  │                  │   ├── FLTBINDFLOWF → FILTER(filter_any)
  │                  │   └── PROTBINDFLOWF → L7FILTER(l7_video) [L7 URL]
  │                  └── PCCPOLICYGRP(PPG_video)
  │                      └── URRGROUP(urrg_video)
  │                          └── URR(urr_video) [ONLINE, VOLUME, RG=100]
  ├── RULEBINDING → RULE(Rule_im)  [...]
  └── RULEBINDING → RULE(Rule_default)
                       ├── FLOWFILTER(ff_any)
                       │   └── FLTBINDFLOWF → FILTER(filter_any)
                       └── PCCPOLICYGRP(PPG_default)
                           ├── URRGROUP(urrg_default)
                           │   └── URR(urr_default) [ONLINE, VOLUME, RG=300]
                           └── PCCACTIONPROP(pccact_block) [配额耗尽BLOCK]
```

### 6.4 E4: Feature --differentiates--> ConfigObject

> 这是表达"同一方案下不同Feature仅少数参数不同"的关键边。

基准Feature：GWFD-020301（内容计费基本功能）——不设定特定的METERINGTYPE。

| Feature | 差异化ConfigObject | 差异参数 | 值 | 额外约束 | 本案例使用 |
|---------|-------------------|---------|-----|---------|-----------|
| GWFD-020303(流量计费) | URR | ONLMETERINGTYPE | VOLUME | 无特殊约束 | 视频+默认 |
| GWFD-020302(时长计费) | URR | ONLMETERINGTYPE | DURATION | CTP/QCT两种计时模式 | IM |
| GWFD-020300(在线计费) | URR | USAGERPTMODE | ONLINE | 需配额管理 | 全部3个URR |

**差异化链条**：

```
内容计费基本功能(基准)
  ├→ 在线计费: USAGERPTMODE=ONLINE (所有URR)
  │   ├→ 流量计费: ONLMETERINGTYPE=VOLUME (urr_video, urr_default)
  │   └→ 时长计费: ONLMETERINGTYPE=DURATION (urr_im)
```

### 6.5 E5: EngineeringTask --output_propagates_to--> EngineeringTask

> 这是表达"上游Task创建的对象名称如何传播到下游Task引用参数"的关键边。

| 上游Task | 下游Task | 传播实体 | 传播方式 | 本案例具体值 |
|---------|---------|---------|---------|------------|
| T-PLAN-004 | T-EXEC-005 | URR/URRGROUP/PCCPOLICYGRP 名称 | 规划名称→创建对象时使用相同名称 | urr_video/urrg_video/PPG_video 等 |
| T-EXEC-005 | T-EXEC-008 | PCCPOLICYGRP 名称 | RULE.POLICYNAME引用PPG名称 | PPG_video→Rule_video.POLICYNAME |
| T-EXEC-004 | T-EXEC-008 | FLOWFILTER 名称 | RULE.FLOWFILTERNAME引用ff名称 | ff_video→Rule_video.FLOWFILTERNAME |
| T-EXEC-005 | T-EXEC-010 | URRGROUP 名称 | URRGRPBINDING.DFTURRGRPNAME引用 | urrg_default→DFTURRGRPNAME |
| T-EXEC-008 | T-EXEC-010 | RULE 名称 | RULEBINDING.RULENAME引用 | Rule_video→RULEBINDING.RULENAME |
| T-PLAN-001 | T-EXEC-010 | USERPROFILE 名称 | 所有绑定引用UP名称 | up_online_charging |

**输出传播可视化**：

```
T-PLAN-004 ──name──→ T-EXEC-005 ──PPG_name──→ T-EXEC-008 ──Rule_name──→ T-EXEC-010
     │                   │                        │                      │
     │                   ├──ff_name────────────────┘                      │
     │                   │                                                │
     │                   └──urrg_name────────────────────────────────────┘
     │                                                                    │
     └──UP_name─────────────────────────────────────────────────────────→┘
```

---

## 7. 完整实例关系表

### 7.1 业务层关系（3条）

| 起点 | 终点 | 关系标识 | 业务解释 |
|------|------|---------|---------|
| 业务感知(BD) | NS-01 计费场景 | contains | 业务感知域中存在按业务粒度差异化计费的稳定问题空间 |
| NS-01 计费场景 | DS-01 差异化计费组合方案 | instantiated_as | 计费场景收敛为差异化计费方案闭包 |
| NS-01 计费场景 | DP-01(计费方式选择) | has_decision | 进入计费场景时必须选择计费方式 |

### 7.2 方案到任务关系（15条）

| 起点 | 终点 | 关系标识 | 业务解释 |
|------|------|---------|---------|
| DS-01 | T-PLAN-001 | uses_task | 规划生效范围(UserProfile=up_online_charging) |
| DS-01 | T-PLAN-002 | uses_task | 规划识别条件(L7 URL/L34协议/ANY) |
| DS-01 | T-PLAN-003 | uses_task | 规划Rule与优先级(视频100/IM200/默认65000) |
| DS-01 | T-PLAN-004 | uses_task | 规划计费对象(3套三件套) |
| DS-01 | T-PLAN-005 | uses_task | 规划配额耗尽动作(BLOCK) |
| DS-01 | T-EXEC-002 | uses_task | 配置FILTER(filter_any, filter_im) |
| DS-01 | T-EXEC-003 | uses_task | 配置L7FILTER(l7_video) |
| DS-01 | T-EXEC-004 | uses_task | 配置FLOWFILTER(ff_video/ff_im/ff_any)及绑定 |
| DS-01 | T-EXEC-005 | uses_task | 配置URR→URRGROUP→PCCPOLICYGRP(3套)+PCCACTIONPROP |
| DS-01 | T-EXEC-008 | uses_task | 配置RULE(Rule_video/Rule_im/Rule_default) |
| DS-01 | T-EXEC-010 | uses_task | 配置UserProfile+URRGRPBINDING+RULEBINDING+REFRESHSRV |
| DS-01 | T-VERIFY-001 | uses_task | 验证4个License开关 |
| DS-01 | T-VERIFY-002 | uses_task | 验证配置链逐层回查 |
| DS-01 | T-VERIFY-003 | uses_task | 验证PFCP会话上报与计费流量 |
| DS-01 | T-EXEC-001 | uses_task | 配置IP地址列表（**被gates跳过**） |

### 7.3 支撑关系（14条）

| 起点 | 终点 | 关系标识 | 业务解释 |
|------|------|---------|---------|
| DS-01 | P-02(SMF) | involves | 控制面计费策略编排，与OCS交互配额 |
| DS-01 | P-03(UPF) | involves | 用户面计费执行，统计流量/时长 |
| DS-01 | P-04(OCS) | involves | 在线计费核心：配额分配和重授权 |
| DS-01 | P-05(UE) | involves | 产生视频/IM/默认三类待计费流量 |
| DS-01 | S-01(用户级) | applies_to | 计费策略按5G用户粒度生效 |
| DS-01 | S-02(APN/DNN) | applies_to | 计费策略按DNN=internet生效 |
| DS-01 | S-06(UserProfile) | applies_to | UserProfile=up_online_charging承载最终生效 |
| DS-01 | DP-02(配额耗尽) | has_decision | 在线计费配额耗尽→BLOCK |
| DS-01 | DP-03(匹配层次) | has_decision | 视频L7/IM协议/默认ANY |
| DS-01 | VP-01 | validated_by | 在线计费差异化验收 |
| VP-01 | T-VERIFY-001 | executed_by | License验证 |
| VP-01 | T-VERIFY-002 | executed_by | 配置链回查 |
| VP-01 | T-VERIFY-003 | executed_by | PFCP上报验证 |
| VP-01 | BR-02 | uses_rule | 配置链一致性校验 |
| VP-01 | BR-03 | uses_rule | PFCP上报一致性校验 |
| DS-01 | BR-01 | governed_by | License约束(含在线计费License) |
| DS-01 | BR-05 | governed_by | URRID唯一性约束 |
| DS-01 | BR-06 | governed_by | 默认URR组必须配置 |

### 7.4 桥接关系（10条）

| 起点 | 终点 | 关系标识 | 业务解释 |
|------|------|---------|---------|
| NS-01 | BA.FilterCondition | uses_semantic_object | 计费场景通过过滤条件识别业务流 |
| NS-01 | BA.Charging | uses_semantic_object | 计费场景核心语义 |
| DS-01 | BA.FilterCondition | instantiates_semantic_object | 落实为FILTER/L7FILTER/FLOWFILTER |
| DS-01 | BA.Rule | instantiates_semantic_object | 落实为3个RULE |
| DS-01 | BA.Charging | instantiates_semantic_object | 落实为URR→URRGROUP→PCCPOLICYGRP |
| DS-01 | BA.Quota | instantiates_semantic_object | 在线计费配额控制，PCCACTIONPROP |
| DS-01 | GWFD-110101(SA-Basic) | requires_capability | 识别底座 |
| DS-01 | GWFD-020301(内容计费) | requires_capability | 内容计费能力 |
| DS-01 | GWFD-020300(在线计费) | requires_capability | 在线计费核心能力 |
| DS-01 | GWFD-020303(流量计费) | requires_capability | 视频和默认的VOLUME统计 |
| DS-01 | GWFD-020302(时长计费) | requires_capability | IM的DURATION统计 |
| DS-01 | URR | realized_by_config | 计费对象 |
| DS-01 | URRGROUP | realized_by_config | 计费组合 |
| DS-01 | PCCPOLICYGRP | realized_by_config | 策略封装 |
| DS-01 | RULE | realized_by_config | 规则汇聚 |
| DS-01 | USERPROFILE | realized_by_config | 策略容器 |
| DS-01 | FILTER | realized_by_config | 识别条件 |
| DS-01 | FLOWFILTER | realized_by_config | 流过滤器 |

### 7.5 Task→ConfigObject关系（8条）

| 起点 | 终点 | 关系标识 | 业务解释 |
|------|------|---------|---------|
| T-EXEC-002 | FILTER | creates_config | 创建filter_any, filter_im |
| T-EXEC-003 | L7FILTER | creates_config | 创建l7_video |
| T-EXEC-004 | FLOWFILTER | creates_config | 创建ff_video/ff_im/ff_any |
| T-EXEC-005 | URR, URRGROUP, PCCPOLICYGRP, PCCACTIONPROP | creates_config | 创建3套三件套+1个门控 |
| T-EXEC-008 | RULE | creates_config | 创建3个RULE |
| T-EXEC-010 | USERPROFILE, RULEBINDING, URRGRPBINDING | creates_config | 创建容器和绑定 |
| T-VERIFY-001 | LICENSESWITCH | verifies_config | 验证4个License |
| T-VERIFY-002 | RULEBINDING→RULE→全链路 | verifies_config | 逐层回查 |

### 7.6 决策驱动关系（5条新边，共20条实例）

> 见§6节详细展开。这里仅汇总计数。

| 关系标识 | 本案例实例数 | 分布 |
|---------|------------|------|
| parameter_binding | 9 | DP-01→URR(6) + DP-02→PCCPOLICYGRP(1) + DP-03→FLOWFILTER(2) |
| gates | 6 | DP-01→T-PLAN-005(1) + DP-03→T-EXEC-001(1) + DP-03→T-EXEC-003(4) |
| composes | 22 | URRGROUP→URR(3) + PCCPOLICYGRP→URRGROUP(3) + PCCPOLICYGRP→PCCACTIONPROP(1) + RULE→FLOWFILTER(3) + RULE→PCCPOLICYGRP(3) + USERPROFILE→RULE(3) + USERPROFILE→URRGROUP(1) + FLOWFILTER→FILTER(3) + FLOWFILTER→L7FILTER(2) |
| differentiates | 3 | 流量→VOLUME + 时长→DURATION + 在线→ONLINE |
| output_propagates_to | 6 | 见§6.5 |

---

## 8. 验证场景：端到端走一遍

> 这是业务图谱的核心价值——给定一个具体需求，图谱如何**逐步**引导Agent从决策点走到具体配置。

### 输入需求

> "5G用户在线计费：视频流量按VOLUME(RG=100)，IM消息按DURATION(RG=200)，默认在线计费(RG=300)，配额耗尽后阻断。"

### 步骤1：场景路由

| 步骤 | 匹配 | 结果 |
|------|------|------|
| 需求解析 | "按业务粒度差异化计费" | → NS-01 计费场景 |
| 方案匹配 | "过滤条件+计费链+默认兜底+配额动作" | → DS-01 差异化计费组合方案 |
| 加载知识 | NS-01匹配 | → 加载计费知识库 |

### 步骤2：决策点解析

| DecisionPoint | 需求中的信号 | 选择 |
|--------------|------------|------|
| DP-01 计费方式 | "在线计费" | **ONLINE** |
| DP-02 配额动作 | "配额耗尽后阻断" | **BLOCK** |
| DP-03 匹配层次 | "视频"(URL) + "IM"(协议) + "默认"(all) | **混合匹配** |

### 步骤3：任务编排（受gates影响）

```
T-PLAN-001(规划UserProfile=up_online_charging)
  → T-PLAN-002(规划L7 URL + L34协议 + L34 ANY三类过滤条件)
    → T-PLAN-003(规划3条Rule，PRIORITY=100/200/65000)
      → T-PLAN-004(规划3套三件套: urr_video/urrg_video/PPG_video...)
        → T-PLAN-005(active: 规划配额耗尽BLOCK→PCCACTIONPROP)
          ↓ gates: T-EXEC-001(skip, 无特定IP)
          → T-EXEC-002(FILTER: filter_any, filter_im)
            → T-EXEC-003(active: L7FILTER l7_video, 仅1个)
              → T-EXEC-004(FLOWFILTER: ff_video/ff_im/ff_any + 绑定)
                → T-EXEC-005(URR×3 + URRGROUP×3 + PCCPOLICYGRP×3 + PCCACTIONPROP×1)
                  → T-EXEC-008(RULE×3, 引用FLOWFILTER和PPG名称)
                    → T-EXEC-010(USERPROFILE + RULEBINDING×3 + URRGRPBINDING + REFRESHSRV)
```

### 步骤4：参数填充（受parameter_binding影响）

| 对象 | 参数来源 | 具体值 |
|------|---------|-------|
| urr_video.USAGERPTMODE | DP-01=在线 | ONLINE |
| urr_video.ONLMETERINGTYPE | Feature=流量计费(differentiates) | VOLUME |
| urr_video.RG | 用户输入 | 100 |
| urr_video.URRID | 规划分配 | 1001 |
| urr_im.USAGERPTMODE | DP-01=在线 | ONLINE |
| urr_im.ONLMETERINGTYPE | Feature=时长计费(differentiates) | DURATION |
| urr_im.RG | 用户输入 | 200 |
| ff_video.PROTBINDFLOWF | DP-03=L7 | PROTOCOLNAME=http, L7FILTERNAME=l7_video |
| ff_im.PROTBINDFLOWF | DP-03=协议 | PROTOCOLNAME=im |
| PPG_default.PCCACTPROPNAME | DP-02=BLOCK | pccact_block |

### 步骤5：输出传播（受output_propagates_to影响）

```
T-PLAN-004输出 "urr_video" ──→ T-EXEC-005 使用 "urr_video" 创建URR
T-EXEC-005输出 "PPG_video" ──→ T-EXEC-008 使用 "PPG_video" 作为 RULE.POLICYNAME
T-EXEC-004输出 "ff_video"  ──→ T-EXEC-008 使用 "ff_video" 作为 RULE.FLOWFILTERNAME
T-EXEC-005输出 "urrg_default" ──→ T-EXEC-010 使用 "urrg_default" 作为 DFTURRGRPNAME
T-EXEC-008输出 "Rule_video" ──→ T-EXEC-010 使用 "Rule_video" 作为 RULEBINDING.RULENAME
T-PLAN-001输出 "up_online_charging" ──→ T-EXEC-010 所有绑定引用此名称
```

### 步骤6：最终配置脚本

```sql
-- === T-EXEC-002: 配置三四层过滤条件 ===
ADD FILTER:FILTERNAME="filter_any",L34PROTTYPE=STRING,L34PROTOCOL=ANY;
ADD FILTER:FILTERNAME="filter_im",L34PROTTYPE=STRING,L34PROTOCOL=ANY;

-- === T-EXEC-003: 配置七层过滤条件 ===
ADD L7FILTER:L7FILTERNAME="l7_video",URLTYPE=URL,URL="video.huawei.com/*";

-- === T-EXEC-004: 配置流过滤器与绑定 ===
ADD FLOWFILTER:FLOWFILTERNAME="ff_video";
ADD FLTBINDFLOWF:FLOWFILTERNAME="ff_video",FILTERNAME="filter_any";
ADD PROTBINDFLOWF:FLOWFILTERNAME="ff_video",PROTOCOLNAME="http",L7FILTERNAME="l7_video";

ADD FLOWFILTER:FLOWFILTERNAME="ff_im";
ADD FLTBINDFLOWF:FLOWFILTERNAME="ff_im",FILTERNAME="filter_im";
ADD PROTBINDFLOWF:FLOWFILTERNAME="ff_im",PROTOCOLNAME="im";

ADD FLOWFILTER:FLOWFILTERNAME="ff_any";
ADD FLTBINDFLOWF:FLOWFILTERNAME="ff_any",FILTERNAME="filter_any";

-- === T-EXEC-005: 配置计费动作链 ===
-- 视频业务：按流量在线计费
ADD URR:URRNAME="urr_video",URRID=1001,USAGERPTMODE=ONLINE,ONLMETERINGTYPE=VOLUME,RG=100;
ADD URRGROUP:URRGROUPNAME="urrg_video",UPURRNAME1="urr_video",DOWNURRNAME1="urr_video";
ADD PCCPOLICYGRP:PCCPOLICYGRPNM="PPG_video",URRGROUPNAME="urrg_video";

-- IM消息：按时长在线计费
ADD URR:URRNAME="urr_im",URRID=1002,USAGERPTMODE=ONLINE,ONLMETERINGTYPE=DURATION,RG=200;
ADD URRGROUP:URRGROUPNAME="urrg_im",UPURRNAME1="urr_im",DOWNURRNAME1="urr_im";
ADD PCCPOLICYGRP:PCCPOLICYGRPNM="PPG_im",URRGROUPNAME="urrg_im";

-- 默认计费：按流量在线 + 配额耗尽BLOCK
ADD URR:URRNAME="urr_default",URRID=1003,USAGERPTMODE=ONLINE,ONLMETERINGTYPE=VOLUME,RG=300;
ADD URRGROUP:URRGROUPNAME="urrg_default",UPURRNAME1="urr_default",DOWNURRNAME1="urr_default";
ADD PCCACTIONPROP:PCCACTPROPNM="pccact_block",GATINGSTATUS=CLS;
ADD PCCPOLICYGRP:PCCPOLICYGRPNM="PPG_default",URRGROUPNAME="urrg_default",PCCACTPROPNAME="pccact_block";

-- === T-EXEC-008: 配置Rule ===
ADD RULE:RULENAME="Rule_video",POLICYTYPE=PCC,FILTERINGMODE=FLOWFILTER,FLOWFILTERNAME="ff_video",PRIORITY=100,POLICYNAME="PPG_video";
ADD RULE:RULENAME="Rule_im",POLICYTYPE=PCC,FILTERINGMODE=FLOWFILTER,FLOWFILTERNAME="ff_im",PRIORITY=200,POLICYNAME="PPG_im";
ADD RULE:RULENAME="Rule_default",POLICYTYPE=PCC,FILTERINGMODE=FLOWFILTER,FLOWFILTERNAME="ff_any",PRIORITY=65000,POLICYNAME="PPG_default";

-- === T-EXEC-010: 配置UserProfile与Rule绑定 ===
ADD USERPROFILE:USERPROFILENAME="up_online_charging";
SET URRGRPBINDING:USERPROFILENAME="up_online_charging",DFTURRGRPNAME="urrg_default",DFTSIGURRGNAME="urrg_default";
ADD RULEBINDING:USERPROFILENAME="up_online_charging",POLICYTYPE=PCC,RULENAME="Rule_video";
ADD RULEBINDING:USERPROFILENAME="up_online_charging",POLICYTYPE=PCC,RULENAME="Rule_im";
ADD RULEBINDING:USERPROFILENAME="up_online_charging",POLICYTYPE=PCC,RULENAME="Rule_default";
SET REFRESHSRV:REFRESHTYPE=ALL;
```

### 步骤7：校验脚本

```sql
-- T-VERIFY-001: 验证License开关
LST LICENSESWITCH:LICITEM="LKV3G5SABS01";   -- 预期: ENABLE
LST LICENSESWITCH:LICITEM="LKV3G5BCBC01";   -- 预期: ENABLE
LST LICENSESWITCH:LICITEM="LKV3G5PCCB01";   -- 预期: ENABLE
LST LICENSESWITCH:LICITEM="LKV3G5OLCH01";   -- 预期: ENABLE (在线计费)

-- T-VERIFY-002: 验证配置链逐层回查
LST RULEBINDING:USERPROFILENAME="up_online_charging";
-- 预期: 3条绑定 → Rule_video, Rule_im, Rule_default

LST RULE:RULENAME="Rule_video",POLICYTYPE=PCC;
-- 预期: FLOWFILTERNAME=ff_video, PRIORITY=100, POLICYNAME=PPG_video

LST PCCPOLICYGRP:PCCPOLICYGRPNM="PPG_video";
-- 预期: URRGROUPNAME=urrg_video

LST URRGROUP:URRGROUPNAME="urrg_video";
-- 预期: UPURRNAME1=urr_video, DOWNURRNAME1=urr_video

LST URR:URRNAME="urr_video";
-- 预期: URRID=1001, USAGERPTMODE=ONLINE, ONLMETERINGTYPE=VOLUME, RG=100

LST PCCPOLICYGRP:PCCPOLICYGRPNM="PPG_default";
-- 预期: URRGROUPNAME=urrg_default, PCCACTPROPNAME=pccact_block

LST PCCACTIONPROP:PCCACTPROPNM="pccact_block";
-- 预期: GATINGSTATUS=CLS

-- T-VERIFY-003: 验证PFCP会话上报
-- 通过OM Portal抓取PFCP Session Report
-- 预期: Usage Report中包含URRID=1001(VOLUME), 1002(DURATION), 1003(VOLUME)
```

---

## 9. MVP 与完整图谱的对照

| 维度 | 完整计费场景图谱 | 本MVP |
|------|---------------|-------|
| 计费方式 | 离线/在线/融合三选一 | 仅在线 |
| 业务数量 | 泛指N个业务 | 具体3个(视频/IM/默认) |
| 匹配层次 | 泛指 | 具体(L7 URL/L34协议/ANY) |
| 配额动作 | BLOCK/REDIRECT/FORWARD | 仅BLOCK |
| OR条件 | FLOWFILTERGRP | 无(本案例各业务无交集) |
| 免费业务 | OFFMETERINGTYPE=FREE | 无(全部在线计费) |
| 异常URR | 有SIGURRGRPNAME | 无(简化) |
| UNC/SMF侧 | 完整CCT/CHFINIT配置 | 未展开(仅UDG侧) |

> MVP 的价值不在于覆盖面，而在于**端到端走通**：从一个需求，到决策点选择，到任务编排，到参数填充，到最终配置脚本——业务图谱的每条边都有实实在在的落地。
