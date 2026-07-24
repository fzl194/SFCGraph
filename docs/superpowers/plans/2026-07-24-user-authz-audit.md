# 用户体系 + 权限 + 审计打点 实现计划（v2）

> **For agentic workers:** REQUIRED: Use superpowers:subagent-driven-development (if subagents available) or superpowers:executing-plans to implement this plan. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 把 v1「单一 KEY 门禁 + 打点」升级为多用户（users.json）+ 三 flag 权限 + 全量审计打点（统计仍只 SKILL 两接口，加 by_user；轨迹 admin 看）。

**Architecture:** `users.json` 明文 KEY；鉴权中间件 KEY 反查用户 + 权限校验 + 请求级打点①；`/md`/`/domains` router 对象级打点②；统计只聚合②+skill，轨迹聚合①按 user。前端登录页用户名+KEY，新增 admin 用户管理菜单。

**Tech Stack:** FastAPI + pytest + httpx（后端）；Vue3 + TS + vue-router + Element Plus（前端，`npm run build` + 浏览器验证）。

**Spec:** `docs/superpowers/specs/2026-07-24-user-authz-audit-design.md`
**前序（v1）：** `docs/superpowers/plans/2026-07-23-auth-and-telemetry.md`（本次改造其产物）

**工作目录：** 后端命令在 `graph-asset-platform/backend/`；前端在 `graph-asset-platform/frontend/`；直接在 master 提交（用户全局规则）。

**关键改造点（相对 v1）：**
- `config.py`：+`USERS_FILE`，删 `API_KEY`（Task 5 随 auth 改造删）
- `middleware/auth.py`：单一 KEY → 用户体系 + 权限 + 打点① + `/users/login` 豁免 + 取消旁路
- `telemetry/recorder.py`：`record(endpoint, id_="", type_="", *, user, caller, level)` 新签名
- `telemetry/aggregator.py`：`aggregate_stats`（②+skill+by_user）+ `aggregate_activity`（①按 user）
- `routers/objects.py`：`/md`/`/domains` record 传 `level="object"`+user/caller，handler 加 `request: Request`
- v1 的 `test_auth.py`/`test_telemetry.py`/`test_api_objects.py` 埋点测试要同步更新

---

## Chunk 1: 后端用户体系（users.json + store/service + users router）

### Task 1: config 加 USERS_FILE

**Files:** Modify `graph-asset-platform/backend/app/config.py`

- [ ] **Step 1: 加 USERS_FILE（暂保留 API_KEY，Task 5 删）**

在 `config.py` 末尾加：
```python
# —— 用户体系（多用户，明文 KEY，不入 git）——
USERS_FILE = DATA_DIR / "users.json"
```

- [ ] **Step 2: 验证 import**

Run（在 `backend/`）: `python -c "from app import config; print(config.USERS_FILE)"`
Expected: 打印 `...platform-data\users.json`

- [ ] **Step 3: Commit**

```bash
git add app/config.py
git commit -m "feat(platform): config 加 USERS_FILE（用户体系）"
```

---

### Task 2: users/store.py（TDD）

**Files:**
- Create: `app/users/__init__.py`（空）
- Create: `app/users/store.py`
- Create: `tests/test_users_store.py`

- [ ] **Step 1: 写失败测试** `tests/test_users_store.py`

```python
"""users.store 测试：users.json 读写、按 key/name 查、增删改。"""
import json


def _use_tmp_users(tmp_path, monkeypatch):
    f = tmp_path / "users.json"
    import app.config as cfg
    monkeypatch.setattr(cfg, "USERS_FILE", f)
    return f


def test_load_empty_when_absent(tmp_path, monkeypatch):
    _use_tmp_users(tmp_path, monkeypatch)
    from app.users.store import list_users
    assert list_users() == []


def test_add_and_find_by_key(tmp_path, monkeypatch):
    _use_tmp_users(tmp_path, monkeypatch)
    from app.users.store import add_user, find_by_key
    add_user({"username": "admin", "key": "gap_abc", "can_frontend": True})
    u = find_by_key("gap_abc")
    assert u is not None and u["username"] == "admin"
    assert find_by_key("nope") is None


def test_find_by_name_and_update_and_delete(tmp_path, monkeypatch):
    _use_tmp_users(tmp_path, monkeypatch)
    from app.users.store import add_user, find_by_name, update_user, delete_user
    add_user({"username": "u1", "key": "k1", "can_skill": True})
    assert find_by_name("u1") is not None
    updated = update_user("u1", {"can_frontend": True})
    assert updated["can_frontend"] is True
    assert delete_user("u1") is True
    assert find_by_name("u1") is None
    assert delete_user("u1") is False  # 已删


def test_persists_to_disk(tmp_path, monkeypatch):
    f = _use_tmp_users(tmp_path, monkeypatch)
    from app.users.store import add_user
    add_user({"username": "x", "key": "kx"})
    data = json.loads(f.read_text(encoding="utf-8"))
    assert data["users"][0]["username"] == "x"
```

- [ ] **Step 2: 跑验证失败**

Run: `pytest tests/test_users_store.py -v`
Expected: FAIL（`ModuleNotFoundError: app.users.store`）

- [ ] **Step 3: 实现 `app/users/store.py`**

```python
"""users.json 读写（明文 KEY；进程内 Lock 串行写，保证原子）。"""
import json
import threading
from pathlib import Path
from typing import Optional

from .. import config

_lock = threading.Lock()


def _load() -> dict:
    path = Path(config.USERS_FILE)
    if not path.exists():
        return {"users": []}
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    data.setdefault("users", [])
    return data


def _save(data: dict) -> None:
    path = Path(config.USERS_FILE)
    path.parent.mkdir(parents=True, exist_ok=True)
    with _lock:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)


def list_users() -> list:
    return _load()["users"]


def find_by_key(key: str) -> Optional[dict]:
    for u in _load()["users"]:
        if u.get("key") == key:
            return u
    return None


def find_by_name(username: str) -> Optional[dict]:
    for u in _load()["users"]:
        if u.get("username") == username:
            return u
    return None


def add_user(user: dict) -> dict:
    data = _load()
    data["users"].append(user)
    _save(data)
    return user


def update_user(username: str, patch: dict) -> Optional[dict]:
    data = _load()
    for u in data["users"]:
        if u.get("username") == username:
            u.update(patch)
            _save(data)
            return u
    return None


def delete_user(username: str) -> bool:
    data = _load()
    before = len(data["users"])
    data["users"] = [u for u in data["users"] if u.get("username") != username]
    if len(data["users"]) < before:
        _save(data)
        return True
    return False
```

- [ ] **Step 4: 跑验证通过**

Run: `pytest tests/test_users_store.py -v`
Expected: 4 PASS

- [ ] **Step 5: Commit**

```bash
git add app/users/__init__.py app/users/store.py tests/test_users_store.py
git commit -m "feat(platform): users.store（users.json 读写）"
```

