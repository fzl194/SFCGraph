<template>
  <div class="md-preview">
    <div v-if="!objectId" class="empty">
      <div class="empty-icon">
        <svg width="48" height="48" viewBox="0 0 24 24" fill="none">
          <path
            d="M6 2h8l5 5v13a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2Z"
            stroke="currentColor"
            stroke-width="1.2"
            stroke-linejoin="round"
            opacity="0.4"
          />
          <path d="M14 2v5h5" stroke="currentColor" stroke-width="1.2" opacity="0.4" />
          <path
            d="M8 13h8M8 16h5"
            stroke="currentColor"
            stroke-width="1.2"
            stroke-linecap="round"
            opacity="0.3"
          />
        </svg>
      </div>
      <div class="empty-title">未选择对象</div>
      <div class="empty-sub">从左侧目录选择一个文件以预览其内容</div>
    </div>

    <template v-else>
      <div class="meta-bar">
        <div class="meta-left">
          <span v-if="detail?.type" class="badge badge-type">{{ detail.type }}</span>
          <span v-if="detail?.nf" class="badge">{{ detail.nf }}</span>
          <span v-if="detail?.version" class="badge badge-ver mono">{{ detail.version }}</span>
          <span class="meta-id mono" :title="objectId">{{ objectId }}</span>
        </div>
        <div class="meta-right">
          <el-select
            v-if="versions.length > 1"
            v-model="selectedVersion"
            size="small"
            class="ver-select"
            @change="onVersionChange"
          >
            <el-option
              v-for="v in versions"
              :key="v"
              :label="v"
              :value="v"
            />
          </el-select>
          <el-button size="small" :icon="GraphIcon" @click="goGraph">
            在图谱中查看
          </el-button>
        </div>
      </div>

      <div class="fm-bar" v-if="fmEntries.length">
        <span v-for="e in fmEntries" :key="e.k" class="fm-item">
          <span class="fm-key mono">{{ e.k }}</span>
          <span class="fm-val mono">{{ e.v }}</span>
        </span>
      </div>

      <div v-loading="loading" class="md-scroll">
        <article v-if="html" class="md-body" v-html="html"></article>
        <div v-else-if="!loading" class="empty small">
          <div class="empty-sub">无内容</div>
        </div>
      </div>
    </template>
  </div>
</template>

<script setup lang="ts">
import { computed, h, ref, watch } from 'vue'
import { useRouter } from 'vue-router'
import MarkdownIt from 'markdown-it'
import DOMPurify from 'dompurify'
import { getObject, getMd, availableVersionsFromError, type ObjectDetail } from '../api'

const props = defineProps<{ objectId: string | null }>()
const router = useRouter()

const md = new MarkdownIt({
  html: false,
  linkify: true,
  breaks: false,
  typographer: false,
})

const detail = ref<ObjectDetail | null>(null)
const html = ref('')
const loading = ref(false)
const selectedVersion = ref<string>('')

const versions = computed(() => detail.value?.versions ?? [])
const fmEntries = computed(() => {
  const fm = detail.value?.frontmatter
  if (!fm) return []
  return Object.entries(fm)
    .filter(([k]) => !['id', 'type', 'nf', 'version'].includes(k))
    .slice(0, 8)
    .map(([k, v]) => ({ k, v: formatFm(v) }))
})

function formatFm(v: unknown): string {
  if (v == null) return ''
  if (typeof v === 'string' || typeof v === 'number' || typeof v === 'boolean') {
    return String(v)
  }
  if (Array.isArray(v)) return v.join(', ')
  return JSON.stringify(v)
}

