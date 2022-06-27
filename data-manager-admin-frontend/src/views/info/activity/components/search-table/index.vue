<template>
  <div class="container">
      <a-table
        row-key="activityId"
        :data="data"
      >
        <template #columns>
          <a-table-column
            title="序号"
            data-index="activityId"
          >
          </a-table-column>
          <a-table-column
            title="活动封面"
            data-index="activityCoverImg"
          >
          <template #cell="{ rowIndex }">
            <a-image
            width="60"
            :src="data[rowIndex].activityCoverImg"
            />
          </template>
          </a-table-column>
          <a-table-column
            title="活动标题"
            data-index="activityTitle"
          >
          </a-table-column>
          <a-table-column
            title="活动时间"
            data-index="activityTime"
          >
          </a-table-column>
          <a-table-column
            title="活动地点"
            data-index="activityPlace"
          >
          </a-table-column>
          <a-table-column
            title="发布时间"
            data-index="publishTime"
          >
          </a-table-column>
          <a-table-column
            title="操作"
            data-index="operations"
          >
          <template #cell>
            <a-button type="text" size="small">
              编辑
            </a-button>
            <a-button type="text" size="small">
              置顶
            </a-button>
            <a-button type="text" size="small">
              删除
            </a-button>
          </template>
          </a-table-column>
        </template>
      </a-table>
    <!-- <a-table :columns="columns" :data="data">
      <template #activityId="{ rowIndex }">
        {{ data[rowIndex].activityId }}  
      </template>
      <template #activityCoverImg="{ rowIndex }">
        {{ data[rowIndex].activityTitle }}  
      </template>
      <template #activityTitle="{ rowIndex }">
        {{ data[rowIndex].activityTitle }}  
      </template>
    </a-table> -->
  </div>
</template>

<script lang="ts" setup>
  import { ref, reactive } from 'vue';

  const columns = [{
      title: '序号',
      dataIndex: 'activityId',
      slotName: 'activityId'
    }, {
      title: '活动封面',
      dataIndex: 'activityCoverImg',
    }, {
      title: '活动标题',
      dataIndex: 'activityTitle',
    }, {
      title: '活动时间',
      dataIndex: 'activityTime',
    }, {
      title: '活动地点',
      dataIndex: 'activityPlace',
    }, {
      title: '发布时间',
      dataIndex: 'publishTime',
    }];
  
  const data = reactive([
    {
      activityId: '1',
      activityCoverImg: 'https://p1-arco.byteimg.com/tos-cn-i-uwbnlip3yd/a8c8cdb109cb051163646151a4a5083b.png~tplv-uwbnlip3yd-webp.webp',
      activityTitle: '标题1',
      activityTime: '时间1',
      activityPlace: '地点1',
      publishTime: '时间1',
    },
    {
      activityId: '2',
      activityCoverImg: 'https://p1-arco.byteimg.com/tos-cn-i-uwbnlip3yd/a8c8cdb109cb051163646151a4a5083b.png~tplv-uwbnlip3yd-webp.webp',
      activityTitle: '标题2',
      activityTime: '时间2',
      activityPlace: '地点2',
      publishTime: '时间2',
    },
    ]);
</script>

<script lang="ts">
  export default {
    name: 'SearchTable',
  };
</script>

<style scoped lang="less">
  .container {
    padding: 0 20px 20px 20px;
  }
  :deep(.arco-table-th) {
    &:last-child {
      .arco-table-th-item-title {
        margin-left: 16px;
      }
    }
  }
</style>
