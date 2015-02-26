from django.conf.urls import include, url
from django.contrib import admin
from papih_user.urls import router as user_router
from papih_key.urls import router as key_router
from papih_track.urls import router as track_router
from papih_artist.urls import router as artist_router
from papih_release.urls import router as release_router
from papih_stream.urls import router as stream_router

admin.autodiscover()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),

    url(r'^', include(user_router.urls)),
    url(r'^key/', include(key_router.urls)),
    url(r'^track/', include(track_router.urls)),
    url(r'^artist/', include(artist_router.urls)),
    url(r'^release/', include(release_router.urls)),
    url(r'^stream/', include(stream_router.urls)),
]
