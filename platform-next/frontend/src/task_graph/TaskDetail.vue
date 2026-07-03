<template>
  <div v-if="error" class="tg-detail-error">
    <el-alert :title="error" type="error" show-icon :closable="false" />
  </div>

  <div v-else-if="task" class="tg-detail">
    <!-- ===== Hero ===== -->
    <header class="tg-hero-detail">
      <div class="tg-hero-id">{{ task.short }}</div>
      <h1 class="tg-hero-name">{{ task.task_logical_name || '-' }}</h1>
      <div class="tg-hero-tags">
        <el-tag size="small" effect="dark" :type="layerTagType(task.task_layer)">{{ task.task_layer || '-' }}</el-tag>
        <el-tag v-if="task.task_category" size="small" effect="plain">{{ task.task_category }}</el-tag>
        <el-tag size="small" :type="statusTagType(task.status)" effect="dark">{{ task.status || '-' }}</el-tag>
        <span class="tg-hero-nfver">{{ task.nf }}@{{ task.version }}</span>
      </div>
    </header>

    <!-- ===== ref 跨图谱跳转 ===== -->
    <div v-if="refTarget" class="summary-section">
      <div class="summary-section-title">ref 跨图谱锚点</div>
      <div class="tg-field-content">
        <router-link v-if="refTarget.to" :to="refTarget.to" class="tg-cross-link">
          → {{ refTarget.label }} <span class="tg-cross-value">{{ refTarget.value }}</span>
        </router-link>
        <span v-else class="tg-cross-plain">
          {{ refTarget.label }}: <span class="tg-cross-value">{{ refTarget.value }}</span>
        </span>
      </div>
    </div>

    <!-- ===== 基础字段 ===== -->
    <div class="summary-section">
      <div class="summary-section-title">基础字段</div>
      <div class="tg-field-grid">
        <div v-if="task.task_intent" class="tg-field-row">
          <span class="tg-field-label">意图</span>
          <span class="tg-field-value">{{ task.task_intent }}</span>
        </div>
        <div v-if="task.task_category" class="tg-field-row">
          <span class="tg-field-label">分类</span>
          <span class="tg-field-value">{{ task.task_category }}</span>
        </div>
        <div v-if="task.confidence != null" class="tg-field-row">
          <span class="tg-field-label">置信度</span>
          <span class="tg-field-value tg-mono">{{ task.confidence }}</span>
        </div>
        <div v-if="task.ref && !refTarget" class="tg-field-row">
          <span class="tg-field-label">ref 原文</span>
          <span class="tg-field-value tg-mono">{{ task.ref }}</span>
        </div>
      </div>
      <div v-if="task.notes" class="tg-notes">
        <div class="tg-field-label">备注</div>
        <pre class="tg-notes-pre">{{ task.notes }}</pre>
      </div>
    </div>

    <!-- ===== 参数绑定 ===== -->
    <div class="summary-section">
      <div class="summary-section-title">参数绑定 ({{ parameterBindings.length }})</div>
      <div v-if="parameterBindings.length" class="tg-field-content">
        <el-table :data="parameterBindings" size="small" border style="width: 100%">
          <el-table-column label="参数" min-width="180">
            <template #default="{ row }">
              <span class="tg-mono">{{ lastColonSegment(row.parameter_ref) || '-' }}</span>
            </template>
          </el-table-column>
          <el-table-column prop="binding_type" label="绑定类型" width="130" />
          <el-table-column prop="variable_source" label="变量来源" width="130" />
          <el-table-column prop="requiredness" label="必选" width="90" />
          <el-table-column label="取值" min-width="160">
            <template #default="{ row }">
              <span class="tg-mono tg-value-cell">{{ formatValue(row.value) }}</span>
            </template>
          </el-table-column>
          <el-table-column label="决策" width="120">
            <template #default="{ row }">
              <span v-if="row.decision_ref" class="tg-mono tg-dp-ref">{{ shortOnly(row.decision_ref) }}</span>
              <span v-else style="color: var(--text-tertiary)">-</span>
            </template>
          </el-table-column>
        </el-table>
      </div>
      <div v-else class="tg-empty-inline">无</div>
    </div>

    <!-- ===== 编排结构（task_relations）===== -->
    <div class="summary-section">
      <div class="summary-section-title">编排结构 ({{ taskRelations.length }})</div>
      <div v-if="taskRelations.length" class="tg-relations">
        <div v-for="(rel, idx) in taskRelations" :key="idx" class="tg-rel-row">
          <router-link
            v-if="rel.from_short"
            :to="`/task-graph/${task.nf}/${task.version}/${rel.from_short}`"
            class="tg-rel-node"
          >{{ rel.from_logical_name || rel.from_short }}<span class="tg-rel-layer">({{ rel.from_layer || '?' }})</span></router-link>
          <span v-else class="tg-rel-node tg-rel-node--muted">?</span>
          <span class="tg-rel-arrow">—{{ rel.relation_type }}→</span>
          <router-link
            v-if="rel.to_short"
            :to="`/task-graph/${task.nf}/${task.version}/${rel.to_short}`"
            class="tg-rel-node"
          >{{ rel.to_logical_name || rel.to_short }}<span class="tg-rel-layer">({{ rel.to_layer || '?' }})</span></router-link>
          <span v-else class="tg-rel-node tg-rel-node--muted">?</span>
          <el-tag v-if="rel.condition_ref" size="small" type="warning" effect="plain" class="tg-rel-cond">[DP {{ rel.condition_ref }}]</el-tag>
          <span v-if="rel.propagated_context && rel.propagated_context.length" class="tg-rel-prop">
            ↑ {{ rel.propagated_context.join(', ') }}
          </span>
        </div>
      </div>
      <div v-else class="tg-empty-inline">无</div>

      <!-- 作为端点的边：仅当 task_relations 空 且 endpoint_relations 非空 时显示(避免 feature 重复)-->
      <div
        v-if="!taskRelations.length && endpointRelations.length"
        class="tg-endpoint-relations"
      >
        <div class="tg-endpoint-label">作为端点的边（被引用 {{ endpointRelations.length }}）</div>
        <div class="tg-relations">
          <div v-for="(rel, idx) in endpointRelations" :key="'ep-' + idx" class="tg-rel-row">
            <span class="tg-rel-direction tg-mono">{{ rel.direction === 'from' ? '出→' : '入←' }}</span>
            <router-link
              v-if="rel.other"
              :to="`/task-graph/${task.nf}/${task.version}/${rel.other}`"
              class="tg-rel-node"
            >{{ rel.other_logical_name || rel.other }}<span class="tg-rel-layer">({{ rel.other_layer || '?' }})</span></router-link>
            <span v-else class="tg-rel-node tg-rel-node--muted">?</span>
            <span class="tg-rel-arrow">—{{ rel.relation_type }}—</span>
            <el-tag v-if="rel.condition_ref" size="small" type="warning" effect="plain" class="tg-rel-cond">[DP {{ rel.condition_ref }}]</el-tag>
          </div>
        </div>
      </div>

      <!-- parents -->
      <div v-if="parents.length" class="tg-parents">
        <div class="tg-field-label">被编排于（parents）</div>
        <div class="tg-parents-list">
          <router-link
            v-for="p in parents"
            :key="p.short"
            :to="`/task-graph/${task.nf}/${task.version}/${p.short}`"
            class="tg-parent-pill"
          >{{ p.logical_name || p.short }}<span class="tg-parent-layer">{{ p.layer || '?' }}</span></router-link>
        </div>
      </div>
    </div>

    <!-- ===== DecisionPoints（本 task 挂）===== -->
    <div class="summary-section">
      <div class="summary-section-title">决策点 ({{ decisionPoints.length }})</div>
      <div v-if="decisionPoints.length" class="tg-dps">
        <div v-for="dp in decisionPoints" :key="dp.decision_id" class="tg-dp-card">
          <header class="tg-dp-head">
            <span class="tg-dp-name">{{ dp.decision_name || '-' }}</span>
            <el-tag size="small" effect="plain" type="info">{{ dp.decision_type || '?' }}</el-tag>
            <span class="tg-dp-id tg-mono">{{ shortOnly(dp.decision_id) }}</span>
          </header>
          <div v-if="dp.options && dp.options.length" class="tg-dp-options">
            <div v-for="opt in dp.options" :key="opt.option_id" class="tg-dp-option">
              <div class="tg-dp-option-head">
                <span class="tg-mono tg-dp-option-id">{{ opt.option_id }}</span>
                <span class="tg-dp-option-name">{{ opt.option_name || '-' }}</span>
              </div>
              <el-table
                v-if="opt.impacts && opt.impacts.length"
                :data="opt.impacts"
                size="small"
                border
                style="width: 100%"
              >
                <el-table-column prop="target_type" label="目标类型" width="110" />
                <el-table-column prop="target_ref" label="目标引用" min-width="160">
                  <template #default="{ row }">
                    <span class="tg-mono">{{ row.target_ref || '-' }}</span>
                  </template>
                </el-table-column>
                <el-table-column prop="effect_type" label="影响类型" width="120" />
                <el-table-column label="影响详情" min-width="220">
                  <template #default="{ row }">
                    <span class="tg-impact-detail">{{ formatValue(row.effect_detail) }}</span>
                  </template>
                </el-table-column>
              </el-table>
              <div v-else class="tg-empty-inline">无 impacts</div>
            </div>
          </div>
        </div>
      </div>
      <div v-else class="tg-empty-inline">无</div>
    </div>

    <!-- ===== Rules（本 task 挂）===== -->
    <div class="summary-section">
      <div class="summary-section-title">规则 ({{ rules.length }})</div>
      <div v-if="rules.length" class="tg-field-content">
        <el-table :data="rules" size="small" border style="width: 100%">
          <el-table-column label="ID" width="110">
            <template #default="{ row }">
              <span class="tg-mono">{{ shortOnly(row.rule_id) }}</span>
            </template>
          </el-table-column>
          <el-table-column prop="rule_type" label="类型" width="120" />
          <el-table-column label="严重度" width="100">
            <template #default="{ row }">
              <el-tag size="small" :type="severityTagType(row.severity)" effect="dark">{{ row.severity || '-' }}</el-tag>
            </template>
          </el-table-column>
          <el-table-column prop="rule_name" label="名称" min-width="180" />
          <el-table-column label="约束" min-width="280">
            <template #default="{ row }">
              <span class="tg-constraint-cell">{{ truncate(constraintExpression(row.constraint), 120) || '-' }}</span>
            </template>
          </el-table-column>
        </el-table>
      </div>
      <div v-else class="tg-empty-inline">无</div>
    </div>

    <!-- ===== 证据 ===== -->
    <div class="summary-section">
      <div class="summary-section-title">证据 ({{ sourceEvidenceIds.length }})</div>
      <div v-if="sourceEvidenceIds.length" class="tg-evidence">
        <div v-for="ev in sourceEvidenceIds" :key="ev" class="tg-evidence-item tg-mono">{{ ev }}</div>
      </div>
      <div v-else class="tg-empty-inline">无</div>
    </div>
  </div>

  <div v-else class="tg-notfound">
    <span v-if="loading">加载中…</span>
    <span v-else>任务未找到：{{ nf }} / {{ version }} / {{ taskId }}</span>
  </div>
