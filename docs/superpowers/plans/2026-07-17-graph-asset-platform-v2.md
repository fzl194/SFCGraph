# 图谱资产管理平台 v2 前端重构 Implementation Plan

> **For agentic workers:** REQUIRED: Use superpowers:subagent-driven-development (if subagents available) or superpowers:executing-plans to implement this plan. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 把前端重构为三菜单 IA（图谱浏览[层Tab导航+三栏含右栏图谱]/统计[卡片]/上传[异步]），导入异步化不阻塞，左栏缓存 + 跨栏跳转自动同步。

**Architecture:** 后端加异步导入任务（BackgroundTasks + 内存 job 表）+ /stats 扩充 per层×网元×版本；前端层 Tab 导航（复用 /objects 过滤）+ 导航状态 composable（缓存 + syncTo）+ 统计卡 + 异步上传轮询；删 /browse、AssetTree、独立 GraphView、/overview。

**Tech Stack:** 后端 Python FastAPI + BackgroundTasks；前端 Vue3+TS + Element Plus(el-table-v2 虚拟表) + vis-network + splitpanes。

**Spec：** `docs/superpowers/specs/2026-07-17-graph-asset-platform-v2-frontend-design.md`（权威）。v1 spec：`docs/superpowers/specs/2026-07-16-graph-asset-platform-design.md`。

---

## 全局约定

1. **工作目录**：`D:\mywork\KnowledgeBase\SFCGraph`（master，直接提交，不开分支）。
2. **⚠️ GIT 陷阱**：`三层图谱构建规范/scripts/product_doc_md_exporter_optimized.py` 长期 git 暂存态(A)。提交**只能** `git add <平台具体文件>` 然后 `git commit -m "..." -- graph-asset-platform/`（或 `-- docs/superpowers/`）。**绝不** `git add -A`/`git add .`/`git commit -am`。每次 `git show --stat HEAD` 自检只含目标路径。
3. **TDD**：后端红→绿→commit；前端以 `npm run build`（vue-tsc 过）+ 联调为准。
4. **不耦合业务名**（用 demo/中立名）。
5. **cwd 提示**：bash 的 cwd 可能停在 `graph-asset-platform/` 或子目录；用绝对路径或 `git -C /d/mywork/KnowledgeBase/SFCGraph`。

---

## File Structure（v2 改动锁定）

**后端：**
- 改 `app/routers/assets.py`：`POST /import` 异步化(202+job)、新增 `GET /import/jobs` & `/import/jobs/{id}`、`/stats` 扩充、**删 `/browse` 与 `/overview`**。
- 新增 `app/jobs.py`：内存 ImportJob 注册表（create/get/list/update + 线程锁）。
- 改 `app/service.py`：加 `import_lock`（导入+重建原子化，避免并发读不一致）。
- 改 `tests/test_api_assets.py`：加异步导入/统计扩充测试；删 browse/overview 测试。

**前端：**
- 新增 `src/composables/useNav.ts`：导航状态缓存（每层选择器/搜索/列表分页缓存）+ `syncTo(id)` 自动同步。
- 改 `src/api.ts`：加 `importJobs()`/`importJob(id)`；`stats()` 类型扩充；删 `browse`/`overview`。
- 新增 `src/views/BrowserView.vue`（图谱浏览，三栏，替代 AssetsView）。
- 新增 `src/components/LayerNav.vue`（B 布局：层 Tab + 选择器 + el-table-v2 虚拟列表）——替代 AssetTree。
- 新增 `src/components/NeighborPane.vue`（右栏：单跳图谱 + 边清单）——由 GraphCanvas+EdgeList 组合。
- 新增 `src/views/StatsView.vue` + `src/components/StatCard.vue`（统计卡）。
- 改 `src/views/UploadView.vue`：异步状态（非阻塞轮询）。
- 改 `src/router.ts` + `src/components/AppHeader.vue`：3 路由/Tab（图谱浏览/统计/上传），删 /graph。
- **删** `src/views/AssetsView.vue`、`src/views/GraphView.vue`、`src/components/AssetTree.vue`（被取代）；保留 `GraphCanvas.vue`/`ObjectDetail.vue`/`EdgeList.vue`（NeighborPane 复用）。

