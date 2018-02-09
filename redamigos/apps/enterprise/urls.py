# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from redamigos.apps.enterprise.viewsets import EnterpriseViewSet


router = DefaultRouter()
router.register(r'enterprise', EnterpriseViewSet, 'enterprise')

urlpatterns = [
    url(r'^api/v1/', include(router.urls)),
]