<template>
  <div class="login-page">
    <form class="login-card" @submit.prevent="onSubmit">
      <h1 class="title">图谱资产</h1>
      <p class="sub">请输入用户名与访问 KEY</p>
      <input
        v-model="username"
        class="input"
        placeholder="用户名"
        autofocus
        autocomplete="username"
      />
      <input
        v-model="key"
        type="password"
        class="input"
        placeholder="API Key"
        autocomplete="current-password"
      />
      <div v-if="err" class="err">{{ err }}</div>
      <button type="submit" class="btn" :disabled="loading || !username.trim() || !key.trim()">
        {{ loading ? '验证中…' : '进入' }}
      </button>
    </form>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { setSession, type Session } from '../auth'
import { login } from '../api'

const username = ref('')
const key = ref('')
const err = ref('')
const loading = ref(false)

async function onSubmit(): Promise<void> {
  loading.value = true
  err.value = ''
  try {
    const u = await login(username.value.trim(), key.value.trim())
    setSession({ username: u.username, key: key.value.trim(), is_admin: u.is_admin } as Session)
    // 整页跳转，绕开 router 实例依赖
    window.location.assign('/')
  } catch (e: unknown) {
    err.value = e instanceof Error ? e.message : '登录失败'
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
