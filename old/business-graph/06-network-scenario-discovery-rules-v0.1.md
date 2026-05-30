# 业务感知场景发现规则 v0.1

## 1. 目标

本页定义：

```text
如何从业务感知原料池中归纳第一批 NetworkScenario
```

这里不是最终业务方案，也不是现网定稿，而是先把业务感知拆成稳定的业务子场景。

## 2. 场景发现的基本原则

### 2.1 先发现“问题类型”，不是先发现“命令”

`NetworkScenario` 回答的是：

```text
一线到底在解决什么业务问题
```

不是：

```text
某条命令怎么配
```

### 2.2 一个场景要能被多处证据共同支撑

不能只因为业务专题有一页，就定义一个场景。

一个场景至少应同时被下列两类来源支撑：

- 业务专题 / 基础知识
- 相关特性或命令对象链

### 2.3 场景命名优先按业务目标命名

例如：

- 差异化计费
- 默认兜底计费
- 配额耗尽重定向
- URL/域名访问限制

不要命名成：

- URR 场景
- RuleBinding 场景
- FlowFilter 场景

## 3. 第一批建议场景

当前建议第一批只收下面 5 个：

1. 差异化计费
2. 默认兜底计费
3. 配额耗尽重定向
4. URL/域名访问限制
5. 带宽控制

其中：

```text
第一条闭包优先做：
差异化计费 + 默认兜底计费
```

## 4. 场景发现输入

输入来自：

- `business_source_index.csv`
- `business_related_features_candidates.csv`
- `business_related_commands_candidates.csv`
- `business_related_object_chains_candidates.csv`
- 业务感知语义定义

## 5. 代码先做什么

代码不直接定义最终场景，但可以先做候选聚类。

### 5.1 基于关键词打场景标签

例如：

#### 差异化计费 / 默认兜底计费

- 计费
- 免费
- 费率
- RG
- URR
- 默认
- 兜底
- 独立

#### 配额耗尽重定向

- 配额
- 余额
- 重定向
- 阻断
- Portal
- Quota

#### URL/域名访问限制

- URL
- Host
- 过滤
- 黑名单
- 限制
- 阻断

#### 带宽控制

- BWM
- 带宽
- 限速
- QoS

### 5.2 基于对象链打场景标签

例如：

- `URR -> URRGroup -> PccPolicyGrp -> Rule`
  - 更偏计费类场景
- `FlowFilter/L7Filter -> Rule`
  - 更偏识别、限制、重定向类场景

### 5.3 产出候选表

建议产出：

- `network_scenario_candidates.csv`

字段建议：

- `candidate_id`
- `candidate_name`
- `source_ids_json`
- `feature_codes_json`
- `command_ids_json`
- `object_chain_hints_json`
- `semantic_tags_json`
- `confidence_hint`

## 6. Agent 怎么定稿

Agent 在场景发现阶段只做三件事：

### 6.1 合并同类候选

例如：

- “内容计费”
- “业务差异化计费”
- “套餐1：计费场景”

这些在第一轮可以先归到：

```text
差异化计费
```

### 6.2 区分主场景和子问题

例如：

- “默认兜底计费”
  - 当前更适合作为主场景之一
- “Rule 优先级”
  - 更适合作为语义或方案问题，不适合作为独立场景

### 6.3 生成第一批 `NetworkScenario`

输出：

- `network_scenarios.csv`

字段建议：

- `scenario_id`
- `scenario_name`
- `scenario_summary`
- `business_goal`
- `source_evidence_ids`
- `supporting_feature_codes_json`
- `supporting_command_ids_json`
- `supporting_object_chains_json`
- `status`

## 7. 场景发现的判定标准

一个候选可以升格为 `NetworkScenario`，建议至少满足 3 条：

1. 能用一句业务目标描述清楚
2. 能映射到明确的语义对象
3. 能落到一条或多条特性/命令对象链
4. 不是单纯一个参数约束或单个配置动作
5. 能形成一线可理解的交付问题

## 8. 当前第一条场景主线为什么选“差异化计费 + 默认兜底计费”

原因如下：

1. 它能同时连接：
   - 流量识别
   - 规则语义
   - 计费语义
   - UDG 识别执行链
   - UNC 计费控制链
2. 它不是只围绕一个专题页，而是能被多处特性和命令共同支撑
3. 它是后续扩到：
   - 配额耗尽重定向
   - 免费 / 默认收费
   - 融合计费

的天然母体

## 9. 第一轮输出建议

第一轮只需要产出：

1. `network_scenario_candidates.csv`
2. `network_scenarios.csv`
3. 一个小闭包审查包

审查重点不是数量，而是：

- 场景边界是否合理
- 是否能回到真实文档
- 是否能挂到特性和命令对象链上

## 10. 当前结论

场景发现阶段的目标不是“找全所有业务”，而是：

```text
先把业务感知拆成稳定、可继续扩展的第一批业务子场景
```

然后沿着这些场景去逐步扩展整个业务感知业务图谱。
