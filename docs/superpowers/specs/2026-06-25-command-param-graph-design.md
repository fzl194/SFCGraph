# 命令详情：参数展示 + 图谱视图设计

- **日期**：2026-06-25
- **范围**：命令图谱详情页（CommandDetail）新增"参数"tab 和"图谱"tab
- **状态**：设计待用户确认

## 1. 背景与目标

当前 `CommandDetail.vue` 左侧只有一个 MMLCommand tab（命令抽取字段），右侧原始文档。命令的**参数和关系**已在设计态抽取（`command_parameters.jsonl` + `has_parameter` + `depends_on` 边），但前端没展示、后端也没暴露。

目标：详情页左侧改为 3 个 tab——
1. **MMLCommand**（不变）：命令抽取字段
2. **参数**（新）：该命令的参数表
3. **图谱**（新）：命令 + 参数 + 关系的 vis-network 图

## 2. 已锁定决策

| 决策项 | 结论 |
|---|---|
| 参数匹配 | 严格按 `command_id`（`nf@version:command_name`），**不跨版本**；修 test.csv 版本 20.13.2→20.15.2 |
| Tab2 参数展示 | 精选列表格（7 列）+ 行展开看全 28 字段 |
| Tab3 图谱范围 | 完整：命令节点 + 参数节点 + has_parameter 边 + depends_on 边（边标条件） |
| Tab3 交互 | 静态全展示 + 拖拽缩放（范围限定单命令，不做 click-to-expand） |
| 图谱组装 | **后端组装**成 vis-network 就绪的 nodes/edges，前端直接渲染 |
| 图谱库 | vis-network（已装，复用 `feature_graph/FeatureDetail.vue` 范式） |
| 端点形态 | 两个新端点，各自单一职责，按 tab 懒加载 |
| 组件结构 | CommandDetail 拆成 tab 壳 + 新建 CommandParameters + CommandGraph 子组件 |

## 3. 数据现状（调研结论）

- `command_parameters.jsonl`：每条 CommandParameter **28 字段**（parameter_name/parameter_name_zh/data_type/required_mode/default_value/min_value/max_value/value_range/enum_values/description…）
- `command_has_parameter.jsonl`：边 `{edge_type, from_command_ref, to_parameter_ref}`
- `parameter_depends_on.jsonl`：边 `{edge_type, from_parameter_ref, to_parameter_ref, condition_ref, condition_logic, condition_value}`（样本为同命令内参数条件依赖）
- 后端现状：service.py 只统计参数数，**不暴露参数详情**；前端 `CommandDetail.vue:23` 有 `TODO 参数/配置对象 tab`
- vis-network `^9.1.9` 已在 `package.json`，`FeatureDetail.vue:469` 有完整使用范式
- **数据问题**：参数 command_id 是 `UDG@20.13.2:...`（test.csv 旧版），命令是 20.15.2 → 严格匹配会全空。修复见 §6.1

## 4. 后端设计（platform-next/command_graph/）

### 4.1 两个新端点

**端点 1：`GET /api/v1/command-graph/command-parameters`**（供 Tab2）
```
?nf=UDG&command_name=SET AUTOLOGPOLICY&version=20.15.2
→ { "parameters": [ {28字段完整记录}, ... ] }
```

**端点 2：`GET /api/v1/command-graph/command-graph`**（供 Tab3，后端组装）
```
?nf=UDG&command_name=SET AUTOLOGPOLICY&version=20.15.2
→ {
    "nodes": [ {id, label, group, title}, ... ],   # group: command | parameter | parameter_external
    "edges": [ {from, to, type, label?, title?}, ... ]
  }
```

### 4.2 service.py 改动

- `_load`：完整加载 `command_parameters.jsonl` / `command_has_parameter.jsonl` / `parameter_depends_on.jsonl`，按 (nf, version) 分桶索引（扫描自动发现，不写死文件名；关系文件此前已识别未加载，现在加载）
- `get_command_parameters(nf, command_name, version)`：按 `command_id = f"{nf}@{version}:{command_name}"` 严格匹配，返回参数列表
- `get_command_graph(nf, command_name, version)`：组装 vis 就绪结构
  - 命令节点 1 个（group=command）
  - 参数节点 N 个（group=parameter，label=parameter_name，title=中文名+类型+必选）
  - has_parameter 边（command→param，type=has_parameter）
  - depends_on 边（param→param，type=depends_on，**label=条件值**如 `=IPV4`，title=完整条件"参数 等于 值"）
  - depends_on 引用集合外参数时，补 group=parameter_external 节点纳入，不丢关系

