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
        release = {}
        release['id'] = str(raw['id'] or '')
        release['url'] = reverse('release_discogs-detail', args=[release['id']], request=request)
        release['title'] = raw['title'] if 'title' in raw else ''
        # release['thumbnail'] = raw['thumb'] if 'thumb' in raw else ''
        release['date'] = raw['released'] if 'released' in raw else ''
        release['genres'] = raw['genres'] if 'genres' in raw else ''
        release['artists'] = []
        for artist in raw['artists']:
            release['artists'].append(reverse('artist_discogs-detail', args=[artist['id']], request=request))
        release['tracklist'] = []
        for track in raw['tracklist']:
            release['tracklist'].append(track['title'])
        return release


    @staticmethod
    def list(request, params, raw):
        prev_params = params.copy()
        next_params = params.copy()
        prev_params['page_token'] = int(params['page_token']) - 1 if int(params['page_token']) > 1 else None
        next_params['page_token'] = int(params['page_token']) + 1
        releases = []
        for result in raw['results']:
            release = {}
            release['id'] = str(result['id'] or '')
            release['url'] = reverse('release_discogs-detail', args=[release['id']], request=request)
            release['title'] = result['title']  if 'title' in result else ''
            releases.append(release)
        return {
            'count': len(releases),
            'prev': build_url('release_discogs-list', params=prev_params, request=request) if prev_params['page_token'] else None,
            'next': build_url('release_discogs-list', params=next_params, request=request) if next_params['page_token'] else None,
            'results': releases,
        }
