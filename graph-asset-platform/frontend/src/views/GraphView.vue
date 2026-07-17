<template>
  <div class="graph-view stagger-in">
    <div class="graph-toolbar">
      <div class="search-wrap">
        <el-input
          v-model="searchId"
          placeholder="输入对象 id（如 UDG@MMLCommand@ACT ACSPACKAGE）"
          :prefix-icon="SearchIcon"
          clearable
          class="search-input"
          @keyup.enter="onSearch"
        />
        <el-button type="primary" :loading="loading" @click="onSearch">聚焦</el-button>
      </div>
      <el-select
        v-if="nfOptions.length"
        v-model="versionFilter"
        placeholder="版本"
        size="default"
        class="ver-filter"
      >
        <el-option v-for="v in versionOptions" :key="v" :label="v" :value="v" />
      </el-select>
    </div>

    <div v-if="error" class="graph-error">
      <svg width="16" height="16" viewBox="0 0 24 24" fill="none">
        <circle cx="12" cy="12" r="9" stroke="currentColor" stroke-width="1.8" />
        <path d="M12 7v6m0 3v.5" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" />
      </svg>
      <span class="mono">{{ error }}</span>
    </div>

    <div class="graph-body">
      <Splitpanes class="graph-panes default-theme">
        <Pane :size="68" :min-size="40">
          <div class="canvas-col">
            <div v-if="loading && !focusPayload" class="canvas-loading">
              <svg width="40" height="40" viewBox="0 0 24 24" fill="none" class="spin">
                <path d="M12 3a9 9 0 1 0 9 9" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" />
              </svg>
              <span>加载邻居关系…</span>
            </div>
            <div v-else-if="!focusPayload && !overviewPayload && !error" class="canvas-loading">
              <span>加载业务概览…</span>
            </div>
            <GraphCanvas
              v-if="focusPayload"
              :focus="focusPayload"
              @node-click="focusOn"
            />
            <GraphCanvas
              v-else-if="overviewPayload"
              :focus="overviewPayload"
              :is-overview="true"
              @node-click="focusOn"
            />
            <div v-if="!focusPayload && overviewPayload" class="overview-hint">
              <span class="hint-pill">概览：业务结构，点节点钻取或搜索任意对象</span>
            </div>
          </div>
        </Pane>
        <Pane :size="32" :min-size="18" :max-size="55">
          <aside class="detail-col">
            <ObjectDetailPanel
              :center="center"
              :out="out"
              :in-edges="inEdges"
              @navigate="focusOn"
            />
          </aside>
        </Pane>
      </Splitpanes>
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed, h, onMounted, ref, watch } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { Splitpanes, Pane } from 'splitpanes'
import 'splitpanes/dist/splitpanes.css'
import GraphCanvas from '../components/GraphCanvas.vue'
import ObjectDetailPanel from '../components/ObjectDetail.vue'
import { neighbors, overview, stats } from '../api'
import type { Edge, ObjectDetail as ObjectDetailData, Stats } from '../api'

const route = useRoute()
const router = useRouter()

const searchId = ref((route.query.o as string) || '')
const versionFilter = ref<string>('')
const loading = ref(false)
const error = ref('')
const focusPayload = ref<{
  centerId: string
  centerDetail: ObjectDetailData | null
  out: Edge[]
  in: Edge[]
  version?: string
} | null>(null)

// 概览图 payload（GraphView 初始默认渲染，无需指定对象）
const overviewPayload = ref<{
  centerId: string
  centerDetail: null
  out: Edge[]
  in: Edge[]
  isOverview?: boolean
} | null>(null)

const center = ref<ObjectDetailData | null>(null)
const out = ref<Edge[]>([])
const inEdges = ref<Edge[]>([])

const globalStats = ref<Stats | null>(null)
const nfOptions = computed(() => globalStats.value?.nfs ?? [])
const versionOptions = computed(() => {
  const perNf = globalStats.value?.versions_per_nf
  if (!perNf) return []
  return Array.from(new Set(Object.values(perNf).flat()))
})

const SearchIcon = () =>
  h(
    'svg',
    { width: '14', height: '14', viewBox: '0 0 24 24', fill: 'none' },
    [
      h('circle', { cx: '11', cy: '11', r: '7', stroke: 'currentColor', 'stroke-width': '2' }),
      h('path', {
        d: 'M20 20l-3.2-3.2',
        stroke: 'currentColor',
        'stroke-width': '2',
        'stroke-linecap': 'round',
      }),
    ],
  )

