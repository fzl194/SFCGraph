<template>
  <div v-loading="loading" class="cmd-graph-wrap">
    <div v-if="hasGraph" ref="containerRef" class="cmd-graph-canvas"></div>
    <div v-else-if="!loading" class="cmd-pane-empty">
      该命令无参数，无可绘制关系
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

// 节点 group 配色（项目色系：command 突出/parameter 常规/external 弱化虚线）
const GROUP_COLORS = {
  command: { background: '#0891b2', border: '#0e7490', font: { color: '#ffffff' } },
  parameter: { background: '#ffffff', border: '#0891b2', font: { color: '#1a1d23' } },
  parameter_external: { background: '#f6f7f9', border: '#94a3b8', font: { color: '#94a3b8' } },
}

interface VisNode {
  id: string
  label: string
  group: string
  title?: string
}
interface VisEdge {
  from: string
  to: string
  type: string
  label?: string
  title?: string
}

function buildVisNodes(nodes: VisNode[]) {
  return nodes.map((n) => {
    const color = (GROUP_COLORS as any)[n.group] || GROUP_COLORS.parameter
    const isExternal = n.group === 'parameter_external'
    return {
      id: n.id,
      label: n.label,
      title: n.title || n.label,
      group: n.group,
      shape: n.group === 'command' ? 'box' : 'ellipse',
      color: {
        background: color.background,
        border: color.border,
        highlight: { background: color.background, border: color.border },
      },
      font: { ...color.font, size: n.group === 'command' ? 14 : 12, face: 'Inter', multi: false },
      borderWidth: n.group === 'command' ? 2 : 1,
      borderWidthSelected: 2,
      dashes: isExternal, // external 弱化为虚边框
      margin: 8,
    }
  })
}

function buildVisEdges(edges: VisEdge[]) {
  return edges.map((e) => {
    const isDepends = e.type === 'depends_on'
    return {
      from: e.from,
      to: e.to,
      type: e.type,
      arrows: 'to' as const,
      // depends_on 用实线 + 条件 label；has_parameter 用淡实线无 label
      color: { color: isDepends ? '#0891b2' : '#cbd5e1', highlight: '#0891b2' },
      dashes: false,
      label: isDepends ? e.label : undefined,
      title: e.title || (isDepends ? '依赖' : '包含参数'),
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

async function renderGraph(nodes: VisNode[], edges: VisEdge[]) {
  if (!containerRef.value) return
  const vis = await import('vis-network/standalone')
  const Network = vis.Network
  const DataSet: any = vis.DataSet

  const visNodes = buildVisNodes(nodes)
  const visEdges = buildVisEdges(edges)

  // 销毁旧实例防泄漏
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

  // 容器尺寸变化（拖拽分隔条 / 折叠栏）时重绘 canvas，避免错位
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
    const data = await fetchJson(commandGraphApi.commandGraph(props.nf, props.commandName, props.version))
    const nodes: VisNode[] = data.nodes || []
    const edges: VisEdge[] = data.edges || []
    // 有节点且至少有命令节点才认为有可绘制内容
    hasGraph.value = nodes.length > 0
    if (hasGraph.value) {
      await nextTick()
      await renderGraph(nodes, edges)
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
