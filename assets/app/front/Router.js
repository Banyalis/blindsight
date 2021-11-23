var Backbone = require('backbone');
var _ = require('underscore');

var Urls = require('django_js_front/reverse.js');

var Section = require('front/pages/Section/Section');
var SubSectionDummy = require('front/pages/Section/SubSectionDummy');

var IndexSection = require('front/pages/Index/IndexSection');
var MemoriesSection = require('front/pages/Memories/MemoriesSection');
var AboutSection = require('front/pages/About/AboutSection');
var NotFound = require('front/pages/NotFound/NotFound');
var MemoriesPopup = require('front/pages/MemoriesPopup/MemoriesPopup');

module.exports = Backbone.Router.extend({
    routes: {
        '': 'index',
        'memories(/)': 'memories',
        'about(/)': 'about',
        'memories/memory-:slug(/)': 'memoriesPopup',
    },

    index: function () {
        this.activate(IndexSection, {view: SubSectionDummy});
    },

    memories: function () {
        this.activate(MemoriesSection, {view: SubSectionDummy});
    },

    about: function () {
        this.activate(AboutSection, {view: SubSectionDummy});
    },

    notFound: function () {
        this.activate(NotFound);
    },

    memoriesPopup: function (slug) {
        this.activate(MemoriesSection, {
            view: MemoriesPopup,
            viewData: {slug: slug}
        });
    },

    activate: function (view, params) {
        params = params || {};

        // view is rendered on server
        if (!app.state.view) {
            params.server = true;
            params.inAnimated = false;
            app.state.viewConstructor = view;
            app.state.view = new view(params);
            app.state.view.activate();
            app.state.currentViewClass = view;

            return;
        }

        app.state.prevView = app.state.view;

        if (this.isSectionLogic(app.state.prevView, view)) {
            this.activateSectionLogic(view, params);
        } else {
            this.activateStandardLogic(view, params);
        }
    },

    // активация перехода с полной перезагрузкой и лоадером
    activateStandardLogic: function (view, params) {
        var newParams = _.defaults({server: false, inAnimated: true}, params);
        app.state.viewConstructor = view;

        var newView = new view(newParams);
        // var duration = params.fastNavigate ? 0 : ANIMATION_DURATION;

        return Promise.all([app.state.view.playOut({
            // duration: duration,
            // zoom: params.zoomNavigate,
            view: newView
        }), newView.loadData()])
            .then(function () {
                app.els.$content.css({minHeight: app.els.$content.height()});

                return app.state.view.deactivate({destroy: true});
            })
            .then(function () {
                app.state.isServer = false;
                app.state.view = newView;
                app.state.view.activate(newParams)
                    .then(function () {
                        app.els.$content.css({minHeight: ''});
                        $(window)
                            .scrollTop(0);

                        return app.state.view.playIn({
                            // duration: duration,
                            // zoom: params.zoomNavigate,
                            view: newView
                        });
                    });
            });

    },

    // navigation activation with popup
    activateSectionLogic: function (view, viewParams) {
        var view = viewParams.view;
        var params = _.omit(viewParams, 'view');
        params.server = false;
        params.inAnimated = true;
        app.state.isServer = false;

        if (viewParams.apiUrl) {
            params.viewData = {
                apiUrl: viewParams.apiUrl
            };
        }

        app.state.view.update(view, params);
    },


    isSectionLogic: function (prevView, view) {
        return app.state.prevView instanceof Section && app.state.prevView.constructor === view;
    },

    navigateBack: function () {
        Backbone.history.navigate(this.history[this.history.length - 1], {trigger: 'true'});
        this.history.pop(); //pop, after Backbone.history.navigate onroute listener add return url to history stack, remove it
    },

    start: function () {
        var is404 = app.els.$body.hasClass('Page404');
        var pushStateSupported = history && _.isFunction(history.pushState);


        this.history = [];

        this.listenTo(this, 'route', function (name, args) {
            //do not store popup urls in history, to force popup close to underlying page (even if there is a sequence of opened popups, especially years on awards)
            if (/Popup$/.test(name)) return;

            this.history.push(Backbone.history.fragment);
        }.bind(this));

        Backbone.history.start({pushState: pushStateSupported, silent: is404});

        if (is404) {
            this.notFound();
        }
    }
});
