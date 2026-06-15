<template>
  <div class="cascade-node">
    <div v-if="relationLabel" class="cascade-edge">
      <div class="cascade-edge-line"></div>
      <span class="cascade-edge-label">{{ relationLabel }}</span>
    </div>

    <div class="cascade-card" :class="{ selected: isSelected }" @click="handleSelect">
      <div class="cascade-card-header">
        <span class="cascade-type-badge" :style="{ background: typeColor }">{{ typeLabel }}</span>
        <span v-if="productTag" class="cascade-product-badge" :class="productTagClass">{{ productTag }}</span>
        <span class="cascade-card-id">{{ displayId }}</span>
        <span class="cascade-card-name">{{ displayName }}</span>
        <span v-if="sharedCount > 1" class="cascade-shared-badge" title="被多个上游引用">⟲ 共享</span>
        <button v-if="hasChildren" class="cascade-expand-btn" @click.stop="toggleExpand">
          {{ expanded ? '▾' : '▸' }}
        </button>
      </div>
      <p v-if="node.summary" class="cascade-card-summary">{{ node.summary }}</p>
      <div class="cascade-card-meta">
        <span v-for="(count, rel) in childCounts" :key="rel" class="cascade-meta-pill">
          {{ count }} {{ relLabel(rel) }}
        </span>
      </div>
    </div>

    <div v-if="expanded && hasChildren" class="cascade-children">
      <div class="cascade-children-row">
        <CascadeNode
          v-for="child in children"
          :key="child.object_id"
          :node="child"
          :relation-label="childRelation"
          :graph="graph"
          :selected-id="selectedId"
          :shared-counts="sharedCounts"
          :max-depth="maxDepth"
          :current-depth="currentDepth + 1"
          @select="$emit('select', $event)"
          @navigate="$emit('navigate', $event)"
        />
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed, ref } from 'vue'

