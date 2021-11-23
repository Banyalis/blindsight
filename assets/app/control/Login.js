import Vue from 'vue';
import VueResource from 'vue-resource';
import svg4everybody from 'svg4everybody';
import objectFitImages from 'object-fit-images/dist/ofi.common-js.js';
import Promise from 'promise-polyfill';
import 'babel-polyfill';
import Cookies from 'js-cookie';
import axios from 'axios';

import LoginPage from './modules/login/Page.vue';

import './utils/utils';
import './styles/styles.less';


import Urls from 'django_js_control/reverse.js';
window.Urls = Urls;

svg4everybody({ polyfill: app.settings.hotReloading });
objectFitImages();

axios.interceptors.request.use(
    config => {
        config.headers['X-CSRFToken'] = Cookies.get('csrftoken') || $('meta[name="csrf-token"]').attr('content');
        return config;
    },
    error => Promise.reject(error)
);

Vue.use(VueResource);

const App = new Vue({
    el: '#app',
    name: 'App',
    render: h => h(LoginPage),
    methods: {},
    created() {
        console.log('Login app created....');
    }
});





