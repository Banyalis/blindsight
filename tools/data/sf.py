# -*- coding: utf-8 -*-

import sys
import os
import django

MY_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.abspath(MY_DIR+'/../../')
sys.path.append(BASE_DIR)
os.environ['DJANGO_SETTINGS_MODULE'] = 'config.settings_local'
django.setup()


if __name__ == '__main__':
    print "Salesforce test script"
