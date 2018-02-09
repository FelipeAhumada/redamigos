# -*- coding: utf-8 -*-
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import SubsidiarySerializer
from redamigos.apps.subsidiary.models import Subsidiary

class SubsidiaryViewSet(viewsets.ModelViewSet,):
    permission_classes = (AllowAny,)
    model = Subsidiary
    serializer_class = SubsidiarySerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('enterprise',)

    def get_queryset(self):
        return Subsidiary.objects.all()
