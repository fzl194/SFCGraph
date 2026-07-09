<template>
  <div class="md-scroll" v-loading="loading">
    <div v-if="error" class="md-state">
      <div class="md-state-icon md-state-icon--err">⚠</div>
      <div class="md-state-title">该页加载失败</div>
      <div class="md-state-desc">{{ error }}</div>
    </div>
    <div v-else-if="!content && !loading" class="md-state">
      <div class="md-state-icon">▤</div>
      <div class="md-state-title">图谱总览</div>
      <div class="md-state-desc">
        在左侧选择对象，或在文档链接 / 图谱节点间点击跳转。<br />
        URL 驱动 —— 可前进后退、可分享。
      </div>
    </div>
    <article v-else class="doc-viewer md-article" v-html="rendered" @click="handleClick"></article>
  </div>
</template>

<script setup lang="ts">
import { ref, watch, computed } from 'vue'
import MarkdownIt from 'markdown-it'
import DOMPurify from 'dompurify'
import { wikiApi } from './wikiApi'

const props = defineProps<{ path: string | null }>()
const emit = defineEmits<{ (e: 'navigate', path: string): void }>()

const content = ref('')
const meta = ref<{ type?: string; name?: string; title?: string }>({})
const loading = ref(false)
const error = ref('')

const md = new MarkdownIt({ html: true, linkify: true, breaks: true })

const rendered = computed(() => {
  if (!content.value) return ''
  // assets 根相对链接 → 拦截为 #md-ref: 占位；[[ID]] 占位 → 灰 chip
  let src = content.value
  src = src.replace(/\[\[([^\]]+)\]\]/g, (_m, id) =>
    `<span class="md-placeholder" title="未构建：${id}">${id}</span>`)
  src = src.replace(/!\[([^\]]*)\]\(([^)]+)\)/g, '[_img_]')  // 简化：暂不渲染图
  src = src.replace(/\[([^\]]+)\]\(([^)\s]+?)(?:\s+"[^"]*")?\)/g, (m, text, href) => {
    if (!href.endsWith('.md')) return m
    return `[${text}](#md-ref:${encodeURIComponent(href)})`
  })
  return DOMPurify.sanitize(md.render(src), { ADD_ATTR: ['target'] })
})

async function load() {
  if (!props.path) { content.value = ''; return }
  loading.value = true; error.value = ''
  try {
    const res = await wikiApi.md(props.path)
    content.value = res.content; meta.value = res.meta
  } catch (e: unknown) {
    content.value = ''; error.value = e instanceof Error ? e.message : '未知错误'
  } finally { loading.value = false }
}

watch(() => props.path, load, { immediate: true })

function handleClick(ev: MouseEvent) {
  const a = (ev.target as HTMLElement).closest('a') as HTMLAnchorElement | null
  if (!a) return
  const href = a.getAttribute('href') || ''
  if (href.startsWith('#md-ref:')) {
    ev.preventDefault()
    emit('navigate', decodeURIComponent(href.substring('#md-ref:'.length)))
  }
}
</script>

<style scoped>
.md-scroll { flex: 1; overflow-y: auto; overflow-x: hidden; }

/* centered readable column — inherits global .doc-viewer typography */
.md-article { max-width: 880px; margin: 0 auto; padding: var(--space-8) var(--space-8) var(--space-12); }

/* 宽/长表格：横向滚动，不再撑破版面；表头吸顶便于阅读 */
.md-article :deep(table) {
  display: block;
  max-width: 100%;
  overflow-x: auto;
}
.md-article :deep(th) { position: sticky; top: 0; z-index: 1; }

/* [[ID]] placeholder chip */
.md-article :deep(.md-placeholder) {
  font-family: var(--font-mono);
  font-size: 0.82em;
  color: var(--text-tertiary);
  background: var(--bg-page);
  border: 1px dashed var(--border);
  padding: 1px 6px;
  border-radius: var(--radius-sm);
  white-space: nowrap;
}

/* empty / error state — placeholder-page pattern */
.md-state {
  flex: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: var(--space-3);
  padding: var(--space-12);
  text-align: center;
  color: var(--text-tertiary);
}
.md-state-icon {
  width: 56px; height: 56px;
  border-radius: var(--radius-lg);
  background: var(--accent-soft);
  color: var(--accent);
  display: flex; align-items: center; justify-content: center;
  font-size: 26px;
}
.md-state-icon--err { background: var(--danger-soft); color: var(--danger); }
.md-state-title { font-size: var(--text-xl); font-weight: 600; color: var(--text-secondary); }
.md-state-desc { font-size: var(--text-sm); line-height: 1.7; max-width: 380px; }
</style>
