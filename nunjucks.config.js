var _ = require('underscore');
var moment = require('moment-strftime');

module.exports = function (env) {
    var staticPath = '/static/';

    if (typeof window !== 'undefined') {
        staticPath = window.app.settings.staticUrl;
    }

    env.addGlobal('static', function (file) {
        return staticPath + file;
    }, true);

    env.addGlobal('url', function (name, params) {
        params = params || {};

        return Urls[name].apply(null, params.args);
    }, true);

    env.addGlobal('isMobile', function (name) {
        return app.settings.isMobile;
    });

    env.addGlobal('isTablet', function (name) {
        return app.settings.isTablet;
    });

    env.addFilter('jsonify', function (obj) {
        return JSON.stringify(obj);
    });

    env.addFilter('datetime', function (date, format) {
        return moment.parseZone(date).strftime(format);
    });
};
