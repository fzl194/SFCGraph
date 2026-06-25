<template>
  <div class="page-container">
    <div class="page-inner">
      <div class="section-header">
        <div>
          <h1 class="section-title">命令图谱</h1>
          <p class="section-desc">MML 命令管理与浏览</p>
        </div>
      </div>

      <!-- 面包屑：统计 > {nf} > {version}（未到的层级不显示）-->
      <el-breadcrumb v-if="nf || version" class="cg-breadcrumb" separator="/">
        <el-breadcrumb-item>
          <router-link :to="{ name: 'command-overview' }">统计</router-link>
        </el-breadcrumb-item>
        <el-breadcrumb-item v-if="nf">
          <router-link v-if="version" :to="{ name: 'command-versions', params: { nf } }">{{ nf }}</router-link>
          <span v-else>{{ nf }}</span>
        </el-breadcrumb-item>
        <el-breadcrumb-item v-if="version">{{ version }}</el-breadcrumb-item>
      </el-breadcrumb>

      <router-view />
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed } from 'vue'
import { useRoute } from 'vue-router'

const route = useRoute()
const nf = computed(() => (route.params.nf as string) || '')
const version = computed(() => (route.params.version as string) || '')
</script>

<style scoped>
.cg-breadcrumb {
  margin-bottom: var(--space-4);
}
.cg-breadcrumb a {
  color: var(--accent);
  text-decoration: none;
}
.cg-breadcrumb a:hover {
  text-decoration: underline;
}
</style>
