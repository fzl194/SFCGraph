# 业务感知相关特性与命令筛选规则 v0.1

## 1. 目标

本页定义：

```text
业务感知相关特性怎么筛
业务感知相关命令怎么筛
业务感知相关对象链怎么筛
```

目的不是一次性得出最终全集，而是先形成：

- `business_related_features_candidates.csv`
- `business_related_commands_candidates.csv`
- `business_related_object_chains_candidates.csv`

然后再由 Agent 做归并和裁剪。

## 2. 为什么必须单独做这一层

业务图谱最终目标是整个业务感知工作面。

如果只按一个最小闭包做：

```text
差异化计费 + 默认兜底计费
```

那容易把业务感知相关的其他特性、命令遗漏掉。

所以需要一层“覆盖面筛选”，逐步把：

- 业务感知相关特性全集
- 业务感知相关命令全集
- 业务感知相关对象链全集

收出来。

## 3. 特性筛选规则

### 3.1 强相关特性

满足任一条件，即可先打 `relevance=high` 候选：

1. 位于：

```text
UDG特性指南\业务感知功能
```

2. 特性名称或页面内容明显包含：

- 内容计费
- PCC
- 融合计费
- 热计费
- 离线计费
- 七层重定向
- URL过滤
- 流量识别
- 防欺诈
- 头增强
- 带宽控制

3. 文档中明确出现业务感知典型对象链：

- `FlowFilter / L7Filter / Rule / RuleBinding / UserProfile`
- `URR / URRGroup / PccPolicyGrp / Rule / RuleBinding / UserProfile`

### 3.2 中相关特性

满足任一条件，即可先打 `relevance=medium` 候选：

1. 位于智能 PCC、QoS、5G LAN、MEC、业务控制相关目录
2. 明确为业务感知场景提供外围支撑
3. 主要提供环境准备、对端协同、增强能力，而不是直接提供主业务动作

### 3.3 低相关特性

例如：

- 仅做日志、告警、基础 O&M
- 与业务感知主线无直接识别/控制/计费/动作关联

保留为 `low`，不进入第一批工作面。

## 4. 命令筛选规则

### 4.1 强相关命令

满足任一条件，即可先打 `relevance=high` 候选：

1. 命令属于业务感知识别、规则、计费主链对象：

- `ADD FLOWFILTER`
- `ADD L7FILTER`
- `ADD RULE`
- `ADD RULEBINDING`
- `ADD USERPROFILE`
- `ADD URR`
- `ADD URRGROUP`
- `ADD PCCPOLICYGRP`
- `SET URRGRPBINDING`

2. 命令操作的 `ConfigObject` 位于业务感知主链：

- `FlowFilter`
- `L7Filter`
- `Rule`
- `RuleBinding`
- `UserProfile`
- `URR`
- `URRGroup`
- `PccPolicyGrp`

3. 命令文档路径位于：

- UDG 业务匹配策略 / 业务感知公共配置相关路径
- UNC 计费和策略的业务管理 / 内容计费 / PCC / 规则绑定相关路径

### 4.2 中相关命令

满足任一条件，即可先打 `relevance=medium` 候选：

1. 用于业务感知外围配置或环境支撑
2. 与配额动作、带宽、增强、安全等扩展主线有关
3. 与业务感知主链对象有关，但不是第一批闭包核心命令

### 4.3 低相关命令

例如：

- 通用 O&M 查询类命令
- 与业务感知无关的 NAT、DNS、基础维护命令

## 5. 对象链筛选规则

对象链不是独立发明出来的，而是从命令图谱对象关系中筛出来。

### 5.1 第一批主链

#### UDG 识别与执行主链

```text
FlowFilter / L7Filter
-> Rule
-> RuleBinding
-> UserProfile
```

#### UNC 计费与策略主链

```text
URR
-> URRGroup
-> PccPolicyGrp
-> Rule
-> RuleBinding
-> UserProfile
```

### 5.2 第二批扩展主链

- 配额动作主链
- 七层重定向主链
- 带宽控制主链
- 增强/防欺诈主链

## 6. 哪些可以用代码

### 6.1 特性候选筛选

代码可以基于：

- 目录路径
- 特性名称关键词
- 页面标题关键词

先产出：

- `business_related_features_candidates.csv`

字段建议：

- `feature_code`
- `feature_name`
- `vendor`
- `candidate_reason`
- `relevance_candidate`
- `evidence_id`

### 6.2 命令候选筛选

代码可以基于：

- `command-graph/data/raw/command_source_index.csv`
- `command-graph/data/stage1/config_objects.csv`
- `command-graph/data/stage1/command_object_actions.csv`

先产出：

- `business_related_commands_candidates.csv`

字段建议：

- `command_id`
- `command_name`
- `vendor`
- `object_id`
- `candidate_reason`
- `relevance_candidate`
- `evidence_id`

### 6.3 对象链候选筛选

代码可以基于：

- `config_object_relations_candidates.csv`
- 业务感知主链对象白名单

先产出：

- `business_related_object_chains_candidates.csv`

字段建议：

- `chain_id`
- `vendor`
- `object_path`
- `candidate_reason`
- `relevance_candidate`
- `evidence_ids`

## 7. 哪些必须 Agent 定稿

### 7.1 特性是否真属于业务感知主线

代码只能按关键词和目录先收候选，最终是否属于主线，需要 Agent 结合定义、作用、场景来判断。

### 7.2 命令是否只是外围支撑

例如某些 QoS、MEC、环境命令，可能与业务感知有关，但不是核心命令。

### 7.3 对象链是不是完整闭包的一部分

代码能筛出候选链，但是否构成：

- 主业务链
- 辅助链
- 环境支撑链

必须 Agent 判。

## 8. 当前建议的工作方式

先让代码尽量宽松地筛出候选集，再让 Agent 做两步：

1. 归并同类候选
2. 给出 `core / supporting / peripheral` 三档归类

这样业务图谱扩展时，就不会只围绕第一条闭包盲目推进，而是始终同步扩大业务感知相关特性和命令的覆盖面。
