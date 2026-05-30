# 业务图谱对象 Schema 与展示模型

## 目标

本文件定义：

```text
本次“业务感知业务图谱”展示版
到底使用哪些对象 schema
以及这些对象在展示中如何分层表达
```

## 对象 Schema

### 一、业务层核心对象

- `BusinessDomain`
- `NetworkScenario`
- `ReferencePattern`
- `DeliverySolution`
- `EngineeringTask`

### 二、支撑与约束对象

- `Participant`
- `Scope`
- `DecisionPoint`
- `RuntimeFlow`
- `ValidationPlan`
- `DiagnosisRule`
- `RiskConstraint`
- `Evidence`

### 三、向下桥接对象

- `DomainSemanticObject`
- `Capability`
- `Feature`
- `ConfigObject`

## 展示原则

这版不是把所有 schema 平铺展示，而是按“整体认知优先”的方式分三层：

### 1. 业务层

回答：

- 业务感知这个域包含哪些场景
- 每类场景在解决什么问题
- 文档中有哪些参考范式
- 可能形成哪些交付方案候选

### 2. 支撑层

回答：

- 场景对谁生效
- 有哪些关键参与方
- 有哪些关键决策点
- 方案如何验证、诊断、受什么约束

### 3. 桥接层

回答：

- 业务语义如何向下连接能力、特性、配置对象
- UDG/UPF 与 UNC/SMF 分别主要承接什么

## 第一版重点展开对象

### 必展开

- `BusinessDomain`
- `NetworkScenario`
- `ReferencePattern`
- `DeliverySolution`
- `EngineeringTask`
- `Participant`
- `RuntimeFlow`
- `ValidationPlan`
- `RiskConstraint`
- `DomainSemanticObject`
- `Feature`

### 骨架保留，必要时轻展开

- `Scope`
- `DecisionPoint`
- `DiagnosisRule`
- `Capability`
- `ConfigObject`
- `Evidence`

## 关键区分

### `ReferencePattern`

含义：

```text
产品文档中已有的参考范式或样板
```

### `DeliverySolution`

含义：

```text
面向现网交付问题归纳出来的方案候选
```

展示时必须显式区分二者，避免把“文档样例”误讲成“图谱里的交付方案”。

## 侧别表达

第一版显式区分：

- `UDG/UPF 侧`
- `UNC/SMF 侧`

其中：

- UDG/UPF 更偏识别、规则匹配、动作执行、用户面落地
- UNC/SMF 更偏策略承接、计费控制、配额控制、控制面编排

该判断后续需由原始语料逐轮修正，不在本页直接定死。
