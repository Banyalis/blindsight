var Backbone = require('backbone');
var _ = require('underscore');

var Base = require('front/components/Base/Base');

require('./CommonVideoPlayer.less');

module.exports = Base.extend({
    template: require('./CommonVideoPlayer.jinja'),

    el: '.CommonVideoPlayer',

    events: {
        'click .CommonVideoPlayer-inner': 'togglePlayback',
        'mousemove .CommonVideoPlayer-controlsTimeline': 'onTimelineMove',
        'click .CommonVideoPlayer-controlsTimeline': 'onTimelineClick',
    },

    initialize: function (options) {
        this.$video = this.$('video');

        this.$video.on('pause', function () {
            this.$('.CommonVideoPlayer-playback')
                .addClass('isPlay')
                .removeClass('isPause');
        }.bind(this));

        this.$video.on('play', function () {
            this.$('.CommonVideoPlayer-playback')
                .addClass('isPause')
                .removeClass('isPlay');
        }.bind(this));

        this.$video.on('timeupdate', function () {
            var percentage = (this.$video[0].currentTime / this.$video[0].duration) * 100;
            var time = Math.round(this.$video[0].currentTime);
            var minutes = Math.floor(time / 60);
            var seconds = time % 60;

            if (!isNaN(percentage)) {
                this.$('.CommonVideoPlayer-controlsTimelineProgress').css('width', percentage + '%');
                this.$('.CommonVideoPlayer-controlsCurrentTime')
                    .text(('00' + minutes)
                    .substring(Math.min(('' + minutes).length, 2)) + ':' + ('00' + seconds)
                    .substring(Math.min(('' + seconds).length, 2)));
                }
        }.bind(this));

        this.$video.on('loadedmetadata', function () {
            var time = Math.round(this.$video[0].duration);
            var minutes = Math.floor(time / 60);
            var seconds = time % 60;

            this.$('.CommonVideoPlayer-controlsDuration')
                .text(('00' + minutes)
                .substring(Math.min(('' + minutes).length, 2)) + ':' + ('00' + seconds)
                .substring(Math.min(('' + seconds).length, 2)));
        }.bind(this));

        Base.prototype.initialize.call(this, options);
    },

    togglePlayback: function () {
        this.$('.CommonVideoPlayer-image').addClass('isHide');

        if (this.$('.CommonVideoPlayer-playback').hasClass('isPause')) {
            this.$video[0].pause();
            // if (this.$el.hasClass('isPopupVideoPlayer')) {
            //     $('.Cursor').addClass('isPlay').removeClass('isPause');
            // }
            this.$('.CommonVideoPlayer-inner').addClass('Cursor-play').removeClass('Cursor-pause');
            $('.Cursor').addClass('isPlay').removeClass('isPause');
            
        } else {
            $('.CommonVideoPlayer video').each(function (index, el) {
                $('.CommonVideoPlayer video')[index].pause();
            });
            $('audio').each(function (index, el) {
                $('.CommonAudioPlayer').removeClass('isPlaying');
                $('audio')[index].pause();
            });
            this.$video[0].play();
            // if (this.$el.hasClass('isPopupVideoPlayer')) {
            //     $('.Cursor').addClass('isPause').removeClass('isPlay');
            // }
            this.$('.CommonVideoPlayer-inner').addClass('Cursor-pause').removeClass('Cursor-play');
            $('.Cursor').addClass('isPause').removeClass('isPlay');
        }
    },

    onTimelineMove: function (e) {
        var percentage = e.offsetX / this.$('.CommonVideoPlayer-controlsTimeline').width();

        if (!isNaN(percentage)) {
            this.$('.CommonVideoPlayer-controlsTimelineLine').css('left', e.offsetX);
        }
    },

    onTimelineClick: function (e) {
        var percentage = e.offsetX / this.$('.CommonVideoPlayer-controlsTimeline').width();
        var time = (this.$video[0].duration * percentage);

        this.$video[0].currentTime = time;
    }
});