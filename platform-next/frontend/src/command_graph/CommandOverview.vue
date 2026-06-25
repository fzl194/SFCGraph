<template>
  <div v-loading="loading">
    <!-- 统计面板 -->
    <div class="cg-stats">
      <div class="cg-stat">
        <div class="cg-stat-num">{{ stats.total ?? '-' }}</div>
        <div class="cg-stat-label">命令总数</div>
      </div>
      <div class="cg-stat">
        <div class="cg-stat-num">{{ stats.nes?.length ?? '-' }}</div>
        <div class="cg-stat-label">网元数</div>
      </div>
      <div class="cg-stat">
        <div class="cg-stat-num">{{ totalVersions }}</div>
        <div class="cg-stat-label">版本数</div>
      </div>
      <div class="cg-stat">
        <div class="cg-stat-num">{{ stats.total_parameters ?? '-' }}</div>
        <div class="cg-stat-label">参数总数</div>
      </div>
    </div>

    <!-- 网元卡片网格 -->
    <div class="cg-section-title">
      <h3>网元</h3>
      <span class="cg-section-sub">{{ stats.nes?.length || 0 }} 个网元</span>
    </div>
    <div v-if="stats.nes?.length" class="cg-ne-grid">
      <div
        v-for="ne in stats.nes"
        :key="ne.name"
        class="cg-ne-card card-hover"
        @click="goNe(ne.name)"
      >
        <div class="cg-ne-card-header">
          <h4>{{ ne.name }}</h4>
          <span class="cg-ne-arrow" aria-hidden="true">→</span>
        </div>
        <div class="cg-ne-meta">
          <span class="cg-meta-pill">{{ ne.versions?.length || 0 }} 个版本</span>
          <span class="cg-meta-pill">{{ ne.command_count }} 条命令</span>
          <span v-if="ne.parameter_count" class="cg-meta-pill">{{ ne.parameter_count }} 个参数</span>
        </div>
      </div>
    </div>
    <div v-else-if="!loading" class="cg-empty">暂无命令数据</div>
  </div>
</template>

<script setup lang="ts">
import { ref, computed, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { commandGraphApi, fetchJson } from '../api'

const router = useRouter()
const loading = ref(true)
const stats = ref<any>({})

const totalVersions = computed(() => {
  const nes = stats.value.nes || []
  return nes.reduce((sum: number, ne: any) => sum + (ne.versions?.length || 0), 0)
})

function goNe(nf: string) {
  router.push({ name: 'command-versions', params: { nf } })
}

onMounted(async () => {
  try {
    stats.value = await fetchJson(commandGraphApi.stats)
  } finally {
    loading.value = false
  }
})
</script>

<style scoped>
/* 统计面板：4 个 KPI 一字排开 */
.cg-stats {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(160px, 1fr));
  gap: var(--space-4);
  margin-bottom: var(--space-8);
}
.cg-stat {
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: var(--radius-lg, 12px);
  padding: var(--space-5) var(--space-6);
  text-align: center;
}
.cg-stat-num {
  font-size: var(--text-2xl);
  font-weight: 700;
  color: var(--accent);
  line-height: 1.2;
}
.cg-stat-label {
  margin-top: var(--space-2);
  font-size: var(--text-xs);
  color: var(--text-tertiary);
}

/* 分区标题 */
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

/* 网元卡片网格 */
.cg-ne-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: var(--space-4);
}
.cg-ne-card {
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: var(--radius-lg, 12px);
  padding: var(--space-5) var(--space-6);
  cursor: pointer;
  transition: all 0.2s ease;
}
.cg-ne-card:hover {
  border-color: var(--accent);
  box-shadow: var(--shadow-card);
  transform: translateY(-1px);
}
.cg-ne-card-header {
  display: flex;
  align-items: center;
  gap: var(--space-2);
  margin-bottom: var(--space-3);
}
.cg-ne-card-header h4 {
  font-size: var(--text-base);
  font-weight: 600;
  margin: 0;
  flex: 1;
}
.cg-ne-arrow {
  color: var(--text-tertiary);
  transition: color 0.2s;
}
.cg-ne-card:hover .cg-ne-arrow {
  color: var(--accent);
}
.cg-ne-meta {
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