---

### Task 3: users/service.py（TDD）

**Files:**
- Create: `app/users/service.py`
- Create: `tests/test_users_service.py`

- [ ] **Step 1: 写失败测试** `tests/test_users_service.py`

```python
"""users.service 测试：gen_key 唯一、authenticate、check_perm 矩阵、create/reset/delete。"""


def _seed(tmp_path, monkeypatch, users):
    import app.config as cfg
    monkeypatch.setattr(cfg, "USERS_FILE", tmp_path / "users.json")
    import json
    (tmp_path / "users.json").write_text(json.dumps({"users": users}), encoding="utf-8")


def test_gen_key_unique_and_prefixed(tmp_path, monkeypatch):
    _seed(tmp_path, monkeypatch, [{"username": "a", "key": "gap_existing"}])
    from app.users.service import gen_key
    k = gen_key()
    assert k.startswith("gap_") and k != "gap_existing"


def test_authenticate_by_key(tmp_path, monkeypatch):
    _seed(tmp_path, monkeypatch, [{"username": "u", "key": "k1", "can_skill": True}])
    from app.users.service import authenticate
    assert authenticate("k1")["username"] == "u"
    assert authenticate("nope") is None


def test_check_perm_matrix(tmp_path, monkeypatch):
    from app.users.service import check_perm
    admin = {"is_admin": True}
    fe = {"can_frontend": True}
    sk = {"can_skill": True}
    plain = {}
    # admin 全权
    assert check_perm(admin, "frontend") and check_perm(admin, "skill") and check_perm(admin, "admin")
    # can_frontend：前端✓、skill✓（前端也能调两接口）、admin✗
    assert check_perm(fe, "frontend") and check_perm(fe, "skill") and not check_perm(fe, "admin")
    # can_skill：前端✗、skill✓、admin✗
    assert not check_perm(sk, "frontend") and check_perm(sk, "skill") and not check_perm(sk, "admin")
    # 无权限：全✗
    assert not check_perm(plain, "frontend")


def test_create_user_returns_key_and_rejects_dup(tmp_path, monkeypatch):
    _seed(tmp_path, monkeypatch, [{"username": "u", "key": "k"}])
    from app.users.service import create_user
    import pytest
    u = create_user("new", can_frontend=True, can_skill=False)
    assert u["key"].startswith("gap_") and u["can_frontend"] is True
    with pytest.raises(ValueError):
        create_user("u", can_frontend=False, can_skill=False)  # 重名


def test_reset_key_and_set_perms(tmp_path, monkeypatch):
    _seed(tmp_path, monkeypatch, [{"username": "u", "key": "k", "can_frontend": False}])
    from app.users.service import reset_key, set_perms, find_by_name
    import app.users.store as store
    monkeypatch.setattr(store, "find_by_name", lambda n: store.find_by_name(n))  # no-op
    new_k = reset_key("u")
    assert new_k and new_k != "k"
    set_perms("u", can_frontend=True, can_skill=True, is_admin=False)
    assert find_by_name("u")["can_frontend"] is True
```

- [ ] **Step 2: 跑验证失败**

Run: `pytest tests/test_users_service.py -v`
Expected: FAIL（`ModuleNotFoundError: app.users.service`）

- [ ] **Step 3: 实现 `app/users/service.py`**

```python
"""用户操作：生成 key、认证、权限检查、CRUD。"""
import secrets
from datetime import datetime, timezone
from typing import Optional

from . import store


def gen_key() -> str:
    """生成全局唯一 key（撞则重试）。"""
    while True:
        k = "gap_" + secrets.token_hex(16)
        if store.find_by_key(k) is None:
            return k


def authenticate(key: str) -> Optional[dict]:
    return store.find_by_key(key)


def check_perm(user: dict, perm: str) -> bool:
    """perm ∈ frontend/skill/admin。is_admin 全权。"""
    if user.get("is_admin"):
        return True
    if perm == "frontend":
        return bool(user.get("can_frontend"))
    if perm == "skill":
        return bool(user.get("can_skill")) or bool(user.get("can_frontend"))
    return False  # admin 仅 is_admin


def create_user(username: str, can_frontend: bool, can_skill: bool, is_admin: bool = False) -> dict:
    if store.find_by_name(username) is not None:
        raise ValueError(f"用户已存在: {username}")
    user = {
        "username": username,
        "key": gen_key(),
        "can_frontend": can_frontend,
        "can_skill": can_skill,
        "is_admin": is_admin,
        "created_at": datetime.now(timezone.utc).isoformat(),
    }
    return store.add_user(user)


def reset_key(username: str) -> Optional[str]:
    k = gen_key()
    u = store.update_user(username, {"key": k})
    return k if u else None


def set_perms(username: str, can_frontend: bool, can_skill: bool, is_admin: bool) -> Optional[dict]:
    return store.update_user(username, {
        "can_frontend": can_frontend, "can_skill": can_skill, "is_admin": is_admin,
    })


def delete_user(username: str) -> bool:
    return store.delete_user(username)
```

- [ ] **Step 4: 跑验证通过**

Run: `pytest tests/test_users_service.py -v`
Expected: 5 PASS

- [ ] **Step 5: Commit**

```bash
git add app/users/service.py tests/test_users_service.py
git commit -m "feat(platform): users.service（gen_key/authenticate/check_perm/CRUD）"
```

---

### Task 4: routers/users.py（login + CRUD，TDD）

**Files:**
- Create: `app/routers/users.py`
- Create: `tests/test_users_api.py`
- Modify: `app/main.py`（注册 router）

- [ ] **Step 1: 写失败测试** `tests/test_users_api.py`