const GraphIcon = () =>
  h(
    'svg',
    { width: '14', height: '14', viewBox: '0 0 24 24', fill: 'none' },
    [
      h('circle', { cx: '6', cy: '7', r: '2', stroke: 'currentColor', 'stroke-width': '1.7' }),
      h('circle', { cx: '18', cy: '7', r: '2', stroke: 'currentColor', 'stroke-width': '1.7' }),
      h('circle', { cx: '12', cy: '17', r: '2', stroke: 'currentColor', 'stroke-width': '1.7' }),
      h('path', {
        d: 'M7.8 8.3 16.2 8.3 M7 8.7 10.8 15 M17 8.7 13.2 15',
        stroke: 'currentColor',
        'stroke-width': '1.4',
        opacity: '0.6',
      }),
    ],
  )

async function load(id: string, ver?: string): Promise<void> {
  loading.value = true
  html.value = ''
  try {
    const [obj, raw] = await Promise.all([
      getObject(id, ver),
      getMd(id, ver),
    ])
    detail.value = obj
    selectedVersion.value = obj.version ?? ver ?? ''
    html.value = DOMPurify.sanitize(md.render(raw || ''))
  } catch (e: unknown) {
    const avail = availableVersionsFromError(e)
    detail.value = null
    if (avail && avail.length) {
      html.value = `<p style="color:var(--text-muted)">该版本缺失，可用版本：<code>${avail.join(
        ', ',
      )}</code></p>`
    } else {
      const msg = e instanceof Error ? e.message : String(e)
      html.value = `<p style="color:var(--danger)">加载失败：${escapeHtml(msg)}</p>`
    }
  } finally {
    loading.value = false
  }
}

function escapeHtml(s: string): string {
  return s
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
}

function onVersionChange(v: string): void {
  if (props.objectId) load(props.objectId, v)
}

function goGraph(): void {
  if (!props.objectId) return
  router.push({
    path: '/graph',
    query: { o: props.objectId, version: selectedVersion.value || undefined },
  })
}

watch(
  () => props.objectId,
  (id) => {
    if (id) load(id)
  },
  { immediate: true },
)
</script>

<style scoped>
.md-preview {
  display: flex;
  flex-direction: column;
  height: 100%;
  background: var(--bg-elev);
}

.empty {
  flex: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: var(--space-2);
  color: var(--text-faint);
}

.empty.small {
  padding: var(--space-10);
}

.empty-icon {
  color: var(--text-faint);
  margin-bottom: var(--space-2);
}

.empty-title {
  font-family: var(--display);
  font-size: 16px;
  font-weight: 600;
  color: var(--text-muted);
}

.empty-sub {
  font-size: 13px;
}

.meta-bar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: var(--space-3);
  padding: var(--space-3) var(--space-5);
  border-bottom: 1px solid var(--border);
  background: var(--bg-elev);
  flex-wrap: wrap;
}

.meta-left {
  display: flex;
  align-items: center;
  gap: var(--space-2);
  min-width: 0;
  flex: 1;
}

.meta-right {
  display: flex;
  align-items: center;
  gap: var(--space-2);
  flex-shrink: 0;
}

.badge {
  display: inline-flex;
  align-items: center;
  font-size: 11px;
  font-weight: 500;
  padding: 2px 8px;
  border-radius: var(--radius-sm);
  background: var(--bg-sunken);
  color: var(--text-muted);
  border: 1px solid var(--border);
}

.badge-type {
  background: var(--accent-soft);
  color: var(--accent);
  border-color: transparent;
}

.badge-ver {
  font-size: 10.5px;
}

.meta-id {
  font-size: 12px;
  color: var(--text-muted);
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
  min-width: 0;
}

.fm-bar {
  display: flex;
  flex-wrap: wrap;
  gap: var(--space-2);
  padding: var(--space-2) var(--space-5);
  border-bottom: 1px solid var(--border-faint);
  background: var(--bg-sunken);
}

.fm-item {
  display: inline-flex;
  gap: 6px;
  font-size: 11.5px;
  align-items: baseline;
}

.fm-key {
  color: var(--text-faint);
}

.fm-val {
  color: var(--text);
}

.ver-select {
  width: 130px;
}

.md-scroll {
  flex: 1;
  overflow: auto;
  padding: var(--space-5) var(--space-6);
}
</style>
