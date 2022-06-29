<template>
  <div class="container">
    <Breadcrumb :items="['menu.info', 'menu.info.notice']" />
    <a-card>
      <a-row :gutter="24" class="action-panel" justify="start">
        <a-col :span="4">
          <a-button type="outline" @click="addNotice">
            <template #icon>
              <icon-plus />
            </template>
            发布通知
          </a-button>
          <a-modal
            v-model:visible="visibleAddModal"
            width="50%"
            title="发布通知"
            @cancel="addNoticeCancel"
            @ok="addNoticeOk"
          >
            <a-form :model="noticeForm">
              <a-form-item field="NoticeTitle" label="通知标题">
                <a-input v-model="noticeForm.NoticeTitle" />
              </a-form-item>
              <QuillEditor
                v-model="noticeForm.NoticeContent"
                theme="snow"
                toolbar="full"
                content-type="html"
                style="height: 500px"
              />
            </a-form>
          </a-modal>
        </a-col>
        <a-col :span="8">
          <a-input
            v-model="searchTitle"
            placeholder="输入通知标题"
            allow-clear
          />
        </a-col>
        <a-col :span="4">
          <a-button @click="searchNotice">
            <template #icon>
              <icon-search />
            </template>
            搜索
          </a-button>
        </a-col>
      </a-row>
      <a-divider></a-divider>
      <a-table :data="noticeTableData" style="margin-top: 30px">
        <template #columns>
          <a-table-column title="序号" data-index="noticeId"></a-table-column>
          <a-table-column
            title="通知标题"
            data-index="noticeTitle"
          ></a-table-column>
          <a-table-column
            title="发表日期"
            data-index="noticeDate"
          ></a-table-column>
          <a-table-column
            title="已读数量"
            data-index="noticeReadnum"
          ></a-table-column>
          <a-table-column title="操作">
            <template #cell="{ record }">
              <a-button type="text" size="small" @click="editNotice(record)">
                编辑
              </a-button>

              <a-modal
                v-model:visible="visibleEditModal"
                title="编辑通知"
                @cancel="editNoticeCancel"
                @ok="editNoticeOk(record)"
              >
                <a-form :model="noticeForm">
                  <a-form-item field="NoticeTitle" label="通知标题">
                    <a-input v-model="noticeForm.NoticeTitle" />
                  </a-form-item>
                  <QuillEditor
                    v-model:content="noticeForm.NoticeContent"
                    theme="snow"
                    toolbar="full"
                    content-type="html"
                    style="height: 500px"
                  />
                </a-form>
              </a-modal>
              <a-button
                v-if="!record.isTop"
                type="text"
                size="small"
                @click="topNotice(record)"
              >
                置顶
              </a-button>
              <a-button
                v-else
                type="text"
                size="small"
                @click="topNotice(record)"
              >
                取消置顶
              </a-button>
              <a-button type="text" size="small" @click="deleteNotice(record)">
                删除
              </a-button>
            </template>
          </a-table-column>
        </template>
      </a-table>
    </a-card>
  </div>
</template>

