# 业务感知图谱重构接手上下文 v0.1

## 1. 这份文档给谁看

这份文档是给“中途接手这个项目的 Agent”看的。

目标是让新 Agent 一拿到就知道：

1. 这个项目现在在做什么
2. 为什么要换路线
3. 当前该做哪一层
4. 哪些旧结果可以参考，哪些不能直接继承
5. 下一步具体怎么推进

## 2. 项目目标

项目目标不是单纯做“三层图谱”概念展示，而是：

```text
探索云核心网领域知识如何沉淀，
以及 Agent 如何准确使用这些知识，
最终支撑行业级数字员工。
```

“业务图谱 / 特性图谱 / 命令图谱”只是当前采用的一种组织方式，不是终极真理。

因此：

```text
schema 可以迭代，
对象类型可以调整，
承载形式也可以调整。
```

但底线不变：

```text
必须以原始产品文档为依据，
必须能形成结构化、可审查、可迭代的知识结果。
```

## 3. 当前阶段判断

旧的 `business-graph/data` 是一版顶向下的结果。  
它的价值在于：

1. 证明了业务、语义、特性、命令、证据可以分层组织
2. 沉淀了一批对象命名和桥接思路
3. 暴露了哪些层没有真正落稳

它的问题在于：

1. 业务层先行，底层对象有断层
2. 一些关系只是说明文字或 JSON 字段
3. 原始 `work/` schema 并不一定全部合理

因此项目现在决定：

```text
停止继续往旧 data 里补，
转到 data2，
改走底向上路线。
```

## 4. 当前必须遵守的新路线

### Phase 1：命令图谱

只处理命令层对象和关系。

### Phase 2：特性图谱

建立特性、可获得性、流程、变体、步骤，并与命令层挂接。

### Phase 3：业务图谱

最后再回到业务场景、方案、工程任务、语义桥接。

## 5. 当前工作目录

### 5.1 设计稿与历史讨论

目录：

`work\business-awareness-result`

用途：

1. 保存最初的 schema 设计稿
2. 保存命令层/特性层/业务层的早期讨论
3. 作为“旧思路参考”

注意：

```text
这个目录不是权威结果，
而是设计草稿和历史材料。
```

### 5.2 当前工作目录

目录：

`business-graph`

注意：

1. `data/` 是旧路线结果
2. `data2/` 是新路线结果

### 5.3 原始语料

#### UDG 命令

`output\UDG_Product_Documentation_CH_20.15.2\OM参考\命令\UDG MML命令`

#### UNC 命令

`output\UNC 20.15.2 产品文档(裸机容器) 05\OM参考\命令\UNC MML命令`

#### UDG 特性

`output\UDG_Product_Documentation_CH_20.15.2\特性部署\特性指南`

#### UNC 特性

`output\UNC 20.15.2 产品文档(裸机容器) 05\网络部署\特性部署`

## 6. 当前阶段的权威约束

对新 Agent 来说，当前最重要的约束只有五条：

1. 以原始产品文档为准
2. 先做命令层，不先做业务层
3. 新数据全部沉淀到 `business-graph/data2/`
4. 每完成一小步就要能被用户审查
5. 如果真实文档和旧 schema 冲突，以真实文档为准，反向修 schema

## 7. 当前 phase 1 的最小目标

当前只需要回答：

```text
命令图谱本层到底有哪些稳定对象和关系。
```

不要回答：

- 哪些命令属于哪个业务场景
- 哪些命令支撑哪个交付方案
- 哪些命令对应哪个业务语义对象

这些是后面的事。

## 8. phase 1 推荐对象与关系

### 对象

- `MMLCommand`
- `CommandParameter`
- `ConfigObject`
- `Evidence`

### 关系

- `acts_on`
- `has_parameter`
- `references`
- `binds`
- `contains`
- `supported_by`

## 9. 当前 phase 1 的重点难点

### 9.1 参数约束 vs 对象关系

必须分清：

1. 某参数何时必选，是参数约束
2. 某参数值引用已有对象，是对象关系

### 9.2 `references / binds / contains` 的边界

典型例子：

- `Rule -> PccPolicyGrp` 更像 `references`
- `RuleBinding -> Rule/UserProfile` 更像 `binds`
- `Pool -> Section` 更像 `contains`

### 9.3 `SET` 类命令的处理

`SET URRGRPBINDING` 这种命令容易混：

1. 它是命令
2. 它可能建立绑定关系
3. 它不一定创建一个新的持久对象

这里不要先拍脑袋定死，允许通过打样再调整。

## 10. 当前推荐的 data2 目录职责

### `data2/01-command-source`

放命令层原料索引。

### `data2/02-command-entities`

放命令、参数、配置对象等实体表。

### `data2/03-command-relations`

放命令到对象、命令到参数、对象到对象的关系表。

### `data2/04-command-evidence`

放证据表和证据支撑关系。

### `data2/90-review`

放 review 队列、对比结果、审查材料。

## 11. 当前推荐执行方式

### 第一步

只选一小组命令打样：

- `ADD RULE`
- `ADD RULEBINDING`
- `ADD PCCPOLICYGRP`
- `ADD URR`
- `ADD URRGROUP`
- `SET URRGRPBINDING`
- `ADD FLOWFILTER`
- `ADD L7FILTER`

### 第二步

从这些命令里抽：

1. 命令实体
2. 参数实体
3. 配置对象实体
4. 初步对象关系

### 第三步

让用户审对象粒度和关系分类：

- 哪些是对象
- 哪些只是参数属性
- 哪些关系应该保留

### 第四步

通过这一轮审查，反过来修 schema。

## 12. 当前不要做的事情

1. 不继续往旧 `data/` 补内容
2. 不先扩业务感知全景
3. 不先做可视化大图
4. 不为了闭包完整性强行发明跨层关系
5. 不把 `work/` 里的设计稿当成最终真相

## 13. 交接时的推荐阅读顺序

1. [13-data2-bottom-up-rebuild-plan-v0.1.md](13-data2-bottom-up-rebuild-plan-v0.1.md)
2. [work/business-awareness-result/09-command-graph-build-plan-v0.2.md](../work/business-awareness-result/09-command-graph-build-plan-v0.2.md)
3. [work/business-awareness-result/10-command-graph-extraction-pipeline-v0.1.md](../work/business-awareness-result/10-command-graph-extraction-pipeline-v0.1.md)
4. `business-graph/data2/README.md`
5. 原始命令文档

## 14. 一句话交接结论

如果你是新接手的 Agent，当前你的任务不是“继续补业务图谱”，而是：

```text
在 data2 中重新从命令层开始，
用原始命令文档验证对象和关系，
把命令图谱底座打稳。
```
