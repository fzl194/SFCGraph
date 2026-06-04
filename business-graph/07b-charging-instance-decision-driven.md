# 计费场景实例扩展：决策驱动的配置差异

## 文档说明

本文档基于 `06-business-awareness-business-graph-final.md` Part B 的实例，填充 `07a-schema-extension-decision-driven.md` 中定义的 5 条新边和 2 个新属性在 **NS-01 计费场景 / DS-01 差异化计费组合方案** 上的具体实例。

所有内容来自 9 个特性的 MOP 文档和验证报告（详见 `SKILL/knowledge/计费知识库.md`），是对 06 文件中已有实例的**结构化追加**。

## 1. 新增 DecisionPoint 实例：DP-06 匹配层次选择

| 字段 | 值 |
|------|-----|
| decision_id | DP-06 |
| decision_name | 匹配层次选择 |
| 挂载层级 | DeliverySolution(DS-01) |
| decision_question | 业务流通过 L34 层还是 L7 层匹配 |
| option_set | `["L34层匹配","L7层URL匹配","L7层协议匹配","L34+L7混合匹配"]` |
| trigger_condition | 规划识别条件时 |
| impact_summary | 决定是否需要 L7FILTER 和 PROTBINDFLOWF，影响配置对象链长度 |
| status | active |

**边**：

```text
DS-01(差异化计费组合方案) --has_decision--> DP-06(匹配层次选择)
```

## 2. E1 实例：DecisionPoint --parameter_binding--> ConfigObject

### 2.1 DP-01(计费方式选择) → ConfigObject 参数绑定

| DP选项 | 目标ConfigObject | 参数 | 值 | 附带影响 |
|--------|-----------------|------|-----|---------|
| 离线计费 | URR | USAGERPTMODE | OFFLINE | OFFMETERINGTYPE 生效（VOLUME/DURATION/FREE） |
| 离线计费 | URRGROUP | UPURRNAME1/DOWNURRNAME1 | 引用离线URR | UPURRNAME2/DOWNURRNAME2 不填 |
| 在线计费 | URR | USAGERPTMODE | ONLINE | ONLMETERINGTYPE 生效（VOLUME/DURATION/EVENT） |
| 在线计费 | URRGROUP | UPURRNAME2/DOWNURRNAME2 | 引用在线URR | UPURRNAME1/DOWNURRNAME1 不填 |
| 融合计费 | URR | 每业务创建2个URR | 1个OFFLINE+1个ONLINE | URRGROUP 同时填 UPURRNAME1-4 |
| 融合+DEFAULT | URR | 每业务仅1个URR | 按业务选OFFLINE或ONLINE | URRGROUP 只填一种模式 |

### 2.2 DP-06(匹配层次选择) → ConfigObject 参数绑定

| DP选项 | 目标ConfigObject | 影响 |
|--------|-----------------|------|
| L34层匹配 | FLOWFILTER | 仅通过 FLTBINDFLOWF 绑定 FILTER，不需要 L7FILTER |
| L7层URL匹配 | FLOWFILTER | 需通过 PROTBINDFLOWF 绑定 L7FILTER，需指定 PROTOCOLNAME |
| L7层协议匹配 | FLOWFILTER | 需通过 PROTBINDFLOWF 绑定协议（无 L7FILTERNAME） |
| L34+L7混合 | FLOWFILTER | 两种绑定都用 |

## 3. E2 实例：DecisionPoint --gates--> EngineeringTask

| DecisionPoint | 选项 | 门控Task | 门控条件 | 说明 |
|--------------|------|---------|---------|------|
| DP-01 | 离线计费 | T-PLAN-005(规划配额耗尽动作) | skip | 离线计费无配额管理 |
| DP-01 | 在线计费 | T-PLAN-005 | active | 在线计费需规划配额耗尽动作 |
| DP-01 | 融合计费 | T-PLAN-005 | active | 融合需规划配额耗尽动作 |
| DP-06 | L34匹配 | T-EXEC-003(配置七层过滤条件) | skip | 不需要 L7FILTER |
| DP-06 | 含L7匹配 | T-EXEC-003 | active | 需要 L7FILTER |
| DP-06 | any-to-any | T-EXEC-001(配置IP地址列表) | skip | 不需要 IPLIST |
| DP-06 | 特定IP匹配 | T-EXEC-001 | active | 需要 IPLIST |

