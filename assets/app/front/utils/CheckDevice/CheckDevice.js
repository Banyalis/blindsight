var _ = require('underscore');

require('./CheckDevice.less');

module.exports = {
    initialize: function () {
        var html = document.querySelector('html');
        this.viewport = document.getElementById('viewport');

        var isHighDensity = this.isHighDensity();

        if (isHighDensity) {
            window.app.isRetina = true;
            html.className = html.className + ' isRetina';
        }

        var isIos = this.isIos();

        window.app.isIos = isIos;
        if (isIos) {
            html.className = html.className + ' isIos';
        }

        var isSafari = navigator.vendor && navigator.vendor.indexOf('Apple') > -1 &&
            navigator.userAgent && !navigator.userAgent.match('CriOS');

        window.app.isSafari = isSafari;
        if (isSafari) {
            html.className = html.className + ' isSafari';
        }

        var isIE = this.isIE();
        window.app.isIE = isIE;
        if (isIE) {
            html.className = html.className + ' isIE';
        }

        var isTouch = this.isTouch();
        window.app.isTouch = isTouch;
        if (isTouch) {
            html.className = html.className + ' isTouch';
        } else {
            html.className = html.className + ' isNotTouch';
        }

        window.app.deviceType = this.checkDeviceType();
        // html.classList.add('is' + this._capitalize(window.app.deviceType));

        window.addEventListener('resize', _.throttle(function () {
            var deviceType = this.checkDeviceType();

            if (deviceType !== window.app.deviceType) {
                app.vent.trigger('preChangeDeviceType', deviceType);

                // html.classList.remove('is' + this._capitalize(window.app.deviceType));
                window.app.deviceType = deviceType;
                // html.classList.add('is' + this._capitalize(deviceType));

                app.vent.trigger('changeDeviceType', deviceType);
            }
        }.bind(this), 100));
    },


    isHighDensity: function () {
        return ((window.matchMedia && (window.matchMedia('only screen and (min-resolution: 124dpi), only screen and (min-resolution: 1.3dppx), only screen and (min-resolution: 48.8dpcm)').matches || window.matchMedia('only screen and (-webkit-min-device-pixel-ratio: 1.3), only screen and (-o-min-device-pixel-ratio: 2.6/2), only screen and (min--moz-device-pixel-ratio: 1.3), only screen and (min-device-pixel-ratio: 1.3)').matches)) || (window.devicePixelRatio && window.devicePixelRatio > 1.3));
    },


    isIos: function () {
        return /iPad|iPhone|iPod/.test(navigator.userAgent) && !window.MSStream;
    },


    isIE: function () {
        if (navigator.userAgent.indexOf('MSIE') !== -1
            || navigator.appVersion.indexOf('Trident/') > 0) {
            return true;
        }

        if (/Edge/.test(navigator.userAgent)) {
            return true;
        }

        return false;
    },


    isTouch: function () {
        return 'ontouchstart' in document.documentElement;
    },


    checkDeviceType: function () {
        var indicator = document.querySelector('.u-StateIndicator');

        if (!indicator) {
            indicator = document.createElement('div');
            indicator.className = 'u-StateIndicator';
            document.body.appendChild(indicator);
        }

        var index = 1;

        // Для мобильного Firefox нужна отдельная проверка, т.к. при загрузке media query не срабатывает
        if (/Firefox/.test(navigator.userAgent) && /Mobile/.test(navigator.userAgent)) {
            index = 4;
        } else {
            index = parseInt(window.getComputedStyle(indicator).getPropertyValue('z-index'), 10);
        }

        var deviceTypes = {
            1: 'desktop',
            2: 'laptop',
            3: 'tablet',
            4: 'mobile'
        };

        return deviceTypes[index] || 'desktop';
    },


    _capitalize: function (string) {
        return string.charAt(0).toUpperCase() + string.slice(1);
    }
};
