<template>
    <div id="user" v-loading="loading">
        <div class="op-nav">
            <div class="op-search">
                <Input search enter-button placeholder="请输入姓名" v-model="condition" @on-search="search()"/>
            </div>
            <div class="op-add">
                <Button type="primary" @click="add">新增用户</Button>
            </div>
        </div>
        <CwTable
            :columns="columns"
            :data="userList"
            cutHeight="40">
        </CwTable>
        <UserModal :modal-data="modalData" @save="save"></UserModal>
    </div>
</template>
<script src="../../controller/user/user.js"></script>
<style lang="scss" scoped>
    #user {
        height: 100%;
        width: 100%;
        padding: 10px;
        .op-nav {
            height: 40px;
            .op-search {
                float: left;
                width: 250px;
            }
            .op-add {
                float: right;
            }
        }
    }
</style>