## 4. E3 实例：ConfigObject --composes--> ConfigObject

### 4.1 计费三件套组合关系

| 容器对象 | 被包含对象 | 基数 | 条件 |
|---------|-----------|------|------|
| URRGROUP | URR | DP-01=离线: 1个(UPURRNAME1/DOWNURRNAME1) | DP-01=在线: 1个(UPURRNAME2/DOWNURRNAME2) |
| URRGROUP | URR | DP-01=融合: 2个(UPURRNAME1-4) | 融合+DEFAULT: 1个(选一种模式) |
| PCCPOLICYGRP | URRGROUP | 1:1 | URRGROUPNAME 必填 |
| PCCPOLICYGRP(兜底) | 异常URRGROUP | 0:1 | 仅兜底 PCCPOLICYGRP 有 SIGURRGRPNAME |
| RULE | FLOWFILTER | 1:1 | FLOWFILTERNAME 必填 |
| RULE | PCCPOLICYGRP | 1:1 | POLICYNAME 必填(计费场景 POLICYTYPE=PCC) |
| USERPROFILE | RULE | 1:N | 通过 RULEBINDING 绑定，数量=RULE 总数 |
| USERPROFILE | 默认URRGROUP | 1:1 | DFTURRGRPNAME 必填 |
| USERPROFILE | 异常URRGROUP | 1:1 | DFTSIGURRGNAME 必填 |
| FLOWFILTER | FILTER | 1:1 | 通过 FLTBINDFLOWF 绑定 |
| FLOWFILTER | L7FILTER | 0:1 | 通过 PROTBINDFLOWF 绑定，仅 L7 匹配场景 |

### 4.2 过滤链组合关系

| 容器对象 | 被包含对象 | 基数 | 说明 |
|---------|-----------|------|------|
| FLOWFILTERGRP | FLOWFILTER | N:N | OR 条件组合，多个 FLOWFILTER 编入同一组 |

## 5. E4 实例：Feature --differentiates--> ConfigObject

以下表达各计费子特性相对于基准（内容计费 GWFD-020301）在 ConfigObject 参数上的差异。

| Feature | 差异化ConfigObject | 差异参数 | 值 | 额外约束 |
|---------|-------------------|---------|-----|---------|
| GWFD-020302(时长) | URR | OFFMETERINGTYPE | DURATION | CTP/QCT 两种计时模式 |
| GWFD-020302(时长) | URR | ONLMETERINGTYPE | DURATION | - |
| GWFD-020303(流量) | URR | OFFMETERINGTYPE | VOLUME | 无特殊约束 |
| GWFD-020303(流量) | URR | ONLMETERINGTYPE | VOLUME | - |
| GWFD-020306(事件) | URR | ONLMETERINGTYPE | EVENT | 仅 SCUR 模式，不支持 Free RG，不支持 Default Quota |
| GWFD-010171(离线) | URR | USAGERPTMODE | OFFLINE | UNC 侧重 CG 连接 |
| GWFD-020300(在线) | URR | USAGERPTMODE | ONLINE | UNC 侧重 OCS+CCT 模板，配额管理 |
| GWFD-010173(融合) | URR | USAGERPTMODE | 按子业务 | UNC 侧重 CHF+Nchf 接口，仅 5G |

> 注：GWFD-020302/020303/020306 在 06 文件 §21 的 Feature 实例表中未单独列出（06 仅列粗粒度特性），此处作为计费场景的知识层实例补充。

## 6. E5 实例：EngineeringTask --output_propagates_to--> EngineeringTask

| 上游Task | 下游Task | 传播实体 | 传播方式 |
|---------|---------|---------|---------|
| T-PLAN-004(规划计费对象) | T-EXEC-005(配置计费动作链) | URR/URRGROUP/PCCPOLICYGRP 名称 | 规划名称 → 创建对象时使用相同名称 |
| T-EXEC-005 | T-EXEC-008(配置Rule) | PCCPOLICYGRP 名称 | RULE.POLICYNAME 引用 PPG 名称 |
| T-EXEC-004(配置流过滤器) | T-EXEC-008 | FLOWFILTER 名称 | RULE.FLOWFILTERNAME 引用 ff 名称 |
| T-EXEC-005 | T-EXEC-010(配置UserProfile) | URRGROUP 名称 | URRGRPBINDING.DFTURRGRPNAME 引用 URRG 名称 |
| T-EXEC-008 | T-EXEC-010 | RULE 名称 | RULEBINDING.RULENAME 引用 Rule 名称 |
| T-PLAN-001(规划生效范围) | T-EXEC-010 | USERPROFILE 名称 | 所有 RULEBINDING/URRGRPBINDING 引用 UP 名称 |

