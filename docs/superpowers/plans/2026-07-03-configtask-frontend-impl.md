# ConfigTask 前端展示 Implementation Plan

> **For agentic workers:** 用 superpowers:executing-plans 实施。Steps 用 checkbox 跟踪。
> 设计依据:对话已确认(数据源 `ConfigTask/assert/`、IA 对齐 command_graph、纯展示只读、ref 跨图谱跳转)。
> 参考样板:`platform-next/command_graph/`(后端 service+router)+ `frontend/src/command_graph/*.vue`(前端页面)。

**Goal:** 在 platform-next 加一个"配置任务"图谱域:后端 FastAPI service 直读 `ConfigTask/assert/` YAML,前端 4 页(导航→列表→详情),TaskDetail 展现 task 完整结构(字段+参数绑定+task_relations+owned DP 含 impacts+owned rule+ref 跳转)。

**Architecture:** 后端 `task_graph/` 3 文件(已起草,需修 relations bug + 补 TDD),启动扫 `assert/{nf}/{version}/{tasks,task_rules,decision_points}/*.yaml` 建内存索引(task/rules-by-owner/dps-by-owner/orchestrated-by)。前端 `src/task_graph/` 4 Vue 页,复用 shared/ + Element Plus + CSS 变量,IA 对齐 command_graph。

**Tech Stack:** Python 3 + FastAPI + pyyaml(后端);Vue 3 + vue-router + Element Plus + TypeScript(前端)。

**关键设计点(bug 修复)**:feature 的 `task_relations` 是**子节点间的边**(如 1-00001→1-00002),不是 feature→子。因此 get_task 必须返回:**(a) 自身 yaml 的 task_relations 原始边**(=该 task 的"编排结构",从中可派生它编排的子任务集)+ **(b) parents**(全局扫:谁的 task_relations 引用了我)。当前 service 的 `_relations_by_task` 只做了全局 from/to,对 feature 自身返回空——错。

---

## File Structure

| 文件 | 状态 | 职责 |
|---|---|---|
| `platform-next/task_graph/service.py` | 起草,需修 | ConfigTaskService:扫 assert/、stats/list/get_task/task-tree;修 relations 逻辑 |
| `platform-next/task_graph/router.py` | 已完成 | `/api/v1/task-graph` 路由(stats/tasks/task/task-tree) |
| `platform-next/task_graph/__init__.py` | 已完成 | 导出 router |
| `platform-next/tests/test_task_graph_service.py` | **新建** | service TDD 测试 |
| `platform-next/config.yaml` | 已完成 | `task_graph.assets_root: ../ConfigTask/assert` |
| `platform-next/main.py` | 已完成 | 注册 task_router |
| `platform-next/frontend/src/api.ts` | 改 | 加 `taskGraphApi` |
| `platform-next/frontend/src/router.ts` | 改 | 加 `/task-graph` 路由 |
| `platform-next/frontend/src/shared/TopBar.vue` | 改 | 加"配置任务"顶部导航 |
| `platform-next/frontend/src/task_graph/TaskIndex.vue` | 新建 | shell(breadcrumb + router-view),照 CommandIndex |
| `platform-next/frontend/src/task_graph/TaskOverview.vue` | 新建 | 落地:hero + nf/version 卡片,照 CommandOverview |
| `platform-next/frontend/src/task_graph/TaskList.vue` | 新建 | task 队列(layer 筛选 + 搜索 + el-table + 分页),照 CommandList |
| `platform-next/frontend/src/task_graph/TaskDetail.vue` | 新建 | 完整结构单栏分节 |

---

## Chunk 1: 后端 service TDD + relations bug 修复

### Task 1: service 测试 + 修复(TDD)

**Files:**
- Test: `platform-next/tests/test_task_graph_service.py`(Create)
- Modify: `platform-next/task_graph/service.py`(修 get_task + 加 `_orchestrated_by` 索引)

- [ ] **Step 1: 写失败测试**

