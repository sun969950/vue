import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/views/home'
import User from '@/views/user/user'
import Host from '@/views/host/host'
import Hostimg from '@/views/host/host_img'
// import Test from '@/views/test'

Vue.use(Router);

let router = new Router({
    routes: [
        {title: '首页', path: '/', name: 'home', component: Home},
        {title: '用户管理', path: '/user', name: 'user', component: User},
        {title: '主机配置', path: '/host', name: 'host', component: Host},
        {title: '主机性能', path: '/host_img', name: 'host_img', component: Hostimg}
        // {
        //     title: '报表',
        //     path: '/report',
        //     name: 'report',
        //     component: Report,
        //     children: [
        //         {title: '报表首页', path: '/report/home', name: 'report/home', component: ReportHome},
        //         {title: '报表中心', path: '/report/center', name: 'report/center', component: ReportCenter},
        //         {
        //             title: '报表分类',
        //             path: '/report/classification',
        //             name: 'report/classification',
        //             component: ReportClassification
        //         },
        //         {title: '报表详细', path: '/report/report', name: 'report/report', component: ReportReport},
        //         {title: '编辑报表', path: '/report/edit', name: 'report/edit', component: ReportEdit}
        //     ]
        // },
    ]
});

router.beforeEach((to, from, next) => {
    if (to.matched.length === 0) {
        from.name ? next({name: from.name}) : next('/');
    } else {
        next();
    }
});
export default router
