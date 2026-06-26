# 命令图谱 JSONL 数据源 + 数据驱动字段展示 实现计划

> **For agentic workers:** REQUIRED: Use superpowers:subagent-driven-development (if subagents available) or superpowers:executing-plans to implement this plan. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 把 platform-next 命令图谱数据源从（已删除的）CSV 切换为 builder 产出的 JSONL，前端详情页改为数据驱动地展示所有抽取字段。

**Architecture:** 后端 `CommandGraphService` 重写为读取两个 JSONL、纯透传完整 record（仅从 `command_id` 解析 product/version）；前端 `CommandDetail.vue` 用常量 `ID_SLOTS`/`HIDE_FIELDS` 排除身份槽位与隐藏字段后，遍历 record 其余 key 自动渲染 markdown 分区。MMLCommand only。

**Tech Stack:** Python 3.12 + FastAPI（后端）；Vue 3 + TypeScript + Element Plus + markdown-it + dompurify（前端）。

**Spec:** `docs/superpowers/specs/2026-06-24-command-graph-jsonl-frontend-design.md`

> **实现后修订（用户反馈）**：Task 6 的 `CommandDetail.vue` 代码里的 `ID_SLOTS` / `HIDE_FIELDS` 排除集合**已删除**。用户明确"json 所有字段都展示，不隐藏任何字段"——`parameter_description` 与全部字段一律渲染。最终代码以仓库实际文件为准（见 spec §4.2）。最新 JSONL 为 24-key schema（原生 `nf`/`version`，无 `_review_status`/`_stage`/`_derived_review`）。

**Testing note:** `platform-next` 无 Python 测试框架（非 pytest 项目）。验证采用：后端直接调用 service 方法的 smoke 检查（`python -c`）+ 前端 `npm run build`（vue-tsc 类型检查 + vite 构建）+ 启动后手测。不强行引入 pytest 脚手架（YAGNI）。

**Commit note:** 用户全局规则"未经请求不提交"。计划的 commit 步骤为标准模板；执行时仅在用户要求时提交。

---

## File Structure

| 文件 | 动作 | 职责 |
|---|---|---|
| `platform-next/command_graph/service.py` | 重写 | 读 JSONL、解析 product/version、过滤/查找/读 md（去 CSV 依赖） |
| `platform-next/command_graph/router.py` | 修改 | `/commands` `/command` `/command-md` 增可选 `version` 参数 |
| `platform-next/frontend/src/shared/markdown.ts` | 新建 | md → 安全 HTML 的渲染工具（复用 markdown-it + dompurify） |
| `platform-next/frontend/src/api.ts` | 修改 | `command/commandMd` helper 透传可选 version |
| `platform-next/frontend/src/command_graph/CommandList.vue` | 修改 | 加版本下拉；category_path 按数组处理；增版本列 |
| `platform-next/frontend/src/command_graph/CommandDetail.vue` | 重写 | 数据驱动字段分区；移除所有硬编码分区与键值表 |

---

## Chunk 1: 后端（service.py + router.py）

### Task 1: 重写 `service.py`（CSV → JSONL，纯透传 record）

**Files:**
- Modify (full rewrite): `platform-next/command_graph/service.py`

- [ ] **Step 1: 用下面完整内容覆写 `service.py`**

