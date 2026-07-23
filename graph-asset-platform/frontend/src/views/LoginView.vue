<template>
  <div class="login-page">
    <form class="login-card" @submit.prevent="onSubmit">
      <h1 class="title">图谱资产</h1>
      <p class="sub">请输入访问 KEY</p>
      <input
        v-model="key"
        type="password"
        class="input"
        placeholder="API Key"
        autofocus
        autocomplete="current-password"
      />
      <div v-if="err" class="err">{{ err }}</div>
      <button type="submit" class="btn" :disabled="loading || !key.trim()">
        {{ loading ? '验证中…' : '进入' }}
      </button>
    </form>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { setKey } from '../auth'
import { verifyKey } from '../api'

const key = ref('')
const err = ref('')
const loading = ref(false)

async function onSubmit(): Promise<void> {
  loading.value = true
  err.value = ''
  try {
    setKey(key.value.trim())
    await verifyKey() // 200 → KEY 对
    // 整页跳转，绕开 router 实例依赖，最稳
    window.location.assign('/')
  } catch {
    err.value = 'KEY 无效或后端不可达'
  } finally {
    loading.value = false
  }
}
</script>

<style scoped>
.login-page {
  height: 100%;
  display: grid;
  place-items: center;
  background: var(--bg-sunken);
}
.login-card {
  display: flex;
  flex-direction: column;
  gap: var(--space-3);
  width: 320px;
  padding: var(--space-7);
  background: var(--bg-elev);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  box-shadow: var(--shadow);
}
.title {
  font-family: var(--display);
  font-size: 22px;
  font-weight: 700;
  margin: 0;
  text-align: center;
}
.sub {
  font-size: 13px;
  color: var(--text-muted);
  text-align: center;
  margin: 0;
}
.input {
  padding: 9px 12px;
  font-size: 14px;
  border: 1px solid var(--border);
  border-radius: var(--radius-sm);
  background: var(--bg);
  color: var(--text);
}
.input:focus {
  outline: none;
  border-color: var(--accent);
}
.err {
  font-size: 12.5px;
  color: var(--danger, #dc2626);
}
.btn {
  padding: 9px 12px;
  font-size: 14px;
  font-weight: 600;
  color: #fff;
  background: var(--accent);
  border: none;
  border-radius: var(--radius-sm);
  cursor: pointer;
}
.btn:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}
</style>