## 7. A1 实例：EngineeringTask.output_cardinality

| Task | 输出ConfigObject | 基数公式 | 输入变量 |
|------|-----------------|---------|---------|
| T-EXEC-001(配置IP地址列表) | IPLIST | P(IPLIST数量) | P=需要特定IP匹配的业务数 |
| T-EXEC-002(配置三四层过滤条件) | FILTER | M(FILTER数量) | M=业务需要的 L34 过滤条件数 |
| T-EXEC-003(配置七层过滤条件) | L7FILTER | K(L7数量) | K=含 L7 匹配的业务数，纯 L34 时 K=0 |
| T-EXEC-004(配置流过滤器) | FLOWFILTER | S(场景数) | S=匹配场景数(含兜底) |
| T-EXEC-004 | FLTBINDFLOWF | S | 1:1 跟随 FLOWFILTER |
| T-EXEC-004 | PROTBINDFLOWF | K | 仅 L7 场景 |
| T-EXEC-005(配置计费动作链) | URR | 2N+2(融合) / N+2(单一模式) | N=特定业务数，+2=兜底+异常 |
| T-EXEC-005 | URRGROUP | N+2 | 每业务1 + 兜底1 + 异常1 |
| T-EXEC-005 | PCCPOLICYGRP | N+1 | 每业务1 + 共享兜底(含 SIGURRGRPNAME) |
| T-EXEC-008(配置Rule) | RULE | S | 1:1 跟随 FLOWFILTER |
| T-EXEC-010(配置UserProfile) | RULEBINDING | S | 1:1 跟随 RULE |
| T-EXEC-010 | USERPROFILE | 通常1 | 可多个 UP 按 DNN 拆分 |

**示例验证**：输入"2个特定业务 + 融合计费 + 兜底"

- N=2, S=3(2特定+1兜底, 不含异常FLOWFILTER)
- URR: 2×2+2 = 6 (每业务1个OFFLINE+1个ONLINE + 兜底+异常)
- URRGROUP: 2+2 = 4
- PCCPOLICYGRP: 2+1 = 3
- RULE: 3 (含兜底)
- RULEBINDING: 3

## 8. A2 实例：ConfigObject.naming_pattern

| ConfigObject | 命名模式 | 示例 | 优先级模式 |
|-------------|---------|------|-----------|
| URR | `{业务}_{模式}` | video_offline, video_online | - |
| URRGROUP | `{业务}` | video, default, abnormal | - |
| PCCPOLICYGRP | `PPG_{业务}` | PPG_video, PPG_default | - |
| FILTER | `L34_{描述}` | L34_dns, L34_any | - |
| L7FILTER | `L7_{描述}` | L7_huawei | - |
| FLOWFILTER | `ff_{描述}` | ff_L7, ff_IMS, ff_any | - |
| RULE | `Rule{序号}_{业务}` | Rule001_video, Rule999_any | 特定100+, 兜底65000+ |

## 9. 新增实例关系表

以下为在 06 文件 §23 实例关系表的基础上追加的 **§23.5 决策驱动关系** 子节。

### 9.1 E1: parameter_binding 实例

| 起点对象 | 终点对象 | 关系标识 | 参数绑定 |
|---------|---------|---------|---------|
| DP-01(离线) | URR | parameter_binding | USAGERPTMODE=OFFLINE |
| DP-01(在线) | URR | parameter_binding | USAGERPTMODE=ONLINE |
| DP-01(融合) | URR | parameter_binding | 每业务2个URR(OFFLINE+ONLINE) |
| DP-06(L34) | FLOWFILTER | parameter_binding | 仅FLTBINDFLOWF，无PROTBINDFLOWF |
| DP-06(L7) | FLOWFILTER | parameter_binding | 需PROTBINDFLOWF+L7FILTERNAME |

### 9.2 E2: gates 实例

