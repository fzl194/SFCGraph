<template>
  <section class="telemetry-section stagger-in">
    <header class="ts-head">
      <div>
        <h2 class="ts-title">SKILL 取用频次</h2>
        <p class="ts-sub">只统计 SKILL 的 /domains + /md（按对象）</p>
      </div>
      <div class="ts-controls">
        <el-select v-model="days" size="small" @change="load">
          <el-option :value="7" label="近 7 天" />
          <el-option :value="30" label="近 30 天" />
          <el-option :value="90" label="近 90 天" />
        </el-select>
        <span class="ts-total">共 {{ formatNum(stats?.total ?? 0) }} 次取用</span>
      </div>
    </header>

    <div v-if="err" class="ts-err">{{ err }}</div>
    <div v-else-if="!stats || stats.total === 0" class="ts-empty">
      暂无取用记录（SKILL 调用 /domains 或 /md 后此处展示）。
    </div>

    <div v-else class="ts-grid">
      <!-- 按 type 横条 -->
      <div class="ts-block">
        <div class="block-title">按类型</div>
        <div class="type-rows">
          <div v-for="r in typeRows" :key="r.type" class="type-row">
            <span class="type-label">{{ typeLabel(r.type) }}</span>
            <div class="type-bar-wrap">
              <div class="type-bar" :style="{ width: r.pct + '%' }" />
            </div>
            <span class="type-count mono">{{ formatNum(r.count) }}</span>
          </div>
        </div>
      </div>

      <!-- 热门对象 top-N -->
      <div class="ts-block">
        <div class="block-title">热门对象 Top {{ stats.top_ids.length }}</div>
        <ol class="top-list">
          <li v-for="(t, i) in stats.top_ids" :key="t.id" class="top-item">
            <span class="top-rank">{{ i + 1 }}</span>
            <span class="top-id mono" :title="t.id">{{ t.id }}</span>
            <span class="top-type">{{ typeLabel(t.type) }}</span>
            <span class="top-count mono">{{ formatNum(t.count) }}</span>
          </li>
        </ol>
      </div>

      <!-- 按用户（SKILL） -->
      <div class="ts-block">
        <div class="block-title">按用户（SKILL）</div>
        <div class="type-rows">
          <div v-for="(c, u) in stats.by_user" :key="u" class="type-row">
            <span class="type-label">{{ u }}</span>
            <span class="type-count mono">{{ formatNum(c) }}</span>
          </div>
        </div>
      </div>

      <!-- 按工号（SKILL 使用者） -->
      <div class="ts-block">
        <div class="block-title">按工号（SKILL 使用者）</div>
        <div class="type-rows">
          <div v-for="(c, op) in stats.by_operator" :key="op" class="type-row">
            <span class="type-label">{{ op }}</span>
            <span class="type-count mono">{{ formatNum(c) }}</span>
          </div>
        </div>
      </div>

      <!-- 时间趋势（SVG 折线；数据点 <2 时退化提示） -->
      <div class="ts-block ts-block-wide">
        <div class="block-title">时间趋势（按日）</div>
        <svg v-if="stats.timeline.length > 1" class="trend" :viewBox="`0 0 ${W} ${H}`" preserveAspectRatio="none">
          <polyline :points="linePoints" fill="none" :stroke="accent" stroke-width="2" />
        </svg>
        <div v-else class="trend-empty">数据点不足（需 ≥2 天记录才画折线）</div>
        <div v-if="stats.timeline.length > 1" class="trend-axis">
          <span>{{ stats.timeline[0]?.date ?? '' }}</span>
          <span>{{ stats.timeline[stats.timeline.length - 1]?.date ?? '' }}</span>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup lang="ts">
import { computed, onMounted, ref } from 'vue'
import { ElSelect, ElOption } from 'element-plus'
import { fetchTelemetryStats, type TelemetryStats } from '../api'

const stats = ref<TelemetryStats | null>(null)
const days = ref(30)
const err = ref('')
const accent = '#4f46e5'
const W = 600
const H = 120

const TYPE_LABELS: Record<string, string> = {
  MMLCommand: '命令', ConfigObject: '配置对象', Feature: '特性', License: 'License',
  AtomTask: '原子Task', CompoundTask: '步骤Task', FeatureTask: '特性Task', Task: '任务',
  BusinessDomain: '业务域', NetworkScenario: '场景', ConfigurationSolution: '方案',
}

