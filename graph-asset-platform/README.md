# 图谱资产管理平台 (Graph Asset Platform) v1

一个**独立**的图谱资产管理平台：上传 md 资产包 → 自动解压、分析、归类合并进**唯一统一资产库** → 用通用机制解析对象/边 → 提供**读 API（单对象 / 单跳）**和**三栏只读前端**浏览游走 → 可导出。

> 与仓库里的 `assets/` **完全无关**——平台自管一份资产库，导入即权威。

## 资产格式（权威：`三层图谱构建规范/command`）

完整设计见 `docs/superpowers/specs/2026-07-16-graph-asset-platform-design.md`。要点：

- 每个 md = YAML frontmatter + 正文 + 底部 `## 边` 章节（边用 wikilink `[[{nf}@{Type}@{local}]]`）。
- 对象 ID **版本无关**：NF 隔离类 3 段 `{nf}@{Type}@{local}`，跨 NF 类 2 段 `{Type}@{semantic}`。
- **版本只在目录和 frontmatter 字段**：NF 类目录 `{Layer}/{nf}/{version}/`，文件名 = 逻辑ID。
- 版本解析：每个 (id, version) 一个节点；不带版本时按**该 id 最新现存版本**解析，`?version=` 显式指定。
- bundle = 一个 zip，里面一堆 md（**无 manifest**）；导入按 frontmatter 自动归类合并。

## 目录结构

```
graph-asset-platform/
├── backend/        FastAPI 后端（Python）
│   ├── app/        models/logical_id/registry/classify/md_parser/edges/version
│   │               store/index/bundle/service/main + routers/
│   └── tests/      单元 + 集成 + e2e；fixtures/sample_bundle/ 样例资产
└── frontend/       Vue3+TS 三栏只读前端
```

## 启动

### 1. 后端

```bash
cd graph-asset-platform/backend
pip install -e ".[dev]"              # fastapi uvicorn[standard] pyyaml python-multipart + pytest httpx
uvicorn app.main:app --port 8000 --reload
```

- API 根：`http://localhost:8000/api/v1`
- Swagger 文档：`http://localhost:8000/docs`
- 前端（需先 build，见下）：`http://localhost:8000/`

### 2. 前端

两种方式任选：

**A. 生产模式（后端托管 dist）**
```bash
cd graph-asset-platform/frontend
npm install
npm run build          # 产出 dist/，后端 main.py 自动托管为 SPA
# 然后访问 http://localhost:8000/
```

**B. 开发模式（热更新，代理 /api → 8000）**
```bash
cd graph-asset-platform/frontend
npm install
npm run dev            # → http://localhost:5173
```

### 3. 导入样例数据（首次测试用）

平台启动后资产库是空的，导入一份样例 bundle 即可浏览：

```bash
cd graph-asset-platform/backend
# 把 tests/fixtures/sample_bundle 打包成 zip
python -c "import zipfile,glob,os; \
  z=zipfile.ZipFile('sample.zip','w',zipfile.ZIP_DEFLATED); \
  [z.write(f, os.path.relpath(f,'tests/fixtures/sample_bundle')) \
   for f in glob.glob('tests/fixtures/sample_bundle/**/*', recursive=True) if os.path.isfile(f)]; \
  z.close()"
# 导入
curl -F "file=@sample.zip" http://localhost:8000/api/v1/import
```

或直接在前端顶栏点「导入」上传 `sample.zip`。

## API 速查（前缀 `/api/v1`）

| 端点 | 说明 |
|---|---|
| `POST /import` | 上传 zip 合并进资产库 → `{added, updated, skipped, warnings, counts}` |
| `GET /imports` | 上传记录 |
| `GET /export?nf=&version=&domain=&scenario=` | 导出资产库（可切片）→ zip |
| `GET /stats` | 对象/边计数、nfs、versions_per_nf |
| `GET /objects?type=&q=&nf=&domain=&page=&size=` | 列对象（按 id 聚合 + versions[]） |
| `GET /objects/{id}?version=` | 单对象（不带版本=最新现存；带 `?version=` 指定） |
| `GET /objects/{id}/neighbors?hops=1&version=` | 单跳邻居（含反链） |
| `GET /objects/{id}/md?version=` | 原始 md |
| `GET /subgraph?center=&hops=&type=&version=` | N 跳子图 |

> `{id}` 含 `@` 和空格，URL 须 encode（`@`→`%40`、空格→`%20`）。`?version=X` 不在该 id 可用版本时 → 404 + `available_versions`。

## 测试

```bash
cd graph-asset-platform/backend
python -m pytest -q          # 全量（单元+集成+e2e，99 测试）
```

## ⚠️ 提交注意（GIT 陷阱）

仓库里 `三层图谱构建规范/scripts/product_doc_md_exporter_optimized.py` **长期处于 git 暂存态（A）**。对本仓库做任何 `git commit`，若**不路径限定**，都会把它夹带进提交。

**务必**这样提交平台代码：
```bash
git add graph-asset-platform/<具体文件>
git commit -m "<type>: <描述>" -- graph-asset-platform/
```
**绝不要** `git add -A` / `git add .` / `git commit -am`。

## 二期预留（v1 不做）

在线编辑 / 写 API、资产内容级版本管理、变更评审回路 + Agent 编排、多用户鉴权。接入点见 spec §10。
