var Backbone = require('backbone');
var _ = require('underscore');

var Base = require('front/components/Base/Base');

require('./MemoriesPopupFilm.less');

// var Utils = require('front/utils/Utils');

module.exports = Base.extend({
    template: require('./MemoriesPopupFilm.jinja'),

    el: '.MemoriesPopup-film',

    events: {
        'click .MemoriesPopup-filmButton': 'openPopupVideo'
    },

    initialize: function (options) {
        // if (app.settings.isMobile) {
        //     clearTimeout(utilsTimer);

        //     var utilsTimer = setTimeout(function () {
        //         Utils.detectVideoAutoplayFeature(function (autoplaySupported) {
        //             if (!autoplaySupported) {
        //                 this.$('.MemoriesPopup-filmVideo').addClass('isHidden');
        //             }
        //         }.bind(this));
        //     }, 1000);
        // }

        Base.prototype.initialize.call(this, options);
    },

    openPopupVideo: function (e) {
        app.vent.trigger('openPopup');

        e.preventDefault();
    }
});