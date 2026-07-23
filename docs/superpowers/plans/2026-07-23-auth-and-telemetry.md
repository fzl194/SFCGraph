# 鉴权 + 运营打点 实现计划

> **For agentic workers:** REQUIRED: Use superpowers:subagent-driven-development (if subagents available) or superpowers:executing-plans to implement this plan. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 给 graph-asset-platform 加单一 KEY 鉴权 + SKILL 取用打点（jsonl 三维聚合，前端并入统计页）。

**Architecture:** 后端 FastAPI 中间件鉴权（`GAP_API_KEY`，未配旁路）+ 独立 `app/telemetry/` 模块（recorder 追加 jsonl / aggregator 聚合三维）+ `/domains` 改 POST 并在 `/domains`、`/md` 末尾埋点。前端 sessionStorage 存 KEY、`_req` 注入 header + 401 跳登录、统计页加「知识取用频次」section。全隔离，不动图谱 service/tests service 逻辑。

**Tech Stack:** FastAPI + pytest + httpx TestClient（后端）；Vue 3.5 + TS + vue-router + Element Plus（前端，无单测，靠 `npm run build` + 浏览器验证）。

**Spec:** `docs/superpowers/specs/2026-07-23-auth-and-telemetry-design.md`

**工作目录约定：**
- 后端命令在 `graph-asset-platform/backend/` 下跑（`pyproject.toml` 配 `pythonpath=["."]`）
- 前端命令在 `graph-asset-platform/frontend/` 下跑
- 提交按"直接在 master，不开分支"（用户全局规则）

---

## Chunk 1: 后端核心（鉴权 + 打点 + 接口改 POST）

### Task 1: config.py 扩展（读 env + 打点路径）

**Files:**
- Modify: `graph-asset-platform/backend/app/config.py`

- [ ] **Step 1: 改 config.py**

```python
import os
from pathlib import Path

# 资产库根（可被环境变量覆盖）。默认 ./platform-data/assets
DATA_DIR = Path(__file__).resolve().parents[2] / "platform-data"
ASSETS_DIR = DATA_DIR / "assets"
TESTS_DIR = DATA_DIR / "tests"  # 测试用例管理子系统（独立于 assets，隔离）
DEFAULT_REGISTRY_PATH = Path(__file__).resolve().parent / "default_registry.yaml"

# —— 鉴权（单一共享 KEY；空 → 中间件旁路，仅开发用）——
# 取值绝不 echo 到日志/响应（见 spec §6）。
API_KEY = os.environ.get("GAP_API_KEY", "")

# —— 运营打点（jsonl，对象级）——
TELEMETRY_DIR = DATA_DIR / "telemetry"
TELEMETRY_FILE = TELEMETRY_DIR / "access.jsonl"
```

- [ ] **Step 2: 验证 import 不报错**

Run（在 `backend/` 下）: `python -c "from app import config; print(bool(config.API_KEY), config.TELEMETRY_FILE)"`
Expected: 打印 `(False, ...platform-data\telemetry\access.jsonl)`（未设 env 时 API_KEY 为空）

- [ ] **Step 3: Commit**

```bash
git add graph-asset-platform/backend/app/config.py
git commit -m "feat(platform): config 读 GAP_API_KEY + 打点路径"
```

---

### Task 2: 打点 recorder（TDD）

**Files:**
- Create: `graph-asset-platform/backend/app/telemetry/__init__.py`（空文件）
- Create: `graph-asset-platform/backend/app/telemetry/recorder.py`
- Create: `graph-asset-platform/backend/tests/test_telemetry.py`

- [ ] **Step 1: 写失败测试** `tests/test_telemetry.py`

```python
"""telemetry 测试：recorder 追加 / aggregator 聚合 / 接口。"""
import json
from pathlib import Path


def _use_tmp_telemetry(tmp_path, monkeypatch):
    """把 config.TELEMETRY_FILE 指到临时目录，隔离测试。"""
    f = tmp_path / "access.jsonl"
    import app.config as cfg
    monkeypatch.setattr(cfg, "TELEMETRY_FILE", f)
    return f


def test_record_appends_jsonl_line(tmp_path, monkeypatch):
    f = _use_tmp_telemetry(tmp_path, monkeypatch)
    from app.telemetry.recorder import record
    record("/md", "UDG@Feature@F-1", "Feature")
    record("/md", "UDG@Feature@F-1", "Feature")
    lines = f.read_text(encoding="utf-8").strip().split("\n")
    assert len(lines) == 2
    rec = json.loads(lines[0])
    assert rec["endpoint"] == "/md"
    assert rec["id"] == "UDG@Feature@F-1"
    assert rec["type"] == "Feature"
    assert "ts" in rec


def test_record_makes_parent_dir(tmp_path, monkeypatch):
    f = tmp_path / "nested" / "deep" / "access.jsonl"
    import app.config as cfg
    monkeypatch.setattr(cfg, "TELEMETRY_FILE", f)
    from app.telemetry.recorder import record
    record("/domains", "BusinessDomain@demo", "BusinessDomain")
    assert f.exists()


def test_record_swallows_failure(tmp_path, monkeypatch):
    """打点失败绝不抛（观测用，不阻断业务）。"""
    import app.config as cfg
    # TELEMETRY_FILE 指到已存在目录 → open(dir, 'a') 跨平台必抛（Windows/Linux 均可复现）
    monkeypatch.setattr(cfg, "TELEMETRY_FILE", tmp_path)
    from app.telemetry.recorder import record
    record("/md", "x", "y")  # 不抛即通过
```

- [ ] **Step 2: 跑测试验证失败**

Run: `pytest tests/test_telemetry.py -v`
Expected: FAIL（`ModuleNotFoundError: app.telemetry.recorder`）

- [ ] **Step 3: 实现 `app/telemetry/recorder.py`**

```python
"""打点记录器：对象级访问追加到 jsonl。

打点是观测用、非功能性：record() 内部吞异常，绝不向上抛，绝不阻断 /md、/domains 请求。
"""
import json
import logging
import threading
from datetime import datetime, timezone
from pathlib import Path

from ..config import TELEMETRY_FILE

logger = logging.getLogger(__name__)
_lock = threading.Lock()


def record(endpoint: str, id_: str, type_: str) -> None:
    """追加一条对象级访问记录。失败吞掉 + log，不抛。"""
    try:
        line = {
            "ts": datetime.now(timezone.utc).isoformat(),
            "endpoint": endpoint,
            "id": id_,
            "type": type_,
        }
        path = Path(TELEMETRY_FILE)
        path.parent.mkdir(parents=True, exist_ok=True)
        with _lock:
            with open(path, "a", encoding="utf-8") as f:
                f.write(json.dumps(line, ensure_ascii=False) + "\n")
    except Exception as e:  # noqa: BLE001 — 观测用，绝不阻断业务
        logger.warning("telemetry record failed: %s", e)
```

