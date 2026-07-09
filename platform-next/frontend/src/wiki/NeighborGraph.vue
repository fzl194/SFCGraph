<template>
  <div class="nb-graph-wrap">
    <div v-if="loading" v-loading="true" class="nb-graph-canvas"></div>
    <div v-else-if="!centerPath" class="nb-empty">选择对象后展示其周围关系</div>
    <div v-else-if="empty" class="nb-empty">该对象无关系</div>
    <div v-show="!loading && centerPath && !empty" ref="containerRef" class="nb-graph-canvas"></div>
    <div class="nb-legend">点节点跳转 · 灰虚=未构建</div>
  </div>
</template>

<script setup lang="ts">
import { ref, watch, onMounted, onBeforeUnmount, nextTick } from 'vue'
import { wikiApi, type NbNode, type NbEdge } from './wikiApi'

const props = defineProps<{ centerPath: string | null }>()
const emit = defineEmits<{ (e: 'navigate', path: string): void }>()

const loading = ref(false)
const empty = ref(false)
const containerRef = ref<HTMLDivElement | null>(null)
let network: any = null
let ro: ResizeObserver | null = null

const NODE_COLOR: Record<string, { bg: string; bd: string }> = {
  MMLCommand: { bg: '#0891b2', bd: '#0e7490' },
  ConfigObject: { bg: '#7c3aed', bd: '#6d28d9' },
  Feature: { bg: '#0d9488', bd: '#0f766e' },
  License: { bg: '#ea580c', bd: '#c2410c' },
  Task: { bg: '#db2777', bd: '#be185d' },
}
const EDGE_COLOR: Record<string, string> = {
  operates_on: '#7c3aed', operated_by: '#7c3aed', requires_license: '#ea580c',
  controls_feature: '#ea580c',
  parent: '#475569', child: '#475569', ref_command: '#db2777', has_task: '#db2777',
  evidenced_by: '#94a3b8', relates_to: '#64748b', related: '#cbd5e1',
}

async function load() {
  if (!props.centerPath) { empty.value = false; return }
  loading.value = true
  try {
    const nb = await wikiApi.neighborhood(props.centerPath)
    empty.value = nb.nodes.length <= 1
    await nextTick()
    await render(nb.nodes, nb.edges, props.centerPath)
  } catch {
    empty.value = true
    network?.destroy(); network = null
  } finally {
    loading.value = false
  }
}

async function render(nodes: NbNode[], edges: NbEdge[], centerPath: string) {
  if (!containerRef.value) return
  const vis: any = await import('vis-network/standalone')
  const Network = vis.Network
  const DataSet: any = vis.DataSet

  const visNodes = nodes.map((n) => {
    const c = NODE_COLOR[n.type] || { bg: '#64748b', bd: '#475569' }
    const isCenter = n.path === centerPath
    return {
      id: n.path || n.id,
      label: n.name,
      title: n.id || n.name,
      shape: n.resolved ? 'box' : 'ellipse',
      color: { background: c.bg, border: c.bd, highlight: { background: c.bg, border: c.bd } },
      font: { color: '#ffffff', size: isCenter ? 14 : 12 },
      borderWidth: isCenter ? 3 : 1,
      dashes: !n.resolved,
      _path: n.path,
    }
  })
  const visEdges = edges.map((e) => ({
    from: e.from,
    to: e.to,
    arrows: 'to' as const,
    color: { color: EDGE_COLOR[e.relation_type] || '#cbd5e1' },
    label: e.relation_type,
    font: { size: 10, color: '#4b5563', strokeWidth: 3, strokeColor: '#ffffff', align: 'top' as const },
    smooth: { enabled: true, type: 'cubicBezier', forceDirection: 'none', roundness: 0.5 },
  }))

  network?.destroy()
  network = new Network(
    containerRef.value,
    { nodes: new DataSet(visNodes), edges: new DataSet(visEdges) },
    {
      layout: { improvedLayout: true },
      physics: {
        enabled: true,
        barnesHut: { gravitationalConstant: -3000, centralGravity: 0.3, springLength: 80, springConstant: 0.04, damping: 0.4 },
        stabilization: { iterations: 120, fit: true },
      },
      interaction: { dragNodes: true, dragView: true, zoomView: true, hover: true, tooltipDelay: 120 },
    },
  )
  network.on('click', (params: any) => {
    const nodeId = params.nodes?.[0]
    if (nodeId == null) return
    const node = visNodes.find((n) => n.id === nodeId)
    if (node && node._path) emit('navigate', node._path)
  })

  ro?.disconnect()
  if (typeof ResizeObserver !== 'undefined' && containerRef.value) {
    ro = new ResizeObserver(() => network?.redraw())
    ro.observe(containerRef.value)
  }
}

watch(() => props.centerPath, load)
onMounted(() => { if (props.centerPath) load() })
onBeforeUnmount(() => {
  ro?.disconnect(); ro = null
  network?.destroy(); network = null
})
</script>

<style scoped>
.nb-graph-wrap { height: 100%; display: flex; flex-direction: column; }
.nb-graph-canvas { flex: 1; min-height: 300px; background: var(--bg-card); border: 1px solid var(--border); border-radius: var(--radius); }
.nb-empty { color: var(--text-tertiary); padding: 60px 12px; text-align: center; font-size: 13px; }
.nb-legend { font-size: 11px; color: var(--text-tertiary); padding: 4px; }
</style>
