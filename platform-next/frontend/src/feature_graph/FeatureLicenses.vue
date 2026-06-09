<template>
  <div>
    <!-- Filters -->
    <div class="filter-bar">
      <el-input
        v-model="search"
        placeholder="搜索特性ID、License名称..."
        clearable
        size="small"
        style="width: 260px"
        @clear="onFilter"
        @keyup.enter="onFilter"
      />
      <el-select v-model="reviewFilter" placeholder="审查状态" clearable size="small" style="width: 140px" @change="onFilter">
        <el-option label="待审查" value="pending" />
        <el-option label="已接受" value="accepted" />
        <el-option label="已拒绝" value="rejected" />
      </el-select>
      <span class="filter-count">{{ filteredLicenses.length }} 条 License</span>
    </div>

    <div class="card" style="overflow: hidden">
      <el-table :data="pagedLicenses" stripe size="small" style="width: 100%" v-loading="loading">
        <el-table-column prop="feature_id" label="特性ID" width="150">
          <template #default="{ row }">
            <router-link
              :to="{ name: 'feature-detail', params: { id: row.feature_id }, query: row.product_type ? { product: row.product_type } : undefined }"
              class="feature-id-cell"
            >{{ row.feature_id }}</router-link>
          </template>
        </el-table-column>
        <el-table-column prop="license_number" label="License编号" width="140" />
        <el-table-column prop="license_code" label="License Code" width="180" />
        <el-table-column prop="license_name" label="License名称" min-width="220">
          <template #default="{ row }">
            <span style="font-size: var(--text-xs); color: var(--text-secondary)">{{ row.license_name || '-' }}</span>
          </template>
        </el-table-column>
        <el-table-column label="审查状态" width="120">
          <template #default="{ row }">
            <el-tag :type="reviewTagType(row._reviewStatus)" size="small" effect="plain">
              {{ reviewLabel(row._reviewStatus) }}
            </el-tag>
          </template>
        </el-table-column>
        <el-table-column label="操作" width="200" fixed="right">
          <template #default="{ row }">
            <div style="display: flex; gap: 4px; flex-wrap: wrap">
              <el-button
                size="small"
                type="primary"
                plain
                :disabled="row._reviewStatus === 'accepted'"
                @click="doReview('accept', row)"
              >接受</el-button>
              <el-button
                size="small"
                type="danger"
                plain
                :disabled="row._reviewStatus === 'rejected'"
                @click="doReview('reject', row)"
              >拒绝</el-button>
              <el-button
                v-if="row._reviewStatus !== 'pending'"
                size="small"
                plain
                @click="doReview('reset', row)"
              >重置</el-button>
            </div>
          </template>
        </el-table-column>
      </el-table>

      <div style="padding: var(--space-3) var(--space-4)">
        <el-pagination
          v-model:current-page="page"
          v-model:page-size="pageSize"
          :total="filteredLicenses.length"
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
const allLicenses = ref<any[]>([])
const search = ref('')
const reviewFilter = ref('')
const page = ref(1)
const pageSize = ref(50)
const reviewStatuses = ref<Record<string, string>>({})

function getItemId(row: any): string {
  return `${row.feature_id}:lic:${row.license_number}`
}

const enrichedLicenses = computed(() =>
  allLicenses.value.map((l: any) => ({
    ...l,
    _reviewStatus: reviewStatuses.value[getItemId(l)] || 'pending',
  }))
)

const filteredLicenses = computed(() => {
  let items = enrichedLicenses.value
  if (search.value) {
    const q = search.value.toLowerCase()
    items = items.filter((l: any) =>
      (l.feature_id || '').toLowerCase().includes(q) ||
      (l.license_name || '').toLowerCase().includes(q) ||
      (l.license_code || '').toLowerCase().includes(q)
    )
  }
  if (reviewFilter.value) {
    items = items.filter((l: any) => l._reviewStatus === reviewFilter.value)
  }
  return items
})

const pagedLicenses = computed(() => {
  const start = (page.value - 1) * pageSize.value
  return filteredLicenses.value.slice(start, start + pageSize.value)
})

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

function onFilter() {
  page.value = 1
}

async function doReview(action: 'accept' | 'reject' | 'reset', row: any) {
  const itemId = getItemId(row)
  const url = action === 'accept'
    ? featureGraphApi.reviewAccept
    : action === 'reject'
    ? featureGraphApi.reviewReject
    : featureGraphApi.reviewReset
  await postJson(url, { item_type: 'license', item_id: itemId })
  reviewStatuses.value[itemId] = action === 'accept' ? 'accepted' : action === 'reject' ? 'rejected' : 'pending'
}

async function loadLicenses() {
  loading.value = true
  try {
    const [licData] = await Promise.all([
      fetchJson(featureGraphApi.licenses),
    ])
    allLicenses.value = licData.licenses || []
    // Bulk-fetch review statuses
    const ids = allLicenses.value.map(getItemId)
    if (ids.length > 0) {
      try {
        const params = new URLSearchParams()
        params.set('item_type', 'license')
        params.set('item_ids', ids.join(','))
        const bulkData = await fetchJson(`${featureGraphApi.reviewBulk}?${params}`)
        reviewStatuses.value = bulkData.statuses || {}
      } catch {
        // Review store might be empty, that's fine
      }
    }
  } finally {
    loading.value = false
  }
}

onMounted(loadLicenses)
</script>