```python
"""Command graph data service — reads JSONL extracted by command-graph/builder.

Data source: command-graph/data/output/mml_commands_{udg,unc}.jsonl
Each record is a full MMLCommand (章节级 + 派生字段), passed through verbatim
to the frontend, which renders fields data-driven. This service only:
  - loads JSONL,
  - derives product(nf) + version from command_id,
  - filters / paginates / looks up / reads raw md.
"""
import json
from pathlib import Path


class CommandGraphService:
    def __init__(self):
        project_root = Path(__file__).resolve().parent.parent.parent
        self._doc_root = project_root
        self._data_dir = project_root / "command-graph" / "data" / "output"
        self._records: list[dict] = []
        self._by_id: dict[str, dict] = {}
        self._load()

    # ---- loading ----
    def _load(self) -> None:
        files = [
            self._data_dir / "mml_commands_udg.jsonl",
            self._data_dir / "mml_commands_unc.jsonl",
        ]
        for fp in files:
            if not fp.exists():
                continue
            with fp.open(encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    try:
                        rec = json.loads(line)
                    except json.JSONDecodeError:
                        continue
                    product, version = self._parse_id(rec.get("command_id", ""))
                    rec["product"] = product
                    rec["version"] = version
                    self._records.append(rec)
                    self._by_id[rec.get("command_id", "")] = rec

    @staticmethod
    def _parse_id(command_id: str) -> tuple[str, str]:
        # "UDG@20.15.2:DSP DFSBUCKET" -> ("UDG", "20.15.2")
        if "@" in command_id and ":" in command_id:
            nf_ver, _name = command_id.split(":", 1)
            if "@" in nf_ver:
                nf, version = nf_ver.split("@", 1)
                return nf, version
        return "", ""

    # ---- stats ----
    def get_stats(self) -> dict:
        by_product: dict[str, int] = {}
        by_version: dict[str, int] = {}
        for r in self._records:
            p = r.get("product") or "unknown"
            v = r.get("version") or "unknown"
            by_product[p] = by_product.get(p, 0) + 1
            by_version[v] = by_version.get(v, 0) + 1
        return {
            "total": len(self._records),
            "by_product": by_product,
            "by_version": by_version,
            "versions": sorted(by_version.keys()),
        }

    # ---- list (slim items) ----
    @staticmethod
    def _slim(r: dict) -> dict:
        return {
            "command_id": r.get("command_id"),
            "command_name": r.get("command_name"),
            "command_name_zh": r.get("command_name_zh"),
            "product": r.get("product"),
            "version": r.get("version"),
            "verb": r.get("verb"),
            "category_path": r.get("category_path") or [],
            "command_function": r.get("command_function") or "",
        }

    def list_commands(
        self,
        product: str | None = None,
        version: str | None = None,
        search: str | None = None,
        page: int = 1,
        size: int = 50,
    ) -> dict:
        s = (search or "").lower()
        filtered: list[dict] = []
        for r in self._records:
            if product and r.get("product") != product:
                continue
            if version and r.get("version") != version:
                continue
            if s:
                cat = " ".join(r.get("category_path") or [])
                hay = " ".join([
                    r.get("command_name") or "",
                    r.get("command_name_zh") or "",
                    r.get("command_function") or "",
                    cat,
                ]).lower()
                if s not in hay:
                    continue
            filtered.append(r)

        filtered.sort(key=lambda r: (r.get("product") or "", r.get("command_name") or ""))
        total = len(filtered)
        start = (page - 1) * size
        items = [self._slim(r) for r in filtered[start:start + size]]
        return {"total": total, "page": page, "size": size, "items": items}

    # ---- single (full record) ----
    def get_command(
        self, product: str, command_name: str, version: str | None = None
    ) -> dict | None:
        for r in self._records:
            if r.get("product") != product:
                continue
            if r.get("command_name") != command_name:
                continue
            if version and r.get("version") != version:
                continue
            return r
        return None

    def get_command_md(
        self, product: str, command_name: str, version: str | None = None
    ) -> str:
        rec = self.get_command(product, command_name, version)
        if not rec:
            return ""
        md_path = rec.get("md_path")
        if not md_path:
            return ""
        full = self._doc_root / md_path
        if not full.exists() or not full.is_file():
            return ""
        return full.read_text(encoding="utf-8")

    # ---- static file serving (unchanged contract; images etc.) ----
    def resolve_doc_path(self, rel_path: str) -> Path | None:
        """Resolve a relative path under doc_root/output, with safety checks."""
        full = (self._doc_root / "output" / rel_path).resolve()
        output_root = (self._doc_root / "output").resolve()
        if not str(full).startswith(str(output_root)):
            return None
        if full.exists() and full.is_file():
            return full
        return None

    def get_doc_content(self, rel_path: str) -> str:
        full = self.resolve_doc_path(rel_path)
        if not full:
            return ""
        return full.read_text(encoding="utf-8")


# Singleton
_service: CommandGraphService | None = None


def get_service() -> CommandGraphService:
    global _service
    if _service is None:
        _service = CommandGraphService()
    return _service
```

