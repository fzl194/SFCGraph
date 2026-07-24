# 用户体系 + 权限 + 审计打点 设计（graph-asset-platform）

> 日期：2026-07-24
> 范围：`graph-asset-platform/`（后端 FastAPI + 前端 Vue3）。在 v1「单一 KEY 门禁 + 打点」基础上升级为多用户 + 权限分级 + 全量审计打点。
> 前序：`docs/superpowers/specs/2026-07-23-auth-and-telemetry-design.md`（v1，本次多处反转其决策）。
> 状态：设计中（待 spec 审查 → 用户复核 → writing-plans）

---

## 1. 背景：为什么升级

v1（单一 `GAP_API_KEY`）上线后发现需要：
- 区分「谁」在访问（SKILL 调用按用户级别统计）；
- 前端访问要有身份（不能裸 KEY）；
- admin 能发 KEY、授予权限给不同人/不同 SKILL；
- 全量审计「谁在什么时候访问/操作了什么」（运营/审计需要）。

**v1 → v2 决策反转**（明确记录，避免混淆）：

| 维度 | v1 | v2（本次） |
|---|---|---|
| 鉴权 | 单一 `GAP_API_KEY`（env） | 多用户（`users.json`，每用户独立明文 KEY） |
| 权限 | 无（有 KEY 即全权） | `can_frontend` / `can_skill` / `is_admin` 三 flag |
| 未配 KEY | 旁路（开发放行） | **取消旁路**（空用户表拒绝所有，必须初始化 admin） |
| 打点范围 | 只 `/domains`+`/md` | **全量 `/api/*`**（前端 + SKILL） |
| caller | 砍掉 | **恢复**（`web`/`skill`，前端带 `X-Client:web`） |
| 统计口径 | `/domains`+`/md` | **不变**（仍只 SKILL 的 `/domains`+`/md`），补 `by_user` |
| 轨迹 | 无 | **新增**（admin 看某用户全量行为时间线） |

---

## 2. 现状（已核实）

- `app/middleware/auth.py`：单一 KEY（`config.API_KEY`），未配旁路。
- `app/telemetry/recorder.py`：`record(endpoint, id_, type_)` 写 `{ts,endpoint,id,type}`。
- `app/telemetry/aggregator.py`：聚合三维（by_type/top_ids/timeline）。
- 打点调用点：仅 `routers/objects.py` 的 `/domains`、`/md` 末尾 `record()`。
- 前端 `LoginView.vue`：单 KEY 字段；`auth.ts` 存 `gap_api_key`；两个 `_req`（`api.ts`+`tests-module/api.ts`）带 `X-API-Key`，401 跳登录。
- 36 个 `/api/v1/*` 端点（详见 §6 接口清单）。

---

## 3. 需求（用户确认）

1. 用户名 + 明文 KEY（每用户独立），前端登录后才允许访问。
2. 权限分级：前端访问需管理员级（`can_frontend`）；SKILL 调用是用户级（`can_skill`，只能 `/domains`+`/md`）；SKILL 接口形态不变（仍只带 KEY header）。
3. admin 超管：创建用户、自动生成 KEY、授予 `can_frontend`/`can_skill` 权限。
4. 打点按用户粒度（username / key 全局唯一，按 username 记）。
5. 前端全量打点（用户行为轨迹，每次访问都记）——运营数据。
6. SKILL 打点按用户级别。
7. **统计仍只关注 SKILL 的 `/domains`+`/md`**（加 `by_user`）；用户轨迹只给 admin 看，不参与统计。

---

## 4. 设计

### 4.1 用户体系

**存储**：`platform-data/users.json`（**不入 git**，含明文 KEY），结构：
```json
{
  "users": [
    {"username":"admin","key":"明文KEY","can_frontend":true,"can_skill":true,"is_admin":true,"created_at":"2026-07-24T..."},
    {"username":"sa-zhang","key":"明文KEY","can_frontend":false,"can_skill":true,"is_admin":false,"created_at":"..."}
  ]
}
```
- `username` 全局唯一；`key` 全局唯一（随机生成，如 `gap_<32hex>`），明文存。
- **初始 admin**：实现时预置到 `users.json`（username=admin，随机 KEY，三 flag 全 true），KEY 交付用户。无 bootstrap 自动逻辑；新环境部署需手动创建该文件（README 注明）。
- 新模块 `app/users/`：
  - `store.py`：读写 `users.json`（进程内 `threading.Lock` 串行写；读返回用户列表/单用户/按 key 反查）。
  - `service.py`：`create_user / update_user / delete_user / gen_key / authenticate(key)→user / check_perm(user, need)`。
  - `gen_key()`：`secrets.token_hex(16)` 前缀 `gap_`；若与现有 key 撞（概率极低）则重试。

