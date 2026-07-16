<template>
  <div class="browser-view">
    <TopBar
      ref="topBarRef"
      @version-change="onVersionChange"
      @imported="onImported"
    />

    <div class="main-row">
      <div class="pane left-pane">
        <ObjectIndex
          ref="indexRef"
          :selected-id="currentId"
          :refresh-key="indexRefreshKey"
          @select="onSelectFromIndex"
        />
      </div>

      <div class="pane center-pane">
        <MdPane
          :id="currentId"
          :version="resolvedVersion"
          @fallback-version="onFallbackVersion"
        />
      </div>

      <div class="pane right-pane">
        <NeighborGraph
          :id="currentId"
          :version="resolvedVersion"
          @select="onSelectFromGraph"
        />
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, computed, watch } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import TopBar from '../components/TopBar.vue'
import ObjectIndex from '../components/ObjectIndex.vue'
import MdPane from '../components/MdPane.vue'
import NeighborGraph from '../components/NeighborGraph.vue'
import type { ImportResult } from '../api'

const route = useRoute()
const router = useRouter()

const topBarRef = ref<InstanceType<typeof TopBar> | null>(null)
const indexRef = ref<InstanceType<typeof ObjectIndex> | null>(null)
const indexRefreshKey = ref(0)

// 版本选择器：nf → version 映射（空串=最新）
const versionMap = ref<Record<string, string>>({})
// 当前对象详情（用于按其 nf 解析版本）
const currentNf = ref<string | undefined>(undefined)

// URL 中的 o（对象 id）与 version
const currentId = computed(() => (route.query.o as string) || '')
const urlVersion = computed(() => (route.query.version as string) || '')

// 实际使用的版本：优先 URL 显式 version（来源：MdPane 回退/切换也会写回 URL）
// resolvedVersion=undefined → 后端默认最新
const resolvedVersion = computed(() => urlVersion.value || undefined)

function onSelectFromIndex(id: string) {
  pushUrl(id, undefined)
}

function onSelectFromGraph(id: string) {
  pushUrl(id, undefined)
}

function pushUrl(id: string, version: string | undefined) {
  // 查询：切换对象时清掉旧 version，交由版本选择器按新对象 nf 重新解析
  // 但若显式给 version（如子组件回退），则带上
  const q: Record<string, string> = {}
  if (id) q.o = id
  // 对象切换时不自动继承 version（避免跨 nf 串版本）；显式传则用
  if (version !== undefined && version.length > 0) q.version = version
  router.push({ query: q })
}

// 版本选择器变更：把全局选中版本映射同步过来。
// 当 currentId 对应的 nf 有显式版本选择 → 写进 URL ?version=
function onVersionChange(selected: Record<string, string>) {
  versionMap.value = selected
  applyVersionByNf()
}

// 当对象切换后，需要按其 nf 应用版本选择器里该 nf 的版本
function applyVersionByNf() {
  if (!currentId.value || !currentNf.value) return
  const v = versionMap.value[currentNf.value]
  const wantVersion = v && v.length > 0 ? v : ''
  if (wantVersion !== urlVersion.value) {
    // 更新 URL version 段，保留 o
    router.replace({
      query: { o: currentId.value, ...(wantVersion ? { version: wantVersion } : {}) },
    })
  }
}

// MdPane 回退版本：404 版本缺失 / 用户手动切换版本
function onFallbackVersion(id: string, available: string[]) {
  // available 是“用户期望切到的版本列表”：取第一个（回退时通常是最新；切换时为单项）
  const target = available[0]
  if (!target) return
  // 若与当前 URL version 不同 → 写回
  if (target !== urlVersion.value) {
    router.replace({
      query: { o: id, ...(target ? { version: target } : {}) },
    })
  }
}

function onImported(_res: ImportResult) {
  // 刷新对象索引
  indexRefreshKey.value++
}

// 监听 URL 中 o 变化：取出其 nf（通过 MdPane 内部已加载详情，这里仅做轻量桥接）
// 实际 nf 来源：MdPane 加载后无法直接 emit，简化处理——用版本选择器取数，
// 这里 watch currentId：清掉旧 version，让组件按新对象重新请求；
// 版本联动靠 versionMap + applyVersionByNf（在 MdPane 渲染后需要 nf，故用一个额外 watch）。
watch(currentId, () => {
  // 切换对象时：清除 URL 上的 version（由后续按 nf 重新解析）
  if (urlVersion.value) {
    router.replace({ query: { o: currentId.value } })
  }
})
</script>

<style scoped>
.browser-view {
  display: flex;
  flex-direction: column;
  height: 100vh;
  width: 100vw;
  overflow: hidden;
}
.main-row {
  flex: 1;
  display: flex;
  min-height: 0;
  gap: 1px;
  background: #e4e7ed;
}
.pane {
  background: #fff;
  overflow: hidden;
  display: flex;
  flex-direction: column;
}
.left-pane {
  flex: 0 0 260px;
  min-width: 200px;
}
.center-pane {
  flex: 1 1 40%;
  min-width: 0;
}
.right-pane {
  flex: 0 0 360px;
  min-width: 280px;
}
</style>
