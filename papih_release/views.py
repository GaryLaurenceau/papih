from rest_framework import viewsets
from rest_framework.response import Response
from papih_key import models
import providers, adapters

class BasicView(viewsets.ViewSet):
    def list(self, request):
        params = {}
        params['query'] = request.GET.get('query', '')
        params['page_size'] = request.GET.get('page_size', 20)
        params['page_token'] = request.GET.get('page_token', '')
        result = self.adapter().list(request, params, self.provider().list(params, self.key.objects.get(owner=self.request.user)))
        return Response(result)

    def retrieve(self, request, pk=None):
        result = self.adapter().get(request, self.provider().get(pk, self.key.objects.get(owner=self.request.user)))
        return Response(result)


class Discogs(BasicView):
    key = models.Discogs
    provider = providers.Discogs
    adapter = adapters.Discogs
