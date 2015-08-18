from rest_framework import routers
import views

router = routers.DefaultRouter()

router.register(r'user', views.User, base_name='user')
router.register(r'group', views.Group, base_name='group')
