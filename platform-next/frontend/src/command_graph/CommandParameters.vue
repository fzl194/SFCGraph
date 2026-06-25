<template>
  <div v-loading="loading" class="cmd-params">
    <el-table
      v-if="parameters.length"
      :data="parameters"
      size="small"
      stripe
      style="width: 100%"
      row-key="parameter_id"
      :default-expand-all="false"
    >
      <el-table-column type="expand">
        <template #default="{ row }">
          <div class="param-detail">
            <div
              v-for="section in expandSections(row)"
              :key="section.key"
              class="param-detail-section"
            >
              <div class="param-detail-label">{{ section.label }}</div>
              <div class="param-detail-value" v-html="section.html"></div>
            </div>
          </div>
        </template>
      </el-table-column>

      <el-table-column prop="native_parameter_id" label="ID" width="70" sortable align="center">
        <template #default="{ row }">
          <span class="param-id-num">{{ row.native_parameter_id ?? '-' }}</span>
        </template>
      </el-table-column>
      <el-table-column prop="parameter_name" label="参数标识" width="200" sortable>
        <template #default="{ row }">
          <span class="param-id-cell">{{ row.parameter_name || '-' }}</span>
        </template>
      </el-table-column>
      <el-table-column prop="parameter_name_zh" label="中文名" min-width="140">
        <template #default="{ row }">
          <span class="param-name-cell">{{ row.parameter_name_zh || '-' }}</span>
        </template>
      </el-table-column>
      <el-table-column prop="data_type" label="类型" width="100">
        <template #default="{ row }">
          <el-tag v-if="row.data_type" size="small" effect="plain" type="info">{{ row.data_type }}</el-tag>
          <span v-else class="param-dim">-</span>
        </template>
      </el-table-column>
      <el-table-column label="必选" width="70" align="center">
        <template #default="{ row }">
          <el-tag v-if="isRequired(row)" size="small" type="danger" effect="dark">必</el-tag>
          <el-tag v-else size="small" effect="plain" type="info">否</el-tag>
        </template>
      </el-table-column>
      <el-table-column label="默认值" width="110">
        <template #default="{ row }">
          <span class="param-mono">{{ formatDefault(row) }}</span>
        </template>
      </el-table-column>
      <el-table-column label="取值范围" min-width="160">
        <template #default="{ row }">
          <span class="param-range">{{ formatRange(row) || '-' }}</span>
        </template>
      </el-table-column>
      <el-table-column label="说明摘要" min-width="240">
        <template #default="{ row }">
          <span class="param-desc">{{ truncate(row.description, 120) }}</span>
        </template>
      </el-table-column>
    </el-table>

    <div v-else-if="!loading" class="cmd-pane-empty">该命令无参数</div>
  </div>
</template>

<script setup lang="ts">
import { ref, watch, onMounted } from 'vue'
import { commandGraphApi, fetchJson } from '../api'
import { renderMarkdown } from '../shared/markdown'

interface Props {
  nf: string
  commandName: string
  version?: string
}
const props = defineProps<Props>()

const loading = ref(true)
const parameters = ref<any[]>([])

// 参数字段的中文标题装饰（未命中用原 key）
const LABEL_MAP: Record<string, string> = {
  parameter_id: '参数ID',
  parameter_name: '参数标识',
  parameter_name_zh: '中文名',
  data_type: '数据类型',
  required_mode: '必选模式',
  default_value: '默认值',
  min_value: '最小值',
  max_value: '最大值',
  value_range: '取值范围',
  enum_values: '枚举值',
  description: '说明',
  unit: '单位',
  length: '长度',
  is_array: '是否数组',
  array_dim: '数组维度',
  editable: '是否可编辑',
  scope: '作用域',
  effect_mode: '生效方式',
  restart_required: '是否需重启',
  related_object: '关联对象',
  related_field: '关联字段',
  validation_rule: '校验规则',
  example: '示例',
  source_evidence_ids: '来源证据',
  notes: '备注',
  condition_logic: '条件逻辑',
  condition_value: '条件值',
}

function isNonEmpty(v: any): boolean {
  if (v === null || v === undefined) return false
  if (typeof v === 'string') return v.trim() !== ''
  if (Array.isArray(v)) return v.length > 0
  if (typeof v === 'object') return Object.keys(v).length > 0
  return true // bool / number（含 false / 0）视为有值
}

function renderValue(v: any): string {
  if (Array.isArray(v)) {
    return v
      .map((el) =>
        renderMarkdown(
          el !== null && typeof el === 'object'
            ? '```json\n' + JSON.stringify(el, null, 2) + '\n```'
            : String(el)
        )
      )
      .join('\n')
  }
  if (v !== null && typeof v === 'object') {
    return renderMarkdown('```json\n' + JSON.stringify(v, null, 2) + '\n```')
  }
  if (typeof v === 'boolean') return renderMarkdown(v ? '是' : '否')
  if (typeof v === 'number') return renderMarkdown(String(v))
  return renderMarkdown(String(v))
}

