<template>
  <div v-loading="loading" class="cmd-graph-wrap">
    <div v-if="hasGraph" ref="containerRef" class="cmd-graph-canvas"></div>
    <div v-else-if="!loading" class="cmd-pane-empty">
      该命令无可绘制关系
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, watch, onMounted, onBeforeUnmount, nextTick } from 'vue'
import { commandGraphApi, fetchJson } from '../api'

interface Props {
  nf: string
  commandName: string
  version?: string
}
const props = defineProps<Props>()

const loading = ref(true)
const containerRef = ref<HTMLDivElement | null>(null)
const hasGraph = ref(false)

let networkInstance: any = null
let resizeObserver: ResizeObserver | null = null

// node.type → 渲染 group 配色（与 get_subgraph 返回的 type 对齐）
const GROUP_COLORS = {
  command: { background: '#0891b2', border: '#0e7490', font: { color: '#ffffff' } },
  config_object: { background: '#7c3aed', border: '#6d28d9', font: { color: '#ffffff' } },
  parameter: { background: '#ffffff', border: '#0891b2', font: { color: '#1a1d23' } },
  parameter_external: { background: '#f6f7f9', border: '#94a3b8', font: { color: '#94a3b8' } },
}
// command→object 关系（紫）；has_parameter/conditional_required/references 青；refers_to 紫虚线
const OBJECT_RELATIONS = new Set(['creates', 'modifies', 'deletes', 'sets', 'queries', 'operates_on'])

interface VisNode { id: string; type: string; label: string; properties?: Record<string, any> }
interface VisEdge { from: string; to: string; type: string; properties?: Record<string, any> }

function buildVisNodes(nodes: VisNode[], centerCommandId: string) {
  return nodes.map((n) => {
    let group = n.type === 'MMLCommand' ? 'command'
      : n.type === 'ConfigObject' ? 'config_object' : 'parameter'
    // parameter_external：参数所属命令 ≠ center（跨命令 references 来的外部参数），或悬空（无 command_id）
    if (group === 'parameter') {
      const cmdId = n.properties?.command_id
      if (!cmdId || cmdId !== centerCommandId) group = 'parameter_external'
    }
    const color = (GROUP_COLORS as any)[group] || GROUP_COLORS.parameter
    const isExternal = group === 'parameter_external'
    const isMajor = group === 'command' || group === 'config_object'
    return {
      id: n.id,
      label: n.label,
      title: n.label,
      group,
      shape: group === 'command' ? 'box' : group === 'config_object' ? 'diamond' : 'ellipse',
      color: {
        background: color.background,
        border: color.border,
        highlight: { background: color.background, border: color.border },
      },
      font: { ...color.font, size: isMajor ? 14 : 12, face: 'Inter', multi: false },
      borderWidth: isMajor ? 2 : 1,
      borderWidthSelected: 2,
      dashes: isExternal, // external 弱化虚边框
      margin: 8,
    }
  })
}

function buildVisEdges(edges: VisEdge[]) {
  return edges.map((e) => {
    const isCond = e.type === 'conditional_required'
    const isRef = e.type === 'references'
    const isObj = OBJECT_RELATIONS.has(e.type)
    const isRefersTo = e.type === 'refers_to'
    // 配色：条件/引用 青；对象边/refers 紫（refers 虚线）；has_parameter 淡灰
    const color = (isCond || isRef) ? '#0891b2' : (isObj || isRefersTo) ? '#7c3aed' : '#cbd5e1'
    const props = e.properties || {}
    const label = isCond ? `=${props.condition_value || ''}`
      : isRef ? '引用'
      : isObj ? e.type
      : isRefersTo ? 'refers'
      : undefined
    return {
      from: e.from,
      to: e.to,
      type: e.type,
      arrows: 'to' as const,
      color: { color, highlight: '#0891b2' },
      dashes: isRefersTo,
      label,
      title: label || e.type,
      font: {
        size: 10,
        color: '#4b5563',
        strokeWidth: 3,
        strokeColor: '#ffffff',
        face: 'JetBrains Mono',
        align: 'top' as const,
      },
      smooth: { enabled: true, type: 'cubicBezier', forceDirection: 'none', roundness: 0.5 },
    }
  })
}

