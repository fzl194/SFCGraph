<template>
  <div v-if="feature" class="cmd-split" :class="{ 'is-dragging': dragging }" ref="splitRef">
    <section class="cmd-pane cmd-pane--left" :style="leftStyle">
      <el-tabs v-model="leftTab" class="cmd-tabs" @tab-change="onTabChange">
        <el-tab-pane label="特性" name="feature">
          <header class="cmd-hero">
            <div class="cmd-hero-id">{{ feature.feature_code }}</div>
            <h1 class="cmd-hero-name">{{ feature.name }}</h1>
            <div class="cmd-hero-tags">
              <el-tag size="small" effect="plain">{{ feature.feature_category }}</el-tag>
              <el-tag size="small" effect="plain" type="info">{{ feature.config_relevance }}</el-tag>
              <el-tag size="small" effect="plain">{{ nf }}</el-tag>
            </div>
          </header>
          <div v-for="s in sections" :key="s.key" class="summary-section">
            <div class="summary-section-title">{{ s.label }}</div>
            <div class="cmd-field-content" v-html="s.html"></div>
          </div>
          <div v-if="!sections.length" class="cmd-pane-empty">无抽取字段</div>
        </el-tab-pane>

        <el-tab-pane label="特性关系" name="relations">
          <el-table v-if="relations.length" :data="relations" size="small" @row-click="(r:any)=>goFeature(r.peer_code)">
            <el-table-column prop="peer_code" label="相关特性" width="140" />
            <el-table-column prop="peer_name" label="名称" min-width="160" show-overflow-tooltip />
            <el-table-column prop="relation_type" label="关系" width="120" />
            <el-table-column prop="interaction_note" label="说明" min-width="220" show-overflow-tooltip />
          </el-table>
          <div v-else class="cmd-pane-empty">无特性关系</div>
        </el-tab-pane>

        <el-tab-pane label="License" name="licenses">
          <el-table v-if="featLicenses.length" :data="featLicenses" size="small" @row-click="(r:any)=>goLicense(r.license_code)">
            <el-table-column prop="license_code" label="License" width="180" />
            <el-table-column prop="license_name" label="名称" min-width="200" show-overflow-tooltip />
            <el-table-column prop="control_item_id" label="控制项编号" width="120" />
          </el-table>
          <div v-else class="cmd-pane-empty">无 License 关联</div>
        </el-tab-pane>
      </el-tabs>
    </section>

    <div class="cmd-divider" @mousedown="startDrag">
      <button v-if="!leftCollapsed && !rightCollapsed" class="cmd-toggle" @click="leftCollapsed = true">‹</button>
      <button v-if="!leftCollapsed && !rightCollapsed" class="cmd-toggle" @click="rightCollapsed = true">›</button>
      <button v-if="leftCollapsed" class="cmd-toggle" @click="leftCollapsed = false">›</button>
      <button v-if="rightCollapsed" class="cmd-toggle" @click="rightCollapsed = false">‹</button>
    </div>

    <section class="cmd-pane cmd-pane--right" :style="rightStyle">
      <div class="cmd-pane-head">
        <div class="doc-tabs" v-if="featureDocs.length > 1">
          <button v-for="(d, i) in featureDocs" :key="i" :class="['doc-tab', { active: activeDoc === i }]"
                  :title="d.doc_title" @click="switchDoc(i)">{{ docLabel(d) }}</button>
        </div>
        <span v-else>原始文档</span>
      </div>
      <div class="cmd-pane-body">
        <DocViewer v-if="mdContent" :content="mdContent" :file-path="currentDocPath" api-base="feature-graph" :show-title="true" />
        <div v-else class="cmd-pane-empty">该特性无产品文档</div>
      </div>
    </section>
  </div>
  <div v-else class="cmd-notfound">
    <span v-if="loading">加载中…</span><span v-else>特性未找到：{{ code }}</span>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, computed, watch } from 'vue'
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
const feature = ref<any>(null)
const mdContent = ref('')
const leftTab = ref('feature')
const featureDocs = ref<{ doc_path: string; doc_title: string; doc_type?: string }[]>([])
const activeDoc = ref(0)
const currentDocPath = computed(() => featureDocs.value[activeDoc.value]?.doc_path || '')
const relations = ref<any[]>([])
const featLicenses = ref<any[]>([])
const activatedTabs = ref({ relations: false, licenses: false })

// ---- 数据驱动 sections（复刻 CommandDetail）----
const SKIP_KEYS = new Set(['id', 'nf', 'version', 'source_path', 'source_evidence_ids',
  'variant_dimensions', 'is_directory', 'doc_assets', 'has_activation_doc', 'overview_count'])
