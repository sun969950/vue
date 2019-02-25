<script src="../../controller/host/host_modal2.js"></script>
<template>
    <div id="host_modal" ref="host_modal">
        <Modal
            v-model="modalDataEdit.status"
            :title="modalDataEdit.title"
            footer-hide
            @on-ok="save"
            @on-cancel="cancel">
            <Form :label-width="80">
                <FormItem label="业务信息">
                    <Input v-model="item.business" placeholder="" disabled></Input>
                </FormItem>
                <FormItem label="主机信息">
                    <Input v-model="item.host_ip" placeholder="" disabled></Input>
                </FormItem>
                <FormItem label="备注">
                    <Input v-model="item.remark" type="textarea" placeholder="Enter something..." />
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