| 起点对象 | 终点对象 | 关系标识 | 门控条件 |
|---------|---------|---------|---------|
| DP-01(离线) | T-PLAN-005(规划配额耗尽动作) | gates | skip |
| DP-01(在线) | T-PLAN-005 | gates | active |
| DP-01(融合) | T-PLAN-005 | gates | active |
| DP-06(L34) | T-EXEC-003(配置七层过滤条件) | gates | skip |
| DP-06(含L7) | T-EXEC-003 | gates | active |
| DP-06(any-to-any) | T-EXEC-001(配置IP地址列表) | gates | skip |
| DP-06(特定IP) | T-EXEC-001 | gates | active |

### 9.3 E3: composes 实例

| 起点对象 | 终点对象 | 关系标识 | 组合基数 |
|---------|---------|---------|---------|
| URRGROUP | URR | composes | 离线1/在线1/融合2 |
| PCCPOLICYGRP | URRGROUP | composes | 1:1 |
| PCCPOLICYGRP(兜底) | 异常URRGROUP | composes | 0:1 |
| RULE | FLOWFILTER | composes | 1:1 |
| RULE | PCCPOLICYGRP | composes | 1:1 |
| USERPROFILE | RULE | composes | 1:N |
| USERPROFILE | 默认URRGROUP | composes | 1:1 |
| FLOWFILTER | FILTER | composes | 1:1 |
| FLOWFILTER | L7FILTER | composes | 0:1(仅L7) |
| FLOWFILTERGRP | FLOWFILTER | composes | N:N(OR组合) |

### 9.4 E4: differentiates 实例

| 起点对象 | 终点对象 | 关系标识 | 差异参数 |
|---------|---------|---------|---------|
| GWFD-020302(时长) | URR | differentiates | METERINGTYPE=DURATION |
| GWFD-020303(流量) | URR | differentiates | METERINGTYPE=VOLUME |
| GWFD-020306(事件) | URR | differentiates | METERINGTYPE=EVENT, 仅SCUR, 不支持Free RG |
| GWFD-010171(离线) | URR | differentiates | USAGERPTMODE=OFFLINE |
| GWFD-020300(在线) | URR | differentiates | USAGERPTMODE=ONLINE |
| GWFD-010173(融合) | URR | differentiates | USAGERPTMODE=按子业务 |

### 9.5 E5: output_propagates_to 实例

| 起点对象 | 终点对象 | 关系标识 | 传播实体 |
|---------|---------|---------|---------|
| T-EXEC-005(配置计费动作链) | T-EXEC-008(配置Rule) | output_propagates_to | PCCPOLICYGRP名称→RULE.POLICYNAME |
| T-EXEC-004(配置流过滤器) | T-EXEC-008 | output_propagates_to | FLOWFILTER名称→RULE.FLOWFILTERNAME |
| T-EXEC-005 | T-EXEC-010(配置UserProfile) | output_propagates_to | URRGROUP名称→URRGRPBINDING.DFTURRGRPNAME |
| T-EXEC-008 | T-EXEC-010 | output_propagates_to | RULE名称→RULEBINDING.RULENAME |
| T-PLAN-004(规划计费对象) | T-EXEC-005 | output_propagates_to | URR/URRGROUP/PCCPOLICYGRP规划名称 |
| T-PLAN-001(规划生效范围) | T-EXEC-010 | output_propagates_to | USERPROFILE名称 |

## 10. 验证场景

用复杂需求模拟验证新增边的实际效果：

**输入**："按流量在线计费视频业务 + 按时长离线计费IM消息 + 默认计费"

| # | 验证点 | 使用的边/属性 | 预期结果 |
|---|--------|-------------|---------|
| 1 | 选择 USAGERPTMODE | E1(parameter_binding) | 视频:ONLINE, IM:OFFLINE |
| 2 | T-PLAN-005 是否执行 | E2(gates) | 视频业务在线→active(部分在线), IM离线→不影响(已由视频触发) |
| 3 | 计算对象数量 | A1(output_cardinality) | N=2, 混合模式: 2+2=4 URR + 3 URRGROUP + 3 PCCPOLICYGRP |
| 4 | 名称传播 | E5(output_propagates_to) | T-EXEC-005创建的PPG_video→T-EXEC-008的RULE.POLICYNAME |
| 5 | 选择 METERINGTYPE | E4(differentiates) | 视频:VOLUME, IM:DURATION |
| 6 | 构建 URRGROUP | E3(composes) | 视频:UPURRNAME2(在线), IM:UPURRNAME1(离线) |