async function renderGraph(nodes: VisNode[], edges: VisEdge[], centerCommandId: string) {
  if (!containerRef.value) return
  const vis = await import('vis-network/standalone')
  const Network = vis.Network
  const DataSet: any = vis.DataSet

  const visNodes = buildVisNodes(nodes, centerCommandId)
  const visEdges = buildVisEdges(edges)

  if (networkInstance) {
    networkInstance.destroy()
    networkInstance = null
  }

  networkInstance = new Network(
    containerRef.value,
    { nodes: new DataSet(visNodes), edges: new DataSet(visEdges) },
    {
      nodes: { borderWidth: 1, borderWidthSelected: 2 },
      edges: { smooth: { enabled: true, type: 'cubicBezier', forceDirection: 'none', roundness: 0.5 } },
      groups: {
        command: { shape: 'box', color: GROUP_COLORS.command },
        config_object: { shape: 'diamond', color: GROUP_COLORS.config_object },
        parameter: { shape: 'ellipse', color: GROUP_COLORS.parameter },
        parameter_external: { shape: 'ellipse', color: GROUP_COLORS.parameter_external, dashes: true },
      },
      layout: { improvedLayout: true },
      physics: {
        enabled: true,
        barnesHut: { gravitationalConstant: -3000, centralGravity: 0.3, springLength: 80, springConstant: 0.04, damping: 0.4 },
        stabilization: { iterations: 150, fit: true },
      },
      interaction: { dragNodes: true, dragView: true, zoomView: true, hover: true, tooltipDelay: 120, navigationButtons: false },
    }
  )

  if (resizeObserver) resizeObserver.disconnect()
  if (typeof ResizeObserver !== 'undefined' && containerRef.value) {
    resizeObserver = new ResizeObserver(() => {
      if (networkInstance) networkInstance.redraw()
    })
    resizeObserver.observe(containerRef.value)
  }
}

async function load() {
  loading.value = true
  try {
    const center = `${props.nf}@${props.version}@MMLCommand@${props.commandName}`
    const url = commandGraphApi.subgraph(center, 2, [
      'has_parameter', 'creates', 'modifies', 'sets', 'queries', 'operates_on',
      'conditional_required', 'references', 'refers_to',
    ])
    const data = await fetchJson(url)
    const nodes: VisNode[] = data.nodes || []
    const edges: VisEdge[] = data.edges || []
    hasGraph.value = nodes.length > 0
    if (hasGraph.value) {
      await nextTick()
      await renderGraph(nodes, edges, center)
    } else if (networkInstance) {
      networkInstance.destroy()
      networkInstance = null
    }
  } catch {
    hasGraph.value = false
    if (networkInstance) {
      networkInstance.destroy()
      networkInstance = null
    }
  } finally {
    loading.value = false
  }
}

watch(() => [props.nf, props.commandName, props.version], load)
onMounted(load)

onBeforeUnmount(() => {
  if (resizeObserver) {
    resizeObserver.disconnect()
    resizeObserver = null
  }
  if (networkInstance) {
    networkInstance.destroy()
    networkInstance = null
  }
})
</script>

<style scoped>
.cmd-graph-wrap {
  /* 必须有明确高度，否则 vis-network canvas 高度为 0 不显示 */
  height: calc(100vh - var(--navbar-height) - 120px);
  min-height: 360px;
  display: flex;
  flex-direction: column;
}
.cmd-graph-canvas {
  flex: 1;
  width: 100%;
  min-height: 360px;
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: var(--radius);
}

.cmd-pane-empty {
  padding: 80px 20px;
  text-align: center;
  color: var(--text-tertiary);
  font-size: var(--text-sm);
}
</style>
