<template>
  <div v-loading="loading" class="cg-overview">
    <section class="cg-hero">
      <div class="cg-hero-head">
        <h1 class="cg-hero-title">特性图谱</h1>
        <p class="cg-hero-desc">
          产品能力世界的数字孪生——把<strong>特性</strong>、<strong>License 控制项</strong>及<strong>特性关系</strong>结构化，支撑配置生成、能力追溯与依赖/互斥分析。
        </p>
      </div>

      <div class="cg-hero-objects">
        <div class="cg-obj">
          <div class="cg-obj-glyph cg-glyph-box" aria-hidden="true">□</div>
          <div class="cg-obj-body">
            <div class="cg-obj-name">特性<span class="cg-obj-type">Feature</span></div>
            <div class="cg-obj-desc">产品正式能力：定义 / 应用场景 / 依赖 / License / 规格</div>
          </div>
          <div class="cg-obj-count">{{ stats.total_features ?? '-' }}</div>
        </div>
        <div class="cg-obj">
          <div class="cg-obj-glyph cg-glyph-ellipse" aria-hidden="true">○</div>
          <div class="cg-obj-body">
            <div class="cg-obj-name">License<span class="cg-obj-type">License</span></div>
            <div class="cg-obj-desc">License 控制项：功能开关 / 资源控制 / 取值范围</div>
          </div>
          <div class="cg-obj-count">{{ stats.total_licenses ?? '-' }}</div>
        </div>
        <div class="cg-obj">
          <div class="cg-obj-glyph cg-glyph-diamond" aria-hidden="true">◇</div>
          <div class="cg-obj-body">
            <div class="cg-obj-name">特性关系<span class="cg-obj-type">FeatureRelation</span></div>
            <div class="cg-obj-desc">依赖 / 互斥 / 协同：能力间交互约束</div>
          </div>
          <div class="cg-obj-count cg-obj-count--obj">{{ stats.total_relations ?? '-' }}</div>
        </div>
      </div>

      <div class="cg-hero-relations">
        <span class="cg-rel-label">关系</span>
        <span class="cg-rel"><span class="cg-rel-glyph">□</span>特性<span class="cg-rel-arrow">— depends_on →</span><span class="cg-rel-glyph">□</span>特性</span>
        <span class="cg-rel"><span class="cg-rel-glyph">□</span>特性<span class="cg-rel-arrow cg-rel-arrow--obj">— conflicts_with →</span><span class="cg-rel-glyph">□</span>特性</span>
        <span class="cg-rel"><span class="cg-rel-glyph">□</span>特性<span class="cg-rel-arrow">— requires_license →</span><span class="cg-rel-glyph cg-rel-glyph--obj">○</span>License</span>
      </div>
    </section>

    <div class="cg-section-title">
      <h2>网元版本</h2>
      <span class="cg-section-sub">{{ neVersions.length }} 个 · 点击进入特性列表</span>
    </div>
    <div v-if="neVersions.length" class="cg-nv-grid">
      <div
        v-for="nv in neVersions"
        :key="nv.nf + '@' + nv.version"
        class="cg-nv-card"
        @click="goList(nv.nf, nv.version)"
      >
        <div class="cg-nv-id">
          <span class="cg-nv-nf">{{ nv.nf }}</span><span class="cg-nv-at">@</span><span class="cg-nv-ver">{{ nv.version }}</span>
        </div>
        <div class="cg-nv-meta">
          <span class="cg-pill cg-pill--cmd">{{ nv.feature_count }} 特性</span>
          <span v-if="nv.license_count" class="cg-pill cg-pill--param">{{ nv.license_count }} License</span>
          <span v-if="nv.relation_count" class="cg-pill cg-pill--obj">{{ nv.relation_count }} 关系</span>
        </div>
        <span class="cg-nv-arrow" aria-hidden="true">→</span>
      </div>
    </div>
    <div v-else-if="!loading" class="cg-empty">暂无特性数据</div>
  </div>
</template>

