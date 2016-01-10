from __future__ import unicode_literals

from django.db import models
from .utils import class_name_pk

# Create your models here.

max_length = 300

CLIENT_ICONS = (('briefcase', 'Corporate'), ('building', 'Government'), )


class Client(models.Model):
    icon = models.CharField(max_length=max_length, choices=CLIENT_ICONS)
    name = models.CharField(default=None,
                            max_length=max_length,
                            blank=True,
                            null=True)
    text = models.TextField(default=None, blank=True, null=True)

    def __unicode__(self):
        return class_name_pk(self)


class Service(models.Model):
    name = models.CharField(max_length=max_length, blank=True, null=True)
    icon = models.CharField(default=None,
                            max_length=max_length,
                            blank=True,
                            null=True)
    text = models.TextField(default=None, blank=True, null=True)

    def __unicode__(self):
        return class_name_pk(self)


class TeamMember(models.Model):
    name = models.CharField(max_length=max_length, blank=True, null=True)
    icon = models.ImageField(blank=True, null=True)
    text = models.TextField(default=None, blank=True, null=True)

    def __unicode__(self):
        return class_name_pk(self)


class Testimonial(models.Model):
    name = models.CharField(max_length=max_length, blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    date = models.DateTimeField(default=None, blank=True, null=True)

    def __unicode__(self):
        return class_name_pk(self)
