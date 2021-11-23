var Backbone = require('backbone');
var _ = require('underscore');

var Base = require('front/components/Base/Base');

require('./IndexIntro.less');

var gsap = require('gsap').gsap;

module.exports = Base.extend({
    template: require('./IndexIntro.jinja'),

    el: '.IndexIntro',

    events: {
        'click .Cursor-play': 'openPopupVideo'
    },

    initialize: function (options) {
        _.bindAll(this, 'introAnimate');

        if (app.els.$body.hasClass('isInitialState')) {
            this.introAnimate();
        } else {
            app.vent.on('loader', this.introAnimate);
        }

        Base.prototype.initialize.call(this, options);
    },

    introAnimate: function () {
        var tl = gsap.timeline();

        tl.staggerFrom(this.$('.IndexIntro-navItem'), .5, {
            opacity: 0,
            y: 20,
            clearProps: 'all'
        }, .3, '0');

        tl.from(this.$('.IndexIntro-alert'), .5, {
            opacity: 0,
            x: 20,
            clearProps: 'all'
        }, '.9');
    },

    openPopupVideo: function (e) {
        app.vent.trigger('openPopup');

        e.preventDefault();
    }
});