# -*- coding: utf-8 -*-
from rest_framework import viewsets
from .serializers import ChipSerializer, StateSerializer, ChipDeliverySerializer
from redamigos.apps.chip.models import Chip, State, ChipDelivery

class ChipViewSet(viewsets.ModelViewSet,):

    model = Chip
    serializer_class = ChipSerializer

    def get_queryset(self):
        return Chip.objects.all()


class StateViewSet(viewsets.ModelViewSet,):

    model = State
    serializer_class = StateSerializer

    def get_queryset(self):
        return State.objects.all()


class ChipDeliveryViewSet(viewsets.ModelViewSet,):

    model = ChipDelivery
    serializer_class = ChipDeliverySerializer

    def get_queryset(self):
        return ChipDelivery.objects.all()
