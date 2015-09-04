import json
from apiclient.discovery import build
from soundcloud import Client
import requests
from papih import settings

class Youtube:
    YOUTUBE_API_SERVICE_NAME = "youtube"
    YOUTUBE_API_VERSION = "v3"

    def __init__(self):
        pass

    def get(self, pk, auth):
        client = build(self.YOUTUBE_API_SERVICE_NAME, self.YOUTUBE_API_VERSION, developerKey=auth.key)
        response = client.videos().list(
            id=pk,
            part='id,snippet,contentDetails',
        ).execute()
        return response

    def list(self, params, auth):
        client = build(self.YOUTUBE_API_SERVICE_NAME, self.YOUTUBE_API_VERSION, developerKey=auth.key)
        response = client.search().list(
            q=params['query'],
            type='video',
            part='id,snippet',
            order='relevance',
            maxResults=params['page_size'],
            pageToken=params['page_token'],
        ).execute()
        response = self.getvideoduration(response, auth)
        return response


## See https://code.google.com/p/gdata-issues/issues/detail?id=4294
## no other way to do it due tu google implementation
    def getvideoduration(self, response, auth):
        idlist = []
        for result in response.get("items", []):
            idlist.append(result["id"]["videoId"])
        print idlist
        stridlist = ",".join(idlist)
        print stridlist
        headers = {
            'user-agent': "musicsphere",
        }
        params = {
            'id': stridlist,
            'part': 'id,snippet,contentDetails',
            'key': auth.key,
        }
        secresponse = requests.get(
            'https://www.googleapis.com/youtube/v3/videos',
            params=params,
            headers=headers
        )
        a = json.loads(secresponse.content)
        response ['items'] = a['items']
        return response



class Soundcloud:
    def __init__(self):
        pass

    @staticmethod
    def get(pk, auth):
        client = Client(client_id=auth.key, client_secret=auth.secret)
        response = client.get(
            '/tracks/' + pk,
        )
        response = json.loads(response.raw_data)
        return response

    @staticmethod
    def list(params, auth):
        if params['page_token'] == '':
            params['page_token'] = 1

        client = Client(client_id=auth.key, client_secret=auth.secret)
        response = client.get(
            '/tracks',
            q=params['query'],
            limit=params['page_size'],
            offset=(int(params['page_token']) - 1) * int(params['page_size']),
        )
        response = json.loads(response.raw_data)
        return response