<script lang="ts" setup>
  import { ref, reactive } from 'vue';
  import { QuillEditor } from '@vueup/vue-quill';
  import '@vueup/vue-quill/dist/vue-quill.snow.css';
  import { Message } from '@arco-design/web-vue';

  // 变量声明区块 START =======

  // 后台请求 URL
  const API_URL = 'http://127.0.0.1:5000/api';

  // 搜索变量
  const searchTitle = ref('');

  // 对话框显示调节变量
  const visibleAddModal = ref(false);
  const visibleEditModal = ref(false);

  // 对话框表单变量
  const noticeForm = reactive({
    NoticeTitle: '',
    NoticeDate: '',
    NoticeReadnum: '',
    NoticeContent: '',
    isTop: false,
  });

  // 表格表头变量
  const noticeColumes = [
    {
      title: '序号',
      dataIndex: 'noticeId',
    },
    {
      title: '通知标题',
      dataIndex: 'noticeTitle',
    },
    {
      title: '发表日期',
      dataIndex: 'noticeDate',
    },
    {
      title: '已读数量',
      dataIndex: 'noticeReadnum',
    },
    {
      title: '操作',
      slotname: 'operation',
    },
  ];

  // 表格数据变量
  const noticeTableData = reactive([]);

  // 变量声明区块 END =======

  // 方法声明区块 START =======

  // 初始化表格数据
  const loadTableData = () => {
    fetch(`${API_URL}/notice_list`, {
      method: 'GET',
      mode: 'cors',
      headers: {
        'Content-Type': 'application/json',
      },
    })
      .then((response) => response.json())
      .then((json) => {
        noticeTableData.splice(0, noticeTableData.length);
        for (let i = 0; i < json.length; i += 1) {
          noticeTableData[i] = json[i];
        }
      })
      .catch((error) => {
        Message.error('Error:', error);
      });
  };

  // 添加通知按钮 --> 打开添加通知表单
  const addNotice = () => {
    visibleAddModal.value = true;
    noticeForm.NoticeTitle = ' ';
    noticeForm.NoticeContent = ' ';
  };

  // 按钮方法

  // 添加企业账户OK按钮 --> 确定添加企业账户
  const addNoticeOk = () => {
    fetch(`${API_URL}/notice/0`, {
      method: 'PUT',
      mode: 'cors',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        noticeTitle: noticeForm.NoticeTitle,
        noticeDate: new Date().toLocaleString('zh-CN'),
        noticeReadnum: '0',
        noticeContent: noticeForm.NoticeContent,
        isTop: false,
      }),
    })
      .then((response) => response.json())
      .then((json) => {
        Message.info(json);
        loadTableData();
      })
      .catch((error) => {
        Message.error('Error:', error);
      });
  };

  // 添加通知Cancel按钮 --> 取消添加通知
  const addNoticeCancel = () => {
    visibleAddModal.value = false;
  };

  // 编辑通知按钮 --> 打开通知编辑表单  
  const editNotice = (record) => {
    visibleEditModal.value = true;
    noticeForm.NoticeTitle = record.noticeTitle;
    noticeForm.NoticeContent = record.noticeContent;
  };

  // 编辑通知OK按钮 --> 确定通知
  const editNoticeOk = (record) => {
    fetch(`${API_URL}/notice/${record.noticeId}`, {
      method: 'PUT',
      mode: 'cors',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        noticeTitle: noticeForm.NoticeTitle,
        noticeContent: noticeForm.NoticeContent,
      }),
    })
      .then((response) => response.json())
      .then((json) => {
        Message.info(json);
        loadTableData();
      })
      .catch((error) => {
        Message.error('Error:', error);
      });
  };

  // 编辑通知Cancel按钮 --> 取消编辑通知
  const editNoticeCancel = () => {
    visibleAddModal.value = false;
  };

  // 删除通知按钮
  const deleteNotice = (record) => {
    fetch(`${API_URL}/notice/${record.noticeId}`, {
      method: 'DELETE',
      mode: 'cors',
      headers: {
        'Content-Type': 'application/json',
      },
    })
      .then((response) => response.json())
      .then((json) => {
        Message.info(json);
        loadTableData();
      })
      .catch((error) => {
        Message.error('Error:', error);
      });
  };

  // 根据通知内容进行搜索按钮
  const searchNotice = () => {
    fetch(`${API_URL}/notice_search_by_title`, {
      method: 'GET',
      mode: 'cors',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        noticeTitle: searchTitle,
      }),
    })
      .then((response) => response.json())
      .then((json) => {
        noticeTableData.splice(0, noticeTableData.length);
        for (let i = 0; i < json.length; i += 1) {
          noticeTableData[i] = json[i];
        }
      })
      .catch((error) => {
        Message.error('Error:', error);
      });
  };

  const topNotice = (e) => {
    e.isTop = !e.isTop;
  };

  // 方法声明区块 END =======

  // 页面加载时调用方法  =======
  loadTableData();
</script>

<style scoped lang="less">
  .container {
    padding: 0 20px 20px 20px;
  }
</style>
