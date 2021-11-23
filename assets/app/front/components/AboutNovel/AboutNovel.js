var Backbone = require('backbone');
var _ = require('underscore');

var Base = require('front/components/Base/Base');

require('./AboutNovel.less');

module.exports = Base.extend({
    template: require('./AboutNovel.jinja'),

    el: '.AboutNovel',

    initialize: function (options) {
        Base.prototype.initialize.call(this, options);
    }
});