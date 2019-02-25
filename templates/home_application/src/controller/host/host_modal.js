export default {
    name: 'host_modal',
    props: {
        modalData: {
            status: false,
            row: {},
            title: '',
            is_create: true
      },
    },
    data() {
        return {
          item: {
            biz_list: [],
            host_list: [],
          },
          value: '',
          condition: '',
          textcontent: '',
          bk_biz_id: '',
          host_conf: '',
          remark: '',
        }
    },
    mounted() {
      // this.item.biz_list = [{'id': 4, 'name': 'sun'}]
      // console.log(this.item)
      this.search_biz()
      console.log(this.item)
    },
    watch: {
        // 'modalData.status'() {
        //     // alert(this.$store.state.test);
        //     // console.log('created',this.$refs.user_modal);
        //     this.item = this.$copy(this.modalData.row);
        // },
    },
    methods: {
        search_biz() {
                this.loading = true;
                this.$http.post('search_biz', {condition: this.condition}).then(res => {
                    this.loading = false;
                    if (res.result) {
                        // this.item.id = res.data;
                        this.item.biz_list = res.data;
                        console.log(this.item)
                    } else {
                        this.$message.error(res.message);
                    }
                })
        },
        search_host_list(bk_biz_id) {
            this.loading = true;
                this.$http.post('search_host_list', {bk_biz_id: bk_biz_id}).then(res => {
                    this.loading = false;
                    if (res.result) {
                        // this.item.id = res.data;
                    // this.item.host_list = [{'id': 888, 'name': 'pppp'}]
                    this.item.host_list = res.data
                    // console.log(this.item.host_list)
                    } else {
                        this.$message.error(res.message);
                    }
                })
        },
        save() {
            if (this.modalData.is_create) {
                this.add();
            } else {
                this.modify();
            }
            this.modalData.status = false;
        },
        add() {
            this.loading = true;
            this.$http.post('create_host', { 'bk_biz_id': this.bk_biz_id, 'host_conf': this.host_conf, 'remark': this.remark }).then(res => {
                this.loading = false;
                if (res.result) {
                    // this.item.id = res.data;
                    this.modalData.status = false;
                    this.search_biz()
                    this.$emit('save', {})
                } else {
                    this.$message.error(res.message);
                }
            })
        },
        modify() {
            delete this.item._index;
            delete this.item._rowKey;
            this.loading = true;
            this.$http.post('update_user', this.item).then(res => {
                this.loading = false;
                if (res.result) {
                    this.$emit('save', {});
                    this.modalData.status = false;
                } else {
                    this.$message.error(res.message);
                }
            })
        },
        cancel() {
            // this.bk_biz_id = ''
            // this.host_conf = ''
            this.modalData.status = false;
            this.condition = '';
            this.textcontent = '';
            this.bk_biz_id = '';
            this.host_conf = '';
            this.remark = '';
        }
    }
}
