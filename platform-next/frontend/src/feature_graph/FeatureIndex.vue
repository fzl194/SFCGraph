<template>
  <div class="page-container">
    <div class="page-inner">
      <!-- Header -->
      <div class="section-header">
        <div>
          <h1 class="section-title">特性图谱</h1>
          <p class="section-desc">产品特性管理与审查</p>
        </div>
      </div>

      <!-- Sub-tabs -->
      <el-tabs v-model="activeTab" class="feature-main-tabs" @tab-change="onTabChange">
        <el-tab-pane label="特性总表" name="list" />
        <el-tab-pane label="特性关系" name="relations" />
        <el-tab-pane label="特性 License" name="licenses" />
      </el-tabs>

      <!-- Child route content -->
      <router-view />
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, computed, watch } from 'vue'
import { useRouter, useRoute } from 'vue-router'

const router = useRouter()
const route = useRoute()

function nameToTab(name: string | symbol | undefined): string {
  if (name === 'feature-relations') return 'relations'
  if (name === 'feature-licenses') return 'licenses'
  return 'list'
}

const activeTab = ref(nameToTab(route.name))

function onTabChange(name: string) {
  if (name === 'relations') {
    router.push({ name: 'feature-relations' })
  } else if (name === 'licenses') {
    router.push({ name: 'feature-licenses' })
  } else {
    router.push({ name: 'feature-list' })
  }
}

watch(() => route.name, (name) => {
  activeTab.value = nameToTab(name)
})
</script>
