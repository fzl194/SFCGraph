<template>
  <div class="md-pane">
    <div v-if="!id" class="empty muted">从左侧选择一个对象以查看内容</div>

    <template v-else>
      <div class="header">
        <div class="title-row">
          <span class="obj-id" :title="id">{{ id }}</span>
        </div>
        <div class="badges">
          <el-tag v-if="detail?.type" size="small">{{ detail.type }}</el-tag>
          <el-tag v-if="detail?.layer" size="small" type="info">
            {{ detail.layer }}
          </el-tag>
          <el-tag v-if="detail?.nf" size="small" type="success">
            {{ detail.nf }}
          </el-tag>
          <el-tag v-if="detail?.version" size="small" type="warning">
            {{ detail.version }}
          </el-tag>
          <el-tag v-if="detail?.domain" size="small" effect="plain">
            {{ detail.domain }}
          </el-tag>
        </div>

        <!-- 多版本切换 -->
        <div v-if="multiVersion" class="version-row">
          <span class="ver-label">版本：</span>
          <el-select
            v-model="localVersion"
            size="small"
            style="width: 140px"
            @change="onVersionSwitch"
          >
            <el-option
              v-for="v in detail!.versions"
              :key="v"
              :label="v"
              :value="v"
            />
          </el-select>
          <span v-if="versionMissing" class="warn-text">
            ⚠ 所选版本不存在，已回退
          </span>
        </div>
      </div>

      <div v-if="loading" class="status muted">加载中…</div>
      <div v-else-if="error" class="status error">
        {{ error }}
      </div>
      <el-scrollbar v-else class="md-scroll">
        <div class="markdown-body" v-html="rendered"></div>
      </el-scrollbar>
    </template>
  </div>
</template>

<script setup lang="ts">
import { ref, computed, watch } from 'vue'
import MarkdownIt from 'markdown-it'
import DOMPurify from 'dompurify'
import {
  getObject,
  getMd,
  availableVersionsFromError,
  type ObjectDetail,
  type ApiError,
} from '../api'

const props = defineProps<{
  id?: string
  version?: string
}>()

const emit = defineEmits<{
  // 版本回退通知：父级据可用版本回退 ?version=
  (e: 'fallbackVersion', id: string, available: string[]): void
}>()

const md = new MarkdownIt({
  html: false, // 原 md 已可信，但正文 body 可能含标签 → 允许但经 DOMPurify
  linkify: true,
  breaks: false,
})

const detail = ref<ObjectDetail | null>(null)
const rawMd = ref('')
const loading = ref(false)
const error = ref('')
const versionMissing = ref(false)

const localVersion = ref<string>('')

const multiVersion = computed(
  () => detail.value && detail.value.versions.length > 1,
)

const rendered = computed(() => {
  if (!rawMd.value) return ''
  const html = md.render(rawMd.value)
  // DOMPurify 防 XSS（即便 md 来源可信，仍兜底）
  return DOMPurify.sanitize(html, {
    ADD_ATTR: ['target'],
  })
})

async function load() {
  if (!props.id) {
    detail.value = null
    rawMd.value = ''
    return
  }
  loading.value = true
  error.value = ''
  versionMissing.value = false
  try {
    const [obj, text] = await Promise.all([
      getObject(props.id, props.version),
      getMd(props.id, props.version),
    ])
    detail.value = obj
    rawMd.value = text
    localVersion.value = obj.version || ''
  } catch (e) {
    const err = e as ApiError
    const avail = availableVersionsFromError(err)
    if (err.status === 404 && avail && avail.length > 0) {
      // 版本缺失 → 通知父级回退到最新可用版本
      versionMissing.value = true
      emit('fallbackVersion', props.id, avail)
      error.value = `版本 "${props.version}" 不存在，可用版本：${avail.join(', ')}（已请求回退）`
    } else {
      error.value = err.message || String(e)
    }
    detail.value = null
    rawMd.value = ''
  } finally {
    loading.value = false
  }
}

function onVersionSwitch(v: string) {
  // 子组件内切换版本 → 交给父级统一驱动 URL（通过 reload 时 props.version 生效）
  // 这里复用 fallbackVersion 通道传“用户想看的版本”
  emit('fallbackVersion', props.id!, [v])
}

watch(
  () => [props.id, props.version],
  () => load(),
  { immediate: true },
)
</script>

<style scoped>
.md-pane {
  display: flex;
  flex-direction: column;
  height: 100%;
  background: #fff;
}
.empty,
.status {
  padding: 32px;
  text-align: center;
}
.muted {
  color: #909399;
}
.error {
  color: #f56c6c;
}
.header {
  padding: 10px 16px;
  border-bottom: 1px solid #ebeef5;
  background: #fafafa;
}
.title-row {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-bottom: 6px;
}
.obj-id {
  font-weight: 600;
  font-size: 14px;
  word-break: break-all;
}
.badges {
  display: flex;
  gap: 6px;
  flex-wrap: wrap;
}
.version-row {
  margin-top: 8px;
  display: flex;
  align-items: center;
  gap: 8px;
}
.ver-label {
  font-size: 13px;
  color: #606266;
}
.warn-text {
  color: #e6a23c;
  font-size: 12px;
}
.md-scroll {
  flex: 1;
  min-height: 0;
}
.markdown-body {
  padding: 16px 24px;
  font-size: 14px;
  line-height: 1.7;
  color: #2c3e50;
}
.markdown-body :deep(h1),
.markdown-body :deep(h2),
.markdown-body :deep(h3) {
  margin: 16px 0 8px;
  font-weight: 600;
}
.markdown-body :deep(h1) {
  font-size: 20px;
  border-bottom: 1px solid #eee;
  padding-bottom: 6px;
}
.markdown-body :deep(h2) {
  font-size: 17px;
}
.markdown-body :deep(h3) {
  font-size: 15px;
}
.markdown-body :deep(pre) {
  background: #f6f8fa;
  padding: 10px 12px;
  border-radius: 4px;
  overflow-x: auto;
  font-size: 13px;
}
.markdown-body :deep(code) {
  background: #f6f8fa;
  padding: 2px 4px;
  border-radius: 3px;
  font-size: 13px;
}
.markdown-body :deep(table) {
  border-collapse: collapse;
  margin: 8px 0;
}
.markdown-body :deep(th),
.markdown-body :deep(td) {
  border: 1px solid #dfe2e5;
  padding: 6px 10px;
}
.markdown-body :deep(blockquote) {
  border-left: 3px solid #dfe2e5;
  margin: 8px 0;
  padding: 4px 12px;
  color: #606266;
}
.markdown-body :deep(a) {
  color: #409eff;
  text-decoration: none;
}
.markdown-body :deep(a:hover) {
  text-decoration: underline;
}
</style>