---

## Chunk 1: 后端 —— 异步导入 + 统计扩充 + 清理

### Task 1.1: ImportJob 注册表（app/jobs.py）

**Files:** Create `graph-asset-platform/backend/app/jobs.py`; Test `tests/test_jobs.py`.

- [ ] **Step 1: 写测试** `tests/test_jobs.py`：
```python
from app.jobs import create_job, get_job, list_jobs, update_job
def test_job_lifecycle():
    j = create_job()
    assert j.status == "processing"
    assert get_job(j.job_id).status == "processing"
    update_job(j.job_id, status="done", added=5, updated=1)
    j2 = get_job(j.job_id)
    assert j2.status == "done" and j2.added == 5
    assert any(x.job_id == j.job_id for x in list_jobs())
```
- [ ] **Step 2: 跑红** `python -m pytest tests/test_jobs.py -q` → FAIL（无模块）。
- [ ] **Step 3: 实现** `app/jobs.py`：
```python
import threading, uuid, time
from dataclasses import dataclass, field, asdict

@dataclass
class ImportJob:
    job_id: str
    status: str = "processing"      # processing | done | failed
    added: int = 0
    updated: int = 0
    skipped: int = 0
    warnings: list = field(default_factory=list)
    error: str = ""
    started_at: float = field(default_factory=time.time)
    finished_at: float = 0.0

    def summary(self) -> dict:
        d = asdict(self)
        return d

_registry: dict[str, ImportJob] = {}
_lock = threading.Lock()

def create_job() -> ImportJob:
    j = ImportJob(job_id=uuid.uuid4().hex[:12])
    with _lock:
        _registry[j.job_id] = j
    return j

def get_job(jid: str):
    with _lock:
        return _registry.get(jid)

def list_jobs() -> list[ImportJob]:
    with _lock:
        # 按 started_at 倒序，最多 100
        return sorted(_registry.values(), key=lambda j: j.started_at, reverse=True)[:100]

def update_job(jid: str, **kw) -> None:
    with _lock:
        j = _registry.get(jid)
        if not j:
            return
        for k, v in kw.items():
            setattr(j, k, v)
        if kw.get("status") in ("done", "failed"):
            j.finished_at = time.time()
```
- [ ] **Step 4: 跑绿** → PASS。
- [ ] **Step 5: Commit** `-- graph-asset-platform/`。

### Task 1.2: POST /import 异步化 + job 查询端点

**Files:** Modify `app/routers/assets.py`, `app/service.py`; Test `tests/test_api_assets.py`.

