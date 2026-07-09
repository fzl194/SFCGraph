const BASE = '/api/v1/wiki'

async function fetchJson<T>(url: string): Promise<T> {
  const r = await fetch(url)
  if (!r.ok) throw new Error(`${r.status} ${url}`)
  return (await r.json()) as T
}

export interface CategoryNf { nf: string; versions: { version: string; count: number }[] }
export interface Category { type: string; nfs: CategoryNf[] }
export interface GroupBucket { key: string; count: number }
export interface ListItem { path: string; name: string; id: string; title: string }
export interface NbNode {
  path: string | null; id: string; type: string; name: string
  nf?: string; version?: string; title?: string; resolved: boolean
}
export interface NbEdge { from: string; to: string; relation_type: string; resolved: boolean }
export interface Neighborhood { center: NbNode | null; nodes: NbNode[]; edges: NbEdge[] }
export interface MdResp { path: string; content: string; meta: { type?: string; name?: string; title?: string } }

export const wikiApi = {
  categories: () => fetchJson<Category[]>(`${BASE}/categories`),
  group: (type: string, nf: string, version: string) =>
    fetchJson<GroupBucket[]>(`${BASE}/group?type=${type}&nf=${nf}&version=${version}`),
  list: (p: { type: string; nf: string; version: string; group_field?: string; group_value?: string; q?: string; page?: number; size?: number }) => {
    const qs = new URLSearchParams({ type: p.type, nf: p.nf, version: p.version })
    if (p.group_field) qs.set('group_field', p.group_field)
    if (p.group_value) qs.set('group_value', p.group_value)
    if (p.q) qs.set('q', p.q)
    qs.set('page', String(p.page ?? 1)); qs.set('size', String(p.size ?? 100))
    return fetchJson<{ items: ListItem[]; total: number }>(`${BASE}/list?${qs}`)
  },
  neighborhood: (path: string) =>
    fetchJson<Neighborhood>(`${BASE}/neighborhood?path=${encodeURIComponent(path)}`),
  md: (path: string) => fetchJson<MdResp>(`${BASE}/md?path=${encodeURIComponent(path)}`),
  search: (q: string) => fetchJson<ListItem[]>(`${BASE}/search?q=${encodeURIComponent(q)}`),
}
