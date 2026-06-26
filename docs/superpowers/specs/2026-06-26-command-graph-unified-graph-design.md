# 命令图谱统一图架构设计

> 日期：2026-06-26（rev2：按 spec review 修复 B1/B2/M1-M4/m1-m5）
> 范围：命令图谱层（先验证，架构预留跨层扩展）
> 状态：设计已获批，spec review 修复中
> 相关：`CommandGraph/COMMAND_GRAPH_SCHEMA.md` §3（对象）/ §4（关系）；`platform-next/command_graph/`

---

## 1. 背景与目标

当前 platform-next 命令图谱前端只展示**单命令视图**（命令→参数→配置对象），service 按对象类型分桶加载 jsonl，各 API（`get_command` / `get_command_graph`）独立拼接。问题：

- 点边**分散分桶**，没有统一图模型
- 前端**不能按需取子图**，固定单命令视图
- **缺跨命令引用**（references）+ 对象间引用（refers_to）展示
- 三层（command/business/feature）各自独立，**不能跨层**

**目标**：把命令图谱所有点边合并成**一张内存图**（统一 node/edge 模型），前端用 `get_subgraph` 按需取子图渲染，支持跨命令引用 + 对象间引用。架构通用，**预留跨层**。

## 2. 当前架构

| 层 | 数据源 | 存储/查询 |
|---|---|---|
| command_graph | jsonl（mml_commands/parameters/config_objects + 各 edges）| service 按对象分桶 + 各自 API |
| business_graph | 三层图谱 md（00-06）| graph_parser 解析 → Scenario/Domain |
| feature_graph | 特性 csv | service 按特性 |

三层各自独立，**无统一点边模型，不能跨层**。

## 3. 设计

### 3.1 统一点边模型 + jsonl 字段映射

```
node = { id, type, label, properties }
edge = { from, to, type, properties }
```

**本期加载的边类型**（已抽资产，对应 schema §4.2/4.3/4.4.1/4.4.2/4.5-refers_to）：

| edge.type | schema | jsonl 来源 | from 字段 → 统一 from | to 字段 → 统一 to | edge.type 来源 |
|---|---|---|---|---|---|
| `has_parameter` | §4.2 | command_has_parameter.jsonl | `from_command_ref` | `to_parameter_ref` | 硬编码 has_parameter |
| `conditional_required` | §4.4.1 | parameter_depends_on.jsonl | `from_parameter_ref` | `to_parameter_ref` | 硬编码（原 edge_type=depends_on 改名）|
| `references` | §4.4.2 | parameter_references.jsonl | `from_parameter_ref` | `to_parameter_ref` | `edge_type` 字段 |
| `creates`/`modifies`/`deletes`/`sets`/`queries`/`operates_on` | §4.3 | command_object_edges.jsonl | `from_command_ref` | `to_object_ref` | `edge_type` 字段（动词派生；verb 未映射时 builder 产 `operates_on` 后备）|
| `refers_to` | §4.5 | object_refers_to.jsonl | `from_object_ref` | `to_object_ref` | `edge_type` 字段 |

> **`operates_on` 语义**：builder `config_object._build_edge` 对未映射动词的命令产出 `operates_on`（后备），是真实边类型，会进邻接表。
>
> **本期不加载**（schema 定义但资产未抽/未产出）：object→object 的 `has/contains/composed_by/conflicts_with/depends_on`（§4.5 其余）、command→command `must_precede/must_be_last/refers_to/modifies_target_of/removes_target_of`（§4.6）、CommandRule `governs`（§4.7，CommandRule 未抽）、**command→object 的 `binds`（§4.3——builder 当前未对任何 verb 映射 binds，BIND 命令按 verb 分流到 creates/modifies/deletes，资产中 binds=0）**。这些 edge.type 不在当前枚举内，等对应资产抽出/产出再并入。

**点**：
- `id` = 四段实例键（`UDG@20.15.2@MMLCommand@ADD URR`）
- `type` ∈ {MMLCommand, CommandParameter, ConfigObject}
- `label` = command_name / parameter_name / object_name
- `properties` = 原对象字段（object_kind / parameter_name_zh / ...）

**边**：
- `from/to` = 实例键（按上表从各 jsonl 的 `*_ref` 字段取）
- `type` = 上表 edge.type
- `properties` = 边属性（各 jsonl 自带：`source_condition`/`binding_strength`/`cascade_delete`/`via_parameter`/`condition_ref`/`condition_logic`/`condition_value` 等，原样保留）

### 3.2 内存图（adjacency dict）

