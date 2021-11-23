import Vue from 'vue';
import VueResource from 'vue-resource';
// import PageWrapper from './pages/PageWrapper.vue';
import svg4everybody from 'svg4everybody';
import objectFitImages from 'object-fit-images/dist/ofi.common-js.js';
import Promise from 'promise-polyfill';
import axios from 'axios';
import Cookies from 'js-cookie';
import ProgressBar from 'vuejs-progress-bar';
import VueClipboard from 'vue-clipboard2';

import './utils/utils';
import './styles/styles.less';

import store from './store';
import { router } from './router';
import 'babel-polyfill';

import Urls from 'django_js_control/reverse.js';
window.Urls = Urls;

import Vuelidate from 'vuelidate'
Vue.use(Vuelidate);

import smoothscroll from 'smoothscroll-polyfill';
smoothscroll.polyfill();

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
Vue.use(ProgressBar);
VueClipboard.config.autoSetContainer = true;
Vue.use(VueClipboard);

const App = new Vue({
    el: '#app',
    store,
    router,
    name: 'App',
    // render: h => h(PageWrapper),
    methods: {},
    created() {
        console.log('App created....');
    }
});