</template>

<script setup lang="ts">
import { ref, computed, onMounted, watch } from 'vue'
import { useRoute } from 'vue-router'
import { taskGraphApi, fetchJson } from '../api'

// ===== 详情响应类型（与后端 get_task 对齐）=====
interface RefParsed { type: string; value: string }
interface ParameterBinding {
  parameter_ref?: string
  binding_type?: string
  variable_source?: string
  requiredness?: string
  value?: unknown
  decision_ref?: string
}
interface TaskRelation {
  from_short?: string
  to_short?: string
  from_logical_name?: string
  from_layer?: string
  to_logical_name?: string
  to_layer?: string
  relation_type?: string
  condition_ref?: string
  propagated_context?: string[]
}
interface EndpointRelation {
  other?: string
  other_logical_name?: string
  other_layer?: string
  direction?: string
  relation_type?: string
  condition_ref?: string
}
interface Parent { short: string; logical_name: string; layer: string }
interface RuleImpact {
  target_type?: string
  target_ref?: string
  effect_type?: string
  effect_detail?: unknown
}
interface DecisionOption {
  option_id?: string
  option_name?: string
  impacts?: RuleImpact[]
}
interface DecisionPoint {
  decision_id?: string
  decision_name?: string
  decision_type?: string
  options?: DecisionOption[]
}
interface Rule {
  rule_id?: string
  rule_type?: string
  rule_name?: string
  severity?: string
  constraint?: unknown
}
interface TaskDetailResp {
  task_id: string
  short: string
  task_logical_name: string
  task_layer: string
  task_intent: string
  task_category: string
  nf: string
  version: string
  status: string
  ref: string
  ref_parsed: RefParsed
  confidence?: unknown
  notes?: string
  parameter_bindings?: ParameterBinding[]
  source_evidence_ids?: string[]
  task_relations?: TaskRelation[]
  endpoint_relations?: EndpointRelation[]
  parents?: Parent[]
  rules?: Rule[]
  decision_points?: DecisionPoint[]
}

