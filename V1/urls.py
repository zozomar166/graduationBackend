from django.urls import path
from django.urls.conf import include
from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()
router.register('customers', views.CustomerViewSet, basename='customers')
router.register('blinds', views.BlindViewSet, basename='blinds')
router.register('devices', views.DeviceViewSet, basename='devices')

customer_router = routers.NestedDefaultRouter(router, 'customers', lookup='customers')
customer_router.register('blinds', views.CustomerViewSet, basename='customers-blinds')

customer_blind_devices_router = routers.NestedDefaultRouter(customer_router, 'blinds', lookup='blinds')
customer_blind_devices_router.register('devices', views.DeviceViewSet, basename='customers-devices')

blind_router = routers.NestedDefaultRouter(router, 'blinds', lookup='blinds')
blind_router.register('devices', views.DeviceViewSet, basename='blinds-devices')

urlpatterns = router.urls + customer_router.urls + customer_blind_devices_router.urls + blind_router.urls
