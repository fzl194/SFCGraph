<template>
  <div v-if="feature" class="detail-layout">
    <!-- Sidebar -->
    <div class="detail-sidebar">
      <div class="detail-sidebar-header">
        <button class="back-btn" @click="$router.push(productType ? { path: '/feature', query: { product: productType } } : '/feature')">← 返回列表</button>
        <div class="sidebar-id">{{ feature.feature_id }}</div>
        <div class="sidebar-name">{{ feature.feature_name }}</div>
      </div>

      <div class="sidebar-meta">
        <div class="sidebar-meta-row">
          <span class="sidebar-meta-label">产品</span>
          <span class="sidebar-meta-value">{{ feature.product_type }}</span>
        </div>
        <div class="sidebar-meta-row">
          <span class="sidebar-meta-label">类型</span>
          <el-tag size="small" effect="plain">{{ feature.feature_type || '-' }}</el-tag>
        </div>
        <div class="sidebar-meta-row">
          <span class="sidebar-meta-label">分组</span>
          <span class="sidebar-meta-value">{{ feature.section || '-' }}</span>
        </div>
        <div class="sidebar-meta-row">
          <span class="sidebar-meta-label">需配置</span>
          <el-tag :type="feature.config_required === 'true' ? 'success' : 'info'" size="small">
            {{ feature.config_required === 'true' ? '是' : '否' }}
          </el-tag>
        </div>
        <div v-if="feature.applicable_nf" class="sidebar-meta-row">
          <span class="sidebar-meta-label">网元</span>
          <span class="sidebar-meta-value">{{ feature.applicable_nf }}</span>
        </div>
      </div>

      <div class="doc-section" v-for="group in docGroups" :key="group.type">
        <div class="doc-section-title">{{ group.label }} ({{ group.docs.length }})</div>
        <button
          v-for="doc in group.docs"
          :key="doc.id"
          class="doc-item"
          :class="{ active: activeDoc?.id === doc.id }"
          @click="selectDoc(doc)"
        >
          {{ doc.doc_title }}
        </button>
      </div>
    </div>

    <!-- Content: centered with balanced padding -->
    <div class="detail-content">
      <div class="detail-content-inner">
        <el-tabs v-model="activeTab">
          <el-tab-pane label="概要" name="summary">
            <!-- Hero header -->
            <div class="summary-hero">
              <div class="summary-hero-id">{{ feature.feature_id }}</div>
              <h1 class="summary-hero-name">{{ feature.feature_name }}</h1>
              <div class="summary-hero-tags">
                <el-tag :type="feature.config_required === 'true' ? 'success' : 'info'" size="small">
                  {{ feature.config_required === 'true' ? '需配置' : '免配置' }}
                </el-tag>
                <el-tag v-if="feature.feature_type" size="small" effect="plain">{{ feature.feature_type }}</el-tag>
                <el-tag v-if="feature.product_type" size="small" effect="plain" class="summary-product-tag">{{ feature.product_type }}</el-tag>
                <el-tag v-if="feature.applicable_nf" size="small" effect="plain" type="info">{{ feature.applicable_nf }}</el-tag>
              </div>
            </div>

            <!-- Definition block -->
            <div v-if="feature.definition" class="summary-def">
              <div class="summary-def-label">定义</div>
              <p class="summary-def-text">{{ feature.definition }}</p>
            </div>

            <!-- Key attributes -->
            <div class="summary-section" v-if="summaryKeyFields.length">
              <div class="summary-section-title">关键属性</div>
              <dl class="summary-dl">
                <div v-for="f in summaryKeyFields" :key="f.key" class="summary-dl-row">
                  <dt>{{ f.label }}</dt>
                  <dd>{{ feature[f.key] || '—' }}</dd>
                </div>
              </dl>
            </div>

            <!-- Extended attributes -->
            <div class="summary-section" v-if="summaryExtraFields.length">
              <div class="summary-section-title">扩展信息</div>
              <dl class="summary-dl">
                <div v-for="f in summaryExtraFields" :key="f.key" class="summary-dl-row">
                  <dt>{{ f.label }}</dt>
                  <dd>{{ feature[f.key] || '—' }}</dd>
                </div>
              </dl>
            </div>
          </el-tab-pane>

          <el-tab-pane label="文档" name="doc">
            <div v-if="activeDoc">
              <div style="margin-bottom: 16px; padding: 10px 14px; background: var(--accent-soft); border-radius: var(--radius); border-left: 3px solid var(--accent)">
                <span style="font-size: var(--text-sm); font-weight: 500; color: var(--accent)">{{ activeDoc.doc_title }}</span>
                <span style="font-size: var(--text-xs); color: var(--text-tertiary); margin-left: 8px">{{ activeDoc.doc_type }}</span>
              </div>
              <DocViewer v-if="docContent" :content="docContent" :file-path="activeDoc.file_path" @open-ref="openRefDoc" />
              <div v-else style="padding: 40px; text-align: center; color: var(--text-tertiary)">加载中...</div>
            </div>
            <div v-else style="padding: 60px; text-align: center; color: var(--text-tertiary); font-size: var(--text-sm)">
              从左侧选择文档查看内容
            </div>
          </el-tab-pane>

          <el-tab-pane name="deps">
            <template #label>
              依赖关系 <span style="font-size: var(--text-xs); color: var(--text-tertiary)">( {{ deps.length }} )</span>
            </template>
            <!-- Graph with expandable neighbors -->
            <div style="margin-bottom: var(--space-4); position: relative">
              <div class="graph-container" ref="miniGraphRef"></div>
              <div v-if="graphExpandedNodes.size > 1" class="graph-info">
                已展开 {{ graphExpandedNodes.size }} 个节点 · 点击节点继续扩展
              </div>
            </div>
            <!-- Dep table -->
            <el-table :data="enrichedDeps" stripe size="small" style="width: 100%">
              <el-table-column prop="source_feature_id" label="源" width="140">
                <template #default="{ row }">
                  <router-link
                    v-if="row.source_feature_id !== featureId"
                    :to="{ name: 'feature-detail', params: { id: row.source_feature_id }, query: productType ? { product: productType } : undefined }"
                    class="feature-id-cell"
                  >{{ row.source_feature_id }}</router-link>
                  <span v-else class="feature-id-cell" style="color: var(--text-primary)">{{ row.source_feature_id }}</span>
                </template>
              </el-table-column>
              <el-table-column prop="target_feature_id" label="目标" width="140">
                <template #default="{ row }">
                  <router-link
                    v-if="row.target_feature_id !== featureId"
                    :to="{ name: 'feature-detail', params: { id: row.target_feature_id }, query: productType ? { product: productType } : undefined }"
                    class="feature-id-cell"
                  >{{ row.target_feature_id }}</router-link>
                  <span v-else class="feature-id-cell" style="color: var(--text-primary)">{{ row.target_feature_id }}</span>
                </template>
              </el-table-column>
              <el-table-column prop="dependency_type" label="类型" width="120">
                <template #default="{ row }">
                  <el-tag :type="depTagType(row.dependency_type)" size="small">{{ row.dependency_type }}</el-tag>
                </template>
              </el-table-column>
              <el-table-column prop="description" label="描述" min-width="200">
                <template #default="{ row }">
                  <span style="color: var(--text-secondary); font-size: var(--text-xs)">{{ cleanHtml(row.description) }}</span>
                </template>
              </el-table-column>
              <el-table-column label="状态" width="90">
                <template #default="{ row }">
                  <el-tag :type="reviewTagType(row._reviewStatus)" size="small" effect="plain">{{ reviewLabel(row._reviewStatus) }}</el-tag>
                </template>
              </el-table-column>
              <el-table-column label="操作" width="130">
                <template #default="{ row }">
                  <el-button size="small" type="primary" link :disabled="row._reviewStatus === 'accepted'" @click="doDepReview('accept', row)">接受</el-button>
                  <el-button size="small" type="danger" link :disabled="row._reviewStatus === 'rejected'" @click="doDepReview('reject', row)">拒绝</el-button>
                </template>
              </el-table-column>
            </el-table>
          </el-tab-pane>

          <el-tab-pane name="license">
            <template #label>
              License <span style="font-size: var(--text-xs); color: var(--text-tertiary)">( {{ licenses.length }} )</span>
            </template>
            <el-table :data="enrichedLicenses" stripe size="small">
              <el-table-column prop="license_number" label="编号" width="140" />
              <el-table-column prop="license_code" label="Code" width="180" />
              <el-table-column prop="license_name" label="名称" min-width="200" />
              <el-table-column label="状态" width="90">
                <template #default="{ row }">
                  <el-tag :type="reviewTagType(row._reviewStatus)" size="small" effect="plain">{{ reviewLabel(row._reviewStatus) }}</el-tag>
                </template>
              </el-table-column>
              <el-table-column label="操作" width="130">
                <template #default="{ row }">
                  <el-button size="small" type="primary" link :disabled="row._reviewStatus === 'accepted'" @click="doLicReview('accept', row)">接受</el-button>
                  <el-button size="small" type="danger" link :disabled="row._reviewStatus === 'rejected'" @click="doLicReview('reject', row)">拒绝</el-button>
                </template>
              </el-table-column>
            </el-table>
          </el-tab-pane>
        </el-tabs>
      </div>

      <!-- Sidebar panel for MD cross-references -->
      <Transition name="ref-slide">
        <div v-if="refSidebar.show" class="ref-sidebar">
          <div class="ref-sidebar-header">
            <span class="ref-sidebar-title">{{ refSidebar.title }}</span>
            <button class="ref-sidebar-close" @click="refSidebar.show = false">✕</button>
          </div>
          <div class="ref-sidebar-body">
            <div v-if="refSidebar.loading" style="padding: 40px; text-align: center; color: var(--text-tertiary)">加载中...</div>
            <DocViewer
              v-else-if="refSidebar.content"
              :content="refSidebar.content"
              :file-path="refSidebar.path"
              @open-ref="openRefDoc"
            />
          </div>
        </div>
      </Transition>
    </div>
  </div>
  <div v-else class="page-container">
    <div class="page-inner" style="text-align: center; padding-top: 80px">
      <div v-if="loading">加载中...</div>
      <div v-else>特性未找到: {{ featureId }}</div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, computed, watch, nextTick } from 'vue'
