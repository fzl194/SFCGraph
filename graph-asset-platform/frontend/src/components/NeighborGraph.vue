<template>
  <div class="neighbor-graph">
    <div class="header">
      <span class="title">节点关系（单跳）</span>
      <span v-if="!id" class="muted">未选中对象</span>
    </div>

    <div v-if="loading" class="status muted">加载中…</div>
    <div v-else-if="error" class="status error">{{ error }}</div>

    <template v-else-if="id && data">
      <div ref="canvasRef" class="canvas"></div>

      <div class="neighbor-list">
        <div class="list-title">
          邻居清单
          <span class="muted">（{{ totalCount }} 条）</span>
        </div>
        <el-scrollbar class="list-scroll">
          <div v-if="!totalCount" class="empty muted">无关系</div>
          <div
            v-for="(item, idx) in neighborItems"
            :key="idx"
            class="nb-row"
            :class="{ clickable: true }"
            @click="onNeighborClick(item.target)"
          >
            <span class="dir" :class="item.dir">[{{ item.dir === 'out' ? '出' : '入' }}]</span>
            <span class="rel">{{ item.relation }}</span>
            <span class="sep">→</span>
            <span class="target" :title="item.target">{{ item.target }}</span>
          </div>
        </el-scrollbar>
      </div>
    </template>
  </div>
</template>

<script setup lang="ts">
import { ref, watch, onMounted, onBeforeUnmount, nextTick } from 'vue'
import { Network, type Options as NetworkOptions } from 'vis-network'
import { neighbors as fetchNeighbors, type Neighbors } from '../api'

const props = defineProps<{
  id?: string
  version?: string
}>()

const emit = defineEmits<{
  (e: 'select', id: string): void
}>()

const canvasRef = ref<HTMLElement | null>(null)
const data = ref<Neighbors | null>(null)
const loading = ref(false)
const error = ref('')
let network: Network | null = null

interface NbItem {
  dir: 'out' | 'in'
  relation: string
  target: string
}

const neighborItems = ref<NbItem[]>([])
const totalCount = ref(0)

async function load() {
  if (!props.id) {
    data.value = null
    neighborItems.value = []
    totalCount.value = 0
    return
  }
  loading.value = true
  error.value = ''
  try {
    const res = await fetchNeighbors(props.id, props.version, 1)
    data.value = res
    // 合并 out + in 方向（入边：from→center；展示 target=from）
    const items: NbItem[] = []
    for (const e of res.out) items.push({ dir: 'out', relation: e.relation, target: e.to })
    for (const e of res.in) items.push({ dir: 'in', relation: e.relation, target: e.from })
    neighborItems.value = items
    totalCount.value = items.length
    await nextTick()
    renderGraph(res)
  } catch (e) {
    error.value = e instanceof Error ? e.message : String(e)
    data.value = null
    neighborItems.value = []
    totalCount.value = 0
  } finally {
    loading.value = false
  }
}

