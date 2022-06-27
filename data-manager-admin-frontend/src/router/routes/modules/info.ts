import { DEFAULT_LAYOUT } from '@/router/constants';

export default {
  path: '/info',
  name: 'info',
  component: DEFAULT_LAYOUT,
  meta: {
    locale: 'menu.info',
    requiresAuth: true,
    icon: 'icon-computer',
    order: 0,
  },
  children: [
    {
      path: 'activity',
      name: 'activity',
      component: () => import('@/views/info/activity/index.vue'),
      meta: {
        locale: 'menu.info.activity',
        requiresAuth: true,
        roles: ['*'],
        icon: 'icon-calendar',
      },
    },
    {
      path: 'notice',
      name: 'notice',
      component: () => import('@/views/info/notice/index.vue'),
      meta: {
        locale: 'menu.info.notice',
        requiresAuth: true,
        roles: ['*'],
        icon: 'icon-message',
      },
    },
    {
      path: 'policy',
      name: 'policy',
      component: () => import('@/views/info/policy/index.vue'),
      meta: {
        locale: 'menu.info.policy',
        requiresAuth: true,
        roles: ['*'],
        icon: 'icon-public',
      },
    },
    {
        path: 'data',
        name: 'data',
        component: () => import('@/views/info/data/index.vue'),
        meta: {
          locale: 'menu.info.data',
          requiresAuth: true,
          roles: ['*'],
          icon: 'icon-file',
        },
      },
  ],
};