import { useRoute } from 'vue-router'
import { featureGraphApi, fetchJson, postJson } from '../api'
import DocViewer from '../shared/DocViewer.vue'

const route = useRoute()
const featureId = computed(() => route.params.id as string)
const productType = computed(() => (route.query.product as string) || '')

const loading = ref(true)
const feature = ref<any>(null)
const columns = ref<any[]>([])
const docs = ref<any[]>([])
const deps = ref<any[]>([])
const licenses = ref<any[]>([])
const activeTab = ref('summary')
const activeDoc = ref<any>(null)
const docContent = ref('')
const miniGraphRef = ref<HTMLElement | null>(null)

// Review state
const depReviewStatuses = ref<Record<string, string>>({})
const licReviewStatuses = ref<Record<string, string>>({})

function depItemId(row: any): string {
  return `${row.source_feature_id}:dep:${row.target_feature_id}`
}
function licItemId(row: any): string {
  return `${row.feature_id}:lic:${row.license_number}`
}

const enrichedDeps = computed(() =>
  deps.value.map((d: any) => ({
    ...d,
    _reviewStatus: depReviewStatuses.value[depItemId(d)] || 'pending',
  }))
)

const enrichedLicenses = computed(() =>
  licenses.value.map((l: any) => ({
    ...l,
    _reviewStatus: licReviewStatuses.value[licItemId(l)] || 'pending',
  }))
)