```python
"""users router 测试：login（公开）+ CRUD（需 is_admin）。
每测用 tmp users.json + 显式 seed admin（is_admin）登录拿 X-API-Key。
"""
import json
from fastapi.testclient import TestClient


def _seed_users(tmp_path, monkeypatch, users):
    import app.config as cfg
    monkeypatch.setattr(cfg, "USERS_FILE", tmp_path / "users.json")
    (tmp_path / "users.json").write_text(json.dumps({"users": users}), encoding="utf-8")


ADMIN = {"username": "admin", "key": "gap_admin", "can_frontend": True, "can_skill": True, "is_admin": True}
SKILL_ONLY = {"username": "sa", "key": "gap_sa", "can_skill": True}


def test_login_success(tmp_path, monkeypatch):
    _seed_users(tmp_path, monkeypatch, [ADMIN])
    from app.main import app
    with TestClient(app) as c:
        r = c.post("/api/v1/users/login", json={"username": "admin", "key": "gap_admin"})
        assert r.status_code == 200
        assert r.json()["is_admin"] is True


def test_login_wrong_creds(tmp_path, monkeypatch):
    _seed_users(tmp_path, monkeypatch, [ADMIN])
    from app.main import app
    with TestClient(app) as c:
        assert c.post("/api/v1/users/login", json={"username": "admin", "key": "wrong"}).status_code == 401


def test_login_no_frontend_perm(tmp_path, monkeypatch):
    _seed_users(tmp_path, monkeypatch, [SKILL_ONLY])
    from app.main import app
    with TestClient(app) as c:
        # sa 只有 can_skill，不能登录前端
        assert c.post("/api/v1/users/login", json={"username": "sa", "key": "gap_sa"}).status_code == 403


def test_admin_can_list_and_create(tmp_path, monkeypatch):
    _seed_users(tmp_path, monkeypatch, [ADMIN])
    from app.main import app
    with TestClient(app) as c:
        h = {"X-API-Key": "gap_admin"}
        assert c.get("/api/v1/users", headers=h).status_code == 200
        r = c.post("/api/v1/users", json={"username": "new", "can_skill": True}, headers=h)
        assert r.status_code == 200
        assert r.json()["key"].startswith("gap_")


def test_non_admin_cannot_list(tmp_path, monkeypatch):
    _seed_users(tmp_path, monkeypatch, [ADMIN, SKILL_ONLY])
    from app.main import app
    with TestClient(app) as c:
        # sa 调 /users（admin 专属）→ 403（Task5 权限中间件；本 Task 先 401/占位）
        # 注：本 Task 权限中间件未改，/users 暂无保护；Task 5 补权限后此测试生效
        pass  # 占位，Task 5 启用
```

> 注：`test_non_admin_cannot_list` 在 Task 5（权限中间件改造）后才生效，本 Task 先占位。其他测试本 Task 通过（login 公开 + admin CRUD）。CRUD 端点暂不加权限保护（Task 5 中间件统一加），或本 Task 先加 `is_admin` 检查占位。

- [ ] **Step 2: 跑验证失败**

Run: `pytest tests/test_users_api.py -v`
Expected: FAIL（404，router 未注册）

- [ ] **Step 3: 实现 `app/routers/users.py`**

```python
"""users router：登录（公开）+ 用户管理（is_admin）。

权限由中间件统一校验（Task 5）：/users/login 豁免；GET/POST/PATCH/DELETE /users* 需 is_admin；
GET /users/{name}/activity 需 is_admin（Task 9 加）。
本 Task 先实现端点逻辑，权限依赖 Task 5 中间件。
"""
from typing import Optional

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from .. import service

router = APIRouter()


class LoginIn(BaseModel):
    username: str
    key: str


class UserCreateIn(BaseModel):
    username: str
    can_frontend: bool = False
    can_skill: bool = False
    is_admin: bool = False


class UserPatchIn(BaseModel):
    can_frontend: Optional[bool] = None
    can_skill: Optional[bool] = None
    is_admin: Optional[bool] = None
    reset_key: bool = False


def _safe(u: dict) -> dict:
    return {k: u.get(k) for k in ("username", "key", "can_frontend", "can_skill", "is_admin", "created_at")}


@router.post("/users/login")
def login(req: LoginIn):
    """登录：username+key 匹配且 can_frontend → 返用户。公开（中间件豁免）。"""
    u = service.authenticate(req.key)
    if u is None or u.get("username") != req.username:
        raise HTTPException(401, "用户名或 KEY 错误")
    if not service.check_perm(u, "frontend"):
        raise HTTPException(403, "无前端访问权限")
    return _safe(u)


@router.get("/users")
def list_users():
    return [_safe(u) for u in service.list_users()]


@router.post("/users")
def create_user(req: UserCreateIn):
    try:
        return _safe(service.create_user(req.username, req.can_frontend, req.can_skill, req.is_admin))
    except ValueError as e:
        raise HTTPException(400, str(e))


@router.patch("/users/{username}")
def update_user(username: str, req: UserPatchIn):
    from . import store  # 局部 import 避免循环
    u = store.find_by_name(username)
    if u is None:
        raise HTTPException(404, "用户不存在")
    if req.reset_key:
        service.reset_key(username)
    if any(v is not None for v in (req.can_frontend, req.can_skill, req.is_admin)):
        service.set_perms(
            username,
            req.can_frontend if req.can_frontend is not None else u["can_frontend"],
            req.can_skill if req.can_skill is not None else u["can_skill"],
            req.is_admin if req.is_admin is not None else u["is_admin"],
        )
    return _safe(store.find_by_name(username))


@router.delete("/users/{username}")
def delete_user(username: str):
    if not service.delete_user(username):
        raise HTTPException(404, "用户不存在")
    return {"ok": True}
```

> `update_user` 里 `from . import store` 的 `.` 指向 `routers` 包，错误。改 `from ..users import store`。

- [ ] **Step 4: 注册 router 到 `main.py`**

import 区加 `from .routers import users as users_router`；注册区加 `app.include_router(users_router.router, prefix="/api/v1")`。

- [ ] **Step 5: 跑验证通过**

Run: `pytest tests/test_users_api.py -v`
Expected: login/CRUD 测试 PASS（`test_non_admin_cannot_list` 占位 pass）

- [ ] **Step 6: Commit**

```bash
git add app/routers/users.py app/main.py tests/test_users_api.py
git commit -m "feat(platform): users router（login+CRUD，权限待Task5中间件）"
```

---

## Chunk 2: 后端鉴权 + 打点改造

### Task 5: auth 中间件改造（KEY→用户→权限+打点①，TDD）+ 删 config.API_KEY

**Files:**
- Modify: `app/middleware/auth.py`
- Modify: `app/config.py`（删 `API_KEY`）
- Modify: `tests/test_auth.py`（v1 单 KEY 测试 → 用户体系测试）
- Modify: `app/main.py`（启动检查 users.json）

- [ ] **Step 1: 重写 `tests/test_auth.py`**（替换 v1 单 KEY 测试）

