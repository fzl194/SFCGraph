<template>
  <div class="cat">
    <div class="cat-head">
      <span class="cat-head-title">对象浏览</span>
      <button class="cat-refresh" title="刷新树" @click="refresh">↻</button>
    </div>

    <el-input v-model="searchQ" size="small" placeholder="搜索对象名 / id…" clearable
              @keyup.enter="runSearch" @clear="clearSearch" class="cat-search">
      <template #append><el-button @click="runSearch">搜</el-button></template>
    </el-input>

    <div class="cat-body">
      <el-tree v-if="!searchMode" :key="treeVersion" ref="treeRef" :props="treeProps" lazy node-key="key"
               :load="loadLazy" highlight-current @node-click="onNodeClick" class="cat-el-tree"
               :indent="14">
        <template #default="{ data }">
          <!-- 类型：色条 + 名称 + 总数徽章 -->
          <span v-if="data.type === 'type'" class="tnode tnode--type">
            <span class="tnode-bar" :style="{ background: typeColor(data.raw.type) }"></span>
            <span class="tnode-type-name">{{ typeLabel(data.raw.type) }}</span>
            <span class="tnode-badge">{{ typeCount(data.raw) }}</span>
          </span>
          <!-- NF -->
          <span v-else-if="data.type === 'nf'" class="tnode tnode--mono">{{ data.label }}</span>
          <!-- 版本 -->
          <span v-else-if="data.type === 'version'" class="tnode tnode--mono tnode--version">{{ data.label }}</span>
          <!-- 分组桶 -->
          <span v-else-if="data.type === 'group'" class="tnode tnode--group">{{ data.label }}</span>
          <!-- 业务层 bucket -->
          <span v-else-if="data.type === 'biz-bucket'" class="tnode tnode--biz">
            <span class="tnode-bar" :style="{ background: typeColor(rawType(data.raw.type)) }"></span>
            <span class="tnode-biz-name">{{ data.label }}</span>
            <span class="tnode-badge">{{ data.raw.count }}</span>
          </span>
          <!-- 对象叶子 -->
          <span v-else-if="data.type === 'object'" class="tnode tnode--obj">
            <span class="tnode-obj-dot" :style="{ background: objDotColor(data.raw.path) }"></span>
            <span class="tnode-obj-name">{{ data.label }}</span>
          </span>
          <span v-else class="tnode">{{ data.label }}</span>
        </template>
      </el-tree>

      <div v-else class="cat-search-result">
        <div v-if="!searchHits.length" class="cat-empty">无匹配</div>
        <div v-for="h in searchHits" :key="h.path" class="cat-hit" @click="emit('select', h.path)">
          <span class="cat-hit-dot" :style="{ background: typeColor(h.type) }"></span>
          <span class="cat-hit-type" :style="{ color: typeColor(h.type) }">{{ typeLabel(h.type) }}</span>
          <span class="cat-hit-name">{{ h.name }}</span>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, watch, nextTick } from 'vue'
import { wikiApi, type Category, type ListItem, type LocateResp } from './wikiApi'
import { GROUP_FIELD, BUSINESS_TYPES, typeColor, typeLabel, taskLayerColor } from './wikiTokens'

const props = defineProps<{ currentPath: string | null }>()
const emit = defineEmits<{ (e: 'select', path: string): void }>()

const searchQ = ref('')
const searchMode = ref(false)
const searchHits = ref<ListItem[]>([])
const treeVersion = ref(0)
const treeRef = ref<any>(null)

const treeProps = { label: 'label', isLeaf: 'leaf' }

function typeCount(cat: Category): number {
  // 业务层 buckets 直接 sum 计数；产品层 nf→version→count 累加
  if (cat.buckets) return cat.buckets.reduce((s, b) => s + b.count, 0)
  return cat.nfs.reduce((s, n) => s + n.versions.reduce((a, v) => a + v.count, 0), 0)
}
/** 从对象 path 推断类型（command/...→MMLCommand），用于叶子的类型色点 */
function parentType(path: string): string {
  const top = path.split('/', 1)[0]
  return { command: 'MMLCommand', configobject: 'ConfigObject', feature: 'Feature', license: 'License', task: 'Task' }[top] || ''
}
/** Task 叶子按 task_layer（前缀 0-/1-/2-）取同色系深浅；其他对象按 type 色 */
function objDotColor(path: string): string {
  if (path.startsWith('task/')) {
    // task/UDG/20.15.2/0-00001.md → layer='0-'
    const m = path.match(/task\/[^/]+\/[^/]+\/(\d-)/)
    if (m) return taskLayerColor(m[1])
  }
  return typeColor(parentType(path))
}
/** biz-bucket 节点的 data.raw.type 在不同层：type层=字符串；biz-bucket层=包装对象。统一取出。 */
function rawType(t: any): string {
  return typeof t === 'string' ? t : (t?.type || '')
}