- [ ] **Step 2: smoke 检查 service 能加载且计数正确**

Run:
```bash
cd platform-next && python -c "from command_graph.service import CommandGraphService; s=CommandGraphService(); st=s.get_stats(); print('total',st['total'],'by_product',st['by_product'],'versions',st['versions'])"
```
Expected: `total 13075 by_product {'UDG': 4577, 'UNC': 8498} versions ['20.15.2']`

- [ ] **Step 3: smoke 检查 lookup + md 读取**

Run:
```bash
cd platform-next && python -c "from command_graph.service import CommandGraphService; s=CommandGraphService(); c=s.get_command('UDG','ADD URR'); print('found' if c else 'MISS'); print('keys',len(c)); md=s.get_command_md('UDG','ADD URR'); print('md_len',len(md))"
```
Expected: `found` / `keys 25`（或当前 record 实际 key 数）/ `md_len` 为正数。

- [ ] **Step 4: smoke 检查 list 过滤+分页**

Run:
```bash
cd platform-next && python -c "from command_graph.service import CommandGraphService; s=CommandGraphService(); r=s.list_commands(product='UDG',search='URR',page=1,size=5); print('total',r['total'],'items',len(r['items'])); print([i['command_name'] for i in r['items']])"
```
Expected: `total` > 0，`items` ≤ 5，列表含 `ADD URR` 类命令。

### Task 2: 修改 `router.py`（增可选 version 参数）

**Files:**
- Modify: `platform-next/command_graph/router.py`

- [ ] **Step 1: 用下面完整内容覆写 `router.py`**

```python
"""Command graph API routes."""
from fastapi import APIRouter, Query
from fastapi.responses import FileResponse
from .service import get_service

router = APIRouter(prefix="/api/v1/command-graph", tags=["command-graph"])


@router.get("/stats")
def get_stats():
    svc = get_service()
    return svc.get_stats()


@router.get("/commands")
def list_commands(
    product: str | None = Query(None),
    version: str | None = Query(None),
    search: str | None = Query(None),
    page: int = Query(1, ge=1),
    size: int = Query(50, ge=1, le=200),
):
    svc = get_service()
    return svc.list_commands(product=product, version=version, search=search, page=page, size=size)


@router.get("/command")
def get_command(
    product: str = Query(...),
    command_name: str = Query(...),
    version: str | None = Query(None),
):
    svc = get_service()
    cmd = svc.get_command(product, command_name, version)
    if not cmd:
        return {"error": "Command not found", "product": product, "command_name": command_name}
    return cmd


@router.get("/command-md")
def get_command_md(
    product: str = Query(...),
    command_name: str = Query(...),
    version: str | None = Query(None),
):
    svc = get_service()
    content = svc.get_command_md(product, command_name, version)
    return {"content": content, "product": product, "command_name": command_name}


@router.get("/doc-content")
def get_doc_content(path: str = Query(..., description="Relative path to md file")):
    svc = get_service()
    content = svc.get_doc_content(path)
    return {"content": content, "path": path}


@router.get("/file")
def serve_file(path: str = Query(..., description="Relative path to file")):
    """Serve a static file (image, etc.) from doc_root/output."""
    svc = get_service()
    full_path = svc.resolve_doc_path(path)
    if not full_path:
        return {"error": "Access denied or file not found"}
    suffix = full_path.suffix.lower()
    content_types = {
        ".png": "image/png",
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".gif": "image/gif",
        ".svg": "image/svg+xml",
        ".webp": "image/webp",
    }
    media_type = content_types.get(suffix, "application/octet-stream")
    return FileResponse(str(full_path), media_type=media_type)
```

