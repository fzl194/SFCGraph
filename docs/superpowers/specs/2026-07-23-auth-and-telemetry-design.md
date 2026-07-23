# 鉴权 + 运营打点 设计（graph-asset-platform）

> 日期：2026-07-23
> 范围：`graph-asset-platform/`（后端 FastAPI + 前端 Vue3）。临时增量，不引数据库，不改图谱资产解析/索引逻辑。
> 状态：设计中（待 spec 审查 → 用户复核 → writing-plans）

---

## 1. 背景与目标

平台当前**零鉴权**（`main.py` CORS 全开、无任何身份校验），且无任何取用统计。两件事要补：

1. **鉴权**：平台要对外开放/跨网段使用，不能裸跑。两类调用方都要受控——
   - 前端（人通过浏览器访问）
   - SKILL（Agent 通过 `图谱接口.md` 的两个端点程序化访问）
2. **运营打点**：回答"SA 跑配置生成时，图谱里**哪些知识被取了、取了多少次、什么最热、趋势如何**"——这是数据飞轮里"知识被消费"的度量，给运营/领导看。

### 非目标（YAGNI，明确不做）

- ❌ 多用户体系 / 区分"哪个人"在访问（统一一把 KEY，不区分人）
- ❌ web 浏览打点（只记录 SKILL 程序化取用，人工浏览不入统计，避免噪声）
- ❌ caller（web vs SKILL）维度——经分析，前端不调打点接口，该维度恒空，砍掉
- ❌ 数据库（打点走 jsonl 文件，沿用平台 md-only/no-DB 约束）
- ❌ 图表库（前端用 CSS 横条 + SVG 折线，零依赖）

---

## 2. 现状（已核实）

| 事实 | 来源 |
|---|---|
| Agent 两个端点：`GET /domains`（Phase0 入口）+ `POST /md`（批量取 md 主力） | `三层图谱构建规范/skill/图谱接口.md` |
| 前端**不调** `/domains`、**不调** `/md`（纯 Agent 接口） | grep `frontend/src` |
| 前端请求统一走两个 `_req` 封装：`api.ts`、`tests-module/api.ts` | 同上 |
| `main.py` 零鉴权、CORS `allow_origins=["*"]`；前后端同源（后端托管 `dist`，前端走相对路径 `/api/v1`） | `main.py`、`api.ts` |
| `config.py` 只有路径常量，不读环境变量 | `config.py` |
| 顶部菜单 4 个 tab：图谱浏览 / 统计 / 上传 / 测试 | `AppHeader.vue`、`router.ts` |

---

## 3. 需求（三项）

### 3.1 双轨鉴权（单一共享 KEY）

- 一把 KEY，存环境变量 `GAP_API_KEY`。
- **前端**：首屏登录页输入 KEY → `sessionStorage` → 两个 `_req` 自动带 `X-API-Key` header → 收 401 清 KEY 跳登录。
- **SKILL**：从环境变量读同一把 KEY，curl 加 `-H "X-API-Key: $GAP_API_KEY"`。
- 所有 `/api/v1/*` 都校验；不符 → 401 JSON `{"detail":"missing or invalid api key"}`。
- `GAP_API_KEY` 未配置 → 中间件旁路 + 启动日志 WARNING（开发友好；生产必配）。

### 3.2 接口统一改 POST

- `GET /domains` → `POST /domains`（无 body，逻辑不变）。
- `POST /md` 已是 POST，不动。
- 前端零影响（不调这两个接口）。`GET /domains` 直接删除。
- `图谱接口.md`、`SKILL.md` 示例同步改 POST + 带 `X-API-Key`。

### 3.3 运营打点（jsonl，对象级，三维）

- 只打 `POST /domains` + `POST /md`。
- 记录粒度：一次请求展开成对象级——`/md` 带 N 个 id → 每个 id 记一条（type 取该 id 的 type）；`/domains` → 每个返回域 id 记一条（type=BusinessDomain）。
- 存储：`platform-data/telemetry/access.jsonl`（gitignore），追加写。
- 前端在「统计」页（`StatsView.vue`）新增「知识取用频次」区块，展示三维：按 type 聚合 / 热门对象 top-N / 时间趋势。**不新增菜单**。

---

## 4. 设计

### 4.1 后端

#### 4.1.1 `config.py` 扩展

```python
import os
API_KEY = os.environ.get("GAP_API_KEY", "")  # 空 → 鉴权旁路
TELEMETRY_DIR = DATA_DIR / "telemetry"
TELEMETRY_FILE = TELEMETRY_DIR / "access.jsonl"
```

#### 4.1.2 鉴权中间件（新 `app/middleware/auth.py`）

