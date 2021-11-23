var Backbone = require('backbone');
var _ = require('underscore');

var Base = require('front/components/Base/Base');

require('./MemoriesPopupCredits.less');

module.exports = Base.extend({
    template: require('./MemoriesPopupCredits.jinja'),

    el: '.MemoriesPopup-credits',

    initialize: function (options) {
        Base.prototype.initialize.call(this, options);
    }
});