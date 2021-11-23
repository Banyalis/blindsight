var Backbone = require('backbone');
var _ = require('underscore/underscore');

var Urls = require('django_js_front/reverse.js');

var SubSection = require('front/pages/Section/SubSection');
var MemoriesPopupIntro = require('front/components/MemoriesPopupIntro/MemoriesPopupIntro.js');
var MemoriesPopupChat = require('front/components/MemoriesPopupChat/MemoriesPopupChat.js');
var MemoriesPopupGallery = require('front/components/MemoriesPopupGallery/MemoriesPopupGallery.js');
var MemoriesPopupNote = require('front/components/MemoriesPopupNote/MemoriesPopupNote.js');
var MemoriesPopupFilm = require('front/components/MemoriesPopupFilm/MemoriesPopupFilm.js');
var MemoriesPopupLater = require('front/components/MemoriesPopupLater/MemoriesPopupLater.js');
var MemoriesPopupModel = require('front/components/MemoriesPopupModel/MemoriesPopupModel.js');
var MemoriesPopupExploration = require('front/components/MemoriesPopupExploration/MemoriesPopupExploration.js');
var MemoriesPopupVideo = require('front/components/MemoriesPopupVideo/MemoriesPopupVideo.js');
var MemoriesPopupAcknowledgements = require('front/components/MemoriesPopupAcknowledgements/MemoriesPopupAcknowledgements.js');
var MemoriesPopupWallpaper = require('front/components/MemoriesPopupWallpaper/MemoriesPopupWallpaper.js');
var MemoriesPopupResources = require('front/components/MemoriesPopupResources/MemoriesPopupResources.js');
var MemoriesPopupNext = require('front/components/MemoriesPopupNext/MemoriesPopupNext.js');
var MemoriesPopupInfo = require('front/components/MemoriesPopupInfo/MemoriesPopupInfo.js');
var MemoriesPopupCredits = require('front/components/MemoriesPopupCredits/MemoriesPopupCredits.js');

require('./MemoriesPopup.less');

var gsap = require('gsap/dist/gsap').gsap;
var ScrollScene = require('scrollscene').ScrollScene;
var Draggable = require('gsap/Draggable').Draggable;
var InertiaPlugin = require('gsap/InertiaPlugin').InertiaPlugin;
var SplitText = require('gsap/SplitText').SplitText;

gsap.registerPlugin(Draggable, InertiaPlugin, SplitText);