<script setup lang="ts">
import { ref, computed, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { featureGraphApi, fetchJson } from '../api'

const router = useRouter()
const loading = ref(true)
const stats = ref<any>({})

const neVersions = computed(() => stats.value.ne_versions || [])

function goList(nf: string, version: string) {
  router.push({ name: 'feature-list', params: { nf, version } })
}

onMounted(async () => {
  try {
    stats.value = await fetchJson(featureGraphApi.stats)
  } finally {
    loading.value = false
  }
})
</script>

<style scoped>
.cg-hero {
  background:
    radial-gradient(120% 80% at 100% 0%, rgba(8, 145, 178, 0.06), transparent 60%),
    radial-gradient(100% 60% at 0% 100%, rgba(124, 58, 237, 0.05), transparent 55%),
    var(--bg-card);
  border: 1px solid var(--border);
  border-radius: var(--radius-lg, 14px);
  padding: var(--space-10) var(--space-10) var(--space-8);
  margin-bottom: var(--space-10);
}
.cg-hero-head { margin-bottom: var(--space-8); }
.cg-hero-title {
  font-size: var(--text-3xl, 30px);
  font-weight: 700;
  letter-spacing: -0.02em;
  margin: 0 0 var(--space-3);
  color: var(--text-primary);
}
.cg-hero-desc {
  margin: 0;
  font-size: var(--text-sm);
  color: var(--text-secondary);
  line-height: 1.75;
}
.cg-hero-desc strong { color: var(--text-primary); font-weight: 600; }

.cg-hero-objects {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: var(--space-8);
  padding: var(--space-6) 0;
  border-top: 1px solid var(--border);
  border-bottom: 1px solid var(--border);
  margin-bottom: var(--space-6);
}
.cg-obj { display: flex; align-items: center; gap: var(--space-4); padding: 0 var(--space-2); min-width: 0; }
.cg-obj-glyph {
  flex-shrink: 0; width: 44px; height: 44px;
  display: flex; align-items: center; justify-content: center;
  font-size: 26px; line-height: 1;
}
.cg-glyph-box { color: var(--accent); }
.cg-glyph-ellipse { color: var(--accent); border: 1.5px solid var(--accent); border-radius: 50%; }
.cg-glyph-diamond { color: #7c3aed; }
.cg-obj-body { flex: 1; min-width: 0; }
.cg-obj-name { font-size: var(--text-base); font-weight: 600; color: var(--text-primary); line-height: 1.4; }
.cg-obj-type { font-family: var(--font-mono); font-size: var(--text-xs); color: var(--text-tertiary); font-weight: 400; margin-left: var(--space-2); }
.cg-obj-desc { font-size: var(--text-xs); color: var(--text-tertiary); margin-top: 3px; line-height: 1.6; }
.cg-obj-count { font-family: var(--font-mono); font-size: var(--text-xl); font-weight: 700; color: var(--accent); flex-shrink: 0; letter-spacing: -0.02em; }
.cg-obj-count--obj { color: #7c3aed; }

.cg-hero-relations { display: flex; flex-wrap: wrap; align-items: center; gap: var(--space-3) var(--space-6); }
.cg-rel-label { font-size: var(--text-2xs); color: var(--text-tertiary); text-transform: uppercase; letter-spacing: 0.1em; font-weight: 600; }
.cg-rel { font-family: var(--font-mono); font-size: var(--text-xs); color: var(--text-secondary); display: inline-flex; align-items: center; gap: 6px; }
.cg-rel-glyph { color: var(--accent); font-size: var(--text-sm); }
.cg-rel-glyph--obj { color: #7c3aed; }
.cg-rel-arrow { color: var(--text-tertiary); }
.cg-rel-arrow--obj { color: #dc2626; }

.cg-section-title { display: flex; align-items: baseline; gap: var(--space-3); margin-bottom: var(--space-5); }
.cg-section-title h2 { font-size: var(--text-xl); font-weight: 600; margin: 0; color: var(--text-primary); }
.cg-section-sub { font-size: var(--text-xs); color: var(--text-tertiary); }
.cg-nv-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(320px, 1fr)); gap: var(--space-4); }
.cg-nv-card {
  position: relative;
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-left: 3px solid var(--accent);
  border-radius: var(--radius-lg, 12px);
  padding: var(--space-5) var(--space-12) var(--space-5) var(--space-6);
  cursor: pointer;
  transition: transform 0.18s ease, box-shadow 0.18s ease, border-color 0.18s ease;
}
.cg-nv-card:hover { border-color: var(--accent); box-shadow: var(--shadow-card); transform: translateY(-1px); }
.cg-nv-id { font-family: var(--font-mono); font-size: var(--text-lg); font-weight: 600; margin-bottom: var(--space-3); letter-spacing: -0.01em; }
.cg-nv-nf { color: var(--text-primary); }
.cg-nv-at { color: var(--text-tertiary); margin: 0 1px; }
.cg-nv-ver { color: var(--accent); }
.cg-nv-meta { display: flex; flex-wrap: wrap; gap: var(--space-2); }
.cg-pill { font-size: var(--text-2xs); padding: 2px 8px; border-radius: 999px; font-weight: 500; }
.cg-pill--cmd { color: var(--accent); background: var(--accent-soft); }
.cg-pill--param { color: var(--text-secondary); background: var(--bg-page); }
.cg-pill--obj { color: #7c3aed; background: rgba(124, 58, 237, 0.1); }
.cg-nv-arrow { position: absolute; right: var(--space-5); top: 50%; transform: translateY(-50%); color: var(--text-tertiary); transition: color 0.18s, transform 0.18s; }
.cg-nv-card:hover .cg-nv-arrow { color: var(--accent); transform: translateY(-50%) translateX(2px); }
.cg-empty { padding: var(--space-12); text-align: center; color: var(--text-tertiary); }

@media (max-width: 900px) {
  .cg-hero { padding: var(--space-6) var(--space-5); }
  .cg-hero-objects { grid-template-columns: 1fr; gap: var(--space-5); }
  .cg-hero-relations { flex-direction: column; align-items: flex-start; }
}
</style>
