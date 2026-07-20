<template>
  <div class="upload-view">
    <div class="upload-container stagger-in">
      <header class="page-head">
        <h1 class="page-title">导入资产包</h1>
        <p class="page-sub">
          上传一个 markdown 资产压缩包（.zip），系统将解析其中的 frontmatter 与对象/边关系，并入资产库。
        </p>
      </header>

      <div
        class="dropzone"
        :class="{
          'is-drag': isDrag,
          'is-done': job && job.status === 'done',
          'is-error': errorMsg || (job && job.status === 'failed'),
        }"
        @dragenter.prevent="onDragEnter"
        @dragover.prevent="onDragEnter"
        @dragleave.prevent="onDragLeave"
        @drop.prevent="onDrop"
      >
        <input
          ref="fileInput"
          type="file"
          accept=".zip"
          class="file-input"
          @change="onFileChange"
        />

        <div v-if="!uploading && !(job && job.status === 'done')" class="dz-content">
          <div class="dz-icon">
            <svg width="56" height="56" viewBox="0 0 24 24" fill="none">
              <path
                d="M12 16V4m0 0L7 9m5-5 5 5"
                stroke="currentColor"
                stroke-width="1.4"
                stroke-linecap="round"
                stroke-linejoin="round"
              />
              <path
                d="M4 17v2a1 1 0 0 0 1 1h14a1 1 0 0 0 1-1v-2"
                stroke="currentColor"
                stroke-width="1.4"
                stroke-linecap="round"
              />
            </svg>
          </div>
          <div class="dz-title">拖拽 .zip 文件到此处</div>
          <div class="dz-sub">或</div>
          <el-button type="primary" @click="pickFile">选择文件</el-button>
          <div class="dz-hint">支持包含 frontmatter 的 markdown 文件包</div>
        </div>

        <div v-else-if="uploading" class="dz-content">
          <div class="dz-icon spin">
            <svg width="56" height="56" viewBox="0 0 24 24" fill="none">
              <path
                d="M12 3a9 9 0 1 0 9 9"
                stroke="currentColor"
                stroke-width="2"
                stroke-linecap="round"
              />
            </svg>
          </div>
          <div class="dz-title">正在解析与导入…</div>
          <div class="dz-sub mono">{{ currentFile?.name }}</div>
        </div>

        <div v-else-if="job && job.status === 'done'" class="dz-content">
          <div class="dz-icon done">
            <svg width="56" height="56" viewBox="0 0 24 24" fill="none">
              <circle cx="12" cy="12" r="9" stroke="currentColor" stroke-width="1.4" opacity="0.3" />
              <path
                d="M8 12.5l2.5 2.5L16 9.5"
                stroke="currentColor"
                stroke-width="2"
                stroke-linecap="round"
                stroke-linejoin="round"
              />
            </svg>
          </div>
          <div class="dz-title">导入完成</div>
          <el-button text @click="reset">再导入一个</el-button>
        </div>
      </div>

      <div v-if="errorMsg" class="error-banner">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none">
          <circle cx="12" cy="12" r="9" stroke="currentColor" stroke-width="1.8" />
          <path d="M12 7v6m0 3v.5" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" />
        </svg>
        <span class="mono">{{ errorMsg }}</span>
      </div>

      <!-- 导入结果（job 完成后展示） -->
      <transition name="slide-up">
        <section v-if="job && job.status === 'done'" class="result-card stagger-in">
          <div class="result-head">
            <span class="result-title">导入结果</span>
            <span class="result-file mono">{{ currentFile?.name }}</span>
          </div>
          <div class="stat-grid">
            <div class="stat stat-added">
              <div class="stat-val">{{ job.added }}</div>
              <div class="stat-label">新增</div>
            </div>
            <div class="stat stat-updated">
              <div class="stat-val">{{ job.updated }}</div>
              <div class="stat-label">更新</div>
            </div>
            <div class="stat stat-skipped">
              <div class="stat-val">{{ job.skipped }}</div>
              <div class="stat-label">跳过</div>
            </div>
          </div>
          <div v-if="warnings.length" class="warnings">
            <div class="warn-head">
              <span>警告 ({{ warnings.length }})</span>
            </div>
            <ul class="warn-list">
              <li v-for="(w, i) in warnings" :key="i" class="warn-item mono">{{ w }}</li>
            </ul>
          </div>
        </section>
      </transition>

      <!-- 上传历史 -->
      <section class="history">
        <div class="history-head">
          <span class="history-title">上传历史</span>
          <span v-if="history.length" class="history-count mono">{{ history.length }}</span>
        </div>
        <div v-if="historyLoading" class="history-empty">加载中…</div>
        <div v-else-if="!history.length" class="history-empty">暂无记录</div>
        <ul v-else class="history-list">
          <li v-for="(h, i) in history" :key="i" class="history-row">
            <div class="hr-main">
              <span class="hr-file mono" :title="h.filename">{{ h.filename }}</span>
              <div class="hr-stats">
                <span class="hr-tag hr-add">+{{ h.added }}</span>
                <span v-if="h.updated" class="hr-tag hr-upd">~{{ h.updated }}</span>
                <span v-if="h.skipped" class="hr-tag hr-skip">{{ h.skipped }}</span>
              </div>
            </div>
            <span class="hr-time mono">{{ formatTime(h.timestamp) }}</span>
          </li>
        </ul>
      </section>
    </div>
  </div>
