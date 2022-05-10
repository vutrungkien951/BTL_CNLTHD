from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(prefix='rides', viewset=views.RideViewSet, basename='ride')
router.register(prefix='ports', viewset=views.PortViewSet, basename='port')

urlpatterns = [
    path('', include(router.urls))
]
