import Vue from 'vue'
import Urls from 'django_js_control/reverse.js';
import moment from 'moment';

// import SvgView from './components/SvgView.vue';
// import BackView from './components/BackView.vue';
// import EditView from './components/EditView.vue';
// import HideView from './components/HideView.vue';
// import SectionView from './components/SectionView.vue';
// import InputView from './components/InputView.vue';
// import CheckboxView from './components/CheckboxView.vue';
// import TextareaView from './components/TextareaView.vue';
// import SaveView from './components/SaveView.vue';
// import MediumEditor from './components/MediumEditor.vue';
// import ImageUploadView from './components/ImageUploadView.vue';
// import ListEditView from './components/ListEditView/ListEditView.vue';
// import CloseView from './components/CloseView.vue';
// import SortView from './components/SortView.vue';
// import PopupView from './components/PopupView.vue';
// import SelectView from './components/SelectView.vue';
// import ExpandView from './components/ExpandView.vue';
// import DatePickerView from './components/DatePickerView.vue';
// import ContentEditor from './components/ContentEditor/ContentEditor.vue';
// import ClientsList from './components/ClientsList.vue';
import VueAppend from 'vue-append';
import {HandleDirective} from 'vue-slicksort';

let cid = 1;

Object.defineProperty( Array.prototype, "last", {
    enumerable: false,
    configurable: false,
    writable: false,
    value: function() {
        return this[ this.length - 1 ];
    }
} );

function formatDate(value, format) {
    if (value) {
        return moment(String(value)).format(format || 'MM/DD/YYYY')
    } else {
        return value
    }
}

Vue.mixin({
    directives: {sort: HandleDirective},
    // components: {
    //     HideView, SvgView, BackView, EditView, SectionView, InputView, TextareaView, SaveView, MediumEditor,
    //     ImageUploadView, ListEditView, CloseView, SortView, PopupView, SelectView, ContentEditor, ExpandView,
    //     DatePickerView, CheckboxView, ClientsList
    // },
    methods: {
        static(url) {
            return app.settings.staticUrl + url;
        },
        urlStatic(url) {
            return `url('${app.settings.staticUrl + url}'`;
        },
        generateCid() {
            return `cid${++cid}`;
        },
        reorder(list) {
            return list.map((item, index) => ({...item, order: index}))
        },
        reorderObject(list) {
            return { ...this.reorder(Object.values(list)) }
        },
        formatDate
    },
    computed: {
        documentTitle() {
            return this.makeDocumentTitle();
        }
    },
    data: function () {
        return {
            ...(app.settings || {}),
            Urls
        }
    }
});

Vue.filter('formatDate', formatDate);

Vue.use(VueAppend);

Vue.directive('click-outside', {
    bind: function (el, binding, vnode) {
        el.clickOutsideEvent = function (event) {
            // here I check that click was outside the el and his childrens
            if (!(el == event.target || el.contains(event.target))) {
                // and if it did, call method provided in attribute value
                vnode.context[binding.expression](event);
            }
        };
        document.body.addEventListener('click', el.clickOutsideEvent)
    },
    unbind: function (el) {
        document.body.removeEventListener('click', el.clickOutsideEvent)
    },
});
/*
let pageTitleObjects = [];
function refreshPageTitles();
Vue.directive('pageTitle', {
    bind: function (el, binding, vnode) {
        pageTitleObjects.push(pageTitleObjects)
        el.clickOutsideEvent = function (event) {
            // here I check that click was outside the el and his childrens
            if (!(el == event.target || el.contains(event.target))) {
                // and if it did, call method provided in attribute value
                vnode.context[binding.expression](event);
            }
        };
        document.body.addEventListener('click', el.clickOutsideEvent)
    },
    unbind: function (el) {
        document.body.removeEventListener('click', el.clickOutsideEvent)
    },
});
*/
