var Backbone = require('backbone');
var _ = require('underscore');

var Base = require('front/components/Base/Base');

require('./MemoriesPopupLater.less');

module.exports = Base.extend({
    template: require('./MemoriesPopupLater.jinja'),

    el: '.MemoriesPopup-later',

    initialize: function (options) {
        Base.prototype.initialize.call(this, options);
    }
});