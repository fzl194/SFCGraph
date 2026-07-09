<template>
  <div class="wiki-shell">
    <aside class="wiki-left">左树（待建）</aside>
    <section class="wiki-center">中区（待建）</section>
    <aside class="wiki-right">图谱（待建）</aside>
  </div>
</template>

<script setup lang="ts"></script>

<style scoped>
.wiki-shell { display: grid; grid-template-columns: 280px 1fr 1fr; height: calc(100vh - var(--navbar-height)); }
.wiki-left, .wiki-right { border-right: 1px solid var(--border); overflow: auto; padding: 12px; }
.wiki-center { overflow: auto; padding: 16px 24px; }
</style>
