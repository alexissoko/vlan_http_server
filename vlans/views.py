from django.shortcuts import render

from rest_framework import generics, permissions, mixins, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from django.urls import reverse_lazy # new

from .models import Vlan
from .serializers import VlanSerializer



class UpdateVlan(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Vlan.objects.all()
    serializer_class = VlanSerializer
    # only authenticated users can POST otherwise only GET methods in API
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save()


class DeleteVlan(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Vlan.objects.all()
    serializer_class = VlanSerializer
    # only authenticated users can POST otherwise only GET methods in API
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save()


class VlansList(generics.ListCreateAPIView):
    queryset = Vlan.objects.all()
    serializer_class = VlanSerializer
    # only authenticated users can POST otherwise only GET methods in API
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save()