### 4.3 router.py
新增两个端点，形参 `nf`（必填）/ `command_name`（必填）/ `version`（可选），与现有端点风格一致。

## 5. 前端设计（platform-next/frontend/src/command_graph/）

### 5.1 组件结构
```
CommandDetail.vue          ← tab 壳：3 个 el-tab-pane + 懒加载编排 + 右栏原始文档（不动）
├── Tab1: MMLCommand       ← 现有逻辑原样保留
├── Tab2: CommandParameters.vue  ← 新建
└── Tab3: CommandGraph.vue      ← 新建
```

### 5.2 CommandParameters.vue（Tab2）
- `el-table`，精选 7 列：参数标识 / 中文名 / 类型 / 必选 / 默认值 / 取值范围 / 说明摘要
- 行展开（`type="expand"`）：用"非空即展示"分区渲染该参数全部 28 字段（复用 `isNonEmpty`/`renderValue` 思路，参数有自己的 `LABEL_MAP`）
- 组件激活时调 `/command-parameters`
- 空状态：`该命令无参数`

### 5.3 CommandGraph.vue（Tab3）
- 容器 `div` + `await import('vis-network/standalone')`，参考 FeatureDetail.vue
- 组件激活时调 `/command-graph`，拿后端组装好的 `{nodes, edges}` 直接 `new DataSet` → `new Network`
- 节点按 group 着色（command/parameter/external 不同色），depends_on 边显示 label
- 静态全展示 + 拖拽/缩放（`interaction: {dragNodes, zoomView}`）
- 空状态：`该命令无参数，无可绘制关系`

### 5.4 懒加载编排（CommandDetail.vue）
- 进入详情只加载 Tab1（现有 `/command` + `/command-md`）
- `watch(leftTab)` + 已加载标记：切 Tab2 才请求 `/command-parameters`，切 Tab3 才请求 `/command-graph`，不重复请求

### 5.5 api.ts 新增
```ts
commandParameters: (nf, commandName, version) => `.../command-parameters?nf=..&command_name=..&version=..`,
commandGraph:      (nf, commandName, version) => `.../command-graph?nf=..&command_name=..&version=..`,
```

## 6. 数据修复、测试与范围

### 6.1 数据修复
- 拷 `command-graph/test.csv` → `CommandGraph/data/udg_params.csv`（CommandGraph 自包含）
- 版本列 `20.13.2` → `20.15.2`
- `pipeline.yaml` 的 `parameter_csv` 改指 `data/udg_params.csv`
- 重跑 `python build_all.py UDG 20.15.2` → 参数 command_id 对齐 20.15.2

### 6.2 测试
- 后端 service 单测：`get_command_parameters`、`get_command_graph`（组装正确、条件 label、外部参数补节点），小型 assets fixture
- 前端 `npm run build`（vue-tsc）通过；手测 3 tab、懒加载、空状态、拖拽缩放
- 端到端：用 `SET AUTOLOGPOLICY`（有参数 + 有 depends_on 条件依赖）验 Tab2/Tab3

### 6.3 范围边界
- 不在本次：ConfigObject 抽取与展示（架构留扩展点）；参数详情独立子页（已选行内展开）
- UNC 无参数文件 → Tab2/Tab3 空状态，不报错
- 跨命令 depends_on：防御性处理不丢关系，非重点

## 7. 风险与缓解

| 风险 | 缓解 |
|---|---|
| depends_on 引用集合外参数导致图混乱 | 后端补 parameter_external 节点 + 不同着色，关系不丢但不喧宾夺主 |
| 参数多的命令图拥挤 | 静态全展示 + 拖拽缩放可应对；若极端拥挤后续再加 click-to-expand（YAGNI 暂不做） |
| vis-network 与 Vue 3 生命周期/响应式冲突 | 参考 FeatureDetail.vue 已验证范式；Network 实例挂容器 ref，组件卸载时 destroy |
| csv 版本修复后行数/关系数变化 | 重跑后对比 parameters/edges 数与修复前一致（只改 version，行数不变） |
