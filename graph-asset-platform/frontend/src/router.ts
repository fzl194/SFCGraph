import { createRouter, createWebHistory } from 'vue-router'
import BrowserView from './views/BrowserView.vue'

// 单路由：根路径 → BrowserView。
// URL 同步 ?o={id}&version={v}（在 BrowserView 内 watch route.query 双向同步）。
export const router = createRouter({
  history: createWebHistory(),
  routes: [{ path: '/', name: 'browser', component: BrowserView }],
})
