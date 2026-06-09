<template>
  <!-- Filter bar -->
  <div class="filter-bar">
    <el-select
      v-model="filters.product_type"
      placeholder="产品"
      clearable
      size="small"
      style="width: 120px"
      @change="onFilterChange"
    >
      <el-option v-for="p in products" :key="p" :label="p" :value="p" />
    </el-select>
    <el-select
      v-model="filters.feature_type"
      placeholder="类型"
      clearable
      size="small"
      style="width: 150px"
      @change="onFilterChange"
    >
      <el-option v-for="t in featureTypes" :key="t" :label="t || '(未分类)'" :value="t" />
    </el-select>
    <el-input
      v-model="filters.search"
      placeholder="搜索 ID / 名称..."
      clearable
      size="small"
      style="width: 200px"
      @input="debouncedSearch"
    />
    <span class="filter-count">{{ total }} 条特性</span>
  </div>

  <!-- Table -->
  <div class="card" style="overflow: hidden">
    <el-table
      :data="features"
      :default-sort="{ prop: 'feature_id', order: 'ascending' }"
      @row-click="onRowClick"
      style="width: 100%"
      v-loading="loading"
      size="small"
    >
      <el-table-column
        v-for="col in visibleColumns"
        :key="col.key"
        :prop="col.key"
        :label="col.label"
        :width="col.key === 'definition' ? undefined : col.width"
        :min-width="col.key === 'definition' ? 300 : undefined"
        :sortable="col.sortable"
      >
        <template #default="{ row }">
          <span v-if="col.key === 'feature_id'" class="feature-id-cell">{{ row[col.key] }}</span>
          <span v-else-if="col.key === 'feature_name'" class="feature-name-cell">{{ row[col.key] }}</span>
          <el-tag v-else-if="col.key === 'config_required'" :type="row[col.key] === 'true' ? 'success' : 'info'" size="small">
            {{ row[col.key] === 'true' ? '是' : '否' }}
          </el-tag>
          <el-tag v-else-if="col.key === 'feature_type'" size="small" effect="plain">{{ row[col.key] || '-' }}</el-tag>
          <span v-else-if="col.key === 'definition'" class="definition-cell">{{ truncate(row[col.key], 120) }}</span>
          <span v-else style="font-size: var(--text-xs); color: var(--text-secondary)">{{ row[col.key] }}</span>
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
        @current-change="loadFeatures"
        @size-change="onSizeChange"
      />
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, computed } from 'vue'
import { useRouter } from 'vue-router'
import { featureGraphApi, fetchJson } from '../api'

const router = useRouter()
const loading = ref(false)
const columns = ref<any[]>([])
const features = ref<any[]>([])
const stats = ref<any>({})
const total = ref(0)
const page = ref(1)
const size = ref(50)

const filters = ref({ product_type: '', feature_type: '', search: '' })

const visibleColumns = computed(() =>
  columns.value.filter(c =>
    ['feature_id', 'feature_name', 'product_type', 'feature_type', 'section', 'config_required', 'definition'].includes(c.key)
  )
)

// Sort by count desc, empty string shown as last
const featureTypes = computed(() => {
  const bt = stats.value.by_type || {}
  return Object.entries(bt)
    .sort(([aKey, aVal], [bKey, bVal]) => {
      if (aKey === '' && bKey !== '') return 1
      if (bKey === '' && aKey !== '') return -1
      return (bVal as number) - (aVal as number)
    })
    .map(([k]) => k)
})

const products = computed(() => {
  const bp = stats.value.by_product || {}
  return Object.entries(bp).sort(([, a], [, b]) => (b as number) - (a as number)).map(([k]) => k)
})

let searchTimer: any = null
function debouncedSearch() {
  clearTimeout(searchTimer)
  searchTimer = setTimeout(() => { page.value = 1; loadFeatures() }, 300)
}

function onFilterChange() {
  page.value = 1
  loadFeatures()
}

function onSizeChange() {
  page.value = 1
  loadFeatures()
}

function truncate(s: string, n: number) {
  if (!s) return ''
  return s.length > n ? s.slice(0, n) + '...' : s
}

function onRowClick(row: any) {
  router.push({
    name: 'feature-detail',
    params: { id: row.feature_id },
    query: row.product_type ? { product: row.product_type } : undefined,
  })
}

async function loadColumns() {
  const data = await fetchJson(featureGraphApi.columns)
  columns.value = data.columns || []
}

async function loadStats() {
  stats.value = await fetchJson(featureGraphApi.stats)
}

async function loadFeatures() {
  loading.value = true
  try {
    const params = new URLSearchParams()
    params.set('page', String(page.value))
    params.set('size', String(size.value))
    if (filters.value.product_type) params.set('product_type', filters.value.product_type)
    if (filters.value.feature_type) params.set('feature_type', filters.value.feature_type)
    if (filters.value.search) params.set('search', filters.value.search)
    const data = await fetchJson(`${featureGraphApi.features}?${params}`)
    features.value = data.items || []
    total.value = data.total || 0
  } finally {
    loading.value = false
  }
}

onMounted(async () => {
  await Promise.all([loadColumns(), loadStats()])
  await loadFeatures()
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
