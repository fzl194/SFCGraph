<template>
  <div v-loading="loading" class="tg-overview">
    <el-alert
      v-if="error"
      :title="error"
      type="error"
      show-icon
      :closable="false"
      style="margin-bottom: var(--space-6)"
    />
    <!-- ===== 介绍大卡片：配置任务是啥 + 包含啥 ===== -->
    <section class="tg-hero">
      <div class="tg-hero-head">
        <h1 class="tg-hero-title">配置任务</h1>
        <p class="tg-hero-desc">
          云核心网配置的<strong>动态编排层</strong>——把 <strong>Task</strong>（generalized → feature → compound → atom 层级）+ <strong>TaskRule</strong> + <strong>DecisionPoint</strong>（含 impacts）+ <strong>TaskParameterBinding</strong> + <strong>TaskRelation</strong> 结构化，承接特性意图到命令编排的中间桥梁。
        </p>
      </div>

      <!-- 3 对象：Task / Rule / DP -->
      <div class="tg-hero-objects">
        <div class="tg-obj">
          <div class="tg-obj-glyph tg-glyph-box" aria-hidden="true">□</div>
          <div class="tg-obj-body">
            <div class="tg-obj-name">任务<span class="tg-obj-type">Task</span></div>
            <div class="tg-obj-desc">配置意图单元：层级（atom/compound/feature/solution/generalized）+ 意图 + ref 跨图谱锚点</div>
          </div>
          <div class="tg-obj-count">{{ stats.total_tasks ?? '-' }}</div>
        </div>
        <div class="tg-obj">
          <div class="tg-obj-glyph tg-glyph-ellipse" aria-hidden="true">○</div>
          <div class="tg-obj-body">
            <div class="tg-obj-name">规则<span class="tg-obj-type">TaskRule</span></div>
            <div class="tg-obj-desc">任务约束：severity / constraint 表达式 / 命中条件</div>
          </div>
          <div class="tg-obj-count">{{ stats.total_rules ?? '-' }}</div>
        </div>
        <div class="tg-obj">
          <div class="tg-obj-glyph tg-glyph-diamond" aria-hidden="true">◇</div>
          <div class="tg-obj-body">
            <div class="tg-obj-name">决策点<span class="tg-obj-type">DecisionPoint</span></div>
            <div class="tg-obj-desc">分支决策：options × impacts（影响 task / command / parameter）</div>
          </div>
          <div class="tg-obj-count tg-obj-count--dp">{{ stats.total_dps ?? '-' }}</div>
        </div>
      </div>

      <!-- 关系示意 -->
      <div class="tg-hero-relations">
        <span class="tg-rel-label">编排层级</span>
        <span class="tg-rel"><span class="tg-rel-glyph">▲</span>generalized<span class="tg-rel-arrow">→</span>feature<span class="tg-rel-arrow">→</span>compound<span class="tg-rel-arrow">→</span><span class="tg-rel-glyph">●</span>atom</span>
        <span class="tg-rel"><span class="tg-rel-glyph">◇</span>DP<span class="tg-rel-arrow tg-rel-arrow--dp">— impacts →</span>task / command / parameter</span>
      </div>
    </section>

    <!-- ===== 网元版本条目 ===== -->
    <div class="tg-section-title">
      <h2>网元版本</h2>
      <span class="tg-section-sub">{{ neVersions.length }} 个 · 点击进入任务列表</span>
    </div>
    <div v-if="neVersions.length" class="tg-nv-grid">
      <div
        v-for="nv in neVersions"
        :key="nv.nf + '@' + nv.version"
        class="tg-nv-card"
        @click="goList(nv.nf, nv.version)"
      >
        <div class="tg-nv-id">
          <span class="tg-nv-nf">{{ nv.nf }}</span><span class="tg-nv-at">@</span><span class="tg-nv-ver">{{ nv.version }}</span>
        </div>
        <div class="tg-nv-meta">
          <span class="tg-pill tg-pill--task">{{ nv.task_count }} 任务</span>
          <span
            v-for="(count, layer) in nv.layers"
            :key="layer"
            class="tg-pill tg-pill--layer"
          >{{ layer }}: {{ count }}</span>
        </div>
        <span class="tg-nv-arrow" aria-hidden="true">→</span>
      </div>
    </div>
    <div v-else-if="!loading" class="tg-empty">暂无任务数据</div>
  </div>
</template>

