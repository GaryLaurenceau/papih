from rest_framework import routers
import views

router = routers.DefaultRouter()

router.register(r'youtube', views.Youtube, base_name='youtube')
router.register(r'soundcloud', views.Soundcloud, base_name='soundcloud')
router.register(r'discogs', views.Discogs, base_name='discogs')
