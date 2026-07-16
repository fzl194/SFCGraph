<template>
  <div class="object-index">
    <div class="search-box">
      <el-input
        v-model="q"
        placeholder="搜索 id / name…"
        size="small"
        clearable
        :prefix-icon="undefined"
        @input="onSearchDebounced"
        @clear="reload"
      />
    </div>

    <div v-if="loading" class="status muted">加载中…</div>
    <div v-else-if="!rows.length" class="status muted">
      {{ q ? '无匹配对象' : '（空）' }}
    </div>

    <el-scrollbar v-else class="tree-scroll">
      <el-tree
        :data="treeData"
        :props="{ label: 'label', children: 'children' }"
        node-key="key"
        :default-expand-all="false"
        :expand-on-click-node="false"
        :highlight-current="true"
        :current-node-key="selectedId"
        @node-click="onNodeClick"
      >
        <template #default="{ node: n, data: d }">
          <span class="tree-node" :class="{ isLeaf: !!d.id }">
            <span class="node-label">{{ n.label }}</span>
            <span v-if="d.count !== undefined" class="node-count">
              {{ d.count }}
            </span>
          </span>
        </template>
      </el-tree>
    </el-scrollbar>
  </div>
</template>

<script setup lang="ts">
import { ref, computed, onMounted, watch } from 'vue'
import { listObjects, type ObjectRow } from '../api'

const props = defineProps<{
  selectedId?: string
  // 父级强制刷新（如导入后）
  refreshKey?: number
}>()

const emit = defineEmits<{
  (e: 'select', id: string): void
}>()

const q = ref('')
const rows = ref<ObjectRow[]>([])
const loading = ref(false)
let debounceTimer: ReturnType<typeof setTimeout> | null = null

// 按 type 分组：每组 { type, items }；并按 type 字母序
const treeData = computed(() => {
  const groups = new Map<string, ObjectRow[]>()
  for (const r of rows.value) {
    const t = r.type || '(未分类)'
    if (!groups.has(t)) groups.set(t, [])
    groups.get(t)!.push(r)
  }
  const tree: TreeNode[] = []
  for (const [type, items] of [...groups.entries()].sort((a, b) =>
    a[0].localeCompare(b[0]),
  )) {
    items.sort((a, b) => a.id.localeCompare(b.id))
    tree.push({
      key: `g:${type}`,
      label: type,
      count: items.length,
      children: items.map((it) => ({
        key: `i:${it.id}`,
        id: it.id,
        label: shortLabel(it),
        raw: it,
      })),
    })
  }
  return tree
})

function shortLabel(r: ObjectRow): string {
  // 优先显示 frontmatter.name，否则用 id 去掉 type 前缀（slug 部分）
  if (r.name) return `${r.name}  ·  ${slugOf(r.id)}`
  return slugOf(r.id)
}

function slugOf(id: string): string {
  // id 形如 ObjectType@semantic-slug；显示 slug 部分
  const at = id.indexOf('@')
  return at >= 0 ? id.slice(at + 1) : id
}

async function reload() {
  loading.value = true
  try {
    rows.value = await listObjects({
      q: q.value || undefined,
      size: 5000, // v1：一次性拉全，前端分组；后续如量大再加分页
    })
  } catch (e) {
    console.error('[listObjects]', e)
    rows.value = []
  } finally {
    loading.value = false
  }
}

function onSearchDebounced() {
  if (debounceTimer) clearTimeout(debounceTimer)
  debounceTimer = setTimeout(reload, 250)
}

function onNodeClick(data: TreeNode) {
  if (data.id) emit('select', data.id)
}

interface TreeNode {
  key: string
  label: string
  id?: string
  count?: number
  children?: TreeNode[]
  raw?: ObjectRow
}

watch(
  () => props.refreshKey,
  () => reload(),
)

onMounted(reload)

defineExpose({ reload })
</script>

<style scoped>
.object-index {
  display: flex;
  flex-direction: column;
  height: 100%;
  background: #fff;
}
.search-box {
  padding: 8px;
  border-bottom: 1px solid #ebeef5;
}
.tree-scroll {
  flex: 1;
  min-height: 0;
}
.status {
  padding: 16px;
  text-align: center;
}
.muted {
  color: #909399;
  font-size: 13px;
}
.tree-node {
  display: flex;
  align-items: center;
  justify-content: space-between;
  width: 100%;
  padding-right: 8px;
}
.tree-node.isLeaf {
  cursor: pointer;
}
.node-label {
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}
.node-count {
  margin-left: 8px;
  font-size: 12px;
  color: #909399;
  background: #f4f4f5;
  border-radius: 8px;
  padding: 0 6px;
  min-width: 18px;
  text-align: center;
}
:deep(.el-tree-node__content) {
  height: 30px;
}
</style>
