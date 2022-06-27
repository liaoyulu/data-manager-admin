<template>
  <div class="container">
    <Breadcrumb :items="['menu.account', 'menu.account.staff']" />
    <a-card>
      <a-row :gutter="24" class="action-panel" justify="start">
        <a-col :span="8">
          <a-input
            v-model="inputStuff"
            :style="{ width: '500px' }"
            placeholder="输入姓名查询"
            allow-clear
          />
        </a-col>
        <a-col :span="4">
          <a-button @click="searchStuff">
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
          <a-table-column
            title="员工序号"
            data-index="stuffId"
          ></a-table-column>
          <a-table-column title="用户名" data-index="userName"></a-table-column>
          <a-table-column title="姓名" data-index="stuffName"></a-table-column>
          <a-table-column title="性别" data-index="sex"></a-table-column>
          <a-table-column
            title="出生年月"
            data-index="birthDate"
          ></a-table-column>
          <a-table-column title="操作">
            <template #cell="{ record }">
              <a-button type="text" size="small" @click="deleteStuff(record)">
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
import { forEach } from 'lodash';

const columns = [
  {
    title: '序号',
    dataIndex: 'stuffId',
  },
  {
    title: '用户名',
    dataIndex: 'userName',
  },
  {
    title: '姓名',
    dataIndex: 'stuffName',
  },
  {
    title: '性别',
    dataIndex: 'sex',
  },
  {
    title: '出生年月',
    dataIndex: 'birthDate',
  },
  {
    title: '操作',
    slotname: 'operation',
  },
];

const data = reactive([
  {
    stuffId: 1,
    userName: 'yoooo',
    stuffName: '刘玉茹',
    sex: '女',
    birthDate: '1988.7.8',
  },
  {
    stuffId: 2,
    userName: 'yoo0o',
    stuffName: '李志伟',
    sex: '男',
    birthDate: '1988.7.9',
  },
  {
    stuffId: 3,
    userName: 'yoooo',
    stuffName: '黄蝉兰',
    sex: '女',
    birthDate: '1990.7.8',
  },
]);

const stuffForm = reactive({
  stuffId: 0,
  userName: '',
  stuffName: '',
  sex: '',
  birthDate: '',
});

const inputStuff = ref('');

const deleteStuff = (e) => {
  data.forEach((element, index) => {
    if (e.stuffId === element.stuffId) {
      fetch(`http://127.0.0.1:5000/api/stuff/${data[index].stuffId}`, {
        method: 'DELETE',
        mode: 'cors',
        headers: {
          'Content-Type': 'application/json',
        },
      })
        .then((response) => response.json())
        .then((json) => {
          console.log(json);
          data.splice(index, 1);
        })
        .catch((error) => {
          console.error('Error:', error);
        });    
    }
  });
  /*
  for (let i = 0; i <= data.length; i += 1) {
    if (e.stuffId === data[i].stuffId) {
      data.splice(i, 1);
    }
  }
  */
};

const searchStuff = () => {
  fetch(`http://127.0.0.1:5000/api/search/Stuff/${inputStuff.value}`, {
    method: 'GET',
    mode: 'cors',
    headers: {
      'Content-Type': 'application/json',
    },
  })
    .then((response) => response.json())
    .then((json) => {
      console.log(json);
      console.log(data);
      data.splice(0, data.length);
      for (let i = 0; i < json.length; i += 1) {
        data[i] = json[i];
      }
    })
    .catch((error) => {
      console.error('Error:', error);
    });
};
</script>


<style scoped lang="less">
.container {
  padding: 0 20px 20px 20px;
}
</style>