# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from redamigos.apps.chip.viewsets import ChipViewSet, StateViewSet, ChipDeliveryViewSet


router = DefaultRouter()
router.register(r'chip', ChipViewSet, 'chip')
router.register(r'state', StateViewSet, 'state')
router.register(r'sale', ChipDeliveryViewSet, 'sale')

urlpatterns = [
    url(r'^api/v1/', include(router.urls)),
]