service 启动加载所有 jsonl → 按上表合并统一 nodes/edges → 建 adjacency 常驻内存：

```python
adjacency = {
  node_id: {
    "node": {...},
    "out": [(to_id, edge_type, edge_props), ...],
    "in":  [(from_id, edge_type, edge_props), ...],
  }
}
```

> **(nf, version) 隔离**：邻接表是**全局扁平**字典，以完整四段实例键（含 `nf@version`）为键。`(nf, version)` 隔离**隐式**保留——实例键已含 `nf@version`，不同层（UDG@20.15.2 / UNC@20.15.2）的节点天然不会混淆，无需嵌套分桶。

### 3.3 API: get_subgraph

```
GET /api/v1/command-graph/subgraph?center=<node_id>&hops=2&edge_types=has_parameter,creates,references
```

- **center**：中心节点实例键（**前端须 `encodeURIComponent`**——实例键含 `@` 和空格，如 `UDG@20.15.2@MMLCommand@ADD URR`）
- **hops**：跳数（默认 2，**上限 3**，防爆）
- **edge_types**：可选边类型过滤（逗号分隔；缺省 = 所有本期类型）

返回（vis-network 直接渲染格式）：
```json
{"nodes": [{"id","type","label","properties"}], "edges": [{"from","to","type","properties"}]}
```

**BFS 语义**：
- `edge_types` **既限制遍历也限制包含**（不在列表的边不扩展、不返回）
- **去重**：node 按 `id` 去重；edge 按 **身份** `(from, to, type, properties)` 去重——同对节点间的多条不同条件边（如多条 conditional_required）**各自保留**，不合并。**实现注**：`properties` 是 dict 不可直接 hash，须先序列化为稳定字符串（`json.dumps(props, sort_keys=True)`）或元组再入 set；否则 TypeError，或回退到 `(from,to,type)` 去重会错误合并多条件边（实测 UDG 有 17 对节点挂多条 conditional_required）

### 3.4 前端通用图视图

- **node.type 配色/形状**：MMLCommand 青色 box；CommandParameter 白边 ellipse；ConfigObject 紫色 diamond（沿用 `CommandGraph.vue` 现有）；外部命令的参数（references 目标）渲染为 `parameter_external` 组（虚边框，弱化）
- **边按 type 配色/label**：has_parameter 淡灰无 label；conditional_required/references 青色 + label（条件）；creates/modifies/sets/queries 紫 + label；refers_to 紫虚线；operates_on/binds 灰
- **命令详情「图谱」tab** 改调 `get_subgraph(center=命令, hops=2, edge_types=[has_parameter,creates,references,conditional_required,refers_to])`

> **hops=2 可见性说明**：命令→参数(1)/对象(1)；参数→references 目标参数(2，跨命令)；对象→refers_to 目标对象(2)。**注意**：跨命令 `references` 的目标参数所属的**命令节点**在 hops=2 内不会自动出现（它是目标参数的 1 跳，但从 center 算是 3 跳）。若需把目标命令也画进来，前端可：① 用 hops=3；② 或单独再发一次 get_subgraph(center=目标参数, hops=1)。默认 hops=2 够展示"引用了谁的参数"，是否画目标命令按需。

### 3.5 depends_on → conditional_required（字段保留）

趁统一一起改名（schema §4.4.1）：

- **builder parameter step**：`edge_type: depends_on` → `conditional_required`
- **边字段保留不变**（builder 现有产出）：`from_parameter_ref` / `to_parameter_ref` / **`condition_ref` / `condition_logic` / `condition_value`**
- **schema §4.4.1 同步**（实现时改）：把之前理想化的 `{condition_value, condition_expression, required_mode}` 对齐为 builder 实际的 `{condition_ref, condition_logic, condition_value}`
- **service**：读 `conditional_required`（不再 depends_on）
- **前端**：`depends_on` → `conditional_required`
- **文件名** `parameter_depends_on.jsonl` → `parameter_conditional_required.jsonl`（`PRODUCT_FILE` 同步）

### 3.6 跨层预留

点边模型通用（`node.type` 标识所属层）。未来：business/feature 点边按同模型合并（node.type 加 BusinessObject/Feature/ConfigTask）+ 跨层边（`ConfigTask invokes MMLCommand`、`Feature decomposes_to ConfigTask`）+ 同一套 get_subgraph 跨层查询。

## 4. 组件改造

