import { createRouter, createWebHistory } from 'vue-router'

// 三菜单信息架构：图谱浏览（默认）/ 统计 / 上传
export const router = createRouter({
  history: createWebHistory(),
  routes: [
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
  ],
})
