# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from redamigos.apps.user.viewsets import (
    UserViewSet,
    UserGeneralViewSet,
    PasswordChangeView,
    PasswordResetConfirmView,
    PasswordResetView
)


router = DefaultRouter()
router.register(r'user', UserViewSet, 'user')
router.register(r'users', UserGeneralViewSet, 'users')

urlpatterns = [
    url(r'^api/v1/', include(router.urls)),
    url(r'^password/reset/$', PasswordResetView.as_view(),
        name='rest_password_reset'),
    url(r'^password/reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', PasswordResetConfirmView.as_view(),
        name='rest_password_reset_confirm'),
    url(r'^password/change/$', PasswordChangeView.as_view(),
        name='rest_password_change'),
]