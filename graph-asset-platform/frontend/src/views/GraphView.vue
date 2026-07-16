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
      <div class="canvas-col">
        <div v-if="loading && !focusPayload" class="canvas-loading">
          <svg width="40" height="40" viewBox="0 0 24 24" fill="none" class="spin">
            <path d="M12 3a9 9 0 1 0 9 9" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" />
          </svg>
          <span>加载邻居关系…</span>
        </div>
        <div v-else-if="!focusPayload && !error" class="canvas-placeholder">
          <div class="ph-title">知识图谱浏览器</div>
          <div class="ph-sub">输入或粘贴一个对象 id，查看其单跳邻居关系</div>
          <div class="ph-hint mono">只渲染单跳邻居，保证大规模数据下流畅</div>
        </div>
        <GraphCanvas v-if="focusPayload" :focus="focusPayload" @node-click="focusOn" />
      </div>

      <aside class="detail-col">
        <ObjectDetailPanel
          :center="center"
          :out="out"
          :in-edges="inEdges"
          @navigate="focusOn"
        />
      </aside>
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed, h, onMounted, ref, watch } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import GraphCanvas from '../components/GraphCanvas.vue'
import ObjectDetailPanel from '../components/ObjectDetail.vue'
import { neighbors, stats } from '../api'
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
  if (searchId.value) focusOn(searchId.value)
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
  display: grid;
  grid-template-columns: 1fr 340px;
  min-height: 0;
}

.canvas-col {
  position: relative;
  min-width: 0;
  overflow: hidden;
  border-right: 1px solid var(--border);
}

.canvas-loading,
.canvas-placeholder {
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
}

.canvas-placeholder {
  gap: var(--space-3);
}

.ph-title {
  font-family: var(--display);
  font-size: 20px;
  font-weight: 700;
  color: var(--text-muted);
}

.ph-sub {
  font-size: 13.5px;
}

.ph-hint {
  font-size: 11.5px;
  color: var(--text-faint);
  background: var(--bg-sunken);
  padding: 3px 10px;
  border-radius: 999px;
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
  overflow: hidden;
  background: var(--bg-elev);
}

@media (max-width: 900px) {
  .graph-body {
    grid-template-columns: 1fr;
  }
  .detail-col {
    display: none;
  }
}
</style>
