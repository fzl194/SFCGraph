<template>
  <div class="tests-page">
    <div class="page-head">
      <div>
        <h1 class="page-title">测试用例</h1>
        <p class="page-sub">
          数据飞轮·数据层。用例（输入）→ 运行（产出）→ 审查（问题清单）→ 定位改图谱。
          <span v-if="stats" class="page-stats">
            {{ stats.case_count }} 用例 · {{ stats.run_count }} 运行 ·
            {{ stats.review_count }} 审查
          </span>
        </p>
      </div>
      <div class="head-actions">
        <el-button type="primary" @click="toggleForm">
          {{ showForm ? '收起' : '+ 新建用例' }}
        </el-button>
        <el-button :loading="refreshing" @click="refresh">刷新索引</el-button>
      </div>
    </div>

    <TestCaseForm v-if="showForm" @created="onCreated" @cancel="showForm = false" />

    <div class="filter-bar">
      <el-select
        v-model="domain"
        placeholder="全部业务域"
        clearable
        class="f-domain"
        @change="reload"
      >
        <el-option v-for="d in domainOptions" :key="d" :label="d" :value="d" />
      </el-select>
      <el-input
        v-model="q"
        placeholder="搜索用例（id / 名称）"
        clearable
        class="f-q"
        @input="onQ"
        @clear="reload"
      />
    </div>

    <div v-loading="loading" class="cases-list">
      <div v-if="!loading && cases.length === 0" class="empty">
        暂无用例。点上方"+ 新建用例"由 SA 直接建；或把 TestCase md 放到
        <code>platform-data/tests/cases/{域}/{场景}/</code>，再"刷新索引"。
      </div>
      <div v-for="c in cases" :key="c.id" class="case-row" @click="goCase(c.id)">
        <div class="case-main">
          <div class="case-name">{{ c.name || c.id }}</div>
          <div class="case-meta">
            <span class="tag">{{ c.domain || '未分类' }}</span>
            <span v-if="c.scenario" class="tag tag-scene">{{ c.scenario }}</span>
            <span class="dot">·</span>
            <span>{{ c.file_count }} 文件</span>
            <span class="dot">·</span>
            <span>{{ c.run_count }} 次运行</span>
          </div>
        </div>
        <div class="case-side">
          <button class="dl-btn" title="打包下载" @click.stop="download(c.id)">下载</button>
          <span :class="['verdict', verdictClass(c.latest_verdict)]">
            {{ c.latest_verdict || '未审查' }}
          </span>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed, onMounted, ref } from 'vue'
import { useRouter } from 'vue-router'
import { ElInput, ElSelect, ElOption, ElButton } from 'element-plus'
import { listCases, testsStats, reindexTests, downloadCaseURL, type TestCaseRow, type TestStats, type CaseDetail } from '../api'
import TestCaseForm from '../components/TestCaseForm.vue'

const router = useRouter()
const cases = ref<TestCaseRow[]>([])
const stats = ref<TestStats | null>(null)
const loading = ref(false)
const refreshing = ref(false)
const domain = ref('')
const q = ref('')
const showForm = ref(false)
let qTimer: ReturnType<typeof setTimeout> | null = null

const domainOptions = computed(() => (stats.value ? Object.keys(stats.value.cases_by_domain) : []))

async function reload(): Promise<void> {
  loading.value = true
  try {
    cases.value = await listCases({ domain: domain.value || undefined, q: q.value || undefined })
  } finally {
    loading.value = false
  }
}

async function loadStats(): Promise<void> {
  try {
    stats.value = await testsStats()
  } catch {
    /* 容错 */
  }
}

function onQ(): void {
  if (qTimer) clearTimeout(qTimer)
  qTimer = setTimeout(reload, 250)
}

function toggleForm(): void {
  showForm.value = !showForm.value
}

async function onCreated(_c: CaseDetail): Promise<void> {
  showForm.value = false
  await Promise.all([reload(), loadStats()])
}

