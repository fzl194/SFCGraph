<template>
  <div v-loading="loading">
    <!-- 当前网元小标题 -->
    <div class="cg-section-title">
      <h3>{{ nf }}</h3>
      <span class="cg-section-sub">{{ versions.length }} 个版本</span>
    </div>

    <div v-if="versions.length" class="cg-ver-grid">
      <div
        v-for="v in versions"
        :key="v.version"
        class="cg-ver-card card-hover"
        @click="goVersion(v.version)"
      >
        <div class="cg-ver-card-header">
          <h4>{{ v.version }}</h4>
          <span class="cg-ver-arrow" aria-hidden="true">→</span>
        </div>
        <div class="cg-ver-meta">
          <span class="cg-meta-pill">{{ v.command_count }} 条命令</span>
          <span v-if="v.parameter_count" class="cg-meta-pill">{{ v.parameter_count }} 个参数</span>
        </div>
      </div>
    </div>
    <div v-else-if="!loading" class="cg-empty">网元 {{ nf }} 暂无版本数据</div>
  </div>
</template>

<script setup lang="ts">
import { ref, computed, onMounted, watch } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { commandGraphApi, fetchJson } from '../api'

const route = useRoute()
const router = useRouter()
const loading = ref(true)
const stats = ref<any>({})

const nf = computed(() => route.params.nf as string)
const versions = computed(() => {
  const ne = (stats.value.nes || []).find((n: any) => n.name === nf.value)
  return ne?.versions || []
})

function goVersion(version: string) {
  router.push({ name: 'command-list', params: { nf: nf.value, version } })
}

async function loadStats() {
  loading.value = true
  try {
    stats.value = await fetchJson(commandGraphApi.stats)
  } finally {
    loading.value = false
  }
}

watch(nf, loadStats)
onMounted(loadStats)
</script>

<style scoped>
.cg-section-title {
  display: flex;
  align-items: baseline;
  gap: var(--space-3);
  margin-bottom: var(--space-4);
  padding-bottom: var(--space-3);
  border-bottom: 1px solid var(--border-light);
}
.cg-section-title h3 {
  font-size: var(--text-lg);
  font-weight: 600;
  margin: 0;
}
.cg-section-sub {
  font-size: var(--text-xs);
  color: var(--text-tertiary);
}

.cg-ver-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
  gap: var(--space-4);
}
.cg-ver-card {
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: var(--radius-lg, 12px);
  padding: var(--space-5) var(--space-6);
  cursor: pointer;
  transition: all 0.2s ease;
}
.cg-ver-card:hover {
  border-color: var(--accent);
  box-shadow: var(--shadow-card);
  transform: translateY(-1px);
}
.cg-ver-card-header {
  display: flex;
  align-items: center;
  gap: var(--space-2);
  margin-bottom: var(--space-3);
}
.cg-ver-card-header h4 {
  font-size: var(--text-base);
  font-weight: 600;
  margin: 0;
  flex: 1;
  font-family: var(--font-mono);
}
.cg-ver-arrow {
  color: var(--text-tertiary);
  transition: color 0.2s;
}
.cg-ver-card:hover .cg-ver-arrow {
  color: var(--accent);
}
.cg-ver-meta {
  display: flex;
  flex-wrap: wrap;
  gap: var(--space-2);
}
.cg-meta-pill {
  font-size: var(--text-2xs);
  color: var(--accent);
  background: var(--accent-soft);
  padding: 2px 8px;
  border-radius: 999px;
  font-weight: 500;
}
.cg-empty {
  padding: var(--space-12);
  text-align: center;
  color: var(--text-tertiary);
}
</style>
