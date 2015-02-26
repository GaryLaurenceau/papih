from rest_framework import routers
import views

router = routers.DefaultRouter()

router.register(r'discogs', views.Discogs, base_name='track_discogs')
