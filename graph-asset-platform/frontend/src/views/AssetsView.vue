<template>
  <div class="assets-view stagger-in">
    <Splitpanes class="assets-panes default-theme" @resized="onPaneResize">
      <Pane :size="leftSize" :min-size="15" :max-size="40">
        <AssetTree class="col-tree" @select="onSelect" />
      </Pane>
      <Pane :size="midSize" :min-size="30">
        <div class="col-main">
          <MdPreview :object-id="selectedId" @navigate="onNavigate" />
        </div>
      </Pane>
      <Pane :size="rightSize" :min-size="12" :max-size="35">
        <aside class="col-edges">
          <EdgeList :object-id="selectedId" @navigate="onNavigate" />
        </aside>
      </Pane>
    </Splitpanes>
  </div>
</template>

<script setup lang="ts">
import { ref, watch } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { Splitpanes, Pane } from 'splitpanes'
import 'splitpanes/dist/splitpanes.css'
import AssetTree from '../components/AssetTree.vue'
import MdPreview from '../components/MdPreview.vue'
import EdgeList from '../components/EdgeList.vue'

const route = useRoute()
const router = useRouter()
const selectedId = ref<string | null>((route.query.o as string) || null)

// 三列默认占比（百分比）。min/max 限制防止拖拽挤压到不可用。
const leftSize = ref(24)
const midSize = ref(54)
const rightSize = ref(22)

function onSelect(id: string): void {
  selectedId.value = id
}

function onNavigate(id: string): void {
  // 接收 MdPreview / EdgeList 的内联 wikilink 跳转
  selectedId.value = id
}

function onPaneResize(payload: { panes: { size: number }[] }): void {
  const panes = payload.panes
  if (panes.length === 3) {
    leftSize.value = panes[0].size
    midSize.value = panes[1].size
    rightSize.value = panes[2].size
  }
}

// URL 同步选中对象（可分享、可从图谱回跳）
watch(selectedId, (id) => {
  const q = { ...route.query }
  if (id) q.o = id
  else delete q.o
  router.replace({ path: '/assets', query: q })
})

watch(
  () => route.query.o,
  (o) => {
    const id = (o as string) || null
    if (id !== selectedId.value) selectedId.value = id
  },
)
</script>

<style scoped>
.assets-view {
  height: 100%;
  min-height: 0;
}

.assets-panes {
  height: 100%;
}

.col-tree {
  height: 100%;
  border-right: 1px solid var(--border);
  min-width: 0;
  overflow: hidden;
}

.col-main {
  height: 100%;
  min-width: 0;
  overflow: hidden;
}

.col-edges {
  height: 100%;
  border-left: 1px solid var(--border);
  background: var(--bg-elev);
  overflow: auto;
}

/* splitpanes 主题定制：细分隔条 + hover 高亮（用 tokens 变量） */
:deep(.splitpanes__splitter) {
  background: var(--border);
  position: relative;
  flex-shrink: 0;
}

:deep(.splitpanes--vertical > .splitpanes__splitter) {
  width: 5px;
  margin-left: -2px;
  border-left: 2px solid transparent;
  border-right: 2px solid transparent;
  transition: background var(--dur-fast) var(--ease),
    border-color var(--dur-fast) var(--ease);
}

:deep(.splitpanes--vertical > .splitpanes__splitter:hover),
:deep(.splitpanes--vertical > .splitpanes__splitter.active) {
  background: var(--accent-soft);
  border-left-color: var(--accent);
  border-right-color: var(--accent);
}

:deep(.splitpanes__pane) {
  background: transparent;
  overflow: hidden;
  display: flex;
  min-width: 0;
}

:deep(.splitpanes__pane > *) {
  flex: 1;
  min-width: 0;
}

@media (max-width: 1100px) {
  .col-edges {
    display: none;
  }
}

@media (max-width: 760px) {
  .col-tree {
    max-height: 40vh;
    border-right: none;
    border-bottom: 1px solid var(--border);
  }
}
</style>