- [ ] **Step 1: service.py 加导入锁**（导入+重建原子化）：
```python
import threading
class Service:
    def __init__(self):
        self.store = Store(ASSETS_DIR)
        self.registry = Registry.load_default()
        self.index = Index.build(self.store, self.registry)
        self.import_lock = threading.Lock()
_service = None
def get_service() -> "Service": ...  # 同前
```
- [ ] **Step 2: assets.py 改 /import 为异步 + 新增 job 端点**：
```python
from fastapi import BackgroundTasks, HTTPException
from ..jobs import create_job, get_job, list_jobs
from ..service import get_service

def _process_import(job_id: str, zip_bytes: bytes):
    """后台：解压→归类→合并→重建→更新 job。单例 service 跨线程共享，加锁。"""
    from ..service import get_service
    svc = get_service()
    try:
        with svc.import_lock:
            res = import_bundle(zip_bytes, svc.store, svc.registry)
            svc.rebuild()
        update_job(job_id, status="done", added=res.added, updated=res.updated,
                   skipped=res.skipped, warnings=res.warnings)
    except Exception as ex:  # 任意失败不卡死 job
        update_job(job_id, status="failed", error=str(ex))

@router.post("/import", status_code=202)
async def do_import(file: UploadFile = File(...), bg: BackgroundTasks = BackgroundTasks()):
    data = await file.read()
    job = create_job()
    # 记录到 _imports.log（job_id 便于追溯）
    _append_import_log(job.job_id, "processing")
    bg.add_task(_process_import, job.job_id, data)   # 响应立即返回，后台处理
    return {"job_id": job.job_id, "status": "processing"}

@router.get("/import/jobs")
def jobs_list():
    return [j.summary() for j in list_jobs()]

@router.get("/import/jobs/{job_id}")
def job_detail(job_id: str):
    j = get_job(job_id)
    if not j:
        raise HTTPException(404, "job 不存在")
    return j.summary()
```
> `_append_import_log`：把原 `_imports.log` 写入逻辑抽成函数（job_id, status 一行 JSON）。`update_job` 完成后可再追加一行 done 记录（或只在 job 表查）。`import_bundle` / `svc.rebuild()` 保持同步函数（在后台线程内调用）。
- [ ] **Step 3: 写测试**（异步导入）：上传后立即得 202 + job_id（status=processing）；轮询/直接跑后台函数后 job 变 done。
```python
def test_import_async_returns_job(tmp_data_dir, monkeypatch):
    _setup_service(tmp_data_dir, monkeypatch)
    with TestClient(app) as c:
        r = c.post("/api/v1/import", files={"file": _zip_upload({"a.md": CMD})})
        assert r.status_code == 202
        body = r.json()
        assert body["status"] == "processing" and body["job_id"]
        # TestClient 会等 BackgroundTasks 执行完再返回（同步语义），故此时应已 done
        j = c.get(f"/api/v1/import/jobs/{body['job_id']}").json()
        assert j["status"] == "done" and j["added"] == 1
```
> 注：FastAPI TestClient（httpx）默认等 BackgroundTasks 完成再返回响应，故 202 响应里 job 已 done。生产是异步。
- [ ] **Step 4: 跑绿**（必要时微调）。
- [ ] **Step 5: Commit**。

### Task 1.3: /stats 扩充 per层×网元×版本

**Files:** Modify `assets.py` `/stats`; Test.

- [ ] **Step 1: 改 /stats**：
```python
from collections import defaultdict
@router.get("/stats")
def stats():
    svc = get_service(); idx = svc.index
    per_layer = defaultdict(int)
    per_layer_per_nf = defaultdict(lambda: defaultdict(int))
    per_layer_per_nf_per_version = defaultdict(lambda: defaultdict(lambda: defaultdict(int)))
    per_domain = defaultdict(int)
    for obj in idx.nodes.values():
        per_layer[obj.layer] += 1
        if obj.nf:
            per_layer_per_nf[obj.layer][obj.nf] += 1
            if obj.version:
                per_layer_per_nf_per_version[obj.layer][obj.nf][obj.version] += 1
        if obj.domain:
            per_domain[obj.domain] += 1
    def dd(d): return {k: (dd(v) if isinstance(v, dict) else v) for k, v in d.items()}
    return {
        "object_counts_by_type": _counts(svc), "edge_count": _edge_count(svc),
        "nfs": sorted(idx.nfs()), "versions_per_nf": idx.versions_per_nf(),
        "per_layer": dict(per_layer),
        "per_layer_per_nf": dd(dict(per_layer_per_nf)),
        "per_layer_per_nf_per_version": dd({k: dict(v) for k, v in per_layer_per_nf_per_version.items()}),
        "per_domain": dict(per_domain),
    }
```
- [ ] **Step 2: 测试**（导入含命令+业务对象 → /stats 返回 per_layer/per_layer_per_nf/per_domain 正确）。
- [ ] **Step 3: 跑绿**；全量 `pytest -q` 绿。
- [ ] **Step 4: Commit**。

### Task 1.4: 清理 /browse、/overview + 相关测试

**Files:** Modify `assets.py`（删两个端点）、`store.py`（删 `list_dir`）、`test_api_assets.py`（删 browse/overview 测试）。