- [ ] **Step 2: 确认 router 可导入**

Run:
```bash
cd platform-next && python -c "from command_graph.router import router; print('routes', [r.path for r in router.routes])"
```
Expected: 路径列表含 `/api/v1/command-graph/stats`、`/commands`、`/command`、`/command-md`、`/doc-content`、`/file`。

- [ ] **Step 3: （可选）提交后端改动**

```bash
git add platform-next/command_graph/service.py platform-next/command_graph/router.py
git commit -m "refactor: 命令图谱数据源 CSV→JSONL，纯透传 record"
```

---

## Chunk 2: 前端（markdown 工具 + api + CommandList + CommandDetail）

### Task 3: 新建 `shared/markdown.ts`

**Files:**
- Create: `platform-next/frontend/src/shared/markdown.ts`

- [ ] **Step 1: 创建文件，内容如下**

```typescript
import MarkdownIt from 'markdown-it'
import DOMPurify from 'dompurify'

// 与 DocViewer 同款配置：html/linkify/breaks 全开，输出经 dompurify 净化。
const md = new MarkdownIt({ html: true, linkify: true, breaks: true })

/** 把 markdown 字符串渲染成已净化的 HTML；空输入返回空串。 */
export function renderMarkdown(src: string): string {
  if (!src) return ''
  return DOMPurify.sanitize(md.render(String(src)))
}
```

### Task 4: 修改 `api.ts`（command/commandMd 透传 version）

**Files:**
- Modify: `platform-next/frontend/src/api.ts`（仅 `commandGraphApi` 对象）

- [ ] **Step 1: 把 `commandGraphApi` 块替换为下面内容**

```typescript
export const commandGraphApi = {
  stats: `${BASE}/command-graph/stats`,
  commands: `${BASE}/command-graph/commands`,
  command: (product: string, commandName: string, version?: string) => {
    const p = new URLSearchParams({ product, command_name: commandName })
    if (version) p.set('version', version)
    return `${BASE}/command-graph/command?${p}`
  },
  commandMd: (product: string, commandName: string, version?: string) => {
    const p = new URLSearchParams({ product, command_name: commandName })
    if (version) p.set('version', version)
    return `${BASE}/command-graph/command-md?${p}`
  },
}
```

> 注意：`businessGraphApi` / `featureGraphApi` / `fetchJson` / `postJson` 保持原样，只改 `commandGraphApi`。

### Task 5: 修改 `CommandList.vue`（版本下拉 + 数组分类 + 版本列）

**Files:**
- Modify (full rewrite template + script): `platform-next/frontend/src/command_graph/CommandList.vue`

- [ ] **Step 1: 用下面完整内容覆写 `CommandList.vue`**

