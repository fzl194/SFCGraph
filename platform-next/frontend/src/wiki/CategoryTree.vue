<template>
  <div class="cat-tree">
    <el-input v-model="searchQ" size="small" placeholder="搜索对象名 / id…" clearable
              @keyup.enter="runSearch" @clear="clearSearch" class="cat-search">
      <template #append><el-button @click="runSearch">搜</el-button></template>
    </el-input>

    <el-tree v-if="!searchMode" :props="treeProps" lazy node-key="key"
             :load="loadLazy" highlight-current @node-click="onNodeClick" class="cat-el-tree">
      <template #default="{ data }">
        <span class="tnode">
          <span v-if="data.type === 'object'" class="tnode-obj">{{ data.label }}</span>
          <span v-else-if="data.type === 'type'" class="tnode-type">{{ data.label }}</span>
          <span v-else class="tnode-mid">{{ data.label }}</span>
        </span>
      </template>
    </el-tree>

    <div v-else class="cat-search-result">
      <div v-if="!searchHits.length" class="cat-empty">无匹配</div>
      <div v-for="h in searchHits" :key="h.path" class="cat-hit" @click="emit('select', h.path)">
        <span class="cat-hit-type" :class="typeClass(h.type)">{{ typeLabel(h.type) }}</span>
        <span class="cat-hit-name">{{ h.name }}</span>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { wikiApi, type Category, type ListItem } from './wikiApi'

const emit = defineEmits<{ (e: 'select', path: string): void }>()

const searchQ = ref('')
const searchMode = ref(false)
const searchHits = ref<ListItem[]>([])

const treeProps = { label: 'label', isLeaf: 'leaf' }

const TYPE_LABEL: Record<string, string> = {
  MMLCommand: '命令', ConfigObject: '配置对象', Feature: '特性',
  License: 'License', Task: '任务', BusinessDomain: '业务层',
}
const GROUP_FIELD: Record<string, string> = {
  MMLCommand: 'category_path', ConfigObject: 'object_kind',
  Feature: 'parent_feature_code', License: 'applicable_nf', Task: 'task_layer',
}

function typeLabel(t?: string) { return (t && TYPE_LABEL[t]) || (t || '?') }
function typeClass(t?: string) { return t ? `cat-hit-type--${t}` : '' }

// 全懒加载：每层（含 root）都经 :load 取数，避免内联 children 与 lazy 冲突。
async function loadLazy(node: { level: number; data?: any }, resolve: (data: any[]) => void) {
  if (node.level === 0) {
    let cats: Category[] = []
    try { cats = await wikiApi.categories() } catch { return resolve([]) }
    return resolve(cats.map((c) => ({
      key: `t:${c.type}`, label: `${TYPE_LABEL[c.type] ?? c.type}`, type: 'type', raw: c, leaf: false,
    })))
  }
  const data = node.data || {}
  if (data.type === 'type') {
    return resolve(data.raw.nfs.map((n: any) => ({
      key: `n:${data.raw.type}:${n.nf}`, label: n.nf, type: 'nf',
      raw: { type: data.raw.type, nf: n.nf, versions: n.versions }, leaf: false,
    })))
  }
  if (data.type === 'nf') {
    return resolve(data.raw.versions.map((v: any) => ({
      key: `v:${data.raw.type}:${data.raw.nf}:${v.version}`, label: `${v.version} (${v.count})`, type: 'version',
      raw: { type: data.raw.type, nf: data.raw.nf, version: v.version }, leaf: false,
    })))
  }
  if (data.type === 'version') {
    let buckets: { key: string; count: number }[] = []
    try { buckets = await wikiApi.group(data.raw.type, data.raw.nf, data.raw.version) } catch { return resolve([]) }
    return resolve(buckets.map((b) => ({
      key: `g:${data.raw.type}:${data.raw.nf}:${data.raw.version}:${b.key}`,
      label: `${b.key} (${b.count})`, type: 'group',
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
  resolve([])
}

function onNodeClick(data: any) {
  if (data.type === 'object') emit('select', data.raw.path)
}

async function runSearch() {
  if (!searchQ.value.trim()) return
  searchMode.value = true
  try { searchHits.value = await wikiApi.search(searchQ.value.trim()) } catch { searchHits.value = [] }
}
function clearSearch() { searchMode.value = false; searchHits.value = [] }
</script>

<style scoped>
.cat-tree { display: flex; flex-direction: column; gap: var(--space-2); padding: var(--space-3); flex: 1; min-height: 0; overflow: auto; }

/* el-tree — quiet, token-driven */
.cat-el-tree { background: transparent; flex: 1; --el-tree-node-hover-bg-color: transparent; }
.cat-el-tree :deep(.el-tree-node__content) {
  height: 30px;
  border-radius: var(--radius-sm);
  padding-left: var(--space-1) !important;
  transition: background var(--duration) var(--ease);
}
.cat-el-tree :deep(.el-tree-node__content:hover) { background: var(--accent-soft); }
.cat-el-tree :deep(.el-tree-node.is-current > .el-tree-node__content) {
  background: var(--accent-soft);
  box-shadow: inset 2px 0 0 var(--accent);
}
.cat-el-tree :deep(.el-tree-node__expand-icon) { color: var(--text-tertiary); font-size: 11px; }

.tnode { display: flex; align-items: center; gap: var(--space-1); overflow: hidden; }
.tnode-type {
  font-size: var(--text-sm); font-weight: 700; color: var(--text-primary);
  letter-spacing: -0.005em;
}
.tnode-mid {
  font-size: var(--text-xs); color: var(--text-secondary);
  font-family: var(--font-mono);
}
.tnode-obj {
  font-size: var(--text-sm); color: var(--text-primary); font-weight: 500;
  overflow: hidden; text-overflow: ellipsis; white-space: nowrap;
}
.cat-el-tree :deep(.el-tree-node__content:hover) .tnode-obj { color: var(--accent); }

/* search results */
.cat-search-result { display: flex; flex-direction: column; gap: 2px; margin-top: var(--space-1); }
.cat-hit {
  display: flex; align-items: center; gap: var(--space-2);
  padding: var(--space-2); cursor: pointer; border-radius: var(--radius-sm);
  transition: background var(--duration) var(--ease);
}
.cat-hit:hover { background: var(--accent-soft); }
.cat-hit-type {
  font-size: var(--text-2xs); font-weight: 600; color: var(--text-tertiary);
  background: var(--bg-page); padding: 1px 6px; border-radius: var(--radius-sm);
  flex-shrink: 0; border: 1px solid var(--border);
}
.cat-hit-type--MMLCommand { color: #0891b2; }
.cat-hit-type--ConfigObject { color: #7c3aed; }
.cat-hit-type--Feature { color: #0d9488; }
.cat-hit-type--License { color: #d97706; }
.cat-hit-type--Task { color: #db2777; }
.cat-hit-name { font-size: var(--text-sm); color: var(--text-primary); overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
.cat-empty { color: var(--text-tertiary); font-size: var(--text-sm); padding: var(--space-4); text-align: center; }
</style>
