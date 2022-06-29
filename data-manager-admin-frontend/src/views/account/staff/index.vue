data-manager-admin<template>
  <div class="container">
    <Breadcrumb :items="['menu.account', 'menu.account.staff']" />
    <a-card>
      <a-row :gutter="24" class="action-panel" justify="start">
        <a-col :span="8">
          <a-input v-model="searchName" placeholder="输入姓名查询" allow-clear />
        </a-col>
        <a-col :span="4">
          <a-button @click="searchStaff">
            <template #icon>
              <icon-search />
            </template>
            搜索
          </a-button>
        </a-col>
      </a-row>
      <a-divider></a-divider>
      <a-table :data="staffTableData" style="margin-top: 30px">
        <template #columns>
          <a-table-column title="员工序号" data-index="staffId"></a-table-column>
          <a-table-column title="用户名" data-index="staffUserName"></a-table-column>
          <a-table-column title="姓名" data-index="staffName"></a-table-column>
          <a-table-column title="性别" data-index="staffSex"></a-table-column>
          <a-table-column title="出生年月" data-index="staffBirthDate"></a-table-column>
          <a-table-column title="操作">
            <template #cell="{ record }">
              <a-button type="text" size="small" @click="deleteStaff(record)">
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
  import '@vueup/vue-quill/dist/vue-quill.snow.css';
  import { Message } from '@arco-design/web-vue';

  // 变量声明区块 START ======= 
  
  // 后台请求 URL
  const API_URL = 'http://127.0.0.1:5000/api';

  // 搜索变量
  const searchName = ref('');

  // 对话框表单变量
  const staffForm = reactive({
    StaffUserName: '',
    StaffName: '',
    StaffSex: '',
    StaffBirthDate: '',
  });


  // 表格表头变量
  const staffColumns = [
    {
      title: '序号',
      dataIndex: 'staffId',
    },
    {
      title: '用户名',
      dataIndex: 'staffUserName',
    },
    {
      title: '姓名',
      dataIndex: 'staffName',
    },
    {
      title: '性别',
      dataIndex: 'staffSex',
    },
    {
      title: '出生年月',
      dataIndex: 'staffBirthDate',
    },
    {
      title: '操作',
      slotname: 'operation',
    },
  ];
  // 表格数据变量
  const staffTableData = reactive([]);

  // 变量声明区块 END ======= 

  // 方法声明区块 START ======= 

  // 初始化表格数据
  const loadTableData = () => {
    fetch(`${API_URL}/staff_list`, {
      method: 'GET',
      mode: 'cors',
      headers: {
        'Content-Type': 'application/json',
      },
    })
    .then((response) => response.json())
    .then((json) => {
      console.log(json)
      staffTableData.splice(0, staffTableData.length);
      for (let i = 0; i < json.length; i += 1) {
        staffTableData[i] = json[i];
      }
    })
    .catch((error) => {
      console.error('Error:', error);
    });
  };

  const deleteStaff = (record) => {
    fetch(`${API_URL}/staff/${record.staffId}`, {
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

  const searchStaff = () => {
    fetch(`${API_URL}/staff_search_by_name`, {
      method: 'POST',
      mode: 'cors',
      headers: {
        'Content-Type': 'application/json',
      },
      body:JSON.stringify({
        staffName: searchName,
      })
    })
    .then((response) => response.json())
    .then((json) => {
      staffTableData.splice(0, staffTableData.length);
      for (let i=0; i<json.length; i+=1) {
        staffTableData[i] = json[i];
      }
    })
    .catch((error) => {
      Message.error('Error:', error);
    });
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