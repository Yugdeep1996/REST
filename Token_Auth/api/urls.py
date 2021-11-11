from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

from .auth import CustomAuthToken
from .views import * 

# Create your urls here.

router = DefaultRouter()

router.register('studentapi', StudentModelViewSet, basename='student')

urlpatterns = [
    path('', include(router.urls)), 
    path('auth/', include('rest_framework.urls'), name='rest_framework'),
    path('gettoken/', CustomAuthToken.as_view()),
]

# using httpie.
# to send req at a link.
# http POST http://127.0.0.1:8000/api/gettoken/ username="user1" password="Admin@123"