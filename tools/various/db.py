# -*- coding: utf-8 -*-
import re
from django.db import models
from caching.base import CachingManager as CMCachingManager, CachingQuerySet as CMCachingQuerySet
from django.core.cache.backends.base import DEFAULT_TIMEOUT


class Base(models.Model):
    """
    Абстрактная модель с часто используемыми методами
    """
    order = models.IntegerField(blank=True, default=0)

    class Meta:
        ordering = ('order', 'id',)
        abstract = True


class CachingManager(CMCachingManager):

    def get_queryset(self):
        return CachingQuerySet(self.model, using=self._db)


class CachingQuerySet(CMCachingQuerySet):
    """
    Restore right DEFAULT_TIMEOUT after this:
    > self.filters = copy.deepcopy(self.base_filters)
    in django-filters(django_filters/filterset.py) BaseFilterSet constructor.

    Possible solution is replace deepcopy to:
            for k, v in self.base_filters.items():
            t = copy.deepcopy(v)
            if 'queryset' in v.__dict__:
                t.queryset.timeout = v.queryset.timeout
            self.filters[k] = t
    """

    def _clone(self, *args, **kw):
        qs = super(CachingQuerySet, self)._clone(*args, **kw)
        try:
            if self.timeout != DEFAULT_TIMEOUT:
                int(self.timeout)
            qs.timeout = self.timeout
        except TypeError:
            qs.timeout = DEFAULT_TIMEOUT
        return qs