### 4.2 鉴权与权限校验（改造 `app/middleware/auth.py`）

中间件对每个 `/api/*` 请求：
1. 取 `X-API-Key` header → `authenticate(key)` 反查用户；**找不到 → 401**。
2. **取消旁路**：`users.json` 空/不存在 → 所有 `/api/*` 返 401 + 提示「需初始化 admin」（非 `/api/` 路径不拦截）。
3. **caller 判定**：`X-Client: web` header 存在 → `caller="web"`；否则 `caller="skill"`。
4. 把 `user`、`caller` 挂到 `request.state.user` / `request.state.caller`（供打点/router 用）。
5. **权限规则**（不符 → 403 `{detail:"permission denied"}`）：

| 请求 | 所需权限 |
|---|---|
| `POST /domains`、`POST /md` | `can_skill` 或 `can_frontend` 或 `is_admin` |
| 其他 `/api/*`（前端用的：`/objects*`、`/tests/*`、`/import*`、`/export`、`/stats`、`/names`、`/subgraph`、`/telemetry/stats`） | `can_frontend` 或 `is_admin` |
| `/users/*`（用户管理 + 轨迹） | `is_admin` |
| `can_skill` 用户调非 `/domains`/`/md` | **403** |

> SKILL 调用形态不变：只带 `X-API-Key`（无 `X-Client`）→ `caller="skill"`，走 `can_skill` 规则。
> **豁免**：`POST /api/v1/users/login` **跳过鉴权与打点**（登录前无 user；空 `users.json` 也能登录完成 bootstrap）。
> **规则优先级**：`/domains`、`/md` 走第 1 行（需 `can_skill`/`can_frontend`/`is_admin` 任一），优先于第 2 行「其他 `/api/*` 需 `can_frontend`」。

### 4.3 前端登录（改造 `LoginView.vue` + `auth.ts`）

- 登录页两字段：**用户名 + KEY** → 后端 `POST /users/login`（见 §4.5）校验 `username+key` 匹配且 `can_frontend` → 200 返用户信息（含 `is_admin`）→ 前端 `sessionStorage` 存 `{username, key, is_admin}`。
- 401（KEY/用户名错）/ 403（无 `can_frontend`）→ 登录页提示。
- 两个 `_req` 带 `X-API-Key` + `X-Client: web`；401 清 session 跳登录；403 提示「权限不足」。

### 4.4 打点（全量审计，两层）

**一个 jsonl**：`platform-data/telemetry/access.jsonl`（不入 git），两种记录用字段区分：

**① 请求级（中间件记，全量轨迹）**——每个 `/api/*`（排除 `/telemetry/*` 自身避免自循环）一条：
```json
{"ts":"...","user":"sa-zhang","caller":"web","endpoint":"/api/v1/objects/UDG@Feature@GWFD-020351/md","level":"request"}
```

**② 对象级（router 记，统计用）**——仅 `/domains`、`/md`，每个成功 id 一条（v1 已有，加 `user`/`caller`，从 `request.state` 取）：
```json
{"ts":"...","user":"sa-zhang","caller":"skill","endpoint":"/md","id":"UDG@Feature@GWFD-020351","type":"Feature","level":"object"}
```

- 中间件记①在鉴权通过后、`call_next` 后（响应完成再记，含状态）；router 内记②不变。
- 失败吞掉（`record` 内 try/except），绝不阻断业务。
- `id/type` 提取：① 对 `/objects/{id}*` 从 path 提取 `id`（`type` 不填，轨迹不关心 type）；② 由 router 已 resolve 的 `obj.type` 提供。
- `/md`、`/domains` 请求**同时产生**①（一条请求级）+ ②（N 条对象级）。统计只看②，轨迹看①（或①+②，见 §4.6）。
- **`record()` 统一签名**（①②共用，新增 kwargs）：`record(endpoint, id_="", type_="", *, user, caller, level)`。① 传 `level="request"`（`id_` = path 解析值或空、`type_=""`）；② 传 `level="object"`（`id_`/`type_` 由 router 提供）。
- **① 排除**：`/users/login`（登录前无 user）+ `/telemetry/*`（自循环）。
- **① path 提取 `id`**：`/objects/{id}*` 从 URL-decode 后的 path 正则提取（id 含 `@`/空格，须先 decode）。

