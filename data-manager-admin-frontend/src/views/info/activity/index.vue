<template>
  <div class="container">
    <Breadcrumb :items="['menu.info', 'menu.info.activity']" />
    <a-card>
      <a-form :model="formData">
        <a-row :gutter="24" class="action-panel" justify="start">
          <a-col :span="4">
            <a-button type="primary" @click="addActivity">
            <template #icon>
                <icon-plus />
            </template>
            添加活动
            </a-button>
            <a-modal 
              v-model:visible="formData.visible" 
              @ok="addActivityOk" 
              @cancel="addActivityCancel"
              width="60%"
              title="活动内容编辑器">
              <a-row :gutter="24" justify="start">
                <a-col :span="12">
                  <a-form-item 
                  field="activityTitle"
                  label='活动标题'
                  >
                  <a-input 
                  v-model="formData.activityTitle"
                  placeholder="请输入活动标题"
                  />
                  </a-form-item> 
                </a-col>
                <a-col :span="12">
                <a-form-item 
                  field="activityPlace"
                  label="活动地点">
                  <a-input
                  v-model="formData.activityPlace"
                  placeholder="请输入活动地点"
                  />
                </a-form-item>
                </a-col>
              </a-row>
              <a-row :gutter="24" justify="start">
                <a-col :span="12">
                  <a-form-item
                    field="activityTime"
                    label="活动时间">
                    <a-range-picker
                      v-model="formData.activityTime"
                    />
                  </a-form-item>
                </a-col>
                <a-col :span="12">
                <a-form-item 
                    label="活动封面">
                    <a-upload 
                    action="/" 
                    draggable 
                    list-type="picture-card" 
                    :limit="1"/>
                </a-form-item>
                </a-col>
              </a-row>
              <QuillEditor 
                theme="snow" 
                toolbar="full" 
                contentType="html"
                v-model:content="formData.activityContent"
                style="height: 500px;"/>
            </a-modal>
          </a-col>
          <a-col :span="8">
            <a-input
            v-model="formData.searchTitle"
            placeholder="请输入待搜索的活动标题"
            />
          </a-col>
          <a-col :span="4">
            <a-button @click="searchActivity">
            <template #icon>
                <icon-search />
            </template>
            搜索
            </a-button>
          </a-col>
        </a-row>
        <a-divider></a-divider>
        <SearchTable/>
      </a-form>
    </a-card>
  </div>
</template>

<script lang="ts" setup>
  import { ref } from 'vue';
  import { QuillEditor } from '@vueup/vue-quill'
  import '@vueup/vue-quill/dist/vue-quill.snow.css';
  import SearchTable from './components/search-table/index.vue';
  

  const formData = ref({
    visible: false,
    searchTitle: '',
    activityTitle: '',
    activityTime: [],
    activityPlace: '',
    activityContent: '',
  });

  const addActivity = () => {
    formData.value.visible = true
  };

  const searchActivity = () => {
    alert(formData.value.searchTitle)
  };

  const addActivityOk = () => {
    alert(formData.value.activityTitle)
    alert(formData.value.activityTime)
    alert(formData.value.activityPlace)
    alert(formData.value.activityContent)
    formData.value.visible = false
  }

  const addActivityCancel = () => {
    formData.value.visible = false
  }
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
  .panel {
    background-color: var(--color-bg-2);
    border-radius: 4px;
    overflow: auto;
  }
  .editor-card {
    width: 80%;
    margin-left: auto;
    margin-right: auto;
  }
</style>