<template>
  <div class="object-detail" v-if="obj">
    <!-- Header -->
    <div class="detail-header">
      <div class="detail-type-row">
        <span class="detail-type-badge" :style="{ background: typeColor }">{{ typeLabel }}</span>
        <span v-if="productTag" class="detail-product-badge" :class="productTag.toLowerCase()">{{ productTag }}</span>
        <span class="detail-id">{{ obj.object_id }}</span>
      </div>
      <h2 class="detail-name">{{ obj.name }}</h2>
      <p v-if="obj.summary" class="detail-summary">{{ obj.summary }}</p>
    </div>

    <!-- Schema Attributes -->
    <div class="detail-section" v-if="Object.keys(obj.attributes).length">
      <h3 class="detail-section-title">Schema 属性</h3>
      <div class="attr-table">
        <div v-for="(val, key) in obj.attributes" :key="key" class="attr-row">
          <div class="attr-key">{{ key }}</div>
          <div class="attr-val">{{ cleanValue(val) }}</div>
        </div>
      </div>
    </div>

    <!-- Relationships -->
    <div class="detail-section" v-if="hasAnyRelationship">
      <h3 class="detail-section-title">关联关系</h3>

      <!-- Downstream groups -->
      <div v-for="g in downstreamGroups" :key="'d_' + g.relation" class="rel-group">
        <div class="rel-group-header" @click="toggleGroup(g, 'd')">
          <span class="rel-arrow">{{ isCollapsed(g, 'd') ? '▸' : '▾' }}</span>
          <span class="rel-label">下游 · {{ relLabel(g.relation) }}</span>
          <span class="rel-count">{{ g.edges.length }}</span>
        </div>
        <div v-if="!isCollapsed(g, 'd')" class="rel-items">
          <div
            v-for="edge in g.edges"
            :key="edge.to"
            class="rel-item"
            @click="$emit('navigate', edge.to)"
          >
            <span class="rel-item-id">{{ edge.to }}</span>
            <span class="rel-item-name">{{ graph.objects[edge.to]?.name || '' }}</span>
            <span v-if="edge.meta?.context" class="rel-item-meta">{{ edge.meta.context }}</span>
          </div>
        </div>
      </div>

      <!-- Upstream groups -->
      <div v-for="g in upstreamGroups" :key="'u_' + g.relation" class="rel-group">
        <div class="rel-group-header" @click="toggleGroup(g, 'u')">
          <span class="rel-arrow">{{ isCollapsed(g, 'u') ? '▸' : '▾' }}</span>
          <span class="rel-label">上游 · {{ relLabel(g.relation) }}</span>
          <span class="rel-count">{{ g.edges.length }}</span>
        </div>
        <div v-if="!isCollapsed(g, 'u')" class="rel-items">
          <div
            v-for="edge in g.edges"
            :key="edge.from"
            class="rel-item"
            @click="$emit('navigate', edge.from)"
          >
            <span class="rel-item-id">{{ edge.from }}</span>
            <span class="rel-item-name">{{ graph.objects[edge.from]?.name || '' }}</span>
          </div>
        </div>
      </div>

      <!-- Cross-cutting groups -->
      <div v-for="g in crossGroups" :key="'c_' + g.relation" class="rel-group">
        <div class="rel-group-header" @click="toggleGroup(g, 'c')">
          <span class="rel-arrow">{{ isCollapsed(g, 'c') ? '▸' : '▾' }}</span>
          <span class="rel-label">{{ relLabel(g.relation) }}</span>
          <span class="rel-count">{{ g.edges.length }}</span>
        </div>
        <div v-if="!isCollapsed(g, 'c')" class="rel-items">
          <div
            v-for="edge in g.edges"
            :key="edge.to"
            class="rel-item"
            @click="$emit('navigate', edge.to)"
          >
            <span class="rel-item-id">{{ edge.to }}</span>
            <span class="rel-item-name">{{ graph.objects[edge.to]?.name || '' }}</span>
          </div>
        </div>
      </div>
    </div>
  </div>
  <div v-else class="object-detail-empty">
    选择左侧对象查看详情
  </div>
</template>

<script setup lang="ts">
import { computed, ref } from 'vue'

interface GraphObject {
  object_id: string
  object_type: string
  name: string
  summary: string
  attributes: Record<string, string>
}

interface GraphEdge {
  from: string
  relation: string
  to: string
  meta?: Record<string, string>
}

