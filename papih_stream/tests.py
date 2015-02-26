from django.test import TestCase

# Create your tests here.

import providers, adapters
import json


def prettyprint(obj):
    print json.dumps(obj, sort_keys=True, indent=4, separators=(',', ': '))
    print '\n\n'


#class Youtube:
#    key = 'AIzaSyB8Ld7UXx_Q0vRff_CTi7rwbPpgMzpxUU0'
#
#youtubeProvider = providers.Youtube()
#youtubeAdapter = adapters.Youtube()
#prettyprint(youtubeAdapter.list(None, youtubeProvider.list({'query': 'jaar', 'page_size': '5'}, Youtube())))


#class Soundcloud:
#    key = 'e0e75f69d1d8d800594a55ed65e67a0d'
#    secret = '1b4c86a301c80629a1fbea87b23eead7'
#
#soundcloudProvider = providers.Soundcloud()
#prettyprint(soundcloudProvider.list({'query': 'jaar', 'page_size': '5'}, Soundcloud()))