```python
"""鉴权中间件测试（v2 用户体系）：KEY 反查用户 + 权限 + login 豁免 + 取消旁路 + 打点①。"""
import json
from fastapi.testclient import TestClient


def _seed(tmp_path, monkeypatch, users):
    import app.config as cfg
    monkeypatch.setattr(cfg, "USERS_FILE", tmp_path / "users.json")
    (tmp_path / "users.json").write_text(json.dumps({"users": users}), encoding="utf-8")


ADMIN = {"username": "admin", "key": "gap_admin", "can_frontend": True, "can_skill": True, "is_admin": True}
FE = {"username": "fe", "key": "gap_fe", "can_frontend": True}
SK = {"username": "sk", "key": "gap_sk", "can_skill": True}


def test_no_key_401(tmp_path, monkeypatch):
    _seed(tmp_path, monkeypatch, [ADMIN])
    from app.main import app
    with TestClient(app) as c:
        assert c.get("/api/v1/names").status_code == 401


def test_wrong_key_401(tmp_path, monkeypatch):
    _seed(tmp_path, monkeypatch, [ADMIN])
    from app.main import app
    with TestClient(app) as c:
        assert c.get("/api/v1/names", headers={"X-API-Key": "wrong"}).status_code == 401


def test_login_exempt_from_auth(tmp_path, monkeypatch):
    """login 端点免鉴权（空 users 也能调）。"""
    _seed(tmp_path, monkeypatch, [])
    from app.main import app
    with TestClient(app) as c:
        r = c.post("/api/v1/users/login", json={"username": "x", "key": "y"})
        assert r.status_code == 401  # 校验失败但不因「无权」401（login 豁免）


def test_empty_users_401_all(tmp_path, monkeypatch):
    _seed(tmp_path, monkeypatch, [])
    from app.main import app
    with TestClient(app) as c:
        assert c.get("/api/v1/names", headers={"X-API-Key": "any"}).status_code == 401


def test_skill_user_can_md_but_not_objects(tmp_path, monkeypatch):
    _seed(tmp_path, monkeypatch, [SK])
    from app.main import app
    with TestClient(app) as c:
        h = {"X-API-Key": "gap_sk"}
        assert c.post("/api/v1/md", json={"ids": ["x"]}, headers=h).status_code != 403  # /md 允许（404/200，非403）
        assert c.get("/api/v1/objects", headers=h).status_code == 403


def test_frontend_user_can_objects(tmp_path, monkeypatch):
    _seed(tmp_path, monkeypatch, [FE])
    from app.main import app
    with TestClient(app) as c:
        assert c.get("/api/v1/objects", headers={"X-API-Key": "gap_fe"}).status_code == 200


def test_admin_can_users(tmp_path, monkeypatch):
    _seed(tmp_path, monkeypatch, [ADMIN])
    from app.main import app
    with TestClient(app) as c:
        assert c.get("/api/v1/users", headers={"X-API-Key": "gap_admin"}).status_code == 200


def test_frontend_user_cannot_users(tmp_path, monkeypatch):
    _seed(tmp_path, monkeypatch, [FE])
    from app.main import app
    with TestClient(app) as c:
        assert c.get("/api/v1/users", headers={"X-API-Key": "gap_fe"}).status_code == 403
```

- [ ] **Step 2: 跑验证失败**

Run: `pytest tests/test_auth.py -v`
Expected: FAIL（旧中间件逻辑，新断言不通过）

- [ ] **Step 3: 重写 `app/middleware/auth.py`**

```python
"""鉴权 + 审计中间件（v2）：KEY 反查用户 → 权限校验 → 请求级打点①。

- /users/login 豁免（登录前无 user，空 users 也能调）。
- 其他 /api/*：无 KEY/未知 KEY → 401；权限不符 → 403。
- 空 users.json → 所有 /api/*（非 login）→ 401（取消旁路）。
- 打点①：鉴权通过后记一行请求级（排除 /users/login、/telemetry/*）。
- caller：X-Client:web → web；否则 skill。
"""
import logging
import urllib.parse

from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware

from .. import config
from ..telemetry.recorder import record
from ..users.service import authenticate, check_perm

logger = logging.getLogger(__name__)

# 路径 → 所需权限
def _need_perm(path: str) -> str:
    if path.startswith("/api/v1/users"):  # 用户管理（login 在外豁免）
        return "admin"
    if path in ("/api/v1/domains", "/api/v1/md"):
        return "skill"
    return "frontend"  # 其他前端用的接口


class AuthMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        path = request.url.path
        if not path.startswith("/api/"):
            return await call_next(request)
        # login 豁免
        if path == "/api/v1/users/login":
            return await call_next(request)

        key = request.headers.get("X-API-Key", "")
        user = authenticate(key) if key else None
        if user is None:
            return JSONResponse(status_code=401, content={"detail": "missing or invalid api key"})

        caller = "web" if request.headers.get("X-Client") == "web" else "skill"
        request.state.user = user["username"]
        request.state.caller = caller

        if not check_perm(user, _need_perm(path)):
            return JSONResponse(status_code=403, content={"detail": "permission denied"})

        response = await call_next(request)

        # 打点①请求级（排除 login、telemetry 自身）
        if not (path.startswith("/api/v1/telemetry")):
            try:
                id_ = _extract_id(path)
                record(path, id_=id_, type_="", user=user["username"], caller=caller, level="request")
            except Exception as e:  # 观测用，不阻断
                logger.warning("audit record failed: %s", e)
        return response


def _extract_id(path: str) -> str:
    """从 /objects/{id}* 提取 id（URL-decode）。"""
    # /api/v1/objects/{id}、/objects/{id}/neighbors、/objects/{id}/md
    if "/objects/" in path:
        rest = path.split("/objects/", 1)[1]
        id_encoded = rest.split("/", 1)[0]
        return urllib.parse.unquote(id_encoded)
    return ""
```

- [ ] **Step 4: 删 `config.API_KEY`**

`config.py` 删 `API_KEY = os.environ.get(...)` 行（及 import os 若不再用）。`auth.py` 不再引用 `config.API_KEY`（已重写）。检查 `main.py`/其他无引用。

- [ ] **Step 5: `main.py` 启动检查 users.json**

lifespan 加（建索引后）：
```python
from . import config
from pathlib import Path
if not Path(config.USERS_FILE).exists() or not _load_users_count():
    print("[startup] WARNING: users.json 不存在或为空 → 需初始化 admin（否则无法登录）", flush=True)
```
（`_load_users_count` 读 users.json 计数；或简单 `not Path.exists()`）

- [ ] **Step 6: 跑验证通过**

Run: `pytest tests/test_auth.py tests/test_users_api.py -v`
Expected: 全 PASS

- [ ] **Step 7: 回归现有 API 测试（test_api_objects 等会因需 KEY 失败）**

Run: `pytest tests/test_api_objects.py -v`
Expected: **大量失败**（现有测试不带 KEY → 401）。需给现有测试补 KEY——见 Task 8 统一处理（fixture 注入 admin KEY）。本 Task 暂不修，Task 8 补。

> **关键**：Task 5 后所有现有 API 测试需带 admin KEY。Task 8 提供共享 fixture（seed admin + 注入 X-API-Key header）。本 Task 先让 test_auth/test_users_api 通过。

- [ ] **Step 8: Commit**

```bash
git add app/middleware/auth.py app/config.py app/main.py tests/test_auth.py
git commit -m "feat(platform): auth 中间件 v2（用户+权限+打点①+login豁免+取消旁路），删API_KEY"
```

---

### Task 6: recorder 新签名（TDD）

**Files:** Modify `app/telemetry/recorder.py`, `tests/test_telemetry.py`

- [ ] **Step 1: 改 `test_telemetry.py` recorder 部分**（新签名 user/caller/level）

