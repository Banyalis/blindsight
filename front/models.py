# -*- coding: utf-8 -*-

from django.db import models
from django.utils.functional import cached_property
from pytils.translit import slugify
from django.conf import settings
from django.template.loader import get_template
from django.utils.html import strip_tags

from tools.various.db import Base
from tools.various.fields import CustomListField
from tools.files.fields import CustomImgFieldS3, CustomFileFieldS3
from django.utils import timezone

from caching.base import CachingMixin
from tools.various.db import CachingManager

from django.core.mail import EmailMultiAlternatives
import xlwt
import pendulum
import json
import os
