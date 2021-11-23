var Backbone = require('backbone');
var _ = require('underscore');

var Base = require('front/components/Base/Base');

require('./MemoriesPopupChat.less');

var CommonAudioPlayer = require('front/components/CommonAudioPlayer/CommonAudioPlayer.js');

module.exports = Base.extend({
    template: require('./MemoriesPopupChat.jinja'),

    el: '.MemoriesPopup-chat',

    VIEWS_TO_REGISTER: {
        'CommonAudioPlayer': {
            selector: '.CommonAudioPlayer', viewConstructor: CommonAudioPlayer
        }
    },

    events: {
        'click .MemoriesPopup-chatItemImageZoomOpen': 'openImageZoom',
        'click .MemoriesPopup-chatItemImageZoomClose': 'closeImageZoom'
    },

    initialize: function (options) {
        _.bindAll(this, 'closeOnKey');

        app.vent.on('wheelOffset', function (x) {
            this.wheelOffset = x;
        }.bind(this));

        app.vent.on('gsapOffset', function (x) {
            this.gsapOffset =- x;
        }.bind(this));

        Base.prototype.initialize.call(this, options);
    },

    openImageZoom: function (e) {
        if (app.settings.isDesktop) {
            this.$imageZoom = $(e.currentTarget).next();

            this.$('.MemoriesPopup-chatItemImageZoom img').each(function () {
                var src = $(this).data('src');

                $(this).attr('src', src);
            });

            this.$imageZoom.addClass('isOpen');
            $('.Cursor').removeClass('isRedZone');
            app.vent.trigger('zoomOpen');

            if (app.els.$body.hasClass('isDragEnd')) {
                this.$imageZoom.css('left', this.gsapOffset + 'px');
            } else {
                this.$imageZoom.css('left', this.wheelOffset + 'px');
            }

            app.els.$document.on('keydown', this.closeOnKey);
        }
    },

    closeImageZoom: function () {
        if (app.settings.isDesktop) {
            this.$imageZoom.removeClass('isOpen').removeAttr('style');
            app.vent.trigger('zoomClose');
            app.els.$document.off('keydown', this.closeOnKey);
        }
    },

    closeOnKey: function () {
        switch (event.keyCode) {
    
        case 27:
            event.returnValue = false;
            event.keyCode = 0;
            this.closeImageZoom();
            break;
        }
    }
});