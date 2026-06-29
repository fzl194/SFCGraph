const BASE = '/api/v1'

export const commandGraphApi = {
  stats: `${BASE}/command-graph/stats`,
  commands: `${BASE}/command-graph/commands`,
  command: (nf: string, commandName: string, version?: string) => {
    const p = new URLSearchParams({ nf, command_name: commandName })
    if (version) p.set('version', version)
    return `${BASE}/command-graph/command?${p}`
  },
  commandMd: (nf: string, commandName: string, version?: string) => {
    const p = new URLSearchParams({ nf, command_name: commandName })
    if (version) p.set('version', version)
    return `${BASE}/command-graph/command-md?${p}`
  },
  commandParameters: (nf: string, commandName: string, version?: string) => {
    const p = new URLSearchParams({ nf, command_name: commandName })
    if (version) p.set('version', version)
    return `${BASE}/command-graph/command-parameters?${p}`
  },
  commandGraph: (nf: string, commandName: string, version?: string) => {
    const p = new URLSearchParams({ nf, command_name: commandName })
    if (version) p.set('version', version)
    return `${BASE}/command-graph/command-graph?${p}`
  },
  commandObject: (nf: string, commandName: string, version?: string) => {
    const p = new URLSearchParams({ nf, command_name: commandName })
    if (version) p.set('version', version)
    return `${BASE}/command-graph/command-object?${p}`
  },
  subgraph: (center: string, hops = 2, edgeTypes?: string[]) => {
    const p = new URLSearchParams({ center, hops: String(hops) })
    if (edgeTypes?.length) p.set('edge_types', edgeTypes.join(','))
    return `${BASE}/command-graph/subgraph?${p}`
  },
}

export const businessGraphApi = {
  domains: `${BASE}/business-graph/domains`,
  domain: (name: string) => `${BASE}/business-graph/domains/${encodeURIComponent(name)}`,
  scenario: (id: string) => `${BASE}/business-graph/scenarios/${encodeURIComponent(id)}`,
  layers: (id: string) => `${BASE}/business-graph/scenarios/${encodeURIComponent(id)}/layers`,
  layer: (id: string, layerId: string) =>
    `${BASE}/business-graph/scenarios/${encodeURIComponent(id)}/layers/${layerId}`,
  rawMd: (id: string, layerId: string) =>
    `${BASE}/business-graph/scenarios/${encodeURIComponent(id)}/layers/${layerId}/raw`,
  graph: (id: string) => `${BASE}/business-graph/scenarios/${encodeURIComponent(id)}/graph`,
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
