<template>
  <div class="gop">
    <div v-if="modelValue.length" class="gop-picked">
      <span v-for="id in modelValue" :key="id" class="chip">
        <span class="chip-label">{{ labelOf(id) }}</span>
        <button class="chip-x" type="button" @click="remove(id)">×</button>
      </span>
    </div>
    <div class="gop-controls">
      <el-select v-model="layer" size="small" class="gop-sel" @change="onLayer">
        <el-option v-for="l in layers" :key="l" :label="l" :value="l" />
      </el-select>
      <el-select v-model="type" size="small" class="gop-sel" @change="search">
        <el-option v-for="t in types" :key="t" :label="t" :value="t" />
      </el-select>
      <el-input
        v-model="q"
        size="small"
        placeholder="搜 ID 或中文名"
        class="gop-q"
        clearable
        @input="onQ"
        @clear="results = []"
      />
    </div>
    <div v-if="loading" class="gop-hint">搜索中…</div>
    <div v-else-if="results.length" class="gop-results">
      <div
        v-for="r in results"
        :key="r.id"
        class="res"
        :class="{ picked: modelValue.includes(r.id) }"
        @click="toggle(r)"
      >
        <span class="res-name">{{ r.name }}</span>
        <span class="res-id">{{ r.id }}</span>
        <span v-if="modelValue.includes(r.id)" class="res-check">✓</span>
      </div>
    </div>
    <div v-else-if="q" class="gop-hint">无匹配</div>
    <div v-else class="gop-hint">选层 + 类型，输入关键词搜索后点结果添加</div>
  </div>
</template>

<script setup lang="ts">
import { computed, onMounted, ref } from 'vue'
import { ElSelect, ElOption, ElInput } from 'element-plus'
import { LAYER_TYPES, fetchGraphObjects, getNameMap } from '../api'

const props = defineProps<{ modelValue: string[] }>()
const emit = defineEmits<{ 'update:modelValue': [ids: string[]] }>()

const layers = Object.keys(LAYER_TYPES)
const layer = ref(layers[0])
const type = ref(LAYER_TYPES[layers[0]][0])
const types = computed(() => LAYER_TYPES[layer.value] || [])
const q = ref('')
const results = ref<{ id: string; name: string }[]>([])
const loading = ref(false)
const nameMap = ref<Record<string, string>>({})
let qTimer: ReturnType<typeof setTimeout> | null = null

function onLayer(): void {
  type.value = types.value[0] || ''
  q.value = ''
  results.value = []
}
function onQ(): void {
  if (qTimer) clearTimeout(qTimer)
  qTimer = setTimeout(search, 250)
}

async function search(): Promise<void> {
  if (!q.value.trim()) {
    results.value = []
    return
  }
  loading.value = true
  try {
    const res = await fetchGraphObjects(type.value, q.value.trim())
    results.value = res
    res.forEach((r) => {
      nameMap.value[r.id] = r.name
    })
  } finally {
    loading.value = false
  }
}

function labelOf(id: string): string {
  return nameMap.value[id] ? `${nameMap.value[id]}` : id
}

function toggle(r: { id: string; name: string }): void {
  nameMap.value[r.id] = r.name
  const cur = [...props.modelValue]
  const i = cur.indexOf(r.id)
  if (i >= 0) cur.splice(i, 1)
  else cur.push(r.id)
  emit('update:modelValue', cur)
}

function remove(id: string): void {
  emit('update:modelValue', props.modelValue.filter((x) => x !== id))
}

// 编辑模式预填：用图谱 names 给已选 id 补可读名
onMounted(async () => {
  try {
    const m = await getNameMap()
    props.modelValue.forEach((id) => {
      const n = m.get(id)
      if (n) nameMap.value[id] = n
    })
  } catch {
    /* 容错 */
  }
})
</script>

<style scoped>
.gop {
  width: 100%;
}
.gop-picked {
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
  margin-bottom: 8px;
}
.chip {
  display: inline-flex;
  align-items: center;
  gap: 4px;
  background: rgba(79, 70, 229, 0.1);
  border: 1px solid rgba(79, 70, 229, 0.3);
  color: #4338ca;
  border-radius: 999px;
  padding: 2px 6px 2px 10px;
  font-size: 11.5px;
}
.chip-label {
  max-width: 320px;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}
.chip-x {
  background: none;
  border: none;
  color: #4338ca;
  cursor: pointer;
  font-size: 14px;
  line-height: 1;
  padding: 0 2px;
}
.chip-x:hover {
  color: #dc2626;
}
.gop-controls {
  display: flex;
  gap: 6px;
}
.gop-sel {
  width: 110px;
  flex-shrink: 0;
}
.gop-q {
  flex: 1;
}
.gop-results {
  margin-top: 6px;
  max-height: 200px;
  overflow-y: auto;
  border: 1px solid var(--border);
  border-radius: var(--radius-sm);
  background: var(--bg-elev);
}
.res {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 5px 10px;
  cursor: pointer;
  font-size: 12px;
  border-bottom: 1px solid var(--border-faint, var(--border));
}
.res:last-child {
  border-bottom: none;
}
.res:hover {
  background: var(--bg-hover, var(--bg-sunken));
}
.res.picked {
  background: rgba(79, 70, 229, 0.06);
}
.res-name {
  color: var(--text);
  flex-shrink: 0;
  max-width: 40%;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}
.res-id {
  color: var(--text-faint);
  font-family: var(--mono);
  font-size: 11px;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}
.res-check {
  margin-left: auto;
  color: #4338ca;
  font-weight: 700;
}
.gop-hint {
  font-size: 11.5px;
  color: var(--text-faint);
  margin-top: 6px;
}
</style>
