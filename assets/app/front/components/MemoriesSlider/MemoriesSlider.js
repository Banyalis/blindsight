var Backbone = require('backbone');
var _ = require('underscore');

var Base = require('front/components/Base/Base');

require('./MemoriesSlider.less');

var gsap = require('gsap').gsap;
var Swiper = require('swiper/js/swiper');
require('swiper/css/swiper.css');

module.exports = Base.extend({
    template: require('./MemoriesSlider.jinja'),

    el: '.MemoriesSlider',

    initialize: function (options) {
        _.bindAll(this, 'sliderAnimate', 'memoriesSlider', 'triggerMemoryOpen', 'triggerMemoryClose');

        if (app.els.$body.hasClass('isInitialState')) {
            this.sliderAnimate();
        } else {
            app.vent.on('loader', this.sliderAnimate);
        }
        this.memoriesSlider();
        if (app.settings.isMobile) {
            app.vent.on('memoryOpen', this.triggerMemoryOpen);
            app.vent.on('memoryClose', this.triggerMemoryClose);
        }

        Base.prototype.initialize.call(this, options);
    },

    sliderAnimate: function () {
        gsap.from(this.$('.MemoriesSlider-inner'), .5, {
            opacity: 0,
            scale: .8,
            clearProps: 'all'
        });
    },

    memoriesSlider: function () {
        var $sliderHint = $('.MemoriesSlider-hint');
        var sliderOptions = {
            loop: false,
            speed: 500,
            watchSlidesProgress: true,
            on: {
                progress: function () {
                    var swiper = this;

                    for (var i = 0; i < swiper.slides.length; i++) {
                        var slideProgress = swiper.slides[i].progress;
                        var innerOffset = swiper.width * -0.1;
                        var innerTranslate = slideProgress * innerOffset;
                        
                        swiper.slides[i].style.transform = 'rotate(' + innerTranslate + 'deg)';
                    }
                },

                slideChange: function () {
                    if (swiper.activeIndex >= 1) {
                        $sliderHint.addClass('isHidden');
                    } else {
                        $sliderHint.removeClass('isHidden');
                    }
                },

                touchStart: function () {
                    var swiper = this;

                    for (var i = 0; i < swiper.slides.length; i++) {
                        swiper.slides[i].style.transition = '';
                    }
                },

                setTransition: function (speed) {
                    var swiper = this;

                    for (var i = 0; i < swiper.slides.length; i++) {
                        swiper.slides[i].style.transition = speed + 'ms';
                    }
                }
            },
            pagination: {
                el: '.swiper-pagination'
            },
        };

        var swiper = new Swiper('.MemoriesSlider-inner', sliderOptions);
    },

    triggerMemoryOpen: function () {
        this.$el.addClass('isHidden');
    },

    triggerMemoryClose: function () {
        this.$el.removeClass('isHidden');
    }
});