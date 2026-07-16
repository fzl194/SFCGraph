import { createRouter, createWebHistory } from 'vue-router'

// 三视图信息架构：资产浏览（默认）/ 图谱 / 上传
export const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: '/',
      redirect: '/assets',
    },
    {
      path: '/assets',
      name: 'assets',
      component: () => import('./views/AssetsView.vue'),
    },
    {
      path: '/graph',
      name: 'graph',
      component: () => import('./views/GraphView.vue'),
    },
    {
      path: '/upload',
      name: 'upload',
      component: () => import('./views/UploadView.vue'),
    },
  ],
})
