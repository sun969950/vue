// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import axios from 'axios'

import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import iViewUI from 'iview';
import 'iview/dist/styles/iview.css';
import Echarts from 'echarts'
import G2 from '@antv/g2';
import store from './store'
import $ from 'jquery'

Vue.use(ElementUI);
Vue.use(iViewUI);
Vue.use(Echarts);
Vue.prototype.$echarts = Echarts;
Vue.prototype.$ = $;
Vue.prototype.$copy = function (val) {
    return JSON.parse(JSON.stringify(val))
};
Vue.config.productionTip = false;
axios.defaults.baseURL = window.siteUrl;
axios.defaults.withCredentials = true;
Vue.prototype.$http = axios;
axios.interceptors.request.use(config => {
    config.headers['X-Requested-With'] = 'XMLHttpRequest';
    let regex = /.*cwcsrftoken=([^;.]*).*$/;
    config.headers['X-CSRFToken'] = document.cookie.match(regex) === null ? null : document.cookie.match(regex)[1];
    return config
});

axios.interceptors.response.use(response => {
    // 登录重定向begin
    // let resUrl = response.request.responseURL;
    // if (resUrl.indexOf('/login/') !== -1) {
    //     let login_url = resUrl.split('?')[0] + '?c_url=' + window.location.href;
    //     window.location.href = login_url
    // }
    // 登录重定向end
    if (response.status !== 200) {
        return {
            code: response.status,
            message: '请求异常，请刷新重试',
            result: false
        }
    }
    return response.data
}, error => {
    return {
        code: 500,
        message: '未知错误，请刷新重试',
        error: error,
        result: false
    }
});

/* eslint-disable no-new */
new Vue({
    el: '#app',
    router,
    store,
    components: {App},
    template: '<App/>'
});
