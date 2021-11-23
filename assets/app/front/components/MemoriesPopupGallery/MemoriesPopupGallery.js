var Backbone = require('backbone');
var _ = require('underscore');

var Base = require('front/components/Base/Base');

require('./MemoriesPopupGallery.less');

require('slick-carousel/slick/slick.min');
require('slick-carousel/slick/slick.css');

var Utils = require('front/utils/Utils');

module.exports = Base.extend({
    template: require('./MemoriesPopupGallery.jinja'),

    el: '.MemoriesPopup-galleryWrapper',

    events: {
        'click .MemoriesPopup-galleryZoomOpen': 'openGalleryZoom',
        'click .MemoriesPopup-galleryOverlay': 'openGalleryZoom',
        'click .MemoriesPopup-galleryZoomClose': 'closeGalleryZoom'
    },

    initialize: function (options) {
        _.bindAll(this, 'gallerySlider', 'imageMovement', 'closeOnKey');

        this.gallerySlider();
        this.imageMovement();

        app.vent.on('wheelOffset', function (x) {
            this.wheelOffset = x;
        }.bind(this));

        app.vent.on('gsapOffset', function (x) {
            this.gsapOffset =- x;
        }.bind(this));

        // if (app.settings.isMobile) {
        //     clearTimeout(utilsTimer);

        //     var utilsTimer = setTimeout(function () {
        //         Utils.detectVideoAutoplayFeature(function (autoplaySupported) {
        //             if (!autoplaySupported) {
        //                 this.$('.MemoriesPopup-galleryItemInner').addClass('isHidden');
        //             }
        //         }.bind(this));
        //     }, 1000);
        // }

        Base.prototype.initialize.call(this, options);
    },

    gallerySlider: function () {
        var $gallery = this.$('[data-gallery]');

        $gallery.slick({
            slidesToShow: 1,
            slidesToScroll: 1,
            dots: false,
            arrows: false,
            infinite: true,
            draggable: false,
            fade: true,
            speed: 1000,
            waitForAnimate: false
        });

        this.$('[data-gallery-prev]').on('click', function (e) {
            $gallery.slick('slickPrev');

            e.preventDefault();
        });

        this.$('[data-gallery-next]').on('click', function (e) {
            $gallery.slick('slickNext');

            e.preventDefault();
        });

        app.els.$document.on('keydown', function (e) {
            if (e.keyCode == 37) {
                $gallery.slick('slickPrev');
            }
            if (e.keyCode == 39) {
                $gallery.slick('slickNext');
            }
        });
    },

    openGalleryZoom: function () {
        if (app.settings.isDesktop) {
            this.$galleryZoom = this.$('.MemoriesPopup-galleryZoom');

            this.$('.MemoriesPopup-galleryZoomItemInner img').each(function () {
                var src = $(this).data('src');

                $(this).parent().css({backgroundImage: 'url(' + src + ')'});
            });

            this.$galleryZoom.addClass('isOpen');
            app.vent.trigger('zoomOpen');

            if (app.els.$body.hasClass('isDragEnd')) {
                this.$galleryZoom.css('left', this.gsapOffset + 'px');
            } else {
                this.$galleryZoom.css('left', this.wheelOffset + 'px');
            }
        
            app.els.$document.on('keydown', this.closeOnKey);
        }
    },

    closeGalleryZoom: function () {
        if (app.settings.isDesktop) {
            this.$galleryZoom.removeClass('isOpen');
            app.vent.trigger('zoomClose');
            app.els.$document.off('keydown', this.closeOnKey);
        }
    },

    closeOnKey: function () {
        switch (event.keyCode) {
    
        case 27:
            event.returnValue = false;
            event.keyCode = 0;
            this.closeGalleryZoom();
            break;
        }
    },

    imageMovement: function () {
        if (app.settings.isDesktop) {
            this.$('.MemoriesPopup-galleryZoomClose').on('mousemove', function (e) {
                var target = e.currentTarget.getBoundingClientRect();
                var mouseX = e.clientX - target.left;
                var mouseY = e.clientY - target.top;
                var xPercent = (mouseX / target.width) * 100;
                var yPercent = (mouseY / target.height) * 100;
    
                this.$('.MemoriesPopup-galleryZoomItemInner').css('background-position', (xPercent + '%' + yPercent + '%'));
            }.bind(this));
        }
    }
});