### 4.5 接口（改造 + 新增）

**新增 `routers/users.py`**（admin）：
| 端点 | 用途 | 权限 |
|---|---|---|
| `POST /users/login` | 登录校验（username+key→用户+is_admin），**不要求登录**（登录用） | 公开 |
| `GET /users` | 用户列表（含 key 明文，admin 复制分配） | `is_admin` |
| `POST /users` | 建用户（username + 勾权限 → 自动 gen key → 返 key） | `is_admin` |
| `PATCH /users/{username}` | 改权限 / 重置 key | `is_admin` |
| `DELETE /users/{username}` | 删用户 | `is_admin` |
| `GET /users/{username}/activity?days=30` | 该用户行为轨迹（① 请求级记录时间线） | `is_admin` |

**改造 `routers/telemetry.py`**：
- `GET /telemetry/stats?days=30` 聚合口径改为：**只 `level=object` 且 `caller=skill` 且 `endpoint in (/domains,/md)`** 的记录，聚合 `{total, by_type, top_ids, timeline, by_user}`。`by_user` 新增：`{username: count}`。

**`routers/objects.py`**：`/domains`、`/md` handler 加 `request: Request` 参数（FastAPI 自动注入），从 `request.state.user`/`request.state.caller` 取值传给 `record(..., level="object")`。

**`config.py`**：新增 `USERS_FILE = DATA_DIR / "users.json"`；**删除** `API_KEY` 字段（v1 单一 KEY，v2 不再用；`auth.py` 中对 `config.API_KEY` 的引用一并清除）。

**`main.py`**：注册 `users_router`；启动时检查 `users.json`，空/不存在 → 打 WARNING「未初始化 admin，请创建 users.json」。

### 4.6 统计 vs 轨迹（口径严格分开）

| 视角 | 数据源 | 内容 | 受众 |
|---|---|---|---|
| **取用频次** `/telemetry/stats` | ② 对象级 + `caller=skill` + `/domains`/`/md` | by_type / top_ids / timeline / **by_user** | 统计页（所有人可见） |
| **用户轨迹** `/users/{name}/activity` | ① 请求级（全量该 user 的访问） | 时间线（ts + endpoint） | admin（用户管理页点用户） |

> 轨迹**不**参与取用频次统计；取用频次**只**反映 SKILL 取知识。

---

## 5. 前端落点

| 文件 | 改动 |
|---|---|
| `src/auth.ts` | 存 `{username, key, is_admin}`；提供 `getUser()/logout()`（非单 key） |
| `src/views/LoginView.vue` | 用户名 + KEY 两字段；登录调 `POST /users/login` |
| `src/api.ts` + `tests-module/api.ts` | `_req` 加 `X-Client: web`；401/403 分流 |
| `src/components/TelemetrySection.vue` | 加「按用户」区块（`by_user`）；标题改「SKILL 取用频次」 |
| `src/views/UsersView.vue`（新） | 用户列表 + 创建（生 KEY/勾权限） + 删除 + 看轨迹 |
| `src/router.ts` | `+ /users` 路由；守卫：无 session 跳登录；`/users` 仅 `is_admin` |
| `src/components/AppHeader.vue` | 新增「用户」菜单项（仅 `is_admin` 可见） |

---

## 6. 接口清单（36 个，分类备查）

- **A 内容访问**（7）：`GET /objects`、`/objects/{id}`、`/objects/{id}/neighbors`、`/objects/{id}/md`、`/subgraph`、`POST /domains`、`POST /md`
- **B 高频元数据**（4）：`GET /names`、`/stats`、`/tests/stats`、`/telemetry/stats`
- **C 测试操作**（21）：`/tests/cases*`、`/tests/runs*`、`/tests/reviews*`、`/tests/reindex`（GET/POST/PATCH/DELETE）
- **D 资产管理**（5）：`POST /import`、`GET /import/jobs*`、`/imports`、`/export`

