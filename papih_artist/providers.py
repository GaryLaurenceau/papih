import json
import urllib


class Discogs:
    def __init__(self):
        pass

    @staticmethod
    def get(pk, auth):
        params = {
            'key' : auth.key,
            'secret' : auth.secret,
        }
        url = 'https://api.discogs.com/artists/%s?%s' % (pk, urllib.urlencode(params))
        response = json.loads(urllib.urlopen(url).read())
        print json.dumps(response, sort_keys=True, indent=4, separators=(',', ': '))
        return response

    @staticmethod
    def list(params, auth):
        if params['page_token'] == '':
            params['page_token'] = 1

        params = {
            'type' : 'artist',
            'q' : params['query'],
            'page' : params['page_token'],
            'per_page' : params['page_size'],
            'key' : auth.key,
            'secret' : auth.secret,
        }
        url = 'https://api.discogs.com/database/search?%s' % (urllib.urlencode(params))
        response = json.loads(urllib.urlopen(url).read())
        print json.dumps(response, sort_keys=True, indent=4, separators=(',', ': '))
        return response
