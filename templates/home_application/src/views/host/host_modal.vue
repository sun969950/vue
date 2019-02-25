<script src="../../controller/host/host_modal.js"></script>
<template>
    <div id="host_modal" ref="host_modal">
        <Modal
            v-model="modalData.status"
            :title="modalData.title"
            footer-hide
            @on-ok="save"
            @on-cancel="cancel">
            <Form :label-width="80">
                <FormItem label="选择业务">
                  <Select v-model="bk_biz_id" style="width:400px" @on-change='search_host_list(bk_biz_id)'>
                    <Option v-for="item in item.biz_list" :value="item.bk_biz_id" :key="item.bk_biz_id">{{ item.bk_biz_name }}</Option>
                  </Select>
                    <!--<Input v-model="item.name" placeholder="请输入姓名"></Input>-->
                </FormItem>
                <FormItem label="选择主机">
                  <Select v-model="host_conf" style="width:400px">
                    <Option v-for="item in item.host_list" :value="item" :key="item.bk_host_innerip">{{ item.bk_host_innerip }}</Option>
                  </Select>
                    <!--<Input v-model="item.name" placeholder="请输入姓名"></Input>-->
                </FormItem>
                <FormItem label="备注">
                    <Input v-model="remark" type="textarea" placeholder="Enter something..." />
                </FormItem>
            </Form>
            <div style="width: 100%;text-align: center;">
                <Button type="primary" @click="save">保存</Button>
                <Button @click="cancel" style="margin-left: 8px">取消</Button>
            </div>
        </Modal>
    </div>
</template>
<style lang="scss" scoped>

</style>
