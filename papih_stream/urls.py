from rest_framework import routers
import views

router = routers.DefaultRouter()

router.register(r'youtube', views.Youtube, base_name='stream_youtube')
router.register(r'soundcloud', views.Soundcloud, base_name='stream_soundcloud')
