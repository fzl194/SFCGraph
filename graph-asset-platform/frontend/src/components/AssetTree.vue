<template>
  <div class="asset-tree-wrap">
    <div class="tree-toolbar">
      <el-input
        v-model="query"
        placeholder="在当前目录过滤…"
        :prefix-icon="SearchIcon"
        clearable
        size="small"
        class="search-input"
        @input="onSearch"
      />
    </div>

    <el-tree-v2
      ref="treeRef"
      :data="roots"
      :props="treeProps"
      :height="treeHeight"
      :item-size="30"
      :indent="22"
      :expand-on-click-node="true"
      :highlight-current="true"
      :current-node-key="currentKey"
      node-key="key"
      @node-click="onNodeClick"
      @node-expand="onNodeExpand"
    >
      <template #default="{ node, data }">
        <span
          class="node-row"
          :class="{
            'is-file': data.kind === 'file',
            'is-more': data.kind === 'more',
            'is-dir': data.kind === 'dir',
          }"
          :style="nodeDepthStyle(node.level)"
        >
          <span v-if="data.kind === 'dir'" class="node-caret">
            <svg width="10" height="10" viewBox="0 0 24 24" fill="none">
              <path
                d="M9 6l6 6-6 6"
                stroke="currentColor"
                stroke-width="2.5"
                stroke-linecap="round"
                stroke-linejoin="round"
                :transform="node.expanded ? 'rotate(90 12 12)' : ''"
              />
            </svg>
          </span>
          <span v-else class="node-caret placeholder" />

          <span v-if="data.kind === 'dir'" class="node-icon dir">
            <!-- 展开态：打开的文件夹图标 -->
            <svg v-if="node.expanded" width="14" height="14" viewBox="0 0 24 24" fill="none">
              <path
                d="M3 9a2 2 0 0 1 2-2h4l2 2h8a2 2 0 0 1 2 2v1H3V9Z"
                fill="currentColor"
                opacity="0.22"
              />
              <path
                d="M3 9a2 2 0 0 1 2-2h4l2 2h8a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V9Z"
                stroke="currentColor"
                stroke-width="1.4"
                stroke-linejoin="round"
                fill="none"
              />
              <path
                d="M3 11h18"
                stroke="currentColor"
                stroke-width="1.2"
                opacity="0.5"
              />
            </svg>
            <!-- 收起态：闭合文件夹 -->
            <svg v-else width="14" height="14" viewBox="0 0 24 24" fill="none">
              <path
                d="M3 7a2 2 0 0 1 2-2h4l2 2h8a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V7Z"
                fill="currentColor"
                opacity="0.18"
              />
              <path
                d="M3 7a2 2 0 0 1 2-2h4l2 2h8a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V7Z"
                stroke="currentColor"
                stroke-width="1.4"
                stroke-linejoin="round"
              />
            </svg>
          </span>
          <span v-else-if="data.kind === 'file'" class="node-icon file">
            <svg width="13" height="13" viewBox="0 0 24 24" fill="none">
              <path
                d="M6 2h8l5 5v13a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2Z"
                stroke="currentColor"
                stroke-width="1.5"
                stroke-linejoin="round"
              />
              <path d="M14 2v5h5" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round" />
            </svg>
          </span>

          <span v-if="data.kind === 'more'" class="node-label more-label">
            <svg width="11" height="11" viewBox="0 0 24 24" fill="none" class="spin">
              <path
                d="M12 3a9 9 0 1 0 9 9"
                stroke="currentColor"
                stroke-width="2.5"
                stroke-linecap="round"
              />
            </svg>
            <span v-if="loadingMore">加载中…</span>
            <span v-else>加载更多（剩余 {{ data.remaining }}）</span>
          </span>

          <span v-else class="node-label" :class="{ mono: data.kind === 'file' }">
            {{ data.label }}
          </span>

          <span v-if="data.kind === 'dir' && data.count !== undefined" class="node-count mono">
            {{ data.count }}
          </span>
        </span>
      </template>
    </el-tree-v2>
  </div>
</template>

<script setup lang="ts">
import { h, onMounted, onUnmounted, ref } from 'vue'
import { browse } from '../api'

// 树节点形状。dir 有 children（懒填充）；file 叶子；more 是分页哨兵。
interface AssetNode {
  key: string
  label: string
  kind: 'dir' | 'file' | 'more'
  path: string // 该节点对应的 browse path（dir/文件所在目录）
  id?: string // file 的对象 id
  children?: AssetNode[]
  count?: number // dir 的子项总数（用于角标）
  loaded?: boolean // dir 是否已懒加载过
  parent?: AssetNode
  offset?: number // more 节点已加载到哪
  remaining?: number
  isLeaf?: boolean // el-tree-v2 用：file/more 为 true，避免误触发展开
}