```vue
<template>
  <!-- Filter bar -->
  <div class="filter-bar">
    <el-select
      v-model="filters.product"
      placeholder="产品"
      clearable
      size="small"
      style="width: 120px"
      @change="onFilterChange"
    >
      <el-option v-for="p in products" :key="p" :label="p" :value="p" />
    </el-select>
    <el-select
      v-model="filters.version"
      placeholder="版本"
      clearable
      size="small"
      style="width: 140px"
      @change="onFilterChange"
    >
      <el-option v-for="v in versions" :key="v" :label="v" :value="v" />
    </el-select>
    <el-input
      v-model="filters.search"
      placeholder="搜索命令名 / 中文名 / 功能..."
      clearable
      size="small"
      style="width: 260px"
      @input="debouncedSearch"
    />
    <span class="filter-count">{{ total }} 条命令</span>
  </div>

  <!-- Table -->
  <div class="card" style="overflow: hidden">
    <el-table
      :data="commands"
      :default-sort="{ prop: 'command_name', order: 'ascending' }"
      @row-click="onRowClick"
      style="width: 100%"
      v-loading="loading"
      size="small"
    >
      <el-table-column prop="command_name" label="命令" width="180" sortable>
        <template #default="{ row }">
          <span class="feature-id-cell">{{ row.command_name }}</span>
        </template>
      </el-table-column>
      <el-table-column prop="command_name_zh" label="中文名" width="180" sortable>
        <template #default="{ row }">
          <span class="feature-name-cell">{{ row.command_name_zh }}</span>
        </template>
      </el-table-column>
      <el-table-column prop="product" label="产品" width="90" sortable>
        <template #default="{ row }">
          <el-tag size="small" effect="plain">{{ row.product }}</el-tag>
        </template>
      </el-table-column>
      <el-table-column prop="version" label="版本" width="100" sortable>
        <template #default="{ row }">
          <span style="font-size: var(--text-xs); color: var(--text-secondary)">{{ row.version || '-' }}</span>
        </template>
      </el-table-column>
      <el-table-column label="分类路径" min-width="200">
        <template #default="{ row }">
          <span style="font-size: var(--text-xs); color: var(--text-secondary)">
            {{ formatCategoryPath(row.category_path) }}
          </span>
        </template>
      </el-table-column>
      <el-table-column prop="command_function" label="功能" min-width="300">
        <template #default="{ row }">
          <span class="definition-cell">{{ truncate(row.command_function, 120) || '-' }}</span>
        </template>
      </el-table-column>
    </el-table>

    <div style="padding: var(--space-3) var(--space-4)">
      <el-pagination
        v-model:current-page="page"
        v-model:page-size="size"
        :total="total"
        :page-sizes="[50, 100, 200]"
        layout="total, sizes, prev, pager, next"
        small
        @current-change="loadCommands"
        @size-change="onSizeChange"
      />
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, computed } from 'vue'
import { useRouter } from 'vue-router'
import { commandGraphApi, fetchJson } from '../api'

const router = useRouter()
const loading = ref(false)
const commands = ref<any[]>([])
const stats = ref<any>({})
const total = ref(0)
const page = ref(1)
const size = ref(50)

const filters = ref({ product: '', version: '', search: '' })

const products = computed(() => {
  const bp = stats.value.by_product || {}
  return Object.entries(bp).sort(([, a], [, b]) => (b as number) - (a as number)).map(([k]) => k)
})
const versions = computed(() => stats.value.versions || [])

let searchTimer: any = null
function debouncedSearch() {
  clearTimeout(searchTimer)
  searchTimer = setTimeout(() => { page.value = 1; loadCommands() }, 300)
}

function onFilterChange() {
  page.value = 1
  loadCommands()
}

function onSizeChange() {
  page.value = 1
  loadCommands()
}

function truncate(s: string, n: number) {
  if (!s) return ''
  return s.length > n ? s.slice(0, n) + '...' : s
}

function formatCategoryPath(raw: any) {
  if (Array.isArray(raw)) return raw.join(' > ') || '-'
  if (!raw) return '-'
  return String(raw)
}

function onRowClick(row: any) {
  router.push({
    name: 'command-detail',
    params: { product: row.product, commandName: row.command_name },
  })
}

async function loadStats() {
  stats.value = await fetchJson(commandGraphApi.stats)
}

async function loadCommands() {
  loading.value = true
  try {
    const params = new URLSearchParams()
    params.set('page', String(page.value))
    params.set('size', String(size.value))
    if (filters.value.product) params.set('product', filters.value.product)
    if (filters.value.version) params.set('version', filters.value.version)
    if (filters.value.search) params.set('search', filters.value.search)
    const data = await fetchJson(`${commandGraphApi.commands}?${params}`)
    commands.value = data.items || []
    total.value = data.total || 0
  } finally {
    loading.value = false
  }
}

onMounted(async () => {
  await loadStats()
  await loadCommands()
})
</script>

<style scoped>
.definition-cell {
  color: var(--text-tertiary);
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
  font-size: var(--text-xs);
  line-height: 1.5;
}
</style>
```

