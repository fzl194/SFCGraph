<template>
  <div class="review-form">
    <h3 class="form-title">{{ review ? '修改审查' : '添加审查' }}</h3>

    <div class="field">
      <label>结论 <span class="req">*</span></label>
      <el-radio-group v-model="verdict">
        <el-radio value="通过">通过</el-radio>
        <el-radio value="不通过">不通过</el-radio>
        <el-radio value="部分通过">部分通过</el-radio>
      </el-radio-group>
    </div>

    <div class="field">
      <label>审查人</label>
      <el-input v-model="reviewer" placeholder="如 human:zhang（可空）" />
    </div>

    <div class="field">
      <label>总结</label>
      <el-input v-model="conclusion" type="textarea" :rows="2" placeholder="整体结论（可选）" />
    </div>

    <div class="field">
      <div class="problems-head">
        <label>问题清单 <span class="hint">每条带归因——喂给定位 Agent</span></label>
        <el-button size="small" @click="addProblem">+ 加问题</el-button>
      </div>
      <div v-for="(p, i) in problems" :key="i" class="problem-row">
        <div class="pr-top">
          <el-input v-model="p.desc" type="textarea" :rows="2" placeholder="问题描述" />
          <el-button class="pr-del" size="small" type="danger" link @click="delProblem(i)">删除</el-button>
        </div>
        <div class="pr-fields">
          <el-select v-model="p.attribution" placeholder="归因" class="pr-attr">
            <el-option label="图谱知识" value="图谱知识" />
            <el-option label="配置流程" value="配置流程" />
            <el-option label="其他" value="其他" />
          </el-select>
          <el-autocomplete
            v-model="p.object"
            :fetch-suggestions="fetchSugg"
            placeholder="涉及对象（图谱 ID，可搜索）"
            clearable
            class="pr-obj"
          >
            <template #default="{ item }">
              <div class="sugg">
                <span class="sugg-name">{{ item.name }}</span>
                <span class="sugg-id">{{ item.value }}</span>
              </div>
            </template>
          </el-autocomplete>
        </div>
      </div>
      <div v-if="problems.length === 0" class="no-problem">无问题（点上方"+ 加问题"）</div>
    </div>

    <div v-if="error" class="err">{{ error }}</div>
    <div class="form-actions">
      <el-button @click="$emit('cancel')">取消</el-button>
      <el-button type="primary" :loading="submitting" @click="submit">
        {{ review ? '保存修改' : '提交审查' }}
      </el-button>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import {
  ElInput,
  ElRadio,
  ElRadioGroup,
  ElSelect,
  ElOption,
  ElAutocomplete,
  ElButton,
} from 'element-plus'
import {
  createReview,
  updateReview,
  suggestObjects,
  type ReviewDetail,
  type ReviewWriteBody,
} from '../api'

const props = defineProps<{ runId: string; review?: ReviewDetail | null }>()
const emit = defineEmits<{ submitted: []; cancel: [] }>()

const verdict = ref(props.review?.verdict || '不通过')
const reviewer = ref(props.review?.reviewer || '')
const conclusion = ref('')
const problems = ref(
  props.review?.problems.map((p) => ({ desc: p.description, attribution: p.attribution, object: p.object })) || [
    { desc: '', attribution: '图谱知识', object: '' },
  ],
)
const submitting = ref(false)
const error = ref('')

function addProblem(): void {
  problems.value.push({ desc: '', attribution: '图谱知识', object: '' })
}
function delProblem(i: number): void {
  problems.value.splice(i, 1)
}

async function fetchSugg(
  query: string,
  cb: (items: { value: string; name: string }[]) => void,
): Promise<void> {
  const res = await suggestObjects(query)
  cb(res.map((r) => ({ value: r.id, name: r.name })))
}

async function submit(): Promise<void> {
  submitting.value = true
  error.value = ''
  try {
    const body: ReviewWriteBody = {
      run: props.runId,
      reviewer: reviewer.value || undefined,
      verdict: verdict.value,
      conclusion: conclusion.value || undefined,
      problems: problems.value
        .filter((p) => p.desc.trim() !== '')
        .map((p) => ({ desc: p.desc, attribution: p.attribution, object: p.object })),
    }
    if (props.review) {
      await updateReview(props.review.id, body)
    } else {
      await createReview(body)
    }
    emit('submitted')
  } catch (e) {
    error.value = e instanceof Error ? e.message : String(e)
  } finally {
    submitting.value = false
  }
}
</script>

<style scoped>
.review-form {
  background: var(--bg-sunken);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  padding: var(--space-5);
  margin-top: var(--space-3);
}
.form-title {
  font-size: 14px;
  font-weight: 600;
  color: var(--text);
  margin: 0 0 var(--space-4);
}
.field {
  margin-bottom: var(--space-4);
}
label {
  display: block;
  font-size: 12.5px;
  font-weight: 600;
  color: var(--text-muted);
  margin-bottom: 6px;
}
.req {
  color: #dc2626;
}
.hint {
  font-weight: 400;
  color: var(--text-faint);
  margin-left: 4px;
}
.problems-head {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 6px;
}
.problems-head label {
  margin-bottom: 0;
}
.problem-row {
  background: var(--bg-elev);
  border: 1px solid var(--border);
  border-radius: var(--radius-sm);
  padding: var(--space-3);
  margin-bottom: 8px;
}
.pr-top {
  display: flex;
  gap: var(--space-2);
  align-items: flex-start;
}
.pr-del {
  flex-shrink: 0;
  margin-top: 2px;
}
.pr-fields {
  display: flex;
  gap: var(--space-2);
  margin-top: 8px;
}
.pr-attr {
  width: 150px;
  flex-shrink: 0;
}
.pr-obj {
  flex: 1;
}
.no-problem {
  font-size: 12.5px;
  color: var(--text-faint);
  padding: var(--space-2);
}
.sugg {
  display: flex;
  justify-content: space-between;
  gap: 12px;
  line-height: 1.4;
}
.sugg-name {
  color: var(--text);
}
.sugg-id {
  color: var(--text-faint);
  font-size: 11px;
  font-family: var(--mono);
}
.err {
  color: #dc2626;
  font-size: 12.5px;
  margin-bottom: var(--space-3);
}
.form-actions {
  display: flex;
  justify-content: flex-end;
  gap: var(--space-2);
}
</style>
