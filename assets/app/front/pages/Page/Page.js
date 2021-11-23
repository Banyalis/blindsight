var _ = require('underscore/underscore');

var Base = require('front/components/Base/Base');
var Utils = require('front/utils/Utils');

var gsap = require('gsap').gsap;

module.exports = Base.extend({
    // Тип страницы, используется для поиска активного элемента меню
    type: '',

    // Заголовок страницы
    title: undefined,

    // Title of page before current
    titleBefore: undefined,

    TIME_ANIMATION: 400,

    initialize: function (options) {
        Base.prototype.initialize.call(this, options);

        _.bindAll(this, 'googleAnalytics', 'lazyLoad', 'customCursor', 'trackpadСheck', 'updateHorizontalScroll', 'onResizeHorizontalScroll', 'enabledHorizontalScroll', 'disabledHorizontalScroll');

        window.app.vent.on('gsapOffset', function (x) {
            this.offset = -x;
        }.bind(this));

        this.prevTime = new Date().getTime();
        this.scrollingX = [];
        this.scrollingY = [];
        this.offset = 0;
        this.detectScroll = false;

        document.body.addEventListener('wheel', this.trackpadСheck, {passive: true});
        window.app.vent.on('enabledHorizontalScroll', this.enabledHorizontalScroll);
        window.app.vent.on('disabledHorizontalScroll', this.disabledHorizontalScroll);
    },

    googleAnalytics: function () {
        if ($('.Button-cta').length >= 1) {
            var openVideo = document.querySelector('.Button-cta');
        
            openVideo.onclick = function () {
                gtag('event', 'Open video', { 'event_category': 'link', 'event_action': 'click' });
            };
        }
    },

    lazyLoad: function () {
        var images = document.querySelectorAll('[data-lazy-load]');

        function onIntersection(imageEntites) {
            imageEntites.forEach(function (image) {
                if (image.isIntersecting) {
                    observer.unobserve(image.target);
                    if (image.target.tagName.toLowerCase() === 'img') {
                        image.target.src = image.target.dataset.src;
                    } else {
                        image.target.style.backgroundImage = 'url(' + image.target.dataset.src +')';
                    }
                }
            });
        }

        var observer = new IntersectionObserver(onIntersection);

        images.forEach(function (image) {
            return observer.observe(image);
        });
    },

    customCursor: function () {
        if (app.settings.isDesktop) {
            var $cursor = $('.Cursor');

            $('*').on('mousedown', function () {
                $cursor.addClass('isPressed');
            });

            $('*').on('mouseup', function () {
                $cursor.removeClass('isPressed');
            });

            $('*').on('mouseenter', function (e) {
                var $cursorTarget = $(e.currentTarget);
                var classList = $cursorTarget[0].classList.value;

                switch (true) {
                    case classList.indexOf('Cursor-play') !== -1:
                        $cursor.addClass('isPlay');
                        break;
                    case classList.indexOf('Cursor-pause') !== -1:
                        $cursor.addClass('isPause');
                        break;
                    case classList.indexOf('Cursor-zoom') !== -1:
                        $cursor.addClass('isZoom');
                        break;
                    case classList.indexOf('Cursor-close') !== -1:
                        $cursor.addClass('isClose');
                        break;
                    case classList.indexOf('Cursor-next') !== -1:
                        $cursor.addClass('isNext');
                        break;
                    case classList.indexOf('Cursor-memories') !== -1:
                        $cursor.addClass('isMemories');
                        break;
                    case classList.indexOf('Cursor-increase') !== -1:
                        $cursor.addClass('isIncrease');
                        break;
                    case classList.indexOf('Cursor-redZone') !== -1:
                        $cursor.addClass('isRedZone');
                        break;
                    default:
                        if ($cursorTarget[0].tagName.toLowerCase() === 'a') {
                            $cursor.addClass('isDefault');
                        }
                }
            });

            $('*').on('mouseleave', function (e) {
                var $cursorTarget = $(e.currentTarget);
                var classList = $cursorTarget[0].classList.value;

                switch (true) {
                    case classList.indexOf('Cursor-play') !== -1:
                        $cursor.removeClass('isPlay');
                        break;
                    case classList.indexOf('Cursor-pause') !== -1:
                        $cursor.removeClass('isPause');
                        break;
                    case classList.indexOf('Cursor-zoom') !== -1:
                        $cursor.removeClass('isZoom');
                        break;
                    case classList.indexOf('Cursor-close') !== -1:
                        $cursor.removeClass('isClose');
                        break;
                    case classList.indexOf('Cursor-next') !== -1:
                        $cursor.removeClass('isNext');
                        break;
                    case classList.indexOf('Cursor-memories') !== -1:
                        $cursor.removeClass('isMemories');
                        break;
                    case classList.indexOf('Cursor-increase') !== -1:
                        $cursor.removeClass('isIncrease');
                        break;
                    case classList.indexOf('Cursor-redZone') !== -1:
                        $cursor.removeClass('isRedZone');
                        break;
                    default:
                        if ($cursorTarget[0].tagName.toLowerCase() === 'a') {
                            $cursor.removeClass('isDefault');
                        }
                }
            });
        }
    },

    trackpadСheck: function (e) {
        var curTime = new Date().getTime();
   
        if (this.scrollingX.length > 149) {
            this.scrollingX.shift();
        }

        if (this.scrollingY.length > 149) {
            this.scrollingY.shift();
        }

        this.scrollingX.push(Math.abs(e.deltaX));
        this.scrollingY.push(Math.abs(e.deltaY));

        var timeDiff = curTime - this.prevTime;
        this.prevTime = curTime;

        if (timeDiff > 200) {
            this.scrollingX = [];
            this.scrollingY = [];
        }

        var averageEndX = getAverage(this.scrollingX, 10);
        var averageMiddleX = getAverage(this.scrollingX, 70);
        var isAcceleratingX = averageEndX >= averageMiddleX / 2.3;
        var averageEndY = getAverage(this.scrollingY, 10);
        var averageMiddleY = getAverage(this.scrollingY, 70);
        var isAcceleratingY = averageEndY >= averageMiddleY / 2.3;

        if (!isAcceleratingX || !isAcceleratingY) {
            window.app.data.startScroll = false;
        } else {
            window.app.data.startScroll = true;
        }

        function getAverage (elements, number) {
            var sum = 0;
            var lastElements = elements.slice(Math.max(elements.length - number, 1));

            for (var i = 0; i < lastElements.length; i++) {
                sum = sum + lastElements[i];
            }
            return Math.ceil(sum / number);
        }
    },

    updateHorizontalScroll: function (e) {
        var wheelDelta = Math.abs(e.deltaX) > Math.abs(e.deltaY) ? e.deltaX : e.deltaY;

        if (Math.abs(wheelDelta) > 600) {
            wheelDelta = 200 * Math.sign(wheelDelta);
        } else if (window.app.data.startScroll && Math.abs(wheelDelta) < 25) {
            wheelDelta *= 15;
        }

        app.els.$body.addClass('disabledHover');

        clearTimeout(this.detectScroll);

        this.detectScroll = setTimeout(function () {
            app.els.$body.removeClass('disabledHover');
            this.detectScroll = undefined;
        }, 500);

        this.offset += wheelDelta;

        if (this.offset < 0) {
            this.offset = 0;
        } else if (this.offset > this.scrollHeight - window.innerHeight) {
            this.offset = this.scrollHeight - window.innerHeight;
        }

        gsap.to(this.horizontalPage, 1, {
            x: -this.offset
        });

        app.els.$body.removeClass('isDragEnd');
        app.vent.trigger('wheelOffset', this.offset);
    },

    onResizeHorizontalScroll: function () {
        this.scrollHeight = app.els.$window.height() + (this.horizontalPage.width() - app.els.$window.width());
    },

    enabledHorizontalScroll: function () {
        if (app.settings.isDesktop) {
            this.horizontalPage = $('.HorizontalPage');

            this.onResizeHorizontalScroll();
            app.els.$window.on('resize', this.onResizeHorizontalScroll);
            app.els.$window[0].addEventListener('wheel', this.updateHorizontalScroll, {passive: true});
        }
    },

    disabledHorizontalScroll: function () {
        if (app.settings.isDesktop) {
            app.els.$window.off('resize', this.onResizeHorizontalScroll);
            app.els.$window[0].removeEventListener('wheel', this.updateHorizontalScroll);
        }
    },

    setTitle: function (title, isInherit) {
        title = title || this.title;
        this.titleBefore = document.title;

        if (isInherit) {
            title = this.titleBefore + title;
        }

        if (title !== undefined) {
            document.title = (title ? $('<div>' + title + '</div>').text() : 'Blindsight');
        }
    },

    setClass: function (className) {
        if (className !== undefined) {
            app.els.$contentContent.attr('class', 'Content ' + className);
        }
    },

    $parent: function () {
        return app.els.$content;
    },

    viewsRegistration: function () {
        Base.prototype.viewsRegistration.call(this);
    },

    activate: function (params) {
        this.setTitle();

        return Base.prototype.activate.call(this, params);
    },

    deactivate: function (params) {
        var cursor = document.querySelector('.Cursor');
        cursor.classList = 'Cursor';
        document.body.removeEventListener('wheel', this.trackpadСheck);

        return Base.prototype.deactivate.call(this, params);
    }
});