- [ ] **Step 4: 跑测试验证通过**

Run: `pytest tests/test_telemetry.py -v`
Expected: 3 PASS

- [ ] **Step 5: Commit**

```bash
git add graph-asset-platform/backend/app/telemetry/__init__.py graph-asset-platform/backend/app/telemetry/recorder.py graph-asset-platform/backend/tests/test_telemetry.py
git commit -m "feat(platform): 打点 recorder（jsonl 追加，失败不阻断）"
```

---

### Task 3: 打点 aggregator（TDD）

**Files:**
- Create: `graph-asset-platform/backend/app/telemetry/aggregator.py`
- Modify: `graph-asset-platform/backend/tests/test_telemetry.py`（追加聚合测试）

- [ ] **Step 1: 追加失败测试** 到 `tests/test_telemetry.py`

```python
def _seed(f, rows):
    """直接写若干行 jsonl 作为打点种子。"""
    with open(f, "w", encoding="utf-8") as out:
        for r in rows:
            out.write(json.dumps(r, ensure_ascii=False) + "\n")


def test_aggregate_three_dimensions(tmp_path, monkeypatch):
    f = _use_tmp_telemetry(tmp_path, monkeypatch)
    _seed(f, [
        {"ts": "2026-07-23T10:00:00+00:00", "endpoint": "/md", "id": "F@1", "type": "Feature"},
        {"ts": "2026-07-23T10:01:00+00:00", "endpoint": "/md", "id": "F@1", "type": "Feature"},
        {"ts": "2026-07-23T10:02:00+00:00", "endpoint": "/md", "id": "C@2", "type": "MMLCommand"},
        {"ts": "2026-07-23T10:03:00+00:00", "endpoint": "/domains", "id": "BD@x", "type": "BusinessDomain"},
    ])
    from app.telemetry.aggregator import aggregate
    r = aggregate(days=30)
    assert r["total"] == 4
    assert r["by_type"]["Feature"] == 2
    assert r["by_type"]["MMLCommand"] == 1
    # top_ids：F@1 最热（2 次），排第一
    assert r["top_ids"][0] == {"id": "F@1", "type": "Feature", "count": 2}
    # timeline 按日
    assert r["timeline"] == [{"date": "2026-07-23", "count": 4}]


def test_aggregate_days_filter(tmp_path, monkeypatch):
    """老记录（now-40d）被 days=10 过滤；新记录（now-1d）保留。动态种子，无日期漂移 flaky。"""
    from datetime import datetime, timedelta, timezone
    now = datetime.now(timezone.utc)
    old_ts = (now - timedelta(days=40)).isoformat()
    new_ts = (now - timedelta(days=1)).isoformat()
    f = _use_tmp_telemetry(tmp_path, monkeypatch)
    _seed(f, [
        {"ts": old_ts, "endpoint": "/md", "id": "OLD", "type": "Feature"},
        {"ts": new_ts, "endpoint": "/md", "id": "NEW", "type": "Feature"},
    ])
    from app.telemetry.aggregator import aggregate
    r = aggregate(days=10)
    assert r["total"] == 1  # 只剩 NEW
    assert r["top_ids"][0]["id"] == "NEW"
```

- [ ] **Step 2: 跑测试验证失败**

Run: `pytest tests/test_telemetry.py::test_aggregate_three_dimensions -v`
Expected: FAIL（`ModuleNotFoundError: app.telemetry.aggregator`）

- [ ] **Step 3: 实现 `app/telemetry/aggregator.py`**

```python
"""打点聚合器：流式读 jsonl，聚合三维（type / top-N / 时间）。"""
import json
from collections import Counter
from datetime import datetime, timedelta, timezone
from pathlib import Path

from ..config import TELEMETRY_FILE


def aggregate(days: int = 30) -> dict:
    """聚合最近 days 天的访问记录，返回 {total, by_type, top_ids, timeline}。"""
    by_type: Counter = Counter()
    by_id: Counter = Counter()
    id_type: dict = {}
    by_date: Counter = Counter()

    cutoff = None
    if days and days > 0:
        cutoff = datetime.now(timezone.utc) - timedelta(days=days)

    path = Path(TELEMETRY_FILE)
    if path.exists():
        with open(path, "r", encoding="utf-8") as f:
            for raw in f:
                raw = raw.strip()
                if not raw:
                    continue
                try:
                    rec = json.loads(raw)
                except json.JSONDecodeError:
                    continue
                ts = _parse_ts(rec.get("ts", ""))
                if cutoff and ts and ts < cutoff:
                    continue
                type_ = rec.get("type") or "unknown"
                id_ = rec.get("id") or "unknown"
                by_type[type_] += 1
                by_id[id_] += 1
                id_type[id_] = type_
                if ts:
                    by_date[ts.strftime("%Y-%m-%d")] += 1

    top_ids = [
        {"id": i, "type": id_type.get(i, "unknown"), "count": c}
        for i, c in by_id.most_common(20)
    ]
    timeline = [{"date": d, "count": c} for d, c in sorted(by_date.items())]
    return {
        "total": sum(by_type.values()),
        "by_type": dict(by_type),
        "top_ids": top_ids,
        "timeline": timeline,
    }


def _parse_ts(s: str):
    if not s:
        return None
    try:
        return datetime.fromisoformat(s.replace("Z", "+00:00"))
    except ValueError:
        return None
```

- [ ] **Step 4: 跑测试验证通过**

Run: `pytest tests/test_telemetry.py -v`
Expected: 5 PASS

- [ ] **Step 5: Commit**

```bash
git add graph-asset-platform/backend/app/telemetry/aggregator.py graph-asset-platform/backend/tests/test_telemetry.py
git commit -m "feat(platform): 打点 aggregator（三维聚合 + days 过滤）"
```

---

### Task 4: 鉴权中间件（TDD）

**Files:**
- Create: `graph-asset-platform/backend/app/middleware/__init__.py`（空）
- Create: `graph-asset-platform/backend/app/middleware/auth.py`
- Create: `graph-asset-platform/backend/tests/test_auth.py`
- Modify: `graph-asset-platform/backend/app/main.py`（挂中间件）

- [ ] **Step 1: 写失败测试** `tests/test_auth.py`

