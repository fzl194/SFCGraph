// 测试子系统 API 客户端（自包含，不引用图谱前端代码）。
// 全部走 /api/v1/tests/*；id 含 @ 与空格时路径段 encodeURIComponent。
// "涉及对象" autocomplete 另调图谱 /api/v1/names（只读跨子系统，后端两侧零耦合）。

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
  const ct = resp.headers.get('content-type') || ''
  if (ct.includes('application/json')) return (await resp.json()) as T
  return (await resp.text()) as unknown as T
}

function qs(p: Record<string, string | undefined>): string {
  const entries = Object.entries(p).filter(([, v]) => v !== undefined && v !== '')
  if (entries.length === 0) return ''
  return '?' + entries.map(([k, v]) => `${k}=${encodeURIComponent(String(v))}`).join('&')
}

// ---------- 类型（与后端 routers/tests.py 对齐） ----------

export interface Problem {
  description: string
  attribution: string // 图谱知识/配置流程/其他/""
  object: string // 涉及图谱对象 id 或 ""
}

export interface TestCaseRow {
  id: string
  name: string
  domain: string
  scenario: string
  status: string
  file_count: number
  run_count: number
  latest_verdict: string
}

export interface CaseDetail {
  id: string
  name: string
  domain: string
  scenario: string
  status: string
  solution: string
  author: string
  frontmatter: Record<string, unknown>
  body_md: string
  raw_md: string
  files: string[]
  runs: RunRow[]
}

export interface RunRow {
  id: string
  runner: string
  run_at: string
  status: string
  artifact_count: number
  verdict: string
  review_count: number
}

export interface RunDetail {
  id: string
  case: string
  name: string
  runner: string
  run_at: string
  status: string
  artifacts: string[]
  body_md: string
  reviews: ReviewDetail[]
}

export interface ReviewDetail {
  id: string
  run: string
  reviewer: string
  reviewed_at: string
  verdict: string
  problem_count: number
  problems: Problem[]
  body_md: string
  raw_md: string
}

export interface TestStats {
  case_count: number
  run_count: number
  review_count: number
  cases_by_domain: Record<string, number>
  cases_by_domain_scenario: Record<string, number>
  verdict_distribution: Record<string, number>
  warnings: string[]
}

export interface ReviewWriteBody {
  run: string
  reviewer?: string
  verdict: string
  conclusion?: string
  problems: { desc: string; attribution: string; object: string }[]
}

// ---------- API ----------

export const listCases = (p: { domain?: string; scenario?: string; q?: string } = {}): Promise<TestCaseRow[]> =>
  _req<TestCaseRow[]>(`${BASE}/tests/cases${qs(p)}`)

export const getCase = (id: string): Promise<CaseDetail> =>
  _req<CaseDetail>(`${BASE}/tests/cases/${encodeURIComponent(id)}`)

// Phase 1：前端建用例（multipart：意图正文 + 可选上传输入/参考配置文件）
export async function createCase(data: {
  name: string
  intent: string
  domain?: string
  scenario?: string
  slug?: string
  author?: string
  inputFiles?: File[]
  referenceFiles?: File[]
}): Promise<CaseDetail> {
  const fd = new FormData()
  fd.append('name', data.name)
  fd.append('intent', data.intent)
  if (data.domain) fd.append('domain', data.domain)
  if (data.scenario) fd.append('scenario', data.scenario)
  if (data.slug) fd.append('slug', data.slug)
  if (data.author) fd.append('author', data.author)
  ;(data.inputFiles || []).forEach((f) => fd.append('input_files', f))
  ;(data.referenceFiles || []).forEach((f) => fd.append('reference_files', f))
  return _req<CaseDetail>(`${BASE}/tests/cases`, { method: 'POST', body: fd })
}

export const downloadCaseURL = (id: string): string =>
  `${BASE}/tests/cases/${encodeURIComponent(id)}/download`

export const getRun = (id: string): Promise<RunDetail> =>
  _req<RunDetail>(`${BASE}/tests/runs/${encodeURIComponent(id)}`)

// Phase 2：上传运行结果 zip → 解包成 Run 文件夹
export async function uploadRun(caseId: string, file: File, slug?: string): Promise<RunDetail> {
  const fd = new FormData()
  fd.append('case', caseId)
  fd.append('file', file)
  if (slug) fd.append('slug', slug)
  return _req<RunDetail>(`${BASE}/tests/runs`, { method: 'POST', body: fd })
}

export const downloadRunURL = (id: string): string =>
  `${BASE}/tests/runs/${encodeURIComponent(id)}/download`

// 取用例附件文件内容（txt 预览用）
export const getCaseFile = (caseId: string, name: string): Promise<string> =>
  _req<string>(`${BASE}/tests/cases/${encodeURIComponent(caseId)}/file/${name.split('/').map(encodeURIComponent).join('/')}`)

export const getArtifact = (runId: string, name: string): Promise<string> =>
  _req<string>(`${BASE}/tests/runs/${encodeURIComponent(runId)}/artifact/${encodeURIComponent(name)}`)

export const listReviews = (run?: string): Promise<ReviewDetail[]> =>
  _req<ReviewDetail[]>(`${BASE}/tests/reviews${qs({ run })}`)

export const testsStats = (): Promise<TestStats> => _req<TestStats>(`${BASE}/tests/stats`)

export const createReview = (body: ReviewWriteBody): Promise<ReviewDetail> =>
  _req<ReviewDetail>(`${BASE}/tests/reviews`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(body),
  })

export const updateReview = (id: string, body: ReviewWriteBody): Promise<ReviewDetail> =>
  _req<ReviewDetail>(`${BASE}/tests/reviews/${encodeURIComponent(id)}`, {
    method: 'PATCH',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(body),
  })

export const deleteReview = (id: string): Promise<{ ok: boolean }> =>
  _req<{ ok: boolean }>(`${BASE}/tests/reviews/${encodeURIComponent(id)}`, { method: 'DELETE' })

export const reindexTests = (): Promise<{ ok: boolean; case_count: number; run_count: number; review_count: number }> =>
  _req(`${BASE}/tests/reindex`, { method: 'POST' })

// ---------- 涉及对象 autocomplete：调图谱 /names（只读） ----------

let _nameMap: Map<string, string> | null = null
let _namePromise: Promise<Map<string, string>> | null = null

export async function getNameMap(): Promise<Map<string, string>> {
  if (_nameMap) return _nameMap
  if (!_namePromise) {
    _namePromise = _req<Record<string, string>>(`${BASE}/names`)
      .then((d) => {
        _nameMap = new Map(Object.entries(d || {}))
        return _nameMap
      })
      .catch(() => {
        _namePromise = null
        return new Map<string, string>()
      })
  }
  return _namePromise
}

// 输入前缀 → 候选 [{id, name}]（按 name/id 子串匹配，限 20 条）
export async function suggestObjects(prefix: string): Promise<{ id: string; name: string }[]> {
  const m = await getNameMap()
  const p = prefix.trim().toLowerCase()
  if (!p) return []
  const out: { id: string; name: string }[] = []
  for (const [id, name] of m.entries()) {
    if (id.toLowerCase().includes(p) || String(name || '').toLowerCase().includes(p)) {
      out.push({ id, name: String(name || id) })
      if (out.length >= 20) break
    }
  }
  return out
}
