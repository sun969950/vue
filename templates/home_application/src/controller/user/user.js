import CwTable from '@com/table/cw-table'
import UserModal from '@/views/user/user_modal'

export default {
    name: 'user',
    components: {
        CwTable, UserModal
    },
    data() {
        return {
            loading: false,
            condition: '',
            userList: [],
            columns: [],
            modalData: {
                status: false,
                row: {},
                title: '编辑'
            }
        }
    },
    mounted() {
        this.init();
    },
    methods: {
        init() {
            this.columns = [
                {
                    title: '姓名',
                    key: 'name'
                },
                {
                    title: '年龄',
                    key: 'age'
                },
                {
                    title: '账号',
                    key: 'account'
                },
                {
                    title: '性别',
                    key: 'sex'
                },
                {
                    title: '创建时间',
                    key: 'when_created'
                },
                {
                    title: '操作',
                    render: (h, params) => {
                        return h('div', [
                            h('Button', {
                                props: {
                                    type: 'error',
                                    size: 'small'
                                },
                                style: {
                                    marginRight: '5px'
                                },
                                on: {
                                    click: () => {
                                        this.del(params.row, params.index)
                                    }
                                }
                            }, '删除'),
                            h('Button', {
                                props: {
                                    type: 'info',
                                    size: 'small'
                                },
                                on: {
                                    click: () => {
                                        this.edit(params.row, params.index)
                                    }
                                }
                            }, '编辑')
                        ]);
                    }
                }
            ];
            this.search();
        },
        search() {
            this.loading = true;
            this.$http.post('search_user', {condition: this.condition}).then(res => {
                this.loading = false;
                if (res.result) {
                    this.userList = res.data;
                } else {
                    this.$message.error(res.message);
                }
            })
        },
        add() {
            this.$store.state.test = true;
            this.modalData = {
                status: true,
                row: {},
                title: '添加用户',
                is_create: true
            }
        },
        edit(row, index) {
            this.modalData = {
                status: true,
                row: row,
                title: '修改用户',
                is_create: false
            }
        },
        save() {
            this.search();
        },
        del(row, index) {
            this.$Modal.confirm({
                title: '确认删除吗',
                content: '',
                onOk: () => {
                    this.loading = true;
                    this.$http.get('delete_user?id=' + row.id).then(res => {
                        this.loading = false;
                        if (res.result) {
                            this.userList.splice(index, 1)
                        } else {
                            this.$message.error(res.message);
                        }
                    })
                }
            });
        }
    }
}
