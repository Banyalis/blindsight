var Backbone = require('backbone');
var _ = require('underscore');

var Base = require('front/components/Base/Base');

require('./CommonVideoPopup.less');

var CommonVideoPlayer = require('front/components/CommonVideoPlayer/CommonVideoPlayer.js');

var Plyr = require('plyr');

module.exports = Base.extend({
    template: require('./CommonVideoPopup.jinja'),

    el: '.CommonVideoPopup',

    events: {
        'click .CommonVideoPopup-close': 'closePopup',
    },

    VIEWS_TO_REGISTER: {
        'CommonVideoPlayer': {
            selector: '.CommonVideoPlayer', viewConstructor: CommonVideoPlayer
        }
    },

    initialize: function (options) {
        _.bindAll(this, 'openPopup', 'loadVideo', 'onVideoPlay', 'onVideoPause', 'triggerPopupShown', 'triggerPopupHidded');

        this.video = this.$('video');

        app.vent.on('openPopup', this.openPopup);

        this.VimeoPlayer = new Plyr('.VimeoPlayer', {
            controls: [
                'current-time',
                'progress',
                'duration',
                'fullscreen',
                'captions'
            ],
            tooltips: false,
            fullscreen: {
                enabled: true,
                iosNative: true,
                container: null
            }
        });

        if (!app.settings.isDesktop) {
            this.VimeoPlayer.on('click', function () {
                this.VimeoPlayer.togglePlay()
            }.bind(this));
        }

        Base.prototype.initialize.call(this, options);
    },

    openPopup: function () {
        // this.videoSrc = this.$('.CommonVideoPopup-inner').data('video-popup');
        
        // this.loadVideo();
        // this.video[0].play();
        this.$el.addClass('isOpen');
        this.VimeoPlayer.play();
        this.triggerPopupShown();
        // app.vent.trigger('disabledHorizontalScroll');

        this.$el.on('mousemove', function () {
            if (this.$('.CommonVideoPopup-inner:hover').length == false || $('.plyr__controls:hover').length == true) {
                $('.Cursor').removeClass('isPause isPlay');
            }
        }.bind(this));

        this.VimeoPlayer.on('play', this.onVideoPlay);
        this.VimeoPlayer.on('pause', this.onVideoPause);
        this.VimeoPlayer.on('ended', this.onVideoPause);
    },

    loadVideo: function () {
        if (this.loadInitiated) return;

        this.$('source').attr('src', this.videoSrc);
        this.video[0].load();

        this.loadInitiated = true;
    },

    onVideoPlay: function () {
        $('.Cursor').addClass('isPause').removeClass('isPlay');
    },

    onVideoPause: function () {
        $('.Cursor').addClass('isPlay').removeClass('isPause');
    },

    closePopup: function (e) {
        // this.video[0].pause();
        // this.video[0].currentTime = 0;
        this.$el.removeClass('isOpen');
        this.VimeoPlayer.stop();
        this.triggerPopupHidded();

        clearTimeout(timer);

        var timer = setTimeout(function () {
            $('.Cursor').removeClass('isPause isPlay');
        }, 100);
        // app.vent.trigger('enabledHorizontalScroll');

        e.preventDefault();
    },

    triggerPopupShown: function () {
        this.savedScroll = app.els.$window.scrollTop();

        app.vent.trigger('PopupShown');
        app.els.$window.scrollTop(0);
    },

    triggerPopupHidded: function () {
        app.vent.trigger('PopupHidded');
        app.els.$window.scrollTop(this.savedScroll);
    }
});