function renderGraph(res: Neighbors) {
  if (!canvasRef.value) return
  // 销毁旧实例
  if (network) {
    network.destroy()
    network = null
  }

  const centerId = res.center.id
  // 节点：中心 + 邻居（去重）
  const nodeSet = new Map<string, { id: string; label: string; isCenter: boolean }>()
  nodeSet.set(centerId, { id: centerId, label: shortLabel(centerId), isCenter: true })
  const edgeList: { from: string; to: string; label: string; id: string }[] = []

  for (const e of res.out) {
    if (!nodeSet.has(e.to)) {
      nodeSet.set(e.to, { id: e.to, label: shortLabel(e.to), isCenter: false })
    }
    edgeList.push({ from: centerId, to: e.to, label: e.relation, id: `o:${centerId}->${e.to}:${e.relation}` })
  }
  for (const e of res.in) {
    if (!nodeSet.has(e.from)) {
      nodeSet.set(e.from, { id: e.from, label: shortLabel(e.from), isCenter: false })
    }
    edgeList.push({ from: e.from, to: centerId, label: e.relation, id: `i:${e.from}->${centerId}:${e.relation}` })
  }

  // vis-network 的 Node/Edge 类型对联合字段（margin/smooth）要求严格；
  // 数据形状由我们构造，直接用 any 适配 vis 的 DataSet 接口。
  const nodes: any[] = [...nodeSet.values()].map((n) => ({
    id: n.id,
    label: n.label,
    color: n.isCenter ? { background: '#409eff', border: '#337ecc' } : { background: '#e8f4ff', border: '#a0cfff' },
    font: { color: n.isCenter ? '#fff' : '#303133', size: n.isCenter ? 16 : 13 },
    shape: n.isCenter ? 'box' : 'ellipse',
    margin: 6,
  }))

  const edges: any[] = edgeList.map((e) => ({
    from: e.from,
    to: e.to,
    label: e.label,
    arrows: 'to',
    font: { size: 10, color: '#909399' },
    smooth: { enabled: true, type: 'cubicBezier', roundness: 0.5 },
  }))

  const options: NetworkOptions = {
    layout: { improvedLayout: true },
    physics: {
      stabilization: { iterations: 80 },
      barnesHut: { gravitationalConstant: -8000, springLength: 120 },
    },
    interaction: { hover: true, zoomView: true },
  }

  network = new Network(
    canvasRef.value,
    { nodes, edges },
    options,
  )

  network.on('doubleClick', (params) => {
    if (params.nodes && params.nodes.length > 0) {
      const clicked = params.nodes[0] as string
      if (clicked !== centerId) {
        emit('select', clicked)
      }
    }
  })
}

function shortLabel(id: string): string {
  const at = id.indexOf('@')
  const slug = at >= 0 ? id.slice(at + 1) : id
  // 过长截断
  return slug.length > 24 ? slug.slice(0, 24) + '…' : slug
}

function onNeighborClick(target: string) {
  emit('select', target)
}

watch(
  () => [props.id, props.version],
  () => load(),
  { immediate: false },
)

onMounted(() => {
  if (props.id) load()
})

onBeforeUnmount(() => {
  if (network) {
    network.destroy()
    network = null
  }
})
</script>

<style scoped>
.neighbor-graph {
  display: flex;
  flex-direction: column;
  height: 100%;
  background: #fff;
}
.header {
  padding: 8px 12px;
  border-bottom: 1px solid #ebeef5;
  display: flex;
  align-items: center;
  gap: 8px;
}
.title {
  font-weight: 600;
  font-size: 13px;
}
.muted {
  color: #909399;
  font-size: 12px;
}
.status {
  padding: 24px;
  text-align: center;
  font-size: 13px;
}
.error {
  color: #f56c6c;
}
.canvas {
  flex: 1 1 60%;
  min-height: 200px;
  border-bottom: 1px solid #ebeef5;
}
.neighbor-list {
  flex: 0 0 auto;
  display: flex;
  flex-direction: column;
  max-height: 45%;
}
.list-title {
  padding: 6px 12px;
  font-size: 12px;
  font-weight: 600;
  color: #606266;
  background: #fafafa;
  border-bottom: 1px solid #ebeef5;
}
.list-scroll {
  flex: 1;
  min-height: 0;
}
.empty {
  padding: 12px;
  text-align: center;
  font-size: 12px;
}
.nb-row {
  display: flex;
  align-items: center;
  gap: 6px;
  padding: 5px 12px;
  font-size: 12px;
  border-bottom: 1px solid #f5f7fa;
  cursor: pointer;
}
.nb-row:hover {
  background: #f0f7ff;
}
.dir {
  font-weight: 600;
  flex-shrink: 0;
}
.dir.out {
  color: #409eff;
}
.dir.in {
  color: #e6a23c;
}
.rel {
  color: #606266;
  flex-shrink: 0;
}
.sep {
  color: #c0c4cc;
  flex-shrink: 0;
}
.target {
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
  color: #303133;
}
</style>
