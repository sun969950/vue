export default {
    name: 'user_modal',
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
            item: {}
        }
    },
    watch: {
        'modalData.status'() {
            // alert(this.$store.state.test);
            // console.log('created',this.$refs.user_modal);
            this.item = this.$copy(this.modalData.row);
        },
    },
    methods: {
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
            this.$http.post('create_user', this.item).then(res => {
                this.loading = false;
                if (res.result) {
                    // this.item.id = res.data;
                    this.modalData.status = false;
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
            this.modalData.status = false;
        }
    }
}
