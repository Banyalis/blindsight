var Backbone = require('backbone');
var _ = require('underscore');

var Base = require('front/components/Base/Base');

require('./CommonVideoBackground.less');

module.exports = Base.extend({
    template: require('./CommonVideoBackground.jinja'),

    el: '.CommonVideo-background',

    initialize: function (options) {
        _.bindAll(this, 'videoLoad', 'triggerMemoryOpen', 'triggerMemoryClose');

        this.videoLoad();
        if (app.settings.isDesktop) {
            app.vent.on('memoryOpen', this.triggerMemoryOpen);
            app.vent.on('memoryClose', this.triggerMemoryClose);
        }

        Base.prototype.initialize.call(this, options);
    },

    videoLoad: function () {
        if (app.settings.isDesktop) {
            var $videoSources = this.$('video');

            $videoSources[0].setAttribute('src', $videoSources[0].getAttribute('data-src'));
            this.$('video').load();
        }
    },

    triggerMemoryOpen: function () {
        this.$('video')[0].pause();
    },

    triggerMemoryClose: function () {
        this.$('video')[0].play();
    }
});