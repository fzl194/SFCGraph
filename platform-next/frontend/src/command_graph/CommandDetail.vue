<template>
  <div v-if="command" class="detail-layout">
    <!-- Sidebar -->
    <div class="detail-sidebar">
      <div class="detail-sidebar-header">
        <button class="back-btn" @click="$router.push('/command-graph')">← 返回列表</button>
        <div class="sidebar-id">{{ command.command_name }}</div>
        <div class="sidebar-name">{{ command.command_name_zh }}</div>
      </div>

      <div class="sidebar-meta">
        <div class="sidebar-meta-row">
          <span class="sidebar-meta-label">产品</span>
          <el-tag size="small" effect="plain">{{ command.product }}</el-tag>
        </div>
        <div class="sidebar-meta-row">
          <span class="sidebar-meta-label">版本</span>
          <span class="sidebar-meta-value">{{ command.version }}</span>
        </div>
        <div class="sidebar-meta-row">
          <span class="sidebar-meta-label">分类</span>
          <span class="sidebar-meta-value" style="font-size: var(--text-xs)">{{ formatCategoryPath(command.category_path) }}</span>
        </div>
      </div>
    </div>

    <!-- Content -->
    <div class="detail-content">
      <div class="detail-content-inner">
        <el-tabs v-model="activeTab">
          <el-tab-pane label="抽取字段" name="fields">
            <!-- Hero header -->
            <div class="summary-hero">
              <div class="summary-hero-id">{{ command.command_name }}</div>
              <h1 class="summary-hero-name">{{ command.command_name_zh }}</h1>
              <div class="summary-hero-tags">
                <el-tag size="small" effect="plain">{{ command.product }}</el-tag>
                <el-tag size="small" effect="plain" type="info">{{ command.version }}</el-tag>
              </div>
            </div>

            <!-- Command Function -->
            <div v-if="command.command_function" class="summary-def">
              <div class="summary-def-label">命令功能</div>
              <p class="summary-def-text">{{ command.command_function }}</p>
            </div>

            <!-- Notes -->
            <div v-if="command.notes" class="summary-section">
              <div class="summary-section-title">注意事项</div>
              <p style="font-size: var(--text-sm); color: var(--text-secondary); line-height: 1.8; white-space: pre-line">{{ command.notes }}</p>
            </div>

            <!-- Permission -->
            <div v-if="command.permission" class="summary-section">
              <div class="summary-section-title">操作用户权限</div>
              <p style="font-size: var(--text-sm); color: var(--text-secondary); line-height: 1.6">{{ command.permission }}</p>
            </div>

            <!-- Examples -->
            <div v-if="command.examples" class="summary-section">
              <div class="summary-section-title">使用实例</div>
              <pre class="cmd-example">{{ command.examples }}</pre>
            </div>

            <!-- Raw fields table -->
            <div class="summary-section">
              <div class="summary-section-title">全部字段</div>
              <dl class="summary-dl">
                <div v-for="f in allFields" :key="f.key" class="summary-dl-row">
                  <dt>{{ f.label }}</dt>
                  <dd>{{ f.value }}</dd>
                </div>
              </dl>
            </div>
          </el-tab-pane>

          <el-tab-pane label="原始文档" name="doc">
            <div v-if="mdContent">
              <DocViewer :content="mdContent" :file-path="command.file_path || ''" api-base="command-graph" />
            </div>
            <div v-else style="padding: 60px; text-align: center; color: var(--text-tertiary); font-size: var(--text-sm)">
              {{ command.file_path ? '加载中...' : '无关联文档' }}
            </div>
          </el-tab-pane>
        </el-tabs>
      </div>
    </div>
  </div>
  <div v-else class="page-container">
    <div class="page-inner" style="text-align: center; padding-top: 80px">
      <div v-if="loading">加载中...</div>
      <div v-else>命令未找到: {{ product }}/{{ commandName }}</div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, computed, watch } from 'vue'
import { useRoute } from 'vue-router'
import { commandGraphApi, fetchJson } from '../api'
import DocViewer from '../shared/DocViewer.vue'

const route = useRoute()
const product = computed(() => route.params.product as string)
const commandName = computed(() => route.params.commandName as string)

const loading = ref(true)
const command = ref<any>(null)
const mdContent = ref('')
const activeTab = ref('fields')

function formatCategoryPath(raw: string) {
  if (!raw) return '-'
  try {
    const arr = JSON.parse(raw)
    return Array.isArray(arr) ? arr.join(' > ') : raw
  } catch {
    return raw
  }
}

const allFields = computed(() => {
  if (!command.value) return []
  const labels: Record<string, string> = {
    product: '产品',
    version: '版本',
    command_name: '命令名',
    command_name_zh: '中文名',
    category_path: '分类路径',
    file_path: '文件路径',
    topic_id: 'Topic ID',
    command_function: '命令功能',
    notes: '注意事项',
    permission: '操作权限',
    examples: '使用实例',
  }
  const skip = new Set(['command_function', 'notes', 'permission', 'examples'])
  return Object.entries(command.value)
    .filter(([k]) => !skip.has(k))
    .map(([k, v]) => {
      let val = v
      if (k === 'category_path') val = formatCategoryPath(v as string)
      return { key: k, label: labels[k] || k, value: val || '-' }
    })
})

async function loadAll() {
  loading.value = true
  mdContent.value = ''
  try {
    const data = await fetchJson(commandGraphApi.command(product.value, commandName.value))
    command.value = data.error ? null : data

    if (command.value?.file_path) {
      const mdData = await fetchJson(commandGraphApi.commandMd(product.value, commandName.value))
      mdContent.value = mdData.content || ''
    }
  } finally {
    loading.value = false
  }
}

watch([product, commandName], () => {
  activeTab.value = 'fields'
  loadAll()
})

onMounted(loadAll)
</script>

<style scoped>
.cmd-example {
  background: var(--bg-secondary, #f8fafc);
  border: 1px solid var(--border, #e2e8f0);
  border-radius: var(--radius, 6px);
  padding: 12px 16px;
  font-size: var(--text-xs);
  line-height: 1.7;
  white-space: pre-wrap;
  word-break: break-all;
  color: var(--text-secondary);
  font-family: 'JetBrains Mono', 'Fira Code', monospace;
}
</style>