把 `record("/md", id, type)` 调用改为 `record("/md", id_, type_, user="u", caller="skill", level="object")`，断言行含 `user/caller/level` 字段。例如：
```python
def test_record_appends_jsonl_line(tmp_path, monkeypatch):
    f = _use_tmp_telemetry(tmp_path, monkeypatch)
    from app.telemetry.recorder import record
    record("/md", "UDG@Feature@F-1", "Feature", user="sa", caller="skill", level="object")
    rec = json.loads(f.read_text(encoding="utf-8").strip().split("\n")[0])
    assert rec["user"] == "sa" and rec["caller"] == "skill" and rec["level"] == "object"
    assert rec["endpoint"] == "/md" and rec["id"] == "UDG@Feature@F-1"
```
（其他 recorder 测试同理加 kwargs；swallows_failure 用任意 kwargs）

- [ ] **Step 2: 跑验证失败**

Run: `pytest tests/test_telemetry.py -v`
Expected: FAIL（签名不匹配）

- [ ] **Step 3: 重写 `recorder.py` 的 `record`**

```python
def record(endpoint: str, id_: str = "", type_: str = "", *, user: str = "", caller: str = "", level: str = "request") -> None:
    """追加一条访问记录。失败吞掉 + log，不抛。"""
    try:
        line = {
            "ts": datetime.now(timezone.utc).isoformat(),
            "user": user,
            "caller": caller,
            "endpoint": endpoint,
            "id": id_,
            "type": type_,
            "level": level,
        }
        path = Path(config.TELEMETRY_FILE)
        path.parent.mkdir(parents=True, exist_ok=True)
        with _lock:
            with open(path, "a", encoding="utf-8") as f:
                f.write(json.dumps(line, ensure_ascii=False) + "\n")
    except Exception as e:  # noqa: BLE001
        logger.warning("telemetry record failed: %s", e)
```

- [ ] **Step 4: 跑验证通过**

Run: `pytest tests/test_telemetry.py -v`
Expected: recorder 测试 PASS（aggregator 测试 Task 7 改）

- [ ] **Step 5: Commit**

```bash
git add app/telemetry/recorder.py tests/test_telemetry.py
git commit -m "feat(platform): recorder 新签名（user/caller/level）"
```

---

### Task 7: aggregator 改造（stats 口径 + activity + by_user，TDD）

**Files:** Modify `app/telemetry/aggregator.py`, `tests/test_telemetry.py`

- [ ] **Step 1: 改 `test_telemetry.py` aggregator 部分**

替换 v1 三维聚合测试为两个函数：
```python
def test_aggregate_stats_skill_objects_only(tmp_path, monkeypatch):
    f = _use_tmp_telemetry(tmp_path, monkeypatch)
    _seed(f, [
        {"ts": _now(), "user": "sk1", "caller": "skill", "endpoint": "/md", "id": "F@1", "type": "Feature", "level": "object"},
        {"ts": _now(), "user": "sk1", "caller": "skill", "endpoint": "/md", "id": "F@1", "type": "Feature", "level": "object"},
        {"ts": _now(), "user": "sk2", "caller": "skill", "endpoint": "/domains", "id": "BD@x", "type": "BusinessDomain", "level": "object"},
        # 下方两条不计入统计（非 skill 或 request 级）：
        {"ts": _now(), "user": "fe", "caller": "web", "endpoint": "/md", "id": "F@1", "type": "Feature", "level": "object"},
        {"ts": _now(), "user": "fe", "caller": "web", "endpoint": "/api/v1/objects/F@1/md", "id": "", "type": "", "level": "request"},
    ])
    from app.telemetry.aggregator import aggregate_stats
    r = aggregate_stats(days=30)
    assert r["total"] == 3  # 只 skill 的 3 条 object
    assert r["by_type"]["Feature"] == 2
    assert r["by_user"] == {"sk1": 2, "sk2": 1}
    assert r["top_ids"][0]["id"] == "F@1"


def test_aggregate_activity_by_user(tmp_path, monkeypatch):
    f = _use_tmp_telemetry(tmp_path, monkeypatch)
    _seed(f, [
        {"ts": _now(), "user": "fe", "caller": "web", "endpoint": "/api/v1/objects/F@1/md", "id": "F@1", "type": "", "level": "request"},
        {"ts": _now(), "user": "fe", "caller": "web", "endpoint": "/api/v1/stats", "id": "", "type": "", "level": "request"},
        {"ts": _now(), "user": "other", "caller": "web", "endpoint": "/api/v1/objects/F@2/md", "id": "F@2", "type": "", "level": "request"},
    ])
    from app.telemetry.aggregator import aggregate_activity
    r = aggregate_activity("fe", days=30)
    assert len(r) == 2  # fe 的两条
    assert all(item["endpoint"] for item in r)
```
（`_now()` = `datetime.now(timezone.utc).isoformat()`，测试顶部定义）

- [ ] **Step 2: 跑验证失败**

Run: `pytest tests/test_telemetry.py -v`
Expected: FAIL（aggregate_stats/activity 未定义）

- [ ] **Step 3: 重写 `aggregator.py`**

```python
"""打点聚合：stats（SKILL 取用，②对象级）+ activity（用户轨迹，①请求级）。"""
import json
from collections import Counter
from datetime import datetime, timedelta, timezone
from pathlib import Path

from .. import config

_STATS_ENDPOINTS = {"/md", "/domains", "/api/v1/md", "/api/v1/domains"}


def _iter_records():
    path = Path(config.TELEMETRY_FILE)
    if not path.exists():
        return
    with open(path, "r", encoding="utf-8") as f:
        for raw in f:
            raw = raw.strip()
            if not raw:
                continue
            try:
                yield json.loads(raw)
            except json.JSONDecodeError:
                continue


def _parse_ts(s):
    if not s:
        return None
    try:
        return datetime.fromisoformat(s.replace("Z", "+00:00"))
    except ValueError:
        return None


def aggregate_stats(days: int = 30) -> dict:
    """只 caller=skill + level=object + endpoint∈{/md,/domains}。返回 total/by_type/top_ids/timeline/by_user。"""
    cutoff = datetime.now(timezone.utc) - timedelta(days=days) if days > 0 else None
    by_type, by_id, id_type, by_date, by_user = Counter(), Counter(), {}, Counter(), Counter()
    for rec in _iter_records():
        if rec.get("level") != "object" or rec.get("caller") != "skill":
            continue
        if rec.get("endpoint") not in _STATS_ENDPOINTS:
            continue
        ts = _parse_ts(rec.get("ts", ""))
        if cutoff and ts and ts < cutoff:
            continue
        t, i, u = rec.get("type") or "?", rec.get("id") or "?", rec.get("user") or "?"
        by_type[t] += 1; by_id[i] += 1; id_type[i] = t; by_user[u] += 1
        if ts: by_date[ts.strftime("%Y-%m-%d")] += 1
    return {
        "total": sum(by_type.values()),
        "by_type": dict(by_type),
        "top_ids": [{"id": i, "type": id_type.get(i, "?"), "count": c} for i, c in by_id.most_common(20)],
        "timeline": [{"date": d, "count": c} for d, c in sorted(by_date.items())],
        "by_user": dict(by_user),
    }


def aggregate_activity(username: str, days: int = 30) -> list:
    """某 user 的全量请求级轨迹（level=request），按时间倒序。"""
    cutoff = datetime.now(timezone.utc) - timedelta(days=days) if days > 0 else None
    rows = []
    for rec in _iter_records():
        if rec.get("user") != username:
            continue
        ts = _parse_ts(rec.get("ts", ""))
        if cutoff and ts and ts < cutoff:
            continue
        rows.append({"ts": rec.get("ts", ""), "endpoint": rec.get("endpoint", ""), "caller": rec.get("caller", "")})
    rows.sort(key=lambda r: r["ts"], reverse=True)
    return rows
```

