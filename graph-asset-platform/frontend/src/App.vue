<template>
  <router-view />
</template>

<script setup lang="ts">
// 根组件：仅承载 router-view。布局在 BrowserView 中组合。
</script>

<style>
html,
body,
#app {
  height: 100%;
  margin: 0;
  padding: 0;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto,
    'Helvetica Neue', Arial, 'PingFang SC', 'Microsoft YaHei', sans-serif;
  color: #2c3e50;
  background: #f5f7fa;
}
</style>
