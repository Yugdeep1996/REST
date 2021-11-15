from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('studentapi', StudentModelViewset, basename="student")

urlpatterns = [
    path('', include(router.urls)),
]