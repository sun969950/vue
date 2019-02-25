<template>
    <div id="home">
        <span>{{msg}}</span>
    </div>
</template>

<script>
    export default {
        name: 'home',
        data() {
            return {
                msg: '欢迎使用嘉维蓝鲸开发框架'
            }
        }
    }
</script>

<style lang="scss" scoped>
    #home {
        background: url('../assets/img/control.png') repeat;
        height: 100%;
        width: 100%;
        text-align: center;
        span {
            display: inline-block;
            color: #fff;
            margin-top: 15%;
            font-size: 30px;
        }
    }
</style>
