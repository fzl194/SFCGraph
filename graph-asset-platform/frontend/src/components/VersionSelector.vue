<template>
  <div class="version-selector">
    <span class="label">版本：</span>
    <div v-if="loading" class="muted">加载中…</div>
    <div v-else-if="!nfs.length" class="muted">（无数据）</div>
    <div v-else class="nf-list">
      <div v-for="nf in nfs" :key="nf" class="nf-item">
        <span class="nf-name">{{ nf }}</span>
        <el-select
          v-model="selected[nf]"
          size="small"
          placeholder="最新"
          clearable
          style="width: 120px"
          @change="(v: string) => onChange(nf, v)"
        >
          <el-option label="（最新）" value="" />
          <el-option
            v-for="v in versionsPerNf[nf] || []"
            :key="v"
            :label="v"
            :value="v"
          />
        </el-select>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, computed, onMounted, watch } from 'vue'
import { stats as fetchStats, type Stats } from '../api'

// 按 nf 选版本，emit 变更给父级。父级据当前对象 nf 取对应版本驱动 ?version=。
const emit = defineEmits<{
  (e: 'change', selected: Record<string, string>): void
}>()

const props = defineProps<{
  // 父级强制重置（如导入后刷新）
  refreshKey?: number
}>()

const loading = ref(false)
const data = ref<Stats | null>(null)
// 每个 nf 的选中版本：空字符串=最新（不传 version 参数）
const selected = ref<Record<string, string>>({})

const nfs = computed(() => data.value?.nfs ?? [])
const versionsPerNf = computed(
  () => data.value?.versions_per_nf ?? {},
)

async function load() {
  loading.value = true
  try {
    data.value = await fetchStats()
    // 初始化 selected：默认全部"最新"（空串）
    const next: Record<string, string> = {}
    for (const nf of data.value.nfs) next[nf] = ''
    selected.value = next
    emit('change', { ...next })
  } finally {
    loading.value = false
  }
}

function onChange(nf: string, v: string) {
  selected.value = { ...selected.value, [nf]: v || '' }
  emit('change', { ...selected.value })
}

watch(
  () => props.refreshKey,
  () => {
    load()
  },
)

onMounted(load)

// 暴露给父级：取某 nf 的选中版本（空串=未选=用最新）
defineExpose({
  getVersionFor(nf: string | undefined): string | undefined {
    if (!nf) return undefined
    const v = selected.value[nf]
    return v && v.length > 0 ? v : undefined
  },
})
</script>

<style scoped>
.version-selector {
  display: flex;
  align-items: center;
  gap: 8px;
  flex-wrap: wrap;
}
.label {
  font-weight: 600;
  color: #606266;
}
.muted {
  color: #909399;
  font-size: 13px;
}
.nf-list {
  display: flex;
  gap: 12px;
  flex-wrap: wrap;
}
.nf-item {
  display: flex;
  align-items: center;
  gap: 6px;
}
.nf-name {
  font-size: 13px;
  color: #303133;
}
</style>
