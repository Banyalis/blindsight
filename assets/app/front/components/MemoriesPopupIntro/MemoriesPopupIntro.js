var Backbone = require('backbone');
var _ = require('underscore');

var Base = require('front/components/Base/Base');

require('./MemoriesPopupIntro.less');

module.exports = Base.extend({
    template: require('./MemoriesPopupIntro.jinja'),

    el: '.MemoriesPopup-intro',

    initialize: function (options) {
        Base.prototype.initialize.call(this, options);
    }
});