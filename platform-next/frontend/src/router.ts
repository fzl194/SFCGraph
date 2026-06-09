import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: '/',
      component: () => import('./PlaceholderPage.vue'),
      props: { title: 'SFCGraph Platform', desc: '三层图谱审查管理平台' },
    },
    {
      path: '/command-graph',
      component: () => import('./PlaceholderPage.vue'),
      props: { title: '命令图谱', desc: 'MML 命令关系图谱 — 开发中' },
    },
    {
      path: '/feature',
      component: () => import('./feature_graph/FeatureIndex.vue'),
      children: [
        {
          path: '',
          name: 'feature-list',
          component: () => import('./feature_graph/FeatureList.vue'),
        },
        {
          path: 'relations',
          name: 'feature-relations',
          component: () => import('./feature_graph/FeatureRelations.vue'),
        },
        {
          path: 'licenses',
          name: 'feature-licenses',
          component: () => import('./feature_graph/FeatureLicenses.vue'),
        },
      ],
    },
    {
      path: '/feature/:id',
      name: 'feature-detail',
      component: () => import('./feature_graph/FeatureDetail.vue'),
    },
    {
      path: '/business-graph',
      component: () => import('./PlaceholderPage.vue'),
      props: { title: '业务图谱', desc: '业务场景图谱 — 开发中' },
    },
  ],
})

export default router
