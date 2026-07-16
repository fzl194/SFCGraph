<template>
  <div ref="hostRef" class="graph-canvas"></div>
</template>

<script setup lang="ts">
import { onBeforeUnmount, onMounted, ref, watch } from 'vue'
import { DataSet } from 'vis-data/peer/esm/vis-data'
import { Network, type Options } from 'vis-network/peer/esm/vis-network'
import type { Edge } from '../api'

interface FocusPayload {
  centerId: string
  centerDetail: {
    id: string
    type?: string
    frontmatter?: Record<string, unknown>
  } | null
  out: Edge[]
  in: Edge[]
  version?: string
}

const props = defineProps<{ focus: FocusPayload | null }>()
const emit = defineEmits<{
  (e: 'nodeClick', id: string): void
}>()

const hostRef = ref<HTMLDivElement | null>(null)
let network: Network | null = null
const nodes = new DataSet<{ id: string; label: string; group: string; title?: string }>([])
const edges = new DataSet<{ id: string; from: string; to: string; label?: string }>([])

// 待渲染的 focus（在 network 初始化前到达时暂存）
let pending: FocusPayload | null = null

function buildOptions(): Options {
  return {
    nodes: {
      shape: 'dot',
      size: 14,
      font: {
        size: 13,
        color: '#1c1917',
        face: 'JetBrains Mono, monospace',
      },
      borderWidth: 1.5,
      shadow: { enabled: true, size: 6, x: 0, y: 2, color: 'rgba(28,25,23,0.08)' },
    },
    edges: {
      width: 1.2,
      color: { color: '#d6d3d1', highlight: '#4f46e5', hover: '#a8a29e' },
      arrows: { to: { enabled: true, scaleFactor: 0.6 } },
      font: {
        size: 10,
        color: '#a8a29e',
        strokeWidth: 3,
        strokeColor: '#fafaf9',
        face: 'Inter, sans-serif',
      },
      smooth: { enabled: true, type: 'continuous', roundness: 0.4 },
    },
    groups: {
      center: {
        color: {
          background: '#4f46e5',
          border: '#4338ca',
          highlight: { background: '#4338ca', border: '#4338ca' },
        },
        font: { color: '#ffffff' },
        size: 20,
        borderWidth: 2,
      },
      related: {
        color: {
          background: '#eef2ff',
          border: '#4f46e5',
          highlight: { background: '#c7d2fe', border: '#4f46e5' },
        },
      },
    },
    physics: {
      stabilization: { iterations: 120 },
      barnesHut: {
        gravitationalConstant: -8000,
        springLength: 140,
        springConstant: 0.04,
        damping: 0.4,
      },
    },
    interaction: {
      hover: true,
      tooltipDelay: 120,
      navigationButtons: false,
      keyboard: false,
    },
  }
}

function ensureNetwork(): void {
  if (network || !hostRef.value) return
  network = new Network(hostRef.value, { nodes, edges }, buildOptions())
  network.on('click', (params: { nodes?: string[] }) => {
    const id = params.nodes?.[0]
    if (id) emit('nodeClick', id)
  })
  if (pending) {
    const p = pending
    pending = null
    render(p)
  }
}

function render(payload: FocusPayload): void {
  if (!network) {
    pending = payload
    return
  }
  nodes.clear()
  edges.clear()

  const centerId = payload.centerId
  nodes.add({
    id: centerId,
    label: shortLabel(centerId),
    group: 'center',
    title: centerId,
  })

  const seen = new Set<string>([centerId])
  const edgeList: { id: string; from: string; to: string; label?: string }[] = []

  for (const e of payload.out) {
    if (!seen.has(e.to)) {
      seen.add(e.to)
      nodes.add({ id: e.to, label: shortLabel(e.to), group: 'related', title: e.to })
    }
    edgeList.push({
      id: 'o::' + e.from + '->' + e.to + '::' + e.relation,
      from: e.from,
      to: e.to,
      label: e.relation,
    })
  }
  for (const e of payload.in) {
    if (!seen.has(e.from)) {
      seen.add(e.from)
      nodes.add({ id: e.from, label: shortLabel(e.from), group: 'related', title: e.from })
    }
    edgeList.push({
      id: 'i::' + e.from + '->' + e.to + '::' + e.relation,
      from: e.from,
      to: e.to,
      label: e.relation,
    })
  }

  edges.add(edgeList)
  network.setData({ nodes, edges })

  network.once('stabilizationIterationsDone', () => {
    network?.focus(centerId, {
      scale: 1,
      animation: { duration: 400, easingFunction: 'easeInOutQuad' },
    })
  })
}

function shortLabel(id: string): string {
  const parts = id.split('@')
  return parts.length > 1 ? parts[parts.length - 1] : id
}

watch(
  () => props.focus,
  (p) => {
    if (p) render(p)
  },
)

onMounted(() => {
  ensureNetwork()
  window.addEventListener('resize', onResize)
})

function onResize(): void {
  network?.redraw()
}

onBeforeUnmount(() => {
  window.removeEventListener('resize', onResize)
  network?.destroy()
  network = null
})
</script>

<style scoped>
.graph-canvas {
  width: 100%;
  height: 100%;
  background:
    radial-gradient(circle at 1px 1px, rgba(28, 25, 23, 0.04) 1px, transparent 0)
    var(--bg-elev);
  background-size: 22px 22px;
}
</style>