```python
"""鉴权中间件测试：单一 KEY 门禁；未配 KEY 旁路。

测试默认不设 GAP_API_KEY，故现有 test_api_* 不受影响（中间件旁路）。
本文件显式 monkeypatch config.API_KEY 验证鉴权生效（auth.dispatch 运行时读 config.API_KEY）。
"""
from fastapi.testclient import TestClient

import app.config as config


def _set_key(monkeypatch, key):
    """直接打 config.API_KEY（auth.dispatch 运行时读取，即时生效，无需 reload）。"""
    monkeypatch.setattr(config, "API_KEY", key)


def _clear_key(monkeypatch):
    monkeypatch.setattr(config, "API_KEY", "")


def test_no_key_configured_bypasses(tmp_data_dir, monkeypatch):
    """未配 KEY → 全放行（开发模式）。"""
    _clear_key(monkeypatch)
    from app.main import app
    with TestClient(app) as c:
        r = c.get("/api/v1/names")
        assert r.status_code == 200


def test_missing_header_returns_401(tmp_data_dir, monkeypatch):
    _set_key(monkeypatch, "secret123")
    from app.main import app
    with TestClient(app) as c:
        r = c.get("/api/v1/names")
        assert r.status_code == 401
        assert "api key" in r.json()["detail"]


def test_wrong_header_returns_401(tmp_data_dir, monkeypatch):
    _set_key(monkeypatch, "secret123")
    from app.main import app
    with TestClient(app) as c:
        r = c.get("/api/v1/names", headers={"X-API-Key": "wrong"})
        assert r.status_code == 401


def test_correct_header_passes(tmp_data_dir, monkeypatch):
    _set_key(monkeypatch, "secret123")
    from app.main import app
    with TestClient(app) as c:
        r = c.get("/api/v1/names", headers={"X-API-Key": "secret123"})
        assert r.status_code == 200


def test_non_api_path_not_guarded(tmp_data_dir, monkeypatch):
    """非 /api/ 路径（前端静态、SPA 兜底）不拦截。"""
    _set_key(monkeypatch, "secret123")
    from app.main import app
    with TestClient(app) as c:
        # 根路径 SPA 兜底返回 index.html 或 404，但绝不是 401
        r = c.get("/")
        assert r.status_code != 401
```

> 注：`tmp_data_dir` fixture 来自 `tests/conftest.py`（现有 test_api_objects.py 已使用）。这些测试不依赖图谱数据，`/api/v1/names` 空库返回 `{}` 也算 200。

- [ ] **Step 2: 跑测试验证失败**

Run: `pytest tests/test_auth.py -v`
Expected: FAIL（`ModuleNotFoundError: app.middleware.auth`）

- [ ] **Step 3: 实现 `app/middleware/auth.py`**

```python
"""鉴权中间件：单一共享 KEY（环境变量 GAP_API_KEY）。

- 保护所有 /api/* 请求：须带 X-API-Key header 且等于 GAP_API_KEY，否则 401。
- GAP_API_KEY 未配置 → 旁路（开发友好）。
- 非 /api/ 路径不拦截。
- KEY 取值绝不 echo（spec §6）。
- dispatch 运行时读 config.API_KEY（非 import 期绑定），便于测试 monkeypatch。
"""
import logging

from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware

from .. import config

logger = logging.getLogger(__name__)
if not config.API_KEY:
    logger.warning("鉴权未启用：未配置环境变量 GAP_API_KEY（生产请配置）")


class AuthMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        key = config.API_KEY  # 运行时读取，测试可 monkeypatch.setattr(config, "API_KEY", ...)
        if key and request.url.path.startswith("/api/"):
            if request.headers.get("X-API-Key", "") != key:
                return JSONResponse(
                    status_code=401,
                    content={"detail": "missing or invalid api key"},
                )
        return await call_next(request)
```

- [ ] **Step 4: 挂中间件到 `main.py`**

在 `main.py` 顶部 import 区加：
```python
from .middleware.auth import AuthMiddleware
```

把现有 CORS 块改为（**auth 先 add = 内层，CORS 后 add = 外层**，让 CORS 包装 401 响应、跨域兼容）：
```python
app = FastAPI(title="Graph Asset Platform", version="0.1.0", lifespan=lifespan)
# 先 add auth（内层），再 add CORS（外层）：CORS 包装 auth 的 401，保证跨域时 401 响应带 CORS 头。
# 同源前端不受影响；此顺序为跨域调试/未来部署预留。
app.add_middleware(AuthMiddleware)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
```

- [ ] **Step 5: 跑测试验证通过**

Run: `pytest tests/test_auth.py -v`
Expected: 5 PASS

- [ ] **Step 6: 回归现有 API 测试不受影响**

Run: `pytest tests/test_api_objects.py tests/test_api_assets.py -v`
Expected: 全 PASS（未配 KEY → 中间件旁路，现有测试绿）

- [ ] **Step 7: Commit**

```bash
git add graph-asset-platform/backend/app/middleware/__init__.py graph-asset-platform/backend/app/middleware/auth.py graph-asset-platform/backend/app/main.py graph-asset-platform/backend/tests/test_auth.py
git commit -m "feat(platform): 鉴权中间件（单一 KEY，未配旁路）"
```

---

### Task 5: `/domains` 改 POST + `/md`、`/domains` 埋点（TDD）

**Files:**
- Modify: `graph-asset-platform/backend/app/routers/objects.py`（`/domains` GET→POST；`/md`、`/domains` 末尾 `record()`）
- Modify: `graph-asset-platform/backend/tests/test_api_objects.py`（`test_domains_endpoint...` 改 POST；新增埋点测试）

- [ ] **Step 1: 改现有 /domains 测试为 POST + 加埋点测试**

在 `tests/test_api_objects.py` 把 `test_domains_endpoint_returns_business_domain_md` 里的 `c.get("/api/v1/domains")` 改为 `c.post("/api/v1/domains")`：

```python
def test_domains_endpoint_returns_business_domain_md(tmp_data_dir, monkeypatch):
    """/domains 一次性返全部 BusinessDomain 的 {id,name,md}（Agent 入口，只含 BD）。"""
    _setup(tmp_data_dir, monkeypatch, {"bd.md": _BD, "ns.md": _NS, "cs.md": _CS})
    with TestClient(app) as c:
        rows = c.post("/api/v1/domains").json()
        ids = {r["id"] for r in rows}
        assert ids == {"BusinessDomain@demo"}
        item = rows[0]
        assert item["name"] is not None
        assert "demo domain" in item["md"]
```

