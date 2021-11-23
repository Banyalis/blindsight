var Backbone = require('backbone');
var _ = require('underscore');

var Base = require('front/components/Base/Base');

require('./AboutVideo.less');

// var Utils = require('front/utils/Utils');

module.exports = Base.extend({
    template: require('./AboutVideo.jinja'),

    el: '.AboutVideo',

    events: {
        'click .AboutVideo-playIcon, .AboutVideo-button': 'openPopupVideo'
    },

    initialize: function (options) {
        // Utils.detectVideoAutoplayFeature(function (autoplaySupported) {
        //     if (!autoplaySupported) {
        //         this.$el.addClass('isHidden');
        //     }
        // }.bind(this));

        Base.prototype.initialize.call(this, options);
    },

    openPopupVideo: function (e) {
        app.vent.trigger('openPopup');

        e.preventDefault();
    }
});