/** 行展开：record 全部非空字段一律展示，未命中 LABEL_MAP 用原 key。 */
function expandSections(row: any): { key: string; label: string; html: string }[] {
  const out: { key: string; label: string; html: string }[] = []
  for (const key of Object.keys(row)) {
    const value = row[key]
    if (!isNonEmpty(value)) continue
    out.push({ key, label: LABEL_MAP[key] || key, html: renderValue(value) })
  }
  return out
}

function isRequired(row: any): boolean {
  const mode = String(row.required_mode ?? '').toLowerCase()
  if (!mode) return false
  return mode.includes('mandatory') || mode.includes('required') || mode === 'm' || mode === 'y' || mode === '是'
}

function formatDefault(row: any): string {
  if (row.default_value === null || row.default_value === undefined || row.default_value === '') return '-'
  return String(row.default_value)
}

function formatRange(row: any): string {
  if (row.value_range && String(row.value_range).trim()) return String(row.value_range)
  const hasMin = row.min_value !== null && row.min_value !== undefined && row.min_value !== ''
  const hasMax = row.max_value !== null && row.max_value !== undefined && row.max_value !== ''
  if (hasMin && hasMax) return `${row.min_value} ~ ${row.max_value}`
  if (hasMin) return `≥ ${row.min_value}`
  if (hasMax) return `≤ ${row.max_value}`
  return ''
}

function truncate(v: any, n: number): string {
  if (v === null || v === undefined) return '-'
  const s = String(v)
  return s.length > n ? s.slice(0, n) + '…' : s
}

async function load() {
  loading.value = true
  try {
    const data = await fetchJson(commandGraphApi.commandParameters(props.nf, props.commandName, props.version))
    // 按 native_parameter_id 从小到大排列（缺值排最后）
    const list = [...(data.parameters || [])]
    list.sort((a, b) => {
      const va = Number(a?.native_parameter_id)
      const vb = Number(b?.native_parameter_id)
      return (Number.isFinite(va) ? va : Infinity) - (Number.isFinite(vb) ? vb : Infinity)
    })
    parameters.value = list
  } catch {
    parameters.value = []
  } finally {
    loading.value = false
  }
}

watch(() => [props.nf, props.commandName, props.version], load)
onMounted(load)
</script>

<style scoped>
.cmd-params {
  min-height: 120px;
}

.param-id-cell {
  font-family: var(--font-mono);
  font-size: var(--text-xs);
  font-weight: 600;
  color: var(--accent);
}
.param-id-num {
  font-family: var(--font-mono);
  font-size: var(--text-xs);
  color: var(--text-tertiary);
}
.param-name-cell {
  font-size: var(--text-sm);
  color: var(--text-primary);
}
.param-mono {
  font-family: var(--font-mono);
  font-size: var(--text-xs);
  color: var(--text-secondary);
}
.param-range {
  font-family: var(--font-mono);
  font-size: var(--text-xs);
  color: var(--text-secondary);
}
.param-desc {
  font-size: var(--text-xs);
  color: var(--text-secondary);
  line-height: 1.5;
}
.param-dim {
  color: var(--text-tertiary);
}

/* 行展开详情 */
.param-detail {
  padding: var(--space-3) var(--space-5);
  background: var(--bg-page);
  border-top: 1px solid var(--border-light);
}
.param-detail-section {
  padding: var(--space-2) 0;
  border-bottom: 1px dashed var(--border-light);
}
.param-detail-section:last-child {
  border-bottom: none;
}
.param-detail-label {
  font-size: var(--text-2xs);
  color: var(--text-tertiary);
  text-transform: uppercase;
  letter-spacing: 0.06em;
  margin-bottom: var(--space-1);
}
.param-detail-value {
  font-size: var(--text-sm);
  color: var(--text-secondary);
  line-height: 1.7;
}
.param-detail-value :deep(table) {
  border-collapse: collapse;
  width: 100%;
  margin: 6px 0;
}
.param-detail-value :deep(th),
.param-detail-value :deep(td) {
  border: 1px solid var(--border);
  padding: 4px 8px;
  text-align: left;
  font-size: var(--text-xs);
}
.param-detail-value :deep(th) {
  background: var(--bg-card);
}
.param-detail-value :deep(pre) {
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  padding: 8px 12px;
  font-size: var(--text-xs);
  line-height: 1.5;
  overflow-x: auto;
}
.param-detail-value :deep(code) {
  font-family: var(--font-mono);
}

.cmd-pane-empty {
  padding: 80px 20px;
  text-align: center;
  color: var(--text-tertiary);
  font-size: var(--text-sm);
}
</style>
