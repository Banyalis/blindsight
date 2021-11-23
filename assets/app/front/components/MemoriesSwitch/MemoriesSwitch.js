var Backbone = require('backbone');
var _ = require('underscore');

var Base = require('front/components/Base/Base');

require('./MemoriesSwitch.less');

var gsap = require('gsap').gsap;

module.exports = Base.extend({
    template: require('./MemoriesSwitch.jinja'),

    el: '.MemoriesSwitch',

    events: {
        'click .MemoriesSwitch-item': 'changeGrid'
    },

    initialize: function (options) {
        _.bindAll(this, 'toggleSpiral', 'triggerMemoryOpen', 'triggerMemoryClose');

        if (!app.settings.isMobile) {
            app.vent.on('memoryOpen', this.triggerMemoryOpen);
            app.vent.on('memoryClose', this.triggerMemoryClose);
        }

        Base.prototype.initialize.call(this, options);
    },

    changeGrid: function (e) {
        var tl = gsap.timeline();
        var $switchItem = this.$('.MemoriesSwitch-item');
        var $memoriesNav = $('.MemoriesNav');
        var $memoriesItem = $('.MemoriesNav-item');
        var $memoriesItemVideo = $memoriesItem.find('video');

        this.$('.MemoriesSwitch-item.isActive').removeClass('isActive');
        $(e.currentTarget).addClass('isActive');
        $switchItem.addClass('isDisabled');

        setTimeout(function () {
            $switchItem.removeClass('isDisabled');
        }.bind(this), 2000);

        $memoriesItem.removeClass('onHover');
        $memoriesItemVideo[0].pause();
        $memoriesItemVideo[0].currentTime = 0;

        tl.to($memoriesItem, .3, {
            autoAlpha: 0,
            scale: 0
        }, '0');

        setTimeout(function () {
            if ($memoriesNav.hasClass('isGrid')) {
                $memoriesNav.removeClass('isGrid').addClass('isSpiral');
                $memoriesItem.not($('.inCenter')).removeClass('Cursor-next').addClass('Cursor-increase');
                this.toggleSpiral(true);

                tl.to($memoriesItem, .3, {
                    autoAlpha: 1,
                    scale: 1,
                    clearProps: 'all'
                }, '.5');
            } else {
                $('.MemoriesNav.isSpiral').removeClass('isSpiral');
                $memoriesNav.addClass('isGrid');
                $memoriesItem.removeClass('Cursor-increase').addClass('Cursor-next');
                this.toggleSpiral(false);

                tl.staggerTo($memoriesItem, .3, {
                    autoAlpha: 1,
                    scale: 1,
                    clearProps: 'all'
                }, .1, '0');
            }
        }.bind(this), 300);

        e.preventDefault();
    },

    toggleSpiral: function (isEnabled) {
        if (isEnabled) {
            app.els.$body.removeClass('enabledScroll');
            app.vent.trigger('enabledSpiralScroll');
        } else {
            app.els.$body.addClass('enabledScroll');
            app.vent.trigger('disabledSpiralScroll');
        }
    },

    triggerMemoryOpen: function () {
        this.$el.addClass('isHidden');
    },

    triggerMemoryClose: function () {
        this.$el.removeClass('isHidden');
    }
});