from django.contrib.auth import models
from rest_framework import serializers


class User(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.User
        fields = ('url', 'username', 'email', 'groups')


class Group(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Group
        fields = ('url', 'name')
