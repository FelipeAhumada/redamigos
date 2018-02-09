# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from redamigos.apps.deliveries.viewsets import DeliveryViewSet, TypeViewSet


router = DefaultRouter()
router.register(r'delivery', DeliveryViewSet, 'delivery')
router.register(r'type', TypeViewSet, 'type')

urlpatterns = [
    url(r'^api/v1/', include(router.urls)),
]