> 全部进①请求级打点（轨迹）；仅 A 中的 `POST /domains`+`POST /md` 进②对象级打点（统计）。

---

## 7. 隔离与文件清单

**隔离红线**：不动图谱资产解析/索引（`service.py`/`index.py`/`store.py`/`edges.py`/`models.py`/`bundle.py`）+ 测试子系统源码（`app/tests/`）。鉴权/打点/用户管理均为新增或中间件/router 末尾改动。

| 类型 | 路径 |
|---|---|
| 后端新增 | `app/users/{__init__,store,service}.py`、`routers/users.py` |
| 后端改动 | `middleware/auth.py`（KEY→用户→权限+打点①，取消旁路）、`telemetry/recorder.py`（加 user/caller/level 字段）、`telemetry/aggregator.py`（skill 过滤+by_user）、`routers/objects.py`（record 传 user/caller）、`routers/telemetry.py`（stats 口径+by_user）、`config.py`（+USERS_FILE）、`main.py`（+users router+启动检查） |
| 前端新增 | `views/UsersView.vue` |
| 前端改动 | `auth.ts`、`LoginView.vue`、`api.ts`、`tests-module/api.ts`、`TelemetrySection.vue`、`router.ts`、`AppHeader.vue` |
| 数据 | `platform-data/users.json`（初始 admin，**不入 git**）、`.gitignore`（+users.json） |

---

## 8. 环境变量

| 变量 | 说明 |
|---|---|
| （无新增） | 取消 `GAP_API_KEY`（v1 单一 KEY，v2 不再用）。初始 admin 直接写 `users.json`。 |

> `users.json` 不入 git（明文 KEY）。新环境部署需手动创建 + 写初始 admin（README 注明；或提供 `python -m app.users.bootstrap` 辅助命令——可选，非必须）。

---

## 9. 测试要点（实现阶段覆盖）

- **用户 CRUD**：建用户返 key、key 唯一、改权限生效、删用户。
- **鉴权矩阵**：
  - 无 key → 401；错 key → 401
  - `can_skill` 用户：`/md` 200、`/objects` 403
  - `can_frontend` 用户：`/objects` 200、`/md` 200（前端也能调）、`/users` 403
  - `is_admin`：`/users` 200
  - 空 `users.json` → 所有 `/api/*` 401
- **打点**：前端 `/objects/{id}/md` → ①一条（user/caller=web）；SKILL `/md` 3 ids → ①一条 + ②三条（caller=skill）。
- **统计**：`/telemetry/stats` 只算②+skill：前端调 `/md`（caller=web）不计入；SKILL 调计入 + `by_user` 正确。
- **轨迹**：`/users/{name}/activity` 返该 user 的①全量时间线；非 admin 调 → 403。
- **隔离**：`git diff` 确认图谱 service/index + `app/tests/` 零改动。

---

## 10. 非目标（YAGNI）

- ❌ KEY 哈希存储（明文，admin 要能看/复制分配）
- ❌ 用户自助改 KEY / 改密码（KEY 是 admin 发的工作令牌）
- ❌ 密码登录（KEY 即凭证）
- ❌ JWT / session token（sessionStorage 存 KEY 即可，够用）
- ❌ 用户分组 / 细粒度资源权限（只有三个 flag）
- ❌ 轨迹参与取用频次统计（严格分开）

---

## 11. 风险与权衡

| 风险 | 应对 |
|---|---|
| `users.json` 并发写（多 admin 同时操作） | 进程内 `threading.Lock` 串行写；单进程部署够用 |
| 明文 KEY 泄漏 | `users.json` 入 `.gitignore`；内网受控环境；KEY 可由 admin 重置 |
| 打点 jsonl 膨胀（全量前端请求） | 接受（审计需要）；后续可加滚动/按天分文件（本 spec 不做） |
| `/md` 请求级① + 对象级②双记 | 设计如此（①轨迹/②统计分开），jsonl 体积可接受 |
| 取消旁路影响开发 | 开发时预置 admin 到 `users.json`（KEY 已知）；或测试用 tmp users.json |
| caller 误归属（手 curl 漏带 `X-Client`） | 归为 `skill`；无提权（`/domains`/`/md` 本就允许 skill），仅统计归属偏差，可接受 |
