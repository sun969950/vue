<template>
    <div id="g2">
        <div ref="main" id="main"></div>
    </div>
</template>

<script>
    import G2 from '@antv/g2';

    export default {
        name: 'g2',
        components: {},
        props: {
            type: { // 图表类型：line, pie, bar, loop
                default: 'line'
            },
            nameKey: {
                default: 'name'
            },
            valueKey: {
                default: 'value'
            },
            eventClick: {
                default: false
            },
            showEmpty: {
                default: true
            },
            showLabel: {
                default: true
            },
            paddingAuto: {
                default: true,
            },
            data: {
                default: function () {
                    return []
                    // return [
                    //     {name: '业务1', value: 0.270},
                    //     {name: '业务2', value: 0.115},
                    //     {name: '业务3', value: 0.120},
                    //     {name: '业务4', value: 0.350},
                    //     {name: '业务5', value: 0.150},
                    //     {name: '业务6', value: 0},
                    //     {name: '业务7', value: 0},
                    //     {name: '业务8', value: 0},
                    //     {name: '业务9', value: 0},
                    //     {name: '业务10', value: 0},
                    //     {name: '业务11', value: 0},
                    //     {name: '业务12', value: 0},
                    //     {name: '业务13', value: 0},
                    //     {name: '业务14', value: 0},
                    //     {name: '业务15', value: 0},
                    //     {name: '业务16', value: 0},
                    //     {name: '业务17', value: 0},
                    //     {name: '业务18', value: 0},
                    //     {name: '业务19', value: 0},
                    //     {name: '业务20', value: 0},
                    //     {name: '业务21', value: 0},
                    //     {name: '业务22', value: 0},
                    //     {name: '业务23', value: 0},
                    //     {name: '业务24', value: 0},
                    //     {name: '业务25', value: 0},
                    //     {name: '业务26', value: 0},
                    //     {name: '业务27', value: 0},
                    //     {name: '业务28', value: 0},
                    //     {name: '业务29', value: 0},
                    //     {name: '业务30', value: 0},
                    //     {name: '业务31', value: 0},
                    //     {name: '业务32', value: 0},
                    //     {name: '业务33', value: 0},
                    //     {name: '业务34', value: 0},
                    //     {name: '业务35', value: 0},
                    //     {name: '业务36', value: 0},
                    //     {name: '业务37', value: 0},
                    //     {name: '业务38', value: 0},
                    //     {name: '业务39', value: 0},
                    //     {name: '业务40', value: 0},
                    //     {name: '业务41', value: 0},
                    //     {name: '业务42', value: 0},
                    //     {name: '业务43', value: 0},
                    //     {name: '业务44', value: 0},
                    //     {name: '业务45', value: 0},
                    //     {name: '业务46', value: 0},
                    //     {name: '业务47', value: 0},
                    //     {name: '业务48', value: 0},
                    //     {name: '业务49', value: 0},
                    //     {name: '业务50', value: 0}
                    // ]
                }
            }
        },
        data() {
            return {
                chart: '',
                chartData: []
            }
        },
        watch: {
            data: function () {
                this.buildChart();
            },
            type: function () {
                this.buildChart();
            },
            showEmpty: function() {
                this.buildChart();
            }
        },
        mounted() {
            this.initChart();
            this.buildChart();
        },
        methods: {
            bar(chart, data) {
                chart.source(data);
                chart.interval().position(this.nameKey + '*' + this.valueKey).color(this.nameKey);
                chart.on('interval:click', ev => {
                    this.clickNode(ev)
                });
            },
            line(chart, data) {
                chart.source(data);
                chart.line().position(this.nameKey + '*' + this.valueKey);
            },
            pie(chart, data, showLoop) {
                chart.source(data, {
                    percent: {
                        formatter: function formatter(val) {
                            // val = val * 100 + '%';
                            return val;
                        }
                    }
                });
                let coordConf = {
                    radius: 0.8,
                };
                if (showLoop) {
                    coordConf.innerRadius = 0.5
                }
                chart.coord('theta', coordConf);
                chart.tooltip({
                    showTitle: false
                });
                let intervalStack = chart.intervalStack(
                ).position(
                    this.valueKey
                ).color(
                    this.nameKey
                ).label('value', {
                    formatter: function formatter(val, item) {
                        return item.point.name;
                    }
                }).tooltip(this.nameKey + '*' + this.valueKey, function (item, percent) {
                    // percent = percent * 100 + '%';
                    return {
                        name: item,
                        value: percent
                    };
                });
                chart.render();
                chart.on('interval:click', ev => {
                    this.clickNode(ev)
                });
            },
            initChart(data) {
                let width = this.$refs.main.offsetWidth;
                let height = this.$refs.main.offsetHeight;
                let conf = {
                    container: this.$refs.main,
                    width: width,
                    height: height
                };
                if (this.paddingAuto) {
                    conf.padding = 60;
                    conf.paddingTop = 0
                }
                this.chart = new G2.Chart(conf);
            },
            buildChart() {
                let chart = this.chart;
                let data = this.clearData(this.data);
                chart.legend(this.showLabel);
                switch (this.type) {
                    case 'line':
                        this.line(chart, data);
                        break;
                    case 'bar':
                        this.bar(chart, data);
                        break;
                    case 'pie':
                        this.pie(chart, data, false);
                        break;
                    case 'loop':
                        this.pie(chart, data, true);
                        break;
                    default:
                        this.bar(chart, data);
                        break
                }
                chart.render();
            },
            clearData() {
                let newData = [];
                if (!this.showEmpty) {
                    this.data.forEach(item => {
                        if (item[this.valueKey] !== 0) {
                            newData.push(item);
                        }
                    });
                    return newData
                } else {
                    return this.data;
                }
            },
            clickNode(e) {
                let origin = e.data._origin;
                if (this.eventClick) {
                    this.$emit('clickNode', origin)
                }
            }
        }
    }
</script>

<style scoped lang="scss">
    #g2 {
        width: 100%;
        height: 100%;
        #main {
            width: 100%;
            height: 100%;
        }
    }
</style>
