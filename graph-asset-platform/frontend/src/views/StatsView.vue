<template>
  <div class="stats-view">
    <div class="placeholder">
      <div class="ph-icon">
        <svg width="48" height="48" viewBox="0 0 24 24" fill="none">
          <rect x="3" y="11" width="4" height="9" rx="1" stroke="currentColor" stroke-width="1.6" />
          <rect x="10" y="6" width="4" height="14" rx="1" stroke="currentColor" stroke-width="1.6" />
          <rect x="17" y="3" width="4" height="17" rx="1" stroke="currentColor" stroke-width="1.6" />
        </svg>
      </div>
      <div class="ph-title">统计（待 C4 实现）</div>
      <div class="ph-sub">将展示命令层 / 特性层 / 任务层 / 业务层的对象计数卡片</div>
    </div>
  </div>
</template>

<script setup lang="ts"></script>

<style scoped>
.stats-view {
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
</style>