module.exports = SubSection.extend({
    template: require('./MemoriesPopup.jinja'),

    el: '.MemoriesPopup',

    VIEWS_TO_REGISTER: {
        'MemoriesPopupIntro': {
            selector: '.MemoriesPopup-intro', viewConstructor: MemoriesPopupIntro
        },
        'MemoriesPopupChat': {
            selector: '.MemoriesPopup-chat', viewConstructor: MemoriesPopupChat
        },
        'MemoriesPopupGallery': {
            selector: '.MemoriesPopup-galleryWrapper', viewConstructor: MemoriesPopupGallery
        },
        'MemoriesPopupNote': {
            selector: '.MemoriesPopup-note', viewConstructor: MemoriesPopupNote
        },
        'MemoriesPopupFilm': {
            selector: '.MemoriesPopup-film', viewConstructor: MemoriesPopupFilm
        },
        'MemoriesPopupLater': {
            selector: '.MemoriesPopup-later', viewConstructor: MemoriesPopupLater
        },
        'MemoriesPopupModel': {
            selector: '.MemoriesPopup-model', viewConstructor: MemoriesPopupModel
        },
        'MemoriesPopupExploration': {
            selector: '.MemoriesPopup-exploration', viewConstructor: MemoriesPopupExploration
        },
        'MemoriesPopupVideo': {
            selector: '.MemoriesPopup-video', viewConstructor: MemoriesPopupVideo
        },
        'MemoriesPopupAcknowledgements': {
            selector: '.MemoriesPopup-acknowledgements', viewConstructor: MemoriesPopupAcknowledgements
        },
        'MemoriesPopupWallpaper': {
            selector: '.MemoriesPopup-wallpaper', viewConstructor: MemoriesPopupWallpaper
        },
        'MemoriesPopupResources': {
            selector: '.MemoriesPopup-resources', viewConstructor: MemoriesPopupResources
        },
        'MemoriesPopupNext': {
            selector: '.MemoriesPopup-next', viewConstructor: MemoriesPopupNext
        },
        'MemoriesPopupInfo': {
            selector: '.MemoriesPopup-info', viewConstructor: MemoriesPopupInfo
        },
        'MemoriesPopupCredits': {
            selector: '.MemoriesPopup-credits', viewConstructor: MemoriesPopupCredits
        }
    },

    events: {
        'click .MemoriesPopup-close': 'close'
    },

    apiUrl: function () {
        var slug = this.slug;

        return Urls['front:api:memories-popup'](slug);
    },

    initialize: function (options) {
        this.options = options || {};

        SubSection.prototype.initialize.call(this, options);

        _.bindAll(this, 'onScrollAnimation', 'draggablePopup', 'onScrollLeft', 'triggerZoomOpen', 'triggerZoomClose', 'closeOnKey', 'activateLogic');

        this.rootUrl = Urls['front:memories']();

        this.slug = this.options.slug;

        if (this.options.server) {
            this.activateLogic(true);
            this.data = {};
        }
    },

    onScrollAnimation: function () {
        var animationOpacity = {
            autoAlpha: 0,
            willChange: 'opacity, transform',
            clearProps: 'all'
        }

        var animationTransformX = Object.assign({
             x: 100
        }, animationOpacity);

        var animationTransformY = Object.assign({
             y: 50
        }, animationOpacity);

        var animationTransformYNegative = Object.assign({
             y: -50
        }, animationOpacity);

        gsap.from(this.$('.MemoriesPopup-hintWrapper'), 1, Object.assign({
            x: -50
        }, animationOpacity));

        this.$('.isAnimated').each(function (index, item) {
            var tl = gsap.timeline({ paused: true });

            if ($(item).find('.MemoriesPopup-introTitle').length >= 1) {
                tl.from($(item).find($('.MemoriesPopup-introTitle')), .5, Object.assign({}, animationTransformX), '0');
                tl.from($(item).find($('.MemoriesPopup-introNumber')), .5, Object.assign({}, animationTransformX), '.2');
                tl.from($(item).find($('.MemoriesPopup-introSize')), .5, Object.assign({}, animationTransformX), '.4');

                var fractionalNumber = Math.pow(10, 2);

                tl.from($(item).find($('.MemoriesPopup-introSize span')), .5, Object.assign({
                    innerHTML: '0',
                    roundProps: 'innerHTML',
                    modifiers: {
                        innerHTML: function (i) {
                            return Math.round(i * fractionalNumber) / fractionalNumber;
                        }
                    }
                }, animationOpacity), '.4');

                tl.from($(item).find($('.MemoriesPopup-introDescription')), .5, Object.assign({}, animationOpacity), '.2');
                tl.from($(item).find($('.MemoriesPopup-introText')), .5, Object.assign({}, animationOpacity), '.4');
            }

            if ($(item).find('.MemoriesPopup-chatItem').length >= 1) {
                tl.staggerFrom($(item).find($('.MemoriesPopup-chatItem')), .5, Object.assign({}, animationTransformY), .2, '0');
            }

            if ($(item).find('.MemoriesPopup-gallery').length >= 1) {
                tl.from($(item).find($('.MemoriesPopup-gallery')), .5, Object.assign({}, animationOpacity), '0');

                var mySplitText = new SplitText($(item).find('.MemoriesPopup-galleryTitle, .MemoriesPopup-galleryCaption'), {type: 'words, chars'});
                var chars = mySplitText.chars.length; 

                for (var i = 0; i < chars; i++){
                    tl.from(mySplitText.chars[i], 1, Object.assign({}, animationOpacity), Math.random() * 1);
                }

                // if ($(item).find('video').length >= 1) {
                //     $(item).find($('video'))[0].play();
                // }

                tl.from($(item).find($('.MemoriesPopup-galleryFile')), .5, Object.assign({}, animationOpacity), '.2');
            }

            if ($(item).find('.MemoriesPopup-galleryNav').length >= 1) {
                tl.from($(item).find($('.MemoriesPopup-galleryNav')), .5, Object.assign({}, animationTransformYNegative), '.4');
            }

            if ($(item).find('.MemoriesPopup-noteQuestion').length >= 1) {
                tl.staggerFrom($(item).find($('.MemoriesPopup-note > div')), .5, Object.assign({}, animationOpacity), .2, '0');
            }

            if ($(item).find('.MemoriesPopup-filmTitle').length >= 1) {
                tl.from($(item).find($('.MemoriesPopup-filmVideo')), .5, Object.assign({}, animationOpacity), '0');

                var mySplitText = new SplitText($(item).find('.MemoriesPopup-filmTitle, .MemoriesPopup-filmCaption'), {type: 'words, chars'});
                var chars = mySplitText.chars.length; 

                for (var i = 0; i < chars; i++){
                    tl.from(mySplitText.chars[i], 1, Object.assign({}, animationOpacity), Math.random() * 1);
                }

                // $(item).find($('video'))[0].play();

                tl.from($(item).find($('.MemoriesPopup-filmButtonWrapper')), .5, Object.assign({}, animationTransformYNegative), '.4');
            }

            if ($(item).find('.MemoriesPopup-wallpaperImage').length >= 1) {
                tl.from($(item).find($('.MemoriesPopup-wallpaperImage')), .5, Object.assign({}, animationOpacity), '0');

                var mySplitText = new SplitText($(item).find('.MemoriesPopup-wallpaperTitle'), {type: 'words, chars'});
                var chars = mySplitText.chars.length; 

                for (var i = 0; i < chars; i++){
                    tl.from(mySplitText.chars[i], 1, Object.assign({}, animationOpacity), Math.random() * 1);
                }

                tl.from($(item).find($('.MemoriesPopup-wallpaperFile')), .5, Object.assign({}, animationOpacity), '.2');
                tl.from($(item).find($('.MemoriesPopup-wallpaperButtonWrapper')), .5, Object.assign({}, animationTransformYNegative), '.4');
            }

            if ($(item).find('.MemoriesPopup-resourcesTitle').length >= 1) {
                tl.from($(item).find($('.MemoriesPopup-resourcesTitle')), .5, Object.assign({}, animationTransformY), '0');
                tl.staggerFrom($(item).find($('.MemoriesPopup-resourcesListItemLine')), .5, Object.assign({}, animationOpacity), .2, '.4');
                tl.from($(item).find($('.MemoriesPopup-resourcesListItemTitle')), .5, Object.assign({}, animationOpacity), '.4');
                tl.from($(item).find($('.MemoriesPopup-resourcesListItemValue')), .5, Object.assign({
                    innerHTML: '0',
                    roundProps: 'innerHTML'
                }, animationOpacity), '.4');
            }

            if ($(item).find('.MemoriesPopup-resourcesCaption').length >= 1) {
                tl.from($(item).find($('.MemoriesPopup-resourcesCaption')), .5, Object.assign({}, animationTransformY), '.2');
            }

            if ($(item).find('.MemoriesPopup-resourcesText').length >= 1) {
                tl.from($(item).find($('.MemoriesPopup-resourcesText')), .5, Object.assign({}, animationOpacity), '.4');
            }

            if ($(item).find('.MemoriesPopup-nextCardImage').length >= 1) {
                tl.from($(item).find($('.MemoriesPopup-nextCardImage')), .5, Object.assign({}, animationOpacity), '0');
                tl.from($(item).find($('.MemoriesPopup-nextCardCaption')), .5, Object.assign({}, animationTransformYNegative), '.2');
                tl.from($(item).find($('.MemoriesPopup-nextCardHint')), .5, Object.assign({
                    x: -100
                }, animationOpacity), '.4');
                tl.from($(item).find($('.MemoriesPopup-nextCardTitle')), .5, Object.assign({}, animationTransformX), '.6');
            }

            if ($(item).find('.MemoriesPopup-laterTitle').length >= 1) {
                tl.from($(item).find($('.MemoriesPopup-laterTitle')), .5, Object.assign({}, animationOpacity), '0');
                tl.from($(item).find($('.MemoriesPopup-laterText')), .5, Object.assign({}, animationOpacity), '.2');
            }

            if ($(item).find('.MemoriesPopup-explorationTitle').length >= 1) {
                var mySplitText = new SplitText($(item).find('.MemoriesPopup-explorationTitle, .MemoriesPopup-explorationCaption'), {type: 'words, chars'});
                var chars = mySplitText.chars.length; 

                for (var i = 0; i < chars; i++){
                    tl.from(mySplitText.chars[i], 1, Object.assign({}, animationOpacity), Math.random() * 1);
                }

                tl.from($(item).find($('.MemoriesPopup-explorationFile')), .5, Object.assign({}, animationOpacity), '.2');
            }

            if ($(item).find('.MemoriesPopup-videoTitle').length >= 1) {
                var mySplitText = new SplitText($(item).find('.MemoriesPopup-videoTitle, .MemoriesPopup-videoCaption'), {type: 'words, chars'});
                var chars = mySplitText.chars.length; 

                for (var i = 0; i < chars; i++){
                    tl.from(mySplitText.chars[i], 1, Object.assign({}, animationOpacity), Math.random() * 1);
                }

                tl.from($(item).find($('.MemoriesPopup-videoFile')), .5, Object.assign({}, animationOpacity), '.2');
            }

            if ($(item).find('.MemoriesPopup-acknowledgementsTitle').length >= 1) {
                var mySplitText = new SplitText($(item).find('.MemoriesPopup-acknowledgementsTitle'), {type: 'words, chars'});
                var chars = mySplitText.chars.length; 

                for (var i = 0; i < chars; i++){
                    tl.from(mySplitText.chars[i], 1, Object.assign({}, animationOpacity), Math.random() * 1);
                }

                tl.staggerFrom($(item).find($('.MemoriesPopup-acknowledgementsListColumn')), .5, Object.assign({}, animationTransformYNegative), .2, '.2');
                tl.from($(item).find($('.MemoriesPopup-acknowledgementsOwner')), .5, Object.assign({}, animationOpacity), '1.4');
            }

            var offsetAnimation = 200;

            if (app.settings.isMobile) {
                offsetAnimation = 0;
            }

            var scrollScene = new ScrollScene({
                triggerElement: $(item)[0],
                triggerHook: 'onEnter',
                offset: offsetAnimation,
                scene: {
                    reverse: false,
                },
                gsap: {
                    timeline: tl
                },
                controller: {
                    vertical: false
                }
            })
        });
    },

    draggablePopup: function () {
        if (app.settings.isDesktop) {
            this.currentX = 0;

            Draggable.create('.HorizontalPage', {
                bounds: '.MemoriesPopup',
                type: 'x',
                cursor: 'none',
                inertia: true,
                onDrag: function () {
                    this.update(true);
                    this.currentX =- this.x;

                    if (this.currentX >= 50) {
                        app.vent.trigger('headerHidden');
                    } else if (this.currentX <= 30) {
                        app.vent.trigger('headerShow');
                    }
                },
                onThrowUpdate: function () {
                    app.vent.trigger('gsapOffset', this.x);
                },
                onDragStart: function () {
                    app.els.$body.removeClass('isDragEnd');
                },
                onDragEnd: function () {
                    app.els.$body.addClass('isDragEnd');
                }
            });
        }
    },

    onScrollLeft: function () {
        if (this.$('.HorizontalPage').scrollLeft() > 50) {
            if (app.settings.isMobile) {
                this.$('.MemoriesPopup-hint').addClass('isHidden');
            } else {
                app.vent.trigger('headerHidden');
            }
        } else {
            if (app.settings.isMobile) {
                this.$('.MemoriesPopup-hint').removeClass('isHidden');
            } else {
                app.vent.trigger('headerShow');
            }
        }
    },

    triggerZoomOpen: function () {
        if (app.settings.isDesktop) {
            Draggable.get('.HorizontalPage').disable();
        }
        this.$('.MemoriesPopup-close').hide();
        this.$('.HorizontalPage').addClass('disabledScroll');
        this.disabledHorizontalScroll();
        app.els.$document.off('keydown', this.closeOnKey);
    },

    triggerZoomClose: function () {
        if (app.settings.isDesktop) {
            Draggable.get('.HorizontalPage').enable();
        }
        this.$('.MemoriesPopup-close').show();
        this.$('.HorizontalPage').removeClass('disabledScroll');
        this.enabledHorizontalScroll();
        app.els.$document.on('keydown', this.closeOnKey);
    },

    closeOnKey: function () {
        switch (event.keyCode) {
    
        case 27:
            event.returnValue = false;
            event.keyCode = 0;
            Backbone.history.navigate(this.rootUrl, {trigger: 'true'});
            this.setTitle(this.titleBefore);
            break;
        }
    },

    close: function (e) {
        Backbone.history.navigate(this.rootUrl, {trigger: 'true'});
        this.setTitle(this.titleBefore);

        e.preventDefault();
    },

    render: function () {
        SubSection.prototype.render.call(this);
    },

    activateLogic: function () {
        app.vent.on('loader', this.onScrollAnimation);
        this.draggablePopup();
        this.$('.HorizontalPage').on('scroll', this.onScrollLeft);
        app.vent.on('zoomOpen', this.triggerZoomOpen);
        app.vent.on('zoomClose', this.triggerZoomClose);
        this.enabledHorizontalScroll();
        this.googleAnalytics();
    },

    activate: function (params) {
        return SubSection.prototype.activate.call(this, params)
            .then(function () {
                app.els.$document.on('keydown', this.closeOnKey);

                app.vent.on('wheelOffset', function (x) {
                    if (x >= 50) {
                        app.vent.trigger('headerHidden');
                    } else if (x <= 30) {
                        app.vent.trigger('headerShow');
                    }
                }.bind(this));
                app.vent.trigger('disabledSpiralScroll');
                app.vent.trigger('memoryOpen');
            }.bind(this));
    },

    playIn: function () {
        var self = this;

        return new Promise(function (resolve) {
            clearTimeout(this.playOutTimeOutId);

            gsap.from(this.$('.MemoriesPopup-overlay'), .4, {
                opacity: 0
            });
    
            gsap.from(this.$('.MemoriesPopup-inner'), .4, {
                opacity: 0,
                scale: .9,
                transformOrigin: 'left center'
            });

            self.onScrollAnimation();

            setTimeout(function () {
                self.draggablePopup();
                this.$('.HorizontalPage').on('scroll', self.onScrollLeft);
                app.vent.on('zoomOpen', self.triggerZoomOpen);
                app.vent.on('zoomClose', self.triggerZoomClose);
                app.vent.trigger('memoryOpen');
                self.customCursor();
                self.lazyLoad();
                self.enabledHorizontalScroll();
                self.googleAnalytics();
                ga('set', 'page', window.location.pathname);
                ga('send', 'pageview');
                resolve();
            }, 400);
        });
    },

    playOut: function () {
        return new Promise(function (resolve) {
            gsap.to(this.$('.MemoriesPopup-overlay'), .4, {
                opacity: 0
            });
    
            gsap.to(this.$('.MemoriesPopup-inner'), .4, {
                opacity: 0,
                x: 50
            });

            setTimeout(function () {
                resolve();

                this.playOutTimeOutId = setTimeout(function () {
                    app.vent.trigger('memoryClose');
                }, 50);
            }, 400);
        });
    },

    destroy: function () {
        return SubSection.prototype.destroy.call(this);
    },

    deactivate: function (params) {
        app.els.$document.off('keydown', this.closeOnKey);
        this.$('.HorizontalPage').off('scroll', this.onScrollLeft);
        app.vent.off('zoomOpen', this.triggerZoomOpen);
        app.vent.off('zoomClose', this.triggerZoomClose);
        app.vent.off('wheelOffset');
        app.vent.trigger('headerShow');
        app.vent.trigger('enabledSpiralScroll');
        this.disabledHorizontalScroll();

        return SubSection.prototype.deactivate.call(this, params);
    }
});