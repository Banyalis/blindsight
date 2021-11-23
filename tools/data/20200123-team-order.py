# -*- coding: utf-8 -*-

import sys
import os
import subprocess
import json
import django
from django.db import models
from django.db import DEFAULT_DB_ALIAS, connections
from django.core.management import call_command
import sqlparse


MY_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.abspath(MY_DIR+'/../../')
sys.path.append(BASE_DIR)
os.environ['DJANGO_SETTINGS_MODULE'] = 'config.settings_local'
django.setup()


from front.models import CommonTeamPeople


def process():

    max_order = CommonTeamPeople.objects.order_by('-order')[0].order

    for member in CommonTeamPeople.objects.filter(team=CommonTeamPeople.Team.Development):
        member.order = max_order
        member.save(update_fields=['order'])

        max_order += 11


if __name__ == '__main__':
    print "Rearrange team people..."
    process()
