# -*- coding: utf-8 -*-

import sys
import os
import django

MY_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.abspath(MY_DIR+'/../../')
sys.path.append(BASE_DIR)
os.environ['DJANGO_SETTINGS_MODULE'] = 'config.settings_local'
django.setup()

from front import models


def regenerate_images():
    for year in models.TrueStoryYear.objects.all():
        if year.image:
            year.image.regenerate_images()

        if year.image2:
            year.image2.regenerate_images()

    for news in models.News.objects.all():
        if news.cover:
            news.cover.regenerate_images()

    for img in models.ContentBlock.objects.all():
        if img.image:
            img.image.regenerate_images()

    for img in models.ContentBlockGalleryImage.objects.all():
        if img.image:
            img.image.regenerate_images()

    for pos in models.SearchPosition.objects.all():
        if pos.logo:
            pos.logo.regenerate_images()

    for logo in models.CommonClient.objects.all():
        if logo.logo:
            logo.logo.regenerate_images()

    for member in models.CommonTeamPeople.objects.all():
        if member.image:
            member.image.regenerate_images()

    for placement in models.SearchRecentPlacement.objects.all():
        if placement.logo:
            placement.logo.regenerate_images()


if __name__ == '__main__':
    print "Regenerate images..."
    regenerate_images()