const LABEL_MAP: Record<string, string> = {
  feature_code: '特性编号', name: '名称', feature_category: '类别', config_relevance: '配置相关性',
  catalog_section: '清单分区', parent_feature_code: '父特性', applicable_nf: '适用NF',
  nf_support_map: '代际支持', first_release_version: '首发版本', standards: '遵循标准',
  category_reason: '分类理由', has_overview: '概述状态',
  definition_raw: '定义', customer_value_raw: '客户价值', application_scenario_raw: '应用场景',
  availability_raw: '可获得性', feature_interaction_raw: '与其他特性的交互',
  system_impact_raw: '对系统的影响', restrictions_raw: '应用限制', principle_raw: '原理概述',
  charging_raw: '计费与话单', spec_raw: '特性规格', standards_raw: '遵循标准(原文)',
  release_history_raw: '发布历史', applicable_nf_raw: '适用NF(原文)',
}

function isNonEmpty(v: any): boolean {
  if (v === null || v === undefined) return false
  if (typeof v === 'string') return v.trim() !== ''
  if (Array.isArray(v)) return v.length > 0
  if (typeof v === 'object') return Object.keys(v).length > 0
  return true
}
function renderValue(v: any): string {
  if (Array.isArray(v)) return v.map((el) => renderMarkdown(el !== null && typeof el === 'object'
    ? '```json\n' + JSON.stringify(el, null, 2) + '\n```' : String(el))).join('\n')
  if (v !== null && typeof v === 'object') return renderMarkdown('```json\n' + JSON.stringify(v, null, 2) + '\n```')
  if (typeof v === 'boolean') return renderMarkdown(v ? '是' : '否')
  return renderMarkdown(String(v))
}
const DOC_TYPE_LABELS: Record<string, string> = {
  overview: '概述', activation: '激活', reference: '参考信息', principle: '原理',
  debug: '调测', flow: '流程', other: '文档',
}
function docLabel(d: { doc_type?: string; doc_title: string }): string {
  return DOC_TYPE_LABELS[d.doc_type || ''] || d.doc_title.slice(0, 18)
}

const sections = computed(() => {
  if (!feature.value) return []
  const out: { key: string; label: string; html: string }[] = []
  for (const key of Object.keys(feature.value)) {
    if (SKIP_KEYS.has(key)) continue
    const value = feature.value[key]
    if (!isNonEmpty(value)) continue
    out.push({ key, label: LABEL_MAP[key] || key, html: renderValue(value) })
  }
  return out
})

// ---- 多 md ----
async function switchDoc(i: number) {
  activeDoc.value = i
  mdContent.value = ''
  if (currentDocPath.value) {
    const data = await fetchJson(featureGraphApi.docContent(currentDocPath.value))
    mdContent.value = data.content || ''
  }
}

async function loadAll() {
  loading.value = true
  mdContent.value = ''
  feature.value = null
  featureDocs.value = []
  relations.value = []
  featLicenses.value = []
  activatedTabs.value = { relations: false, licenses: false }
  try {
    const data = await fetchJson(featureGraphApi.feature(nf.value, version.value, code.value))
    feature.value = data.error ? null : data
    if (!feature.value) return
    const docsData = await fetchJson(featureGraphApi.featureDocs(nf.value, version.value, code.value))
    featureDocs.value = docsData.docs || []
    activeDoc.value = 0
    if (featureDocs.value.length) {
      const mdData = await fetchJson(featureGraphApi.docContent(featureDocs.value[0].doc_path))
      mdContent.value = mdData.content || ''
    }
  } finally {
    loading.value = false
  }
}

async function onTabChange(t: string) {
  if (t === 'relations' && !activatedTabs.value.relations) {
    activatedTabs.value.relations = true
    const data = await fetchJson(featureGraphApi.featureRelations(nf.value, version.value, code.value))
    relations.value = data.relations || []
  }
  if (t === 'licenses' && !activatedTabs.value.licenses) {
    activatedTabs.value.licenses = true
    const data = await fetchJson(featureGraphApi.featureLicenses(nf.value, version.value, code.value))
    featLicenses.value = data.licenses || []
  }
}

function goFeature(peerCode: string) {
  if (!peerCode || peerCode.includes(' ')) return
  router.push({ name: 'feature-detail', params: { nf: nf.value, version: version.value, code: peerCode } })
}
function goLicense(licCode: string) {
  if (!licCode) return
  router.push({ name: 'license-detail', params: { nf: nf.value, version: version.value, code: licCode } })
}