async function focusOn(id: string): Promise<void> {
  const trimmed = id.trim()
  if (!trimmed) return
  searchId.value = trimmed
  loading.value = true
  error.value = ''
  // 钻取时清空概览，只显示聚焦邻居
  overviewPayload.value = null
  try {
    const ver = versionFilter.value || undefined
    const r = await neighbors(trimmed, ver, 1)
    center.value = r.center
    out.value = r.out
    inEdges.value = r.in
    focusPayload.value = {
      centerId: r.center.id,
      centerDetail: r.center,
      out: r.out,
      in: r.in,
      version: ver,
    }
    syncUrl(trimmed)
  } catch (e: unknown) {
    center.value = null
    out.value = []
    inEdges.value = []
    focusPayload.value = null
    error.value = e instanceof Error ? e.message : String(e)
  } finally {
    loading.value = false
  }
}

async function loadOverview(): Promise<void> {
  loading.value = true
  error.value = ''
  focusPayload.value = null
  center.value = null
  out.value = []
  inEdges.value = []
  try {
    const ov = await overview()
    // 概览图无中心：用占位 centerId，把所有业务节点当 out 邻居渲染
    const fakeCenterId = '__overview__'
    const nodes = ov.nodes || []
    const edges = ov.edges || []
    // 每个业务节点作为 fake center 的"邻居"，边直接转 Edge[]
    const outEdges: Edge[] = edges.map((e: { from: string; relation: string; to: string }) => ({
      from: e.from,
      relation: e.relation,
      to: e.to,
    }))
    // 把孤立节点也作为 fake center 邻居（否则 vis 不画它们）
    const referenced = new Set<string>()
    for (const e of edges) {
      referenced.add(e.from)
      referenced.add(e.to)
    }
    for (const n of nodes) {
      if (!referenced.has(n.id)) {
        outEdges.push({ from: fakeCenterId, relation: 'contains', to: n.id })
      }
    }
    overviewPayload.value = {
      centerId: fakeCenterId,
      centerDetail: null,
      out: outEdges,
      in: [],
      isOverview: true,
    }
  } catch (e: unknown) {
    overviewPayload.value = null
    error.value = e instanceof Error ? e.message : String(e)
  } finally {
    loading.value = false
  }
}

function onSearch(): void {
  if (searchId.value.trim()) focusOn(searchId.value)
}

function syncUrl(id: string): void {
  router.replace({
    path: '/graph',
    query: { o: id, version: versionFilter.value || undefined },
  })
}

watch(
  () => route.query.o,
  (o) => {
    const id = (o as string) || ''
    if (id && id !== searchId.value) {
      searchId.value = id
      focusOn(id)
    }
  },
)

onMounted(async () => {
  try {
    globalStats.value = await stats()
    if (!versionFilter.value && versionOptions.value.length === 1) {
      versionFilter.value = versionOptions.value[0]
    }
  } catch {
    /* 降级：无版本过滤 */
  }
  if (searchId.value) {
    focusOn(searchId.value)
  } else {
    // 默认渲染业务概览
    loadOverview()
  }
})
</script>

<style scoped>
.graph-view {
  display: flex;
  flex-direction: column;
  height: 100%;
  min-height: 0;
}

.graph-toolbar {
  display: flex;
  align-items: center;
  gap: var(--space-3);
  padding: var(--space-3) var(--space-5);
  border-bottom: 1px solid var(--border);
  background: var(--bg-elev);
  flex-shrink: 0;
}

.search-wrap {
  display: flex;
  gap: var(--space-2);
  flex: 1;
  max-width: 640px;
}

.search-input {
  flex: 1;
}

.ver-filter {
  width: 160px;
  flex-shrink: 0;
}

.graph-error {
  display: flex;
  align-items: center;
  gap: var(--space-2);
  padding: var(--space-3) var(--space-5);
  background: #fef2f2;
  border-bottom: 1px solid #fecaca;
  color: var(--danger);
  font-size: 12.5px;
}

.graph-body {
  flex: 1;
  min-height: 0;
}

.graph-panes {
  height: 100%;
}

.canvas-col {
  position: relative;
  height: 100%;
  min-width: 0;
  overflow: hidden;
  border-right: 1px solid var(--border);
}

.canvas-loading {
  position: absolute;
  inset: 0;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: var(--space-2);
  color: var(--text-faint);
  pointer-events: none;
  background: var(--bg-elev);
  z-index: 1;
}

.overview-hint {
  position: absolute;
  top: var(--space-3);
  left: 50%;
  transform: translateX(-50%);
  z-index: 2;
  pointer-events: none;
}

.hint-pill {
  display: inline-block;
  font-size: 11.5px;
  color: var(--text-muted);
  background: var(--bg-elev);
  border: 1px solid var(--border);
  padding: 4px 12px;
  border-radius: 999px;
  box-shadow: var(--shadow-sm);
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

.detail-col {
  height: 100%;
  overflow: hidden;
  background: var(--bg-elev);
}

/* splitpanes 主题定制（与 AssetsView 一致） */
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

@media (max-width: 900px) {
  .detail-col {
    display: none;
  }
}
</style>
