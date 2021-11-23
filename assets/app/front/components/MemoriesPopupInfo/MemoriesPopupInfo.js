var Backbone = require('backbone');
var _ = require('underscore');

var Base = require('front/components/Base/Base');

require('./MemoriesPopupInfo.less');

module.exports = Base.extend({
    template: require('./MemoriesPopupInfo.jinja'),

    el: '.MemoriesPopup-info',

    initialize: function (options) {
        Base.prototype.initialize.call(this, options);
    }
});