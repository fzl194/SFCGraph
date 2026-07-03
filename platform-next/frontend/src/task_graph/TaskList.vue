<template>
  <!-- 筛选条：层级 select + 搜索框 -->
  <div class="filter-bar">
    <el-select
      v-model="filters.layer"
      placeholder="层级"
      size="small"
      style="width: 140px"
      @change="onLayerChange"
    >
      <el-option label="全部层级" value="" />
      <el-option label="atom" value="atom" />
      <el-option label="compound" value="compound" />
      <el-option label="feature" value="feature" />
      <el-option label="solution" value="solution" />
      <el-option label="generalized" value="generalized" />
    </el-select>
    <el-input
      v-model="filters.search"
      placeholder="搜索 task_id / 逻辑名 / 意图..."
      clearable
      size="small"
      style="width: 280px"
      @input="debouncedSearch"
    />
    <span class="filter-count">{{ total }} 条任务</span>
  </div>

  <el-alert
    v-if="error"
    :title="error"
    type="error"
    show-icon
    :closable="false"
    style="margin-bottom: var(--space-4)"
  />

  <!-- Table -->
  <div class="card" style="overflow: hidden">
    <el-table
      :data="tasks"
      :default-sort="{ prop: 'task_id', order: 'ascending' }"
      @row-click="onRowClick"
      style="width: 100%"
      v-loading="loading"
      size="small"
    >
      <el-table-column prop="task_id" label="任务ID" width="120" sortable>
        <template #default="{ row }">
          <span class="task-id-cell">{{ row.task_id }}</span>
        </template>
      </el-table-column>
      <el-table-column prop="task_logical_name" label="逻辑名" min-width="180" sortable>
        <template #default="{ row }">
          <span class="task-name-cell">{{ row.task_logical_name || '-' }}</span>
        </template>
      </el-table-column>
      <el-table-column prop="task_layer" label="层级" width="120" sortable>
        <template #default="{ row }">
          <el-tag size="small" effect="plain" :type="layerTagType(row.task_layer)">{{ row.task_layer || '-' }}</el-tag>
        </template>
      </el-table-column>
      <el-table-column prop="task_category" label="分类" width="140">
        <template #default="{ row }">
          <span style="font-size: var(--text-xs); color: var(--text-secondary)">{{ row.task_category || '-' }}</span>
        </template>
      </el-table-column>
      <el-table-column prop="status" label="状态" width="100" sortable>
        <template #default="{ row }">
          <el-tag size="small" :type="statusTagType(row.status)" effect="dark">{{ row.status || '-' }}</el-tag>
        </template>
      </el-table-column>
      <el-table-column label="ref 跨图谱" width="170">
        <template #default="{ row }">
          <span v-if="row.ref_type" class="task-ref-cell">{{ row.ref_type }}:{{ row.ref_value }}</span>
          <span v-else style="color: var(--text-tertiary)">-</span>
        </template>
      </el-table-column>
      <el-table-column label="DP·规则·关系" width="130" align="center">
        <template #default="{ row }">
          <span class="task-counts">
            <span :title="`决策点 ${row.n_dps}`">{{ row.n_dps }}</span>
            <span class="task-counts-sep">/</span>
            <span :title="`规则 ${row.n_rules}`">{{ row.n_rules }}</span>
            <span class="task-counts-sep">/</span>
            <span :title="`关系 ${row.n_relations}`">{{ row.n_relations }}</span>
          </span>
        </template>
      </el-table-column>
      <el-table-column prop="task_intent" label="意图" min-width="260">
        <template #default="{ row }">
          <span class="definition-cell">{{ truncate(row.task_intent, 100) || '-' }}</span>
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
        @current-change="loadTasks"
        @size-change="onSizeChange"
      />
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, computed, watch } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { taskGraphApi, fetchJson } from '../api'

