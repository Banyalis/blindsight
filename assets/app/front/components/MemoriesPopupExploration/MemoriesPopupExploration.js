var Backbone = require('backbone');
var _ = require('underscore');

var Base = require('front/components/Base/Base');

require('./MemoriesPopupExploration.less');

module.exports = Base.extend({
    template: require('./MemoriesPopupExploration.jinja'),

    el: '.MemoriesPopup-exploration',

    initialize: function (options) {
        this.options = options || {}

        _.bindAll(this, 'sequencePreloader');

        this.$images = this.$('.MemoriesPopup-explorationImage');

        if (app.settings.isDesktop) {
            this.sequencePreloader();
            this.loadImages();
            this.startMousemove();
        }
        
        Base.prototype.initialize.call(this, options);
    },

    sequencePreloader: function () {
        // Don't look here, I'm ashamed :-D
        var count = 0;

        var innterval = setInterval(function () {
            if (count == 74) {
                clearInterval(innterval);

                this.$el.addClass('Loaded');
            } else {
                count++;
                this.$('.MemoriesPopup-explorationLoaderPercentage span').html(count);
            } 
        }.bind(this), 200);
    },

    loadImages: function () {
        this.$images.each(function () {
            var src = $(this).data('src');

            $(this).css({backgroundImage: 'url(' + src + ')'});
        });
    },

    startMousemove: function () {
        this.$mouseCatchContainer = this.options.$mouseCatchContainer || this.$el;

        this.$mouseCatchContainer.on('mousemove', function (e) {
            var containerWidth = this.$mouseCatchContainer.outerWidth();
            var x = e.pageX - $(e.currentTarget).offset().left;
            var ratio = Math.min(Math.max((x / containerWidth), 0), 0.999);
            var index = Math.floor(ratio * this.$images.length);

            this.$images.removeClass('isShow');
            this.$images.eq(index).addClass('isShow');
        }.bind(this));
    }
});