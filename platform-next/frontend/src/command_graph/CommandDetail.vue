<template>
  <div v-if="command" class="cmd-split" :class="{ 'is-dragging': dragging }" ref="splitRef">
    <!-- LEFT: 对象 tab -->
    <section class="cmd-pane cmd-pane--left" :style="leftStyle">
      <el-tabs v-model="leftTab" class="cmd-tabs">
        <el-tab-pane label="MMLCommand" name="mmlcommand">
          <header class="cmd-hero">
            <div class="cmd-hero-id">{{ command.command_name }}</div>
            <h1 class="cmd-hero-name">{{ command.command_name_zh }}</h1>
            <div class="cmd-hero-tags">
              <el-tag size="small" effect="plain">{{ command.nf }}</el-tag>
              <el-tag size="small" effect="plain" type="info">{{ command.version || '-' }}</el-tag>
            </div>
          </header>

          <!-- 数据驱动：record 所有非空字段一律渲染成分区 -->
          <div v-for="section in sections" :key="section.key" class="summary-section">
            <div class="summary-section-title">{{ section.label }}</div>
            <div class="cmd-field-content" v-html="section.html"></div>
          </div>
          <div v-if="!sections.length" class="cmd-pane-empty">无抽取字段</div>
        </el-tab-pane>

        <el-tab-pane label="参数" name="parameters">
          <CommandParameters
            v-if="activatedTabs.parameters"
            :nf="nf"
            :command-name="commandName"
            :version="version"
          />
        </el-tab-pane>

        <el-tab-pane label="图谱" name="graph">
          <CommandGraph
            v-if="activatedTabs.graph"
            :nf="nf"
            :command-name="commandName"
            :version="version"
          />
        </el-tab-pane>

        <el-tab-pane label="配置对象" name="object">
          <div v-if="commandObject" class="cmd-object">
            <header class="cmd-hero">
              <div class="cmd-hero-id">{{ commandObject.object_name }}</div>
              <h1 class="cmd-hero-name">{{ commandObject.object_name_zh || commandObject.object_name }}</h1>
              <div class="cmd-hero-tags">
                <el-tag size="small" effect="plain">{{ commandObject.object_kind }}</el-tag>
                <el-tag size="small" effect="plain" type="info">{{ commandObject.nf }}</el-tag>
              </div>
            </header>
            <div v-for="section in objectSections" :key="section.key" class="summary-section">
              <div class="summary-section-title">{{ section.label }}</div>
              <div class="cmd-field-content" v-html="section.html"></div>
            </div>
          </div>
          <div v-else-if="!loadingObject" class="cmd-pane-empty">该命令未关联配置对象</div>
          <div v-else class="cmd-pane-empty">加载中…</div>
        </el-tab-pane>
      </el-tabs>
    </section>

    <!-- 分隔条：拖拽调宽 + 双向折叠（不能同时收起）-->
    <div
      class="cmd-divider"
      :title="canDrag ? '拖拽调整宽度' : ''"
      @mousedown="startDrag"
    >
      <!-- 双栏时：可收起任一侧（箭头=分隔条将移动的方向）-->
      <button
        v-if="!leftCollapsed && !rightCollapsed"
        class="cmd-toggle"
        title="收起左侧"
        @click="leftCollapsed = true"
      >‹</button>
      <button
        v-if="!leftCollapsed && !rightCollapsed"
        class="cmd-toggle"
        title="收起右侧"
        @click="rightCollapsed = true"
      >›</button>
      <!-- 单侧收起时：只显示对应“展开”按钮，保证一定能回到双栏，且不会同时收起 -->
      <button
        v-if="leftCollapsed"
        class="cmd-toggle"
        title="展开左侧"
        @click="leftCollapsed = false"
      >›</button>
      <button
        v-if="rightCollapsed"
        class="cmd-toggle"
        title="展开右侧"
        @click="rightCollapsed = false"
      >‹</button>
    </div>

    <!-- RIGHT: 原始文档，常驻显示，独立滚动 -->
    <section class="cmd-pane cmd-pane--right" :style="rightStyle">
      <div class="cmd-pane-head">原始文档</div>
      <div class="cmd-pane-body">
        <DocViewer
          v-if="mdContent"
          :content="mdContent"
          :file-path="evidencePath"
          api-base="command-graph"
          :show-title="true"
        />
        <div v-else class="cmd-pane-empty">{{ evidencePath ? '加载中…' : '无关联文档' }}</div>
      </div>
    </section>
  </div>

  <div v-else class="cmd-notfound">
    <span v-if="loading">加载中…</span>
    <span v-else>命令未找到：{{ nf }} / {{ commandName }}</span>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, computed, watch } from 'vue'