interface GraphObject {
  object_id: string
  object_type: string
  name: string
  summary: string
  layer: string
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

const props = withDefaults(defineProps<{
  node: GraphObject
  relationLabel?: string
  graph: GraphData
  selectedId?: string
  sharedCounts?: Record<string, number>
  maxDepth?: number
  currentDepth?: number
}>(), {
  maxDepth: 4,
  currentDepth: 1,
})

const emit = defineEmits<{
  (e: 'select', id: string): void
  (e: 'navigate', id: string): void
}>()

const expanded = ref(props.currentDepth <= 2)

// Tree-driving relations by parent type
const TREE_RELATIONS: Record<string, string> = {
  BusinessDomain: 'contains',
  NetworkScenario: 'instantiated_as',
  ConfigurationSolution: 'uses_feature',
  Feature: 'decomposes_to',
  ConfigTask: 'invokes',
}

const childRelation = computed(() => TREE_RELATIONS[props.node.object_type] || '')

const children = computed<GraphObject[]>(() => {
  if (!childRelation.value || props.currentDepth >= props.maxDepth) return []
  const childIds = props.graph.edges
    .filter(e => e.from === props.node.object_id && e.relation === childRelation.value)
    .map(e => e.to)
  return childIds
    .map(id => props.graph.objects[id])
    .filter((o): o is GraphObject => Boolean(o))
})

const hasChildren = computed(() => {
  if (props.currentDepth >= props.maxDepth) return false
  if (!childRelation.value) return false
  return props.graph.edges.some(
    e => e.from === props.node.object_id && e.relation === childRelation.value
  )
})

const childCounts = computed<Record<string, number>>(() => {
  const counts: Record<string, number> = {}
  for (const e of props.graph.edges) {
    if (e.from === props.node.object_id) {
      counts[e.relation] = (counts[e.relation] || 0) + 1
    }
  }
  return counts
})

const isSelected = computed(() => props.selectedId === props.node.object_id)
const sharedCount = computed(() => props.sharedCounts?.[props.node.object_id] || 1)

const TYPE_LABELS: Record<string, string> = {
  BusinessDomain: '业务域',
  NetworkScenario: '场景',
  ConfigurationSolution: '方案',
  Feature: '特性',
  ConfigTask: '任务',
  MMLCommand: '命令',
  DecisionPoint: '决策点',
  BusinessRule: '规则',
  SemanticObject: '语义',
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

const typeLabel = computed(() => TYPE_LABELS[props.node.object_type] || props.node.object_type)
const typeColor = computed(() => TYPE_COLORS[props.node.object_type] || '#64748b')

// UDG/UNC product tag for Features (GWFD- = UDG, WSFD- = UNC) and Commands (CMD-UDG- / CMD-UNC-)
const productTag = computed(() => {
  const t = props.node.object_type
  const id = props.node.object_id
  if (t === 'Feature') {
    if (id.startsWith('GWFD-')) return 'UDG'
    if (id.startsWith('WSFD-')) return 'UNC'
  }
  if (t === 'MMLCommand') {
    if (id.startsWith('CMD-UDG-')) return 'UDG'
    if (id.startsWith('CMD-UNC-')) return 'UNC'
  }
  return ''
})
const productTagClass = computed(() => productTag.value.toLowerCase())

// For MMLCommand, show command_syntax (e.g., "ADD URR") instead of raw ID
const displayId = computed(() => {
  if (props.node.object_type === 'MMLCommand') {
    return props.node.attributes?.command_syntax || props.node.object_id
  }
  return props.node.object_id
})
const displayName = computed(() => {
  if (props.node.object_type === 'MMLCommand') {
    return '' // syntax is already shown as ID; name is duplicate
  }
  return props.node.name
})

function relLabel(rel: string): string {
  const labels: Record<string, string> = {
    uses_feature: '特性',
    uses_task: '任务',
    decomposes_to: '任务',
    invokes: '命令',
    constrained_by: '规则',
    has_decision: '决策',
    uses_semantic_object: '语义',
    requires_license: 'License',
    contains: '场景',
    instantiated_as: '方案',
    operates_on: '对象',
    selects: '选项',
    sets_value_pattern: '参数模式',
  }
  return labels[rel] || rel
}

function handleSelect() {
  emit('select', props.node.object_id)
  if (hasChildren.value) {
    expanded.value = !expanded.value
  }
}

function toggleExpand() {
  expanded.value = !expanded.value
}
</script>

<style scoped>
.cascade-node {
  margin-bottom: var(--space-2);
}
.cascade-edge {
  display: flex;
  align-items: center;
  gap: var(--space-2);
  padding-left: var(--space-3);
  margin-bottom: var(--space-1);
}
.cascade-edge-line {
  width: 2px;
  height: 14px;
  background: var(--border);
}
.cascade-edge-label {
  font-size: var(--text-2xs);
  color: var(--text-tertiary);
  font-family: var(--font-mono);
}
.cascade-card {
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: var(--radius-lg);
  padding: var(--space-3) var(--space-4);
  cursor: pointer;
  transition: border-color var(--duration) var(--ease), box-shadow var(--duration) var(--ease);
}
.cascade-card:hover {
  border-color: var(--accent-glow);
  box-shadow: var(--shadow-card);
}
.cascade-card.selected {
  border-left: 3px solid var(--accent);
  padding-left: calc(var(--space-4) - 2px);
}
.cascade-card-header {
  display: flex;
  align-items: center;
  gap: var(--space-2);
  flex-wrap: wrap;
}
.cascade-type-badge {
  color: white;
  font-size: 10px;
  padding: 1px 8px;
  border-radius: 999px;
  font-weight: 500;
  letter-spacing: 0.02em;
  white-space: nowrap;
}
.cascade-product-badge {
  font-size: 9px;
  padding: 1px 6px;
  border-radius: 999px;
  font-weight: 600;
  letter-spacing: 0.03em;
  white-space: nowrap;
}
.cascade-product-badge.udg {
  color: #1e40af;
  background: #dbeafe;
}
.cascade-product-badge.unc {
  color: #9d174d;
  background: #fce7f3;
}
.cascade-card-id {
  font-family: var(--font-mono);
  font-size: var(--text-2xs);
  color: var(--text-tertiary);
}
.cascade-card-name {
  font-size: var(--text-sm);
  font-weight: 600;
  color: var(--text-primary);
}
.cascade-shared-badge {
  font-size: 10px;
  color: var(--accent);
  background: var(--accent-soft);
  padding: 1px 6px;
  border-radius: 999px;
}
.cascade-expand-btn {
  background: none;
  border: none;
  cursor: pointer;
  color: var(--text-tertiary);
  font-size: var(--text-xs);
  padding: 0 4px;
  margin-left: auto;
  transition: color var(--duration) var(--ease);
}
.cascade-expand-btn:hover {
  color: var(--accent);
}
.cascade-card-summary {
  font-size: var(--text-2xs);
  color: var(--text-secondary);
  line-height: 1.5;
  margin: var(--space-1) 0 0;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
.cascade-card-meta {
  display: flex;
  gap: var(--space-2);
  flex-wrap: wrap;
  margin-top: var(--space-2);
}
.cascade-meta-pill {
  font-size: 9px;
  color: var(--text-tertiary);
  background: var(--bg-page);
  padding: 1px 6px;
  border-radius: 999px;
  border: 1px solid var(--border-light);
}
.cascade-children {
  padding-left: var(--space-4);
  margin-top: var(--space-2);
  border-left: 1px dashed var(--border);
  margin-left: var(--space-3);
}
.cascade-children-row {
  display: flex;
  flex-direction: column;
  gap: var(--space-2);
}
.cascade-children-row > .cascade-node {
  width: 100%;
}
</style>
