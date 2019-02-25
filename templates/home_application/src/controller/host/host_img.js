import G2 from '@/components/g2/cw-g2'
import CwTable from '@com/table/cw-table'
export default {
  name: 'g2',
  components: {
    G2, CwTable
  },
  data() {
    return {
      columns: [],
      dataList: [],
      ip: '',
      item: {
        line: {
          data: [{ 'name': '2019-01-08_16:00:03', 'value': 50.81 },
            { 'name': '2019-01-08_15:00:03', 'value': 26.81 },
          {'name': '2019-01-08_13:00:03', 'value': 10.81}]
        },
        round: {
          data: [{ 'name': '2019-01-08_16:00:03', 'value': 50.81 },
            { 'name': '2019-01-08_15:00:03', 'value': 26.81 },
          {'name': '2019-01-08_13:00:03', 'value': 10.81}]
        }
    }
    }
  },
  mounted () {
    this.init()
  },
  methods: {
    init() {
      this.columns = [
        {
          title: '文件系统',
          key: 'Filesystem',
        },
        {
          title: '盘大小',
          key: 'Size',
        },
        {
          title: '已用大小',
          key: 'Used',
        },
        {
          title: '使用率',
          key: 'Use%',
        },
        {
          title: '挂载点',
          key: 'Mounted',
        },
        {
          title: '操作',
          key: 'handle',
        },
      ];
      this.search()
    },
    search() {
      this.ip = this.$route.query.ip
            this.loading = true;
            this.$http.post('search_loadavg', {ip: this.ip}).then(res => {
                this.loading = false;
                if (res.result) {
                  this.item.line.data = res.load;
                  this.item.round.data = res.memory;
                  this.dataList = res.disk_list
                } else {
                    this.$message.error(res.message);
                }
            })
        },
  }
 }
