// 鉴权 session（username + key + is_admin），sessionStorage 存储。
const SESSION = 'gap_session'

export interface Session {
  username: string
  key: string
  is_admin: boolean
}

export function getSession(): Session | null {
  const raw = sessionStorage.getItem(SESSION)
  return raw ? (JSON.parse(raw) as Session) : null
}
export function setSession(s: Session): void {
  sessionStorage.setItem(SESSION, JSON.stringify(s))
}
export function clearSession(): void {
  sessionStorage.removeItem(SESSION)
}
export function getKey(): string {
  return getSession()?.key || ''
}
export function isAdmin(): boolean {
  return !!getSession()?.is_admin
}
export function hasKey(): boolean {
  return !!getSession()
}
