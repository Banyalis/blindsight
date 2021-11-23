var Backbone = require('backbone');
var _ = require('underscore');

var Base = require('front/components/Base/Base');

require('./MemoriesPopupResources.less');

module.exports = Base.extend({
    template: require('./MemoriesPopupResources.jinja'),

    el: '.MemoriesPopup-resources',

    initialize: function (options) {
        Base.prototype.initialize.call(this, options);
    }
});