function reviewTagType(s: string) {
  if (s === 'accepted') return 'success'
  if (s === 'rejected') return 'danger'
  return 'info'
}

function reviewLabel(s: string) {
  if (s === 'accepted') return '已接受'
  if (s === 'rejected') return '已拒绝'
  return '待审查'
}

async function doDepReview(action: 'accept' | 'reject', row: any) {
  const itemId = depItemId(row)
  const url = action === 'accept' ? featureGraphApi.reviewAccept : featureGraphApi.reviewReject
  await postJson(url, { item_type: 'dependency', item_id: itemId })
  depReviewStatuses.value[itemId] = action === 'accept' ? 'accepted' : 'rejected'
}

async function doLicReview(action: 'accept' | 'reject', row: any) {
  const itemId = licItemId(row)
  const url = action === 'accept' ? featureGraphApi.reviewAccept : featureGraphApi.reviewReject
  await postJson(url, { item_type: 'license', item_id: itemId })
  licReviewStatuses.value[itemId] = action === 'accept' ? 'accepted' : 'rejected'
}

// Ref sidebar state
const refSidebar = ref({
  show: false,
  loading: false,
  path: '',
  title: '',
  content: '',
})

// Graph state: all deps from backend for expansion
const allDepsCache = ref<any[]>([])
const graphExpandedNodes = ref<Set<string>>(new Set())
let networkInstance: any = null
let nodesDataSet: any = null
let edgesDataSet: any = null

