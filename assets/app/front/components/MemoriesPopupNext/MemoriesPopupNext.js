var Backbone = require('backbone');
var _ = require('underscore');

var Base = require('front/components/Base/Base');

require('./MemoriesPopupNext.less');

module.exports = Base.extend({
    template: require('./MemoriesPopupNext.jinja'),

    el: '.MemoriesPopup-next',

    initialize: function (options) {
        Base.prototype.initialize.call(this, options);
    }
});