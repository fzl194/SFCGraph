<template>
  <div class="assets-view stagger-in">
    <AssetTree class="col-tree" @select="onSelect" />
    <div class="col-main">
      <MdPreview :object-id="selectedId" />
    </div>
    <aside class="col-edges">
      <EdgeList :object-id="selectedId" />
    </aside>
  </div>
</template>

<script setup lang="ts">
import { ref, watch } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import AssetTree from '../components/AssetTree.vue'
import MdPreview from '../components/MdPreview.vue'
import EdgeList from '../components/EdgeList.vue'

const route = useRoute()
const router = useRouter()
const selectedId = ref<string | null>((route.query.o as string) || null)

function onSelect(id: string): void {
  selectedId.value = id
}

// URL 同步选中对象（可分享、可从图谱回跳）
watch(selectedId, (id) => {
  const q = { ...route.query }
  if (id) q.o = id
  else delete q.o
  router.replace({ path: '/assets', query: q })
})

watch(
  () => route.query.o,
  (o) => {
    const id = (o as string) || null
    if (id !== selectedId.value) selectedId.value = id
  },
)
</script>

<style scoped>
.assets-view {
  display: grid;
  grid-template-columns: 320px 1fr 280px;
  height: 100%;
  min-height: 0;
}

.col-tree {
  border-right: 1px solid var(--border);
  min-width: 0;
  overflow: hidden;
}

.col-main {
  min-width: 0;
  overflow: hidden;
}

.col-edges {
  border-left: 1px solid var(--border);
  background: var(--bg-elev);
  overflow: auto;
}

@media (max-width: 1100px) {
  .assets-view {
    grid-template-columns: 280px 1fr;
  }
  .col-edges {
    display: none;
  }
}

@media (max-width: 760px) {
  .assets-view {
    grid-template-columns: 1fr;
  }
  .col-tree {
    max-height: 40vh;
    border-right: none;
    border-bottom: 1px solid var(--border);
  }
}
</style>
