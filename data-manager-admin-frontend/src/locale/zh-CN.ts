import localeMessageBox from '@/components/message-box/locale/zh-CN';
import localeLogin from '@/views/login/locale/zh-CN';

import localeSettings from './zh-CN/settings';

export default {
  // 自定义添加
  'menu.account': '账户管理',
  'menu.account.enterprise': '企业账户',
  'menu.account.staff': '员工账户',

  'menu.info': '信息管理',
  'menu.info.activity': '园区活动',
  'menu.info.notice': '通知公告',
  'menu.info.policy': '服务政策',
  'menu.info.data': '数据上报',

  'menu.other': '其他',
  'menu.other.carousel': '小程序轮播图',
  'menu.other.visualization': '数据可视化',


  'activity.searchTable.operation.create': '添加活动',
  'activity.searchTable.form.title.placeholder': '请输入活动标题',
  'activity.searchTable.form.search': '搜索',

  // 模板原始项，不修改
  'menu.dashboard': '仪表盘',
  'menu.server.dashboard': '仪表盘-服务端',
  'menu.server.workplace': '工作台-服务端',
  'menu.server.monitor': '实时监控-服务端',
  'menu.list': '列表页',
  'menu.result': '结果页',
  'menu.exception': '异常页',
  'menu.form': '表单页',
  'menu.profile': '详情页',
  'menu.visualization': '数据可视化',
  'menu.user': '个人中心',
  'menu.arcoWebsite': 'Arco Design',
  'menu.faq': '常见问题',
  'navbar.docs': '文档中心',
  'navbar.action.locale': '切换为中文',
  ...localeSettings,
  ...localeMessageBox,
  ...localeLogin,
};
