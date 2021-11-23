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


def call_duply(age=None):
    try:
        os.unlink(os.path.join(MY_DIR, 'duply-database.sql'))
    except OSError:
        pass
    args = ['duply', 'trueplatform.com', 'fetch', 'database.sql', os.path.join(MY_DIR, 'duply-database.sql')]
    if age:
        args.append(age)
    subprocess.call(args)


def parse():

    f = open(os.path.join(MY_DIR, 'duply-database.sql'), 'r')
    source = sqlparse.parse(f)

    credits = []
    force = False

    for statement in source:

        if statement.get_type() != 'INSERT':
            continue

        table = unicode(filter(lambda x: isinstance(x, sqlparse.sql.Identifier), statement.tokens)[0])
        # values = list(unicode(t).strip(' \'') for t in unicode(statement.tokens[-2][1]).split('\',\''))

        if table != '`front_commonteampeople`':
            continue

        print(table)

        values = filter(lambda x: isinstance(x, sqlparse.sql.Values), statement.tokens)[0]

        orders = {
            int(str(row[1][0])): int(str(row[1][2]))
            for row in filter(
                lambda x: isinstance(x, sqlparse.sql.Parenthesis),
                values.tokens)
        }

        return orders


def process():

    age = 1

    exists = dict(CommonTeamPeople.objects.all().values_list('id', 'order'))

    while True:

        duply_age = '%dD' % age

        print 'AGE: ', duply_age

        call_duply(duply_age)
        parsed = parse()

        diff = False

        for key, order in parsed.iteritems():
            exists_order = exists.get(key, None)
            # print key, order, exists_order
            if exists_order is not None and order != exists_order:
                print key, order, exists_order
                obj = CommonTeamPeople.objects.get(id=key)
                obj.order = order
                obj.save(update_fields=['order'])
                diff = True

        if diff:
            break

        age += 1


if __name__ == '__main__':
    print "Parse team people..."
    process()