- [ ] **Step 1:** 删 `assets.py` 的 `@router.get("/browse")` 与 `@router.get("/overview")`（及 `_node_label`/`_dedup_edges` 仅 overview 用的辅助）。
- [ ] **Step 2:** 删 `store.py` 的 `list_dir`（仅 /browse 用）。
- [ ] **Step 3:** 删 `test_api_assets.py` 里 `test_browse_*` 与 `test_overview_*`。
- [ ] **Step 4:** 全量 `pytest -q` 绿。
- [ ] **Step 5: Commit**。

**Chunk 1 完成**：后端异步导入 + 统计扩充 + 清理。派发 plan-document-reviewer 审 Chunk 1。

---

## Chunk 2: 前端基础 —— api.ts + 导航 composable + 路由/顶栏

### Task 2.1: api.ts 适配（异步 job + stats 扩充 + 删 browse/overview）

**Files:** Modify `src/api.ts`.
- [ ] 加 `importJobs()`、`importJob(id)`；`Stats` 类型加 `per_layer/per_layer_per_nf/per_layer_per_nf_per_version/per_domain`；删 `browse`、`overview`。
- [ ] `npm run build` 绿。
- [ ] Commit。

### Task 2.2: 导航 composable（useNav.ts）—— 缓存 + syncTo

**Files:** Create `src/composables/useNav.ts`.
- [ ] **实现要点**：
  - 模块级单例 reactive 状态（全局缓存）：`activeLayer`（'Command'|'Feature'|'Task'|'Business'）；各层选择器 `sel = { nf, version, type, domain, scenario, q }`；`listCache`（key=`层|nf|version|page` → {rows,total}）；`selectedId`。
  - `loadList(layer)`：按层+选择器调 `listObjects`（type=该层类型集合），分页，写 listCache。
  - `selectLayer(l)`：切层（保留各层已缓存选择器/列表，不重拉）。
  - **`syncTo(id)`**：调 `getObject(id)` 取 type/nf/version/domain/scenario → 推断层（type→layer 映射：MMLCommand/ConfigObject→Command；Feature/License→Feature；Task→Task；BusinessDomain/NetworkScenario/ConfigurationSolution→Business）→ 设 activeLayer + 选择器(nf/version 或 domain/scenario) → 刷新列表 → 设 selectedId（列表高亮 + 滚动）。
- [ ] type→layer 映射抽成常量表（与后端 registry layer 对齐）。
- [ ] Commit。

### Task 2.3: 路由 + 顶栏改三菜单

**Files:** Modify `src/router.ts`, `src/components/AppHeader.vue`.
- [ ] 路由：`/` → BrowserView（图谱浏览）；`/stats` → StatsView；`/upload` → UploadView。删 `/graph`、`/assets`。
- [ ] AppHeader 三 Tab：图谱浏览 / 统计 / 上传。
- [ ] Commit。

**Chunk 2 完成**（此时 BrowserView/StatsView 尚为占位）。审 Chunk 2。

---

## Chunk 3: 图谱浏览（三栏 + LayerNav + NeighborPane + 自动同步）

### Task 3.1: LayerNav.vue（B 布局）

**Files:** Create `src/components/LayerNav.vue`（替代 AssetTree）.
- [ ] **结构**：
  - 顶部 4 层 Tab（el-tabs / 按钮组）。
  - 当前层选择器：Command/Feature/Task → `网元 el-select + 版本 el-select + 类型 el-select + 搜索 el-input`；Business → `域 el-select + 场景 el-select`（无版本）。
  - 列表：**el-table-v2 虚拟表**（列：id[等宽] + type badge），数据来自 `useNav.loadList`（分页/虚拟），只渲染可见行。
  - 选择器/层变化 → useNav 更新 + 重新 loadList（命中缓存则不请求）。
  - 点行 → `useNav.selectedId = id`（联动中栏+右栏）。
  - 高亮：`selectedId` 对应行高亮 + scrollIntoView。
- [ ] 网元/版本/域/场景 选项来自 stats（nfs/versions_per_nf）或首次列表推导。
- [ ] Commit。

### Task 3.2: NeighborPane.vue（右栏：单跳图谱 + 边清单）

