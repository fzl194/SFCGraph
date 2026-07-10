/** wiki 共享视觉 token —— 对象类型的中文名 + 谐调配色（Tailwind-600/700 族）。
 *  全局唯一来源：左树类型色条/标签、图谱节点配色、搜索结果标签都从这里取，保证色彩一致。 */
export interface TypeStyle { label: string; bg: string; bd: string }

export const TYPE_META: Record<string, TypeStyle> = {
  MMLCommand:     { label: '命令',     bg: '#0891b2', bd: '#0e7490' },  // cyan
  ConfigObject:   { label: '配置对象', bg: '#4f46e5', bd: '#4338ca' },  // indigo
  Feature:        { label: '特性',     bg: '#0d9488', bd: '#0f766e' },  // teal
  License:        { label: 'License', bg: '#d97706', bd: '#b45309' },  // amber
  Task:           { label: '任务',     bg: '#e11d48', bd: '#be123c' },  // rose（基色）
  BusinessDomain: { label: '业务域',   bg: '#64748b', bd: '#475569' },  // slate
  NetworkScenario:      { label: '场景', bg: '#0891b2', bd: '#0e7490' }, // cyan（与命令同色系区分通过形状/标签）
  ConfigurationSolution: { label: '方案', bg: '#7c3aed', bd: '#6d28d9' }, // violet
}

/** Task 按 task_layer（0-atom / 1-compound / 2-feature）做同色系深浅：
 *  0- 最浅（atom，颗粒细），1- 中，2- 最深（feature，最抽象/上层）。
 *  同一色系（rose）保证视觉家族一致，深浅区分层次。 */
export const TASK_LAYER_META: Record<string, TypeStyle> = {
  '0-': { label: 'atom',     bg: '#fda4af', bd: '#fb7185' },  // rose-300 / rose-400
  '1-': { label: 'compound', bg: '#fb7185', bd: '#f43f5e' },  // rose-400 / rose-500
  '2-': { label: 'feature',  bg: '#e11d48', bd: '#be123c' },  // rose-600 / rose-700（基色）
}

/** 每类对象在左树下钻时用的分组字段（front-matter） */
export const GROUP_FIELD: Record<string, string> = {
  MMLCommand: 'category_path',
  ConfigObject: 'object_kind',
  Feature: 'parent_feature_code',
  License: 'applicable_nf',
  Task: 'task_layer',
  BusinessDomain: 'domain',
  NetworkScenario: 'domain',
  ConfigurationSolution: 'domain',
}

/** 业务层对象（无 nf/version，按 domain[/scenario] 分组） */
export const BUSINESS_TYPES = new Set(['BusinessDomain', 'NetworkScenario', 'ConfigurationSolution'])

export function typeLabel(t?: string): string {
  return (t && TYPE_META[t]?.label) || t || '?'
}
export function typeColor(t?: string): string {
  return (t && TYPE_META[t]?.bg) || '#64748b'
}

/** Task 节点取色：按 task_layer（0-/1-/2-）返回同色系深浅；fallback Task 基色 */
export function taskLayerColor(layer: string | undefined, fallbackType = 'Task'): string {
  if (layer && TASK_LAYER_META[layer]) return TASK_LAYER_META[layer].bg
  return typeColor(fallbackType)
}
