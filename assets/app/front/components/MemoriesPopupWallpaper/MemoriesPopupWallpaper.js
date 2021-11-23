var Backbone = require('backbone');
var _ = require('underscore');

var Base = require('front/components/Base/Base');

require('./MemoriesPopupWallpaper.less');

module.exports = Base.extend({
    template: require('./MemoriesPopupWallpaper.jinja'),

    el: '.MemoriesPopup-wallpaper',

    initialize: function (options) {
        Base.prototype.initialize.call(this, options);
    }
});