- [ ] **Step 4: 跑验证通过**

Run: `pytest tests/test_telemetry.py -v`
Expected: 全 PASS

- [ ] **Step 5: Commit**

```bash
git add app/telemetry/aggregator.py tests/test_telemetry.py
git commit -m "feat(platform): aggregator（stats只skill对象级+by_user / activity按user轨迹）"
```

---

### Task 8: objects.py 改造（/md /domains 对象级打点②）+ 修复现有 API 测试

**Files:** Modify `app/routers/objects.py`, `tests/test_api_objects.py`（+ conftest 共享 fixture）

- [ ] **Step 1: 加共享 fixture（conftest.py）注入 admin KEY**

在 `tests/conftest.py` 加：
```python
@pytest.fixture
def admin_client(tmp_path, monkeypatch):
    """seed 一个 admin 到 tmp users.json，返回 (TestClient, admin_key)——供需登录的 API 测试。"""
    import json
    import app.config as cfg
    monkeypatch.setattr(cfg, "USERS_FILE", tmp_path / "users.json")
    (tmp_path / "users.json").write_text(json.dumps({"users": [
        {"username": "admin", "key": "gap_test_admin", "can_frontend": True, "can_skill": True, "is_admin": True}
    ]}), encoding="utf-8")
    from app.main import app
    from fastapi.testclient import TestClient
    with TestClient(app) as c:
        yield c, "gap_test_admin"
```

> 现有 `test_api_objects.py` 等用 `_setup` 构造图谱数据 + `with TestClient(app) as c`。需给这些 `c.get/post` 加 `headers={"X-API-Key": "gap_test_admin"}` 并 seed 该 admin。最简：在每个 `_setup` 里同时 seed admin（或用 `admin_client` fixture）。实现期统一改造（工作量大但机械）。

- [ ] **Step 2: 改 `objects.py` 的 `/md`、`/domains` handler**

两个 handler 加 `request: Request` 参数；`record(...)` 调用改：
```python
from fastapi import APIRouter, HTTPException, Query, Request
# ...

@router.post("/domains")
def list_domains_with_md(request: Request):
    # ... 原逻辑 ...
    for item in out:
        record("/domains", item["id"], "BusinessDomain",
               user=request.state.user, caller=request.state.caller, level="object")
    return out

@router.post("/md")
def batch_md(req: BatchMdRequest, request: Request):
    # ... 原逻辑 ...
        out[id_] = {"version": obj.version, "md": obj.raw_md}
        record("/md", id_, obj.type,
               user=request.state.user, caller=request.state.caller, level="object")
    return out
```

- [ ] **Step 3: 改 `test_api_objects.py`** —— 所有 `c.get/post` 加 admin KEY header + `_setup` seed admin

在 `_setup` 末尾（或 fixture）seed admin 到 tmp users.json；所有 API 调用加 `headers={"X-API-Key": "gap_test_admin"}`。埋点测试断言 jsonl 行含 `user/caller/level=object`。

- [ ] **Step 4: 跑全量后端回归**

Run: `pytest tests/ -v`
Expected: 全 PASS（含改后的 test_api_objects、test_auth、test_telemetry、test_users_*）

- [ ] **Step 5: Commit**

```bash
git add app/routers/objects.py tests/test_api_objects.py tests/conftest.py
git commit -m "feat(platform): /md /domains 对象级打点②(user/caller) + 现有API测试补admin KEY"
```

---

### Task 9: users activity 接口 + telemetry stats 口径 + main 注册 + 启动检查

**Files:** Modify `app/routers/users.py`, `app/routers/telemetry.py`

- [ ] **Step 1: users.py 加 activity 端点**

```python
from ..telemetry.aggregator import aggregate_activity

@router.get("/users/{username}/activity")
def user_activity(username: str, days: int = 30):
    """该用户行为轨迹（需 is_admin，中间件校验）。"""
    return aggregate_activity(username, days)
```

- [ ] **Step 2: telemetry.py stats 改用 aggregate_stats**

```python
from ..telemetry.aggregator import aggregate_stats

@router.get("/telemetry/stats")
def telemetry_stats(days: int = Query(default=30, ge=1, le=365)):
    return aggregate_stats(days)
```

- [ ] **Step 3: 加 activity 接口测试**（`tests/test_users_api.py`）

```python
def test_admin_can_view_activity(tmp_path, monkeypatch):
    _seed_users(tmp_path, monkeypatch, [ADMIN])
    from app.main import app
    with TestClient(app) as c:
        r = c.get("/api/v1/users/admin/activity?days=7", headers={"X-API-Key": "gap_admin"})
        assert r.status_code == 200
        assert isinstance(r.json(), list)
```

- [ ] **Step 4: 跑全量回归**

Run: `pytest tests/ -v`
Expected: 全 PASS

- [ ] **Step 5: Commit**

```bash
git add app/routers/users.py app/routers/telemetry.py tests/test_users_api.py
git commit -m "feat(platform): users activity 轨迹接口 + telemetry stats 改 aggregate_stats"
```

---

## Chunk 3: 前端 + 收尾

> 前端无单测，每 Task 用 `npm run build` + 浏览器验证。命令在 `frontend/` 下。

### Task 10: auth.ts + LoginView（用户名+KEY）

**Files:** Modify `src/auth.ts`, `src/views/LoginView.vue`

- [ ] **Step 1: 改 `auth.ts`**（存 {username,key,is_admin} + getUser/logout）

```typescript
const SESSION = 'gap_session'

export interface Session { username: string; key: string; is_admin: boolean }

export function getSession(): Session | null {
  const raw = sessionStorage.getItem(SESSION)
  return raw ? JSON.parse(raw) : null
}
export function setSession(s: Session): void { sessionStorage.setItem(SESSION, JSON.stringify(s)) }
export function clearSession(): void { sessionStorage.removeItem(SESSION) }
export function getKey(): string { return getSession()?.key || '' }
export function isAdmin(): boolean { return !!getSession()?.is_admin }
```
（`api.ts`/`tests-module/api.ts` 里 `getKey` 仍可用；`hasKey` → `!!getSession()`）

