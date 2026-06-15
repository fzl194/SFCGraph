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

const filters = ref({ product: '', search: '' })

const products = computed(() => {
  const bp = stats.value.by_product || {}
  return Object.entries(bp).sort(([, a], [, b]) => (b as number) - (a as number)).map(([k]) => k)
})

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

function formatCategoryPath(raw: string) {
  if (!raw) return '-'
  try {
    const arr = JSON.parse(raw)
    return Array.isArray(arr) ? arr.join(' > ') : raw
  } catch {
    return raw
  }
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