在该文件末尾追加埋点测试：
```python
def test_md_endpoint_records_telemetry(tmp_data_dir, monkeypatch, tmp_path):
    """/md 调用 → 每个成功 id 追加一条 jsonl 打点。"""
    import app.config as cfg
    monkeypatch.setattr(cfg, "TELEMETRY_FILE", tmp_path / "access.jsonl")
    _setup(tmp_data_dir, monkeypatch, {"a.md": CMD_EDGES, "b.md": CFG})
    with TestClient(app) as c:
        c.post("/api/v1/md", json={"ids": ["alpha@MMLCommand@ADD DEMO", "alpha@ConfigObject@DEMO_OBJ"]})
    import json
    lines = (tmp_path / "access.jsonl").read_text(encoding="utf-8").strip().split("\n")
    types = {json.loads(l)["type"] for l in lines}
    assert types == {"MMLCommand", "ConfigObject"}
    assert all(json.loads(l)["endpoint"] == "/md" for l in lines)


def test_domains_endpoint_records_telemetry(tmp_data_dir, monkeypatch, tmp_path):
    """/domains 调用 → 每个域 id 追加一条打点。"""
    import app.config as cfg
    monkeypatch.setattr(cfg, "TELEMETRY_FILE", tmp_path / "access.jsonl")
    _setup(tmp_data_dir, monkeypatch, {"bd.md": _BD, "ns.md": _NS})
    with TestClient(app) as c:
        c.post("/api/v1/domains")
    import json
    lines = (tmp_path / "access.jsonl").read_text(encoding="utf-8").strip().split("\n")
    assert len(lines) == 1
    rec = json.loads(lines[0])
    assert rec["id"] == "BusinessDomain@demo"
    assert rec["type"] == "BusinessDomain"
    assert rec["endpoint"] == "/domains"
```

- [ ] **Step 2: 跑测试验证失败**

Run: `pytest tests/test_api_objects.py::test_domains_endpoint_returns_business_domain_md tests/test_api_objects.py::test_md_endpoint_records_telemetry -v`
Expected: FAIL——`/domains` 此时仍是 GET 路由，`c.post` 触发 **405 Method Not Allowed**；且 `record` 未接线

- [ ] **Step 3: 改 `routers/objects.py`**

顶部 import 区加：
```python
from ..telemetry.recorder import record
```

把 `@router.get("/domains")` 改为 `@router.post("/domains")`，并在函数末尾 return 前埋点：
```python
@router.post("/domains")
def list_domains_with_md():
    """一次性返回全部业务域的完整 md（``[{id, name, md}, ...]``）。

    业务域是用户最优先的业务归属定位层——数量少（跨 NF 类，version 恒 null），
    Agent 入口直接取全部域 md。其他层级仍按 POST /md 沿 [[ID]] 引用下钻。
    """
    idx = get_service().index
    latest: dict = {}
    for (id_, _ver), obj in idx.nodes.items():
        if obj.type != "BusinessDomain":
            continue
        cur = latest.get(id_)
        if cur is None or (obj.version or "") > (cur.version or ""):
            latest[id_] = obj
    out = [
        {"id": id_, "name": obj.frontmatter.get("name"), "md": obj.raw_md}
        for id_, obj in latest.items()
    ]
    for item in out:
        record("/domains", item["id"], "BusinessDomain")
    return out
```

**完整重写 `batch_md`**（在成功赋值分支内加 `record()`，保留 `dict.fromkeys` 去重、两个错误 `continue` 分支、循环外 `return`）：

```python
@router.post("/md")
def batch_md(req: BatchMdRequest):
    idx = get_service().index
    out: dict = {}
    for id_ in dict.fromkeys(req.ids):
        available = idx.versions_of(id_)
        if not available:
            out[id_] = {"error": "对象不存在", "available_versions": []}
            continue
        obj = idx.resolve_node(id_, req.version)
        if obj is None:
            out[id_] = {
                "error": f"版本不存在: {id_}@{req.version}",
                "available_versions": available,
            }
            continue
        out[id_] = {"version": obj.version, "md": obj.raw_md}
        record("/md", id_, obj.type)  # 仅成功取到才埋点
    return out
```

> `record()` 必须在循环体内、成功赋值之后；不要放到循环外（否则丢失对象级粒度）。

- [ ] **Step 4: 跑测试验证通过**

Run: `pytest tests/test_api_objects.py -v`
Expected: 全 PASS（含新增 2 个埋点测试 + 改 POST 的 /domains 测试）

- [ ] **Step 5: Commit**

```bash
git add graph-asset-platform/backend/app/routers/objects.py graph-asset-platform/backend/tests/test_api_objects.py
git commit -m "feat(platform): /domains 改 POST + /md、/domains 对象级埋点"
```

---

### Task 6: 打点查询接口 `GET /telemetry/stats`（TDD）

**Files:**
- Create: `graph-asset-platform/backend/app/routers/telemetry.py`
- Modify: `graph-asset-platform/backend/app/main.py`（注册 router）
- Modify: `graph-asset-platform/backend/tests/test_telemetry.py`（加接口测试）

- [ ] **Step 1: 追加接口失败测试** 到 `tests/test_telemetry.py`

```python
def test_telemetry_stats_endpoint(tmp_path, monkeypatch):
    f = _use_tmp_telemetry(tmp_path, monkeypatch)
    _seed(f, [
        {"ts": "2026-07-23T10:00:00+00:00", "endpoint": "/md", "id": "F@1", "type": "Feature"},
        {"ts": "2026-07-23T10:01:00+00:00", "endpoint": "/md", "id": "C@2", "type": "MMLCommand"},
    ])
    from fastapi.testclient import TestClient
    from app.main import app
    with TestClient(app) as c:
        r = c.get("/api/v1/telemetry/stats", params={"days": 30})
        assert r.status_code == 200
        body = r.json()
        assert body["total"] == 2
        assert body["by_type"]["Feature"] == 1
        assert len(body["top_ids"]) >= 1
```

- [ ] **Step 2: 跑测试验证失败**

Run: `pytest tests/test_telemetry.py::test_telemetry_stats_endpoint -v`
Expected: FAIL（404，router 未注册）

- [ ] **Step 3: 实现 `routers/telemetry.py`**

```python
"""telemetry router：取用频次聚合查询（受鉴权中间件保护）。"""
from fastapi import APIRouter, Query

from ..telemetry.aggregator import aggregate

router = APIRouter()


@router.get("/telemetry/stats")
def telemetry_stats(days: int = Query(default=30, ge=1, le=365)):
    """返回最近 days 天的取用频次聚合：{total, by_type, top_ids, timeline}。"""
    return aggregate(days)
```

- [ ] **Step 4: 在 `main.py` 注册 router**

import 区加：
```python
from .routers import telemetry as telemetry_router
```
router 注册区加：
```python
app.include_router(telemetry_router.router, prefix="/api/v1")
```

- [ ] **Step 5: 跑测试验证通过**

Run: `pytest tests/test_telemetry.py -v`
Expected: 全 PASS

- [ ] **Step 6: 全量后端回归**

