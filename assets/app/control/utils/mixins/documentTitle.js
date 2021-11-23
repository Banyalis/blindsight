function _refreshDocumentTitle(newVal) {
    document.title = (newVal || '');
}

function makeDocumentTitle(page, subpage) {
    if (page && subpage) {
        return `True CMS — ${page}: ${subpage}`
    }
    if (page) {
        return `True CMS — ${page}`
    }
    return `True CMS`
}

function updateTitle() {
    try {
        _refreshDocumentTitle(window.router.currentRoute.matched.last().instances.default.documentTitle);
    } catch {
        //_refreshDocumentTitle(makeDocumentTitle())
    }
}

export default {
    methods: {
        makeDocumentTitle,
        refreshDocumentTitle(newVal) {
            if (this.$router.currentRoute.matched.last().instances.default === this) {
                _refreshDocumentTitle(newVal);
            }
        }
    },
    computed: {
        /*documentTitle() {
            return this.makeDocumentTitle();
        }*/
    },
    watch: {
        documentTitle(newVal) {
            this.refreshDocumentTitle(newVal);
        }
    },
    mounted() {
        this.refreshDocumentTitle(this.documentTitle);
    },
};
export { updateTitle };

/*$(document).ready(function() {
    window.router.afterEach(updateTitle);
})*/