### 4.1 service.py
- **新增** `_load_graph`：按 §3.1 表加载所有 jsonl → 统一 nodes/edges → adjacency dict
- **新增加载**：parameter_references + object_refers_to（之前未加载）
- **改名同步**：`_load` 的 object_type 分支 `parameter_depends_on` → `parameter_conditional_required`（配合 §3.5 文件改名，否则新 builder 产出的文件被静默跳过）
- **新增** `get_subgraph(center, hops, edge_types)` → BFS 子图（§3.3 语义）
- **保留不动**：`get_command` / `list_commands` / `get_command_parameters` / `get_command_object`（列表/详情/参数 tab/配置对象 tab，非图视图）
- **`get_command_graph`（旧单命令图谱）**：**保留现有语义不封装**（它有特殊行为：`parameter_external` 组节点、空命令节点保证、`param_by_id` 成员判断——见 service.py 现状）。前端命令图谱 tab **改调 `get_subgraph`** 而非 `get_command_graph`；`get_subgraph` 的 BFS 天然把 references 的外部参数作为邻居节点返回，前端按 `parameter_external` 组渲染（虚边框）。`get_command_graph` 暂留作向后兼容，后续可废弃。

### 4.2 router.py
- **新增** `GET /subgraph`

### 4.3 前端
- `api.ts`：加 `subgraph(center, hops, edge_types)`（center 用 `encodeURIComponent`）
- `CommandGraph.vue`：改调 `get_subgraph`（命令 2 跳）+ node.type/edge.type 配色 + 跨命令 references / 对象间 refers_to 边渲染 + 外部参数 `parameter_external` 组

### 4.4 builder（depends_on 改名）
- `parameter` step：`edge_type` depends_on → conditional_required；输出文件名 + `PRODUCT_FILE` 同步
- schema §4.4.1 字段对齐（condition_ref/condition_logic/condition_value）

## 5. 数据流

```
内网规则 + md → builder 各 step → jsonl（点边分散，字段名各异）
  → service _load_graph（按 §3.1 表映射 from/to + edge.type）→ 统一内存图（adjacency）
  → get_subgraph(center, hops, edge_types) BFS → {nodes, edges}
  → 前端 vis-network 渲染
```

## 6. 边界 / 约束

- **hops 上限 3**（防爆；前端默认 2；跨命令目标命令节点需 hops=3 或二次查询，见 §3.4）
- **edge_types 既限遍历也限包含**（§3.3）
- **规模**：命令图谱几千节点 / 几万边，内存图足够；跨层扩展后再评估
- **向后兼容**：`get_command` / `list_commands` / `get_command_parameters` / `get_command_object` / `get_command_graph` 全保留；前端图谱 tab 改 get_subgraph
- **depends_on 改名全链路同步**：builder / service / 前端 / schema §4.4.1
- **center URL 编码**：前端 `encodeURIComponent`（实例键含 `@` 空格）
- **UNC 子图退化**：UNC 暂无参数资产（无 parameter_*），UNC 命令 `get_subgraph` 子图仅含 command→object，非 bug（loader 通用，有则加载）

## 7. 测试

- **_load_graph**：所有 jsonl → adjacency，节点/边数 + from/to 字段映射正确（按 §3.1 表）
- **get_subgraph BFS**：center + hops + edge_types 过滤（既限遍历也限包含）；跨命令 references / 对象间 refers_to 命中；node by id 去重、edge by 身份去重（同对多条件边保留）
- **depends_on → conditional_required**：builder 产出 + service 读取 + 字段（condition_ref/logic/value）保留
- **前端**：get_subgraph 渲染（命令 2 跳含跨命令引用 + 对象间引用 + 外部参数 parameter_external 组）

## 8. 实现步骤（高层）

1. **builder**：parameter step `depends_on`→`conditional_required`（edge_type + 文件名 + PRODUCT_FILE）；schema §4.4.1 字段对齐
2. **service `_load_graph`**：按 §3.1 表加载所有 jsonl（含 parameter_references/object_refers_to）→ adjacency
3. **service `get_subgraph`**：BFS（center + hops + edge_types 过滤 + 去重）
4. **router** `/subgraph`
5. **前端 api** `subgraph`（encodeURIComponent）
6. **前端 CommandGraph**：改 get_subgraph + 配色 + 跨命令/对象间引用 + parameter_external
7. **测试 + 验证**

## 9. 未来扩展（跨层，本期不做）

- business/feature 点边按同模型合并
- 跨层边（ConfigTask invokes MMLCommand、Feature decomposes_to ConfigTask、TaskRule refined_by CommandRule）
- `get_subgraph` 跨层查询（center=特性 → hops 跨层到命令/参数）
- object→object 其余关系（has/contains/...）、command→command（must_precede/...）、CommandRule governs——待对应资产抽出
