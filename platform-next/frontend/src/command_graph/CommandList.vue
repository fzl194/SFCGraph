<template>
  <!-- 筛选条：版本范围已由路由固定，只保留版本内搜索 -->
  <div class="filter-bar">
    <el-input
      v-model="filters.search"
      placeholder="搜索命令名 / 中文名 / 功能..."
      clearable
      size="small"
      style="width: 280px"
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
      <el-table-column prop="nf" label="网元" width="90" sortable>
        <template #default="{ row }">
          <el-tag size="small" effect="plain">{{ row.nf }}</el-tag>
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
import { ref, onMounted, computed, watch } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { commandGraphApi, fetchJson } from '../api'

const route = useRoute()
const router = useRouter()
const loading = ref(false)
const commands = ref<any[]>([])
const total = ref(0)
const page = ref(1)
const size = ref(50)

const filters = ref({ search: '' })

// 范围由路由固定：nf + version
const nf = computed(() => route.params.nf as string)
const version = computed(() => route.params.version as string)

let searchTimer: any = null
function debouncedSearch() {
  clearTimeout(searchTimer)
  searchTimer = setTimeout(() => { page.value = 1; loadCommands() }, 300)
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
    params: { nf: nf.value, version: version.value, commandName: row.command_name },
  })
}

async function loadCommands() {
  loading.value = true
  try {
    const params = new URLSearchParams()
    params.set('nf', nf.value)
    params.set('version', version.value)
    params.set('page', String(page.value))
    params.set('size', String(size.value))
    if (filters.value.search) params.set('search', filters.value.search)
    const data = await fetchJson(`${commandGraphApi.commands}?${params}`)
    commands.value = data.items || []
    total.value = data.total || 0
  } finally {
    loading.value = false
  }
}

// 路由参数变化时（切到别的 nf/version）重置并重载
watch([nf, version], () => {
  page.value = 1
  filters.value.search = ''
  loadCommands()
})

onMounted(loadCommands)
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