const PAGE = 200 // 单次分页：平衡首屏与请求次数

// 深响应 ref：子节点 children 变更能被 el-tree-v2 感知（shallowRef 会丢失深层依赖）
const roots = ref<AssetNode[]>([])
const treeRef = ref<{ setData?: (d: AssetNode[]) => void; filter?: (q: string) => void } | null>(null)
const treeHeight = ref(600)
const query = ref('')
const currentKey = ref<string>('')
const loadingMore = ref(false)

const treeProps = {
  value: 'key',
  label: 'label',
  children: 'children',
  isLeaf: 'isLeaf',
}

// 按深度生成引导线：每层左侧叠一条淡色竖线（linear-gradient 模拟）。
// 虚拟滚动下稳定：仅依赖 node.level，padding 由 el-tree 的 indent 控制。
function nodeDepthStyle(level: number | undefined): Record<string, string> {
  const depth = Math.max(0, (level ?? 1) - 1) // level 从 1 起，根节点无线
  if (depth === 0) return {}
  // 每深一层在 22px 间距处叠一条 1px 垂直线（与 :indent=22 对齐）
  const bg = Array.from({ length: depth }, (_, i) => {
    const x = (i + 1) * 22 - 11
    return `linear-gradient(to right, transparent ${x - 1}px, var(--tree-line) ${x - 1}px ${x}px, transparent ${x}px 100%)`
  }).join(', ')
  return {
    backgroundImage: bg,
    backgroundRepeat: 'no-repeat',
  }
}

// 内联 search icon
const SearchIcon = () =>
  h(
    'svg',
    { width: '14', height: '14', viewBox: '0 0 24 24', fill: 'none' },
    [
      h('circle', { cx: '11', cy: '11', r: '7', stroke: 'currentColor', 'stroke-width': '2' }),
      h('path', {
        d: 'M20 20l-3.2-3.2',
        stroke: 'currentColor',
        'stroke-width': '2',
        'stroke-linecap': 'round',
      }),
    ],
  )

// 层目录根（Command/ConfigObject/...）
async function loadRoots(): Promise<void> {
  const r = await browse({ path: '', limit: 200 })
  roots.value = r.dirs.map(
    (name): AssetNode => ({
      key: name,
      label: name,
      kind: 'dir',
      path: name,
      children: [],
      loaded: false,
      isLeaf: false,
    }),
  )
}

// 展开目录节点：懒拉子项
async function onNodeExpand(data: AssetNode): Promise<void> {
  if (data.kind !== 'dir') return
  if (data.loaded) return
  await fillDirChildren(data)
  syncRender()
}

async function fillDirChildren(node: AssetNode): Promise<void> {
  try {
    const r = await browse({ path: node.path, limit: PAGE, offset: 0 })
    node.children = buildChildren(node, r.dirs, r.files, r.total_files, 0)
    node.loaded = true
    node.count = r.dirs.length + r.total_files
    syncRender()
  } catch {
    node.children = []
    node.loaded = true
    syncRender()
  }
}

function buildChildren(
  parent: AssetNode,
  dirs: string[],
  files: { name: string; id: string }[],
  totalFiles: number,
  offset: number,
): AssetNode[] {
  const dirNodes: AssetNode[] = dirs.map(
    (name): AssetNode => ({
      key: parent.path + '/' + name,
      label: name,
      kind: 'dir',
      path: parent.path ? parent.path + '/' + name : name,
      children: [],
      loaded: false,
      isLeaf: false,
      parent,
    }),
  )
  const fileNodes: AssetNode[] = files.map(
    (f): AssetNode => ({
      key: 'obj::' + f.id,
      label: f.id,
      kind: 'file',
      path: parent.path,
      id: f.id,
      isLeaf: true,
      parent,
    }),
  )
  const loaded = offset + files.length
  const remaining = totalFiles - loaded
  const more: AssetNode[] =
    remaining > 0
      ? [
          {
            key: `more::${parent.path}::${loaded}`,
            label: `加载更多`,
            kind: 'more',
            path: parent.path,
            offset: loaded,
            remaining,
            parent,
          },
        ]
      : []
  return [...dirNodes, ...fileNodes, ...more]
}

// 点击：file → 选中对象；more → 翻页
async function onNodeClick(data: AssetNode): Promise<void> {
  if (data.kind === 'file' && data.id) {
    currentKey.value = data.key
    emit('select', data.id)
  } else if (data.kind === 'more') {
    await loadMore(data)
  }
}