const route = useRoute()
const nf = computed(() => route.params.nf as string)
const version = computed(() => route.params.version as string)
const taskId = computed(() => route.params.taskId as string)

const loading = ref(true)
const error = ref('')
const task = ref<TaskDetailResp | null>(null)

// ===== 派生 =====
const parameterBindings = computed(() => task.value?.parameter_bindings || [])
const taskRelations = computed(() => task.value?.task_relations || [])
const endpointRelations = computed(() => task.value?.endpoint_relations || [])
const parents = computed(() => task.value?.parents || [])
const rules = computed(() => task.value?.rules || [])
const decisionPoints = computed(() => task.value?.decision_points || [])
const sourceEvidenceIds = computed(() => task.value?.source_evidence_ids || [])

// ref 跨图谱跳转目标
interface RefTarget { to: string | null; label: string; value: string }
const refTarget = computed<RefTarget | null>(() => {
  if (!task.value) return null
  const rp = task.value.ref_parsed
  if (!rp || !rp.type || !rp.value) return null
  const v = encodeURIComponent(rp.value)
  const nfEnc = encodeURIComponent(task.value.nf)
  const verEnc = encodeURIComponent(task.value.version)
  switch (rp.type) {
    case 'MMLCommand':
      return { to: `/command-graph/${nfEnc}/${verEnc}/${v}`, label: '命令图谱', value: rp.value }
    case 'Feature':
    case 'SubFeature':
      return { to: `/feature-graph/${nfEnc}/${verEnc}/feature/${v}`, label: '特性图谱', value: rp.value }
    case 'ConfigurationSolution':
      return { to: null, label: '配置方案', value: rp.value }
    default:
      return null
  }
})

