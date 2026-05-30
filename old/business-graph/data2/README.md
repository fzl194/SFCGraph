# data2 说明

## 1. 定位

`data2/` 是新的底向上构建工作面。

它和旧的 `data/` 区别是：

| 目录 | 作用 |
| --- | --- |
| `data/` | 旧的顶向下结果，用于保留历史产物和对照 |
| `data2/` | 新的底向上结果，从命令层开始重新构建 |

## 2. 当前阶段

当前只做：

```text
Phase 1：命令图谱
```

不做：

- 特性图谱
- 业务图谱
- 跨层桥接

## 3. 目录结构

```text
data2/
  01-command-source/
  02-command-entities/
  03-command-relations/
  04-command-evidence/
  90-review/
```

## 4. 各目录职责

### `01-command-source`

放命令层原料索引。

例如：

- `command_source_index.csv`

### `02-command-entities`

放命令层实体表。

例如：

- `mml_commands.csv`
- `command_parameters.csv`
- `config_objects.csv`

### `03-command-relations`

放命令层关系表。

例如：

- `command_object_actions.csv`
- `command_parameter_mapping.csv`
- `config_object_relations.csv`

### `04-command-evidence`

放证据表和证据支撑关系。

例如：

- `evidence.csv`
- `evidence_support_mapping.csv`

### `90-review`

放审查材料和待确认队列。

例如：

- `relation_review_queue.csv`
- `schema_adjustment_notes.md`

## 5. 当前工作原则

1. 先命令层，后特性层，再业务层
2. 以原始命令 md 为准
3. schema 可以因真实数据而调整
4. 每次先打小样，再批量扩展
