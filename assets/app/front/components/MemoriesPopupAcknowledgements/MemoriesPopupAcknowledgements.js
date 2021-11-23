var Backbone = require('backbone');
var _ = require('underscore');

var Base = require('front/components/Base/Base');

require('./MemoriesPopupAcknowledgements.less');

module.exports = Base.extend({
    template: require('./MemoriesPopupAcknowledgements.jinja'),

    el: '.MemoriesPopup-acknowledgements',

    initialize: function (options) {
        Base.prototype.initialize.call(this, options);
    }
});