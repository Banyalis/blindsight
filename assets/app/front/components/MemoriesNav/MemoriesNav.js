var Backbone = require('backbone');
var _ = require('underscore');

var Base = require('front/components/Base/Base');

require('./MemoriesNav.less');

var gsap = require('gsap').gsap;

module.exports = Base.extend({
    template: require('./MemoriesNav.jinja'),

    el: '.MemoriesNav',

    events: {
        'click .MemoriesNav-item': 'scrollOnClick',
        'click .MemoriesNav-controlPrev': 'scrollToPrev',
        'click .MemoriesNav-controlNext': 'scrollToNext'
    },

    initialize: function (options) {
        _.bindAll(this, 'memoriesAnimate', 'onHover', 'unHover', 'playVideo', 'enabledSpiralScroll', 'disabledSpiralScroll', 'onResize', 'onScroll', 'disabledHover', 'scrollOnKey', 'scrollToStep', 'memoriesSpiral', 'triggerMemoryOpen', 'triggerMemoryClose');

        this.items = [];
        this.tarPercentage = 0;
        this.curPercentage = 0;
        this.isMouse = false;
        this.scrollRawPos = 0;
        this.scrollStep = 50 / 900;
        this.angleBetween = 50;
        this.detectScroll = false;
        this.isOpenMemoryPopup = false;

        if (app.els.$body.hasClass('isInitialState')) {
            this.memoriesAnimate();
        } else if ($('.MemoriesPopup').length == false) {
            app.vent.on('loader', this.memoriesAnimate);
        }
        this.$('.MemoriesNav-item').hover(this.onHover, this.unHover);

        $('.isSpiral .MemoriesNav-itemWrapper').each(function (index, item) {
            this.items[index] = {
                el: item,
                visible: true,
                angle: 0,
                link: item.querySelector('.MemoriesNav-item'),
                content: item.querySelector('.MemoriesNav-itemContent'),
                overlay: item.querySelector('.MemoriesNav-itemOverlay')
            }
            item.setAttribute('data-index', index)
        }.bind(this));

        this.enabledSpiralScroll();
        app.vent.on('enabledSpiralScroll', this.enabledSpiralScroll);
        app.vent.on('disabledSpiralScroll', this.disabledSpiralScroll);
        
        this.onResize();
        app.els.$window.on('resize', this.onResize);
        app.els.$document.on('keydown', this.scrollOnKey);
        if (!app.settings.isMobile) {
            app.vent.on('memoryOpen', this.triggerMemoryOpen);
            app.vent.on('memoryClose', this.triggerMemoryClose);
        }

        Base.prototype.initialize.call(this, options);
    },

    memoriesAnimate: function () {
        if (!app.settings.isMobile) {
            var tl = gsap.timeline();

            tl.from(this.$el, 1, {
                autoAlpha: 0,
                scale: .99,
                rotation: 5,
                transformOrigin: 'right center',
                clearProps: 'all'
            }, '.4');
        }
    },

    onHover: function (e) {
        if (app.settings.isDesktop) {
            this.$card = $(e.currentTarget);

            if (this.$card.hasClass('inCenter') || this.$el.hasClass('isGrid')) {
                this.$cardVideo = this.$card.find('video');
                this.$cardVideo[0].currentTime = 0;

                if (this.$cardVideo.attr('src').length == false) {
                    this.$cardVideo.attr('src', this.$cardVideo.data('src'));
                    this.$cardVideo[0].load();
                }

                clearTimeout(timer);

                var timer = setTimeout(function () {
                    if (this.$cardVideo[0].readyState == 3 || this.$cardVideo[0].readyState == 4)  {
                        this.playVideo();
                    } else {
                        this.$cardVideo.on('canplaythrough', this.playVideo);
                    }
                }.bind(this), 300);
            }
        }
    },

    unHover: function () {
        if (app.settings.isDesktop) {
            this.$card.removeClass('onHover');
            if (this.$card.hasClass('inCenter') || this.$el.hasClass('isGrid')) {
                this.$cardVideo[0].pause();
                this.$cardVideo[0].currentTime = 0;
            }
        }
    },

    playVideo: function () {
        this.$cardVideo.off('canplaythrough', this.playVideo);

        this.$card.addClass('onHover');
        this.$cardVideo[0].play();
    },

    enabledSpiralScroll: function () {
        if (app.settings.isDesktop) {
            if (this.$el.hasClass('isSpiral')) {
                document.body.addEventListener('wheel', this.onScroll, {passive: true});
            }
        }
    },

    disabledSpiralScroll: function () {
        if (app.settings.isDesktop) {
            document.body.removeEventListener('wheel', this.onScroll);
        }
    },

    onResize: function () {
        this.windowWidth = this.$el.width();
        this.memoriesSpiral(this.curPercentage);
    },

    onScroll: function (e) {
        var wheelDelta = e.deltaY;

        // if (wheelDelta <= 0) {
        //     return;
        // }

        if (!window.app.data.startScroll) {
            this.isMouse = false;
            return;
        }

        this.disabledHover();

        if (Math.abs(wheelDelta) > 600) {
            wheelDelta = 200 * Math.sign(wheelDelta);
        } else if (window.app.data.startScroll && Math.abs(wheelDelta) < 25) {
            wheelDelta *= 10;
        }

        this.scrollRawPos += wheelDelta;

        if (this.scrollRawPos > 0) {
            this.tarPercentage = Math.ceil(this.scrollRawPos / 240) * this.scrollStep;
        } else {
            this.tarPercentage = Math.floor(this.scrollRawPos / 240) * this.scrollStep;
        }

        if (!this.scrollToStepId) {
            this.scrollToStep();
        }
    },

    disabledHover: function () {
        var cursor = document.querySelector('.Cursor');
        cursor.classList = 'Cursor';

        app.els.$body.addClass('disabledHover');

        clearTimeout(this.detectScroll);

        this.detectScroll = setTimeout(function () {
            app.els.$body.removeClass('disabledHover');
            this.detectScroll = undefined;
        }, 1000);
    },

    scrollOnKey: function () {
        if (this.$el.hasClass('isSpiral')) {
            switch (event.keyCode) {
                case 38:
                case 40:
                    if (event.keyCode == 38) {
                        this.tarPercentage += this.scrollStep;
                    } else {
                        this.tarPercentage -= this.scrollStep;
                    }

                    this.scrollRawPos = this.tarPercentage * 900 / 50 * 240;
                    this.disabledHover();

                    if (!this.scrollToStepId) {
                        this.scrollToStep();
                    }
    
                    break;
            }
        }
    },

    scrollOnClick: function (e) {
        if (this.$el.hasClass('isSpiral')) {
            var cardIndex = Number($(e.currentTarget).parent().data('index'));
            var tarAngle = this.items[cardIndex].angle;
    
            this.disabledHover();
    
            if (tarAngle > 220 || tarAngle < 135) {
                e.preventDefault();
                e.stopPropagation();
    
                var curIndex = Math.round((tarAngle - 179.4) / this.angleBetween);
    
                this.tarPercentage += curIndex * this.scrollStep;
                this.scrollRawPos = this.tarPercentage * 900 / 50 * 240;
        
                if (!this.scrollToStepId) {
                    this.scrollToStep();
                }
            }
        }
    },

    scrollToPrev: function () {
        this.tarPercentage -= this.scrollStep;
        this.scrollRawPos = this.tarPercentage * 900 / 50 * 240;

        if (!this.scrollToStepId) {
            this.scrollToStep();
        }
    },

    scrollToNext: function () {
        this.tarPercentage += this.scrollStep;
        this.scrollRawPos = this.tarPercentage * 900 / 50 * 240;

        if (!this.scrollToStepId) {
            this.scrollToStep();
        }
    },

    scrollToStep: function () {
        var delta = (this.tarPercentage - this.curPercentage) * 0.1;

        this.curPercentage += delta;
        this.memoriesSpiral(this.curPercentage);

        if (this.isMouse) {
            this.scrollRawPos = this.tarPercentage * 900 / 50 * 240;
        }

        if (Math.abs(this.tarPercentage - this.curPercentage) <= 0.0001) {
            this.scrollToStepId = null;

            // if (!this.isMouse) {
            //     this.scrollRawPos = this.tarPercentage * 900 / 50 * 240;
            // }
            return;
        }

        this.scrollToStepId = requestAnimationFrame(this.scrollToStep);
    },

    memoriesSpiral: function (percentage) {
        var angleBetween = this.angleBetween;
        var itemsLen = this.items.length;
        var totalAngles = angleBetween * itemsLen;
        var angle = -(percentage - Math.floor(percentage)) * totalAngles + 179.4 - 4 * angleBetween;
        var width, loopAngle;
        var scale = this.windowWidth / 1920;
        var innerCircleRadius = 25 * scale;
        var isInvisible, scaler;
        var angleRange = totalAngles - 300;

        this.items.forEach(function (item, index) {
            loopAngle = angle < 0 ? angle + totalAngles : angle;
            scaler = Math.pow(1.33, loopAngle / angleBetween);
            width = 2781.2067557 * scale / scaler;
            isInvisible = loopAngle < 45;
            opacity = Math.min((1 - loopAngle / totalAngles) * itemsLen, 1);
            changeCursor = loopAngle > 220 || loopAngle < 135;
            contentBrightnessEnabled = (totalAngles - loopAngle) / angleRange * 65 / 100;
            overlayBrightnessEnabled = loopAngle / angleRange * 65 / 100;
            blurEnabled = loopAngle < 135;
            cursorDisabled = loopAngle > 550;
            cursorEnabled = loopAngle < 550 && loopAngle > 135;
            // styleDisabled = loopAngle < 220 && loopAngle > 135 || loopAngle < 100;
            styleDisabled = loopAngle < 220 && loopAngle > 170;
            item.angle = loopAngle;

            if (!isInvisible) {
                if (item.opacity !== opacity) {
                    item.el.style.opacity = opacity;
                }
                if (!item.visible) {
                    item.el.style.display = 'block';
                }
                if (item.visible == changeCursor) {
                    item.link.classList.add('Cursor-increase');
                    item.link.classList.remove('Cursor-next', 'inCenter');
                }
                if (item.visible !== contentBrightnessEnabled) {
                    item.content.style.filter = 'brightness(' + contentBrightnessEnabled + ')';
                    item.overlay.style.opacity = overlayBrightnessEnabled;
                }
                if (item.visible == blurEnabled) {
                    if (document.documentElement.classList.contains('isFirefox')) {
                        item.el.style.filter = null;
                    } else {
                        item.el.style.filter = 'blur(20px)';
                    }
                }
                if (item.visible == cursorDisabled) {
                    item.el.style.pointerEvents = 'none';
                }
                if (item.visible == cursorEnabled) {
                    item.el.style.pointerEvents = null;
                }
                if (item.visible == styleDisabled) {
                    item.el.style.filter = null;
                    item.content.style.filter = null;
                    item.overlay.style.opacity = 0;
                    item.link.classList.remove('Cursor-increase');
                    item.link.classList.add('Cursor-next', 'inCenter');
                }
                item.el.style.transform = 'rotate(' + (loopAngle + 180) + 'deg) translate(' + -width + 'px, ' + innerCircleRadius + 'px) scale(' + width / 880 +') rotate(' + (loopAngle / 7 - 25) + 'deg)';
                item.visible = true;
                item.opacity = opacity;
            } else {
                if (item.visible) {
                    item.el.style.display = 'none';
                }
                item.visible = false;
                item.opacity = null;
            }

            angle += angleBetween;
        });
    },

    triggerMemoryOpen: function () {
        if (!app.settings.isMobile || this.isOpenMemoryPopup) {
            this.isOpenMemoryPopup = true;

            this.$('.MemoriesNav-control').addClass('isHidden');

            if (this.$el.hasClass('isSpiral')) {
                gsap.to(this.$el, 0, {
                    autoAlpha: 0,
                    scale: .99,
                    rotation: 5,
                    pointerEvents: 'none'
                });
            } else {
                gsap.to(this.$el, 0, {
                    autoAlpha: 0
                });
            }
        }
    },

    triggerMemoryClose: function () {
        if (!app.settings.isMobile) {
            this.isOpenMemoryPopup = false;
            var tl = gsap.timeline();

            this.$('.MemoriesNav-control').removeClass('isHidden');

            if (this.$el.hasClass('isSpiral')) {
                tl.to(this.$el, .5, {
                    autoAlpha: 1,
                    scale: 1,
                    rotation: 0,
                    transformOrigin: 'right center'
                }, '0');

                tl.to(this.$el, .5, {
                    pointerEvents: 'all'
                }, '.6');
            } else {
                tl.to(this.$el, .5, {
                    autoAlpha: 1
                }, '0');
            }
        }
    },

    deactivate: function (params) {
        app.els.$window.off('resize', this.onResize);
        document.body.removeEventListener('wheel', this.onScroll);

        return Base.prototype.deactivate.call(this, params);
    }
});