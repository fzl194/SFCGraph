# 命令图谱统一图架构设计

> 日期：2026-06-26
> 范围：命令图谱层（先验证，架构预留跨层扩展）
> 状态：设计已获批，待 spec review
> 相关：`COMMAND_GRAPH_SCHEMA.md` §3（对象）/ §4（关系）；`platform-next/command_graph/`

---

## 1. 背景与目标

当前 platform-next 命令图谱前端只展示**单命令视图**（命令→参数→配置对象），service 按对象类型分桶加载 jsonl，各 API（`get_command` / `get_command_graph`）独立拼接。问题：

- 点边**分散分桶**，没有统一图模型
- 前端**不能按需取子图**，固定单命令视图
- **缺跨命令引用**（references）+ 对象间引用（refers_to）展示
- 三层（command/business/feature）各自独立，**不能跨层**

**目标**：把命令图谱所有点边合并成**一张内存图**（统一 node/edge 模型），前端用 `get_subgraph` 按需取子图渲染，支持跨命令引用 + 对象间引用。架构通用，**预留跨层**（business/feature + 跨层边）。

## 2. 当前架构

| 层 | 数据源 | 存储/查询 | 现状 |
|---|---|---|---|
| command_graph | jsonl（mml_commands / parameters / config_objects + 各 edges）| service 按对象分桶 + 各自 API | 点边都有，但分桶、单命令视图 |
| business_graph | 三层图谱 md（00-06）| graph_parser 解析 → Scenario/Domain/Section | md 解析，非图结构 |
| feature_graph | 特性 csv/列配置 | service 按特性 | 表格，非图 |

三层各自独立（数据源/存储/查询），**无统一点边模型，不能跨层查询**。

## 3. 设计

### 3.1 统一点边模型

```
node = { id, type, label, properties }
edge = { from, to, type, properties }
```

- **node.id** = 四段实例键（`UDG@20.15.2@MMLCommand@ADD URR`）
- **node.type** ∈ {MMLCommand, CommandParameter, ConfigObject}
- **node.label** = 展示名（command_name / parameter_name / object_name）
- **node.properties** = 原对象字段（object_kind / parameter_name_zh / ...）
- **edge.from / to** = 实例键
- **edge.type** ∈ {`has_parameter`, `conditional_required`, `references`, `creates`, `modifies`, `deletes`, `sets`, `queries`, `operates_on`, `refers_to`}
- **edge.properties** = 边属性（source_condition / binding_strength / cascade_delete / via_parameter / condition_value / ...）

**jsonl → 统一点边映射**：

| jsonl | → 统一 |
|---|---|
| mml_commands.jsonl | nodes(type=MMLCommand) |
| command_parameters.jsonl | nodes(type=CommandParameter) |
| config_objects.jsonl | nodes(type=ConfigObject) |
| command_has_parameter.jsonl | edges(type=has_parameter, command→parameter) |
| parameter_depends_on.jsonl | edges(type=**conditional_required**, parameter→parameter)【depends_on 改名】|
| parameter_references.jsonl | edges(type=references, parameter→parameter 跨命令) |
| command_object_edges.jsonl | edges(type=creates/modifies/..., command→object) |
| object_refers_to.jsonl | edges(type=refers_to, object→object) |

### 3.2 内存图（adjacency dict）

service 启动加载所有 jsonl → 合并统一 nodes/edges → 建 adjacency 常驻内存：

```python
adjacency = {
  node_id: {
    "node": {...},
    "out": [(to_id, edge_type, edge_props), ...],
    "in":  [(from_id, edge_type, edge_props), ...],
  }
}
```

查询走 BFS 遍历 adjacency。

### 3.3 API: get_subgraph

```
GET /api/v1/command-graph/subgraph?center=<node_id>&hops=2&edge_types=has_parameter,creates,references
```

- **center**：中心节点实例键
- **hops**：跳数（默认 2，**上限 3**，防爆炸）
- **edge_types**：可选边类型过滤（逗号分隔；缺省 = 所有类型）

返回（vis-network 直接渲染格式）：

```json
{
  "nodes": [{"id","type","label","properties"}],
  "edges": [{"from","to","type","properties"}]
}
```

实现：BFS from center，沿 out + in 边扩展 N 跳（edge_types 过滤），收集 nodes/edges（去重）。

### 3.4 前端通用图视图

- **通用图组件**（vis-network）：输入 `{nodes, edges}`，按 `node.type` 配色/形状渲染
  - MMLCommand = 青色 box；CommandParameter = 白边 ellipse；ConfigObject = 紫色 diamond（沿用现有图谱配色）
