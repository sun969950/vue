export default {
    name: 'host_modal_edit',
    props: {
        modalDataEdit: {
            status: false,
            row: {},
            title: '',
            is_create: true
      },
    },
    data() {
        return {
          item: {
            // biz_list: [],
            // host_list: [],
          },
          remark: '',
          // value: '',
          // condition: '',
          // textcontent: '',
          // bk_biz_id: '',
          // host_conf: '',
          // remark: '',
        }
    },
    mounted() {
      // this.item.biz_list = [{'id': 4, 'name': 'sun'}]
      // console.log(this.item)
      // this.search_biz()
    },
    watch: {
      'modalDataEdit.status'() {
        if (this.modalDataEdit.status) {
            this.item = this.$copy(this.modalDataEdit.row);
          }
            // alert(this.$store.state.test);
            // console.log('created',this.$refs.user_modal);
            // this.item = this.$copy(this.modalDataEdit.row);
      },
    },
    methods: {
      search_biz() {
            this.loading = true;
            this.$http.post('search_biz', {condition: this.condition}).then(res => {
                this.loading = false;
                if (res.result) {
                    // this.item.id = res.data;
                    this.item.biz_list = res.data;
                } else {
                    this.$message.error(res.message);
                }
            })
      },
      search_host_list(bk_biz_id) {
        this.loading = true;
        console.log(bk_biz_id)
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
            if (this.modalDataEdit.is_create) {
                this.add();
            } else {
                this.modify();
            }
            this.modalDataEdit.status = false;
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
            this.$http.post('modify_host', { 'item': this.item }).then(res => {
                this.loading = false;
                if (res.result) {
                    this.$emit('save', {});
                    this.modalDataEdit.status = false;
                } else {
                    this.$message.error(res.message);
                }
            })
        },
        cancel() {
          // this.bk_biz_id = ''
          // this.host_conf = ''
            this.modalDataEdit.status = false;
            this.item = ''
        }
    }
}
