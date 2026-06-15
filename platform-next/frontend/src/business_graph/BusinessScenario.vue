<template>
  <div class="explorer-root" v-if="!loading && ready">
    <div class="explorer-header">
      <button class="back-btn" @click="goBack">← 返回</button>
      <div class="explorer-breadcrumb">
        <template v-if="isDomainMode">
          <span class="breadcrumb-domain">{{ domainName }}</span>
          <span class="breadcrumb-sep">/</span>
          <span class="breadcrumb-scenario">{{ scenarioCount }} 个场景合并视图</span>
        </template>
        <template v-else>
          <span class="breadcrumb-domain">{{ scenario.domain_name }}</span>
          <span class="breadcrumb-sep">/</span>
          <span class="breadcrumb-scenario">{{ scenario.scenario_name }}</span>
        </template>
      </div>
      <div class="explorer-stats" v-if="graphData">
        {{ Object.keys(graphData.objects).length }} 对象 · {{ graphData.edges.length }} 关系
      </div>
    </div>

    <div class="explorer-body" v-if="graphData">
      <div class="explorer-left">
        <CascadeTree
          :graph="graphData"
          :selected-id="selectedId"
          :max-depth="6"
          @select="handleSelect"
          @navigate="handleNavigate"
        />
      </div>
      <div class="explorer-right">
        <ObjectDetail
          :obj="selectedObject"
          :graph="graphData"
          @navigate="handleNavigate"
        />
      </div>
    </div>
  </div>
  <div v-else-if="loading" class="explorer-loading">加载图数据中...</div>
  <div v-else class="explorer-loading">未找到数据</div>
</template>

<script setup lang="ts">
import { ref, onMounted, computed, watch } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { businessGraphApi, fetchJson } from '../api'
import CascadeTree from './CascadeTree.vue'
import ObjectDetail from './ObjectDetail.vue'

interface GraphObject {
  object_id: string
  object_type: string
  name: string
  summary: string
  layer: string
  attributes: Record<string, string>
}
interface GraphEdge { from: string; relation: string; to: string; meta?: Record<string, string> }
interface GraphData {
  objects: Record<string, GraphObject>
  edges: GraphEdge[]
  root_id: string
  error?: string
}

const route = useRoute()
const router = useRouter()

const isDomainMode = computed(() => route.name === 'business-domain')
const domainName = computed(() => decodeURIComponent(route.params.domainName as string || ''))
const scenarioId = computed(() => decodeURIComponent(route.params.scenarioId as string || ''))

const loading = ref(true)
const scenario = ref<any>(null)
const graphData = ref<GraphData | null>(null)
const selectedId = ref('')
const scenarioCount = ref(0)

const ready = computed(() => isDomainMode.value ? Boolean(graphData.value) : Boolean(scenario.value && graphData.value))

const selectedObject = computed(() => {
  if (!selectedId.value || !graphData.value) return null
  return graphData.value.objects[selectedId.value] || null
})

// --- Graph merging for domain mode ---
function mergeGraphs(graphs: GraphData[], rootName: string): GraphData {
  const objects: Record<string, GraphObject> = {}
  const edges: GraphEdge[] = []
  const nsIds: string[] = []

  for (const g of graphs) {
    if (!g || g.error) continue
    Object.assign(objects, g.objects)
    edges.push(...g.edges)
    for (const [id, obj] of Object.entries(g.objects)) {
      if (obj.object_type === 'NetworkScenario') nsIds.push(id)
    }
  }

  // Synthetic virtual BD root containing all NS nodes
  const rootId = `BD-DOMAIN-${rootName}`
  objects[rootId] = {
    object_id: rootId,
    object_type: 'BusinessDomain',
    name: rootName,
    summary: `${nsIds.length} 个子场景`,
    layer: 'business',
    attributes: { domain_name: rootName },
  }
  for (const nsId of nsIds) {
    edges.push({ from: rootId, relation: 'contains', to: nsId })
  }
  return { objects, edges, root_id: rootId }
}

