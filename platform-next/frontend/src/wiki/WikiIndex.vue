<template>
  <div class="wiki-page">
    <header class="wiki-crumb">
      <span class="wiki-crumb-label">PATH</span>
      <span v-if="!history.length" class="wiki-crumb-empty">在左侧选择对象开始浏览</span>
      <template v-for="(h, i) in history" :key="i">
        <span class="wiki-crumb-item" :class="{ active: i === history.length - 1 }" @click="backTo(i)">{{ labelOf(h) }}</span>
        <span v-if="i < history.length - 1" class="wiki-crumb-sep">›</span>
      </template>
    </header>
    <div class="wiki-shell">
      <aside class="wiki-pane wiki-left"><CategoryTree ref="categoryTreeRef" :current-path="currentPath" @select="select" /></aside>
      <section class="wiki-pane wiki-center"><MdPane :path="currentPath" @navigate="select" /></section>
      <aside class="wiki-pane wiki-right"><NeighborGraph :center-path="currentPath" @navigate="select" /></aside>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, computed, watch } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import CategoryTree from './CategoryTree.vue'
import MdPane from './MdPane.vue'
import NeighborGraph from './NeighborGraph.vue'

const route = useRoute()
const router = useRouter()

const currentPath = computed<string | null>(() => {
  const p = route.params.path
  return Array.isArray(p) ? p.join('/') : (p || null)
})

// 会话跳转历史（与会话面包屑绑定；浏览器前进/后退由 URL 驱动，与此解耦）
const history = ref<string[]>([])
const categoryTreeRef = ref<{ refresh: () => void } | null>(null)

function labelOf(p: string): string {
  return decodeURIComponent(p).split('/').pop()?.replace(/\.md$/, '') || p
}
function pushRoute(path: string) {
  router.push(`/graph-overview/a/${path}`)
}
function select(path: string) {            // 前进跳转（左树 / md 链接 / 图谱节点）
  if (history.value[history.value.length - 1] !== path) history.value.push(path)
  pushRoute(path)
}
function backTo(index: number) {           // 面包屑回跳：截断历史到该处
  history.value = history.value.slice(0, index + 1)
  pushRoute(history.value[index])
}
// 经 URL 直接落地（刷新 / 分享链接）时，若历史为空，用当前 path 做种子
watch(currentPath, (p) => {
  if (p && history.value.length === 0) history.value = [p]
}, { immediate: true })

// 重进「图谱总览」tab（路由落到 /graph-overview 首页）→ 刷新左树
watch(() => route.fullPath, (fp) => {
  if (fp === '/graph-overview') categoryTreeRef.value?.refresh()
})
</script>

<style scoped>
.wiki-page {
  display: flex;
  flex-direction: column;
  height: calc(100vh - var(--navbar-height));
  background: var(--bg-page);
}

/* breadcrumb — quiet functional strip, monospace path */
.wiki-crumb {
  display: flex;
  align-items: center;
  gap: var(--space-1);
  height: 38px;
  padding: 0 var(--space-5);
  background: var(--bg-card);
  border-bottom: 1px solid var(--border);
  font-size: var(--text-xs);
  flex-shrink: 0;
  overflow-x: auto;
  white-space: nowrap;
  box-shadow: var(--shadow-xs);
}
.wiki-crumb-label {
  color: var(--text-tertiary);
  text-transform: uppercase;
  letter-spacing: 0.08em;
  font-size: var(--text-2xs);
  font-weight: 700;
  margin-right: var(--space-3);
  flex-shrink: 0;
}
.wiki-crumb-empty { color: var(--text-tertiary); }
.wiki-crumb-item {
  font-family: var(--font-mono);
  color: var(--text-secondary);
  cursor: pointer;
  padding: 2px 6px;
  border-radius: var(--radius-sm);
  transition: all var(--duration) var(--ease);
}
.wiki-crumb-item:hover { background: var(--accent-soft); color: var(--accent); }
.wiki-crumb-item.active { color: var(--accent); font-weight: 600; cursor: default; }
.wiki-crumb-sep { color: var(--text-tertiary); margin: 0 1px; }

/* 3-pane shell */
.wiki-shell {
  flex: 1;
  display: grid;
  grid-template-columns: 300px minmax(0, 1fr) minmax(0, 1fr);
  min-height: 0;
}
.wiki-pane { min-height: 0; overflow: hidden; display: flex; flex-direction: column; }
.wiki-left { background: var(--bg-card); border-right: 1px solid var(--border); }
.wiki-center { background: var(--bg-page); }
.wiki-right { background: var(--bg-card); border-left: 1px solid var(--border); }
</style>
