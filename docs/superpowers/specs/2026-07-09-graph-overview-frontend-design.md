# 图谱总览前端设计（platform-next · 新增「图谱总览」tab）

> 2026-07-09 · 需求经 brainstorming 对齐（三栏 Obsidian 式 + 1 跳邻域图谱 + front-matter 天然分组下钻）。
> 上游体系：`docs/superpowers/specs/2026-07-08-config-generation-e2e-design.md`（Typed LLM Wiki 端到端方案）。
> 数据面：`assets/`（自包含 typed wiki，唯一对外知识面）。准则：`assets/CLAUDE.md`。

---

## 1. 背景与目标

`assets/` 已 Compile 出 **21000+ 个 typed md**（命令 13075 / 配置对象 5820 / 特性 942 / License 635 / 任务 UDG187+UNC / 业务层 P4 待建），对象间用 `[[wiki 链接]]` / 标准 markdown 链接承载 Schema 关系。现有 platform-next 的 4 个 tab（命令/特性/业务/任务图谱）服务的是**旧 jsonl 结构化数据**，不是 assets/ wiki。

**目标**：新增「图谱总览」tab，作为 assets/ typed wiki 的**浏览器**——分类导航 + md 阅读 + 周围关系图谱三位一体，点击 md 内链接 / 图谱节点即可在对象间自由跳转，图谱随跳转自动以新对象为中心重画。

**一句话**：Obsidian 式的 assets/ wiki 浏览器。

## 2. 范围

**In**
- 新增独立 `wiki` 后端模块（只读 `assets/`）+ 前端「图谱总览」tab（三栏）。
- 索引构建器：扫 assets/ 全量 md → nodes/edges/反邻接索引。
- 三栏交互：左树分类导航、中区 md 渲染（链接拦截跳转）、右栏 1 跳邻域图谱（节点跳转）。
- URL 驱动跳转 + 跳转历史面包屑。
- 边界：`[[ID]]` 占位灰显、evidence 可达、空类别标注。

**Out（本次不做）**
- 不改现有 4 个 tab 及其数据源。
- 不做业务层（P4）的内容 Compile——business 类别仅占位显示。
- 不做 skill/schema 类别（价值低，后置）。
- 不做 N≥2 跳图谱、不做全局力导向大图（性能与可用性风险，留待后续）。
- 不引入前端测试框架（项目无现成基建）；走后端 pytest + 人工 e2e 清单。

## 3. 架构定位

```
assets/（typed wiki，只读真相面）
   │  build_wiki_index.py（构建器，扫全量 md）
   ▼
platform-next/wiki/data/wiki_index.json（nodes + edges + 反邻接，内存载入）
   │  service.py（查询）
   ▼
/api/v1/wiki/{categories,group,list,md,neighborhood,search}
   ▼
frontend/src/wiki/（三栏：CategoryTree / MdPane / NeighborGraph）
```

- 新模块 `wiki` 与 `feature_graph`/`command_graph`/`business_graph`/`task_graph` 并列，**只读 assets/**。
- 复用现有范式：vis-network 图谱（CommandGraph.vue）、md 渲染 + 链接拦截（DocViewer.vue）、router+service 分层（task_graph）。

## 4. 后端设计（`platform-next/wiki/`）

### 4.1 索引构建器 `build_wiki_index.py`

扫 `assets/**/*.md`，逐文件解析：

**front-matter**（YAML）：抽 `id`/`type`/`name`/`nf`/`version`/`status` + 分组字段：
| type | 分组字段 | 示例 |
|---|---|---|
| MMLCommand | `category_path`（list）、`verb`、`object_keyword` | 用户面服务管理/业务控制策略/计费控制/使用率上报规则 |
| ConfigObject | `object_kind`、`object_name` | entity |
| Feature | `feature_category`、`parent_feature_code`、`catalog_section` | enhanced / GWFD-020350 |
| License | （按 license_code 前缀或 applicable_nf 分桶） | LKV6SFVCPU01 |
| Task | `task_layer`（atom/compound/feature/solution/generalized）、`ref` | atom |

**正文链接**（两种）：
1. 标准 markdown 链接 `[text](path.md)` → `resolved` 边（目标文件存在）。路径为 assets 根相对（CLAUDE.md §5.5）。
2. `[[对象ID]]` 占位（双方括号，非标准 md 链接，渲染为字面文本）→ `resolved=false` 边，从 ID 的 ObjectType 段推断目标 type。

**关系类型推断**（按链接所在 `##` 小节标题映射，未知小节 → `related`）：

| 链接所在小节 | relation_type | 方向 |
|---|---|---|
| 操作的配置对象 / 操作本对象的命令 | `operates_on` / `operated_by` | command↔configobject |
| 关联任务 / 关联命令 | `has_task` / `ref_command` | command↔task |
| 所属目录 / 子特性 | `parent` / `child` | feature↔feature |
| 所需 License / 控制的能力 | `requires_license` | feature↔license |
| 关联对象 / object_refers_to | `relates_to` | configobject↔configobject |
| depends_on/conflicts_with/interacts_with/affects/supports | 同名 | feature↔feature |
| 证据 | `evidenced_by` | *→evidence |
| 其他 | `related` | — |

