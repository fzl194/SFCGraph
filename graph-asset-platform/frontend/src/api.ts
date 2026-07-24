// API 客户端：全部走 /api/v1/*。
// id 含 @ 与空格，路径段必须 encodeURIComponent（@→%40、空格→%20）。
// 统一 _req 封装错误：404 时后端返回 detail.message + available_versions（版本缺失），
// 或 detail: "对象不存在: ..."（id 完全不存在）→ 抛出 ApiError 带 status/detail/payload。

import { getKey, clearSession } from './auth'

const BASE = '/api/v1'

export interface ApiError extends Error {
  status: number
  detail: unknown
}

async function _req<T>(url: string, init?: RequestInit): Promise<T> {
  const headers = new Headers(init?.headers)
  const k = getKey()
  if (k) headers.set('X-API-Key', k)
  headers.set('X-Client', 'web')
  const resp = await fetch(url, { ...init, headers })
  if (resp.status === 401) {
    clearSession()
    // window.location 最稳，绕开 router 实例（避免 api.ts ↔ router.ts 循环依赖）
    if (!window.location.pathname.startsWith('/login')) {
      window.location.assign('/login')
    }
    throw new Error('未授权，已跳转登录')
  }
  if (resp.status === 403) {
    throw Object.assign(new Error('权限不足'), { status: 403 })
  }
  if (!resp.ok) {
    let detail: unknown
    try {
      detail = await resp.json()
    } catch {
      detail = await resp.text().catch(() => '')
    }
    const msg =
      (detail && typeof detail === 'object' && 'detail' in detail
        ? JSON.stringify((detail as { detail: unknown }).detail)
        : String(detail)) || `HTTP ${resp.status}`
    const err = new Error(`API ${resp.status}: ${msg}`) as ApiError
    err.status = resp.status
    err.detail = detail
    throw err
  }
  // md 接口返回 text/markdown
  const ct = resp.headers.get('content-type') || ''
  if (ct.includes('application/json')) {
    return (await resp.json()) as T
  }
  // 纯文本
  return (await resp.text()) as unknown as T
}

// 登录：username+key → 用户信息（含全部权限位）
export interface LoginUser {
  username: string
  can_frontend: boolean
  can_upload: boolean
  can_test: boolean
  can_skill: boolean
  is_admin: boolean
}
export const login = (username: string, key: string): Promise<LoginUser> =>
  _req<LoginUser>(`${BASE}/users/login`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ username, key }),
  })

// SKILL 取用频次聚合（统计页 TelemetrySection 用）
export interface TelemetryStats {
  total: number
  by_type: Record<string, number>
  top_ids: { id: string; type: string; count: number }[]
  timeline: { date: string; count: number }[]
  by_user: Record<string, number>
  by_operator: Record<string, number>
}

export const fetchTelemetryStats = (days = 30): Promise<TelemetryStats> =>
  _req<TelemetryStats>(`${BASE}/telemetry/stats?days=${days}`)

// ---------- 用户管理（admin）----------
export interface UserRow {
  username: string
  key: string
  can_frontend: boolean
  can_upload: boolean
  can_test: boolean
  can_skill: boolean
  is_admin: boolean
  created_at?: string
}

export const listUsers = (): Promise<UserRow[]> => _req(`${BASE}/users`)

export const createUser = (b: {
  username: string
  can_frontend?: boolean
  can_upload?: boolean
  can_test?: boolean
  can_skill?: boolean
  is_admin?: boolean
}): Promise<UserRow> =>
  _req(`${BASE}/users`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(b),
  })

export const updateUser = (name: string, b: Record<string, unknown>): Promise<UserRow> =>
  _req(`${BASE}/users/${encodeURIComponent(name)}`, {
    method: 'PATCH',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(b),
  })

export const deleteUser = (name: string): Promise<{ ok: boolean }> =>
  _req(`${BASE}/users/${encodeURIComponent(name)}`, { method: 'DELETE' })

export const userActivity = (
  name: string,
  days = 30,
): Promise<{ ts: string; endpoint: string; caller: string; operator: string }[]> =>
  _req(`${BASE}/users/${encodeURIComponent(name)}/activity?days=${days}`)

function qs(p: Record<string, string | number | undefined>): string {
  const entries = Object.entries(p).filter(([, v]) => v !== undefined && v !== '')
  if (entries.length === 0) return ''
  return '?' + entries.map(([k, v]) => `${k}=${encodeURIComponent(String(v))}`).join('&')
}

// ---------- 类型（与后端 routers 序列化对齐） ----------

export interface ObjectRow {
  id: string
  type: string
  layer?: string
  nf?: string
  domain?: string
  scenario?: string
  name?: string | null
  versions: string[]
}

export interface ObjectDetail {
  id: string
  type: string
  layer?: string
  scope?: string
  nf?: string
  version?: string
  domain?: string
  scenario?: string
  frontmatter: Record<string, unknown>
  body_md: string
  source_path?: string
  versions: string[]
  out_edges: Edge[]
}

