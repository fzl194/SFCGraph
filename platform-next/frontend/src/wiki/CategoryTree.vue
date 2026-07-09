<template>
  <div class="cat-tree">
    <el-input v-model="searchQ" size="small" placeholder="搜索对象名/id…" clearable
              @keyup.enter="runSearch" @clear="clearSearch" class="cat-search">
      <template #append><el-button @click="runSearch">搜</el-button></template>
    </el-input>

    <el-tree v-if="!searchMode" :data="treeData" :props="treeProps" lazy node-key="key"
             @node-expand="onExpand" :load="loadLazy" highlight-current
             @node-click="onNodeClick" ref="treeRef" />
    <div v-else class="cat-search-result">
      <div v-if="!searchHits.length" class="cat-empty">无匹配</div>
      <div v-for="h in searchHits" :key="h.path" class="cat-hit" @click="$emit('select', h.path)">
        <span class="cat-hit-type">[{{ h.type }}]</span> {{ h.name }}
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { wikiApi, type Category, type ListItem } from './wikiApi'

const emit = defineEmits<{ (e: 'select', path: string): void }>()

const searchQ = ref('')
const searchMode = ref(false)
const searchHits = ref<ListItem[]>([])
const treeData = ref<any[]>([])
const treeRef = ref<any>(null)
const treeProps = { label: 'label', isLeaf: 'leaf' }

const TYPE_LABEL: Record<string, string> = {
  MMLCommand: '命令', ConfigObject: '配置对象', Feature: '特性',
  License: 'License', Task: '任务', BusinessDomain: '业务层',
}
const GROUP_FIELD: Record<string, string> = {
  MMLCommand: 'category_path', ConfigObject: 'object_kind',
  Feature: 'parent_feature_code', License: 'applicable_nf', Task: 'task_layer',
}

onMounted(async () => {
  const cats = await wikiApi.categories()
  treeData.value = cats.map((c: Category) => ({
    key: `t:${c.type}`, label: `${TYPE_LABEL[c.type] ?? c.type}`, type: 'type',
    raw: c, children: c.nfs.map(n => ({
      key: `n:${c.type}:${n.nf}`, label: n.nf, type: 'nf',
      raw: { type: c.type, nf: n.nf, versions: n.versions }, leaf: false,
    })),
  }))
})

// Element Plus el-tree lazy load signature: (node, resolve)
function loadLazy(node: { data?: any }, resolve: (data: any[]) => void) {
  const data = node.data
  if (!data) { resolve([]); return }
  void doLoadLazy(data, resolve)
}

async function doLoadLazy(data: any, resolve: (data: any[]) => void) {
  // nf -> version 列表
  if (data.type === 'nf') {
    resolve(data.raw.versions.map((v: { version: string; count: number }) => ({
      key: `v:${data.raw.type}:${data.raw.nf}:${v.version}`, label: v.version, type: 'version',
      raw: { type: data.raw.type, nf: data.raw.nf, version: v.version, count: v.count }, leaf: false,
    })))
    return
  }
  // version -> 分组桶（懒加载调 /group）
  if (data.type === 'version') {
    const buckets = await wikiApi.group(data.raw.type, data.raw.nf, data.raw.version)
    resolve(buckets.map(b => ({
      key: `g:${data.raw.type}:${data.raw.nf}:${data.raw.version}:${b.key}`,
      label: `${b.key} (${b.count})`,
      type: 'group',
      raw: { ...data.raw, group_field: GROUP_FIELD[data.raw.type], group_value: b.key },
      leaf: false,
    })))
    return
  }
  // group -> 对象叶子（懒加载调 /list）
  if (data.type === 'group') {
    const res = await wikiApi.list({ type: data.raw.type, nf: data.raw.nf, version: data.raw.version,
      group_field: data.raw.group_field, group_value: data.raw.group_value, size: 500 })
    resolve(res.items.map(it => ({ key: `o:${it.path}`, label: it.name, type: 'object', raw: it, leaf: true })))
    return
  }
  resolve([])
}

function onExpand(_n: any, _info: any) {}
function onNodeClick(node: any) { if (node.type === 'object') emit('select', node.raw.path) }

async function runSearch() {
  if (!searchQ.value.trim()) return
  searchMode.value = true
  searchHits.value = await wikiApi.search(searchQ.value.trim())
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
