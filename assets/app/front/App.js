var Backbone = require('backbone');
var _ = require('underscore');

var svg4everybody = require('svg4everybody');
var MobileDetect = require('mobile-detect');
var objectFitImages = require('object-fit-images/dist/ofi.common-js.js');
var Promise = require('promise-polyfill');

var Settings = require('./Settings');
var Utils = require('front/utils/Utils.js');
var Router = require('./Router');

var Urls = require('django_js_front/reverse.js');
window.Urls = Urls;

// Here we declare root components that are rendered on server
// and exist all the time
var Header = require('front/components/Header/Header');
// require('front/components/Content/Content');

require('reset.css');
require('front/fonts.less');
require('front/utils.less');
require('front/style.less');

var gsap = require('gsap').gsap;

app.AdoptTempFileObject = function (responseText, dataType) {
    var parsedData = JSON.parse(responseText);
    var responseObject = {};

    if (dataType == 'image') {
        responseObject = {
            aspect: parsedData.aspect,
            width: parsedData.width,
            height: parsedData.height,
            tempImg: parsedData.url,
            tempImgId: parsedData.id
        };
    }

    if (dataType == 'file') {
        responseObject = {
            originalName: parsedData.originalName,
            mime: parsedData.mime && parsedData.mime[0],
            typ: parsedData.mime && parsedData.mime[0].split('/')[1],
            tempFile: parsedData.url,
            tempFileId: parsedData.id
        };
    }

    return responseObject;
};

app.shareFacebook = function (data) {
    window.open(
        'https://www.facebook.com/sharer/sharer.php?u=' + encodeURIComponent(data.link),
        'facebooksharedialog',
        'width=626,height=436');
};


app.shareTwitter = function (data) {
    var tweetUrl = 'https://twitter.com/share' +
        '?url=' + encodeURIComponent(data.link) +
        '&text=' + encodeURIComponent(data.title);

    window.open(tweetUrl, '', 'menubar=no,toolbar=no,resizable=yes,scrollbars=yes,height=600,width=600');
};

app.shareMail = function (data) {
    window.location.href = 'mailto:?body=' + encodeURIComponent(data.title + ' — ' + data.link);
};


app.shareLinked = function (data) {
    window.open('http://www.linkedin.com/shareArticle?mini=true&url=' + encodeURIComponent(data.link) + '&title=' + encodeURIComponent(data.title) + '&summary=' + encodeURIComponent(data.title)/* + '&source=site.com'*/, 'sharer', 'toolbar=0, status=0, width=626, height=436');
};

// To add to Promise to window for IE
if (!window.Promise) {
    window.Promise = Promise;
}

/* Инициализация полифиллов */
// Поддержка css свойства object-fit для IE и старых браузеров.
objectFitImages();

// Поддержка svg sprites в IE.
svg4everybody();

app.configure = Settings.configure;
app.configure();

window.app.vent = _.extend({}, Backbone.Events);

window.app.state = {};
window.app.cache = {};
window.app.utils = Utils;

window.app.state = {
    // Переделать в очередь вьюх
    // view: null,
    // prevView: null,
    // subView: null,
    // popupOpened: false
};

app.scrollTo = function (dataid) {
    var top = $('[data-id="' + dataid + '"]')
        .offset().top - $('.Header')
        .innerHeight();
    $('body,html')
        .animate({scrollTop: top}, 300);
};

// Global storage for frequently used DOM elements
// Example usage in views: app.els.$body
window.app.els = {
    $window: $(window),
    $document: $(document),
    $body: $('body'),
    $htmlBody: $('html,body'),
    $content: $('.Content-content'),
    $contentContent: $('.Content'),
    $pageSectionBody: $('.Content-body'),
    $Header: $('.Header')
};

window.app.views = {
    nav: new Header()
};

var mobileDetect = new MobileDetect(window.navigator.userAgent);
var phone = mobileDetect.phone();

if (navigator.maxTouchPoints && navigator.maxTouchPoints > 2 && /MacIntel/.test(navigator.platform)) {
    window.app.settings.isTablet = true;
}

window.app.settings.isDesktop = !phone && !app.settings.isTablet;
window.app.settings.isMobile = !!phone;

document.documentElement.className += ' ' + (app.settings.isDesktop ? 'isDesktop' : 'isNotDesktop');
document.documentElement.className += ' ' + (app.settings.isTablet ? 'isTablet' : 'isNotTablet');
document.documentElement.className += ' ' + (app.settings.isMobile ? 'isMobile' : 'isNotMobile');

//if youtube api is ready before all we should trigger "youtube-ready"
//cause onYouTubePlayerAPIReady on base.jinja can't invoke it (no app.vent on that moment)
if (window.app.state.youtubePlayerAPIReady) {
    window.app.vent.trigger('youtube-ready');
}

//if youtube api is ready before all we should trigger "youtube-ready"
//cause onYouTubePlayerAPIReady on base.jinja can't invoke it (no app.vent on that moment)
if (window.app.state.googleMapsAPIReady) {
    window.app.vent.trigger('google-maps-ready');
}

