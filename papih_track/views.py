from rest_framework import viewsets
from rest_framework.response import Response
<<<<<<< HEAD
from papih_key import models
import providers, adapters
=======
from papih_utils import view_utils
from papih_key import models
import providers
import adapters

>>>>>>> develop

class BasicView(viewsets.ViewSet):
    def list(self, request):
        params = {}
        params['query'] = request.GET.get('query', '')
        params['page_size'] = request.GET.get('page_size', 20)
        params['page_token'] = request.GET.get('page_token', '')
<<<<<<< HEAD
        result = self.adapter().list(request, params, self.provider().list(params, self.key.objects.get(owner=self.request.user)))
        return Response(result)

    def retrieve(self, request, pk=None):
        result = self.adapter().get(request, self.provider().get(pk, self.key.objects.get(owner=self.request.user)))
=======

        key = view_utils.get_key(self.keys, self.request.user)

        result = self.adapter().list(
            request,
            params,
            self.provider().list(params, key)
        )
        return Response(result)

    def retrieve(self, request, pk=None):
        key = view_utils.get_key(self.keys, self.request.user)

        result = self.adapter().get(
            request,
            self.provider().get(pk, key)
        )
>>>>>>> develop
        return Response(result)


class Discogs(BasicView):
    key = models.Discogs
    provider = providers.Discogs
    adapter = adapters.Discogs