- [ ] **Step 2: 改 `LoginView.vue`**（用户名+KEY 两字段，调 `/users/login`）

```vue
<template>
  <div class="login-page">
    <form class="login-card" @submit.prevent="onSubmit">
      <h1 class="title">图谱资产</h1>
      <input v-model="username" class="input" placeholder="用户名" autofocus />
      <input v-model="key" type="password" class="input" placeholder="API Key" autocomplete="current-password" />
      <div v-if="err" class="err">{{ err }}</div>
      <button type="submit" class="btn" :disabled="loading || !username.trim() || !key.trim()">
        {{ loading ? '验证中…' : '进入' }}
      </button>
    </form>
  </div>
</template>
<script setup lang="ts">
import { ref } from 'vue'
import { setSession, type Session } from '../auth'
import { login } from '../api'
const username = ref(''); const key = ref(''); const err = ref(''); const loading = ref(false)
async function onSubmit() {
  loading.value = true; err.value = ''
  try {
    const u = await login(username.value.trim(), key.value.trim())
    setSession({ username: u.username, key: key.value.trim(), is_admin: u.is_admin } as Session)
    window.location.assign('/')
  } catch (e) { err.value = (e instanceof Error ? e.message : '登录失败') }
  finally { loading.value = false }
}
</script>
```
（样式沿用 v1 `.login-page/.login-card/.input/.btn/.err`）

- [ ] **Step 3: `api.ts` 加 `login`**

```typescript
export const login = (username: string, key: string): Promise<{ username: string; is_admin: boolean }> =>
  _req<{ username: string; is_admin: boolean }>(`${BASE}/users/login`, {
    method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ username, key }),
  })
```

- [ ] **Step 4: build + Commit**

Run: `npm run build` → 构建成功
```bash
git add src/auth.ts src/views/LoginView.vue src/api.ts
git commit -m "feat(platform): 登录页用户名+KEY（/users/login）+ session{username,key,is_admin}"
```

---

### Task 11: _req 加 X-Client:web + 403 分流

**Files:** Modify `src/api.ts`, `src/tests-module/api.ts`

- [ ] **Step 1: 两个 `_req` 加 `X-Client: web` + 403 提示**

在 `_req` 的 header 设置后加 `headers.set('X-Client', 'web')`；401 分支保留；403 分支：
```typescript
if (resp.status === 403) {
  ElMessage?.error('权限不足')  // 或 throw 带 status，调用方处理
  throw Object.assign(new Error('权限不足'), { status: 403 })
}
```
（Element Plus `ElMessage` 已在项目用；或简单 throw，调用方 catch 提示。实现期统一。）

- [ ] **Step 2: `tests-module/api.ts` 同样加 `X-Client: web`**

import 改 `import { getKey, clearSession } from '../auth'`（getSdk 改 getSession().key）。

- [ ] **Step 3: build + Commit**

```bash
git add src/api.ts src/tests-module/api.ts
git commit -m "feat(platform): _req 加 X-Client:web + 403 权限不足提示"
```

---

### Task 12: UsersView + router + AppHeader（用户管理菜单）

**Files:** Create `src/views/UsersView.vue`; Modify `src/router.ts`, `src/components/AppHeader.vue`; `src/api.ts` 加用户 CRUD 函数

- [ ] **Step 1: `api.ts` 加用户管理函数**

```typescript
export interface UserRow { username: string; key: string; can_frontend: boolean; can_skill: boolean; is_admin: boolean }
export const listUsers = (): Promise<UserRow[]> => _req(`${BASE}/users`)
export const createUser = (b: { username: string; can_frontend?: boolean; can_skill?: boolean; is_admin?: boolean }): Promise<UserRow> =>
  _req(`${BASE}/users`, { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(b) })
export const updateUser = (name: string, b: Record<string, unknown>): Promise<UserRow> =>
  _req(`${BASE}/users/${encodeURIComponent(name)}`, { method: 'PATCH', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(b) })
export const deleteUser = (name: string): Promise<{ ok: boolean }> =>
  _req(`${BASE}/users/${encodeURIComponent(name)}`, { method: 'DELETE' })
export const userActivity = (name: string, days = 30): Promise<{ ts: string; endpoint: string }[]> =>
  _req(`${BASE}/users/${encodeURIComponent(name)}/activity?days=${days}`)
```

- [ ] **Step 2: `UsersView.vue`**（用户列表表格 + 新建对话框（勾权限+生成key）+ 删除 + 看轨迹抽屉）

骨架（完整实现含 Element Plus `el-table/el-dialog/el-checkbox`）：
```vue
<template>
  <div class="users-page">
    <header class="page-head"><h1>用户管理</h1>
      <el-button type="primary" @click="showCreate = true">+ 新建用户</el-button>
    </header>
    <el-table :data="users" v-loading="loading">
      <el-table-column prop="username" label="用户名" />
      <el-table-column prop="key" label="API Key" #default="{ row }">
        <code>{{ row.key }}</code> <el-button link size="small" @click="copy(row.key)">复制</el-button>
      </el-table-column>
      <el-table-column label="权限" #default="{ row }">
        <el-tag v-if="row.is_admin">admin</el-tag>
        <el-tag v-if="row.can_frontend" type="success">前端</el-tag>
        <el-tag v-if="row.can_skill" type="warning">SKILL</el-tag>
      </el-table-column>
      <el-table-column label="操作" #default="{ row }">
        <el-button link size="small" @click="viewActivity(row)">轨迹</el-button>
        <el-button link size="small" @click="togglePerm(row)">改权限</el-button>
        <el-button link size="small" type="danger" @click="del(row)" :disabled="row.username === 'admin'">删除</el-button>
      </el-table-column>
    </el-table>
    <!-- 新建/改权限对话框 + 轨迹抽屉（el-dialog / el-drawer）省略，实现期补全 -->
  </div>
</template>
<script setup lang="ts">
import { onMounted, ref } from 'vue'
import { listUsers, createUser, deleteUser, userActivity, type UserRow } from '../api'
const users = ref<UserRow[]>([]); const loading = ref(false); const showCreate = ref(false)
async function load() { loading.value = true; users.value = await listUsers(); loading.value = false }
function copy(k: string) { navigator.clipboard.writeText(k) }
async function del(u: UserRow) { await deleteUser(u.username); await load() }
async function viewActivity(u: UserRow) { const rows = await userActivity(u.username); console.log(rows) /* → 抽屉 */ }
onMounted(load)
</script>
```

- [ ] **Step 3: `router.ts` 加 `/users`（守卫 is_admin）**