import { useRoute } from 'vue-router'
import { commandGraphApi, fetchJson } from '../api'
import DocViewer from '../shared/DocViewer.vue'
import { renderMarkdown } from '../shared/markdown'
import CommandParameters from './CommandParameters.vue'
import CommandGraph from './CommandGraph.vue'

const route = useRoute()
const nf = computed(() => route.params.nf as string)
const version = computed(() => route.params.version as string)
const commandName = computed(() => route.params.commandName as string)

const loading = ref(true)
const command = ref<any>(null)
const mdContent = ref('')
const leftTab = ref('mmlcommand')
// 懒加载：首次切到对应 tab 才挂载子组件（v-if 控制首次挂载才请求，避免进详情即拉全量）
const activatedTabs = ref({ parameters: false, graph: false, object: false })
const commandObject = ref<any>(null)
const loadingObject = ref(false)

// 切 tab 时按需激活（仅置 true，不回退；切命令时重置）
watch(leftTab, (tab) => {
  if (tab === 'parameters') activatedTabs.value.parameters = true
  if (tab === 'graph') activatedTabs.value.graph = true
  if (tab === 'object' && !commandObject.value && !loadingObject.value) loadObject()
})

async function loadObject() {
  loadingObject.value = true
  try {
    const data = await fetchJson(commandGraphApi.commandObject(nf.value, commandName.value, version.value))
    commandObject.value = data.object || null
  } finally {
    loadingObject.value = false
  }
}

// ===== 可拖拽 + 可折叠的双栏 =====
const splitRef = ref<HTMLElement>()
const leftPct = ref(60)              // 左侧占比（两栏都展开时）；左侧是重点，默认更宽
const leftCollapsed = ref(false)
const rightCollapsed = ref(false)
const dragging = ref(false)
const canDrag = computed(() => !leftCollapsed.value && !rightCollapsed.value)

const leftStyle = computed(() => {
  if (leftCollapsed.value) return { flex: '0 0 0%', minWidth: '0' }
  if (rightCollapsed.value) return { flex: '1 1 0%' }   // 右栏收起 → 左栏占满
  return { flex: `0 0 ${leftPct.value}%` }
})
const rightStyle = computed(() => {
  if (rightCollapsed.value) return { flex: '0 0 0%', minWidth: '0' }
  return { flex: '1 1 0%' }
})

