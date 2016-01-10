from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Client(models.Model):
    icon = models.CharField(default=None, max_length=30, null=True)
    name = models.CharField(default=None, max_length=90)
    text = models.TextField(default=None)

    def __unicode__(self):
        return self.name


class Service(models.Model):
    name = models.CharField(max_length=60)
    icon = models.CharField(default=None, max_length=30)
    text = models.TextField(default=None)

    def __unicode__(self):
        return self.name


class TeamMember(models.Model):
    name = models.CharField(max_length=60)
    icon = models.ImageField()
    text = models.TextField(default=None)

    def __unicode__(self):
        return self.name


class Testimonial(models.Model):
    name = models.CharField(max_length=120)
    text = models.TextField()
    date = models.DateTimeField(default=None)

    def __unicode__(self):
        return self.name