### Task 6: 重写 `CommandDetail.vue`（数据驱动分区）

**Files:**
- Modify (full rewrite): `platform-next/frontend/src/command_graph/CommandDetail.vue`

- [ ] **Step 1: 用下面完整内容覆写 `CommandDetail.vue`**

```vue
<template>
  <div v-if="command" class="detail-layout">
    <!-- Sidebar -->
    <div class="detail-sidebar">
      <div class="detail-sidebar-header">
        <button class="back-btn" @click="$router.push('/command-graph')">← 返回列表</button>
        <div class="sidebar-id">{{ command.command_name }}</div>
        <div class="sidebar-name">{{ command.command_name_zh }}</div>
      </div>

      <div class="sidebar-meta">
        <div class="sidebar-meta-row">
          <span class="sidebar-meta-label">产品</span>
          <el-tag size="small" effect="plain">{{ command.product }}</el-tag>
        </div>
        <div class="sidebar-meta-row">
          <span class="sidebar-meta-label">版本</span>
          <span class="sidebar-meta-value">{{ command.version || '-' }}</span>
        </div>
        <div class="sidebar-meta-row">
          <span class="sidebar-meta-label">分类</span>
          <span class="sidebar-meta-value" style="font-size: var(--text-xs)">{{ formatCategoryPath(command.category_path) }}</span>
        </div>
      </div>
    </div>

    <!-- Content -->
    <div class="detail-content">
      <div class="detail-content-inner">
        <el-tabs v-model="activeTab">
          <el-tab-pane label="抽取字段" name="fields">
            <!-- Hero header -->
            <div class="summary-hero">
              <div class="summary-hero-id">{{ command.command_name }}</div>
              <h1 class="summary-hero-name">{{ command.command_name_zh }}</h1>
              <div class="summary-hero-tags">
                <el-tag size="small" effect="plain">{{ command.product }}</el-tag>
                <el-tag size="small" effect="plain" type="info">{{ command.version || '-' }}</el-tag>
              </div>
            </div>

            <!-- Data-driven content sections -->
            <div v-for="section in sections" :key="section.key" class="summary-section">
              <div class="summary-section-title">{{ section.label }}</div>
              <div class="cmd-field-content" v-html="section.html"></div>
            </div>
            <div v-if="sections.length === 0" style="padding: 40px; text-align: center; color: var(--text-tertiary)">
              无抽取字段
            </div>
          </el-tab-pane>

          <el-tab-pane label="原始文档" name="doc">
            <div v-if="mdContent">
              <DocViewer :content="mdContent" :file-path="command.md_path || ''" api-base="command-graph" />
            </div>
            <div v-else style="padding: 60px; text-align: center; color: var(--text-tertiary); font-size: var(--text-sm)">
              {{ command.md_path ? '加载中...' : '无关联文档' }}
            </div>
          </el-tab-pane>
        </el-tabs>
      </div>
    </div>
  </div>
  <div v-else class="page-container">
    <div class="page-inner" style="text-align: center; padding-top: 80px">
      <div v-if="loading">加载中...</div>
      <div v-else>命令未找到: {{ product }}/{{ commandName }}</div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, computed, watch } from 'vue'
import { useRoute } from 'vue-router'
import { commandGraphApi, fetchJson } from '../api'
import DocViewer from '../shared/DocViewer.vue'
import { renderMarkdown } from '../shared/markdown'

const route = useRoute()
const product = computed(() => route.params.product as string)
const commandName = computed(() => route.params.commandName as string)

const loading = ref(true)
const command = ref<any>(null)
const mdContent = ref('')
const activeTab = ref('fields')

// === 身份槽位（渲染在 hero/sidebar，排除出动态分区）===
const ID_SLOTS = new Set([
  'command_name',
  'command_name_zh',
  'product',
  'version',
  'category_path',
])

// === 在 JSONL 里但暂不展示的字段（配置驱动；想展示则删掉对应 key）===
const HIDE_FIELDS = new Set(['parameter_description'])

// === 装饰性中文标题；未知 key 降级为原 key ===
const LABEL_MAP: Record<string, string> = {
  command_id: '命令ID',
  command_function: '命令功能',
  notes: '注意事项',
  permission_text: '操作用户权限',
  permission_groups: '权限组',
  usage_examples: '使用实例',
  output_description: '输出结果说明',
  output_ref_command: '输出引用命令',
  reference_info: '参考信息',
  verb: '动词',
  object_keyword: '对象关键字',
  command_category: '命令分类',
  is_dangerous: '是否高危',
  applicable_nf: '适用网元',
  max_records: '最大记录数',
  status: '状态',
  source_evidence_ids: '来源证据',
  md_path: '源文件路径',
  _review_status: '审查状态',
  _stage: '构建阶段',
  _derived_review: '派生审查',
}

function isNonEmpty(v: any): boolean {
  if (v === null || v === undefined) return false
  if (typeof v === 'string') return v.trim() !== ''
  if (Array.isArray(v)) return v.length > 0
  if (typeof v === 'object') return Object.keys(v).length > 0
  return true // bool / number（含 false / 0）视为有值，展示
}

/** 按 §4.2 规则把任意取值归一化为已渲染的 HTML。 */
function renderValue(v: any): string {
  if (Array.isArray(v)) {
    return v
      .map((el) =>
        renderMarkdown(
          el !== null && typeof el === 'object'
            ? '```json\n' + JSON.stringify(el, null, 2) + '\n```'
            : String(el)
        )
      )
      .join('\n')
  }
  if (v !== null && typeof v === 'object') {
    return renderMarkdown('```json\n' + JSON.stringify(v, null, 2) + '\n```')
  }
  if (typeof v === 'boolean') return renderMarkdown(v ? '是' : '否')
  if (typeof v === 'number') return renderMarkdown(String(v))
  return renderMarkdown(String(v))
}

const sections = computed(() => {
  if (!command.value) return []
  const out: { key: string; label: string; html: string }[] = []
  for (const key of Object.keys(command.value)) {
    if (ID_SLOTS.has(key) || HIDE_FIELDS.has(key)) continue
    const value = command.value[key]
    if (!isNonEmpty(value)) continue
    out.push({ key, label: LABEL_MAP[key] || key, html: renderValue(value) })
  }
  return out
})

function formatCategoryPath(raw: any): string {
  if (Array.isArray(raw)) return raw.join(' > ') || '-'
  if (!raw) return '-'
  return String(raw)
}

async function loadAll() {
  loading.value = true
  mdContent.value = ''
  try {
    const data = await fetchJson(commandGraphApi.command(product.value, commandName.value))
    command.value = data.error ? null : data

    if (command.value?.md_path) {
      const mdData = await fetchJson(commandGraphApi.commandMd(product.value, commandName.value))
      mdContent.value = mdData.content || ''
    }
  } finally {
    loading.value = false
  }
}

watch([product, commandName], () => {
  activeTab.value = 'fields'
  loadAll()
})

onMounted(loadAll)
</script>

<style scoped>
.cmd-field-content {
  font-size: var(--text-sm);
  color: var(--text-secondary);
  line-height: 1.7;
}
.cmd-field-content :deep(table) {
  border-collapse: collapse;
  width: 100%;
  margin: 8px 0;
}
.cmd-field-content :deep(th),
.cmd-field-content :deep(td) {
  border: 1px solid var(--border, #e2e8f0);
  padding: 6px 10px;
  text-align: left;
  font-size: var(--text-xs);
}
.cmd-field-content :deep(th) {
  background: var(--bg-secondary, #f8fafc);
}
.cmd-field-content :deep(pre) {
  background: var(--bg-secondary, #f8fafc);
  border: 1px solid var(--border, #e2e8f0);
  border-radius: var(--radius, 6px);
  padding: 10px 14px;
  font-size: var(--text-xs);
  line-height: 1.6;
  overflow-x: auto;
}
.cmd-field-content :deep(code) {
  font-family: 'JetBrains Mono', 'Fira Code', monospace;
}
</style>
```

