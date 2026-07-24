<template>
  <div class="users-page">
    <header class="page-head">
      <h1 class="page-title">用户管理</h1>
      <el-button type="primary" @click="openCreate">+ 新建用户</el-button>
    </header>

    <el-table :data="users" v-loading="loading" stripe>
      <el-table-column prop="username" label="用户名" width="140" />
      <el-table-column label="API Key" min-width="280">
        <template #default="{ row }">
          <code class="key">{{ row.key }}</code>
          <el-button link size="small" @click="copy(row.key)">复制</el-button>
        </template>
      </el-table-column>
      <el-table-column label="权限" width="220">
        <template #default="{ row }">
          <el-tag v-if="row.is_admin" type="danger" size="small">admin</el-tag>
          <el-tag v-if="row.can_frontend" type="success" size="small">前端</el-tag>
          <el-tag v-if="row.can_skill" type="warning" size="small">SKILL</el-tag>
        </template>
      </el-table-column>
      <el-table-column label="操作" width="220">
        <template #default="{ row }">
          <el-button link size="small" @click="openActivity(row as UserRow)">轨迹</el-button>
          <el-button link size="small" @click="openEdit(row as UserRow)">改权限</el-button>
          <el-button link size="small" type="danger" :disabled="row.username === 'admin'" @click="del(row as UserRow)">删除</el-button>
        </template>
      </el-table-column>
    </el-table>

    <!-- 新建用户 -->
    <el-dialog v-model="createVisible" title="新建用户" width="420px">
      <el-form label-width="90px">
        <el-form-item label="用户名"><el-input v-model="form.username" /></el-form-item>
        <el-form-item label="前端权限"><el-checkbox v-model="form.can_frontend" /></el-form-item>
        <el-form-item label="SKILL权限"><el-checkbox v-model="form.can_skill" /></el-form-item>
        <el-form-item label="管理员"><el-checkbox v-model="form.is_admin" /></el-form-item>
      </el-form>
      <template #footer>
        <el-button @click="createVisible = false">取消</el-button>
        <el-button type="primary" :loading="saving" @click="doCreate">创建（自动生成 KEY）</el-button>
      </template>
    </el-dialog>

    <!-- 改权限 / 重置 KEY -->
    <el-dialog v-model="editVisible" title="修改权限 / 重置 KEY" width="420px">
      <el-form label-width="90px">
        <el-form-item label="用户名"><span>{{ editTarget?.username }}</span></el-form-item>
        <el-form-item label="前端权限"><el-checkbox v-model="editForm.can_frontend" /></el-form-item>
        <el-form-item label="SKILL权限"><el-checkbox v-model="editForm.can_skill" /></el-form-item>
        <el-form-item label="管理员"><el-checkbox v-model="editForm.is_admin" /></el-form-item>
        <el-form-item label="重置 KEY"><el-checkbox v-model="editForm.reset_key" /></el-form-item>
      </el-form>
      <template #footer>
        <el-button @click="editVisible = false">取消</el-button>
        <el-button type="primary" :loading="saving" @click="doEdit">保存</el-button>
      </template>
    </el-dialog>

    <!-- 行为轨迹 -->
    <el-drawer v-model="activityVisible" :title="`行为轨迹 - ${activityTarget?.username}`" size="50%">
      <el-table :data="activity" v-loading="activityLoading" size="small">
        <el-table-column prop="ts" label="时间" width="220" />
        <el-table-column prop="endpoint" label="接口" />
        <el-table-column prop="caller" label="来源" width="80" />
      </el-table>
    </el-drawer>
  </div>
</template>

<script setup lang="ts">
import { onMounted, reactive, ref } from 'vue'
import {
  ElButton, ElTable, ElTableColumn, ElDialog, ElForm, ElFormItem, ElInput,
  ElCheckbox, ElTag, ElDrawer, ElMessage, ElMessageBox,
} from 'element-plus'
import {
  listUsers, createUser, updateUser, deleteUser, userActivity, type UserRow,
} from '../api'

const users = ref<UserRow[]>([])
const loading = ref(false)
const saving = ref(false)

const createVisible = ref(false)
const form = reactive({ username: '', can_frontend: false, can_skill: false, is_admin: false })

const editVisible = ref(false)
const editTarget = ref<UserRow | null>(null)
const editForm = reactive({ can_frontend: false, can_skill: false, is_admin: false, reset_key: false })

const activityVisible = ref(false)
const activityTarget = ref<UserRow | null>(null)
const activity = ref<{ ts: string; endpoint: string; caller: string }[]>([])
const activityLoading = ref(false)

async function load(): Promise<void> {
  loading.value = true
  try {
    users.value = await listUsers()
  } catch (e) {
    ElMessage.error(e instanceof Error ? e.message : '加载失败')
  } finally {
    loading.value = false
  }
}

function openCreate(): void {
  Object.assign(form, { username: '', can_frontend: false, can_skill: false, is_admin: false })
  createVisible.value = true
}

async function doCreate(): Promise<void> {
  if (!form.username.trim()) return
  saving.value = true
  try {
    const u = await createUser({
      username: form.username.trim(),
      can_frontend: form.can_frontend,
      can_skill: form.can_skill,
      is_admin: form.is_admin,
    })
    ElMessage.success(`已创建，KEY：${u.key}`)
    createVisible.value = false
    await load()
  } catch (e) {
    ElMessage.error(e instanceof Error ? e.message : '创建失败')
  } finally {
    saving.value = false
  }
}

function openEdit(row: UserRow): void {
  editTarget.value = row
  Object.assign(editForm, {
    can_frontend: row.can_frontend,
    can_skill: row.can_skill,
    is_admin: row.is_admin,
    reset_key: false,
  })
  editVisible.value = true
}

async function doEdit(): Promise<void> {
  if (!editTarget.value) return
  saving.value = true
  try {
    await updateUser(editTarget.value.username, { ...editForm })
    ElMessage.success('已保存')
    editVisible.value = false
    await load()
  } catch (e) {
    ElMessage.error(e instanceof Error ? e.message : '保存失败')
  } finally {
    saving.value = false
  }
}

async function del(row: UserRow): Promise<void> {
  try {
    await ElMessageBox.confirm(`确定删除用户「${row.username}」？`, '确认删除', { type: 'warning' })
  } catch {
    return
  }
  try {
    await deleteUser(row.username)
    ElMessage.success('已删除')
    await load()
  } catch (e) {
    ElMessage.error(e instanceof Error ? e.message : '删除失败')
  }
}

async function openActivity(row: UserRow): Promise<void> {
  activityTarget.value = row
  activityVisible.value = true
  activityLoading.value = true
  try {
    activity.value = await userActivity(row.username, 30)
  } catch (e) {
    ElMessage.error(e instanceof Error ? e.message : '加载失败')
  } finally {
    activityLoading.value = false
  }
}

function copy(k: string): void {
  navigator.clipboard?.writeText(k).then(() => ElMessage.success('已复制 KEY'))
}

onMounted(load)
</script>

<style scoped>
.users-page {
  height: 100%;
  overflow: auto;
  padding: var(--space-6) var(--space-7);
  max-width: 1100px;
  margin: 0 auto;
}
.page-head {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: var(--space-4);
}
.page-title {
  font-family: var(--display);
  font-size: 22px;
  font-weight: 700;
  margin: 0;
}
.key {
  font-family: var(--mono);
  font-size: 12px;
}
</style>