- `@app.middleware("http")`，仅拦截 `path.startswith("/api/")`。
- `API_KEY` 为空 → 直接放行（旁路）。
- 否则比对 `request.headers.get("X-API-Key")`：不等或缺失 → `JSONResponse(401, {"detail": "missing or invalid api key"})`。
- 静态资源（前端 dist、SPA 兜底）不拦截。
- 独立模块，不 import 图谱 service/tests service。
- **中间件顺序**：auth 须在现有 `CORSMiddleware` **之后** `add_middleware`（FastAPI 中间件 LIFO，后 add 先执行），确保 auth 先跑、而 401 响应仍被 CORS 包装带上跨域头——否则浏览器 opaque 401，前端 `clearKey → /login` 流程会断。

#### 4.1.3 打点模块（新 `app/telemetry/`，隔离）

- `recorder.py`：
  - `record(endpoint: str, id_: str, type_: str) -> None`：追加一行 `{"ts": <ISO8601>, "endpoint": ..., "id": ..., "type": ...}` 到 jsonl。
  - 进程内 `threading.Lock` + 小批量缓冲（如满 50 条或 5s flush），避免每请求一次 IO；进程退出/uvicorn reload 时 flush。MVP 也可直接同步追加（jsonl 追加开销可接受），缓冲为可选优化。
  - ts 用 `datetime.now(timezone.utc).isoformat()`。
  - **失败处理**：打点是观测用、非功能性——`record()` 内部 try/except 吞异常 + log，**绝不向上抛**，绝不因打点失败让 `/md`、`/domains` 请求失败。
- `aggregator.py`：
  - `aggregate(days: int = 30) -> dict`：流式读 jsonl，过滤最近 `days` 天，返回：
    ```json
    {
      "total": 230,
      "by_type": {"Feature": 120, "MMLCommand": 80, "BusinessDomain": 30},
      "top_ids": [{"id": "...", "type": "...", "count": 42}, ...],   // top 20
      "timeline": [{"date": "2026-07-22", "count": 50}, ...]          // 按日，最近 days 天
    }
    ```
- 不依赖图谱 service；`type` 复用 router 已为响应 resolve 出的 `obj.type`（`/md` 走 `resolve_node` 结果、`/domains` 恒 `BusinessDomain`），recorder 不反向查 index，零额外访问。

#### 4.1.4 `routers/objects.py` 改造

- 删 `@router.get("/domains")` → 改 `@router.post("/domains")`，函数体不变。
- `batch_md(req)` 末尾：对每个成功取到的 id 调 `record("/md", id, obj.type)`。
- `list_domains_with_md()` 末尾：对每个返回域 id 调 `record("/domains", id, "BusinessDomain")`。
- 仅末尾加 `record()` 调用，不动既有解析逻辑（隔离红线）。

#### 4.1.5 打点查询接口（新 `routers/telemetry.py`）

- `GET /api/v1/telemetry/stats?days=30` → `aggregator.aggregate(days)`。
- 受鉴权中间件保护（前端登录后看）。

#### 4.1.6 `main.py`

- 挂鉴权中间件：`add_middleware` 或 `@app.middleware`（实现细节）。
- 注册 telemetry router：`app.include_router(telemetry_router, prefix="/api/v1")`。
- 启动日志：`API_KEY` 为空 → 打 WARNING"鉴权未启用：未配置 GAP_API_KEY"。

### 4.2 前端

#### 4.2.1 登录态（新 `auth.ts` + `views/LoginView.vue`）

- `auth.ts`：`getKey()`/`setKey()`/`clearKey()`（`sessionStorage` 读写 `gap_api_key`）。
- `LoginView.vue`：输入框 + "验证并登录"按钮 → 调 `/api/v1/names`（轻接口）验证，200 存 KEY 跳 `/`，401 报错提示。
- `router.ts` 加全局前置守卫：除 `/login` 外，无 KEY → 跳 `/login`。
- 新增路由 `/login`（不在顶部 tab 显示）。

#### 4.2.2 `_req` 注入 header + 401 跳登录

- `api.ts` 与 `tests-module/api.ts` 的 `_req`：
  - 所有请求加 `X-API-Key: getKey()` header。
  - 响应 401 → `clearKey()` + 跳 `/login`，再抛错。
  - **避免循环依赖**：`router.ts` 懒加载 views、views 又 import `api.ts`，故 `_req` **不能**静态 `import router`。跳转用懒加载 `import('./router').then(r => r.router.push('/login'))`，或干脆 `window.location.assign('/login')`（最稳，绕开 router 实例）。
- 两个封装共享同一把 KEY（`sessionStorage` 同源）。

#### 4.2.3 取用频次（并入第三菜单「统计」`StatsView.vue`，不新增菜单/路由）

