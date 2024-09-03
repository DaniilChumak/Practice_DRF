from vehicle.apps import VehicleConfig
from rest_framework.routers import DefaultRouter
from vehicle.views import CarViewSet, BikeCreateAPIView, BikeListAPIView, BikeRetrieveAPIView, BikeUpdateAPIView, BikeDestroyAPIView
from django.urls import path

app_name = VehicleConfig.name

router = DefaultRouter()
router.register(r'cars', CarViewSet, basename='cars')

urlpatterns = [
    path('bike/create/', BikeCreateAPIView.as_view(), name='bike-create'),
    path('bike/', BikeListAPIView.as_view(), name='bike-list'),
    path('bike/<int:pk>/', BikeRetrieveAPIView.as_view(), name='bike-get'),
    path('bike/update/<int:pk>/', BikeUpdateAPIView.as_view(), name='bike-update'),
    path('bike/delete/<int:pk>/', BikeDestroyAPIView.as_view(), name='bike-delete'),
  ] + router.urls