// ---- 可拖拽双栏（复刻 CommandDetail）----
const splitRef = ref<HTMLElement>()
const leftPct = ref(58)
const leftCollapsed = ref(false)
const rightCollapsed = ref(false)
const dragging = ref(false)
const canDrag = computed(() => !leftCollapsed.value && !rightCollapsed.value)
const leftStyle = computed(() => {
  if (leftCollapsed.value) return { flex: '0 0 0%', minWidth: '0' }
  if (rightCollapsed.value) return { flex: '1 1 0%' }
  return { flex: `0 0 ${leftPct.value}%` }
})
const rightStyle = computed(() => {
  if (rightCollapsed.value) return { flex: '0 0 0%', minWidth: '0' }
  return { flex: '1 1 0%' }
})
function startDrag(e: MouseEvent) {
  if ((e.target as HTMLElement)?.closest('.cmd-toggle')) return
  if (!canDrag.value) return
  e.preventDefault()
  dragging.value = true
  const container = splitRef.value
  if (!container) return
  const onMove = (ev: MouseEvent) => {
    const rect = container.getBoundingClientRect()
    let pct = ((ev.clientX - rect.left) / rect.width) * 100
    pct = Math.max(20, Math.min(85, pct))
    leftPct.value = pct
  }
  const onUp = () => {
    dragging.value = false
    document.removeEventListener('mousemove', onMove)
    document.removeEventListener('mouseup', onUp)
  }
  document.addEventListener('mousemove', onMove)
  document.addEventListener('mouseup', onUp)
}

watch([nf, version, code], loadAll)
onMounted(loadAll)
</script>

<style scoped>
.cmd-split { display: flex; height: calc(100vh - var(--navbar-height)); overflow: hidden; }
.cmd-pane { display: flex; flex-direction: column; overflow: hidden; min-width: 0; transition: flex-basis 0.18s, flex-grow 0.18s; }
.cmd-split.is-dragging .cmd-pane { transition: none; }
.cmd-pane--left, .cmd-pane--right { background: var(--bg-card); }
.cmd-divider { flex: 0 0 8px; position: relative; background: var(--border); cursor: col-resize; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 28px; z-index: 5; user-select: none; }
.cmd-divider:hover, .cmd-split.is-dragging .cmd-divider { background: var(--accent); }
.cmd-toggle { width: 20px; height: 20px; border: 1px solid var(--border); background: var(--bg-card); color: var(--text-secondary); border-radius: 3px; font-size: 14px; line-height: 1; cursor: pointer; display: flex; align-items: center; justify-content: center; padding: 0; }
.cmd-toggle:hover { color: var(--accent); border-color: var(--accent); }
.cmd-tabs { flex: 1; display: flex; flex-direction: column; overflow: hidden; }
.cmd-tabs :deep(.el-tabs__header) { flex-shrink: 0; margin: 0; padding: 0 var(--space-5); }
.cmd-tabs :deep(.el-tabs__content) { flex: 1; overflow-y: auto; }
.cmd-tabs :deep(.el-tab-pane) { padding: var(--space-5); }
.cmd-pane-head { flex-shrink: 0; padding: var(--space-3) var(--space-5); font-size: var(--text-2xs); color: var(--text-tertiary); text-transform: uppercase; letter-spacing: 0.08em; border-bottom: 1px solid var(--border); }
.cmd-pane-body { flex: 1; overflow-y: auto; }
.doc-tabs { display: flex; gap: 4px; flex-wrap: wrap; }
.doc-tab { font-size: var(--text-xs); padding: 4px 10px; border: 1px solid var(--border); background: var(--bg-card); border-radius: 4px; cursor: pointer; color: var(--text-secondary); }
.doc-tab.active { color: var(--accent); border-color: var(--accent); }
.cmd-hero { margin-bottom: var(--space-5); padding-bottom: var(--space-4); border-bottom: 1px solid var(--border); }
.cmd-hero-id { font-family: var(--font-mono); font-size: var(--text-sm); font-weight: 600; color: var(--accent); }
.cmd-hero-name { font-size: var(--text-xl); font-weight: 700; margin: var(--space-1) 0 var(--space-2); color: var(--text-primary); }
.cmd-hero-tags { display: flex; gap: var(--space-2); }
.cmd-pane-empty { padding: 60px 20px; text-align: center; color: var(--text-tertiary); font-size: var(--text-sm); }
.cmd-notfound { height: calc(100vh - var(--navbar-height)); display: flex; align-items: center; justify-content: center; color: var(--text-tertiary); }
.summary-section { margin-bottom: var(--space-5); }
.summary-section-title { font-size: var(--text-2xs); color: var(--text-tertiary); text-transform: uppercase; letter-spacing: 0.08em; font-weight: 600; margin-bottom: var(--space-2); }
.cmd-field-content { font-size: var(--text-sm); color: var(--text-secondary); line-height: 1.7; }
.cmd-field-content :deep(table) { border-collapse: collapse; width: 100%; margin: 8px 0; }
.cmd-field-content :deep(th), .cmd-field-content :deep(td) { border: 1px solid var(--border); padding: 6px 10px; text-align: left; font-size: var(--text-xs); }
.cmd-field-content :deep(th) { background: var(--bg-page); }
.cmd-field-content :deep(pre) { background: var(--bg-page); border: 1px solid var(--border); border-radius: var(--radius); padding: 10px 14px; overflow-x: auto; }
:deep(.el-table__row) { cursor: pointer; }
</style>