</template>

<script setup lang="ts">
import { onMounted, onUnmounted, ref } from 'vue'
import {
  importBundle,
  importJob,
  importHistory,
  type ImportAccepted,
  type ImportJob,
  type ImportHistoryItem,
} from '../api'

const fileInput = ref<HTMLInputElement | null>(null)
const isDrag = ref(false)
const uploading = ref(false)
const currentFile = ref<File | null>(null)
// 当前活跃 job（异步导入：POST /import 立即返回 job_id，后台处理）
const job = ref<ImportJob | null>(null)
// 兼容模板：result 非空即代表已上传（详情取自 job）
const result = ref<ImportAccepted | null>(null)
const errorMsg = ref('')
const warnings = ref<string[]>([])

const history = ref<ImportHistoryItem[]>([])
const historyLoading = ref(false)

let pollTimer: ReturnType<typeof setInterval> | null = null

function stopPoll(): void {
  if (pollTimer !== null) {
    clearInterval(pollTimer)
    pollTimer = null
  }
}

async function pollJob(jobId: string): Promise<void> {
  try {
    const j = await importJob(jobId)
    job.value = j
    if (j.status === 'done') {
      stopPoll()
      uploading.value = false
      warnings.value = j.warnings ?? []
      refreshGlobalStats()
      loadHistory()
    } else if (j.status === 'failed') {
      stopPoll()
      uploading.value = false
      errorMsg.value = j.error || '导入失败'
    }
  } catch {
    /* 轮询失败暂忽略，下轮重试 */
  }
}

function pickFile(): void {
  fileInput.value?.click()
}

function onFileChange(e: Event): void {
  const f = (e.target as HTMLInputElement).files?.[0]
  if (f) doUpload(f)
}

function onDragEnter(): void {
  isDrag.value = true
}
function onDragLeave(): void {
  isDrag.value = false
}
function onDrop(e: DragEvent): void {
  isDrag.value = false
  const f = e.dataTransfer?.files?.[0]
  if (f) doUpload(f)
}

async function doUpload(f: File): Promise<void> {
  currentFile.value = f
  uploading.value = true
  result.value = null
  job.value = null
  errorMsg.value = ''
  warnings.value = []
  stopPoll()
  try {
    const accepted = await importBundle(f)
    result.value = accepted
    // 非阻塞轮询 job 状态（每 1.5s）
    pollTimer = setInterval(() => void pollJob(accepted.job_id), 1500)
    // 立即拉一次（FastAPI TestClient 场景下后台已可能完成）
    void pollJob(accepted.job_id)
  } catch (e: unknown) {
    errorMsg.value = e instanceof Error ? e.message : String(e)
    uploading.value = false
  }
}

function reset(): void {
  stopPoll()
  result.value = null
  job.value = null
  currentFile.value = null
  errorMsg.value = ''
  warnings.value = []
  if (fileInput.value) fileInput.value.value = ''
}

function refreshGlobalStats(): void {
  const w = window as unknown as { __refreshStats?: () => Promise<void> }
  w.__refreshStats?.()
}

async function loadHistory(): Promise<void> {
  historyLoading.value = true
  try {
    history.value = await importHistory()
  } catch {
    history.value = []
  } finally {
    historyLoading.value = false
  }
}

function formatTime(ts: string): string {
  try {
    const d = new Date(ts)
    return d.toLocaleString('zh-CN', { hour12: false })
  } catch {
    return ts
  }
}

onMounted(loadHistory)
onUnmounted(stopPoll)
</script>

<style scoped>
.upload-view {
  height: 100%;
  overflow: auto;
  padding: var(--space-8) var(--space-6);
}

.upload-container {
  max-width: 760px;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  gap: var(--space-6);
}

.page-head {
  display: flex;
  flex-direction: column;
  gap: var(--space-2);
}

.page-title {
  font-family: var(--display);
  font-size: 26px;
  font-weight: 700;
  color: var(--text);
  margin: 0;
  letter-spacing: -0.02em;
}

.page-sub {
  margin: 0;
  color: var(--text-muted);
  font-size: 13.5px;
  max-width: 560px;
}

.dropzone {
  position: relative;
  border: 1.5px dashed var(--border-strong);
  border-radius: var(--radius-lg);
  background: var(--bg-elev);
  min-height: 280px;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all var(--dur) var(--ease);
}

