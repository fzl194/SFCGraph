# 图谱总览（Graph Overview）

> platform-next 的「图谱总览」tab —— assets/ typed wiki 的三栏 Obsidian 式浏览器。

## 是什么

一个把 `assets/` 知识库当作可点击 wiki 来浏览的页面：

- **左栏**：分类导航树。按对象类型（命令 / 配置对象 / 特性 / License / 任务）→ NF → 版本 → front-matter 天然分组（命令按 category_path、配置对象按 object_kind、特性按目录父子、任务按 task_layer）下钻到具体对象，顶部带跨类搜索。
- **中区**：当前对象的 md 渲染。点击 md 内的 `[链接](path.md)` 即跳转到目标对象；`[[未构建ID]]` 显示为灰色不可点 chip。
- **右栏**：以当前对象为中心的 **1 跳邻域图谱**（vis-network）。出向链接 + 反链，边按关系类型上色。点节点即跳转，图谱随之重画。
- **顶部面包屑**：本会话跳转历史，点任意节点回跳。

四种入口（左树叶子 / md 链接 / 图谱节点 / 搜索结果）跳转一致，URL 驱动（`/graph-overview/a/<assets路径>`），浏览器前进/后退/分享链接可用。

## 数据来源

只读 `../assets/`（typed wiki 唯一对外面）。后端 `platform-next/wiki/`：
- `build_wiki_index.py` 扫全量 md → `wiki/data/wiki_index.json`（nodes + edges + 反邻接）。
- `service.py` 载入索引到内存，提供 `categories/group/list/neighborhood/md/search`。
- `router.py` 暴露 `/api/v1/wiki/*`。

## 重建索引

assets/ 变更后需重建索引（服务启动时若索引缺失会自动建，但已存在则用缓存）：

```bash
cd platform-next
rm -f wiki/data/wiki_index.json            # 强制重建
python -m wiki.build_wiki_index ../assets wiki/data/wiki_index.json   # 或显式建
python main.py                              # 启动（首访触发惰性载入/构建）
```

索引文件 `wiki/data/wiki_index.json` 已 gitignore（生成物）。真实 assets 全量约 37000 节点，冷构建约 50s，磁盘载入约 1.7s，之后查询走内存（neighborhood < 1ms）。

## 运行

```bash
cd platform-next && python main.py    # http://localhost:8000 —— 同时服务 API 与前端 dist
# 或前端开发模式（热更新）：cd frontend && npm run dev   # :3000，调 :8000 API
```

访问 `http://localhost:8000/`，点顶部「图谱总览」。

## 测试

- 后端：`cd platform-next && python -m pytest tests/wiki/ -v`（27 测试，含路径穿越防护）。
- 前端：`cd platform-next/frontend && npm run build`（vue-tsc 类型检查 + 构建）。

## 关联

- 总方案：`docs/superpowers/specs/2026-07-08-config-generation-e2e-design.md`
- 本特性 spec：`docs/superpowers/specs/2026-07-09-graph-overview-frontend-design.md`
- 本特性 plan：`docs/superpowers/plans/2026-07-09-graph-overview-frontend.md`
