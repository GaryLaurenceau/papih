from rest_framework import viewsets
import models
import serializers


class Youtube(viewsets.ModelViewSet):
    model = models.Youtube.objects.all()
    serializer_class = serializers.Youtube

    def get_queryset(self):
        return models.Youtube.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class Soundcloud(viewsets.ModelViewSet):
    model = models.Soundcloud.objects.all()
    serializer_class = serializers.Soundcloud

    def get_queryset(self):
        return models.Soundcloud.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class Discogs(viewsets.ModelViewSet):
    model = models.Discogs.objects.all()
    serializer_class = serializers.Discogs

    def get_queryset(self):
        return models.Discogs.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
