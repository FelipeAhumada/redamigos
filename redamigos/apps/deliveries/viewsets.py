# -*- coding: utf-8 -*-
from rest_framework import viewsets
from .serializers import DeliverySerializer, TypeSerializer
from redamigos.apps.deliveries.models import Delivery, Type

class DeliveryViewSet(viewsets.ModelViewSet,):

    model = Delivery
    serializer_class = DeliverySerializer

    def get_queryset(self):
        return Delivery.objects.all()


class TypeViewSet(viewsets.ModelViewSet,):

    model = Type
    serializer_class = TypeSerializer

    def get_queryset(self):
        return Type.objects.all()
