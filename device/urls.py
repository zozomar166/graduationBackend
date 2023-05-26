from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()
router.register('customers', views.CustomerViewSet, basename='customer')
router.register('blind', views.BlindViewSet, basename='blind')
router.register('devices', views.DeviceViewSet, basename='device')

customers_blind_router = routers.NestedDefaultRouter(router, 'customers', lookup='customers')
customers_blind_router.register('blind', views.BlindViewSet, basename='customers-blind')

customers_blind_devices_router = routers.NestedDefaultRouter(customers_blind_router, 'blind', lookup='blind')
customers_blind_devices_router.register('devices', views.DeviceViewSet, basename='blind-devices')

blind_devices_router = routers.NestedDefaultRouter(router, 'blind', lookup='blind')
blind_devices_router.register('devices', views.DeviceViewSet, basename='blind-devices')

urlpatterns = router.urls + customers_blind_router.urls + customers_blind_devices_router.urls + blind_devices_router.urls