Run: `pytest tests/ -v`
Expected: 全 PASS（鉴权旁路，无回归）

- [ ] **Step 7: Commit**

```bash
git add graph-asset-platform/backend/app/routers/telemetry.py graph-asset-platform/backend/app/main.py graph-asset-platform/backend/tests/test_telemetry.py
git commit -m "feat(platform): GET /telemetry/stats 取用频次聚合接口"
```

---

## Chunk 2: 前端（登录态 + _req 注入 + 统计页取用频次）

> 前端无单测框架。每个 Task 的"测试" = `npm run build`（vue-tsc 类型检查 + 构建）通过 + 手动浏览器验证清单。前端命令在 `graph-asset-platform/frontend/` 下跑。

### Task 7: 登录态（auth.ts + LoginView + 路由守卫）

**Files:**
- Create: `graph-asset-platform/frontend/src/auth.ts`
- Create: `graph-asset-platform/frontend/src/views/LoginView.vue`
- Modify: `graph-asset-platform/frontend/src/router.ts`
- Modify: `graph-asset-platform/frontend/src/api.ts`（加 `verifyKey` 导出，供登录页验证）

- [ ] **Step 1: 写 `src/auth.ts`**

```typescript
// 鉴权 KEY 的浏览器存储（sessionStorage：关标签页即失效，适度安全）。
const KEY = 'gap_api_key'

export function getKey(): string {
  return sessionStorage.getItem(KEY) || ''
}
export function setKey(k: string): void {
  sessionStorage.setItem(KEY, k)
}
export function clearKey(): void {
  sessionStorage.removeItem(KEY)
}
export function hasKey(): boolean {
  return !!getKey()
}
```

- [ ] **Step 2: 在 `src/api.ts` 加 `verifyKey`**

在 api.ts 合适位置加（复用现有 `_req`）：
```typescript
import { getKey } from './auth'  // 顶部加（若已 import 则合并）

// 登录页验证 KEY：调轻接口 /names，200 即 KEY 正确。
export const verifyKey = (): Promise<Record<string, string>> =>
  _req<Record<string, string>>(`${BASE}/names`)
```

> 注意：`_req` 在 Task 8 才加 X-API-Key header。此处 verifyKey 在 Task 8 完成后才能带上 KEY。Task 7 末尾的 build 验证不依赖运行时鉴权（后端未配 KEY 时旁路）。

- [ ] **Step 3: 写 `src/views/LoginView.vue`**

```vue
<template>
  <div class="login-page">
    <form class="login-card" @submit.prevent="onSubmit">
      <h1 class="title">图谱资产</h1>
      <p class="sub">请输入访问 KEY</p>
      <input
        v-model="key"
        type="password"
        class="input"
        placeholder="API Key"
        autofocus
        autocomplete="current-password"
      />
      <div v-if="err" class="err">{{ err }}</div>
      <button type="submit" class="btn" :disabled="loading || !key.trim()">
        {{ loading ? '验证中…' : '进入' }}
      </button>
    </form>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { setKey } from '../auth'
import { verifyKey } from '../api'

const key = ref('')
const err = ref('')
const loading = ref(false)

async function onSubmit(): Promise<void> {
  loading.value = true
  err.value = ''
  try {
    setKey(key.value.trim())
    await verifyKey() // 200 → KEY 对
    // 整页跳转，绕开 router 实例依赖，最稳
    window.location.assign('/')
  } catch {
    err.value = 'KEY 无效或后端不可达'
  } finally {
    loading.value = false
  }
}
</script>

<style scoped>
.login-page {
  height: 100%;
  display: grid;
  place-items: center;
  background: var(--bg-sunken);
}
.login-card {
  display: flex;
  flex-direction: column;
  gap: var(--space-3);
  width: 320px;
  padding: var(--space-7);
  background: var(--bg-elev);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  box-shadow: var(--shadow);
}
.title {
  font-family: var(--display);
  font-size: 22px;
  font-weight: 700;
  margin: 0;
  text-align: center;
}
.sub {
  font-size: 13px;
  color: var(--text-muted);
  text-align: center;
  margin: 0;
}
.input {
  padding: 9px 12px;
  font-size: 14px;
  border: 1px solid var(--border);
  border-radius: var(--radius-sm);
  background: var(--bg);
  color: var(--text);
}
.input:focus {
  outline: none;
  border-color: var(--accent);
}
.err {
  font-size: 12.5px;
  color: var(--danger, #dc2626);
}
.btn {
  padding: 9px 12px;
  font-size: 14px;
  font-weight: 600;
  color: #fff;
  background: var(--accent);
  border: none;
  border-radius: var(--radius-sm);
  cursor: pointer;
}
.btn:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}
</style>
```

- [ ] **Step 4: 改 `src/router.ts` 加 /login + 守卫（用 Edit 针对性插入，保留现有路由与注释）**

三处 Edit（现有 7 条路由 + 顶部注释原样保留，**不全文重写**）：
1. 顶部 import 追加 auth：
```typescript
import { createRouter, createWebHistory } from 'vue-router'
import { hasKey } from './auth'
```
2. `routes:` 数组首项（`path: '/'`）前插 /login：
```typescript
    {
      path: '/login',
      name: 'login',
      component: () => import('./views/LoginView.vue'),
    },
```
3. 文件末尾（`createRouter({...})` 赋值语句之后）追加守卫：
```typescript
// 守卫：除登录页外，无 KEY → 跳登录
router.beforeEach((to) => {
  if (to.name === 'login') return true
  if (!hasKey()) return { name: 'login' }
  return true
})
```

- [ ] **Step 5: build 验证**

Run（在 `frontend/` 下）: `npm run build`
Expected: vue-tsc 无类型错误，构建成功

- [ ] **Step 6: Commit**

```bash
git add graph-asset-platform/frontend/src/auth.ts graph-asset-platform/frontend/src/views/LoginView.vue graph-asset-platform/frontend/src/router.ts graph-asset-platform/frontend/src/api.ts
git commit -m "feat(platform): 前端登录态（sessionStorage KEY + 路由守卫）"
```

---

### Task 8: `_req` 注入 X-API-Key + 401 跳登录

**Files:**
- Modify: `graph-asset-platform/frontend/src/api.ts`（`_req`）
- Modify: `graph-asset-platform/frontend/src/tests-module/api.ts`（`_req`）

- [ ] **Step 1: 改 `src/api.ts` 的 `_req`**

