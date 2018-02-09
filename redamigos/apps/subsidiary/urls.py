# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from redamigos.apps.subsidiary.viewsets import SubsidiaryViewSet


router = DefaultRouter()
router.register(r'subsidiary', SubsidiaryViewSet, 'subsidiary')

urlpatterns = [
    url(r'^api/v1/', include(router.urls)),
]