from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()
router.register('devices', views.DeviceViewSet, basename='device')
router.register('customers', views.CustomerViewSet, basename='customer')

customers_router = routers.NestedDefaultRouter(router, 'customers', lookup='customers')
customers_router.register('devices', views.DeviceViewSet, basename='customers-devices')

# users_router = routers.NestedDefaultRouter(router, 'users', lookup='id')
# users_router.register('customers', views.CustomerViewSet, basename='users-customers')
urlpatterns = router.urls + customers_router.urls

