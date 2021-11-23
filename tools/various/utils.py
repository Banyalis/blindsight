# -*- coding: utf-8 -*-

import urllib2
import oembed
import re
import json

from tools.remote_typograf.RemoteTypograf import RemoteTypograf


def find(f, seq):
    """Return first item in sequence where f(item) == True."""
    for item in seq:
        if f(item):
            return item


# Количество символов Unicode на которые разбивать строки для Типографа
CHUNK_SIZE = 15000


def fix_markup(text):
    return text.replace(u'&#132;', u'&bdquo;') \
        .replace(u'&#8222;', u'&bdquo;') \
        .replace(u'&#147;', u'&ldquo;') \
        .replace(u'&#8220;', u'&ldquo;') \
        .replace(u'&#151;', u'&mdash;') \
        .replace(u'&#150;', u'&ndash;') \
        .replace(u'&#145;', u'&lsquo;') \
        .replace(u'&#146;', u'&rsquo;')


def decode(data):
    return unicode(urllib2.unquote(data.encode('utf-8')).decode('utf-8'))


def get_oembed(video_url):

    consumer = oembed.OEmbedConsumer()
    endpoint = oembed.OEmbedEndpoint('http://www.youtube.com/oembed', [str(s) for s in ['http://*.youtube.com/*', 'http://youtu.be/*', 'https://*.youtube.com/*', 'https://youtu.be/*']])
    consumer.addEndpoint(endpoint)
    endpoint = oembed.OEmbedEndpoint('https://vimeo.com/api/oembed.json', [str(s) for s in ['http://*.vimeo.com/*', 'https://*.vimeo.com/*', 'http://vimeo.com/*', 'https://vimeo.com/*']])
    consumer.addEndpoint(endpoint)
    endpoint = oembed.OEmbedEndpoint('http://www.soundcloud.com/oembed?format=json&maxheight=200', [str(s) for s in ['http://*.soundcloud.com/*', 'https://*.soundcloud.com/*', 'http://soundcloud.com/*', 'https://soundcloud.com/*']])
    consumer.addEndpoint(endpoint)

    response = consumer.embed(video_url)
    return response.getData()


def oembed_parsed(video_url):
    video_url = video_url.strip()
    video_provider = ''
    video_oembed = ''
    video_id = ''
    video_preview = ''
    video_height = None
    video_width = None
    video_duration = None
    try:
        res = get_oembed(video_url)
        #print res
        video_provider = res['provider_name'].lower()
        video_oembed = res['html']
        video_preview = res['thumbnail_url']
        video_height = res.get('height')
        video_width = res.get('width')
        video_duration = res.get('duration')
        # print(json.dumps(res, indent=2))

        if video_provider == 'youtube':
            pattern = r'(?:https?:\/\/)?(?:[0-9A-Z-]+\.)?(?:youtube|youtu|youtube-nocookie)\.(?:com|be)\/(?:watch\?v=|watch\?.+&v=|embed\/|v\/|.+\?v=)?([^&=\n%\?]{11})'
            video_id = re.findall(pattern, video_url, re.IGNORECASE)[0]
        else:
            video_id = res['video_id']
    except:
        pass

    return video_provider, video_oembed, video_id, video_preview, video_height, video_width, video_duration
