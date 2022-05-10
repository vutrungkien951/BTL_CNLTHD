from django.shortcuts import render
from .models import Ride, Port
from rest_framework import viewsets, permissions, generics
from .serializers import RideSerializer, PortSerializer
# Create your views here.


class RideViewSet(viewsets.ViewSet, generics.ListAPIView):
    serializer_class = RideSerializer
    permission_classes = [permissions.AllowAny]
    queryset = Ride.objects.filter(active=True)


class PortViewSet(viewsets.ModelViewSet):
    serializer_class = PortSerializer
    permission_classes = [permissions.AllowAny]
    queryset = Port.objects.filter(active=True)