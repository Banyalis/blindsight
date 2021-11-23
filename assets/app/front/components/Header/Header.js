var Backbone = require('backbone');
var _ = require('underscore');

var Base = require('front/components/Base/Base');

require('./Header.less');

var gsap = require('gsap').gsap;

module.exports = Base.extend({
    template: require('./Header.jinja'),

    el: '.Header',

    events: {
        'click .Header-openMenu': 'openMobileMenu',
        'click .Header-closeMenu': 'closeMobileMenu',
        'click .Header-menuItem': 'setActivePage',
        'click .Header-menuButton': 'openPopupVideo'
    },

    initialize: function (options) {
        _.bindAll(this, 'headerAnimate', 'triggerMemoryOpen', 'triggerMemoryClose', 'triggerHeaderShow', 'triggerHeaderHidden', 'triggerZoomOpen', 'triggerZoomClose');

        app.vent.on('loader', this.headerAnimate);

        if (!app.settings.isMobile) {
            app.vent.on('memoryOpen', this.triggerMemoryOpen);
            app.vent.on('memoryClose', this.triggerMemoryClose);
            app.vent.on('headerShow', this.triggerHeaderShow);
            app.vent.on('headerHidden', this.triggerHeaderHidden);
            app.vent.on('zoomOpen', this.triggerZoomOpen);
            app.vent.on('zoomClose', this.triggerZoomClose);
        }
        
        this.$menu = this.$('.Header-menuWrapper');

        Base.prototype.initialize.call(this, options);
    },

    headerAnimate: function () {
        gsap.from(this.$el, .5, {
            opacity: 0,
            y: -30,
            clearProps: 'all'
        });
    },

    openMobileMenu: function () {
        var tl = gsap.timeline();

        this.$menu.addClass('isOpen');

        tl.to(this.$menu, .2, {
            autoAlpha: 1
        }, '0');

        tl.from(this.$('.Header-closeMenu'), .3, {
            opacity: 0,
            y: -50
        }, '0');

        tl.staggerFrom(this.$('.Header-menuItem'), .3, {
            opacity: 0,
            y: 50
        }, .2, '0');

        tl.staggerTo(this.$('.Header-menuItemSeparator'), .5, {
            width: '100%'
        }, .2, '0');

        tl.from(this.$('.Header-menuButtonWrapper'), .3, {
            opacity: 0,
            y: -50
        }, '.6');
    },

    closeMobileMenu: function () {
        this.$menu.removeClass('isOpen');

        gsap.to(this.$menu, .2, {
            autoAlpha: 0
        });

        gsap.to(this.$('.Header-menuItemSeparator'), 0, {
            clearProps: 'width'
        });
    },

    setActivePage: function (e) {
        var $menuItem = $(e.currentTarget);
        var menuItemId = $menuItem.data('id').toString();

        if (menuItemId == 'index') {
            this.setClass('IndexPage');
        } else if (menuItemId == 'memories') {
            this.setClass('MemoriesPage');
        } else if (menuItemId == 'about') {
            this.setClass('AboutPage');
        }

        if (this.$menu.hasClass('isOpen')) {
            var tl = gsap.timeline();

            tl.to(this.$menu, .2, {
                autoAlpha: 0
            }, '.5');

            tl.to(this.$('.Header-menuItemSeparator'), 0, {
                clearProps: 'width'
            }, '.5');
        };
    },

    triggerMemoryOpen: function () {
        this.$el.addClass('isDarkTheme');
    },

    triggerMemoryClose: function () {
        this.$el.removeClass('isDarkTheme');
    },

    triggerHeaderShow: function () {
        gsap.to(this.$el, .5, {
            autoAlpha: 1,
            x: 0
        });
    },

    triggerHeaderHidden: function () {
        gsap.to(this.$el, .5, {
            autoAlpha: 0,
            x: -50
        });
    },

    triggerZoomOpen: function () {
        this.$el.hide();
    },

    triggerZoomClose: function () {
        this.$el.show();
    },

    openPopupVideo: function (e) {
        app.vent.trigger('openPopup');

        e.preventDefault();
    }
});