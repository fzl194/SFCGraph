<template>
  <div class="doc-viewer" v-html="rendered" @click="handleClick"></div>
</template>

<script setup lang="ts">
import { computed } from 'vue'
import MarkdownIt from 'markdown-it'
import DOMPurify from 'dompurify'

const FILE_BASE = '/api/v1/feature-graph/file?path='
const DOC_BASE = '/api/v1/feature-graph/doc-content?path='

const props = defineProps<{
  content: string
  filePath: string
}>()

const emit = defineEmits<{
  (e: 'open-ref', path: string, title: string): void
}>()

const md = new MarkdownIt({ html: true, linkify: true, breaks: true })

// Get directory of current MD file for resolving relative paths
function getBaseDir(filePath: string): string {
  const idx = filePath.lastIndexOf('/')
  return idx >= 0 ? filePath.substring(0, idx + 1) : ''
}

// Resolve a relative path against a base directory
function resolvePath(base: string, rel: string): string {
  // Normalize to forward slashes
  const parts = (base + rel).split('/')
  const resolved: string[] = []
  for (const part of parts) {
    if (part === '' || part === '.') continue
    if (part === '..') {
      resolved.pop()
    } else {
      resolved.push(part)
    }
  }
  return resolved.join('/')
}

// Strip optional markdown title from URL: 'url "title"' → 'url'
function stripTitle(url: string): string {
  return url.replace(/\s+["'][^"']*["']\s*$/, '').trim()
}

function processContent(raw: string, filePath: string): string {
  const baseDir = getBaseDir(filePath)

  // 0. Strip leading H1 — the sidebar already shows the doc title,
  //    and the MD file almost always repeats it as "# GWFD-xxxx 特性名称"
  let processed = raw.replace(/^#\s+.+$/m, (match, offset) => {
    // Only strip if it's in the first 3 lines (actual title, not a section heading)
    return offset < 200 ? '' : match
  }).replace(/^\s+/, '')

  // 1. Rewrite image references: ![alt](url "title") → img with backend URL
  processed = processed.replace(
    /!\[([^\]]*)\]\(([^)]+)\)/g,
    (_match, alt, rawSrc) => {
      const src = stripTitle(rawSrc)
      // Skip already-absolute URLs
      if (src.startsWith('http://') || src.startsWith('https://') || src.startsWith('data:')) {
        return `![${alt}](${src})`
      }
      const resolved = resolvePath(baseDir, src)
      const encoded = encodeURIComponent(resolved)
      return `![${alt}](${FILE_BASE}${encoded})`
    }
  )

  // 2. Rewrite MD links: [text](url "title") → clickable with data attribute
  processed = processed.replace(
    /\[([^\]]+)\]\(([^)]+)\)/g,
    (_match, text, rawHref) => {
      const href = stripTitle(rawHref)
      if (!href.endsWith('.md')) return `[${text}](${rawHref})`
      const resolved = resolvePath(baseDir, href)
      const encoded = encodeURIComponent(resolved)
      return `[${text}](#md-ref:${encoded})`
    }
  )

  return processed
}

const rendered = computed(() => {
  if (!props.content) return ''
  const processed = processContent(props.content, props.filePath || '')
  const html = md.render(processed)
  return DOMPurify.sanitize(html, {
    ADD_ATTR: ['target'],
  })
})

function handleClick(event: MouseEvent) {
  const target = event.target as HTMLElement
  const anchor = target.closest('a') as HTMLAnchorElement | null
  if (!anchor) return

  const href = anchor.getAttribute('href') || ''
  // Handle MD cross-references
  if (href.startsWith('#md-ref:')) {
    event.preventDefault()
    const encodedPath = href.substring('#md-ref:'.length)
    const path = decodeURIComponent(encodedPath)
    const title = anchor.textContent || path.split('/').pop() || 'Reference'
    emit('open-ref', path, title)
  }
}
</script>
