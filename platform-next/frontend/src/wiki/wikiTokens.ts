/** wiki 共享视觉 token —— 对象类型的中文名 + 谐调配色（Tailwind-600/700 族）。
 *  全局唯一来源：左树类型色条/标签、图谱节点配色、搜索结果标签都从这里取，保证色彩一致。 */
export interface TypeStyle { label: string; bg: string; bd: string }

export const TYPE_META: Record<string, TypeStyle> = {
  MMLCommand: { label: '命令', bg: '#0891b2', bd: '#0e7490' },     // cyan
  ConfigObject: { label: '配置对象', bg: '#4f46e5', bd: '#4338ca' }, // indigo
  Feature: { label: '特性', bg: '#0d9488', bd: '#0f766e' },         // teal
  License: { label: 'License', bg: '#d97706', bd: '#b45309' },      // amber
  Task: { label: '任务', bg: '#e11d48', bd: '#be123c' },            // rose
  BusinessDomain: { label: '业务层', bg: '#64748b', bd: '#475569' }, // slate
}

/** 每类对象在左树下钻时用的分组字段（front-matter） */
export const GROUP_FIELD: Record<string, string> = {
  MMLCommand: 'category_path',
  ConfigObject: 'object_kind',
  Feature: 'parent_feature_code',
  License: 'applicable_nf',
  Task: 'task_layer',
}

export function typeLabel(t?: string): string {
  return (t && TYPE_META[t]?.label) || t || '?'
}
export function typeColor(t?: string): string {
  return (t && TYPE_META[t]?.bg) || '#64748b'
}
