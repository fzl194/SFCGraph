<template>
  <div class="nb-wrap">
    <div class="nb-head">
      <span class="nb-head-title">周围关系 · 1 跳</span>
      <span v-if="centerPath && !empty && !loading" class="nb-head-count">{{ nodeCount }} 节点</span>
    </div>

    <div class="nb-body">
      <div v-if="loading" v-loading="true" class="nb-canvas"></div>
      <div v-else-if="!centerPath" class="nb-state">
        <div class="nb-state-icon">◌</div>
        <div class="nb-state-text">选择对象后展示其周围关系</div>
      </div>
      <div v-else-if="empty" class="nb-state">
        <div class="nb-state-icon">◌</div>
        <div class="nb-state-text">该对象无关系</div>
      </div>
      <div v-show="!loading && centerPath && !empty" ref="containerRef" class="nb-canvas"></div>
      <div v-if="centerPath && !empty && !loading" class="nb-hint">点节点跳转 · 灰虚＝未构建</div>
    </div>

    <div class="nb-foot">
      <span v-for="t in legendTypes" :key="t" class="nb-leg">
        <span class="nb-leg-dot" :style="{ background: TYPE_META[t].bg }"></span>{{ TYPE_META[t].label }}
      </span>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, watch, onMounted, onBeforeUnmount, nextTick } from 'vue'
import { wikiApi, type NbNode, type NbEdge } from './wikiApi'
import { TYPE_META } from './wikiTokens'

const props = defineProps<{ centerPath: string | null }>()
const emit = defineEmits<{ (e: 'navigate', path: string): void }>()

const loading = ref(false)
const empty = ref(false)
const nodeCount = ref(0)
const containerRef = ref<HTMLDivElement | null>(null)
let network: any = null
let ro: ResizeObserver | null = null

const legendTypes = ['MMLCommand', 'ConfigObject', 'Feature', 'License', 'Task']

// 关系边配色（与类型色呼应：对象关系=紫、License=琥珀、命令/任务=品红、其余中性）
const EDGE_COLOR: Record<string, string> = {
  operates_on: '#4f46e5', operated_by: '#4f46e5', requires_license: '#d97706',
  controls_feature: '#d97706',
  parent: '#475569', child: '#475569', ref_command: '#e11d48', has_task: '#e11d48',
  evidenced_by: '#94a3b8', relates_to: '#64748b', related: '#cbd5e1',
}

async function load() {
  if (!props.centerPath) { empty.value = false; nodeCount.value = 0; return }
  loading.value = true
  let nb: { nodes: NbNode[]; edges: NbEdge[] } | null = null
  try {
    nb = await wikiApi.neighborhood(props.centerPath)
  } catch {
    empty.value = true; nodeCount.value = 0; loading.value = false
    network?.destroy(); network = null
    return
  }
  nodeCount.value = nb.nodes.length
  empty.value = nb.nodes.length <= 1
  loading.value = false            // 先显出画布，再渲染（避免 display:none 下 vis 量到 0 尺寸）
  if (empty.value) { network?.destroy(); network = null; return }
  await nextTick()
  await render(nb.nodes, nb.edges, props.centerPath)
}

async function render(nodes: NbNode[], edges: NbEdge[], centerPath: string) {
  if (!containerRef.value) return
  const vis: any = await import('vis-network/standalone')
  const Network = vis.Network
  const DataSet: any = vis.DataSet

  const visNodes = nodes.map((n) => {
    const c = TYPE_META[n.type] || { bg: '#64748b', bd: '#475569' }
    const isCenter = n.path === centerPath
    return {
      id: n.path || n.id,
      label: n.name,
      title: n.id || n.name,
      shape: n.resolved ? 'box' : 'ellipse',
      color: { background: c.bg, border: c.bd, highlight: { background: c.bg, border: c.bd } },
      font: { color: '#ffffff', size: isCenter ? 14 : 12, face: 'Inter' },
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
    font: { size: 10, color: '#4b5563', strokeWidth: 3, strokeColor: '#ffffff', align: 'top' as const, face: 'JetBrains Mono' },
    smooth: { enabled: true, type: 'cubicBezier', forceDirection: 'none', roundness: 0.5 },
  }))

  network?.destroy()
  network = new Network(
    containerRef.value,
    { nodes: new DataSet(visNodes), edges: new DataSet(visEdges) },
    {
      nodes: { borderWidth: 1, borderWidthSelected: 2 },
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
.nb-wrap { height: 100%; display: flex; flex-direction: column; }

.nb-head {
  display: flex; align-items: center; justify-content: space-between;
  padding: var(--space-3) var(--space-4);
  background: var(--bg-page);
  border-bottom: 1px solid var(--border);
  flex-shrink: 0;
}
.nb-head-title {
  font-size: var(--text-2xs); font-weight: 700; color: var(--text-tertiary);
  text-transform: uppercase; letter-spacing: 0.08em;
}
.nb-head-count {
  font-size: var(--text-2xs); color: var(--text-secondary); font-family: var(--font-mono);
  background: var(--bg-card); border: 1px solid var(--border);
  padding: 1px 8px; border-radius: var(--radius-sm);
}

.nb-body { flex: 1; position: relative; padding: var(--space-3); min-height: 0; }
.nb-canvas {
  width: 100%; height: 100%; min-height: 300px;
  background-color: var(--bg-card);
  background-image: radial-gradient(rgba(8, 145, 178, 0.08) 1px, transparent 1px);
  background-size: 18px 18px;
  border: 1px solid var(--border);
  border-radius: var(--radius);
}
.nb-state {
  height: 100%; min-height: 300px;
  display: flex; flex-direction: column; align-items: center; justify-content: center;
  gap: var(--space-2); color: var(--text-tertiary);
}
.nb-state-icon { font-size: 40px; color: var(--border); line-height: 1; }
.nb-state-text { font-size: var(--text-sm); }
.nb-hint {
  position: absolute; bottom: calc(var(--space-3) + 10px); left: calc(var(--space-3) + 10px);
  font-size: var(--text-2xs); color: var(--text-tertiary);
  background: rgba(255, 255, 255, 0.85);
  padding: 4px 10px; border-radius: var(--radius-sm);
  backdrop-filter: blur(4px); border: 1px solid var(--border-light);
}

/* type-color legend — decodes the graph palette */
.nb-foot {
  display: flex; flex-wrap: wrap; gap: var(--space-3);
  padding: var(--space-2) var(--space-4);
  border-top: 1px solid var(--border);
  background: var(--bg-card);
  flex-shrink: 0;
}
.nb-leg { display: inline-flex; align-items: center; gap: 4px; font-size: var(--text-2xs); color: var(--text-secondary); }
.nb-leg-dot { width: 8px; height: 8px; border-radius: 2px; display: inline-block; }
</style>
