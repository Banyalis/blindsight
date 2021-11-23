var Backbone = require('backbone');
var _ = require('underscore');

var Base = require('front/components/Base/Base');

require('./MemoriesPopupNote.less');

module.exports = Base.extend({
    template: require('./MemoriesPopupNote.jinja'),

    el: '.MemoriesPopup-note',

    initialize: function (options) {
        Base.prototype.initialize.call(this, options);
    }
});