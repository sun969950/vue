import CwTable from '@com/table/cw-table'
import HostModal from '@/views/host/host_modal'
import HostModalEdit from '@/views/host/host_modal2'
export default {
    name: 'host',
    components: {
        CwTable, HostModal, HostModalEdit
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
            },
            modalDataEdit: {
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
                    title: '主机IP',
                    key: 'host_ip'
                },
                {
                    title: '主机名称',
                    key: 'host_name'
                },
                {
                    title: '所属业务',
                    key: 'business'
                },
                {
                    title: '备注',
                    key: 'remark'
                },
                {
                    title: '操作系统类型',
                    key: 'os'
                },
                {
                    title: '操作',
                    render: (h, params) => {
                        return h('div', [
                            h('Button', {
                                props: {
                                    type: 'info',
                                    size: 'small'
                                },
                                style: {
                                    marginRight: '5px'
                                },
                                on: {
                                    click: () => {
                                      this.edit(params.row, params.index)
                                    }
                                }
                            }, '修改'),
                            h('Button', {
                                props: {
                                    type: 'success',
                                    size: 'small',
                                    to: {path: '/host_img', query: {ip: params.row.host_ip}}
                                },
                                style: {
                                    marginRight: '5px'
                                },
                                // on: {
                                //     click: () => {
                                //       this.look(params.row, params.index)
                                //     }
                                // }
                            }, '查看性能'),
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
                        ]);
                    }
                }
            ];
            this.search();
        },
        search() {
            this.loading = true;
            this.$http.post('search_host_config', {condition: this.condition}).then(res => {
                this.loading = false;
                if (res.result) {
                    this.userList = res.data;
                    console.log('ttttttttttt', this.userList)
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
            this.modalDataEdit = {
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
                    this.$http.get('delete_host?id=' + row.id).then(res => {
                        console.log(row.id)
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