const docTypeLabels: Record<string, string> = {
  overview: '概述',
  principle: '原理',
  activation: '激活',
  reference: '参考',
  other: '其他',
  index: '索引',
}

const docGroups = computed(() => {
  const groups: Record<string, any[]> = {}
  for (const doc of docs.value) {
    const t = doc.doc_type || 'other'
    if (!groups[t]) groups[t] = []
    groups[t].push(doc)
  }
  return Object.entries(groups).map(([type, items]) => ({
    type,
    label: docTypeLabels[type] || type,
    docs: items,
  }))
})

function depTagType(t: string) {
  if (t === 'depends_on') return 'primary'
  if (t === 'conflicts_with') return 'danger'
  if (t === 'cooperates_with') return 'success'
  return 'info'
}

function formatValue(val: any) {
  if (val === undefined || val === null || val === '') return '-'
  if (typeof val === 'string' && val.length > 300) return val.slice(0, 300) + '...'
  return String(val)
}

function cleanHtml(s: string) {
  if (!s) return ''
  return s.replace(/<br\s*\/?>/gi, ' ').replace(/<[^>]*>/g, '')
}

// Summary tab: split columns into key vs extra
const SUMMARY_KEY_FIELDS = new Set(['feature_type', 'section', 'applicable_nf', 'config_required', 'product_type'])
// Fields excluded from the detail summary entirely (already shown in hero / definition)
const SUMMARY_SKIP_FIELDS = new Set(['feature_id', 'feature_name', 'definition'])

const summaryKeyFields = computed(() =>
  columns.value.filter(c => SUMMARY_KEY_FIELDS.has(c.key))
)

const summaryExtraFields = computed(() =>
  columns.value.filter(c => !SUMMARY_KEY_FIELDS.has(c.key) && !SUMMARY_SKIP_FIELDS.has(c.key))
)

let docLoadSeq = 0

async function selectDoc(doc: any) {
  activeDoc.value = doc
  activeTab.value = 'doc'
  const seq = ++docLoadSeq
  const params = new URLSearchParams()
  params.set('path', doc.file_path)
  const data = await fetchJson(`${featureGraphApi.docContent}?${params}`)
  // Only apply if this is still the active request
  if (seq === docLoadSeq) {
    docContent.value = data.content || ''
  }
}

