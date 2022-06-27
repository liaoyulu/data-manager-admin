import { DEFAULT_LAYOUT } from '@/router/constants';

export default {
  path: '/account',
  name: 'account',
  component: DEFAULT_LAYOUT,
  meta: {
    locale: 'menu.account',
    requiresAuth: true,
    icon: 'icon-user',
    order: 0,
  },
  children: [
    {
      path: 'enterprise',
      name: 'enterprise',
      component: () => import('@/views/account/enterprise/index.vue'),
      meta: {
        locale: 'menu.account.enterprise',
        requiresAuth: true,
        roles: ['*'],
        icon: 'icon-user-group',
      },
    },
    {
      path: 'staff',
      name: 'staff',
      component: () => import('@/views/account/staff/index.vue'),
      meta: {
        locale: 'menu.account.staff',
        requiresAuth: true,
        roles: ['*'],
        icon: 'icon-skin',
      },
    },
  ],
};