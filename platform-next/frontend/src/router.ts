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
      component: () => import('./command_graph/CommandIndex.vue'),
      children: [
        {
          path: '',
          name: 'command-list',
          component: () => import('./command_graph/CommandList.vue'),
        },
      ],
    },
    {
      path: '/command-graph/:product/:commandName(.*)',
      name: 'command-detail',
      component: () => import('./command_graph/CommandDetail.vue'),
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
      component: () => import('./business_graph/BusinessGraphIndex.vue'),
    },
    {
      path: '/business-graph/domain/:domainName',
      name: 'business-domain',
      component: () => import('./business_graph/BusinessScenario.vue'),
    },
    {
      path: '/business-graph/:scenarioId',
      name: 'business-scenario',
      component: () => import('./business_graph/BusinessScenario.vue'),
    },
  ],
})

export default router
