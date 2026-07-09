<template>
  <div class="wiki-page">
    <div class="wiki-crumb">
      <span v-if="!history.length" class="wiki-crumb-hint">图谱总览 · 在左侧选择对象开始浏览</span>
      <template v-for="(h, i) in history" :key="i">
        <span class="wiki-crumb-item" :class="{ active: i === history.length - 1 }" @click="backTo(i)">
          {{ labelOf(h) }}
        </span>
        <span v-if="i < history.length - 1" class="wiki-crumb-sep">›</span>
      </template>
    </div>
    <div class="wiki-shell">
      <aside class="wiki-left"><CategoryTree @select="select" /></aside>
      <section class="wiki-center"><MdPane :path="currentPath" @navigate="select" /></section>
      <aside class="wiki-right"><NeighborGraph :center-path="currentPath" @navigate="select" /></aside>
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
</script>

<style scoped>
.wiki-page { display: flex; flex-direction: column; height: calc(100vh - var(--navbar-height)); }
.wiki-crumb { padding: 6px 16px; border-bottom: 1px solid var(--border); font-size: 13px; color: var(--text-tertiary); min-height: 32px; display: flex; flex-wrap: wrap; gap: 2px; align-items: center; }
.wiki-crumb-hint { color: var(--text-tertiary); }
.wiki-crumb-item { cursor: pointer; padding: 0 2px; }
.wiki-crumb-item:hover { color: var(--text-primary, #1a1d23); }
.wiki-crumb-item.active { color: var(--text-primary, #1a1d23); font-weight: 600; cursor: default; }
.wiki-crumb-sep { color: var(--text-tertiary); margin: 0 2px; }
.wiki-shell { flex: 1; display: grid; grid-template-columns: 300px 1fr 1fr; min-height: 0; }
.wiki-left { border-right: 1px solid var(--border); overflow: auto; padding: 10px; }
.wiki-center { overflow: auto; padding: 16px 24px; }
.wiki-right { border-left: 1px solid var(--border); overflow: hidden; padding: 10px; }
</style>
