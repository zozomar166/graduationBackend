from rest_framework import routers
from rest_framework.routers import DefaultRouter
from . import views

router = routers.DefaultRouter()
router.register('device', views.DeviceViewSet, basename='device')
router.register('customer', views.CustomerViewSet, basename='customer')
urlpatterns = router.urls
