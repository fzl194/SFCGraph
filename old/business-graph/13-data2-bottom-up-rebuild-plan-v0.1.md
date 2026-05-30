# data2 底向上重构计划 v0.1

## 1. 这次路线为什么要改

当前 `business-graph/data` 的问题不是完全错误，而是：

```text
它主要按顶向下方式先定义了业务层、语义层、方案层，
再回填特性和命令。
```

这样做的问题是：

1. 中间桥接容易断层
2. 部分关系只能先写成说明文字
3. 容易把还没验证稳定的 schema 直接投射到数据层

所以接下来改成：

```text
先从命令图谱底座开始，
再往上长特性图谱，
最后再回到业务图谱。
```

这不是推翻原设计，而是换构建顺序。

## 2. data2 的定位

`data2/` 是新的构建工作面，只承载：

```text
底向上重构后的新数据
```

原则：

1. 不覆盖 `data/`
2. 不假定 `work/business-awareness-result/` 的 schema 全都正确
3. 每一阶段都允许反向修正 schema
4. 每个对象和关系都尽量回到原始产品文档

因此：

```text
work/ 里的 schema 是“待验证设计稿”
data2/ 里的数据是“经原始文档验证后的落地结果”
```

## 3. 新路线总览

### Phase 1：命令图谱

只处理命令图谱相关对象和关系，先把最底层打稳。

关注：

- `MMLCommand`
- `CommandParameter`
- `ConfigObject`
- `Evidence`
- 命令到对象动作关系
- 对象到对象关系

### Phase 2：特性图谱

在命令图谱之上构建特性层。

关注：

- `Feature`
- `FeatureAvailability`
- `FeatureProcedure`
- `ProcedureVariant`
- `ProcedureStep`
- 特性到命令/配置对象的挂接

### Phase 3：业务图谱

最后才回到：

- `NetworkScenario`
- `DeliverySolution`
- `EngineeringTask`
- `DomainSemanticObject`

这时业务图谱不再凭空抽象，而是挂在已经验证过的命令层和特性层之上。

## 4. 第一阶段边界

第一阶段只考虑：

```text
命令图谱相关对象
```

明确不做：

1. 不先建业务场景
2. 不先建交付方案
3. 不先建语义对象到业务场景的映射
4. 不为了凑闭包提前发明跨层关系

第一阶段的问题只有一个：

```text
从真实命令文档出发，
命令世界里到底有哪些稳定对象、参数和关系。
```

## 5. 第一阶段输入语料

以原始命令文档为准。

### UDG

路径：

`output\UDG_Product_Documentation_CH_20.15.2\OM参考\命令\UDG MML命令`

### UNC

路径：

`output\UNC 20.15.2 产品文档(裸机容器) 05\OM参考\命令\UNC MML命令`

说明：

1. 可以参考 `work/business-awareness-result/09` 和 `10`
2. 可以参考已有 `command-graph/` 代码
3. 但最终抽取结论必须能回到原始命令 md

## 6. 第一阶段建议 schema

第一阶段不要把 schema 铺太大，先收敛到命令层最小稳定集合。

### 6.1 对象

| 对象 | 中文名 | 是否进入 phase 1 |
| --- | --- | --- |
| `MMLCommand` | MML命令 | 是 |
| `CommandParameter` | 命令参数 | 是 |
| `ConfigObject` | 配置对象 | 是 |
| `Evidence` | 证据 | 是 |

### 6.2 关系

| 关系 | 中文名 | 是否进入 phase 1 |
| --- | --- | --- |
| `acts_on` | 命令作用于对象 | 是 |
| `has_parameter` | 命令拥有参数 | 是 |
| `references` | 对象引用对象 | 是 |
| `binds` | 对象绑定对象 | 是 |
| `contains` | 对象包含对象 | 是 |
| `supported_by` | 对象或关系由证据支撑 | 是 |

### 6.3 暂不进入 phase 1

| 对象/关系 | 原因 |
| --- | --- |
| `RuntimeObject` / `RuntimeEvent` | 不是命令层最底座 |
| `FeatureProcedure` / `ProcedureVariant` | 属于特性层 |
| `NetworkScenario` / `DeliverySolution` | 属于业务层 |
| `semantic_*` | 属于更上层桥接 |

## 7. 第一阶段产物要求

第一阶段必须产出结构化文件，不接受只在 md 里总结。

建议最小结果集：

### 7.1 实体表

1. `mml_commands.csv`
2. `command_parameters.csv`
3. `config_objects.csv`
4. `evidence.csv`

### 7.2 关系表

1. `command_object_actions.csv`
2. `command_parameter_mapping.csv`
3. `config_object_relations.csv`
4. `evidence_support_mapping.csv`

说明：

- `command_parameter_mapping.csv` 可以独立落，也可以并入参数表，后续可迭代
- 当前先允许最小实现，不把字段一次性定死

## 8. 第一阶段工作方式

采用：

```text
Code 主抽取
LLM 辅助判别
结果回到结构化文件
人工审查再迭代
```

### Code 负责

1. 命令标题识别
2. 参数表机械抽取
3. 证据节点生成
4. 初步配置对象识别
5. 初步关系候选生成

### LLM 负责

1. 歧义对象归一
2. `references / binds / contains` 判别
3. 参数提示到底是参数约束还是对象关系的判断
4. 高歧义命令用途归纳

### 人工负责

1. 看抽取原则是否对齐
2. 看对象粒度是否合理
3. 看 schema 是否需要调整

## 9. 这一轮最关键的工程纪律

### 9.1 先做对象和本层关系

不要在 phase 1 提前写：

- 业务感知相关场景
- 业务语义对象
- 方案闭包

### 9.2 每次只修一层

当前只修命令层。

### 9.3 schema 可以被数据反推修正

如果原先 `work/` 中的 schema 定义和原始命令文档不匹配，应以原始文档为准修 schema，而不是硬套 schema。

## 10. 下一步执行顺序

下一步不要直接扩数据量，先做：

1. 建 `data2/` 目录结构
2. 固定 phase 1 的表清单
3. 先抽一小组命令打样
4. 审对象粒度和关系类型
5. 再决定是否批量扩

建议第一批打样命令：

### UDG

- `ADD RULE`
- `ADD FLOWFILTER`
- `ADD L7FILTER`
- `ADD RULEBINDING`
- `ADD PCCPOLICYGRP`
- `ADD URR`
- `ADD URRGROUP`

### UNC

- `ADD RULE`
- `ADD RULEBINDING`
- `ADD PCCPOLICYGRP`
- `ADD URR`
- `ADD URRGROUP`
- `SET URRGRPBINDING`

## 11. 当前结论

接下来应把 `business-graph` 的主要工作理解成：

```text
不是继续在旧的顶向下 data 上补字段，
而是在 data2 上重新走一遍底向上构建。
```

第一阶段只做命令图谱。  
等命令层稳定后，再进入特性层。  
业务层最后重建。