// ===== 工具函数 =====
function lastColonSegment(s?: string): string {
  if (!s) return ''
  const parts = s.split(':')
  return parts[parts.length - 1] || ''
}

function shortOnly(ref?: string): string {
  if (!ref) return ''
  return ref.split('@').pop() || ref
}

function formatValue(v: unknown): string {
  if (v === null || v === undefined) return '-'
  if (typeof v === 'string') return v
  if (typeof v === 'number' || typeof v === 'boolean') return String(v)
  try {
    return JSON.stringify(v)
  } catch {
    return String(v)
  }
}

function constraintExpression(c: unknown): string {
  if (!c || typeof c !== 'object') return ''
  const obj = c as Record<string, unknown>
  // 常见字段：expression / description / template
  const expr = obj.expression ?? obj.description ?? obj.template
  if (typeof expr === 'string') return expr
  try {
    return JSON.stringify(c)
  } catch {
    return ''
  }
}

function truncate(s: string, n: number) {
  if (!s) return ''
  return s.length > n ? s.slice(0, n) + '...' : s
}

// tag 配色（与 TaskList 对齐）
type TagType = 'primary' | 'success' | 'warning' | 'info' | 'danger'
function layerTagType(layer: string): TagType {
  switch ((layer || '').toLowerCase()) {
    case 'atom': return 'primary'
    case 'compound': return 'success'
    case 'feature': return 'warning'
    case 'solution': return 'info'
    case 'generalized': return 'danger'
    default: return 'info'
  }
}
function statusTagType(status: string): TagType {
  switch ((status || '').toLowerCase()) {
    case 'active': return 'success'
    case 'inferred': return 'warning'
    case 'draft': return 'info'
    default: return 'info'
  }
}
function severityTagType(severity: string): TagType {
  switch ((severity || '').toLowerCase()) {
    case 'critical':
    case 'error': return 'danger'
    case 'warning':
    case 'warn': return 'warning'
    case 'info': return 'info'
    case 'success': return 'success'
    default: return 'info'
  }
}

