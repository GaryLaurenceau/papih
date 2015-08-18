from rest_framework.reverse import reverse
from django.http import QueryDict
import isodate

def build_url(*args, **kwargs):
    params = kwargs.pop('params', {})
    url = reverse(*args, **kwargs)
    if not params: return url

    qdict = QueryDict('', mutable=True)
    for k, v in params.iteritems():
        if type(v) is list: qdict.setlist(k, v)
        else: qdict[k] = v

    return url + '?' + qdict.urlencode()


class Discogs:
    def __init__(self):
        pass

    @staticmethod
    def get(request, raw):
        artist = {}
        artist['id'] = str(raw['id'] or '')
        artist['url'] = reverse('artist_discogs-detail', args=[artist['id']], request=request)
        artist['name'] = raw['name'] if 'name' in raw else ''
        artist['description'] = raw['profile'] if 'profile' in raw else ''
        return artist


    @staticmethod
    def list(request, params, raw):
        prev_params = params.copy()
        next_params = params.copy()
        prev_params['page_token'] = int(params['page_token']) - 1 if int(params['page_token']) > 1 else None
        next_params['page_token'] = int(params['page_token']) + 1
        artists = []
        for result in raw['results']:
            artist = {}
            artist['id'] = str(result['id'] or '')
            artist['url'] = reverse('artist_discogs-detail', args=[artist['id']], request=request)
            artist['name'] = result['title']  if 'title' in result else ''
            artists.append(artist)
        return {
            'count': len(artists),
            'prev': build_url('artist_discogs-list', params=prev_params, request=request) if prev_params['page_token'] else None,
            'next': build_url('artist_discogs-list', params=next_params, request=request) if next_params['page_token'] else None,
            'results': artists,
        }
