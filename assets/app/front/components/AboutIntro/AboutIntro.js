var Backbone = require('backbone');
var _ = require('underscore');

var Base = require('front/components/Base/Base');

require('./AboutIntro.less');

module.exports = Base.extend({
    template: require('./AboutIntro.jinja'),

    el: '.AboutIntro',

    initialize: function (options) {
        Base.prototype.initialize.call(this, options);
    }
});