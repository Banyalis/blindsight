var Backbone = require('backbone');
var _ = require('underscore');

var Urls = require('django_js_front/reverse.js');

var Section = require('front/pages/Section/Section');
var AboutIntro = require('front/components/AboutIntro/AboutIntro.js');
var AboutCredits = require('front/components/AboutCredits/AboutCredits.js');
var AboutNovel = require('front/components/AboutNovel/AboutNovel.js');
var AboutPress = require('front/components/AboutPress/AboutPress.js');
var AboutVideo = require('front/components/AboutVideo/AboutVideo.js');
var CommonVideoBackground = require('front/components/CommonVideoBackground/CommonVideoBackground.js');
var CommonVideoPopup = require('front/components/CommonVideoPopup/CommonVideoPopup.js');

require('./AboutSection.less');

var gsap = require('gsap/dist/gsap').gsap;
var ScrollScene = require('scrollscene').ScrollScene;

module.exports = Section.extend({
    template: require('./AboutSection.jinja'),

    el: '.AboutSection',

    VIEWS_TO_REGISTER: {
        'AboutIntro': {
            selector: '.AboutIntro', viewConstructor: AboutIntro
        },
        'AboutCredits': {
            selector: '.AboutCredits', viewConstructor: AboutCredits
        },
        'AboutNovel': {
            selector: '.AboutNovel', viewConstructor: AboutNovel
        },
        'AboutPress': {
            selector: '.AboutPress', viewConstructor: AboutPress
        },
        'AboutVideo': {
            selector: '.AboutVideo', viewConstructor: AboutVideo
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

        _.bindAll(this, 'activateLogic', 'onScrollAnimation');

        if (this.options.server) {
            this.activateLogic();
        } else {
            this.apiUrl = Urls['front:api:about']();
            this.startAnimation();
        }
    },

    onScrollAnimation: function () {
        var animationOpacity = {
            autoAlpha: 0,
            clearProps: 'all'
        }

        var animationTransformX = Object.assign({
             x: 50
        }, animationOpacity);

        var animationTransformXNegative = Object.assign({
             x: -50
        }, animationOpacity);

        var animationTransformY = Object.assign({
             y: 50
        }, animationOpacity);

        this.$('.isAnimated').each(function (index, item) {
            var tl = gsap.timeline({ paused: true });

            if ($(item).find('.AboutIntro-title').length >= 1) {
                tl.from($(item).find($('.AboutIntro-title')), .5, Object.assign({}, animationTransformY), '0');
                tl.from($(item).find($('.AboutIntro-disclaimer')), .5, Object.assign({}, animationTransformXNegative), '.2');
                tl.from($(item).find($('.AboutIntro-text')), .5, Object.assign({}, animationTransformX), '.4');
            }
            
            if ($(item).find('.AboutCredits-title').length >= 1) {
                tl.from($(item).find($('.AboutCredits-title')), .5, Object.assign({}, animationTransformX), '0');
                tl.staggerFrom($(item).find($('.AboutCredits-listItem')), .4, Object.assign({}, animationTransformY), .1, '.2');
                tl.from($(item).find($('.AboutCredits-period')), .5, Object.assign({}, animationTransformX), '.9');
            }

            if ($(item).find('.AboutNovel-title').length >= 1) {
                tl.from($(item).find($('.AboutNovel-title')), .5, Object.assign({}, animationTransformX), '0');
                tl.from($(item).find($('.AboutNovel-text')), 1, Object.assign({}, animationOpacity), '.2');
                tl.from($(item).find($('.AboutNovel-buttonsItemWrapper')), .5, Object.assign({}, animationTransformY), '.4');
            }

            if ($(item).find('.AboutPress-title').length >= 1) {
                tl.from($(item).find($('.AboutPress-title')), .5, Object.assign({}, animationTransformX), '0');
                tl.from($(item).find($('.AboutPress-text, .AboutPress-image')), 1, Object.assign({}, animationOpacity), '.2');
                tl.staggerFrom($(item).find($('.AboutPress-buttonsItemWrapper')), .5, Object.assign({}, animationTransformY), .2, '.4');
            }

            if ($(item).find('.AboutVideo-playIcon').length >= 1) {
                tl.from($(item).find($('.AboutVideo video')), .5, Object.assign({}, animationOpacity), '0');
                tl.from($(item).find($('.AboutVideo-playIcon')), .5, Object.assign({
                    scale: .5
                }, animationOpacity), '.2');
                tl.from($(item).find($('.AboutVideo-buttonWrapper')), .5, Object.assign({}, animationTransformY), '.4');
                $(item).find($('video'))[0].play();
            }

            var offsetAnimation = 200;

            if (app.settings.isMobile) {
                offsetAnimation = 0;
            }

            var scrollScene = new ScrollScene({
                triggerElement: $(item)[0],
                triggerHook: 'onEnter',
                offset: offsetAnimation,
                scene: {
                    reverse: false,
                },
                gsap: {
                    timeline: tl
                },
                controller: {
                    vertical: false
                }
            })
        });
    },

    activateLogic: function () {
        if (app.els.$body.hasClass('isInitialState')) {
            this.onScrollAnimation();
        } else {
            app.vent.on('loader', this.onScrollAnimation);
        }
        this.googleAnalytics();
        this.lazyLoad();
        this.customCursor();
        this.enabledHorizontalScroll();
    },

    render: function () {
        this.setTitle('About');
        this.setClass('AboutPage');

        Section.prototype.render.call(this);
        this.activateLogic();
    },

    deactivate: function (params) {
        this.disabledHorizontalScroll();

        return Section.prototype.deactivate.call(this, params);
    }
});