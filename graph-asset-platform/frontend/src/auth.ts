// 鉴权 KEY 的浏览器存储（sessionStorage：关标签页即失效，适度安全）。
const KEY = 'gap_api_key'

export function getKey(): string {
  return sessionStorage.getItem(KEY) || ''
}
export function setKey(k: string): void {
  sessionStorage.setItem(KEY, k)
}
export function clearKey(): void {
  sessionStorage.removeItem(KEY)
}
export function hasKey(): boolean {
  return !!getKey()
}
