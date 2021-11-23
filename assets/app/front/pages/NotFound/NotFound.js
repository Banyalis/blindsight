var Backbone = require('backbone');
var _ = require('underscore');

var Page = require('front/pages/Page/Page');
var CommonVideoBackground = require('front/components/CommonVideoBackground/CommonVideoBackground.js');

require('./NotFound.less');

var gsap = require('gsap').gsap;

module.exports = Page.extend({
    template: require('./NotFound.jinja'),

    el: '.NotFound',

    initialize: function () {
        _.bindAll(this, 'errorAnimate');

        var videoBackground = new CommonVideoBackground({
            el: '.CommonVideo-background'
        });

        window.app.vent.on('loader', this.errorAnimate);
        this.lazyLoad();
        this.customCursor();
    },

    errorAnimate: function () {
        var tl = gsap.timeline();

        tl.from(this.$('.NotFound-nav'), .5, {
            opacity: 0,
            x: 30,
            clearProps: 'all'
        }, '0');

        tl.from(this.$('.NotFound-title'), .5, {
            opacity: 0,
            y: 30,
            clearProps: 'all'
        }, '.5');
    },

    render: function () {
        this.setTitle('Not Found');
    }
});