from __future__ import unicode_literals

from django.db import models
from .utils import class_name_pk

# Create your models here.

MAX_LENGTH = 300

CLIENT_ICONS = (('briefcase', 'Corporate'), ('building', 'Government'), )
SERVICE_ICONS = (('briefcase', 'Corporate'), ('building', 'Government'), )


class Client(models.Model):
    active = models.NullBooleanField(default=True, blank=True, null=True)
    icon = models.CharField(default='briefcase',
                            max_length=MAX_LENGTH,
                            choices=CLIENT_ICONS)
    description = models.TextField(default=None, blank=True, null=True)
    name = models.CharField(default=None,
                            max_length=MAX_LENGTH,
                            blank=True,
                            null=True)

    def __unicode__(self):
        return class_name_pk(self)


class Service(models.Model):
    active = models.NullBooleanField(default=True, blank=True, null=True)
    icon = models.CharField(default='briefcase',
                            max_length=MAX_LENGTH,
                            choices=CLIENT_ICONS)
    description = models.TextField(default=None, blank=True, null=True)
    name = models.CharField(max_length=MAX_LENGTH, blank=True, null=True)

    def __unicode__(self):
        return class_name_pk(self)


class Developer(models.Model):
    active = models.NullBooleanField(default=True, blank=True, null=True)
    description = models.TextField(default=None, blank=True, null=True)
    name = models.CharField(max_length=MAX_LENGTH, blank=True, null=True)
    photo = models.ImageField(blank=True, null=True)

    def __unicode__(self):
        return class_name_pk(self)


class Partner(models.Model):
    active = models.NullBooleanField(default=True, blank=True, null=True)
    description = models.TextField(default=None, blank=True, null=True)
    name = models.CharField(max_length=MAX_LENGTH, blank=True, null=True)
    photo = models.ImageField(blank=True, null=True)

    def __unicode__(self):
        return class_name_pk(self)


class Testimonial(models.Model):
    active = models.NullBooleanField(default=True, blank=True, null=True)
    author = models.CharField(max_length=MAX_LENGTH, blank=True, null=True)
    date = models.DateTimeField(default=None, blank=True, null=True)
    testimonial = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return class_name_pk(self)
