<template>
  <div class="page-container">
    <div class="page-inner">
      <!-- 面包屑：统计 > {nf}@{version}（网元版本合并后单级）-->
      <el-breadcrumb v-if="nf && version" class="cg-breadcrumb" separator="/">
        <el-breadcrumb-item>
          <router-link :to="{ name: 'command-overview' }">统计</router-link>
        </el-breadcrumb-item>
        <el-breadcrumb-item>{{ nf }}@{{ version }}</el-breadcrumb-item>
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