async function loadMore(moreNode: AssetNode): Promise<void> {
  if (loadingMore.value || !moreNode.parent) return
  loadingMore.value = true
  try {
    const offset = moreNode.offset ?? 0
    const r = await browse({ path: moreNode.path, limit: PAGE, offset })
    const parent = moreNode.parent
    // 移除旧 more，append 新文件，按需追加新 more
    const withoutMore = (parent.children ?? []).filter((c) => c.kind !== 'more')
    const newFiles = r.files.map(
      (f, i): AssetNode => ({
        key: 'obj::' + f.id + '::' + (offset + i),
        label: f.id,
        kind: 'file',
        path: parent.path,
        id: f.id,
        isLeaf: true,
        parent,
      }),
    )
    const loaded = offset + r.files.length
    const remaining = r.total_files - loaded
    const newMore: AssetNode[] =
      remaining > 0
        ? [
            {
              key: `more::${parent.path}::${loaded}`,
              label: '加载更多',
              kind: 'more',
              path: parent.path,
              offset: loaded,
              remaining,
              parent,
            },
          ]
        : []
    parent.children = [...withoutMore, ...newFiles, ...newMore]
    syncRender()
  } finally {
    loadingMore.value = false
  }
}

// 触发 el-tree-v2 重新读取 data：用暴露的 setData 强制重建内部节点树。
// 仅赋值 roots.value（哪怕新数组引用）不够——el-tree-v2 按节点引用 diff，
// 改 children 不换对象则不更新；setData 走全量重建路径最可靠。
function syncRender(): void {
  if (treeRef.value?.setData) {
    treeRef.value.setData(roots.value)
  } else {
    roots.value = [...roots.value]
  }
}

// 搜索：debounce，对当前已加载范围过滤（不全量拉取）
let searchTimer: ReturnType<typeof setTimeout> | null = null
function onSearch(): void {
  if (searchTimer) clearTimeout(searchTimer)
  searchTimer = setTimeout(async () => {
    const q = query.value.trim()
    // el-tree-v2 自带 filterMethod 仅过滤已加载节点；这里对根层做服务端 q 查询更高效，
    // 但为避免破坏已展开状态，先用本地 filter。
    applyFilter(q)
  }, 250)
}

function applyFilter(q: string): void {
  treeRef.value?.filter?.(q)
}

// 高度自适应
function fitHeight(): void {
  treeHeight.value = Math.max(320, window.innerHeight - 170)
}

const emit = defineEmits<{
  (e: 'select', id: string): void
}>()

// 暴露：外部跳转时定位节点（如图谱→资产）
function revealFile(id: string): void {
  currentKey.value = 'obj::' + id
}

defineExpose({ revealFile })

onMounted(async () => {
  fitHeight()
  window.addEventListener('resize', fitHeight)
  await loadRoots()
})

onUnmounted(() => {
  window.removeEventListener('resize', fitHeight)
  if (searchTimer) clearTimeout(searchTimer)
})

// 让 el-tree-v2 的 filterMethod 生效（默认按 label 包含）
// filterMethod 在 el-tree-v2 中通过 filter(val) + filterMethod prop 配合；这里暂用本地内置。
</script>

<style scoped>
.asset-tree-wrap {
  display: flex;
  flex-direction: column;
  height: 100%;
  background: var(--bg-sunken);
}

.tree-toolbar {
  padding: var(--space-3);
  border-bottom: 1px solid var(--border);
  background: var(--bg-elev);
}

.search-input :deep(.el-input__wrapper) {
  background: var(--bg-sunken) !important;
}

.node-row {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  width: 100%;
  padding-right: 8px;
  font-size: 13px;
  color: var(--text-muted);
  background-color: transparent;
}

.node-caret {
  display: inline-flex;
  width: 12px;
  color: var(--text-faint);
  flex-shrink: 0;
}

.node-caret.placeholder {
  visibility: hidden;
}

.node-icon {
  display: inline-flex;
  flex-shrink: 0;
}

.node-icon.dir {
  color: #8b8680;
}

.node-icon.file {
  color: var(--text-faint);
}

.node-label {
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.node-label.mono {
  font-family: var(--mono);
  font-size: 12px;
  color: var(--text);
}

.node-row.is-file:hover .node-label {
  color: var(--accent);
}

.node-row.is-more {
  color: var(--accent);
  font-weight: 500;
  cursor: pointer;
  padding: 4px 0;
}

.more-label {
  display: inline-flex;
  align-items: center;
  gap: 6px;
}

.node-count {
  margin-left: auto;
  font-size: 11px;
  color: var(--text-faint);
  background: var(--bg-elev);
  border: 1px solid var(--border);
  border-radius: 999px;
  padding: 1px 7px;
  flex-shrink: 0;
}

:deep(.el-tree-node__content) {
  height: 30px;
  padding-left: 4px !important;
}

:deep(.el-tree-node__content:hover) {
  background: var(--bg-hover);
}

:deep(.el-tree-node.is-current > .el-tree-node__content) {
  background: var(--accent-soft);
}

.spin {
  animation: spin 0.8s linear infinite;
}

@keyframes spin {
  to {
    transform: rotate(360deg);
  }
}
</style>