- [ ] **Step 2: 类型检查 + 构建**

Run:
```bash
cd platform-next/frontend && npm run build
```
Expected: `vue-tsc --noEmit` 无类型错误，`vite build` 成功产出 `dist/`。

- [ ] **Step 3: （可选）提交前端改动**

```bash
git add platform-next/frontend/src/shared/markdown.ts platform-next/frontend/src/api.ts platform-next/frontend/src/command_graph/CommandList.vue platform-next/frontend/src/command_graph/CommandDetail.vue
git commit -m "feat: 命令图谱前端数据驱动字段展示 + 版本筛选"
```

---

## Chunk 3: 集成验证

### Task 7: 端到端 smoke

- [ ] **Step 1: 启动后端**

Run:
```bash
cd platform-next && python main.py
```
Expected: uvicorn 启动在 `0.0.0.0:8000`，无导入错误。

- [ ] **Step 2: 验证 API（新开终端或用 curl）**

Run:
```bash
curl -s "http://127.0.0.1:8000/api/v1/command-graph/stats"
curl -s "http://127.0.0.1:8000/api/v1/command-graph/commands?product=UDG&search=URR&size=3"
curl -s "http://127.0.0.1:8000/api/v1/command-graph/command?product=UDG&command_name=ADD%20URR"
curl -s "http://127.0.0.1:8000/api/v1/command-graph/command-md?product=UDG&command_name=ADD%20URR" | head -c 300
```
Expected: stats total=13075；commands 含 ADD URR；command 返回完整 record（含 notes/usage_examples 等）；command-md 返回非空 md。

