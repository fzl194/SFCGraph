<template>
  <div class="case-form">
    <h3 class="form-title">新建测试用例</h3>

    <div class="row">
      <div class="field flex2">
        <label>用例名称 <span class="req">*</span></label>
        <el-input v-model="name" placeholder="如：离线计费-基础开通" />
      </div>
      <div class="field">
        <label>slug（用例 ID 后缀）</label>
        <el-input v-model="slug" placeholder="留空自动生成（建议英文，如 charging-offline-basic）" />
      </div>
    </div>

    <div class="row">
      <div class="field">
        <label>业务域</label>
        <el-select v-model="domain" filterable allow-create default-first-option clearable
          placeholder="选或输入新域（空=未分类）" class="sel">
          <el-option v-for="d in domainOptions" :key="d" :label="d" :value="d" />
        </el-select>
      </div>
      <div class="field">
        <label>场景</label>
        <el-select v-model="scenario" filterable allow-create default-first-option clearable
          placeholder="选或输入新场景" :disabled="!domain" class="sel">
          <el-option v-for="s in scenarioOptions" :key="s" :label="s" :value="s" />
        </el-select>
      </div>
      <div class="field">
        <label>编写人</label>
        <el-input v-model="author" placeholder="如 SA-zhang" />
      </div>
    </div>

    <div class="field">
      <label>意图描述（业务诉求）<span class="req">*</span></label>
      <el-input v-model="intent" type="textarea" :rows="5" placeholder="这个用例测什么：业务诉求、网元/版本、关注点……" />
    </div>

    <div class="row">
      <div class="field flex2">
        <label>输入配置 txt（任意数量，可选）</label>
        <input ref="inputFileEl" type="file" multiple class="file-input" @change="onInputFiles" />
        <div v-if="inputFiles.length" class="file-list">
          <span v-for="f in inputFiles" :key="f.name" class="file-chip">{{ f.name }}</span>
        </div>
      </div>
      <div class="field flex2">
        <label>参考输出配置 txt（任意数量，可选）</label>
        <input ref="refFileEl" type="file" multiple class="file-input" @change="onRefFiles" />
        <div v-if="referenceFiles.length" class="file-list">
          <span v-for="f in referenceFiles" :key="f.name" class="file-chip">{{ f.name }}</span>
        </div>
      </div>
    </div>

    <div v-if="error" class="err">{{ error }}</div>
    <div class="form-actions">
      <el-button @click="$emit('cancel')">取消</el-button>
      <el-button type="primary" :loading="submitting" :disabled="!name.trim() || !intent.trim()" @click="submit">
        建用例
      </el-button>
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed, onMounted, ref, watch } from 'vue'
import { ElInput, ElSelect, ElOption, ElButton } from 'element-plus'
import { createCase, testsStats, type CaseDetail, type TestStats } from '../api'

const emit = defineEmits<{ created: [c: CaseDetail]; cancel: [] }>()

const name = ref('')
const slug = ref('')
const domain = ref('')
const scenario = ref('')
const author = ref('')
const intent = ref('')
const inputFiles = ref<File[]>([])
const referenceFiles = ref<File[]>([])
const inputFileEl = ref<HTMLInputElement | null>(null)
const refFileEl = ref<HTMLInputElement | null>(null)
const submitting = ref(false)
const error = ref('')
const stats = ref<TestStats | null>(null)

const domainOptions = computed(() => (stats.value ? Object.keys(stats.value.cases_by_domain) : []))
const scenarioOptions = computed(() => {
  if (!stats.value || !domain.value) return [] as string[]
  const prefix = domain.value + '/'
  return Object.keys(stats.value.cases_by_domain_scenario)
    .filter((k) => k.startsWith(prefix))
    .map((k) => k.slice(prefix.length))
})

async function loadStats(): Promise<void> {
  try {
    stats.value = await testsStats()
  } catch {
    /* 容错：拿不到就纯手输 */
  }
}

// 切域清场景
watch(domain, () => {
  scenario.value = ''
})

onMounted(loadStats)

function onInputFiles(e: Event): void {
  inputFiles.value = Array.from((e.target as HTMLInputElement).files || [])
}
function onRefFiles(e: Event): void {
  referenceFiles.value = Array.from((e.target as HTMLInputElement).files || [])
}

async function submit(): Promise<void> {
  submitting.value = true
  error.value = ''
  try {
    const c = await createCase({
      name: name.value.trim(),
      intent: intent.value,
      domain: domain.value.trim() || undefined,
      scenario: scenario.value.trim() || undefined,
      slug: slug.value.trim() || undefined,
      author: author.value.trim() || undefined,
      inputFiles: inputFiles.value,
      referenceFiles: referenceFiles.value,
    })
    emit('created', c)
  } catch (e) {
    error.value = e instanceof Error ? e.message : String(e)
  } finally {
    submitting.value = false
  }
}
</script>

<style scoped>
.case-form {
  background: var(--bg-sunken);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  padding: var(--space-5);
  margin-bottom: var(--space-5);
}
.form-title {
  font-size: 14px;
  font-weight: 600;
  color: var(--text);
  margin: 0 0 var(--space-4);
}
.row {
  display: flex;
  gap: var(--space-3);
  margin-bottom: var(--space-3);
}
.field {
  flex: 1;
}
.flex2 {
  flex: 2;
}
.field label {
  display: block;
  font-size: 12.5px;
  font-weight: 600;
  color: var(--text-muted);
  margin-bottom: 6px;
}
.sel {
  width: 100%;
}
.req {
  color: #dc2626;
}
.file-input {
  font-size: 12.5px;
  width: 100%;
}
.file-list {
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
  margin-top: 6px;
}
.file-chip {
  background: var(--bg-elev);
  border: 1px solid var(--border);
  border-radius: 4px;
  padding: 2px 8px;
  font-size: 11.5px;
  color: var(--text-muted);
  font-family: var(--mono);
}
.err {
  color: #dc2626;
  font-size: 12.5px;
  margin: var(--space-2) 0;
}
.form-actions {
  display: flex;
  justify-content: flex-end;
  gap: var(--space-2);
  margin-top: var(--space-3);
}
</style>
