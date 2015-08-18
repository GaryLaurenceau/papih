from rest_framework import serializers
import models


class Youtube(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = models.Youtube
        fields = ('url', 'owner', 'key')


class Soundcloud(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = models.Soundcloud
        fields = ('url', 'owner', 'key', 'secret')


class Discogs(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = models.Discogs
        fields = ('url', 'owner', 'key', 'secret')