```python
# platform-next/tests/test_task_graph_service.py
"""ConfigTaskService 字段派生 + relations/parents 逻辑测试。"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from shared.config import load_config
from task_graph.service import get_service, _short, _parse_ref

def setup_module(module):
    load_config()

def test_short_and_parse_ref():
    assert _short("UDG@20.15.2@Task@0-00001") == "0-00001"
    assert _short("") == ""
    assert _parse_ref("UDG@20.15.2@MMLCommand@ADD URR") == {"type": "MMLCommand", "value": "ADD URR"}
    assert _parse_ref("UDG@20.15.2@Feature@GWFD-020301") == {"type": "Feature", "value": "GWFD-020301"}
    assert _parse_ref("") == {}

def test_stats_counts():
    svc = get_service()
    st = svc.get_stats()
    assert st["total_tasks"] == 201          # 187 atom(含12缺 layer)+ 4 compound + 10 feature
    assert st["total_rules"] == 205
    assert st["total_dps"] == 55
    assert any(v["nf"] == "UDG" and v["version"] == "20.15.2" and v["task_count"] == 201
               for v in st["ne_versions"])

def test_list_tasks_layer_filter_and_slim():
    svc = get_service()
    r = svc.list_tasks(nf="UDG", version="20.15.2", layer="feature")
    assert r["total"] == 10
    assert all(it["task_layer"] == "feature" for it in r["items"])
    it = r["items"][0]
    assert it["ref_type"] == "Feature"                     # feature.ref→Feature
    assert "n_dps" in it and "n_rules" in it and "n_relations" in it

def test_get_task_returns_own_relations_and_children():
    """key 修复:feature 的 task_relations 在子节点间,get_task 返回自身 yaml 的原始边。"""
    svc = get_service()
    t = svc.get_task("UDG", "20.15.2", "2-00002")
    assert t is not None
    assert len(t["task_relations"]) == 6                   # 2-00002 own yaml 6 条边
    # 每条边补全 from/to 的 short+name+layer
    r0 = t["task_relations"][0]
    for k in ("from_short", "to_short", "relation_type"):
        assert k in r0
    children = {r["from_short"] for r in t["task_relations"]} | \
               {r["to_short"] for r in t["task_relations"]}
    children.discard("2-00002")
    assert "1-00001" in children and "0-00016" in children  # 编排 backbone + 在线 atom

def test_get_task_parents():
    """parents = 全局扫,谁的 task_relations 引用了我(在 assert/ 范围内)。"""
    svc = get_service()
    # atom 0-00016 被 2-00002 的 task_relations 引用 → 2-00002 是它 parent
    t = svc.get_task("UDG", "20.15.2", "0-00016")
    assert t is not None
    assert t["task_relations"] == []                       # atom 不编排子
    parent_shorts = [p["short"] for p in t["parents"]]
    assert "2-00002" in parent_shorts

def test_get_task_dp_with_impacts():
    svc = get_service()
    t = svc.get_task("UDG", "20.15.2", "2-00002")
    dps = t["decision_points"]
    assert any(d["decision_id"].endswith("0-00154") for d in dps)
    dp = next(d for d in dps if d["decision_id"].endswith("0-00154"))
    # DP 0-00154 的 options[].impacts 含 target_type=task(在线 SET atom 门控)
    impacts = [imp for opt in dp["options"] for imp in opt.get("impacts", [])]
    assert any(imp.get("target_type") == "task" for imp in impacts)

def test_get_task_ref_cross_link():
    """ref_parsed 给前端跳转用:atom→MMLCommand、feature→Feature。"""
    svc = get_service()
    feat = svc.get_task("UDG", "20.15.2", "2-00001")
    assert feat["ref_parsed"] == {"type": "Feature", "value": "GWFD-020301"}
    atom = svc.get_task("UDG", "20.15.2", "0-00001")
    assert atom["ref_parsed"]["type"] == "MMLCommand"
    assert atom["ref_parsed"]["value"] == "ADD URR"

def test_task_tree():
    svc = get_service()
    tr = svc.get_task_tree("0-00016")
    assert tr["center"] == "0-00016"
    assert any(n["id"] == "2-00002" for n in tr["nodes"])   # 1 跳到 2-00002
```

- [ ] **Step 2: 跑测试确认 FAIL**

Run: `cd platform-next && python -m pytest tests/test_task_graph_service.py -v`
Expected: FAIL(`get_task` 返回的 `task_relations`/`parents` 字段缺失或语义错——当前是 `_resolve_relations` 返回空)

- [ ] **Step 3: 修 service.py**

在 `_load` 末尾构建 `_orchestrated_by` 索引(替换/补充原 `_relations_by_task`):

