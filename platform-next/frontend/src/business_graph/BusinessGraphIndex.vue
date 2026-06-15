<template>
  <div class="page-container">
    <div class="page-inner">
      <div class="section-header">
        <div>
          <h1 class="section-title">业务图谱</h1>
          <p class="section-desc">按业务域组织的场景化三层图谱</p>
        </div>
      </div>

      <!-- Level 1: Domain cards -->
      <div v-if="domains.length" class="bg-domains">
        <div
          v-for="d in domains"
          :key="d.domain_name"
          class="bg-domain-card card-hover"
          :class="{ active: activeDomain === d.domain_name }"
          @click="selectDomain(d.domain_name)"
        >
          <div class="bg-domain-header">
            <span class="bg-domain-icon" aria-hidden="true">◆</span>
            <h2 class="bg-domain-name">{{ d.domain_name }}</h2>
            <span class="bg-domain-count">{{ d.scenario_count }} 个场景</span>
          </div>
          <p class="bg-domain-summary">{{ d.summary || '—' }}</p>
        </div>
      </div>
      <div v-else-if="!loading" class="bg-empty">暂无业务域数据</div>

      <!-- Level 2: Scenario cards under active domain -->
      <div v-if="activeDomainData" class="bg-scenario-section">
        <div class="bg-scenario-title">
          <h3>{{ activeDomainData.domain_name }} · 场景列表</h3>
          <span class="bg-scenario-subtitle">{{ activeDomainData.scenarios.length }} 个子场景</span>
        </div>
        <div class="bg-scenarios">
          <div
            v-for="s in activeDomainData.scenarios"
            :key="s.scenario_id"
            class="bg-scenario-card card-hover"
            @click="goScenario(s.scenario_id)"
          >
            <div class="bg-scenario-card-header">
              <h4>{{ s.scenario_name }}</h4>
              <span class="bg-scenario-arrow" aria-hidden="true">→</span>
            </div>
            <p class="bg-scenario-summary">{{ s.summary || '—' }}</p>
            <div class="bg-scenario-meta">
              <span v-if="getObjectCount(s, 'Feature')" class="bg-meta-pill">{{ getObjectCount(s, 'Feature') }} 特性</span>
              <span v-if="getObjectCount(s, 'ConfigTask')" class="bg-meta-pill">{{ getObjectCount(s, 'ConfigTask') }} 任务</span>
              <span v-if="getObjectCount(s, 'MMLCommand')" class="bg-meta-pill">{{ getObjectCount(s, 'MMLCommand') }} 命令</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, computed } from 'vue'
import { useRouter } from 'vue-router'
import { businessGraphApi, fetchJson } from '../api'

const router = useRouter()
const loading = ref(true)
const domains = ref<any[]>([])
const activeDomain = ref<string>('')

const activeDomainData = computed(() =>
  domains.value.find((d) => d.domain_name === activeDomain.value)
)

function selectDomain(name: string) {
  activeDomain.value = name
  router.push({ name: 'business-domain', params: { domainName: name } })
}

function goScenario(id: string) {
  router.push({ name: 'business-scenario', params: { scenarioId: id } })
}

function getObjectCount(s: any, keyword: string): string {
  if (!s.object_counts) return ''
  for (const [k, v] of Object.entries(s.object_counts)) {
    if (k.includes(keyword)) return String(v).replace(/\*\*/g, '')
  }
  return ''
}

onMounted(async () => {
  try {
    const data = await fetchJson(businessGraphApi.domains)
    domains.value = data.domains || []
    if (domains.value.length) {
      activeDomain.value = domains.value[0].domain_name
    }
  } finally {
    loading.value = false
  }
})
</script>

<style scoped>
.bg-domains {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
  gap: var(--space-4);
  margin-bottom: var(--space-10);
}
.bg-domain-card {
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: var(--radius-lg, 12px);
  padding: var(--space-5) var(--space-6);
  cursor: pointer;
  transition: all 0.2s ease;
}
.bg-domain-card:hover {
  border-color: var(--accent);
  box-shadow: var(--shadow-card);
}
.bg-domain-card.active {
  border-color: var(--accent);
  background: var(--accent-soft);
}
.bg-domain-header {
  display: flex;
  align-items: center;
  gap: var(--space-2);
  margin-bottom: var(--space-2);
}
.bg-domain-icon {
  color: var(--accent);
  font-size: var(--text-lg);
}
.bg-domain-name {
  font-size: var(--text-xl);
  font-weight: 600;
  margin: 0;
  flex: 1;
}
.bg-domain-count {
  font-size: var(--text-xs);
  color: var(--text-tertiary);
  background: var(--bg-page);
  padding: 2px 8px;
  border-radius: 999px;
}
.bg-domain-summary {
  font-size: var(--text-sm);
  color: var(--text-secondary);
  line-height: 1.6;
  margin: 0;
}
.bg-scenario-section {
  margin-top: var(--space-8);
}
.bg-scenario-title {
  display: flex;
  align-items: baseline;
  gap: var(--space-3);
  margin-bottom: var(--space-4);
  padding-bottom: var(--space-3);
  border-bottom: 1px solid var(--border-light);
}
.bg-scenario-title h3 {
  font-size: var(--text-lg);
  font-weight: 600;
  margin: 0;
}
.bg-scenario-subtitle {
  font-size: var(--text-xs);
  color: var(--text-tertiary);
}
.bg-scenarios {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(360px, 1fr));
  gap: var(--space-4);
}
.bg-scenario-card {
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: var(--radius-lg, 12px);
  padding: var(--space-5) var(--space-6);
  cursor: pointer;
  transition: all 0.2s ease;
}
.bg-scenario-card:hover {
  border-color: var(--accent);
  box-shadow: var(--shadow-card);
  transform: translateY(-1px);
}
.bg-scenario-card-header {
  display: flex;
  align-items: center;
  gap: var(--space-2);
  margin-bottom: var(--space-2);
}
.bg-scenario-card-header h4 {
  font-size: var(--text-base);
  font-weight: 600;
  margin: 0;
  flex: 1;
}
.bg-scenario-arrow {
  color: var(--text-tertiary);
  transition: color 0.2s;
}
.bg-scenario-card:hover .bg-scenario-arrow {
  color: var(--accent);
}
.bg-scenario-summary {
  font-size: var(--text-xs);
  color: var(--text-tertiary);
  line-height: 1.6;
  margin: 0 0 var(--space-3);
  display: -webkit-box;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
.bg-scenario-meta {
  display: flex;
  flex-wrap: wrap;
  gap: var(--space-2);
}
.bg-meta-pill {
  font-size: var(--text-2xs);
  color: var(--accent);
  background: var(--accent-soft);
  padding: 2px 8px;
  border-radius: 999px;
  font-weight: 500;
}
.bg-empty {
  padding: var(--space-12);
  text-align: center;
  color: var(--text-tertiary);
}
</style>
