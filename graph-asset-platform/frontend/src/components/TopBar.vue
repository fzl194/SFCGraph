<template>
  <div class="topbar">
    <div class="left">
      <span class="title">图谱资产管理平台</span>
      <el-tag v-if="!loadingStats" size="small" type="info">
        对象 {{ totalObjects }} · 边 {{ edgeCount }}
      </el-tag>
    </div>

    <div class="center">
      <VersionSelector ref="versionRef" :refresh-key="refreshKey" @change="onVersionChange" />
    </div>

    <div class="right">
      <el-upload
        :show-file-list="false"
        :before-upload="onUpload"
        accept=".zip"
      >
        <el-button size="small" type="primary" :loading="uploading">
          导入 bundle
        </el-button>
      </el-upload>
      <el-dropdown @command="onExport" trigger="click">
        <el-button size="small">导出 ▾</el-button>
        <template #dropdown>
          <el-dropdown-menu>
            <el-dropdown-item command="all">全部</el-dropdown-item>
            <el-dropdown-item
              v-for="nf in nfs"
              :key="nf"
              :command="nf"
            >
              {{ nf }}
            </el-dropdown-item>
          </el-dropdown-menu>
        </template>
      </el-dropdown>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, computed } from 'vue'
import { ElMessage } from 'element-plus'
import VersionSelector from './VersionSelector.vue'
import {
  stats as fetchStats,
  importBundle,
  exportUrl,
  type Stats,
  type ImportResult,
} from '../api'

const emit = defineEmits<{
  // 版本选择变更（selected: nf→version，空串=最新）
  (e: 'versionChange', selected: Record<string, string>): void
  // 导入成功：通知父级刷新索引/对象
  (e: 'imported', res: ImportResult): void
  // 当前选中的版本映射变化：给父级一个权威取值函数
}>()

const versionRef = ref<InstanceType<typeof VersionSelector> | null>(null)
const statsData = ref<Stats | null>(null)
const loadingStats = ref(false)
const uploading = ref(false)
const refreshKey = ref(0)

const totalObjects = computed(() =>
  statsData.value
    ? Object.values(statsData.value.object_counts_by_type).reduce((a, b) => a + b, 0)
    : 0,
)
const edgeCount = computed(() => statsData.value?.edge_count ?? 0)
const nfs = computed(() => statsData.value?.nfs ?? [])

async function loadStats() {
  loadingStats.value = true
  try {
    statsData.value = await fetchStats()
  } finally {
    loadingStats.value = false
  }
}

function onVersionChange(selected: Record<string, string>) {
  emit('versionChange', selected)
}

async function onUpload(file: File): Promise<boolean> {
  uploading.value = true
  try {
    const res = await importBundle(file)
    ElMessage.success(
      `导入完成：新增 ${res.added} · 更新 ${res.updated} · 跳过 ${res.skipped}` +
        (res.warnings.length ? ` · 警告 ${res.warnings.length}` : ''),
    )
    if (res.warnings.length) {
      console.warn('[import warnings]', res.warnings)
    }
    // 刷新统计 + 版本选择器
    await loadStats()
    refreshKey.value++
    emit('imported', res)
  } catch (e) {
    ElMessage.error('导入失败：' + (e instanceof Error ? e.message : String(e)))
  } finally {
    uploading.value = false
  }
  // 返回 false 阻止 el-upload 内置 ajax 上传
  return false
}

function onExport(cmd: string) {
  if (cmd === 'all') {
    window.open(exportUrl({}), '_blank')
    return
  }
  // cmd = nf；带上该 nf 当前选中的 version（若有）
  const ver = versionRef.value?.getVersionFor(cmd)
  window.open(exportUrl({ nf: cmd, version: ver }), '_blank')
}

// 父级可调 refresh() 强制刷新（如外部导入后）
function refresh() {
  loadStats()
  refreshKey.value++
}

defineExpose({ refresh, loadStats, versionRef })

// 初始加载统计
loadStats()
</script>

<style scoped>
.topbar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
  padding: 8px 16px;
  background: #fff;
  border-bottom: 1px solid #e4e7ed;
  box-shadow: 0 1px 4px rgba(0, 0, 0, 0.04);
  flex-wrap: wrap;
}
.left,
.right {
  display: flex;
  align-items: center;
  gap: 12px;
}
.center {
  flex: 1;
  display: flex;
  justify-content: center;
  min-width: 0;
}
.title {
  font-weight: 700;
  font-size: 15px;
  color: #303133;
  white-space: nowrap;
}
</style>
