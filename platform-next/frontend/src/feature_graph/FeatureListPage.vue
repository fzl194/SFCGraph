<template>
  <div class="feature-list" v-loading="loading">
    <el-tabs v-model="tab" @tab-change="onTabChange">
      <el-tab-pane label="特性" name="features">
        <div class="list-toolbar">
          <el-input v-model="featSearch" placeholder="搜索特性编号/名称" clearable style="width:280px"
                    @keyup.enter="loadFeatures(1)" @clear="loadFeatures(1)" />
          <el-select v-model="featCategory" placeholder="类别" clearable style="width:140px;margin-left:8px"
                     @change="loadFeatures(1)">
            <el-option v-for="c in ['base','enhanced','operations','protocol','integration']" :key="c" :label="c" :value="c" />
          </el-select>
          <span class="list-count">共 {{ featTotal }} 条</span>
        </div>
        <el-table :data="featItems" size="small" @row-click="(r:any)=>goFeature(r.feature_code)" highlight-current-row>
          <el-table-column prop="feature_code" label="特性编号" width="150" />
          <el-table-column prop="name" label="名称" min-width="200" show-overflow-tooltip />
          <el-table-column prop="feature_category" label="类别" width="100" />
          <el-table-column prop="config_relevance" label="配置" width="90" />
          <el-table-column label="适用NF" width="200" show-overflow-tooltip>
            <template #default="{row}">{{ (row.applicable_nf||[]).join('、') }}</template>
          </el-table-column>
        </el-table>
        <el-pagination background layout="prev, pager, next, sizes, total" :total="featTotal"
                       :page-sizes="[20,50,100]" v-model:current-page="featPage" v-model:page-size="featSize"
                       @current-change="loadFeatures()" @size-change="loadFeatures(1)" style="margin-top:12px" />
      </el-tab-pane>

      <el-tab-pane label="License" name="licenses">
        <div class="list-toolbar">
          <el-input v-model="licSearch" placeholder="搜索 License 编号/名称" clearable style="width:280px"
                    @keyup.enter="loadLicenses(1)" @clear="loadLicenses(1)" />
          <span class="list-count">共 {{ licTotal }} 条</span>
        </div>
        <el-table :data="licItems" size="small" @row-click="(r:any)=>goLicense(r.license_code)" highlight-current-row>
          <el-table-column prop="license_code" label="License编码" width="180" />
          <el-table-column prop="name" label="名称" min-width="220" show-overflow-tooltip />
          <el-table-column prop="control_item_id" label="控制项编号" width="130" />
          <el-table-column prop="control_item_type" label="类型" width="90" />
          <el-table-column label="适用NF" width="200" show-overflow-tooltip>
            <template #default="{row}">{{ (row.applicable_nf||[]).join('、') }}</template>
          </el-table-column>
        </el-table>
        <el-pagination background layout="prev, pager, next, sizes, total" :total="licTotal"
                       :page-sizes="[20,50,100]" v-model:current-page="licPage" v-model:page-size="licSize"
                       @current-change="loadLicenses()" @size-change="loadLicenses(1)" style="margin-top:12px" />
      </el-tab-pane>
    </el-tabs>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { featureGraphApi, fetchJson } from '../api'

const route = useRoute()
const router = useRouter()
const nf = route.params.nf as string
const version = route.params.version as string

const tab = ref('features')
const loading = ref(false)

const featSearch = ref(''); const featCategory = ref('')
const featItems = ref<any[]>([]); const featTotal = ref(0)
const featPage = ref(1); const featSize = ref(50)

const licSearch = ref('')
const licItems = ref<any[]>([]); const licTotal = ref(0)
const licPage = ref(1); const licSize = ref(50)

async function loadFeatures(page?: number) {
  if (page) featPage.value = page
  loading.value = true
  try {
    const url = featureGraphApi.features(nf, version) +
      `&search=${encodeURIComponent(featSearch.value)}&category=${featCategory.value}` +
      `&page=${featPage.value}&size=${featSize.value}`
    const data = await fetchJson(url)
    featItems.value = data.items || []
    featTotal.value = data.total || 0
  } finally { loading.value = false }
}

async function loadLicenses(page?: number) {
  if (page) licPage.value = page
  loading.value = true
  try {
    const url = featureGraphApi.licenses(nf, version) +
      `&search=${encodeURIComponent(licSearch.value)}&page=${licPage.value}&size=${licSize.value}`
    const data = await fetchJson(url)
    licItems.value = data.items || []
    licTotal.value = data.total || 0
  } finally { loading.value = false }
}

function onTabChange(t: string) {
  if (t === 'licenses' && licItems.value.length === 0) loadLicenses(1)
}

function goFeature(code: string) {
  router.push({ name: 'feature-detail', params: { nf, version, code } })
}
function goLicense(code: string) {
  router.push({ name: 'license-detail', params: { nf, version, code } })
}

onMounted(() => loadFeatures(1))
</script>

<style scoped>
.feature-list { padding: var(--space-2) 0; }
.list-toolbar { display: flex; align-items: center; gap: var(--space-2); margin-bottom: var(--space-3); }
.list-count { font-size: var(--text-xs); color: var(--text-tertiary); margin-left: auto; }
:deep(.el-table__row) { cursor: pointer; }
</style>