async function loadDomain() {
  loading.value = true
  try {
    const domainData = await fetchJson(businessGraphApi.domain(domainName.value))
    if (domainData.error) {
      graphData.value = null
      return
    }
    scenarioCount.value = domainData.scenarios?.length || 0
    scenario.value = {
      domain_name: domainData.domain_name,
      scenario_name: `${domainData.scenarios?.length || 0} 个场景合并`,
    }

    // Fetch all scenario graphs in parallel
    const scenarioIds: string[] = (domainData.scenarios || []).map((s: any) => s.scenario_id)
    const graphs = await Promise.all(
      scenarioIds.map(id => fetchJson(businessGraphApi.graph(id)).catch(() => null))
    )

    graphData.value = mergeGraphs(graphs.filter(Boolean) as GraphData[], domainData.domain_name)
    if (graphData.value?.root_id) {
      selectedId.value = graphData.value.root_id
    }
  } catch (e) {
    console.error('Failed to load domain graph:', e)
  } finally {
    loading.value = false
  }
}

async function loadScenario() {
  loading.value = true
  try {
    const [scenData, graph] = await Promise.all([
      fetchJson(businessGraphApi.scenario(scenarioId.value)),
      fetchJson(businessGraphApi.graph(scenarioId.value)),
    ])
    scenario.value = scenData.error ? null : scenData
    graphData.value = graph.error ? null : graph

    if (graphData.value?.root_id) {
      selectedId.value = graphData.value.root_id
    }
  } catch (e) {
    console.error('Failed to load graph:', e)
  } finally {
    loading.value = false
  }
}

function load() {
  if (isDomainMode.value) {
    loadDomain()
  } else {
    loadScenario()
  }
}

function handleSelect(id: string) { selectedId.value = id }
function handleNavigate(id: string) { selectedId.value = id }
function goBack() { router.push('/business-graph') }

watch(() => [route.name, domainName.value, scenarioId.value], () => { load() })
onMounted(load)
</script>

<style scoped>
.explorer-root {
  display: flex;
  flex-direction: column;
  height: calc(100vh - var(--navbar-height));
  overflow: hidden;
}
.explorer-header {
  display: flex;
  align-items: center;
  gap: var(--space-4);
  padding: var(--space-3) var(--space-5);
  border-bottom: 1px solid var(--border);
  background: var(--bg-card);
  flex-shrink: 0;
}
.back-btn {
  background: var(--bg-card);
  border: 1px solid var(--border);
  color: var(--text-secondary);
  padding: var(--space-2) var(--space-3);
  border-radius: var(--radius);
  font-size: var(--text-xs);
  cursor: pointer;
  transition: all var(--duration) var(--ease);
  white-space: nowrap;
}
.back-btn:hover {
  border-color: var(--accent);
  color: var(--accent);
}
.explorer-breadcrumb {
  font-size: var(--text-sm);
  flex: 1;
  min-width: 0;
}
.breadcrumb-domain { color: var(--text-tertiary); }
.breadcrumb-sep { color: var(--text-tertiary); margin: 0 var(--space-1); }
.breadcrumb-scenario { color: var(--text-primary); font-weight: 600; }
.explorer-stats {
  font-size: var(--text-2xs);
  color: var(--text-tertiary);
  font-family: var(--font-mono);
  white-space: nowrap;
}
.explorer-body {
  display: flex;
  flex: 1;
  overflow: hidden;
}
.explorer-left {
  flex: 1;
  overflow-y: auto;
  padding: var(--space-4);
  min-width: 0;
}
.explorer-right {
  width: 520px;
  flex-shrink: 0;
  overflow-y: auto;
  border-left: 1px solid var(--border);
  padding: var(--space-4);
  background: var(--bg-card);
}
.explorer-loading {
  display: flex;
  align-items: center;
  justify-content: center;
  height: calc(100vh - var(--navbar-height));
  color: var(--text-tertiary);
  font-size: var(--text-sm);
}
</style>