function typeLabel(t: string): string {
  return TYPE_LABELS[t] ?? t
}
function formatNum(n: number): string {
  return n.toLocaleString('zh-CN')
}

const typeRows = computed(() => {
  if (!stats.value) return []
  const entries = Object.entries(stats.value.by_type).sort((a, b) => b[1] - a[1])
  const max = entries[0]?.[1] || 1
  return entries.map(([type, count]) => ({ type, count, pct: Math.round((count / max) * 100) }))
})

const linePoints = computed(() => {
  if (!stats.value || stats.value.timeline.length === 0) return ''
  const tl = stats.value.timeline
  const max = Math.max(...tl.map((p) => p.count), 1)
  const n = tl.length
  return tl
    .map((p, i) => {
      const x = n === 1 ? W / 2 : (i / (n - 1)) * W
      const y = H - (p.count / max) * (H - 10) - 5
      return `${x.toFixed(1)},${y.toFixed(1)}`
    })
    .join(' ')
})

async function load(): Promise<void> {
  err.value = ''
  try {
    stats.value = await fetchTelemetryStats(days.value)
  } catch (e: unknown) {
    err.value = e instanceof Error ? e.message : String(e)
    stats.value = null
  }
}

onMounted(load)
</script>

<style scoped>
.telemetry-section {
  display: flex;
  flex-direction: column;
  gap: var(--space-4);
  padding: var(--space-5);
  background: var(--bg-elev);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  box-shadow: var(--shadow-sm);
}
.ts-head {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  gap: var(--space-3);
}
.ts-title {
  font-size: 16px;
  font-weight: 700;
  margin: 0;
}
.ts-sub {
  font-size: 12.5px;
  color: var(--text-muted);
  margin: 2px 0 0;
}
.ts-controls {
  display: flex;
  align-items: center;
  gap: var(--space-3);
}
.ts-total {
  font-size: 12.5px;
  color: var(--text-muted);
}
.ts-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: var(--space-5);
}
.ts-block-wide {
  grid-column: 1 / -1;
}
.block-title {
  font-size: 12px;
  font-weight: 600;
  color: var(--text-faint);
  text-transform: uppercase;
  letter-spacing: 0.04em;
  margin-bottom: var(--space-2);
}
.type-rows {
  display: flex;
  flex-direction: column;
  gap: 6px;
}
.type-row {
  display: grid;
  grid-template-columns: 70px 1fr 50px;
  align-items: center;
  gap: 8px;
  font-size: 12.5px;
}
.type-bar-wrap {
  height: 8px;
  background: var(--bg-sunken);
  border-radius: 999px;
  overflow: hidden;
}
.type-bar {
  height: 100%;
  background: var(--accent);
  border-radius: 999px;
}
.type-count {
  text-align: right;
  color: var(--text);
  font-weight: 600;
}
.top-list {
  list-style: none;
  margin: 0;
  padding: 0;
  display: flex;
  flex-direction: column;
  gap: 4px;
}
.top-item {
  display: grid;
  grid-template-columns: 24px 1fr auto auto;
  align-items: center;
  gap: 8px;
  font-size: 12.5px;
  padding: 3px 0;
}
.top-rank {
  color: var(--text-faint);
  font-weight: 600;
}
.top-id {
  color: var(--text);
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}
.top-type {
  font-size: 11px;
  color: var(--text-muted);
  background: var(--bg-sunken);
  padding: 1px 6px;
  border-radius: 4px;
}
.top-count {
  color: var(--text);
  font-weight: 600;
}
.trend {
  width: 100%;
  height: 120px;
  background: var(--bg-sunken);
  border-radius: var(--radius-sm);
}
.trend-empty {
  height: 120px;
  display: grid;
  place-items: center;
  font-size: 12px;
  color: var(--text-faint);
  background: var(--bg-sunken);
  border-radius: var(--radius-sm);
}
.trend-axis {
  display: flex;
  justify-content: space-between;
  font-size: 11px;
  color: var(--text-faint);
  margin-top: 4px;
}
.ts-empty,
.ts-err {
  font-size: 13px;
  color: var(--text-muted);
  padding: var(--space-3) 0;
}
.ts-err {
  color: var(--danger, #dc2626);
}
</style>
