# -*- coding: utf-8 -*-
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .serializers import EnterpriseSerializer
from redamigos.apps.enterprise.models import Enterprise

class EnterpriseViewSet(viewsets.ModelViewSet,):
    permission_classes = (AllowAny,)
    model = Enterprise
    serializer_class = EnterpriseSerializer

    def get_queryset(self):
        return Enterprise.objects.all()