// Enabling frontend routing
app.els.$body.on('click', '.u-Route', function (e) {
    if (app.els.$body.hasClass('Page404')) {
        return;
    }

    var currentRoute = Backbone.history.getFragment();

    var parentUrl = $(e.target)
        .closest('a')
        .attr('href');

    var url = $(e.currentTarget)
        .attr('href') || parentUrl;

    e.preventDefault();
    Backbone.history.navigate(url, {trigger: 'true'});
});

app.router = new Router();

app.router.start();

//proceed any popup show/hide
//set all underlying content fixed position
app.vent.on('PopupShown', function () {
    window.app.settings.scrollingProgrammaticaly = true;
    var top = 0;
    var scrollTop = $(window)
        .scrollTop();

    // //first of all get top position of all elements that need to be fixed on popup shown
    // $('.NeedFixOnPopup').each(function (id, item) {
    //     var $item = $(item);
    //     $items.push($item);
    //     tops.push($item.offset().top);
    // });
    //
    // //after that set all items fixed position and position them at the very point there where they was
    // _.each($items, function ($item, ind) {
    //     $item
    //         .css('top', tops[ind] - scrollTop)
    //         .addClass('FixedOnPopup');
    // });

    top = $('.NeedFixOnPopup')
        .offset().top;

    if (app.settings.isMobile) {
        $('.Section-content')
            .addClass('overlay');
    }

    $('.NeedFixOnPopup')
        .css('top', top - scrollTop)
        .addClass('FixedOnPopup');

    app.state.popupShown = true;

    $(window)
        .resize();
});

app.vent.on('PopupHidded', function () {
    // $('.NeedFixOnPopup').each(function (id, item) {
    //     $(item)
    //         .css('top', '')
    //         .removeClass('FixedOnPopup');
    // });
    $('.NeedFixOnPopup')
        .css('top', '')
        .removeClass('FixedOnPopup');

    if (app.settings.isMobile) {
        $('.Section-content')
            .removeClass('overlay');
    }

    app.state.popupShown = false;
    $(window)
        .resize();
});

var $cursor = $('.Cursor');
var posX = 0;
var posY = 0;
var mouseX = 0;
var mouseY = 0;

gsap.to({}, 0.016, {
    repeat: -1,
    onRepeat: function () {
        posX += (mouseX - posX) / 9;
        posY += (mouseY - posY) / 9;

        gsap.set($cursor, {
            css: {
                top: mouseY - $cursor.innerHeight() / 2,
                left: mouseX - $cursor.innerWidth() / 2
            }
        });
    }
});

if (app.settings.isDesktop) {
    $(document).on('mousemove', function (e) {
        mouseX = e.clientX;
        mouseY = e.clientY;
    });
}

var loaderBarPercentage = 100;
var performanceData = window.performance.timing;
var estimatedTime = -(performanceData.loadEventEnd - performanceData.navigationStart);
var time = parseInt((estimatedTime / 1000) % 60) * 100;

if (!app.settings.isMobile) {
    $('.Loader-bar').animate({
        width: loaderBarPercentage + '%'
    }, time);
} else {
    $('.Loader-bar').animate({
        height: loaderBarPercentage + '%'
    }, time);
}

var $loaderPercentage = $('.Loader-percentage');
var	loaderPercentageStart = 0;
var	loaderPercentageEnd = 100;
var	loaderPercentageDuration = time;

animatePercentage($loaderPercentage, loaderPercentageStart, loaderPercentageEnd, loaderPercentageDuration);
        
function animatePercentage(id, start, end, duration) {
    var range = end - start;
    var current = start;
    var increment = end > start ? 1 : -1;
    var stepTime = Math.abs(Math.floor(duration / range));
    var obj = $(id);
    
    var timer = setInterval(function () {
        current += increment;
        $(obj).text(current + '%');

        if (current == end) {
            clearInterval(timer);
        }
    }, stepTime);
}

setTimeout(function () {
    $('.Loader').fadeOut(300);

    window.app.vent.trigger('loader');
}, time);

function setHeight () {
    var vh = window.innerHeight * 0.01;

    document.documentElement.style.setProperty('--vh', vh + 'px');
}

setHeight();
app.els.$window.on('resize', setHeight);

function orientationAlert () {
    if (app.settings.isTablet) {
        if (window.orientation == 0) {
            $('.Content').addClass('isPortrait');
            $('.Orientation-alert').addClass('isShow');
        } else {
            $('.Content').removeClass('isPortrait');
            $('.Orientation-alert').removeClass('isShow');
        }
    } else if (app.settings.isMobile) {
        if (window.orientation != 90) {
            $('.Content').removeClass('isLandscape');
            $('.Orientation-alert').removeClass('isShow');
        } else {
            $('.Content').addClass('isLandscape');
            $('.Orientation-alert').addClass('isShow');
        }
    }
}

orientationAlert();
app.els.$window.on('orientationchange', orientationAlert);