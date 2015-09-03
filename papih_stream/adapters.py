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


class Youtube:
    def __init__(self):
        pass

    @staticmethod
    def get(request, raw):
        track = {}
        for result in raw.get("items", []):
            track['id'] = result["id"]
            track['url'] = reverse('stream_youtube-detail', args=[track['id']], request=request)
            track['title'] = result["snippet"]["title"]
            track['description'] = result["snippet"]["description"]
            track['thumbnail'] = result["snippet"]["thumbnails"]["high"]["url"]
            track['duration'] = str(int(isodate.parse_duration(result["contentDetails"]["duration"]).total_seconds()))
        return track

    @staticmethod
    def list(request, params, raw):
        prev_params = params.copy()
        next_params = params.copy()
        prev_params['page_token'] = raw['prevPageToken'] if 'prevPageToken' in raw else None
        next_params['page_token'] = raw['nextPageToken'] if 'nextPageToken' in raw else None

        tracks = []
        for result in raw.get("items", []):
            track = {}
            track['id'] = result["id"]["videoId"]
            track['url'] = reverse('stream_youtube-detail', args=[track['id']], request=request)
            track['title'] = result["snippet"]["title"]
            track['description'] = result["snippet"]["description"]
            track['thumbnail'] = result["snippet"]["thumbnails"]["high"]["url"]
            track['duration'] = str(int(isodate.parse_duration(result["contentDetails"]["duration"]).total_seconds()))
            tracks.append(track)

        return {
            'count': len(tracks),
            'prev': build_url('stream_youtube-list', params=prev_params, request=request) if prev_params['page_token'] else None,
            'next': build_url('stream_youtube-list', params=next_params, request=request) if next_params['page_token'] else None,
            'results': tracks,
        }


class Soundcloud:
    def __init__(self):
        pass

    @staticmethod
    def get(request, raw):
        track = {}
        track['id'] = str(raw['id'] or '')
        track['url'] = reverse('stream_soundcloud-detail', args=[track['id']], request=request)
        track['title'] = raw['title'] or ''
        track['description'] = raw['description'] or ''
        track['thumbnail'] = raw['artwork_url'].replace("large.jpg", "crop.jpg") if raw['artwork_url'] else ""
        track['duration'] = str(raw['duration'] / 1000 or '')
        return track


    @staticmethod
    def list(request, params, raw):
        prev_params = params.copy()
        next_params = params.copy()
        prev_params['page_token'] = int(params['page_token']) - 1 if int(params['page_token']) > 1 else None
        next_params['page_token'] = int(params['page_token']) + 1
        tracks = []
        for result in raw:
            track = {}
            if result['streamable'] is False:
                continue
            track['id'] = str(result['id'] or '')
            track['url'] = reverse('stream_soundcloud-detail', args=[track['id']], request=request)
            track['title'] = result['title'] or ''
            track['description'] = result['description'] or ''
            track['thumbnail'] = result['artwork_url'].replace("large.jpg", "crop.jpg") if result['artwork_url'] else ""
            track['duration'] = str(raw['duration'] / 1000 or '')
            tracks.append(track)
        return {
            'count': len(tracks),
            'prev': build_url('stream_soundcloud-list', params=prev_params, request=request) if prev_params['page_token'] else None,
            'next': build_url('stream_soundcloud-list', params=next_params, request=request) if next_params['page_token'] else None,
            'results': tracks,
        }