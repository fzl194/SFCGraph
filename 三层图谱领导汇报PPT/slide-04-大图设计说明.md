# Slide 4 大图设计说明

## 页标题

三层图谱本体与关系全景图

## 页目标

用一张图完整回答以下问题：

1. 三层图谱里到底有哪些核心对象
2. 这些对象分别属于哪一层
3. 不同层之间靠什么关系连接
4. 顺序关系如何承载
5. 为什么这套图谱不是文档分类，而是配置知识本体

## 图的结构

整页采用自上而下五层结构：

1. 证据层
2. 业务图谱层
3. 特性图谱层
4. 任务原子层
5. 命令图谱层

整体阅读方向为：

```text
证据支撑
  ↓
业务问题与方案
  ↓
正式产品能力
  ↓
最小可复用配置动作
  ↓
底层命令、参数、配置对象
```

## 每层放置的对象

### 1. 证据层

- EvidenceSource

说明：
- 单独位于最上方
- 用浅灰色横条表示
- 向下以虚线连接各层

### 2. 业务图谱层

建议从左到右放：

- BusinessDomain
- NetworkScenario
- ConfigurationSolution
- BusinessRule
- DecisionPoint
- SemanticObject

核心关系：

- `BusinessDomain -> contains -> NetworkScenario`
- `NetworkScenario -> instantiated_as -> ConfigurationSolution`
- `ConfigurationSolution -> constrained_by -> BusinessRule`
- `NetworkScenario / ConfigurationSolution -> has_decision -> DecisionPoint`
- `NetworkScenario / ConfigurationSolution -> uses_semantic_object -> SemanticObject`

### 3. 特性图谱层

建议从左到右放：

- Feature
- SubFeature
- FeatureRule
- License
- DecisionPoint
- SemanticObject
- FeatureTaskOrderEdge

核心关系：

- `Feature -> has_subfeature -> SubFeature`
- `Feature / SubFeature -> depends_on -> Feature / SubFeature`
- `Feature / SubFeature -> requires_license -> License`
- `Feature / SubFeature -> constrained_by -> FeatureRule`
- `Feature / SubFeature -> has_decision -> DecisionPoint`
- `Feature / SubFeature -> uses_semantic_object -> SemanticObject`
- `Feature / SubFeature -> orchestrates -> FeatureTaskOrderEdge`

### 4. 任务原子层

建议从左到右放：

- ConfigTask
- TaskRule
- DecisionPoint
- SemanticObject
- TaskCommandOrderEdge

核心关系：

- `ConfigTask -> constrained_by -> TaskRule`
- `ConfigTask -> has_decision -> DecisionPoint`
- `ConfigTask -> targets -> SemanticObject`
- `ConfigTask -> orchestrates -> TaskCommandOrderEdge`

### 5. 命令图谱层

建议从左到右放：

- MMLCommand
- CommandParameter
- ConfigObject
- CommandRule

核心关系：

- `MMLCommand -> has_parameter -> CommandParameter`
- `MMLCommand -> operates_on -> ConfigObject`
- `CommandParameter -> references -> ConfigObject`
- `CommandRule -> governs -> MMLCommand / CommandParameter / ConfigObject`
- `ConfigObject <-> ConfigObject`

ConfigObject 之间的边可抽象表示为：

- `depends_on`
- `contains`
- `refers_to`
- `conflicts_with`
- `composed_by`

## 跨层主关系

这些关系建议用粗线高亮，作为全图主链：

### 业务到特性

- `ConfigurationSolution -> uses_feature -> Feature / SubFeature`
- `BusinessRule -> refined_by -> FeatureRule`
- `SemanticObject -> realized_by -> Feature / SubFeature`

### 业务到任务

- `ConfigurationSolution -> uses_task -> ConfigTask`
- `BusinessRule -> refined_by -> TaskRule`
- `SemanticObject -> realized_by -> ConfigTask`

### 特性到任务

- `Feature / SubFeature -> decomposes_to -> ConfigTask`
- `FeatureRule -> constrains_task -> ConfigTask`

### 任务到命令

- `ConfigTask -> invokes -> MMLCommand`
- `ConfigTask -> targets -> SemanticObject / ConfigObject`
- `TaskRule -> refined_by -> CommandRule`

## 顺序关系的展示方式

顺序关系不要和普通结构关系混在一起，建议在右侧单独做一个“编排关系”说明框。

框内只放两类：

### FeatureTaskOrderEdge

含义：
- 表达特性下 task 的稳定编排顺序

### TaskCommandOrderEdge

含义：
- 表达 task 内命令的稳定执行顺序

补一句注释：

- 方案级完整顺序当前不进入主 schema

## 视觉规则

### 配色

- 业务层：蓝色
- 特性层：绿色
- Task 层：橙色
- 命令层：红色
- 证据层：灰色

### 线型

- 主链关系：粗实线
- 规则约束：细虚线
- 证据支撑：浅灰虚线
- 编排顺序：高亮箭头线

### 布局

- 每层对象用圆角矩形节点
- 层与层之间保持明显水平分区
- 不要把所有关系都画满，重点保留主链和关键约束
- DecisionPoint、Rule、SemanticObject 作为跨层同构对象，可用同样形态但不同层颜色

## 页内讲解口径

这页建议只讲四句话：

1. 业务层定义问题空间、场景和方案。
2. 特性层定义正式能力与能力细分。
3. Task 层定义最小可复用配置动作。
4. 命令层定义最终配置执行本体。

最后补一句：

这张图的核心不是把对象堆在一起，而是把“业务问题、产品能力、复用任务、底层命令”分层解耦，再通过有限主关系打通。

## 这一页不应出现的内容

- 不要出现字段级 schema 表
- 不要出现过多英文长句解释
- 不要把所有边都标全
- 不要加入实现细节、CSV、脚本、数据库结构

这页是本体总图，不是落库设计图。