.dropzone.is-drag {
  border-color: var(--accent);
  background: var(--accent-soft);
  transform: scale(1.005);
  box-shadow: 0 0 0 4px var(--accent-ring);
}

.dropzone.is-done {
  border-color: var(--success);
  border-style: solid;
}

.dropzone.is-error {
  border-color: var(--danger);
}

.file-input {
  display: none;
}

.dz-content {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: var(--space-3);
  text-align: center;
  padding: var(--space-8);
}

.dz-icon {
  color: var(--text-faint);
}

.dropzone.is-drag .dz-icon {
  color: var(--accent);
}

.dz-icon.done {
  color: var(--success);
}

.dz-title {
  font-family: var(--display);
  font-size: 16px;
  font-weight: 600;
  color: var(--text);
}

.dz-sub {
  font-size: 13px;
  color: var(--text-faint);
}

.dz-hint {
  font-size: 11.5px;
  color: var(--text-faint);
  margin-top: var(--space-1);
}

.spin {
  animation: spin 1s linear infinite;
  color: var(--accent);
}

@keyframes spin {
  to {
    transform: rotate(360deg);
  }
}

.error-banner {
  display: flex;
  align-items: center;
  gap: var(--space-2);
  padding: var(--space-3) var(--space-4);
  background: #fef2f2;
  border: 1px solid #fecaca;
  border-radius: var(--radius-sm);
  color: var(--danger);
  font-size: 12.5px;
}

.result-card {
  background: var(--bg-elev);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  box-shadow: var(--shadow-sm);
  overflow: hidden;
}

.result-head {
  display: flex;
  align-items: baseline;
  justify-content: space-between;
  padding: var(--space-4) var(--space-5);
  border-bottom: 1px solid var(--border-faint);
}

.result-title {
  font-family: var(--display);
  font-weight: 600;
  font-size: 15px;
}

.result-file {
  font-size: 12px;
  color: var(--text-muted);
}

.stat-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  padding: var(--space-5);
  gap: var(--space-4);
}

.stat {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 4px;
}

.stat-val {
  font-family: var(--display);
  font-size: 32px;
  font-weight: 700;
  line-height: 1;
}

.stat-added .stat-val {
  color: var(--success);
}
.stat-updated .stat-val {
  color: var(--accent);
}
.stat-skipped .stat-val {
  color: var(--text-faint);
}

.stat-label {
  font-size: 12px;
  color: var(--text-muted);
}

.warnings {
  border-top: 1px solid var(--border-faint);
  padding: var(--space-4) var(--space-5);
}

.warn-head {
  font-size: 12px;
  font-weight: 600;
  color: var(--warn);
  margin-bottom: var(--space-2);
}

.warn-list {
  list-style: none;
  margin: 0;
  padding: 0;
  max-height: 180px;
  overflow: auto;
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.warn-item {
  font-size: 11.5px;
  color: var(--text-muted);
  background: var(--bg-sunken);
  padding: var(--space-2) var(--space-3);
  border-radius: var(--radius-sm);
}

.history {
  background: var(--bg-elev);
  border: 1px solid var(--border);
  border-radius: var(--radius);
}

.history-head {
  display: flex;
  align-items: baseline;
  justify-content: space-between;
  padding: var(--space-3) var(--space-4);
  border-bottom: 1px solid var(--border-faint);
}

.history-title {
  font-family: var(--display);
  font-weight: 600;
  font-size: 13px;
}

.history-count {
  font-size: 11px;
  color: var(--text-faint);
}

.history-empty {
  padding: var(--space-5);
  text-align: center;
  font-size: 12.5px;
  color: var(--text-faint);
}

.history-list {
  list-style: none;
  margin: 0;
  padding: 0;
}

.history-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: var(--space-3);
  padding: var(--space-2) var(--space-4);
  border-bottom: 1px solid var(--border-faint);
}

.history-row:last-child {
  border-bottom: none;
}

.hr-main {
  display: flex;
  align-items: center;
  gap: var(--space-3);
  min-width: 0;
  flex: 1;
}

.hr-file {
  font-size: 12px;
  color: var(--text);
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.hr-stats {
  display: flex;
  gap: 4px;
  flex-shrink: 0;
}

.hr-tag {
  font-size: 10.5px;
  font-weight: 600;
  padding: 1px 6px;
  border-radius: 4px;
  font-family: var(--mono);
}

.hr-add {
  color: var(--success);
  background: #ecfdf5;
}
.hr-upd {
  color: var(--accent);
  background: var(--accent-soft);
}
.hr-skip {
  color: var(--text-muted);
  background: var(--bg-sunken);
}

.hr-time {
  font-size: 11px;
  color: var(--text-faint);
  flex-shrink: 0;
}

.slide-up-enter-active {
  transition: all var(--dur) var(--ease);
}
.slide-up-enter-from {
  opacity: 0;
  transform: translateY(8px);
}
</style>
