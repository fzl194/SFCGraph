# 命令详情：参数展示 + 图谱视图 实现计划

> **For agentic workers:** 用 superpowers:subagent-driven-development 实施。步骤用 `- [ ]` 跟踪。

**Goal:** 给命令详情页加"参数"tab（表格）和"图谱"tab（vis-network 图），后端组装图谱数据。

**Architecture:** 后端完整加载参数+两种关系边，新增 `/command-parameters`（参数列表）和 `/command-graph`（组装好的 nodes/edges）两端点；前端 CommandDetail 拆成 tab 壳 + CommandParameters + CommandGraph 子组件，按 tab 懒加载；先修 csv 版本让参数对齐 20.15.2。

**Tech Stack:** Python/FastAPI · Vue 3 + Element Plus + vis-network · pytest

**Spec:** `docs/superpowers/specs/2026-06-25-command-param-graph-design.md`

---

## Chunk 1: 数据修复（让参数对齐 20.15.2）

**Files:**
- Create: `CommandGraph/data/udg_params.csv`（从 `command-graph/test.csv` 拷贝，版本列改 20.15.2）
- Modify: `CommandGraph/pipeline.yaml`（parameter_csv 改指 data/udg_params.csv）

- [ ] **Step 1:** 拷 `command-graph/test.csv` → `CommandGraph/data/udg_params.csv`
- [ ] **Step 2:** 把 `网元版本` 列所有 `20.13.2` → `20.15.2`（456 行，其他不动）
- [ ] **Step 3:** `pipeline.yaml` 的 UDG `parameter_csv: command-graph/test.csv` → `data/udg_params.csv`
- [ ] **Step 4:** 重跑 `python CommandGraph/build_all.py UDG 20.15.2`
- [ ] **Step 5:** 验证：`command_parameters.jsonl` 行数仍 443（只改版本，行数不变）；command_id 现在是 `UDG@20.15.2:...`；pytest 仍全绿

---

## Chunk 2: 后端（platform-next/command_graph/）

**Files:**
- Modify: `platform-next/command_graph/service.py`
- Modify: `platform-next/command_graph/router.py`

### Task 2.1: service.py 完整加载参数 + 两种关系边

- [ ] **Step 1:** `_load` 里，扫描到的 `command_parameters.jsonl` / `command_has_parameter.jsonl` / `parameter_depends_on.jsonl` 完整加载（按 nf/version 分桶）：`self._params[(nf,version)] = [records]`、`self._has_param[(nf,version)] = [edges]`、`self._depends[(nf,version)] = [edges]`（此前只统计 count，现在存全量）
- [ ] **Step 2:** 写 `get_command_parameters(nf, command_name, version) -> list[dict]`：按 `command_id = f"{nf}@{version}:{command_name}"` 严格匹配，返回参数列表
- [ ] **Step 3:** 写 `get_command_graph(nf, command_name, version) -> dict`：组装 `{nodes, edges}`
  - nodes：1 个命令节点（group=command, label=command_name）+ N 个参数节点（group=parameter, label=parameter_name, title=中文名+类型+必选）
  - edges：has_parameter（command→param, type=has_parameter）+ depends_on（param→param, type=depends_on, **label=condition_value** 如 `=IPV4`, title=`{condition_ref} {condition_logic} {condition_value}`）
  - depends_on 引用集合外参数：补 group=parameter_external 节点
- [ ] **Step 4:** 单测（新建 `platform-next/tests/test_command_graph_service.py` 或就地）：小 fixture 验 get_command_parameters 匹配、get_command_graph 组装（条件 label、external 补节点）。Run: `pytest -q`，PASS

### Task 2.2: router.py 两个新端点

- [ ] **Step 3:** 新增
  - `GET /command-parameters`（nf, command_name, version）→ `{"parameters": svc.get_command_parameters(...)}`
  - `GET /command-graph`（nf, command_name, version）→ `svc.get_command_graph(...)`
- [ ] **Step 4:** 启动后端冒烟：`curl /command-parameters?nf=UDG&command_name=SET AUTOLOGPOLICY&version=20.15.2` 有参数；`curl /command-graph?...` 返回 nodes/edges 含 depends_on 条件 label。验证完 kill 进程释放 8000

---

## Chunk 3: 前端（platform-next/frontend/src/command_graph/）

**Files:**
- Modify: `platform-next/frontend/src/api.ts`
- Modify: `platform-next/frontend/src/command_graph/CommandDetail.vue`
- Create: `platform-next/frontend/src/command_graph/CommandParameters.vue`
- Create: `platform-next/frontend/src/command_graph/CommandGraph.vue`
- Reference: `platform-next/frontend/src/feature_graph/FeatureDetail.vue`（vis-network 范式，~line 469）

### Task 3.1: api.ts 新增两个 URL 构造器
- [ ] `commandParameters(nf, commandName, version)` 和 `commandGraph(nf, commandName, version)`，参数键用 nf

### Task 3.2: CommandParameters.vue（Tab2 新建）
- [ ] `el-table` 精选 7 列（参数标识/中文名/类型/必选/默认值/取值范围/说明摘要）+ `type="expand"` 行展开
- [ ] props: `nf, commandName, version`；激活时（onMounted/被父触发）调 `/command-parameters`
- [ ] 行展开用"非空即展示"分区渲染 28 字段（复用 isNonEmpty/renderValue 思路，参数自己的 LABEL_MAP）
- [ ] 空状态 `该命令无参数`

### Task 3.3: CommandGraph.vue（Tab3 新建）
- [ ] 容器 div ref + `await import('vis-network/standalone')`，参考 FeatureDetail.vue
- [ ] props: `nf, commandName, version`；激活时调 `/command-graph`，`new DataSet(nodes/edges)` → `new Network`
- [ ] 节点按 group 着色（command/parameter/external），depends_on 边显示 label；静态 + 拖拽缩放（`interaction:{dragNodes:true, zoomView:true}`）；卸载时 `network.destroy()`
- [ ] 空状态 `该命令无参数，无可绘制关系`

### Task 3.4: CommandDetail.vue 改 tab 壳 + 懒加载
- [ ] el-tabs 加两个 tab-pane：`参数`（CommandParameters）、`图谱`（CommandGraph）
- [ ] `watch(leftTab)` + 已加载标记：切 Tab2 才挂载/请求 CommandParameters，切 Tab3 才 CommandGraph（用 `v-if` 按已激活控制挂载即可懒加载）；Tab1 现有逻辑不动
- [ ] 把 nf/commandName/version 作为 props 传给两个子组件

### Task 3.5: 前端构建
- [ ] `cd platform-next/frontend && npm run build`（vue-tsc）通过

---

## Chunk 4: 端到端验证

- [ ] 启后端，用 `SET AUTOLOGPOLICY`（有参数 + 有 depends_on 条件依赖）验：Tab1 不变、Tab2 参数表+行展开、Tab3 图谱（命令+参数+条件依赖边，拖拽缩放）
- [ ] 用一个无参数命令（如 `ADD URR`）验 Tab2/Tab3 空状态
- [ ] UNC 命令（无参数文件）验空状态不报错
- [ ] kill 进程释放端口