```python
        # 谁编排了我:扫每个 task 自己的 task_relations,引用到的 short → 该 task 是其 parent
        self._orchestrated_by: dict[str, set[str]] = {}
        for t in self._tasks:
            me = t["_short"]
            for r in (t.get("task_relations") or []):
                for k in ("from_task_ref", "to_task_ref"):
                    s = _short(r.get(k, ""))
                    if s and s != me:
                        self._orchestrated_by.setdefault(s, set()).add(me)
```

重写 `get_task` 的 relations 部分——返回**自身 yaml 原始边**(补全 name/layer)+ **parents**:

```python
    def _own_relations_resolved(self, t: dict) -> list[dict]:
        out = []
        for r in (t.get("task_relations") or []):
            fs, ts = _short(r.get("from_task_ref", "")), _short(r.get("to_task_ref", ""))
            ft, tt = self._by_short.get(fs, {}), self._by_short.get(ts, {})
            out.append({
                "from_short": fs, "to_short": ts,
                "from_logical_name": ft.get("task_logical_name", ""),
                "from_layer": ft.get("task_layer", ""),
                "to_logical_name": tt.get("task_logical_name", ""),
                "to_layer": tt.get("task_layer", ""),
                "relation_type": r.get("relation_type", ""),
                "condition_ref": _short(r.get("condition_ref", "")),
                "propagated_context": r.get("propagated_context") or [],
            })
        return out

    def _parents(self, short: str) -> list[dict]:
        out = []
        for p in sorted(self._orchestrated_by.get(short, set())):
            t = self._by_short.get(p, {})
            out.append({"short": p, "logical_name": t.get("task_logical_name", ""),
                        "layer": t.get("task_layer", "")})
        return out
```

`get_task` 返回里把 `"relations": ...` 改为(并**删除旧 `relations` 键**,避免前端误用):
```python
            "task_relations": self._own_relations_resolved(t),
            "parents": self._parents(short),
```
`get_task_tree` **不动**——沿用现有 `_relations_by_task`(双向索引已能覆盖 atom↔feature 等全部边,tree 测试可直接 PASS,无需改)。

- [ ] **Step 4: 跑测试确认 PASS**

Run: `cd platform-next && python -m pytest tests/test_task_graph_service.py -v`
Expected: 8 passed

- [ ] **Step 5: Commit**

```bash
git add platform-next/task_graph/service.py platform-next/tests/test_task_graph_service.py
git commit -m "feat(task-graph): ConfigTaskService + relations/parents 逻辑(TDD)"
```

### Task 2: 后端 smoke(FastAPI TestClient)

- [ ] 写 `tests/test_task_graph_router.py`(独立文件):用 `fastapi.testclient.TestClient` 验 `/stats` `/tasks?layer=feature` `/task?nf=UDG&version=20.15.2&task_id=2-00002` `/task-tree?task_id=0-00016` 返回 200 + 关键字段
- [ ] 跑通;若 platform-next 无 TestClient 习惯,直接 `python main.py` 起服务 + curl 验证

---

## Chunk 2: 前端(对齐 command_graph)

> 前端 Vue 组件用**视觉 smoke**(dev server 点阅)替代组件单元 TDD(与 command_graph 一致;后端逻辑已 TDD 兜底)。

### Task 3: api.ts + router.ts + TopBar 集成

**Files:** Modify `frontend/src/api.ts`、`frontend/src/router.ts`、`frontend/src/shared/TopBar.vue`

- [ ] **api.ts** 加(照 commandGraphApi 风格):
```typescript
export const taskGraphApi = {
  stats: `${BASE}/task-graph/stats`,
  tasks: `${BASE}/task-graph/tasks`,
  task: (nf: string, version: string, taskId: string) => {
    const p = new URLSearchParams({ nf, version, task_id: taskId })
    return `${BASE}/task-graph/task?${p}`
  },
  taskTree: (taskId: string) => `${BASE}/task-graph/task-tree?task_id=${encodeURIComponent(taskId)}`,
}
```
- [ ] **router.ts** 加路由(照 command-graph):
```typescript
{
  path: '/task-graph',
  component: () => import('./task_graph/TaskIndex.vue'),
  children: [
    { path: '', name: 'task-overview', component: () => import('./task_graph/TaskOverview.vue') },
    { path: ':nf/:version', name: 'task-list', component: () => import('./task_graph/TaskList.vue') },
  ],
},
{
  path: '/task-graph/:nf/:version/:taskId',
  name: 'task-detail',
  component: () => import('./task_graph/TaskDetail.vue'),
},
```
- [ ] **TopBar.vue** 在 nav 加(置于命令图谱后):
```html
<router-link to="/task-graph">配置任务</router-link>
```

