var Backbone = require('backbone');
var _ = require('underscore');

var Urls = require('django_js_front/reverse.js');

var Section = require('front/pages/Section/Section');
var IndexIntro = require('front/components/IndexIntro/IndexIntro.js');
var CommonVideoBackground = require('front/components/CommonVideoBackground/CommonVideoBackground.js');
var CommonVideoPopup = require('front/components/CommonVideoPopup/CommonVideoPopup.js');

require('./IndexSection.less');

module.exports = Section.extend({
    template: require('./IndexSection.jinja'),

    el: '.IndexSection',

    VIEWS_TO_REGISTER: {
        'IndexIntro': {
            selector: '.IndexIntro', viewConstructor: IndexIntro
        },
        'CommonVideoBackground': {
            selector: '.CommonVideo-background', viewConstructor: CommonVideoBackground
        },
        'CommonVideoPopup': {
            selector: '.CommonVideoPopup', viewConstructor: CommonVideoPopup
        }
    },

    initialize: function (options) {
        this.options = options || {};

        Section.prototype.initialize.call(this, options);

        _.bindAll(this, 'activateLogic');

        if (this.options.server) {
            this.activateLogic();
        } else {
            this.apiUrl = Urls['front:api:index']();
            this.startAnimation();
        }
    },

    activateLogic: function () {
        this.googleAnalytics();
        this.lazyLoad();
        this.customCursor();
        app.els.$body.addClass('enabledScroll');
    },

    render: function () {
        this.setTitle('Blindsight');
        this.setClass('IndexPage');

        Section.prototype.render.call(this);
        this.activateLogic();
    },

    deactivate: function (params) {
        app.els.$body.removeClass('enabledScroll');

        return Section.prototype.deactivate.call(this, params);
    }
});