// ===== 列表项类型（与后端 _slim 对齐）=====
interface TaskSlim {
  task_id: string
  task_logical_name: string
  task_layer: string
  task_intent: string
  task_category: string
  nf: string
  version: string
  status: string
  ref_type: string
  ref_value: string
  n_params: number
  n_relations: number
  n_rules: number
  n_dps: number
}
interface TaskListResp {
  items: TaskSlim[]
  total: number
  page: number
  size: number
}

const route = useRoute()
const router = useRouter()
const loading = ref(false)
const error = ref('')
const tasks = ref<TaskSlim[]>([])
const total = ref(0)
const page = ref(1)
const size = ref(50)

const filters = ref({ layer: '', search: '' })

// 范围由路由固定：nf + version
const nf = computed(() => route.params.nf as string)
const version = computed(() => route.params.version as string)

let searchTimer: ReturnType<typeof setTimeout> | null = null
function debouncedSearch() {
  if (searchTimer) clearTimeout(searchTimer)
  searchTimer = setTimeout(() => { page.value = 1; loadTasks() }, 300)
}

function onLayerChange() {
  page.value = 1
  loadTasks()
}

function onSizeChange() {
  page.value = 1
  loadTasks()
}

function truncate(s: string, n: number) {
  if (!s) return ''
  return s.length > n ? s.slice(0, n) + '...' : s
}

// 层级 tag 配色：atom 最具体（accent），generalized 最抽象（紫）
function layerTagType(layer: string): 'primary' | 'success' | 'warning' | 'info' | 'danger' {
  switch ((layer || '').toLowerCase()) {
    case 'atom': return 'primary'
    case 'compound': return 'success'
    case 'feature': return 'warning'
    case 'solution': return 'info'
    case 'generalized': return 'danger'
    default: return 'info'
  }
}

// 状态配色：active=success, inferred=warning, draft=info
function statusTagType(status: string): 'success' | 'warning' | 'info' | 'danger' | 'primary' {
  switch ((status || '').toLowerCase()) {
    case 'active': return 'success'
    case 'inferred': return 'warning'
    case 'draft': return 'info'
    default: return 'info'
  }
}

function onRowClick(row: TaskSlim) {
  router.push({
    name: 'task-detail',
    params: { nf: nf.value, version: version.value, taskId: row.task_id },
  })
}

async function loadTasks() {
  loading.value = true
  error.value = ''
  try {
    const params = new URLSearchParams()
    params.set('nf', nf.value)
    params.set('version', version.value)
    params.set('page', String(page.value))
    params.set('size', String(size.value))
    if (filters.value.layer) params.set('layer', filters.value.layer)
    if (filters.value.search) params.set('search', filters.value.search)
    const data = await fetchJson(`${taskGraphApi.tasks}?${params}`) as TaskListResp
    tasks.value = data.items || []
    total.value = data.total || 0
  } catch (e) {
    error.value = '加载任务列表失败：' + (e instanceof Error ? e.message : String(e))
  } finally {
    loading.value = false
  }
}

// 路由参数变化时（切到别的 nf/version）重置并重载
watch([nf, version], () => {
  page.value = 1
  filters.value.layer = ''
  filters.value.search = ''
  loadTasks()
})

onMounted(loadTasks)
</script>

<style scoped>
.task-id-cell {
  font-family: var(--font-mono);
  font-size: var(--text-xs);
  color: var(--accent);
  font-weight: 600;
}
.task-name-cell {
  font-size: var(--text-sm);
  color: var(--text-primary);
  font-weight: 500;
}
.task-ref-cell {
  font-family: var(--font-mono);
  font-size: var(--text-2xs);
  color: var(--text-secondary);
}
.task-counts {
  font-family: var(--font-mono);
  font-size: var(--text-xs);
  color: var(--text-secondary);
  display: inline-flex;
  align-items: center;
  gap: 2px;
}
.task-counts-sep {
  color: var(--text-tertiary);
  margin: 0 2px;
}
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
