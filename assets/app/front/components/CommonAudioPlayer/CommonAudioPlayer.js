var Backbone = require('backbone');
var _ = require('underscore');

var Base = require('front/components/Base/Base');

require('./CommonAudioPlayer.less');

module.exports = Base.extend({
    template: require('./CommonAudioPlayer.jinja'),

    el: '.CommonAudioPlayer',

    events: {
        'click .CommonAudioPlayer-controlsButton': 'playAudio'
    },

    initialize: function (options) {
        this.audio = this.$('audio');
        this.circle = this.$('.CommonAudioPlayer-controlsProgress path');
        this.getCircle = this.circle.get(0);
        this.totalLength = this.getCircle.getTotalLength();

        this.circle.attr({
            'stroke-dasharray': this.totalLength,
            'stroke-dashoffset': this.totalLength,
        });

        this.audio.on('timeupdate', function () {
            var currentTime = this.audio[0].currentTime;
            var maxduration = this.audio[0].duration;
            var calc = this.totalLength - (currentTime / maxduration * this.totalLength);

            this.circle.attr('stroke-dashoffset', calc);
        }.bind(this));

        this.audio.on('ended', function () {
            this.$el.removeClass('isPlaying');
            this.circle.attr('stroke-dashoffset', this.totalLength);
        }.bind(this));

        Base.prototype.initialize.call(this, options);
    },

    playAudio: function () {
        if (this.audio[0].paused) {
            $('audio').each(function (index, el) {
                $('.CommonAudioPlayer').removeClass('isPlaying');
                $('audio')[index].pause();
            });
            $('.CommonVideoPlayer video').each(function (index, el) {
                $('.CommonVideoPlayer-inner').removeClass('Cursor-pause').addClass('Cursor-play');
                $('.CommonVideoPlayer video')[index].pause();
            });
            this.$el.removeClass('isPlaying');
            this.audio[0].play();
            this.$el.removeClass('isPaused');
            this.$el.addClass('isPlaying');
        } else {
            this.audio[0].pause();
            this.$el.removeClass('isPlaying');
            this.$el.addClass('isPaused');
        }
    }
});