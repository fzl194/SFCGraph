const BASE = '/api/v1'

export const featureGraphApi = {
  columns: `${BASE}/feature-graph/columns`,
  stats: `${BASE}/feature-graph/stats`,
  features: `${BASE}/feature-graph/features`,
  feature: (id: string, product?: string) => {
    const base = `${BASE}/feature-graph/features/${id}`
    return product ? `${base}?product_type=${encodeURIComponent(product)}` : base
  },
  featureDocs: (id: string) => `${BASE}/feature-graph/features/${id}/docs`,
  featureDeps: (id: string) => `${BASE}/feature-graph/features/${id}/dependencies`,
  featureLicenses: (id: string) => `${BASE}/feature-graph/features/${id}/licenses`,
  dependencies: `${BASE}/feature-graph/dependencies`,
  licenses: `${BASE}/feature-graph/licenses`,
  docContent: `${BASE}/feature-graph/doc-content`,
  reviewAccept: `${BASE}/feature-graph/review/accept`,
  reviewReject: `${BASE}/feature-graph/review/reject`,
  reviewReset: `${BASE}/feature-graph/review/reset`,
  reviewBulk: `${BASE}/feature-graph/review/bulk`,
  reviewAll: `${BASE}/feature-graph/review/all`,
}

export async function fetchJson(url: string): Promise<any> {
  const res = await fetch(url)
  if (!res.ok) throw new Error(`API error: ${res.status}`)
  return res.json()
}

export async function postJson(url: string, body: any): Promise<any> {
  const res = await fetch(url, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(body),
  })
  if (!res.ok) throw new Error(`API error: ${res.status}`)
  return res.json()
}