**补充边**（front-matter 派生，丰富图谱）：
- Task `ref:` → command（`ref_command`，与正文"命令 wiki"链接去重）。
- Feature `parent_feature_code` → parent feature（`parent`，与"所属目录"去重）。

**产出**（`platform-next/wiki/data/wiki_index.json`，`.gitignore` 排除——生成物）：
```jsonc
{
  "nodes": {
    "command/UDG/20.15.2/ADD-URR.md": {
      "path": "...", "id": "UDG@20.15.2@MMLCommand@ADD URR",
      "type": "MMLCommand", "name": "ADD URR", "nf": "UDG", "version": "20.15.2",
      "status": "active", "group": {"category_path": [...], "verb": "ADD"},
      "title": "配置URR（ADD URR）"
    }, ...
  },
  "edges": [
    {"from": "command/.../ADD-URR.md", "to": "configobject/.../URR.md",
     "relation_type": "operates_on", "resolved": true}, ...
  ],
  "reverse": { "configobject/.../URR.md": ["command/.../ADD-URR.md", ...], ... }  // 反邻接
}
```

**去重**：同 (from,to,relation_type) 仅留一条。**双向**：正文链接本身已含双向（命令引对象、对象反引命令），构建器不额外造反向边，靠 reverse 索引覆盖反链。

**构建时机**：服务启动时若 `wiki_index.json` 不存在或 stale（mtime < assets 最新文件），自动重建（后台线程，首次请求阻塞等待或返回 503+重试提示）。另提供 CLI `python -m platform-next.wiki.build_wiki_index`。

### 4.2 router.py + service.py（前缀 `/api/v1/wiki`）

仿 `task_graph/router.py` + `service.py`。service 启动载入索引到内存。

| 端点 | 入参 | 出参 | 用途 |
|---|---|---|---|
| `GET /categories` | — | `[{type, nfs:[{nf, versions:[{version, count}]}]}]` | 左树顶层骨架（type→nf→version + 计数，体量小，一次性给） |
| `GET /group` | `type,nf,version` | `[{key, count}]`（如命令的 category_path 桶 / 配置对象的 object_kind 桶） | 左树下钻到分组桶（懒加载，避免一次给 13075） |
| `GET /list` | `type,nf,version,group?,q?,page,size` | `{items:[{path,name,id}], total}` | 桶内对象列表（分页+搜索，给树叶子 / 搜索结果） |
| `GET /md` | `path` | `{path, content, meta}` 或 404 | 中区 md 原文（复用现有 file 读取模式，路径限定 assets/ 内，防穿越） |
| `GET /neighborhood` | `path, depth=1` | `{center, nodes:[...], edges:[...]}` | 右栏图谱（1 跳：出向边 + reverse 反链，节点带 type/name） |
| `GET /search` | `q,type?,limit` | `[{path,type,name}]` | 跨类搜索（备用，左树顶部搜索框） |

**安全**：`/md` 的 path 必须落在 `assets/` 内（normalize 后校验前缀），防路径穿越。

## 5. 前端设计（`frontend/src/wiki/`，三栏）

### 5.1 路由（`router.ts` 新增）
- `/graph-overview` → `WikiIndex.vue`（落地：左树就绪、中区欢迎语 + 使用说明、右栏空）
- `/graph-overview/a/:path(.*)` → `WikiIndex.vue`（path = assets 根相对路径，载入 md + neighborhood）

`TopBar.vue` 新增 `<router-link to="/graph-overview">图谱总览</router-link>`。

### 5.2 组件
| 组件 | 职责 | 复用 |
|---|---|---|
| `WikiIndex.vue` | 三栏 shell + 顶部跳转历史面包屑（`A › B › 当前`，点回跳）；watch 路由 path → 触发中区/右栏取数 | App 布局 |
| `CategoryTree.vue`（左） | el-tree 懒加载：type→nf→version（`/categories`）→ 展开调 `/group` → 桶内调 `/list`（带搜索/分页）；叶子点击 → `router.push` | — |
| `MdPane.vue`（中） | 取 `/md` → 渲染；**改造 DocViewer 链接拦截**：assets 根路径直接解析（`[..](command/UDG/20.15.2/ADD-URR.md)` → 目标 path），点击 → `router.push('/graph-overview/a/'+path)` | DocViewer.vue |
| `NeighborGraph.vue`（右） | 取 `/neighborhood` → vis-network 渲染；边按 relation_type 上色、节点按 type 配色；点节点 → `router.push` | CommandGraph.vue |

