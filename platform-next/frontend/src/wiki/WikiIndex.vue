<template>
  <div class="wiki-shell">
    <aside class="wiki-left"><CategoryTree @select="go" /></aside>
    <section class="wiki-center">中区（待 Task 10）</section>
    <aside class="wiki-right">图谱（待 Task 11）</aside>
  </div>
</template>

<script setup lang="ts">
import { useRouter } from 'vue-router'
import CategoryTree from './CategoryTree.vue'
const router = useRouter()
function go(path: string) { router.push(`/graph-overview/a/${path}`) }
</script>

<style scoped>
.wiki-shell { display: grid; grid-template-columns: 300px 1fr 1fr; height: calc(100vh - var(--navbar-height)); }
.wiki-left { border-right: 1px solid var(--border); overflow: auto; padding: 10px; }
.wiki-center { overflow: auto; padding: 16px 24px; }
.wiki-right { border-left: 1px solid var(--border); overflow: hidden; padding: 10px; }
</style>
