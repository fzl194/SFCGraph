# 命令图谱统一图架构 Implementation Plan

> **For agentic workers:** REQUIRED: Use superpowers:subagent-driven-development (if subagents available) or superpowers:executing-plans to implement this plan. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 命令图谱点边合并成内存图（adjacency），service `get_subgraph` 按需取子图（含跨命令 references + 对象间 refers_to），`depends_on`→`conditional_required` 改名，前端命令图谱改调 get_subgraph。

**Architecture:** service `_load_graph` 按 spec §3.1 映射表加载所有 jsonl → adjacency dict（全局，实例键含 `nf@version`）；`get_subgraph(center, hops, edge_types)` BFS → `{nodes, edges}`；前端 vis-network 按 node.type/edge.type 渲染。

**Tech Stack:** Python 3 / FastAPI / Vue3 + vis-network / jsonl

**Spec:** `docs/superpowers/specs/2026-06-26-command-graph-unified-graph-design.md` (rev3)

---

## File Structure

**修改：**
- `CommandGraph/builder/params.py` — `build_depends_on_edges` 的 edge_type 改名 + 输出文件名
- `CommandGraph/builder/steps/registry.py` — `PRODUCT_FILE` / `PROVIDES` 改名
- `CommandGraph/COMMAND_GRAPH_SCHEMA.md` §4.4.1 — 字段对齐 builder 实际产出
- `CommandGraph/tests/test_build_commandparameter.py` — 断言改名
- `platform-next/command_graph/service.py` — `_load_graph` + `get_subgraph` + `_load` object_type 改名
- `platform-next/command_graph/router.py` — `/subgraph` 端点
- `platform-next/frontend/src/api.ts` — `subgraph`
- `platform-next/frontend/src/command_graph/CommandGraph.vue` — 改调 get_subgraph + 配色

**新建：**
- `platform-next/tests/test_graph_service.py` — `_load_graph` + `get_subgraph` 单元测试

---

## Task 1: depends_on → conditional_required（builder + schema + 测试）

**Files:**
- Modify: `CommandGraph/builder/params.py`（`build_depends_on_edges` ~L198-207；`write` 调用处文件名）
- Modify: `CommandGraph/builder/steps/registry.py`（PRODUCT_FILE / PROVIDES）
- Modify: `CommandGraph/COMMAND_GRAPH_SCHEMA.md` §4.4.1
- Modify: `CommandGraph/tests/test_build_commandparameter.py`

- [ ] **Step 1: 改测试断言（RED）**
  `test_build_commandparameter.py` 里 `edge_type: "depends_on"` → `"conditional_required"`；`deps_path` 文件名 `parameter_depends_on.jsonl` → `parameter_conditional_required.jsonl`。
- [ ] **Step 2: 跑测试确认失败**
  `python -m pytest CommandGraph/tests/test_build_commandparameter.py -v` → FAIL（builder 还产 depends_on）
- [ ] **Step 3: 改 builder**
  `params.py` `build_depends_on_edges`：`"edge_type": "depends_on"` → `"conditional_required"`；`steps/parameter.py` 写出路径 `parameter_depends_on.jsonl` → `parameter_conditional_required.jsonl`。
- [ ] **Step 4: 改 registry**
  `PRODUCT_FILE`: `parameter_depends_on` → `parameter_conditional_required`；`PROVIDES["parameter"]` 同步。
- [ ] **Step 5: 改 schema §4.4.1 字段**
  `{condition_value, condition_expression, required_mode}` → `{condition_ref, condition_logic, condition_value}`（对齐 builder 实际）。
- [ ] **Step 6: 跑测试通过**
  `pytest CommandGraph/tests/test_build_commandparameter.py -v` → PASS
- [ ] **Step 7: 重跑 parameter step 产出新文件**
  `python CommandGraph/build_all.py UDG 20.15.2`（或单跑 parameter step）→ 产出 `parameter_conditional_required.jsonl`