async function openRefDoc(path: string, title: string) {
  refSidebar.value = { show: true, loading: true, path, title, content: '' }
  try {
    const params = new URLSearchParams()
    params.set('path', path)
    const data = await fetchJson(`${featureGraphApi.docContent}?${params}`)
    refSidebar.value.content = data.content || ''
  } finally {
    refSidebar.value.loading = false
  }
}

// --- Expandable graph ---

const typeColors: Record<string, string> = {
  depends_on: '#3b82f6',
  conflicts_with: '#ef4444',
  cooperates_with: '#22c55e',
}

function getNeighbors(nodeId: string, depList: any[]): string[] {
  const neighbors = new Set<string>()
  for (const d of depList) {
    if (d.source_feature_id === nodeId) neighbors.add(d.target_feature_id)
    if (d.target_feature_id === nodeId) neighbors.add(d.source_feature_id)
  }
  return Array.from(neighbors)
}

function getEdgesBetween(expanded: Set<string>, depList: any[]) {
  return depList.filter(d =>
    expanded.has(d.source_feature_id) && expanded.has(d.target_feature_id)
  )
}

function buildVisNodes(expanded: Set<string>, currentId: string) {
  return Array.from(expanded).map(id => {
    const isCurrent = id === currentId
    const dist = isCurrent ? 0 : getDistance(currentId, id)
    return {
      id,
      label: id,
      color: isCurrent
        ? { background: '#0891b2', border: '#0e7490', highlight: { background: '#0891b2', border: '#0e7490' } }
        : { background: '#e2e8f0', border: '#cbd5e1', highlight: { background: '#0891b2', border: '#0e7490' } },
      font: { color: isCurrent ? '#fff' : '#475569', size: isCurrent ? 11 : 10, face: 'JetBrains Mono' },
      size: isCurrent ? 18 : Math.max(8, 14 - dist * 3),
      shape: 'dot' as const,
    }
  })
}

// Track distance from root
const nodeDistance = ref<Map<string, number>>(new Map())

function getDistance(root: string, nodeId: string): number {
  return nodeDistance.value.get(nodeId) ?? 99
}

function computeDistances(root: string) {
  const dist = new Map<string, number>()
  dist.set(root, 0)
  const queue = [root]
  while (queue.length > 0) {
    const current = queue.shift()!
    const currentDist = dist.get(current)!
    for (const nb of getNeighbors(current, allDepsCache.value)) {
      if (!dist.has(nb)) {
        dist.set(nb, currentDist + 1)
        queue.push(nb)
      }
    }
  }
  nodeDistance.value = dist
}

function buildVisEdges(edgeList: any[]) {
  return edgeList.map(d => ({
    from: d.source_feature_id,
    to: d.target_feature_id,
    color: { color: typeColors[d.dependency_type] || '#94a3b8', highlight: typeColors[d.dependency_type] || '#0891b2' },
    dashes: d.dependency_type !== 'depends_on',
    arrows: 'to' as const,
    label: d.dependency_type,
    font: { size: 8, color: '#94a3b8', strokeWidth: 3, strokeColor: '#ffffff', face: 'Inter' },
    title: `${d.source_feature_id} → ${d.target_feature_id}\n${d.dependency_type}`,
  }))
}