interface GraphData {
  objects: Record<string, GraphObject>
  edges: GraphEdge[]
  root_id: string
}

const props = defineProps<{
  obj: GraphObject | null
  graph: GraphData
}>()

defineEmits<{
  (e: 'navigate', id: string): void
}>()

const DOWNSTREAM_RELS = ['contains', 'instantiated_as', 'uses_feature', 'uses_task', 'decomposes_to', 'invokes', 'operates_on']
const CROSS_RELS = ['constrained_by', 'has_decision', 'uses_semantic_object', 'requires_license', 'selects', 'sets_value_pattern']

interface RelGroupData {
  relation: string
  edges: GraphEdge[]
}

interface CollapseState {
  [key: string]: boolean
}

const collapsed = ref<CollapseState>({})

function groupKey(section: string, relation: string): string {
  return `${section}_${relation}`
}

function isCollapsed(g: RelGroupData, section: string): boolean {
  return collapsed.value[groupKey(section, g.relation)] ?? false
}

function toggleGroup(g: RelGroupData, section: string) {
  const key = groupKey(section, g.relation)
  collapsed.value[key] = !collapsed.value[key]
}

function groupEdges(edges: GraphEdge[]): RelGroupData[] {
  const groups: RelGroupData[] = []
  for (const edge of edges) {
    let g = groups.find(g => g.relation === edge.relation)
    if (!g) {
      g = { relation: edge.relation, edges: [] }
      groups.push(g)
    }
    g.edges.push(edge)
  }
  return groups
}

const downstreamGroups = computed<RelGroupData[]>(() => {
  if (!props.obj) return []
  return groupEdges(
    props.graph.edges.filter(e => e.from === props.obj!.object_id && DOWNSTREAM_RELS.includes(e.relation))
  )
})

const upstreamGroups = computed<RelGroupData[]>(() => {
  if (!props.obj) return []
  return groupEdges(
    props.graph.edges.filter(e => e.to === props.obj!.object_id && DOWNSTREAM_RELS.includes(e.relation))
  )
})

const crossGroups = computed<RelGroupData[]>(() => {
  if (!props.obj) return []
  return groupEdges(
    props.graph.edges.filter(e => e.from === props.obj!.object_id && CROSS_RELS.includes(e.relation))
  )
})

const hasAnyRelationship = computed(() =>
  downstreamGroups.value.length > 0 ||
  upstreamGroups.value.length > 0 ||
  crossGroups.value.length > 0
)

const TYPE_LABELS: Record<string, string> = {
  BusinessDomain: '业务域',
  NetworkScenario: '场景',
  ConfigurationSolution: '方案',
  Feature: '特性',
  ConfigTask: '任务',
  DecisionPoint: '决策点',
  BusinessRule: '业务规则',
  SemanticObject: '语义对象',
  MMLCommand: 'MML命令',
  ConfigObject: '配置对象',
  License: 'License',
  TaskRule: '任务规则',
  CommandRule: '命令规则',
}

const TYPE_COLORS: Record<string, string> = {
  BusinessDomain: '#6366f1',
  NetworkScenario: '#8b5cf6',
  ConfigurationSolution: '#3b82f6',
  Feature: '#06b6d4',
  ConfigTask: '#10b981',
  MMLCommand: '#f59e0b',
  DecisionPoint: '#ec4899',
  BusinessRule: '#ef4444',
  SemanticObject: '#14b8a6',
  ConfigObject: '#64748b',
  License: '#ea580c',
}

const typeLabel = computed(() => props.obj ? (TYPE_LABELS[props.obj.object_type] || props.obj.object_type) : '')
const typeColor = computed(() => props.obj ? (TYPE_COLORS[props.obj.object_type] || '#64748b') : '#64748b')

// UDG/UNC product tag for Features
const productTag = computed(() => {
  if (!props.obj || props.obj.object_type !== 'Feature') return ''
  const id = props.obj.object_id
  if (id.startsWith('GWFD-')) return 'UDG'
  if (id.startsWith('WSFD-')) return 'UNC'
  return ''
})

function relLabel(rel: string): string {
  const labels: Record<string, string> = {
    contains: '包含场景',
    instantiated_as: '实例化方案',
    uses_feature: '使用特性',
    uses_task: '使用任务',
    decomposes_to: '分解为任务',
    invokes: '调用命令',
    operates_on: '操作对象',
    constrained_by: '约束规则',
    has_decision: '决策点',
    uses_semantic_object: '语义对象',
    requires_license: '需要License',
    selects: '选择',
    sets_value_pattern: '设置参数模式',
  }
  return labels[rel] || rel
}

