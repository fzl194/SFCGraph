<template>
  <div v-if="loading" v-loading="true" class="md-pane md-pane-loading"></div>
  <div v-else-if="error" class="md-pane md-pane-empty">该页加载失败：{{ error }}</div>
  <div v-else-if="!content" class="md-pane md-pane-empty">
    图谱总览 · 在左侧选择对象，或在任意 md / 图谱节点间点击跳转。
  </div>
  <div v-else class="md-pane md-pane-doc" v-html="rendered" @click="handleClick"></div>
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
.md-pane { min-height: 200px; }
.md-pane-loading { height: 400px; }
.md-pane-empty { color: var(--text-tertiary); padding: 60px 20px; text-align: center; }
.md-pane-doc :deep(.md-placeholder) { color: #94a3b8; background: #f1f5f9; padding: 0 4px; border-radius: 3px; font-family: monospace; font-size: 0.9em; }
.md-pane-doc :deep(h1) { font-size: 1.5rem; margin: 0 0 12px; }
.md-pane-doc :deep(h2) { font-size: 1.15rem; margin: 20px 0 8px; border-bottom: 1px solid var(--border); padding-bottom: 4px; }
.md-pane-doc :deep(table) { border-collapse: collapse; width: 100%; margin: 8px 0; }
.md-pane-doc :deep(th), .md-pane-doc :deep(td) { border: 1px solid var(--border); padding: 6px 8px; vertical-align: top; }
.md-pane-doc :deep(a) { color: #0891b2; cursor: pointer; }
</style>
