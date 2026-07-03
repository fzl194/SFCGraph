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

export const featureGraphApi = {
  stats: `${BASE}/feature-graph/stats`,
  features: (nf: string, version: string) => `${BASE}/feature-graph/features?nf=${nf}&version=${version}`,
  licenses: (nf: string, version: string) => `${BASE}/feature-graph/licenses?nf=${nf}&version=${version}`,
  feature: (nf: string, version: string, code: string) =>
    `${BASE}/feature-graph/feature?nf=${nf}&version=${version}&code=${encodeURIComponent(code)}`,
  featureDocs: (nf: string, version: string, code: string) =>
    `${BASE}/feature-graph/feature-docs?nf=${nf}&version=${version}&code=${encodeURIComponent(code)}`,
  featureRelations: (nf: string, version: string, code: string) =>
    `${BASE}/feature-graph/feature-relations?nf=${nf}&version=${version}&code=${encodeURIComponent(code)}`,
  featureLicenses: (nf: string, version: string, code: string) =>
    `${BASE}/feature-graph/feature-licenses?nf=${nf}&version=${version}&code=${encodeURIComponent(code)}`,
  featureGraph: (nf: string, version: string, code: string, hops = 1) =>
    `${BASE}/feature-graph/feature-graph?nf=${nf}&version=${version}&code=${encodeURIComponent(code)}&hops=${hops}`,
  license: (nf: string, version: string, code: string) =>
    `${BASE}/feature-graph/license?nf=${nf}&version=${version}&code=${encodeURIComponent(code)}`,
  licenseFeatures: (nf: string, version: string, code: string) =>
    `${BASE}/feature-graph/license-features?nf=${nf}&version=${version}&code=${encodeURIComponent(code)}`,
  docContent: (path: string) => `${BASE}/feature-graph/doc-content?path=${encodeURIComponent(path)}`,
  file: (path: string) => `${BASE}/feature-graph/file?path=${encodeURIComponent(path)}`,
}

export const taskGraphApi = {
  stats: `${BASE}/task-graph/stats`,
  tasks: `${BASE}/task-graph/tasks`,
  task: (nf: string, version: string, taskId: string) => {
    const p = new URLSearchParams({ nf, version, task_id: taskId })
    return `${BASE}/task-graph/task?${p}`
  },
  taskTree: (taskId: string) => `${BASE}/task-graph/task-tree?task_id=${encodeURIComponent(taskId)}`,
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