<script setup lang="ts">
import { ref, computed, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { taskGraphApi, fetchJson } from '../api'

// ===== 后端响应类型（结构类型，避免 any）=====
interface NeVersion {
  nf: string
  version: string
  task_count: number
  layers: Record<string, number>
}
interface TaskStats {
  total_tasks?: number
  total_rules?: number
  total_dps?: number
  by_layer?: Record<string, number>
  ne_versions?: NeVersion[]
}

const router = useRouter()
const loading = ref(true)
const error = ref('')
const stats = ref<TaskStats>({})

const neVersions = computed<NeVersion[]>(() => stats.value.ne_versions || [])

function goList(nf: string, version: string) {
  router.push({ name: 'task-list', params: { nf, version } })
}

onMounted(async () => {
  try {
    stats.value = await fetchJson(taskGraphApi.stats)
  } catch (e) {
    error.value = '加载统计数据失败：' + (e instanceof Error ? e.message : String(e))
  } finally {
    loading.value = false
  }
})
</script>

<style scoped>
/* ===== 介绍大卡片：大留白 + 氛围背景 ===== */
.tg-hero {
  background:
    radial-gradient(120% 80% at 100% 0%, rgba(8, 145, 178, 0.06), transparent 60%),
    radial-gradient(100% 60% at 0% 100%, rgba(124, 58, 237, 0.05), transparent 55%),
    var(--bg-card);
  border: 1px solid var(--border);
  border-radius: var(--radius-lg, 14px);
  padding: var(--space-10) var(--space-10) var(--space-8);
  margin-bottom: var(--space-10);
}
.tg-hero-head {
  margin-bottom: var(--space-8);
}
.tg-hero-title {
  font-size: var(--text-3xl, 30px);
  font-weight: 700;
  letter-spacing: -0.02em;
  margin: 0 0 var(--space-3);
  color: var(--text-primary);
}
.tg-hero-desc {
  margin: 0;
  font-size: var(--text-sm);
  color: var(--text-secondary);
  line-height: 1.75;
}
.tg-hero-desc strong {
  color: var(--text-primary);
  font-weight: 600;
}

/* 3 对象：纯排版，无边框，靠网格间距分隔 */
.tg-hero-objects {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: var(--space-8);
  padding: var(--space-6) 0;
  border-top: 1px solid var(--border);
  border-bottom: 1px solid var(--border);
  margin-bottom: var(--space-6);
}
.tg-obj {
  display: flex;
  align-items: center;
  gap: var(--space-4);
  padding: 0 var(--space-2);
  min-width: 0;
}
.tg-obj-glyph {
  flex-shrink: 0;
  width: 44px;
  height: 44px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 26px;
  line-height: 1;
}
.tg-glyph-box {
  color: var(--accent);
}
.tg-glyph-ellipse {
  color: var(--accent);
  border: 1.5px solid var(--accent);
  border-radius: 50%;
}
.tg-glyph-diamond {
  color: #7c3aed;
}
.tg-obj-body {
  flex: 1;
  min-width: 0;
}
.tg-obj-name {
  font-size: var(--text-base);
  font-weight: 600;
  color: var(--text-primary);
  line-height: 1.4;
}
.tg-obj-type {
  font-family: var(--font-mono);
  font-size: var(--text-xs);
  color: var(--text-tertiary);
  font-weight: 400;
  margin-left: var(--space-2);
}
.tg-obj-desc {
  font-size: var(--text-xs);
  color: var(--text-tertiary);
  margin-top: 3px;
  line-height: 1.6;
}
.tg-obj-count {
  font-family: var(--font-mono);
  font-size: var(--text-xl);
  font-weight: 700;
  color: var(--accent);
  flex-shrink: 0;
  letter-spacing: -0.02em;
}
.tg-obj-count--dp {
  color: #7c3aed;
}

/* 关系示意 */
.tg-hero-relations {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: var(--space-3) var(--space-6);
}
.tg-rel-label {
  font-size: var(--text-2xs);
  color: var(--text-tertiary);
  text-transform: uppercase;
  letter-spacing: 0.1em;
  font-weight: 600;
}
.tg-rel {
  font-family: var(--font-mono);
  font-size: var(--text-xs);
  color: var(--text-secondary);
  display: inline-flex;
  align-items: center;
  gap: 6px;
}
.tg-rel-glyph {
  color: var(--accent);
  font-size: var(--text-sm);
}
.tg-rel-arrow {
  color: var(--text-tertiary);
}
.tg-rel-arrow--dp {
  color: #7c3aed;
}

/* ===== 网元版本条目 ===== */
.tg-section-title {
  display: flex;
  align-items: baseline;
  gap: var(--space-3);
  margin-bottom: var(--space-5);
}
.tg-section-title h2 {
  font-size: var(--text-xl);
  font-weight: 600;
  margin: 0;
  color: var(--text-primary);
}
.tg-section-sub {
  font-size: var(--text-xs);
  color: var(--text-tertiary);
}
.tg-nv-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
  gap: var(--space-4);
}
.tg-nv-card {
  position: relative;
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-left: 3px solid var(--accent);
  border-radius: var(--radius-lg, 12px);
  padding: var(--space-5) var(--space-12) var(--space-5) var(--space-6);
  cursor: pointer;
  transition: transform 0.18s ease, box-shadow 0.18s ease, border-color 0.18s ease;
}
.tg-nv-card:hover {
  border-color: var(--accent);
  box-shadow: var(--shadow-card);
  transform: translateY(-1px);
}
.tg-nv-id {
  font-family: var(--font-mono);
  font-size: var(--text-lg);
  font-weight: 600;
  margin-bottom: var(--space-3);
  letter-spacing: -0.01em;
}
.tg-nv-nf { color: var(--text-primary); }
.tg-nv-at { color: var(--text-tertiary); margin: 0 1px; }
.tg-nv-ver { color: var(--accent); }
.tg-nv-meta {
  display: flex;
  flex-wrap: wrap;
  gap: var(--space-2);
}
.tg-pill {
  font-size: var(--text-2xs);
  padding: 2px 8px;
  border-radius: 999px;
  font-weight: 500;
}
.tg-pill--task { color: var(--accent); background: var(--accent-soft); }
.tg-pill--layer { color: var(--text-secondary); background: var(--bg-page); }
.tg-nv-arrow {
  position: absolute;
  right: var(--space-5);
  top: 50%;
  transform: translateY(-50%);
  color: var(--text-tertiary);
  transition: color 0.18s, transform 0.18s;
}
.tg-nv-card:hover .tg-nv-arrow {
  color: var(--accent);
  transform: translateY(-50%) translateX(2px);
}
.tg-empty {
  padding: var(--space-12);
  text-align: center;
  color: var(--text-tertiary);
}

@media (max-width: 900px) {
  .tg-hero { padding: var(--space-6) var(--space-5); }
  .tg-hero-objects {
    grid-template-columns: 1fr;
    gap: var(--space-5);
  }
  .tg-hero-relations { flex-direction: column; align-items: flex-start; }
}
</style>
