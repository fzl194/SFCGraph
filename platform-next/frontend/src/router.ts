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
          name: 'command-overview',
          component: () => import('./command_graph/CommandOverview.vue'),
        },
        {
          path: ':nf/:version',
          name: 'command-list',
          component: () => import('./command_graph/CommandList.vue'),
        },
      ],
    },
    {
      path: '/command-graph/:nf/:version/:commandName(.*)',
      name: 'command-detail',
      component: () => import('./command_graph/CommandDetail.vue'),
    },
    {
      path: '/task-graph',
      component: () => import('./task_graph/TaskIndex.vue'),
      children: [
        { path: '', name: 'task-overview', component: () => import('./task_graph/TaskOverview.vue') },
        { path: ':nf/:version', name: 'task-list', component: () => import('./task_graph/TaskList.vue') },
      ],
    },
    {
      path: '/task-graph/:nf/:version/:taskId',
      name: 'task-detail',
      component: () => import('./task_graph/TaskDetail.vue'),
    },
    {
      path: '/feature-graph',
      component: () => import('./feature_graph/FeatureIndex.vue'),
      children: [
        { path: '', name: 'feature-overview', component: () => import('./feature_graph/FeatureOverview.vue') },
        { path: ':nf/:version', name: 'feature-list', component: () => import('./feature_graph/FeatureListPage.vue') },
      ],
    },
    {
      path: '/feature-graph/:nf/:version/feature/:code',
      name: 'feature-detail',
      component: () => import('./feature_graph/FeatureDetail.vue'),
    },
    {
      path: '/feature-graph/:nf/:version/license/:code',
      name: 'license-detail',
      component: () => import('./feature_graph/LicenseDetail.vue'),
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
    {
      path: '/graph-overview',
      component: () => import('./wiki/WikiIndex.vue'),
    },
    {
      path: '/graph-overview/a/:path(.*)',
      name: 'graph-overview-asset',
      component: () => import('./wiki/WikiIndex.vue'),
    },
  ],
})

export default router