- [ ] **Step 3: 前端手测**

Run: 在浏览器打开 `http://127.0.0.1:8000/`（dist 已挂载）或 `npm run dev` 后开 `:3000`/vite 端口。
验证清单：
1. `/command-graph` 列表加载，产品+版本下拉（版本含 20.15.2），搜索、分页正常。
2. 选产品=UDG + 版本=20.15.2，列表不变（单版本）。
3. 点击一行 → 详情页。
4. Tab1「抽取字段」：hero 显示命令名/中文名/产品/版本；下方分区按 record 顺序出现：命令功能 / 注意事项 / 操作用户权限 / 权限组 / 使用实例 / 输出结果说明 / 命令分类 / 是否高危 / 适用网元 …（稀疏字段仅在有值时出现）；参数说明（parameter_description）**不出现**；表格/代码块正常渲染。
5. Tab2「原始文档」：渲染原始 md，图片正常。
6. 控制台无报错。

- [ ] **Step 4: 数据驱动回归测试**

在 `mml_commands_udg.jsonl` 末尾临时追加一条含新字段的 record（如 `"zzz_test_field": "测试动态字段"`，command_id 用 `UDG@20.15.2:ZZZTEST`），重启服务，访问该命令详情，确认 Tab1 出现「zzz_test_field」分区（标题用原 key）。验证后删除该测试行。

Expected: 新字段零前端改动即出现分区。

---

## 回滚

后端：`git checkout platform-next/command_graph/{service,router}.py`
前端：`git checkout platform-next/frontend/src/` + 删除 `shared/markdown.ts`
