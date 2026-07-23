import { createRouter, createWebHistory } from 'vue-router'
import { hasKey } from './auth'

// 三菜单信息架构：图谱浏览（默认）/ 统计 / 上传
export const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: '/login',
      name: 'login',
      component: () => import('./views/LoginView.vue'),
    },
    {
      path: '/',
      name: 'browser',
      component: () => import('./views/BrowserView.vue'),
    },
    {
      path: '/stats',
      name: 'stats',
      component: () => import('./views/StatsView.vue'),
    },
    {
      path: '/upload',
      name: 'upload',
      component: () => import('./views/UploadView.vue'),
    },
    // 测试用例管理子系统（独立模块，第 4 菜单）
    {
      path: '/tests',
      name: 'tests',
      component: () => import('./tests-module/views/TestCasesView.vue'),
    },
    {
      path: '/tests/cases/:id',
      name: 'tests-case',
      component: () => import('./tests-module/views/CaseDetailView.vue'),
    },
    {
      path: '/tests/runs/:id',
      name: 'tests-run',
      component: () => import('./tests-module/views/RunDetailView.vue'),
    },
  ],
})

// 守卫：除登录页外，无 KEY → 跳登录
router.beforeEach((to) => {
  if (to.name === 'login') return true
  if (!hasKey()) return { name: 'login' }
  return true
})
