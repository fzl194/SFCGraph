<template>
  <div class="browser-view">
    <div class="placeholder">
      <div class="ph-icon">
        <svg width="48" height="48" viewBox="0 0 24 24" fill="none">
          <circle cx="6" cy="7" r="2.2" stroke="currentColor" stroke-width="1.6" />
          <circle cx="18" cy="7" r="2.2" stroke="currentColor" stroke-width="1.6" />
          <circle cx="12" cy="17" r="2.2" stroke="currentColor" stroke-width="1.6" />
          <path
            d="M7.8 8.3 16.2 8.3 M7 8.7 10.8 15 M17 8.7 13.2 15"
            stroke="currentColor"
            stroke-width="1.4"
            opacity="0.6"
          />
        </svg>
      </div>
      <div class="ph-title">图谱浏览（待 C3 实现）</div>
      <div class="ph-sub">
        当前激活层：<span class="mono">{{ activeLayer }}</span>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed } from 'vue'
import { useNav } from '../composables/useNav'

const { state } = useNav()
const activeLayer = computed(() => state.activeLayer)
</script>

<style scoped>
.browser-view {
  height: 100%;
  display: grid;
  place-items: center;
  padding: var(--space-8);
}

.placeholder {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: var(--space-3);
  text-align: center;
  color: var(--text-muted);
}

.ph-icon {
  color: var(--text-faint);
  opacity: 0.7;
}

.ph-title {
  font-family: var(--display);
  font-size: 18px;
  font-weight: 600;
  color: var(--text);
}

.ph-sub {
  font-size: 13px;
  color: var(--text-faint);
}

.mono {
  font-family: var(--mono);
  color: var(--accent);
}
</style>
