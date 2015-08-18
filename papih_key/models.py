from django.db import models
from django.contrib.auth.models import User


class Youtube(models.Model):
    owner = models.ForeignKey(User, related_name='key_youtube')
    key = models.CharField(max_length=64, blank=True, default='')


class Soundcloud(models.Model):
    owner = models.ForeignKey(User, related_name='key_soundcloud')
    key = models.CharField(max_length=64, blank=True, default='')
    secret = models.CharField(max_length=64, blank=True, default='')


class Discogs(models.Model):
    owner = models.ForeignKey(User, related_name='key_discogs')
    key = models.CharField(max_length=64, blank=True, default='')
    secret = models.CharField(max_length=64, blank=True, default='')