- **命令详情「图谱」tab** 改调 `get_subgraph(center=命令, hops=2, edge_types=[has_parameter,creates,references,conditional_required,refers_to])` —— 一次拿到 命令 + 参数 + 配置对象 + 跨命令引用 + 对象间引用
- 边按 type 配色/label：has_parameter 淡灰；conditional_required/references 青色 + label；creates/modifies 紫；refers_to 紫虚线

### 3.5 depends_on → conditional_required

趁统一一起改名（schema §4.4.1 已定义 `conditional_required`）：

- **builder parameter step**：产出 `edge_type: depends_on` → `conditional_required`
- **service**：读 `conditional_required`（不再 depends_on）
- **前端 CommandGraph**：`depends_on` → `conditional_required`
- 文件名 `parameter_depends_on.jsonl` → `parameter_conditional_required.jsonl`（PRODUCT_FILE 同步）

### 3.6 跨层预留

点边模型通用（`node.type` 标识所属层）。架构跑通后：

- business/feature 点边按**同模型**合并（node.type 加 BusinessObject/Feature/ConfigTask 等）
- 加跨层边（`ConfigTask invokes MMLCommand`、`Feature decomposes_to ConfigTask`、`TaskRule refined_by CommandRule` 等）
- 同一套 `get_subgraph` 即可**跨层查询**（center=特性，hops 跨层到命令/参数）

## 4. 组件改造

### 4.1 service.py
- **新增**：统一图加载（`_load_graph` → 合并所有 jsonl 到 adjacency）
- **新增**：`get_subgraph(center, hops, edge_types)` → BFS 子图
- **新增加载**：parameter_references + object_refers_to（之前没加载）
- **保留**：`get_command` / `list_commands` / `get_command_parameters` / `get_command_object`（列表/详情/参数 tab/配置对象 tab，非图视图）
- **废弃/改造**：`get_command_graph`（旧单命令图谱）→ 改为调 `get_subgraph`，或直接前端改调 `/subgraph`

### 4.2 router.py
- **新增**：`GET /subgraph`

### 4.3 前端
- `api.ts`：加 `subgraph(center, hops, edge_types)`
- `CommandGraph.vue`：改调 `get_subgraph`（命令 2 跳），node.type 配色 + 跨命令引用 / 对象间引用边渲染
-（可选）通用 `<GraphView>` 组件（输入 nodes/edges，复用于未来跨层）

### 4.4 builder（depends_on 改名）
- `parameter` step：`edge_type: depends_on` → `conditional_required`；输出文件名 + PRODUCT_FILE 同步

## 5. 数据流

```
内网规则 + md → builder 各 step → jsonl（点边分散）
  → service 启动加载 → 统一内存图（adjacency）
  → get_subgraph(center, hops, edge_types) → {nodes, edges}
  → 前端 vis-network 渲染
```

## 6. 边界 / 约束

- **hops 上限 3**（防爆；前端默认 2）
- **edge_types 过滤**（避免无关边污染子图）
- **规模**：命令图谱几千节点 / 几万边，内存图足够；跨层扩展后再评估（必要时换 NetworkX / Neo4j）
- **向后兼容**：`get_command` / `list_commands` / `get_command_parameters` / `get_command_object` 保留（列表/详情/参数 tab/配置对象 tab 仍用）；`get_command_graph` 改 `/subgraph`
- **depends_on 改名全链路同步**：builder / service / 前端 / schema 一致

## 7. 测试

- **service get_subgraph**：BFS 正确性（center + hops + edge_types 过滤），含跨命令 references / 对象间 refers_to，单元测试
- **内存图加载**：所有 jsonl → adjacency，节点/边数 + 索引正确
- **depends_on → conditional_required**：builder 产出 + service 读取一致
- **前端**：get_subgraph 渲染（命令 2 跳含跨命令引用 + 对象间引用）

## 8. 实现步骤（高层）

1. **builder**：parameter step `depends_on` → `conditional_required`（文件名 + edge_type + PRODUCT_FILE）
2. **service**：统一图加载（`_load_graph` → adjacency）+ 加载 parameter_references / object_refers_to
3. **service**：`get_subgraph(center, hops, edge_types)` + BFS
4. **router**：`/subgraph` 端点
5. **前端 api**：`subgraph(center, hops, edge_types)`
6. **前端 CommandGraph**：改调 `get_subgraph` + node.type 配色 + 跨命令/对象间引用渲染
7. **测试 + 验证**（单命令图谱含跨命令引用）

## 9. 未来扩展（跨层，本期不做）

- business/feature 点边按同模型合并
- 跨层边（`ConfigTask invokes MMLCommand`、`Feature decomposes_to ConfigTask`、`TaskRule refined_by CommandRule`）
- `get_subgraph` 跨层查询（center=特性 → hops 跨层到命令/参数）
- 统一图平台（所有层一张图，前端通用 `<GraphView>` 组件跨层浏览）