把 `_req` 改为（加 header + 401 处理）：
```typescript
import { getKey, clearKey } from './auth'  // 顶部（合并已有 import）

async function _req<T>(url: string, init?: RequestInit): Promise<T> {
  const headers = new Headers(init?.headers)
  const k = getKey()
  if (k) headers.set('X-API-Key', k)
  const resp = await fetch(url, { ...init, headers })
  if (resp.status === 401) {
    clearKey()
    // window.location 最稳，绕开 router 实例（避免 api.ts ↔ router.ts 循环依赖）
    if (!window.location.pathname.startsWith('/login')) {
      window.location.assign('/login')
    }
    throw new Error('未授权，已跳转登录')
  }
  if (!resp.ok) {
    let detail: unknown
    try {
      detail = await resp.json()
    } catch {
      detail = await resp.text().catch(() => '')
    }
    const msg =
      (detail && typeof detail === 'object' && 'detail' in detail
        ? JSON.stringify((detail as { detail: unknown }).detail)
        : String(detail)) || `HTTP ${resp.status}`
    const err = new Error(`API ${resp.status}: ${msg}`) as ApiError
    err.status = resp.status
    err.detail = detail
    throw err
  }
  const ct = resp.headers.get('content-type') || ''
  if (ct.includes('application/json')) {
    return (await resp.json()) as T
  }
  return (await resp.text()) as unknown as T
}
```

- [ ] **Step 2: 改 `src/tests-module/api.ts` 的 `_req`（同样改造）**

顶部 import（`tests-module/` 在 `src/` 下一层，`../auth` 回到 `src/`）：
```typescript
import { getKey, clearKey } from '../auth'
```
`_req` 同样加 header + 401 分支（与上一步代码一致）。

- [ ] **Step 3: build 验证**

Run: `npm run build`
Expected: 构建成功

- [ ] **Step 4: 手动验证清单（后端配 KEY 起来后做；也可在 Chunk 3 统一验证）**

- 未登录访问 `/` → 跳 `/login`
- 登录页输错 KEY → 提示"KEY 无效"
- 输对 KEY → 进 `/`，后续请求带 header
- 清掉 sessionStorage 再操作 → 401 → 跳 `/login`

- [ ] **Step 5: Commit**

```bash
git add graph-asset-platform/frontend/src/api.ts graph-asset-platform/frontend/src/tests-module/api.ts
git commit -m "feat(platform): _req 注入 X-API-Key + 401 跳登录"
```

---

### Task 9: 统计页「知识取用频次」section

**Files:**
- Create: `graph-asset-platform/frontend/src/components/TelemetrySection.vue`
- Modify: `graph-asset-platform/frontend/src/api.ts`（加 `fetchTelemetryStats` + 类型）
- Modify: `graph-asset-platform/frontend/src/views/StatsView.vue`（接入 section）

- [ ] **Step 1: 在 `src/api.ts` 加类型与函数**

```typescript
export interface TelemetryStats {
  total: number
  by_type: Record<string, number>
  top_ids: { id: string; type: string; count: number }[]
  timeline: { date: string; count: number }[]
}

export const fetchTelemetryStats = (days = 30): Promise<TelemetryStats> =>
  _req<TelemetryStats>(`${BASE}/telemetry/stats?days=${days}`)
```

- [ ] **Step 2: 写 `src/components/TelemetrySection.vue`**

