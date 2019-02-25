<template>
    <div id='app'>
        <title>{{title}}</title>
        <Header :title="title"></Header>
        <Container :style="{height: winHeight}"></Container>
    </div>
</template>

<script>
    import Header from '@/components/base/header'
    import Container from '@/components/base/container'
    import '@/assets/css/base.scss'
    import '@/assets/icon/cc-icon/style.css'
    import '@/assets/icon/bk-icon-2.0/iconfont.css'

    export default {
        name: 'App',
        components: {
            Header,
            Container
        },
        created() {
            let headerHeight = 60;
            if (window.innerHeight) {
                this.winHeight = window.innerHeight;
            }
            if (document.documentElement && document.documentElement.clientHeight && document.documentElement.clientWidth) {
                this.winHeight = document.documentElement.clientHeight;
            }
            this.winHeight = this.winHeight - headerHeight + 'px';
        },
        data() {
            return {
                title: '配置管理门户'
            }
        }
    }
</script>
<style>
</style>
