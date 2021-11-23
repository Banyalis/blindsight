module.exports = {
    createEmptyPromise: function () {
        return new Promise(function (resolve) {
            resolve();
        });
    },

    detectVideoAutoplayFeature: function (cb) {
        var blankVideo = 'data:video/mp4;base64,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IHdlaWdodGI9MCBvcGVuX2dvcD0wIHdlaWdodHA9MCBrZXlpbnQ9MzAwIGtleWludF9taW49MzAgc2NlbmVjdXQ9NDAgaW50cmFfcmVmcmVzaD0wIHJjX2xvb2thaGVhZD02MCByYz1jcmYgbWJ0cmVlPTEgY3JmPTUxLjAgcWNvbXA9MC42MCBxcG1pbj0wIHFwbWF4PTY5IHFwc3RlcD00IHZidl9tYXhyYXRlPTIwMDAwIHZidl9idWZzaXplPTI1MDAwIGNyZl9tYXg9MC4wIG5hbF9ocmQ9bm9uZSBmaWxsZXI9MCBpcF9yYXRpbz0xLjQwIGFxPTE6MS4wMACAAAADj2WIgQAGomKAAeunc99999999999999999999999999999999999999bvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrwAAAACUGaCRYJQASxgAAAAAlBnhCDgSgAljAAAAAIAZ4YE0UAEsYAAAAIAZ4YI0UAEsYAAAAIAZ4YM0UAEsYAAAAIAZ4YQ0UAEsYAAAAIAZ4YU0UAEsYAAAAIAZ4YY0UAEsYAAAAIAZ4Yc0UAEsYAAAAIAZ4YlqUAEsYAAAAIAZ4YpqUAEsYAAAAIAZ4YtqUAEsYAAAAIAZ4YxqUAEsYAAAAIAZ4Y1qUAEsYAAAAIAZ4Y5qUAEsYAAAAIAZ4Y9qUAEsYAAAAIAZ4ZBqUAEsYAAAAKQZoZ1eloigAljAAAAAlBniFy4OgAljAAAAAJAZ4pItFABLGAAAAACQGeKTLRQASxgAAAAAkBnilC0UAEsYAAAAAJAZ4pUtFABLGAAAAACQGeKWLRQASxgAAAAAkBnimGSUAEsYAAAAAJAZ4plklABLGAAAAACQGeKaZJQASxgAAAAAkBnim2SUAEsYAAAAAJAZ4pxklABLGA';
        var $video = $('<video muted playsinline crossorigin loop preload="auto">')
            .attr('src', blankVideo)
            .css({
                'position': 'absolute',
                'top': -9999
            })
            .appendTo('body');
        var playPromise = $video[0].play();

        if (playPromise !== undefined) {
            playPromise
                .then(function () {
                    $video.remove();
                    cb(true);
                })
                .catch(function () {
                    $video.remove();
                    cb(false);
                });
        } else {
            $video.remove();

            setTimeout(function () {
                cb(true);
            }, 100);
        }
    }
};