### Task 4: TaskIndex.vue + TaskOverview.vue

- [ ] **TaskIndex.vue**:照 `command_graph/CommandIndex.vue`(breadcrumb `统计 > {nf}@{version}` + `<router-view />`)
- [ ] **TaskOverview.vue**:照 `CommandOverview.vue`——hero 卡(配置任务 = 动态编排层;5 类对象 Task/TaskRule/DecisionPoint/TaskParameterBinding/TaskRelation)+ 关系示意(generalized→feature→compound→atom + DP impacts)+ 网元版本卡片网格(点 → task-list)。数据 `fetchJson(taskGraphApi.stats)`,字段:`total_tasks / total_rules / total_dps / ne_versions[].task_count`

### Task 5: TaskList.vue

- [ ] 照 `CommandList.vue`:filter-bar 含**层级筛选**(el-select:全部/atom/compound/feature/generalized)+ 搜索(task_id/logical_name/intent)+ `{{ total }} 条`;el-table 列:task_id / logical_name / layer(el-tag)/ category / status(el-tag)/ ref(ref_type:ref_value)/ DP·rule·rel 计数;row-click → `task-detail`;el-pagination
- [ ] 数据 `fetchJson(taskGraphApi.tasks + '?nf=&version=&layer=&search=&page=&size=')`,读 `items` / `total`

### Task 6: TaskDetail.vue(完整结构,核心)

- [ ] 路由参数 `nf/version/taskId` → `fetchJson(taskGraphApi.task(nf,version,taskId))`
- [ ] 布局(单栏分节,Element Plus 卡片):
  - **Hero**:`{short}` + logical_name + layer/category/status tags + nf@version
  - **ref 跨图谱跳转**:`ref_parsed.type==MMLCommand` → `<router-link :to="/command-graph/{nf}/{version}/{value}">`;`==Feature` → `/feature-graph/{nf}/{version}/feature/{value}`;无 ref(generalized/compound)则不显示
  - **基础字段**:task_intent / task_category / confidence / notes
  - **参数绑定**(atom 才有):el-table(parameter_ref/binding_type/variable_source/requiredness/value/decision_ref)
  - **编排结构(task_relations)**:列出自身 yaml 边(from→to / relation_type / condition_ref),from/to 可点(跳 `/task-graph/{nf}/{version}/{short}`);附 **parents** 列表(谁编排本 task,可点→ `/task-graph/{nf}/{version}/{parent.short}`)
  - **DecisionPoints(本 task 挂)**:每个 DP 卡片——decision_name/type + options 表(option_id/option_name)+ 每选项 **impacts** 表(target_type/target_ref/effect_type/effect_detail)。"影响范围"= impacts 平铺
  - **Rules(本 task 挂)**:el-table(rule_id/rule_type/severity/constraint.expression)
  - **证据**:source_evidence_ids 列表(纯文本;md 在线查看后续加)
- [ ] DP/Rule 嵌在 task 详情内(不作一级导航,符合用户决策)

### Task 7: 前端 smoke

- [ ] `cd platform-next/frontend && npm run dev`(或 build)+ 后端 `python main.py`
- [ ] 点阅:首页 → 配置任务(顶部导航)→ overview(UDG@20.15.2 卡片)→ task-list(层级筛 feature=10 条)→ 任一 feature(如 2-00002)详情:看 6 条 task_relations + DP 0-00154 的 impacts + rule 0-00011 + ref 跳特性图谱生效
- [ ] 点 atom(如 0-00001)详情:参数绑定表 + ref 跳命令图谱 ADD URR 生效 + parents 含 2-00001 等

---

## 验收
- 后端 8 测试 PASS;`/stats` `/tasks` `/task` `/task-tree` 200
- 前端三页可点;TaskDetail 完整结构呈现(字段+参数绑定+task_relations+DP+impacts+rule+ref 跳转)
- 顶部"配置任务"导航出现;层级筛选生效(feature=10 / atom=175 / compound=4)
- atom 冻结:本任务只读 assert/,不改 ConfigTask 任何 yaml
