from django.contrib.auth import models
from rest_framework import viewsets
import serializers


class User(viewsets.ModelViewSet):
    queryset = models.User.objects.all()
    serializer_class = serializers.User


class Group(viewsets.ModelViewSet):
    queryset = models.Group.objects.all()
    serializer_class = serializers.Group
