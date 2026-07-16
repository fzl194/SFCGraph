// API 客户端：全部走 /api/v1/*。
// id 含 @ 与空格，路径段必须 encodeURIComponent（@→%40、空格→%20）。
// 统一 _req 封装错误：404 时后端返回 detail.message + available_versions（版本缺失），
// 或 detail: "对象不存在: ..."（id 完全不存在）→ 抛出 ApiError 带 status/detail/payload。

const BASE = '/api/v1'

export interface ApiError extends Error {
  status: number
  detail: unknown
}

async function _req<T>(url: string, init?: RequestInit): Promise<T> {
  const resp = await fetch(url, init)
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
}

// 懒加载目录树：path="" 为根；逐层下钻。total_files 用于"加载更多"分页。
export interface BrowseResult {
  path: string
  dirs: string[]
  files: { name: string; id: string }[]
  total_files: number
  offset: number
  limit: number
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

// ---------- API ----------

export const listObjects = (p: {
  type?: string
  q?: string
  nf?: string
  domain?: string
  page?: number
  size?: number
} = {}): Promise<ObjectRow[]> =>
  _req<ObjectRow[]>(`${BASE}/objects${qs(p)}`)

export const getObject = (id: string, version?: string): Promise<ObjectDetail> =>
  _req<ObjectDetail>(`${BASE}/objects/${encodeURIComponent(id)}${qs({ version })}`)

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

export const importBundle = (file: File): Promise<ImportResult> => {
  const fd = new FormData()
  fd.append('file', file)
  return _req<ImportResult>(`${BASE}/import`, { method: 'POST', body: fd })
}

export const exportUrl = (f: {
  nf?: string
  version?: string
  domain?: string
  scenario?: string
}): string => `${BASE}/export${qs(f)}`

// 懒加载目录树（性能关键：替代旧的 listObjects 全量拉取）
// path 形如 "" → "Command" → "Command/UDG" → "Command/UDG/20.15.2"
export const browse = (p: {
  path?: string
  q?: string
  limit?: number
  offset?: number
}): Promise<BrowseResult> => _req<BrowseResult>(`${BASE}/browse${qs(p)}`)

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
