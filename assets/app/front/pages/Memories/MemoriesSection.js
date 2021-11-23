var Backbone = require('backbone');
var _ = require('underscore');

var Urls = require('django_js_front/reverse.js');

var Section = require('front/pages/Section/Section');
var MemoriesNav = require('front/components/MemoriesNav/MemoriesNav.js');
var MemoriesSlider = require('front/components/MemoriesSlider/MemoriesSlider.js');
var MemoriesSwitch = require('front/components/MemoriesSwitch/MemoriesSwitch.js');
var CommonVideoBackground = require('front/components/CommonVideoBackground/CommonVideoBackground.js');
var CommonVideoPopup = require('front/components/CommonVideoPopup/CommonVideoPopup.js');

require('./MemoriesSection.less');

module.exports = Section.extend({
    template: require('./MemoriesSection.jinja'),

    el: '.MemoriesSection',

    VIEWS_TO_REGISTER: {
        'MemoriesNav': {
            selector: '.MemoriesNav', viewConstructor: MemoriesNav
        },
        'MemoriesSlider': {
            selector: '.MemoriesSlider', viewConstructor: MemoriesSlider
        },
        'MemoriesSwitch': {
            selector: '.MemoriesSwitch', viewConstructor: MemoriesSwitch
        },
        'CommonVideoBackground': {
            selector: '.CommonVideo-background', viewConstructor: CommonVideoBackground
        },
        'CommonVideoPopup': {
            selector: '.CommonVideoPopup', viewConstructor: CommonVideoPopup
        }
    },

    initialize: function (options) {
        this.options = options || {};

        Section.prototype.initialize.call(this, options);

        _.bindAll(this, 'activateLogic');

        if (this.options.server) {
            this.activateLogic();
        } else {
            this.apiUrl = Urls['front:api:memories']();
            this.startAnimation();
        }
    },

    activateLogic: function () {
        this.lazyLoad();
        this.customCursor();
    },

    render: function () {
        this.setTitle('Memories');
        this.setClass('MemoriesPage');

        Section.prototype.render.call(this);
        this.activateLogic();
    }
});