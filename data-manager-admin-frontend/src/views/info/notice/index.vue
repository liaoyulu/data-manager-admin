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
            v-model:visible="visible"
            width="50%"
            title="发布通知"
            @cancel="noticeCancel"
            @ok="noticeOk"
          >
            <a-form :model="noticeForm">
              <a-form-item field="noticeTitle" label="通知标题">
                <a-input v-model="noticeForm.noticeTitle" />
              </a-form-item>
              <QuillEditor
                theme="snow"
                toolbar="full"
                contentType="html"
                v-model:content="noticeForm.noticeContent"
                style="height: 500px"
              />
            </a-form>
          </a-modal>
        </a-col>
        <a-col :span="8">
          <a-input
            :style="{ width: '500px' }"
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
      <a-table :data="data" style="margin-top: 30px">
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
            data-index="readnum"
          ></a-table-column>
          <a-table-column title="操作">
            <template #cell="{ record }">
              <a-button type="text" size="small" @click="editNotice(record)">
                编辑
              </a-button>

              <a-modal
                v-model:visible="editAddVisible"
                @cancel="editNoticeCancel"
                @ok="editNoticeOk"
                title="编辑通知"
              >
                <a-form :model="noticeForm">
                  <a-form-item field="noticeTitle" label="通知标题">
                    <a-input v-model="noticeForm.noticeTitle" />
                  </a-form-item>
                  <QuillEditor
                    theme="snow"
                    toolbar="full"
                    contentType="html"
                    v-model:content="noticeForm.noticeContent"
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
import { dataTool, number } from 'echarts/core';
import { ref, reactive } from 'vue';
import { QuillEditor } from '@vueup/vue-quill';
import '@vueup/vue-quill/dist/vue-quill.snow.css';
import { max } from 'lodash';

const columns = [
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
    dataIndex: 'readnum',
  },
  {
    title: '操作',
    slotname: 'operation',
  },
];

const data = reactive([
  {
    noticeId: 1,
    noticeTitle: '下午三点到四点集中核酸',
    noticeDate: '2022/6/24 13:31:44',
    readnum: '322',
    noticeContent: 'wde',
    isTop: false,
  },
]);

const visible = ref(false);

const editAddVisible = ref(false);

const noticeForm = reactive({
  noticeId: 0,
  noticeTitle: '',
  noticeDate: '',
  readnum: '',
  noticeContent: '',
  isTop: false,
});

const addNotice = () => {
  visible.value = true;
  noticeForm.noticeTitle = ' ';
};

const noticeCancel = () => {
  visible.value = false;
};

const noticeOk = () => {
  let sum = 0;
  data.forEach((topElement) => {
    if (topElement.isTop) {
      sum += 1;
    }
  });
  const now = new Date().toLocaleString('zh-CN');
  const newItem = {
    noticeId: data.length + 1,
    noticeTitle: noticeForm.noticeTitle,
    noticeDate: now,
    readnum: '322',
    isTop: false,
  };
  data.splice(sum, 0, newItem);
};

const deleteNotice = (e) => {
  data.forEach((element, index) => {
    if (e.noticeId === element.noticeId) {
      data.splice(index, 1);
    }
  });
};

const editNotice = (e) => {
  editAddVisible.value = true;
  noticeForm.noticeId = e.noticeId;
  noticeForm.noticeTitle = e.noticeTitle;
};

const editNoticeOk = () => {
  for (let i = 0; i < data.length; i += 1) {
    if (data[i].noticeId === noticeForm.noticeId) {
      data[i].noticeTitle = noticeForm.noticeTitle;
    }
  }
};

const topNotice = (e) => {
  if (!e.isTop) {
    data.forEach((element, index) => {
      if (e.noticeId === element.noticeId) {
        element.isTop = !element.isTop;
        data.unshift(element);
        data.splice(index + 1, 1);
      }
    });
  } else {
    let sum = 0;
    data.forEach((topElement) => {
      if (topElement.isTop) {
        sum += 1;
      }
    });
    console.log(sum);
    data.forEach((element, index) => {
      if (e.noticeId === element.noticeId) {
        console.log(e.noticeId);
        console.log(element.isTop);
        element.isTop = !element.isTop;
        data.splice(index, 1);
        data.splice(sum, 0, element);
        console.log(element.isTop);
      }
    });
  }
  /*
  data.forEach((element, index) => {
    if (!element.isTop) {
      console.log(e.isTop);
      if (e.noticeId === element.noticeId) {
        element.isTop = !element.isTop;
        console.log(element.isTop);
        data.unshift(element);
        data.splice(index + 1, 1);
      } else {
        console.log(e.isTop);
        let sum = 0;
        data.forEach((topElement) => {
          if (topElement.isTop) {
            sum += 1;
          }
          console.log(sum);
          if (e.noticeId === element.noticeId) {
            element.isTop = !element.isTop;
            data.splice(sum , 0, element);
            data.splice(index, 1);
          }
        });
      }
        else {
        let sum = 0;
        for (let j = 0; j <= data.length; j += 1) {
          if (data[j].isTop) {
            sum += 1;
          }
        }
        if (e.noticeId === data[i].noticeId) {
          data[i].isTop = !data[i].isTop;
          data.splice(sum - 1, 0, data[i]);
          data.splice(i + 1, 1);
        }
      }  
    }
  });
  */
};
</script>


<style scoped lang="less">
.container {
  padding: 0 20px 20px 20px;
}
</style>