### 5.3 跳转与"图谱自动更新"（核心交互）
- 统一跳转入口：`router.push('/graph-overview/a/<目标 path>')`，来源 = md 链接 / 图谱节点 / 左树叶子 / 搜索结果。
- `WikiIndex` watch `route.params.path`：变 → 并行取 `/md` + `/neighborhood` → 中区换文、右栏图谱以新对象为中心重画（destroy 旧 network 实例再建，仿 CommandGraph）。
- 浏览器前进/后退天然生效（URL 驱动）；面包屑维护本会话访问栈，支持跨多步回跳。
- 取数中用 `v-loading`，失败显式错误（不复用全局吞错）。

### 5.4 配色与关系图例
节点按 type：命令=青 box / 配置对象=紫 diamond / 特性=蓝绿 / License=橙 / 任务=粉 / 业务=红 / evidence=灰。边按 relation_type 上色（operates_on 紫、requires_license 橙、parent/child 深灰、ref_command 粉、related 浅灰）。右栏底部一小行图例。`[[ID]]` 未解析目标 → 灰色虚边节点 + 不可点（hover 显示 ID）。

## 6. 边界处理

- **`[[ID]]` 占位**：md 渲染为灰色不可点 chip（`[[UDG@20.15.2@Task@0-00001]]` 字面）；图谱里灰色虚边节点，点击不跳转。
- **evidence（16000+）**：不进左树（浏览价值低、量大）；作为图谱邻居 + md 链接目标可达，点开在中区正常显示（其 front-matter 简单，neighborhood 通常很小）。
- **business 层（P4 未建）**：`/categories` 返回该类 count=0；左树显示「业务层(P4 待建)」且不可展开。
- **悬空 md 链接**（指向不存在的 .md，极少数 lint 残留）：图谱 resolved=false，灰显；中区点击 → `/md` 404 → 中区显示"该页尚未构建"。
- **大量节点**：1 跳通常 <30 节点；若超阈值（如 >60）仅显示前 N + 提示"节点过多，请用左树/搜索"。

## 7. 测试

**后端 pytest**（`platform-next/tests/wiki/`）：
- 索引构建器：用 assets/ 小样子集（或 mock tmp dir）验证 nodes/edges/reverse 正确、双向去重、`[[ID]]` resolved=false、front-matter 派生边。
- `/categories`、`/group`、`/list`、`/neighborhood`、`/md`（含路径穿越拒绝）、`/search` 端点契约。

**前端人工 e2e 清单**（写入 spec，不建框架）：
1. 进 `/graph-overview`：左树 type→nf→version 展开、中区欢迎语、右栏空。
2. 左树点命令叶子：中区显示该命令 md、右栏以该命令为中心画 1 跳图。
3. 点中区 md 内链接（如 `[URR](configobject/.../URR.md)`）：URL 变、中区换为 URR md、右栏重画以 URR 为中心。
4. 点右栏图谱节点：同 3 的效果。
5. 浏览器后退：回到上一对象。
6. 面包屑点 A：回跳到 A。
7. `[[ID]]` 占位：灰显不可点。
8. evidence 链接：可打开。
9. business 类别：标"待建"不可展开。
10. 搜索框：输入命中跳转。

## 8. 文件清单

**新建**
- `platform-next/wiki/__init__.py`、`router.py`、`service.py`、`build_wiki_index.py`、`config.py`（assets 根路径）
- `platform-next/wiki/data/`（`.gitkeep` + `.gitignore` 排除 `wiki_index.json`）
- `platform-next/tests/wiki/test_build_index.py`、`test_router.py`
- `frontend/src/wiki/WikiIndex.vue`、`CategoryTree.vue`、`MdPane.vue`、`NeighborGraph.vue`、`wikiApi.ts`

**修改**
- `platform-next/main.py`：`include_router(wiki_router)`、lifespan 触发索引载入/构建
- `frontend/src/router.ts`：加两条路由
- `frontend/src/shared/TopBar.vue`：加「图谱总览」链接
- `frontend/src/api.ts`：加 wiki api 工厂（仿现有 `commandGraphApi`）

## 9. 待定 / 风险

- **关系类型推断的覆盖**：section 标题→relation_type 映射表需对照真实 md 小节标题校准（构建器加"未匹配小节"告警，迭代补全）。
- **索引构建耗时**：21000 文件首建预计数秒；可接受。若慢，增量构建（按 mtime）为后续优化。
- **左树超大桶**：某 category_path 下可能数百命令；`/list` 分页 + 桶内搜索缓解。
- **UNC 任务 wiki**：已建（assets/task/UNC/），任务类按 nf 分 UDG/UNC 下钻即可。
- **evidence 是否需要独立"证据"类入口**：本次不做，后续若需要再加搜索直达。

## 10. 验收标准

- 「图谱总览」tab 可进，三栏布局正确。
- 任选一 md，中区正确渲染、右栏 1 跳邻域图谱正确（出向 + 反链、边按类型上色）。
- md 内链接、图谱节点、左树叶子三种入口跳转一致，跳转后中区 + 右栏同步更新。
- URL 驱动：前进/后退/分享链接可用；面包屑回跳可用。
- `[[ID]]` 占位、evidence、空 business 类别按 §6 处理。
- 后端 pytest 全绿；路径穿越被拒。
