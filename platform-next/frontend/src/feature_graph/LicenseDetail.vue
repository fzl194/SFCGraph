<template>
  <div v-if="license" class="cmd-split">
    <section class="cmd-pane cmd-pane--left" style="flex: 0 0 58%">
      <div class="cmd-tabs">
        <header class="cmd-hero">
          <div class="cmd-hero-id">{{ license.license_code }}</div>
          <h1 class="cmd-hero-name">{{ license.name }}</h1>
          <div class="cmd-hero-tags">
            <el-tag size="small" effect="plain">{{ license.control_item_type || '-' }}</el-tag>
            <el-tag size="small" effect="plain" type="info">{{ license.license_domain || '-' }}</el-tag>
            <el-tag size="small" effect="plain">{{ nf }}</el-tag>
          </div>
        </header>
        <div v-for="s in sections" :key="s.key" class="summary-section">
          <div class="summary-section-title">{{ s.label }}</div>
          <div class="cmd-field-content" v-html="s.html"></div>
        </div>
        <div class="summary-section">
          <div class="summary-section-title">关联特性 ({{ licenseFeatures.length }})</div>
          <div v-if="licenseFeatures.length" class="feat-links">
            <el-tag v-for="c in licenseFeatures" :key="c" size="small" effect="plain" class="feat-link"
                    @click="goFeature(c)">{{ c }}</el-tag>
          </div>
          <div v-else class="cmd-pane-empty">无关联特性</div>
        </div>
      </div>
    </section>
    <div class="cmd-divider"></div>
    <section class="cmd-pane cmd-pane--right" style="flex: 1 1 0%">
      <div class="cmd-pane-head">原始文档</div>
      <div class="cmd-pane-body">
        <DocViewer v-if="mdContent" :content="mdContent" :file-path="license.source_path" api-base="feature-graph" :show-title="true" />
        <div v-else class="cmd-pane-empty">无 License 文档</div>
      </div>
    </section>
  </div>
  <div v-else class="cmd-notfound">
    <span v-if="loading">加载中…</span><span v-else>License 未找到：{{ code }}</span>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, computed } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { featureGraphApi, fetchJson } from '../api'
import DocViewer from '../shared/DocViewer.vue'
import { renderMarkdown } from '../shared/markdown'

const route = useRoute()
const router = useRouter()
const nf = computed(() => route.params.nf as string)
const version = computed(() => route.params.version as string)
const code = computed(() => route.params.code as string)

const loading = ref(true)
const license = ref<any>(null)
const mdContent = ref('')
const licenseFeatures = ref<string[]>([])

const SKIP_KEYS = new Set(['id', 'nf', 'version', 'source_path', 'feature_refs_raw', 'feature_refs'])
const LABEL_MAP: Record<string, string> = {
  license_code: 'License编码', name: '名称', control_item_id: '控制项编号', control_item_type: '类型',
  license_domain: '域', applicable_nf: '适用NF', applicable_nf_raw: '适用NF(原文)',
  description_raw: '功能描述', implementation_description_raw: '实现描述',
  value_range_raw: '取值范围', default_value_raw: '默认值',
  related_control_items_raw: '相关控制项', application_scenario_raw: '应用场景',
  source_heading_raw: '来源标题',
}

function isNonEmpty(v: any): boolean {
  if (v === null || v === undefined) return false
  if (typeof v === 'string') return v.trim() !== ''
  if (Array.isArray(v)) return v.length > 0
  if (typeof v === 'object') return Object.keys(v).length > 0
  return true
}
function renderValue(v: any): string {
  if (Array.isArray(v)) return v.map((el) => String(el)).join('、')
  if (typeof v === 'boolean') return renderMarkdown(v ? '是' : '否')
  return renderMarkdown(String(v))
}
const sections = computed(() => {
  if (!license.value) return []
  const out: { key: string; label: string; html: string }[] = []
  for (const key of Object.keys(license.value)) {
    if (SKIP_KEYS.has(key)) continue
    const value = license.value[key]
    if (!isNonEmpty(value)) continue
    out.push({ key, label: LABEL_MAP[key] || key, html: renderValue(value) })
  }
  return out
})

function goFeature(c: string) {
  router.push({ name: 'feature-detail', params: { nf: nf.value, version: version.value, code: c } })
}

onMounted(async () => {
  loading.value = true
  try {
    const data = await fetchJson(featureGraphApi.license(nf.value, version.value, code.value))
    license.value = data.error ? null : data
    if (license.value?.source_path) {
      const mdData = await fetchJson(featureGraphApi.docContent(license.value.source_path))
      mdContent.value = mdData.content || ''
    }
    const featData = await fetchJson(featureGraphApi.licenseFeatures(nf.value, version.value, code.value))
    licenseFeatures.value = featData.feature_codes || []
  } finally {
    loading.value = false
  }
})
</script>

<style scoped>
.cmd-split { display: flex; height: calc(100vh - var(--navbar-height)); overflow: hidden; }
.cmd-pane { display: flex; flex-direction: column; overflow: hidden; min-width: 0; background: var(--bg-card); }
.cmd-divider { flex: 0 0 8px; background: var(--border); }
.cmd-tabs { flex: 1; overflow-y: auto; padding: var(--space-5); }
.cmd-hero { margin-bottom: var(--space-5); padding-bottom: var(--space-4); border-bottom: 1px solid var(--border); }
.cmd-hero-id { font-family: var(--font-mono); font-size: var(--text-sm); font-weight: 600; color: var(--accent); }
.cmd-hero-name { font-size: var(--text-xl); font-weight: 700; margin: var(--space-1) 0 var(--space-2); color: var(--text-primary); }
.cmd-hero-tags { display: flex; gap: var(--space-2); }
.cmd-pane-head { flex-shrink: 0; padding: var(--space-3) var(--space-5); font-size: var(--text-2xs); color: var(--text-tertiary); text-transform: uppercase; border-bottom: 1px solid var(--border); }
.cmd-pane-body { flex: 1; overflow-y: auto; }
.cmd-pane-empty { color: var(--text-tertiary); font-size: var(--text-sm); padding: var(--space-3) 0; }
.cmd-notfound { height: calc(100vh - var(--navbar-height)); display: flex; align-items: center; justify-content: center; color: var(--text-tertiary); }
.summary-section { margin-bottom: var(--space-5); }
.summary-section-title { font-size: var(--text-2xs); color: var(--text-tertiary); text-transform: uppercase; letter-spacing: 0.08em; font-weight: 600; margin-bottom: var(--space-2); }
.cmd-field-content { font-size: var(--text-sm); color: var(--text-secondary); line-height: 1.7; }
.feat-links { display: flex; flex-wrap: wrap; gap: 6px; }
.feat-link { cursor: pointer; font-family: var(--font-mono); }
</style>