```vue
<template>
  <section class="telemetry-section stagger-in">
    <header class="ts-head">
      <div>
        <h2 class="ts-title">知识取用频次</h2>
        <p class="ts-sub">SKILL 取用 /domains + /md 的对象级统计</p>
      </div>
      <div class="ts-controls">
        <el-select v-model="days" size="small" @change="load">
          <el-option :value="7" label="近 7 天" />
          <el-option :value="30" label="近 30 天" />
          <el-option :value="90" label="近 90 天" />
        </el-select>
        <span class="ts-total">共 {{ formatNum(stats?.total ?? 0) }} 次取用</span>
      </div>
    </header>

    <div v-if="err" class="ts-err">{{ err }}</div>
    <div v-else-if="!stats || stats.total === 0" class="ts-empty">
      暂无取用记录（SKILL 调用 /domains 或 /md 后此处展示）。
    </div>

    <div v-else class="ts-grid">
      <!-- 按 type 横条 -->
      <div class="ts-block">
        <div class="block-title">按类型</div>
        <div class="type-rows">
          <div v-for="r in typeRows" :key="r.type" class="type-row">
            <span class="type-label">{{ typeLabel(r.type) }}</span>
            <div class="type-bar-wrap">
              <div class="type-bar" :style="{ width: r.pct + '%' }" />
            </div>
            <span class="type-count mono">{{ formatNum(r.count) }}</span>
          </div>
        </div>
      </div>

      <!-- 热门对象 top-N -->
      <div class="ts-block">
        <div class="block-title">热门对象 Top {{ stats.top_ids.length }}</div>
        <ol class="top-list">
          <li v-for="(t, i) in stats.top_ids" :key="t.id" class="top-item">
            <span class="top-rank">{{ i + 1 }}</span>
            <span class="top-id mono" :title="t.id">{{ t.id }}</span>
            <span class="top-type">{{ typeLabel(t.type) }}</span>
            <span class="top-count mono">{{ formatNum(t.count) }}</span>
          </li>
        </ol>
      </div>

      <!-- 时间趋势（SVG 折线；数据点 <2 时退化提示） -->
      <div class="ts-block ts-block-wide">
        <div class="block-title">时间趋势（按日）</div>
        <svg v-if="stats.timeline.length > 1" class="trend" :viewBox="`0 0 ${W} ${H}`" preserveAspectRatio="none">
          <polyline :points="linePoints" fill="none" :stroke="accent" stroke-width="2" />
        </svg>
        <div v-else class="trend-empty">数据点不足（需 ≥2 天记录才画折线）</div>
        <div v-if="stats.timeline.length > 1" class="trend-axis">
          <span>{{ stats.timeline[0]?.date ?? '' }}</span>
          <span>{{ stats.timeline[stats.timeline.length - 1]?.date ?? '' }}</span>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup lang="ts">
import { computed, onMounted, ref } from 'vue'
import { ElSelect, ElOption } from 'element-plus'
import { fetchTelemetryStats, type TelemetryStats } from '../api'

const stats = ref<TelemetryStats | null>(null)
const days = ref(30)
const err = ref('')
const accent = '#4f46e5'
const W = 600
const H = 120

const TYPE_LABELS: Record<string, string> = {
  MMLCommand: '命令', ConfigObject: '配置对象', Feature: '特性', License: 'License',
  AtomTask: '原子Task', CompoundTask: '步骤Task', FeatureTask: '特性Task', Task: '任务',
  BusinessDomain: '业务域', NetworkScenario: '场景', ConfigurationSolution: '方案',
}

function typeLabel(t: string): string {
  return TYPE_LABELS[t] ?? t
}
function formatNum(n: number): string {
  return n.toLocaleString('zh-CN')
}

const typeRows = computed(() => {
  if (!stats.value) return []
  const entries = Object.entries(stats.value.by_type).sort((a, b) => b[1] - a[1])
  const max = entries[0]?.[1] || 1
  return entries.map(([type, count]) => ({ type, count, pct: Math.round((count / max) * 100) }))
})

const linePoints = computed(() => {
  if (!stats.value || stats.value.timeline.length === 0) return ''
  const tl = stats.value.timeline
  const max = Math.max(...tl.map((p) => p.count), 1)
  const n = tl.length
  return tl
    .map((p, i) => {
      const x = n === 1 ? W / 2 : (i / (n - 1)) * W
      const y = H - (p.count / max) * (H - 10) - 5
      return `${x.toFixed(1)},${y.toFixed(1)}`
    })
    .join(' ')
})

async function load(): Promise<void> {
  err.value = ''
  try {
    stats.value = await fetchTelemetryStats(days.value)
  } catch (e: unknown) {
    err.value = e instanceof Error ? e.message : String(e)
    stats.value = null
  }
}

onMounted(load)
</script>

<style scoped>
.telemetry-section {
  display: flex;
  flex-direction: column;
  gap: var(--space-4);
  padding: var(--space-5);
  background: var(--bg-elev);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  box-shadow: var(--shadow-sm);
}
.ts-head {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  gap: var(--space-3);
}
.ts-title {
  font-size: 16px;
  font-weight: 700;
  margin: 0;
}
.ts-sub {
  font-size: 12.5px;
  color: var(--text-muted);
  margin: 2px 0 0;
}
.ts-controls {
  display: flex;
  align-items: center;
  gap: var(--space-3);
}
.ts-total {
  font-size: 12.5px;
  color: var(--text-muted);
}
.ts-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: var(--space-5);
}
.ts-block-wide {
  grid-column: 1 / -1;
}
.block-title {
  font-size: 12px;
  font-weight: 600;
  color: var(--text-faint);
  text-transform: uppercase;
  letter-spacing: 0.04em;
  margin-bottom: var(--space-2);
}
.type-rows {
  display: flex;
  flex-direction: column;
  gap: 6px;
}
.type-row {
  display: grid;
  grid-template-columns: 70px 1fr 50px;
  align-items: center;
  gap: 8px;
  font-size: 12.5px;
}
.type-bar-wrap {
  height: 8px;
  background: var(--bg-sunken);
  border-radius: 999px;
  overflow: hidden;
}
.type-bar {
  height: 100%;
  background: var(--accent);
  border-radius: 999px;
}
.type-count {
  text-align: right;
  color: var(--text);
  font-weight: 600;
}
.top-list {
  list-style: none;
  margin: 0;
  padding: 0;
  display: flex;
  flex-direction: column;
  gap: 4px;
}
.top-item {
  display: grid;
  grid-template-columns: 24px 1fr auto auto;
  align-items: center;
  gap: 8px;
  font-size: 12.5px;
  padding: 3px 0;
}
.top-rank {
  color: var(--text-faint);
  font-weight: 600;
}
.top-id {
  color: var(--text);
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}
.top-type {
  font-size: 11px;
  color: var(--text-muted);
  background: var(--bg-sunken);
  padding: 1px 6px;
  border-radius: 4px;
}
.top-count {
  color: var(--text);
  font-weight: 600;
}
.trend {
  width: 100%;
  height: 120px;
  background: var(--bg-sunken);
  border-radius: var(--radius-sm);
}
.trend-empty {
  height: 120px;
  display: grid;
  place-items: center;
  font-size: 12px;
  color: var(--text-faint);
  background: var(--bg-sunken);
  border-radius: var(--radius-sm);
}
.trend-axis {
  display: flex;
  justify-content: space-between;
  font-size: 11px;
  color: var(--text-faint);
  margin-top: 4px;
}
.ts-empty,
.ts-err {
  font-size: 13px;
  color: var(--text-muted);
  padding: var(--space-3) 0;
}
.ts-err {
  color: var(--danger, #dc2626);
}
</style>
```

- [ ] **Step 3: 接入 `StatsView.vue`**

在 `StatsView.vue` 的 `<script setup>` 顶部加 import：
```typescript
import TelemetrySection from '../components/TelemetrySection.vue'
```
在模板的 `<!-- 4 张层级卡片 -->` `<section class="card-grid">...</section>` 之后、`<!-- 空态 -->` 之前插入：
```html
      <!-- 知识取用频次（取用打点聚合） -->
      <TelemetrySection v-if="s" />
```

- [ ] **Step 4: build 验证**

Run: `npm run build`
Expected: 构建成功

- [ ] **Step 5: 手动验证清单（Chunk 3 统一做）**

- 统计页底部出现「知识取用频次」section
- 三区块（按类型横条 / Top-N / 时间折线）渲染
- 天数切换（7/30/90）刷新数据

- [ ] **Step 6: Commit**

```bash
git add graph-asset-platform/frontend/src/components/TelemetrySection.vue graph-asset-platform/frontend/src/api.ts graph-asset-platform/frontend/src/views/StatsView.vue
git commit -m "feat(platform): 统计页加「知识取用频次」section（三维，零依赖）"
```

---

## Chunk 3: 文档 + 配置 + 端到端验证

### Task 10: 配置文件（.gitignore + .env.example）

**Files:**
- Modify: `graph-asset-platform/.gitignore`
- Create: `graph-asset-platform/.env.example`

- [ ] **Step 1: 确认 `.gitignore` 已覆盖打点数据（通常无需改动）**

`graph-asset-platform/.gitignore` 已含 `platform-data/`（整目录），`platform-data/telemetry/` 自动被忽略。**确认该行存在即可，不必额外添加**。若想显式注明，可加一行注释 `# platform-data/telemetry/ 已被 platform-data/ 覆盖`，但不必要。

- [ ] **Step 2: 写 `.env.example`**

```
# 鉴权 KEY：前端登录与 SKILL 调用共用。生产必配；不配则鉴权旁路（仅开发）。
# 取值绝不泄露到日志/响应。
GAP_API_KEY=
```

- [ ] **Step 3: Commit**

```bash
git add graph-asset-platform/.gitignore graph-asset-platform/.env.example
git commit -m "chore(platform): .gitignore 排除打点数据 + .env.example"
```

---

### Task 11: 文档同步（README + 图谱接口.md + SKILL.md）

**Files:**
- Modify: `graph-asset-platform/README.md`
- Modify: `三层图谱构建规范/skill/图谱接口.md`
- Modify: `三层图谱构建规范/skill/SKILL.md`（若有 /domains、/md 示例）

