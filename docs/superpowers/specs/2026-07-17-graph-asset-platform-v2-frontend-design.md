# 图谱资产管理平台 v2 前端重构设计

> 日期：2026-07-17
> 状态：设计（基于用户实测反馈，delta 于 v1）
> 范围：前端 IA 重构 + 异步导入。后端核心（解析/索引/对象边模型/版本解析/读 API 主体）不变。

## 1. 背景

v1（`2026-07-16-graph-asset-platform-design.md`）已完成读侧 + 导入导出 + 三栏前端。实测反馈：
1. 上传后前端一直转圈（同步阻塞）→ 要异步。
2. "图谱"不该是独立菜单 → 应作图谱浏览右栏。
3. 要一个统计菜单（卡片式按层）。
4. 左侧纯文件夹展开难看 → 要按"层"拆分层级（命令/特性/任务/业务 + 网元版本 + 跨层关联）。
5. 图谱 API 已实现且跨层统一（确认）。

本 v2 只改前端 IA + 导入异步化 + 统计接口扩充，并清理被取代的旧前端件。

## 2. 新菜单 IA（3 个）

`图谱浏览` / `统计` / `上传`。**独立"图谱"菜单取消**（并入图谱浏览右栏）。

## 3. 图谱浏览（三栏）

### 3.1 左栏：层 Tab + 选择器 + 虚拟列表（B 布局）
顶部 4 个层 Tab；选中层后显示该层选择器 + 虚拟列表（复用 `/objects?type=&nf=&version=&domain=&page=&size=`，层 = 类型过滤）：
- **命令层**：`网元▼ 版本▼ 类型▼(命令MMLCommand/配置对象ConfigObject/全部)` + 搜索 + 虚拟列表
- **特性层**：`网元▼ 版本▼ 类型▼(特性Feature/license/全部)` + 列表
- **任务层**：`网元▼ 版本▼` + 列表（Task）
- **业务层**（跨网元、无版本）：`域▼ 场景▼` + 列表（BusinessDomain/NetworkScenario/ConfigurationSolution）
- 列表项 = id（等宽）+ 类型 badge；只渲染可见行；点对象 → 中栏 + 右栏。

### 3.2 中栏：md 预览（沿用现有 `MdPreview`）
frontmatter 面板 + 渲染正文 + 底部 `## 边` 可点跳转。不变。

### 3.3 右栏：当前对象单跳邻居图谱
vis-network 渲染选中对象的单跳邻居（出/入边）+ 边清单。点邻居 → 联动中栏 + **左栏自动同步**。**跨层关联在此体现**（邻居可跨层）。

### 3.4 ★ 左栏前端缓存 + 跳转自动同步（重点）
- **缓存**：每层的导航状态（active 层、网元、版本、域、场景、搜索词、已加载列表分页、滚动位）缓存在前端 store；切 Tab / 跨栏跳转回来不丢上下文、不重拉。列表数据按 `(层,网元,版本,页)` 缓存，避免重复请求。
- **自动同步**：当中栏 wiki 链接或右栏邻居被点击 → 跳到对象 X：
  1. 解析 X 的层（id 的 Type 段）、网元（id 的 nf 段）、版本（取 X 的最新现存版本，或跳转源携带的版本）。
  2. 左栏自动切到对应层 Tab + 设选择器（网元/版本 或 域/场景）。
  3. 列表滚到 X 并高亮。
  - 实现：跳转目标 id → 调 `/objects/{id}` 拿 type/nf/version/domain/scenario → 驱动左栏。

## 4. 统计（新菜单，卡片式，前期纯数字）
卡片按层：
- **命令层卡**：总数 + 按网元(UDG/UNC) + 按版本(UDG/20.15.2、UDG/20.16.0、UNC/20.16.0…)
- **特性层卡** / **任务层卡**：总数 + 按网元
- **业务层卡**：总数（跨网元）+ 按域
报表/图表留后期。

## 5. 上传（异步，不转圈）
- `POST /import` **立即返回 202 + 任务记录**（追加 `_imports.log`：job_id、time、status=processing）；后端用 FastAPI BackgroundTasks 后台解压→归类→合并→重建索引→置 status=done + added/updated。
- 前端上传页：拖拽区 + 上传列表（状态 处理中→完成）；**非阻塞状态条**轮询任务状态（`GET /import/jobs` 或 `/imports` 带 status），完成后自动刷统计。**非阻塞，不转圈**。

## 6. API 改动
- **异步导入**：`POST /import` → 202 + `{job_id, status}`；后台处理；`GET /import/jobs`（列表含 status）或 `GET /import/jobs/{id}`。
- **统计扩充**：`/stats` 增加 `per_layer`（层→计数）、`per_layer_per_nf`、`per_layer_per_nf_per_version`（命令/特性/任务）+ 业务层 `per_domain`，供统计卡。
- **复用** `/objects` 做 B 导航列表（层=type 过滤，已支持）。
- 主键解析辅助：跳转同步需要由 id 取对象元数据，复用 `GET /objects/{id}`（已有）。

## 7. 清理（删被取代的件）
- 删 `/browse` 端点 + `AssetTree`（文件夹树）组件 → B 导航取代。
- 删独立 `GraphView` → 并入图谱浏览右栏。
- `/overview`：右栏改单跳后不再用 → 删（或留作统计空态，倾向删）。

## 8. 不变
后端核心：`md_parser` / `index` / `edges` / `classify` / `registry` / `version` / `store` / `bundle`（导出）/ 对象边模型 / 版本解析 / SPA fallback / 读 API 主体（objects/neighbors/md/subgraph/stats/imports/export）。

## 9. 测试
- 后端：异步导入（202→processing→done）、/stats 扩充字段、(删 /browse 的测试随之移除)。
- 前端：层 Tab 切换 + 选择器 + 虚拟列表、缓存命中、跳转自动同步（切 Tab/选择器/高亮）、统计卡数据、上传非阻塞状态。
- 既有 106 测试中 /browse 相关移除后保持其余绿。