function cleanValue(val: string): string {
  if (!val) return ''
  return val.replace(/`/g, '').replace(/\*\*/g, '').trim()
}
</script>

<style scoped>
.object-detail {
  font-size: var(--text-xs);
}
.detail-header {
  margin-bottom: var(--space-4);
  padding-bottom: var(--space-3);
  border-bottom: 1px solid var(--border);
}
.detail-type-row {
  display: flex;
  align-items: center;
  gap: var(--space-2);
  margin-bottom: var(--space-1);
}
.detail-type-badge {
  color: white;
  font-size: 10px;
  padding: 1px 8px;
  border-radius: 999px;
}
.detail-product-badge {
  font-size: 10px;
  padding: 1px 7px;
  border-radius: 999px;
  font-weight: 600;
  letter-spacing: 0.03em;
}
.detail-product-badge.udg {
  color: #1e40af;
  background: #dbeafe;
}
.detail-product-badge.unc {
  color: #9d174d;
  background: #fce7f3;
}
.detail-id {
  font-family: var(--font-mono);
  font-size: var(--text-2xs);
  color: var(--text-tertiary);
}
.detail-name {
  font-size: var(--text-lg);
  font-weight: 700;
  margin: 0 0 var(--space-1);
  letter-spacing: -0.01em;
}
.detail-summary {
  font-size: var(--text-xs);
  color: var(--text-secondary);
  line-height: 1.6;
  margin: 0;
}
.detail-section {
  margin-bottom: var(--space-4);
}
.detail-section-title {
  font-size: 10px;
  font-weight: 700;
  color: var(--text-tertiary);
  text-transform: uppercase;
  letter-spacing: 0.08em;
  margin: 0 0 var(--space-2);
}
.attr-table {
  display: grid;
  grid-template-columns: minmax(110px, 160px) 1fr;
  gap: 1px;
  background: var(--border-light);
  border: 1px solid var(--border-light);
  border-radius: var(--radius);
  overflow: hidden;
}
.attr-row {
  display: contents;
}
.attr-key {
  background: var(--bg-page);
  padding: 4px 10px;
  font-family: var(--font-mono);
  font-size: 10px;
  font-weight: 500;
  color: var(--text-secondary);
  word-break: break-all;
}
.attr-val {
  background: var(--bg-card);
  padding: 4px 10px;
  font-size: var(--text-2xs);
  color: var(--text-primary);
  line-height: 1.5;
  word-break: break-word;
}
.rel-group {
  margin-bottom: var(--space-2);
}
.rel-group-header {
  display: flex;
  align-items: center;
  gap: var(--space-2);
  cursor: pointer;
  padding: var(--space-1) 0;
  user-select: none;
  border-radius: var(--radius-sm);
}
.rel-group-header:hover {
  color: var(--accent);
}
.rel-arrow {
  font-size: 10px;
  color: var(--text-tertiary);
  width: 12px;
}
.rel-label {
  font-size: var(--text-xs);
  font-weight: 500;
}
.rel-count {
  font-size: 10px;
  color: var(--accent);
  background: var(--accent-soft);
  padding: 1px 6px;
  border-radius: 999px;
  margin-left: auto;
}
.rel-items {
  padding-left: var(--space-5);
  margin-top: var(--space-1);
}
.rel-item {
  display: flex;
  align-items: baseline;
  gap: var(--space-2);
  padding: 3px 6px;
  border-radius: var(--radius-sm);
  cursor: pointer;
  font-size: var(--text-2xs);
  transition: background var(--duration) var(--ease);
  flex-wrap: wrap;
}
.rel-item:hover {
  background: var(--accent-soft);
}
.rel-item-id {
  font-family: var(--font-mono);
  color: var(--accent);
  flex-shrink: 0;
  font-weight: 500;
}
.rel-item-name {
  color: var(--text-secondary);
  flex: 1;
  min-width: 0;
}
.rel-item-meta {
  color: var(--text-tertiary);
  font-style: italic;
  font-size: 10px;
}
.object-detail-empty {
  text-align: center;
  padding: var(--space-12);
  color: var(--text-tertiary);
  font-size: var(--text-sm);
}
</style>
