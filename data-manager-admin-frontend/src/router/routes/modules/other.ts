import { DEFAULT_LAYOUT } from '@/router/constants';

export default {
  path: '/other',
  name: 'other',
  component: DEFAULT_LAYOUT,
  meta: {
    locale: 'menu.other',
    requiresAuth: true,
    icon: 'icon-settings',
    order: 0,
  },
  children: [
    {
      path: 'carousel',
      name: 'carousel',
      component: () => import('@/views/other/carousel/index.vue'),
      meta: {
        locale: 'menu.other.carousel',
        requiresAuth: true,
        roles: ['*'],
        icon: 'icon-file-image',
      },
    },
    {
        path: 'visualization',
        name: 'visualization',
        component: () => import('@/views/other/visualization/index.vue'),
        meta: {
          locale: 'menu.other.visualization',
          requiresAuth: true,
          roles: ['*'],
          icon: 'icon-bar-chart',
        },
      },
  ],
};