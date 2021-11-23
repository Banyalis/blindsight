var Backbone = require('backbone');
var _ = require('underscore');

var Base = require('front/components/Base/Base');

require('./MemoriesPopupModel.less');

module.exports = Base.extend({
    template: require('./MemoriesPopupModel.jinja'),

    el: '.MemoriesPopup-model',

    initialize: function (options) {
        _.bindAll(this, 'interactiveModel');

        this.interactiveModel();

        Base.prototype.initialize.call(this, options);
    },

    interactiveModel: function () {
        if ($('#api-frame').length >= 1) {
            var iframe = document.getElementById('api-frame');
            var modelId = '4c2f6379a0d84e2ea4f530f844be7018';
            var client = new Sketchfab(iframe);
    
            client.init(modelId, {
                success: function onSuccess (api) {
                    api.start();
                },
                scrollwheel: 0
            });
        }
    }
});