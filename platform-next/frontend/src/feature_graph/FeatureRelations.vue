<template>
  <div>
    <!-- Filters -->
    <div class="filter-bar">
      <el-select v-model="depFilter" placeholder="依赖类型" clearable size="small" style="width: 160px" @change="filterDeps">
        <el-option label="depends_on" value="depends_on" />
        <el-option label="conflicts_with" value="conflicts_with" />
        <el-option label="cooperates_with" value="cooperates_with" />
      </el-select>
      <el-select v-model="reviewFilter" placeholder="审查状态" clearable size="small" style="width: 140px" @change="filterDeps">
        <el-option label="待审查" value="pending" />
        <el-option label="已接受" value="accepted" />
        <el-option label="已拒绝" value="rejected" />
      </el-select>
      <span class="filter-count">{{ filteredDeps.length }} 条关系</span>
    </div>

    <div class="card" style="overflow: hidden">
      <el-table :data="pagedDeps" stripe size="small" style="width: 100%" v-loading="loading">
        <el-table-column prop="source_feature_id" label="源特性" width="150">
          <template #default="{ row }">
            <router-link
              :to="{ name: 'feature-detail', params: { id: row.source_feature_id }, query: row.source_product_type ? { product: row.source_product_type } : undefined }"
              class="feature-id-cell"
            >{{ row.source_feature_id }}</router-link>
          </template>
        </el-table-column>
        <el-table-column prop="target_feature_id" label="目标特性" width="150">
          <template #default="{ row }">
            <router-link
              :to="{ name: 'feature-detail', params: { id: row.target_feature_id }, query: row.target_product_type ? { product: row.target_product_type } : undefined }"
              class="feature-id-cell"
            >{{ row.target_feature_id }}</router-link>
          </template>
        </el-table-column>
        <el-table-column prop="dependency_type" label="类型" width="140">
          <template #default="{ row }">
            <el-tag :type="depTagType(row.dependency_type)" size="small">{{ row.dependency_type }}</el-tag>
          </template>
        </el-table-column>
        <el-table-column prop="description" label="描述" min-width="200">
          <template #default="{ row }">
            <span style="color: var(--text-secondary); font-size: var(--text-xs)">{{ truncate(row.description, 150) }}</span>
          </template>
        </el-table-column>
        <el-table-column label="审查状态" width="100">
          <template #default="{ row }">
            <el-tag :type="reviewTagType(row._reviewStatus)" size="small" effect="plain">
              {{ reviewLabel(row._reviewStatus) }}
            </el-tag>
          </template>
        </el-table-column>
        <el-table-column label="操作" width="200" fixed="right">
          <template #default="{ row }">
            <div style="display: flex; gap: 4px; flex-wrap: wrap">
              <el-button size="small" type="primary" plain :disabled="row._reviewStatus === 'accepted'" @click="doReview('accept', row)">接受</el-button>
              <el-button size="small" type="danger" plain :disabled="row._reviewStatus === 'rejected'" @click="doReview('reject', row)">拒绝</el-button>
              <el-button v-if="row._reviewStatus !== 'pending'" size="small" plain @click="doReview('reset', row)">重置</el-button>
            </div>
          </template>
        </el-table-column>
      </el-table>

      <div style="padding: var(--space-3) var(--space-4)">
        <el-pagination
          v-model:current-page="page"
          v-model:page-size="pageSize"
          :total="filteredDeps.length"
          :page-sizes="[50, 100, 200]"
          layout="total, sizes, prev, pager, next"
          small
          @size-change="page = 1"
        />
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, computed, onMounted } from 'vue'
import { featureGraphApi, fetchJson, postJson } from '../api'

const loading = ref(false)
const allDeps = ref<any[]>([])
const depFilter = ref('')
const reviewFilter = ref('')
const page = ref(1)
const pageSize = ref(50)
const reviewStatuses = ref<Record<string, string>>({})

function getItemId(row: any): string {
  return `${row.source_feature_id}:dep:${row.target_feature_id}`
}

const enrichedDeps = computed(() =>
  allDeps.value.map((d: any) => ({
    ...d,
    _reviewStatus: reviewStatuses.value[getItemId(d)] || 'pending',
  }))
)

const filteredDeps = computed(() => {
  let items = enrichedDeps.value
  if (depFilter.value) {
    items = items.filter((d: any) => d.dependency_type === depFilter.value)
  }
  if (reviewFilter.value) {
    items = items.filter((d: any) => d._reviewStatus === reviewFilter.value)
  }
  return items
})

const pagedDeps = computed(() => {
  const start = (page.value - 1) * pageSize.value
  return filteredDeps.value.slice(start, start + pageSize.value)
})

function depTagType(t: string) {
  if (t === 'depends_on') return 'primary'
  if (t === 'conflicts_with') return 'danger'
  if (t === 'cooperates_with') return 'success'
  return 'info'
}

function reviewTagType(s: string) {
  if (s === 'accepted') return 'success'
  if (s === 'rejected') return 'danger'
  return 'info'
}

function reviewLabel(s: string) {
  if (s === 'accepted') return '已接受'
  if (s === 'rejected') return '已拒绝'
  return '待审查'
}

function truncate(s: string, n: number) {
  if (!s) return ''
  const clean = s.replace(/<br>/g, ' ').replace(/<[^>]*>/g, '')
  return clean.length > n ? clean.slice(0, n) + '...' : clean
}

function filterDeps() {
  page.value = 1
}

async function doReview(action: 'accept' | 'reject' | 'reset', row: any) {
  const itemId = getItemId(row)
  const url = action === 'accept'
    ? featureGraphApi.reviewAccept
    : action === 'reject'
    ? featureGraphApi.reviewReject
    : featureGraphApi.reviewReset
  await postJson(url, { item_type: 'dependency', item_id: itemId })
  reviewStatuses.value[itemId] = action === 'accept' ? 'accepted' : action === 'reject' ? 'rejected' : 'pending'
}

async function loadDeps() {
  loading.value = true
  try {
    const data = await fetchJson(featureGraphApi.dependencies)
    allDeps.value = data.dependencies || []
    // Bulk-fetch review statuses
    const ids = allDeps.value.map(getItemId)
    if (ids.length > 0) {
      try {
        const params = new URLSearchParams()
        params.set('item_type', 'dependency')
        params.set('item_ids', ids.join(','))
        const bulkData = await fetchJson(`${featureGraphApi.reviewBulk}?${params}`)
        reviewStatuses.value = bulkData.statuses || {}
      } catch {
        // Review store might be empty
      }
    }
  } finally {
    loading.value = false
  }
}

onMounted(loadDeps)
</script>