- [ ] **Step 8: commit**
  `git add CommandGraph/ && git commit -m "refactor: depends_on→conditional_required（命令内条件依赖改名，schema§4.4.1 字段对齐）"`

---

## Task 2: service _load_graph（统一图 adjacency）

**Files:**
- Create: `platform-next/tests/test_graph_service.py`
- Modify: `platform-next/command_graph/service.py`

- [ ] **Step 1: 写测试（RED）**
  `test_graph_service.py::test_load_graph`：构造内存 service（注入小样例 nodes/edges jsonl 或用 `__new__` 跳过扫描 + 手填 `_adjacency`），断言：
  - 节点数 = mml_commands + parameters + config_objects 总数
  - 边按 §3.1 表的 from/to 字段正确进 `out`/`in`
  - 含 parameter_references（references 边）+ object_refers_to（refers_to 边）
- [ ] **Step 2: 跑确认失败**
  `pytest platform-next/tests/test_graph_service.py::test_load_graph -v` → FAIL（`_load_graph` 不存在）
- [ ] **Step 3: 实现 `_load_graph`**
  按 spec §3.1 映射表，加载 8 个 jsonl → 统一 nodes（{id,type,label,properties}）+ edges（{from,to,type,properties}）→ 建 adjacency：
  ```python
  # adjacency[node_id] = {"node": {...}, "out": [(to,type,props)...], "in": [(from,type,props)...]}
  ```
  - `_load` 的 object_type 分支：`parameter_depends_on` → `parameter_conditional_required`（配合 Task 1 改名）
  - 新增加载 `parameter_references` + `object_refers_to`
  - 保留现有 `_records/_by_id/_params/_has_param/_depends/_obj_objects/_obj_edges`（向后兼容 get_command 等）
- [ ] **Step 4: 跑测试通过** → PASS
- [ ] **Step 5: commit**
  `git add platform-next/command_graph/service.py platform-next/tests/test_graph_service.py && git commit -m "feat: service _load_graph 统一点边加载到内存 adjacency"`

---

## Task 3: service get_subgraph（BFS）

**Files:**
- Modify: `platform-next/command_graph/service.py`
- Modify: `platform-next/tests/test_graph_service.py`

- [ ] **Step 1: 写测试（RED）**
  `test_get_subgraph`：
  - center=某命令，hops=2，edge_types=[has_parameter,creates,references] → 返回命令+参数+对象+跨命令引用参数
  - edge_types 过滤：不在列表的边不返回
  - 去重：同对多条件边保留（造两条 conditional_required 同 from/to 不同 condition，断言都返回）
- [ ] **Step 2: 跑确认失败** → FAIL
- [ ] **Step 3: 实现 `get_subgraph(center, hops=2, edge_types=None)`**
  ```python
  def get_subgraph(self, center, hops=2, edge_types=None):
      # BFS：edge_types 既限遍历也限包含
      # node 去重 by id；edge 去重 by (from,to,type, json.dumps(properties,sort_keys=True))
      # 返回 {"nodes":[{id,type,label,properties}], "edges":[{from,to,type,properties}]}
  ```
  注意 properties dict 不可 hash，须 `json.dumps(..., sort_keys=True)` 序列化入 set（spec §3.3 实现注）。
- [ ] **Step 4: 跑测试通过** → PASS
- [ ] **Step 5: commit**
  `git commit -m "feat: service get_subgraph BFS 取子图（edge_types 过滤+身份去重）"`

---

## Task 4: router /subgraph 端点

**Files:**
- Modify: `platform-next/command_graph/router.py`

- [ ] **Step 1: 加端点**
  ```python
  @router.get("/subgraph")
  def get_subgraph(center: str = Query(...), hops: int = Query(2, ge=1, le=3),
                   edge_types: str | None = Query(None)):
      svc = get_service()
      types = edge_types.split(",") if edge_types else None
      return svc.get_subgraph(center, hops, types)
  ```
- [ ] **Step 2: 跑后端测试 + 手动 curl 验证**
  `pytest platform-next/tests/ -v`；起服务 `curl ".../subgraph?center=UDG@20.15.2@MMLCommand@ADD%20URR&hops=2"`
