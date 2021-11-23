# -*- coding: utf-8 -*-

import sys
import os
import json
import django
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
import urllib


MY_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.abspath(MY_DIR+'/../../')
sys.path.append(BASE_DIR)
os.environ['DJANGO_SETTINGS_MODULE'] = 'config.settings_local'
django.setup()


from front.models import SearchRecentPlacementPractice, SearchRecentPlacementFunction,\
    SearchRecentPlacementAssetClass, SearchRecentPlacementLocation, SearchRecentPlacementQuarter, SearchRecentPlacement

from control.serializers.search import SearchRecentPlacementPracticeSerializer,\
    SearchRecentPlacementFunctionSerializer, SearchRecentPlacementAssetClassSerializer,\
    SearchRecentPlacementLocationSerializer, SearchRecentPlacementQuarterSerializer, SearchRecentPlacementSerializer


def scroll_shim(passed_in_driver, object):
    x = object.location['x']
    y = object.location['y']
    scroll_by_coord = 'window.scrollTo(%s,%s);' % (
        x,
        y
    )
    scroll_nav_out_of_way = 'window.scrollBy(0, -120);'
    passed_in_driver.execute_script(scroll_by_coord)
    passed_in_driver.execute_script(scroll_nav_out_of_way)


def parse():

    filters = dict()
    filtersIds = dict()
    classes = dict()

    filtersSerializers = {
        'practices': SearchRecentPlacementPracticeSerializer,
        'functions': SearchRecentPlacementFunctionSerializer,
        'asset-classes': SearchRecentPlacementAssetClassSerializer,
        'locations': SearchRecentPlacementLocationSerializer,
        'quarters': SearchRecentPlacementQuarterSerializer,
    }

    filtersFields = {
        'practices': 'practice_id',
        'functions': 'function_id',
        'asset-classes': 'asset_class_id',
        'locations': 'location_id',
        'quarters': 'quarter_id',
    }

    opts = Options()
    # opts.headless = True
    browser = Firefox(options=opts)
    browser.get('https://truesearch.com/placement_collection/2019-placements/#-')
    el = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'placement-previews'))
    )

    for select in browser.find_elements_by_class_name('sf-input-select'):
        name = select.get_attribute('name')

        filters[name] = dict()

        for option in select.find_elements_by_xpath('.//option'):
            value = option.get_attribute('value')
            title = option.text

            if value:
                filters[name][value] = title
                classes[value] = name

    print json.dumps(filters, indent=4)

    # SearchRecentPlacementPractice.objects.all().delete()
    # SearchRecentPlacementFunction.objects.all().delete()
    # SearchRecentPlacementAssetClass.objects.all().delete()
    # SearchRecentPlacementLocation.objects.all().delete()
    # SearchRecentPlacementQuarter.objects.all().delete()
    # SearchRecentPlacement.objects.all().delete()

    existFilters = dict()

    for filter in filtersSerializers.iterkeys():
        filtersIds[filter] = dict()
        for value in filtersSerializers[filter].Meta.model.objects.all():
            filtersIds[filter][value.title] = value.id

    for filter in filters.iterkeys():
        if filter not in filtersIds:
            filtersIds[filter] = dict()
        serializer = filtersSerializers.get(filter, None)
        if not serializer:
            print "Cannot find serializer for", filter
            continue

        for val, title in filters[filter].iteritems():

            if not filtersIds[filter].get(title, None):

                s = serializer(data={'title': title}, context={'view': {'request': {}}})

                print "New filter", filter, title, val

                if s.is_valid():
                    inst = s.save()
                    filtersIds[filter][title] = inst.id

    print json.dumps(filtersIds, indent=4)
    print "===="

    for elem in el.find_elements_by_class_name('placement-preview')[:1]:
        cls = elem.get_attribute('class')
        img_elem = elem.find_element_by_xpath('.//img')
        img_src = img_elem.get_attribute('src')
        title = elem.find_element_by_xpath('.//h3').text
        location = elem.find_element_by_xpath('.//li').text

        # print title
        #
        # scroll_shim(browser, img_elem)
        # ActionChains(browser).move_to_element(img_elem).context_click().pause(2)\
        #     .send_keys(Keys.ARROW_DOWN, Keys.ARROW_DOWN, Keys.ARROW_DOWN, Keys.ARROW_DOWN,
        #                Keys.ARROW_DOWN, Keys.ENTER, Keys.ENTER)\
        #     .pause(1).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
        #
        # return
        # continue

        filter = dict()
        for cl in cls.split(' '):
            t = classes.get(cl, None)

            if not t:
                if cl != "placement-preview":
                    print u'Can`t parse class "%s"' % (cl, )
                continue

            _t = t.replace('-', '_')

            if t not in filter:
                filter[_t] = list()
            filter[_t].append(dict([(filtersFields[t], filtersIds[t][filters[t][cl]])]))

        print json.dumps(filter)

        # Trying to find previous parsed item

        try:
            instance = SearchRecentPlacement.objects.get(
                title=title,
                location=location,
                quarters__quarter_id__in=[q['quarter_id'] for q in filter.get('quarters', [])],
            )
        except SearchRecentPlacement.DoesNotExist:
            instance = None

        if instance:
            print "%s already exist: %d" % (title, instance.id, )
            continue

        # print json.dumps(filter, indent=4)

        data = {
            'title': title,
            'location': location,
            'practices': [],
            'functions': [],
            'asset_classes': [],
            'locations': [],
            'quarters': [],
        }

        data.update(filter)
        print json.dumps(data, indent=4)

        s = SearchRecentPlacementSerializer(data=data)

        if s.is_valid():
            s.save()
        else:
            print s.errors

        # print title, location, classes, img_src

        print "\n\n"

    browser.quit()


if __name__ == '__main__':
    print "Parse recent placements..."
    parse()
