var Backbone = require('backbone');
var _ = require('underscore');

var Base = require('front/components/Base/Base');

require('./MemoriesPopupVideo.less');

var CommonVideoPlayer = require('front/components/CommonVideoPlayer/CommonVideoPlayer.js');

module.exports = Base.extend({
    template: require('./MemoriesPopupVideo.jinja'),

    el: '.MemoriesPopupVideo',

    VIEWS_TO_REGISTER: {
        'CommonVideoPlayer': {
            selector: '.CommonVideoPlayer', viewConstructor: CommonVideoPlayer
        }
    },

    initialize: function (options) {
        Base.prototype.initialize.call(this, options);

        this.$el.on('mousemove', function () {
            if (this.$('.CommonVideoPlayer-inner:hover').length == false) {
                $('.Cursor').removeClass('isPause isPlay');
            }
        }.bind(this));
    }
});