async function loadTask() {
  loading.value = true
  error.value = ''
  try {
    const data = await fetchJson(taskGraphApi.task(nf.value, version.value, taskId.value)) as TaskDetailResp & { error?: string }
    task.value = data && !data.error ? data : null
  } catch (e) {
    task.value = null
    error.value = '加载任务详情失败：' + (e instanceof Error ? e.message : String(e))
  } finally {
    loading.value = false
  }
}

watch([nf, version, taskId], loadTask)
onMounted(loadTask)
</script>

<style scoped>
.tg-detail {
  max-width: 1100px;
}

/* Hero */
.tg-hero-detail {
  margin-bottom: var(--space-5);
  padding-bottom: var(--space-4);
  border-bottom: 1px solid var(--border);
}
.tg-hero-id {
  font-family: var(--font-mono);
  font-size: var(--text-sm);
  font-weight: 600;
  color: var(--accent);
}
.tg-hero-name {
  font-size: var(--text-2xl, 24px);
  font-weight: 700;
  line-height: 1.3;
  margin: var(--space-1) 0 var(--space-2);
  color: var(--text-primary);
}
.tg-hero-tags {
  display: flex;
  align-items: center;
  gap: var(--space-2);
  flex-wrap: wrap;
}
.tg-hero-nfver {
  font-family: var(--font-mono);
  font-size: var(--text-xs);
  color: var(--text-tertiary);
  margin-left: var(--space-2);
}

/* 分节（参考 CommandDetail 的 summary-section 风格）*/
.summary-section {
  margin-bottom: var(--space-6);
}
.summary-section-title {
  font-size: var(--text-2xs);
  color: var(--text-tertiary);
  text-transform: uppercase;
  letter-spacing: 0.08em;
  font-weight: 600;
  margin-bottom: var(--space-3);
  padding-bottom: var(--space-2);
  border-bottom: 1px solid var(--border);
}

.tg-field-content {
  font-size: var(--text-sm);
  color: var(--text-secondary);
  line-height: 1.7;
}

/* 跨图谱链接 */
.tg-cross-link {
  display: inline-flex;
  align-items: center;
  gap: var(--space-2);
  color: var(--accent);
  text-decoration: none;
  font-size: var(--text-sm);
  font-weight: 500;
}
.tg-cross-link:hover {
  text-decoration: underline;
}
.tg-cross-plain {
  font-size: var(--text-sm);
  color: var(--text-secondary);
}
.tg-cross-value {
  font-family: var(--font-mono);
  font-size: var(--text-xs);
  color: var(--text-primary);
}

/* 基础字段网格 */
.tg-field-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: var(--space-3) var(--space-6);
  margin-bottom: var(--space-3);
}
.tg-field-row {
  display: flex;
  flex-direction: column;
  gap: 2px;
  min-width: 0;
}
.tg-field-label {
  font-size: var(--text-2xs);
  color: var(--text-tertiary);
  text-transform: uppercase;
  letter-spacing: 0.06em;
  font-weight: 600;
}
.tg-field-value {
  font-size: var(--text-sm);
  color: var(--text-primary);
  word-break: break-word;
}
.tg-mono {
  font-family: var(--font-mono);
  font-size: var(--text-xs);
}

.tg-notes {
  margin-top: var(--space-3);
}
.tg-notes-pre {
  margin: var(--space-2) 0 0;
  padding: var(--space-3);
  background: var(--bg-page);
  border: 1px solid var(--border);
  border-radius: var(--radius, 6px);
  font-family: var(--font-mono);
  font-size: var(--text-xs);
  line-height: 1.6;
  color: var(--text-secondary);
  white-space: pre-wrap;
  word-break: break-word;
  max-height: 280px;
  overflow-y: auto;
}