- [ ] **Step 1: README 启动命令加 GAP_API_KEY**

先定位现有启动命令：`grep -n "uvicorn" graph-asset-platform/README.md`，把后端启动行从（before）：
```
uvicorn app.main:app --app-dir graph-asset-platform/backend --port 8000
```
改为（after，前缀 KEY）：
```
GAP_API_KEY=你的KEY uvicorn app.main:app --app-dir graph-asset-platform/backend --port 8000
```
> Windows cmd: `set GAP_API_KEY=你的KEY && uvicorn ...`；PowerShell: `$env:GAP_API_KEY="你的KEY"; uvicorn ...`；Git Bash 用上面的 bash 语法。
并在启动段补一句：
> 鉴权：未配置 `GAP_API_KEY` 时鉴权旁路（仅开发）。生产/外网必须配置。SKILL 与前端登录共用此 KEY。

- [ ] **Step 2: `图谱接口.md` 改 POST + KEY**

把"## 1. 业务域直取 GET /domains"改为 `POST /domains`，curl 示例：
```cmd
curl -s -X POST http://127.0.0.1:8000/api/v1/domains -H "X-API-Key: %GAP_API_KEY%"
```
端点表格里 `GET /domains` → `POST /domains`。
`POST /md` 的 curl 示例加 `-H "X-API-Key: $GAP_API_KEY"`。
顶部 BASE 段补一句：所有请求须带 `-H "X-API-Key: $GAP_API_KEY"`（未配 KEY 时后端旁路）。

- [ ] **Step 3: `SKILL.md` 同步**

凡是引用 `GET /domains` 或 `/md` 调用的章节，统一改 POST + KEY header 说明。

- [ ] **Step 4: Commit**

```bash
git add graph-asset-platform/README.md 三层图谱构建规范/skill/图谱接口.md 三层图谱构建规范/skill/SKILL.md
git commit -m "docs(platform): 鉴权KEY + /domains改POST 文档同步"
```

---

### Task 12: 端到端验证

**Files:** 无（验证 + 必要时微调）

- [ ] **Step 1: 后端带 KEY 启动**

Run（在 `backend/` 下，Git Bash）:
```bash
GAP_API_KEY=testkey123 uvicorn app.main:app --port 8000
```
> Windows cmd: `set GAP_API_KEY=testkey123 && uvicorn app.main:app --port 8000`；PowerShell: `$env:GAP_API_KEY="testkey123"; uvicorn app.main:app --port 8000`。
Expected: 启动日志不再有"鉴权未启用"WARNING（KEY 已配）。

- [ ] **Step 2: 鉴权 curl 验证**

```bash
# 无 KEY → 401
curl -s -o /dev/null -w "%{http_code}\n" http://127.0.0.1:8000/api/v1/names
# 期望 401

# 错 KEY → 401
curl -s -o /dev/null -w "%{http_code}\n" -H "X-API-Key: wrong" http://127.0.0.1:8000/api/v1/names
# 期望 401

# 对 KEY → 200
curl -s -o /dev/null -w "%{http_code}\n" -H "X-API-Key: testkey123" http://127.0.0.1:8000/api/v1/names
# 期望 200

# POST /domains 带 KEY → 200
curl -s -X POST -H "X-API-Key: testkey123" http://127.0.0.1:8000/api/v1/domains | head -c 200
# 期望返回业务域 md 数组

# GET /domains → 404（已删）
curl -s -o /dev/null -w "%{http_code}\n" -H "X-API-Key: testkey123" http://127.0.0.1:8000/api/v1/domains
# 期望 405 或 404（GET 路由不存在）
```

- [ ] **Step 3: 打点验证**

```bash
# 取若干 md（若无数据可先 POST /domains）
curl -s -X POST -H "X-API-Key: testkey123" -H "Content-Type: application/json" \
  -d '{"ids":["BusinessDomain@charging"]}' http://127.0.0.1:8000/api/v1/md

# 查频次聚合
curl -s -H "X-API-Key: testkey123" "http://127.0.0.1:8000/api/v1/telemetry/stats?days=7" | head -c 400
# 期望返回 {total, by_type, top_ids, timeline}，total>0

# 查 jsonl 落盘
cat graph-asset-platform/platform-data/telemetry/access.jsonl | head -3
# 期望每行一条 {ts,endpoint,id,type}
```

- [ ] **Step 4: 前端构建 + 启动**

Run（在 `frontend/` 下）: `npm run build`
然后由后端托管 dist（已挂载），或 `npm run dev` 调试。
浏览器访问 `http://127.0.0.1:8000/`。

- [ ] **Step 5: 前端端到端验证清单**

- [ ] 未登录访问 → 自动跳 `/login`
- [ ] 登录页输 `testkey123` → 进入首页
- [ ] 各菜单（图谱浏览/统计/上传/测试）正常加载（请求带 KEY）
- [ ] 统计页底部「知识取用频次」三区块渲染，数据与 curl 一致
- [ ] 手动 sessionStorage 清 KEY → 下次请求 401 → 跳 `/login`
- [ ] DevTools Network：请求 header 带 `X-API-Key`

- [ ] **Step 6: 隔离回归确认（扩面 diff）**

Run:
```bash
git diff master -- graph-asset-platform/backend/app/service.py \
                     graph-asset-platform/backend/app/index.py \
                     graph-asset-platform/backend/app/store.py \
                     graph-asset-platform/backend/app/edges.py \
                     graph-asset-platform/backend/app/models.py \
                     graph-asset-platform/backend/app/bundle.py \
                     graph-asset-platform/backend/app/tests/
```
Expected: **空 diff**（图谱解析/索引/服务 + 测试子系统源码零改动，隔离红线达标）。本次仅动 `config/main/objects(2 处 record)/新模块/前端 _req`，上述文件不应出现。

- [ ] **Step 7: 最终提交（若有验证期微调）**

```bash
git add -A
git commit -m "test(platform): 端到端验证通过（鉴权+打点+频次面板）"
```

---

## 完成标准

- [ ] 后端：`pytest tests/ -v` 全 PASS（含新 test_auth/test_telemetry + 改 POST 的 test_api_objects）
- [ ] 前端：`npm run build` 无类型错误
- [ ] 鉴权：无/错 KEY → 401；对 KEY → 200；未配 KEY → 旁路
- [ ] 打点：`/md`、`/domains` 调用后 jsonl 落盘；`/telemetry/stats` 返回三维聚合
- [ ] 前端：登录页 + 401 跳转 + 统计页取用频次 section
- [ ] 隔离：图谱 service / tests service 零改动
- [ ] 文档：README / 图谱接口.md / SKILL.md 同步 POST + KEY