async function refresh(): Promise<void> {
  refreshing.value = true
  try {
    await reindexTests()
    await Promise.all([reload(), loadStats()])
  } finally {
    refreshing.value = false
  }
}

function download(id: string): void {
  window.open(downloadCaseURL(id), '_blank')
}

function goCase(id: string): void {
  router.push({ name: 'tests-case', params: { id } })
}

function verdictClass(v: string): string {
  if (v === '通过') return 'v-pass'
  if (v === '不通过') return 'v-fail'
  if (v === '部分通过') return 'v-partial'
  return 'v-none'
}

onMounted(async () => {
  await Promise.all([loadStats(), reload()])
})
</script>

<style scoped>
.tests-page {
  height: 100%;
  overflow-y: auto;
  padding: var(--space-6) var(--space-7);
  max-width: 1100px;
  margin: 0 auto;
}
.page-head {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  gap: var(--space-4);
  margin-bottom: var(--space-5);
}
.page-title {
  font-family: var(--display);
  font-size: 22px;
  font-weight: 700;
  color: var(--text);
  margin: 0 0 4px;
  letter-spacing: -0.01em;
}
.page-sub {
  font-size: 13px;
  color: var(--text-muted);
  margin: 0;
  line-height: 1.6;
}
.page-stats {
  color: var(--text);
  font-weight: 600;
  margin-left: 6px;
}
.head-actions {
  display: flex;
  gap: var(--space-2);
}
.filter-bar {
  display: flex;
  gap: var(--space-3);
  margin-bottom: var(--space-4);
}
.f-domain {
  width: 220px;
}
.f-q {
  flex: 1;
  max-width: 420px;
}
.cases-list {
  display: flex;
  flex-direction: column;
  gap: 8px;
}
.empty {
  padding: var(--space-8);
  text-align: center;
  color: var(--text-muted);
  font-size: 13px;
  line-height: 1.8;
  background: var(--bg-sunken);
  border-radius: var(--radius);
  border: 1px dashed var(--border);
}
.empty code {
  background: var(--bg-elev);
  padding: 1px 5px;
  border-radius: 4px;
  font-size: 12px;
}
.case-row {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: var(--space-3) var(--space-4);
  background: var(--bg-elev);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  cursor: pointer;
  transition: border-color var(--dur-fast) var(--ease), transform var(--dur-fast) var(--ease);
}
.case-row:hover {
  border-color: var(--accent);
  transform: translateY(-1px);
}
.case-name {
  font-size: 14px;
  font-weight: 600;
  color: var(--text);
  margin-bottom: 4px;
}
.case-meta {
  font-size: 12px;
  color: var(--text-faint);
  display: flex;
  align-items: center;
  gap: 6px;
}
.tag {
  padding: 1px 7px;
  background: var(--bg-sunken);
  border-radius: 4px;
  font-size: 11px;
  color: var(--text-muted);
}
.tag-scene {
  color: var(--accent);
}
.dot {
  opacity: 0.5;
}
.case-side {
  display: flex;
  align-items: center;
  gap: var(--space-2);
}
.dl-btn {
  font-size: 12px;
  color: var(--text-muted);
  background: var(--bg-sunken);
  border: 1px solid var(--border);
  border-radius: var(--radius-sm);
  padding: 3px 10px;
  cursor: pointer;
}
.dl-btn:hover {
  color: var(--accent);
  border-color: var(--accent);
}
.verdict {
  font-size: 12px;
  font-weight: 600;
  padding: 3px 10px;
  border-radius: 999px;
  white-space: nowrap;
}
.v-pass {
  background: rgba(16, 185, 129, 0.12);
  color: #059669;
}
.v-fail {
  background: rgba(239, 68, 68, 0.12);
  color: #dc2626;
}
.v-partial {
  background: rgba(245, 158, 11, 0.14);
  color: #d97706;
}
.v-none {
  background: var(--bg-sunken);
  color: var(--text-faint);
}
</style>
