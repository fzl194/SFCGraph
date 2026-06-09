<template>
  <div class="placeholder-page">
    <div class="placeholder-icon">{{ icon }}</div>
    <h2>{{ title }}</h2>
    <p>{{ desc }}</p>
  </div>
</template>

<script setup lang="ts">
defineProps<{
  title: string
  desc: string
  icon?: string
}>()
</script>