```typescript
import { getSession } from './auth'
// routes 加：
{ path: '/users', name: 'users', component: () => import('./views/UsersView.vue') }
// 守卫改：
router.beforeEach((to) => {
  const s = getSession()
  if (to.name === 'login') return true
  if (!s) return { name: 'login' }
  if (to.name === 'users' && !s.is_admin) return false  // 非 admin 拒绝
  return true
})
```

- [ ] **Step 4: `AppHeader.vue` 加「用户」菜单（仅 is_admin）**

tabs 改为计算属性，仅 `isAdmin()` 时含 `{ to: '/users', label: '用户' }`：
```typescript
import { getSession } from '../auth'
const tabs = computed(() => {
  const t = [/* 图谱浏览/统计/上传/测试 */]
  if (getSession()?.is_admin) t.splice(4, 0, { to: '/users', label: '用户', icon: UserIcon })
  return t
})
```

- [ ] **Step 5: build + 手动验证（admin 登录见「用户」菜单，建用户/看轨迹）+ Commit**

```bash
git add src/views/UsersView.vue src/router.ts src/components/AppHeader.vue src/api.ts
git commit -m "feat(platform): 用户管理菜单（admin，CRUD+轨迹）"
```

---

### Task 13: TelemetrySection 加 by_user 区块

**Files:** Modify `src/components/TelemetrySection.vue`, `src/api.ts`（TelemetryStats 加 by_user）

- [ ] **Step 1: `api.ts` TelemetryStats 加 by_user**

```typescript
export interface TelemetryStats {
  total: number; by_type: Record<string, number>
  top_ids: { id: string; type: string; count: number }[]
  timeline: { date: string; count: number }[]
  by_user: Record<string, number>  // 新增
}
```

- [ ] **Step 2: `TelemetrySection.vue` 加「按用户」区块 + 标题改「SKILL 取用频次」**

在 ts-grid 加一个 block：
```html
<div class="ts-block">
  <div class="block-title">按用户（SKILL）</div>
  <div class="type-rows">
    <div v-for="(c, u) in stats.by_user" :key="u" class="type-row">
      <span class="type-label">{{ u }}</span>
      <span class="type-count mono">{{ c }}</span>
    </div>
  </div>
</div>
```
标题 `知识取用频次` → `SKILL 取用频次`；副标题加「（只统计 SKILL 的 /domains+/md）」。

- [ ] **Step 3: build + Commit**

```bash
git add src/components/TelemetrySection.vue src/api.ts
git commit -m "feat(platform): 统计页加「按用户」区块（by_user）+ 标题改 SKILL 取用频次"
```

---

### Task 14: 初始 admin + .gitignore + README + E2E

**Files:** Create `platform-data/users.json`; Modify `.gitignore`, `README.md`

- [ ] **Step 1: 生成初始 admin 的 users.json**（不入 git）

```bash
cd graph-asset-platform/backend && python -c "
import secrets, json
from pathlib import Path
key = 'gap_' + secrets.token_hex(16)
Path('../platform-data/users.json').write_text(json.dumps({'users':[{
  'username':'admin','key':key,'can_frontend':True,'can_skill':True,'is_admin':True,
  'created_at':'2026-07-24T00:00:00+00:00'}]}, ensure_ascii=False, indent=2), encoding='utf-8')
print('初始 admin KEY:', key)
"
```
> **把打印的 KEY 交给用户**（这是 admin 登录凭证）。

- [ ] **Step 2: `.gitignore` 加 users.json**

```
platform-data/users.json
```
（`platform-data/` 已整体忽略，此行显式注明 users.json 含明文 KEY）

- [ ] **Step 3: README 更新启动说明**

启动命令去掉 `GAP_API_KEY`（v2 不再用），改为：首次需 `platform-data/users.json` 存在（初始 admin KEY 见交付）；登录页输入用户名（admin）+ KEY。SKILL 调用带 `X-API-Key: <用户KEY>`（无 `X-Client`）。

- [ ] **Step 4: E2E 验证**

启动后端（无需 KEY env）+ 前端 build：
```bash
cd graph-asset-platform/backend && python -m uvicorn app.main:app --port 8000
```
curl 矩阵：
```bash
# login（公开）
curl -s -X POST http://localhost:8000/api/v1/users/login -H "Content-Type: application/json" -d '{"username":"admin","key":"<初始KEY>"}'
# admin 建 SKILL 用户
curl -s -X POST http://localhost:8000/api/v1/users -H "X-API-Key: <初始KEY>" -H "Content-Type: application/json" -d '{"username":"sa1","can_skill":true}'
# SKILL 用户调 /md（带其 KEY，无 X-Client）
curl -s -X POST http://localhost:8000/api/v1/md -H "X-API-Key: <sa1的KEY>" -H "Content-Type: application/json" -d '{"ids":["<某真实id>"]}'
# SKILL 用户调 /objects → 403
curl -s -o /dev/null -w "%{http_code}\n" http://localhost:8000/api/v1/objects -H "X-API-Key: <sa1的KEY>"
# admin 看取用统计（应含 by_user）
curl -s http://localhost:8000/api/v1/telemetry/stats?days=7 -H "X-API-Key: <初始KEY>"
# admin 看某用户轨迹
curl -s http://localhost:8000/api/v1/users/admin/activity?days=7 -H "X-API-Key: <初始KEY>"
```
浏览器：登录（admin+KEY）→ 见「用户」菜单 → 建 SKILL 用户 → 统计页看「按用户」区块 → 点用户看轨迹。

- [ ] **Step 5: 隔离核查 + 最终 Commit**

```bash
git diff master -- graph-asset-platform/backend/app/service.py graph-asset-platform/backend/app/index.py graph-asset-platform/backend/app/store.py graph-asset-platform/backend/app/edges.py graph-asset-platform/backend/app/models.py graph-asset-platform/backend/app/bundle.py graph-asset-platform/backend/app/tests/
# 期望空 diff（隔离达标）
git add .gitignore README.md
git commit -m "chore(platform): 初始admin users.json + .gitignore + README（v2用户体系）"
```

---

## 完成标准

- [ ] 后端 `pytest tests/ -v` 全 PASS（含新 test_users_*、改后的 test_auth/test_telemetry/test_api_objects）
- [ ] 前端 `npm run build` 无类型错误
- [ ] 鉴权矩阵：无/错 KEY→401；can_skill 只 /domains//md（其他 403）；can_frontend 前端全访问；is_admin 用户管理
- [ ] login 公开豁免；空 users.json → 非login 全 401
- [ ] 打点①全量（轨迹）+ ②对象级（/md//domains，统计）；统计只 skill+object，含 by_user
- [ ] 前端：登录（用户名+KEY）、用户管理菜单（admin，CRUD+轨迹）、统计页 by_user
- [ ] 初始 admin KEY 交付用户；users.json 不入 git
- [ ] 隔离：图谱 service/index/store + app/tests/ 零改动
