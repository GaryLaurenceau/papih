import json
from apiclient.discovery import build
from soundcloud import Client


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
