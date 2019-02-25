<script src="../../controller/user/user_modal.js"></script>
<template>
    <div id="user_modal" ref="user_modal">
        <Modal
            v-model="modalData.status"
            :title="modalData.title"
            footer-hide
            @on-ok="save"
            @on-cancel="cancel">
            <Form :label-width="80">
                <FormItem label="姓名">
                    <Input v-model="item.name" placeholder="请输入姓名"></Input>
                </FormItem>
                <FormItem label="性别">
                    <RadioGroup v-model="item.sex">
                        <Radio label="男">男</Radio>
                        <Radio label="女">女</Radio>
                    </RadioGroup>
                </FormItem>
                <FormItem label="账号">
                    <Input v-model="item.account" placeholder="请输入账号"></Input>
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
    #user_modal {
    }
</style>
