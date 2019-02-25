<template>
    <div id="user" v-loading="loading">
        <div class="op-nav">
            <div class="op-search">
                <Input search enter-button placeholder="请输入IP" v-model="condition" @on-search="search()"/>
            </div>
            <div class="op-add">
                <Button type="primary" @click="add">新增主机</Button>
            </div>
        </div>
        <CwTable
            :columns="columns"
            :data="userList"
            cutHeight="40">
        </CwTable>
        <HostModal :modal-data="modalData" @save="save"></HostModal>
        <HostModalEdit :modal-data-edit="modalDataEdit" @save="save"></HostModalEdit>
    </div>
</template>
<script src="../../controller/host/host.js"></script>
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
