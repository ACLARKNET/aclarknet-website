from __future__ import unicode_literals

from django.db import models
from solo.models import SingletonModel
from .utils import class_name_pk

# Create your models here.

MAX_LENGTH = 300


class Company(SingletonModel):
    """
    """
    name = models.CharField(max_length=255, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'Company'


class Developer(models.Model):
    active = models.NullBooleanField(default=True, blank=True, null=True)
    description = models.TextField(default=None, blank=True, null=True)
    name = models.CharField(max_length=MAX_LENGTH, blank=True, null=True)
    photo = models.ImageField(blank=True, null=True)

    def __unicode__(self):
        return class_name_pk(self)


class Page(models.Model):
    active = models.NullBooleanField(default=True, blank=True, null=True)
    name = models.CharField(max_length=MAX_LENGTH, blank=True, null=True)
    description = models.TextField(default=None, blank=True, null=True)
    body = models.TextField(default=None, blank=True, null=True)
    slug = models.SlugField(max_length=MAX_LENGTH)

    def __unicode__(self):
        return class_name_pk(self)


class Partner(models.Model):
    active = models.NullBooleanField(default=True, blank=True, null=True)
    description = models.TextField(default=None, blank=True, null=True)
    name = models.CharField(max_length=MAX_LENGTH, blank=True, null=True)
    photo = models.ImageField(blank=True, null=True)

    def __unicode__(self):
        return class_name_pk(self)
