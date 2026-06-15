<template>
  <div class="cascade-tree">
    <CascadeNode
      v-if="rootNode"
      :node="rootNode"
      :graph="graph"
      :selected-id="selectedId"
      :shared-counts="sharedCounts"
      :max-depth="maxDepth"
      :current-depth="1"
      @select="$emit('select', $event)"
      @navigate="$emit('navigate', $event)"
    />
    <div v-else class="cascade-tree-empty">
      未找到根对象（BusinessDomain）
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed } from 'vue'
import CascadeNode from './CascadeNode.vue'

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
  graph: GraphData
  selectedId?: string
  maxDepth?: number
}>(), {
  maxDepth: 4,
})

defineEmits<{
  (e: 'select', id: string): void
  (e: 'navigate', id: string): void
}>()

const rootNode = computed(() => {
  if (!props.graph.root_id) return null
  return props.graph.objects[props.graph.root_id] || null
})

const sharedCounts = computed<Record<string, number>>(() => {
  const counts: Record<string, number> = {}
  for (const e of props.graph.edges) {
    counts[e.to] = (counts[e.to] || 0) + 1
  }
  return counts
})
</script>

<style scoped>
.cascade-tree {
  padding: var(--space-2);
}
.cascade-tree-empty {
  padding: var(--space-8);
  text-align: center;
  color: var(--text-tertiary);
}
</style>
