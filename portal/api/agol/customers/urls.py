from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

from rest_framework.routers import DefaultRouter
from customers.views import (OrderViewSet,
                    BlacklistTokenUpdateView,
                    CustomerTrailerViewSet,
                    CustomerViewSet, 
                    VehicleViewSet, 
                    DriverViewSet,
                    CustomerDriverViewSet, 
                    LoginView,
                    CustomerTruckViewSet,
                    BulkOrderViewSet)

from customers.api import (
                    CustomerListAPI
                    )

router = DefaultRouter()

router.register('order', OrderViewSet, basename='customer order')
router.register('customer', CustomerViewSet, basename='customer')
router.register('vehicle', VehicleViewSet, basename='vehicle')
router.register('driver', DriverViewSet, basename='driver')
router.register('customer-driver', CustomerDriverViewSet, basename='customer-driver')
router.register('customer-driver/<int:pk>/', CustomerDriverViewSet, basename='customer-driver')
router.register('customer-truck', CustomerTruckViewSet, basename='customer-truck')
router.register('customer-trailer', CustomerTrailerViewSet, basename='customer-trailer')
router.register('bulk-order', BulkOrderViewSet, basename='bulk-order')

urlpatterns = [
    # path('', include(router.urls)),
    path("login/", LoginView.as_view(), name="login"),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('customer-list/',CustomerListAPI.as_view(), name="customer_list"),
    
    # path("order/", views.get_orders, name="get_orders"),
    # path('customer-trailer/', views.CustomerTrailerListView.as_view(), name='customer-trailer')

]

urlpatterns += router.urls