export interface Edge {
  from: string
  from_version?: string
  relation: string
  to: string
}

export interface Neighbors {
  center: ObjectDetail
  out: Edge[]
  in: Edge[]
}

export interface Stats {
  object_counts_by_type: Record<string, number>
  edge_count: number
  nfs: string[]
  versions_per_nf: Record<string, string[]>
  // UI 层聚合（4 层：命令层/特性层/任务层/业务层）
  per_layer: Record<string, number>
  per_layer_per_nf: Record<string, Record<string, number>>
  per_layer_per_nf_per_version: Record<
    string,
    Record<string, Record<string, number>>
  >
  per_domain: Record<string, number>
  per_domain_scenario: Record<string, Record<string, number>>
}

export interface ImportHistoryItem {
  timestamp: string
  filename: string
  added: number
  updated: number
  skipped: number
  warnings: number
}

export interface ImportResult {
  added: number
  updated: number
  skipped: number
  warnings: string[]
  counts: Record<string, number>
}

// 异步导入 job（POST /import 立即返回 job_id，后台处理）
export interface ImportJob {
  job_id: string
  status: 'processing' | 'done' | 'failed'
  added: number
  updated: number
  skipped: number
  warnings: string[]
  error: string
  started_at: number
  finished_at: number
}

// POST /import 202 响应
export interface ImportAccepted {
  job_id: string
  status: 'processing'
}

// ---------- API ----------

export const listObjects = (p: {
  type?: string
  layer?: string
  q?: string
  nf?: string
  version?: string
  domain?: string
  scenario?: string
  page?: number
  size?: number
} = {}): Promise<ObjectRow[]> =>
  _req<ObjectRow[]>(`${BASE}/objects${qs(p)}`)

export const getObject = (id: string, version?: string): Promise<ObjectDetail> =>
  _req<ObjectDetail>(`${BASE}/objects/${encodeURIComponent(id)}${qs({ version })}`)

// id→name 映射（供正文 [[ID]] 渲染可读名）；进程内缓存，首次后只命中内存
let _nameMap: Map<string, string> | null = null
let _nameMapPromise: Promise<Map<string, string>> | null = null

export async function getNameMap(): Promise<Map<string, string>> {
  if (_nameMap) return _nameMap
  if (!_nameMapPromise) {
    _nameMapPromise = _req<Record<string, string>>(`${BASE}/names`).then((d) => {
      _nameMap = new Map(Object.entries(d || {}))
      return _nameMap
    })
  }
  return _nameMapPromise
}

export const neighbors = (
  id: string,
  version?: string,
  hops: number = 1,
): Promise<Neighbors> =>
  _req<Neighbors>(
    `${BASE}/objects/${encodeURIComponent(id)}/neighbors${qs({ hops, version })}`,
  )

export const getMd = (id: string, version?: string): Promise<string> =>
  _req<string>(`${BASE}/objects/${encodeURIComponent(id)}/md${qs({ version })}`)

export const stats = (): Promise<Stats> => _req<Stats>(`${BASE}/stats`)

// 异步导入：立即返回 job_id（202），后台处理；通过 importJob(id) 轮询。
export const importBundle = (file: File): Promise<ImportAccepted> => {
  const fd = new FormData()
  fd.append('file', file)
  return _req<ImportAccepted>(`${BASE}/import`, { method: 'POST', body: fd })
}

export const importJobs = (): Promise<ImportJob[]> =>
  _req<ImportJob[]>(`${BASE}/import/jobs`)

export const importJob = (id: string): Promise<ImportJob> =>
  _req<ImportJob>(`${BASE}/import/jobs/${encodeURIComponent(id)}`)

export const exportUrl = (f: {
  nf?: string
  version?: string
  domain?: string
  scenario?: string
}): string => `${BASE}/export${qs(f)}`

export const importHistory = (): Promise<ImportHistoryItem[]> =>
  _req<ImportHistoryItem[]>(`${BASE}/imports`)

export const subgraph = (p: {
  center: string
  hops?: number
  type?: string
  version?: string
}): Promise<{
  nodes: { id: string; type?: string; label?: string }[]
  edges: { source: string; target: string; relation: string }[]
}> => _req(`${BASE}/subgraph${qs(p)}`)

// 解析 404 detail（版本缺失时带 available_versions）
export function availableVersionsFromError(e: unknown): string[] | null {
  if (!e || typeof e !== 'object' || !('detail' in e)) return null
  const d = (e as { detail: unknown }).detail
  // 后端包装层：fetch.json() 返回 { detail: {...} }
  const inner =
    d && typeof d === 'object' && 'detail' in d
      ? (d as { detail: unknown }).detail
      : d
  if (inner && typeof inner === 'object' && 'available_versions' in inner) {
    return (inner as { available_versions: string[] }).available_versions
  }
  return null
}
