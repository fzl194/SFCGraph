<template>
  <div class="explorer-root" v-if="!loading && scenario">
    <div class="explorer-header">
      <button class="back-btn" @click="goBack">← 返回</button>
      <div class="explorer-breadcrumb">
        <span class="breadcrumb-domain">{{ scenario.domain_name }}</span>
        <span class="breadcrumb-sep">/</span>
        <span class="breadcrumb-scenario">{{ scenario.scenario_name }}</span>
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
          :max-depth="4"
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
  <div v-else class="explorer-loading">未找到场景</div>
</template>

<script setup lang="ts">
import { ref, onMounted, computed, watch } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { businessGraphApi, fetchJson } from '../api'
import CascadeTree from './CascadeTree.vue'
import ObjectDetail from './ObjectDetail.vue'

const route = useRoute()
const router = useRouter()
const scenarioId = computed(() => decodeURIComponent(route.params.scenarioId as string))

const loading = ref(true)
const scenario = ref<any>(null)
const graphData = ref<any>(null)
const selectedId = ref('')

const selectedObject = computed(() => {
  if (!selectedId.value || !graphData.value) return null
  return graphData.value.objects[selectedId.value] || null
})

async function loadGraph() {
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

function handleSelect(id: string) {
  selectedId.value = id
}

function handleNavigate(id: string) {
  selectedId.value = id
}

function goBack() {
  router.push('/business-graph')
}

watch(scenarioId, () => {
  loadGraph()
})

onMounted(loadGraph)
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
.breadcrumb-domain {
  color: var(--text-tertiary);
}
.breadcrumb-sep {
  color: var(--text-tertiary);
  margin: 0 var(--space-1);
}
.breadcrumb-scenario {
  color: var(--text-primary);
  font-weight: 600;
}
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
  width: 420px;
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
