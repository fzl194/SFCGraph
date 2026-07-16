<template>
  <AppHeader />
  <main class="app-main">
    <router-view v-slot="{ Component }">
      <transition name="view-fade" mode="out-in">
        <component :is="Component" />
      </transition>
    </router-view>
  </main>
</template>

<script setup lang="ts">
import { onMounted, ref } from 'vue'
import AppHeader from './components/AppHeader.vue'
import { stats, type Stats } from './api'

// 全站 stats（AppHeader chip 用）。挂载时拉一次，上传后由 UploadView 触发刷新。
const globalStats = ref<Stats | null>(null)
const statsLoading = ref(false)

async function refreshStats(): Promise<void> {
  statsLoading.value = true
  try {
    globalStats.value = await stats()
  } catch {
    // 静默：header chip 容错
  } finally {
    statsLoading.value = false
  }
}

// 暴露给全局以便子组件刷新（上传后调用）
;(window as unknown as { __refreshStats?: () => Promise<void> }).__refreshStats =
  refreshStats

onMounted(refreshStats)
</script>

<style scoped>
.app-main {
  flex: 1;
  min-height: 0;
  overflow: hidden;
}

.view-fade-enter-active,
.view-fade-leave-active {
  transition: opacity var(--dur) var(--ease), transform var(--dur) var(--ease);
}

.view-fade-enter-from {
  opacity: 0;
  transform: translateY(4px);
}

.view-fade-leave-to {
  opacity: 0;
}
</style>