**Files:** Create `src/components/NeighborPane.vue`.
- [ ] props：`objectId`。调 `neighbors(id, version, 1)` → vis-network（复用 GraphCanvas 渲染逻辑）渲染中心+单跳邻居；下方边清单（复用 EdgeList）。点邻居 → `useNav.syncTo(neighborId)`（触发左栏同步 + 中栏切换）。
- [ ] 空态：未选对象时提示"从左栏选一个对象"。
- [ ] Commit。

### Task 3.3: BrowserView.vue（三栏组合 + splitpanes + 联动）

**Files:** Create `src/views/BrowserView.vue`（替代 AssetsView）.
- [ ] splitpanes 三栏：`<LayerNav>` | `<MdPreview :object-id="selectedId">` | `<NeighborPane :object-id="selectedId">`。
- [ ] `selectedId` 来自 useNav（响应式）。中栏 MdPreview 点 wiki 链接 → `useNav.syncTo(id)`（左栏自动同步 + 中右切换）。右栏点邻居同上。
- [ ] URL 同步 `?o={id}&version=`（可分享；挂载时若有 ?o 则 syncTo）。
- [ ] 删 `AssetsView.vue`、`GraphView.vue`、`AssetTree.vue`。
- [ ] `npm run build` 绿 + 联调（选对象→中栏md+右栏图谱；点邻居/wikilink→左栏切层+选择器+高亮）。
- [ ] Commit。

**Chunk 3 完成**。审 Chunk 3。

---

## Chunk 4: 统计卡 + 上传异步 UI

### Task 4.1: StatsView.vue + StatCard.vue

**Files:** Create `src/views/StatsView.vue`, `src/components/StatCard.vue`.
- [ ] 调 `stats()` 取 `per_layer/per_layer_per_nf/per_layer_per_nf_per_version/per_domain`。
- [ ] 4 张卡：命令层（总数 + 按网元 + 按版本[网元/版本]）、特性层（总数+按网元）、任务层（总数+按网元）、业务层（总数+按域）。前期纯数字（StatCard：标题 + 大数字 + 小字明细）。
- [ ] Commit。

### Task 4.2: UploadView.vue 异步状态（非阻塞轮询）

**Files:** Modify `src/views/UploadView.vue`.
- [ ] 上传 → `POST /import`（202 + job_id）→ 上传列表插入一条 `处理中`（不阻塞、不转圈）。
- [ ] 非阻塞轮询：对该 job 每 ~1.5s 调 `importJob(id)`，`done`→标`完成(added/updated)`并刷新 stats；`failed`→标失败。多个 job 并行轮询；用 setInterval + onUnmounted 清理。
- [ ] 拖拽区 + 列表（状态 chip）。
- [ ] 联调：上传后界面不卡、状态从处理中→完成、统计刷新。
- [ ] Commit。

**Chunk 4 完成**。审 Chunk 4。

---

## Chunk 5: 收尾验证

### Task 5.1: 全量验证 + 联调 + README 更新
- [ ] 后端 `pytest -q` 全绿。
- [ ] 前端 `npm run build` 绿（vue-tsc 过）。
- [ ] 联调（后端 :8000 + 前端 dev）：图谱浏览层Tab/选择器/列表/缓存/跳转同步；统计卡；上传异步。
- [ ] README 更新（新菜单 IA + 异步导入说明 + 启动）。
- [ ] grep 无业务名；git 自检无夹带。
- [ ] Commit。

**Chunk 5 完成** → 审 Chunk 5 → 执行交接（subagent-driven-development）。

---

## Plan Review Loop

每完成一个 Chunk 派发 plan-document-reviewer（提供 chunk + spec 路径 `docs/superpowers/specs/2026-07-17-graph-asset-platform-v2-frontend-design.md`），❌ 修复再审，✅ 进下一 chunk，超 5 轮上报。

## Execution Handoff

Plan 完成并保存到 `docs/superpowers/plans/2026-07-17-graph-asset-platform-v2.md` 后：
> "Plan complete and saved to `docs/superpowers/plans/2026-07-17-graph-asset-platform-v2.md`. Ready to execute?"

有 subagents → 用 superpowers:subagent-driven-development（每 task 一个 fresh subagent + 两阶段 review）。