- **不新增 tab、不新增 `/telemetry` 路由、不改 `AppHeader.vue`。**
- 在 `StatsView.vue` 现有 4 张层级卡片下方新增一个 `<section>`「知识取用频次」，含三区块（零依赖）：
  1. **按 type 横条**：CSS 横条，每 type 一行，宽度按 count 归一。
  2. **热门对象 top-20**：列表，`id` + `type` tag + count。
  3. **时间趋势**：按日 SVG 折线（最近 N 天，N 可选 7/30/90）。
- section 顶部：总次数 + 时间范围切换（7/30/90 天）+ 独立刷新。
- 数据：`api.ts` 加 `fetchTelemetryStats(days)` → `GET /api/v1/telemetry/stats?days=N`。
- 三区块倾向抽成 `components/TelemetrySection.vue`（保持 `StatsView` 聚焦资产统计），实现期定。

### 4.3 文档同步

- `三层图谱构建规范/skill/图谱接口.md`：`GET /domains` → `POST /domains`，所有 curl 示例加 `-H "X-API-Key: $GAP_API_KEY"`。
- `三层图谱构建规范/skill/SKILL.md`：同步接口签名 + KEY 用法。
- `graph-asset-platform/README.md`：启动命令前置 `GAP_API_KEY=xxx`，说明未配则鉴权旁路。
- `.env.example`（新）：`GAP_API_KEY=`。

---

## 5. 隔离与文件清单

**隔离红线**：不动图谱资产解析/索引/现有视图行为；只**加**中间件、新模块、新视图、`_req` 加 header、两处 router 末尾加 `record()`。

| 类型 | 路径 |
|---|---|
| 后端新增 | `app/middleware/__init__.py`、`app/middleware/auth.py`、`app/telemetry/__init__.py`、`app/telemetry/recorder.py`、`app/telemetry/aggregator.py`、`routers/telemetry.py` |
| 后端改动 | `config.py`（+env）、`main.py`（+中间件 +router）、`routers/objects.py`（`/domains` 改 POST + 2 处 `record()`） |
| 前端新增 | `src/auth.ts`、`src/views/LoginView.vue`、（建议）`src/components/TelemetrySection.vue` |
| 前端改动 | `src/api.ts`（+`fetchTelemetryStats` +`_req` header/401）、`src/tests-module/api.ts`（`_req` +header +401 跳登录）、`src/router.ts`（+`/login` 路由 +守卫）、`src/views/StatsView.vue`（+取用频次 section） |
| 文档 | `图谱接口.md`、`SKILL.md`、`README.md`、`.env.example` |
| 配置 | `platform-data/telemetry/`（gitignore）、`.gitignore`（+telemetry 行） |

---

## 6. 环境变量

| 变量 | 必需 | 说明 |
|---|---|---|
| `GAP_API_KEY` | 生产必配 | 鉴权 KEY；前端登录与 SKILL 调用共用。空 → 鉴权旁路（仅开发） |

> 安全：`GAP_API_KEY` 的**存在与否**可日志（缺失打 WARNING），但**取值绝不 echo**（启动日志、错误信息、任何响应都不得回显 KEY）。

---

## 7. 测试要点（实现阶段覆盖）

- **鉴权**：无 KEY → 401；错 KEY → 401；对 KEY → 200；未配 `GAP_API_KEY` → 全放行。
- **/domains 改 POST**：`POST /domains` 200 返回域 md；`GET /domains` 404（已删）；带 KEY 可调。
- **打点**：`POST /md` 带 3 个 id → jsonl 追加 3 行，type 正确；`POST /domains` → 每域一行。
- **聚合**：造若干 jsonl 行 → `aggregate()` 的 total/by_type/top_ids/timeline 正确；`days` 过滤生效。
- **前端**：未登录访问任意页 → 跳 `/login`；输错 KEY → 提示；输对 → 进 `/`；频次面板三区块渲染、天数切换。
- **隔离**：`git diff` 确认图谱 service/tests service 零改动。

---

## 8. 风险与权衡

| 风险 | 应对 |
|---|---|
| jsonl 无限增长 | 临时项目可接受；后续可加滚动/截断（本 spec 不做，YAGNI） |
| 同步追加 IO 阻塞 | MVP 先同步；若 /md 批量大 perceived 慢，再上缓冲 flush |
| KEY 泄漏（前端 sessionStorage 可被同源脚本读） | 接受（内网/受控环境）；非生产级机密，是门禁不是强认证 |
| 改 POST 破坏未知调用方 | 已核实前端不用；SKILL 文档同步；GET 直接删（用户拍板） |

---

## 9. 后续（不在本 spec）

- Agent 一键审查入口（review 自动定位图谱问题）——测试子系统已预留。
- 打点扩展到 web 浏览（若将来要看人工浏览热区）——届时需引入双 KEY 区分 caller。