// 全懒加载：每层（含 root）经 :load 取数。
async function loadLazy(node: { level: number; data?: any }, resolve: (data: any[]) => void) {
  if (node.level === 0) {
    let cats: Category[] = []
    try { cats = await wikiApi.categories() } catch { return resolve([]) }
    return resolve(cats.map((c) => ({
      key: `t:${c.type}`, label: typeLabel(c.type), type: 'type', raw: c, leaf: false,
    })))
  }
  const data = node.data || {}
  // 业务层：type→buckets（domain[/scenario]），无 nfs/version；展开 bucket 触发对象列表
  if (data.type === 'type' && BUSINESS_TYPES.has(data.raw.type) && data.raw.buckets) {
    return resolve(data.raw.buckets.map((b: any) => ({
      key: `biz:${data.raw.type}:${b.key}`, label: `${b.key} · ${b.count}`, type: 'biz-bucket',
      raw: { type: data.raw.type, bucket_key: b.key, count: b.count }, leaf: false,
    })))
  }
  if (data.type === 'type') {
    return resolve(data.raw.nfs.map((n: any) => ({
      key: `n:${data.raw.type}:${n.nf}`, label: n.nf, type: 'nf',
      raw: { type: data.raw.type, nf: n.nf, versions: n.versions }, leaf: false,
    })))
  }
  if (data.type === 'nf') {
    return resolve(data.raw.versions.map((v: any) => ({
      key: `v:${data.raw.type}:${data.raw.nf}:${v.version}`,
      label: `${v.version} · ${v.count}`, type: 'version',
      raw: { type: data.raw.type, nf: data.raw.nf, version: v.version }, leaf: false,
    })))
  }
  if (data.type === 'version') {
    let buckets: { key: string; count: number }[] = []
    try { buckets = await wikiApi.group(data.raw.type, data.raw.nf, data.raw.version) } catch { return resolve([]) }
    return resolve(buckets.map((b) => ({
      key: `g:${data.raw.type}:${data.raw.nf}:${data.raw.version}:${b.key}`,
      label: `${b.key} · ${b.count}`, type: 'group',
      raw: { ...data.raw, group_field: GROUP_FIELD[data.raw.type], group_value: b.key }, leaf: false,
    })))
  }
  if (data.type === 'group') {
    let res: { items: ListItem[]; total: number } = { items: [], total: 0 }
    try {
      res = await wikiApi.list({
        type: data.raw.type, nf: data.raw.nf, version: data.raw.version,
        group_field: data.raw.group_field, group_value: data.raw.group_value, size: 500,
      })
    } catch { return resolve([]) }
    return resolve(res.items.map((it) => ({
      key: `o:${it.path}`, label: it.name, type: 'object', raw: it, leaf: true,
    })))
  }
  // 业务层 bucket（domain[/scenario]）→ 列出该 bucket 下所有对象（按 type+bucket 精确取）
  if (data.type === 'biz-bucket') {
    let items: ListItem[] = []
    try { items = await wikiApi.listBusiness(data.raw.type, data.raw.bucket_key) } catch { return resolve([]) }
    return resolve(items.map((it) => ({
      key: `o:${it.path}`, label: it.name, type: 'object', raw: it, leaf: true,
    })))
  }
  resolve([])
}

function onNodeClick(data: any) {
  if (data.type === 'object') emit('select', data.raw.path)
}

// 同步：跳转到新对象时，左树逐层展开并高亮（evidence 等不可分类对象跳过）
watch(() => props.currentPath, async (p) => {
  if (!p || !treeRef.value) return
  if (searchMode.value) return                       // 搜索态不打断
  if (p.startsWith('evidence/')) return              // 证据不在树内
  const objKey = `o:${p}`
  // 已在树里加载过 → 直接高亮
  if (treeRef.value.getNode?.(objKey)) { treeRef.value.setCurrentKey?.(objKey); return }
  // 否则向 /locate 取位置，逐层展开祖先再高亮
  let loc: LocateResp | null = null
  try { loc = await wikiApi.locate(p) } catch { return }
  if (!loc) return
  let ancestors: string[]
  if (loc.business) {
    // 业务层：t:{type} → biz:{type}:{bucket_key}
    ancestors = [`t:${loc.type}`, `biz:${loc.type}:${loc.bucket_key}`]
  } else {
    if (!loc.nf || !loc.version || !loc.group_value) return
    ancestors = [
      `t:${loc.type}`,
      `n:${loc.type}:${loc.nf}`,
      `v:${loc.type}:${loc.nf}:${loc.version}`,
      `g:${loc.type}:${loc.nf}:${loc.version}:${loc.group_value}`,
    ]
  }
  for (const k of ancestors) {
    const n = treeRef.value.getNode?.(k)
    if (!n) return
    if (!n.expanded) {
      if (typeof n.expand === 'function') n.expand()
      else n.expanded = true
    }
    if (!n.loaded) await waitLoaded(n)
  }
  await nextTick()
  const obj = treeRef.value.getNode?.(objKey)
  if (obj) treeRef.value.setCurrentKey?.(objKey)
})