- [ ] **Step 3: commit**

---

## Task 5: 前端 api subgraph

**Files:**
- Modify: `platform-next/frontend/src/api.ts`

- [ ] **Step 1: 加 subgraph**
  ```ts
  subgraph: (center: string, hops = 2, edgeTypes?: string[]) => {
    const p = new URLSearchParams({ center, hops: String(hops) })
    if (edgeTypes?.length) p.set('edge_types', edgeTypes.join(','))
    return `${BASE}/command-graph/subgraph?${p}`  // center 已 encodeURIComponent by URLSearchParams
  },
  ```
- [ ] **Step 2: vue-tsc**
  `cd platform-next/frontend && npx vue-tsc --noEmit` → exit 0
- [ ] **Step 3: commit**

---

## Task 6: 前端 CommandGraph 改调 get_subgraph

**Files:**
- Modify: `platform-next/frontend/src/command_graph/CommandGraph.vue`

- [ ] **Step 1: 改 load() 调 get_subgraph**
  ```ts
  const url = commandGraphApi.subgraph(
    `${props.nf}@${props.version}@MMLCommand@${props.commandName}`,  // center 实例键
    2,
    ['has_parameter','creates','references','conditional_required','refers_to']
  )
  const data = await fetchJson(url)
  ```
  （返回 {nodes:[{id,type,label,properties}], edges:[{from,to,type,properties}]}）
- [ ] **Step 2: node.type 配色/形状**
  GROUP_COLORS：MMLCommand 青 box / CommandParameter 白 ellipse / ConfigObject 紫 diamond；外部命令参数（references 目标，其 command != center）→ `parameter_external` 组（虚边框弱化）。判断：edge.type=references 且 to 参数所属 command ≠ center → group=parameter_external。
- [ ] **Step 3: edge.type 配色/label**
  has_parameter 淡灰无 label；conditional_required/references 青色 + label（条件值/`=值`）；creates/modifies/sets/queries 紫 + label；refers_to 紫虚线；operates_on 灰。
- [ ] **Step 4: vue-tsc + 起服务看**
  `npx vue-tsc --noEmit` → 0；起服务进命令详情图谱 tab，看跨命令 references + 对象间 refers_to。
- [ ] **Step 5: commit**

---

## Task 7: 端到端验证

- [ ] **Step 1: 重跑 build_all**（确保 parameter_conditional_required.jsonl 产出）
  `python CommandGraph/build_all.py`
- [ ] **Step 2: 起服务，命令详情图谱验证**
  - 选 ADD URR（有跨命令引用）：图谱应含 URR 命令 + 参数 + URR ConfigObject + （references）URRGROUP 的 UPURRNAME 等引用 URR.URRNAME 的参数（parameter_external 组）
  - 选 ADD FLTBINDFLOWF：应含 FILTERNAME references FILTER.FILTERNAME
  - hops=2 可见性核对（spec §3.4）：跨命令目标参数在 2 跳内，目标命令节点不在（需 hops=3 或二次查询）
- [ ] **Step 3: 全量测试**
  `pytest CommandGraph/tests/ platform-next/tests/ -v` 全绿
- [ ] **Step 4: commit（如有调整）**

---

## 风险 / 注意

- **Task 1 改名链路**：builder → 文件名 → PRODUCT_FILE → service `_load` object_type → 前端，任一漏改导致 conditional_required 边丢失。测试覆盖。
- **Task 3 去重**：properties dict 不可直接 hash，必须 json.dumps 序列化（否则 TypeError 或错误合并多条件边）。
- **Task 6 parameter_external 判断**：要区分"本命令参数"vs"跨命令引用来的外部参数"——靠 edge.type=references + 目标参数所属 command 判断。
- **get_command_graph 保留**（spec §4.1）：不破坏，前端图谱 tab 改调 get_subgraph；旧 API 暂留向后兼容。
- **UNC 退化**（spec §6）：UNC 无参数资产，子图仅 command→object，非 bug。