async function renderMiniGraph() {
  if (!miniGraphRef.value) return
  const vis = await import('vis-network/standalone')
  const Network = vis.Network
  const DataSet: any = vis.DataSet

  const currentId = featureId.value
  // Build 1-hop neighborhood (expand by double-click for more)
  const expanded = new Set<string>([currentId])
  for (const n of getNeighbors(currentId, allDepsCache.value)) {
    expanded.add(n)
  }
  graphExpandedNodes.value = expanded
  computeDistances(currentId)

  const edges = getEdgesBetween(expanded, allDepsCache.value)
  const visNodes = buildVisNodes(expanded, currentId)
  const visEdges = buildVisEdges(edges)

  nodesDataSet = new DataSet(visNodes)
  edgesDataSet = new DataSet(visEdges)

  networkInstance = new Network(miniGraphRef.value, { nodes: nodesDataSet, edges: edgesDataSet }, {
    nodes: { borderWidth: 1, borderWidthSelected: 2 },
    edges: { smooth: false, arrows: { to: { enabled: true, scaleFactor: 0.4 } } },
    physics: { barnesHut: { gravitationalConstant: -2000, springLength: 60 }, stabilization: { iterations: 80 } },
    interaction: { hover: true, tooltipDelay: 150, navigationButtons: false },
  })

  // Double-click to expand
  networkInstance.on('doubleClick', async (params: any) => {
    if (params.nodes.length === 0) return
    const clickedId = params.nodes[0] as string
    if (clickedId === currentId) return

    const newNeighbors = getNeighbors(clickedId, allDepsCache.value)
    const newNodeIds: string[] = []
    for (const nb of newNeighbors) {
      if (!graphExpandedNodes.value.has(nb)) {
        graphExpandedNodes.value.add(nb)
        newNodeIds.push(nb)
      }
    }
    if (newNodeIds.length === 0) return

    computeDistances(currentId)
    const newVisNodes = newNodeIds.map(id => buildVisNodes(new Set([id]), currentId)[0])
    const allEdges = getEdgesBetween(graphExpandedNodes.value, allDepsCache.value)
    const newEdges = allEdges.filter(e =>
      newNodeIds.includes(e.source_feature_id) || newNodeIds.includes(e.target_feature_id)
    )

    nodesDataSet.add(newVisNodes)
    edgesDataSet.add(buildVisEdges(newEdges))
  })
}

async function loadAll() {
  loading.value = true
  try {
    const [colData, featData, docsData, depsData, licData, allDepsData] = await Promise.all([
      fetchJson(featureGraphApi.columns),
      fetchJson(featureGraphApi.feature(featureId.value, productType.value)),
      fetchJson(featureGraphApi.featureDocs(featureId.value)),
      fetchJson(featureGraphApi.featureDeps(featureId.value)),
      fetchJson(featureGraphApi.featureLicenses(featureId.value)),
      fetchJson(featureGraphApi.dependencies),
    ])
    columns.value = colData.columns || []
    feature.value = featData.error ? null : featData
    docs.value = docsData.docs || []
    deps.value = depsData.dependencies || []
    licenses.value = licData.licenses || []
    allDepsCache.value = allDepsData.dependencies || []
    networkInstance = null
    nodesDataSet = null
    edgesDataSet = null

    // Bulk-fetch review statuses for deps and licenses
    const depIds = deps.value.map(depItemId)
    const licIds = licenses.value.map(licItemId)
    if (depIds.length > 0) {
      try {
        const params = new URLSearchParams()
        params.set('item_type', 'dependency')
        params.set('item_ids', depIds.join(','))
        const bulkData = await fetchJson(`${featureGraphApi.reviewBulk}?${params}`)
        depReviewStatuses.value = bulkData.statuses || {}
      } catch { /* empty store is fine */ }
    }
    if (licIds.length > 0) {
      try {
        const params = new URLSearchParams()
        params.set('item_type', 'license')
        params.set('item_ids', licIds.join(','))
        const bulkData = await fetchJson(`${featureGraphApi.reviewBulk}?${params}`)
        licReviewStatuses.value = bulkData.statuses || {}
      } catch { /* empty store is fine */ }
    }
  } finally {
    loading.value = false
  }
}

watch(activeTab, async (tab) => {
  if (tab === 'deps') {
    await nextTick()
    renderMiniGraph()
  }
})

watch(featureId, () => {
  activeDoc.value = null
  docContent.value = ''
  activeTab.value = 'summary'
  networkInstance = null
  loadAll()
})

onMounted(loadAll)
</script>