function waitLoaded(node: any, timeout = 4000): Promise<void> {
  return new Promise((resolve) => {
    if (node.loaded) return resolve()
    const t0 = Date.now()
    const iv = setInterval(() => {
      if (node.loaded || Date.now() - t0 > timeout) { clearInterval(iv); resolve() }
    }, 30)
  })
}

function refresh() { treeVersion.value++ }   // :key 变 → el-tree 重建 → 重新懒载 categories
function runSearch() {
  if (!searchQ.value.trim()) return
  searchMode.value = true
  wikiApi.search(searchQ.value.trim()).then((r) => (searchHits.value = r)).catch(() => (searchHits.value = []))
}
function clearSearch() { searchMode.value = false; searchHits.value = [] }

defineExpose({ refresh })
</script>

<style scoped>
.cat { display: flex; flex-direction: column; height: 100%; min-height: 0; }

.cat-head {
  display: flex; align-items: center; justify-content: space-between;
  padding: var(--space-4) var(--space-4) var(--space-2);
  flex-shrink: 0;
}
.cat-head-title {
  font-size: var(--text-2xs); font-weight: 700; color: var(--text-tertiary);
  text-transform: uppercase; letter-spacing: 0.1em;
}
.cat-refresh {
  border: 1px solid var(--border); background: var(--bg-card); color: var(--text-tertiary);
  width: 24px; height: 24px; border-radius: var(--radius-sm); cursor: pointer; font-size: 13px;
  line-height: 1; display: flex; align-items: center; justify-content: center;
  transition: all var(--duration) var(--ease);
}
.cat-refresh:hover { color: var(--accent); border-color: var(--accent); background: var(--accent-soft); transform: rotate(-60deg); }

.cat-search { margin: 0 var(--space-4) var(--space-2); flex-shrink: 0; }

.cat-body { flex: 1; min-height: 0; overflow-y: auto; padding: 0 var(--space-2) var(--space-3); }

/* el-tree */
.cat-el-tree { background: transparent; --el-tree-node-hover-bg-color: transparent; }
.cat-el-tree :deep(.el-tree-node) { position: relative; }
.cat-el-tree :deep(.el-tree-node__content) {
  height: 30px; border-radius: var(--radius-sm); padding-left: var(--space-1) !important;
  transition: background var(--duration) var(--ease);
}
.cat-el-tree :deep(.el-tree-node__content:hover) { background: var(--accent-soft); }
.cat-el-tree :deep(.el-tree-node.is-current > .el-tree-node__content) {
  background: var(--accent-soft);
  box-shadow: inset 2px 0 0 var(--accent);
}
.cat-el-tree :deep(.el-tree-node__expand-icon) { color: var(--text-tertiary); font-size: 11px; }
.cat-el-tree :deep(.el-tree-node__expand-icon.leaf) { display: none; }

/* node rows */
.tnode { display: flex; align-items: center; gap: var(--space-2); overflow: hidden; min-width: 0; }
.tnode--type { padding: 2px 0; }
.tnode-bar { width: 3px; height: 14px; border-radius: 2px; flex-shrink: 0; }
.tnode-type-name { font-size: var(--text-sm); font-weight: 700; color: var(--text-primary); letter-spacing: -0.005em; }
.tnode-badge {
  font-size: var(--text-2xs); font-weight: 600; color: var(--text-tertiary);
  background: var(--bg-page); border: 1px solid var(--border);
  padding: 0 6px; border-radius: 10px; line-height: 16px; flex-shrink: 0;
}
.tnode--mono, .tnode--version { font-family: var(--font-mono); font-size: var(--text-xs); color: var(--text-secondary); }
.tnode--version { color: var(--text-tertiary); }
.tnode--group { font-size: var(--text-xs); color: var(--text-secondary); overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
.tnode--biz { gap: var(--space-2); }
.tnode-biz-name { font-size: var(--text-xs); color: var(--text-primary); overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
.tnode--obj { width: 100%; }
.tnode-obj-dot { width: 6px; height: 6px; border-radius: 50%; flex-shrink: 0; }
.tnode-obj-name { font-size: var(--text-sm); color: var(--text-primary); overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
.cat-el-tree :deep(.el-tree-node__content:hover) .tnode-obj-name { color: var(--accent); }

/* search */
.cat-search-result { display: flex; flex-direction: column; gap: 1px; padding: var(--space-2) var(--space-4); }
.cat-hit {
  display: flex; align-items: center; gap: var(--space-2);
  padding: var(--space-2); cursor: pointer; border-radius: var(--radius-sm);
  transition: background var(--duration) var(--ease);
}
.cat-hit:hover { background: var(--accent-soft); }
.cat-hit-dot { width: 6px; height: 6px; border-radius: 50%; flex-shrink: 0; }
.cat-hit-type { font-size: var(--text-2xs); font-weight: 600; flex-shrink: 0; }
.cat-hit-name { font-size: var(--text-sm); color: var(--text-primary); overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
.cat-empty { color: var(--text-tertiary); font-size: var(--text-sm); padding: var(--space-4); text-align: center; }
</style>