function startDrag(e: MouseEvent) {
  // 点折叠按钮不触发拖拽
  if ((e.target as HTMLElement)?.closest('.cmd-toggle')) return
  if (!canDrag.value) return
  e.preventDefault()
  dragging.value = true
  const container = splitRef.value
  if (!container) return
  const onMove = (ev: MouseEvent) => {
    const rect = container.getBoundingClientRect()
    let pct = ((ev.clientX - rect.left) / rect.width) * 100
    pct = Math.max(20, Math.min(85, pct))   // 自由调整范围 20%~85%（更窄/更宽用折叠按钮）
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

// 原始 md 路径取自 source_evidence_ids[0]（md_path 已从提取中移除，二者原为同一值）
const evidencePath = computed(() => command.value?.source_evidence_ids?.[0] || '')

// 不隐藏任何字段：record 里所有非空 key 一律渲染成分区。
// LABEL_MAP 仅做装饰性中文标题；未命中的 key 直接用原 key 作标题
// （所以新增字段无需改前端代码即可自动出现）。
const LABEL_MAP: Record<string, string> = {
  command_id: '命令ID',
  command_name: '命令名',
  command_name_zh: '中文名',
  nf: '网元',
  version: '版本',
  verb: '动词',
  object_keyword: '对象关键字',
  command_category: '命令分类',
  is_dangerous: '是否高危',
  command_function: '命令功能',
  notes: '注意事项',
  permission_text: '操作用户权限',
  permission_groups: '权限组',
  parameter_description: '参数说明',
  usage_examples: '使用实例',
  output_description: '输出结果说明',
  output_ref_command: '输出引用命令',
  reference_info: '参考信息',
  applicable_nf: '适用网元',
  max_records: '最大记录数',
  effect_mode: '生效方式',
  spec_threshold: '超阈值告警',
  initial_values: '系统初始值',
  output_fields: '输出字段表',
  category_path: '分类路径',
  status: '状态',
  source_evidence_ids: '来源证据',
  // ConfigObject 字段
  object_id: '对象ID',
  object_name: '对象名',
  object_name_zh: '中文名',
  object_kind: '对象类型',
  identifier_parameters: '定位参数',
  uniqueness_keys: '唯一性键',
  attribute_names: '属性名',
}

function isNonEmpty(v: any): boolean {
  if (v === null || v === undefined) return false
  if (typeof v === 'string') return v.trim() !== ''
  if (Array.isArray(v)) return v.length > 0
  if (typeof v === 'object') return Object.keys(v).length > 0
  return true // bool / number（含 false / 0）视为有值，展示
}

/** 按 §4.2 规则把任意取值归一化为已渲染的 HTML。 */
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

const sections = computed(() => {
  if (!command.value) return []
  const out: { key: string; label: string; html: string }[] = []
  for (const key of Object.keys(command.value)) {
    const value = command.value[key]
    if (!isNonEmpty(value)) continue
    out.push({ key, label: LABEL_MAP[key] || key, html: renderValue(value) })
  }
  return out
})

const objectSections = computed(() => {
  if (!commandObject.value) return []
  const out: { key: string; label: string; html: string }[] = []
  for (const key of Object.keys(commandObject.value)) {
    const value = commandObject.value[key]
    if (!isNonEmpty(value)) continue
    out.push({ key, label: LABEL_MAP[key] || key, html: renderValue(value) })
  }
  return out
})

async function loadAll() {
  loading.value = true
  mdContent.value = ''
  try {
    const data = await fetchJson(commandGraphApi.command(nf.value, commandName.value, version.value))
    command.value = data.error ? null : data

    if (command.value?.source_evidence_ids?.length) {
      const mdData = await fetchJson(commandGraphApi.commandMd(nf.value, commandName.value, version.value))
      mdContent.value = mdData.content || ''
    }
  } finally {
    loading.value = false
  }
}

watch([nf, commandName, version], () => {
  leftTab.value = 'mmlcommand'
  // 切换命令重置懒加载标记 + 配置对象，新命令首次切 tab 再挂载
  activatedTabs.value = { parameters: false, graph: false, object: false }
  commandObject.value = null
  loadAll()
})

onMounted(loadAll)
</script>

<style scoped>
/* ===== 双栏拆分布局（复用项目既有 token，不引入新视觉体系）===== */
.cmd-split {
  display: flex;
  height: calc(100vh - var(--navbar-height));
  overflow: hidden;
}
.cmd-pane {
  display: flex;
  flex-direction: column;
  overflow: hidden;
  min-width: 0;
  transition: flex-basis 0.18s ease, flex-grow 0.18s ease;
}
.cmd-split.is-dragging .cmd-pane {
  transition: none;                 /* 拖拽时关闭过渡，避免滞后 */
}
.cmd-pane--left {
  background: var(--bg-card);
}
.cmd-pane--right {
  background: var(--bg-card);
}

/* 分隔条：拖拽调宽 + 双向折叠按钮（不能同时收起）*/
.cmd-divider {
  flex: 0 0 8px;
  position: relative;
  background: var(--border);
  cursor: col-resize;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 28px;
  z-index: 5;
  user-select: none;
}
.cmd-divider:hover,
.cmd-split.is-dragging .cmd-divider {
  background: var(--accent);
}
.cmd-toggle {
  width: 20px;
  height: 20px;
  border: 1px solid var(--border);
  background: var(--bg-card);
  color: var(--text-secondary);
  border-radius: 3px;
  font-size: 14px;
  line-height: 1;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 0;
  flex-shrink: 0;
}
.cmd-toggle:hover {
  color: var(--accent);
  border-color: var(--accent);
}

/* 左栏：tab 头固定，tab 内容独立滚动 */
.cmd-tabs {
  flex: 1;
  display: flex;
  flex-direction: column;
  overflow: hidden;
}
.cmd-tabs :deep(.el-tabs__header) {
  flex-shrink: 0;
  margin: 0;
  padding: 0 var(--space-5);
  background: var(--bg-card);
}
.cmd-tabs :deep(.el-tabs__nav-wrap)::after {
  background-color: var(--border);
}
.cmd-tabs :deep(.el-tabs__content) {
  flex: 1;
  overflow-y: auto;
  overflow-x: hidden;
}
.cmd-tabs :deep(.el-tab-pane) {
  padding: var(--space-5) var(--space-5) var(--space-8);
}

/* 右栏：标题固定，正文独立滚动 */
.cmd-pane-head {
  flex-shrink: 0;
  padding: var(--space-3) var(--space-6);
  font-size: var(--text-2xs);
  color: var(--text-tertiary);
  text-transform: uppercase;
  letter-spacing: 0.08em;
  border-bottom: 1px solid var(--border);
}
.cmd-pane-body {
  flex: 1;
  overflow-y: auto;
  padding: var(--space-5) var(--space-6);
}

/* 左栏顶部命令标识（紧凑 hero）*/
.cmd-hero {
  margin-bottom: var(--space-5);
  padding-bottom: var(--space-4);
  border-bottom: 1px solid var(--border);
}
.cmd-hero-id {
  font-family: var(--font-mono);
  font-size: var(--text-sm);
  font-weight: 600;
  color: var(--accent);
}
.cmd-hero-name {
  font-size: var(--text-xl);
  font-weight: 700;
  line-height: 1.3;
  margin: var(--space-1) 0 var(--space-2);
  color: var(--text-primary);
}
.cmd-hero-tags {
  display: flex;
  gap: var(--space-2);
}

.cmd-pane-empty {
  padding: 80px 20px;
  text-align: center;
  color: var(--text-tertiary);
  font-size: var(--text-sm);
}
.cmd-notfound {
  height: calc(100vh - var(--navbar-height));
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--text-tertiary);
  font-size: var(--text-sm);
}

/* 字段正文渲染（表格/代码块）*/
.cmd-field-content {
  font-size: var(--text-sm);
  color: var(--text-secondary);
  line-height: 1.7;
}
.cmd-field-content :deep(table) {
  border-collapse: collapse;
  width: 100%;
  margin: 8px 0;
}
.cmd-field-content :deep(th),
.cmd-field-content :deep(td) {
  border: 1px solid var(--border);
  padding: 6px 10px;
  text-align: left;
  font-size: var(--text-xs);
}
.cmd-field-content :deep(th) {
  background: var(--bg-page);
}
.cmd-field-content :deep(pre) {
  background: var(--bg-page);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  padding: 10px 14px;
  font-size: var(--text-xs);
  line-height: 1.6;
  overflow-x: auto;
}
.cmd-field-content :deep(code) {
  font-family: var(--font-mono);
}
</style>
