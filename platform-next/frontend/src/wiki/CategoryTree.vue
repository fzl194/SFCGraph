<template>
  <div class="cat-tree">
    <el-input v-model="searchQ" size="small" placeholder="搜索对象名/id…" clearable
              @keyup.enter="runSearch" @clear="clearSearch" class="cat-search">
      <template #append><el-button @click="runSearch">搜</el-button></template>
    </el-input>

    <el-tree v-if="!searchMode" :props="treeProps" lazy node-key="key"
             :load="loadLazy" highlight-current @node-click="onNodeClick" />
    <div v-else class="cat-search-result">
      <div v-if="!searchHits.length" class="cat-empty">无匹配</div>
      <div v-for="h in searchHits" :key="h.path" class="cat-hit" @click="emit('select', h.path)">
        <span class="cat-hit-type">[{{ h.type || '?' }}]</span> {{ h.name }}
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

// 全懒加载：每层（含 root）都经 :load 取数，避免内联 children 与 lazy 冲突。
async function loadLazy(node: { level: number; data?: any }, resolve: (data: any[]) => void) {
  // root：加载对象类型
  if (node.level === 0) {
    let cats: Category[] = []
    try { cats = await wikiApi.categories() } catch { return resolve([]) }
    return resolve(cats.map((c) => ({
      key: `t:${c.type}`, label: `${TYPE_LABEL[c.type] ?? c.type}`, type: 'type', raw: c, leaf: false,
    })))
  }
  const data = node.data || {}
  // type -> nf
  if (data.type === 'type') {
    return resolve(data.raw.nfs.map((n: any) => ({
      key: `n:${data.raw.type}:${n.nf}`, label: n.nf, type: 'nf',
      raw: { type: data.raw.type, nf: n.nf, versions: n.versions }, leaf: false,
    })))
  }
  // nf -> version
  if (data.type === 'nf') {
    return resolve(data.raw.versions.map((v: any) => ({
      key: `v:${data.raw.type}:${data.raw.nf}:${v.version}`, label: `${v.version} (${v.count})`, type: 'version',
      raw: { type: data.raw.type, nf: data.raw.nf, version: v.version }, leaf: false,
    })))
  }
  // version -> 分组桶（/group）
  if (data.type === 'version') {
    let buckets: { key: string; count: number }[] = []
    try { buckets = await wikiApi.group(data.raw.type, data.raw.nf, data.raw.version) } catch { return resolve([]) }
    return resolve(buckets.map((b) => ({
      key: `g:${data.raw.type}:${data.raw.nf}:${data.raw.version}:${b.key}`,
      label: `${b.key} (${b.count})`, type: 'group',
      raw: { ...data.raw, group_field: GROUP_FIELD[data.raw.type], group_value: b.key }, leaf: false,
    })))
  }
  // group -> 对象叶子（/list）
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
.cat-tree { display: flex; flex-direction: column; gap: 8px; }
.cat-search-result { display: flex; flex-direction: column; gap: 4px; }
.cat-hit { padding: 4px 6px; cursor: pointer; border-radius: 4px; font-size: 13px; }
.cat-hit:hover { background: var(--bg-hover, #f0f5ff); }
.cat-hit-type { color: #7c3aed; font-size: 11px; }
.cat-empty { color: var(--text-tertiary); font-size: 13px; padding: 8px; }
</style>