/* 关系 */
.tg-relations {
  display: flex;
  flex-direction: column;
  gap: var(--space-2);
}
.tg-rel-row {
  display: flex;
  align-items: center;
  flex-wrap: wrap;
  gap: var(--space-2);
  padding: var(--space-2) var(--space-3);
  background: var(--bg-page);
  border-radius: var(--radius, 6px);
  font-size: var(--text-xs);
}
.tg-rel-node {
  color: var(--accent);
  text-decoration: none;
  font-weight: 500;
  display: inline-flex;
  align-items: baseline;
  gap: 4px;
}
.tg-rel-node:hover {
  text-decoration: underline;
}
.tg-rel-node--muted {
  color: var(--text-tertiary);
  font-weight: 400;
  cursor: default;
}
.tg-rel-layer {
  font-family: var(--font-mono);
  font-size: var(--text-2xs);
  color: var(--text-tertiary);
  font-weight: 400;
}
.tg-rel-arrow {
  font-family: var(--font-mono);
  color: var(--text-tertiary);
}
.tg-rel-cond {
  font-family: var(--font-mono);
}
.tg-rel-prop {
  color: var(--text-secondary);
  font-style: italic;
}

/* 作为端点的边 */
.tg-endpoint-relations {
  margin-top: var(--space-3);
  padding-top: var(--space-3);
  border-top: 1px dashed var(--border);
}
.tg-endpoint-label {
  font-size: var(--text-2xs);
  color: var(--text-tertiary);
  text-transform: uppercase;
  letter-spacing: 0.06em;
  font-weight: 600;
  margin-bottom: var(--space-2);
}
.tg-rel-direction {
  color: var(--accent);
  font-weight: 600;
  margin-right: 2px;
}

.tg-detail-error {
  padding: var(--space-6) 0;
}

/* parents */
.tg-parents {
  margin-top: var(--space-4);
  padding-top: var(--space-3);
  border-top: 1px dashed var(--border);
}
.tg-parents-list {
  display: flex;
  flex-wrap: wrap;
  gap: var(--space-2);
  margin-top: var(--space-2);
}
.tg-parent-pill {
  display: inline-flex;
  align-items: baseline;
  gap: 4px;
  padding: 3px 10px;
  background: var(--accent-soft);
  color: var(--accent);
  border-radius: 999px;
  text-decoration: none;
  font-size: var(--text-xs);
  font-weight: 500;
}
.tg-parent-pill:hover {
  text-decoration: underline;
}
.tg-parent-layer {
  font-family: var(--font-mono);
  font-size: var(--text-2xs);
  color: var(--text-tertiary);
}

/* DP 卡片 */
.tg-dps {
  display: flex;
  flex-direction: column;
  gap: var(--space-4);
}
.tg-dp-card {
  border: 1px solid var(--border);
  border-left: 3px solid #7c3aed;
  border-radius: var(--radius-lg, 10px);
  padding: var(--space-4) var(--space-5);
  background: var(--bg-card);
}
.tg-dp-head {
  display: flex;
  align-items: center;
  gap: var(--space-3);
  margin-bottom: var(--space-3);
}
.tg-dp-name {
  font-size: var(--text-sm);
  font-weight: 600;
  color: var(--text-primary);
}
.tg-dp-id {
  color: var(--text-tertiary);
  margin-left: auto;
}
.tg-dp-options {
  display: flex;
  flex-direction: column;
  gap: var(--space-3);
}
.tg-dp-option {
  padding: var(--space-2) var(--space-3);
  background: var(--bg-page);
  border-radius: var(--radius, 6px);
}
.tg-dp-option-head {
  display: flex;
  align-items: baseline;
  gap: var(--space-2);
  margin-bottom: var(--space-2);
}
.tg-dp-option-id {
  color: #7c3aed;
  font-weight: 600;
}
.tg-dp-option-name {
  font-size: var(--text-sm);
  color: var(--text-primary);
}
.tg-value-cell {
  color: var(--text-secondary);
  word-break: break-all;
}
.tg-impact-detail {
  font-size: var(--text-xs);
  color: var(--text-secondary);
  word-break: break-word;
}
.tg-constraint-cell {
  color: var(--text-tertiary);
  font-size: var(--text-xs);
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

/* 证据 */
.tg-evidence {
  display: flex;
  flex-direction: column;
  gap: 4px;
}
.tg-evidence-item {
  font-size: var(--text-xs);
  color: var(--text-secondary);
  padding: 4px var(--space-3);
  background: var(--bg-page);
  border-radius: var(--radius, 6px);
  word-break: break-all;
}

.tg-empty-inline {
  color: var(--text-tertiary);
  font-size: var(--text-sm);
  padding: var(--space-2) 0;
}

.tg-notfound {
  height: calc(100vh - var(--navbar-height));
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--text-tertiary);
  font-size: var(--text-sm);
}
</style>
